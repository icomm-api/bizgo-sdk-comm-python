# Changelog

이 프로젝트는 [Semantic Versioning](https://semver.org/lang/ko/)을 따릅니다.

## 1.2.0 - 2026-09-28

`bizgo-sdk-comm`의 첫 공개 릴리스입니다. 비즈고 커뮤니케이션 API(`https://mars.ibapi.kr`, API Key 인증) 기준으로 새로 작성했으며,
이전 `infobank-omni-sdk-python`(OMNI API, ID/PW 인증)과 호환되지 않습니다. 버전 번호는 여섯 개 비즈고 SDK를 1.2.0으로 맞춘 것입니다.

### 추가
- `Bizgo` / `AsyncBizgo` 클라이언트, API Key 인증(환경변수 `BIZGO_API_KEY`), 운영·sandbox 환경
- 통합 발송 `send.omni()`와 간편 메서드 `send.sms()`/`lms()`/`mms()`, 대체발송, 치환, 멱등성 키
- 채널 모델: SMS, LMS/MMS, 국제, RCS, 알림톡, 브랜드메시지, 네이버 톡톡 (OpenAPI 스펙에서 생성)
- 보내기 전 검증: 필수·오타 필드, 바이트 길이(EUC-KR), 수신자 200명 제한
- 이미지 업로드: MMS, RCS, 브랜드메시지 6종
- 리포트: polling(`consume`), 수신 확인, 개별 조회
- 조회: 상태(단건·요청별), 발송 이력·MO 이력(페이지 자동 순회), 통계
- 웹훅: 서명 검증, 리포트·MO 페이로드 파싱
- 오류 계층(게이트웨이/상품 단계 구분, 에러코드 설명), 재시도(429·5xx·네트워크, 발송은 멱등성 키가 있을 때만)
- **API 전체 지원**: 스펙의 146개 operation을 `client.<리소스>.<메서드>`로 호출 (예약 발송, 인사이트, 카카오 발신프로필·그룹·제재, 알림톡 템플릿, 브랜드메시지 동보·템플릿·친구 그룹·동영상, RCS 브랜드·대화방·템플릿, 카카오 상담톡). `x-sdk-*` 메타데이터에서 sync·async 메서드를 생성합니다(경로 파라미터 인코딩, 본문 검증, 쿼리 검증, 재시도 정책, `iter_*` 페이지 순회, multipart 업로드).
- 상담톡 웹훅 7종 파서(`WebhookReceiver.counsel_*`, `parse_counsel_*`, `parse(name, body)`)와 `counsel_ack()`. 상담톡 웹훅에는 서명이 없어 서명 검사 없이 파싱하며(서명 헤더는 무시), 본문 크기·JSON 중첩 64·타입 검사는 적용합니다. secret 없이 `parse_counsel_*`로 사용할 수 있습니다.
- `DEFAULT_IDEMPOTENCY_TTL = 86400`: `idempotencyKey`만 주고 `idempotencyTtl`을 생략하면 SDK가 86400초를 채워 보냅니다(비즈고는 TTL 없는 키를 A309로 거절, 2026-09-28 sandbox 확인). 명시한 TTL(0 포함)은 그대로, 키가 없으면 TTL을 넣지 않습니다. `send.omni/sms/lms/mms/request/bulk`(sync·async)와 `idempotencyKey`·`idempotencyTtl`을 가진 생성 메서드 본문(dict 포함, 입력은 바꾸지 않음)에 적용됩니다.
- `send.bulk()` / `await send.bulk()`: 수신자 수 제한 없는 대량 발송(청크별 멱등성 키, 부분 실패 결과 `BulkSendResult`).
- `SendResult.duplicates` / `BulkSendResult.duplicates`: 같은 `idempotencyKey`로 이미 접수된 수신자(수신자별 `A301`, 요청은 성공, 2026-09-28 sandbox 확인). `failed`·`succeeded`에 넣지 않으며 모든 수신자가 A301인 청크도 오류가 아닙니다. 요청 단위 `A301`은 `DuplicateRequestError`. `bizgo.testing`의 `Stub.duplicates()`로 흉내 낼 수 있습니다.
- 클라이언트 속도 제한(`rate_limit=RateLimit(send=200, other=5)`, 기본 켜짐): send 버킷은 **초당 200 메시지(수신번호 기준)**, 그 외 초당 5 요청. send 버킷 대상은 스펙의 `x-sdk-rate: send`.
- `bizgo.testing`: `FakeTransport`(요청 기록, operation별 기본 성공 응답, 오류 주입), `sign_webhook()`.
- 관측: `hooks=`(요청 시작·종료, 경로 템플릿·상태·코드만), `bizgo.otel.OpenTelemetryHooks`(`[otel]` extra).
- SDK 식별 헤더: `User-Agent: bizgo-sdk-comm-python/<ver> python/<ver> (<os>; <arch>)`, `X-Bizgo-Client`, 선택 `app_info=(name, version)`.
- 조건부 필수 필드 검사(스펙의 `x-sdk-required-if`): 생성기가 규칙 표(`bizgo/_generated_required_if.py`)를 만들고 `RequestModel`이 보내기 전에 검사합니다(모델·dict 본문, 서버 호출 없음, 오류에는 필드 경로·조건만). `$.` 경로(예: 템플릿 자동 치환 발송의 `$.destinations[].replaceWords`)는 요청 본문(`SendOmniRequest`, `ReservationCreateRequest` 등) 단위로 검사하고, `send.bulk` 오류는 `to` 목록 기준 인덱스로 알려 줍니다.
- 알림톡 전문 발송(`sendType`이 `template`이 아님)은 `msgType`(`AT`/`AI`)과 `text`가 필수입니다(없으면 서버 A523, 2026-09-28 sandbox 확인). 템플릿 조회 응답의 `AlimtalkTemplate.msg_type`(문자열)을 그대로 쓸 수 있습니다.
- 요청·응답 양쪽에서 쓰는 스키마(버튼, 템플릿 항목 등)는 두 모듈에 모두 생성합니다. `bizgo.models`는 요청 모델을 내보내고, 응답은 알 수 없는 필드를 허용하는 응답 모델로 파싱합니다.

### 보안
- 응답 파싱 실패(필드 형식 불일치, JSON 아님, 깊은 중첩)는 `pydantic.ValidationError`/`RecursionError` 대신 `InvalidResponseError`(HTTP 상태·`tracking_id`·`body` 포함)로 냅니다. 발송이면 "접수됐을 수 있음" 안내를 붙입니다. 응답 모델의 봉투 필드(`common`, `authResult`, `result` 등)는 필수가 아닙니다.
- `send.bulk`는 청크별로 모든 예외를 잡아(설정 오류 제외) 이미 받은 결과를 잃지 않습니다.
- `send.bulk` 멱등성 키는 `<prefix>-<chunk_size>-<시작 인덱스>-<해시8>` 형식입니다(다른 수신자 묶음에 같은 키를 쓰지 않음, 200자 검증).
- 재시도(타임아웃·네트워크·5xx·429) 뒤 받은 `A301`은 `DuplicateRequestError.already_accepted = True`와 안내 메시지를 붙입니다.
- 경로 값 `.`·`..`을 거부하고, 헤더 파라미터는 출력 가능한 ASCII만 허용합니다.
- 사용자 `http_client`의 `auth=`·기본 헤더가 `Authorization`을 바꾸지 못하게 요청마다 끄고, 리다이렉트를 따르지 않습니다(오류 메시지에 HTTP 상태). `base_url`의 `user:pw@`·쿼리·fragment는 설정 오류입니다.
- 응답은 스트리밍으로 읽고 gzip/deflate를 직접 풀어 압축 해제 후 16MB, JSON 중첩 64단계에서 멈춥니다(압축 폭탄 방어). `Accept-Encoding: gzip, deflate`.
- 웹훅: `X-IB-Timestamp`는 ASCII 숫자 1~16자리만, 본문 JSON 오류·깊은 중첩·배열·필드 오류는 새 `WebhookPayloadError`(`WebhookVerificationError` 하위). 공백만 있는 secret과 0 이하·무한·NaN `tolerance`를 거부합니다(`None`은 명시적 비활성화).
- `Retry-After`는 유한한 0 이상 숫자만 씁니다(`nan` 등은 무시).
- 모든 SDK 예외를 pickle로 왕복할 수 있습니다. API Key를 담은 `ClientConfig`는 pickle할 수 없습니다.
- 모델 `repr`/`str`에서 전화번호(`to`, `from`, `phoneNumber`, `originator`, `callback` 등)를 `010****0000`처럼 가리고 `content`는 길이만 보입니다.
- 모델 생성자가 pydantic mypy 플러그인 없이도 Python 필드 이름(`sender_key=`, `from_=`)으로 타입 검사됩니다(`validation_alias`/`serialization_alias`, `Field(default=...)`). README·llms.txt 코드는 `mypy --strict`를 통과합니다(테스트로 검사).
- SECURITY.md: 직접 넘긴 `http_client`의 TLS 설정이 적용된다는 점을 정확히 적었습니다. 속도 제한 버킷이 가득 찬 상태로 시작한다는 점(서버 판정 방식 미확인)을 문서화했습니다.
- `bizgo.testing`: MMS/RCS 업로드 기본 응답에 가짜 `fileKey`/`media`.
- 사용자 hooks(동기·`async def`)와 `bizgo` 로거에서 난 예외는 삼키고(경고 한 번) 결과·재시도·대량 발송 결과에 영향을 주지 않습니다. 비동기 클라이언트는 `async def` hook을 await합니다.
- API Key는 `[!-~]+`만 허용합니다. 앞뒤 공백·줄바꿈을 조용히 잘라내지 않고 `ConfigurationError`를 냅니다(환경변수 포함).
- 3xx 응답은 재시도하지 않습니다(SAFE 정책 포함).
- `http_client=`는 SDK가 제어할 수 있는 클라이언트만 받습니다(기본 `HTTPTransport(retries=0)`/`MockTransport`, event hooks·쿠키 없음). 그 밖에는 `trust_http_client=True`가 필요합니다. 새 옵션 `proxy=`, `verify=`(CA 번들 경로, `False` 거부).
- `repr` 마스킹 확대: 8~10자리 번호는 절반 이상, 7자리 이하는 전부, `userName`·`nickname`·`email`, `text`·`message`는 길이만. `SignedWebhook` repr에 본문 없음.
- 생성 메서드는 성공 응답에 데이터가 없어도 `None` 대신 빈 결과 객체를 돌려줍니다(반환 타입에서 `Optional` 제거).
- 업로드 파일을 읽지 못하면(없음·권한·디렉터리) `OSError` 대신 파일 이름만 담은 `ValueError`를 냅니다(전체 경로 없음).
