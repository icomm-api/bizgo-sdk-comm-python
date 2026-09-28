"""Send a Kakao AlimTalk message; if it fails, Bizgo sends the SMS instead (fallback)."""

import uuid

from _env import env

from bizgo import AlimtalkMessage, Bizgo, Destination, DuplicateRequestError, Environment, SmsMessage


def main(client: Bizgo, *, from_: str, to: str, sender_key: str, template_code: str) -> None:
    order_id = "20260923-0001"
    try:
        result = client.send.omni(
            to=[Destination(to=to, replace_words={"name": "홍길동", "order": order_id})],
            messages=[
                AlimtalkMessage(
                    sender_key=sender_key,
                    template_code=template_code,
                    msg_type="AT",
                    text="#{name}님, 주문(#{order})이 접수되었습니다.",  # must match the approved template
                ),
                SmsMessage(from_=from_, text="#{name}님, 주문(#{order})이 접수되었습니다."),
            ],
            # same key => a second send is not delivered again (recipients come back in result.duplicates)
            idempotency_key=f"order-{order_id}-{uuid.uuid5(uuid.NAMESPACE_URL, to)}",
            ref=order_id,
        )
    except DuplicateRequestError:
        print("이미 발송된 주문입니다.")
        return
    if result.duplicates:
        print("이미 발송된 주문입니다.")
        return
    print("접수:", result.msg_keys, "실패:", [d.code for d in result.failed])


if __name__ == "__main__":
    with Bizgo(environment=Environment.SANDBOX) as client:
        main(
            client,
            from_=env("BIZGO_FROM"),
            to=env("BIZGO_TO"),
            sender_key=env("BIZGO_KAKAO_SENDER_KEY"),
            template_code=env("BIZGO_KAKAO_TEMPLATE_CODE"),
        )
