# ISSUES & DECISIONS LOG

> Open blockers, resolved issues, and key decisions. Updated live.
> Last updated: 2026-09-01 22:58 IST

## Open Issues

| # | Issue | Severity | Impact | Owner | Next Step |
|---|-------|----------|--------|-------|-----------|
| — | *No open issues* | — | — | — | All operational issues and architectural decisions resolved. |

## Resolved Issues

| # | Issue | Severity | Resolution | Resolved |
|---|-------|----------|------------|----------|
| 1 | **Sequential vs parallel bug** — `wf_19071a3d-703` ran R-A→R-B sequentially despite plan. | Medium | Killed `w8qvg25ko` via `TaskStop`; redeployed `wf_c917d118-556` with `pipeline([R-A,R-B], agent)` — verified 2 `started` simultaneously. | 2026-08-31 20:14 |
| 1 (Gate) | **Content Pipeline `gate.sh` decision** — should Firecrawl+browser-use+n8n publishing loop get own gate or reuse C4 research gate? | Low | `gate.sh` IS the canonical sandbox gate for all archetypes. C4 AgenticResearch uses it with `--network allow-egress` enabled. No separate Firecrawl/browser-use gate is needed. | 2026-09-01 |
| 2 | **WSL stdout garble** — `wsl --status` UTF-16LE garble looked like WSL1 error. | Low | Verified WSL2 Ubuntu 26.04, `opencode 1.18.18`, `agy 1.1.21` via `wsl bash -lc`. `agy --print="prompt"` confirmed. | 2026-08-31 20:20 |
| 3 | **No .md tracking files** — user flagged lack of file-based auditability. | Medium | Created `update.md`, `phase-0/STATUS.md`, `R-A/B_*.md`, `AGENTS.md`, `ISSUES.md`. Rule: every deliverable mirrored to `.md` same turn. | 2026-08-31 20:31 |
| 4 | **Python `charmap` crash** on `→` in journal polling scripts (Windows cp1252). | Low | Patched to `encoding='utf-8'` + `errors='replace'`; extraction via file write not `print()`. | 2026-08-31 20:38 |
| 5 | **Verifier payload truncation** — V-C/V-D received truncated R-A + missing R-B bundle (orchestrator sliced at ~8K). | Medium | Repaired by re-reading full `R-A/B_*.md` from disk during synthesis in [`ARCHETYPES_AND_CRITERIA.md`](phase-0/ARCHETYPES_AND_CRITERIA.md). Logged as known gap; future workflows will use file refs or higher slice budget. | 2026-08-31 20:42 |
| 6 | **Batch 3 R-A terminal error (2026-08-31 ~22:15)** — R-A Broad Mapper `a227f20e7480f01ac` failed after 3 searches on `wf_0122c038-89e` (resumed). Journal logged `failed`; only ~11K partial draft recovered. | Medium | agy re-dispatch with `--dangerously-skip-permissions` succeeded; Batch 3 completed via agy fleet. | 2026-09-01 |
| 7 | **WSL `agy` connection reset (2026-08-31 18:32-18:33)** — Both R-A and R-B agy research dispatches to `daily-cloudcode-pa.googleapis.com/v1internal:loadCodeAssist` hit `read: connection reset by peer`. Output files 0 bytes. Smoke test earlier worked (cached). Root cause: transient network/auth. | High | Transient network error; all subsequent agy dispatches succeeded with `--dangerously-skip-permissions`. | 2026-09-01 |
| 8 | **WSL var scoping vs `tee`** — `$DEST` inside `wsl bash -lc` background subshell doesn't propagate to `tee` pipeline; writes to `/`. Fixed with literal absolute paths. | Medium | Use literal paths; fixed with literal absolute paths in background subshell pipelines. | 2026-08-31 |
| 9 | **agy headless permission auto-deny (2026-09-01)** — `agy --print` headless mode auto-denied a `command`-type tool (likely web search) it couldn't prompt for → 0-byte outputs. Fix per agy error: run with `--dangerously-skip-permissions` (correct for headless research; no interactive prompt available). | Medium | Redispatch with `--dangerously-skip-permissions`. Logged integration finding: headless agy requires either allow-rules in `settings.json` or the skip flag. | 2026-09-01 |
| 10 | **batch-4/ dir missing on first dispatch** — `tee` to non-existent dir silently fails → no file. | Low | `mkdir -p` before dispatch; ensure target directories exist prior to pipeline execution. | 2026-09-01 |
| 11 | **opencode long-prompt truncation (Phases 2-3)** — `opencode run` with long multi-part research prompts produced 0-byte output repeatedly (T-A/T-C/T-E/T-G, arbiter). Short prompts work; deep research does not emit on this socket. Fix: route substantive research via `agy --skip-permissions \| tee`; opencode usable only for short targeted queries. | Medium | agy is the fleet workhorse; routed substantive research via `agy --dangerously-skip-permissions \| tee`, opencode restricted to short queries only. | 2026-09-01 |

## Key Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-08-31 | **137 micro-tasks** (not ~30 coarse tasks) — per user: "break down research into 100s of small tasks" | Eliminate lazy surfaces; depth via granularity. |
| 2026-08-31 | **Folder `the harness` is the repo root** — all artifacts versioned here, harness-as-code from day one | Per user: "same folder the harness", `git init` at root. |
| 2026-08-31 | **Workflow `pipeline()` for true parallel** — not sequential `await agent()` | Operating Contract requires R-A+R-B divergent lenses running simultaneously. |
| 2026-08-31 | **Every output mirrored to `.md` + `update.md` live log** | User: "make files for everything in .md" + "update.md where you write what has happened also related to agents deployed separately too" |
| 2026-09-01 | **S-tier archetype priority queue:** C1 ProductEngineering → C2 DataMLOps → C4 AgenticResearch → C5 PlatformInfra → C6 Modernization | Closes Pending Decision 1; per GAP-GOV-01 remediation. |
| 2026-09-01 | **Empirical validation tasks (Phase 3.5):** Defer to GAP-VAL-01 sprint; real repos to be nominated (TypeScript full-stack, Python data pipeline, Java legacy migration) | Closes Pending Decision 2. |
| 2026-09-01 | **Versioning scheme adopted:** SemVer 2.0.0 for HaC manifests (`.harness/`); CalVer `YYYY.MM.MINOR` for research phase artifacts (`phase-*/`) | Closes Pending Decision 3. |

## How to Use This File

- **If you hit an issue:** describe it in chat — I log it here immediately with severity + next step.
- **If you make a decision:** tell me — I record it in Key Decisions so future agents don't re-litigate.
- **If an issue is resolved:** I move it to Resolved with timestamp.
