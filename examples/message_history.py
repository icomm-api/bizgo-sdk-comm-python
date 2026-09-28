"""Walk the send history of the last hour, then look up one message's status."""

import datetime as dt

from bizgo import Bizgo, Environment


def main(client: Bizgo) -> None:
    since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=1)  # converted to KST automatically
    failed = [
        m for m in client.messages.iter_history(since, service_type=["SMS", "ALIMTALK"]) if m.report_code != "10000"
    ]
    print(f"최근 1시간 실패 {len(failed)}건")
    for message in failed[:1]:
        for step in client.messages.status(message.msg_key or ""):  # one entry per channel tried (fallback)
            print(step.service_type, step.report_code, step.report_text)


if __name__ == "__main__":
    with Bizgo(environment=Environment.SANDBOX) as client:
        main(client)
