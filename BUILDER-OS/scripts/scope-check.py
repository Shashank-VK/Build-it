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


def _words(text: str) -> set:
    """Lowercase content words: strip punctuation, drop STOPWORDS."""
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOPWORDS}


STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "in", "on",
    "for", "with", "without", "no", "not", "we", "will",
    "would", "should", "could", "our", "is", "are", "be",
    "as", "by",
}


def extract_no_gos(content: str) -> list[str]:
    """Extract No-gos / Non-Goals from a pitch document."""
    no_gos = []
    in_no_gos = False
    for line in content.splitlines():
        if re.match(r"#+\s*(no.gos?|non.goals?)", line, re.IGNORECASE):
            in_no_gos = True
            continue
        if in_no_gos and line.startswith("#"):
            break
        if in_no_gos:
            stripped = line.strip()
            text = ""
            if stripped.startswith(("-", "*")):
                text = stripped[1:].strip()
            else:
                m = re.match(r"\d+\.\s+(.*)", stripped)
                if m:
                    text = m.group(1).strip()
            if text:
                no_gos.append(text)
    return no_gos


def check_conflict(task: str, no_gos: list[str]) -> tuple[bool, list[str]]:
    """Check if a task description overlaps with any No-go (>=2 content words)."""
    task_words = _words(task)
    conflicts = []
    for no_go in no_gos:
        no_go_words = _words(no_go)
        if len(task_words & no_go_words) >= 2:
            conflicts.append(no_go)
    return bool(conflicts), conflicts


def main() -> int:
    parser = argparse.ArgumentParser(description="Check task against project No-gos")
    parser.add_argument("--task", required=True, help="Proposed task description")
    parser.add_argument("--pitch", required=True, help="Path to pitch.md")
    parser.add_argument(
        "--tier",
        default="default",
        help="tiny warns+passes on missing section; default fails",
    )
    args = parser.parse_args()

    pitch_path = Path(args.pitch)
    if not pitch_path.exists():
        print(f"[scope-check] ERROR: Pitch file not found: {args.pitch}")
        return 1

    content = pitch_path.read_text(encoding="utf-8", errors="replace")
    no_gos = extract_no_gos(content)

    if not no_gos:
        print("[scope-check] WARNING: No No-gos section found in pitch document.")
        print("[scope-check] Add a '## No-gos' section with at least 2 explicit items.")
        print("[scope-check] Scope gate cannot run without it.")
        if args.tier == "tiny":
            return 0
        return 1

    has_conflict, conflicts = check_conflict(args.task, no_gos)

    if has_conflict:
        print("[scope-check] CONFLICT DETECTED")
        print(f"  Proposed task: {args.task}")
        print("  Conflicts with:")
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
