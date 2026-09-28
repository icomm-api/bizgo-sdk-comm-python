"""Client configuration."""

from __future__ import annotations

import enum
import os
import platform
import re
import sys
from dataclasses import dataclass, field
from urllib.parse import urlsplit

import httpx

from ._errors import ConfigurationError
from ._version import __version__

API_KEY_ENV = "BIZGO_API_KEY"
DEFAULT_TIMEOUT = httpx.Timeout(30.0, connect=5.0)
DEFAULT_MAX_RETRIES = 2
_LOCAL_HOSTS = {"localhost", "127.0.0.1", "::1"}


class Environment(str, enum.Enum):
    """Bizgo API server."""

    PRODUCTION = "https://mars.ibapi.kr"
    """운영 서버. 실제로 발송됩니다."""
    SANDBOX = "https://sandbox-mars.ibapi.kr"
    """테스트 서버. 운영과 같은 API Key를 쓰며 실제로 발송되지 않습니다."""


_API_KEY = re.compile(r"[\x21-\x7e]+")


def resolve_api_key(api_key: str | None) -> str:
    key = api_key if api_key is not None else os.environ.get(API_KEY_ENV, "")
    if not isinstance(key, str):
        raise ConfigurationError("API Key는 문자열이어야 합니다")
    if not key:
        raise ConfigurationError(
            f"API Key가 없습니다. api_key 인자로 넘기거나 환경변수 {API_KEY_ENV}에 설정하세요. "
            "키는 코드에 직접 쓰지 말고 환경변수나 시크릿 저장소에서 읽어 오세요."
        )
    if any(c.isspace() for c in key):
        # not stripped silently (SDK-DESIGN.md §12.16): a stray newline usually means the key was read wrongly
        raise ConfigurationError(
            "API Key에 공백·줄바꿈이 있습니다. 'Bearer '나 'ApiKey ' 같은 접두어와 앞뒤 공백 없이 키만 넣으세요."
        )
    if not _API_KEY.fullmatch(key):
        raise ConfigurationError("API Key에 쓸 수 없는 문자(제어문자·비ASCII)가 있습니다. 콘솔에서 받은 키만 넣으세요.")
    return key


def resolve_base_url(environment: Environment | str, base_url: str | None) -> str:
    url = (base_url or Environment(environment).value).rstrip("/")
    try:
        parts = urlsplit(url)
        parts.port  # noqa: B018 - validates the port
    except ValueError:
        raise ConfigurationError("base_url 형식이 올바르지 않습니다") from None
    if parts.username is not None or parts.password is not None or "@" in parts.netloc:
        # user:pw@ would make httpx send Basic auth instead of the API key
        raise ConfigurationError("base_url에 사용자 정보(user:pw@)를 넣을 수 없습니다")
    if parts.query or parts.fragment or "?" in url or "#" in url:
        raise ConfigurationError("base_url에 쿼리(?)나 fragment(#)를 넣을 수 없습니다")
    if not parts.hostname:
        raise ConfigurationError("base_url에 호스트가 없습니다")
    if parts.scheme != "https" and parts.hostname not in _LOCAL_HOSTS:
        # The API key travels in a header, so it must never be sent over plain HTTP.
        raise ConfigurationError(f"base_url은 https여야 합니다: {parts.scheme}://{parts.hostname}")
    return url


SDK_NAME = "bizgo-sdk-comm-python"
_APP_NAME = re.compile(r"[A-Za-z0-9._-]{1,50}")
_APP_VERSION = re.compile(r"[A-Za-z0-9._+-]{1,30}")


def os_name(value: str | None = None) -> str:
    """Coarse OS name for the User-Agent (SDK-DESIGN.md §2.1). Never the host name, user or kernel version."""
    value = (value if value is not None else sys.platform).lower()
    if value.startswith("linux"):
        return "linux"
    if value.startswith(("win32", "cygwin", "msys", "windows")):
        return "windows"
    if value.startswith("darwin"):
        return "darwin"
    if value.startswith("freebsd"):
        return "freebsd"
    return "other"


def arch_name(value: str | None = None) -> str:
    """Coarse CPU architecture for the User-Agent: x64, arm64, x86, arm or other."""
    value = (value if value is not None else platform.machine()).lower()
    if value in ("x86_64", "amd64", "x64"):
        return "x64"
    if value in ("aarch64", "arm64", "armv8", "armv8l"):
        return "arm64"
    if value in ("i386", "i486", "i586", "i686", "x86"):
        return "x86"
    if value.startswith("arm"):
        return "arm"
    return "other"


def user_agent(app_info: tuple[str, str] | None = None) -> str:
    """``bizgo-sdk-comm-python/<ver> python/<ver> (<os>; <arch>)[ app/<name>-<version>]``"""
    agent = f"{SDK_NAME}/{__version__} python/{platform.python_version()} ({os_name()}; {arch_name()})"
    if app_info is not None:
        if not isinstance(app_info, tuple) or len(app_info) != 2 or not all(isinstance(v, str) for v in app_info):
            raise ConfigurationError("app_info는 (이름, 버전) 문자열 두 개의 tuple이어야 합니다")
        name, version = app_info
        # strict patterns: no header injection (CR/LF), no spaces, no personal data such as e-mail addresses
        if not _APP_NAME.fullmatch(name):
            raise ConfigurationError("app_info 이름은 영문·숫자·._- 1~50자만 쓸 수 있습니다")
        if not _APP_VERSION.fullmatch(version):
            raise ConfigurationError("app_info 버전은 영문·숫자·._+- 1~30자만 쓸 수 있습니다")
        agent += f" app/{name}-{version}"
    return agent


CLIENT_HEADER = f"{SDK_NAME}/{__version__}"
"""``X-Bizgo-Client`` value: survives proxies that rewrite the User-Agent."""


@dataclass(frozen=True)
class ClientConfig:
    base_url: str
    timeout: httpx.Timeout
    max_retries: int
    api_key: str = field(repr=False)
    user_agent: str = field(default_factory=user_agent)

    def __reduce__(self) -> tuple[()]:
        # the API key must not end up in pickles (task queues, caches, core dumps of worker payloads)
        raise TypeError(
            "ClientConfig는 API Key를 담고 있어 pickle할 수 없습니다. 작업자에서 클라이언트를 새로 만드세요."
        )
