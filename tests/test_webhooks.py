from __future__ import annotations

import base64
import hashlib
import hmac
import json

import pytest

from bizgo.webhooks import WebhookReceiver, WebhookVerificationError, ack, parse_mo, verify_signature

SECRET = "test-webhook-secret"
NOW = 1743381600.0
TIMESTAMP = "1743381600000"  # epoch ms, as in the API reference example
BODY = json.dumps(
    {"msgKey": "KEY001", "serviceType": "SMS", "reportTime": "t", "reportType": "0", "reportCode": "10000"}
).encode()


def sign(timestamp: str = TIMESTAMP, secret: str = SECRET) -> bytes:
    return hmac.new(secret.encode(), timestamp.encode(), hashlib.sha256).digest()


@pytest.mark.parametrize(
    "encode",
    [
        lambda d: d.hex(),
        lambda d: d.hex().upper(),
        lambda d: base64.b64encode(d).decode(),
    ],
)
def test_valid_signature_encodings(encode) -> None:  # type: ignore[no-untyped-def]
    verify_signature(secret=SECRET, timestamp=TIMESTAMP, signature=encode(sign()), now=NOW)


def test_wrong_secret() -> None:
    with pytest.raises(WebhookVerificationError, match="일치하지"):
        verify_signature(secret=SECRET, timestamp=TIMESTAMP, signature=sign(secret="other").hex(), now=NOW)


def test_prefixed_signature_is_rejected() -> None:
    with pytest.raises(WebhookVerificationError, match="일치하지"):
        verify_signature(secret=SECRET, timestamp=TIMESTAMP, signature="sha256=" + sign().hex(), now=NOW)


def test_old_timestamp_is_rejected_to_limit_replay() -> None:
    with pytest.raises(WebhookVerificationError, match="허용 범위"):
        verify_signature(secret=SECRET, timestamp=TIMESTAMP, signature=sign().hex(), now=NOW + 301)


def test_seconds_timestamp_is_accepted() -> None:
    verify_signature(secret=SECRET, timestamp="1743381600", signature=sign("1743381600").hex(), now=NOW)


@pytest.mark.parametrize(("timestamp", "signature"), [("", "x"), ("abc", "x"), (TIMESTAMP, "")])
def test_missing_or_malformed_headers(timestamp: str, signature: str) -> None:
    with pytest.raises(WebhookVerificationError):
        verify_signature(secret=SECRET, timestamp=timestamp, signature=signature, now=NOW)


def test_receiver_verifies_then_parses(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("bizgo.webhooks.time.time", lambda: NOW)
    receiver = WebhookReceiver(SECRET)
    headers = {"x-ib-timestamp": TIMESTAMP, "X-IB-SIGNATURE": sign().hex()}  # header names are case-insensitive
    report = receiver.report(headers, BODY)
    assert report.msg_key == "KEY001"
    assert receiver.ack(report.msg_key) == {"msgKey": "KEY001"}
    assert SECRET not in repr(receiver)


def test_receiver_rejects_unsigned_request() -> None:
    with pytest.raises(WebhookVerificationError):
        WebhookReceiver(SECRET).report({}, BODY)


def test_parse_mo_and_invalid_json() -> None:
    mo = parse_mo(
        {
            "msgKey": "K",
            "serviceType": "MO",
            "msgType": "SM",
            "to": "#000000",
            "from": "01000000000",
            "carrier": "10001",
            "originator": "01000000000",
            "content": "투표 1",
            "occurredTime": "t",
        }
    )
    assert mo.from_ == "01000000000"
    with pytest.raises(WebhookVerificationError, match="JSON"):
        parse_mo(b"not json")


def test_ack_shape() -> None:
    assert ack("K") == {"msgKey": "K"}
