"""SDK-DESIGN.md §12 rules 15-18 (added after the JS review), plus the cross-SDK rule 3 test vector."""

from __future__ import annotations

import io
import logging
import pathlib
from collections.abc import Iterator
from typing import Any

import httpx
import pytest

from bizgo import Bizgo, ConfigurationError, Hooks, InvalidResponseError, RequestEvent, SmsMessage
from bizgo.resources.send import bulk_idempotency_key
from bizgo.testing import FAKE_API_KEY, FakeTransport

MESSAGE = [SmsMessage(from_="01000000000", text="x")]


# ---------------------------------------------------------------- 3. cross-SDK test vector


def test_rule3_cross_sdk_idempotency_key_vector() -> None:
    recipients = ["01000000000", "01000000001", "01000000002"]
    assert bulk_idempotency_key("camp", 2, 0, recipients[0:2]) == "camp-2-0-32fe30d2"
    assert bulk_idempotency_key("camp", 2, 2, recipients[2:3]) == "camp-2-2-370752d8"
    fake = FakeTransport()
    with fake.client() as client:
        client.send.bulk(to=recipients, messages=MESSAGE, chunk_size=2, idempotency_key_prefix="camp", concurrency=1)
    assert [r.json["idempotencyKey"] for r in fake.requests] == ["camp-2-0-32fe30d2", "camp-2-2-370752d8"]


# ---------------------------------------------------------------- 15. user callbacks are isolated


class Raising(Hooks):
    def on_request_start(self, event: RequestEvent) -> None:
        raise RuntimeError("start boom")

    def on_request_end(self, event: RequestEvent) -> None:
        raise RuntimeError("end boom")


class AsyncHooks(Hooks):
    """``async def`` hooks: awaited by the async client, closed (never left un-awaited) by the sync client."""

    def __init__(self, fail: bool) -> None:
        self.fail = fail
        self.calls: list[str] = []

    async def on_request_start(self, event: RequestEvent) -> None:  # type: ignore[override]
        self.calls.append("start")
        if self.fail:
            raise RuntimeError("async start boom")

    async def on_request_end(self, event: RequestEvent) -> None:  # type: ignore[override]
        self.calls.append("end")
        if self.fail:
            raise RuntimeError("async end boom")


class RaisingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        raise RuntimeError("logger boom")


def test_rule15_raising_hooks_do_not_change_results_or_retries() -> None:
    fake = FakeTransport()
    fake.on("getMessageStatistics").respond(503, {}, {"retry-after": "0"}).default()
    with fake.client(hooks=Raising()) as client:
        assert client.messages.statistics("20260101") == []
        result = client.send.bulk(to=["01000000000"] * 3, messages=MESSAGE, chunk_size=2)
    assert len(fake.requests_for("getMessageStatistics")) == 2  # the retry still happened
    assert result.ok and len(result.msg_keys) == 3  # bulk results are intact


def test_rule15_async_hooks_on_the_sync_client_are_closed_not_leaked() -> None:
    # pytest runs with filterwarnings=error, so an un-awaited coroutine would fail this test
    hooks = AsyncHooks(fail=False)
    with FakeTransport().client(hooks=hooks) as client:
        assert client.send.sms(to="01000000000", from_="01000000000", text="x").msg_keys


async def test_rule15_async_hooks_are_awaited_and_their_errors_swallowed() -> None:
    ok, failing = AsyncHooks(fail=False), AsyncHooks(fail=True)
    async with FakeTransport().async_client(hooks=[failing, ok]) as client:
        result = await client.send.bulk(to=["01000000000"] * 3, messages=MESSAGE, chunk_size=2)
    assert result.ok and len(result.msg_keys) == 3
    assert ok.calls == ["start", "end", "start", "end"]
    assert failing.calls == ok.calls


def test_rule15_a_broken_logger_does_not_affect_requests() -> None:
    logger = logging.getLogger("bizgo")
    broken = RaisingFilter()
    old_level = logger.level
    logger.addFilter(broken)
    logger.setLevel(logging.DEBUG)
    try:
        with FakeTransport().client(hooks=Raising()) as client:
            assert client.reports.inquiry("K") == []
    finally:
        logger.removeFilter(broken)
        logger.setLevel(old_level)


# ---------------------------------------------------------------- 16. API key format


@pytest.mark.parametrize(
    "key",
    [f"{FAKE_API_KEY}\n", f" {FAKE_API_KEY}", f"{FAKE_API_KEY}\t", "key\x00x", "키-non-ascii", "Bearer x", "a b"],
    ids=["trailing-newline", "leading-space", "tab", "nul", "non-ascii", "bearer", "inner-space"],
)
def test_rule16_invalid_api_keys_are_rejected_not_stripped(key: str) -> None:
    with pytest.raises(ConfigurationError) as info:
        Bizgo(key)
    assert FAKE_API_KEY not in str(info.value) and key not in str(info.value)


def test_rule16_environment_key_with_newline_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BIZGO_API_KEY", f"{FAKE_API_KEY}\n")
    with pytest.raises(ConfigurationError):
        Bizgo()
    monkeypatch.setenv("BIZGO_API_KEY", FAKE_API_KEY)
    assert Bizgo()._config.api_key == FAKE_API_KEY


# ---------------------------------------------------------------- 17. redirects are never retried


@pytest.mark.parametrize("status", [301, 302, 307, 308])
def test_rule17_redirect_is_not_retried_even_for_safe_operations(status: int) -> None:
    calls: list[int] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(status, headers={"Location": "https://example.invalid/"})

    http = httpx.Client(transport=httpx.MockTransport(handler))
    client = Bizgo(FAKE_API_KEY, http_client=http, rate_limit=None, max_retries=2)
    with client, pytest.raises(InvalidResponseError) as info:
        client.reports.inquiry("K")  # SAFE retry policy
    assert calls == [1]
    assert info.value.http_status == status and f"HTTP {status}" in str(info.value) and "base_url" in str(info.value)


# ---------------------------------------------------------------- 18. unreadable upload files


def test_rule18_missing_file_is_a_validation_error_with_the_name_only(tmp_path: pathlib.Path) -> None:
    missing = tmp_path / "secret-dir" / "banner.jpg"
    fake = FakeTransport()
    with fake.client() as client, pytest.raises(ValueError) as info:
        client.files.upload_mms(missing)
    message = str(info.value)
    assert "banner.jpg" in message and "secret-dir" not in message and str(tmp_path) not in message
    assert not isinstance(info.value, OSError) and info.value.__cause__ is None
    assert fake.requests == []


def test_rule18_directory_and_generated_upload(tmp_path: pathlib.Path) -> None:
    with FakeTransport().client() as client:
        with pytest.raises(ValueError) as info:
            client.files.upload_alimtalk_template_image(tmp_path)
        assert str(tmp_path.parent) not in str(info.value)


class BrokenFile(io.RawIOBase):
    name = "/home/someone/private/report.pdf"

    def read(self, size: int = -1) -> bytes:
        raise PermissionError("denied: /home/someone/private/report.pdf")

    def __iter__(self) -> Iterator[bytes]:  # pragma: no cover - not used
        return iter(())


def test_rule18_unreadable_file_object(tmp_path: pathlib.Path) -> None:
    broken: Any = BrokenFile()
    with FakeTransport().client() as client, pytest.raises(ValueError) as info:
        client.counsel.files.upload(broken, sender_key="SENDER_KEY_EXAMPLE")
    assert "report.pdf" in str(info.value) and "/home/someone" not in str(info.value)
    assert "권한" in str(info.value)
