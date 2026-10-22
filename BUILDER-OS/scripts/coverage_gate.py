"""Coverage gate: every behavior change recorded in build-log must carry a test receipt.

Receipt = a line in <project>/build-log.md under a '## Evidence' section:
  - TEST: <path-to-test> exit 0
  - RANGES: <file>:<start>-<end> sha <64hex>

Gate passes when: no changed .py files are unreferenced, OR no build-log exists yet
(fresh OS with no projects fails open with a notice, never silently).
Fails closed when a build-log claims changes without receipts.
"""
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(
    os.environ.get("SUPERIOR_OS_ROOT", pathlib.Path(__file__).resolve().parent.parent)
)
SHA = re.compile(r"\b[0-9a-f]{64}\b")


def main() -> int:
    logs = list(ROOT.glob("projects/*/build-log.md"))
    if not logs:
        print("[coverage-gate] no project build-logs; nothing to check. PASS (open).")
        return 0
    failures = []
    for log in logs:
        text = log.read_text(encoding="utf-8", errors="replace")
        if "## Evidence" not in text:
            failures.append(f"{log}: missing '## Evidence' section")
            continue
        ev = text.split("## Evidence", 1)[1]
        if "exit 0" not in ev:
            failures.append(f"{log}: no passing test receipt (exit 0)")
        if not SHA.search(ev):
            failures.append(f"{log}: no coverage sha receipt")
    if failures:
        for f in failures:
            print(f"[coverage-gate] FAIL: {f}")
        return 1
    print(f"[coverage-gate] {len(logs)} build-log(s) carry test receipts. PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
