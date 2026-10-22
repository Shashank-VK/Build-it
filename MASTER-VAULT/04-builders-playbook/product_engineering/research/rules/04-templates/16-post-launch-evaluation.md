# Template 16 — Post-Launch Evaluation

**Use when:** after the pre-committed measurement window for any bet (template 03, §3). **Enforces:** R-02 (metrics), R-34 (kill/fix/keep). This is where the outcome metric renders its verdict.

## 1. The bet (as committed)

- Bet: _…_ · Shipped: _date_ · Evaluation date: _…_
- Primary metric: _…_ · Baseline: _…_ · Target: _…_ (from template 03 — copied, not rewritten)

## 2. What actually happened

| Metric | Baseline | Target | Actual | Verdict |
|---|---|---|---|---|
| Primary: _…_ | | | | ☐ hit / ☐ missed |
| Guardrail 1: _…_ | | | | ☐ held / ☐ broken |
| Guardrail 2: _…_ | | | | ☐ held / ☐ broken |

*Qualitative signal: what did users actually say/do? (support themes, session notes, churn reasons)*

> _Fill in._

## 3. Why

*Your best honest explanation of the gap (or the success). Separate what the data says from what you believe.*

- Data says: _…_
- We believe: _…_
- What we'd need to learn to be sure: _…_

## 4. Decision: keep, fix, or kill

- [ ] **Keep and invest** — metric hit (or credibly trending); next investment: _…_
- [ ] **Fix (bounded)** — one more appetite of _…_, targeting _…_; new kill criteria: _…_
- [ ] **Kill** — removal plan: _… (rollout care per R-25; user communication; data handling)_ · lesson recorded: _…_

*No fourth option. "Wait and see" without a new measurement date is kill-avoidance.*

## 5. Lessons for the system

*What does this teach future bets? (Feeds templates 01–03 and the kill/fix/keep review.)*

> _Fill in._

## Acceptance criteria

- [ ] Actuals compared against the *pre-committed* target — no post-hoc metric shopping
- [ ] Guardrail metrics checked (did we break anything to win?)
- [ ] A keep/fix/kill decision made by the named decider, on the committed date
- [ ] Kill decisions include a removal plan and a recorded lesson

## Anti-patterns this blocks

AP-04 (zombie features) · AP-19 (vanity metrics) · sunk-cost continuation.
