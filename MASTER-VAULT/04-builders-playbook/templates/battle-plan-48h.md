> **Adapts:** §17 template 03 (prd.md) → shrunk to the one-page bet doc / napkin spec, plus §17 template 16's pre-committed evaluation date folded in as the demo moment. **Cut:** full PRD sections, EARS acceptance criteria → plain observable outcomes; the "sections 1–3 suffice for ≤2-week appetites" rule becomes the default. (Proposed adaptation.)

# 48-Hour Hackathon Battle Plan

Fill this in the 10-minute pre-hack sit-down. One page. If it doesn't fit, your scope is already too big.

**Event:** ______________________ | **Clock starts:** ______ | **Hard cutoff:** ______ | **Submit-by (30 min early):** ______

## The demo moment (outcome metric)

In one sentence, the moment that must land for a judge:

> _"

## Judging criteria (Finding #5 — Verified: read the rubric, then aim at it)

| Criterion (copied from the rules) | What we demo for it | Status |
|---|---|---|
| 1. | | ☐ |
| 2. | | ☐ |
| 3. | | ☐ |
| 4. | | ☐ |

**Kill rule:** any feature not serving a criterion above dies on sight. (Adapted from §14 R-01/R-02.)

## The hero feature (Finding #2 — Corroborated: one feature)

> _

**The 3-minute filter:** can we demo this compellingly in 3 minutes? ☐ yes / ☐ scope it down / ☐ kill it

## The cut list — WHAT THE DEMO WILL NOT SHOW (sacred)

1. _
2. _
3. _

## Prize-track call (Corroborated: target less-competitive tracks deliberately)

- [ ] Main track only
- [ ] Targeting: ______________________ (sponsor/API track) — genuine use of their API, not shoehorned (Verified score-killer screen)

## Battle rhythm (hours — Proposed/Inferred; structure Corroborated)

| Phase | Hours | Target |
|---|---|---|
| 0 — Idea + scope lock | 0–4 | Evaluator passed, napkin spec written, cut list locked. No new features after. |
| 1 — Skeleton to live URL | 4–12 | Repo + hello-world deployed live. Rollback = last good commit. |
| 2 — Hero feature | 12–34 | One feature, end-to-end, real code path. |
| 3 — Polish + insurance | 34–41 | Demo flow only. Mock fallbacks for every live API. **Backup video recorded.** |
| 4 — Freeze + submit | 41–48 | Bug fixes only. Demo path E2E on prod. **Submitted 30 min early.** |

## Insurance moves (Finding #1 — Corroborated)

- Backup video: ☐ recorded (by end of phase 3) | location: ______
- Mock-data fallbacks: ☐ verified for API: ______ / ______
- Deploy path tested before clock start: ☐ (live URL: ______)
- Secrets: env-based config only, scan on every push ☐ (adapted from §14 R-15)

## Roles-for-one (Proposed)

- Coding blocks: ______ → ______
- Pitch/video owner (also me, timeboxed): ______ → ______
- Hard stop for sleep: ______ ("never ship after midnight")

## Sign-off

Idea passes the evaluator (attached / linked): ☐ | Cut list written before coding: ☐
