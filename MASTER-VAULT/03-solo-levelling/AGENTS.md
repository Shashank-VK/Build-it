# Solo AI Product Engineering System v1.0
# AGENT REGISTRY — AI Development Harness

> Every agent deployed or invoked in this system is tracked here.
> Sourced from 15 research phases and 102+ empirical validation fleet deployments.
> All executions operate under deterministic loop limits (`max_steps=15`), IAL debounce, and formal ABAC policies.

---

## Operating Contract & Agent Taxonomy

| Role Category | Archetype | Autonomy Model | Primary Toolset | Verification Gate |
|---------------|-----------|----------------|-----------------|-------------------|
| **C1-ProductEngineering** | Fullstack / Product | AI-Assisted / HITL | File I/O, Testing, Linting, Web Search | Gate 5 (PR Quality) + Gate 6 (Launch) |
| **C2-DataMLOps** | Pipeline / ML / Data | AI-Assisted / HITL | Python, File I/O, Pipeline Testing | Data integrity + Deterministic output |
| **C3-PersonalAutomation** | Headless Scripts | Automated / Scoped | Shell, File I/O, Scheduled runners | Dry-run execution + Error alert |
| **C4-AgenticResearch** | Research / Multi-model | AI-First / Human Approved | Web Search, Synthesis, Document Generation | Gate 4 (FCAR Adversarial Review) |

---

## Autonomous Loop Constraints (Phase 16 Hardening)

1. **Max Steps Global Rail:** `max_steps=15` across all agent loops. Any step count exceeding 15 throws a fatal error and hands control back to developer.
2. **IAL Debounce (Infinite Agentic Loop Guard):** If identical tool + arguments are called twice consecutively, execution halts immediately with fatal exit.
3. **Deterministic Termination Gate (ECT):** Agents cannot declare task completion through conversational self-assessment. External exit code (e.g. `task verify` exit 0, test exit 0, linter clean) is mandatory (arXiv:2608.23623).
4. **Fresh Context Adversarial Review (FCAR):** Review agents MUST be invoked in an isolated context with zero memory of authoring history to prevent reviewer collusion.

---

## Autonomous Project Execution Protocol

When given a PRD, project idea, or feature request:
- Do not bypass lifecycle gates.
- Create `projects/<name>/` via `task new-project -- <name>`.
- Generate PR/FAQ (`prfaq.md`) with customer narrative & cynical challenge.
- Lock Appetite in `pitch.md` before designing architecture.
- Draft `design-note.md` with Non-Goals and Alternatives.
- Perform TDD implementation with uphill tasks first.
- Complete `task verify` with exit code 0 before declaring completion.

---

## Historical Validation Fleet Provenance (102+ Agent Deployments)

- **Phase 0 (Taxonomy & Criteria):** 4 agents (`R-A`, `R-B`, `V-C`, `V-D`) → Canonical taxonomy (22K)
- **Phase 1 (Batches 1–5 Discovery):** 20 agents across Execution, Context, Integration, Safety, DX/Meta → Master Taxonomy (48 elements)
- **Phase 2 (Ranking):** 10 agents (5 rankers + arbiter + tension verifier) → 21S/12A/4B ranking
- **Phase 3 (Tool Selection):** 26 agents across 8 tool batches + slice build → Tool Selection Index
- **Phase 3.5 (Empirical Validation):** 8 agents + 3 materializers → Operational `.harness/`
- **Phase 4 (Documentation):** 6 agents → Complete OS documentation suite
- **Validation Fleet:** 28 agents (26 validators + 2 synthesizers) → Zero false-positive security guard, hardened Cedar ABAC, sandbox isolation.
