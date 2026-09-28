from __future__ import annotations

from collections.abc import Iterator
from typing import Any

import pytest
import respx

from bizgo import AsyncBizgo, Bizgo, Environment

API_KEY = "test-api-key-not-real"
BASE = Environment.SANDBOX.value


def envelope(data: Any = None, *, code: str = "A000", ref: str | None = None) -> dict[str, Any]:
    body: dict[str, Any] = {
        "common": {"authCode": "A000", "authResult": "Success", "infobankTrId": "TR-TEST"},
        "data": {"code": code, "result": "Success" if code == "A000" else "Failed"},
    }
    if data is not None:
        body["data"]["data"] = data
    if ref is not None:
        body["data"]["ref"] = ref
    return body


@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Retries must not slow down the test suite; record the requested delays instead."""
    delays: list[float] = []

    async def fake_async_sleep(seconds: float) -> None:
        delays.append(seconds)

    monkeypatch.setattr("bizgo._transport.time.sleep", delays.append)
    monkeypatch.setattr("bizgo._transport.asyncio.sleep", fake_async_sleep)
    return delays


@pytest.fixture
def api() -> Iterator[respx.MockRouter]:
    with respx.mock(base_url=BASE, assert_all_called=False) as router:
        yield router


@pytest.fixture
def client() -> Iterator[Bizgo]:
    with Bizgo(API_KEY, environment=Environment.SANDBOX) as c:
        yield c


@pytest.fixture
async def aclient() -> Any:
    async with AsyncBizgo(API_KEY, environment=Environment.SANDBOX) as c:
        yield c
