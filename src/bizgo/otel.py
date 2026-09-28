"""OpenTelemetry tracing for the SDK, built on :mod:`bizgo.hooks` (optional extra).

Install with ``pip install "bizgo-sdk-comm[otel]"`` (adds ``opentelemetry-api``) and configure an OpenTelemetry
SDK/exporter as usual. The core package never imports this module, so it has no OpenTelemetry dependency.

Example::

    from bizgo import Bizgo
    from bizgo.otel import OpenTelemetryHooks

    client = Bizgo(hooks=OpenTelemetryHooks())

One client span per API call (retries included): name ``bizgo <resource>.<method>`` (for example
``bizgo send.omni``), attributes ``http.request.method``, ``url.template``, ``bizgo.operation_id``,
``http.response.status_code``, ``bizgo.code``, ``bizgo.layer``, ``bizgo.retry_count`` and ``error.type``. Spans never
carry bodies, query strings, header values, real path values, phone numbers or the API key; error messages are
not copied into spans either.
"""

from __future__ import annotations

from typing import Any

from ._version import __version__
from .hooks import Hooks, RequestEvent

try:
    from opentelemetry import trace
    from opentelemetry.trace import SpanKind, Status, StatusCode
except ImportError as exc:  # pragma: no cover - exercised only without the extra
    raise ImportError('bizgo.otel에는 opentelemetry-api가 필요합니다: pip install "bizgo-sdk-comm[otel]"') from exc

__all__ = ["OpenTelemetryHooks"]


class OpenTelemetryHooks(Hooks):
    """Hooks that record one span per Bizgo API call.

    Args:
        tracer: Tracer to use (default ``trace.get_tracer("bizgo-sdk-comm", <version>)`` from the global provider).
    """

    def __init__(self, tracer: Any = None) -> None:
        self._tracer = tracer if tracer is not None else trace.get_tracer("bizgo-sdk-comm", __version__)
        self._spans: dict[int, Any] = {}

    def on_request_start(self, event: RequestEvent) -> None:
        span = self._tracer.start_span(
            f"bizgo {event.operation}",
            kind=SpanKind.CLIENT,
            attributes={
                "http.request.method": event.method,
                "url.template": event.path_template,
                "bizgo.operation_id": event.operation_id,
            },
        )
        self._spans[id(event)] = span

    def on_request_end(self, event: RequestEvent) -> None:
        span = self._spans.pop(id(event), None)
        if span is None:
            return
        if event.status is not None:
            span.set_attribute("http.response.status_code", event.status)
        if event.code is not None:
            span.set_attribute("bizgo.code", event.code)
        if event.layer is not None:
            span.set_attribute("bizgo.layer", event.layer)
        span.set_attribute("bizgo.retry_count", max(0, event.attempts - 1))
        if event.success:
            span.set_status(Status(StatusCode.OK))
        else:
            span.set_attribute("error.type", event.error_type or "error")
            span.set_status(Status(StatusCode.ERROR, event.error_type or "error"))
        span.end()
