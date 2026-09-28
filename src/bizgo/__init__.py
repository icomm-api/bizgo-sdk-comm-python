"""Python SDK for the Bizgo Communication API.

Quick start::

    from bizgo import Bizgo, Environment, AlimtalkMessage, SmsMessage

    client = Bizgo(environment=Environment.SANDBOX)  # API key from the BIZGO_API_KEY env var

    # AlimTalk, falling back to SMS if it fails
    result = client.send.omni(
        to="01000000000",
        messages=[
            AlimtalkMessage(sender_key="SENDER_KEY", template_code="TEMPLATE_CODE", msg_type="AT", text="..."),
            SmsMessage(from_="01000000000", text="..."),
        ],
        idempotency_key="order-1234",  # idempotencyTtl defaults to DEFAULT_IDEMPOTENCY_TTL (86400 s)
    )

Every other operation of the API is generated from the OpenAPI spec, for example
``client.alimtalk.templates.list(sender_key=...)`` or ``client.reservations.create(...)``.
Test helpers live in :mod:`bizgo.testing`, OpenTelemetry tracing in :mod:`bizgo.otel` (``[otel]`` extra).

See https://developers.bizgo.io/api-sdk/api-reference for the API itself.
"""

from . import hooks, models, webhooks
from ._client import AsyncBizgo, Bizgo
from ._config import Environment
from ._errors import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    BizgoError,
    ConfigurationError,
    DuplicateRequestError,
    InternalServerError,
    InvalidResponseError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    WebhookPayloadError,
    WebhookVerificationError,
)
from ._ratelimit import RateLimit
from ._version import __version__
from .hooks import Hooks, RequestEvent
from .models._generated_request import (
    AlimtalkMessage,
    BrandMessage,
    Destination,
    InternationalMessage,
    MmsMessage,
    NaverTalkMessage,
    RcsMessage,
    SendOmniRequest,
    SmsMessage,
)
from .models._results import BulkChunkError, BulkSendResult, MessagePage, MoPage, ReportBatch, SendResult
from .resources._common import DEFAULT_IDEMPOTENCY_TTL

__all__ = [
    "DEFAULT_IDEMPOTENCY_TTL",
    "APIConnectionError",
    "APIError",
    "APITimeoutError",
    "AlimtalkMessage",
    "AsyncBizgo",
    "AuthenticationError",
    "BadRequestError",
    "Bizgo",
    "BizgoError",
    "BrandMessage",
    "BulkChunkError",
    "BulkSendResult",
    "ConfigurationError",
    "Destination",
    "DuplicateRequestError",
    "Environment",
    "Hooks",
    "InternalServerError",
    "InternationalMessage",
    "InvalidResponseError",
    "MessagePage",
    "MmsMessage",
    "MoPage",
    "NaverTalkMessage",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimit",
    "RateLimitError",
    "RcsMessage",
    "ReportBatch",
    "RequestEvent",
    "SendOmniRequest",
    "SendResult",
    "SmsMessage",
    "WebhookPayloadError",
    "WebhookVerificationError",
    "__version__",
    "hooks",
    "models",
    "webhooks",
]
