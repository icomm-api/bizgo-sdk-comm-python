"""SDK-DESIGN.md §12 rules 6 (general principle), 11 (extended masking) and 19 (no None for success responses)."""

from __future__ import annotations

import inspect
import pathlib
from typing import Any

import certifi
import httpx
import pytest
from pydantic import BaseModel

from bizgo import AsyncBizgo, Bizgo, ConfigurationError, Destination, SendOmniRequest, SmsMessage
from bizgo._base import mask_phone
from bizgo._operations import OPERATIONS
from bizgo.models import _generated_response as r
from bizgo.testing import FAKE_API_KEY, FakeTransport, sign_webhook, success_envelope

from .test_all_operations import arguments, target

# ---------------------------------------------------------------- 6. unsafe HTTP clients are refused


class RedirectingTransport(httpx.BaseTransport):
    """Follows redirects itself: would resend the request (and the key) elsewhere."""

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=success_envelope({"report": []}))


class RetryingTransport(httpx.BaseTransport):
    """Retries on its own: a send could be delivered twice."""

    def __init__(self) -> None:
        self.calls = 0

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.calls += 1
        return httpx.Response(200, json=success_envelope({"report": []}))


class AuthenticatingTransport(httpx.BaseTransport):
    """Replaces the Authorization header."""

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        request.headers["Authorization"] = "Basic other"
        return httpx.Response(200, json=success_envelope({"report": []}))


class AsyncCustomTransport(httpx.AsyncBaseTransport):
    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=success_envelope({"report": []}))


def _hook(request: httpx.Request) -> None:
    request.headers["Authorization"] = "stolen"


@pytest.mark.parametrize(
    "make",
    [
        lambda: httpx.Client(transport=RedirectingTransport()),
        lambda: httpx.Client(transport=RetryingTransport()),
        lambda: httpx.Client(transport=AuthenticatingTransport()),
        lambda: httpx.Client(transport=httpx.HTTPTransport(retries=3)),
        lambda: httpx.Client(event_hooks={"request": [_hook]}),
        lambda: httpx.Client(cookies={"session": "x"}),
        lambda: httpx.Client(mounts={"https://": RetryingTransport()}),
    ],
    ids=["redirecting", "retrying", "authenticating", "http-transport-retries", "event-hooks", "cookies", "mounts"],
)
def test_rule6_unsafe_http_clients_are_refused_by_default(make: Any) -> None:
    with pytest.raises(ConfigurationError, match="trust_http_client"):
        Bizgo(FAKE_API_KEY, http_client=make())


def test_rule6_trust_http_client_allows_it_and_auth_is_still_forced() -> None:
    transport = AuthenticatingTransport()
    client = Bizgo(FAKE_API_KEY, http_client=httpx.Client(transport=transport), trust_http_client=True, rate_limit=None)
    with client:
        assert client.reports.inquiry("K") == []


def test_rule6_safe_clients_are_accepted() -> None:
    for http in (
        httpx.Client(),
        httpx.Client(transport=httpx.HTTPTransport(retries=0)),
        httpx.Client(proxy="http://proxy.example:3128"),
        httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(200))),
        httpx.Client(transport=FakeTransport()),
        httpx.Client(auth=("user", "pw"), follow_redirects=True),  # forced off per request (auth=None, no redirects)
    ):
        Bizgo(FAKE_API_KEY, http_client=http)


def test_rule6_client_type_and_option_conflicts() -> None:
    with pytest.raises(ConfigurationError):
        Bizgo(FAKE_API_KEY, http_client=httpx.AsyncClient())  # type: ignore[arg-type]
    with pytest.raises(ConfigurationError):
        AsyncBizgo(FAKE_API_KEY, http_client=httpx.AsyncClient(transport=AsyncCustomTransport()))
    AsyncBizgo(FAKE_API_KEY, http_client=httpx.AsyncClient(transport=AsyncCustomTransport()), trust_http_client=True)
    with pytest.raises(ConfigurationError):
        Bizgo(FAKE_API_KEY, http_client=httpx.Client(), proxy="http://proxy.example:3128")


def test_rule6_verify_accepts_a_ca_bundle_path_only(tmp_path: pathlib.Path) -> None:
    Bizgo(FAKE_API_KEY, verify=certifi.where())
    Bizgo(FAKE_API_KEY, verify=pathlib.Path(certifi.where()))
    for bad in (False, 0, "", object()):
        with pytest.raises(ConfigurationError):
            Bizgo(FAKE_API_KEY, verify=bad)  # type: ignore[arg-type]
    missing = tmp_path / "private-dir" / "ca.pem"
    with pytest.raises(ConfigurationError) as info:
        Bizgo(FAKE_API_KEY, verify=missing)
    assert "ca.pem" in str(info.value) and "private-dir" not in str(info.value)


def test_rule6_proxy_option() -> None:
    client = Bizgo(FAKE_API_KEY, proxy="http://user:secret@proxy.example:3128")
    assert client._transport._client._mounts  # the SDK's own client routes through the proxy
    assert "secret" not in repr(client)
    for bad in ("ftp://user:secret@proxy.example", "user:secret@proxy.example:3128", "socks4://user:secret@proxy"):
        with pytest.raises(ConfigurationError) as info:
            Bizgo(FAKE_API_KEY, proxy=bad)
        assert "secret" not in str(info.value)  # the URL (with credentials) is never echoed


# ---------------------------------------------------------------- 11. masking in repr


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("01000000000", "010****0000"),
        ("0100000000", "010*****00"),
        ("158800001", "158*****1"),
        ("15880000", "158****0"),
        ("0100000", "*******"),
        ("112", "***"),
    ],
)
def test_rule11_short_numbers_mask_at_least_half(value: str, expected: str) -> None:
    masked = mask_phone(value)
    assert masked == expected
    assert masked.count("*") * 2 >= len(value) or len(value) >= 11


def test_rule11_request_objects_mask_phones_and_text() -> None:
    request = SendOmniRequest(
        destinations=[Destination(to="01000001234")],
        message_flow=[{"sms": SmsMessage(from_="15880000", text="인증번호 123456")}],  # type: ignore[list-item]
    )
    text = repr(request) + str(request)
    assert "01000001234" not in text and "15880000" not in text and "123456" not in text
    assert request.destinations[0].to == "01000001234"


def test_rule11_person_fields_and_message_bodies() -> None:
    info = r.CounselPersonalInfo.model_validate({"phone_number": "01000001234", "nickname": "홍길동"})
    text = repr(info)
    assert "01000001234" not in text and "홍길동" not in text
    assert info.nickname == "홍길동"
    event = r.CounselMessageWebhookPayload.model_construct(user_name="홍길동", content="상담 내용")
    assert "홍길동" not in repr(event) and "상담 내용" not in repr(event)


def test_rule11_signed_webhook_and_recorded_request_repr() -> None:
    signed = sign_webhook("test-webhook-secret", {"to": "01000001234"})
    assert "01000001234" not in repr(signed)
    fake = FakeTransport()
    with fake.client() as client:
        client.send.sms(to="01000001234", from_="01000000000", text="secret")
    assert "01000001234" not in repr(fake.last_request) and "secret" not in repr(fake.last_request)


# ---------------------------------------------------------------- 19. success responses never return None

GENERATED = sorted(op_id for op_id, op in OPERATIONS.items() if not op.handwritten)


@pytest.mark.parametrize("op_id", GENERATED)
@pytest.mark.parametrize("envelope", ["no-data", "null-data"])
def test_rule19_success_without_data_returns_an_empty_result(op_id: str, envelope: str) -> None:
    op = OPERATIONS[op_id]
    body = success_envelope()
    if envelope == "null-data":
        body["data"]["data"] = None
    fake = FakeTransport()
    fake.on(op_id).respond(200, body)
    with fake.client() as client:
        method = target(client, op)
        annotation = str(inspect.signature(method).return_annotation)
        args, kwargs = arguments(op)
        result = method(*args, **kwargs)
    if annotation == "None":
        assert result is None  # a void operation
        return
    assert "None" not in annotation, f"{op_id} still returns Optional: {annotation}"
    assert result is not None
    assert isinstance(result, (list, BaseModel))
    if isinstance(result, list):
        assert result == []
