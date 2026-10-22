"""Eval 2 — contract traceability: every skill/workflow points at its card source."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _md_files(*dirs):
    out = []
    for d in dirs:
        base = ROOT / d
        if d.endswith("skills"):
            out += [p / "SKILL.md" for p in base.iterdir() if p.is_dir()]
        else:
            out += list(base.glob("*.yaml"))
    return out


def test_every_capability_cites_contract():
    missing = []
    for f in _md_files(".harness/skills", ".harness/workflows"):
        text = f.read_text(encoding="utf-8", errors="replace")
        if "how-to-use/" not in text and "files/" not in text:
            missing.append(str(f.relative_to(ROOT)))
    assert not missing, f"capabilities without contract refs: {missing}"
