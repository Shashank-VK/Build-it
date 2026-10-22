# AI DEVELOPMENT HARNESS — MASTER PLAN
## Spiral Research & Build: 0 → 4 + Empirical Validation

> **Folder:** `the harness` (this directory) — all artifacts versioned here.
> **Mode:** Senior-managed, 4-agent spiral. 2 Researchers (parallel, different lenses) + 2 Verifiers (adversarial + architectural). Repeat per phase. Gates between phases.
> **Orchestration:** WSL via `opencode` + `antigravity (agy)` — terminal-driven. User grants all perms.
> **Principle:** 100s of micro-tasks so no lazy surfaces. Depth over breadth theatre.

---

## 0) OPERATING CONTRACT

### 0.1 Team
| Agent | Codename | Lens | Non-negotiable |
|-------|----------|------|----------------|
| R-A | Broad Mapper | Multi-ecosystem, vendor-agnostic sweep | Must touch ≥10 ecosystems per batch |
| R-B | Challenger | Deliberately hunt what R-A would miss, split/merge test | Must propose ≥3 splits/merges per batch |
| V-C | Adversarial Verifier | Refute every claim, translation-check, dedupe | Must try to kill each finding with ≥2 counter-sources |
| V-D | Architectural Verifier | Abstraction levels, lifecycle roles, foundational vs situational | Must re-tag every element to Capability/Mechanism/Protocol/Framework/Tool |

- R-A and R-B run **in parallel** with **different prompts** on the **same brief** — divergence is intentional.
- V-C and V-D only start after R-A + R-B deliver — they work in parallel on the combined findings.
- No phase advances without **gate sign-off**: V-C + V-D + senior (you/me) agree.

### 0.2 Quality Bar
- Every claim needs **≥2 independent sources** outside vendor marketing.
- Every element needs a **translation check** — what is it called in ≥2 other ecosystems?
- Every batch respects the **stop rule**: 3 consecutive distinct searches yielding only known synonyms/implementation trivia/niche noise → stop that sub-area.
- Every tool that reaches Essential must pass the **verification gate** (link valid, maintained, corroborated, adopted, relevant, compatible, licensed clean).

### 0.3 Anti-Lazy Rules (enforced on researchers)
- No single-search conclusions. Min 5 distinct search angles per sub-area.
- No reasoning from memory. Cite sources with URLs.
- No averaging away archetype differences.
- No unbounded scope creep — complexity budgets tracked explicitly.
- Log dead ends and negative results — they prevent re-work.

### 0.4 Harness-as-Code From Day One
- All plan/taxonomy/rankings/tool selections are files in this repo, versioned in git.
- Every run/config is diffable. Prompts, models, tool versions captured.
- `plan.md` (this file) is the execution backbone — tasks checked off atomically.

---

## 1) PHASE 0 — ANCHOR THE PROJECT

**Goal:** Define what the harness is actually for, in measurable terms, before any discovery.
**Deliverable:** `phase-0/ARCHETYPES_AND_CRITERIA.md`

### P0 Tasks

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P0-01 | Draft candidate archetype longlist (10–12 types: greenfield web, prod backend, ETL/pipeline, internal automation, AI/ML exp, research/writing, browser-heavy, dev tooling, data science, infra/DevOps, migration/modernization, agent system) | R-A | — | ☐ |
| P0-02 | Independently draft archetype longlist from first-principles (user jobs, not tool categories) | R-B | — | ☐ |
| P0-03 | Merge longlists, cluster overlaps, propose 5–7 canonical archetypes with justification for each keep/drop | V-C+V-D | P0-01,02 | ☐ |
| P0-04 | For each archetype define constraints: solo vs team, prototype vs production, cost/latency/security/reliability sensitivity, duration, human-supervision level, autonomy tolerance | R-A | P0-03 | ☐ |
| P0-05 | Cross-check P0-04 constraints against real project postmortems / case studies (≥2 per archetype) | R-B | P0-03 | ☐ |
| P0-06 | Verify archetypes cover the user's actual past + intended future work (infer from conversation + ask user to confirm) | V-C | P0-04,05 | ☐ |
| P0-07 | Draft longlist of candidate success metrics (20+): manual interventions, regressions, time-to-working-code, token cost/feature, debug cycles, irreversible mistakes, coverage, task completion, reliability, cognitive load, etc. | R-A | — | ☐ |
| P0-08 | Map each metric to which archetypes it meaningfully discriminates vs which it is noise for | R-B | P0-07 | ☐ |
| P0-09 | Select 8–12 final harness success criteria with **measurement method** each (how to observe, what instrument, what threshold) | V-D | P0-07,08 | ☐ |
| P0-10 | Define how Phase 2 rankings will be traceable to these criteria (scoring rubric wiring) | V-D | P0-09 | ☐ |
| P0-11 | V-C adversarial pass: try to prove an important archetype or metric is missing; log the attempt | V-C | P0-03,09 | ☐ |
| P0-12 | Synthesize `phase-0/ARCHETYPES_AND_CRITERIA.md` with archetypes, constraints matrix, metrics, measurement methods, and open questions | R-A | P0-06,10,11 | ☐ |
| P0-13 | Gate review: senior sign-off on Phase 0 before Phase 1 begins | Senior | P0-12 | ☐ |

---

## 2) PHASE 1 — DISCOVER ALL ELEMENTS / SEEDS

**Goal:** Practical completeness of the capability universe — not tool list, not skill list. Elements only.
**Deliverable:** `phase-1/MASTER_TAXONOMY.md` (living) + `phase-1/EVIDENCE_LOG.md`
**Batches:** 5 batches × ~8 tasks = ~40 micro-tasks. Each batch follows Research → Converge → Verify → Tag.

### Shared Phase 1 Protocol (applies to every batch)
- R-A and R-B each run ≥5 distinct search strategies per batch (different ecosystems, different vocabularies).
- For every candidate element, record: canonical name, definition, problem, why it matters, level (Capability/Mechanism/Protocol/Framework/Tool), lifecycle role, related concepts, cross-ecosystem terms, confidence (high/med/low), and whether it is foundational/important/specialized/situational (preliminary).
- Translation check required before any candidate is accepted.
- Stop rule tracked **per sub-area**, not globally.
- V-C tries to kill/merge each candidate; V-D re-tags abstraction level and lifecycle role.

### Batch 1 — Execution & Agency Layer
*Sub-areas: subagents, delegation, orchestration, workflows, background tasks, git worktrees, agent teams, autonomy calibration, human-in-the-loop*

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P1-01 | Seed sweep: map execution concepts across Claude Code, OpenAI Codex, Cursor, Windsurf, Gemini CLI, Copilot, OpenCode, Cline, Roo, Aider, OpenHands, enterprise platforms | R-A | P0-13 | ☐ |
| P1-02 | Challenger sweep: same scope, different vocabulary — search via "delegation", "handoff", "spawning", "worktree", "parallelism", "autonomy" to surface hidden synonyms | R-B | P0-13 | ☐ |
| P1-03 | Deep dive: subagent vs agent-team vs workflow — are they one capability or three? Evidence for split/merge | R-A | P1-01 | ☐ |
| P1-04 | Deep dive: background tasks vs async jobs vs queued execution — mechanism or capability? | R-B | P1-02 | ☐ |
| P1-05 | Investigate commonly missed: autonomy calibration, human-in-the-loop controls, human trust/review UX, side-effect safety, idempotency, undo/reversibility | R-A+R-B | P1-01,02 | ☐ |
| P1-06 | Translation check pass for Batch 1 candidates (≥2 ecosystems each) | V-C | P1-03,04,05 | ☐ |
| P1-07 | Abstraction re-tag pass for Batch 1 (Capability vs Mechanism vs Protocol vs Framework vs Tool) | V-D | P1-03,04,05 | ☐ |
| P1-08 | Converge Batch 1: write taxonomy slice + evidence rows + open questions | R-A | P1-06,07 | ☐ |

### Batch 2 — Context, Memory & Knowledge
*Sub-areas: context management, prompt/context engineering, prompt architecture, memory, retrieval, knowledge management, context budget/competition, prompt injection defense*

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P1-09 | Sweep context/memory/retrieval across agent SDKs, runtimes, RAG systems, IDE agents, security literature | R-A | P1-08 | ☐ |
| P1-10 | Challenger sweep via "memory", "recall", "episodic", "semantic", "working memory", "context window", "injection" | R-B | P1-08 | ☐ |
| P1-11 | Distinguish: context management vs memory vs retrieval vs knowledge management — four capabilities or one with mechanisms? | R-A | P1-09 | ☐ |
| P1-12 | Investigate: prompt injection / untrusted-content defense as cross-cutting concern vs standalone capability | R-B | P1-10 | ☐ |
| P1-13 | Investigate: prompt architecture & complexity budgets — where do they live in taxonomy? | R-A | P1-11 | ☐ |
| P1-14 | Translation check pass for Batch 2 | V-C | P1-11,12,13 | ☐ |
| P1-15 | Abstraction re-tag + lifecycle role pass for Batch 2 | V-D | P1-11,12,13 | ☐ |
| P1-16 | Converge Batch 2: update MASTER_TAXONOMY + EVIDENCE_LOG | R-A | P1-14,15 | ☐ |

### Batch 3 — Integration & Extensibility
*Sub-areas: MCP, plugins/marketplaces, Skills, discipline/skill packs, documentation-context MCP, hook-management CLIs, awesome-lists/cross-tool directories, model/provider abstraction, portability, routing*

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P1-17 | Sweep MCP, plugin systems, Skills, marketplaces, registries across all target ecosystems | R-A | P1-16 | ☐ |
| P1-18 | Challenger sweep via "extension", "tool use", "function calling", "registry", "marketplace", "capability pack" | R-B | P1-16 | ☐ |
| P1-19 | Distinguish: Skills vs Plugins vs MCP servers vs Hooks — capabilities or mechanisms? Vendor-specific vs portable? | R-A | P1-17 | ☐ |
| P1-20 | Investigate commonly missed: model/provider abstraction, portability, routing — distinct capability or infrastructure concern? | R-B | P1-18 | ☐ |
| P1-21 | Audit awesome-lists / cross-tool directories for hidden categories not in vendor docs | R-A | P1-17 | ☐ |
| P1-22 | Translation check pass for Batch 3 | V-C | P1-19,20,21 | ☐ |
| P1-23 | Abstraction re-tag + redundancy check for Batch 3 (e.g., "Skills" as capability category vs individual skill as resource) | V-D | P1-19,20,21 | ☐ |
| P1-24 | Converge Batch 3 | R-A | P1-22,23 | ☐ |

### Batch 4 — Safety, Governance & Trust
*Sub-areas: permission modes, sandboxing, safety nets/guardrails, security review, security scanners, credential/secret mgmt, data governance, privacy, licensing/IP, audit trail, side-effect safety, reproducibility*

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P1-25 | Sweep permission modes, sandboxing, guardrails across Claude Code, Codex, Cline, enterprise platforms | R-A | P1-24 | ☐ |
| P1-26 | Challenger sweep via "least privilege", "allowlist", "denylist", "policy as code", "guardrail", "sandbox boundary" | R-B | P1-24 | ☐ |
| P1-27 | Distinguish: guardrails vs safety nets vs permission modes — one capability or three mechanisms? | R-A | P1-25 | ☐ |
| P1-28 | Deep dive: credential/secret management, data governance, privacy, licensing/IP — which are distinct capabilities vs cross-cutting? | R-B | P1-26 | ☐ |
| P1-29 | Deep dive: audit trail vs observability vs reproducibility — three capabilities or facets of one? | R-A | P1-27 | ☐ |
| P1-30 | Translation check + security-boundary mapping (hooks ↔ sandbox, content vs instruction trust boundaries) | V-C | P1-27,28,29 | ☐ |
| P1-31 | Abstraction + lifecycle pass for Batch 4 (build-time vs run-time vs review-time) | V-D | P1-27,28,29 | ☐ |
| P1-32 | Converge Batch 4 | R-A | P1-30,31 | ☐ |

### Batch 5 — DX, Observability & Meta
*Sub-areas: checkpoints/rewind, hooks, statusline/agent status, output styles, usage/cost tracking, headless/CI, self-improving/instinct-mining, harness-as-code, harness versioning/migration, reliability/recovery, observability, evaluation, meta-evaluation, complexity budgets, anti-bloat, governance, lifecycle/maintenance, deprecation*

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P1-33 | Sweep DX/observability concepts across all ecosystems + DevOps/infra/eval literature | R-A | P1-32 | ☐ |
| P1-34 | Challenger sweep via "checkpoint", "rewind", "cost", "budget", "governance", "deprecation" in non-agent contexts (DevOps, DB, infra) | R-B | P1-32 | ☐ |
| P1-35 | Distinguish: checkpoints vs git worktrees vs undo vs harness versioning — overlapping mechanisms? | R-A | P1-33 | ☐ |
| P1-36 | Investigate commonly missed: evaluation, meta-evaluation of the harness, complexity budgets, anti-bloat mechanisms, deprecation management | R-B | P1-34 | ☐ |
| P1-37 | Investigate: headless/CI as deployment mode vs distinct capability; self-improving/instinct-mining — capability or emergent property? | R-A | P1-35 | ☐ |
| P1-38 | Translation check pass for Batch 5 | V-C | P1-35,36,37 | ☐ |
| P1-39 | Abstraction + harm-if-absent pre-score for Batch 5 | V-D | P1-35,36,37 | ☐ |
| P1-40 | Converge Batch 5 + produce full MASTER_TAXONOMY v1 + EVIDENCE_LOG v1 | R-A | P1-38,39 | ☐ |
| P1-41 | Cross-batch dedupe: V-C scans all 5 batches for duplicates/synonyms/redundant splits | V-C | P1-40 | ☐ |
| P1-42 | Cross-batch level hygiene: V-D re-tags any element where Capability/Mechanism/Protocol/Framework/Tool was conflated | V-D | P1-40 | ☐ |
| P1-43 | Phase 1 Gate: senior review of MASTER_TAXONOMY v1 — approve or send back with revision notes | Senior | P1-41,42 | ☐ |

---

## 3) PHASE 2 — RESEARCH & RANK EACH ELEMENT

**Goal:** For every element in MASTER_TAXONOMY, understand it deeply and rank it with a traceable rubric.
**Deliverable:** `phase-2/RANKINGS.md` + `phase-2/elements/<element>.md` per element + `phase-2/RUBRIC.md`

### Rubric (1–5 each; documented in RUBRIC.md)
1. Frequency of need — across archetypes
2. Harm if absent — capability/reliability/safety/quality loss
3. Benefit — actual outcome improvement
4. Complexity cost — conceptual/config complexity added (inverse scored)
5. Maintenance burden — ongoing cost (inverse scored)
6. Security / risk impact — reduces risk (+) or introduces risk (−)
7. General applicability — breadth across project types

Tier derived from weighted evidence, not fake math precision. Document weighting + archetype-dependent variance.

| Tier | Meaning |
|------|---------|
| S | Fundamental / extremely important |
| A | Highly valuable for most serious workflows |
| B | Useful but not universally necessary |
| C | Specialized / situational |
| D | Niche / redundant / declining / low priority |
| + tags | experimental / emerging / declining / obsolete where relevant |

### Phase 2 Tasks

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P2-01 | Write RUBRIC.md: define 1–5 anchors per dimension, weighting, tier thresholds, archetype variance handling, example scorecard | V-D | P1-43 | ☐ |
| P2-02 | Create element research template: what/how/problem/why/forms/approaches/pros/cons/maturity/limits/failures/alternatives/interactions/when-use/when-not/absent-impact/applicability | R-A | P2-01 | ☐ |
| P2-03 | Batch elements into groups of 4–5 for parallel research (Group A: execution layer, B: context/memory, C: integration, D: safety/governance, E: DX/observability/meta) | Senior | P1-43 | ☐ |
| P2-04 | Group A deep research: R-A takes 2 elements, R-B takes the other 2–3 — parallel, different source pools | R-A,R-B | P2-02,03 | ☐ |
| P2-05 | Group A verification: V-C adversarial cross-check, V-D rubric scoring + archetype matrix | V-C,V-D | P2-04 | ☐ |
| P2-06 | Group B deep research (same pattern) | R-A,R-B | P2-05 | ☐ |
| P2-07 | Group B verification | V-C,V-D | P2-06 | ☐ |
| P2-08 | Group C deep research | R-A,R-B | P2-05 | ☐ |
| P2-09 | Group C verification | V-C,V-D | P2-08 | ☐ |
| P2-10 | Group D deep research | R-A,R-B | P2-07 | ☐ |
| P2-11 | Group D verification | V-C,V-D | P2-10 | ☐ |
| P2-12 | Group E deep research | R-A,R-B | P2-09 | ☐ |
| P2-13 | Group E verification | V-C,V-D | P2-12 | ☐ |
| P2-14 | Archetype-dependent ranking pass: for each element produce S/A/B/C/D per archetype + global tier rationale | V-D | P2-05,07,09,11,13 | ☐ |
| P2-15 | Interaction pre-scan: note element↔element tensions that affect ranking (e.g., subagents ↔ cost, memory ↔ context budget) | V-C+V-D | P2-14 | ☐ |
| P2-16 | Revision gate: if research shows taxonomy is wrong (merge/split/discover/drop), update MASTER_TAXONOMY and log the change | Senior | P2-14,15 | ☐ |
| P2-17 | Synthesize RANKINGS.md: table of elements with scores, tiers, archetype matrix, evidence links, dissent notes | R-A | P2-14,16 | ☐ |
| P2-18 | Phase 2 Gate: senior sign-off on rankings before tool selection | Senior | P2-17 | ☐ |

---

## 4) PHASE 3 — FIND & SELECT ACTUAL TOOLS / RESOURCES

**Goal:** Per element, move from abstract capability to concrete implementations — Essential vs Optional vs Avoid.
**Deliverable:** `phase-3/tools/<element>.md` per element + `phase-3/TOOL_SELECTION_INDEX.md`
**Method:** One element at a time where it makes sense; parallelize independent elements. Build minimal slices as you go — do not wait for all elements.

### Per-Element Protocol (repeat for each element, tracked individually)

For each element E:
1. Discover implementations (official ecosystems + mature OSS + registries + repos)
2. Compare alternatives (capability, reliability, maturity, maintenance, docs, integration, ecosystem, security, usability, flexibility, perf, cost, portability, lock-in, adoption, fit, burden)
3. Filter overlap/redundancy
4. Classify: Essential (load-bearing) / Optional (situational) / Avoid (with reason)
5. Verification gate (link valid, maintained, corroborated, adopted, relevant, compatible, licensed)
6. Write `<element>.md`
7. Immediately integrate into working harness slice if Essential

### Phase 3 Tasks

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P3-01 | Create tool-selection template + verification checklist (link, maintenance window, corroboration, adoption, relevance, compatibility, license) | V-D | P2-18 | ☐ |
| P3-02 | Prioritize elements for tool selection by tier (S → A → B) + archetype coverage — produce ordered queue | Senior | P2-18 | ☐ |
| P3-03 | Element: Skills — discover Skills landscape (Anthropic official + community + GitHub repos); target 30–40 keepers without forcing the number | R-A | P3-01,02 | ☐ |
| P3-04 | Element: Skills — challenger pass: hunt duplication, vendor-specific vs portable, capability vs resource confusion | R-B | P3-03 | ☐ |
| P3-05 | Element: Skills — verify top candidates; produce Essential/Optional/Avoid with install links + last-verified dates | V-C | P3-03,04 | ☐ |
| P3-06 | Element: MCP — discover MCP servers/integrations (official + community registries) | R-A | P3-01 | ☐ |
| P3-07 | Element: MCP — challenger + verification pass | R-B+V-C | P3-06 | ☐ |
| P3-08 | Element: Testing (unit/integration/e2e) — discover strongest frameworks/tools per archetype | R-A | P3-01 | ☐ |
| P3-09 | Element: Testing — challenger + verification | R-B+V-C | P3-08 | ☐ |
| P3-10 | Element: Security (scanners, guardrails, injection defense) — discover + compare | R-A | P3-01 | ☐ |
| P3-11 | Element: Security — challenger + verification | R-B+V-C | P3-10 | ☐ |
| P3-12 | Elements: UI/UX, Frontend, Backend — discover tooling/resources per archetype | R-A+R-B | P3-01 | ☐ |
| P3-13 | Elements: UI/UX, Frontend, Backend — verify + classify | V-C | P3-12 | ☐ |
| P3-14 | Elements: Databases, APIs, Cloud/Infra, DevOps — discover | R-A+R-B | P3-01 | ☐ |
| P3-15 | Elements: Databases, APIs, Cloud/Infra, DevOps — verify + classify | V-C | P3-14 | ☐ |
| P3-16 | Elements: AI/ML, Data Science, Data Pipelines — discover | R-A+R-B | P3-01 | ☐ |
| P3-17 | Elements: AI/ML, Data Science, Data Pipelines — verify + classify | V-C | P3-16 | ☐ |
| P3-18 | Elements: Orchestration, Subagents, Agent SDKs/Runtimes, Workflow — discover | R-A+R-B | P3-01 | ☐ |
| P3-19 | Elements: Orchestration, Subagents, Agent SDKs/Runtimes, Workflow — verify + classify | V-C | P3-18 | ☐ |
| P3-20 | Elements: Context Mgmt, Memory, Retrieval, Prompt Arch — discover | R-A+R-B | P3-01 | ☐ |
| P3-21 | Elements: Context Mgmt, Memory, Retrieval, Prompt Arch — verify + classify | V-C | P3-20 | ☐ |
| P3-22 | Elements: Hooks, Checkpoints, Statusline, Output Styles, Cost Tracking, Headless/CI — discover | R-A+R-B | P3-01 | ☐ |
| P3-23 | Elements: Hooks, Checkpoints, Statusline, Output Styles, Cost Tracking, Headless/CI — verify + classify | V-C | P3-22 | ☐ |
| P3-24 | Elements: Sandboxing, Permission Modes, Credential Mgmt, Audit Trail — discover | R-A+R-B | P3-01 | ☐ |
| P3-25 | Elements: Sandboxing, Permission Modes, Credential Mgmt, Audit Trail — verify + classify | V-C | P3-24 | ☐ |
| P3-26 | Cross-element overlap sweep: identify redundant tools selected under different elements; dedupe | V-C+V-D | P3-05,07,09,11,13,15,17,19,21,23,25 | ☐ |
| P3-27 | Build minimal working harness slice (S-tier essentials first) — wire together, expose integration conflicts, permission/context/cost friction | R-A+V-D | P3-26 | ☐ |
| P3-28 | Slice smoke test: does the slice run end-to-end on a trivial task without manual rescue? Record friction | V-C | P3-27 | ☐ |
| P3-29 | Expand slice to A-tier essentials, re-test integration | R-A+V-D | P3-28 | ☐ |
| P3-30 | Produce TOOL_SELECTION_INDEX.md: master table of elements → Essential/Optional/Avoid with links, last-verified, re-check triggers | R-A | P3-26,29 | ☐ |
| P3-31 | Phase 3 Gate: senior sign-off on tool selections + working slice before empirical validation | Senior | P3-30 | ☐ |

---

## 5) PHASE 3.5 — EMPIRICAL VALIDATION LOOP (MANDATORY)

**Goal:** Prove the harness survives real use. Rankings are hypotheses until validated.
**Deliverable:** `phase-3.5/VALIDATION_REPORT.md` + feedback patches to Phase 1/2/3 artifacts

### Validation Tasks

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P3.5-01 | Select 2–3 real tasks from actual work (not toys) — one per archetype, with clear success criteria | Senior | P3-31 | ☐ |
| P3.5-02 | Run Task 1 against harness slice — instrument: what worked, failed, needed hand-holding, conflicted, lost context, cost spike | R-A | P3.5-01 | ☐ |
| P3.5-03 | Shadow-observe Task 1: independent V-C pass recording friction R-A missed | V-C | P3.5-02 | ☐ |
| P3.5-04 | Run Task 2 against harness slice — same instrumentation | R-B | P3.5-01 | ☐ |
| P3.5-05 | Shadow-observe Task 2: V-D pass (architectural friction: abstraction leaks, level conflation) | V-D | P3.5-04 | ☐ |
| P3.5-06 | Run Task 3 (if selected) — stress archetype not covered by 1 & 2 | R-A | P3.5-01 | ☐ |
| P3.5-07 | Synthesize friction log: categorize by (ranking wrong? tool wrong? taxonomy wrong? integration wrong? permission/autonomy wrong? testing gap? orchestration overhead? maintenance pain?) | V-C+V-D | P3.5-02,03,04,05,06 | ☐ |
| P3.5-08 | Feed back into Phase 2: revise rankings where S-tier did not deliver or low-tier mattered | V-D | P3.5-07 | ☐ |
| P3.5-09 | Feed back into Phase 3: swap/add/drop tools where selection caused friction | V-C | P3.5-07 | ☐ |
| P3.5-10 | Feed back into Phase 1: revise MASTER_TAXONOMY if validation reveals missing/merged/split elements | Senior | P3.5-07 | ☐ |
| P3.5-11 | Re-run affected tasks against revised harness — confirm friction reduced | R-A+R-B | P3.5-08,09,10 | ☐ |
| P3.5-12 | Write VALIDATION_REPORT.md: tasks, what worked/failed, cost/context/permission/autonomy observations, ranking/tool/taxonomy revisions, re-test results | R-A | P3.5-11 | ☐ |
| P3.5-13 | Phase 3.5 Gate: senior sign-off — is the harness empirically credible? If not, loop P3.5-02 → P3.5-12 again | Senior | P3.5-12 | ☐ |

---

## 6) PHASE 4 — DOCUMENT THE FINAL RESEARCH

**Goal:** Per-element .md knowledge base + master interaction/conflict map + versioned harness.
**Deliverable:** `elements/<element>.md` per element (18-section template) + `INTERACTION_MAP.md` + versioned harness config

### Per-Element .md Template (18 sections)
1. Element Overview
2. Why It Matters
3. How It Works
4. When to Use It
5. When NOT to Use It
6. Importance (S/A/B/C/D + rubric scores + reasoning + archetype-dependent matrix)
7. Essential Tools / Resources
8. Optional Tools / Resources
9. Recommended Usage Rules
10. Dependencies
11. Integration
12. Failure Modes
13. Security Considerations
14. Maintenance
15. Sources (primary + key secondary)
16. Download / Repository / Installation Links (official preferred)
17. Last Verified (date)
18. Re-check Trigger (version change, archetype change, ecosystem change, 6-month review, abandonment, security issue, arch change)

### Phase 4 Tasks

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| P4-01 | Create element .md template file + linter (required sections, link checks, last-verified freshness) | V-D | P3.5-13 | ☐ |
| P4-02 | Batch 1 docs: execution layer elements (subagents, orchestration, workflows, git worktrees, autonomy) — R-A drafts, V-C verifies | R-A+V-C | P4-01 | ☐ |
| P4-03 | Batch 2 docs: context/memory/retrieval/prompt-arch/injection-defense | R-B+V-D | P4-01 | ☐ |
| P4-04 | Batch 3 docs: integration layer (MCP, Skills, plugins, model abstraction/portability/routing) | R-A+V-C | P4-01 | ☐ |
| P4-05 | Batch 4 docs: safety/governance (permissions, sandboxing, credentials, audit, licensing, data governance) | R-B+V-D | P4-01 | ☐ |
| P4-06 | Batch 5 docs: DX/observability/meta (hooks, checkpoints, statusline, output styles, cost tracking, headless/CI, evaluation, meta-eval, harness versioning) | R-A+V-C | P4-01 | ☐ |
| P4-07 | Batch 6 docs: domain tooling (testing, security scanners, UI/UX, frontend, backend, DB, APIs, cloud/infra, AI/ML, data) | R-B+V-D | P4-01 | ☐ |
| P4-08 | Cross-doc consistency pass: terminology, tier labels, link freshness, abstraction levels aligned | V-C+V-D | P4-02,03,04,05,06,07 | ☐ |
| P4-09 | Build INTERACTION_MAP.md: dependencies, conflicts, overlaps, resource competition, security-boundary interactions, context competition, lifecycle conflicts, failure propagation — with tensions explicit, not forced into a DAG | V-D | P4-08 | ☐ |
| P4-10 | Harness-as-code assembly: versioned config capturing Skills, hooks, MCP, permissions, models, workflows, agent roles, tool versions, policies — diffable & reversible | R-A+V-D | P4-08 | ☐ |
| P4-11 | Reproducibility/auditability check: can we reconstruct prompts, context, models, tools, decisions per run? | V-C | P4-10 | ☐ |
| P4-12 | Complexity/anti-bloat audit: every addition answers benefit > cost? Used? Redundant? Removable? Failure surface? | V-D | P4-10 | ☐ |
| P4-13 | Side-effect safety classification: tag every harness action as reversible / recoverable / hard-to-reverse / irreversible + guard rules | V-C | P4-10 | ☐ |
| P4-14 | Final harness smoke test: greenfield task end-to-end with the documented harness — no undocumented steps | R-A | P4-10 | ☐ |
| P4-15 | Phase 4 Gate: senior sign-off on knowledge base + interaction map + versioned harness | Senior | P4-08,09,10,11,12,13,14 | ☐ |

---

## 7) CONTINUOUS RESEARCH / RECHECK

| # | Task | Owner | Depends | Done |
|---|------|-------|---------|------|
| CR-01 | Define recheck triggers per element (from section 18 of each .md) + global triggers (major model/protocol/tool version, archetype drift, security issue, friction signals) | V-D | P4-15 | ☐ |
| CR-02 | Set quarterly review cadence + fast-path triggers; document in `GOVERNANCE.md` | V-D | CR-01 | ☐ |
| CR-03 | Establish harness versioning scheme (semver or calver) + changelog + migration notes | V-D | P4-10 | ☐ |
| CR-04 | Handover: how to run the harness, how to extend it, how to deprecate, how to evaluate it | R-A | P4-15 | ☐ |

---

## 8) EXECUTION PROTOCOL FOR WSL AGENTS

### 8.1 Deploy
Each task row above is dispatchable via `agy` / `opencode` on WSL.
Dispatch shape per task:
```
agy run --prompt "<task-specific prompt>" --label "<task-id>"
# or
opencode run --model <tier> --prompt "<task prompt>"
```
- R-A and R-B prompts for the same brief must be **semantically distinct** (different angles, different source pools).
- V-C prompts must be adversarial: "refute this finding; find counter-evidence."
- V-D prompts must be architectural: "re-tag abstraction level; identify level conflation."

### 8.2 Tracking
- Every task update is a checkbox in this file + a commit.
- Evidence lives in `phase-*/EVIDENCE_LOG.md` with source URLs.
- Blocker tasks are flagged in `BLOCKERS.md` if a task cannot proceed.

### 8.3 Gates
No phase's first task starts without prior gate = ✅.
Gates: P0-13, P1-43, P2-18, P3-31, P3.5-13, P4-15.

---

## 9) TASK COUNTS

| Phase | Tasks | Notes |
|-------|-------|-------|
| Phase 0 | 13 | Archetypes + criteria |
| Phase 1 | 43 | 5 batches + cross-batch + gate |
| Phase 2 | 18 | Rubric + 5 groups + synthesis + gate |
| Phase 3 | 31 | Template + queue + per-element + overlap + slices + index + gate |
| Phase 3.5 | 13 | 3 tasks + friction synthesis + feedback loops + re-test + gate |
| Phase 4 | 15 | Template + 6 batches + consistency + interaction map + harness-as-code + audits + gate |
| Continuous | 4 | Recheck + governance |
| **Total** | **137** | Micro-tasks — no lazy surface |

---

## 10) WHAT HAPPENS NEXT

1. You review this plan — call out archetype hints or constraints to bake into P0.
2. I initialize the folder skeleton (`phase-0/`, `phase-1/`, `phase-2/`, `phase-3/`, `phase-3.5/`, `elements/`, `phase-3/tools/`).
3. On your go, I deploy R-A + R-B on P0-01/P0-02 in parallel via WSL (`agy`/`opencode`).
4. We spiral — gate to gate — until the versioned harness is validated and documented.

> **Anti-bloat reminder (enforced at every gate):** Does this materially improve the harness? Is it actually used? Is benefit > complexity? Is it redundant? Can it stay optional? Can it be removed later?
