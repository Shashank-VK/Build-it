#!/usr/bin/env python3
"""
scope-check.py
Checks whether a proposed new task conflicts with a project's No-gos list.
Usage: python3 scripts/scope-check.py --task "Add mobile app" --pitch projects/myapp/pitch.md
Solo AI Product Engineering System v1.0
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple


def extract_no_gos(content: str) -> List[str]:
    """Extract No-gos from a pitch document."""
    no_gos = []
    in_no_gos = False
    for line in content.splitlines():
        if re.match(r"#+\s*no.gos?", line, re.IGNORECASE):
            in_no_gos = True
            continue
        if in_no_gos and line.startswith("#"):
            break
        if in_no_gos and line.strip().startswith("-"):
            text = line.strip().lstrip("- ").strip()
            if text:
                no_gos.append(text)
    return no_gos


def check_conflict(task: str, no_gos: List[str]) -> Tuple[bool, List[str]]:
    """Check if a task description overlaps with any No-go."""
    task_words = set(task.lower().split())
    conflicts = []
    for no_go in no_gos:
        no_go_words = set(no_go.lower().split())
        if len(task_words & no_go_words) >= 2:
            conflicts.append(no_go)
    return bool(conflicts), conflicts


def main() -> int:
    parser = argparse.ArgumentParser(description="Check task against project No-gos")
    parser.add_argument("--task", required=True, help="Proposed task description")
    parser.add_argument("--pitch", required=True, help="Path to pitch.md")
    args = parser.parse_args()

    pitch_path = Path(args.pitch)
    if not pitch_path.exists():
        print(f"[scope-check] ERROR: Pitch file not found: {args.pitch}")
        return 1

    content = pitch_path.read_text(encoding="utf-8", errors="replace")
    no_gos = extract_no_gos(content)

    if not no_gos:
        print("[scope-check] WARNING: No No-gos section found in pitch document.")
        print("[scope-check] Add a '## No-gos' section with at least 3 explicit items.")
        print("[scope-check] Scope gate cannot run without it.")
        return 0

    has_conflict, conflicts = check_conflict(args.task, no_gos)

    if has_conflict:
        print("[scope-check] CONFLICT DETECTED")
        print(f"  Proposed task: {args.task}")
        print(f"  Conflicts with:")
        for c in conflicts:
            print(f"    - {c}")
        print()
        print("Options:")
        print("  1. Remove the task from the current scope")
        print("  2. Revise the No-gos with documented reason for the change")
        return 1
    else:
        print(f"[scope-check] PASSED: No conflict with {len(no_gos)} No-gos.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
