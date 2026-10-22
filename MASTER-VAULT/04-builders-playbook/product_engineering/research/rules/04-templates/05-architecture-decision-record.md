# Template 05 — Architecture Decision Record (ADR)

**Use when:** any decision that constrains future work (tech choice, data model, API contract, build-vs-buy, infra topology). **Enforces:** R-06. **Timebox:** 20 minutes. Stored with the code, named `docs/adr/NNNN-title.md`.

## ADR-NNNN: _Title_

- **Status:** proposed | accepted | deprecated | superseded by _…_
- **Date:** _…_ · **Deciders:** _…_

## Context

*What situation forces this decision? What constraints (appetite, team size, scale, regulation) apply? Two to five sentences.*

> _Fill in._

## Decision

*What we will do, in one paragraph. Concrete enough that a new hire could act on it.*

> _Fill in._

## Consequences

*What becomes easier, harder, or impossible because of this? Include the innovation tokens spent (R-07) and the reversibility story.*

- Good: _…_
- Bad: _…_
- Reversal cost if we're wrong: _…_

## Alternatives considered (brief)

| Alternative | Why it lost |
|---|---|
| | |

## Acceptance criteria

- [ ] Context explains *why now*, not just *what*
- [ ] Consequences name at least one real cost (no cost-free decisions exist)
- [ ] Reversal cost is estimated honestly
- [ ] Filed in the repo's ADR directory, linked from the relevant code or README

## Anti-patterns this blocks

Re-litigation of settled decisions; accidental reversal of load-bearing choices; knowledge loss when people leave.
