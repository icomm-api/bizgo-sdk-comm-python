from __future__ import annotations

import datetime as dt

import httpx
import pytest
import respx

from bizgo import Bizgo, models

from .conftest import envelope

REPORT = {"msgKey": "KEY001", "serviceType": "SMS", "msgType": "SM", "reportCode": "10000", "reportType": "0"}


def test_consume_acks_each_batch_after_handler(client: Bizgo, api: respx.MockRouter) -> None:
    api.get("/api/comm/v1/report/polling").mock(
        side_effect=[
            httpx.Response(200, json=envelope({"reportId": "R1", "report": [REPORT, REPORT]})),
            httpx.Response(200, json=envelope({"reportId": "", "report": None})),
        ]
    )
    ack = api.delete("/api/comm/v1/report/polling/R1").respond(json=envelope())
    seen: list[str] = []
    assert client.reports.consume(lambda reports: seen.extend(r.msg_key or "" for r in reports)) == 2
    assert seen == ["KEY001", "KEY001"]
    assert ack.call_count == 1


def test_consume_does_not_ack_when_handler_fails(client: Bizgo, api: respx.MockRouter) -> None:
    api.get("/api/comm/v1/report/polling").respond(json=envelope({"reportId": "R1", "report": [REPORT]}))
    ack = api.delete("/api/comm/v1/report/polling/R1")

    def handler(reports: list[models.Report]) -> None:
        raise RuntimeError("db down")

    with pytest.raises(RuntimeError):
        client.reports.consume(handler)
    assert not ack.called


def test_path_parameters_are_escaped(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.get(url__regex=r".*/report/inquiry/.*").respond(json=envelope({"report": [REPORT]}))
    client.reports.inquiry("a/b?c")
    assert route.calls.last.request.url.raw_path.endswith(b"/report/inquiry/a%2Fb%3Fc")


def test_iter_history_follows_last_seq(client: Bizgo, api: respx.MockRouter) -> None:
    msg = {"msgKey": "K", "serviceType": "SMS"}
    route = api.get("/api/comm/v1/message/history").mock(
        side_effect=[
            httpx.Response(200, json=envelope({"messages": [msg, msg], "lastSeq": 10, "hasNext": True})),
            httpx.Response(200, json=envelope({"messages": [msg], "lastSeq": 11, "hasNext": False})),
        ]
    )
    items = list(client.messages.iter_history(dt.datetime(2026, 9, 23, 9, 0), service_type=["SMS", "RCS"], limit=2))
    assert len(items) == 3
    first, second = (call.request.url.params for call in route.calls)
    assert first["requestTime"] == "2026-09-23T09:00:00"
    assert first["serviceType"] == "SMS,RCS"
    assert "lastSeq" not in first and second["lastSeq"] == "10"


def test_iter_history_stops_if_cursor_does_not_move(client: Bizgo, api: respx.MockRouter) -> None:
    page = envelope({"messages": [{"msgKey": "K"}], "lastSeq": 5, "hasNext": True})
    route = api.get("/api/comm/v1/message/history").respond(json=page)
    assert len(list(client.messages.iter_history("2026-09-23T09:00:00"))) == 2
    assert route.call_count == 2


def test_mo_history_time_is_sent_with_kst_offset(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.get("/api/comm/v1/message/history/mo").respond(json=envelope({"messages": [], "hasNext": False}))
    client.messages.mo_history(dt.datetime(2026, 4, 23, 14, 11, 1))
    assert route.calls.last.request.url.params["occurredTime"] == "2026-04-23T14:11:01+09:00"


def test_aware_datetime_is_converted_to_kst(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.get("/api/comm/v1/message/history").respond(json=envelope({"messages": []}))
    client.messages.history(dt.datetime(2026, 9, 23, 0, 0, tzinfo=dt.timezone.utc))
    assert route.calls.last.request.url.params["requestTime"] == "2026-09-23T09:00:00"


def test_limit_range(client: Bizgo) -> None:
    with pytest.raises(ValueError, match="1~1000"):
        client.messages.history("2026-09-23T09:00:00", limit=1001)


def test_statistics(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.get("/api/comm/v1/message/statistics").respond(
        json=envelope({"statistics": [{"statDate": "20260923", "recvTotalCnt": 3}]})
    )
    stats = client.messages.statistics(dt.date(2026, 9, 1), dt.date(2026, 9, 23), service_type="SMS")
    assert stats[0].recv_total_cnt == 3
    assert dict(route.calls.last.request.url.params) == {
        "startDate": "20260901",
        "endDate": "20260923",
        "serviceType": "SMS",
    }


def test_response_keeps_unknown_fields(client: Bizgo, api: respx.MockRouter) -> None:
    api.get("/api/comm/v1/message/inquiry/msgKey/K").respond(
        json=envelope({"messages": [{"msgKey": "K", "newServerField": "v"}]})
    )
    status = client.messages.status("K")[0]
    assert status.model_extra == {"newServerField": "v"}


def test_upload_mms_sends_multipart(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post("/api/comm/v1/file/mms").respond(
        json=envelope({"fileKey": "FILE_KEY_001", "expired": "2027-04-24T10:45:24+09:00"})
    )
    result = client.files.upload_mms(b"\xff\xd8jpeg-bytes", filename="a.jpg", image_name="banner")
    request = route.calls.last.request
    assert request.headers["Content-Type"].startswith("multipart/form-data; boundary=")
    assert b'name="file"; filename="a.jpg"' in request.content and b"Content-Type: image/jpeg" in request.content
    assert b'name="imageName"' in request.content
    assert result.file_key == "FILE_KEY_001"


def test_upload_mms_size_limit(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post("/api/comm/v1/file/mms")
    with pytest.raises(ValueError, match="300KB"):
        client.files.upload_mms(b"x" * (300 * 1024 + 1), filename="a.jpg")
    assert not route.called


def test_upload_brand_message_path(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.post("/api/comm/v1/file/brandmessage/wideItemList/first").respond(
        json=envelope({"imgUrl": "https://example.com/img.jpg"})
    )
    result = client.files.upload_brand_message(b"img", filename="a.png", kind="wideItemList/first")
    assert route.called and result.img_url == "https://example.com/img.jpg"
    with pytest.raises(ValueError):
        client.files.upload_brand_message(b"img", kind="../etc")  # type: ignore[arg-type]
