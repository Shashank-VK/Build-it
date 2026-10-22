"""Tests for scripts/scope-check.py (12+ cases).

Covers: overlap true (mobile app), stopword-only overlap passes,
synonym false-negative documented, missing section behavior,
numbered bullets, Non-Goals heading variant, case-insensitivity,
punctuation stripping.
"""
import importlib.util
import sys
from pathlib import Path

_SCOPE_PATH = Path(__file__).parent / "scope-check.py"


def _load():
    spec = importlib.util.spec_from_file_location("scope_check", _SCOPE_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mod = _load()
extract_no_gos = mod.extract_no_gos
check_conflict = mod.check_conflict


# 1. overlap true (mobile app)
def test_overlap_true_mobile_app():
    no_gos = ["No mobile app development"]
    has_conflict, conflicts = check_conflict("Add mobile app", no_gos)
    assert has_conflict is True
    assert conflicts == ["No mobile app development"]


# 2. stopword-only overlap passes (shared stopwords are stripped)
def test_stopword_only_overlap_passes():
    # 'the' is a stopword so zero content-word overlap -> no conflict
    has_conflict, conflicts = check_conflict("Add the thing", ["Build the system"])
    assert has_conflict is False
    assert conflicts == []


def test_stopword_no_overlap_passes():
    has_conflict, _ = check_conflict("Do the thing", ["Build the system"])
    assert has_conflict is False


# 3. synonym false-negative documented (no semantic matching, only tokens)
def test_synonym_false_negative_documented():
    # 'handset'/'smartphone' vs 'mobile app' share <2 tokens -> missed conflict.
    # Documents known limitation: token overlap only, no synonym expansion.
    has_conflict, _ = check_conflict(
        "Build smartphone handset client", ["No mobile app development"]
    )
    assert has_conflict is False  # false-negative by design


# 4. missing section behavior
def test_missing_section_returns_empty():
    content = "# Pitch\n\n## Goals\n- Ship fast\n"
    assert extract_no_gos(content) == []


def test_missing_section_empty_pitch():
    assert extract_no_gos("") == []


def test_missing_section_main_fails_default_tier(tmp_path, monkeypatch, capsys):
    pitch = tmp_path / "pitch.md"
    pitch.write_text("# Pitch\n\n## Goals\n- x\n", encoding="utf-8")
    monkeypatch.setattr(
        sys, "argv", ["scope-check.py", "--task", "Do work", "--pitch", str(pitch)]
    )
    rc = mod.main()
    assert rc == 1
    out = capsys.readouterr().out
    assert "WARNING" in out


def test_missing_section_tiny_tier_passes(tmp_path, monkeypatch):
    pitch = tmp_path / "pitch.md"
    pitch.write_text("# Pitch\n\n## Goals\n- x\n", encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        ["scope-check.py", "--task", "Do work", "--pitch", str(pitch), "--tier", "tiny"],
    )
    assert mod.main() == 0


# 5. numbered bullets
def test_numbered_bullets_extracted():
    content = "## No-gos\n1. No mobile app development\n2. No blockchain ledger\n"
    no_gos = extract_no_gos(content)
    assert "No mobile app development" in no_gos
    assert "No blockchain ledger" in no_gos


def test_numbered_bullets_conflict():
    content = "## No-gos\n1. No mobile app development\n"
    no_gos = extract_no_gos(content)
    has_conflict, _ = check_conflict("Add mobile app", no_gos)
    assert has_conflict is True


# 6. Non-Goals heading variant
def test_non_goals_heading_variant():
    content = "## Non-Goals\n- No mobile app development\n"
    no_gos = extract_no_gos(content)
    assert no_gos == ["No mobile app development"]


def test_non_goals_hyphen_variant_conflict():
    no_gos = extract_no_gos("## Non-Goals\n- No mobile app development\n")
    has_conflict, _ = check_conflict("Add mobile app", no_gos)
    assert has_conflict is True


# 7. case-insensitivity
def test_case_insensitive_heading():
    content = "## NO-GOS\n- No mobile app development\n"
    assert extract_no_gos(content) == ["No mobile app development"]


def test_case_insensitive_conflict():
    has_conflict, _ = check_conflict("ADD MOBILE APP", ["no mobile app development"])
    assert has_conflict is True


# 8. punctuation stripping
def test_punctuation_stripping():
    # 'app!' and 'app,' normalize to 'app' via [a-z0-9]+ tokenization
    has_conflict, _ = check_conflict("Add mobile app!", ["No mobile app development"])
    assert has_conflict is True


def test_punctuation_stripping_commas():
    has_conflict, _ = check_conflict("Add, mobile. app?", ["No mobile (app) development!"])
    assert has_conflict is True


# extra: clean task passes, multi-item extraction, heading boundary, main() integration
def test_clean_task_no_conflict():
    has_conflict, _ = check_conflict("Fix login bug", ["No mobile app development"])
    assert has_conflict is False


def test_multiple_no_gos_extraction():
    content = "## No-gos\n- No mobile app\n- No blockchain\n- No hardware device\n"
    assert extract_no_gos(content) == [
        "No mobile app",
        "No blockchain",
        "No hardware device",
    ]


def test_extract_stops_at_next_heading():
    content = "## No-gos\n- No mobile app\n# Next Section\n- Should not include\n"
    assert extract_no_gos(content) == ["No mobile app"]


def test_star_bullet_extracted():
    content = "## No-gos\n* No mobile app development\n"
    assert extract_no_gos(content) == ["No mobile app development"]


def test_main_conflict_returns_one(tmp_path, monkeypatch):
    pitch = tmp_path / "pitch.md"
    pitch.write_text("## No-gos\n- No mobile app development\n", encoding="utf-8")
    monkeypatch.setattr(
        sys, "argv", ["scope-check.py", "--task", "Add mobile app", "--pitch", str(pitch)]
    )
    assert mod.main() == 1


def test_main_pass_returns_zero(tmp_path, monkeypatch):
    pitch = tmp_path / "pitch.md"
    pitch.write_text("## No-gos\n- No mobile app development\n", encoding="utf-8")
    monkeypatch.setattr(
        sys, "argv", ["scope-check.py", "--task", "Fix login bug", "--pitch", str(pitch)]
    )
    assert mod.main() == 0


def test_missing_pitch_file_returns_one(tmp_path, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["scope-check.py", "--task", "x", "--pitch", str(tmp_path / "nope.md")],
    )
    assert mod.main() == 1
