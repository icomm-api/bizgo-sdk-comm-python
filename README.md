# bizgo-sdk-comm (Python)

[비즈고(Bizgo)](https://bizgo.io) 커뮤니케이션 API의 Python SDK입니다.
SMS/LMS/MMS, 국제문자, RCS, 카카오 알림톡·브랜드메시지, 네이버 톡톡을 하나의 클라이언트로 발송하고, 리포트·이력·통계를 조회하고, 웹훅을 검증합니다.
예약 발송, 발신프로필·템플릿 관리, 브랜드메시지 동보, RCS 브랜드·템플릿, 인사이트, 카카오 상담톡까지 **API 전체(146개 operation)** 를 지원합니다.

- Python 3.10 이상 · 동기(`Bizgo`)와 비동기(`AsyncBizgo`) 클라이언트 · 전체 타입 힌트(`py.typed`)
- 요청 모델은 보내기 전에 검증합니다: 필수 필드, 오타 필드, **바이트 길이**(SMS 90byte 등), EUC-KR 범위 밖 문자, 발송 방식·타입별 조건부 필수 필드(스펙의 `x-sdk-required-if`)
- 편의 기능: 대량 발송(`send.bulk`), 클라이언트 속도 제한, 테스트 도구(`bizgo.testing`), hooks·OpenTelemetry
- 스펙: [bizgo-api-spec](https://github.com/icomm-api/bizgo-api-spec) (OpenAPI 3.1) · 원문: [API 레퍼런스](https://developers.bizgo.io/api-sdk/api-reference)

> 이전 `infobank-omni-sdk-python`(OMNI API, ID/PW 인증)을 쓰고 있다면 [이전 SDK에서 옮기기](#이전-sdk에서-옮기기)를 참고하세요.

## 설치

```bash
pip install bizgo-sdk-comm
# 버전 고정: pip install bizgo-sdk-comm==1.2.0
```

## 시작하기

1. 콘솔 `발송관리 > 연동관리`에서 **API Key**를 발급하고, 호출할 서버의 **공인 IP를 등록**합니다.
2. 키를 환경변수로 설정합니다. 키는 코드나 저장소에 쓰지 않습니다.

```bash
export BIZGO_API_KEY=...
```

3. sandbox(실제 발송 없음)에서 먼저 확인합니다.

```python
from bizgo import Bizgo, Environment

with Bizgo(environment=Environment.SANDBOX) as client:  # 키는 BIZGO_API_KEY에서 읽음
    result = client.send.sms(to="01000000000", from_="01000000000", text="[비즈고] 인증번호는 123456 입니다.")

print(result.msg_keys)  # 접수된 메시지 키
print(result.failed)  # 접수 단계에서 거절된 수신자 (없으면 [])
print(result.duplicates)  # 같은 idempotency_key로 이미 접수된 수신자(A301). 거절이 아니며 다시 발송되지 않음
```

운영에 보낼 때는 `environment`를 생략하거나 `Environment.PRODUCTION`을 씁니다.

> **접수 ≠ 발송 완료.** `send.*`의 결과는 접수 결과입니다. 최종 결과는 [리포트](#리포트)로 받습니다.

## 발송

모든 채널은 `client.send.omni()` 하나로 보냅니다. `messages`에 여러 개를 넣으면 **앞 메시지가 실패할 때 다음 메시지로 대체발송**됩니다.

```python
from bizgo import AlimtalkMessage, Destination, SmsMessage

result = client.send.omni(
    to=[Destination(to="01000000000", replace_words={"name": "홍길동"})],  # 최대 200명
    messages=[
        AlimtalkMessage(sender_key="...", template_code="...", msg_type="AT", text="#{name}님, 주문이 접수되었습니다."),
        SmsMessage(from_="01000000000", text="#{name}님, 주문이 접수되었습니다."),  # 알림톡 실패 시
    ],
    idempotency_key="order-20260923-0001",  # 권장: 재시도해도 중복 발송되지 않음
    ref="order-20260923-0001",  # 리포트에 그대로 돌아오는 참조값
)
```

`idempotency_key`를 주고 `idempotency_ttl`을 생략하면 SDK가 `idempotencyTtl`을 `bizgo.DEFAULT_IDEMPOTENCY_TTL`(86400초 = 24시간)로 채워 보냅니다(비즈고는 키만 있고 TTL이 없으면 A309로 거절). 직접 준 값(0~86400, `0` 포함)은 그대로 보내고, 키가 없으면 TTL도 보내지 않습니다. `send.bulk`의 청크 키와 `idempotencyKey`를 받는 생성 메서드(dict 본문 포함)에도 같은 규칙이 적용됩니다.

| 채널 | 모델 | 간편 메서드 |
|---|---|---|
| SMS (90byte) | `SmsMessage` | `send.sms()` |
| LMS (2,000byte) | `MmsMessage` (`file_key` 없음) | `send.lms()` |
| MMS | `MmsMessage` (`file_key` 최대 3개) | `send.mms()` |
| 국제문자 | `InternationalMessage` | |
| RCS | `RcsMessage` | |
| 카카오 알림톡 | `AlimtalkMessage` | |
| 카카오 브랜드메시지 | `BrandMessage` | |
| 네이버 톡톡 | `NaverTalkMessage` | |

필드 이름은 Python식(`sender_key`)과 API식(`senderKey`) 모두 쓸 수 있습니다. `from`은 예약어라 `from_`입니다.
모델에 없는 필드를 넣으면 보내기 전에 `pydantic.ValidationError`가 납니다.

발송 방식·타입에 따라 필수가 되는 필드도 보내기 전에 검사합니다(스펙의 `x-sdk-required-if`, 모델·dict 본문 모두). 오류에는 필드 경로와 조건만 나옵니다(예: `msgType: required when sendType != template`).

- 알림톡 전문 발송(`send_type` 생략 또는 `template`이 아님)은 `msg_type`(`"AT"` 텍스트형, `"AI"` 이미지형)과 `text`가 필수입니다(빠지면 서버가 A523으로 거절). 템플릿 조회 결과의 `template.msg_type`을 그대로 넣으면 됩니다.
- 템플릿 자동 치환 발송(`send_type="template"`, 알림톡·브랜드메시지)은 `msg_type`·`text` 없이 보내고, 모든 수신자에 `replace_words`가 있어야 합니다(`destinations[1].replaceWords: required when ...`).
- 그 밖에 브랜드메시지 `send_type`별 필드, 브랜드메시지 버튼 `WL`(`url_pc`·`url_mobile`)·`AL`(`url_mobile`), RCS `header="1"`이면 `footer`, 상담톡 메시지 타입별 첨부.

### 이미지

```python
uploaded = client.files.upload_mms("banner.jpg")  # jpg, 최대 300KB
if uploaded.file_key is None:  # 응답 모델의 필드는 Optional입니다
    raise RuntimeError("fileKey를 받지 못했습니다")
client.send.mms(to="01000000000", from_="01000000000", text="...", file_keys=[uploaded.file_key])

client.files.upload_rcs("card.png")  # → uploaded.media
client.files.upload_brand_message("wide.jpg", kind="wide")  # → uploaded.img_url
```

## 리포트

콘솔에서 API Key별로 리포트 수신 방식(POLLING 또는 WEBHOOK)을 정합니다.

**Polling** — 처리에 성공한 배치만 수신 확인합니다. 처리 함수가 예외를 내면 같은 배치를 다시 받습니다.

```python
from bizgo.models import Report


def save(reports: list[Report]) -> None:
    for r in reports:
        db.upsert(r.msg_key, r.report_code)  # 같은 리포트가 다시 올 수 있으니 upsert


client.reports.consume(save)
```

**Webhook** — 서명을 검증하고 5초 안에 `{"msgKey": ...}`로 응답합니다. 웹훅 secret은 비즈고에 요청해 별도로 받습니다.

```python
import os
from collections.abc import Mapping

from bizgo.webhooks import WebhookPayloadError, WebhookReceiver, WebhookVerificationError

receiver = WebhookReceiver(secret=os.environ["BIZGO_WEBHOOK_SECRET"])


def endpoint(headers: Mapping[str, str], body: bytes) -> tuple[int, dict[str, str]]:  # 웹 프레임워크 핸들러 안에서
    try:
        report = receiver.report(headers, body)
    except WebhookPayloadError:  # 본문이 JSON이 아니거나 필드가 문서와 다름
        return 400, {}
    except WebhookVerificationError:  # 서명·시각 검증 실패
        return 401, {}
    enqueue(report)  # 무거운 처리는 비동기로
    return 200, receiver.ack(report.msg_key)
```

> 웹훅 서명과 timestamp 허용 오차를 검증하세요. 운영 환경에서는 HTTPS, 비즈고 웹훅 발신 IP 허용 목록, `msgKey` 기준 중복 제거를 함께 적용하고, 중요한 판단은 리포트·상태 조회 API로 결과를 확인하세요.

**상담톡 웹훅** — `counsel_message`, `counsel_reference`, `counsel_expired_session`, `counsel_seen_info`, `counsel_personal_info`, `counsel_cert_result`, `counsel_result`. 응답은 `{"msgKey"}`가 아니라 `counsel_ack()`(`{"code": "A000", "result": "Success"}`)입니다.

상담톡 웹훅에는 서명이 없습니다(서명은 리포트·MO 웹훅에만 적용). SDK는 서명을 요구하거나 검사하지 않고, `X-IB-Timestamp`/`X-IB-Signature` 헤더가 와도 무시합니다. 본문 크기(1MB)·JSON 중첩(64단계)·타입 검사는 그대로 적용합니다. 웹훅 secret이 필요 없으므로 상담톡만 받는다면 모듈 함수 `parse_counsel_*`를 쓰세요.

```python
from bizgo.webhooks import WebhookPayloadError, counsel_ack, parse_counsel_message


def counsel_endpoint(body: bytes) -> tuple[int, dict[str, str]]:  # secret 없이 사용
    try:
        event = parse_counsel_message(body)
    except WebhookPayloadError:  # 본문이 JSON이 아니거나 필드가 문서와 다름
        return 400, {}
    enqueue(event)
    return 200, counsel_ack()
```

- 리포트·MO와 같은 `WebhookReceiver`를 이미 쓴다면 `receiver.counsel_message(headers, body)`도 같은 동작입니다(서명 검사 없음). 리포트·MO 웹훅은 항상 서명이 필요합니다.
- 운영 환경에서는 HTTPS, 비즈고 웹훅 발신 IP 허용 목록, `msgKey`가 있는 이벤트는 `msgKey` 기준 중복 제거를 적용하세요.
- 본문에는 사용자 식별자·상담 내용·개인정보(`counsel_personal_info`, `counsel_cert_result`)가 들어 있습니다. 로그·APM·에러 리포트에 남기지 마세요.

**개별 조회** — `client.reports.inquiry(msg_key)` (30일 이내)

## 조회

```python
import datetime as dt

client.messages.status(msg_key)  # 단건 상태 (대체발송 시 채널별 항목)
client.messages.status_by_request_id(request_id)  # 동보 요청 전체 (msg_key에서 끝 3자리를 뺀 값)
client.messages.statistics(dt.date(2026, 9, 1), dt.date(2026, 9, 23), service_type="SMS")

for m in client.messages.iter_history(dt.datetime(2026, 9, 23, 9, 0), service_type=["SMS", "ALIMTALK"]):
    ...  # 페이지(lastSeq)를 자동으로 따라감

for mo in client.messages.iter_mo_history(dt.datetime(2026, 9, 23, 9, 0)):
    ...  # MO(수신) 이력
```

조회 API의 기본 호출 한도는 초당 5회입니다(클라이언트가 [속도 제한](#속도-제한)으로 맞춥니다).

## 전체 API

위의 발송·파일·리포트·조회 외에 **스펙의 모든 operation(146개)** 을 `client.<리소스>.<메서드>(...)`로 호출할 수 있습니다.
메서드는 OpenAPI 스펙의 `x-sdk-*` 메타데이터에서 **생성**합니다(`scripts/generate_models.py`). 규칙은 모두 같습니다.

- 인자: 경로 파라미터(순서대로, 필수, URL 인코딩) → 요청 본문(모델 또는 API 필드 이름의 dict, 보내기 전에 검증) → 쿼리·헤더 파라미터(키워드 전용). multipart 업로드는 `file`(경로·bytes·파일 객체)과 키워드 인자로 받습니다.
- 반환: 스펙이 정한 응답 부분(`x-sdk-result`, 기본 `data.data`)의 모델. 성공 응답에 데이터가 없어도 `None`이 아니라 빈 객체(목록은 `[]`)를 돌려줍니다. 원래 반환값이 없는 operation(삭제 등)만 `None`입니다.
- 재시도: 스펙의 `x-sdk-retry` (`safe` = 429·5xx·네트워크 오류, `rate_limit_only` = 429만).
- 목록 API에 페이지 규칙(`x-sdk-pagination`)이 있으면 `iter_<메서드>()`가 페이지를 자동으로 따라갑니다.
- 날짜 파라미터는 `datetime.date`/`datetime.datetime` 또는 문서 형식의 문자열을 받습니다.
- 동기(`Bizgo`)와 비동기(`AsyncBizgo`) 클라이언트에 같은 이름으로 있습니다.

```python
import datetime as dt

# 알림톡 템플릿
page = client.alimtalk.templates.list(sender_key="SENDER_KEY_EXAMPLE", limit=100)
for template in client.alimtalk.templates.iter_list(sender_key="SENDER_KEY_EXAMPLE"):
    print(template.template_code, template.template_name)
client.alimtalk.templates.delete("SENDER_KEY_EXAMPLE", "TEMPLATE_CODE_EXAMPLE")  # 경로 파라미터는 위치 인자

# 예약 발송: 결과에 resvKey와 수신자별 접수 결과가 함께 옵니다
reservation = client.reservations.create(
    {
        "destinations": [{"to": "01000000000"}],
        "messageFlow": [{"sms": {"from": "01000000000", "text": "예약 안내입니다."}}],
        "resvSendTime": "2026-10-01 10:00:00",
    }
)
if reservation.resv_key:  # 결과는 None이 아닌 객체(데이터가 없으면 빈 객체), 필드는 Optional
    client.reservations.cancel(reservation.resv_key)

# 알림톡 통계(인사이트)
client.insights.alimtalk.get(
    start_date=dt.date(2026, 9, 1), end_date=dt.date(2026, 9, 23), sender_key=["SENDER_KEY_EXAMPLE"]
)
```

| 리소스 | 메서드 (`*` = 직접 작성한 편의 메서드) |
|---|---|
| `client.send` | `omni*`, `request*`, `sms*`, `lms*`, `mms*`, `bulk*` |
| `client.files` | `upload_mms*`, `upload_rcs*`, `upload_brand_message*`(kind), `upload_brand_message_default`, `upload_brand_message_wide`, `upload_brand_message_wide_item_list`, `upload_brand_message_wide_item_list_first`, `upload_brand_message_carousel_feed`, `upload_brand_message_carousel_commerce`, `upload_brand_message_catalog`, `upload_brand_message_catalog_odd_first`, `upload_alimtalk_template_image`, `upload_alimtalk_item_highlight_image` |
| `client.reports` | `poll*`, `ack*`, `consume*`, `inquiry*` |
| `client.messages` | `status*`, `status_by_request_id*`, `statistics*`, `history*`, `iter_history*`, `mo*`, `mo_history*`, `iter_mo_history*` |
| `client.reservations` (예약 발송) | `create`, `list`/`iter_list`, `get`, `update`, `cancel`, `pause`, `resume` |
| `client.reservations.recipients` | `create`, `list`/`iter_list`, `delete` |
| `client.insights.alimtalk` / `.brand_message` (인사이트) | `get`, `get_hourly`, `get_by_template` |
| `client.insights.rcs` | `get_message`, `get_message_button`, `get_persistent_menu`, `get_brand_profile` |
| `client.kakao.senders` (발신프로필) | `request_token`, `create`, `find`, `list`/`iter_list`, `get`, `recover` |
| `client.kakao.categories` / `.groups` / `.sanctions` | `list`, `get` / `list`, `add_sender`, `remove_sender` / `get_sender`, `get_group_template_exclusion`, `get_template` |
| `client.alimtalk.templates` | `get`, `create`, `update`, `list`/`iter_list`, `list_modified`/`iter_list_modified`, `delete`, `request_inspection`, `request_inspection_with_files`, `cancel_inspection` |
| `client.alimtalk.template_categories` / `.public_templates` | `list` / `list`/`iter_list` |
| `client.brand_message.group_sends` (동보) | `create`, `get`, `pause`, `resume`, `terminate` |
| `client.brand_message.audience` / `.permissions` | `check_possible`, `check_possible_by_phone_numbers`, `get_friend_count`, `estimate` / `check`, `apply` |
| `client.brand_message.templates` | `get`, `create`, `update`, `list`/`iter_list`, `list_last_modified`/`iter_list_last_modified`, `delete` |
| `client.brand_message.videos` / `.group_tags` | `register_upload`, `register_existing`, `get`, `list`/`iter_list` / `list`, `get`, `create`, `update`, `delete` |
| `client.brand_message.friend_groups` | `upload_file`, `create`, `get`, `list`, `delete`, `add_phone_numbers`, `delete_phone_numbers`, `list_phone_number_requests`/`iter_list_phone_number_requests`, `get_phone_number_request` |
| `client.brand_message.marketing_agreements` / `.unsubscribe_contents` | `upload_evidence` / `register` |
| `client.rcs.brands` / `.chatbots` | `get`, `update` / `list`/`iter_list`, `get`, `update`, `cancel`, `delete`, `get_usable_queries` |
| `client.rcs.templates` / `.template_forms` / `.common_formats` / `.template_images` | `list`, `get`, `create`, `update`, `cancel`, `delete` / `list`/`iter_list`, `get` / `list`, `get` / `get`, `upload`, `list_form_logos` |
| `client.counsel.messages` (상담톡) | `send_plain`, `send_rich`, `delete` |
| `client.counsel.sessions` / `.users` / `.certs` / `.files` | `end`, `end_with_bot`, `get` / `block`, `unblock` / `get` / `upload_image`, `upload` |
| `client.counsel.channels` / `.consult_time` / `.system_messages` | `activate`, `deactivate`, `activate_chat`, `deactivate_chat` / `get`, `save` / `list`, `create`, `delete`, `request_approval`, `cancel_approval` |

각 메서드의 docstring에 스펙의 요약·설명, HTTP 메서드·경로, 재시도 정책, 속도 제한 버킷이 들어 있습니다. 스펙에 `x-unverified`로 표시된 동작(문서가 불명확한 부분)은 스펙 저장소의 GitHub Issues로 문의해 주세요.

## 오류 처리

```python
import pydantic

import bizgo
from bizgo import SmsMessage

try:
    client.send.omni(to="01000000000", messages=[SmsMessage(from_="01000000000", text="안내")], idempotency_key="k-1")
except pydantic.ValidationError:  # 보내기 전 검증 실패 (필드, 길이, 문자). 아무것도 보내지 않음
    ...
except bizgo.AuthenticationError:  # 키가 틀렸거나 IP가 등록되지 않음
    ...
except bizgo.RateLimitError as e:  # 자동 재시도 후에도 한도 초과
    print(e.retry_after)
except bizgo.DuplicateRequestError as e:  # 요청 단위 A301: 같은 idempotency_key가 이미 접수됨 (다시 발송되지 않음)
    print(e.already_accepted)  # True면 SDK의 재시도 전 시도가 접수된 것 → 상태 조회로 확인
except bizgo.APIError as e:  # 그 밖의 거절
    print(e.code, e.layer, e.description, e.tracking_id)
except bizgo.InvalidResponseError as e:  # 응답을 해석하지 못함(형식·크기). 발송은 접수됐을 수 있음 → 상태 조회
    print(e.http_status, e.tracking_id)
except bizgo.APIConnectionError:  # 네트워크 오류. 발송은 접수됐을 수도 있음 → 상태 조회로 확인
    ...
```

- `pydantic.ValidationError`는 **보내기 전** 요청 검증에서만 납니다. 응답을 해석하지 못하면(필드 형식이 다름, 16MB 초과, JSON이 아님 등) `bizgo.InvalidResponseError`이며, 발송 요청이었다면 이미 접수됐을 수 있습니다.
- 모든 SDK 예외는 pickle로 주고받을 수 있습니다(작업 큐·멀티프로세스). 모델·요청 객체의 `repr`/`str`에서 전화번호는 `010****0000`처럼(8~10자리는 절반 이상, 7자리 이하는 전부) 가리고, `userName`·`nickname`·`email`도 가리며, `text`·`message`·`content`는 길이만 보입니다(속성 값은 그대로).
- 응답은 두 단계로 판정합니다: `common.authCode`(게이트웨이: 인증·형식) → `data.code`(상품 처리). `e.layer`가 `"gateway"`/`"service"`입니다. 같은 코드라도 단계마다 뜻이 다릅니다.
- 발송 요청이 성공해도 **일부 수신자는 거절될 수 있습니다.** 항상 `result.failed`를 확인하세요.
- 같은 `idempotency_key`로 다시 보내면 요청은 성공하고 이미 접수된 수신자는 수신자별 코드 `A301`로 돌아옵니다(2026-09-28 sandbox 확인). SDK는 이들을 `failed`가 아닌 `result.duplicates`에 넣습니다(`succeeded`에도 없음, 다시 발송되지 않음). 같은 키로 재시도하는 것은 안전합니다: 이미 접수된 수신자는 `duplicates`로 돌아옵니다. 요청 단위 `A301`은 여전히 `DuplicateRequestError`입니다.

## 재시도와 타임아웃

| 요청 | 자동 재시도 |
|---|---|
| 조회, 리포트 | 429, 5xx, 네트워크 오류 |
| 발송 (`idempotency_key` 있음) | 429, 5xx, 네트워크 오류 |
| 발송 (`idempotency_key` 없음), 업로드 | 429만 (중복 발송 방지) |

기본값은 최대 2회 재시도(지수 백오프, `Retry-After` 우선), 타임아웃 30초(연결 5초)입니다.

```python
import httpx

from bizgo import Bizgo

Bizgo(max_retries=3, timeout=10.0)
Bizgo(proxy="http://proxy.example:3128")  # 프록시
Bizgo(verify="/etc/ssl/private-ca.pem")  # 사설 CA 번들 (TLS 검증은 끌 수 없음)
Bizgo(http_client=httpx.Client(timeout=10.0))  # 직접 만든 클라이언트: 기본 transport(retries=0)만 허용
```

## 대량 발송

수신자 수에 제한 없이 보낼 때는 `send.bulk()`를 씁니다. `chunk_size`(1~200, 기본 200)씩 나눠 `send.omni`를 호출합니다.

```python
from bizgo import SmsMessage

result = client.send.bulk(
    to=recipients,  # 전화번호·Destination 목록, 개수 제한 없음
    messages=[SmsMessage(from_="01000000000", text="[비즈고] 정기 점검 안내")],
    concurrency=4,  # 동시에 보내는 요청 수 (속도 제한은 그대로 적용)
    idempotency_key_prefix="notice-20261001",  # 청크 키: notice-20261001-<chunk_size>-<시작 인덱스>-<해시8>
)
print(len(result.msg_keys), len(result.failed), len(result.duplicates))  # 접수 / 거절 / 이미 접수(A301)
for error in result.errors:  # 통째로 실패한 청크 (네트워크 오류 등)
    print(error.chunk_index, error.start, error.end, type(error.error).__name__)
```

- 보내기 전에 **모든 청크를 검증**합니다. 하나라도 잘못되면 아무것도 보내지 않고 `ValueError`를 냅니다(위치는 `to` 목록의 인덱스로 알려 줌).
- 한 청크가 어떤 이유로 실패해도(API·네트워크 오류, 응답 해석 실패 등) 나머지는 계속 보내고 이미 받은 결과를 잃지 않습니다. 오류에는 청크 번호와 수신자 **인덱스 범위만** 들어가고 전화번호는 들어가지 않습니다.
- 멱등성 키는 `<prefix>-<chunk_size>-<시작 인덱스>-<해시8>`입니다(해시8 = 청크 수신번호 목록의 SHA-256 앞 8자리). **재실행은 같은 목록·같은 `chunk_size`로** 하세요(키 유지 기간 `idempotency_ttl` 안에서 이미 접수된 청크의 수신자는 `result.duplicates`(A301)로 돌아오고 다시 발송되지 않음. 오류가 아님). 목록이나 `chunk_size`가 바뀌면 키가 달라지므로 중복 발송될 수 있습니다. 실패한 청크만 다시 보내려면 `result.errors`의 `chunk_index`·`start`·`end`로 그 수신자만 골라 보내세요.
- `idempotency_key_prefix`가 없으면 청크는 429일 때만 재시도합니다(중복 발송 방지). 있으면 타임아웃·5xx에도 재시도합니다.
- 비동기: `await client.send.bulk(...)`.

## 속도 제한

클라이언트는 요청 전에 **토큰 버킷 2개**로 속도를 맞춥니다(기본 켜짐).

| 버킷 | 기본 한도 | 비용 | 대상 |
|---|---|---|---|
| `send` | **초당 200 메시지(수신번호 기준)** | 요청의 수신자 수(`destinations` 개수, 최소 1) | 스펙에서 `x-sdk-rate: send`인 operation: 통합 발송(`send.*`, `bulk`), 예약 발송 등록·수신자 추가, 브랜드메시지 동보 생성, 상담톡 발송 |
| `other` | 초당 5 요청 | 요청마다 1 | 그 밖의 모든 API |

- 수신자 200명짜리 발송 요청은 토큰 200개를 쓰므로 기본값에서는 **초당 1건**만 나갑니다. 그래서 `send.bulk`는 `concurrency`와 관계없이 200명 청크를 약 1초에 하나씩 보냅니다.
- 수신자 목록이 없는 발송(예: 친구 그룹 대상 동보, 상담톡)은 1로 셉니다. 재시도도 시도마다 토큰을 씁니다.
- 한도를 청크 크기보다 낮게 잡아도(예: `send=100`인데 200명 요청) 멈추지 않습니다. 버킷이 가득 찰 때까지 기다린 뒤 보내고 부족분은 다음 요청이 갚습니다.

```python
from bizgo import Bizgo, RateLimit

Bizgo(rate_limit=RateLimit(send=100, other=5))  # 계약한 한도에 맞춰 조정
Bizgo(rate_limit=None)  # 끄기
```

- 버킷은 **가득 찬 상태로 시작**합니다(처음 1초 분량은 바로 나감). 비즈고 서버도 토큰 버킷 방식으로 판정합니다(2026-09-24 확인). 서버 버킷 용량은 문서화되지 않아 초당 한도와 같다고 보며, 넘치면 429를 재시도합니다.

> **프로세스 단위입니다.** 비즈고의 한도는 계정(API Key) 단위인데, 이 제한은 클라이언트 인스턴스 하나만 맞춥니다. 여러 프로세스·서버·워커가 같은 키를 쓰면 한도를 나눠 설정하거나 별도로 조정해야 합니다. 서버가 429를 주면 기존처럼 `Retry-After`를 따라 재시도합니다.

## 테스트 도구

`bizgo.testing`으로 네트워크·API Key 없이 **여러분의 코드**를 테스트할 수 있습니다. 운영 코드에서는 import하지 않아도 되고, 추가 의존성도 없습니다.

```python
from bizgo import RateLimitError
from bizgo.testing import FakeTransport, sign_webhook

fake = FakeTransport()
client = fake.client()  # 가짜 키(test-api-key-not-real), sandbox URL, 속도 제한 끔, 실제로 연결하지 않음

client.send.sms(to="01000000000", from_="01000000000", text="hello")  # 기본: 모든 수신자 A000 + 가짜 msgKey
assert fake.last_request.operation_id == "sendOmni"
assert fake.last_request.json["destinations"] == [{"to": "01000000000"}]

fake.on("sendOmni").fail("service", 200, "A020", retry_after=0)  # 다음 호출: RateLimitError
fake.on("sendOmni").send_result("A000", "A306")  # 그다음: 두 번째 수신자 거절
fake.on("GET", "/api/comm/v1/report/inquiry/{msgKey}").data({"report": []})
fake.on("getReportPolling").network_error()  # 또는 .timeout()

headers, body = sign_webhook("test-webhook-secret", {"msgKey": "KEY001"})  # WebhookReceiver 테스트용 요청
```

- 요청마다 operation, 메서드, 경로, 쿼리, JSON 본문(multipart는 필드 이름과 파일 크기)을 기록합니다. **헤더 값(API Key 포함)은 기록하지 않습니다.**
- stub이 없으면 operation별 성공 응답을 돌려줍니다. 발송(`sendOmni`, 예약 등록, 예약 수신자 추가)은 수신자마다 `A000`과 가짜 `msgKey`, 예약 등록은 가짜 `resvKey`도 넣습니다. 그 밖의 operation은 `data.data = {}`(빈 목록, 다음 페이지 없음)입니다.
- 비동기: `fake.async_client()`.

## 관측 (hooks · OpenTelemetry)

API 호출마다(재시도 포함 한 번) 시작·종료 hook이 불립니다. 전달되는 값은 operationId, `리소스.메서드`, HTTP 메서드, **경로 템플릿**(`/api/comm/v1/report/inquiry/{msgKey}`), 상태 코드, 오류 단계·코드·종류, 시도 횟수, 소요 시간뿐입니다. **본문·쿼리·헤더 값·실제 경로 값·전화번호·키는 넘기지 않습니다.** hook(동기·`async def`)이나 `bizgo` 로거에서 난 예외는 무시되어(경고 한 번) 결과·재시도·대량 발송 결과에 영향을 주지 않습니다. 비동기 클라이언트는 `async def` hook을 await합니다.

```python
from bizgo import Bizgo, Hooks, RequestEvent


class Metrics(Hooks):
    def on_request_end(self, event: RequestEvent) -> None:
        print(event.operation, event.status, event.code, event.attempts, event.duration_ms)


client = Bizgo(hooks=Metrics())
```

OpenTelemetry는 선택 extra입니다(core 의존성은 그대로 `httpx`, `pydantic`).

```bash
pip install "bizgo-sdk-comm[otel]"
```

```python
from bizgo import Bizgo
from bizgo.otel import OpenTelemetryHooks

client = Bizgo(hooks=OpenTelemetryHooks())  # 전역 TracerProvider 사용. hooks=[Metrics(), OpenTelemetryHooks()]도 가능
```

span 이름은 `bizgo <리소스>.<메서드>`(예: `bizgo send.omni`), 속성은 `http.request.method`, `url.template`, `bizgo.operation_id`, `http.response.status_code`, `bizgo.code`, `bizgo.layer`, `bizgo.retry_count`, `error.type`입니다.

## 보안

- API Key는 **접두어 없이** 키 값만 씁니다(`Bearer`/`ApiKey` 접두어는 401). 공백·줄바꿈·제어문자·비ASCII 문자가 있으면 잘라내지 않고 `ConfigurationError`로 알립니다(환경변수 값 끝의 줄바꿈 포함). 환경변수나 시크릿 저장소에서 읽고, 코드·저장소·클라이언트 앱에 넣지 않습니다.
- SDK(`bizgo` 로거)는 키, 요청 본문, 쿼리 문자열(전화번호가 들어갈 수 있음)을 로그나 예외 메시지에 남기지 않습니다. 검증 오류에도 입력값을 싣지 않습니다.
- `http_client=`는 SDK가 안전하게 제어할 수 있는 클라이언트만 받습니다: 기본 `httpx.HTTPTransport`(`retries=0`) 또는 테스트용 `MockTransport`, `event_hooks` 없음, 쿠키 없음. 그 밖의 클라이언트(직접 만든 transport, mounts, event hooks)는 `ConfigurationError`이며, 꼭 써야 하면 `trust_http_client=True`로 허용합니다. 이때 그 클라이언트가 **리다이렉트·재시도·자체 인증을 하지 않는다고 여러분이 보장**해야 하며 중복 발송·정보 유출 위험을 감수하는 설정입니다. 프록시·사설 CA는 `proxy=`, `verify=`(CA 번들 경로만, `False` 불가) 옵션을 쓰세요.
- 직접 넘긴 `http_client`의 인증 설정(`auth=`)과 기본 헤더는 요청마다 무시되고(API Key가 바뀌거나 다른 서버로 가지 않도록), 리다이렉트는 따르지 않습니다(`InvalidResponseError`, 메시지에 HTTP 상태). 응답은 압축 해제 후 16MB, JSON 중첩 64단계까지만 읽습니다. `base_url`에 `user:pw@`, 쿼리, fragment를 넣으면 설정 오류입니다.
- 경로 값 `.`, `..`는 거부하고, 그 밖의 값은 `/`·`?`·`#`·`%`를 포함해 한 세그먼트로 인코딩합니다.
- 단, 의존 라이브러리 `httpx`는 **INFO 레벨에서 요청 URL 전체**(쿼리 포함)를 `httpx` 로거로 남깁니다. 운영에서는 `logging.getLogger("httpx").setLevel(logging.WARNING)`을 권장합니다.
- `APIError.body`에는 응답 원문(전화번호 포함 가능)이 있으니 그대로 로그에 남기지 마세요.
- `http://` base URL은 거부합니다(테스트용 localhost 제외).
- 취약점 신고는 [SECURITY.md](SECURITY.md)를 참고하세요.

### SDK 식별 정보

비즈고가 SDK 사용 현황(언어·버전·런타임)을 집계할 수 있게 모든 요청에 다음 두 헤더를 붙입니다. **이 밖에는 아무것도 수집하거나 따로 전송하지 않습니다**(phone-home 없음).

- `User-Agent: bizgo-sdk-comm-python/<SDK 버전> python/<Python 버전> (<os>; <arch>)` — os는 `linux`/`windows`/`darwin`/`freebsd`/`other`, arch는 `x64`/`arm64`/`x86`/`arm`/`other`만 씁니다(호스트명·사용자명·커널 버전 없음).
- `X-Bizgo-Client: bizgo-sdk-comm-python/<SDK 버전>` (예: `bizgo-sdk-comm-python/1.2.0`)
- 선택: `Bizgo(app_info=("myshop", "1.4.2"))`를 주면 User-Agent 끝에 ` app/myshop-1.4.2`가 붙습니다. 이름은 영문·숫자·`._-` 1~50자, 버전은 영문·숫자·`._+-` 1~30자만 허용합니다(그 밖이면 `ConfigurationError`). 이메일·전화번호 같은 개인정보는 넣지 마세요.
- 직접 넘긴 `http_client`의 기본 헤더로 `Authorization`, `User-Agent`, `X-Bizgo-Client`를 덮어쓸 수 없습니다.

## 이전 SDK에서 옮기기

| infobank-omni-sdk-python | bizgo-sdk-comm |
|---|---|
| `https://omni.ibapi.kr`, ID/PW로 토큰 발급 | `https://mars.ibapi.kr`, API Key 하나 (토큰 발급 없음) |
| 채널별 발송 API (`/v1/send/sms` 등) | `client.send.omni()` 하나 (채널은 메시지 모델로 구분) |
| `{code, result, data}` 응답 | `{common, data}` 응답 (SDK가 풀어서 반환) |
| Form API | 없음 (알림톡·브랜드메시지는 템플릿 자동 치환 발송 사용) |

## 타입 검사

모든 공개 API에 타입 힌트가 있고(`py.typed`), README·예제 코드는 `mypy --strict`를 통과합니다(`tests/test_docs_typecheck.py`가 검사).
모델 생성자는 Python 필드 이름(`sender_key=`, `from_=`)으로 타입 검사되므로 pydantic mypy 플러그인 없이도 동작합니다. 플러그인을 쓰면 필드 기본값·검증 규칙까지 더 정확히 검사합니다.

```ini
# mypy.ini (선택)
[mypy]
strict = True
plugins = pydantic.mypy
```

메서드 결과는 `None`이 아닙니다(데이터가 없으면 빈 객체·빈 목록). 다만 응답 모델의 **필드**는 서버가 생략할 수 있어 대부분 `Optional`이니 `if value is None:` 등으로 처리하세요.

## 개발

```bash
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
pytest                                   # 네트워크·키 없이 mock으로 실행
ruff check . && ruff format --check . && mypy
python scripts/generate_models.py        # spec/openapi.yaml이 바뀌었을 때 (모델, 리소스 메서드, operation 표, 웹훅 파서)
python scripts/generate_models.py --check
```

AI 코딩 도구로 이 저장소를 수정할 때의 규칙은 [AGENTS.md](AGENTS.md)에 있습니다.
SDK를 **사용하는** 코드를 AI로 작성할 때는 [llms.txt](llms.txt)를 컨텍스트로 넣으면 정확도가 높아집니다.

## 라이선스

[Apache-2.0](LICENSE)
