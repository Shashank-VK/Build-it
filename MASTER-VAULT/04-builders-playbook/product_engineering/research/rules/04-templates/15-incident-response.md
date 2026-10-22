# Template 15 — Incident Response & Postmortem

**Use when:** any production incident. Part A runs the incident; Part B is the blameless postmortem (R-30). **Enforces:** R-29, R-30.

## Part A — Response

### A1. Declare

- Severity: _Sev-1 (critical) / Sev-2 (major) / Sev-3 (minor)_ — by user impact, not by technical drama
- Incident commander: _…_ · Declared at: _…_ · Channel: _…_

### A2. Respond (the loop)

1. **Assess** — what's the user impact, what's the blast radius?
2. **Mitigate first** — stop the bleeding (rollback, kill switch, traffic shift, scale). *Fixing root cause comes after mitigation.*
3. **Communicate** — status updates every _…_ minutes to _… (stakeholders, users)_
4. **Record** — timeline as it happens (timestamps, actions, observations)

### A3. Resolve and close

- Mitigated at: _…_ · Resolved at: _…_ · Customer communication sent: ☐

## Part B — Blameless postmortem (within 5 days)

*Premise: everyone involved acted reasonably given what they knew at the time. The question is never "who caused this" — it's "how did the system allow it". "Human error" is the start of the investigation, never the conclusion.*

### B1. Summary

*Three sentences: what happened, what the impact was, what we're changing.*

> _Fill in._

### B2. Timeline

| Time | Event (facts only — no blame language) |
|---|---|
| | |

### B3. Impact

- Users affected: _…_ · Duration: _…_ · Data loss: _…_ · Revenue/SLA impact: _…_

### B4. Contributing factors (systems, not people)

*Use "the alert did not fire / the runbook lacked a step / the metric was ambiguous" language. For each factor: why did it make sense at the time?*

1. _…_
2. _…_

### B5. What went well

*Explicit — so it gets repeated.*

> _Fill in._

### B6. Action items (the postmortem is worthless without these)

| # | Action | Owner | Due | Closes which factor |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

*Action items are tracked like any work — they don't evaporate.*

## Acceptance criteria

- [ ] Mitigation preceded root-causing (A2 order honoured)
- [ ] Timeline is factual; no individual is named as a cause
- [ ] Contributing factors explain *why reasonable actions led here* (hindsight bias countered)
- [ ] Every action item has an owner and a due date; closure is tracked
- [ ] Postmortem shared with the wider team (learning is the product)

## Anti-patterns this blocks

Blameful postmortems · "human error" as a finding · incidents that teach nothing · AP-16 (detection gaps discovered here feed R-28).
