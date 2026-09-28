"""SDK identification headers (SDK-DESIGN.md §2.1)."""

from __future__ import annotations

import platform
import re
from typing import Any

import httpx
import pytest

from bizgo import Bizgo, ConfigurationError, Environment, __version__
from bizgo._config import arch_name, os_name
from bizgo.testing import FAKE_API_KEY, success_envelope


class Capture(httpx.MockTransport):
    """A MockTransport (accepted as http_client transport) that records request headers."""

    def __init__(self) -> None:
        self.headers: list[httpx.Headers] = []
        super().__init__(self._handle)

    def _handle(self, request: httpx.Request) -> httpx.Response:
        self.headers.append(request.headers)
        return httpx.Response(200, json=success_envelope())


def _send(**options: Any) -> httpx.Headers:
    http_client = options.pop("http_client", None) or httpx.Client(transport=Capture())
    capture = http_client._transport
    assert isinstance(capture, Capture)
    with Bizgo(FAKE_API_KEY, environment=Environment.SANDBOX, http_client=http_client, rate_limit=None, **options) as c:
        c.messages.statistics("20260101")
    return capture.headers[-1]


def test_exact_header_format() -> None:
    headers = _send()
    pattern = (
        rf"bizgo-sdk-comm-python/{re.escape(__version__)} python/{re.escape(platform.python_version())} "
        r"\((linux|windows|darwin|freebsd|other); (x64|arm64|x86|arm|other)\)"
    )
    assert re.fullmatch(pattern, headers["user-agent"])
    assert headers["x-bizgo-client"] == f"bizgo-sdk-comm-python/{__version__}"
    assert headers["authorization"] == FAKE_API_KEY


def test_app_info_is_appended() -> None:
    headers = _send(app_info=("myshop", "1.4.2+build.7"))
    assert headers["user-agent"].endswith(") app/myshop-1.4.2+build.7")


@pytest.mark.parametrize(
    "app_info",
    [
        ("my shop", "1.0"),
        ("myshop\r\nX-Evil: 1", "1.0"),
        ("myshop", "1.0\n"),
        ("a" * 51, "1.0"),
        ("myshop", "1" * 31),
        ("", "1.0"),
        ("user@example.com", "1.0"),
        ("myshop", "1.0 beta"),
        ("myshop",),
        "myshop-1.0",
    ],
)
def test_invalid_app_info_is_rejected(app_info: Any) -> None:
    with pytest.raises(ConfigurationError):
        Bizgo(FAKE_API_KEY, app_info=app_info)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("linux", "linux"),
        ("win32", "windows"),
        ("cygwin", "windows"),
        ("darwin", "darwin"),
        ("freebsd14", "freebsd"),
        ("sunos5", "other"),
    ],
)
def test_os_mapping(value: str, expected: str) -> None:
    assert os_name(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("x86_64", "x64"),
        ("AMD64", "x64"),
        ("aarch64", "arm64"),
        ("arm64", "arm64"),
        ("i686", "x86"),
        ("armv7l", "arm"),
        ("riscv64", "other"),
        ("", "other"),
    ],
)
def test_arch_mapping(value: str, expected: str) -> None:
    assert arch_name(value) == expected


def test_http_client_headers_cannot_override_identity_or_key() -> None:
    capture = Capture()
    custom = httpx.Client(
        transport=capture,
        headers={"Authorization": "other-key", "User-Agent": "custom/1.0", "X-Bizgo-Client": "fake/0"},
    )
    headers = _send(http_client=custom)
    assert headers["authorization"] == FAKE_API_KEY
    assert headers["user-agent"].startswith("bizgo-sdk-comm-python/")
    assert headers["x-bizgo-client"] == f"bizgo-sdk-comm-python/{__version__}"
    assert headers.get_list("authorization") == [FAKE_API_KEY]


def test_operation_header_params_cannot_override_protected_headers() -> None:
    from bizgo._config import ClientConfig
    from bizgo._transport import SyncTransport

    config = ClientConfig(base_url="https://localhost", timeout=httpx.Timeout(1), max_retries=0, api_key=FAKE_API_KEY)
    transport = SyncTransport(config, httpx.Client(transport=Capture()))
    headers = transport._headers({"authorization": "x", "USER-AGENT": "y", "x-bizgo-client": "z", "token": "t"})
    assert headers["Authorization"] == FAKE_API_KEY and headers["token"] == "t"
    assert {k.lower() for k in headers} == {
        "authorization",
        "accept",
        "accept-encoding",
        "user-agent",
        "x-bizgo-client",
        "token",
    }


def test_user_agent_has_no_host_or_user_details() -> None:
    agent = _send()["user-agent"]
    assert platform.node() not in agent or not platform.node()
    assert platform.release() not in agent.split("(", 1)[1] or not platform.release()
