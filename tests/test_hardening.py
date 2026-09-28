"""Regression tests for the security/usability review (SDK-DESIGN.md §12). One section per rule."""

from __future__ import annotations

import gzip
import json
import math
import pickle
import time
from collections.abc import Iterator
from typing import Any

import httpx
import pytest

import bizgo
from bizgo import (
    Bizgo,
    ConfigurationError,
    DuplicateRequestError,
    InvalidResponseError,
    RateLimitError,
    SmsMessage,
    WebhookPayloadError,
    WebhookVerificationError,
)
from bizgo._config import ClientConfig
from bizgo._ratelimit import TokenBucket
from bizgo._transport import MAX_RESPONSE_BYTES, _retry_after
from bizgo.models import MoMessage, SendDestinationResult
from bizgo.models._results import SendResult
from bizgo.resources.send import bulk_idempotency_key
from bizgo.testing import FAKE_API_KEY, FakeTransport, sign_webhook, success_envelope
from bizgo.webhooks import WebhookReceiver, verify_signature

PHONE = "01000001234"
MESSAGE = [SmsMessage(from_="01000000000", text="x")]
SECRET = "test-webhook-secret"


def mock_client(handler: Any, **options: Any) -> Bizgo:
    http = httpx.Client(transport=httpx.MockTransport(handler), **options.pop("http_options", {}))
    return Bizgo(FAKE_API_KEY, http_client=http, rate_limit=None, max_retries=0, **options)


# ---------------------------------------------------------------- 1. parse failures are SDK errors


def test_rule1_minimal_envelope_without_auth_result_parses() -> None:
    fake = FakeTransport()
    body = {
        "common": {"authCode": "A000"},
        "data": {"code": "A000", "data": {"destinations": [{"msgKey": "K1", "code": "A000"}]}},
    }
    fake.on("sendOmni").respond(200, body)
    with fake.client() as client:
        assert client.send.sms(to=PHONE, from_="01000000000", text="x").msg_keys == ["K1"]


def test_rule1_wrong_field_types_raise_invalid_response_error_with_send_note() -> None:
    fake = FakeTransport()
    bad = success_envelope({"destinations": "not-a-list"})
    fake.on("sendOmni").respond(200, bad)
    with fake.client() as client, pytest.raises(InvalidResponseError) as info:
        client.send.sms(to=PHONE, from_="01000000000", text="x")
    error = info.value
    assert isinstance(error, bizgo.BizgoError)
    assert error.http_status == 200 and error.tracking_id == "FAKE-TR-ID" and error.body == bad
    assert "접수됐을 수 있으니" in str(error) and PHONE not in str(error)
    assert error.__cause__ is None


def test_rule1_generated_operation_parse_error_is_wrapped() -> None:
    fake = FakeTransport()
    fake.on("listAlimtalkTemplates").data({"alimtalk": {"templates": "oops"}})
    with fake.client() as client, pytest.raises(InvalidResponseError) as info:
        client.alimtalk.templates.list(sender_key="SENDER_KEY_EXAMPLE")
    assert "접수" not in str(info.value)  # a read: no "may have been accepted" note


def test_rule1_non_envelope_json_is_invalid_response() -> None:
    fake = FakeTransport()
    fake.on("getReportInquiry").respond(200, {"hello": 1})
    with fake.client() as client, pytest.raises(InvalidResponseError):
        client.reports.inquiry("K")


# ---------------------------------------------------------------- 2. bulk catches every chunk failure


def test_rule2_bulk_keeps_going_after_an_unparseable_chunk() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").default().respond(200, success_envelope({"destinations": 5})).default()
    with fake.client() as client:
        result = client.send.bulk(to=[PHONE] * 5, messages=MESSAGE, chunk_size=2, concurrency=1)
    assert [r is None for r in result.results] == [False, True, False]
    assert isinstance(result.errors[0].error, InvalidResponseError)
    assert len(result.msg_keys) == 3  # results of chunks 0 and 2 are kept


def test_rule2_bulk_still_raises_configuration_errors() -> None:
    fake = FakeTransport()
    with fake.client() as client:
        client.send._transport.request = _raise_config  # type: ignore[method-assign]
        with pytest.raises(ConfigurationError):
            client.send.bulk(to=[PHONE] * 3, messages=MESSAGE, chunk_size=2)


def _raise_config(*_args: Any, **_kwargs: Any) -> Any:
    raise ConfigurationError("bad config")


# ---------------------------------------------------------------- 3. bulk idempotency keys


def test_rule3_key_format_is_reproducible_and_never_reused() -> None:
    numbers = [f"0100000{i:04d}" for i in range(400)]
    fake = FakeTransport()
    with fake.client() as client:
        client.send.bulk(to=numbers, messages=MESSAGE, idempotency_key_prefix="notice", chunk_size=200)
        first = {r.json["idempotencyKey"]: [d["to"] for d in r.json["destinations"]] for r in fake.requests}
        fake.reset()
        client.send.bulk(to=numbers, messages=MESSAGE, idempotency_key_prefix="notice", chunk_size=200)
        again = {r.json["idempotencyKey"]: [d["to"] for d in r.json["destinations"]] for r in fake.requests}
        fake.reset()
        client.send.bulk(to=numbers, messages=MESSAGE, idempotency_key_prefix="notice", chunk_size=100)
        other = {r.json["idempotencyKey"]: [d["to"] for d in r.json["destinations"]] for r in fake.requests}
    assert first == again  # same list + same chunk_size -> same keys (duplicates rejected by the server)
    assert not set(first) & set(other)  # a key is never reused for another group of recipients
    key = next(iter(first))
    assert key == bulk_idempotency_key("notice", 200, 0, numbers[:200])
    assert key.startswith("notice-200-0-") and len(key.rsplit("-", 1)[1]) == 8
    changed = [*numbers[:199], "01000000000", *numbers[200:]]
    assert bulk_idempotency_key("notice", 200, 0, changed[:200]) != key


def test_rule3_key_length_is_checked_before_sending() -> None:
    fake = FakeTransport()
    with fake.client() as client, pytest.raises(ValueError, match="200"):
        client.send.bulk(to=[PHONE], messages=MESSAGE, idempotency_key_prefix="p" * 190)
    assert fake.requests == []


# ---------------------------------------------------------------- 4. A301 after any retry


@pytest.mark.parametrize("first", ["503", "429", "timeout"])
def test_rule4_a301_after_retry_is_marked_already_accepted(first: str) -> None:
    fake = FakeTransport()
    stub = fake.on("sendOmni")
    if first == "timeout":
        stub.timeout()
    else:
        stub.fail("gateway", int(first), "A503" if first == "503" else "A020", retry_after=0)
    stub.fail("service", 200, "A301")
    with fake.client() as client, pytest.raises(DuplicateRequestError) as info:
        client.send.sms(to=PHONE, from_="01000000000", text="x", idempotency_key="order-1")
    assert info.value.already_accepted is True
    assert "이전 시도가 이미 접수" in str(info.value)


def test_rule4_a301_on_first_attempt_is_not_already_accepted() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").fail("service", 200, "A301")
    with fake.client() as client, pytest.raises(DuplicateRequestError) as info:
        client.send.sms(to=PHONE, from_="01000000000", text="x", idempotency_key="order-1")
    assert info.value.already_accepted is False


# ---------------------------------------------------------------- 5. path values


@pytest.mark.parametrize("value", [".", ".."])
def test_rule5_dot_segments_are_rejected_before_sending(value: str) -> None:
    fake = FakeTransport()
    with fake.client() as client:
        with pytest.raises(ValueError):
            client.reports.ack(value)
        with pytest.raises(ValueError):
            client.rcs.chatbots.delete("BRAND_ID_EXAMPLE", value)
        with pytest.raises(ValueError):
            client.reservations.recipients.list(value)
    assert fake.requests == []


def test_rule5_other_values_are_one_encoded_segment() -> None:
    fake = FakeTransport()
    with fake.client() as client:
        client.reports.inquiry("a/b?c#d%e...")
    assert fake.last_request.path == "/api/comm/v1/report/inquiry/a%2Fb%3Fc%23d%25e..."


def test_rule5_header_values_must_be_printable_ascii() -> None:
    fake = FakeTransport()
    body = {"categoryCode": "00000000001", "yellowId": "@KAKAO_CHANNEL_ID_EXAMPLE"}
    with fake.client() as client:
        for token in ("1\r\nX-Evil: 1", "토큰", "a\x00b"):
            with pytest.raises(ValueError):
                client.kakao.senders.create(body, token=token, phone_number="01000000000")
    assert fake.requests == []


# ---------------------------------------------------------------- 6. the API key cannot be taken over


def test_rule6_http_client_auth_and_headers_cannot_replace_the_key() -> None:
    seen: list[str | None] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("authorization"))
        return httpx.Response(200, json=success_envelope({"report": []}))

    for options in ({"auth": ("user", "pw")}, {"headers": {"Authorization": "other"}}):
        with mock_client(handler, http_options=options) as client:
            client.reports.inquiry("K")
    assert seen == [FAKE_API_KEY, FAKE_API_KEY]


def test_rule6_redirects_are_not_followed_and_status_is_in_the_message() -> None:
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return httpx.Response(302, headers={"Location": "https://evil.example/steal"})

    with (
        mock_client(handler, http_options={"follow_redirects": True}) as client,
        pytest.raises(InvalidResponseError) as info,
    ):
        client.reports.inquiry("K")
    assert len(seen) == 1 and "evil" not in seen[0]
    assert info.value.http_status == 302 and "302" in str(info.value)


@pytest.mark.parametrize(
    "url",
    [
        "https://user:pw@mars.ibapi.kr",
        "https://evil.example@mars.ibapi.kr",
        "http://localhost@evil.com",
        "https://mars.ibapi.kr?x=1",
        "https://mars.ibapi.kr#frag",
        "https://mars.ibapi.kr:notaport",
    ],
)
def test_rule6_base_url_userinfo_query_fragment_are_rejected(url: str) -> None:
    with pytest.raises(ConfigurationError):
        Bizgo(FAKE_API_KEY, base_url=url)


# ---------------------------------------------------------------- 7. webhook input


@pytest.mark.parametrize(
    "timestamp",
    ["١٧٠٠٠٠٠٠٠٠", "²", "9" * 17, "9" * 5000, "", "-1", "1.5"],
    ids=["arabic-digits", "superscript", "17-digits", "5000-digits", "empty", "negative", "decimal"],
)
def test_rule7_timestamp_must_be_ascii_digits(timestamp: str) -> None:
    with pytest.raises(WebhookVerificationError):
        WebhookReceiver(SECRET).report({"X-IB-Timestamp": timestamp, "X-IB-Signature": "00"}, b"{}")


@pytest.mark.parametrize(
    "body",
    [b"[" * 100000 + b"]" * 100000, b'{"a":' * 40 + b"1" + b"}" * 40, b"[]", b"not json", b'{"a":"\xff"}', b"{}"],
    ids=["very-deep", "deep", "array", "not-json", "bad-utf8", "missing-fields"],
)
def test_rule7_bad_bodies_raise_payload_error(body: bytes) -> None:
    headers, _ = sign_webhook(SECRET, {})
    with pytest.raises(WebhookPayloadError):
        WebhookReceiver(SECRET).report(headers, body)
    with pytest.raises(WebhookPayloadError):  # counsel webhooks are not signed; the body checks still apply
        WebhookReceiver(SECRET).counsel_message({}, body)


@pytest.mark.parametrize("secret", ["", "   ", b"", b" \t"])
def test_rule7_blank_secrets_are_rejected(secret: Any) -> None:
    with pytest.raises(ValueError):
        WebhookReceiver(secret)
    with pytest.raises(WebhookVerificationError):
        verify_signature(secret=secret, timestamp="1", signature="00")


@pytest.mark.parametrize("tolerance", [0, -5, math.inf, math.nan, True, "300"])
def test_rule7_tolerance_must_be_positive_and_finite(tolerance: Any) -> None:
    with pytest.raises(ValueError):
        WebhookReceiver(SECRET, tolerance=tolerance)


def test_rule7_tolerance_none_disables_the_check_explicitly() -> None:
    headers, body = sign_webhook(SECRET, {"msgKey": "K"}, timestamp=1)
    WebhookReceiver(SECRET, tolerance=None).verify(headers)
    assert body


# ---------------------------------------------------------------- 8. response size and depth


class _Chunks(httpx.SyncByteStream):
    def __init__(self, chunks: list[bytes]) -> None:
        self._chunks = chunks

    def __iter__(self) -> Iterator[bytes]:
        yield from self._chunks


def test_rule8_gzip_bomb_is_cut_off_after_decompression() -> None:
    bomb = gzip.compress(b" " * (MAX_RESPONSE_BYTES * 4), 9)
    chunks = [bomb[i : i + 65536] for i in range(0, len(bomb), 65536)]

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"Content-Encoding": "gzip"}, stream=_Chunks(chunks))

    started = time.monotonic()
    with mock_client(handler) as client, pytest.raises(InvalidResponseError, match="16MB"):
        client.reports.inquiry("K")
    assert time.monotonic() - started < 10


def test_rule8_gzip_response_within_limit_is_decoded() -> None:
    payload = gzip.compress(json.dumps(success_envelope({"report": [{"msgKey": "K1"}]})).encode())

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["accept-encoding"] == "gzip, deflate"
        return httpx.Response(200, headers={"Content-Encoding": "gzip"}, stream=_Chunks([payload]))

    with mock_client(handler) as client:
        assert [r.msg_key for r in client.reports.inquiry("K")] == ["K1"]


@pytest.mark.parametrize(
    "body", [b"[" * 200000 + b"]" * 200000, b'{"a":' * 70 + b"1" + b"}" * 70], ids=["huge", "depth-70"]
)
def test_rule8_deep_json_is_rejected(body: bytes) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=body)

    with mock_client(handler) as client, pytest.raises(InvalidResponseError, match="중첩"):
        client.reports.inquiry("K")


def test_rule8_unsupported_encoding_is_rejected() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"Content-Encoding": "br"}, stream=_Chunks([b"xx"]))

    with mock_client(handler) as client, pytest.raises(InvalidResponseError):
        client.reports.inquiry("K")


# ---------------------------------------------------------------- 9. Retry-After


@pytest.mark.parametrize(
    ("value", "expected"), [("nan", None), ("inf", None), ("-1", None), ("abc", None), ("2", 2.0), ("999", 60.0)]
)
def test_rule9_retry_after_parsing(value: str, expected: float | None) -> None:
    assert _retry_after(httpx.Headers({"retry-after": value})) == expected


def test_rule9_nan_retry_after_does_not_crash(_no_sleep: list[float]) -> None:
    fake = FakeTransport()
    fake.on("getReportInquiry").respond(
        429, {"common": {"authCode": "A020", "authResult": "x"}}, {"Retry-After": "nan"}
    )
    with fake.client() as client, pytest.raises(RateLimitError) as info:
        client.reports.inquiry("K")
    assert info.value.retry_after is None
    assert all(math.isfinite(d) for d in _no_sleep)


# ---------------------------------------------------------------- 10. pickling


def test_rule10_errors_round_trip_through_pickle() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").fail("gateway", 401, "A401")
    with fake.client() as client, pytest.raises(bizgo.AuthenticationError) as info:
        client.send.sms(to=PHONE, from_="01000000000", text="x")
    errors: list[bizgo.BizgoError] = [
        info.value,
        RateLimitError("x", http_status=429, code="A020", layer="service", retry_after=3.0),
        InvalidResponseError("bad", http_status=200, tracking_id="T", body={"a": 1}),
        WebhookPayloadError("bad body"),
    ]
    dup = DuplicateRequestError("dup", http_status=200, code="A301", layer="service")
    dup.already_accepted = True
    errors.append(dup)
    for error in errors:
        copy = pickle.loads(pickle.dumps(error))  # noqa: S301 - our own objects
        assert type(copy) is type(error) and str(copy) == str(error) and vars(copy) == vars(error)
    assert pickle.loads(pickle.dumps(dup)).already_accepted is True  # noqa: S301


def test_rule10_client_config_with_the_key_cannot_be_pickled() -> None:
    config = Bizgo(FAKE_API_KEY)._config
    assert isinstance(config, ClientConfig)
    with pytest.raises(TypeError):
        pickle.dumps(config)


# ---------------------------------------------------------------- 11. masking in repr


def test_rule11_phone_numbers_are_masked_in_repr_only() -> None:
    result = SendResult(destinations=[SendDestinationResult(to=PHONE, msg_key="K", code="A000")])
    assert PHONE not in repr(result) and "010****1234" in repr(result)
    assert result.destinations[0].to == PHONE
    mo = MoMessage.model_validate({"msgKey": "K", "from": PHONE, "originator": PHONE, "content": "개인 메시지"})
    text = repr(mo) + str(mo)
    assert PHONE not in text and "개인 메시지" not in text and "<6 chars>" in text
    assert mo.from_ == PHONE and mo.content == "개인 메시지"
    assert PHONE not in repr(SmsMessage(from_=PHONE, text="x"))


def test_rule11_phone_lists_and_extra_fields_are_masked() -> None:
    from bizgo._base import mask_phone

    assert mask_phone([PHONE, "0100000"]) == ["010****1234", "*******"]
    model = SendDestinationResult.model_validate({"to": PHONE, "phoneNumber": PHONE})
    assert PHONE not in repr(model)


# ---------------------------------------------------------------- 12. documentation accuracy


def test_rule12_security_md_describes_user_http_client_tls() -> None:
    import pathlib

    text = (pathlib.Path(__file__).parents[1] / "SECURITY.md").read_text(encoding="utf-8")
    assert "SDK 자체에는 TLS 검증을 끄는 옵션이 없습니다" in text and "verify=" in text


# ---------------------------------------------------------------- 14. initial burst


def test_rule14_buckets_start_full() -> None:
    now = [0.0]
    bucket = TokenBucket(200, lambda: now[0])
    assert bucket.reserve(200) == 0.0  # the first second of burst goes out at once
    assert bucket.reserve(1) > 0
