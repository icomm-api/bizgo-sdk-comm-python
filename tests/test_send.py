from __future__ import annotations

import json

import httpx
import pydantic
import pytest
import respx

from bizgo import (
    AlimtalkMessage,
    APIConnectionError,
    Bizgo,
    Destination,
    DuplicateRequestError,
    MmsMessage,
    RateLimitError,
    SmsMessage,
)

from .conftest import API_KEY, envelope

PATH = "/api/comm/v1/send/omni"


def accepted(*codes: str) -> dict:
    return envelope(
        {
            "destinations": [
                {"to": "01000000000", "msgKey": f"KEY{i:03d}", "code": c, "result": "r"} for i, c in enumerate(codes)
            ]
        },
        ref="ref-1",
    )


def test_sms_request_body_and_headers(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted("A000"))
    result = client.send.sms(to="01000000000", from_="01000000000", text="인증번호는 123456 입니다.", ref="ref-1")

    request = route.calls.last.request
    assert request.headers["Authorization"] == API_KEY  # raw key, no prefix (verified on sandbox)
    assert request.headers["User-Agent"].startswith("bizgo-sdk-comm-python/")
    assert json.loads(request.content) == {
        "destinations": [{"to": "01000000000"}],
        "messageFlow": [{"sms": {"from": "01000000000", "text": "인증번호는 123456 입니다."}}],
        "ref": "ref-1",
    }
    assert result.msg_keys == ["KEY000"]
    assert result.failed == []
    assert result.ref == "ref-1"
    assert result.tracking_id == "TR-TEST"


def test_fallback_flow_keeps_order_and_omits_unset_defaults(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted("A000"))
    client.send.omni(
        to=[Destination(to="01000000000", replace_words={"name": "홍길동"})],
        messages=[
            AlimtalkMessage(
                sender_key="SENDER_KEY_EXAMPLE",
                template_code="TEMPLATE_CODE_EXAMPLE",
                msg_type="AT",
                text="#{name}님 주문 완료",
            ),
            SmsMessage(from_="01000000000", text="#{name}님 주문 완료"),
        ],
        idempotency_key="order-1",
    )
    body = json.loads(route.calls.last.request.content)
    assert [next(iter(item)) for item in body["messageFlow"]] == ["alimtalk", "sms"]
    assert body["messageFlow"][0]["alimtalk"] == {
        "senderKey": "SENDER_KEY_EXAMPLE",
        "templateCode": "TEMPLATE_CODE_EXAMPLE",
        "msgType": "AT",
        "text": "#{name}님 주문 완료",
    }  # responseMethod/timeout defaults are not sent
    assert body["destinations"] == [{"to": "01000000000", "replaceWords": {"name": "홍길동"}}]
    assert body["idempotencyKey"] == "order-1"


def test_partial_failure_is_reported_per_recipient(client: Bizgo, api: respx.MockRouter) -> None:
    api.post(PATH).respond(json=accepted("A000", "A306"))
    result = client.send.sms(to=["01000000000", "01000000001"], from_="01000000000", text="x")
    assert [d.code for d in result.failed] == ["A306"]
    assert len(result.succeeded) == 1


def test_mms_and_lms(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=accepted("A000"))
    client.send.mms(to="01000000000", from_="01000000000", text="본문", title="제목", file_keys=["FILE_KEY_001"])
    assert json.loads(route.calls.last.request.content)["messageFlow"][0]["mms"]["fileKey"] == ["FILE_KEY_001"]
    client.send.lms(to="01000000000", from_="01000000000", text="본문")
    assert "fileKey" not in json.loads(route.calls.last.request.content)["messageFlow"][0]["mms"]


@pytest.mark.parametrize(
    ("text", "message"),
    [("가" * 46, "최대 90byte"), ("안녕😀", "EUC-KR")],
)
def test_sms_byte_limit_is_checked_before_sending(
    client: Bizgo, api: respx.MockRouter, text: str, message: str
) -> None:
    route = api.post(PATH)
    with pytest.raises(pydantic.ValidationError, match=message):
        client.send.sms(to="01000000000", from_="01000000000", text=text)
    assert not route.called


def test_sms_limit_counts_bytes_not_characters() -> None:
    SmsMessage(from_="01000000000", text="가" * 45)  # 90 bytes: ok
    SmsMessage(from_="01000000000", text="a" * 90)
    MmsMessage(from_="01000000000", text="가" * 1000)  # 2,000 bytes: ok
    with pytest.raises(pydantic.ValidationError):
        MmsMessage(from_="01000000000", text="가" * 1001)


def test_unknown_fields_are_rejected() -> None:
    with pytest.raises(pydantic.ValidationError, match="Extra inputs"):
        AlimtalkMessage(sender_key="S", template_code="T", templatecode="typo")  # type: ignore[call-arg]


def test_more_than_200_recipients_is_rejected(client: Bizgo) -> None:
    with pytest.raises(pydantic.ValidationError):
        client.send.sms(to=[f"010{i:08d}" for i in range(201)], from_="01000000000", text="x")


def test_message_flow_item_needs_exactly_one_channel(client: Bizgo) -> None:
    with pytest.raises(pydantic.ValidationError, match="정확히 하나"):
        client.send.request(
            {
                "destinations": [{"to": "01000000000"}],
                "messageFlow": [{"sms": {"from": "1", "text": "x"}, "mms": {"from": "1", "text": "x"}}],
            }
        )


def test_validation_errors_do_not_echo_phone_numbers(client: Bizgo) -> None:
    with pytest.raises(pydantic.ValidationError) as info:
        client.send.sms(to="01000001234", from_="01000000000", text="😀")
    assert "01000001234" not in str(info.value)


def test_send_without_idempotency_key_is_not_retried_after_timeout(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).mock(side_effect=httpx.ReadTimeout("timeout"))
    with pytest.raises(APIConnectionError):
        client.send.sms(to="01000000000", from_="01000000000", text="x")
    assert route.call_count == 1


def test_send_with_idempotency_key_is_retried_after_timeout(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).mock(side_effect=[httpx.ReadTimeout("timeout"), httpx.Response(200, json=accepted("A000"))])
    result = client.send.sms(to="01000000000", from_="01000000000", text="x", idempotency_key="k-1")
    assert route.call_count == 2
    assert result.msg_keys == ["KEY000"]


def test_duplicate_after_lost_response_explains_what_happened(client: Bizgo, api: respx.MockRouter) -> None:
    api.post(PATH).mock(side_effect=[httpx.ReadTimeout("timeout"), httpx.Response(200, json=envelope(code="A301"))])
    with pytest.raises(DuplicateRequestError, match="이미 접수"):
        client.send.sms(to="01000000000", from_="01000000000", text="x", idempotency_key="k-1")


def test_rate_limit_is_retried_with_retry_after(client: Bizgo, api: respx.MockRouter, _no_sleep: list[float]) -> None:
    limited = httpx.Response(
        429, headers={"Retry-After": "2"}, json={"common": {"authCode": "A020", "authResult": "Ratelimit"}}
    )
    route = api.post(PATH).mock(side_effect=[limited, httpx.Response(200, json=accepted("A000"))])
    client.send.sms(to="01000000000", from_="01000000000", text="x")
    assert route.call_count == 2
    assert _no_sleep == [2.0]


def test_rate_limit_gives_up_after_max_retries(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(429, json={"data": {"code": "A020", "result": "Number of 'Ratelimit' exceeded"}})
    with pytest.raises(RateLimitError):
        client.send.sms(to="01000000000", from_="01000000000", text="x")
    assert route.call_count == 3  # 1 + max_retries(2)
