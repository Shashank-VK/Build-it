# §22 — Accessibility & Inclusive Design: Current Standards and Practice

**Workstream:** quality (research only — read-only) · **Researched:** 2026-10-10
**Scope:** The current state of accessibility standards (WCAG 2.2, WCAG 3.0 draft, EN 301 549, European Accessibility Act, ADA/Section 508 and others), the ten required topic areas, how automated checks differ from assistive-technology testing, and which issues should block release.
**Claim key:** Verified · Corroborated · Inferred · Proposed · Unknown
**Legal caution:** This is research, not legal advice. Legal requirements are reported as found in law texts and official guidance, with uncertainty marked. Verify against counsel for any specific product.

---

## 1. Standards status as of 2026-10-10

| Standard | Status (verified) | Technical bar | Legal weight |
|---|---|---|---|
| **WCAG 2.2** | W3C Recommendation **5 Oct 2023**, updated 12 Dec 2024; approved as **ISO/IEC 40500:2025**. The current recommended standard. (Verified — W3C/WAI, corroborated by multiple 2026 sources.) | 86 success criteria (A/AA/AAA). SC 4.1.1 Parsing is obsolete in 2.2. | Referenced directly by laws (see below). |
| **WCAG 3.0** | **Working Draft, 10 Sept 2026** (also 3 Mar 2026, 4 Sept 2025 before it). Incomplete; conformance model still being developed (single conformance level with reporting tiers below/above under discussion; graduated scoring abandoned). (Verified — W3C publication history.) | Guidelines → requirements → assertions → methods; broader scope (web content, apps, tools, publishing, emerging tech); stronger cognitive-disability coverage. | **None. Do not use for conformance claims.** W3C advises organisations to keep meeting WCAG 2.2 A/AA while 3.0 is developed. |
| **EN 301 549 v3.2.1** (2021-03) | The version **currently cited in the EU Official Journal** — i.e. the one that confers presumption of conformity with the EAA and the Web Accessibility Directive. (Verified — corroborated by ETSI directory research and 2026 practitioner sources.) | Chapter 9 = **WCAG 2.1 AA** (clause 9.x.y.z maps 1:1 to WCAG SC x.y.z), plus hardware/software/document requirements WCAG never covers. | The operative legal yardstick in the EU today. |
| **EN 301 549 v4.1.1** | **Published by ETSI 2 Sept 2026** (adopted 24 Aug 2026); replaces v4.1.0 drafts. **Not yet cited in the Official Journal** as of early Sept 2026 (expected late 2026). (Verified — multiple 2026 sources agree on dates.) | Adopts **WCAG 2.2 AA**; updates real-time-text requirements. | **Not law yet.** Publishing ≠ legal force; obligations shift only on OJEU citation. |
| **European Accessibility Act** — Directive (EU) 2019/882 | **Applicable since 28 June 2025.** (Verified.) | Annex I functional requirements, structured around the four WCAG principles (perceivable, operable, understandable, robust). Presumption of conformity via harmonised standards (EN 301 549). | Direct obligations on private-sector products/services (see §2). Enforcement is member-state-run and uneven (see §6). |

### 1.1 United States

| Regime | Standard named | Dates / status |
|---|---|---|
| **ADA Title II** (state & local government) — DOJ final rule **24 Apr 2024** | **WCAG 2.1 AA** for websites and mobile apps, with narrow content exceptions (archived content, pre-existing conventional documents, certain third-party content, individualized password-protected documents, pre-existing social media posts). (Verified — DOJ/advocacy sources.) | Original dates Apr 2026/2027; **extended by DOJ interim final rule (Apr 2026) to 26 Apr 2027** (entities serving ≥50,000) and **26 Apr 2028** (smaller entities, special districts). DOJ said it had overestimated entities' capacity. (Corroborated.) |
| **ADA Title III** (private places of public accommodation) | **No technical standard in the regulation.** DOJ withdrew the Title III web rulemaking in Dec 2017; its 2018 position: the ADA applies to websites, but noncompliance with a voluntary standard does not necessarily indicate noncompliance. In practice, **courts and settlements have converged on WCAG 2.1 AA** (Robles v. Domino's, Gil v. Winn-Dixie line). (Verified.) | Litigation-driven, not deadline-driven. |
| **Section 508** (federal agencies; vendors selling to them) | **WCAG 2.0 AA** via the 2017 Revised 508 Standards. **No refresh scheduled.** (Corroborated.) | In force now. Note the gap: 508 is two WCAG generations behind current best practice. |
| **Section 504 / HHS** (healthcare receiving federal funds) | WCAG 2.1 AA (HHS rule). Compliance extended a year in May 2026: ~May 2027 (≥15 employees) / May 2028 (fewer). (Corroborated by secondary sources; treat dates as Corroborated, not Verified against the Federal Register.) |

### 1.2 Other jurisdictions (summary)

- **UK:** Public Sector Bodies Accessibility Regulations — **WCAG 2.2 AA** plus a published accessibility statement (Corroborated). Private sector: Equality Act 2010 "reasonable adjustments," no named standard.
- **Canada:** Ontario AODA — WCAG 2.0 AA (less live captions/audio description); federal Accessible Canada Act leans on EN 301 549 via CAN/ASC-EN 301 549 (Corroborated).
- **France:** RGAA (national standard); Article 47 carries fines and a mandatory public conformance declaration. France produced the first EAA-framework court decision against a private company (see §6).
- **Germany:** BFSG (national EAA transposition); fines up to €100,000 per violation; enforcement partly via competition-law warning letters (Corroborated).
- **Practical rule of thumb (Proposed):** build to **WCAG 2.2 AA** and you satisfy every regime above with margin, except where a regime names an older standard — where 2.2 AA is a strict superset of 2.0/2.1 AA and therefore also satisfies it.

---

## 2. The European Accessibility Act — actual requirements

**What it is:** Directive (EU) 2019/882 on the accessibility requirements for products and services. It does not name WCAG in the operative text; its Annex I sets functional accessibility requirements, and compliance with the cited harmonised standard (EN 301 549 → WCAG 2.1 AA today) gives a **presumption of conformity**.

**In scope (products):** computers and operating systems, smartphones, TV equipment for digital television, ATMs and payment terminals, e-readers, ticketing/check-in machines. **In scope (services):** electronic communications, banking, **e-commerce**, transport passenger-service information (websites, apps, e-tickets), e-books, audiovisual media services access, 112 emergency communications. **Applies to non-EU vendors selling to EU consumers** — Dutch and other authorities have asserted reach over companies with no EU headquarters (Corroborated).

**Key dates:** applicable **28 June 2025** to new products/services; transitional relief for products already in use (until 28 June 2030 or end of contractual life); long-life self-service terminals up to 20 years (hard stop 28 June 2045); emergency services 28 June 2027. (Corroborated from directive summaries.)

**Exemptions:** microenterprises *providing services*; purely B2B (non-consumer) services; archived web/app content; pre-2025 digital content; third-party content outside the provider's control; disproportionate burden or fundamental alteration. (Corroborated.)

**Penalties:** set nationally — examples: Germany up to €100,000/violation; Netherlands up to €900,000 or 10% of revenue; Ireland up to €60,000 plus possible imprisonment for severe/repeat breaches; France adds daily penalty payments (astreinte). (Corroborated; exact maxima are national-law details — verify per member state.)

**What the EAA does not do:** it does not require a specific technical standard by name, does not mandate overlays or widgets, and does not bless partial compliance — the first French court decision rejected a claimed 71% compliance rate outright: accessibility is an obligation of result (see §6).

---

## 3. The ten required topic areas

### 3.1 Semantic HTML
Use native elements (`<button>`, `<a>`, `<nav>`, `<main>`, headings, lists, tables) before ARIA. Real buttons/anchors are operable, focusable, and announced by default; `<div onclick>` impostors are none of these. Audit method: accessibility-tree snapshot — flag interactive nodes with `role="generic"` or no accessible name. (Corroborated by APG and practitioner tooling.)

### 3.2 Keyboard navigation
All functionality operable via keyboard: Tab/Shift-Tab, Enter/Space, Escape, arrow keys in composite widgets. Test unplugged-mouse walk-throughs of every flow. No keyboard traps; logical focus order. (See §4 on why this stays manual.)

### 3.3 Focus visibility
A visible focus indicator on every interactive element, with sufficient contrast (WCAG 2.2 SC 2.4.11/2.4.12/2.4.13 tighten this area — Verified as new-in-2.2 criteria). Never remove outlines without a designed replacement.

### 3.4 Labels
Every input has a visible, programmatically associated label (`<label for>`, aria-label/labelledby); groups use fieldset/legend; instructions and required status are communicated. Machine-checkable for *presence* (axe-core); *quality* of the label text is human-judged.

### 3.5 Contrast
Text contrast 4.5:1 (3:1 large text) per WCAG 1.4.3/1.4.6; non-text UI components 3:1 (1.4.11); focus indicators per 2.4.11+. Machine-measurable and reliably caught by scanners — one of the highest-volume findings in WebAIM Million. Note: WCAG 3.0 is exploring APCA as a successor contrast model, but it is **not normative** and contrast decisions today must still use WCAG 2.x ratios (Verified — W3C advises 2.2 remains the standard).

### 3.6 Reduced motion
Honor `prefers-reduced-motion`: disable or minimize non-essential animation, parallax, and auto-playing motion. WCAG 2.3.3 Animation from Interactions. Check at the OS-setting level, not just in-app toggles.

### 3.7 Screen-reader support
Content must expose correct roles, names, states, and live-region announcements through accessibility APIs. Automated checks verify attribute presence; only testing with real assistive technology verifies the experience. Minimum matrix: **NVDA + Chrome** and **VoiceOver + Safari** (covers desktop and iOS; JAWS behaves differently enough to add for high-risk products). Screen-reader survey data and practitioner guidance converge on at least two pairings (Corroborated).

### 3.8 Error announcements
Validation errors must be identified in text, associated with their fields, and announced (e.g. via error summary with focus management and/or live regions). WCAG 3.3.1/3.3.3/4.1.3. Whether the message is *helpful and recoverable* is a human judgment — see §21.

### 3.9 Responsive zoom
Usable at 200% browser zoom and 400% at 1280px width (WCAG 1.4.10 Reflow): no two-dimensional scrolling, no clipped or overlapping content. Test with real zoom, not just narrow viewports.

### 3.10 Accessible dialogs
Modal dialogs trap focus, label themselves (role + accessible name), close on Escape, and return focus to the trigger. APG dialog pattern is the reference implementation guide (Verified — W3C living document).

---

## 4. Automated checks vs manual assistive-technology testing

**What automation reliably does:** axe-core and equivalent engines check machine-decidable rules — missing alt attributes, missing form labels, contrast ratios, missing landmarks/headings, language attributes, some ARIA misuse, target-size measurement. Results come in buckets including `incomplete` ("needs review") — the tool's own admission of its limits.

**Coverage, honestly measured:**
- Deque's analysis of 2,000+ audits (~300,000 issues): automation covered **~57% of issues by volume** — higher than the old 20–30% rule of thumb, but it counted only issues the rules could identify and did not measure whether disabled users could complete tasks (Corroborated).
- By share of success criteria, the machine-decidable portion is **~30–40%** (Corroborated).
- The W3C states the principle without a number: tools "cannot check all accessibility aspects automatically. Human judgement is required" (Verified — W3C WAI).

**What manual testing adds (the three tiers):**
1. **Tier 1 — automated baseline:** axe-core in CI on every page/state; zero new violations.
2. **Tier 2 — keyboard testing:** the fastest, cheapest, most impactful manual test; catches focus traps, missing operability, broken tab order. Recommended at every PR for changed flows (Corroborated practitioner guidance).
3. **Tier 3 — screen-reader testing:** at least two pairings (NVDA+Chrome, VoiceOver+Safari); task-based (complete checkout, complete signup), not feature-tour.

**Overlays/widgets:** third-party "accessibility widget" scripts do not remediate source code. The FTC's April 2025 final order required overlay vendor accessiBe to pay **$1 million** over claims its product could make sites WCAG-compliant, and barred such claims without evidence (Verified — FTC order, corroborated across sources). WebAIM's practitioner survey: 67% of accessibility practitioners rated overlays not at all/not very effective (72% among respondents with disabilities) (Corroborated). UsableNet 2026: ~20% of sued companies had a widget installed; a widget "has not proven to be a meaningful deterrent, legally or practically" (Corroborated). **Implication:** overlays are not a compliance strategy and may appear as evidence *against* a defendant.

---

## 5. Which issues should BLOCK release

Blocking must reflect applicable law *and* product risk — not every WCAG failure is equal. Proposed blocking rules:

**Always block (S1), regardless of product:**
- Keyboard trap or core task unreachable by keyboard.
- Focus completely invisible on interactive elements.
- Form that loses user data or submits with no feedback.
- Missing accessible names on primary CTAs / icon-only controls in core flows.
- New axe-core *violations* (not `incomplete`) on changed pages — the CI baseline must not regress.

**Block when the product is in a regulated scope (EAA-covered service, US public entity, federal contractor):**
- Any failure against the applicable named standard (EN 301 549/WCAG 2.1 AA; WCAG 2.2 AA where the regime names it) on a customer-facing flow.
- Missing accessibility statement where the regime requires one (EU public sector; France RGAA declaration).
- Uncaptioned video / untagged PDF on a covered service.

**Block on product-risk grounds (recommended even where not strictly legally required):**
- Checkout/payment flow with any S1/S2 accessibility defect — this is simultaneously legal exposure and conversion loss; e-commerce is ~70% of US filings and ACM found 61% of large Dutch webshops couldn't complete an order with assistive tech (Corroborated).
- Error messages that are not announced or not recoverable in signup/checkout.
- Contrast failures on primary text (highest-volume real-world defect class).

**Do not block, but track:** AAA-only criteria, `incomplete`/needs-review items pending manual triage (time-box the triage), minor contrast misses on decorative or disabled elements, single-instance low-traffic content defects.

---

## 6. Enforcement & litigation postmortems (why the gates matter)

### 6.1 United States — volume and concentration
- **2025:** 4,928 web accessibility suits filed across all US jurisdictions; federal filings 3,117, up 27% year over year (UsableNet 2025 Year-End Report, Jan 2026 — Corroborated).
- **2026 pace:** on track to top 6,000, up ~20% — a record; H1 2026 had the highest first-half volume UsableNet has tracked (UsableNet 2026 Midyear — Corroborated).
- **Concentration:** ~70% target e-commerce; 35.8% of the top-500 e-retailers were sued in 2025; ~29% of suits hit repeat defendants (46% in federal court); the 10 most active plaintiff firms file ~84% of cases; 20–25 plaintiffs drive most filings (Corroborated).
- **Implication:** exposure is predictable and sector-concentrated, not random. A retail/checkout product that "hasn't been sued yet" is in the highest-risk pool, and settling once does not end exposure.

### 6.2 European Accessibility Act — first enforcement wave (from 28 June 2025)
- **France (civil litigation):** days after the deadline, disability organisations ApiDV and Droit Pluriel with legal collective Intérêt à Agir tested four grocery retailers' online shopping with blind/low-vision users; core functions (listings, checkout, delivery slots, cart, pricing) were broken for screen-reader users everywhere tested. Formal notices July 2025; injunctions filed Nov 2025. **4 June 2026: Tribunal judiciaire de Caen ruled against Carrefour** — six months to full RGAA compliance, €500/day penalty thereafter, €10,000 damages; the court rejected a claimed 71% compliance rate: a platform "cannot be only somewhat accessible" — obligation of result, not effort. The parallel **Auchan case was dismissed 5 May 2026** (Lille) on a disputed reading of the turnover threshold; plaintiffs appealed to Douai. Scoreboard: enforcement is real, outcomes not uniformly pro-plaintiff. (Corroborated across accessiway, digitalapplied, and a community enforcement tracker.)
- **Germany:** private law firms sent e-commerce operators competition-law warning letters within weeks of the law taking effect (BFSG) (Corroborated).
- **Netherlands:** ACM's March 2026 assistive-tech shopping test of ~100 large webshops/telecom/energy sites: **inspectors could not finish the order at 61%**; formal enforcement expected H2 2026 (Corroborated).
- **Sweden:** PTS opened first cases Oct 2025; 124 public complaints logged (110 services, 14 products) (Corroborated).
- **Czechia:** the only EAA fines on the public record in the first 15 months — four fines totalling ~€580, all for a missing accessibility paragraph in shop terms, each bundled with other consumer-law breaches (Peculiar Systems review, Oct 2026 — Corroborated; note: single-studio review, treat totals as Corroborated not Verified).
- **France (regulator):** DGCCRF checked 20+ websites in early 2026; planned corrective/penalty action for about half (Corroborated).
- **Implication:** the EAA's first year shows a split pattern — aggressive civil-society litigation in France, slow administrative fining elsewhere, and regulators starting with paperwork (terms-and-conditions paragraphs) while the real barriers sit in checkouts. A compliance program that only fixes the accessibility *statement* is addressing the part regulators check first and the part users need last.

### 6.3 The accessiBe / overlay lesson
FTC final order (22 Apr 2025): $1M over claims an overlay widget could make any site WCAG-compliant; barred from representing compliance without evidence (Verified). Combined with the lawsuit data above, the postmortem is: **runtime scripts are not remediation; source-code fixes plus manual verification are the only defensible record.**
