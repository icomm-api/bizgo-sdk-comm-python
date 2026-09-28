"""Base classes for all generated models."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from pydantic import BaseModel, ConfigDict, model_validator

from ._required_if import violations


def _key(name: str) -> str:
    """``phoneNumber``, ``phone_number`` and ``from_`` all compare as ``phonenumber`` / ``from``."""
    return name.replace("_", "").lower()


PHONE_FIELDS = frozenset(
    _key(n)
    for n in (
        "to",
        "from",
        "phoneNumber",
        "phoneNumbers",
        "originator",
        "callback",
        "callbackNumber",
        "dialPhoneNumber",
        "telNumber",
        "unsubscribePhoneNumber",
    )
)
"""Fields that hold phone numbers: masked in ``repr``/``str`` (SDK-DESIGN.md §12.11)."""
PERSON_FIELDS = frozenset(_key(n) for n in ("userName", "nickname", "nickName", "email", "userEmail"))
"""Fields that identify a person: masked like phone numbers."""
CONTENT_FIELDS = frozenset(_key(n) for n in ("content", "contents", "text", "message"))
"""Free-text fields (message bodies, MO / counsel content): only their length is shown in ``repr``."""


def mask_phone(value: Any) -> Any:
    """Mask the middle of a phone number (or other identifier); lists are masked item by item.

    - 11+ characters: first 3 and last 4 kept (``01000000000`` -> ``010****0000``)
    - 8-10 characters: first 3 kept and at least half masked (``15880000`` -> ``158****0``)
    - 7 or fewer: everything masked
    """
    if isinstance(value, (list, tuple)):
        return [mask_phone(item) for item in value]
    if not isinstance(value, str):
        return value
    size = len(value)
    if size <= 7:
        return "*" * size
    if size <= 10:
        hidden = (size + 1) // 2
        tail = size - 3 - hidden
        return value[:3] + "*" * hidden + value[size - tail :]
    return value[:3] + "*" * (size - 7) + value[-4:]


class _Length:
    def __init__(self, value: Any) -> None:
        self._text = f"<{len(value)} {'chars' if isinstance(value, str) else 'items'}>"

    def __repr__(self) -> str:
        return self._text


def mask_value(name: str | None, value: Any) -> Any:
    """What ``repr`` shows for a field called ``name`` (API or Python name)."""
    if value is None or not name:
        return value
    key = _key(name)
    if key in PHONE_FIELDS or key in PERSON_FIELDS:
        return mask_phone(value)
    if key in CONTENT_FIELDS and isinstance(value, (str, list)):
        return _Length(value)
    return value


def masked_repr(obj: object, fields: dict[str, Any]) -> str:
    """``Name(field=value, ...)`` with the masking rules applied; for plain params/options objects."""
    inner = ", ".join(f"{name}={mask_value(name, value)!r}" for name, value in fields.items())
    return f"{type(obj).__name__}({inner})"


def _masked_repr_args(model: BaseModel, args: Iterator[tuple[str | None, Any]]) -> Iterator[tuple[str | None, Any]]:
    fields = type(model).model_fields
    for name, value in args:
        field = fields.get(name) if name else None
        api = (field.serialization_alias or field.alias or name) if field else name
        yield name, mask_value(api, mask_value(name, value) if name and value is not None else value)


def byte_length(value: str, charset: str | None) -> int:
    """Return the encoded length of ``value`` the way the carrier counts it.

    For ``EUC-KR`` fields the length is counted with CP949 (a superset of EUC-KR that uses the
    same 2 bytes per Hangul syllable). Characters that CP949 cannot represent, such as emoji,
    raise ``ValueError`` because the carrier rejects them.
    """
    if charset and charset.upper() == "EUC-KR":
        try:
            return len(value.encode("cp949"))
        except UnicodeEncodeError as exc:
            bad = value[exc.start : exc.end]
            raise ValueError(
                f"EUC-KR로 표현할 수 없는 문자가 있습니다: {bad!r} (이모지 등은 문자메시지에 쓸 수 없습니다)"
            ) from None
    return len(value.encode("utf-8"))


class RequestModel(BaseModel):
    """Base for request bodies.

    - Unknown fields are rejected so that typos (for example ``templatecode``) fail fast.
    - Fields marked with ``x-max-bytes`` in the spec are checked by encoded byte length.
    - ``x-sdk-required-if`` rules (fields required depending on another field, such as ``msgType``/``text`` of a
      non-template alimtalk) are checked; a request body checks its whole tree, including ``$.`` paths.
    - Fields can be set by their Python name (``sender_key``) or the API name (``senderKey``).
    """

    model_config = ConfigDict(
        extra="forbid",
        populate_by_name=True,
        use_attribute_docstrings=True,
        # Validation errors must not echo input values: they can contain phone numbers.
        hide_input_in_errors=True,
    )

    @model_validator(mode="after")
    def _check_byte_limits(self) -> RequestModel:
        for name, field in type(self).model_fields.items():
            extra = field.json_schema_extra
            if not isinstance(extra, dict) or "x-max-bytes" not in extra:
                continue
            value = getattr(self, name)
            if not isinstance(value, str):
                continue
            limit = extra["x-max-bytes"]
            charset = extra.get("x-charset")
            size = byte_length(value, charset if isinstance(charset, str) else None)
            if isinstance(limit, int) and size > limit:
                label = field.serialization_alias or field.alias or name
                raise ValueError(f"{label}: 최대 {limit}byte인데 {size}byte입니다")
        return self

    @model_validator(mode="after")
    def _check_required_if(self) -> RequestModel:
        # field paths and the rule's condition only: never input values (SDK-DESIGN.md §4)
        problems = violations(self)
        if problems:
            raise ValueError("; ".join(problems[:20]))
        return self

    def __repr_args__(self) -> Any:
        # phone numbers are masked and free text shortened in repr/str; attribute values are unchanged
        return _masked_repr_args(self, iter(super().__repr_args__()))

    def to_api(self) -> dict[str, Any]:
        """Serialize with API field names. Only fields you set are sent; spec defaults are left to the server."""
        return self.model_dump(mode="json", by_alias=True, exclude_none=True, exclude_unset=True)


class ResponseModel(BaseModel):
    """Base for responses. Unknown fields are kept (``model_extra``) so new server fields never break parsing."""

    model_config = ConfigDict(
        extra="allow", populate_by_name=True, use_attribute_docstrings=True, hide_input_in_errors=True
    )

    def __repr_args__(self) -> Any:
        return _masked_repr_args(self, iter(super().__repr_args__()))
