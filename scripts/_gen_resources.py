"""Generate resource classes, the operation table and webhook parsers from the spec's ``x-sdk-*`` metadata.

Called by generate_models.py (so ``--check`` covers every generated file). Rules (SDK-DESIGN.md §10, §11.5):

- ``client.<x-sdk-resource>.<x-sdk-method>`` in snake_case; dotted resources are nested objects.
- Arguments: path parameters (positional, required, URL-encoded) -> request body model (positional) ->
  query/header parameters (keyword-only; optional ones default to ``None``). Multipart bodies become keyword
  arguments (files, JSON parts, text fields); a single required ``file`` field is positional.
- Return: the response model at ``x-sdk-result`` (default ``data.data``); lists are returned as lists; ``None`` for
  responses without data.
- Retry: ``x-sdk-retry``. Pagination: ``x-sdk-pagination`` adds ``iter_<method>``.
- Rate bucket: ``send`` exactly for operations marked ``x-sdk-rate: send``, ``other`` otherwise.
- Hand-written convenience methods (HANDWRITTEN_OPS) win: no generated method is emitted for them, and the
  hand-written resource classes (HANDWRITTEN_RESOURCES) subclass the generated ``<Name>Base`` class.
"""

from __future__ import annotations

import keyword
import pathlib
import re
import subprocess
import sys
import types
import typing
from typing import Any

HANDWRITTEN_RESOURCES = {"send", "files", "reports", "messages"}
HANDWRITTEN_OPS = {
    "sendOmni",
    "uploadMmsFile",
    "uploadRcsFile",
    "getReportPolling",
    "ackReportPolling",
    "getReportInquiry",
    "getMessageStatistics",
    "getMessageHistory",
    "getMoHistory",
    "getMessageStatusByMsgKey",
    "getMessageStatusByRequestId",
    "getMoByMsgKey",
}
HANDWRITTEN_WEBHOOKS = {"report", "mo"}
DATE_FORMATS = {"YYYYMMDD", "yyyyMMdd"}
DATETIME_FORMATS = {"yyyy-MM-dd'T'HH:mm:ss", "yyyy-MM-dd'T'HH:mm:ssXXX", "yyyy-MM-dd HH:mm:ss", "yyyyMMddHHmmss"}

HEADER = '"""Generated from spec/openapi.yaml by scripts/generate_models.py. Do not edit."""\n\n'


# ---------------------------------------------------------------- naming


def snake(name: str) -> str:
    out = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
    out = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", out).lower()
    out = re.sub(r"[^a-z0-9_]", "_", out)
    if keyword.iskeyword(out) or out in {"self", "cls"}:
        out += "_"
    return out


def pascal(parts: list[str]) -> str:
    return "".join(p[:1].upper() + p[1:] for part in parts for p in [part])


def parse_path(value: str) -> tuple[str | int, ...]:
    out: list[str | int] = []
    for piece in value.split("."):
        match = re.fullmatch(r"(\w+)((?:\[-?\d+\])*)", piece)
        if not match:
            raise SystemExit(f"bad x-sdk path: {value}")
        out.append(match.group(1))
        out.extend(int(i) for i in re.findall(r"\[(-?\d+)\]", match.group(2)))
    return tuple(out)


def doc_text(text: str | None) -> str:
    text = (text or "").strip().replace("\\", "\\\\").replace('"""', "'''")
    return text


def first_line(text: str | None) -> str:
    return doc_text(text).split("\n", 1)[0].strip()


# ---------------------------------------------------------------- spec helpers


class Spec:
    def __init__(self, spec: dict[str, Any]) -> None:
        self.raw = spec
        self.schemas: dict[str, Any] = spec["components"]["schemas"]
        self.parameters: dict[str, Any] = spec["components"].get("parameters", {})
        self.responses: dict[str, Any] = spec["components"].get("responses", {})

    def param(self, node: dict[str, Any]) -> dict[str, Any]:
        while "$ref" in node:
            node = self.parameters[node["$ref"].rsplit("/", 1)[1]]
        return node

    def schema(self, node: dict[str, Any]) -> dict[str, Any]:
        while "$ref" in node:
            node = self.schemas[node["$ref"].rsplit("/", 1)[1]]
        return node

    def response(self, node: dict[str, Any]) -> dict[str, Any]:
        while "$ref" in node:
            node = self.responses[node["$ref"].rsplit("/", 1)[1]]
        return node


def ref_name(node: dict[str, Any]) -> str | None:
    if "$ref" in node:
        return str(node["$ref"]).rsplit("/", 1)[1]
    for part in node.get("allOf", []):
        if "$ref" in part:
            return str(part["$ref"]).rsplit("/", 1)[1]
    return None


# ---------------------------------------------------------------- generated model introspection


def load_models(root: pathlib.Path, name: str, code: str) -> types.ModuleType:
    if "bizgo" not in sys.modules:
        # load only bizgo._base: the package __init__ imports files this generator is about to write
        package = types.ModuleType("bizgo")
        package.__path__ = [str(root / "src" / "bizgo")]
        sys.modules["bizgo"] = package
    from pydantic import BaseModel

    module = types.ModuleType(name)
    sys.modules[name] = module
    exec(compile(code, name, "exec"), module.__dict__)  # noqa: S102 - our own generated code
    for value in list(vars(module).values()):
        if isinstance(value, type) and issubclass(value, BaseModel) and value.__module__ == name:
            value.model_rebuild(_types_namespace=vars(module))
    return module


def _unwrap(tp: Any) -> Any:
    origin = typing.get_origin(tp)
    if origin in (typing.Union, types.UnionType):
        args = [a for a in typing.get_args(tp) if a is not type(None)]
        if len(args) == 1:
            return _unwrap(args[0])
    if origin is typing.Annotated:
        return _unwrap(typing.get_args(tp)[0])
    return tp


def type_at(cls: Any, path: tuple[str | int, ...]) -> Any:
    from pydantic import BaseModel

    tp: Any = cls
    for step in path:
        tp = _unwrap(tp)
        if isinstance(step, int):
            if typing.get_origin(tp) is not list:
                raise SystemExit(f"{cls.__name__}: {path}: not a list")
            tp = typing.get_args(tp)[0]
            continue
        if not (isinstance(tp, type) and issubclass(tp, BaseModel)):
            raise SystemExit(f"{cls.__name__}: {path}: {step} is not an object")
        for attr, info in tp.model_fields.items():
            if (info.validation_alias or info.alias or attr) == step:
                tp = info.annotation
                break
        else:
            raise SystemExit(f"{cls.__name__}: {path}: no field {step}")
    return _unwrap(tp)


def render(tp: Any, prefix: str = "_r") -> str:
    from pydantic import BaseModel

    tp = _unwrap(tp)
    origin = typing.get_origin(tp)
    if origin is list:
        return f"builtins.list[{render(typing.get_args(tp)[0], prefix)}]"
    if origin is dict:
        return "dict[str, Any]"
    if origin in (typing.Union, types.UnionType):
        return " | ".join(render(a, prefix) for a in typing.get_args(tp) if a is not type(None))
    if origin is typing.Literal:
        return "str"
    if isinstance(tp, type) and issubclass(tp, BaseModel):
        return f"{prefix}.{tp.__name__}"
    if tp in (str, int, float, bool):
        return tp.__name__
    return "Any"


# ---------------------------------------------------------------- operation model


class Arg:
    """One Python parameter of a generated method."""

    def __init__(
        self,
        api: str,
        location: str,
        required: bool,
        annotation: str,
        expr: str,
        kind: str,
        doc: str,
    ) -> None:
        self.api = api
        self.python = snake(api)
        self.location = location
        self.required = required
        self.annotation = annotation
        self.expr = expr  # uses {v} for the value
        self.kind = kind
        self.doc = doc


class Op:
    def __init__(self, spec: Spec, path: str, method: str, raw: dict[str, Any], path_level: list[Any]) -> None:
        self.spec = spec
        self.raw = raw
        self.path = path
        self.method = method.upper()
        self.id: str = raw["operationId"]
        self.resource: list[str] = raw["x-sdk-resource"].split(".")
        self.sdk_method: str = raw["x-sdk-method"]
        self.name = f"{raw['x-sdk-resource']}.{self.sdk_method}"
        self.py_method = snake(self.sdk_method)
        self.attribute = (*[snake(r) for r in self.resource], self.py_method)
        self.retry: str = raw["x-sdk-retry"]
        if self.retry not in ("safe", "rate_limit_only"):
            raise SystemExit(f"{self.id}: bad x-sdk-retry {self.retry}")
        # SDK-DESIGN.md §11.2/§11.5: the send bucket is data-driven (x-sdk-rate: send), everything else is other
        self.rate = "send" if raw.get("x-sdk-rate") == "send" else "other"
        self.handwritten = self.id in HANDWRITTEN_OPS
        self.result_path = parse_path(raw.get("x-sdk-result", "data.data"))
        self.fn = snake(self.id)
        params = [spec.param(p) for p in path_level + raw.get("parameters", [])]
        self.path_params = self._path_params(params)
        self.args: list[Arg] = [*self.path_params]
        self.body_model: str | None = None
        self.form: list[Arg] = []
        self.form_schema: str | None = None
        content = raw.get("requestBody", {}).get("content", {})
        self.body_required = bool(raw.get("requestBody", {}).get("required"))
        if "application/json" in content:
            self.body_model = ref_name(content["application/json"]["schema"])
        if "multipart/form-data" in content:
            self.form_schema = ref_name(content["multipart/form-data"]["schema"])
            self.form = self._form_args(content["multipart/form-data"])
        self.query = [self._query_arg(p) for p in params if p["in"] in ("query", "header")]
        self.pagination = raw.get("x-sdk-pagination")
        self.response_class = self._response_class()

    def _path_params(self, params: list[dict[str, Any]]) -> list[Arg]:
        by_name = {p["name"]: p for p in params if p["in"] == "path"}
        out = []
        for name in re.findall(r"\{(\w+)\}", self.path):
            p = by_name.get(name, {"name": name})
            out.append(
                Arg(name, "path", True, "str", f"segment({{v}}, '{name}')", "text", first_line(p.get("description")))
            )
        return out

    def _query_arg(self, p: dict[str, Any]) -> Arg:
        name = p["name"]
        schema = p.get("schema", {})
        required = bool(p.get("required"))
        typ = schema.get("type")
        fmt = schema.get("x-format") or p.get("x-format")
        doc = first_line(p.get("description"))
        if p["in"] == "header":
            return Arg(name, "header", required, "str", f'header("{name}", {{v}})', "text", doc)
        if typ == "array":
            explode = p.get("explode", p.get("style", "form") == "form")
            min_items = schema.get("minItems", 0)
            expr = f'array("{name}", {{v}}, explode={explode}, min_items={min_items})'
            return Arg(name, "query", required, "str | Sequence[str]", expr, "array", doc)
        if typ == "integer":
            expr = f'check_int("{name}", {{v}}, {schema.get("minimum")}, {schema.get("maximum")})'
            return Arg(name, "query", required, "int", expr, "int", doc)
        if typ == "number":
            return Arg(name, "query", required, "float", "{v}", "number", doc)
        if typ == "boolean":
            return Arg(name, "query", required, "bool", f'check_bool("{name}", {{v}})', "bool", doc)
        if fmt in DATE_FORMATS:
            return Arg(name, "query", required, "dt.date | str", f'date_param("{name}", {{v}})', "date", doc)
        if fmt in DATETIME_FORMATS:
            expr = f'datetime_param("{name}", {{v}}, {fmt!r})'
            return Arg(name, "query", required, "dt.datetime | str", expr, "datetime", doc)
        enum = schema.get("enum")
        annotation = "Literal[" + ", ".join(repr(e) for e in enum) + "]" if enum else "str"
        expr = f'check_str("{name}", {{v}}, max_length={schema.get("maxLength")}, enum={tuple(enum or ())!r})'
        return Arg(name, "query", required, annotation, expr, "text", doc)

    def _form_args(self, content: dict[str, Any]) -> list[Arg]:
        schema = self.spec.schema(content["schema"])
        required = set(schema.get("required", []))
        encoding = content.get("encoding", {})
        default_name = "image.jpg" if "image" in self.id.lower() or self.id.startswith("upload") else "file.bin"
        if self.id in {"uploadBrandMessageFriendGroupFile", "uploadCounselFile"}:
            default_name = "file.bin"
        out = []
        for name, prop in schema.get("properties", {}).items():
            doc = first_line(prop.get("description"))
            req = name in required
            if prop.get("format") == "binary":
                limit = prop.get("x-max-bytes")
                filename = "filename" if name == "file" else f"{snake(name)}_filename"
                expr = f'form.file("{name}", {{v}}, {filename}, "{default_name}", max_bytes={limit})'
                out.append(Arg(name, "form", req, "FileInput", expr, "file", doc))
            elif prop.get("type") == "array" and prop.get("items", {}).get("format") == "binary":
                expr = f'form.files_of("{name}", {{v}}, "{default_name}", {prop.get("maxItems")})'
                out.append(Arg(name, "form", req, "Sequence[FileInput]", expr, "files", doc))
            elif encoding.get(name, {}).get("contentType") == "application/json" or ref_name(prop):
                model = ref_name(prop)
                if model is None:
                    raise SystemExit(f"{self.id}: JSON part {name} without schema")
                expr = f'form.json("{name}", _q.{model}, {{v}})'
                out.append(Arg(name, "form", req, f"_q.{model} | Mapping[str, Any]", expr, "json", doc))
            else:
                enum = prop.get("enum")
                annotation = "Literal[" + ", ".join(repr(e) for e in enum) + "]" if enum else "str"
                check = f'check_str("{name}", {{v}}, max_length={prop.get("maxLength")}, enum={tuple(enum or ())!r})'
                out.append(Arg(name, "form", req, annotation, check, "text", doc))
        return out

    def _response_class(self) -> str | None:
        for code in ("200", "201"):
            if code in self.raw["responses"]:
                response = self.spec.response(self.raw["responses"][code])
                schema = response.get("content", {}).get("application/json", {}).get("schema", {})
                return ref_name(schema)
        return None


# ---------------------------------------------------------------- code emission


def _signature(op: Op, args: list[Arg], *, body: bool, form: bool, iterator: bool) -> tuple[str, list[str]]:
    """Return (parameter list, keyword call arguments)."""
    positional = [a for a in args if a.location == "path"]
    keyword_args = [a for a in args if a.location != "path"]
    parts = ["self"] + [f"{a.python}: {a.annotation}" for a in positional]
    call = [f"{a.python}={a.python}" for a in positional]
    if body:
        parts.append(f"body: _q.{op.body_model} | Mapping[str, Any]")
        call.append("body=body")
    form_args: list[Arg] = []
    if form:
        form_args = list(op.form)
        single = [a for a in form_args if a.api == "file" and a.required and a.kind == "file"]
        if single:
            parts.append("file: FileInput")
            call.append("file=file")
            form_args = [a for a in form_args if a is not single[0]]
    kw: list[str] = []
    ordered = [a for a in form_args + keyword_args if a.required] + [
        a for a in form_args + keyword_args if not a.required
    ]
    for a in ordered:
        kw.append(f"{a.python}: {a.annotation}" if a.required else f"{a.python}: {a.annotation} | None = None")
        call.append(f"{a.python}={a.python}")
    if form:
        for a in op.form:
            if a.kind == "file":
                fname = "filename" if a.api == "file" else f"{snake(a.api)}_filename"
                kw.append(f"{fname}: str | None = None")
                call.append(f"{fname}={fname}")
    if kw:
        parts.append("*")
        parts.extend(kw)
    return ", ".join(parts), call


def _call_function(op: Op, *, body: bool, form: bool, suffix: str = "") -> str:
    args = [a for a in op.args if a.location == "path"] + op.query
    params: list[str] = []
    for a in args:
        params.append(f"{a.python}: {a.annotation}" + ("" if a.required else " | None"))
    if body:
        params.append(f"body: _q.{op.body_model} | Mapping[str, Any]")
    if form:
        for a in op.form:
            params.append(f"{a.python}: {a.annotation}" + ("" if a.required else " | None"))
            if a.kind == "file":
                fname = "filename" if a.api == "file" else f"{snake(a.api)}_filename"
                params.append(f"{fname}: str | None")
    path = op.path
    for a in op.path_params:
        path = path.replace("{" + a.api + "}", "{" + a.expr.format(v=a.python) + "}")
    lines = [f"def _call_{op.fn}{suffix}(" + ("*, " + ", ".join(params) if params else "") + ") -> Call:"]
    if form:
        lines.append("    form = Form()")
        for a in op.form:
            if a.required:
                lines.append(f'    need("{a.api}", {a.python})')
            expr = a.expr.format(v=a.python)
            if a.kind == "text":
                expr = f'form.text("{a.api}", {expr})'
            lines.append(f"    {expr}")
    kwargs = [
        f'operation="{op.id}"',
        f'method="{op.method}"',
        f'path=f"{path}"' if op.path_params else f'path="{path}"',
        f"retry=Retry.{'SAFE' if op.retry == 'safe' else 'RATE_LIMIT_ONLY'}",
    ]
    query_args = [a for a in op.query if a.location == "query"]
    header_args = [a for a in op.query if a.location == "header"]
    if query_args:
        items = []
        for a in query_args:
            expr = a.expr.format(v=a.python)
            items.append(f'"{a.api}": ' + (f'need("{a.api}", {expr})' if a.required else expr))
        kwargs.append("params=query({" + ", ".join(items) + "})")
    if header_args:
        items = [f'"{a.api}": {a.expr.format(v=a.python)}' for a in header_args]
        kwargs.append("headers={" + ", ".join(items) + "}")
    if body:
        kwargs.append(f"json=json_body(_q.{op.body_model}, body)")
    if form:
        kwargs.append("**form.call_kwargs()")
    lines.append("    return Call(" + ", ".join(kwargs) + ")")
    return "\n".join(lines) + "\n"


class Emitter:
    def __init__(self, spec: Spec, ops: list[Op], response: types.ModuleType, request: types.ModuleType) -> None:
        self.spec = spec
        self.ops = ops
        self.response = response
        self.request = request

    def result(self, op: Op) -> tuple[str, str]:
        """(annotation, kind) of the value a method returns: kind is void, list, model (never None) or value."""
        if op.response_class is None or op.response_class == "ApiResponse":
            return "None", "void"
        cls = getattr(self.response, op.response_class)
        try:
            tp = type_at(cls, op.result_path)
        except SystemExit:
            if op.raw.get("x-sdk-result"):
                raise
            return "None", "void"  # no data.data in this response
        rendered = render(tp)
        if rendered.startswith("builtins.list["):
            return rendered, "list"
        if self._empty_constructible(tp):
            # SDK-DESIGN.md §12.19: a success response without data returns an empty result object, never None
            return rendered, "model"
        return f"{rendered} | None", "value"

    @staticmethod
    def _empty_constructible(tp: Any) -> bool:
        from pydantic import BaseModel

        tp = _unwrap(tp)
        if not (isinstance(tp, type) and issubclass(tp, BaseModel)):
            return False
        try:
            tp()
        except Exception:  # a result model with required fields cannot be empty
            return False
        return True

    def item_type(self, op: Op) -> str:
        cls = getattr(self.response, op.response_class or "")
        tp = type_at(cls, parse_path(op.pagination["items"]))
        rendered = render(tp)
        if not rendered.startswith("builtins.list["):
            raise SystemExit(f"{op.id}: pagination items is not a list")
        return rendered[len("builtins.list[") : -1]

    def docstring(self, op: Op, returns: str, *, indent: str = "        ", extra: str = "") -> str:
        summary = first_line(op.raw.get("summary")) or op.id
        description = doc_text(op.raw.get("description")).split("\n\n", 1)[0]
        lines = [f'"""{summary}.', ""]
        if description:
            lines += [*description.splitlines(), ""]
        retry = "429·5xx·네트워크 오류 재시도" if op.retry == "safe" else "429만 재시도"
        lines.append(f"``{op.method} {op.path}`` (``{op.id}``). {retry}, 속도 제한 버킷: ``{op.rate}``.")
        if extra:
            lines += ["", extra]
        documented = [a for a in op.args if a.location == "path"] + op.form + op.query
        if documented or op.body_model:
            lines += ["", "Args:"]
            for a in documented:
                lines.append(f"    {a.python}: {a.doc or a.api}")
            if op.body_model and not extra.startswith("multipart"):
                lines.append(
                    f"    body: :class:`~bizgo.models.{op.body_model}` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다."
                )
        lines += ["", "Returns:", f"    {returns}", ""]
        lines += [
            "Raises:",
            "    ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).",
            "    bizgo.APIError: 비즈고가 요청을 거절했습니다.",
            '"""',
        ]
        return "\n".join(indent + line if line else "" for line in lines)

    def methods(self, op: Op, is_async: bool) -> list[str]:
        annotation, kind = self.result(op)
        aw = "await " if is_async else ""
        adef = "async def" if is_async else "def"
        shown = annotation.replace("_r.", "").replace("builtins.", "")
        returns = {
            "void": "None (응답에 데이터가 없습니다).",
            "list": f"``{shown}`` (없으면 빈 목록).",
            "model": f"``{shown}`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). "
            "모델은 ``bizgo.models._generated_response``에 있습니다.",
            "value": f"``{shown}`` (데이터가 없으면 None).",
        }[kind]
        out = []
        variants: list[tuple[str, bool, bool, str]] = []
        if op.body_model:
            variants.append((op.py_method, True, False, ""))
            if op.form:
                variants.append(
                    (op.py_method + "_with_files", False, True, "multipart/form-data로 파일과 함께 보냅니다.")
                )
        elif op.form:
            variants.append((op.py_method, False, True, ""))
        else:
            variants.append((op.py_method, False, False, ""))
        for name, body, form, extra in variants:
            sig, call = _signature(op, op.args + op.query, body=body, form=form, iterator=False)
            suffix = "_form" if (form and op.body_model) else ""
            invoke = f"{aw}self._transport.call(_call_{op.fn}{suffix}({', '.join(call)}))"
            body_code = f"        {invoke}" if kind == "void" else f"        return _parse_{op.fn}({invoke})"
            out.append(
                f"    {adef} {name}({sig}) -> {annotation}:\n"
                + self.docstring(op, returns, extra=extra)
                + "\n"
                + body_code
                + "\n"
            )
        if op.pagination:
            out.append(self.iterator(op, is_async))
        return out

    def iterator(self, op: Op, is_async: bool) -> str:
        pag = op.pagination
        request = pag["request"]
        item = self.item_type(op)
        args = [a for a in op.args + op.query if a.api != request]
        sig, call = _signature(op, args, body=False, form=False, iterator=True)
        call.append(f"{snake(request)}=position")
        size = f"size={snake(pag['size'])}" if pag.get("size") else "size=None"
        start = self._start(op)
        resp = f"_r.{op.response_class}"
        summary = (
            f'        """Iterate over every page of :meth:`{op.py_method}` (``{op.id}``, {pag["style"]} pagination)."""'
        )
        if is_async:
            return (
                f"    def iter_{op.py_method}({sig}) -> AsyncIterator[{item}]:\n{summary}\n\n"
                f"        async def fetch(position: Any) -> Any:\n"
                f"            body = await self._transport.call(_call_{op.fn}({', '.join(call)}))\n"
                f"            return validate({resp}, body, {op.id!r})\n\n"
                f"        return aiterate(fetch, _PAGE_{op.fn.upper()}, {size}, start={start})\n"
            )
        return (
            f"    def iter_{op.py_method}({sig}) -> Iterator[{item}]:\n{summary}\n\n"
            f"        def fetch(position: Any) -> Any:\n"
            f"            body = self._transport.call(_call_{op.fn}({', '.join(call)}))\n"
            f"            return validate({resp}, body, {op.id!r})\n\n"
            f"        return iterate(fetch, _PAGE_{op.fn.upper()}, {size}, start={start})\n"
        )

    def _start(self, op: Op) -> str:
        pag = op.pagination
        if pag["style"] == "cursor":
            return "None"
        for p in op.raw.get("parameters", []):
            p = self.spec.param(p)
            if p["name"] == pag["request"] and "default" in p.get("schema", {}):
                return repr(int(p["schema"]["default"]))
        return "None"

    def pagination_constant(self, op: Op) -> str:
        pag = op.pagination
        fields = [f"style={pag['style']!r}", f"request={pag['request']!r}", f"items={parse_path(pag['items'])!r}"]
        if pag.get("size"):
            fields.append(f"size={pag['size']!r}")
        if pag["style"] == "cursor":
            fields.append(f"cursor={parse_path(pag['response'])!r}")
        if pag.get("hasNext"):
            fields.append(f"has_next={parse_path(pag['hasNext'])!r}")
        if pag.get("total"):
            fields.append(f"total={parse_path(pag['total'])!r}")
        return f"_PAGE_{op.fn.upper()} = Pagination({', '.join(fields)})\n"

    def parse_function(self, op: Op) -> str:
        annotation, kind = self.result(op)
        if kind == "void":
            return ""
        resp = f"_r.{op.response_class}"
        path = repr(op.result_path)
        if kind == "list":
            value = f"pick_list(validate({resp}, body, {op.id!r}), {path})"
        elif kind == "model":
            found = f"pick(validate({resp}, body, {op.id!r}), {path})"
            return (
                f"def _parse_{op.fn}(body: dict[str, Any]) -> {annotation}:\n"
                f"    found = {found}\n"
                f"    return found if isinstance(found, {annotation}) else {annotation}()\n"
            )
        else:
            value = f'cast("{annotation}", pick(validate({resp}, body, {op.id!r}), {path}))'
        return f"def _parse_{op.fn}(body: dict[str, Any]) -> {annotation}:\n    return {value}\n"

    # ------------------------------------------------------------ resources module

    def resources_module(self) -> str:
        tree: dict[str, Any] = {}
        for op in self.ops:
            node = tree
            for part in op.resource:
                node = node.setdefault(part, {"__ops__": []})
            node["__ops__"].append(op)
        helpers: list[str] = []
        for op in self.ops:
            if op.handwritten:
                continue
            if op.body_model:
                helpers.append(_call_function(op, body=True, form=False))
                if op.form:
                    helpers.append(_call_function(op, body=False, form=True, suffix="_form"))
            else:
                helpers.append(_call_function(op, body=False, form=bool(op.form)))
            parse = self.parse_function(op)
            if parse:
                helpers.append(parse)
            if op.pagination:
                helpers.append(self.pagination_constant(op))
        classes: list[str] = []
        roots: list[tuple[str, str]] = []
        for name, node in tree.items():
            self._classes(classes, [name], node)
            if name not in HANDWRITTEN_RESOURCES:
                roots.append((name, pascal([name])))
        root_sync = [
            "class Resources:",
            '    """Top-level resources generated from the spec (mixed into :class:`bizgo.Bizgo`)."""',
            "",
        ]
        root_async = ["class AsyncResources:", '    """Async version of :class:`Resources`."""', ""]
        for attr, cls in roots:
            root_sync.append(f"    {snake(attr)}: {cls}")
            root_async.append(f"    {snake(attr)}: Async{cls}")
        root_sync += ["", "    def _init_resources(self, transport: SyncTransport) -> None:"]
        root_async += ["", "    def _init_resources(self, transport: AsyncTransport) -> None:"]
        for attr, cls in roots:
            root_sync.append(f"        self.{snake(attr)} = {cls}(transport)")
            root_async.append(f"        self.{snake(attr)} = Async{cls}(transport)")
        body = (
            "\n\n".join(helpers)
            + "\n\n"
            + "\n\n".join(classes)
            + "\n\n"
            + "\n".join(root_sync)
            + "\n\n\n"
            + "\n".join(root_async)
            + "\n"
        )
        names = [
            "Form",
            "aiterate",
            "array",
            "check_bool",
            "check_int",
            "check_str",
            "date_param",
            "datetime_param",
            "header",
            "iterate",
            "json_body",
            "need",
            "pick",
            "pick_list",
            "query",
            "segment",
        ]
        runtime = [n for n in names if re.search(rf"\b{n}\(", body)]
        abc = [n for n in ("AsyncIterator", "Iterator", "Mapping", "Sequence") if re.search(rf"\b{n}\[", body)]
        typing_names = [n for n in ("Any", "Literal", "cast") if re.search(rf"\b{n}\b", body)]
        imports = "from __future__ import annotations\n\n"
        if "builtins." in body:
            imports += "import builtins\n"
        if "dt." in body:
            imports += "import datetime as dt\n"
        if abc:
            imports += f"from collections.abc import {', '.join(abc)}\n"
        imports += f"from typing import {', '.join(typing_names)}\n\n"
        if "Pagination(" in body:
            imports += "from .._operation import Pagination\n"
        imports += "from .._transport import AsyncTransport, Call, Retry, SyncTransport, validate\n"
        if "_q." in body:
            imports += "from ..models import _generated_request as _q\n"
        imports += "from ..models import _generated_response as _r\n"
        if "FileInput" in body:
            imports += "from ._common import FileInput\n"
        imports += "from ._runtime import " + ", ".join(runtime) + "\n\n"
        imports += "__all__ = [" + ", ".join(repr(n) for n in sorted(self._class_names)) + "]\n"
        doc = (
            '"""Generated from spec/openapi.yaml by scripts/generate_models.py. Do not edit.\n\n'
            "Resource classes for every operation in the spec (``client.<resource>.<method>``). Hand-written\n"
            "convenience methods in send/files/reports/messages take precedence (those classes subclass the\n"
            '``<Name>Base`` classes below).\n"""\n\n'
        )
        return doc + imports + "\n\n" + body

    _class_names: typing.ClassVar[set[str]] = set()

    def _classes(self, out: list[str], path: list[str], node: dict[str, Any]) -> None:
        children = {k: v for k, v in node.items() if k != "__ops__"}
        for child, sub in children.items():
            self._classes(out, [*path, child], sub)
        ops = [op for op in node["__ops__"] if not op.handwritten]
        base = pascal(path) + ("Base" if len(path) == 1 and path[0] in HANDWRITTEN_RESOURCES else "")
        for is_async in (False, True):
            cls = ("Async" if is_async else "") + base
            self._class_names.add(cls)
            transport = "AsyncTransport" if is_async else "SyncTransport"
            label = ".".join(snake(p) for p in path)
            doc = f'    """``client.{label}``' + (" (async)" if is_async else "") + '."""'
            lines = [f"class {cls}:", doc, ""]
            lines.append(f"    def __init__(self, transport: {transport}) -> None:")
            lines.append("        self._transport = transport")
            for child in children:
                child_cls = ("Async" if is_async else "") + pascal([*path, child])
                lines.append(f"        self.{snake(child)} = {child_cls}(transport)")
            body = "\n".join(lines) + "\n"
            for op in ops:
                for method in self.methods(op, is_async):
                    body += "\n" + method
            out.append(body)

    # ------------------------------------------------------------ operation table

    def operations_module(self) -> str:
        lines = [
            HEADER.rstrip(),
            "",
            "from __future__ import annotations",
            "",
            "from ._operation import Operation, Pagination, Param",
            "",
            "OPERATIONS: dict[str, Operation] = {",
        ]
        for op in self.ops:
            params = []
            for a in [*op.path_params, *op.query, *op.form]:
                params.append(f"Param({a.api!r}, {a.python!r}, {a.location!r}, {a.required}, {a.kind!r})")
            fields = [
                f"id={op.id!r}",
                f"name={op.name!r}",
                f"method={op.method!r}",
                f"path={op.path!r}",
                f"retry={op.retry!r}",
                f"rate={op.rate!r}",
                f"attribute={op.attribute!r}",
                f"handwritten={op.handwritten}",
                f"body={('json' if op.body_model else 'form' if op.form else None)!r}",
                "params=(" + "".join(p + ", " for p in params) + ")",
            ]
            if op.pagination:
                pag = self.pagination_constant(op).split(" = ", 1)[1].strip()
                fields.append(f"pagination={pag}")
                fields.append(f"iterator={'iter_' + op.py_method!r}")
            lines.append(f"    {op.id!r}: Operation({', '.join(fields)}),")
        lines.append("}")
        lines.append('"""Every spec operation by ``operationId``."""')
        return "\n".join(lines) + "\n"

    # ------------------------------------------------------------ webhooks

    def webhooks_module(self) -> str:
        hooks = []
        for name, item in self.spec.raw.get("webhooks", {}).items():
            for _method, raw in item.items():
                hooks.append((name, raw))
        parse, methods, table = [], [], []
        for name, raw in hooks:
            sdk_name = raw["x-sdk-webhook"]
            fn = snake(sdk_name)
            payload = ref_name(raw["requestBody"]["content"]["application/json"]["schema"])
            params = [self.spec.param(p) for p in raw.get("parameters", [])]
            signed = any(p["name"].lower() == "x-ib-signature" for p in params)
            summary = first_line(raw.get("summary")) or name
            table.append(f"    {sdk_name!r}: (_r.{payload}, {signed}),")
            if sdk_name in HANDWRITTEN_WEBHOOKS:
                continue
            parse.append(
                f"def parse_{fn}(body: bytes | str | Mapping[str, Any]) -> _r.{payload}:\n"
                f'    """{summary}: parse the body without verifying a signature."""\n'
                f"    return parse_payload(_r.{payload}, body)\n"
            )
            if signed:
                doc = "Verify the signature headers, then parse."
                check = "        self.verify(headers)\n"
            else:
                doc = (
                    "Parse the body.\n\n"
                    "        This webhook is not signed: no secret is used and signature headers, if present, are\n"
                    "        ignored. The body size cap, JSON depth limit and type checks still apply."
                )
                check = "        del headers  # not signed\n"
            ack_note = "\n        Answer with :meth:`counsel_ack`." if sdk_name.startswith("counsel") else ""
            methods.append(
                f"    def {fn}(self, headers: Mapping[str, str], body: bytes | str) -> _r.{payload}:\n"
                f'        """{summary} (``x-sdk-webhook: {sdk_name}``). {doc}{ack_note}"""\n'
                f"{check}"
                f"        return parse_{fn}(body)\n"
            )
        return (
            HEADER
            + "from __future__ import annotations\n\n"
            + "from collections.abc import Mapping\n"
            + "from typing import Any\n\n"
            + "from ._base import ResponseModel\n"
            + "from ._webhook_body import parse_payload\n"
            + "from .models import _generated_response as _r\n\n"
            + "WEBHOOKS: dict[str, tuple[type[ResponseModel], bool]] = {\n"
            + "\n".join(table)
            + "\n}\n"
            + '"""``x-sdk-webhook`` name -> (payload model, signed). Only signed webhooks (report, MO) are verified."""\n\n\n'
            + "\n\n".join(parse)
            + "\n\nclass WebhookMethods:\n"
            + '    """Generated webhook parsers, mixed into :class:`bizgo.webhooks.WebhookReceiver`."""\n\n'
            + "    def verify(self, headers: Mapping[str, str]) -> None:\n"
            + "        raise NotImplementedError\n\n"
            + "\n".join(methods)
        )


def ruff_format(code: str, name: str) -> str:
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "format", "--stdin-filename", name, "-"],
        input=code.encode("utf-8"),
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stderr.decode("utf-8", "replace"))
        raise SystemExit(f"ruff format failed for {name}")
    return result.stdout.decode("utf-8").replace("\r\n", "\n")


def collect(spec: Spec) -> list[Op]:
    ops = []
    seen: dict[tuple[str, ...], str] = {}
    for path, item in spec.raw["paths"].items():
        path_level = item.get("parameters", [])
        for method, raw in item.items():
            if method == "parameters":
                continue
            op = Op(spec, path, method, raw, path_level)
            if op.attribute in seen:
                raise SystemExit(f"{op.id}: {'.'.join(op.attribute)} clashes with {seen[op.attribute]}")
            seen[op.attribute] = op.id
            names = [a.python for a in op.args + op.query + op.form]
            if len(names) != len(set(names)) or "body" in names:
                raise SystemExit(f"{op.id}: parameter names clash: {names}")
            ops.append(op)
    return ops


def generate_resources(
    raw: dict[str, Any], request_code: str, response_code: str, root: pathlib.Path
) -> dict[pathlib.Path, str]:
    spec = Spec(raw)
    ops = collect(spec)
    response = load_models(root, "bizgo_codegen_response", response_code)
    request = load_models(root, "bizgo_codegen_request", request_code)
    emitter = Emitter(spec, ops, response, request)
    src = root / "src" / "bizgo"
    return {
        src / "resources" / "_generated.py": ruff_format(emitter.resources_module(), "_generated.py"),
        src / "_operations.py": ruff_format(emitter.operations_module(), "_operations.py"),
        src / "_generated_webhooks.py": ruff_format(emitter.webhooks_module(), "_generated_webhooks.py"),
    }
