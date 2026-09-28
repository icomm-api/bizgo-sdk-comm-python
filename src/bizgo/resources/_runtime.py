"""Runtime used by the methods generated from the spec (``resources/_generated.py``).

The generated code builds a :class:`Call` (method, path with encoded values, query, body, retry policy) with the
helpers below, sends it through the transport, and picks the ``x-sdk-result`` part of the parsed response.
Validation errors name the parameter, never its value (values can be phone numbers).
"""

from __future__ import annotations

import datetime as dt
import json
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping, Sequence
from typing import Any, TypeVar
from urllib.parse import quote

from pydantic import BaseModel

from .._base import RequestModel
from .._operation import Pagination, Path
from .._transport import Call as Call
from ._common import KST, FileInput, local_time, offset_time, read_file, with_default_ttl, yyyymmdd

M = TypeVar("M", bound=RequestModel)
T = TypeVar("T")


def segment(value: str, name: str = "path") -> str:
    """URL-encode one path segment (``/``, ``?``, ``#``, ``%`` included) so a value can never change the path.

    ``.`` and ``..`` are rejected: URL normalization would turn them into a different path (another operation).
    """
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name}: 빈 값은 경로에 쓸 수 없습니다")
    if value in (".", ".."):
        raise ValueError(f"{name}: '.'과 '..'은 경로 값으로 쓸 수 없습니다")
    return quote(value, safe="")


# ---------------------------------------------------------------- query and header parameters


def check_int(name: str, value: int | None, minimum: int | None = None, maximum: int | None = None) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name}: 정수여야 합니다")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name}: {minimum} 이상이어야 합니다")
    if maximum is not None and value > maximum:
        raise ValueError(f"{name}: {maximum} 이하여야 합니다")
    return value


def check_str(name: str, value: str | None, *, max_length: int | None = None, enum: Sequence[str] = ()) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"{name}: 문자열이어야 합니다")
    if max_length is not None and len(value) > max_length:
        raise ValueError(f"{name}: 최대 {max_length}자입니다")
    if enum and value not in enum:
        raise ValueError(f"{name}: 허용되는 값은 {', '.join(enum)}입니다")
    return value


def check_bool(name: str, value: bool | None) -> str | None:
    if value is None:
        return None
    if not isinstance(value, bool):
        raise ValueError(f"{name}: True/False여야 합니다")
    return "true" if value else "false"


def array(name: str, value: str | Sequence[str] | None, *, explode: bool, min_items: int = 0) -> Any:
    """A query array: comma-separated (``explode: false``) or repeated (``explode: true``)."""
    if value is None:
        return None
    items = [value] if isinstance(value, str) else list(value)
    if not all(isinstance(item, str) for item in items):
        raise ValueError(f"{name}: 문자열 목록이어야 합니다")
    if len(items) < min_items:
        raise ValueError(f"{name}: {min_items}개 이상 넣으세요")
    return items if explode else ",".join(items)


def date_param(name: str, value: dt.date | str | None) -> str | None:
    """``yyyyMMdd`` (a datetime with a time zone is converted to the KST date)."""
    return None if value is None else yyyymmdd(value)


def datetime_param(name: str, value: dt.datetime | str | None, fmt: str) -> str | None:
    """Format a datetime for the documented ``x-format``. Aware datetimes are converted to KST; strings pass as is."""
    if value is None or isinstance(value, str):
        return value
    if fmt == "yyyy-MM-dd'T'HH:mm:ssXXX":
        return offset_time(value)
    if fmt == "yyyy-MM-dd'T'HH:mm:ss":
        return local_time(value)
    if value.tzinfo:
        value = value.astimezone(KST)
    if fmt == "yyyy-MM-dd HH:mm:ss":
        return value.strftime("%Y-%m-%d %H:%M:%S")
    if fmt == "yyyyMMddHHmmss":
        return value.strftime("%Y%m%d%H%M%S")
    raise ValueError(f"{name}: 지원하지 않는 형식입니다 ({fmt})")


def need(name: str, value: T | None) -> T:
    """A required value: ``None`` is rejected before anything is sent."""
    if value is None:
        raise ValueError(f"{name}: 필수 값입니다")
    return value


def query(values: dict[str, Any]) -> dict[str, Any] | None:
    out = {k: v for k, v in values.items() if v is not None}
    return out or None


def header(name: str, value: str) -> str:
    """A header parameter value: printable ASCII only (no CR/LF/NUL or other control characters)."""
    if not isinstance(value, str) or not value or not all(" " <= c <= "~" for c in value):
        raise ValueError(f"{name}: 비어 있지 않은 한 줄 ASCII 문자열이어야 합니다")
    return value


# ---------------------------------------------------------------- bodies


def json_body(model: type[M], body: M | Mapping[str, Any]) -> dict[str, Any]:
    """Validate a request body (a model, or a dict with API or Python field names) and serialize it.

    If the body has ``idempotencyKey`` but no ``idempotencyTtl``, ``DEFAULT_IDEMPOTENCY_TTL`` (86400) is added to
    the serialized copy (the caller's model or dict is not changed).
    """
    value = body if isinstance(body, model) else model.model_validate(dict(body))
    return with_default_ttl(model, value.to_api())


class Form:
    """Builder for a multipart/form-data body. Files are read once so retries resend the same bytes."""

    def __init__(self) -> None:
        self.files: list[tuple[str, tuple[str | None, bytes, str]]] = []
        self.data: dict[str, str] = {}

    def file(
        self,
        name: str,
        value: FileInput | None,
        filename: str | None,
        default_name: str,
        *,
        max_bytes: int | None = None,
    ) -> None:
        if value is None:
            return
        fname, content, content_type = read_file(value, filename, default_name)
        if max_bytes is not None and len(content) > max_bytes:
            raise ValueError(f"{name}: 파일은 최대 {max_bytes:,}byte입니다")
        self.files.append((name, (fname, content, content_type)))

    def files_of(self, name: str, values: Sequence[FileInput] | None, default_name: str, max_items: int | None) -> None:
        if values is None:
            return
        if isinstance(values, (str, bytes)) or not isinstance(values, Sequence):
            raise ValueError(f"{name}: 파일 목록이어야 합니다")
        if max_items is not None and len(values) > max_items:
            raise ValueError(f"{name}: 최대 {max_items}개입니다")
        for value in values:
            self.file(name, value, None, default_name)

    def json(self, name: str, model: type[M], value: M | Mapping[str, Any] | None) -> None:
        """A JSON part (``encoding: {<name>: {contentType: application/json}}``)."""
        if value is None:
            return
        payload = json.dumps(json_body(model, value), ensure_ascii=False).encode("utf-8")
        self.files.append((name, (None, payload, "application/json")))

    def text(self, name: str, value: str | None) -> None:
        if value is not None:
            self.data[name] = value

    def call_kwargs(self) -> dict[str, Any]:
        return {"files": self.files or None, "data": self.data or None}


# ---------------------------------------------------------------- responses


def _field(model: BaseModel, name: str) -> Any:
    for attr, info in type(model).model_fields.items():
        if name in (attr, info.validation_alias, info.serialization_alias, info.alias):
            return getattr(model, attr)
    extra = model.model_extra or {}
    return extra.get(name)


def pick(value: Any, path: Path) -> Any:
    """Read the part of a parsed response at ``path`` (API names; ``-1`` is the last list item)."""
    node = value
    for step in path:
        if node is None:
            return None
        if isinstance(step, int):
            if not isinstance(node, list) or not node:
                return None
            node = node[step] if -len(node) <= step < len(node) else None
        elif isinstance(node, BaseModel):
            node = _field(node, step)
        elif isinstance(node, dict):
            node = node.get(step)
        else:
            return None
    return node


def pick_list(value: Any, path: Path) -> list[Any]:
    found = pick(value, path)
    return list(found) if isinstance(found, list) else []


# ---------------------------------------------------------------- pagination


def _start(pagination: Pagination, start: int | None) -> Any:
    if pagination.style == "cursor":
        return None
    if start is not None:
        return start
    return 1 if pagination.style == "page" else 0


def _advance(pagination: Pagination, page: Any, position: Any, size: int | None, seen: int) -> tuple[bool, Any]:
    """Return ``(more, next position)`` after one page."""
    items = pick_list(page, pagination.items)
    if pagination.style == "cursor":
        cursor = pick(page, pagination.cursor or ())
        has_next = pick(page, pagination.has_next) if pagination.has_next else bool(items)
        if not has_next or cursor is None or cursor == position:
            return False, position
        return True, cursor
    if not items or (size is not None and len(items) < size):
        return False, position
    if pagination.has_next is not None and pick(page, pagination.has_next) is False:
        return False, position
    if pagination.total is not None:
        total = pick(page, pagination.total)
        if isinstance(total, str) and total.isdigit():
            total = int(total)
        if isinstance(total, int) and not isinstance(total, bool) and seen >= total:
            return False, position
    return True, position + 1 if pagination.style == "page" else position + len(items)


def iterate(
    fetch: Callable[[Any], Any], pagination: Pagination, *, size: int | None = None, start: int | None = None
) -> Iterator[Any]:
    """Walk every page. Cursor: stop when ``hasNext`` is false, the cursor is missing or does not move.
    Page/offset: stop on an empty or short page, ``hasNext`` false, or when ``total`` items were seen."""
    position = _start(pagination, start)
    seen = 0
    while True:
        page = fetch(position)
        items = pick_list(page, pagination.items)
        seen += len(items)
        yield from items
        more, position = _advance(pagination, page, position, size, seen)
        if not more:
            return


async def aiterate(
    fetch: Callable[[Any], Awaitable[Any]],
    pagination: Pagination,
    *,
    size: int | None = None,
    start: int | None = None,
) -> AsyncIterator[Any]:
    """Async version of :func:`iterate`."""
    position = _start(pagination, start)
    seen = 0
    while True:
        page = await fetch(position)
        items = pick_list(page, pagination.items)
        seen += len(items)
        for item in items:
            yield item
        more, position = _advance(pagination, page, position, size, seen)
        if not more:
            return
