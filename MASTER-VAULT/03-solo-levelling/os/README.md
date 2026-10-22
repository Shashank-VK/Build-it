# Solo AI Product Engineering System v1.0
# Operating System (os/)

The Operating System defines the behavioral governance, lifecycle stages, decision gates, and engineering rules for a solo developer operating with an AI co-pilot.

## Core Documents

- [`lifecycle.md`](lifecycle.md): Full 16-stage idea-to-deprecation sequence.
- [`roles.md`](roles.md): Human vs AI delegation model across the 9 Named Workflows.
- [`gates.md`](gates.md): Decision Gates 1 through 6, blocking conditions, and waiver policies.
- [`decision-architecture.md`](decision-architecture.md): Reversible vs irreversible classifications, kill/pause/pivot criteria.
- [`engineering-rules.md`](engineering-rules.md): 10 core engineering rules, 5 anti-patterns, and Phase 16 loop engineering guards.
- [`quality-security.md`](quality-security.md): Hard/soft quality gates, stakes tiering, and security/reliability baselines.
- [`release-experiments.md`](release-experiments.md): Deployment procedure, pre-committed rollback rules, and A/B testing protocols.
- [`fcar-rubric.md`](fcar-rubric.md): Fresh Context Adversarial Review rubric and verbatim system prompt.

## Artifact Templates (`os/artifacts/`)

- [`prfaq-template.md`](artifacts/prfaq-template.md): Press Release + Skeptical FAQ (Workflow 1 / Gate 2).
- [`pitch-template.md`](artifacts/pitch-template.md): Problem, Appetite, Solution sketch, Rabbit Holes, No-gos (Gate 3).
- [`design-note-template.md`](artifacts/design-note-template.md): Goals, Non-Goals, Design, Alternatives, Rabbit Holes (Gate 4).
- [`launch-checklist-template.md`](artifacts/launch-checklist-template.md): 8-item pre-deploy verification (Gate 6).
- [`postmortem-template.md`](artifacts/postmortem-template.md): 3-section blameless incident analysis (Timeline, 5-Whys, Actions).
- [`build-log-template.md`](artifacts/build-log-template.md): Living session log tracking uphill/downhill scopes and consumed appetite.
