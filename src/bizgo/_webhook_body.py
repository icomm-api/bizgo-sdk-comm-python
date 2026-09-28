"""Webhook body loading shared by the hand-written and generated webhook parsers.

Every problem with the body (not JSON, too large, too deeply nested, not an object, fields of the wrong shape)
raises :class:`~bizgo.WebhookPayloadError` (a :class:`~bizgo.WebhookVerificationError`), so a handler that answers
``WebhookVerificationError`` with 4xx never crashes with 500. Messages never contain the body.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any, TypeVar

from pydantic import BaseModel

from ._errors import WebhookPayloadError

MAX_BODY_BYTES = 1024 * 1024
MAX_DEPTH = 64  # same as responses (SDK-DESIGN 12.8)
M = TypeVar("M", bound=BaseModel)


def as_bytes(value: str | bytes) -> bytes:
    return value if isinstance(value, bytes) else value.encode("utf-8")


def _too_deep(value: Any) -> bool:
    stack: list[tuple[Any, int]] = [(value, 1)]
    while stack:
        node, depth = stack.pop()
        if isinstance(node, dict):
            children: Any = node.values()
        elif isinstance(node, list):
            children = node
        else:
            continue
        if depth > MAX_DEPTH:
            return True
        stack.extend((child, depth + 1) for child in children if isinstance(child, (dict, list)))
    return False


def load_body(body: bytes | str | Mapping[str, Any]) -> dict[str, Any]:
    """Parse a webhook body (max 1MB, max nesting depth 32, must be a JSON object)."""
    if isinstance(body, Mapping):
        value: Any = dict(body)
    elif isinstance(body, (bytes, str)):
        raw = as_bytes(body)
        if len(raw) > MAX_BODY_BYTES:
            raise WebhookPayloadError("웹훅 본문이 너무 큽니다")
        try:
            value = json.loads(raw)
        except RecursionError:
            raise WebhookPayloadError("웹훅 본문 JSON의 중첩이 너무 깊습니다") from None
        except ValueError:
            raise WebhookPayloadError("웹훅 본문이 JSON이 아닙니다") from None
    else:
        raise WebhookPayloadError("웹훅 본문은 bytes, str 또는 dict여야 합니다")
    if not isinstance(value, dict):
        raise WebhookPayloadError("웹훅 본문이 JSON 객체가 아닙니다")
    if _too_deep(value):
        raise WebhookPayloadError(f"웹훅 본문 JSON의 중첩이 너무 깊습니다(최대 {MAX_DEPTH})")
    return value


def parse_payload(model: type[M], body: bytes | str | Mapping[str, Any]) -> M:
    """Load and validate a webhook body. Field errors become :class:`~bizgo.WebhookPayloadError`."""
    value = load_body(body)
    try:
        return model.model_validate(value)
    except (ValueError, TypeError, RecursionError):  # pydantic.ValidationError is a ValueError
        raise WebhookPayloadError(f"웹훅 본문의 필드가 문서와 다릅니다({model.__name__})") from None
