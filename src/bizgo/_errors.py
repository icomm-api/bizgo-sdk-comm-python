"""Exception hierarchy.

::

    BizgoError
    ├── ConfigurationError          # missing API key, insecure base URL, ...
    ├── APIConnectionError          # network failure; the request may or may not have reached Bizgo
    │   └── APITimeoutError
    ├── APIError                    # Bizgo answered with a failure code
    │   ├── BadRequestError         # 400 / invalid field (A3xx, A2xx, ...)
    │   ├── AuthenticationError     # 401 / A401, A100, A001, A002
    │   ├── PermissionDeniedError   # 403 / A403, A110, A111
    │   ├── NotFoundError           # 404
    │   ├── DuplicateRequestError   # data.code A301 (same idempotencyKey within its TTL)
    │   ├── RateLimitError          # 429 / A020
    │   └── InternalServerError     # 5xx
    ├── InvalidResponseError        # response body is not the documented envelope
    └── WebhookVerificationError    # signature / timestamp check failed
        └── WebhookPayloadError     # body is not valid JSON / too deep / wrong fields

Exception messages never contain the API key, request bodies or phone numbers.
"""

from __future__ import annotations

from typing import Any, Literal

from ._error_codes import SERVICE_CODES

__all__ = [
    "APIConnectionError",
    "APIError",
    "APITimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "BizgoError",
    "ConfigurationError",
    "DuplicateRequestError",
    "InternalServerError",
    "InvalidResponseError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "WebhookPayloadError",
    "WebhookVerificationError",
]


def _restore(cls: type[BizgoError], args: tuple[Any, ...], state: dict[str, Any]) -> BizgoError:
    error = cls.__new__(cls)
    Exception.__init__(error, *args)
    error.__dict__.update(state)
    return error


class BizgoError(Exception):
    """Base class for every error raised by this SDK.

    Every SDK error can be pickled (for task queues and multiprocessing) with all its attributes.
    """

    def __reduce__(self) -> tuple[Any, ...]:
        return (_restore, (type(self), self.args, dict(self.__dict__)))


class ConfigurationError(BizgoError):
    """The client is configured incorrectly (for example the API key is missing)."""


class InvalidResponseError(BizgoError):
    """The response could not be parsed as the documented ``{common, data}`` envelope (not JSON, too large, too
    deeply nested, or fields of an unexpected type).

    For a send operation the request **may have been accepted**: check with the status inquiry APIs before
    sending again.

    Attributes:
        http_status: HTTP status of the response.
        tracking_id: ``common.infobankTrId`` if it could be read.
        body: the parsed body if it was JSON. It can contain phone numbers; do not log it as is.
    """

    def __init__(
        self,
        message: str,
        *,
        http_status: int | None = None,
        tracking_id: str | None = None,
        body: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.http_status = http_status
        self.tracking_id = tracking_id
        self.body = body

    def __str__(self) -> str:
        parts = [f"HTTP {self.http_status}" if self.http_status else "", self.message]
        if self.tracking_id:
            parts.append(f"infobankTrId={self.tracking_id}")
        return " | ".join(p for p in parts if p)

    def __repr__(self) -> str:
        return f"InvalidResponseError(http_status={self.http_status})"


class WebhookVerificationError(BizgoError):
    """A webhook request failed signature or timestamp verification. Reject it with HTTP 401 (or 400)."""


class WebhookPayloadError(WebhookVerificationError):
    """The webhook body is not valid JSON, too large, too deeply nested, or its fields do not match the spec.
    Answer with HTTP 400. The message never contains the body."""


class APIConnectionError(BizgoError):
    """The request failed before a response arrived.

    For send requests the message may or may not have been accepted. Re-sending can cause a duplicate
    unless you set ``idempotency_key``.
    """


class APITimeoutError(APIConnectionError):
    """The request timed out."""


Layer = Literal["gateway", "service"]


class APIError(BizgoError):
    """Bizgo returned a failure.

    Attributes:
        http_status: HTTP status code.
        code: ``common.authCode`` (gateway layer) or ``data.code`` (service layer), for example ``A401``.
        message: ``authResult`` / ``result`` text from the server.
        layer: ``"gateway"`` when authentication/format checks failed, ``"service"`` when the product API failed.
            The same code can mean different things in each layer (for example ``A301``).
        tracking_id: ``common.infobankTrId``. Give this to Bizgo support when asking about a request.
        description: Korean description of a service-layer ``code`` from the error code table, if known.
        body: the parsed response body. It can contain phone numbers; do not log it as is.
    """

    def __init__(
        self,
        message: str,
        *,
        http_status: int,
        code: str | None,
        layer: Layer,
        tracking_id: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.http_status = http_status
        self.code = code
        self.layer = layer
        self.tracking_id = tracking_id
        self.body = body
        known = SERVICE_CODES.get(code or "") if layer == "service" else None
        self.description: str | None = known[1] if known else None

    def __str__(self) -> str:
        parts = [f"HTTP {self.http_status}", f"{self.layer} code={self.code}", self.message]
        if self.description and self.description != self.message:
            parts.append(self.description)
        if self.tracking_id:
            parts.append(f"infobankTrId={self.tracking_id}")
        return " | ".join(p for p in parts if p)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(http_status={self.http_status}, code={self.code!r}, layer={self.layer!r})"


class BadRequestError(APIError):
    """The request was rejected as invalid."""


class AuthenticationError(APIError):
    """The API key is missing, wrong or expired. Check the key and that the calling IP is registered."""


class PermissionDeniedError(APIError):
    """The key is valid but not allowed to do this (blocked account, IP not allowed, ...)."""


class NotFoundError(APIError):
    """The resource does not exist."""


class DuplicateRequestError(APIError):
    """A request with the same ``idempotencyKey`` was already accepted. The message was not sent again.

    Attributes:
        already_accepted: ``True`` when the SDK had retried this request (after a timeout, network error, 5xx or
            429): an earlier attempt of the *same call* was most likely accepted. Check the result with the status
            inquiry APIs instead of treating it as a failure.
    """

    already_accepted: bool = False


class RateLimitError(APIError):
    """Too many requests (HTTP 429 / A020). Default limits: 200 TPS for send APIs, 5 TPS for the others.

    Attributes:
        retry_after: seconds from the ``Retry-After`` header, if the server sent one.
    """

    def __init__(self, *args: Any, retry_after: float | None = None, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.retry_after = retry_after


class InternalServerError(APIError):
    """Bizgo had an internal error (5xx)."""


_GATEWAY_CODES: dict[str, type[APIError]] = {
    "A400": BadRequestError,
    "A401": AuthenticationError,
    "A403": PermissionDeniedError,
    "A404": NotFoundError,
}
_SERVICE_CODES: dict[str, type[APIError]] = {
    "A001": AuthenticationError,
    "A002": AuthenticationError,
    "A100": AuthenticationError,
    "A110": PermissionDeniedError,
    "A111": PermissionDeniedError,
    "A020": RateLimitError,
    "A301": DuplicateRequestError,
}
_STATUS: dict[int, type[APIError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    429: RateLimitError,
}


def error_class(http_status: int, code: str | None, layer: Layer) -> type[APIError]:
    """Pick the exception class. Gateway (``common.authCode``) and service (``data.code``) codes are looked up
    in separate tables because the same code means different things (service ``A401`` is an invalid
    ``paymentCode`` field, not an authentication failure)."""
    table = _GATEWAY_CODES if layer == "gateway" else _SERVICE_CODES
    if code and code in table:
        return table[code]
    if layer == "service" and http_status < 400 and code in SERVICE_CODES:
        # failures reported inside an HTTP 200: use the status documented for the code
        http_status = SERVICE_CODES[code][0] or http_status
    if http_status in _STATUS:
        return _STATUS[http_status]
    if http_status >= 500:
        return InternalServerError
    if http_status >= 400:
        return BadRequestError
    return APIError
