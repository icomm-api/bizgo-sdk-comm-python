"""Client-side rate limiting (per-recipient send bucket, fake clock) and send.bulk (SDK-DESIGN.md §11.1, §11.2)."""

from __future__ import annotations

import re
import threading
from typing import Any

import pytest

from bizgo import (
    AuthenticationError,
    Bizgo,
    BulkSendResult,
    InternalServerError,
    RateLimit,
    SmsMessage,
)
from bizgo._ratelimit import RateLimiter, TokenBucket, request_cost
from bizgo.models import _generated_request as req
from bizgo.testing import FakeTransport

NUMBERS = [f"010{i:08d}" for i in range(1000)]  # placeholder-style numbers generated for the test only
MESSAGE = SmsMessage(from_="01000000000", text="hello")


class FakeClock:
    """A monotonic clock that only moves when the limiter sleeps."""

    def __init__(self) -> None:
        self.now = 1000.0
        self.slept: list[float] = []
        self._lock = threading.Lock()

    def __call__(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        with self._lock:
            self.slept.append(seconds)
            self.now += seconds

    async def async_sleep(self, seconds: float) -> None:
        self.sleep(seconds)


def limited_client(fake: FakeTransport, clock: FakeClock, limits: RateLimit | None = None) -> Bizgo:
    client = fake.client()
    client._transport._limiter = RateLimiter(
        limits or RateLimit(), clock=clock, sleep=clock.sleep, async_sleep=clock.async_sleep
    )
    return client


# ---------------------------------------------------------------- token bucket


def test_full_send_uses_the_whole_second_and_next_waits_one_second() -> None:
    clock = FakeClock()
    bucket = TokenBucket(200, clock)
    assert bucket.reserve(200) == 0.0  # a 200-recipient send consumes the full second
    assert bucket.reserve(200) == pytest.approx(1.0)  # the next one goes ~1s later


def test_single_recipient_is_not_delayed_by_an_idle_bucket() -> None:
    clock = FakeClock()
    bucket = TokenBucket(200, clock)
    assert bucket.reserve(200) == 0.0
    clock.now += 5  # idle: refilled to capacity (not beyond)
    assert bucket.reserve(1) == 0.0
    assert bucket.reserve(199) == 0.0
    assert bucket.reserve(1) > 0


def test_cost_above_capacity_does_not_deadlock_and_keeps_the_average() -> None:
    clock = FakeClock()
    bucket = TokenBucket(100, clock)  # rate lowered below the chunk size
    first = bucket.reserve(200)
    assert first == 0.0  # waits only until the bucket is full, then leaves debt
    second = bucket.reserve(200)
    assert second == pytest.approx(2.0)  # 400 messages over ~2s at 100/s


def test_other_bucket_counts_requests() -> None:
    clock = FakeClock()
    bucket = TokenBucket(5, clock)
    waits = [bucket.reserve(1) for _ in range(6)]
    assert waits[:5] == [0.0] * 5 and waits[5] == pytest.approx(0.2)


def test_request_cost() -> None:
    assert request_cost("send", {"destinations": [{"to": "01000000000"}] * 3}) == 3
    assert request_cost("send", {"senderKey": "SENDER_KEY_EXAMPLE"}) == 1  # no recipient list (friend group)
    assert request_cost("send", None) == 1
    assert request_cost("other", {"destinations": [{}] * 3}) == 1


@pytest.mark.parametrize("value", [0, -1, float("inf"), True, "5"])
def test_invalid_rate_limit(value: Any) -> None:
    with pytest.raises(ValueError):
        RateLimit(send=value)


def test_rate_limit_can_be_disabled_and_is_on_by_default() -> None:
    assert Bizgo("test-api-key-not-real")._transport._limiter is not None
    assert Bizgo("test-api-key-not-real", rate_limit=None)._transport._limiter is None
    with pytest.raises(TypeError):
        Bizgo("test-api-key-not-real", rate_limit={"send": 1})  # type: ignore[arg-type]


# ---------------------------------------------------------------- through the client


def test_two_full_sends_are_about_one_second_apart() -> None:
    fake, clock = FakeTransport(), FakeClock()
    with limited_client(fake, clock) as client:
        client.send.omni(to=NUMBERS[:200], messages=[MESSAGE])
        assert clock.slept == []
        client.send.omni(to=NUMBERS[200:400], messages=[MESSAGE])
    assert sum(clock.slept) == pytest.approx(1.0)


def test_every_attempt_waits_including_retries() -> None:
    fake, clock = FakeTransport(), FakeClock()
    fake.on("getMessageStatistics").respond(503, {}, {"retry-after": "0"}).default()
    with limited_client(fake, clock, RateLimit(other=1)) as client:
        client.messages.statistics("20260101")
    assert len(fake.requests) == 2
    assert sum(clock.slept) == pytest.approx(1.0)  # the retry took its own token


def test_counsel_send_uses_the_send_bucket_with_cost_one() -> None:
    fake, clock = FakeTransport(), FakeClock()
    with limited_client(fake, clock, RateLimit(send=2, other=1000)) as client:
        for _ in range(3):
            client.counsel.messages.send_plain(req.CounselPlainMessageRequest.model_construct())
    assert sum(clock.slept) == pytest.approx(0.5)  # 3 requests at 2/s: capacity 2, third waits 0.5s


# ---------------------------------------------------------------- bulk


def test_bulk_chunks_with_idempotency_key_per_chunk() -> None:
    fake = FakeTransport()
    with fake.client() as client:
        result = client.send.bulk(
            to=NUMBERS[:450], messages=[MESSAGE], chunk_size=200, concurrency=3, idempotency_key_prefix="job-42"
        )
    assert isinstance(result, BulkSendResult)
    sent = sorted(fake.requests_for("sendOmni"), key=lambda r: int(r.json["idempotencyKey"].split("-")[3]))
    assert [len(r.json["destinations"]) for r in sent] == [200, 200, 50]
    keys = [r.json["idempotencyKey"] for r in sent]
    assert [k.rsplit("-", 1)[0] for k in keys] == ["job-42-200-0", "job-42-200-200", "job-42-200-400"]
    assert all(re.fullmatch(r"job-42-200-\d+-[0-9a-f]{8}", k) for k in keys)
    assert result.ok and len(result.msg_keys) == 450 and len(result.results) == 3


def test_bulk_without_prefix_sends_no_idempotency_key() -> None:
    fake = FakeTransport()
    with fake.client() as client:
        client.send.bulk(to=NUMBERS[:3], messages=[MESSAGE], chunk_size=2)
    assert all("idempotencyKey" not in r.json for r in fake.requests)


def test_bulk_partial_failure_keeps_going_and_hides_numbers() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").send_result("A000", "A000").fail("gateway", 500, "A500").send_result("A000", "A306")
    with fake.client(max_retries=0) as client:
        result = client.send.bulk(to=NUMBERS[:6], messages=[MESSAGE], chunk_size=2, concurrency=1)
    assert [r is None for r in result.results] == [False, True, False]
    assert len(result.errors) == 1
    error = result.errors[0]
    assert (error.chunk_index, error.start, error.end) == (1, 2, 4)
    assert isinstance(error.error, InternalServerError)
    assert len(result.succeeded) == 3 and len(result.failed) == 1 and not result.ok
    text = str(error) + repr(error) + str(result.errors)
    assert not any(number in text for number in NUMBERS[:6])
    assert "recipients 2-3" in str(error)


def test_bulk_validates_every_chunk_before_sending() -> None:
    fake = FakeTransport()
    recipients: list[Any] = [*NUMBERS[:3], {"to": "01000000000", "unknown": 1}]
    with fake.client() as client, pytest.raises(ValueError) as info:
        client.send.bulk(to=recipients, messages=[MESSAGE], chunk_size=2)
    assert fake.requests == []  # nothing was sent
    assert "destinations.3" in str(info.value)  # index in *your* list, not the chunk
    assert "01000000000" not in str(info.value)


@pytest.mark.parametrize(
    "kwargs",
    [{"chunk_size": 0}, {"chunk_size": 201}, {"concurrency": 0}, {"idempotency_key_prefix": ""}],
)
def test_bulk_rejects_bad_options(kwargs: dict[str, Any]) -> None:
    with FakeTransport().client() as client, pytest.raises(ValueError):
        client.send.bulk(to=NUMBERS[:2], messages=[MESSAGE], **kwargs)


def test_bulk_of_1000_takes_about_four_seconds_of_fake_time() -> None:
    fake, clock = FakeTransport(), FakeClock()
    with limited_client(fake, clock) as client:
        result = client.send.bulk(to=NUMBERS, messages=[MESSAGE], concurrency=1)
    assert len(result.msg_keys) == 1000
    assert 4.0 <= clock.now - 1000.0 <= 5.0  # 5 chunks of 200 at 200 messages/s


def test_bulk_concurrency_does_not_raise_the_send_rate() -> None:
    clock = FakeClock()
    limiter = RateLimiter(RateLimit(), clock=clock, sleep=lambda s: clock.slept.append(s))
    fake = FakeTransport()
    with fake.client() as client:
        client._transport._limiter = limiter
        client.send.bulk(to=NUMBERS, messages=[MESSAGE], concurrency=4)
    # the clock does not move here, so each chunk waits for its own reserved slot: 0, 1, 2, 3, 4 seconds
    assert sorted(round(s, 6) for s in clock.slept) == [1.0, 2.0, 3.0, 4.0]


async def test_async_bulk_partial_failure() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").default().fail("gateway", 401, "A401").default()
    async with fake.async_client() as client:
        result = await client.send.bulk(to=NUMBERS[:5], messages=[MESSAGE], chunk_size=2, concurrency=1)
    assert len(result.results) == 3 and result.results[1] is None
    assert isinstance(result.errors[0].error, AuthenticationError)
    assert len(result.msg_keys) == 3


async def test_async_rate_limit_waits_without_blocking() -> None:
    fake, clock = FakeTransport(), FakeClock()
    async with fake.async_client() as client:
        client._transport._limiter = RateLimiter(
            RateLimit(), clock=clock, sleep=clock.sleep, async_sleep=clock.async_sleep
        )
        await client.send.omni(to=NUMBERS[:200], messages=[MESSAGE])
        await client.send.omni(to=NUMBERS[:1], messages=[MESSAGE])
    assert sum(clock.slept) == pytest.approx(1 / 200)
