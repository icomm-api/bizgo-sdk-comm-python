"""Process delivery reports with polling (the API key must be set to POLLING in the console)."""

from bizgo import Bizgo, Environment
from bizgo.models import Report

store: dict[str, str] = {}  # stand-in for your database


def save(reports: list[Report]) -> None:
    for report in reports:
        # upsert by msg_key: a batch is delivered again if this function raises before the ack
        store[report.msg_key or ""] = "delivered" if report.report_code == "10000" else f"failed:{report.report_code}"


def main(client: Bizgo) -> None:
    handled = client.reports.consume(save)  # polls, calls save(), acks only after save() succeeded
    print(f"리포트 {handled}건 처리")


if __name__ == "__main__":
    with Bizgo(environment=Environment.SANDBOX) as client:
        main(client)
