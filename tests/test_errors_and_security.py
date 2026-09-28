from __future__ import annotations

import logging

import httpx
import pytest
import respx

from bizgo import (
    APIConnectionError,
    AuthenticationError,
    BadRequestError,
    Bizgo,
    ConfigurationError,
    Environment,
    InternalServerError,
    InvalidResponseError,
    NotFoundError,
)

from .conftest import API_KEY, envelope

STATS = "/api/comm/v1/message/statistics"


def test_gateway_auth_failure_without_data(client: Bizgo, api: respx.MockRouter) -> None:
    # observed on sandbox: invalid key -> HTTP 401, common.authCode=A401, no data
    api.get(STATS).respond(
        401, json={"common": {"authCode": "A401", "authResult": "Unauthorized", "infobankTrId": "TR-1"}}
    )
    with pytest.raises(AuthenticationError) as info:
        client.messages.statistics("20260101")
    error = info.value
    assert (error.http_status, error.code, error.layer, error.tracking_id) == (401, "A401", "gateway", "TR-1")
    assert API_KEY not in str(error) and API_KEY not in repr(error)


def test_service_error_code_on_http_200_uses_documented_status(client: Bizgo, api: respx.MockRouter) -> None:
    api.get(STATS).respond(200, json=envelope(code="A306"))
    with pytest.raises(BadRequestError) as info:
        client.messages.statistics("20260101")
    assert info.value.layer == "service"
    assert info.value.description == "유효하지 않거나 비어있는 필드 (필드명 : to)"
    assert "필드명 : to" in str(info.value)


def test_same_code_means_different_things_per_layer(client: Bizgo, api: respx.MockRouter) -> None:
    api.get(STATS).respond(400, json=envelope(code="A401"))  # service A401 = invalid paymentCode
    with pytest.raises(BadRequestError):
        client.messages.statistics("20260101")
    api.get(STATS).respond(401, json={"common": {"authCode": "A401", "authResult": "Unauthorized"}})
    with pytest.raises(AuthenticationError):
        client.messages.statistics("20260101")


def test_not_found_status(client: Bizgo, api: respx.MockRouter) -> None:
    api.get(STATS).respond(404, json={"common": {"authCode": "A404", "authResult": "Not Found"}})
    with pytest.raises(NotFoundError):
        client.messages.statistics("20260101")


def test_server_error_with_html_body_is_retried_then_raised(client: Bizgo, api: respx.MockRouter) -> None:
    route = api.get(STATS).respond(502, text="<html>bad gateway</html>")
    with pytest.raises(InternalServerError):
        client.messages.statistics("20260101")
    assert route.call_count == 3


def test_success_status_with_non_json_body(client: Bizgo, api: respx.MockRouter) -> None:
    api.get(STATS).respond(200, text="ok")
    with pytest.raises(InvalidResponseError):
        client.messages.statistics("20260101")


def test_connection_error_hides_request_details(client: Bizgo, api: respx.MockRouter) -> None:
    api.get("/api/comm/v1/message/history/mo").mock(side_effect=httpx.ConnectError("refused"))
    with pytest.raises(APIConnectionError) as info:
        client.messages.mo_history("2026-04-23T14:11:01+09:00", from_="01000001234")
    assert "01000001234" not in str(info.value)
    assert info.value.__cause__ is None  # the httpx error (with the full URL) is not chained


def test_debug_log_has_no_key_query_or_body(
    client: Bizgo, api: respx.MockRouter, caplog: pytest.LogCaptureFixture
) -> None:
    api.get("/api/comm/v1/message/history/mo").respond(json=envelope({"messages": [], "hasNext": False}))
    with caplog.at_level(logging.DEBUG, logger="bizgo"):
        client.messages.mo_history("2026-04-23T14:11:01+09:00", from_="01000001234")
    text = caplog.text
    assert "GET /api/comm/v1/message/history/mo -> 200" in text
    assert API_KEY not in text and "01000001234" not in text


def test_client_repr_hides_key() -> None:
    client = Bizgo(API_KEY)
    assert API_KEY not in repr(client) and API_KEY not in repr(client._config)


@pytest.mark.parametrize("key", ["Bearer abc", "ApiKey abc", "  "])
def test_prefixed_or_blank_keys_are_rejected(key: str) -> None:
    with pytest.raises(ConfigurationError):
        Bizgo(key)


def test_api_key_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BIZGO_API_KEY", API_KEY)
    assert Bizgo().base_url == Environment.PRODUCTION.value


@pytest.mark.parametrize("url", ["http://mars.ibapi.kr", "ftp://example.com"])
def test_plain_http_base_url_is_rejected(url: str) -> None:
    with pytest.raises(ConfigurationError):
        Bizgo(API_KEY, base_url=url)


def test_localhost_http_is_allowed_for_mock_servers() -> None:
    assert Bizgo(API_KEY, base_url="http://localhost:4010").base_url == "http://localhost:4010"
