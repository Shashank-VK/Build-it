# Template 04 — Technical Design Document

**Use when:** designing the build for any bet with architectural surface (new service, data model, integration, or anything irreversible). **Enforces:** R-05, R-06, R-10. **Timebox:** proportional — one page for small, several for large.

## 1. Context

*Link the PRD (template 03) and the ADRs this design follows or creates. One paragraph: what are we building and why, technically.*

> _Fill in._

## 2. Goals and non-goals

- Goals: _…_
- Non-goals (as important as goals): _…_

## 3. Proposed design

*Components, data flow, and interfaces. A diagram plus prose. Name the boring choices (R-07) and where the innovation tokens are spent.*

- Architecture sketch: _…_
- Key interfaces/APIs (request/response shapes, error shapes): _…_
- Data model and storage choices: _…_
- Chosen technologies and why they're boring (or why the novelty is justified): _…_

## 4. Failure modes and resilience (mandatory)

*For EVERY integration point (HTTP, DB, queue, LLM API, webhook), answer:*

| Integration | If it's slow | If it's down | If it returns garbage | Strategy (timeout / breaker / bulkhead / degrade / fail-fast) |
|---|---|---|---|---|
| | | | | |

*Also: what is the blast radius of this design's worst failure? What is the rollback story?*

## 5. Security considerations

*Trust boundaries crossed, authN/authZ model, data classification, secrets handling. Link the threat model (template 13, section 2) if this crosses a trust boundary.*

> _Fill in._

## 6. Operability

*How will we know it's working? Golden signals to instrument (R-28), dashboards, alerts with runbook links (R-29), and what "normal" looks like.*

> _Fill in._

## 7. Alternatives considered

*At least one serious alternative and why it lost. "We didn't consider alternatives" is not an acceptable entry.*

| Alternative | Why it lost |
|---|---|
| | |

## 8. Rollout and migration

*Progressive rollout plan (R-25), flag strategy if any (R-26), migration approach for data/schema (expand/contract), and the rehearsed rollback procedure.*

> _Fill in._

## Acceptance criteria

- [ ] Every integration point has a named failure strategy — no "it won't fail"
- [ ] Blast radius and rollback procedure are written down
- [ ] At least one alternative considered with a reason for rejection
- [ ] Security and operability sections are non-empty (or N/A with a written reason)
- [ ] Boring-vs-novel technology choices are explicit

## Anti-patterns this blocks

AP-06 (fragile architecture) · AP-16 (poor observability) · AP-17 (unnecessary infrastructure).
