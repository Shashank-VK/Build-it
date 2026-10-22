# Solo AI Product Engineering System v1.0
# Decision Architecture

## Reversible vs. Irreversible Classification Rules

A decision is IRREVERSIBLE (one-way door) if ANY of:
- Changing it requires migrating existing user data
- It creates an external API commitment (backward compatibility applies from this point)
- It requires rebuilding >50% of completed work
- It has a significant third-party cost that cannot be recovered

A decision is REVERSIBLE (two-way door) if ALL of:
- Can be changed within current appetite without restarting
- Affects only internal implementation (no external commitment)
- Changing it doesn't break any existing user-facing contract

## Kill / Pause / Pivot Criteria

KILL: After circuit breaker date, minimum shippable version cannot be completed, no appetite to re-pitch.
  Action: Stop work. Write one-paragraph explanation of why. Archive the Pitch document.

PAUSE: A blocking external dependency is unresolved.
  Action: Freeze scope. Set a resume trigger condition explicitly.

PIVOT: An uphill scope reveals the solution approach is fundamentally wrong.
  Action: Update Pitch document. Apply scope hammer (cut must-haves to minimum). Continue within appetite.

## Veto Structure per Gate
- Gate 2: human + AI skeptical-customer jointly hold veto
- Gate 3: human holds sole veto (only the human can make the bet)
- Gate 4: rubric holds veto — rubric fails the artifact BEFORE human can rationalize past it
- Gate 5: automated tests hold hard veto (no override); AI review holds soft veto (human can override with documented reason)
- Gate 6: checklist holds veto — every single item must pass before deploy
