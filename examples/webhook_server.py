"""Receive delivery report webhooks with the standard library.

Production checklist:
- serve over HTTPS and allow only the Bizgo webhook source IPs (see the API overview page)
- answer within 5 seconds; do slow work asynchronously
- deduplicate by msg_key (Bizgo retries up to 3 times)
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from bizgo.webhooks import WebhookReceiver, WebhookVerificationError

seen: set[str] = set()  # stand-in for a persistent dedup store


def handle(receiver: WebhookReceiver, headers: dict[str, str], body: bytes) -> tuple[int, dict[str, str]]:
    """Return (HTTP status, JSON body). Framework-independent so it is easy to test and reuse."""
    try:
        report = receiver.report(headers, body)
    except WebhookVerificationError:
        return 401, {}
    if report.msg_key not in seen:
        seen.add(report.msg_key)
        # enqueue report for processing here
    return 200, receiver.ack(report.msg_key)


class Handler(BaseHTTPRequestHandler):
    receiver: WebhookReceiver

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length") or 0)
        status, payload = handle(self.receiver, dict(self.headers.items()), self.rfile.read(min(length, 1024 * 1024)))
        data = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format: str, *args: object) -> None:  # keep phone numbers out of access logs
        pass


if __name__ == "__main__":
    Handler.receiver = WebhookReceiver(os.environ["BIZGO_WEBHOOK_SECRET"])
    HTTPServer(("127.0.0.1", 8080), Handler).serve_forever()  # put a TLS reverse proxy in front
