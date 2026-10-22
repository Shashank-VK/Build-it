# Template 12 — UX & Visual QA

**Use when:** before any user-facing release. **Enforces:** R-03 (usability risk). One pass per flow; check literally.

## 1. Scope

*Flows under test (link PRD/design):*

> _Fill in._ · *Tested on (devices/browsers):* _…_

## 2. UX states per flow (mandatory)

*For EACH flow, verify every applicable state. Mark N/A only with a reason.*

| State | Flow 1: _…_ | Flow 2: _…_ | Notes |
|---|---|---|---|
| Loading (initial + partial) | ☐ | ☐ | _skeletons/spinners, no blank screens_ |
| Empty (no data yet) | ☐ | ☐ | _helpful, with a next action_ |
| Error (action failed) | ☐ | ☐ | _what happened + what to do; input preserved_ |
| Offline / degraded | ☐ | ☐ | |
| Permission denied | ☐ | ☐ | |
| Rate-limited / quota | ☐ | ☐ | |
| Destructive confirm | ☐ | ☐ | _explicit, reversible where possible_ |
| Success | ☐ | ☐ | _confirmation + next step_ |

## 3. Responsive

- [ ] No horizontal scroll at 360px, 768px, 1280px
- [ ] Tap targets ≥44px on touch viewports; no hover-only interactions on mobile
- [ ] Tables/data degrade gracefully (cards, scroll regions, or progressive disclosure)
- [ ] Tested on at least one real device, not just devtools emulation

## 4. Visual

- [ ] Matches the design-system tokens (template 06) — or deviations are deliberate and recorded
- [ ] Typography hierarchy consistent; no orphan text styles
- [ ] Focus states visible on all interactive elements
- [ ] Reduced-motion respected; no seizure-risk animation
- [ ] Dark mode (if offered) has no invisible text or broken contrast

## 5. Accessibility spot-check

- [ ] Keyboard-only completion of each flow
- [ ] Screen-reader names on icon-only controls
- [ ] Contrast meets WCAG AA for body text
- [ ] Form errors announced and associated with fields

## 6. Content

- [ ] No lorem ipsum, placeholder copy, or TODO text anywhere in the flow
- [ ] Error messages written for users (what happened, what to do), not for developers
- [ ] Dates, numbers, currencies formatted for the user's locale

## Acceptance criteria

- [ ] Every flow has every applicable UX state verified — the table is the proof
- [ ] Responsive checked at 3 widths on a real device
- [ ] Accessibility spot-check passed or failures filed as blocking bugs
- [ ] Zero placeholder content in the release

## Anti-patterns this blocks

AP-12 (broken interactions) · AP-13 (incomplete responsive) · AP-15 (missing UX states).
