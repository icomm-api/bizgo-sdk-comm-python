"""HTTP transport: headers, retries, rate limiting, hooks, envelope parsing and error mapping.

Nothing in this module logs or raises request bodies, header values or query strings,
because they can contain the API key and phone numbers.

Hardening (SDK-DESIGN.md §12):

- Responses are streamed and decoded here (gzip/deflate with a bounded ``zlib``) up to 16MB after decompression;
  larger bodies raise :class:`InvalidResponseError` without being read further. JSON nesting deeper than 64
  levels is rejected.
- Redirects are never followed and the user's ``http_client`` authentication (e.g. ``auth=``) is disabled per
  request, so the API key cannot be replaced or sent to another origin.
- Response model validation errors never escape as ``pydantic.ValidationError``: see :func:`validate`.
"""

from __future__ import annotations

import asyncio
import contextlib
import enum
import json as _json
import logging
import math
import random
import time
import zlib
from dataclasses import dataclass
from typing import Any, TypeVar

import httpx
from pydantic import BaseModel

from . import hooks as _hooks
from ._config import CLIENT_HEADER, ClientConfig, user_agent
from ._errors import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    DuplicateRequestError,
    InvalidResponseError,
    RateLimitError,
    error_class,
)
from ._operations import OPERATIONS
from ._ratelimit import Bucket, RateLimiter, request_cost

logger = logging.getLogger("bizgo")

USER_AGENT = user_agent()
"""Default User-Agent (without app_info)."""
_RETRYABLE_STATUS = {429, 500, 502, 503, 504}
_MAX_BACKOFF = 8.0
_MAX_RETRY_AFTER = 60.0
MAX_RESPONSE_BYTES = 16 * 1024 * 1024
"""Largest response body read, counted after decompression."""
MAX_JSON_DEPTH = 64
"""Deepest JSON nesting accepted in a response."""

JSON = dict[str, Any]
M = TypeVar("M", bound=BaseModel)


class ResponseBody(dict[str, Any]):
    """A parsed JSON response body that also remembers its HTTP status."""

    http_status: int | None = None


class Retry(enum.Enum):
    """Which failures may be retried for a request."""

    SAFE = "safe"
    """Read-only or idempotent calls: retry on 429, 5xx and connection errors."""
    RATE_LIMIT_ONLY = "rate_limit_only"
    """Calls that could create a duplicate (send without idempotency key, uploads): retry only on 429,
    which the gateway returns before the request is processed."""


def _retry_after(headers: httpx.Headers) -> float | None:
    """``Retry-After`` in seconds: a finite number >= 0 (max 60). Anything else is ignored."""
    value = headers.get("retry-after")
    if value is None:
        return None
    try:
        seconds = float(value)
    except ValueError:
        return None
    if not math.isfinite(seconds) or seconds < 0:
        return None
    return min(seconds, _MAX_RETRY_AFTER)


def _backoff(attempt: int, retry_after: float | None) -> float:
    if retry_after is not None:
        return retry_after
    base = min(0.5 * float(2**attempt), _MAX_BACKOFF)
    return base * random.uniform(0.75, 1.25)  # noqa: S311 - jitter, not crypto


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
        if depth > MAX_JSON_DEPTH:
            return True
        stack.extend((child, depth + 1) for child in children if isinstance(child, (dict, list)))
    return False


def _decode(status: int, raw: bytes) -> Any:
    """Parse JSON, or return ``None`` if the body is not JSON. Deep nesting raises."""
    try:
        value = _json.loads(raw)
    except RecursionError:
        raise InvalidResponseError("응답 JSON의 중첩이 너무 깊습니다", http_status=status) from None
    except ValueError:  # includes UnicodeDecodeError
        return None
    if _too_deep(value):
        raise InvalidResponseError(f"응답 JSON의 중첩이 너무 깊습니다(최대 {MAX_JSON_DEPTH})", http_status=status)
    return value


def _parse(status: int, headers: httpx.Headers, raw: bytes) -> ResponseBody:
    """Return the JSON body, or raise the matching :class:`APIError` / :class:`InvalidResponseError`."""
    if 300 <= status < 400:
        raise InvalidResponseError(
            f"리다이렉트(HTTP {status})는 따르지 않습니다. base_url이 올바른지 확인하세요.", http_status=status
        )
    body = _decode(status, raw)
    if not isinstance(body, dict):
        if status >= 400:
            cls = error_class(status, None, "gateway")
            raise cls(f"응답 본문이 JSON이 아닙니다 (HTTP {status})", http_status=status, code=None, layer="gateway")
        raise InvalidResponseError(f"응답 본문이 JSON 객체가 아닙니다 (HTTP {status})", http_status=status)

    raw_common = body.get("common")
    raw_data = body.get("data")
    common: JSON = raw_common if isinstance(raw_common, dict) else {}
    data: JSON | None = raw_data if isinstance(raw_data, dict) else None
    tracking = common.get("infobankTrId")
    tracking_id = tracking if isinstance(tracking, str) else None
    auth_code = common.get("authCode")
    service_code = data.get("code") if data else None

    if auth_code not in (None, "A000"):
        _raise(status, headers, body, str(auth_code), str(common.get("authResult") or ""), "gateway", tracking_id)
    if service_code not in (None, "A000"):
        message = str(data.get("result") or "") if data else ""
        _raise(status, headers, body, str(service_code), message, "service", tracking_id)
    if status >= 400:
        _raise(status, headers, body, None, "요청이 실패했습니다", "gateway", tracking_id)
    if not isinstance(raw_common, dict) and data is None:
        raise InvalidResponseError(
            "응답이 문서의 {common, data} 형식이 아닙니다", http_status=status, tracking_id=tracking_id, body=body
        )
    out = ResponseBody(body)
    out.http_status = status
    return out


def _raise(
    status: int,
    headers: httpx.Headers,
    body: JSON,
    code: str | None,
    message: str,
    layer: Any,
    tracking_id: str | None,
) -> None:
    cls = error_class(status, code, layer)
    kwargs: dict[str, Any] = {
        "http_status": status,
        "code": code,
        "layer": layer,
        "tracking_id": tracking_id,
        "body": body,
    }
    if cls is RateLimitError:
        raise RateLimitError(message, retry_after=_retry_after(headers), **kwargs)
    raise cls(message, **kwargs)


def validate(model: type[M], body: JSON, operation: str) -> M:
    """Validate a response body; errors become :class:`InvalidResponseError` (never ``pydantic.ValidationError``).

    For send operations the message says the request may have been accepted.
    """
    try:
        return model.model_validate(body)
    except (ValueError, TypeError, RecursionError):  # pydantic.ValidationError is a ValueError
        op = OPERATIONS.get(operation)
        if op is not None and op.rate == "send":
            note = " 요청은 접수됐을 수 있으니 다시 보내기 전에 상태 조회로 확인하세요."
        elif op is not None and op.method != "GET":
            note = " 요청은 처리됐을 수 있으니 다시 보내기 전에 조회로 확인하세요."
        else:
            note = ""
        common = body.get("common") if isinstance(body, dict) else None
        tracking = common.get("infobankTrId") if isinstance(common, dict) else None
        raise InvalidResponseError(
            f"응답을 해석하지 못했습니다(필드 형식이 문서와 다름: {model.__name__}).{note}",
            http_status=getattr(body, "http_status", None),
            tracking_id=tracking if isinstance(tracking, str) else None,
            body=body,
        ) from None


def _should_retry(policy: Retry, *, status: int | None, connection_error: bool) -> bool:
    if status == 429:
        return True
    if policy is Retry.RATE_LIMIT_ONLY:
        return False
    return connection_error or (status in _RETRYABLE_STATUS)


def _log(method: str, path: str, status: int | str, started: float, attempt: int) -> None:
    # a broken user logger/filter must never affect results or retries (SDK-DESIGN.md §12.15)
    with contextlib.suppress(Exception):
        if logger.isEnabledFor(logging.DEBUG):
            # path only: query strings can carry phone numbers (e.g. MO history filters)
            elapsed = (time.monotonic() - started) * 1000
            logger.debug("%s %s -> %s (%.0f ms, attempt %d)", method, path, status, elapsed, attempt + 1)


_PROTECTED = frozenset({"authorization", "user-agent", "x-bizgo-client", "accept", "accept-encoding"})


def _headers(config: ClientConfig) -> dict[str, str]:
    return {
        "Authorization": config.api_key,
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",  # only what _BoundedDecoder can decode with a size limit
        "User-Agent": config.user_agent,
        "X-Bizgo-Client": CLIENT_HEADER,
    }


def _connection_error(exc: httpx.TransportError) -> APIConnectionError:
    if isinstance(exc, httpx.TimeoutException):
        return APITimeoutError(f"요청 시간이 초과됐습니다 ({type(exc).__name__})")
    return APIConnectionError(f"서버에 연결하지 못했습니다 ({type(exc).__name__})")


def _after_retry(error: APIError, retried: bool) -> APIError:
    """A301 on a retried request: an earlier attempt of the same call was most likely accepted."""
    if isinstance(error, DuplicateRequestError) and retried:
        error.already_accepted = True
        error.message = (
            "이전 시도가 이미 접수된 것으로 보입니다(같은 idempotencyKey로 재시도). 메시지는 다시 발송되지 않았으며, "
            "접수 결과는 상태 조회 API로 확인하세요."
        )
    return error


class _BoundedDecoder:
    """Decode ``Content-Encoding`` (identity, gzip, deflate) without ever producing more than the size limit.

    Every ``decompress`` call is bounded, so a small compressed chunk cannot expand to gigabytes in memory.
    """

    def __init__(self, status: int, encoding: str) -> None:
        self._status = status
        self._buffer = bytearray()
        encoding = encoding.strip().lower()
        self._raw_deflate = False
        if encoding in ("", "identity"):
            self._zlib: Any = None
        elif encoding in ("gzip", "x-gzip"):
            self._zlib = zlib.decompressobj(16 + zlib.MAX_WBITS)
        elif encoding == "deflate":
            self._zlib = zlib.decompressobj(zlib.MAX_WBITS)
            self._raw_deflate = True  # may need to fall back to raw deflate on the first chunk
        else:
            raise InvalidResponseError(f"지원하지 않는 응답 압축 방식입니다: {encoding[:20]}", http_status=status)

    def _add(self, data: bytes) -> None:
        self._buffer += data
        if len(self._buffer) > MAX_RESPONSE_BYTES:
            raise _too_large(self._status)

    def _inflate(self, chunk: bytes) -> None:
        data = chunk
        while data:
            room = MAX_RESPONSE_BYTES - len(self._buffer) + 1
            out = self._zlib.decompress(data, room)
            self._add(out)
            data = self._zlib.unconsumed_tail

    def feed(self, chunk: bytes) -> None:
        if self._zlib is None:
            self._add(chunk)
            return
        try:
            self._inflate(chunk)
        except zlib.error:
            if not (self._raw_deflate and not self._buffer):
                raise InvalidResponseError("응답 압축을 풀지 못했습니다", http_status=self._status) from None
            self._zlib = zlib.decompressobj(-zlib.MAX_WBITS)
            self._raw_deflate = False
            try:
                self._inflate(chunk)
            except zlib.error:
                raise InvalidResponseError("응답 압축을 풀지 못했습니다", http_status=self._status) from None
        self._raw_deflate = False

    def finish(self) -> bytes:
        if self._zlib is not None:
            try:
                self._add(self._zlib.flush(MAX_RESPONSE_BYTES - len(self._buffer) + 1))
            except zlib.error:
                raise InvalidResponseError("응답 압축을 풀지 못했습니다", http_status=self._status) from None
        return bytes(self._buffer)


def _too_large(status: int) -> InvalidResponseError:
    return InvalidResponseError(
        f"응답이 너무 큽니다(압축 해제 후 {MAX_RESPONSE_BYTES // (1024 * 1024)}MB 초과)", http_status=status
    )


@dataclass(frozen=True)
class Call:
    """One HTTP request of a generated method."""

    operation: str
    method: str
    path: str
    retry: Retry
    params: dict[str, Any] | None = None
    json: dict[str, Any] | None = None
    files: list[tuple[str, tuple[str | None, bytes, str]]] | None = None
    data: dict[str, str] | None = None
    headers: dict[str, str] | None = None

    def __repr__(self) -> str:  # never show values
        return f"Call({self.method} {self.operation})"


def _event(operation: str, method: str) -> _hooks.RequestEvent:
    op = OPERATIONS[operation]
    return _hooks.RequestEvent(operation_id=op.id, operation=op.name, method=method, path_template=op.path)


def _finish(event: _hooks.RequestEvent, error: BaseException | None) -> None:
    event.duration_ms = (time.monotonic() - event.started) * 1000
    event.success = error is None
    if isinstance(error, APIError):
        event.status, event.layer, event.code = error.http_status, error.layer, error.code
    if error is not None:
        event.error_type = type(error).__name__


class _Base:
    def __init__(self, config: ClientConfig, limiter: RateLimiter | None, hooks: tuple[_hooks.Hooks, ...]) -> None:
        self._config = config
        self._limiter = limiter
        self._hooks = hooks

    def _headers(self, extra: dict[str, str] | None) -> dict[str, str]:
        # request-level headers win over an http_client's default headers, and operation header parameters can
        # never replace Authorization, User-Agent or X-Bizgo-Client (SDK-DESIGN.md §2.1)
        headers = {k: v for k, v in (extra or {}).items() if k.lower() not in _PROTECTED}
        headers.update(_headers(self._config))
        return headers


class SyncTransport(_Base):
    def __init__(
        self,
        config: ClientConfig,
        http_client: httpx.Client | None = None,
        *,
        limiter: RateLimiter | None = None,
        hooks: tuple[_hooks.Hooks, ...] = (),
        owns_client: bool = False,
    ) -> None:
        super().__init__(config, limiter, hooks)
        self._owns_client = owns_client or http_client is None
        self._client = http_client or httpx.Client(timeout=config.timeout)

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    def call(self, call: Call) -> JSON:
        return self.request(
            call.method,
            call.path,
            retry=call.retry,
            operation=call.operation,
            params=call.params,
            json=call.json,
            files=call.files,
            data=call.data,
            headers=call.headers,
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        retry: Retry,
        operation: str,
        params: dict[str, Any] | None = None,
        json: JSON | None = None,
        files: Any = None,
        data: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
    ) -> JSON:
        event = _event(operation, method)
        _hooks.emit(self._hooks, "start", event)
        error: BaseException | None = None
        try:
            return self._send(event, method, path, retry, params, json, files, data, headers)
        except BaseException as exc:
            error = exc
            raise
        finally:
            _finish(event, error)
            _hooks.emit(self._hooks, "end", event)

    def _exchange(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None,
        json: JSON | None,
        files: Any,
        data: dict[str, str] | None,
        headers: dict[str, str] | None,
    ) -> tuple[int, httpx.Headers, bytes]:
        request = self._client.build_request(
            method, url, params=params, json=json, files=files, data=data, headers=self._headers(headers)
        )
        # auth=None: the http_client's own auth (e.g. Basic) must not replace the API key; never follow redirects
        response = self._client.send(request, stream=True, auth=None, follow_redirects=False)
        try:
            if response.is_stream_consumed:  # an in-memory response (mock transports): already read and decoded
                decoder = _BoundedDecoder(response.status_code, "identity")
                decoder.feed(response.content)
            else:
                decoder = _BoundedDecoder(response.status_code, response.headers.get("content-encoding", ""))
                for chunk in response.iter_raw():
                    decoder.feed(chunk)
            return response.status_code, response.headers, decoder.finish()
        finally:
            response.close()

    def _send(
        self,
        event: _hooks.RequestEvent,
        method: str,
        path: str,
        retry: Retry,
        params: dict[str, Any] | None,
        json: JSON | None,
        files: Any,
        data: dict[str, str] | None,
        headers: dict[str, str] | None,
    ) -> JSON:
        url = self._config.base_url + path
        bucket: Bucket = OPERATIONS[event.operation_id].rate
        cost = request_cost(bucket, json)
        for attempt in range(self._config.max_retries + 1):
            if self._limiter is not None:
                self._limiter.wait(bucket, cost)
            started = time.monotonic()
            last = attempt == self._config.max_retries
            event.attempts = attempt + 1
            try:
                status, response_headers, raw = self._exchange(method, url, params, json, files, data, headers)
            except httpx.TransportError as exc:
                _log(method, path, type(exc).__name__, started, attempt)
                event.status = None
                if last or not _should_retry(retry, status=None, connection_error=True):
                    raise _connection_error(exc) from None
                time.sleep(_backoff(attempt, None))
                continue
            _log(method, path, status, started, attempt)
            event.status = status
            if not last and _should_retry(retry, status=status, connection_error=False):
                time.sleep(_backoff(attempt, _retry_after(response_headers)))
                continue
            try:
                return _parse(status, response_headers, raw)
            except APIError as error:
                raise _after_retry(error, attempt > 0) from None
        raise AssertionError("unreachable")  # pragma: no cover


class AsyncTransport(_Base):
    def __init__(
        self,
        config: ClientConfig,
        http_client: httpx.AsyncClient | None = None,
        *,
        limiter: RateLimiter | None = None,
        hooks: tuple[_hooks.Hooks, ...] = (),
        owns_client: bool = False,
    ) -> None:
        super().__init__(config, limiter, hooks)
        self._owns_client = owns_client or http_client is None
        self._client = http_client or httpx.AsyncClient(timeout=config.timeout)

    async def close(self) -> None:
        if self._owns_client:
            await self._client.aclose()

    async def call(self, call: Call) -> JSON:
        return await self.request(
            call.method,
            call.path,
            retry=call.retry,
            operation=call.operation,
            params=call.params,
            json=call.json,
            files=call.files,
            data=call.data,
            headers=call.headers,
        )

    async def request(
        self,
        method: str,
        path: str,
        *,
        retry: Retry,
        operation: str,
        params: dict[str, Any] | None = None,
        json: JSON | None = None,
        files: Any = None,
        data: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
    ) -> JSON:
        event = _event(operation, method)
        await _hooks.emit_async(self._hooks, "start", event)
        error: BaseException | None = None
        try:
            return await self._send(event, method, path, retry, params, json, files, data, headers)
        except BaseException as exc:
            error = exc
            raise
        finally:
            _finish(event, error)
            await _hooks.emit_async(self._hooks, "end", event)

    async def _exchange(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None,
        json: JSON | None,
        files: Any,
        data: dict[str, str] | None,
        headers: dict[str, str] | None,
    ) -> tuple[int, httpx.Headers, bytes]:
        request = self._client.build_request(
            method, url, params=params, json=json, files=files, data=data, headers=self._headers(headers)
        )
        response = await self._client.send(request, stream=True, auth=None, follow_redirects=False)
        try:
            if response.is_stream_consumed:  # an in-memory response (mock transports): already read and decoded
                decoder = _BoundedDecoder(response.status_code, "identity")
                decoder.feed(response.content)
            else:
                decoder = _BoundedDecoder(response.status_code, response.headers.get("content-encoding", ""))
                async for chunk in response.aiter_raw():
                    decoder.feed(chunk)
            return response.status_code, response.headers, decoder.finish()
        finally:
            await response.aclose()

    async def _send(
        self,
        event: _hooks.RequestEvent,
        method: str,
        path: str,
        retry: Retry,
        params: dict[str, Any] | None,
        json: JSON | None,
        files: Any,
        data: dict[str, str] | None,
        headers: dict[str, str] | None,
    ) -> JSON:
        url = self._config.base_url + path
        bucket: Bucket = OPERATIONS[event.operation_id].rate
        cost = request_cost(bucket, json)
        for attempt in range(self._config.max_retries + 1):
            if self._limiter is not None:
                await self._limiter.await_(bucket, cost)
            started = time.monotonic()
            last = attempt == self._config.max_retries
            event.attempts = attempt + 1
            try:
                status, response_headers, raw = await self._exchange(method, url, params, json, files, data, headers)
            except httpx.TransportError as exc:
                _log(method, path, type(exc).__name__, started, attempt)
                event.status = None
                if last or not _should_retry(retry, status=None, connection_error=True):
                    raise _connection_error(exc) from None
                await asyncio.sleep(_backoff(attempt, None))
                continue
            _log(method, path, status, started, attempt)
            event.status = status
            if not last and _should_retry(retry, status=status, connection_error=False):
                await asyncio.sleep(_backoff(attempt, _retry_after(response_headers)))
                continue
            try:
                return _parse(status, response_headers, raw)
            except APIError as error:
                raise _after_retry(error, attempt > 0) from None
        raise AssertionError("unreachable")  # pragma: no cover
