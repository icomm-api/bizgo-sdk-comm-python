"""Generate pydantic models from the vendored OpenAPI spec (spec/openapi.yaml).

Request models (every schema reachable from an operation's request body) get `RequestModel` as base class:
unknown fields are rejected and `x-max-bytes` limits are enforced.
Everything reachable from responses and webhook payloads gets `ResponseModel`: unknown fields are kept so new
server fields never break parsing. Schemas used on both sides (buttons, template items, ...) are generated in both
modules; ``bizgo.models`` exports the request version.

It also generates the resource classes, the operation table and the webhook parsers (see _gen_resources.py), and
the conditional-required rules table (``x-sdk-required-if``) checked by ``bizgo._required_if``.

Usage:
    python scripts/generate_models.py          # write src/bizgo/models/_generated_*.py
    python scripts/generate_models.py --check  # fail if the files are out of date (CI)
"""

from __future__ import annotations

import argparse
import copy
import difflib
import json
import pathlib
import re
import subprocess
import sys
import tempfile
from typing import Any

import yaml
from _gen_resources import generate_resources

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = ROOT / "spec" / "openapi.yaml"
ERROR_CODES = ROOT / "spec" / "error-codes.json"
OUT_DIR = ROOT / "src" / "bizgo" / "models"

CODEGEN_ARGS = [
    "--input-file-type",
    "openapi",
    "--output-model-type",
    "pydantic_v2.BaseModel",
    "--snake-case-field",
    "--use-field-description",
    "--use-schema-description",
    "--field-constraints",
    "--target-python-version",
    "3.10",
    "--use-standard-collections",
    "--use-union-operator",
    "--collapse-root-models",
    "--enum-field-as-literal",
    "all",
    "--allow-population-by-field-name",
    "--field-extra-keys",
    "x-max-bytes",
    "x-charset",
    "x-format",
    "--disable-timestamp",
    "--formatters",
    "black",
    "isort",
]

HEADER = '"""Generated from spec/openapi.yaml by scripts/generate_models.py. Do not edit."""\n\n'


def request_roots(spec: dict[str, Any]) -> tuple[set[str], set[str]]:
    """Schemas used as JSON request bodies, and schemas used as multipart form bodies."""
    json_roots: set[str] = set()
    form: set[str] = set()
    for item in spec["paths"].values():
        for method, op in item.items():
            if method == "parameters":
                continue
            for content_type, content in op.get("requestBody", {}).get("content", {}).items():
                names = refs(content.get("schema", {}))
                (json_roots if content_type == "application/json" else form).update(names)
    return json_roots, form


def refs(node: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
            found.add(ref.rsplit("/", 1)[1])
        for value in node.values():
            found |= refs(value)
    elif isinstance(node, list):
        for value in node:
            found |= refs(value)
    return found


def closure(schemas: dict[str, Any], roots: list[str]) -> set[str]:
    seen: set[str] = set()
    stack = list(roots)
    while stack:
        name = stack.pop()
        if name in seen:
            continue
        seen.add(name)
        stack.extend(refs(schemas[name]) - seen)
    return seen


def drop_datetime_format(node: Any) -> None:
    """Keep response timestamps as plain strings so an unexpected server format never breaks parsing."""
    if isinstance(node, dict):
        if node.get("format") == "date-time":
            del node["format"]
        for value in node.values():
            drop_datetime_format(value)
    elif isinstance(node, list):
        for value in node:
            drop_datetime_format(value)


ENVELOPE_SCHEMAS = ("CommonResult", "ServiceResult", "ApiResponse")


def relax_envelopes(schemas: dict[str, Any]) -> None:
    """Envelope fields (``common``, ``authResult``, ``data.result``, ...) are never required in response models
    (SDK-DESIGN.md §12.1): a minimal but valid success envelope must parse. The transport already checks the codes.
    """
    for name, schema in schemas.items():
        if name in ENVELOPE_SCHEMAS or name.endswith(("Response", "ServiceResult")):
            schema.pop("required", None)
            for part in schema.get("allOf", []):
                if isinstance(part, dict):
                    part.pop("required", None)


_ALIAS = re.compile(r"(?<=[(\s,])alias='([^']+)'")
_POSITIONAL_DEFAULT = re.compile(r"\bField\((\s*)(?!\.\.\.|\)|[A-Za-z_]\w*\s*=)")


def split_aliases(code: str) -> str:
    """Make generated fields type-check without the pydantic mypy plugin (SDK-DESIGN.md §12.13).

    - ``alias=`` -> ``validation_alias=`` + ``serialization_alias=``: type checkers (``dataclass_transform``) only
      look at ``alias``, so the typed ``__init__`` keeps the Python field names (``sender_key=``, ``from_=``) while
      API names are still accepted on input and used on output.
    - ``Field(None, ...)`` -> ``Field(default=None, ...)``: a positional default is invisible to
      ``dataclass_transform``, which would make the field look required. ``Field(...)`` (required) is unchanged.
    """
    code = _ALIAS.sub(r"validation_alias='\1', serialization_alias='\1'", code)
    return _POSITIONAL_DEFAULT.sub(r"Field(\1default=", code)


def generate(spec: dict[str, Any], names: set[str], base_class: str, *, lenient: bool = False) -> str:
    doc = {
        "openapi": spec["openapi"],
        "info": spec["info"],
        "paths": {},
        "components": {"schemas": {n: copy.deepcopy(spec["components"]["schemas"][n]) for n in sorted(names)}},
    }
    if lenient:
        drop_datetime_format(doc["components"])
        relax_envelopes(doc["components"]["schemas"])
    with tempfile.TemporaryDirectory() as tmp:
        src = pathlib.Path(tmp) / "spec.yaml"
        out = pathlib.Path(tmp) / "models.py"
        src.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding="utf-8")
        subprocess.run(
            [
                sys.executable,
                "-m",
                "datamodel_code_generator",
                "--input",
                str(src),
                "--output",
                str(out),
                "--base-class",
                base_class,
                *CODEGEN_ARGS,
            ],
            check=True,
        )
        code = out.read_text(encoding="utf-8")
    # drop the generator's own header comment block (it contains a temp file name)
    lines = code.splitlines()
    while lines and (lines[0].startswith("#") or not lines[0].strip()):
        lines.pop(0)
    return HEADER + split_aliases("\n".join(lines).rstrip()) + "\n"


def add_flow_discriminator(code: str, spec: dict[str, Any]) -> str:
    """Make ``messageFlow`` items a discriminated union keyed by the channel property.

    Without this pydantic tries every channel and reports one error per channel.
    """
    schemas = spec["components"]["schemas"]
    members = [ref.rsplit("/", 1)[1] for ref in (s["$ref"] for s in schemas["MessageFlowItem"]["oneOf"])]
    keys = {name: schemas[name]["required"][0] for name in members}
    union = re.compile(r"message_flow: list\[\s*" + r"\s*\|\s*".join(members) + r"\s*\]", re.S)
    if not union.search(code):
        raise SystemExit("messageFlow union not found in generated code")
    code = union.sub("message_flow: list[MessageFlowItem]", code)
    tags = ",\n".join(f"    Annotated[{name}, Tag({key!r})]" for name, key in keys.items())
    helper = (
        "_FLOW_KEYS = frozenset({" + ", ".join(repr(k) for k in keys.values()) + "})\n\n\n"
        "def _flow_key(value: Any) -> str | None:\n"
        '    """Return the channel key of a messageFlow item (``sms``, ``alimtalk``, ...)."""\n'
        "    if isinstance(value, dict):\n"
        "        found = [k for k in value if k in _FLOW_KEYS]\n"
        "        return found[0] if len(found) == 1 else None\n"
        "    for name, key in _FLOW_CLASS_KEYS.items():\n"
        "        if type(value).__name__ == name:\n"
        "            return key\n"
        "    return None\n\n\n"
        "_FLOW_CLASS_KEYS = {" + ", ".join(f"{n!r}: {k!r}" for n, k in keys.items()) + "}\n\n"
        "MessageFlowItem = Annotated[\n    Union[\n" + tags + ",\n    ],\n"
        "    Discriminator(_flow_key, custom_error_type='message_flow_channel',"
        " custom_error_message='messageFlow 항목에는 채널 키("
        + ", ".join(keys.values())
        + ") 중 정확히 하나가 있어야 합니다'),\n]\n"
        '"""messageFlow 항목 1개. 채널 키 하나만 가진 객체입니다."""\n\n\n'
    )
    code = code.replace("class SendOmniRequest(", helper + "class SendOmniRequest(", 1)
    code = code.replace("from typing import Any, Literal", "from typing import Annotated, Any, Literal, Union", 1)
    return code.replace(
        "from pydantic import ConfigDict, Field", "from pydantic import ConfigDict, Discriminator, Field, Tag", 1
    )


def error_code_table() -> str:
    """Service-layer (data.code) codes with their documented HTTP status and Korean description."""
    data = json.loads(ERROR_CODES.read_text(encoding="utf-8"))
    rows = []
    for entry in data["service"]:
        status = int(entry["httpStatus"]) if entry.get("httpStatus") else 0
        text = entry.get("descriptionKo") or entry.get("result") or ""
        rows.append(f"    {entry['code']!r}: ({status}, {text!r}),")
    header = '"""Generated from spec/error-codes.json by scripts/generate_models.py. Do not edit."""\n\n'
    return (
        header
        + f"SOURCE = {data.get('source')!r}\n\n"
        + "# code -> (documented HTTP status, Korean description) for the service layer (data.code)\n"
        + "SERVICE_CODES: dict[str, tuple[int, str]] = {\n"
        + "\n".join(rows)
        + "\n}\n"
    )


REQUIRED_IF_OPS = {"equals": False, "notEquals": False, "in": True, "notIn": True}  # operator -> takes a list


def _rule_value(value: Any) -> str:
    """Rule values are compared as strings (booleans as ``true``/``false``)."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None or isinstance(value, (dict, list)):
        raise SystemExit(f"x-sdk-required-if: unsupported value {value!r}")
    return str(value)


def required_if_table(spec: dict[str, Any], request: set[str], roots: set[str], request_code: str) -> str:
    """``x-sdk-required-if`` rules of request schemas, as data for ``bizgo._required_if`` (AGENTS.md rule 11 of
    bizgo-api-spec, SDK-DESIGN.md §4). The spec format is checked strictly so a typo fails generation."""
    schemas = spec["components"]["schemas"]
    lines: list[str] = []
    for name in sorted(request):
        rules = schemas[name].get("x-sdk-required-if")
        if rules is None:
            continue
        where = f"{name}.x-sdk-required-if"
        props = set(schemas[name].get("properties", {}))
        if not isinstance(rules, list) or not rules:
            raise SystemExit(f"{where}: must be a non-empty list")
        if f"class {name}(" not in request_code:
            raise SystemExit(f"{where}: no generated request model {name}")
        entries: list[str] = []
        for index, rule in enumerate(rules):
            here = f"{where}[{index}]"
            if not isinstance(rule, dict) or set(rule) - {"when", "required", "requiredPaths"}:
                raise SystemExit(f"{here}: unknown keys")
            when = rule.get("when")
            if not isinstance(when, dict) or when.get("field") not in props:
                raise SystemExit(f"{here}.when.field: must be a property of {name}")
            ops = [op for op in when if op != "field"]
            if len(ops) != 1 or ops[0] not in REQUIRED_IF_OPS:
                raise SystemExit(f"{here}.when: exactly one of {sorted(REQUIRED_IF_OPS)} is required")
            op = ops[0]
            raw = when[op]
            if REQUIRED_IF_OPS[op] != isinstance(raw, list) or (isinstance(raw, list) and not raw):
                raise SystemExit(f"{here}.when.{op}: {'a non-empty list' if REQUIRED_IF_OPS[op] else 'one value'}")
            values = tuple(_rule_value(v) for v in (raw if isinstance(raw, list) else [raw]))
            required = rule.get("required", [])
            paths = rule.get("requiredPaths", [])
            if not isinstance(required, list) or not isinstance(paths, list) or not (required or paths):
                raise SystemExit(f"{here}: required and/or requiredPaths (lists) needed")
            for prop in required:
                if prop not in props:
                    raise SystemExit(f"{here}.required: {prop!r} is not a property of {name}")
            for path in paths:
                segments = path[2:].split(".") if isinstance(path, str) and path.startswith("$.") else None
                if segments is None:
                    segments = path.split(".") if isinstance(path, str) else [""]
                    if segments[0].removesuffix("[]") not in props:
                        raise SystemExit(f"{here}.requiredPaths: {path!r} does not start at a property of {name}")
                if not all(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*(\[\])?", seg) for seg in segments):
                    raise SystemExit(f"{here}.requiredPaths: bad path {path!r}")
            entries.append(f"        ({when['field']!r}, {op!r}, {values!r}, {tuple(required)!r}, {tuple(paths)!r}),")
        lines.append(f"    {name!r}: (\n" + "\n".join(entries) + "\n    ),")
    header = (
        '"""Generated from spec/openapi.yaml (x-sdk-required-if) by scripts/generate_models.py. Do not edit."""\n\n'
    )
    root_list = "\n".join(f"        {n!r}," for n in sorted(roots))
    return (
        header
        + "Rule = tuple[str, str, tuple[str, ...], tuple[str, ...], tuple[str, ...]]\n"
        + '"""(when field, operator, values, required properties, required paths). API field names."""\n\n'
        + "RULES: dict[str, tuple[Rule, ...]] = {\n"
        + "\n".join(lines)
        + "\n}\n"
        + '"""Request model name -> conditional-required rules (AND-ed)."""\n\n'
        + "ROOTS: frozenset[str] = frozenset(\n    {\n"
        + root_list
        + "\n    }\n)\n"
        + '"""Request body models: ``$.`` paths are evaluated from these (the whole body is validated there)."""\n'
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    spec = yaml.safe_load(SPEC.read_text(encoding="utf-8"))
    schemas = spec["components"]["schemas"]
    json_roots, form_schemas = request_roots(spec)
    # multipart bodies are built by the SDK (form fields); the JSON parts they carry are request models
    form_refs = set().union(*(refs(schemas[n]) for n in form_schemas)) if form_schemas else set()
    request = closure(schemas, sorted(json_roots | form_refs)) - form_schemas
    response = closure(schemas, sorted(set(schemas) - request - form_schemas))

    request_code = add_flow_discriminator(generate(spec, request, "bizgo._base.RequestModel"), spec)
    response_code = generate(spec, response, "bizgo._base.ResponseModel", lenient=True)
    outputs = {
        OUT_DIR / "_generated_request.py": request_code,
        OUT_DIR / "_generated_response.py": response_code,
        ROOT / "src" / "bizgo" / "_error_codes.py": error_code_table(),
        ROOT / "src" / "bizgo" / "_generated_required_if.py": required_if_table(
            spec, request, (json_roots | form_refs) & request, request_code
        ),
    }
    outputs.update(generate_resources(spec, request_code, response_code, ROOT))
    stale = False
    for path, code in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current == code:
            continue
        if args.check:
            stale = True
            sys.stdout.writelines(
                difflib.unified_diff(current.splitlines(True), code.splitlines(True), str(path), "generated", n=1)
            )
        else:
            path.write_text(code, encoding="utf-8", newline="\n")
            print(f"wrote {path.relative_to(ROOT)}")
    if stale:
        sys.exit("generated models are out of date: run python scripts/generate_models.py")


if __name__ == "__main__":
    main()
