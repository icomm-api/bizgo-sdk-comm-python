"""Consistency with the vendored OpenAPI spec, and the async client."""

from __future__ import annotations

import json
import pathlib
from typing import Any

import httpx
import pytest
import respx
import yaml

from bizgo import AsyncBizgo, SendOmniRequest, SmsMessage, models

from .conftest import envelope

SPEC = yaml.safe_load((pathlib.Path(__file__).parents[1] / "spec" / "openapi.yaml").read_text(encoding="utf-8"))
SEND = SPEC["paths"]["/api/comm/v1/send/omni"]["post"]
EXAMPLES = SEND["requestBody"]["content"]["application/json"]["examples"]


@pytest.mark.parametrize("name", sorted(EXAMPLES))
def test_spec_request_examples_validate_and_round_trip(name: str) -> None:
    value = EXAMPLES[name]["value"]
    assert SendOmniRequest.model_validate(value).to_api() == value


def test_spec_response_example_parses() -> None:
    example = SEND["responses"]["200"]["content"]["application/json"]["example"]
    response = models.SendOmniResponse.model_validate(example)
    assert response.data and response.data.data and response.data.data.destinations


def test_every_operation_is_covered() -> None:
    """Every spec operation has an SDK method (generated or hand-written); see test_all_operations.py."""
    from bizgo._operations import OPERATIONS

    operation_ids = {
        op["operationId"] for item in SPEC["paths"].values() for key, op in item.items() if key != "parameters"
    }
    assert len(operation_ids) == 146
    assert operation_ids == set(OPERATIONS), "run python scripts/generate_models.py after copying the spec"
    handwritten = {op_id for op_id, op in OPERATIONS.items() if op.handwritten}
    assert handwritten == {
        "sendOmni",
        "uploadMmsFile",
        "uploadRcsFile",
        "getReportPolling",
        "ackReportPolling",
        "getReportInquiry",
        "getMessageStatistics",
        "getMessageHistory",
        "getMessageStatusByMsgKey",
        "getMessageStatusByRequestId",
        "getMoHistory",
        "getMoByMsgKey",
    }


async def test_async_send_and_iterate(aclient: AsyncBizgo, api: respx.MockRouter) -> None:
    route = api.post("/api/comm/v1/send/omni").respond(
        json=envelope({"destinations": [{"to": "01000000000", "msgKey": "K", "code": "A000"}]})
    )
    result = await aclient.send.omni(to="01000000000", messages=[SmsMessage(from_="01000000000", text="x")])
    assert result.msg_keys == ["K"]
    assert json.loads(route.calls.last.request.content)["messageFlow"] == [
        {"sms": {"from": "01000000000", "text": "x"}}
    ]
    api.get("/api/comm/v1/message/history/mo").mock(
        side_effect=[
            httpx.Response(200, json=envelope({"messages": [{"msgKey": "M1"}], "lastSeq": 1, "hasNext": True})),
            httpx.Response(200, json=envelope({"messages": [{"msgKey": "M2"}], "lastSeq": 2, "hasNext": False})),
        ]
    )
    keys: list[Any] = [m.msg_key async for m in aclient.messages.iter_mo_history("2026-04-23T14:11:01+09:00")]
    assert keys == ["M1", "M2"]


async def test_async_consume(aclient: AsyncBizgo, api: respx.MockRouter) -> None:
    api.get("/api/comm/v1/report/polling").mock(
        side_effect=[
            httpx.Response(200, json=envelope({"reportId": "R1", "report": [{"msgKey": "K"}]})),
            httpx.Response(200, json=envelope({"reportId": "", "report": None})),
        ]
    )
    ack = api.delete("/api/comm/v1/report/polling/R1").respond(json=envelope())
    got: list[str | None] = []

    async def handler(reports: list[models.Report]) -> None:
        got.extend(r.msg_key for r in reports)

    assert await aclient.reports.consume(handler) == 1
    assert got == ["K"] and ack.called
