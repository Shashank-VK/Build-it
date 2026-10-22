# OpenCode Ecosystem Research

**Environment:** Antigravity + OpenCode (Sonnet, Plan mode)
**Status:** All research phases complete. Architecture finalized. Ready for build phase.

---

## Phase Status

| Phase | Title | Status | File |
|---|---|---|---|
| Phase 0 | Setup & Verify (anti-hallucination pass) | Complete | research/00-verification.md |
| Phase 0 (gaps) | What couldn''t be found | Complete | research/00-gaps-and-unknowns.md |
| Phase 1 | Load Existing Research (all 26 elements) | Complete | research/01-existing-summary.md |
| Phase 2 | UI/UX, Design Systems, Frontend & Backend | Complete | research/02-ui-ux.md |
| Phase 3 | Multi-Agent Verification / Council | Complete | research/03-multi-agent-council.md |
| Phase 4 | Harness, Environment & Definition of Done | Complete | research/04-harness-environment.md |
| Phase 5 | Remaining Named Resources | Complete | research/05-remaining-resources.md |
| Phase 6 | Unfound Items & Ecosystem Gaps | Complete | research/06-unfound-and-gaps.md |
| Phase 7 | Autonomous Agent Architecture | FINAL - all 5 questions closed | research/07-autonomous-agent-architecture.md |

---

## Directory Structure

```
opencode-research/
|
+-- README.md                          This file. Phase tracker + directory map.
|
+-- catalog.md                         Full raw ecosystem catalog (163 usable tools,
|                                      26 elements, ~295 KB). Source data for all phases.
|                                      Not meant for day-to-day reading.
|
+-- research/
|   |
|   +-- 00-verification.md             Anti-hallucination pass. Every named repo fetched
|   |                                  directly and confirmed live/archived/corrected.
|   |                                  Source of truth for what is real vs. invented.
|   |
|   +-- 00-gaps-and-unknowns.md        Items that could not be verified. Repos that failed
|   |                                  to resolve. Known broken or ambiguous names.
|   |
|   +-- 01-existing-summary.md         All 26 ecosystem elements summarized (163 usable
|   |                                  tools, 43 excluded as Claude-Code-only). One
|   |                                  paragraph per element. The main reference index.
|   |
|   +-- 02-ui-ux.md                    UI/UX design systems: Meta Astryx MCP server,
|   |                                  laws-of-ux-skills, emilkowalski/skills, shadcn MCP,
|   |                                  Anthropic DESIGN.md, 3D template options. Finding:
|   |                                  no turnkey backend equivalent of Astryx exists yet.
|   |
|   +-- 03-multi-agent-council.md      Multi-agent verification layer. ngmeyer council-review
|   |                                  vs. skills (both confirmed live, parallel repos).
|   |                                  deliberation plugin config. Two-Judge council setup.
|   |                                  n8n integration evaluation (rejected). Ensemble research.
|   |
|   +-- 04-harness-environment.md      Harness & environment. Antigravity+OpenCode DOM verdict
|   |                                  (no native link, needs Puppeteer MCP bridge). Slash
|   |                                  commands confirmed working in Antigravity terminal.
|   |                                  Claude Code proxy verdict (not worth it). Verified DoD
|   |                                  template (walkinglabs source, 5 subsystems). Harness
|   |                                  evolution loop. Context anxiety mitigations (6 techniques).
|   |
|   +-- 05-remaining-resources.md      5-point breakdown of all 20 verified named resources:
|   |                                  graphify, ruflo, emilkowalski/skills, notebooklm-py,
|   |                                  vercel/eve, vercel/deepsec, claude-mem, last30days-skill,
|   |                                  loop-engineering, LoopBench, loopy, loopx, LoongFlow,
|   |                                  GSD/open-gsd, mattpocock/skills, obra/superpowers,
|   |                                  garrytan/gstack, public-apis, system_prompts_leaks,
|   |                                  claude-cookbooks. What each does, when to use it,
|   |                                  when not to, and final verdict.
|   |
|   +-- 06-unfound-and-gaps.md         Final corrections log and 7 ecosystem gaps. Confirms:
|   |                                  both KanakMalpani repos live and separate; both ngmeyer
|   |                                  repos live and parallel; gsd-build archived (use open-gsd).
|   |                                  Gaps: no backend Astryx, no n8n bridge, no official
|   |                                  marketplace, no Python SDK, no config linter, etc.
|   |
|   +-- 07-autonomous-agent-architecture.md
|                                      FINAL ARCHITECTURE. All 5 design questions closed.
|                                      Defines the autonomous task-execution layer:
|                                        loop-engineering (scaffold / audit / gate)
|                                        -> loopy (bounded loop execution skill)
|                                        -> walkinglabs (sole session state source of truth)
|                                      Includes: Layer 1 / Layer 2 boundary rules (AGENTS.md
|                                      text ready to use), slash command suite (/idea,
|                                      /loop-status, /loop-doctor, /pause, /council),
|                                      finalized Two-Judge council SKILL.md description,
|                                      pre-commit hook spec (feature_list.json only, on
|                                      status -> "passing" transitions), full architecture
|                                      diagram, and decisions log for all 5 questions.
|
+-- harness-templates/                 Verbatim files pulled from walkinglabs/
    |                                  learn-harness-engineering. Real working templates,
    |                                  not notes. Pending copy into RULES\ (awaiting approval).
    |
    +-- AGENTS.md                      Session startup workflow (6 steps) + working rules
    |                                  + Definition of Done + end-of-session checklist.
    |                                  Agent reads this first on every session start.
    |                                  Will have Layer 1/Layer 2 boundary section appended
    |                                  before being copied to RULES\.
    |
    +-- feature_list.json              Scope lock schema. Enforces: single_active_feature,
    |                                  passing_requires_evidence, do_not_skip_verification.
    |                                  Feature entries: id, priority, status, verification[],
    |                                  evidence[]. Statuses: not_started / in_progress /
    |                                  blocked / passing. Replace placeholder features before use.
    |
    +-- claude-progress.md             Per-session progress log. Agent-agnostic (works with
    |                                  OpenCode, Codex, Claude Code, OpenHands, etc.).
    |                                  Fields: Current Verified State + per-session entries
    |                                  (Goal, Completed, Verification run, Evidence captured,
    |                                  Commits, Files updated, Known risk, Next best step).
    |
    +-- init.sh                        Baseline startup script. Runs: install -> verify ->
    |                                  print start command. Three configurable arrays:
    |                                  INSTALL_CMD, VERIFY_CMD, START_CMD (all must be
    |                                  customized per project before first use).
    |
    +-- README.md                      walkinglabs'' own description of the harness.
                                       Descriptive only -- not a working file.
```

---

## Key Corrections (confirmed by direct live fetches)

| Original (distorted or wrong) | Corrected & Verified |
|---|---|
| "ruflo" | ruvnet/ruflo (formerly Claude Flow) -- LIVE |
| "enilkowaski apple designs skill" | emilkowalski/skills by Emil Kowalski -- LIVE |
| "notebooklm py" | teng-lin/notebooklm-py -- LIVE (unofficial, high breakage risk) |
| ngmeyer/council-review said to be archived | WRONG -- LIVE. Standalone council skill. |
| ngmeyer/skills said to replace council-review | WRONG -- both live in parallel. skills is the personal monorepo. |
| KanakMalpani/Loop-Engineering said to not exist | WRONG -- LIVE. Framework repo (separate from LoopBench). |
| KanakMalpani/LoopBench confused with above | LIVE and separate. Benchmark suite only. |
| okjpg/llm-council | Not found -- no public repo under this handle. Skip. |
| gsd-build/get-shit-done | Archived June 2026 (security issue). Use open-gsd/gsd-core only. |

---

## Architecture Decisions Locked In

| Decision | Outcome |
|---|---|
| Session state source of truth | walkinglabs only (loopx dropped -- same dual-source problem) |
| Council trigger mechanism | Two-Judge via deliberation plugin, auto-fires on SKILL.md description match |
| Pre-commit hook scope | feature_list.json only, on status -> "passing" transitions |
| Entry slash command | /idea (goal-engineering not adopted -- GOAL.md = same dual-source problem) |
| Mega-harness adoption | None -- compose from small focused plugins instead |

---

## Where Things Live

| What | Location |
|---|---|
| Research notes & reference | C:\Users\Shashank Karamudi\Desktop\opencode-research\ (this folder) |
| Working toolkit (single source of truth) | C:\Users\Shashank Karamudi\Desktop\RULES\ |
| Harness templates (pending copy to RULES) | opencode-research\harness-templates\ |
| RULES audit log | C:\Users\Shashank Karamudi\Desktop\RULES\audits\ |
