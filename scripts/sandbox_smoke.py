"""End-to-end check of the SDK against the Bizgo **sandbox** (no real delivery).

Usage (values are read from the environment and never printed):
    BIZGO_API_KEY         API key
    BIZGO_TO              test recipient number
    BIZGO_CHANNEL         "alimtalk" (default) or "sms"
    alimtalk:
        BIZGO_SENDER_KEY      Kakao sender profile key
        BIZGO_TEMPLATE_CODE   approved AlimTalk template code
        BIZGO_TEMPLATE_TEXT   optional: the full message text (default: the template text with every
                              #{variable} replaced by "테스트")
    sms:
        BIZGO_FROM            registered sender number
    python scripts/sandbox_smoke.py

The report shows result codes, exception types, lengths and field names only, so it is safe to share.
It sends at most 6 requests to the sandbox: one valid (key + TTL), two probes (key with the SDK default TTL,
no key), one invalid, and two with the same idempotency key.
"""

from __future__ import annotations

import datetime as dt
import os
import re
import sys
import time
import uuid
from collections.abc import Callable, Sequence
from typing import Literal

import pydantic

import bizgo
from bizgo import AlimtalkMessage, Bizgo, Environment, SmsMessage
from bizgo.models import _generated_request as req

WAIT_SECONDS = 20
VARIABLE = re.compile(r"#\{[^}]+\}")

Message = AlimtalkMessage | SmsMessage


def need(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        sys.exit(f"환경변수 {name}를 설정하세요 (값은 출력되지 않습니다)")
    return value


def describe(error: BaseException) -> str:
    if isinstance(error, bizgo.APIError):
        fields = f"http={error.http_status}, layer={error.layer}, code={error.code}, desc={error.description}"
        return f"{type(error).__name__}({fields})"
    return type(error).__name__


def step(title: str) -> None:
    print(f"\n## {title}")


def alimtalk_factory(client: Bizgo) -> Callable[[], Message] | None:
    sender_key, template_code = need("BIZGO_SENDER_KEY"), need("BIZGO_TEMPLATE_CODE")
    step("0. 알림톡 템플릿 조회 (alimtalk.templates.get)")
    try:
        template = client.alimtalk.templates.get(sender_key=sender_key, template_code=template_code)
    except bizgo.BizgoError as error:
        print(f"- 실패: {describe(error)}")
        return None
    template_text = template.text or ""
    variables = len(VARIABLE.findall(template_text))
    print(f"- 검수 상태: {template.inspection_status}, 본문 길이: {len(template_text)}")
    print(f"- 변수 {variables}개, 첨부(버튼 등) 있음: {template.attachment is not None}")
    print(f"- 미정의 필드: {sorted(template.model_extra or {})}")
    # Variable values are free text; the rest must match the template. Fill them with a fixed test value.
    text = os.environ.get("BIZGO_TEMPLATE_TEXT") or VARIABLE.sub("테스트", template_text)
    if VARIABLE.search(text):
        print("- BIZGO_TEMPLATE_TEXT에 변수가 남아 있습니다. 변수를 채운 전체 본문을 넣으세요.")
        return None
    attachment = None
    if template.attachment is not None:
        try:
            attachment = req.AlimtalkAttachment.model_validate(
                template.attachment.model_dump(by_alias=True, exclude_none=True)
            )
        except pydantic.ValidationError:
            print("- 템플릿 첨부를 발송 형식으로 옮기지 못해 첨부 없이 보냅니다.")

    # msgType is required for a full (non-template) send (A523; the SDK checks it first). The template carries it.
    msg_type: Literal["AT", "AI"] = "AI" if template.msg_type == "AI" else "AT"
    print(f"- msgType: {msg_type}")

    def make() -> Message:
        return AlimtalkMessage(
            msg_type=msg_type, sender_key=sender_key, template_code=template_code, text=text, attachment=attachment
        )

    return make


def sms_factory() -> Callable[[], Message]:
    sender = need("BIZGO_FROM")

    def make() -> Message:
        return SmsMessage(from_=sender, text="[SDK 점검] sandbox 테스트 메시지")

    return make


def main() -> None:
    recipient = need("BIZGO_TO")
    need("BIZGO_API_KEY")
    channel = os.environ.get("BIZGO_CHANNEL", "alimtalk").strip().lower()
    if channel not in ("alimtalk", "sms"):
        sys.exit("BIZGO_CHANNEL은 alimtalk 또는 sms입니다")
    with Bizgo(environment=Environment.SANDBOX) as client:
        if client.base_url != Environment.SANDBOX.value:  # never production
            sys.exit("sandbox가 아닙니다")

        make = alimtalk_factory(client) if channel == "alimtalk" else sms_factory()
        if make is None:
            return

        step(f"1. {channel} 발송 (sandbox)")
        started = dt.datetime.now(dt.timezone.utc)
        try:
            result = client.send.omni(
                to=recipient,
                messages=[make()],
                ref="sdk-smoke",
                idempotency_key=f"sdk-smoke-{uuid.uuid4()}",
                idempotency_ttl=600,
            )
        except (bizgo.BizgoError, pydantic.ValidationError) as error:
            print(f"- 실패: {describe(error)}")
            return
        print(f"- 접수: {len(result.succeeded)}건, 거절: {[d.code for d in result.failed]} (idempotency_ttl=600)")
        for label, key in [("키만(SDK 기본 TTL)", f"sdk-smoke-{uuid.uuid4()}"), ("키 없음", None)]:
            time.sleep(0.3)
            try:
                probe = client.send.omni(to=recipient, messages=[make()], idempotency_key=key)
                print(f"- {label}: 접수 {len(probe.succeeded)}건, 거절 {[d.code for d in probe.failed]}")
            except (bizgo.BizgoError, pydantic.ValidationError) as error:
                print(f"- {label}: {describe(error)}")
        print(f"- ref 반환: {result.ref == 'sdk-smoke'}, tracking_id 있음: {bool(result.tracking_id)}")
        if not result.msg_keys:
            return
        msg_key = result.msg_keys[0]
        print(f"- msgKey 길이: {len(msg_key)}")

        step(f"2. 상태 조회 ({WAIT_SECONDS}초 대기 후)")
        time.sleep(WAIT_SECONDS)
        checks: list[tuple[str, Callable[[], Sequence[pydantic.BaseModel]]]] = [
            ("messages.status", lambda: client.messages.status(msg_key)),
            ("messages.status_by_request_id", lambda: client.messages.status_by_request_id(msg_key[:-3])),
            ("reports.inquiry", lambda: client.reports.inquiry(msg_key)),
        ]
        for name, call in checks:
            try:
                items = call()
                codes = [(getattr(i, "service_type", None), getattr(i, "report_code", None)) for i in items]
                extra = sorted({k for i in items for k in (i.model_extra or {})})
                print(f"- {name}: {len(items)}건 {codes} 미정의 필드={extra}")
            except bizgo.BizgoError as error:
                print(f"- {name}: {describe(error)}")
            time.sleep(0.3)

        step("3. 발송 이력에서 찾기")
        try:
            found = [
                m
                for m in client.messages.iter_history(started - dt.timedelta(minutes=1), limit=100)
                if m.msg_key == msg_key
            ]
            print(f"- iter_history에서 발견: {len(found)}건")
        except bizgo.BizgoError as error:
            print(f"- iter_history: {describe(error)}")

        step("4. 잘못된 요청의 실제 오류 형태")
        try:
            bad = client.send.omni(to="0", messages=[make()])
            print(f"- 잘못된 수신번호: 요청은 성공, 수신자별 코드={[d.code for d in bad.destinations]}")
        except (bizgo.BizgoError, pydantic.ValidationError) as error:
            print(f"- 잘못된 수신번호: {describe(error)}")
        duplicate_key = "sdk-smoke-dup-" + msg_key
        try:
            client.send.omni(to=recipient, messages=[make()], idempotency_key=duplicate_key, idempotency_ttl=600)
            again = client.send.omni(
                to=recipient, messages=[make()], idempotency_key=duplicate_key, idempotency_ttl=600
            )
            print(f"- 두 번째 응답 수신자별 코드: {[d.code for d in again.destinations]}")
            if again.duplicates:
                print(f"- 같은 idempotency_key 2회: duplicates {len(again.duplicates)}건 (중복 방지 동작)")
            else:
                print(
                    f"- 같은 idempotency_key 2회: duplicates 없음 (접수 {len(again.succeeded)}건, "
                    f"거절 {[d.code for d in again.failed]})"
                )
        except bizgo.BizgoError as error:
            print(f"- 같은 idempotency_key 2회: {describe(error)}")


if __name__ == "__main__":
    main()
