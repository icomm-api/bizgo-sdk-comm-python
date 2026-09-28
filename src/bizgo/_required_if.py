"""Conditional-required fields (``x-sdk-required-if``, SDK-DESIGN.md §4), checked before anything is sent.

The rules come from the spec (``_generated_required_if.py``); nothing is hard-coded here.

- Every request model checks its own rules when it is built (``required`` and relative ``requiredPaths``).
- A request body model (``SendOmniRequest``, ``ReservationCreateRequest``, ...) walks the whole body and checks
  every nested model's rules, including ``$.`` paths, which are evaluated from the body root
  (e.g. ``$.destinations[].replaceWords`` for a template alimtalk inside ``messageFlow``).

Messages name field paths and the rule's condition only, never input values.
"""

from __future__ import annotations

from collections.abc import Mapping
from functools import cache
from typing import Any

from pydantic import BaseModel

from ._generated_required_if import ROOTS, RULES, Rule

_OPS = {"equals": "==", "notEquals": "!=", "in": "in", "notIn": "not in"}


@cache
def _aliases(cls: type[BaseModel]) -> dict[str, str]:
    """API field name -> Python attribute name."""
    return {(info.serialization_alias or name): name for name, info in cls.model_fields.items()}


def _value(node: Any, name: str) -> Any:
    """The value the rule's ``when`` sees (spec defaults included)."""
    if isinstance(node, BaseModel):
        attr = _aliases(type(node)).get(name)
        return getattr(node, attr) if attr else None
    if isinstance(node, Mapping):
        return node.get(name)
    return None


def _sent(node: Any, name: str) -> Any:
    """The value that is serialized for ``name`` (``None`` when the field is unset or null)."""
    if isinstance(node, BaseModel):
        attr = _aliases(type(node)).get(name)
        return getattr(node, attr) if attr and attr in node.model_fields_set else None
    if isinstance(node, Mapping):
        return node.get(name)
    return None


def _has_field(node: Any, name: str) -> bool:
    if isinstance(node, BaseModel):
        return name in _aliases(type(node))
    return isinstance(node, Mapping)


def _text(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _applies(node: Any, rule: Rule) -> bool:
    field, op, values = rule[0], rule[1], rule[2]
    value = _value(node, field)
    if value is None:
        return op in ("notEquals", "notIn")
    hit = _text(value) in values
    return hit if op in ("equals", "in") else not hit


def _join(base: str, name: str) -> str:
    return f"{base}.{name}" if base else name


def _missing(node: Any, segments: list[str], label: str) -> list[str]:
    """Paths (with indexes) under ``node`` that are missing. ``name[]`` means every element of the array."""
    segment, rest = segments[0], segments[1:]
    is_array = segment.endswith("[]")
    name = segment[:-2] if is_array else segment
    here = _join(label, name)
    value = _sent(node, name)
    if is_array:
        if not isinstance(value, (list, tuple)):
            return []  # absent or empty array: no element to check (the array itself is a separate rule)
        found: list[str] = []
        for index, item in enumerate(value):
            where = f"{here}[{index}]"
            if item is None:
                found.append(".".join([where, *rest]))
            elif rest:
                found.extend(_missing(item, rest, where))
        return found
    if value is None:
        return [".".join([here, *rest])]  # a missing intermediate object makes the whole path missing
    return _missing(value, rest, here) if rest else []


def _rules_of(node: BaseModel) -> tuple[Rule, ...]:
    for cls in type(node).__mro__:
        if cls.__module__ == "bizgo.models._generated_request" and cls.__name__ in RULES:
            return RULES[cls.__name__]
    return ()


def check(node: BaseModel, label: str = "", root: BaseModel | None = None) -> list[str]:
    """Violations of ``node``'s own rules. ``$.`` paths are checked only when ``root`` (the body) is given."""
    problems: list[str] = []
    for rule in _rules_of(node):
        if not _applies(node, rule):
            continue
        field, op, values, required, paths = rule
        shown = values[0] if op in ("equals", "notEquals") else "[" + ", ".join(values) + "]"
        reason = f"required when {_join(label, field)} {_OPS[op]} {shown}"
        missing = [_join(label, name) for name in required if _sent(node, name) is None]
        for path in paths:
            if path.startswith("$."):
                segments = path[2:].split(".")
                if root is not None and _has_field(root, segments[0].removesuffix("[]")):
                    missing.extend(_missing(root, segments, ""))
            else:
                missing.extend(_missing(node, path.split("."), label))
        problems.extend(f"{path}: {reason}" for path in missing)
    return problems


def _walk(node: Any, label: str, root: BaseModel, problems: list[str]) -> None:
    if isinstance(node, BaseModel):
        problems.extend(check(node, label, root))
        for name, info in type(node).model_fields.items():
            value = getattr(node, name)
            if value is not None:
                _walk(value, _join(label, info.serialization_alias or name), root, problems)
    elif isinstance(node, (list, tuple)):
        for index, item in enumerate(node):
            _walk(item, f"{label}[{index}]", root, problems)


def violations(model: BaseModel) -> list[str]:
    """Rule violations for a model being built: the whole tree for a request body, its own rules otherwise."""
    cls = type(model)
    if cls.__module__ == "bizgo.models._generated_request" and cls.__name__ in ROOTS:
        problems: list[str] = []
        _walk(model, "", model, problems)
        return list(dict.fromkeys(problems))
    return check(model)
