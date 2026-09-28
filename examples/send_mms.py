"""Upload an image, then send an MMS with it."""

import pathlib

from _env import env

from bizgo import Bizgo, Environment


def main(client: Bizgo, *, from_: str, to: str, image: bytes) -> None:
    uploaded = client.files.upload_mms(image, filename="banner.jpg")  # jpg, max 300KB
    if not uploaded.file_key:
        raise SystemExit("업로드 응답에 fileKey가 없습니다")
    result = client.send.mms(
        to=to, from_=from_, title="이벤트 안내", text="첨부 이미지를 확인해 주세요.", file_keys=[uploaded.file_key]
    )
    print("접수:", result.msg_keys, "파일 키 만료:", uploaded.expired)


if __name__ == "__main__":
    with Bizgo(environment=Environment.SANDBOX) as client:
        main(client, from_=env("BIZGO_FROM"), to=env("BIZGO_TO"), image=pathlib.Path(env("BIZGO_IMAGE")).read_bytes())
