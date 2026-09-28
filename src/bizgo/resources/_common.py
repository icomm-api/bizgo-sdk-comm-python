"""Helpers shared by the sync and async resources."""

from __future__ import annotations

import datetime as dt
import mimetypes
import os
from collections.abc import Sequence
from typing import IO, Any, TypeAlias

from .._base import RequestModel
from ..models import _generated_request as req

KST = dt.timezone(dt.timedelta(hours=9), "KST")

DEFAULT_IDEMPOTENCY_TTL = 86400
"""Seconds (24 hours) sent as ``idempotencyTtl`` when an ``idempotencyKey`` is set without a TTL.

Bizgo rejects an ``idempotencyKey`` without ``idempotencyTtl`` (A309), so the SDK fills this value. An explicit
TTL (including ``0``) is sent as given; without a key no TTL is added.
"""

Recipient: TypeAlias = str | req.Destination | dict[str, Any]
"""A phone number (``"01000000000"``), a :class:`~bizgo.models.Destination`, or an equivalent dict."""
Recipients: TypeAlias = Recipient | Sequence[Recipient]

ChannelMessage: TypeAlias = (
    req.SmsMessage
    | req.MmsMessage
    | req.InternationalMessage
    | req.RcsMessage
    | req.AlimtalkMessage
    | req.BrandMessage
    | req.NaverTalkMessage
)
"""A channel message model. It is wrapped into its ``messageFlow`` item automatically."""

FileInput: TypeAlias = str | os.PathLike[str] | bytes | IO[bytes]
"""A file path, raw bytes, or a binary file object."""

_FLOW_ITEM: dict[type[RequestModel], tuple[type[RequestModel], str]] = {
    req.SmsMessage: (req.SmsFlowItem, "sms"),
    req.MmsMessage: (req.MmsFlowItem, "mms"),
    req.InternationalMessage: (req.InternationalFlowItem, "international"),
    req.RcsMessage: (req.RcsFlowItem, "rcs"),
    req.AlimtalkMessage: (req.AlimtalkFlowItem, "alimtalk"),
    req.BrandMessage: (req.BrandMessageFlowItem, "brandmessage"),
    req.NaverTalkMessage: (req.NaverTalkFlowItem, "navertalk"),
}


def with_default_ttl(model: type[RequestModel], payload: dict[str, Any]) -> dict[str, Any]:
    """Return ``payload`` (API field names) with ``idempotencyTtl`` set to :data:`DEFAULT_IDEMPOTENCY_TTL` when
    ``model`` has both fields and the payload has an ``idempotencyKey`` but no ``idempotencyTtl``.

    Never mutates ``payload``: a copy is returned when a value is added.
    """
    if payload.get("idempotencyKey") is None or payload.get("idempotencyTtl") is not None:
        return payload
    names = {info.serialization_alias or name for name, info in model.model_fields.items()}
    if not {"idempotencyKey", "idempotencyTtl"} <= names:
        return payload
    return {**payload, "idempotencyTtl": DEFAULT_IDEMPOTENCY_TTL}


def destinations(to: Recipients) -> list[Any]:
    if isinstance(to, (str, req.Destination, dict)):
        items: Sequence[Recipient] = [to]
    else:
        items = to
    return [req.Destination(to=item) if isinstance(item, str) else item for item in items]


def flow_item(message: Any) -> Any:
    entry = _FLOW_ITEM.get(type(message))
    if entry is None:
        return message  # already a flow item or a dict; SendOmniRequest validates it
    flow_cls, key = entry
    return flow_cls(**{key: message})


def build_send_request(
    *,
    to: Recipients,
    messages: Sequence[Any],
    ref: str | None,
    group_key: str | None,
    payment_code: str | None,
    idempotency_key: str | None,
    idempotency_ttl: int | None,
) -> req.SendOmniRequest:
    if not messages:
        raise ValueError("messages가 비어 있습니다. 채널 메시지를 1개 이상 넣으세요.")
    options = {
        "ref": ref,
        "group_key": group_key,
        "payment_code": payment_code,
        "idempotency_key": idempotency_key,
        "idempotency_ttl": idempotency_ttl,
    }
    return req.SendOmniRequest(
        destinations=destinations(to),
        message_flow=[flow_item(m) for m in messages],
        **{k: v for k, v in options.items() if v is not None},
    )


def yyyymmdd(value: dt.date | str) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dt.datetime):
        value = value.astimezone(KST).date() if value.tzinfo else value.date()
    return value.strftime("%Y%m%d")


def local_time(value: dt.datetime | str) -> str:
    """``yyyy-MM-dd'T'HH:mm:ss`` in KST (send history ``requestTime``)."""
    if isinstance(value, str):
        return value
    if value.tzinfo:
        value = value.astimezone(KST)
    return value.strftime("%Y-%m-%dT%H:%M:%S")


def offset_time(value: dt.datetime | str) -> str:
    """``yyyy-MM-dd'T'HH:mm:ss+09:00`` (MO history ``occurredTime``). Naive datetimes are taken as KST."""
    if isinstance(value, str):
        return value
    if value.tzinfo is None:
        value = value.replace(tzinfo=KST)
    return value.isoformat(timespec="seconds")


def _os_reason(exc: OSError) -> str:
    if isinstance(exc, FileNotFoundError):
        return "파일이 없습니다"
    if isinstance(exc, PermissionError):
        return "권한이 없습니다"
    if isinstance(exc, IsADirectoryError):
        return "디렉터리입니다"
    return type(exc).__name__


def read_file(file: FileInput, filename: str | None, default_name: str = "image.jpg") -> tuple[str, bytes, str]:
    """Return ``(filename, content, content_type)``. The content is read once so retries can resend it."""
    if isinstance(file, (bytes, bytearray, memoryview)):
        content, name = bytes(file), filename or default_name
    elif isinstance(file, (str, os.PathLike)):
        base = os.path.basename(os.fspath(file))
        try:
            with open(file, "rb") as fh:
                content = fh.read()
        except OSError as exc:
            # file name only: the full path can reveal user names and directory layout (SDK-DESIGN.md §12.18)
            raise ValueError(f"업로드 파일을 읽지 못했습니다: {base} ({_os_reason(exc)})") from None
        name = filename or base
    else:
        try:
            content = file.read()
        except OSError as exc:
            base = os.path.basename(str(getattr(file, "name", default_name)))
            raise ValueError(f"업로드 파일을 읽지 못했습니다: {base} ({_os_reason(exc)})") from None
        if not isinstance(content, bytes):
            raise TypeError("파일 객체는 바이너리 모드('rb')로 열어야 합니다")
        name = filename or os.path.basename(str(getattr(file, "name", default_name)))
    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    return name, content, content_type


def compact(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}
