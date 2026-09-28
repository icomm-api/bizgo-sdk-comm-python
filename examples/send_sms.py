"""Send an SMS and check the per-recipient acceptance result."""

from _env import env

from bizgo import Bizgo, Environment


def main(client: Bizgo, *, from_: str, to: str) -> None:
    result = client.send.sms(to=to, from_=from_, text="[비즈고] 인증번호는 123456 입니다.", ref="signup-otp")

    for rejected in result.failed:  # accepted != delivered; rejected recipients never get the message
        print("접수 실패:", rejected.code, rejected.result)
    print("접수된 메시지 키:", result.msg_keys)  # final delivery result comes later as a report


if __name__ == "__main__":
    with Bizgo(environment=Environment.SANDBOX) as client:  # API key from BIZGO_API_KEY
        main(client, from_=env("BIZGO_FROM"), to=env("BIZGO_TO"))
