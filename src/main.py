"""Minimal test entry point: prints a greeting and writes a dummy result."""

import json
from pathlib import Path


def main() -> None:
    print("hello from test-repo-20260831")
    out = Path(".research/results/test")
    out.mkdir(parents=True, exist_ok=True)
    (out / "metrics.json").write_text(json.dumps({"ok": True}) + "\n")
    print("wrote .research/results/test/metrics.json")


if __name__ == "__main__":
    main()
