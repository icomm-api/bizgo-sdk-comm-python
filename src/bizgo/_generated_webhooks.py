"""Generated from spec/openapi.yaml by scripts/generate_models.py. Do not edit."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ._base import ResponseModel
from ._webhook_body import parse_payload
from .models import _generated_response as _r

WEBHOOKS: dict[str, tuple[type[ResponseModel], bool]] = {
    "report": (_r.ReportWebhookPayload, True),
    "mo": (_r.MoWebhookPayload, True),
    "counselMessage": (_r.CounselMessageWebhookPayload, False),
    "counselReference": (_r.CounselReferenceWebhookPayload, False),
    "counselExpiredSession": (_r.CounselExpiredSessionWebhookPayload, False),
    "counselSeenInfo": (_r.CounselSeenInfoWebhookPayload, False),
    "counselPersonalInfo": (_r.CounselPersonalInfoWebhookPayload, False),
    "counselCertResult": (_r.CounselCertResultWebhookPayload, False),
    "counselResult": (_r.CounselResultWebhookPayload, False),
}
"""``x-sdk-webhook`` name -> (payload model, signed). Only signed webhooks (report, MO) are verified."""


def parse_counsel_message(body: bytes | str | Mapping[str, Any]) -> _r.CounselMessageWebhookPayload:
    """상담톡 사용자 메시지 수신(Webhook): parse the body without verifying a signature."""
    return parse_payload(_r.CounselMessageWebhookPayload, body)


def parse_counsel_reference(body: bytes | str | Mapping[str, Any]) -> _r.CounselReferenceWebhookPayload:
    """상담톡 사용자 메타 정보 수신(Webhook): parse the body without verifying a signature."""
    return parse_payload(_r.CounselReferenceWebhookPayload, body)


def parse_counsel_expired_session(body: bytes | str | Mapping[str, Any]) -> _r.CounselExpiredSessionWebhookPayload:
    """상담톡 세션 종료 수신(Webhook): parse the body without verifying a signature."""
    return parse_payload(_r.CounselExpiredSessionWebhookPayload, body)


def parse_counsel_seen_info(body: bytes | str | Mapping[str, Any]) -> _r.CounselSeenInfoWebhookPayload:
    """상담톡 읽음 정보 수신(Webhook): parse the body without verifying a signature."""
    return parse_payload(_r.CounselSeenInfoWebhookPayload, body)


def parse_counsel_personal_info(body: bytes | str | Mapping[str, Any]) -> _r.CounselPersonalInfoWebhookPayload:
    """상담톡 개인정보 수신(Webhook): parse the body without verifying a signature."""
    return parse_payload(_r.CounselPersonalInfoWebhookPayload, body)


def parse_counsel_cert_result(body: bytes | str | Mapping[str, Any]) -> _r.CounselCertResultWebhookPayload:
    """상담톡 본인인증 결과 수신(Webhook): parse the body without verifying a signature."""
    return parse_payload(_r.CounselCertResultWebhookPayload, body)


def parse_counsel_result(body: bytes | str | Mapping[str, Any]) -> _r.CounselResultWebhookPayload:
    """상담톡 발송 결과 수신(Webhook): parse the body without verifying a signature."""
    return parse_payload(_r.CounselResultWebhookPayload, body)


class WebhookMethods:
    """Generated webhook parsers, mixed into :class:`bizgo.webhooks.WebhookReceiver`."""

    def verify(self, headers: Mapping[str, str]) -> None:
        raise NotImplementedError

    def counsel_message(self, headers: Mapping[str, str], body: bytes | str) -> _r.CounselMessageWebhookPayload:
        """상담톡 사용자 메시지 수신(Webhook) (``x-sdk-webhook: counselMessage``). Parse the body.

        This webhook is not signed: no secret is used and signature headers, if present, are
        ignored. The body size cap, JSON depth limit and type checks still apply.
        Answer with :meth:`counsel_ack`."""
        del headers  # not signed
        return parse_counsel_message(body)

    def counsel_reference(self, headers: Mapping[str, str], body: bytes | str) -> _r.CounselReferenceWebhookPayload:
        """상담톡 사용자 메타 정보 수신(Webhook) (``x-sdk-webhook: counselReference``). Parse the body.

        This webhook is not signed: no secret is used and signature headers, if present, are
        ignored. The body size cap, JSON depth limit and type checks still apply.
        Answer with :meth:`counsel_ack`."""
        del headers  # not signed
        return parse_counsel_reference(body)

    def counsel_expired_session(
        self, headers: Mapping[str, str], body: bytes | str
    ) -> _r.CounselExpiredSessionWebhookPayload:
        """상담톡 세션 종료 수신(Webhook) (``x-sdk-webhook: counselExpiredSession``). Parse the body.

        This webhook is not signed: no secret is used and signature headers, if present, are
        ignored. The body size cap, JSON depth limit and type checks still apply.
        Answer with :meth:`counsel_ack`."""
        del headers  # not signed
        return parse_counsel_expired_session(body)

    def counsel_seen_info(self, headers: Mapping[str, str], body: bytes | str) -> _r.CounselSeenInfoWebhookPayload:
        """상담톡 읽음 정보 수신(Webhook) (``x-sdk-webhook: counselSeenInfo``). Parse the body.

        This webhook is not signed: no secret is used and signature headers, if present, are
        ignored. The body size cap, JSON depth limit and type checks still apply.
        Answer with :meth:`counsel_ack`."""
        del headers  # not signed
        return parse_counsel_seen_info(body)

    def counsel_personal_info(
        self, headers: Mapping[str, str], body: bytes | str
    ) -> _r.CounselPersonalInfoWebhookPayload:
        """상담톡 개인정보 수신(Webhook) (``x-sdk-webhook: counselPersonalInfo``). Parse the body.

        This webhook is not signed: no secret is used and signature headers, if present, are
        ignored. The body size cap, JSON depth limit and type checks still apply.
        Answer with :meth:`counsel_ack`."""
        del headers  # not signed
        return parse_counsel_personal_info(body)

    def counsel_cert_result(self, headers: Mapping[str, str], body: bytes | str) -> _r.CounselCertResultWebhookPayload:
        """상담톡 본인인증 결과 수신(Webhook) (``x-sdk-webhook: counselCertResult``). Parse the body.

        This webhook is not signed: no secret is used and signature headers, if present, are
        ignored. The body size cap, JSON depth limit and type checks still apply.
        Answer with :meth:`counsel_ack`."""
        del headers  # not signed
        return parse_counsel_cert_result(body)

    def counsel_result(self, headers: Mapping[str, str], body: bytes | str) -> _r.CounselResultWebhookPayload:
        """상담톡 발송 결과 수신(Webhook) (``x-sdk-webhook: counselResult``). Parse the body.

        This webhook is not signed: no secret is used and signature headers, if present, are
        ignored. The body size cap, JSON depth limit and type checks still apply.
        Answer with :meth:`counsel_ack`."""
        del headers  # not signed
        return parse_counsel_result(body)
