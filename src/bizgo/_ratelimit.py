"""Client-side token buckets (SDK-DESIGN.md §11.2, §11.5).

Every client instance has two buckets:

- ``send``: default **200 messages per second, counted per recipient** (not per request). A send request costs
  ``len(destinations)`` tokens (minimum 1; a send without a recipient list, such as a brand message group send to
  a friend group, costs 1). So one 200-recipient request uses the whole second.
- ``other``: default 5 requests per second; every request costs 1.

The capacity (burst) of a bucket equals its per-second rate. Each HTTP attempt, retries included, waits until its
tokens are available (``time.sleep`` in the sync client, ``asyncio.sleep`` in the async client). A request that
costs more than the capacity (you lowered the rate below your chunk size) waits until the bucket is full and then
leaves the balance negative (debt), so it never deadlocks and the average rate still holds.

Operations in the ``send`` bucket are exactly those marked ``x-sdk-rate: send`` in the spec: currently
``sendOmni`` (so ``send.omni/request/sms/lms/mms/bulk``), ``createReservation``, ``addReservationRecipients``,
``createBrandMessageGroupSend`` and the counsel (상담톡) sends ``sendCounselPlain``/``sendCounselRich`` (cost 1 each:
no recipient list). See ``bizgo._operations.OPERATIONS[<id>].rate``.

The buckets start **full** (one second of burst): the Bizgo server also uses a token bucket (confirmed
2026-09-24, SDK-DESIGN.md §12.14). Its capacity is not documented and is assumed equal to the per-second limit;
HTTP 429 is still retried.

The Bizgo limit is per account, so these buckets only pace **one process**. Several processes or servers that share
a key need their own coordination; HTTP 429 is still retried (§6).
"""

from __future__ import annotations

import asyncio
import math
import threading
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any, Literal

Bucket = Literal["send", "other"]


@dataclass(frozen=True)
class RateLimit:
    """Per-second limits of the two buckets. Pass ``rate_limit=None`` to the client to turn limiting off."""

    send: float = 200.0
    """Send APIs: messages (recipients) per second (default 200)."""
    other: float = 5.0
    """Every other API: requests per second (default 5)."""

    def __post_init__(self) -> None:
        for name in ("send", "other"):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
                raise ValueError(f"RateLimit.{name}는 0보다 큰 숫자(초당 한도)여야 합니다")


class TokenBucket:
    """Holds up to ``rate`` tokens (one second of burst), refilled continuously at ``rate`` per second.

    Callers reserve tokens in call order: the balance may go negative and each caller waits until its own tokens
    have been refilled. Thread-safe.
    """

    def __init__(self, rate: float, clock: Callable[[], float] = time.monotonic) -> None:
        self.rate = float(rate)
        self.capacity = self.rate
        self._clock = clock
        self._tokens = self.capacity
        self._updated = clock()
        self._lock = threading.Lock()

    def reserve(self, cost: float = 1.0) -> float:
        """Take ``cost`` tokens and return how many seconds the caller must wait before sending.

        The caller goes when the balance reaches ``min(cost, capacity)``; the rest is left as debt.
        """
        cost = max(float(cost), 1.0)
        with self._lock:
            now = self._clock()
            self._tokens = min(self.capacity, self._tokens + (now - self._updated) * self.rate)
            self._updated = now
            need = min(cost, self.capacity)
            wait = max(0.0, (need - self._tokens) / self.rate)
            self._tokens -= cost
            return wait


def request_cost(bucket: Bucket, json: Any) -> int:
    """Tokens one attempt costs: recipients for the send bucket (minimum 1), 1 otherwise."""
    if bucket != "send" or not isinstance(json, dict):
        return 1
    destinations = json.get("destinations")
    return max(len(destinations), 1) if isinstance(destinations, list) else 1


def _sleep(seconds: float) -> None:
    time.sleep(seconds)


async def _async_sleep(seconds: float) -> None:
    await asyncio.sleep(seconds)


class RateLimiter:
    """The two buckets of one client. ``clock``/``sleep`` can be replaced in tests."""

    def __init__(
        self,
        limits: RateLimit,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], None] = _sleep,
        async_sleep: Callable[[float], Awaitable[None]] = _async_sleep,
    ) -> None:
        self.limits = limits
        self.buckets: dict[str, TokenBucket] = {
            "send": TokenBucket(limits.send, clock),
            "other": TokenBucket(limits.other, clock),
        }
        self._sleep = sleep
        self._async_sleep = async_sleep

    def wait(self, bucket: Bucket, cost: int = 1) -> None:
        delay = self.buckets[bucket].reserve(cost)
        if delay > 0:
            self._sleep(delay)

    async def await_(self, bucket: Bucket, cost: int = 1) -> None:
        delay = self.buckets[bucket].reserve(cost)
        if delay > 0:
            await self._async_sleep(delay)


def build(rate_limit: RateLimit | None) -> RateLimiter | None:
    if rate_limit is None:
        return None
    if not isinstance(rate_limit, RateLimit):
        raise TypeError("rate_limit은 bizgo.RateLimit(send=..., other=...) 또는 None이어야 합니다")
    return RateLimiter(rate_limit)
