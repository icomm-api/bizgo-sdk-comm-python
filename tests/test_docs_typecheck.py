"""Every ```python block in README.md and llms.txt passes ``mypy --strict`` (SDK-DESIGN.md §12.13).

Checked twice: with the pydantic mypy plugin (the documented optional setup) and without it (plain ``--strict``).
Blocks are fragments of one page, so each is checked after a small prelude that defines the names the README
assumes (``client``, ``db``, ``receiver``, ...).
"""

from __future__ import annotations

import pathlib
import re

import pytest

mypy_api = pytest.importorskip("mypy.api")

ROOT = pathlib.Path(__file__).parents[1]
PRELUDE = '''from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from bizgo import Bizgo
from bizgo.testing import FakeTransport
from bizgo.webhooks import WebhookReceiver, WebhookVerificationError

client: Bizgo = FakeTransport().client()
db: Any = None
recipients: list[str] = ["01000000000"]
msg_key = "MSG_KEY_EXAMPLE"
request_id = "REQUEST_ID_EXAMPLE"
receiver = WebhookReceiver("test-webhook-secret")
_ = (Mapping, WebhookVerificationError)


def enqueue(item: object) -> None:
    """Stand-in for the reader's own queue."""

'''


def blocks() -> list[tuple[str, str]]:
    out = []
    for name in ("README.md", "llms.txt"):
        text = (ROOT / name).read_text(encoding="utf-8")
        for index, match in enumerate(re.finditer(r"```python\n(.*?)```", text, re.S)):
            out.append((f"{name.split('.')[0].lower()}_{index}", match.group(1)))
    return out


def test_docs_have_python_blocks() -> None:
    names = [name for name, _ in blocks()]
    assert any(n.startswith("readme") for n in names) and any(n.startswith("llms") for n in names)


@pytest.mark.parametrize("plugin", [True, False], ids=["pydantic-plugin", "plain-strict"])
def test_doc_snippets_pass_mypy_strict(tmp_path: pathlib.Path, plugin: bool) -> None:
    files = []
    for name, code in blocks():
        path = tmp_path / f"doc_{name}.py"
        path.write_text(PRELUDE + code, encoding="utf-8")
        files.append(str(path))
    config = tmp_path / "mypy.ini"
    config.write_text(
        "[mypy]\nstrict = True\n" + ("plugins = pydantic.mypy\n" if plugin else "") + "[mypy-opentelemetry.*]\n"
        "ignore_missing_imports = True\n",
        encoding="utf-8",
    )
    stdout, stderr, status = mypy_api.run(
        ["--config-file", str(config), "--cache-dir", str(tmp_path / ".mypy_cache"), "--no-error-summary", *files]
    )
    assert status == 0, stdout + stderr
