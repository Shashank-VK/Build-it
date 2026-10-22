# §34 — Reusable Checklists & Templates: Index

**Workstream:** rules · **Built:** 2026-10-10 · **Read-only:** research artefacts, not adoption advice.

Fill-in-ready templates, each with sections, prompts, and acceptance criteria. Use the smallest template that fits the bet; escalate only when the risk warrants it.

## Lifecycle order

| # | File | Use when | Pairs with rules |
|---|---|---|---|
| 01 | [problem-validation.md](01-problem-validation.md) | Before resourcing any bet — is the problem real? | R-01, R-03 |
| 02 | [idea-evaluation.md](02-idea-evaluation.md) | Comparing candidate solutions to a validated problem | R-02, R-03 |
| 03 | [prd.md](03-prd.md) | Defining a significant bet (doubles as PR/FAQ for small bets) | R-02, R-04 |
| 04 | [technical-design-document.md](04-technical-design-document.md) | Designing the build — interfaces, data, failure modes | R-05, R-06, R-10 |
| 05 | [architecture-decision-record.md](05-architecture-decision-record.md) | Recording any decision that constrains future work | R-06 |
| 06 | [design-system-definition.md](06-design-system-definition.md) | Defining shared UI foundations (only when ≥2 surfaces share) | R-07 |
| 07 | [prototype-acceptance.md](07-prototype-acceptance.md) | Accepting a prototype or demo — what's real, what's faked | R-04 |
| 08 | [development-task-definition.md](08-development-task-definition.md) | Defining a build task for a human or an agent | R-05, R-14 |
| 09 | [agent-instructions.md](09-agent-instructions.md) | Repo-level instructions for coding agents | R-13, R-21 |
| 10 | [test-plan.md](10-test-plan.md) | Planning verification for a bet | R-18, R-19 |
| 11 | [code-review.md](11-code-review.md) | Reviewing a change (checklist for author and reviewer) | R-14, R-20 |
| 12 | [ux-visual-qa.md](12-ux-visual-qa.md) | UX and visual quality pass before release | R-03 |
| 13 | [security-verification.md](13-security-verification.md) | Security verification, structured on OWASP ASVS | R-09, R-21, R-22, R-23 |
| 14 | [release-readiness.md](14-release-readiness.md) | Go/no-go for a release (the release gate) | R-25, R-26, R-27 |
| 15 | [incident-response.md](15-incident-response.md) | Running an incident + writing the postmortem | R-29, R-30 |
| 16 | [post-launch-evaluation.md](16-post-launch-evaluation.md) | Judging a bet against its pre-committed metric | R-02, R-34 |
| 17 | [product-authenticity-polish.md](17-product-authenticity-polish.md) | Authenticity & polish checklist (visual, functional, trust) | R-03 |
| 18 | [launch-readiness.md](18-launch-readiness.md) | Launch readiness: technical correctness AND real user experience | R-02, R-25 |

## How to use this set

1. **Start at 01.** No bet skips problem validation; everything downstream assumes it's done.
2. **Small bets** (≤2-week appetite): 01 → 03 (as PR/FAQ) → 08 → 11 → 14. That's the whole system.
3. **Large bets**: run the full sequence; 04 and 10 are mandatory, 13 gates internet-facing launch, 18 gates public launch.
4. **Every template ends with acceptance criteria** — the filled template is done when the criteria are met, not when the sections are full.
5. Templates live with the work: in the repo, next to the code, versioned like code.

## Conventions used in every template

- *Italic text is a prompt* — guidance for the person filling it in. Delete the prompt, keep your answer.
- `[ ]` checkboxes are the acceptance criteria. Check them literally.
- "N/A with reason" is always an acceptable answer — but the reason must be written down.
- Each template names the rule(s) it enforces so the *why* survives.
