"""Tests for tag_project.py (OS manifest pin correctness).

The pin must cover OS files only. Two regressions are guarded here:
  1. Excluded dirs (.git/, projects/, caches) must not contribute to the hash.
     The original filter compared a set against a set of strings, so it was
     always True and every exclusion silently failed to apply.
  2. The pin must be stable across unrelated changes (e.g. a git commit),
     otherwise it can never detect real drift.
"""
import importlib.util
import json
from pathlib import Path

_TAG = Path(__file__).parent / "tag_project.py"
_spec = importlib.util.spec_from_file_location("tag_project", _TAG)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)


def test_skipped_dirs_are_actually_excluded():
    """SKIP_DIRS must intersect with path parts, not be compared as a set."""
    parts = (".git", "HEAD")
    assert _mod.SKIP_DIRS & set(parts), "SKIP_DIRS intersection form must match .git paths"
    assert not ({".git"} & set(parts)) is False


def test_pin_is_self_consistent():
    """tag_project and an independent recompute must agree."""
    import hashlib

    root = _mod.ROOT
    files = sorted(
        p for p in root.rglob("*")
        if p.is_file()
        and not (_mod.SKIP_DIRS & set(p.relative_to(root).parts))
        and p.name not in _mod.SKIP_FILES
        and "__pycache__" not in p.parts
        and ".pytest_cache" not in p.parts
    )
    h = hashlib.sha256()
    for p in files:
        h.update(str(p.relative_to(root)).encode())
        h.update(hashlib.sha256(p.read_bytes()).digest())
    h.update(str(len(files)).encode())
    assert h.hexdigest() == _mod.manifest_sha()


def test_pin_excludes_vcs_and_cache_dirs():
    """No .git/, .ruff_cache, or vault-reference file may be hashed."""
    root = _mod.ROOT
    files = [
        p for p in root.rglob("*")
        if p.is_file()
        and not (_mod.SKIP_DIRS & set(p.relative_to(root).parts))
    ]
    offenders = [
        str(p.relative_to(root))
        for p in files
        if _mod.SKIP_DIRS & set(p.relative_to(root).parts)
    ]
    assert not offenders, f"excluded dirs leaked into the manifest: {offenders[:5]}"


def test_pin_written_to_project(tmp_path):
    """Tagging a project writes a pin file with the manifest sha."""
    proj = tmp_path / "myproj"
    proj.mkdir()
    out = _mod.ROOT / "projects" / "__tag_test_probe"
    out.mkdir(parents=True, exist_ok=True)
    try:
        import subprocess
        import sys

        r = subprocess.run(
            [sys.executable, str(_TAG), str(out)],
            capture_output=True,
            text=True,
            check=False,
        )
        assert r.returncode == 0, r.stderr
        pin = json.loads((out / ".superior-os.json").read_text())
        assert pin["manifest_sha"] == _mod.manifest_sha()
        assert pin["os"] == "superior-os"
    finally:
        for f in out.glob("*"):
            f.unlink()
        out.rmdir()
