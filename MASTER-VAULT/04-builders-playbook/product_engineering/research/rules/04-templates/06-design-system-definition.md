# Template 06 — Design-System Definition

**Use when:** two or more surfaces share UI and inconsistency is becoming a tax. **Do not use** for a first product — borrow a component library instead (R-07). **Enforces:** consistency without bureaucracy.

## 1. Scope and non-goals

*Which products/surfaces this system covers, and what it explicitly does not (e.g., marketing site, email templates).*

> _Fill in._

## 2. Principles (3–5, each with an opposite)

*Principles controversial enough to have an opposite — otherwise they're platitudes.*

1. _…_ (opposite: _…_)
2. _…_

## 3. Tokens

*The named values everything derives from. Keep it small.*

| Token | Value | Usage rule |
|---|---|---|
| Color: `brand-primary` | _…_ | _…_ |
| Spacing scale | _…_ | _…_ |
| Type scale | _…_ | _…_ |
| Radius / elevation | _…_ | _…_ |

## 4. Components

*One row per component. "Borrowed from [library]" is a complete and respectable entry.*

| Component | Source (borrowed / built) | States covered (default, hover, focus, disabled, loading, error, empty) | Accessibility notes |
|---|---|---|---|
| Button | | | |
| Input / Form | | | |
| … | | | |

## 5. Patterns

*Recurring compositions: page layouts, empty states, error presentation, confirmation flows, data tables. Each pattern: when to use, when NOT to use, example.*

> _Fill in._

## 6. Accessibility baseline

*The bar every surface meets: keyboard operability, focus visibility, contrast ratios, semantic markup, screen-reader names for icon-only controls, reduced-motion respect. How it's checked (CI lint + periodic manual pass).*

> _Fill in._

## 7. Governance

*Who can add/change components, how proposals are reviewed, how breaking changes are versioned and communicated. Lightweight: a PR and one reviewer.*

> _Fill in._

## Acceptance criteria

- [ ] Every component lists all its states — no happy-path-only components
- [ ] Accessibility baseline is written and checkable, not aspirational
- [ ] Borrowed-vs-built is explicit per component (boring by default)
- [ ] Governance fits on one paragraph — if it needs a committee, the system is too big

## Anti-patterns this blocks

AP-03 (generic design — only where differentiation matters) · AP-15 (missing UX states) · AP-13 (incomplete responsive — tokens include responsive rules).
