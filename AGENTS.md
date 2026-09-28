# AGENTS.md — bizgo-sdk-comm-python

AI 코딩 도구와 기여자가 이 저장소를 수정할 때 따르는 규칙입니다. SDK를 *사용하는* 코드를 쓸 때는 [llms.txt](llms.txt)를 보세요.

## 명령

```bash
pip install -e ".[dev]"
pytest                                    # 전부 mock(respx). 네트워크·API Key 불필요
ruff check . && ruff format --check .
mypy                                      # --strict
python scripts/generate_models.py         # 모델·리소스 메서드·operation 표·웹훅 파서 재생성
python scripts/generate_models.py --check # CI: 생성 결과가 커밋과 같은지 (생성 파일 전부)
```

변경 후 위 5개가 모두 통과해야 합니다. 릴리스 전에는 `pip-audit`, `python -m build`, `twine check --strict dist/*`도 확인합니다.

## 구조

```
spec/openapi.yaml, spec/error-codes.json   # bizgo-api-spec에서 복사한 스펙 (직접 수정 금지, 스펙 저장소에서 고친 뒤 복사)
scripts/generate_models.py                 # 스펙 → 모델 생성 (+ _gen_resources.py 호출)
scripts/_gen_resources.py                  # x-sdk-* → 리소스 메서드, operation 표, 웹훅 파서
src/bizgo/
  __init__.py            # 공개 API. 새 공개 이름은 여기 __all__에 추가
  _client.py             # Bizgo / AsyncBizgo
  _config.py             # Environment, API Key·base URL 검증
  _transport.py          # 헤더(식별 헤더 포함), 재시도, 속도 제한, hooks, 응답 봉투 해석, 오류 매핑 (sync/async)
  _ratelimit.py          # 토큰 버킷 (send: 수신자 수 기준, other: 요청 수 기준)
  _operation.py          # Operation 메타데이터 타입
  _operations.py         # 생성됨: operationId → Operation (경로 템플릿, 재시도, 버킷, 페이지)
  _generated_webhooks.py # 생성됨: 웹훅 파서 (상담톡 등)
  hooks.py               # 관측 hooks (경로 템플릿·코드만, 값 없음)
  otel.py                # OpenTelemetry 어댑터 ([otel] extra, core에서 import 금지)
  testing.py             # FakeTransport, sign_webhook (core에서 import 금지)
  _errors.py             # 예외 계층, 코드→예외 매핑
  _base.py               # RequestModel(extra=forbid, 바이트 검증) / ResponseModel(extra=allow)
  _error_codes.py        # 생성됨: data.code → (HTTP 상태, 설명)
  _generated_required_if.py # 생성됨: x-sdk-required-if 규칙 표 (RULES, 요청 본문 ROOTS)
  _required_if.py        # 조건부 필수 검사기 (RequestModel이 호출)
  models/_generated_*.py # 생성됨 (직접 수정 금지)
  models/_results.py     # SendResult, ReportBatch, MessagePage, MoPage
  resources/             # send, files, reports, messages (직접 작성, sync/Async 짝) — _generated.py의 <Name>Base를 상속
  resources/_generated.py# 생성됨: 스펙의 모든 operation (client.<resource>.<method>)
  resources/_runtime.py  # 생성 메서드용 헬퍼 (경로 인코딩, 파라미터 검증, multipart, 페이지 순회)
  webhooks.py            # 서명 검증, 페이로드 파싱
examples/                # tests/test_examples.py가 mock으로 실행
```

## 규칙

1. **생성 파일은 손으로 고치지 않습니다.** 모델을 바꾸려면 bizgo-api-spec을 고치고 `spec/`에 복사한 뒤 재생성합니다.
2. 새 엔드포인트는 **직접 작성하지 않습니다.** 스펙(`x-sdk-resource`/`x-sdk-method`/`x-sdk-retry`/`x-sdk-pagination`/`x-sdk-result`/`x-sdk-rate`)을 고쳐 복사한 뒤 재생성하면 sync·async 메서드가 함께 생깁니다. 편의 메서드를 직접 만들 때만 `scripts/_gen_resources.py`의 `HANDWRITTEN_OPS`에 operationId를 넣고(생성 메서드보다 우선), `tests/test_all_operations.py`의 `HANDWRITTEN` 표에 호출 방법을 추가합니다.
3. 공개 메서드는 키워드 전용 인자, 타입 힌트, docstring(Args/Returns/Raises)을 갖춥니다. 반환 타입은 생성 모델이나 `_results.py`의 타입입니다(`dict` 반환 금지).
4. 재시도 정책: 생성 메서드는 스펙의 `x-sdk-retry`를 따릅니다. 직접 작성한 메서드는 조회·DELETE는 `Retry.SAFE`, 발송은 `idempotency_key`가 있을 때만 `SAFE`, 업로드와 그 밖의 생성 요청은 `Retry.RATE_LIMIT_ONLY`. transport 호출에는 항상 `operation="<operationId>"`를 넘깁니다(hooks·속도 제한 버킷에 필요).
5. 예제·README의 코드는 실제로 동작해야 합니다. 예제를 바꾸면 `tests/test_examples.py`도 맞춥니다.
6. 문서에 없는 동작을 가정하지 않습니다. 불확실하면 스펙에 `x-unverified`로 표시하고 bizgo-api-spec의 GitHub Issues에 알립니다.
7. `idempotencyKey`가 있고 `idempotencyTtl`이 없으면 `DEFAULT_IDEMPOTENCY_TTL`(86400)을 채웁니다(없으면 A309). 명시한 TTL(0 포함)은 그대로, 키가 없으면 TTL을 넣지 않습니다. 직렬화된 본문에 `resources/_common.with_default_ttl()`로만 적용하며(`send.request`, 생성 메서드의 `json_body`), 호출자의 모델·dict는 바꾸지 않습니다. 관련 테스트: `tests/test_idempotency_ttl.py`. 수신자별 `A301`(같은 키로 이미 접수)은 `failed`가 아닌 `SendResult.duplicates`/`BulkSendResult.duplicates`로 돌려줍니다(`succeeded`에도 없음). 요청 단위 `A301`은 `DuplicateRequestError` 그대로입니다. 관련 테스트: `tests/test_duplicates.py`.
8. 속도 제한 버킷은 스펙의 `x-sdk-rate: send`로만 정합니다(코드에 목록을 두지 않음). send 버킷 비용은 요청의 `destinations` 개수(최소 1)입니다.
9. `bizgo.testing`, `bizgo.otel`은 core(`bizgo/__init__.py`, `_client.py` 등)에서 import하지 않습니다. core 런타임 의존성을 늘리지 않습니다.
10. 상담톡 웹훅에는 서명이 없습니다: 서명을 요구·검사하지 않고 서명 헤더는 무시하며, 본문 크기·JSON 중첩 64·타입 검사만 적용합니다. secret 없이 `parse_counsel_*`로 파싱할 수 있습니다. 리포트·MO는 항상 서명 필요. 이 동작을 바꾸지 마세요. 리포트·MO 웹훅 서명은 `X-IB-Signature` = `HmacSHA256(secret, X-IB-Timestamp)`입니다(비즈고 확인). 다른 서명 헤더 이름이나 `sha256=` 같은 접두어는 받지 않고, 출력 인코딩은 아직 확인되지 않아 hex(대소문자 무시)·base64를 모두 허용합니다. 웹훅 secret은 비즈고에 요청해 받습니다.

11. 조건부 필수(`x-sdk-required-if`)는 스펙에서만 읽습니다(코드에 규칙을 두지 않음). 생성기가 `_generated_required_if.py`를 만들고, `RequestModel`의 검증기가 `_required_if.violations()`로 검사합니다: 모든 요청 모델은 생성 시 자기 규칙(`required`, 상대 `requiredPaths`)을, 요청 본문 모델(`ROOTS`)은 트리 전체와 `$.` 경로를 검사합니다. 오류는 `ValueError` → `pydantic.ValidationError`이며 필드 경로·조건만 담습니다(입력값 금지). 알림톡 전문 발송 예제·문서에는 `msg_type="AT"`를 넣습니다. 관련 테스트: `tests/test_required_if.py`.

## 보안 규칙 (오픈소스 저장소)

- **로그·예외에 민감정보 금지**: API Key, 요청 본문, 쿼리 문자열, 전화번호, 웹훅 secret을 `logger`, 예외 메시지, `repr`에 넣지 않습니다. httpx 예외는 URL을 담고 있으므로 `raise ... from None`으로 끊습니다. 관련 테스트: `tests/test_errors_and_security.py`.
- pydantic 모델은 `hide_input_in_errors=True`를 유지합니다(검증 오류에 전화번호가 찍히지 않도록).
- TLS 검증을 끄는 옵션, `http://` base URL(localhost 제외)을 허용하는 코드를 추가하지 않습니다.
- 경로 파라미터는 `_segment()`로 인코딩합니다(경로 조작 방지).
- 테스트·예제의 값은 placeholder만 씁니다: 전화번호 `01000000000`, 키 `test-api-key-not-real`, `SENDER_KEY_EXAMPLE`. 실제 키·번호·발신프로필 키를 커밋하지 않습니다(gitleaks가 pre-commit·CI에서 검사).
- hooks·OpenTelemetry·테스트 기록에 본문, 쿼리 값, 헤더 값, 실제 경로 값을 넣지 않습니다(경로 템플릿만). 관련 테스트: `tests/test_testing_hooks_webhooks.py`.
- 헤더 파라미터(예: 발신프로필 등록의 `phoneNumber`)도 로그·예외에 넣지 않습니다. `Authorization`, `User-Agent`, `X-Bizgo-Client`는 어떤 옵션으로도 덮어쓸 수 없어야 합니다.
- SDK-DESIGN.md §12 규칙을 지킵니다: 응답 파싱 오류는 `_transport.validate()`로 `InvalidResponseError`, 응답은 `_BoundedDecoder`로 16MB·깊이 64 제한, 요청마다 `auth=None`·`follow_redirects=False`, 경로 값 `.`/`..` 거부, 웹훅 본문 오류는 `WebhookPayloadError`, 모델 `repr` 전화번호 마스킹. 관련 테스트: `tests/test_hardening.py`. README·llms.txt의 ```python 코드는 `tests/test_docs_typecheck.py`가 `mypy --strict`로 검사하므로 실제로 타입이 맞아야 합니다.
- 런타임 의존성은 `httpx`, `pydantic` 두 개만 둡니다(OpenTelemetry는 `[otel]` extra). 추가가 필요하면 이유를 PR에 적습니다.
