# 09 — Accessibility, Performance & UX Polish

*The legal-technical floor (accessibility), the measured floor (performance), and the craft layer (UX polish and state design). Synthesised from the quality stream (§22 accessibility) and the ux-states stream (§§18–19). Claim labels — **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown** — are preserved; nothing upgraded. This is research, not legal advice.*

---

## Part A — Accessibility: the current standards and the block-release rules

### A1. Standards status as of 2026-10-10

| Standard | Status | Technical bar | Legal weight |
|---|---|---|---|
| **WCAG 2.2** | W3C Recommendation 5 Oct 2023 (updated 12 Dec 2024); approved as **ISO/IEC 40500:2025**. The current recommended standard. (**Verified**) | 86 success criteria (A/AA/AAA) | Referenced directly by laws (see below) |
| **WCAG 3.0** | **Working Draft, 10 Sept 2026.** Incomplete; conformance model still being developed. (**Verified** — W3C publication history) | Broader scope; stronger cognitive-disability coverage | **None. Do not use for conformance claims.** W3C advises organisations to keep meeting WCAG 2.2 A/AA |
| **EN 301 549 v3.2.1** (2021-03) | The version **currently cited in the EU Official Journal** — confers presumption of conformity with the EAA and the Web Accessibility Directive. (**Verified**) | Chapter 9 = WCAG 2.1 AA | **The operative legal yardstick in the EU today** |
| **EN 301 549 v4.1.1** | Published by ETSI 2 Sept 2026; **not yet cited in the Official Journal** (expected late 2026). (**Verified**) | Adopts WCAG 2.2 AA | **Not law yet.** Publishing ≠ legal force |
| **European Accessibility Act** (Directive 2019/882) | **Applicable since 28 June 2025.** (**Verified**) | Annex I functional requirements around the four WCAG principles | Direct obligations on private-sector products/services (e-commerce included); enforcement is member-state-run and uneven |
| **ADA Title II** (US state & local government) | DOJ final rule 24 Apr 2024 names **WCAG 2.1 AA**. Compliance dates **extended by DOJ interim final rule (Apr 2026)** to 26 Apr 2027 (large entities) / 26 Apr 2028 (smaller). (**Verified**; extension **Corroborated**) | WCAG 2.1 AA with narrow content exceptions | In force on the extended timeline |
| **ADA Title III** (US private) | **No technical standard in the regulation.** DOJ withdrew the web rulemaking in 2017. (**Verified**) | — | Litigation-driven; courts and settlements have converged on **WCAG 2.1 AA** |
| **Section 508** (US federal; vendors selling to the government) | **WCAG 2.0 AA** via the 2017 Revised 508 Standards. **No refresh scheduled.** (**Corroborated**) | Two WCAG generations behind current best practice | In force now |

**Practical rule of thumb (Proposed):** build to **WCAG 2.2 AA** and you satisfy every regime above with margin — 2.2 AA is a strict superset of 2.0/2.1 AA, so it satisfies regimes naming older standards too.

**Key EAA facts:** it does not name WCAG in its operative text (presumption of conformity comes via the harmonised standard); it applies to non-EU vendors selling to EU consumers; exemptions cover microenterprise service-providers, purely B2B services, archived content, and disproportionate burden. Penalties are national (e.g., Germany up to €100,000/violation; Netherlands up to €900,000 or 10% of revenue). **What the EAA does not do:** bless partial compliance — the first French court decision (Tribunal judiciaire de Caen, 4 June 2026, against Carrefour: six months to full RGAA compliance, €500/day thereafter, €10,000 damages) rejected a claimed 71% compliance rate outright: accessibility is an obligation of *result*, not effort (**Corroborated**).

### A2. The ten required topic areas (condensed)

| # | Area | The requirement, in plain English | Verification reality |
|---|---|---|---|
| 1 | **Semantic HTML** | Native elements (`<button>`, `<a>`, `<nav>`, headings, lists) before ARIA. `<div onclick>` impostors are a functional *and* accessibility defect | a11y-tree snapshot — flag interactive nodes with no accessible name |
| 2 | **Keyboard navigation** | All functionality operable via keyboard; no traps; logical tab order | Stays manual — "the fastest, cheapest, most impactful manual test" |
| 3 | **Focus visibility** | Visible focus indicator on every interactive element, 3:1 contrast against adjacent colours; never remove outlines without a designed replacement; sticky chrome must not cover the focused control | WCAG 2.2 SC 2.4.11/2.4.12/2.4.13 tighten this area (**Verified**) |
| 4 | **Labels** | Every input has a visible, programmatically associated label; required status communicated | Machines check *presence* (axe-core); *quality* of label text is human-judged |
| 5 | **Contrast** | 4.5:1 normal text, 3:1 large text and UI components | Reliably machine-caught; the highest-volume real-world defect class |
| 6 | **Reduced motion** | Honor `prefers-reduced-motion`: disable or minimize non-essential animation, parallax, auto-playing motion (WCAG 2.3.3) | Check at the OS-setting level, not just in-app toggles |
| 7 | **Screen-reader support** | Correct roles, names, states, and live-region announcements through accessibility APIs | Minimum matrix: **NVDA + Chrome** and **VoiceOver + Safari** (**Corroborated**); task-based testing (complete checkout), not feature tours |
| 8 | **Error announcements** | Validation errors identified in text, associated with their fields, announced (error summary with focus management and/or live regions) | Whether the message is *helpful* is a human judgment |
| 9 | **Responsive zoom** | Usable at 200% browser zoom and 400% at 1280px width (WCAG 1.4.10 Reflow): no two-dimensional scrolling, no clipped content | Test with real zoom, not just narrow viewports |
| 10 | **Accessible dialogs** | Trap focus, label themselves (role + accessible name), close on Escape, return focus to the trigger | WAI-ARIA Authoring Practices dialog pattern is the reference (**Verified**) |

### A3. What automation can and cannot do

- **Deque's analysis** (2,000+ audits, ~300,000 issues): automation covered **~57% of issues by volume** — but only of the issues its rules could identify; it did not measure whether disabled users could complete tasks (**Corroborated**).
- **By share of success criteria**, the machine-decidable portion is **~30–40%** (**Corroborated**). The W3C states the principle without a number: tools "cannot check all accessibility aspects automatically. Human judgement is required" (**Verified** — W3C WAI).
- **The three testing tiers:** (1) automated baseline — axe-core in CI on every page/state, zero new violations; (2) keyboard testing — recommended at every PR for changed flows; (3) screen-reader testing — two pairings, task-based (**Corroborated** practitioner guidance).
- **Overlays/widgets are not a compliance strategy.** The FTC's April 2025 final order required overlay vendor accessiBe to pay **$1 million** over claims its product could make sites WCAG-compliant, and barred such claims without evidence (**Verified** — FTC order). WebAIM's survey: 67% of practitioners rated overlays not at all/not very effective (72% among respondents with disabilities) (**Corroborated**). UsableNet 2026: ~20% of sued companies had a widget installed — a widget "has not proven to be a meaningful deterrent, legally or practically" (**Corroborated**). Runtime scripts are not remediation; they may appear as evidence *against* a defendant.

### A4. Which issues should block release (Proposed)

**Always block (S1), regardless of product:** keyboard trap or core task unreachable by keyboard · focus completely invisible on interactive elements · form that loses user data or submits with no feedback · missing accessible names on primary CTAs/icon-only controls in core flows · new axe-core *violations* (not `incomplete`) on changed pages — the CI baseline must not regress.

**Block when in a regulated scope** (EAA-covered service, US public entity, federal contractor): any failure against the applicable named standard on a customer-facing flow · missing accessibility statement where the regime requires one · uncaptioned video/untagged PDF on a covered service.

**Block on product-risk grounds** (recommended even where not strictly required): checkout/payment flow with any S1/S2 defect — simultaneously legal exposure and conversion loss (e-commerce is ~70% of US filings; ACM found 61% of large Dutch webshops couldn't complete an order with assistive tech — **Corroborated**).

**Do not block, but track:** AAA-only criteria · `incomplete`/needs-review items pending manual triage (time-box it) · minor contrast misses on decorative or disabled elements · single-instance low-traffic content defects.

**Why the gates matter — enforcement postmortem (2025–2026, Corroborated):** US filings reached **4,928 suits in 2025** (federal 3,117, up 27% YoY; UsableNet 2025 Year-End Report, Jan 2026) and are on pace to top **6,000 in 2026**; ~70% target e-commerce; ~29% hit repeat defendants; the 10 most active plaintiff firms file ~84% of cases. In the EU's first EAA year: aggressive civil-society litigation in France, competition-law warning letters in Germany within weeks, 124 complaints in Sweden, and regulators starting with paperwork (Czechia's only public fines: ~€580 total, all for a missing accessibility paragraph in shop terms) while the real barriers sit in checkouts.

---

## Part B — Performance: Core Web Vitals, budgets, RUM

### B1. The thresholds — current authoritative guidance (**Verified**, web.dev, page last updated 2024-10-31)

The current set is **LCP, INP, CLS** (INP replaced FID in March 2024), all measured at the **75th percentile** of page loads, segmented mobile vs desktop. A page passes when all three are "Good":

| Metric | Measures (plain English) | Good | Needs improvement | Poor |
|---|---|---|---|---|
| **LCP** (Largest Contentful Paint) | *Loading* — when the main content becomes visible | ≤ 2.5 s | 2.5–4.0 s | > 4.0 s |
| **INP** (Interaction to Next Paint) | *Interactivity* — how fast the page responds to taps/clicks/keys | ≤ 200 ms | 200–500 ms | > 500 ms |
| **CLS** (Cumulative Layout Shift) | *Visual stability* — how much the layout jumps around while loading | ≤ 0.1 | 0.1–0.25 | > 0.25 |

### B2. Budgets, RUM, and the practices that move the numbers

- **Performance budgets:** set per-template budgets (JS payload, image weight, LCP/INP/CLS at p75) and enforce them in CI; budgets turn performance from a launch activity into a maintained property (**Corroborated**).
- **Real-user monitoring:** web.dev explicitly recommends sites set up their **own RUM** (via the `web-vitals` JS library) because CrUX alone lacks the per-pageview telemetry needed to diagnose regressions. Lab tools (Lighthouse, DevTools) catch regressions pre-release; they are not a substitute for field data (**Verified** guidance).
- **The highest-leverage fixes** (**Corroborated**): compress and serve AVIF/WebP with fallbacks; responsive images via `srcset`/`sizes`; eager-load + `fetchpriority="high"` only the true LCP image — **never lazy-load the LCP element** (documented audit failure); `font-display: swap` with metric-matched fallbacks; split by route and defer non-critical CSS/JS; cache static assets with content-hashed filenames; reserve space for everything that loads late (explicit `width`/`height` or `aspect-ratio` on images, embeds, ads — CLS ≤ 0.1 depends on this).
- **Skeleton hygiene:** skeletons must match final geometry or the "fix" becomes a layout jump; mark the region `aria-busy="true"`; never use skeletons on small components like buttons where they imply interactivity that isn't there. For unpredictable waits, contextual loading copy ("Searching 47 sources…") is reported to outperform generic shimmer (**Corroborated** usage rules; the 40%-perceived-speed figure is single-source — **Proposed**).

---

## Part C — UX polish: the highest-leverage small details

*Guiding rule from the research: do not require every app to implement every detail. Effort should be proportional to user needs, task frequency, action complexity, accessibility impact, and product context. The audit question is never "is it present?" but "is its absence costing users here?"*

Condensed from the §18 polish inventory (the full detail lives in `research/ux-states/01-polish-details.md`):

| Detail | The rule of thumb | Evidence |
|---|---|---|
| **Keyboard shortcuts** | Cmd/Ctrl+K command palette as the universal action surface; `?` cheat-sheet overlay; never override OS/browser standards (Cmd+C/V/A/S); shortcuts must not fire while typing | **Corroborated**; keyboard path is **Verified** WCAG 2.1.1 |
| **Undo + notifications** | Prefer reversible actions with undo over modal confirmations for anything recoverable (Gmail pattern: act, toast with Undo, 5–10s window). Success/info toasts auto-dismiss ~3–6s; errors persist until dismissed. Toasts are live regions, never the sole channel for critical outcomes | **Corroborated**; the exact seconds are **Proposed** |
| **Empty states** | The four empty variants are genuinely different designs — first-use, filtered/no-results, cleared/completed, error. Collapsing them is the most-cited generated-UI shortcut. Filtered-zero echoes the query and offers "Clear filters" | **Corroborated** |
| **Autosave honesty** | Two legitimate philosophies (positive confirmation like Google Docs' "Saved to Drive"; silence-when-fine like Figma) — but never claim "saved" for non-durable data (Excalidraw's "stored in this browser — export to keep" precedent) | **Corroborated** |
| **Confirmation dialogs** | Reserve blocking dialogs for **irreversible, high-cost actions**. Severity × reversibility pattern: reversible → act + undo; soft-deletable → act + undo toast + trash; irreversible → dialog naming the consequence on the button ("Delete 3 files", never "OK"), destructive action not default-focused; catastrophic scope → type-to-confirm or re-auth. Confirming every delete trains reflexive "OK" clicks (habituation) | **Corroborated** |
| **Error surfaces** | Match the surface to severity: inline field errors → toasts/banners with retry → modals for blocking errors → full-page for outages with status-page link. Every message carries (1) what happened in plain language, (2) whether data was saved or lost, (3) how to recover — never raw codes in the UI | **Corroborated** |
| **Forms** | Visible `<label>` above every input (placeholder-as-label fails — **Verified** WCAG 3.3.2); validate on blur, re-validate on change once invalid, keep client/server rules in one shared schema; **never clear a form on submit failure** — losing typed input is cited as the worst thing a form can do (**Verified** WCAG 3.3.7); error messages: colour + icon + text, never colour alone | **Corroborated**; label/preserve-input **Verified** |
| **Focus rings** | ~2px outline with ~2px offset via tokens; `:focus-visible` (not `:focus`); never `outline: none` without replacement; verified in both themes | **Verified** (WCAG 2.4.7, 1.4.11, 2.4.11) |
| **Control states** | Every interactive element needs a defined visual for each reachable state (hover/pressed/disabled/selected/loading) or an explicit opt-out; disabled = reduced opacity **plus a reason** | **Corroborated** |
| **Stale-data honesty** | Show data freshness next to the data ("Updated 2m ago") — the cheapest trust signal in the product; never silently serve stale as fresh | **Corroborated** |
| **Unsaved-change warnings** | Warn on navigation/close only when genuinely dirty (`beforeunload` gated on dirty state); with autosave, the need largely disappears — which is the point | **Corroborated** |
| **No page-level horizontal scrolling** | `html, body` never scroll horizontally; wide content scrolls inside its own container — "the fastest way to make a product feel broken" | **Corroborated** |
| **Custom 404s** | Plain-language message, full nav kept, search box, suggested destinations, **real HTTP 404** (a 200 is a "soft 404" that confuses search engines); prevention first (301s, link audits) | **Corroborated** |
| **Favicon & sharing previews** | Real favicon + SVG icon + apple-touch-icon (a placeholder icon is a documented launch-QA failure); OG tags with absolute 1200×630 image; fallback OG image; verify with platform debuggers | **Corroborated** |
| **Copy buttons** | Click → icon morphs to checkmark / label swaps to "Copied", reverts ~2–2.5s — the label change *is* the feedback; a toast on top is redundant | **Corroborated** |
| **Upload honesty** | Client-side type/size validation is for fast feedback only — the server must re-validate (`accept` is trivially spoofed; **Verified** as standard security practice). State constraints up front; per-file progress; cancel; retry | **Corroborated** |

### Content & trust completeness (legal tiers, condensed)

Not everything is required of every product — the research supports three tiers:

- **Tier 1 — Legally required (jurisdiction-dependent, get counsel):** privacy policy whenever personal information is collected (**Corroborated**); EU prior opt-in cookie consent for non-essential cookies — note the UK changed PECR on 5 Feb 2026 to allow opt-out for low-risk statistics cookies, which does **not** apply to EU visitors; FTC fake-review rule (effective 21 Oct 2024, ~$51–53k/violation); EU AI Act Art. 50 transparency duties (effective 2 Aug 2026; disclose AI interaction, machine-mark synthetic content; fines up to €15M or 3%); EU Consumer Rights Directive pre-purchase disclosures.
- **Tier 2 — Platform/contractual:** app-store listing requirements, ad-platform policies, payment-processor terms (refund/dispute policies), consent-signal frameworks (Google Consent Mode v2 mandatory since March 2024 for EEA traffic).
- **Tier 3 — Trust-building:** honest pricing (no drip pricing/junk fees — FTC has pursued junk-fee enforcement); accurate claims; screenshots that match the shipped implementation; named company identity with real contact info; public status page with incident history; transparent AI limitations; published retention/deletion flows. **Subscription cancellation:** the FTC's 2024 "click-to-cancel" rule was **vacated by the Eighth Circuit in July 2025**, but ROSCA, FTC Act §5, and state auto-renewal laws impose substantially similar duties — easy, same-channel cancellation remains the required posture (**Corroborated**).

---

## Part D — The UX state matrix: structure, applicability, pointers

The research's §19 is a **20-state × 6-concern** matrix (the assignment brief says nineteen; the enumerated rows total twenty — preserved as twenty): for every screen or component that displays data or accepts input, the matrix prescribes the visual treatment, user-facing message, recovery action, accessibility behaviour, telemetry, and expected system behaviour for each state.

The 20 states: Initial/pristine · Loading—first · Loading—refresh · Empty—first use · Empty—no results · Empty—cleared · Success · Validation error · Server error (4xx/5xx) · Network failure/offline · Permission denied (403) · Unauthenticated (401) · Expired session · Partial completion/partial data · Disabled · Stale data · Retry · Cancelled · Destructive-action confirmation · No permission/paywalled.

**Applicability rules — do not force-fit (Corroborated):** for each surface, mark every state **applicable / not applicable / inherited** (inherited = handled by a parent shell, e.g. the app-level offline banner). Legitimate opt-outs: *stale data* — N/A for immutable records; *offline queue* — N/A for read-only marketing pages; *partial completion* — N/A for single-source screens; *destructive confirmation* — N/A where no destructive action exists; *session expiry* — inherited from the auth shell on most screens. Enumerate states *before* building; do not discover them in production.

**Anti-patterns the matrix is designed to prevent:** flashing an empty state before data arrives (no loading state in between) · blanking loaded content during refresh · one "Something went wrong" for every failure class with no recovery path · toast-only critical outcomes · auto-retrying non-idempotent writes (duplicate charges/orders) · collapsing the four empties into one message · confirmation dialogs on reversible actions and missing ones on irreversible ones · silent staleness.

**Where the worked examples live:** three full surface treatments are worked through cell-by-cell in `research/ux-states/02-ux-state-matrix.md` — (1) a data list/table (orders list), (2) form submission (account settings/checkout), (3) a long-running async action (video export / report generation) — each covering treatment, accessibility, telemetry, and system behaviour per applicable state.

## Sources

- Full evidence: `research/quality/02-accessibility.md`, `research/ux-states/01-polish-details.md` (§18: polish details, Core Web Vitals §18D, legal tiers §18E), `research/ux-states/02-ux-state-matrix.md` (§19), plus evidence registers `research/quality/04-evidence-register.md` and `research/ux-states/04-evidence-register.md`.
- Standards: WCAG 2.2 (W3C Rec. 5 Oct 2023; ISO/IEC 40500:2025); EN 301 549 v3.2.1 (OJEU) / v4.1.1 (ETSI 2 Sept 2026); WAI-ARIA Authoring Practices (dialog, menu patterns).
- Legal spine (not legal advice): Directive (EU) 2019/882 (EAA, applicable 28 June 2025); DOJ ADA Title II final rule (24 Apr 2024; interim final rule Apr 2026 extending dates); FTC Rule 16 CFR Part 465 (fake reviews, 21 Oct 2024); FTC accessiBe final order (22 Apr 2025); EU AI Act Art. 50 (2 Aug 2026); FTC Negative Option Rule vacated (8th Cir., July 2025).
- Related report sections: §07 (authenticity anchors; FTC fake-review rule in the anti-slop catalogue), §08 (demo-authenticity checklist §5; severity framework), §10 (AI Act Art. 15; consent/security overlap), §11 (quality gates carry accessibility gates G2/G3/G5/G6).
