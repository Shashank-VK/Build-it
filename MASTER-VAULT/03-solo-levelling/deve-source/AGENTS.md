# Solo AI Product Engineering System v1.0
# AGENT REGISTRY — AI Development Harness

> Every agent deployed or invoked in this system is tracked here.
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

## Loop rails

1. **Max Steps Global Rail:** `max_steps=15` across all agent loops. Any step count exceeding 15 throws a fatal error and hands control back to developer.
2. **IAL Debounce (Infinite Agentic Loop Guard):** If identical tool + arguments are called twice consecutively, execution halts immediately with fatal exit.
3. **Deterministic Termination Gate (ECT):** Agents cannot declare task completion through conversational self-assessment. External exit code (e.g. `task verify` exit 0, test exit 0, linter clean) is mandatory (evidence-carrying termination: tests/lint exit 0).
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

## Sources

- Anthropic multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- OpenAI Agents SDK multi-agent orchestration: https://openai.github.io/openai-agents-python/multi_agents/
- AWS Bedrock AgentCore: https://aws.amazon.com/bedrock/agentcore/
- Google SRE launch checklist + canary: https://sre.google/sre-book/launch-checklist/ and https://sre.google/workbook/canarying-releases/
