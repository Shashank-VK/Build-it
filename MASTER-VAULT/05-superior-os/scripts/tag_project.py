#!/usr/bin/env python3
"""Tag a project to this OS copy: writes <project>/.superior-os.json pin.

Pin = {os, version, manifest_sha, tagged_at}. manifest_sha covers every OS file
except projects/, .provisioned, and caches, so doctor/verify can detect drift.
Usage: tag_project.py <project-dir>
"""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"projects"}
SKIP_FILES = {".provisioned", "guard.log", "spend.csv"}


def manifest_sha() -> str:
    h = hashlib.sha256()
    files = sorted(
        p for p in ROOT.rglob("*")
        if p.is_file()
        and SKIP_DIRS not in set(p.relative_to(ROOT).parts)
        and p.name not in SKIP_FILES
        and "__pycache__" not in p.parts
        and ".pytest_cache" not in p.parts
    )
    for p in files:
        rel = str(p.relative_to(ROOT))
        h.update(rel.encode())
        h.update(hashlib.sha256(p.read_bytes()).digest())
    h.update(str(len(files)).encode())
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: tag_project.py <project-dir>", file=sys.stderr)
        return 1
    proj = Path(sys.argv[1])
    if not proj.is_dir():
        print(f"not a directory: {proj}", file=sys.stderr)
        return 1
    pin = {
        "os": "superior-os",
        "version": "2.0.0",
        "manifest_sha": manifest_sha(),
        "tagged_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    (proj / ".superior-os.json").write_text(json.dumps(pin, indent=2) + "\n")
    print(f"[tag] {proj}/.superior-os.json manifest_sha={pin['manifest_sha'][:12]}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
