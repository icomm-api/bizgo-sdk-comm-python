"""``idempotencyTtl`` defaults to 86400 when ``idempotencyKey`` is set without a TTL (A309 otherwise)."""

from __future__ import annotations

import json
from typing import Any

import respx
from pydantic import Field

import bizgo
from bizgo import AsyncBizgo, Bizgo, SendOmniRequest, SmsMessage
from bizgo._base import RequestModel
from bizgo.models import _generated_request as req
from bizgo.resources._runtime import json_body

from .conftest import envelope

PATH = "/api/comm/v1/send/omni"
PHONE = "01000000000"


def accepted(count: int = 1) -> dict[str, Any]:
    return envelope({"destinations": [{"to": PHONE, "msgKey": f"K{i}", "code": "A000"} for i in range(count)]})


def sent(route: respx.Route) -> list[dict[str, Any]]:
    return [json.loads(call.request.content) for call in route.calls]


def test_constant_is_public() -> None:
    assert bizgo.DEFAULT_IDEMPOTENCY_TTL == 86400
    assert "DEFAULT_IDEMPOTENCY_TTL" in bizgo.__all__


def test_key_without_ttl_sends_default(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted())
    client.send.omni(to=PHONE, messages=[SmsMessage(from_=PHONE, text="x")], idempotency_key="k-1")
    client.send.sms(to=PHONE, from_=PHONE, text="x", idempotency_key="k-2")
    client.send.lms(to=PHONE, from_=PHONE, text="x", idempotency_key="k-3")
    client.send.mms(to=PHONE, from_=PHONE, text="x", file_keys=["FILE"], idempotency_key="k-4")
    bodies = sent(route)
    assert [b["idempotencyKey"] for b in bodies] == ["k-1", "k-2", "k-3", "k-4"]
    assert all(b["idempotencyTtl"] == 86400 for b in bodies)


def test_explicit_ttl_is_kept_including_zero(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted())
    for ttl in (0, 600, 86400):
        client.send.omni(
            to=PHONE, messages=[SmsMessage(from_=PHONE, text="x")], idempotency_key="k", idempotency_ttl=ttl
        )
    assert [b["idempotencyTtl"] for b in sent(route)] == [0, 600, 86400]


def test_no_key_no_ttl(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted())
    client.send.omni(to=PHONE, messages=[SmsMessage(from_=PHONE, text="x")])
    client.send.sms(to=PHONE, from_=PHONE, text="x")
    for body in sent(route):
        assert "idempotencyKey" not in body
        assert "idempotencyTtl" not in body


def test_prepared_request_model_and_dict_not_mutated(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted())
    model = SendOmniRequest.model_validate(
        {"destinations": [{"to": PHONE}], "messageFlow": [{"sms": {"from": PHONE, "text": "x"}}], "idempotencyKey": "k"}
    )
    raw: dict[str, Any] = {
        "destinations": [{"to": PHONE}],
        "messageFlow": [{"sms": {"from": PHONE, "text": "x"}}],
        "idempotencyKey": "k2",
    }
    snapshot = json.dumps(raw)
    client.send.request(model)
    client.send.request(raw)
    assert [b["idempotencyTtl"] for b in sent(route)] == [86400, 86400]
    assert model.idempotency_ttl is None
    assert "idempotency_ttl" not in model.model_fields_set
    assert json.dumps(raw) == snapshot


def test_bulk_chunks_get_default_ttl(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted(2))
    client.send.bulk(
        to=[PHONE] * 4,
        messages=[SmsMessage(from_=PHONE, text="x")],
        chunk_size=2,
        concurrency=1,
        idempotency_key_prefix="notice",
    )
    bodies = sent(route)
    assert len(bodies) == 2
    assert all(b["idempotencyKey"].startswith("notice-2-") and b["idempotencyTtl"] == 86400 for b in bodies)


def test_bulk_explicit_ttl_and_no_prefix(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted(2))
    messages = [SmsMessage(from_=PHONE, text="x")]
    client.send.bulk(to=[PHONE] * 2, messages=messages, idempotency_key_prefix="p", idempotency_ttl=0)
    client.send.bulk(to=[PHONE] * 2, messages=messages)
    first, second = sent(route)
    assert first["idempotencyTtl"] == 0
    assert "idempotencyKey" not in second and "idempotencyTtl" not in second


class _KeyedBody(RequestModel):
    name: str
    idempotency_key: str | None = Field(
        default=None, validation_alias="idempotencyKey", serialization_alias="idempotencyKey"
    )
    idempotency_ttl: int | None = Field(
        default=None, validation_alias="idempotencyTtl", serialization_alias="idempotencyTtl"
    )


class _KeyOnlyBody(RequestModel):
    idempotency_key: str | None = Field(
        default=None, validation_alias="idempotencyKey", serialization_alias="idempotencyKey"
    )


def test_generated_json_body_raw_dict_gets_default_without_mutation() -> None:
    raw: dict[str, Any] = {"name": "a", "idempotencyKey": "k"}
    assert json_body(_KeyedBody, raw) == {"name": "a", "idempotencyKey": "k", "idempotencyTtl": 86400}
    assert raw == {"name": "a", "idempotencyKey": "k"}
    model = _KeyedBody(name="a", idempotency_key="k")
    assert json_body(_KeyedBody, model)["idempotencyTtl"] == 86400
    assert model.idempotency_ttl is None
    assert json_body(_KeyedBody, {"name": "a", "idempotencyKey": "k", "idempotencyTtl": 0})["idempotencyTtl"] == 0
    assert json_body(_KeyedBody, {"name": "a"}) == {"name": "a"}
    # a schema without idempotencyTtl is never given one
    assert json_body(_KeyOnlyBody, {"idempotencyKey": "k"}) == {"idempotencyKey": "k"}


def test_every_spec_body_with_both_fields_gets_default() -> None:
    models = [
        cls
        for cls in vars(req).values()
        if isinstance(cls, type)
        and issubclass(cls, RequestModel)
        and {"idempotency_key", "idempotency_ttl"} <= set(cls.model_fields)
    ]
    assert SendOmniRequest in models
    body = {"destinations": [{"to": PHONE}], "messageFlow": [{"sms": {"from": PHONE, "text": "x"}}]}
    assert json_body(SendOmniRequest, {**body, "idempotencyKey": "k"})["idempotencyTtl"] == 86400


async def test_async_paths(aclient: AsyncBizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted())
    await aclient.send.omni(to=PHONE, messages=[SmsMessage(from_=PHONE, text="x")], idempotency_key="k-1")
    await aclient.send.sms(to=PHONE, from_=PHONE, text="x", idempotency_key="k-2")
    await aclient.send.omni(
        to=PHONE, messages=[SmsMessage(from_=PHONE, text="x")], idempotency_key="k-3", idempotency_ttl=0
    )
    await aclient.send.omni(to=PHONE, messages=[SmsMessage(from_=PHONE, text="x")])
    await aclient.send.bulk(
        to=[PHONE] * 2, messages=[SmsMessage(from_=PHONE, text="x")], idempotency_key_prefix="async"
    )
    bodies = sent(route)
    assert [b.get("idempotencyTtl") for b in bodies] == [86400, 86400, 0, None, 86400]
