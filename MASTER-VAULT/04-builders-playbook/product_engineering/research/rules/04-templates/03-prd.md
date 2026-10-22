# Template 03 — PRD (Product Requirements Document)

**Use when:** defining a significant bet. For small bets (≤2-week appetite), sections 1–3 alone serve as the PR/FAQ. **Enforces:** R-02 (metrics), R-04 (launch artefact first), R-05 (appetite, no-gos).

## 1. Press release (write this first)

*One page, as if the product already shipped. If this is boring or hard to write, the thinking isn't done.*

- **Headline** (one sentence): _…_
- **Sub-headline** (the benefit, one sentence): _…_
- **Summary paragraph:** what it is, who it's for, what changes for them.
- **Problem paragraph:** the customer problem, in customer language.
- **Solution paragraph:** how the product solves it — concrete, no adjectives.
- **Quote:** one from a (hypothetical) customer, one from the team — both must sound like something a real person would say.
- **Getting started:** how a customer gets it, what it costs.

## 2. FAQ

*Internal and external hard questions. Minimum: the six below plus three you hope nobody asks.*

1. Who is this NOT for?
2. What does it cost us to build and run? (unit economics sketch)
3. What are we explicitly NOT building? (no-gos)
4. What could go wrong? (risks, abuse cases)
5. How is this different from [competitor/alternative]?
6. What does success look like, in numbers, by when?
7. _Your hardest question:_ …
8. _…_
9. _…_

## 3. Outcome metric and kill criteria

- Primary metric: _…_ · Baseline today: _…_ · Target: _…_ · Measured when: _…_
- Secondary / guardrail metrics (things we must not break): _…_
- If the target is missed: fix with bounded effort of _…_ / kill. Decided by: _…_ on date _…_

## 4. Appetite and scope

- **Appetite:** _… weeks_ (fixed — scope flexes, time doesn't)
- **In scope (the shippable slice):** _…_
- **Rabbit holes** (where we could burn the whole appetite — named so we can route around them): _…_
- **No-gos** (pre-authorised refusals): _…_

## 5. User experience

*Fat-marker level: the key flows as a numbered list or rough sketch. Link detailed designs if they exist. Every flow lists its states (happy, loading, empty, error) — see template 17.*

1. Flow: _…_ → states: _…_
2. …

## 6. Open questions

| Question | Owner | Needed by | Blocks? |
|---|---|---|---|
| | | | |

*No open question may block the bet's start unless named here with an owner and date.*

## Acceptance criteria

- [ ] Press release written before any design artefact, and a stranger can understand the customer value from it alone
- [ ] FAQ answers price/economics, no-gos, risks, and differentiation honestly
- [ ] One primary metric with baseline, target, date, and a named kill/fix decision
- [ ] Appetite fixed; rabbit holes and no-gos named
- [ ] Every key flow lists its non-happy-path states

## Anti-patterns this blocks

AP-01 (weak validation) · AP-02 (scope creep) · AP-04 (unnecessary features) · AP-14 (misleading demos — the PR describes the real product).
