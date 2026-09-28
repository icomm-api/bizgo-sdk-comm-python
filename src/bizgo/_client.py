"""Client entry points."""

from __future__ import annotations

import os
from collections.abc import Sequence
from types import TracebackType
from typing import Any

import httpx

from . import _ratelimit
from ._config import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
    ClientConfig,
    Environment,
    resolve_api_key,
    resolve_base_url,
    user_agent,
)
from ._errors import ConfigurationError
from ._http import build_client, check_http_client
from ._ratelimit import RateLimit
from ._transport import AsyncTransport, SyncTransport
from .hooks import Hooks, normalize
from .resources._generated import AsyncResources, Resources
from .resources.files import AsyncFiles, Files
from .resources.messages import AsyncMessages, Messages
from .resources.reports import AsyncReports, Reports
from .resources.send import AsyncSend, Send


def _config(
    api_key: str | None,
    environment: Environment | str,
    base_url: str | None,
    timeout: float | httpx.Timeout,
    max_retries: int,
    app_info: tuple[str, str] | None = None,
) -> ClientConfig:
    if max_retries < 0:
        raise ValueError("max_retries must be >= 0")
    return ClientConfig(
        base_url=resolve_base_url(environment, base_url),
        timeout=timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout),
        max_retries=max_retries,
        api_key=resolve_api_key(api_key),
        user_agent=user_agent(app_info),
    )


_DEFAULT_RATE_LIMIT = RateLimit()

CAFile = str | os.PathLike[str]
"""Path to a CA bundle file (or directory) for ``verify=``."""


def _http_client(
    http_client: Any, proxy: str | None, verify: Any, trust: bool, timeout: httpx.Timeout, *, is_async: bool
) -> tuple[Any, bool]:
    """Return ``(client, owned)``. A user client is checked (SDK-DESIGN.md §12.6); otherwise the SDK builds one."""
    if http_client is None:
        return build_client(timeout, proxy, verify, is_async=is_async), True
    if proxy is not None or verify is not None:
        raise ConfigurationError(
            "http_client를 넘길 때는 proxy·verify를 함께 쓸 수 없습니다(그 클라이언트에 설정하세요)"
        )
    check_http_client(http_client, is_async=is_async, trust=trust)
    return http_client, False


class Bizgo(Resources):
    """Bizgo Communication API client.

    Example::

        from bizgo import Bizgo, Environment

        with Bizgo(environment=Environment.SANDBOX) as client:   # API key from BIZGO_API_KEY
            result = client.send.sms(to="01000000000", from_="01000000000", text="인증번호는 123456 입니다.")
            print(result.msg_keys, result.failed)

    Args:
        api_key: Integrated API key from the console. Defaults to the ``BIZGO_API_KEY`` environment variable.
            Pass the key only, without ``Bearer``/``ApiKey`` prefixes. Never hard-code it.
        environment: :attr:`Environment.PRODUCTION` (default, real sends) or :attr:`Environment.SANDBOX`.
        base_url: Override the server URL (must be https, except localhost for tests).
        timeout: Seconds, or an :class:`httpx.Timeout`. Default: 30s total, 5s connect.
        max_retries: Retries for rate limits and transient errors (default 2). Sends are retried after a
            timeout only when ``idempotency_key`` is set.
        http_client: Your own :class:`httpx.Client`. It is not closed by this client. It is refused unless the SDK
            can control it (stock ``HTTPTransport`` with ``retries=0`` or ``MockTransport``, no ``event_hooks``,
            no cookies); prefer ``proxy=``/``verify=``. Its own ``auth``/redirect settings are ignored per request.
        proxy: Proxy URL (``http://``, ``https://``, ``socks5://`` with ``httpx[socks]``) for the SDK's own client.
        verify: Path to a CA bundle file or directory for a private CA. TLS verification cannot be turned off
            (``False`` is refused).
        trust_http_client: Accept an ``http_client`` the SDK cannot inspect (custom transport, mounts, event
            hooks). You then guarantee it does not redirect, retry or authenticate by itself and accept the
            duplicate-send and data-leak risk.
        rate_limit: Client-side token buckets (:class:`~bizgo.RateLimit`, default 200/s for send APIs and 5/s for
            the others). ``None`` turns them off. They pace this client instance only; see the README.
        hooks: :class:`~bizgo.hooks.Hooks` (or a list) called at the start and end of every API call, with the
            operation, path template, status and error code only (never bodies, queries or phone numbers).
        app_info: Optional ``(name, version)`` of your application, appended to the User-Agent as
            `` app/<name>-<version>`` (letters, digits and ``._-``; version also ``+``). Do not put e-mail
            addresses, phone numbers or other personal data in it.

    Attributes:
        send: :class:`~bizgo.resources.send.Send`
        files: :class:`~bizgo.resources.files.Files`
        reports: :class:`~bizgo.resources.reports.Reports`
        messages: :class:`~bizgo.resources.messages.Messages`
        reservations, insights, kakao, alimtalk, brand_message, rcs, counsel: resources generated from the spec,
            for example ``client.alimtalk.templates.list(sender_key=...)``.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        environment: Environment | str = Environment.PRODUCTION,
        base_url: str | None = None,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: httpx.Client | None = None,
        rate_limit: RateLimit | None = _DEFAULT_RATE_LIMIT,
        hooks: Hooks | Sequence[Hooks] | None = None,
        app_info: tuple[str, str] | None = None,
        proxy: str | None = None,
        verify: CAFile | None = None,
        trust_http_client: bool = False,
    ) -> None:
        self._config = _config(api_key, environment, base_url, timeout, max_retries, app_info)
        client, owned = _http_client(
            http_client, proxy, verify, trust_http_client, self._config.timeout, is_async=False
        )
        self._transport = SyncTransport(
            self._config,
            client,
            limiter=_ratelimit.build(rate_limit),
            hooks=normalize(hooks),
            owns_client=owned,
        )
        self._init_resources(self._transport)
        self.send = Send(self._transport)
        self.files = Files(self._transport)
        self.reports = Reports(self._transport)
        self.messages = Messages(self._transport)

    @property
    def base_url(self) -> str:
        return self._config.base_url

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> Bizgo:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        self.close()

    def __repr__(self) -> str:
        return f"Bizgo(base_url={self._config.base_url!r})"


class AsyncBizgo(AsyncResources):
    """Async version of :class:`Bizgo`. Use ``async with AsyncBizgo() as client: await client.send.sms(...)``."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        environment: Environment | str = Environment.PRODUCTION,
        base_url: str | None = None,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: httpx.AsyncClient | None = None,
        rate_limit: RateLimit | None = _DEFAULT_RATE_LIMIT,
        hooks: Hooks | Sequence[Hooks] | None = None,
        app_info: tuple[str, str] | None = None,
        proxy: str | None = None,
        verify: CAFile | None = None,
        trust_http_client: bool = False,
    ) -> None:
        self._config = _config(api_key, environment, base_url, timeout, max_retries, app_info)
        client, owned = _http_client(http_client, proxy, verify, trust_http_client, self._config.timeout, is_async=True)
        self._transport = AsyncTransport(
            self._config,
            client,
            limiter=_ratelimit.build(rate_limit),
            hooks=normalize(hooks),
            owns_client=owned,
        )
        self._init_resources(self._transport)
        self.send = AsyncSend(self._transport)
        self.files = AsyncFiles(self._transport)
        self.reports = AsyncReports(self._transport)
        self.messages = AsyncMessages(self._transport)

    @property
    def base_url(self) -> str:
        return self._config.base_url

    async def close(self) -> None:
        await self._transport.close()

    async def __aenter__(self) -> AsyncBizgo:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self.close()

    def __repr__(self) -> str:
        return f"AsyncBizgo(base_url={self._config.base_url!r})"
