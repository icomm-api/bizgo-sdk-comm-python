"""bizgo.testing, hooks / OpenTelemetry (no sensitive data) and counsel webhooks (SDK-DESIGN.md §11.3-11.5)."""

from __future__ import annotations

import json
import logging
import pathlib
import re
from typing import Any

import pytest
import yaml

import bizgo.webhooks
from bizgo import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    Bizgo,
    Hooks,
    NotFoundError,
    RateLimitError,
    RequestEvent,
    SmsMessage,
)
from bizgo._transport import Retry
from bizgo.testing import FAKE_API_KEY, FakeTransport, RecordedFile, sign_webhook
from bizgo.webhooks import (
    MAX_BODY_BYTES,
    WEBHOOKS,
    WebhookPayloadError,
    WebhookReceiver,
    WebhookVerificationError,
    counsel_ack,
    parse,
    parse_counsel_message,
)

PHONE = "01000001234"
SECRET = "test-webhook-secret"
NOW_MS = 1743381600000
REPORT = {"msgKey": "KEY001", "serviceType": "SMS", "reportTime": "t", "reportType": "0", "reportCode": "10000"}
SPEC = yaml.safe_load((pathlib.Path(__file__).parents[1] / "spec" / "openapi.yaml").read_text(encoding="utf-8"))
EXAMPLES = {
    name: item["post"]["requestBody"]["content"]["application/json"].get("example")
    for name, item in SPEC["webhooks"].items()
}


# ---------------------------------------------------------------- bizgo.testing


def test_fake_records_requests_without_header_values() -> None:
    fake = FakeTransport()
    with fake.client() as client:
        result = client.send.sms(to=[PHONE, "01000000000"], from_="01000000000", text="hello", ref="order-1")
    assert result.msg_keys == ["FAKE-MSGKEY-000001", "FAKE-MSGKEY-000002"] and result.ref == "order-1"
    request = fake.last_request
    assert (request.operation_id, request.operation, request.method) == ("sendOmni", "send.omni", "POST")
    assert request.path_template == "/api/comm/v1/send/omni"
    assert request.json["destinations"][0] == {"to": PHONE}
    assert "authorization" in request.header_names
    assert FAKE_API_KEY not in repr(request) and FAKE_API_KEY not in json.dumps(request.json)
    assert PHONE not in repr(request) and repr(fake) == "FakeTransport(requests=1)"


def test_fake_default_reservation_includes_resv_key() -> None:
    fake = FakeTransport()
    with fake.client() as client:
        created = client.reservations.create(
            {
                "destinations": [{"to": "01000000000"}, {"to": PHONE}],
                "messageFlow": [{"sms": {"from": "01000000000", "text": "x"}}],
                "resvSendTime": "2026-05-01 10:00:00",
            }
        )
    assert created is not None and created.resv_key == "FAKE-RESVKEY-000001"
    assert created.data is not None and len(created.data.destinations or []) == 2


def test_fake_error_injection() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").fail("service", 200, "A020", retry_after=0).send_result("A000", "A306")
    fake.on("GET", "/api/comm/v1/message/statistics").fail("gateway", 401, "A401")
    fake.on("getReportPolling").network_error()
    fake.on("getReportInquiry").timeout()
    with fake.client(max_retries=0) as client:
        with pytest.raises(RateLimitError):
            client.send.sms(to="01000000000", from_="01000000000", text="x")
        result = client.send.sms(to=["01000000000", PHONE], from_="01000000000", text="x")
        assert [d.code for d in result.failed] == ["A306"]
        with pytest.raises(AuthenticationError):
            client.messages.statistics("20260101")
        with pytest.raises(APIConnectionError):
            client.reports.poll()
        with pytest.raises(APITimeoutError):
            client.reports.inquiry("KEY")
    assert len(fake.requests_for("sendOmni")) == 2


def test_fake_stub_by_data_and_queue_order() -> None:
    fake = FakeTransport()
    fake.on("getReportInquiry").data({"report": [{"msgKey": "K1"}]}).data({"report": []})
    with fake.client() as client:
        assert [r.msg_key for r in client.reports.inquiry("K1")] == ["K1"]
        assert client.reports.inquiry("K1") == []
        assert client.reports.inquiry("K1") == []  # the last stub repeats
    with pytest.raises(KeyError):
        fake.on("noSuchOperation")
    fake.reset()
    assert fake.requests == []


def test_fake_records_multipart_names_and_sizes_only() -> None:
    fake = FakeTransport()
    with fake.client() as client:
        client.counsel.files.upload(b"\x00" * 10, sender_key="SENDER_KEY_EXAMPLE", filename="a.pdf")
    form = fake.last_request.form
    assert form is not None
    assert form["senderKey"] == "SENDER_KEY_EXAMPLE"
    assert form["file"] == RecordedFile(filename="a.pdf", content_type="application/pdf", size=10)


def test_unknown_path_answers_404() -> None:
    fake = FakeTransport()
    with fake.client() as client, pytest.raises(NotFoundError):
        client._transport.request("GET", "/nope", retry=Retry.SAFE, operation="getReportPolling")
    assert fake.last_request.operation_id is None


async def test_fake_async_client() -> None:
    fake = FakeTransport()
    async with fake.async_client() as client:
        result = await client.send.sms(to="01000000000", from_="01000000000", text="x")
    assert result.msg_keys == ["FAKE-MSGKEY-000001"]


def test_sign_webhook_round_trip(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("bizgo.webhooks.time.time", lambda: NOW_MS / 1000)
    receiver = WebhookReceiver(SECRET)
    for encoding in ("hex", "base64"):
        headers, body = sign_webhook(SECRET, REPORT, timestamp=NOW_MS, encoding=encoding)  # type: ignore[arg-type]
        assert receiver.report(headers, body).msg_key == "KEY001"
    headers, body = sign_webhook("other-secret", REPORT, timestamp=NOW_MS)
    with pytest.raises(WebhookVerificationError):
        receiver.report(headers, body)


# ---------------------------------------------------------------- hooks


class Recorder(Hooks):
    def __init__(self) -> None:
        self.started: list[RequestEvent] = []
        self.ended: list[RequestEvent] = []

    def on_request_start(self, event: RequestEvent) -> None:
        self.started.append(event)

    def on_request_end(self, event: RequestEvent) -> None:
        self.ended.append(event)


class Broken(Hooks):
    def on_request_start(self, event: RequestEvent) -> None:
        raise RuntimeError("boom")

    def on_request_end(self, event: RequestEvent) -> None:
        raise RuntimeError("boom")


def _event_text(event: RequestEvent) -> str:
    return repr(event) + json.dumps({k: str(v) for k, v in vars(event).items()})


def test_hooks_get_operation_template_status_and_no_sensitive_data() -> None:
    fake = FakeTransport()
    recorder = Recorder()
    fake.on("getMoHistory").respond(503, {}, {"retry-after": "0"}).fail("service", 200, "A306")
    with fake.client(hooks=[recorder, Broken()]) as client:
        with pytest.raises(BadRequestError):
            client.messages.mo_history("2026-04-23T14:11:01+09:00", from_=PHONE)
        client.reports.inquiry(PHONE)
        client.send.sms(to=PHONE, from_="01000000000", text="secret text")
    assert len(recorder.started) == len(recorder.ended) == 3
    assert recorder.started[0] is recorder.ended[0]  # the same object at start and end
    failed, inquiry, sent = recorder.ended
    assert (failed.operation_id, failed.operation, failed.method) == ("getMoHistory", "messages.moHistory", "GET")
    assert failed.path_template == "/api/comm/v1/message/history/mo"
    assert (failed.status, failed.layer, failed.code, failed.error_type) == (200, "service", "A306", "BadRequestError")
    assert failed.attempts == 2 and failed.success is False and failed.duration_ms is not None
    assert inquiry.path_template == "/api/comm/v1/report/inquiry/{msgKey}" and inquiry.success
    assert sent.operation == "send.omni" and sent.status == 200 and sent.attempts == 1
    for event in recorder.ended:
        text = _event_text(event)
        assert PHONE not in text and FAKE_API_KEY not in text and "secret text" not in text
        assert "2026-04-23" not in text  # no query values


def test_invalid_hooks_are_rejected() -> None:
    with pytest.raises(TypeError):
        Bizgo(FAKE_API_KEY, hooks=[object()])  # type: ignore[list-item]


def test_opentelemetry_spans() -> None:
    pytest.importorskip("opentelemetry.sdk")
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

    from bizgo.otel import OpenTelemetryHooks

    exporter = InMemorySpanExporter()
    provider = TracerProvider()
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    fake = FakeTransport()
    fake.on("getReportInquiry").fail("gateway", 401, "A401")
    with fake.client(hooks=OpenTelemetryHooks(provider.get_tracer("test"))) as client:
        client.send.sms(to=PHONE, from_="01000000000", text="x")
        with pytest.raises(AuthenticationError):
            client.reports.inquiry(PHONE)
    ok, failed = exporter.get_finished_spans()
    assert ok.name == "bizgo send.omni"
    assert ok.attributes is not None and failed.attributes is not None
    assert ok.attributes["url.template"] == "/api/comm/v1/send/omni"
    assert ok.attributes["http.request.method"] == "POST" and ok.attributes["bizgo.retry_count"] == 0
    assert failed.name == "bizgo reports.inquiry"
    assert failed.attributes["bizgo.code"] == "A401" and failed.attributes["bizgo.layer"] == "gateway"
    assert failed.attributes["http.response.status_code"] == 401
    for span in (ok, failed):
        text = json.dumps(dict(span.attributes or {})) + span.name + str(span.status.description)
        assert PHONE not in text and FAKE_API_KEY not in text


def test_header_params_are_sent_but_never_logged(caplog: pytest.LogCaptureFixture) -> None:
    fake = FakeTransport()
    with fake.client() as client, caplog.at_level(logging.DEBUG, logger="bizgo"):
        client.kakao.senders.create(
            {"categoryCode": "00000000001", "yellowId": "@KAKAO_CHANNEL_ID_EXAMPLE"},
            token="KAKAO_AUTH_TOKEN_EXAMPLE",
            phone_number=PHONE,
        )
    assert "POST /api/comm/v1/account/kakao/sender -> 200" in caplog.text
    assert PHONE not in caplog.text and "KAKAO_AUTH_TOKEN_EXAMPLE" not in caplog.text
    assert {"token", "phonenumber"} <= set(fake.last_request.header_names)


# ---------------------------------------------------------------- counsel webhooks

COUNSEL_BODY = EXAMPLES["counselMessage"]


def _example(method: str) -> Any:
    name = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), method)
    return EXAMPLES[name]


def _signed(payload: Any = COUNSEL_BODY) -> tuple[dict[str, str], bytes]:
    headers, body = sign_webhook(SECRET, payload, timestamp=NOW_MS)
    return headers, body


@pytest.fixture
def now(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("bizgo.webhooks.time.time", lambda: NOW_MS / 1000)


COUNSEL_METHODS = [
    "counsel_message",
    "counsel_reference",
    "counsel_expired_session",
    "counsel_seen_info",
    "counsel_personal_info",
    "counsel_cert_result",
    "counsel_result",
]


def test_every_spec_webhook_has_a_receiver_method() -> None:
    for name in WEBHOOKS:
        method = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", name).lower()
        assert callable(getattr(WebhookReceiver, method)), name
    assert WEBHOOKS["report"][1] is True
    assert WEBHOOKS["mo"][1] is True
    assert all(WEBHOOKS[n][1] is False for n in WEBHOOKS if n.startswith("counsel"))


@pytest.mark.parametrize("method", COUNSEL_METHODS)
def test_counsel_parses_without_signature_headers(method: str) -> None:
    body = json.dumps(_example(method))
    payload = getattr(WebhookReceiver(SECRET), method)({"Content-Type": "application/json"}, body)
    assert payload.model_dump(by_alias=True, exclude_unset=True) == _example(method)


@pytest.mark.parametrize("method", COUNSEL_METHODS)
def test_counsel_ignores_signature_headers(method: str) -> None:
    body = json.dumps(_example(method))
    receiver = WebhookReceiver(SECRET)
    for headers in (
        {"X-IB-Timestamp": "1", "X-IB-Signature": "00" * 32},
        {"X-IB-Signature": "bogus"},
        {"X-IB-Timestamp": "not-a-number"},
        _signed(_example(method))[0],
    ):
        payload = getattr(receiver, method)(headers, body)
        assert payload.model_dump(by_alias=True, exclude_unset=True) == _example(method)


@pytest.mark.parametrize("method", COUNSEL_METHODS)
def test_counsel_without_secret_via_module_parsers(method: str) -> None:
    parser = getattr(bizgo.webhooks, "parse_" + method)
    body = json.dumps(_example(method))
    assert parser(body).model_dump(by_alias=True, exclude_unset=True) == _example(method)
    name = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), method)
    assert type(parse(name, body)) is type(parser(body))


@pytest.mark.parametrize(
    "body",
    [b" " * (MAX_BODY_BYTES + 1), b'{"a":' * 65 + b"1" + b"}" * 65, b"[]", b"not json", b'{"msgKey": 1}'],
    ids=["too-large", "depth-65", "array", "not-json", "wrong-type"],
)
def test_counsel_input_defenses_still_apply(body: bytes) -> None:
    with pytest.raises(WebhookPayloadError):
        WebhookReceiver(SECRET).counsel_message({}, body)
    with pytest.raises(WebhookPayloadError):
        parse_counsel_message(body)


def test_report_and_mo_always_need_a_signature(now: None) -> None:
    receiver = WebhookReceiver(SECRET)
    headers, body = sign_webhook(SECRET, REPORT, timestamp=NOW_MS)
    assert receiver.report(headers, body).msg_key == REPORT["msgKey"]
    for bad in ({}, {"X-IB-Timestamp": str(NOW_MS)}, dict(headers, **{"X-IB-Signature": "00" * 32})):
        with pytest.raises(WebhookVerificationError):
            receiver.report(bad, body)
        with pytest.raises(WebhookVerificationError):
            receiver.mo(bad, b'{"msgKey": "K"}')


def test_counsel_ack_and_parse() -> None:
    assert counsel_ack() == WebhookReceiver.counsel_ack() == {"code": "A000", "result": "Success"}
    assert WebhookReceiver.ack("K") == {"msgKey": "K"}
    assert parse_counsel_message(COUNSEL_BODY).msg_key == COUNSEL_BODY["msgKey"]
    result = EXAMPLES["counselResult"]
    assert parse("counselResult", json.dumps(result)).model_dump(by_alias=True, exclude_unset=True) == result
    with pytest.raises(ValueError):
        parse("unknown", b"{}")
    with pytest.raises(WebhookVerificationError, match="JSON"):
        parse_counsel_message(b"not json")
    assert SECRET not in repr(WebhookReceiver(SECRET))


def test_sms_message_placeholder_only() -> None:
    assert SmsMessage(from_="01000000000", text="x").to_api() == {"from": "01000000000", "text": "x"}
