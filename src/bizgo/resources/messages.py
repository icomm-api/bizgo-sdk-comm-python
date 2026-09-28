"""Message status, history and statistics: ``/api/comm/v1/message/*``.

These are non-send APIs, limited to 5 requests per second by default.
"""

from __future__ import annotations

import datetime as dt
from collections.abc import AsyncIterator, Iterator, Sequence
from typing import Any

from .._transport import Retry, validate
from ..models._generated_response import (
    MessageStatistics,
    MessageStatisticsResponse,
    MessageStatus,
    MessageStatusListResponse,
    MoMessage,
    MoMessageListResponse,
)
from ..models._results import MessagePage, MoPage
from ._common import compact, local_time, offset_time, yyyymmdd
from ._generated import AsyncMessagesBase, MessagesBase
from .reports import _segment

ServiceType = str
"""``SMS``, ``MMS``, ``RCS``, ``ALIMTALK``, ``BRANDMESSAGE``."""


def _statuses(body: dict[str, Any]) -> list[MessageStatus]:
    data = validate(MessageStatusListResponse, body, "getMessageHistory").data
    return list(data.data.messages or []) if data and data.data else []


def _message_page(body: dict[str, Any]) -> MessagePage:
    data = validate(MessageStatusListResponse, body, "getMessageHistory").data
    inner = data.data if data else None
    if inner is None:
        return MessagePage(messages=[], last_seq=None, has_next=False)
    return MessagePage(messages=list(inner.messages or []), last_seq=inner.last_seq, has_next=bool(inner.has_next))


def _mo_page(body: dict[str, Any]) -> MoPage:
    data = validate(MoMessageListResponse, body, "getMoHistory").data
    inner = data.data if data else None
    if inner is None:
        return MoPage(messages=[], last_seq=None, has_next=False)
    return MoPage(messages=list(inner.messages or []), last_seq=inner.last_seq, has_next=bool(inner.has_next))


def _statistics(body: dict[str, Any]) -> list[MessageStatistics]:
    data = validate(MessageStatisticsResponse, body, "getMessageStatistics").data
    return list(data.data.statistics or []) if data and data.data else []


def _limit(limit: int | None) -> int | None:
    if limit is not None and not 1 <= limit <= 1000:
        raise ValueError("limit은 1~1000입니다")
    return limit


def _stats_params(start_date: Any, end_date: Any, service_type: Any, group_key: Any) -> dict[str, Any]:
    return compact(
        {
            "startDate": yyyymmdd(start_date),
            "endDate": yyyymmdd(end_date) if end_date is not None else None,
            "serviceType": service_type,
            "groupKey": group_key,
        }
    )


def _history_params(request_time: Any, service_type: Any, group_key: Any, last_seq: Any, limit: Any) -> dict[str, Any]:
    if service_type is not None and not isinstance(service_type, str):
        service_type = ",".join(service_type)
    return compact(
        {
            "requestTime": local_time(request_time),
            "serviceType": service_type,
            "groupKey": group_key,
            "lastSeq": last_seq,
            "limit": _limit(limit),
        }
    )


def _mo_params(occurred_time: Any, from_: Any, to: Any, last_seq: Any, limit: Any) -> dict[str, Any]:
    return compact(
        {
            "occurredTime": offset_time(occurred_time),
            "from": from_,
            "to": to,
            "lastSeq": last_seq,
            "limit": _limit(limit),
        }
    )


class Messages(MessagesBase):
    """Message status, history and statistics. Access as ``client.messages``."""

    def status(self, msg_key: str) -> list[MessageStatus]:
        """Acceptance/send/report status of one message. With fallback there is one entry per channel tried."""
        path = f"/api/comm/v1/message/inquiry/msgKey/{_segment(msg_key)}"
        return _statuses(self._transport.request("GET", path, retry=Retry.SAFE, operation="getMessageStatusByMsgKey"))

    def status_by_request_id(self, request_id: str) -> list[MessageStatus]:
        """Status of every message in one broadcast request.

        ``request_id`` is ``msg_key`` without its last 3 characters.
        """
        path = f"/api/comm/v1/message/inquiry/requestId/{_segment(request_id)}"
        return _statuses(
            self._transport.request("GET", path, retry=Retry.SAFE, operation="getMessageStatusByRequestId")
        )

    def statistics(
        self,
        start_date: dt.date | str,
        end_date: dt.date | str | None = None,
        *,
        service_type: ServiceType | None = None,
        group_key: str | None = None,
    ) -> list[MessageStatistics]:
        """Daily acceptance and report counts. Dates are ``datetime.date`` or ``"YYYYMMDD"``."""
        params = _stats_params(start_date, end_date, service_type, group_key)
        return _statistics(
            self._transport.request(
                "GET",
                "/api/comm/v1/message/statistics",
                params=params,
                retry=Retry.SAFE,
                operation="getMessageStatistics",
            )
        )

    def history(
        self,
        request_time: dt.datetime | str,
        *,
        service_type: ServiceType | Sequence[ServiceType] | None = None,
        group_key: str | None = None,
        last_seq: int | None = None,
        limit: int | None = None,
    ) -> MessagePage:
        """One page of send history from ``request_time`` (KST). Use :meth:`iter_history` to walk all pages."""
        params = _history_params(request_time, service_type, group_key, last_seq, limit)
        return _message_page(
            self._transport.request(
                "GET", "/api/comm/v1/message/history", params=params, retry=Retry.SAFE, operation="getMessageHistory"
            )
        )

    def iter_history(
        self,
        request_time: dt.datetime | str,
        *,
        service_type: ServiceType | Sequence[ServiceType] | None = None,
        group_key: str | None = None,
        limit: int | None = None,
    ) -> Iterator[MessageStatus]:
        """Iterate over all send history from ``request_time``, following ``lastSeq`` across pages."""
        last_seq: int | None = None
        while True:
            page = self.history(
                request_time, service_type=service_type, group_key=group_key, last_seq=last_seq, limit=limit
            )
            yield from page.messages
            if not page.has_next or page.last_seq is None or page.last_seq == last_seq:
                return
            last_seq = page.last_seq

    def mo(self, msg_key: str) -> list[MoMessage]:
        """Look up an MO (inbound) message by key."""
        path = f"/api/comm/v1/message/inquiry/mo/msgKey/{_segment(msg_key)}"
        return _mo_page(self._transport.request("GET", path, retry=Retry.SAFE, operation="getMoByMsgKey")).messages

    def mo_history(
        self,
        occurred_time: dt.datetime | str,
        *,
        from_: str | None = None,
        to: str | None = None,
        last_seq: int | None = None,
        limit: int | None = None,
    ) -> MoPage:
        """One page of MO history, newest first, from ``occurred_time`` (naive datetimes are taken as KST)."""
        params = _mo_params(occurred_time, from_, to, last_seq, limit)
        return _mo_page(
            self._transport.request(
                "GET", "/api/comm/v1/message/history/mo", params=params, retry=Retry.SAFE, operation="getMoHistory"
            )
        )

    def iter_mo_history(
        self,
        occurred_time: dt.datetime | str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
    ) -> Iterator[MoMessage]:
        """Iterate over all MO history pages."""
        last_seq: int | None = None
        while True:
            page = self.mo_history(occurred_time, from_=from_, to=to, last_seq=last_seq, limit=limit)
            yield from page.messages
            if not page.has_next or page.last_seq is None or page.last_seq == last_seq:
                return
            last_seq = page.last_seq


class AsyncMessages(AsyncMessagesBase):
    """Async version of :class:`Messages`."""

    async def status(self, msg_key: str) -> list[MessageStatus]:
        """See :meth:`Messages.status`."""
        path = f"/api/comm/v1/message/inquiry/msgKey/{_segment(msg_key)}"
        return _statuses(
            await self._transport.request("GET", path, retry=Retry.SAFE, operation="getMessageStatusByMsgKey")
        )

    async def status_by_request_id(self, request_id: str) -> list[MessageStatus]:
        """See :meth:`Messages.status_by_request_id`."""
        path = f"/api/comm/v1/message/inquiry/requestId/{_segment(request_id)}"
        return _statuses(
            await self._transport.request("GET", path, retry=Retry.SAFE, operation="getMessageStatusByRequestId")
        )

    async def statistics(
        self,
        start_date: dt.date | str,
        end_date: dt.date | str | None = None,
        *,
        service_type: ServiceType | None = None,
        group_key: str | None = None,
    ) -> list[MessageStatistics]:
        """See :meth:`Messages.statistics`."""
        params = _stats_params(start_date, end_date, service_type, group_key)
        return _statistics(
            await self._transport.request(
                "GET",
                "/api/comm/v1/message/statistics",
                params=params,
                retry=Retry.SAFE,
                operation="getMessageStatistics",
            )
        )

    async def history(
        self,
        request_time: dt.datetime | str,
        *,
        service_type: ServiceType | Sequence[ServiceType] | None = None,
        group_key: str | None = None,
        last_seq: int | None = None,
        limit: int | None = None,
    ) -> MessagePage:
        """See :meth:`Messages.history`."""
        params = _history_params(request_time, service_type, group_key, last_seq, limit)
        return _message_page(
            await self._transport.request(
                "GET", "/api/comm/v1/message/history", params=params, retry=Retry.SAFE, operation="getMessageHistory"
            )
        )

    async def iter_history(
        self,
        request_time: dt.datetime | str,
        *,
        service_type: ServiceType | Sequence[ServiceType] | None = None,
        group_key: str | None = None,
        limit: int | None = None,
    ) -> AsyncIterator[MessageStatus]:
        """See :meth:`Messages.iter_history`."""
        last_seq: int | None = None
        while True:
            page = await self.history(
                request_time, service_type=service_type, group_key=group_key, last_seq=last_seq, limit=limit
            )
            for message in page.messages:
                yield message
            if not page.has_next or page.last_seq is None or page.last_seq == last_seq:
                return
            last_seq = page.last_seq

    async def mo(self, msg_key: str) -> list[MoMessage]:
        """See :meth:`Messages.mo`."""
        path = f"/api/comm/v1/message/inquiry/mo/msgKey/{_segment(msg_key)}"
        return _mo_page(
            await self._transport.request("GET", path, retry=Retry.SAFE, operation="getMoByMsgKey")
        ).messages

    async def mo_history(
        self,
        occurred_time: dt.datetime | str,
        *,
        from_: str | None = None,
        to: str | None = None,
        last_seq: int | None = None,
        limit: int | None = None,
    ) -> MoPage:
        """See :meth:`Messages.mo_history`."""
        params = _mo_params(occurred_time, from_, to, last_seq, limit)
        return _mo_page(
            await self._transport.request(
                "GET", "/api/comm/v1/message/history/mo", params=params, retry=Retry.SAFE, operation="getMoHistory"
            )
        )

    async def iter_mo_history(
        self,
        occurred_time: dt.datetime | str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
    ) -> AsyncIterator[MoMessage]:
        """See :meth:`Messages.iter_mo_history`."""
        last_seq: int | None = None
        while True:
            page = await self.mo_history(occurred_time, from_=from_, to=to, last_seq=last_seq, limit=limit)
            for message in page.messages:
                yield message
            if not page.has_next or page.last_seq is None or page.last_seq == last_seq:
                return
            last_seq = page.last_seq
