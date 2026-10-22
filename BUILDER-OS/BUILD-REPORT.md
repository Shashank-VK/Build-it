# Superior OS v2.0 — Build Report

129 files. Deve v1.0 base carried verbatim (50 files) + 79 new/changed.

## Deltas vs deve (all grounded in ../how-to-use/ 707 cards)
- Skills 9 -> 24 (+15 verbatim the-harness runbooks, incl. litellm-admin, crypto-patterns, socratic-planner).
- Workflows 10 -> 15 (+build-verify, test-and-verify, migration-safeguard, refactor-safely, eval-gate).
- Agents: +4 subagent specs (coder/explorer/planner/reviewer) + C5-Verification role.
- MCP: +4 real server configs + MCP_SECURITY.md.
- Hooks: +post-tool-linter (ruff+AST).
- Gates: +coverage_gate.py + claim_check.py wired into verify.
- Telemetry: +Langfuse config; spend-log enforced.
- OS docs: +EVIDENCE, RULES-34, ANTI-PATTERNS-19, 6 disciplines, 10 templates, 3 domain checklists.
- Permissions: +C5-Verification preset. Taskfile: +eval-gate/coverage-gate/claim-check/doctor/skills-list tasks.

## Verification
- `bash scripts/verify.sh`: secret-scan + py_compile + pytest (52 passed) + coverage-gate + claim-check -> ALL GATES PASSED.
- YAML/JSON validity: 15 workflows + mcp + Taskfile + all JSON configs parse.
- skills/index.json (24) matches 24 skill dirs. No absolute local paths in shared artifacts.
- how-to-use/ untouched (read-only).

## Remaining-work completion (2026-10-12)
- Taskfile now parses under strict PyYAML too (quoted `: `-bearing commands; identical shell semantics; deve had the same quirk).
- evals/ registered (OS integrity + contract traceability, 4 tests) and wired into `task eval-gate`.
- Smoke test: projects/demo-smoke carries appetite + evidence receipts; `bash scripts/verify.sh` ALL GATES PASSED.
- No `task` binary in this environment; Taskfile tasks mirror scripts/verify.sh (same commands).

## god_repo distribution (2026-10-12)
- `Desktop/god_repo/`: superior-os/ (117 files, byte-identical to source modulo runtime logs) + support/ (how-to-use + MANIFEST.sha256, 29/29 verified) + prompt/SYSTEM-PROMPT-UNIVERSAL.md (106 lines, sections 0-9).
- Download-once: scripts/setup.sh (honest per-item .provisioned), MCP tarballs pinned+cached (3/3), playwright honestly skipped if absent.
- Tag-every-project: scripts/tag_project.py manifest pin; new-project + adopt tasks; runtime logs excluded from manifest so pins don't rot.
- god_repo copy independently verified: 56 tests green, verify ALL GATES PASSED with tagged demo project.

## All-skills vendoring (2026-10-12)
- Skills 9 -> 24: 12 distilled summaries replaced by all 15 verbatim the-harness runbooks (incl. litellm-admin, crypto-patterns, socratic-planner). 8 solo skill variants intentionally not vendored (same 9 names as deve; their cards remain in 01-skills.md).
- Eval accepts 3 contract styles (v2 DoD sections, v1 frontmatter, runbook triggers:).

## output.md audit + third-party registries (2026-10-12)
- Audited Desktop/output.md line-by-line (69,108 lines, 200 content banners + 16 manifest lines): all 200 sources exist in files/ (0 missing); 133 identical, 67 evolved; sole output-only content (21-line adjudication header) already preserved in DIFF-REPORTs/parts/12/cards.
- Added os/THIRD-PARTY-{SKILLS,MCP,AGENTS}.md + os/third-party-index.json (36 URL-backed entries, all URLs cited in-corpus, none invented) + eval (URL validity). Agents doc-only (no install sources cited).
