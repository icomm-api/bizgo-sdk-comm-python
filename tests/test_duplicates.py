"""Per-recipient A301: recipients already accepted with the same idempotency key (SDK-DESIGN.md §12 rule 4)."""

from __future__ import annotations

import asyncio

import pytest

from bizgo import DuplicateRequestError, SmsMessage
from bizgo.models import SendDestinationResult
from bizgo.models._results import BulkSendResult, SendResult
from bizgo.testing import FakeTransport

PHONE = "01000001234"
MESSAGE = [SmsMessage(from_="01000000000", text="x")]


def _result(*codes: str) -> SendResult:
    return SendResult(
        destinations=[SendDestinationResult(to=PHONE, code=c, msg_key=f"K{i}") for i, c in enumerate(codes)]
    )


def test_a301_destinations_are_duplicates_not_failed_or_succeeded() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").duplicates()
    with fake.client() as client:
        result = client.send.omni(to=[PHONE, PHONE], messages=MESSAGE, idempotency_key="k-1")
    assert [d.code for d in result.duplicates] == ["A301", "A301"]
    assert result.failed == [] and result.succeeded == [] and result.msg_keys == []


def test_mixed_response_splits_succeeded_duplicates_failed() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").send_result("A000", "A301", "A306")
    with fake.client() as client:
        result = client.send.omni(to=[PHONE] * 3, messages=MESSAGE, idempotency_key="k-2")
    assert [d.code for d in result.succeeded] == ["A000"]
    assert [d.code for d in result.duplicates] == ["A301"]
    assert [d.code for d in result.failed] == ["A306"]
    assert len(result.msg_keys) == 1


def test_bulk_aggregates_duplicates_and_all_duplicate_chunk_is_not_an_error() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").duplicates().send_result("A000", "A301").send_result("A306")
    with fake.client() as client:
        result = client.send.bulk(
            to=[PHONE] * 5, messages=MESSAGE, chunk_size=2, concurrency=1, idempotency_key_prefix="notice"
        )
    assert result.errors == [] and all(r is not None for r in result.results)
    assert len(result.duplicates) == 3
    assert [d.code for d in result.succeeded] == ["A000"]
    assert [d.code for d in result.failed] == ["A306"]


def test_bulk_ok_is_true_when_only_duplicates() -> None:
    bulk = BulkSendResult(results=[_result("A301", "A301"), _result("A000")])
    assert bulk.ok and len(bulk.duplicates) == 2 and bulk.failed == []


def test_async_duplicates() -> None:
    async def run() -> SendResult:
        fake = FakeTransport()
        fake.on("sendOmni").send_result("A301")
        async with fake.async_client() as client:
            return await client.send.omni(to=PHONE, messages=MESSAGE, idempotency_key="k-3")

    result = asyncio.run(run())
    assert len(result.duplicates) == 1 and not result.failed


def test_request_level_a301_still_raises() -> None:
    fake = FakeTransport()
    fake.on("sendOmni").fail("service", 200, "A301")
    with fake.client() as client, pytest.raises(DuplicateRequestError):
        client.send.omni(to=PHONE, messages=MESSAGE, idempotency_key="k-4")


def test_duplicates_repr_masks_phone_numbers() -> None:
    result = _result("A301")
    assert PHONE not in repr(result.duplicates) and PHONE not in repr(result)
