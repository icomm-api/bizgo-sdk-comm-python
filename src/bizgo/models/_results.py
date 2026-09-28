"""Convenience result types returned by the resources."""

from __future__ import annotations

from dataclasses import dataclass, field

from ._generated_response import MessageStatus, MoMessage, Report, SendDestinationResult

DUPLICATE_CODE = "A301"
"""Per-recipient code for a recipient already accepted with the same idempotency key."""


@dataclass(frozen=True)
class SendResult:
    """Acceptance result of a send request.

    Acceptance is not delivery: the final result arrives later as a report (polling, webhook or inquiry).
    Always check :attr:`failed` — a request can succeed while some recipients were rejected.
    Recipients answered with ``A301`` were already accepted earlier with the same ``idempotency_key``: they are in
    :attr:`duplicates`, not in :attr:`failed` or :attr:`succeeded`.
    """

    destinations: list[SendDestinationResult]
    """Per-recipient acceptance results, in request order."""
    ref: str | None = None
    """The ``ref`` you sent with the request."""
    tracking_id: str | None = None
    """``common.infobankTrId`` for support inquiries."""

    @property
    def succeeded(self) -> list[SendDestinationResult]:
        """Recipients accepted with code ``A000``."""
        return [d for d in self.destinations if d.code == "A000"]

    @property
    def duplicates(self) -> list[SendDestinationResult]:
        """Recipients answered with ``A301``: already accepted by an earlier request with the same idempotency key.

        They are not sent again by this request and are neither :attr:`succeeded` nor :attr:`failed`. Retrying with
        the same key is safe: already-accepted recipients come back here.
        """
        return [d for d in self.destinations if d.code == DUPLICATE_CODE]

    @property
    def failed(self) -> list[SendDestinationResult]:
        """Recipients rejected at acceptance (not ``A000``, not ``A301``). They will not receive the message."""
        return [d for d in self.destinations if d.code not in ("A000", DUPLICATE_CODE)]

    @property
    def msg_keys(self) -> list[str]:
        """Message keys of accepted recipients, for report and status lookups."""
        return [d.msg_key for d in self.succeeded if d.msg_key]


@dataclass(frozen=True)
class ReportBatch:
    """One batch from report polling. Call ``client.reports.ack(batch.report_id)`` after you stored it."""

    report_id: str
    reports: list[Report] = field(default_factory=list)

    @property
    def empty(self) -> bool:
        return not self.reports


@dataclass(frozen=True)
class MessagePage:
    """One page of send history."""

    messages: list[MessageStatus]
    last_seq: int | None
    has_next: bool


@dataclass(frozen=True)
class MoPage:
    """One page of MO (inbound) history."""

    messages: list[MoMessage]
    last_seq: int | None
    has_next: bool


@dataclass(frozen=True)
class BulkChunkError:
    """One chunk of :meth:`bizgo.resources.send.Send.bulk` that failed as a whole.

    Only indexes are kept (never the recipients): ``start``/``end`` are positions in the ``to`` list you passed.
    """

    chunk_index: int
    start: int
    """Index of the first recipient of the chunk."""
    end: int
    """Index after the last recipient of the chunk (exclusive)."""
    error: Exception
    """The error of the chunk (:class:`bizgo.APIError`, :class:`bizgo.APIConnectionError`, ...)."""

    def __str__(self) -> str:
        where = f"chunk {self.chunk_index} (recipients {self.start}-{self.end - 1})"
        return f"{where}: {type(self.error).__name__}: {self.error}"


@dataclass(frozen=True)
class BulkSendResult:
    """Result of a bulk send. Check :attr:`errors` (failed chunks) and :attr:`failed` (rejected recipients).

    Recipients already accepted with the same idempotency key (``A301``) are in :attr:`duplicates`; a chunk whose
    recipients are all duplicates is not an error.
    """

    results: list[SendResult | None]
    """Per chunk, in order: the :class:`SendResult`, or ``None`` if the chunk failed (see :attr:`errors`)."""
    errors: list[BulkChunkError] = field(default_factory=list)

    @property
    def succeeded(self) -> list[SendDestinationResult]:
        """Recipients accepted with ``A000`` across all chunks."""
        return [d for r in self.results if r for d in r.succeeded]

    @property
    def duplicates(self) -> list[SendDestinationResult]:
        """Recipients already accepted with the same idempotency key (``A301``) across all chunks."""
        return [d for r in self.results if r for d in r.duplicates]

    @property
    def failed(self) -> list[SendDestinationResult]:
        """Recipients rejected at acceptance across the chunks that were answered (failed chunks are in errors)."""
        return [d for r in self.results if r for d in r.failed]

    @property
    def msg_keys(self) -> list[str]:
        """Message keys of every accepted recipient."""
        return [k for r in self.results if r for k in r.msg_keys]

    @property
    def ok(self) -> bool:
        """``True`` when every chunk was answered and no recipient was rejected (duplicates are not rejections)."""
        return not self.errors and not self.failed
