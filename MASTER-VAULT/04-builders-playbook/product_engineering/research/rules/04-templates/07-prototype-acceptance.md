# Template 07 — Prototype Acceptance

**Use when:** accepting a prototype, demo, or spike — from a human or an agent. Its job is to make *what's real* explicit, so demos never become commitments by accident. **Enforces:** R-04 (honest artefacts).

## 1. What was asked for

*The task definition or pitch this prototype answers (link template 08 or the pitch).*

> _Fill in._

## 2. Reality inventory (mandatory)

*Every capability shown, marked honestly. This table is the whole point of the template.*

| Capability shown | Real (works on real data, real path) | Simulated (Wizard-of-Oz / hardcoded / mocked) | Notes |
|---|---|---|---|
| | ☐ / ☐ | ☐ | |
| | ☐ / ☐ | ☐ | |

*Rule: anything not marked is assumed simulated. Anything simulated must be disclosed to anyone who sees the demo (AP-14).*

## 3. What was learned

- Feasibility verdict: _…_
- Biggest surprise: _…_
- What we'd do differently in the real build: _…_

## 4. Throwaway or evolve?

- [ ] **Throwaway** — the prototype is discarded; the real build starts clean (Brooks: plan to throw one away). Prototype branch deleted by: _…_
- [ ] **Evolve** — specific parts carry forward: _…_ ; the rest is discarded. Carried parts get full verification (R-13, R-18) before they count as product code.

*Default: throwaway. "Evolve everything" requires justification.*

## 5. Decision

- [ ] Proceed to build (template 03/04) — feasibility retired
- [ ] Iterate the prototype — open question: _…_
- [ ] Kill — reason and lesson: _…_

## Acceptance criteria

- [ ] Reality inventory is complete — a stranger can tell what's real
- [ ] Simulated capabilities are disclosed wherever the demo is shown
- [ ] Throwaway-vs-evolve decided explicitly, with a deletion date for throwaway code
- [ ] Learnings recorded even if the prototype is killed

## Anti-patterns this blocks

AP-14 (misleading product demos) · AP-06 (prototype architecture calcifying into production).
