# Solo AI Product Engineering System v1.0
# Decision Gates and Review System

| Gate | Trigger | Artifact Reviewed | Blocking Condition | Override |
|------|---------|-------------------|--------------------|----------|
| 1 — Appetite | Before any solution thinking | Stated appetite (days/hours) | No appetite stated | None — must be set |
| 2 — PR/FAQ | After press release written | PR/FAQ document | AI challenge destroys value prop | Human can iterate, cannot skip |
| 3 — Pitch | Before implementation commit | Pitch document | Can't honestly say "I can build this in [appetite]" | None — human decides |
| 4 — Design Note FCAR | If design note required | Design note | Any FCAR rubric item fails | Human waive with documented exception logged in artifact |
| 5 — Per-PR Quality | Before every merge | Code change | Failing automated tests (hard); AI review failures (soft) | Hard: no override. Soft: documented exception. |
| 6 — Launch Checklist | Before any production deploy | Launch checklist | Any incomplete item | Human waive with documented exception visible in checklist |

## FCAR Rubric (the locked adversarial review standard)

A design note/PRD/pitch passes if ALL of these are true:
1. Every claimed user benefit or technical claim is sourced (cited, named, or traceable to a prior finding)
2. Non-Goals section lists at least 2 explicit exclusions (not vague "out of scope")
3. No technical claim is asserted without a named source or traceable prior finding
4. Success metric is measurable and specific ("users will be happy" FAILS; "error rate below 1% within 10 min" PASSES)
5. Alternatives Considered lists at least 1 rejected alternative with a specific rejection reason

## Gate Override Policy
- Hard gates (failing automated tests): NO override permitted under any circumstances
- Soft gates: human may override by writing the exception directly into the artifact at the override point
- All waivers are permanent and visible to any future reviewer — no silent skips

## Tiering (tiny / default / high-stakes)
- Tiny (<4h, reversible, no users/data): pitch 5 lines + secret-scan only. Gates 4 and 6 skipped (mark N/A).
- Default: pitch + 2 No-gos + uphill-first + 8-item checklist.
- High-stakes/irreversible (auth, money, data loss, external API contract): + design-note + FCAR fresh-context mandatory + independent re-implementation.
