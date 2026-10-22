# Superior OS v2.0
# AGENT REGISTRY — AI Development Harness

> Every agent deployed or invoked in this system is tracked here.
> All executions operate under deterministic loop limits (`max_steps=15`), IAL debounce, and formal ABAC policies.
> Deve v1.0 roles C1-C4 kept. C5-Verification is new. Evidence rules are mandatory.

---

## Operating Contract & Agent Taxonomy

| Role Category | Archetype | Autonomy Model | Primary Toolset | Verification Gate |
|---------------|-----------|----------------|-----------------|-------------------|
| **C1-ProductEngineering** | Fullstack / Product | AI-Assisted / HITL | File I/O, Testing, Linting, Web Search | Gate 5 (PR Quality) + Gate 6 (Launch) |
| **C2-DataMLOps** | Pipeline / ML / Data | AI-Assisted / HITL | Python, File I/O, Pipeline Testing | Data integrity + Deterministic output |
| **C3-PersonalAutomation** | Headless Scripts | Automated / Scoped | Shell, File I/O, Scheduled runners | Dry-run execution + Error alert |
| **C4-AgenticResearch** | Research / Multi-model | AI-First / Human Approved | Web Search, Synthesis, Document Generation | Gate 4 (FCAR Adversarial Review) |
| **C5-Verification** | Eval-runner / Coverage-keeper | Automated / Blocking | Pytest, Evals, Coverage receipts, Fetch log | coverage_gate.py + claim_check.py exit 0 |

## Subagents (specs in .harness/agents/, sandboxed, step-budgeted)
- **coder**: TDD implementation under max_steps=15, evidence-carrying exit.
- **explorer**: read-only codebase research, zero side effects.
- **planner**: strategic decomposition into state-machine scopes.
- **reviewer**: FCAR staff review in a fresh context (no authoring memory).

---

## Loop rails

1. **Max Steps Global Rail:** `max_steps=15` across all agent loops. Exceeding 15 throws fatal and hands control back.
2. **IAL Debounce:** identical tool + arguments twice consecutively halts with fatal exit.
3. **Deterministic Termination Gate (ECT):** no conversational self-certification. External exit code (`task verify` 0) mandatory.
4. **Fresh Context Adversarial Review (FCAR):** reviewers run isolated with zero authoring memory.
5. **Evidence Gate (new):** behavior changes ship with coverage receipts (tests + ranges + sha); external claims ship with URL + HTTP + date rows. Gaps quarantined, never silently dropped.

---

## Autonomous Project Execution Protocol

When given a PRD, project idea, or feature request:
- Do not bypass lifecycle gates. Tier the work first (tiny / default / high-stakes).
- Create `projects/<name>/` via `task new-project -- <name>`.
- Generate PR/FAQ with customer narrative & cynical challenge.
- Lock Appetite in `pitch.md` before designing architecture.
- Draft `design-note.md` with Non-Goals and Alternatives (Gate 4 FCAR).
- TDD implementation, uphill tasks first (coder subagent, sandboxed).
- `task verify` exit 0 (tests + lint + secret-scan + coverage-gate + claim-check) before declaring completion.

---

## Sources

- Contract: `../how-to-use/` (707 cards; authority: opencode-research + first-pass B/D/C/E/A/00).
- Anthropic multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- OpenAI Agents SDK multi-agent orchestration: https://openai.github.io/openai-agents-python/multi_agents/
- Google SRE launch checklist + canary: https://sre.google/sre-book/launch-checklist/ and https://sre.google/workbook/canarying-releases/
