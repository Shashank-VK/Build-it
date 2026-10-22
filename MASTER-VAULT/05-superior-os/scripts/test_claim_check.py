"""Tests for claim_check.py (SUPERIOR_OS_ROOT redirect)."""
import os
import subprocess
import sys
from pathlib import Path

GATE = Path(__file__).parent / "claim_check.py"


def run(root):
    env = dict(os.environ, SUPERIOR_OS_ROOT=str(root))
    return subprocess.run([sys.executable, str(GATE)], capture_output=True, text=True, env=env)


def test_no_projects_passes(tmp_path):
    assert run(tmp_path).returncode == 0


def test_good_claim_passes(tmp_path):
    d = tmp_path / "projects" / "demo"
    d.mkdir(parents=True)
    (d / "build-log.md").write_text(
        "# Build log\n## Evidence\n"
        "- CLAIM: ruff exists | URL: https://docs.astral.sh/ruff/ | HTTP: 200 | DATE: 2026-10-12\n"
    )
    assert run(tmp_path).returncode == 0


def test_malformed_claim_fails(tmp_path):
    d = tmp_path / "projects" / "demo"
    d.mkdir(parents=True)
    (d / "build-log.md").write_text(
        "# Build log\n## Evidence\n- CLAIM: ruff is great (no evidence row)\n"
    )
    assert run(tmp_path).returncode == 1
