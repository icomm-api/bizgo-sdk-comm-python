"""Message sending: ``POST /api/comm/v1/send/omni``."""

from __future__ import annotations

import asyncio
import hashlib
import re
from collections.abc import Iterable, Sequence
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from pydantic import ValidationError

from .._errors import ConfigurationError
from .._transport import Retry, validate
from ..models import _generated_request as req
from ..models._generated_response import SendOmniResponse
from ..models._results import BulkChunkError, BulkSendResult, SendResult
from ._common import ChannelMessage, Recipient, Recipients, build_send_request, with_default_ttl
from ._generated import AsyncSendBase, SendBase

PATH = "/api/comm/v1/send/omni"


def _result(body: dict[str, Any]) -> SendResult:
    response = validate(SendOmniResponse, body, "sendOmni")
    data = response.data
    inner = data.data if data else None
    return SendResult(
        destinations=list(inner.destinations or []) if inner else [],
        ref=data.ref if data else None,
        tracking_id=response.common.infobank_tr_id if response.common else None,
    )


def _payload(request: req.SendOmniRequest) -> dict[str, Any]:
    return with_default_ttl(req.SendOmniRequest, request.to_api())


def _retry(request: req.SendOmniRequest) -> Retry:
    # Without an idempotency key a retried send after a timeout could deliver twice.
    return Retry.SAFE if request.idempotency_key else Retry.RATE_LIMIT_ONLY


MAX_CHUNK = 200
_DEST_INDEX = re.compile(r"\bdestinations\[(\d+)\]")
MAX_KEY = 200


def _shift_destinations(message: str, start: int) -> str:
    """``destinations[i]`` in a chunk's error message -> the index in the caller's ``to`` list."""
    return _DEST_INDEX.sub(lambda m: f"destinations[{int(m[1]) + start}]", message)


def _recipient_number(recipient: Any) -> str:
    if isinstance(recipient, str):
        return recipient
    if isinstance(recipient, req.Destination):
        return str(recipient.to)
    if isinstance(recipient, dict):
        return str(recipient.get("to", ""))
    return str(getattr(recipient, "to", ""))


def bulk_idempotency_key(prefix: str, chunk_size: int, start: int, recipients: Sequence[Any]) -> str:
    """``<prefix>-<chunkSize>-<startIndex>-<hash8>`` (SDK-DESIGN.md §12.3).

    ``hash8`` is the first 8 hex digits of SHA-256 over the chunk's phone numbers in order, so re-running the same
    list with the same ``chunk_size`` reproduces the keys (no duplicate delivery), and a key is never reused for a
    different group of recipients (for example after changing ``chunk_size`` or the list).
    """
    digest = hashlib.sha256("\n".join(_recipient_number(r) for r in recipients).encode("utf-8")).hexdigest()
    return f"{prefix}-{chunk_size}-{start}-{digest[:8]}"


def _bulk_requests(
    *,
    to: Iterable[Recipient],
    messages: Sequence[Any],
    chunk_size: int,
    concurrency: int,
    idempotency_key_prefix: str | None,
    ref: str | None,
    group_key: str | None,
    payment_code: str | None,
    idempotency_ttl: int | None,
) -> list[tuple[int, int, int, req.SendOmniRequest]]:
    """Split and validate every chunk before anything is sent. Errors name indexes, never recipients."""
    if isinstance(chunk_size, bool) or not isinstance(chunk_size, int) or not 1 <= chunk_size <= MAX_CHUNK:
        raise ValueError(f"chunk_size는 1~{MAX_CHUNK}입니다")
    if isinstance(concurrency, bool) or not isinstance(concurrency, int) or concurrency < 1:
        raise ValueError("concurrency는 1 이상입니다")
    if idempotency_key_prefix is not None and (
        not isinstance(idempotency_key_prefix, str) or not idempotency_key_prefix
    ):
        raise ValueError("idempotency_key_prefix는 비어 있지 않은 문자열이어야 합니다")
    recipients = [to] if isinstance(to, (str, req.Destination, dict)) else list(to)
    if not recipients:
        raise ValueError("to: 수신자가 없습니다")
    chunks = []
    problems: list[str] = []
    for index, start in enumerate(range(0, len(recipients), chunk_size)):
        end = min(start + chunk_size, len(recipients))
        key = None
        if idempotency_key_prefix is not None:
            key = bulk_idempotency_key(idempotency_key_prefix, chunk_size, start, recipients[start:end])
            if len(key) > MAX_KEY:
                raise ValueError(f"idempotency_key_prefix가 너무 깁니다(생성된 키가 {MAX_KEY}자를 넘음)")
        try:
            request = build_send_request(
                to=recipients[start:end],
                messages=messages,
                ref=ref,
                group_key=group_key,
                payment_code=payment_code,
                idempotency_key=key,
                idempotency_ttl=idempotency_ttl,
            )
        except ValidationError as exc:
            for error in exc.errors(include_input=False, include_url=False, include_context=False):
                loc = list(error["loc"])
                if len(loc) > 1 and loc[0] == "destinations" and isinstance(loc[1], int):
                    loc[1] = loc[1] + start  # index in your ``to`` list
                # conditional-required rules name ``destinations[i]`` in the message: shift those indexes too
                msg = _shift_destinations(error["msg"], start)
                text = f"{'.'.join(str(part) for part in loc)}: {msg}" if loc else msg
                if text not in problems:
                    problems.append(text)
            continue
        chunks.append((index, start, end, request))
    if problems:
        raise ValueError("대량 발송 요청이 올바르지 않아 아무것도 보내지 않았습니다: " + "; ".join(problems[:20]))
    return chunks


def _bulk_result(outcomes: list[tuple[int, int, int, SendResult | Exception]]) -> BulkSendResult:
    outcomes.sort(key=lambda item: item[0])
    results: list[SendResult | None] = []
    errors: list[BulkChunkError] = []
    for index, start, end, outcome in outcomes:
        if isinstance(outcome, Exception):
            results.append(None)
            errors.append(BulkChunkError(chunk_index=index, start=start, end=end, error=outcome))
        else:
            results.append(outcome)
    return BulkSendResult(results=results, errors=errors)


_BULK_DOC = """Send one message to any number of recipients, in chunks of up to 200 (``send.omni`` per chunk).

        Every chunk is validated before the first one is sent (nothing is sent if one is invalid). A chunk that
        fails for any reason (API or network error, unreadable response, ...) does not stop the others and never
        loses the results already received: see ``result.errors`` (chunk index and recipient index range, never
        the numbers), ``result.failed`` (rejected recipients) and ``result.duplicates`` (recipients already accepted
        with the same idempotency key, ``A301``; not an error). Requests run ``concurrency`` at a time and share
        the client's rate limiter (send bucket).

        Args:
            to: Recipients (phone numbers, :class:`~bizgo.models.Destination` or dicts). No limit.
            messages: Channel messages in fallback order, as for :meth:`omni`.
            chunk_size: Recipients per request, 1-200 (default 200).
            concurrency: Requests in flight at once (default 4).
            idempotency_key_prefix: When set, each chunk is sent with the idempotency key
                ``<prefix>-<chunk_size>-<start index>-<hash8>`` (hash of the chunk's numbers). Re-run with the same
                list and the same ``chunk_size`` (within ``idempotency_ttl``): recipients of chunks already accepted
                come back in ``result.duplicates`` (``A301``) instead of being delivered twice. To resend only
                failed chunks, use the chunk numbers in
                ``errors``. Timeouts/5xx are retried. Without a prefix chunks are retried only on 429. The key must
                fit in 200 characters.
            ref, group_key, payment_code, idempotency_ttl: As for :meth:`omni` (the same for every chunk).
                With a prefix and no ``idempotency_ttl``, each chunk is sent with ``idempotencyTtl`` 86400.

        Returns:
            :class:`~bizgo.models.BulkSendResult`.

        Raises:
            ValueError: Invalid arguments or an invalid chunk (checked before anything is sent).
        """


class Send(SendBase):
    """Send messages. Access as ``client.send``."""

    def omni(
        self,
        *,
        to: Recipients,
        messages: Sequence[ChannelMessage | req.MessageFlowItem | dict[str, Any]],
        ref: str | None = None,
        group_key: str | None = None,
        payment_code: str | None = None,
        idempotency_key: str | None = None,
        idempotency_ttl: int | None = None,
    ) -> SendResult:
        """Send one message, with optional fallback channels, to up to 200 recipients.

        Args:
            to: Recipient phone number(s) or :class:`~bizgo.models.Destination` objects (for
                ``replace_words`` substitution or a per-recipient ``ref``). Max 200.
            messages: Channel messages in fallback order. If the first fails, the next is sent.
                Example: ``[AlimtalkMessage(...), SmsMessage(...)]``.
            ref: Your reference value; returned in reports.
            group_key: Groups messages in message insight statistics.
            payment_code: Department code for billing.
            idempotency_key: Up to 200 chars. Set it to make retries safe: a resend with the same key
                within ``idempotency_ttl`` seconds is not delivered twice: recipients already accepted come back in
                ``result.duplicates`` (per-recipient ``A301``; a request-level ``A301`` raises
                :class:`~bizgo.DuplicateRequestError`). It also enables automatic retry on timeouts.
            idempotency_ttl: Seconds (0-86400) the idempotency key is remembered. Default 86400
                (:data:`~bizgo.DEFAULT_IDEMPOTENCY_TTL`) when ``idempotency_key`` is set; ``0`` is sent as given.

        Returns:
            :class:`~bizgo.models.SendResult`. Check ``result.failed`` for rejected recipients;
                ``result.duplicates`` holds recipients already accepted with the same idempotency key.
            Final delivery results arrive later via ``client.reports``.

        Raises:
            pydantic.ValidationError: The request is invalid (checked before anything is sent).
            bizgo.APIError: Bizgo rejected the request.
            bizgo.APIConnectionError: Network failure; the message may or may not have been accepted.
        """
        request = build_send_request(
            to=to,
            messages=messages,
            ref=ref,
            group_key=group_key,
            payment_code=payment_code,
            idempotency_key=idempotency_key,
            idempotency_ttl=idempotency_ttl,
        )
        return self.request(request)

    def request(self, request: req.SendOmniRequest | dict[str, Any]) -> SendResult:
        """Send a prepared :class:`~bizgo.models.SendOmniRequest` (or an equivalent dict with API field names).

        If it has ``idempotencyKey`` but no ``idempotencyTtl``, 86400 (:data:`~bizgo.DEFAULT_IDEMPOTENCY_TTL`) is
        sent as the TTL (the request object itself is not changed).
        """
        if not isinstance(request, req.SendOmniRequest):
            request = req.SendOmniRequest.model_validate(request)
        return _result(
            self._transport.request("POST", PATH, json=_payload(request), retry=_retry(request), operation="sendOmni")
        )

    def sms(
        self, *, to: Recipients, from_: str, text: str, ref: str | None = None, idempotency_key: str | None = None
    ) -> SendResult:
        """Send an SMS: text up to 90 bytes in EUC-KR (about 45 Korean characters).

        ``from_`` must be a sender number registered in the Bizgo console.
        """
        return self.omni(
            to=to, messages=[req.SmsMessage(from_=from_, text=text)], ref=ref, idempotency_key=idempotency_key
        )

    def lms(
        self,
        *,
        to: Recipients,
        from_: str,
        text: str,
        title: str | None = None,
        ref: str | None = None,
        idempotency_key: str | None = None,
    ) -> SendResult:
        """Send an LMS (text up to 2,000 bytes in EUC-KR)."""
        message = req.MmsMessage(from_=from_, text=text, **({"title": title} if title else {}))
        return self.omni(to=to, messages=[message], ref=ref, idempotency_key=idempotency_key)

    def mms(
        self,
        *,
        to: Recipients,
        from_: str,
        text: str,
        file_keys: Sequence[str],
        title: str | None = None,
        ref: str | None = None,
        idempotency_key: str | None = None,
    ) -> SendResult:
        """Send an MMS. Get ``file_keys`` (max 3) from ``client.files.upload_mms()`` first."""
        message = req.MmsMessage(
            from_=from_, text=text, file_key=list(file_keys), **({"title": title} if title else {})
        )
        return self.omni(to=to, messages=[message], ref=ref, idempotency_key=idempotency_key)

    def bulk(
        self,
        *,
        to: Iterable[Recipient],
        messages: Sequence[ChannelMessage | req.MessageFlowItem | dict[str, Any]],
        chunk_size: int = MAX_CHUNK,
        concurrency: int = 4,
        idempotency_key_prefix: str | None = None,
        ref: str | None = None,
        group_key: str | None = None,
        payment_code: str | None = None,
        idempotency_ttl: int | None = None,
    ) -> BulkSendResult:
        chunks = _bulk_requests(
            to=to,
            messages=messages,
            chunk_size=chunk_size,
            concurrency=concurrency,
            idempotency_key_prefix=idempotency_key_prefix,
            ref=ref,
            group_key=group_key,
            payment_code=payment_code,
            idempotency_ttl=idempotency_ttl,
        )

        def run(chunk: tuple[int, int, int, req.SendOmniRequest]) -> tuple[int, int, int, SendResult | Exception]:
            index, start, end, request = chunk
            try:
                return index, start, end, self.request(request)
            except ConfigurationError:
                raise
            except Exception as error:  # every per-chunk failure is reported, never loses other chunks
                return index, start, end, error

        if concurrency == 1 or len(chunks) == 1:
            outcomes = [run(chunk) for chunk in chunks]
        else:
            with ThreadPoolExecutor(max_workers=min(concurrency, len(chunks)), thread_name_prefix="bizgo-bulk") as pool:
                outcomes = list(pool.map(run, chunks))
        return _bulk_result(outcomes)

    bulk.__doc__ = _BULK_DOC


class AsyncSend(AsyncSendBase):
    """Async version of :class:`Send`. Access as ``client.send``."""

    async def omni(
        self,
        *,
        to: Recipients,
        messages: Sequence[ChannelMessage | req.MessageFlowItem | dict[str, Any]],
        ref: str | None = None,
        group_key: str | None = None,
        payment_code: str | None = None,
        idempotency_key: str | None = None,
        idempotency_ttl: int | None = None,
    ) -> SendResult:
        """See :meth:`Send.omni`."""
        request = build_send_request(
            to=to,
            messages=messages,
            ref=ref,
            group_key=group_key,
            payment_code=payment_code,
            idempotency_key=idempotency_key,
            idempotency_ttl=idempotency_ttl,
        )
        return await self.request(request)

    async def request(self, request: req.SendOmniRequest | dict[str, Any]) -> SendResult:
        """See :meth:`Send.request`."""
        if not isinstance(request, req.SendOmniRequest):
            request = req.SendOmniRequest.model_validate(request)
        return _result(
            await self._transport.request(
                "POST", PATH, json=_payload(request), retry=_retry(request), operation="sendOmni"
            )
        )

    async def sms(
        self, *, to: Recipients, from_: str, text: str, ref: str | None = None, idempotency_key: str | None = None
    ) -> SendResult:
        """See :meth:`Send.sms`."""
        return await self.omni(
            to=to, messages=[req.SmsMessage(from_=from_, text=text)], ref=ref, idempotency_key=idempotency_key
        )

    async def lms(
        self,
        *,
        to: Recipients,
        from_: str,
        text: str,
        title: str | None = None,
        ref: str | None = None,
        idempotency_key: str | None = None,
    ) -> SendResult:
        """See :meth:`Send.lms`."""
        message = req.MmsMessage(from_=from_, text=text, **({"title": title} if title else {}))
        return await self.omni(to=to, messages=[message], ref=ref, idempotency_key=idempotency_key)

    async def mms(
        self,
        *,
        to: Recipients,
        from_: str,
        text: str,
        file_keys: Sequence[str],
        title: str | None = None,
        ref: str | None = None,
        idempotency_key: str | None = None,
    ) -> SendResult:
        """See :meth:`Send.mms`."""
        message = req.MmsMessage(
            from_=from_, text=text, file_key=list(file_keys), **({"title": title} if title else {})
        )
        return await self.omni(to=to, messages=[message], ref=ref, idempotency_key=idempotency_key)

    async def bulk(
        self,
        *,
        to: Iterable[Recipient],
        messages: Sequence[ChannelMessage | req.MessageFlowItem | dict[str, Any]],
        chunk_size: int = MAX_CHUNK,
        concurrency: int = 4,
        idempotency_key_prefix: str | None = None,
        ref: str | None = None,
        group_key: str | None = None,
        payment_code: str | None = None,
        idempotency_ttl: int | None = None,
    ) -> BulkSendResult:
        chunks = _bulk_requests(
            to=to,
            messages=messages,
            chunk_size=chunk_size,
            concurrency=concurrency,
            idempotency_key_prefix=idempotency_key_prefix,
            ref=ref,
            group_key=group_key,
            payment_code=payment_code,
            idempotency_ttl=idempotency_ttl,
        )
        gate = asyncio.Semaphore(concurrency)

        async def run(chunk: tuple[int, int, int, req.SendOmniRequest]) -> tuple[int, int, int, SendResult | Exception]:
            index, start, end, request = chunk
            async with gate:
                try:
                    return index, start, end, await self.request(request)
                except ConfigurationError:
                    raise
                except Exception as error:  # every per-chunk failure is reported, never loses other chunks
                    return index, start, end, error

        return _bulk_result(list(await asyncio.gather(*(run(chunk) for chunk in chunks))))

    bulk.__doc__ = _BULK_DOC
