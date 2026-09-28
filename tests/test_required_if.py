"""Conditional-required fields (``x-sdk-required-if``): checked before anything is sent, no values in errors."""

from __future__ import annotations

from typing import Any

import pydantic
import pytest
import respx
import yaml

from bizgo import AlimtalkMessage, Bizgo, Destination, SmsMessage
from bizgo._generated_required_if import RULES
from bizgo.models import _generated_request as req

from .conftest import envelope

PATH = "/api/comm/v1/send/omni"
SECRET = "SECRET-TEXT-VALUE"  # a value that must never show up in an error message
ACCEPTED = envelope({"destinations": [{"to": "01000000000", "msgKey": "KEY000", "code": "A000", "result": "r"}]})


def _error_text(exc: pytest.ExceptionInfo[BaseException]) -> str:
    text = str(exc.value)
    assert SECRET not in text
    assert "01000000000" not in text
    return text


def test_rules_table_matches_the_spec() -> None:
    with open("spec/openapi.yaml", encoding="utf-8") as fh:
        schemas = yaml.safe_load(fh)["components"]["schemas"]
    in_spec = {name for name, schema in schemas.items() if "x-sdk-required-if" in schema}
    assert in_spec and set(RULES) == in_spec
    assert RULES["AlimtalkMessage"][0] == ("sendType", "notEquals", ("template",), ("msgType", "text"), ())


def test_alimtalk_full_send_without_msg_type_fails_before_http(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=ACCEPTED)
    with pytest.raises(pydantic.ValidationError) as exc:
        client.send.omni(
            to="01000000000",
            messages=[AlimtalkMessage(sender_key="SENDER_KEY_EXAMPLE", template_code="T1", text=SECRET)],
        )
    assert "msgType: required when sendType != template" in _error_text(exc)
    assert not route.called


def test_alimtalk_dict_body_without_msg_type_and_text_fails_before_http(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=ACCEPTED)
    body: dict[str, Any] = {
        "destinations": [{"to": "01000000000"}],
        "messageFlow": [{"alimtalk": {"senderKey": "SENDER_KEY_EXAMPLE", "templateCode": "T1"}}],
    }
    with pytest.raises(pydantic.ValidationError) as exc:
        client.send.request(body)
    text = _error_text(exc)
    assert "messageFlow.0.alimtalk" in text
    assert "msgType: required" in text and "text: required" in text
    assert not route.called


def test_alimtalk_with_msg_type_and_text_is_sent(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=ACCEPTED)
    client.send.omni(
        to="01000000000",
        messages=[AlimtalkMessage(sender_key="SENDER_KEY_EXAMPLE", template_code="T1", msg_type="AT", text="hi")],
    )
    assert route.called


def test_template_send_needs_replace_words_on_every_destination(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=ACCEPTED)
    message = AlimtalkMessage(sender_key="SENDER_KEY_EXAMPLE", template_code="T1", send_type="template")
    to = [Destination(to="01000000000", replace_words={"name": SECRET}), Destination(to="01000000000")]
    with pytest.raises(pydantic.ValidationError) as exc:
        client.send.omni(to=to, messages=[message])
    text = _error_text(exc)
    assert "destinations[1].replaceWords: required when messageFlow[0].alimtalk.sendType == template" in text
    assert "destinations[0]" not in text
    assert not route.called

    # the same rule for a raw dict body
    with pytest.raises(pydantic.ValidationError):
        client.send.request(
            {
                "destinations": [{"to": "01000000000"}],
                "messageFlow": [{"alimtalk": {"senderKey": "S", "templateCode": "T1", "sendType": "template"}}],
            }
        )
    assert not route.called


def test_template_send_with_replace_words_does_not_need_msg_type(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=ACCEPTED)
    message = AlimtalkMessage(sender_key="SENDER_KEY_EXAMPLE", template_code="T1", send_type="template")
    client.send.omni(to=[Destination(to="01000000000", replace_words={"name": "x"})], messages=[message])
    assert route.called
    alimtalk = route.calls.last.request.read().decode()
    assert "msgType" not in alimtalk


def test_standalone_channel_model_skips_root_paths() -> None:
    # ``$.destinations`` is only known once the whole request is built
    AlimtalkMessage(sender_key="SENDER_KEY_EXAMPLE", template_code="T1", send_type="template")


def test_bulk_reports_recipient_indexes_of_the_whole_list(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=ACCEPTED)
    to = [Destination(to="01000000000", replace_words={"n": "x"}) for _ in range(3)]
    to.append(Destination(to="01000000000"))
    message = AlimtalkMessage(sender_key="SENDER_KEY_EXAMPLE", template_code="T1", send_type="template")
    with pytest.raises(ValueError, match=r"destinations\[3\]\.replaceWords"):
        client.send.bulk(to=to, messages=[message], chunk_size=2)
    assert not route.called


def test_brand_button_web_link_needs_both_urls() -> None:
    with pytest.raises(pydantic.ValidationError) as exc:
        req.BrandMessageButton(type="WL", name=SECRET, url_mobile="https://example.com")
    assert "urlPc: required when type == WL" in _error_text(exc)
    req.BrandMessageButton(type="WL", url_pc="https://example.com", url_mobile="https://example.com")
    with pytest.raises(pydantic.ValidationError, match="urlMobile: required when type == AL"):
        req.BrandMessageButton(type="AL")
    req.BrandMessageButton(type="BK")


def test_rcs_header_needs_footer(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=ACCEPTED)
    rcs: dict[str, Any] = {
        "from": "01000000000",
        "formatId": "RCS_FORMAT_EXAMPLE",
        "brandKey": "RCS_BRAND_EXAMPLE",
        "body": {"title": SECRET, "description": SECRET},
        "header": "1",
    }
    body = {"destinations": [{"to": "01000000000"}], "messageFlow": [{"rcs": rcs}]}
    with pytest.raises(pydantic.ValidationError) as exc:
        client.send.request(body)
    assert "footer: required when header == 1" in _error_text(exc)
    assert not route.called
    client.send.request({**body, "messageFlow": [{"rcs": {**rcs, "footer": "080-000-0000"}}]})
    assert route.called


def test_brand_message_rules_and_fallback_sms(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post(PATH).respond(json=ACCEPTED)
    with pytest.raises(pydantic.ValidationError) as exc:
        req.BrandMessage(send_type="basic", sender_key="SENDER_KEY_EXAMPLE", text=SECRET)
    text = _error_text(exc)
    assert "msgType: required when sendType in [basic, free]" in text
    assert "templateCode: required when sendType in [basic, template]" in text
    free = req.BrandMessage(send_type="free", sender_key="SENDER_KEY_EXAMPLE", msg_type="FT", text="x")
    client.send.omni(to="01000000000", messages=[free, SmsMessage(from_="01000000000", text="x")])
    assert route.called


def test_counsel_rich_message_paths_relative_to_the_body() -> None:
    base: dict[str, Any] = {"userKey": "USER_KEY", "senderKey": "SENDER_KEY_EXAMPLE", "message": SECRET}
    with pytest.raises(pydantic.ValidationError) as exc:
        req.CounselRichMessageRequest.model_validate({**base, "msgType": "IMAGE"})
    assert "attachment.image: required when msgType in [IMAGE, WIDE]" in _error_text(exc)
    with pytest.raises(pydantic.ValidationError, match="certExpiry: required when msgType == KAKAO_CERT"):
        req.CounselRichMessageRequest.model_validate({**base, "msgType": "KAKAO_CERT"})
    req.CounselRichMessageRequest.model_validate({**base, "msgType": "TEXT"})
