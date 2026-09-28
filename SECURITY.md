# 보안 정책

## 취약점 신고

보안 취약점은 **공개 Issue로 올리지 마세요.** GitHub의 [Private vulnerability reporting](../../security/advisories/new)으로 비공개 신고해 주세요.
확인 후 영업일 기준 5일 안에 답변합니다.

## 지원 버전

최신 minor 버전에 보안 수정을 제공합니다.

| 버전 | 지원 |
| --- | --- |
| 1.2.x | 지원 |
| < 1.2 | 미지원 (공개 배포되지 않음) |

## 자격 증명이 노출됐을 때

1. 즉시 비즈고 콘솔 `발송관리 > 연동관리`에서 해당 API Key를 폐기하고 새로 발급합니다. 저장소 기록에서 지워도 이미 복제됐을 수 있으므로 **폐기가 먼저**입니다.
2. 웹훅 secret은 비즈고에 재발급을 요청합니다.
3. 허용 IP(ACL) 목록을 점검합니다.

## SDK의 보안 동작

- API Key는 `Authorization` 헤더로만 보내고, `repr`·로그·예외 메시지에 넣지 않습니다.
- 요청 본문, 쿼리 문자열, 검증 오류의 입력값(전화번호 포함 가능)을 로그·예외에 넣지 않습니다.
  의존 라이브러리 `httpx`는 INFO 레벨에서 요청 URL을 로그로 남기므로 운영에서는 `httpx` 로거를 WARNING 이상으로 두세요.
- `APIError.body`에는 응답 원문이 있습니다. 전화번호가 있을 수 있으니 그대로 로그에 남기지 마세요.
- https가 아닌 base URL은 거부합니다(테스트용 localhost 제외). `base_url`에 사용자 정보(`user:pw@`), 쿼리, fragment가 있으면 설정 오류입니다.
- **SDK 자체에는 TLS 검증을 끄는 옵션이 없습니다**(`verify=`는 CA 번들 경로만 받고 `False`는 거부). 단, `http_client=`로 직접 만든 `httpx.Client`를 넘기면 그 클라이언트의 TLS 설정(`verify=`, 인증서, 프록시)이 그대로 적용됩니다. `verify=False`인 클라이언트를 넘기지 마세요.
- SDK가 점검·강제할 수 없는 `http_client`(직접 만든 transport, `retries>0`, mounts, event hooks, 쿠키)는 기본적으로 거부합니다. `trust_http_client=True`로 허용하면 그 클라이언트가 리다이렉트·재시도·자체 인증을 하지 않는다는 보장은 사용자 책임입니다(중복 발송·API Key 유출 위험). 프록시는 `proxy=`를 쓰세요.
- 넘긴 클라이언트의 인증 설정(`auth=`)과 기본 `Authorization`/`User-Agent` 헤더는 요청마다 무시되며, 리다이렉트는 따르지 않습니다(API Key가 다른 서버로 가지 않도록). 리다이렉트 응답은 HTTP 상태를 담은 `InvalidResponseError`가 됩니다.
- 응답은 압축 해제 후 16MB, JSON 중첩 64단계까지만 읽습니다(압축 폭탄·깊은 중첩 방어). 경로 값 `.`/`..`는 거부합니다.
- 웹훅: `X-IB-Timestamp`는 ASCII 숫자 1~16자리만, 본문은 1MB·중첩 64단계까지만 받습니다. 본문 오류는 `WebhookPayloadError`(→ 4xx)입니다.
- 결과·응답 모델의 `repr`에서 전화번호는 가리고(`010****0000`) 상담·MO 본문(`content`)은 길이만 보입니다. `ClientConfig`(API Key 포함)는 pickle할 수 없습니다.
- 발송은 `idempotency_key`가 없으면 타임아웃 후 자동 재시도하지 않습니다(중복 발송 방지).
- 리포트·MO 웹훅 서명은 constant-time으로 비교하고 timestamp 허용 오차(기본 300초)를 벗어난 오래된 요청을 거부합니다.
  운영 환경에서는 HTTPS, 발신 IP 허용 목록, `msgKey` 기준 중복 제거를 함께 적용하고, 중요한 판단은 조회 API로 결과를 확인하세요.
- 상담톡 웹훅에는 서명이 없습니다(서명은 리포트·MO 웹훅에만 적용). SDK는 서명 헤더를 무시하고 본문 크기·중첩·타입 검사만 적용하며, secret 없이 `parse_counsel_*`로 파싱할 수 있습니다.

## 공급망

- 런타임 의존성은 `httpx`, `pydantic` 두 개입니다.
- PyPI 배포는 GitHub Actions의 Trusted Publishing(OIDC)으로만 하며, 저장소에 PyPI 토큰을 두지 않습니다.
- 모든 커밋과 PR은 gitleaks로 검사하고, 의존성은 pip-audit으로 검사합니다.
