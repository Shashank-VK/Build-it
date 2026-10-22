# Template 10 — Test Plan

**Use when:** planning verification for a bet or release. **Enforces:** R-18 (critical paths gated), R-19 (test the real path). Proportional: a paragraph for small changes, this full template for significant bets.

## 1. Scope

*What's under test (link PRD/design doc). What's explicitly out of scope and why.*

> _Fill in._

## 2. Critical paths (the release gate)

*The flows that must work. Each gets automated tests; a red suite blocks release (R-18).*

| # | Critical path | Test type (unit / integration / E2E) | Production-shaped? (real inputs, real path) | Owner |
|---|---|---|---|---|
| 1 | _e.g., signup → email verify → first use_ | | ☐ | |
| 2 | | | ☐ | |

## 3. Test matrix

| Area | Unit | Integration | E2E / manual | Notes |
|---|---|---|---|---|
| Happy paths | | | | |
| Error / edge cases | | | | _adversarial inputs, not just fixtures_ |
| Failure modes (R-10) | | | | _slow dependency, down dependency, garbage response_ |
| Data migrations | | | | _forward + rollback rehearsed_ |
| Content/config paths | | | | _the CrowdStrike lesson: test the content, not just the code_ |
| Accessibility | | | | |
| Performance baseline | | | | _R-17: baseline, profile, target_ |

## 4. Environments and parity

*Where tests run; how staging differs from prod (R-19); what's validated in prod (synthetics, smoke tests post-deploy).*

> _Fill in._

## 5. Flaky-test policy

*Flaky tests are quarantined within 48h with a named owner and a fix-or-delete date. A red suite nobody trusts is worse than no suite.*

> Owner of quarantine list: _…_

## 6. Entry/exit criteria

- **Entry (ready to test):** _…_
- **Exit (ready to release):** critical paths green ☐ · no open Sev-1/2 defects ☐ · performance within target ☐ · rollback rehearsed ☐

## Acceptance criteria

- [ ] Every critical path has an automated test through a production-shaped path
- [ ] Failure modes from the design doc (template 04, §4) each have a test
- [ ] Content/config/data paths are tested, not just application code
- [ ] Flaky-test ownership is assigned, not aspirational
- [ ] Exit criteria are checkable, not subjective

## Anti-patterns this blocks

AP-07 (poor testing) · AP-12 (broken interactions) · AP-15 (missing UX states — tested, not just designed).
