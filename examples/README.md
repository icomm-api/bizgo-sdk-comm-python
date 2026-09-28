# 예제

모든 예제는 **sandbox**(실제 발송 없음)에 연결하고, 값은 환경변수에서 읽습니다.

```bash
export BIZGO_API_KEY=...            # 콘솔 > 발송관리 > 연동관리 (코드에 쓰지 마세요)
export BIZGO_FROM=...               # 등록한 발신번호
export BIZGO_TO=...                 # 테스트 수신번호
python examples/send_sms.py
```

| 파일 | 내용 |
|---|---|
| `send_sms.py` | SMS 발송과 수신자별 접수 결과 확인 |
| `send_alimtalk_fallback.py` | 알림톡 발송, 실패 시 SMS 대체발송, 멱등성 키 |
| `send_mms.py` | 이미지 업로드 후 MMS 발송 |
| `poll_reports.py` | 리포트 Polling 처리(처리 성공 시에만 수신 확인) |
| `message_history.py` | 발송 이력 전체 조회(페이지 자동 순회)와 상태 조회 |
| `webhook_server.py` | 리포트 웹훅 수신 서버(서명 검증, 중복 처리, 5초 안에 응답) |
| `async_send.py` | 비동기 클라이언트로 여러 요청 동시 발송 |

각 예제의 `main()`은 테스트(`tests/test_examples.py`)에서 mock 서버로 실행되므로, 예제 코드는 항상 현재 SDK와 맞습니다.
