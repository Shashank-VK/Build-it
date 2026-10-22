# CLAUDE.md — Superior OS runtime bridge

Mandatory behavioral protocol (applies to any coding agent: OpenCode, Claude Code, Cursor, Codex, Gemini CLI).

1. Obey `AGENTS.md`: loop rails (max_steps=15, IAL debounce, ECT, FCAR), tier the work first.
2. Skills load by trigger from `.harness/skills/index.json`; read the full SKILL.md on trigger.
3. Subagents (coder/explorer/planner/reviewer) run sandboxed with step budgets; reviewer always fresh-context.
4. Evidence is mandatory: coverage receipts + claim rows in build-log; quarantine unknowns.
5. `task verify` (or `bash scripts/verify.sh`) exit 0 before declaring done. No self-certification.
6. Universal notes: no absolute local paths in shared artifacts; OpenCode-only behaviors flagged.
