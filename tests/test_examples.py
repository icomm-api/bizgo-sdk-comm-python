"""Run every example against a mock server so the examples never drift from the SDK."""

from __future__ import annotations

import hashlib
import hmac
import importlib
import json
import sys
import time
from pathlib import Path
from types import ModuleType

import httpx
import pytest
import respx

from bizgo import AsyncBizgo, Bizgo
from bizgo.webhooks import WebhookReceiver

from .conftest import envelope

sys.path.insert(0, str(Path(__file__).parents[1] / "examples"))

ACCEPTED = envelope({"destinations": [{"to": "01000000000", "msgKey": "K001", "code": "A000", "result": "Success"}]})


def load(name: str) -> ModuleType:
    return importlib.import_module(name)


def test_send_sms(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post("/api/comm/v1/send/omni").respond(json=ACCEPTED)
    load("send_sms").main(client, from_="01000000000", to="01000000000")
    assert route.called


def test_send_alimtalk_fallback(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post("/api/comm/v1/send/omni").respond(json=ACCEPTED)
    load("send_alimtalk_fallback").main(
        client,
        from_="01000000000",
        to="01000000000",
        sender_key="SENDER_KEY_EXAMPLE",
        template_code="TEMPLATE_CODE_EXAMPLE",
    )
    body = json.loads(route.calls.last.request.content)
    assert [next(iter(m)) for m in body["messageFlow"]] == ["alimtalk", "sms"] and body["idempotencyKey"]


def test_send_alimtalk_fallback_already_sent(
    client: Bizgo, api: respx.MockRouter, capsys: pytest.CaptureFixture[str]
) -> None:
    duplicate = envelope({"destinations": [{"to": "01000000000", "msgKey": "K001", "code": "A301", "result": "Dup"}]})
    api.post("/api/comm/v1/send/omni").respond(json=duplicate)
    load("send_alimtalk_fallback").main(
        client,
        from_="01000000000",
        to="01000000000",
        sender_key="SENDER_KEY_EXAMPLE",
        template_code="TEMPLATE_CODE_EXAMPLE",
    )
    assert "이미 발송된 주문입니다." in capsys.readouterr().out


def test_send_mms(client: Bizgo, api: respx.MockRouter) -> None:
    api.post("/api/comm/v1/file/mms").respond(json=envelope({"fileKey": "FILE_KEY_001"}))
    route = api.post("/api/comm/v1/send/omni").respond(json=ACCEPTED)
    load("send_mms").main(client, from_="01000000000", to="01000000000", image=b"\xff\xd8jpeg")
    assert json.loads(route.calls.last.request.content)["messageFlow"][0]["mms"]["fileKey"] == ["FILE_KEY_001"]


def test_poll_reports(client: Bizgo, api: respx.MockRouter) -> None:
    api.get("/api/comm/v1/report/polling").mock(
        side_effect=[
            httpx.Response(
                200, json=envelope({"reportId": "R1", "report": [{"msgKey": "K001", "reportCode": "10000"}]})
            ),
            httpx.Response(200, json=envelope({"reportId": "", "report": None})),
        ]
    )
    api.delete("/api/comm/v1/report/polling/R1").respond(json=envelope())
    module = load("poll_reports")
    module.main(client)
    assert module.store == {"K001": "delivered"}


def test_message_history(client: Bizgo, api: respx.MockRouter) -> None:
    api.get("/api/comm/v1/message/history").respond(
        json=envelope({"messages": [{"msgKey": "K001", "reportCode": "63020"}], "hasNext": False})
    )
    status = api.get("/api/comm/v1/message/inquiry/msgKey/K001").respond(
        json=envelope({"messages": [{"msgKey": "K001", "serviceType": "ALIMTALK", "reportCode": "63020"}]})
    )
    load("message_history").main(client)
    assert status.called


def test_webhook_server() -> None:
    module = load("webhook_server")
    receiver = WebhookReceiver("test-webhook-secret")
    timestamp = str(int(time.time() * 1000))
    signature = hmac.new(b"test-webhook-secret", timestamp.encode(), hashlib.sha256).hexdigest()
    body = json.dumps(
        {"msgKey": "K001", "serviceType": "SMS", "reportTime": "t", "reportType": "0", "reportCode": "10000"}
    ).encode()
    headers = {"X-IB-Timestamp": timestamp, "X-IB-Signature": signature}
    assert module.handle(receiver, headers, body) == (200, {"msgKey": "K001"})
    assert module.handle(receiver, {**headers, "X-IB-Signature": "0" * 64}, body) == (401, {})


async def test_async_send(aclient: AsyncBizgo, api: respx.MockRouter) -> None:
    route = api.post("/api/comm/v1/send/omni").respond(json=ACCEPTED)
    await load("async_send").main(aclient, from_="01000000000", groups=[["01000000000"], ["01000000001"]])
    assert route.call_count == 2
