"""Building and checking the HTTP client (SDK-DESIGN.md §12.6).

The SDK must be able to guarantee that a request is not redirected, retried or re-authenticated by the HTTP
library: a hidden retry can deliver a message twice, and a redirect or client-side auth can send the API key
somewhere else. Per request the transport already forces ``auth=None`` and ``follow_redirects=False`` and sets
its own ``Authorization``. A user-supplied ``http_client`` is accepted only if everything else can be inspected:

- the transport (and every mounted transport) is the stock ``httpx.HTTPTransport``/``AsyncHTTPTransport`` with
  ``retries=0``, an ``httpx.MockTransport`` (tests) or :class:`bizgo.testing.FakeTransport`;
- no ``event_hooks`` (they can rewrite requests and responses);
- an empty cookie jar.

Anything else needs ``trust_http_client=True``: you then guarantee the client does not redirect, retry or
authenticate by itself, and you accept the duplicate-send and data-leak risk. The common reasons for a custom
client are covered by SDK options instead: ``proxy=`` and ``verify=`` (a CA bundle path; never ``False``).
"""

from __future__ import annotations

import os
import ssl
from typing import Any
from urllib.parse import urlsplit

import httpx

from ._errors import ConfigurationError

_PROXY_SCHEMES = {"http", "https", "socks5", "socks5h"}


def _transport_ok(transport: Any, is_async: bool) -> bool:
    if getattr(type(transport), "_bizgo_safe_transport", False):  # bizgo.testing.FakeTransport
        return True
    if isinstance(transport, httpx.MockTransport):  # test transports (never used in production)
        return True
    stock = httpx.AsyncHTTPTransport if is_async else httpx.HTTPTransport
    if type(transport) is not stock:  # subclasses can override handle_request
        return False
    return getattr(getattr(transport, "_pool", None), "_retries", None) == 0


def check_http_client(client: Any, *, is_async: bool, trust: bool) -> None:
    """Refuse a user ``http_client`` whose redirect/retry/auth behaviour the SDK cannot control."""
    expected = httpx.AsyncClient if is_async else httpx.Client
    if not isinstance(client, expected):
        raise ConfigurationError(f"http_client는 {expected.__module__}.{expected.__name__}이어야 합니다")
    if not isinstance(trust, bool):
        raise ConfigurationError("trust_http_client는 True/False여야 합니다")
    problems = []
    if not _transport_ok(getattr(client, "_transport", None), is_async):
        problems.append("transport가 기본 HTTPTransport(retries=0)가 아닙니다")
    for transport in getattr(client, "_mounts", {}).values():
        if transport is not None and not _transport_ok(transport, is_async):
            problems.append("mounts에 기본 HTTPTransport(retries=0)가 아닌 transport가 있습니다")
            break
    hooks = client.event_hooks
    if hooks.get("request") or hooks.get("response"):
        problems.append("event_hooks가 설정되어 있습니다")
    if len(client.cookies.jar):
        problems.append("쿠키가 들어 있습니다")
    if problems and not trust:
        raise ConfigurationError(
            "http_client를 SDK가 안전하게 제어할 수 없습니다: "
            + "; ".join(problems)
            + ". 프록시·CA 인증서가 필요하면 proxy=, verify= 옵션을 쓰세요. 이 클라이언트가 리다이렉트·재시도·"
            "자체 인증을 하지 않는다고 보장할 수 있을 때만 trust_http_client=True로 허용하세요"
            "(중복 발송·정보 유출 위험을 감수하는 설정입니다)."
        )


def _ssl_context(verify: Any) -> ssl.SSLContext | None:
    if verify is None or verify is True:
        return None
    if verify is False or isinstance(verify, bool):
        raise ConfigurationError("verify=False는 허용하지 않습니다. 사설 인증서는 CA 번들 파일 경로를 넘기세요.")
    if not isinstance(verify, (str, os.PathLike)):
        raise ConfigurationError("verify에는 CA 번들 파일(또는 디렉터리) 경로만 넘길 수 있습니다")
    path = os.fspath(verify)
    name = os.path.basename(path.rstrip("/\\")) or "verify"
    try:
        if os.path.isdir(path):
            return ssl.create_default_context(capath=path)
        if os.path.isfile(path):
            return ssl.create_default_context(cafile=path)
    except (OSError, ssl.SSLError):
        raise ConfigurationError(f"CA 번들을 읽지 못했습니다: {name}") from None
    raise ConfigurationError(f"CA 번들 경로가 없습니다: {name}")


def _proxy(proxy: Any) -> str | None:
    if proxy is None:
        return None
    if not isinstance(proxy, str) or not proxy:
        raise ConfigurationError("proxy는 URL 문자열이어야 합니다")
    try:
        parts = urlsplit(proxy)
    except ValueError:
        raise ConfigurationError("proxy URL 형식이 올바르지 않습니다") from None
    if parts.scheme not in _PROXY_SCHEMES or not parts.hostname:
        raise ConfigurationError("proxy는 http://, https://, socks5:// URL이어야 합니다")  # never echo the URL
    return proxy


def build_client(timeout: httpx.Timeout, proxy: Any, verify: Any, *, is_async: bool) -> Any:
    """The SDK's own client: stock transport, no retries, optional proxy and CA bundle."""
    options: dict[str, Any] = {"timeout": timeout}
    context = _ssl_context(verify)
    if context is not None:
        options["verify"] = context
    url = _proxy(proxy)
    if url is not None:
        options["proxy"] = url
    try:
        return httpx.AsyncClient(**options) if is_async else httpx.Client(**options)
    except ImportError:
        raise ConfigurationError("SOCKS 프록시에는 httpx[socks]가 필요합니다") from None
