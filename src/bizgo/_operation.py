"""Metadata of one spec operation. The table itself is generated into :mod:`bizgo._operations`."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Path = tuple[str | int, ...]
"""A path into a response body: API property names, and list indexes (``-1`` is the last item)."""


@dataclass(frozen=True)
class Pagination:
    """``x-sdk-pagination`` of a list operation."""

    style: Literal["cursor", "page", "offset"]
    request: str
    """API name of the query parameter that selects the page (``lastSeq``, ``page``, ``offset``, ...)."""
    items: Path
    size: str | None = None
    """API name of the page size parameter (``limit``, ``count``, ``rows``), for page/offset styles."""
    cursor: Path | None = None
    has_next: Path | None = None
    total: Path | None = None


@dataclass(frozen=True)
class Param:
    """One parameter of a generated method (used by :mod:`bizgo.testing` and the test suite)."""

    api: str
    python: str
    location: Literal["path", "query", "header", "form"]
    required: bool
    kind: str = "text"
    """``text``, ``int``, ``bool``, ``array``, ``date``, ``datetime``, ``file``, ``files`` or ``json``."""


@dataclass(frozen=True)
class Operation:
    id: str
    """``operationId``, for example ``listAlimtalkTemplates``."""
    name: str
    """``<x-sdk-resource>.<x-sdk-method>``, for example ``alimtalk.templates.list``."""
    method: str
    path: str
    """Path template, for example ``/api/comm/v1/report/inquiry/{msgKey}``. Hooks see only this, never real values."""
    retry: Literal["safe", "rate_limit_only"]
    rate: Literal["send", "other"]
    """Client-side token bucket (SDK-DESIGN.md §11.5)."""
    attribute: tuple[str, ...]
    """Python attribute path from the client, for example ``("alimtalk", "templates", "list")``."""
    handwritten: bool = False
    """Implemented by a hand-written convenience method (same attribute path)."""
    body: Literal["json", "form"] | None = None
    params: tuple[Param, ...] = field(default=())
    pagination: Pagination | None = None
    iterator: str | None = None
    """Name of the generated iterator method (``iter_list``) next to the page method."""
