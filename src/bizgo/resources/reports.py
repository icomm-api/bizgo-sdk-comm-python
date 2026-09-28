"""Delivery reports: ``/api/comm/v1/report/*``.

Pick one primary method in the console per API key: POLLING (this module) or WEBHOOK (see :mod:`bizgo.webhooks`).
Use :meth:`Reports.inquiry` to fill gaps.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any

from .._transport import Retry, validate
from ..models._generated_response import Report, ReportInquiryResponse, ReportPollingResponse
from ..models._results import ReportBatch
from ._generated import AsyncReportsBase, ReportsBase
from ._runtime import segment


def _batch(body: dict[str, Any]) -> ReportBatch:
    data = validate(ReportPollingResponse, body, "getReportPolling").data
    inner = data.data if data else None
    return ReportBatch(
        report_id=(inner.report_id or "") if inner else "", reports=list(inner.report or []) if inner else []
    )


def _inquiry(body: dict[str, Any]) -> list[Report]:
    data = validate(ReportInquiryResponse, body, "getReportInquiry").data
    return list(data.data.report or []) if data and data.data else []


def _segment(value: str) -> str:
    return segment(value)


class Reports(ReportsBase):
    """Delivery reports. Access as ``client.reports``."""

    def poll(self) -> ReportBatch:
        """Fetch the next batch of reports. ``batch.empty`` is True when there is nothing new.

        You must call :meth:`ack` with ``batch.report_id`` after storing the batch; otherwise the same
        reports are returned again. Prefer :meth:`consume`, which does this for you.
        """
        return _batch(
            self._transport.request(
                "GET", "/api/comm/v1/report/polling", retry=Retry.SAFE, operation="getReportPolling"
            )
        )

    def ack(self, report_id: str) -> None:
        """Confirm receipt of a polled batch."""
        self._transport.request(
            "DELETE",
            f"/api/comm/v1/report/polling/{_segment(report_id)}",
            retry=Retry.SAFE,
            operation="ackReportPolling",
        )

    def consume(self, handler: Callable[[list[Report]], None], *, max_batches: int | None = None) -> int:
        """Poll until no reports are left, calling ``handler`` for each batch and acking it only if the handler
        returns without raising. Returns the number of reports handled.

        If ``handler`` raises, the batch is not acked and will be delivered again, so make the handler
        idempotent (for example upsert by ``msg_key``).
        """
        handled = batches = 0
        while max_batches is None or batches < max_batches:
            batch = self.poll()
            if batch.empty:
                break
            handler(batch.reports)
            self.ack(batch.report_id)
            handled += len(batch.reports)
            batches += 1
        return handled

    def inquiry(self, msg_key: str) -> list[Report]:
        """Look up the reports of one message (up to 30 days old)."""
        return _inquiry(
            self._transport.request(
                "GET",
                f"/api/comm/v1/report/inquiry/{_segment(msg_key)}",
                retry=Retry.SAFE,
                operation="getReportInquiry",
            )
        )


class AsyncReports(AsyncReportsBase):
    """Async version of :class:`Reports`."""

    async def poll(self) -> ReportBatch:
        """See :meth:`Reports.poll`."""
        return _batch(
            await self._transport.request(
                "GET", "/api/comm/v1/report/polling", retry=Retry.SAFE, operation="getReportPolling"
            )
        )

    async def ack(self, report_id: str) -> None:
        """See :meth:`Reports.ack`."""
        await self._transport.request(
            "DELETE",
            f"/api/comm/v1/report/polling/{_segment(report_id)}",
            retry=Retry.SAFE,
            operation="ackReportPolling",
        )

    async def consume(
        self, handler: Callable[[list[Report]], Awaitable[None]], *, max_batches: int | None = None
    ) -> int:
        """See :meth:`Reports.consume`. ``handler`` is an async function."""
        handled = batches = 0
        while max_batches is None or batches < max_batches:
            batch = await self.poll()
            if batch.empty:
                break
            await handler(batch.reports)
            await self.ack(batch.report_id)
            handled += len(batch.reports)
            batches += 1
        return handled

    async def inquiry(self, msg_key: str) -> list[Report]:
        """See :meth:`Reports.inquiry`."""
        return _inquiry(
            await self._transport.request(
                "GET",
                f"/api/comm/v1/report/inquiry/{_segment(msg_key)}",
                retry=Retry.SAFE,
                operation="getReportInquiry",
            )
        )
