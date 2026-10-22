# Solo AI Product Engineering System v1.0
# CLAUDE.md — AI Development Harness Bridge

This workspace is governed by the Solo AI Product Engineering System + AI Development Harness.
All agent executions operate under deterministic lifecycle interception, formal permission policies,
and behavioral guardrails. Read this file before executing any task in this repository.

## Mandatory Behaviors

1. rule-preserve-code-integrity: Preserve all existing comments, docstrings, and architectural
   rationale. Prefer surgical line replacements over destructive overwrites.
2. rule-strict-typing-hygiene: Maintain strict type annotations on all interfaces and function
   signatures. Never bypass typing.
3. rule-zero-secret-leakage: Never write, log, or hardcode API keys, tokens, credentials, or
   high-entropy secrets in files or commit history.
4. rule-verification-before-done: Always run `task verify` and confirm exit code 0 before done.
5. rule-anti-bloat: Keep changes minimal, modular, focused. No unnecessary dependencies.
6. rule-checkpoint-before-destructive: Halt and require [Y/n] keystroke before any file write,
   git commit, or destructive action.
7. rule-loop-rails: Every autonomous loop must have max_steps=15. If the same tool is called
   with identical arguments twice consecutively, throw a fatal error and hand control back.
8. rule-deterministic-termination: Loop termination cannot be based on LLM self-assessment.
   Completion requires a deterministic external gate (test exit code 0, linter clean, etc.).

## Autonomous Project Execution Protocol (When given a PRD or Project)

When the user provides a project name, PRD, specification, or feature request:
1. NEVER start writing production code immediately.
2. Scaffold: Run `task new-project -- <name>` to initialize `projects/<name>/`.
3. Gate 1 & 2 (Appetite & PR/FAQ): Invoke `.harness/skills/working-backwards/SKILL.md` to draft
   `projects/<name>/prfaq.md` with customer press release and skeptical critique. Fill `pitch.md`
   and lock in the Appetite (hours/days) BEFORE defining technical solutions.
4. Gate 3 & 4 (Design & FCAR): Generate `projects/<name>/design-note.md` with min 2 Non-Goals,
   min 2 Alternatives (`alternatives-generator`), and failure modes (`failure-mode-analyzer`).
   Evaluate against `os/fcar-rubric.md`.
5. Implementation (TDD + ECT): Order scopes uphill first (`unknown-first-sorter`). Write failing
   tests first. Complete with `task verify` exit 0 (ECT: Evidence-Carrying Termination).
6. Gate 6: Complete all 8 items in `projects/<name>/launch-checklist.md` before deploy.

## OS Lifecycle (quick reference)
IDEA → [Gate 1: Appetite] → PR/FAQ → [Gate 2: Press Release] → PITCH → [Gate 3: Bet] →
DESIGN NOTE → [Gate 4: FCAR] → LAUNCH CHECKLIST PRE-CHECK → IMPLEMENTATION →
[Gate 5: Per-PR Quality] → SECURITY CHECK → [Gate 6: Launch Checklist Complete] → DEPLOY →
MONITOR → EXPERIMENT → POST-LAUNCH REVIEW → POSTMORTEM (on incident) → ITERATE

## Key Files
| Path | Description |
|------|-------------|
| .harness/hooks/hooks.json | Pre/post tool interceptor manifest |
| .harness/permissions/policies.cedar | Cedar ABAC security rules |
| .harness/permissions/presets.json | Role-based tool access presets |
| .harness/sandbox/gate.sh | Sandbox blast-radius isolation |
| .harness/telemetry/litellm-config.yaml | LLM routing + budget caps |
| os/lifecycle.md | Full product development lifecycle |
| os/fcar-rubric.md | Adversarial review rubric |

## Quick Commands
- Run Tests: task test
- List Skills: task skills-list
- Run Sandbox: task sandbox -- <command>
- Verify Gate: task verify
- Run FCAR: task fcar -- <artifact-path>
- New Project: task new-project -- <name>
