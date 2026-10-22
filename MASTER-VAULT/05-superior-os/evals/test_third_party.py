"""Eval 3 — third-party registry: every external entry has a real https source."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_third_party_index_valid():
    idx = json.loads((ROOT / "os" / "third-party-index.json").read_text())["entries"]
    assert len(idx) >= 35, f"expected >=35 URL-backed entries, got {len(idx)}"
    for e in idx:
        assert e.get("name") and e.get("trigger"), f"entry missing name/trigger: {e}"
        src = e.get("source", "")
        assert src.startswith("https://"), f"{e.get('name')} has non-https/missing source"
        assert " " not in src and "(" not in src, f"{e.get('name')} has malformed URL"


def test_registry_docs_exist():
    for f in ["os/THIRD-PARTY-SKILLS.md", "os/THIRD-PARTY-MCP.md", "os/THIRD-PARTY-AGENTS.md"]:
        text = (ROOT / f).read_text()
        assert "github.com/" in text, f"{f} cites no sources"
