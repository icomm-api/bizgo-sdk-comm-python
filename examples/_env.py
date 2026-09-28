"""Read example settings from environment variables (never hard-code keys or phone numbers)."""

import os


def env(name: str, default: str = "") -> str:
    value = os.environ.get(name, default)
    if not value:
        raise SystemExit(f"환경변수 {name}를 설정하세요 (examples/README.md 참고)")
    return value
