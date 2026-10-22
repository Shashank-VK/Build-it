"""Tests for coverage_gate.py (SUPERIOR_OS_ROOT redirect)."""
import os
import subprocess
import sys
from pathlib import Path

GATE = Path(__file__).parent / "coverage_gate.py"


def run(root):
    env = dict(os.environ, SUPERIOR_OS_ROOT=str(root))
    return subprocess.run([sys.executable, str(GATE)], capture_output=True, text=True, env=env)


def test_no_projects_passes(tmp_path):
    assert run(tmp_path).returncode == 0


def test_good_receipt_passes(tmp_path):
    d = tmp_path / "projects" / "demo"
    d.mkdir(parents=True)
    (d / "build-log.md").write_text(
        "# Build log\n## Evidence\n- TEST: scripts/test_x.py exit 0\n"
        "- RANGES: app.py:1-40 sha " + "a" * 64 + "\n"
    )
    assert run(tmp_path).returncode == 0


def test_missing_evidence_fails(tmp_path):
    d = tmp_path / "projects" / "demo"
    d.mkdir(parents=True)
    (d / "build-log.md").write_text("# Build log\nno evidence here\n")
    assert run(tmp_path).returncode == 1
