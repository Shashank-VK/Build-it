# Phase 0 — STATUS

> **Phase:** Anchor the Project (Archetypes + Success Criteria) | **Gate:** P0-13
> Last updated: 2026-08-31 20:45 IST | Workflow: `wf_c917d118-556`

## Progress

| Task | Title | Owner | Status | Artifact |
|------|-------|-------|--------|----------|
| P0-01 | Candidate archetype longlist (broad sweep) | R-A `a77a` | **DONE** | [`R-A_BROAD_MAPPER.md`](R-A_BROAD_MAPPER.md) — 12 archetypes, 7 angles, 16 searches, 49K |
| P0-02 | JTBD-derived archetype longlist (challenger) | R-B `a266` | **DONE** | [`R-B_CHALLENGER.md`](R-B_CHALLENGER.md) — 12 JTBD archetypes, 18-metric matrix, 22K |
| P0-07 | Success metrics longlist (broad) | R-A | **DONE** | [`R-A_BROAD_MAPPER.md`](R-A_BROAD_MAPPER.md) — 26 metrics (M01–M26) |
| P0-08 | Metric↔archetype relevance matrix | R-B | **DONE** | [`R-B_CHALLENGER.md`](R-B_CHALLENGER.md) — 18×8 matrix, NOISE detection |
| P0-03 | Merge longlists → 5–7 canonical archetypes | V-C `aa34` | **DONE** | [`V-C_ADVERSARIAL.md`](V-C_ADVERSARIAL.md) — 12→6 canonical, 3 conflations flagged |
| P0-11 | Adversarial missing-archetype hunt | V-C | **DONE** | [`V-C_ADVERSARIAL.md`](V-C_ADVERSARIAL.md) — 4 probes: 2 confirmed (mobile/embedded, cost/timeliness), 2 killed |
| P0-09 | Final 8–12 measurable success criteria | V-D `a80a` | **DONE** | [`V-D_ARCHITECTURAL.md`](V-D_ARCHITECTURAL.md) — 10 SCs with instrument+threshold+archetype |
| P0-10 | Rubric wiring (criteria → 7 rubric dims) | V-D | **DONE** | [`V-D_ARCHITECTURAL.md`](V-D_ARCHITECTURAL.md) — 7-dim wiring matrix, harm 4–5 rules, anti-averaging |
| P0-04 | Per-archetype constraint matrix | Synth | **DONE** | [`ARCHETYPES_AND_CRITERIA.md`](ARCHETYPES_AND_CRITERIA.md) §2 constraints matrix |
| P0-12 | Synthesize `ARCHETYPES_AND_CRITERIA.md` | Senior | **DONE** | [`ARCHETYPES_AND_CRITERIA.md`](ARCHETYPES_AND_CRITERIA.md) — 22K, 6 canonical + 10 SCs + wiring + probes |
| P0-05 | Postmortem cross-check (≥2 per archetype) | — | **DEFERRED** | Lightweight — covered by verifier citations; deep dive in Phase 1 if needed |
| P0-06 | User-fit verification | — | **QUEUED** | Needs your input at gate (see below) |
| P0-13 | **Gate: senior sign-off** | **YOU** | **AWAITING APPROVAL** | → Phase 1 on pass |

## Key Findings

- **Convergence:** Both researchers independently landed on 12 archetypes (vendor vs JTBD cut) — strong signal the space is well-covered at 12 candidates.
- **Reduction:** V-C merged 12→6 canonical (Product Engineering, Data/MLOps Fabric, Automation/Browser, Agentic/Knowledge, Platform/Infra, Migration) — 50% anti-bloat cut.
- **Missing found:** Content Pipeline, Browser/RPA, Glue, Revenue Plumbing (R-B) + mobile/embedded toggles (V-C) — not promoted to canonical, kept as capability-profile toggles.
- **Metrics:** 26 (R-A) + 18 (R-B) longlists → 10 final SCs (V-D) each with instrument + threshold + archetype + leading/lagging tag. Vanity metrics (output volume, registered users, deploy freq on content) flagged as NOISE.
- **Wiring:** 7-dim rubric (frequency, harm, benefit, complexity, maintenance, security, generality) deterministically wired to SCs — Phase 2 ranking is now traceable, not intuition.
- **Payload gaps:** Verifiers received truncated R-A + missing R-B bundle — repaired by re-reading full `.md` files from disk during synthesis. Logged in `ISSUES.md`.

## Gate Questions for You (P0-13)

1. **Mobile/embedded promotion?** V-C says keep as toggles under C1/C5; promote to C7 only if you build on-device. Want C7 now or later?
2. **Content Pipeline sub-mode gate?** Should Firecrawl+browser-use+n8n publishing loop get its own `gate.sh` vs reusing C4 research gate?
3. **Any archetype missing for YOUR work?** Does the 6 cover what you actually ship? If not, name it and we add before Phase 1.

## Next on Pass

**Phase 1 Batch 1 — Execution & Agency Layer** (P1-01..08) via WSL `agy`/`opencode`:
- Subagents, delegation, orchestration, workflows, background tasks, git worktrees, agent teams, autonomy calibration, HITL
- Same 4-agent pattern: R-A + R-B parallel (divergent lenses) → V-C (translation/kill) + V-D (abstraction re-tag) barrier
