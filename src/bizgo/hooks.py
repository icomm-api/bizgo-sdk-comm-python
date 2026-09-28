"""Observability hooks (SDK-DESIGN.md §11.4).

Example::

    from bizgo import Bizgo
    from bizgo.hooks import Hooks, RequestEvent

    class Metrics(Hooks):
        def on_request_end(self, event: RequestEvent) -> None:
            histogram("bizgo.request", event.duration_ms, op=event.operation_id, status=event.status)

    client = Bizgo(hooks=Metrics())

One API call (including its retries) produces one :meth:`Hooks.on_request_start` and one
:meth:`Hooks.on_request_end`, with the **same** event object. An event carries the operation, the HTTP method,
the **path template** (``/api/comm/v1/report/inquiry/{msgKey}``), the status, the error layer/code/type, the
number of attempts and the duration. It never carries request or response bodies, query strings, header values,
real path values, phone numbers or the API key.

Exceptions raised by a hook are swallowed (logged once per hook class at WARNING, without details) so
observability can never change a result, a retry or a bulk result. Hooks may be ``async def``: the async client
awaits them (errors swallowed too); the sync client cannot await, so it closes the coroutine and warns once. Keep
hooks fast: they run in the calling thread (or event loop).
"""

from __future__ import annotations

import contextlib
import inspect
import logging
import threading
import time
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any, Literal

__all__ = ["Hooks", "RequestEvent"]

logger = logging.getLogger("bizgo")


@dataclass(eq=False)
class RequestEvent:
    """What a hook may see about one API call. Filled in at the end of the call."""

    operation_id: str
    """``operationId`` from the spec, for example ``sendOmni``."""
    operation: str
    """``<resource>.<method>``, for example ``send.omni`` or ``alimtalk.templates.list``."""
    method: str
    """HTTP method."""
    path_template: str
    """Path template. Never the real path values."""
    status: int | None = None
    """HTTP status of the last attempt (``None`` after a network error)."""
    layer: Literal["gateway", "service"] | None = None
    """Set when the call failed with an API error code."""
    code: str | None = None
    """API error code (``A020``, ``A401``, ...) when the call failed with one."""
    error_type: str | None = None
    """Exception class name (``RateLimitError``, ``APITimeoutError``, ...) when the call failed."""
    success: bool = False
    attempts: int = 0
    """HTTP attempts made (1 = no retry)."""
    duration_ms: float | None = None
    """From the first attempt to the end."""
    started: float = field(default_factory=time.monotonic, repr=False)


class Hooks:
    """Subclass and override what you need. Both methods default to doing nothing."""

    def on_request_start(self, event: RequestEvent) -> None:
        """Before the first attempt. Only the operation fields are set."""

    def on_request_end(self, event: RequestEvent) -> None:
        """After the call finished, successfully or not, after all retries."""


def normalize(hooks: Hooks | Sequence[Hooks] | None) -> tuple[Hooks, ...]:
    if hooks is None:
        return ()
    items = (hooks,) if isinstance(hooks, Hooks) else tuple(hooks)
    for item in items:
        if not isinstance(item, Hooks):
            raise TypeError("hooks는 bizgo.hooks.Hooks의 인스턴스(또는 그 목록)여야 합니다")
    return items


_warned: set[str] = set()
_warned_lock = threading.Lock()


def _warn_once(hook: Hooks, name: str, problem: str) -> None:
    key = f"{type(hook).__qualname__}.{name}.{problem}"
    with _warned_lock:
        if key in _warned:
            return
        _warned.add(key)
    with contextlib.suppress(Exception):  # a broken user logging setup must not break the request either
        logger.warning("bizgo hook %s.%s %s; ignored (reported once)", type(hook).__name__, name, problem)


def _call(hook: Hooks, name: Literal["start", "end"], event: RequestEvent) -> Any:
    try:
        if name == "start":
            return hook.on_request_start(event)
        return hook.on_request_end(event)
    except Exception:
        _warn_once(hook, name, "raised")
        return None


def emit(hooks: tuple[Hooks, ...], name: Literal["start", "end"], event: RequestEvent) -> None:
    """Call hooks from the sync client. A coroutine returned by an ``async def`` hook is closed (not awaited)."""
    for hook in hooks:
        result = _call(hook, name, event)
        if inspect.iscoroutine(result):
            result.close()
            _warn_once(hook, name, "is async but the client is sync")


async def emit_async(hooks: tuple[Hooks, ...], name: Literal["start", "end"], event: RequestEvent) -> None:
    """Call hooks from the async client, awaiting ``async def`` hooks. Every error is swallowed."""
    for hook in hooks:
        result = _call(hook, name, event)
        if inspect.isawaitable(result):
            try:
                await result
            except Exception:
                _warn_once(hook, name, "raised")
