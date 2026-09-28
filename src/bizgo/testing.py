"""Test your own code against the SDK without a network or an API key (SDK-DESIGN.md §11.3).

Example::

    from bizgo import RateLimitError
    from bizgo.testing import FakeTransport, sign_webhook

    fake = FakeTransport()
    client = fake.client()          # placeholder key, sandbox URL, no rate limit, never connects

    client.send.sms(to="01000000000", from_="01000000000", text="hello")   # default: every recipient A000
    fake.last_request.operation_id  # "sendOmni"
    fake.last_request.json          # the JSON body that would have been sent

    fake.on("sendOmni").fail("service", 200, "A020")      # next call: RateLimitError
    fake.on("sendOmni").send_result("A000", "A306")       # then: the second recipient is rejected
    fake.on("sendOmni").duplicates()                      # then: every recipient A301 (result.duplicates)
    fake.on("GET", "/api/comm/v1/report/inquiry/{msgKey}").data({"report": []})

    headers, body = sign_webhook("test-webhook-secret", {"msgKey": "KEY001"})  # for WebhookReceiver tests

Every request is recorded with its operation, method, path, query and JSON body (or multipart field names and
file sizes). Header **values**, including the API key, are never recorded. Without a stub an operation answers
with a success envelope: sends (``sendOmni``, ``createReservation``, ``addReservationRecipients``) accept every
recipient with a fake ``msgKey`` (``createReservation`` also returns a fake ``resvKey``); MMS/RCS uploads return a
fake ``fileKey``/``media``; other operations return ``data.data = {}`` (empty lists, no next page). An unknown
path answers HTTP 404 (gateway ``A404``).

This module is for tests only. It uses nothing beyond the SDK's own dependencies, and production code never needs
to import it.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import re
import threading
import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from email.message import Message
from email.parser import BytesParser
from email.policy import HTTP
from typing import Any, Literal, NamedTuple

import httpx

from ._client import AsyncBizgo, Bizgo
from ._config import Environment
from ._operation import Operation
from ._operations import OPERATIONS

__all__ = [
    "FAKE_API_KEY",
    "FakeTransport",
    "RecordedFile",
    "RecordedRequest",
    "SignedWebhook",
    "Stub",
    "error_envelope",
    "sign_webhook",
    "success_envelope",
]

FAKE_API_KEY = "test-api-key-not-real"
"""The placeholder API key used by :meth:`FakeTransport.client`."""

Json = dict[str, Any]


def success_envelope(data: Any = None, **extra: Any) -> Json:
    """``{"common": {"authCode": "A000", ...}, "data": {"code": "A000", "result": "Success", "data": <data>}}``"""
    inner: Json = {"code": "A000", "result": "Success", **extra}
    if data is not None:
        inner["data"] = data
    return {"common": {"authCode": "A000", "authResult": "Success", "infobankTrId": "FAKE-TR-ID"}, "data": inner}


def error_envelope(layer: Literal["gateway", "service"], code: str, message: str = "Failed") -> Json:
    """An error envelope: gateway errors set ``common.authCode``, service errors set ``data.code``."""
    if layer == "gateway":
        return {"common": {"authCode": code, "authResult": message, "infobankTrId": "FAKE-TR-ID"}}
    return {
        "common": {"authCode": "A000", "authResult": "Success", "infobankTrId": "FAKE-TR-ID"},
        "data": {"code": code, "result": message},
    }


@dataclass(frozen=True)
class RecordedFile:
    """A multipart file part as recorded: name, type and size only."""

    filename: str
    content_type: str
    size: int


@dataclass(frozen=True)
class RecordedRequest:
    """One request the client made."""

    operation_id: str | None
    """Matched ``operationId`` (``None`` for an unknown path)."""
    operation: str | None
    """``<resource>.<method>`` of the matched operation."""
    method: str
    path: str
    """Real path, with the encoded path values."""
    path_template: str | None
    query: dict[str, str | list[str]]
    json: Any
    """Parsed JSON body, if any."""
    form: dict[str, str | RecordedFile | list[str | RecordedFile]] | None
    """Multipart fields, if any: text (and JSON parts) as text, files as :class:`RecordedFile`."""
    header_names: tuple[str, ...]
    """Names (not values) of the request headers."""

    def __repr__(self) -> str:
        return f"RecordedRequest({self.method} {self.path_template or self.path})"


Reply = Callable[[RecordedRequest], httpx.Response]


def _json_response(status: int, body: Any, headers: Mapping[str, str] | None = None) -> httpx.Response:
    return httpx.Response(status, json=body, headers=dict(headers or {}))


class Stub:
    """Stubbed responses for one operation. Each call adds one response; the last one repeats."""

    def __init__(self, fake: FakeTransport, add: Callable[[Reply], None]) -> None:
        self._fake = fake
        self._add = add

    def respond(self, status: int, body: Any, headers: Mapping[str, str] | None = None) -> Stub:
        """Answer with a raw status and JSON body (and optional headers such as ``Retry-After``)."""
        self._add(lambda _request: _json_response(status, body, headers))
        return self

    def data(self, data: Any, **extra: Any) -> Stub:
        """Answer with a success envelope whose ``data.data`` is ``data`` (``extra`` goes next to it)."""
        return self.respond(200, success_envelope(data, **extra))

    def send_result(self, *codes: str) -> Stub:
        """Answer a send with one destination result per code.

        ``"A000"`` is accepted, ``"A301"`` is a duplicate (``result.duplicates``), anything else is rejected.
        """
        self._add(lambda request: _json_response(200, self._fake._send_body(request.json, codes)))
        return self

    def duplicates(self) -> Stub:
        """Answer a send with ``A301`` for every recipient: already accepted with the same idempotency key.

        The request succeeds; the recipients come back in ``result.duplicates`` (not ``failed``/``succeeded``).
        """

        def answer(request: RecordedRequest) -> httpx.Response:
            count = len(_destinations(request.json)) or 1
            return _json_response(200, self._fake._send_body(request.json, ["A301"] * count))

        self._add(answer)
        return self

    def fail(
        self, layer: Literal["gateway", "service"], status: int, code: str, *, retry_after: float | None = None
    ) -> Stub:
        """Answer with an API error, e.g. ``fail("service", 200, "A020")`` or ``fail("gateway", 401, "A401")``.

        Pass ``retry_after=0`` for retried errors (429, 5xx) so your tests do not wait for the backoff.
        """
        headers = None if retry_after is None else {"retry-after": str(retry_after)}
        return self.respond(status, error_envelope(layer, code), headers)

    def network_error(self) -> Stub:
        """Fail like a refused connection (:class:`bizgo.APIConnectionError`)."""

        def reply(_request: RecordedRequest) -> httpx.Response:
            raise httpx.ConnectError("connection refused (fake)")

        self._add(reply)
        return self

    def timeout(self) -> Stub:
        """Fail like a timeout (:class:`bizgo.APITimeoutError`)."""

        def reply(_request: RecordedRequest) -> httpx.Response:
            raise httpx.ReadTimeout("timed out (fake)")

        self._add(reply)
        return self

    def default(self) -> Stub:
        """Answer with the default success response."""
        self._add(self._fake._default_response)
        return self


def _matchers() -> list[tuple[Operation, re.Pattern[str]]]:
    out = []
    for op in OPERATIONS.values():
        pattern = "[^/]+".join(re.escape(part) for part in re.split(r"\{[^}]+\}", op.path))
        out.append((op, re.compile(f"^{pattern}$")))
    return sorted(out, key=lambda item: item[0].path.count("{"))  # literal paths win over templates


_MATCHERS = _matchers()


def _match(method: str, path: str) -> Operation | None:
    for op, pattern in _MATCHERS:
        if op.method == method and pattern.match(path):
            return op
    return None


def _form(request: httpx.Request) -> dict[str, str | RecordedFile | list[str | RecordedFile]]:
    content_type = request.headers.get("content-type", "")
    raw = b"Content-Type: " + content_type.encode("latin-1") + b"\r\n\r\n" + request.content
    message = BytesParser(policy=HTTP).parsebytes(raw)
    out: dict[str, str | RecordedFile | list[str | RecordedFile]] = {}
    for part in message.iter_parts():
        if not isinstance(part, Message):
            continue
        name = part.get_param("name", header="content-disposition")
        if not isinstance(name, str):
            continue
        payload = part.get_payload(decode=True)
        content = payload if isinstance(payload, bytes) else b""
        filename = part.get_filename()
        value: str | RecordedFile
        if filename is None:
            value = content.decode("utf-8", "replace")
        else:
            value = RecordedFile(filename=filename, content_type=part.get_content_type(), size=len(content))
        existing = out.get(name)
        if existing is None:
            out[name] = value
        elif isinstance(existing, list):
            existing.append(value)
        else:
            out[name] = [existing, value]
    return out


def _record(request: httpx.Request) -> RecordedRequest:
    raw_path = request.url.raw_path.decode("ascii").split("?", 1)[0]
    op = _match(request.method, raw_path)
    query: dict[str, str | list[str]] = {}
    for key, value in request.url.params.multi_items():
        existing = query.get(key)
        if existing is None:
            query[key] = value
        elif isinstance(existing, list):
            existing.append(value)
        else:
            query[key] = [existing, value]
    content_type = request.headers.get("content-type", "")
    body: Any = None
    form = None
    if content_type.startswith("application/json"):
        try:
            body = json.loads(request.content)
        except ValueError:
            body = None
    elif content_type.startswith("multipart/form-data"):
        form = _form(request)
    return RecordedRequest(
        operation_id=op.id if op else None,
        operation=op.name if op else None,
        method=request.method,
        path=raw_path,
        path_template=op.path if op else None,
        query=query,
        json=body,
        form=form,
        header_names=tuple(request.headers.keys()),
    )


class FakeTransport(httpx.BaseTransport, httpx.AsyncBaseTransport):
    """An in-memory stand-in for the Bizgo API. Plug it into a client with :meth:`client` / :meth:`async_client`,
    or pass ``httpx.Client(transport=fake)`` as ``http_client`` yourself. Thread-safe."""

    _bizgo_safe_transport = True
    """Accepted as ``http_client`` transport: it never redirects, retries or authenticates."""

    def __init__(self) -> None:
        self._requests: list[RecordedRequest] = []
        self._stubs: dict[str, list[Reply]] = {}
        self._msg_keys = 0
        self._lock = threading.Lock()

    def __repr__(self) -> str:
        return f"FakeTransport(requests={len(self._requests)})"

    # ------------------------------------------------------------ clients

    def client(self, **overrides: Any) -> Bizgo:
        """A :class:`bizgo.Bizgo` that talks to this fake: placeholder key, sandbox URL, rate limit off."""
        options: dict[str, Any] = {
            "api_key": FAKE_API_KEY,
            "environment": Environment.SANDBOX,
            "rate_limit": None,
            "http_client": httpx.Client(transport=self),
        }
        options.update(overrides)
        return Bizgo(**options)

    def async_client(self, **overrides: Any) -> AsyncBizgo:
        """A :class:`bizgo.AsyncBizgo` that talks to this fake."""
        options: dict[str, Any] = {
            "api_key": FAKE_API_KEY,
            "environment": Environment.SANDBOX,
            "rate_limit": None,
            "http_client": httpx.AsyncClient(transport=self),
        }
        options.update(overrides)
        return AsyncBizgo(**options)

    # ------------------------------------------------------------ stubs and records

    def on(self, operation_or_method: str, path_template: str | None = None) -> Stub:
        """Stub an operation by ``operationId``, or by HTTP method and path template."""
        if path_template is None:
            op = OPERATIONS.get(operation_or_method)
        else:
            method = operation_or_method.upper()
            op = next((o for o in OPERATIONS.values() if o.method == method and o.path == path_template), None)
        if op is None:
            raise KeyError(f"unknown operation: {operation_or_method} {path_template or ''}".strip())
        op_id = op.id

        def add(reply: Reply) -> None:
            with self._lock:
                self._stubs.setdefault(op_id, []).append(reply)

        return Stub(self, add)

    @property
    def requests(self) -> list[RecordedRequest]:
        """Every recorded request, oldest first."""
        with self._lock:
            return list(self._requests)

    def requests_for(self, operation_id: str) -> list[RecordedRequest]:
        """Recorded requests of one operation."""
        return [r for r in self.requests if r.operation_id == operation_id]

    @property
    def last_request(self) -> RecordedRequest:
        """The most recent request (``IndexError`` if there is none)."""
        with self._lock:
            return self._requests[-1]

    def reset(self) -> None:
        """Forget recorded requests and stubs."""
        with self._lock:
            self._requests.clear()
            self._stubs.clear()

    # ------------------------------------------------------------ httpx transport

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        request.read()
        return self._handle(request)

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        await request.aread()
        return self._handle(request)

    def _handle(self, request: httpx.Request) -> httpx.Response:
        recorded = _record(request)
        with self._lock:
            self._requests.append(recorded)
            queue = self._stubs.get(recorded.operation_id or "")
            reply = (queue.pop(0) if len(queue) > 1 else queue[0]) if queue else None
        if recorded.operation_id is None:
            return _json_response(404, error_envelope("gateway", "A404", "Not Found"))
        return reply(recorded) if reply else self._default_response(recorded)

    # ------------------------------------------------------------ default responses

    def _default_response(self, request: RecordedRequest) -> httpx.Response:
        if request.operation_id in ("sendOmni", "createReservation", "addReservationRecipients"):
            count = len(_destinations(request.json)) or 1
            body = self._send_body(request.json, ["A000"] * count)
            if request.operation_id == "createReservation":
                body["data"]["resvKey"] = "FAKE-RESVKEY-000001"  # next to data.data (x-sdk-result: data)
            return _json_response(200, body)
        if request.operation_id == "uploadMmsFile":
            return _json_response(200, success_envelope({"fileKey": "FAKE-FILEKEY-000001"}))
        if request.operation_id == "uploadRcsFile":
            return _json_response(200, success_envelope({"media": "FAKE-MEDIA-000001"}))
        return _json_response(200, success_envelope({}))

    def _send_body(self, request: Any, codes: tuple[str, ...] | list[str]) -> Json:
        given = _destinations(request)
        destinations = []
        for i, code in enumerate(codes):
            entry: Json = {}
            if i < len(given) and isinstance(given[i].get("to"), str):
                entry["to"] = given[i]["to"]
            if i < len(given) and isinstance(given[i].get("ref"), str):
                entry["ref"] = given[i]["ref"]
            with self._lock:
                self._msg_keys += 1
                entry["msgKey"] = f"FAKE-MSGKEY-{self._msg_keys:06d}"
            entry["code"] = code
            entry["result"] = "Success" if code == "A000" else "Failed"
            destinations.append(entry)
        ref = request.get("ref") if isinstance(request, dict) else None
        return success_envelope({"destinations": destinations}, **({"ref": ref} if isinstance(ref, str) else {}))


def _destinations(request: Any) -> list[Json]:
    items = request.get("destinations") if isinstance(request, dict) else None
    return [d for d in items if isinstance(d, dict)] if isinstance(items, list) else []


class SignedWebhook(NamedTuple):
    headers: dict[str, str]
    body: bytes

    def __repr__(self) -> str:  # the body can hold phone numbers
        return f"SignedWebhook(headers={sorted(self.headers)}, body=<{len(self.body)} bytes>)"


def sign_webhook(
    secret: str | bytes,
    payload: Any,
    *,
    timestamp: str | int | None = None,
    encoding: Literal["hex", "base64"] = "hex",
) -> SignedWebhook:
    """Build a signed webhook request for testing your :class:`~bizgo.webhooks.WebhookReceiver` handler.

    Returns ``(headers, body)``: ``X-IB-Timestamp`` (default now, epoch milliseconds as Bizgo sends it),
    ``X-IB-Signature`` = HmacSHA256(secret, timestamp) and the JSON body bytes.
    """
    stamp = str(timestamp if timestamp is not None else int(time.time() * 1000))
    key = secret if isinstance(secret, bytes) else secret.encode("utf-8")
    digest = hmac.new(key, stamp.encode("ascii"), hashlib.sha256).digest()
    signature = digest.hex() if encoding == "hex" else base64.b64encode(digest).decode("ascii")
    if isinstance(payload, bytes):
        body = payload
    elif isinstance(payload, str):
        body = payload.encode("utf-8")
    else:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {"Content-Type": "application/json", "X-IB-Timestamp": stamp, "X-IB-Signature": signature}
    return SignedWebhook(headers=headers, body=body)
