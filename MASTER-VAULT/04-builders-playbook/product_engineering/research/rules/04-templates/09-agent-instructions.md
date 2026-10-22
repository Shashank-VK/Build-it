# Template 09 — Agent Instructions (for coding agents)

**Use when:** defining the standing instructions for coding agents in a repository (e.g., `AGENTS.md`, skill files, harness configs). **Enforces:** R-13 (verification), R-21 (least privilege), R-14 (small changes). Derived from Anthropic's "Building Effective Agents" guidance: simplest pattern first, guardrails and human checkpoints for autonomy.

## 1. Scope of authority

*What the agent may do unsupervised, what needs human approval, what is forbidden. Be explicit — ambiguity becomes autonomy.*

- **May do unsupervised:** _e.g., read-only investigation; edits within the task's listed files; running tests_
- **Needs human approval:** _e.g., schema migrations; dependency additions; changes outside the task scope; anything touching auth/payments_
- **Forbidden:** _e.g., production access; force-push; deleting data; committing secrets; disabling tests or linters_

## 2. Task execution rules

1. Work from a written task definition (template 08) — if the task is ambiguous, ask or state assumptions, don't guess silently.
2. Keep diffs small and single-purpose (R-14). One task, one coherent change.
3. Never bundle refactors with behaviour changes.
4. Follow the repo's existing patterns; match surrounding code style. Boring over clever (R-07).
5. Delete dead code you create; never leave commented-out blocks or repurpose identifiers (R-16).

## 3. Verification requirements (non-negotiable)

*The agent's work is untrusted until verified — by the agent first, then by a human.*

- [ ] Run the relevant test suite; all green (or: new failures triaged and explained)
- [ ] Add or update tests for the changed behaviour (template 10)
- [ ] Self-review the full diff before handing off — read it as a reviewer would
- [ ] SAST/SCA/secrets scans pass (run via the repo's pipeline, not skipped)
- [ ] Verify any dependency the agent suggests exists in the registry before adding (anti-slopsquatting)
- [ ] Summarise for the human reviewer: what changed, why, what was verified, what remains uncertain

## 4. Tool and permission manifest

*Every tool/capability the agent may use, with its permission level. Reviewed like code.*

| Tool / capability | Permission (read / write / none) | Scope limit |
|---|---|---|
| Filesystem | | _e.g., repo dir only_ |
| Shell | | _e.g., no network, no sudo_ |
| Database | | _e.g., none / read-only local_ |
| Network / APIs | | _e.g., package registry read_ |
| … | | |

## 5. Failure behaviour

*What the agent does when stuck, when tests fail irreparably, or when the task conflicts with these instructions: stop, report state, and wait — never improvise destructive recovery. Escalation path: _…_*

## 6. Workflow vs agent choice

*Per Anthropic's taxonomy: use deterministic workflows (fixed code paths) where the steps are known; reserve autonomous agent loops for open-ended investigation with clear stopping conditions. Name which parts of this repo's automation are which.*

> _Fill in._

## Acceptance criteria

- [ ] Authority tiers are explicit — no capability is ambiguous
- [ ] Verification checklist is mandatory, not advisory
- [ ] Tool manifest follows least privilege (R-21)
- [ ] A human reviews every agent-produced diff before merge (R-20)
- [ ] Instructions are versioned with the repo and reviewed when the agent's capabilities change

## Anti-patterns this blocks

AP-09 (AI code without verification) · AP-10 (uncontrolled agents) · AP-11 (excessive automation).
