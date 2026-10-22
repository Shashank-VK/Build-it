"""Eval 1 — OS integrity: registry matches reality, configs parse."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_skills_index_matches_dirs():
    idx = json.loads((ROOT / ".harness/skills/index.json").read_text())["skills"]
    dirs = sorted(p.name for p in (ROOT / ".harness/skills").iterdir() if p.is_dir())
    assert sorted(s["name"] for s in idx) == dirs, "index.json out of sync with skill dirs"
    for s in idx:
        text = (ROOT / ".harness/skills" / s["name"] / "SKILL.md").read_text()
        v2_style = "## DoD" in text and "## Must NOT" in text
        # deve v1.0 frontmatter contract counts: named binding to a
        # workflow/gate + evidence language
        v1_style = (
            text.startswith("---")
            and "description:" in text
            and any(k in text for k in ("Workflow", "Gate", "evidence", "rubric", "checklist"))
        )
        runbook_style = text.startswith("---") and "triggers:" in text
        assert v2_style or v1_style or runbook_style, (
            f"{s['name']} has no recognized skill contract"
        )


def test_configs_parse():
    import yaml

    yaml.safe_load((ROOT / "Taskfile.yml").read_text())
    yaml.safe_load((ROOT / ".harness/config/harness.yaml").read_text())
    yaml.safe_load((ROOT / ".harness/mcp/tools.yaml").read_text())
    for wf in (ROOT / ".harness/workflows").glob("*.yaml"):
        d = yaml.safe_load(wf.read_text())
        assert "states" in d, f"{wf.name} missing states"
    for f in [
        ROOT / ".harness/hooks/hooks.json",
        ROOT / ".harness/permissions/presets.json",
        ROOT / ".harness/skills/index.json",
    ]:
        json.loads(f.read_text())


def test_harness_version():
    import yaml

    cfg = yaml.safe_load((ROOT / ".harness/config/harness.yaml").read_text())
    assert cfg["harness"]["version"] == "2.0.0"
    assert cfg["skills"]["count"] == 25
