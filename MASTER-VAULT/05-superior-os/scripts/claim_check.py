"""Claim check: external claims in build-logs must carry URL + HTTP + date evidence.

Evidence row format inside '## Evidence':
  - CLAIM: <what> | URL: <https://...> | HTTP: <200> | DATE: <iso-date>

Gate passes when every CLAIM row has all three fields. Unverifiable claims must
be moved to a '## Quarantine' section instead (then this gate passes with notice).
"""
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(os.environ.get("SUPERIOR_OS_ROOT", pathlib.Path(__file__).resolve().parent.parent))
ROW = re.compile(r"^- CLAIM: .+\| URL: (\S+) \| HTTP: (\d{3}) \| DATE: (\S+)", re.M)


def main() -> int:
    logs = list(ROOT.glob("projects/*/build-log.md"))
    if not logs:
        print("[claim-check] no project build-logs; nothing to check. PASS (open).")
        return 0
    failures = []
    for log in logs:
        text = log.read_text(encoding="utf-8", errors="replace")
        if "## Evidence" not in text:
            continue
        ev = text.split("## Evidence", 1)[1].split("## Quarantine", 1)[0]
        for line in ev.splitlines():
            s = line.strip()
            if s.startswith("- CLAIM:") and not ROW.match(s):
                failures.append(f"{log}: malformed claim row: {s[:100]}")
    if failures:
        for f in failures:
            print(f"[claim-check] FAIL: {f}")
        return 1
    print(f"[claim-check] {len(logs)} build-log(s) claims evidenced. PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
