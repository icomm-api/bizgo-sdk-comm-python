"""Receive Bizgo webhooks (delivery reports, MO messages and Kakao counsel/상담톡 events).

Typical use in a web handler::

    from bizgo.webhooks import WebhookReceiver, WebhookVerificationError

    receiver = WebhookReceiver(secret=os.environ["BIZGO_WEBHOOK_SECRET"])

    def report_endpoint(request):
        try:
            report = receiver.report(request.headers, request.body)
        except WebhookVerificationError:
            return 401
        store(report)                      # make this idempotent: the same report can arrive again
        return json(receiver.ack(report.msg_key))   # must answer within 5 seconds

Security notes:

- The signature is ``X-IB-Signature = HmacSHA256(secret, X-IB-Timestamp)``; it is verified together with the
  timestamp window. As general practice, also restrict the endpoint to the Bizgo webhook source IPs, serve it over
  HTTPS, and confirm important results with the inquiry APIs.
- Bizgo retries a webhook up to 3 times when it does not get ``{"msgKey": ...}`` back, so deduplicate by ``msg_key``.
- The signature output encoding (hex or base64) is not confirmed yet; both are accepted (hex in any case).
- The webhook secret is obtained by requesting it from Bizgo (it is delivered separately).

Counsel (상담톡) webhooks (``counsel_message``, ``counsel_reference``, ``counsel_expired_session``,
``counsel_seen_info``, ``counsel_personal_info``, ``counsel_cert_result``, ``counsel_result``):

- 상담톡 웹훅에는 서명이 없습니다(서명은 리포트·MO 웹훅에만 적용). The SDK does not require or check a signature for
  them and ignores ``X-IB-Timestamp``/``X-IB-Signature`` if present; the body size cap, JSON depth limit (64) and
  type/shape checks still apply.
- No webhook secret is needed for counsel webhooks: use the module-level parsers (``parse_counsel_message(body)``
  etc.) when you only receive counsel webhooks. :class:`WebhookReceiver` methods behave the same way.
- As general practice, serve counsel endpoints over HTTPS, restrict them to the Bizgo webhook source IPs, and
  deduplicate by ``msg_key`` where the payload has one.
- Answer counsel webhooks with :func:`counsel_ack` (``{"code": "A000", "result": "Success"}``), not :func:`ack`.
- Bodies carry end-user identifiers, chat content and (``counsel_personal_info``/``counsel_cert_result``)
  personal data. Never log them.
- Report and MO webhooks always require a valid signature.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import math
import re
import time
from collections.abc import Mapping
from typing import Any

from ._base import ResponseModel
from ._errors import WebhookPayloadError, WebhookVerificationError
from ._generated_webhooks import (
    WEBHOOKS,
    WebhookMethods,
    parse_counsel_cert_result,
    parse_counsel_expired_session,
    parse_counsel_message,
    parse_counsel_personal_info,
    parse_counsel_reference,
    parse_counsel_result,
    parse_counsel_seen_info,
)
from ._webhook_body import MAX_BODY_BYTES, as_bytes, parse_payload
from .models._generated_response import MoWebhookPayload, ReportWebhookPayload

__all__ = [
    "DEFAULT_TOLERANCE_SECONDS",
    "MAX_BODY_BYTES",
    "WEBHOOKS",
    "MoWebhookPayload",
    "ReportWebhookPayload",
    "WebhookPayloadError",
    "WebhookReceiver",
    "WebhookVerificationError",
    "ack",
    "counsel_ack",
    "parse",
    "parse_counsel_cert_result",
    "parse_counsel_expired_session",
    "parse_counsel_message",
    "parse_counsel_personal_info",
    "parse_counsel_reference",
    "parse_counsel_result",
    "parse_counsel_seen_info",
    "parse_mo",
    "parse_report",
    "verify_signature",
]

TIMESTAMP_HEADER = "X-IB-Timestamp"
SIGNATURE_HEADER = "X-IB-Signature"
DEFAULT_TOLERANCE_SECONDS = 300.0


_TIMESTAMP = re.compile(r"[0-9]{1,16}")


def _check_tolerance(tolerance: float | None) -> float | None:
    """``None`` (explicitly disabled) or a finite number of seconds > 0."""
    if tolerance is None:
        return None
    if isinstance(tolerance, bool) or not isinstance(tolerance, (int, float)):
        raise ValueError("tolerance는 0보다 큰 초 단위 숫자이거나 None(검사 끔)이어야 합니다")
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("tolerance는 0보다 큰 유한한 초 단위 숫자여야 합니다(끄려면 None)")
    return float(tolerance)


def _timestamp_seconds(timestamp: str) -> float:
    # ASCII digits only, 1-16 characters: no Unicode digits, no huge integers
    if not isinstance(timestamp, str) or not _TIMESTAMP.fullmatch(timestamp):
        raise WebhookVerificationError("X-IB-Timestamp가 숫자(1~16자리)가 아닙니다")
    value = int(timestamp)
    return value / 1000 if len(timestamp) >= 13 else float(value)  # epoch ms (documented example) or seconds


def verify_signature(
    *,
    secret: str | bytes,
    timestamp: str,
    signature: str,
    tolerance: float | None = DEFAULT_TOLERANCE_SECONDS,
    now: float | None = None,
) -> None:
    """Verify ``X-IB-Signature`` for a webhook request, or raise :class:`~bizgo.WebhookVerificationError`.

    Args:
        secret: Webhook secret (request it from Bizgo). Read it from an environment variable or vault.
        timestamp: ``X-IB-Timestamp`` header value.
        signature: ``X-IB-Signature`` header value.
        tolerance: Maximum age in seconds, to limit replay. ``None`` disables the check (not recommended).
        now: Current UNIX time, for tests.
    """
    if not secret or not as_bytes(secret).strip():
        raise WebhookVerificationError("웹훅 secret이 비어 있습니다")
    if not signature:
        raise WebhookVerificationError("X-IB-Signature 헤더가 없습니다")
    tolerance = _check_tolerance(tolerance)
    sent_at = _timestamp_seconds(timestamp)
    if tolerance is not None:
        age = (time.time() if now is None else now) - sent_at
        if abs(age) > tolerance:
            raise WebhookVerificationError(f"X-IB-Timestamp가 허용 범위({tolerance:.0f}초)를 벗어났습니다")

    digest = hmac.new(as_bytes(secret), timestamp.encode("ascii"), hashlib.sha256).digest()
    received = signature.strip()
    candidates = [digest.hex().encode("ascii")]
    try:
        decoded = base64.b64decode(received, validate=True)
    except (binascii.Error, ValueError):
        decoded = b""
    ok = hmac.compare_digest(received.lower().encode("ascii", "replace"), candidates[0])
    ok = hmac.compare_digest(decoded, digest) or ok
    if not ok:
        raise WebhookVerificationError("서명이 일치하지 않습니다")


def parse_report(body: bytes | str | Mapping[str, Any]) -> ReportWebhookPayload:
    """Parse a report webhook body. Does not verify the signature; use :class:`WebhookReceiver` for that."""
    return parse_payload(ReportWebhookPayload, body)


def parse_mo(body: bytes | str | Mapping[str, Any]) -> MoWebhookPayload:
    """Parse an MO webhook body. Does not verify the signature; use :class:`WebhookReceiver` for that."""
    return parse_payload(MoWebhookPayload, body)


_ = WebhookPayloadError  # re-exported


def parse(name: str, body: bytes | str | Mapping[str, Any]) -> ResponseModel:
    """Parse any webhook body by its ``x-sdk-webhook`` name (``report``, ``mo``, ``counselMessage``, ...).

    Does not verify the signature.
    """
    entry = WEBHOOKS.get(name)
    if entry is None:
        raise ValueError(f"알 수 없는 웹훅 이름입니다: {name}")
    return parse_payload(entry[0], body)


def ack(msg_key: str) -> dict[str, str]:
    """The response body Bizgo expects for report/MO webhooks: ``{"msgKey": "<received msgKey>"}``."""
    return {"msgKey": msg_key}


def counsel_ack() -> dict[str, str]:
    """The response body Bizgo expects for counsel (상담톡) webhooks: ``{"code": "A000", "result": "Success"}``."""
    return {"code": "A000", "result": "Success"}


def _header(headers: Mapping[str, str], name: str) -> str:
    lowered = name.lower()
    for key, value in headers.items():
        if key.lower() == lowered:
            return value
    return ""


class WebhookReceiver(WebhookMethods):
    """Verify and parse webhook requests with one secret.

    One method per webhook: :meth:`report`, :meth:`mo`, and the counsel (상담톡) webhooks ``counsel_message``,
    ``counsel_reference``, ``counsel_expired_session``, ``counsel_seen_info``, ``counsel_personal_info``,
    ``counsel_cert_result`` and ``counsel_result``.

    Args:
        secret: Webhook secret (request it from Bizgo). Read it from an environment variable or a secret store.
        tolerance: Maximum timestamp age in seconds (replay window): a finite number > 0, or ``None`` to turn
            the check off explicitly (not recommended).

    Report and MO webhooks are always verified. Counsel webhooks are not signed, so the ``counsel_*`` methods only
    parse the body (signature headers are ignored); counsel-only users can call ``parse_counsel_*`` without a secret.
    """

    def __init__(
        self,
        secret: str | bytes,
        *,
        tolerance: float | None = DEFAULT_TOLERANCE_SECONDS,
    ) -> None:
        if not isinstance(secret, (str, bytes)) or not secret or not as_bytes(secret).strip():
            raise ValueError("webhook secret is empty")
        self._secret = as_bytes(secret)
        self._tolerance = _check_tolerance(tolerance)

    def __repr__(self) -> str:
        return f"WebhookReceiver(tolerance={self._tolerance})"

    def verify(self, headers: Mapping[str, str]) -> None:
        """Verify the signature headers of a request (case-insensitive header names)."""
        verify_signature(
            secret=self._secret,
            timestamp=_header(headers, TIMESTAMP_HEADER),
            signature=_header(headers, SIGNATURE_HEADER),
            tolerance=self._tolerance,
        )

    def report(self, headers: Mapping[str, str], body: bytes | str) -> ReportWebhookPayload:
        """Verify, then parse a delivery report webhook."""
        self.verify(headers)
        return parse_report(body)

    def mo(self, headers: Mapping[str, str], body: bytes | str) -> MoWebhookPayload:
        """Verify, then parse an MO webhook."""
        self.verify(headers)
        return parse_mo(body)

    @staticmethod
    def ack(msg_key: str) -> dict[str, str]:
        """See :func:`ack` (report/MO webhooks)."""
        return ack(msg_key)

    @staticmethod
    def counsel_ack() -> dict[str, str]:
        """See :func:`counsel_ack` (counsel webhooks)."""
        return counsel_ack()
