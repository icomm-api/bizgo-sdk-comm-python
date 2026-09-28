"""Every spec operation is reachable at ``client.<resource>.<method>`` with the right HTTP method, encoded path,
retry policy, rate bucket and pagination behaviour (SDK-DESIGN.md §10). Offline: uses bizgo.testing.FakeTransport."""

from __future__ import annotations

import pathlib
import re
from collections.abc import Callable
from typing import Any
from urllib.parse import quote

import pytest
import yaml

from bizgo import AsyncBizgo, Bizgo, InternalServerError, SmsMessage
from bizgo._operation import Operation
from bizgo._operations import OPERATIONS
from bizgo.models import _generated_request as req
from bizgo.testing import FakeTransport, success_envelope

SPEC = yaml.safe_load((pathlib.Path(__file__).parents[1] / "spec" / "openapi.yaml").read_text(encoding="utf-8"))
PARAMS = SPEC["components"]["parameters"]
SCHEMAS = SPEC["components"]["schemas"]
SEGMENT = "a/b?c"  # must be encoded, never interpreted as path/query
ENCODED = quote(SEGMENT, safe="")


def _spec_ops() -> list[tuple[str, str, dict[str, Any], list[Any]]]:
    out = []
    for path, item in SPEC["paths"].items():
        for method, op in item.items():
            if method != "parameters":
                out.append((path, method.upper(), op, item.get("parameters", [])))
    return out


SPEC_OPS = {op["operationId"]: (path, method, op, level) for path, method, op, level in _spec_ops()}


def _param(node: dict[str, Any]) -> dict[str, Any]:
    return PARAMS[node["$ref"].rsplit("/", 1)[1]] if "$ref" in node else node


def _ref(node: dict[str, Any]) -> str:
    if "$ref" in node:
        return str(node["$ref"]).rsplit("/", 1)[1]
    return next(str(p["$ref"]).rsplit("/", 1)[1] for p in node["allOf"] if "$ref" in p)


HANDWRITTEN: dict[str, Callable[[Any], Any]] = {
    "sendOmni": lambda c: c.send.omni(to="01000000000", messages=[SmsMessage(from_="01000000000", text="x")]),
    "uploadMmsFile": lambda c: c.files.upload_mms(b"x"),
    "uploadRcsFile": lambda c: c.files.upload_rcs(b"x"),
    "getReportPolling": lambda c: c.reports.poll(),
    "ackReportPolling": lambda c: c.reports.ack(SEGMENT),
    "getReportInquiry": lambda c: c.reports.inquiry(SEGMENT),
    "getMessageStatistics": lambda c: c.messages.statistics("20260101"),
    "getMessageHistory": lambda c: c.messages.history("2026-01-01T00:00:00"),
    "getMoHistory": lambda c: c.messages.mo_history("2026-01-01T00:00:00+09:00"),
    "getMessageStatusByMsgKey": lambda c: c.messages.status(SEGMENT),
    "getMessageStatusByRequestId": lambda c: c.messages.status_by_request_id(SEGMENT),
    "getMoByMsgKey": lambda c: c.messages.mo(SEGMENT),
}
HANDWRITTEN_ITERATORS: dict[str, Callable[[Any], Any]] = {
    "getMessageHistory": lambda c: c.messages.iter_history("2026-01-01T00:00:00"),
    "getMoHistory": lambda c: c.messages.iter_mo_history("2026-01-01T00:00:00+09:00"),
}


def _sample(op: Operation, api: str, kind: str) -> Any:
    _path, _method, raw, level = SPEC_OPS[op.id]
    schema: dict[str, Any] = {}
    for node in level + raw.get("parameters", []):
        p = _param(node)
        if p["name"] == api:
            schema = p.get("schema", {})
    if kind == "int":
        return max(int(schema.get("minimum", 1)), 1)
    if kind == "date":
        return "20260101"
    if kind == "datetime":
        return "2026-01-01T00:00:00"
    if kind == "array":
        return ["X"]
    if kind == "bool":
        return True
    return schema["enum"][0] if schema.get("enum") else "X"


def _form_sample(op: Operation, api: str, kind: str) -> Any:
    if kind == "file":
        return b"x"
    if kind == "files":
        return [b"x"]
    _path, _method, raw, _level = SPEC_OPS[op.id]
    schema = SCHEMAS[_ref(raw["requestBody"]["content"]["multipart/form-data"]["schema"])]
    prop = schema["properties"][api]
    if kind == "json":
        return getattr(req, _ref(prop)).model_construct()
    return prop["enum"][0] if prop.get("enum") else "X"


def target(client: Any, op: Operation, name: str | None = None) -> Any:
    node = client
    for attr in op.attribute[:-1]:
        node = getattr(node, attr)
    return getattr(node, name or op.attribute[-1])


def arguments(op: Operation, *, skip: str | None = None) -> tuple[list[Any], dict[str, Any]]:
    """Required arguments of the generated method (placeholders; path values that need encoding)."""
    args: list[Any] = [SEGMENT for p in op.params if p.location == "path"]
    kwargs: dict[str, Any] = {}
    _path, _method, raw, _level = SPEC_OPS[op.id]
    content = raw.get("requestBody", {}).get("content", {})
    if op.body == "json":
        args.append(getattr(req, _ref(content["application/json"]["schema"])).model_construct())
    for p in op.params:
        if not p.required or p.api == skip or p.location == "path" or (p.location == "form" and op.body == "json"):
            continue
        if p.location == "form":
            value = _form_sample(op, p.api, p.kind)
            if p.api == "file" and p.kind == "file":
                args.append(value)
            else:
                kwargs[p.python] = value
        else:
            kwargs[p.python] = _sample(op, p.api, p.kind)
    return args, kwargs


def call(client: Any, op: Operation) -> Any:
    if op.handwritten:
        return HANDWRITTEN[op.id](client)
    args, kwargs = arguments(op)
    return target(client, op)(*args, **kwargs)


def expected_path(template: str) -> str:
    return re.sub(r"\{\w+\}", ENCODED, template)


@pytest.fixture
def fake() -> FakeTransport:
    return FakeTransport()


def test_send_bucket_is_exactly_the_operations_tagged_in_the_spec() -> None:
    tagged = {op_id for op_id, (_p, _m, raw, _l) in SPEC_OPS.items() if raw.get("x-sdk-rate") == "send"}
    assert {op_id for op_id, op in OPERATIONS.items() if op.rate == "send"} == tagged
    assert tagged  # the spec tags at least sendOmni
    assert "sendOmni" in tagged


def test_operation_table_matches_the_spec() -> None:
    assert set(OPERATIONS) == set(SPEC_OPS)
    assert len(OPERATIONS) == 146
    for op_id, (path, method, raw, _level) in SPEC_OPS.items():
        op = OPERATIONS[op_id]
        assert (op.path, op.method, op.retry) == (path, method, raw["x-sdk-retry"])
        assert op.name == f"{raw['x-sdk-resource']}.{raw['x-sdk-method']}"
        assert op.rate == ("send" if raw.get("x-sdk-rate") == "send" else "other")
        assert (op.pagination is None) == ("x-sdk-pagination" not in raw)


@pytest.mark.parametrize("op_id", sorted(SPEC_OPS))
def test_operation_is_reachable_with_method_and_encoded_path(op_id: str, fake: FakeTransport) -> None:
    op = OPERATIONS[op_id]
    path, method, _raw, _level = SPEC_OPS[op_id]
    with fake.client() as client:
        assert callable(target(client, op))
        call(client, op)
    request = fake.last_request
    assert request.operation_id == op_id
    assert request.method == method
    assert request.path == expected_path(path)
    if "{" in path:
        assert SEGMENT not in request.path


@pytest.mark.parametrize("op_id", sorted(SPEC_OPS))
def test_retry_policy(op_id: str, fake: FakeTransport) -> None:
    op = OPERATIONS[op_id]
    fake.on(op_id).respond(503, {"common": {"authCode": "A000"}}).default()
    with fake.client() as client:
        if op.retry == "safe":
            call(client, op)
            assert len(fake.requests) == 2
        else:
            with pytest.raises(InternalServerError):
                call(client, op)
            assert len(fake.requests) == 1  # a create/send is never repeated after a 5xx


def _nested(body: dict[str, Any], path: tuple[str | int, ...], value: Any) -> None:
    node = body
    for step in path[:-1]:
        assert isinstance(step, str)
        node = node.setdefault(step, {})
    assert isinstance(path[-1], str)
    node[path[-1]] = value


PAGINATED = sorted(op_id for op_id, op in OPERATIONS.items() if op.pagination)


def _size(op: Operation) -> int:
    """Page size used by the test: 2, or the documented minimum of the size parameter."""
    assert op.pagination is not None
    return max(2, int(_sample(op, op.pagination.size, "int"))) if op.pagination.size else 2


def _pages(op: Operation) -> tuple[dict[str, Any], dict[str, Any], str]:
    """Two response bodies (a full first page, an empty second page) and the expected next request value."""
    pag = op.pagination
    assert pag is not None
    first = success_envelope()
    second = success_envelope()
    cursor_type = next((p.kind for p in op.params if p.api == pag.request), "text")
    if pag.style == "cursor":
        cursor: Any = 7 if cursor_type == "int" else "C7"
        assert pag.cursor is not None
        if -1 in pag.cursor:  # cursor taken from the last item
            item_key = pag.cursor[-1]
            assert isinstance(item_key, str)
            _nested(first, pag.items, [{item_key: cursor}])
        else:
            _nested(first, pag.items, [{}])
            _nested(first, pag.cursor, cursor)
        if pag.has_next:
            _nested(first, pag.has_next, True)
            _nested(second, pag.has_next, False)
        _nested(second, pag.items, [])
        return first, second, str(cursor)
    size = _size(op)
    _nested(first, pag.items, [{} for _ in range(size)])
    _nested(second, pag.items, [])
    if pag.total:
        _nested(first, pag.total, str(size * 10))  # int fields coerce it; some specs type total as a string
    if pag.has_next:
        _nested(first, pag.has_next, True)
    _path, _method, raw, _level = SPEC_OPS[op.id]
    default = next(
        (
            _param(p).get("schema", {}).get("default")
            for p in raw.get("parameters", [])
            if _param(p)["name"] == pag.request
        ),
        None,
    )
    start = int(default) if default is not None else (1 if pag.style == "page" else 0)
    return first, second, str(start + 1 if pag.style == "page" else start + size)


@pytest.mark.parametrize("op_id", PAGINATED)
def test_pagination_iterator_follows_pages(op_id: str, fake: FakeTransport) -> None:
    op = OPERATIONS[op_id]
    first, second, expected_next = _pages(op)
    fake.on(op_id).respond(200, first).respond(200, second)
    with fake.client() as client:
        if op.handwritten:
            items = list(HANDWRITTEN_ITERATORS[op_id](client))
        else:
            assert op.pagination is not None and op.iterator is not None
            args, kwargs = arguments(op, skip=op.pagination.request)
            if op.pagination.size:
                size = next(p.python for p in op.params if p.api == op.pagination.size)
                kwargs[size] = _size(op)
            items = list(target(client, op, op.iterator)(*args, **kwargs))
    assert op.pagination is not None
    assert len(items) == (1 if op.pagination.style == "cursor" else _size(op))
    requests = fake.requests_for(op_id)
    assert len(requests) == 2
    assert op.pagination.request not in requests[0].query or op.pagination.style != "cursor"
    assert requests[1].query[op.pagination.request] == expected_next


async def test_async_client_has_every_operation(fake: FakeTransport) -> None:
    async with fake.async_client() as client:
        assert isinstance(client, AsyncBizgo)
        for op in OPERATIONS.values():
            assert callable(target(client, op)), op.id
        page = await client.alimtalk.templates.list(sender_key="SENDER_KEY_EXAMPLE", limit=10)
        assert page == []
        items = [t async for t in client.alimtalk.templates.iter_list(sender_key="SENDER_KEY_EXAMPLE")]
        assert items == []
        created = await client.reservations.create(
            {
                "destinations": [{"to": "01000000000"}],
                "messageFlow": [{"sms": {"from": "01000000000", "text": "x"}}],
                "resvSendTime": "2026-05-01 10:00:00",
            }
        )
        assert created is not None and created.resv_key == "FAKE-RESVKEY-000001"
    assert fake.last_request.operation_id == "createReservation"


def test_sync_client_type(fake: FakeTransport) -> None:
    with fake.client() as client:
        assert isinstance(client, Bizgo)
