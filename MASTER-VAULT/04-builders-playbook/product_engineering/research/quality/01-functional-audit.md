# §21 — Route-by-Route & Interaction-by-Interaction Functional Audit

**Workstream:** quality (research only — read-only) · **Researched:** 2026-10-10
**Scope:** How teams systematically discover missing functionality in a web product: the interaction inventory, what "expected vs implemented" means per item, automated detection methods, and the hard limits of automation.
**Claim key used throughout:** Verified · Corroborated · Inferred · Proposed · Unknown

---

## 1. The inventory: what a complete functional audit must enumerate

A functional audit begins with a closed inventory. Anything not on the list is not tested. The recommended minimum inventory has 16 element classes. For each class, the audit records four fields:

| Field | Meaning |
|---|---|
| **Expected behaviour** | What the spec/design says the item must do (observable outcome, not implementation) |
| **Implemented behaviour** | What was actually observed when exercised (pass, fail, or partial — with the exact observed result) |
| **Verification method** | How the check was performed (which tool/manual step, on which build, at which route) |
| **Severity if broken** | What happens to users/revenue/legal standing when it fails |

Severity scale used in this document (Proposed, aligned with common QA practice):

- **S1 — Blocker:** core task impossible (checkout, login, payment); or legal/compliance failure. Blocks release.
- **S2 — Critical:** major function degraded or inaccessible to a user group; workaround painful. Must fix before release unless formally excepted.
- **S3 — Major:** feature impaired but usable with effort; visual or content defect on a high-traffic surface.
- **S4 — Minor:** cosmetic, edge-case, or low-traffic surface.

### 1.1 Routes / pages
- **Expected:** every route declared in the routing table renders its intended page; no dead routes; no routes reachable that were never intended (e.g. stale campaign URLs returning 200 with junk).
- **Verification method:** extract the route manifest from the codebase (router config / file-system routes); crawl the built app with a headless-browser crawler seeded from `sitemap.xml` and navigation; compare crawled URL set vs route manifest; log any URL returning 4xx/5xx and any manifest route never reached. (Verification method: Proposed synthesis of crawler practice; route-manifest extraction is standard in React/Next.js audit tooling — Inferred from practitioner sources.)
- **Severity:** S1 if a core-flow route 404s/500s; S2 for orphaned dead links to removed pages; S3 for untracked junk routes returning 200.

### 1.2 Navigation links
- **Expected:** every link navigates to the correct destination, uses the correct target, and its label matches its destination; no link to a retired URL.
- **Verification method:** crawl and HTTP-HEAD/GET every `<a href>`; classify green (OK), yellow (redirect chain), red (broken), gray (error). Browser extensions such as LinkAudit scan per-page with real-time results and CSV/JSON export; site crawlers (e.g. LibreCrawl-style tools, Screaming Frog class) do this site-wide. Record redirect chains longer than 2 hops as S3 (flagged in crawler practice — Corroborated across crawler skill references).
- **Severity:** S2 for broken primary-nav links; S3 for broken footer/content links; S4 for a single redirect hop on a low-traffic page.

### 1.3 Buttons
- **Expected:** every button does something observable (navigates, submits, opens a dialog, changes state) and is not a visual dead end.
- **Verification method:** enumerate interactive elements from the accessibility tree; click each and assert an observable change (URL change, DOM change, network request, dialog open). "Click-everything" crawl scripts built on Playwright do this. Detect `<div onclick>` impostors (non-semantic clickable divs) via the accessibility tree — these are both a functional smell and an accessibility defect. (Proposed synthesis; click-everything crawlers are a known QA technique — Inferred.)
- **Severity:** S1 for dead primary CTAs; S2 for dead secondary controls.

### 1.4 Forms
- **Expected:** every input has a visible, programmatically associated label; required/optional status is communicated; validation errors are announced and recoverable; submission produces a confirmation or a clear error; no data loss on validation failure.
- **Verification method:** automated: axe-core flags missing labels and some markup errors (Verified — axe rule set). Manual/keyboard: submit empty, submit invalid, submit valid; check error messaging and focus movement to the error summary. (Proposed as standard practice — Corroborated by WCAG error-identification requirements.)
- **Severity:** S1 for a form that loses user data or blocks submission silently; S2 for unlabelled inputs.

### 1.5 Modals / dialogs
- **Expected:** open on trigger, trap focus while open, close on Escape/close-button/backdrop (per design), return focus to the trigger on close, expose an accessible name and role.
- **Verification method:** keyboard-only open/close cycle; axe-core + manual focus-trap check; WAI-ARIA Authoring Practices dialog pattern as reference (Verified — APG is a W3C living document; status confirmed via the standards registry found in research).
- **Severity:** S1 for a focus trap that strands keyboard users; S2 for missing accessible name.

### 1.6 Menus (nav menus, dropdowns, context menus)
- **Expected:** open/close via mouse, touch, and keyboard; arrow-key navigation where the pattern calls for it; dismiss on Escape or outside click; no orphaned open state.
- **Verification method:** scripted keyboard walk-through against the APG menu-button/disclosure patterns; automated checks limited to presence of keyboard handlers (mostly manual). (Inferred from APG coverage.)
- **Severity:** S2 if keyboard users cannot reach menu items; S3 for minor dismiss quirks.

### 1.7 Upload controls
- **Expected:** accept/reject file types and sizes with clear messaging; show progress; handle network failure mid-upload; never silently drop a file.
- **Verification method:** e2e test with fixture files of each type/size class, including an oversized file and a mid-upload network abort (Playwright `route.abort` / offline simulation). (Proposed — standard e2e technique.)
- **Severity:** S2 for silent data loss; S3 for unclear error text.

### 1.8 Search & filtering
- **Expected:** queries return relevant results; empty result sets explain themselves; filters combine correctly; pagination/sorting preserve filter state.
- **Verification method:** seeded-data test matrix (known corpus, expected result sets); assert result counts and ordering; test the zero-result state explicitly. (Proposed.)
- **Severity:** S2 for filters that silently drop criteria; S3 for poor relevance.

### 1.9 Auth flows
- **Expected:** sign-up, login, logout, password reset, session expiry, and multi-factor steps all complete; error messages don't leak account existence beyond policy; sessions expire as specified.
- **Verification method:** e2e with test users; time-travel or short-lived tokens for expiry; check that logged-out state actually invalidates the session server-side. Auth flows cannot be crawled anonymously — they need scripted, credentialed e2e. (Inferred from crawler limitations — crawlers cannot bypass login screens, Verified from crawler documentation found in research.)
- **Severity:** S1 for login/logout or reset broken; S1 for session-invalidation failure (security).

### 1.10 Payment flows
- **Expected:** the full purchase path completes in test mode: cart → details → payment → confirmation; failures (declined card, 3-D Secure challenge, timeout) produce recoverable states; no double-charge on retry; amounts displayed match amounts charged.
- **Verification method:** gateway sandbox/test cards; idempotency-key check on retry; never against production. (Proposed — standard payments QA; this document does not instruct implementation.)
- **Severity:** S1 for any charge/display mismatch or double-charge; S1 for a dead checkout step.

### 1.11 Integrations (third-party embeds, APIs, webhooks)
- **Expected:** each integration degrades gracefully when the third party is slow or down; failures are logged and surfaced, not silent.
- **Verification method:** stub/fault-inject the third party in a test environment (timeout, 500, malformed payload); verify fallback UI. (Proposed.)
- **Severity:** S1 if a third-party outage takes down a core flow with no fallback; S2 for silent failures.

### 1.12 Keyboard interactions
- **Expected:** every interactive element reachable and operable by keyboard; visible focus; no traps; logical tab order; skip links where appropriate.
- **Verification method:** manual keyboard walk-through of every flow (the single cheapest high-yield manual test — Corroborated by practitioner guidance found in research); supplement with automated tab-order capture. No automated tool fully verifies logical order or trap-freedom.
- **Severity:** S1 for traps or unreachable core controls; S2 for illogical order.

### 1.13 Responsive behaviours
- **Expected:** at each supported breakpoint the layout is usable: no horizontal overflow, no overlapping hit targets, no clipped text, tap targets ≥ minimum size.
- **Verification method:** automated viewport sweep — load key pages at mobile/tablet/desktop widths, assert `document.documentElement.scrollWidth <= window.innerWidth` (no horizontal overflow), screenshot each. Mobile overflow detection via scrollWidth comparison is a known scripted technique (Inferred). Visual regression tools (Percy/Chromatic/Playwright `toHaveScreenshot`) capture unintended layout shifts — see §3.
- **Severity:** S2 for unusable mobile layout or overlapping tap targets on a core flow; S3 for minor clipping.

### 1.14 Empty / error states
- **Expected:** every list, search, and data view has a designed empty state; every failure mode (network down, 500, timeout, permission denied) shows a human-readable, recoverable message — never a blank page or raw stack trace.
- **Verification method:** fault injection (offline mode, forced 500s) plus seeded empty datasets; screenshot each state. These are the states most often never designed and never tested — the audit must enumerate them explicitly. (Inferred from QA practice; empty-state coverage is a recurring practitioner complaint — Corroborated by UX research conventions.)
- **Severity:** S2 for blank/500-exposing states on core flows; S3 elsewhere.

### 1.15 External links
- **Expected:** open the correct destination; clearly signal when leaving the product (icon/label/`rel` attributes per policy); no link to compromised or parked domains.
- **Verification method:** same crawl as §1.2, plus periodic re-checks on a schedule (link rot is time-dependent). (Proposed.)
- **Severity:** S3 generally; S1 if a payment/support link points at a hijacked domain.

### 1.16 Destructive actions
- **Expected:** delete/cancel/unsubscribe require explicit confirmation; the confirmation names what will be destroyed; undo or recovery exists where promised; the action is idempotent (double-click ≠ double-delete).
- **Verification method:** e2e double-submit test; verify confirmation copy and post-action state. (Proposed.)
- **Severity:** S1 for unconfirmed irreversible destruction or data loss.

---

## 2. Methods for AUTOMATICALLY detecting defects

| Defect class | Automated method | Tooling (examples, not endorsements) | What it reliably proves |
|---|---|---|---|
| Broken links | Full-site crawl; HEAD/GET every href/src | Link-checker extensions (per-page), site crawlers, Playwright crawl scripts, sitemap-vs-crawl diff | That the URL resolves and returns non-error status. Nothing about whether the destination is *correct*. |
| Dead buttons | Enumerate interactive nodes from the accessibility tree; click each; assert observable change | Playwright/Cypress scripts; a11y-tree snapshots | That a click produces *some* observable effect. Not that the effect is the *right* one. |
| Missing routes | Diff route manifest against crawled URL set; flag 4xx/5xx; flag manifest routes never visited | Router-config extraction + crawler | Coverage of declared routes. Cannot find routes that exist but are never linked (orphan pages) without the manifest. |
| JS errors | Attach console/pageerror listeners during crawl and e2e runs; fail on uncaught exceptions | Playwright `page.on('pageerror')`, Cypress failure capture, error-tracking in staging | That an exception fired on exercised paths. Silent logic errors produce no signal. |
| Failed requests | Intercept/log network traffic; flag 4xx/5xx, timeouts, aborted critical requests | Playwright request/response listeners, HAR capture | That requests failed. Not whether the UI handled the failure well (needs the error-state check in §1.14). |
| Inaccessible controls | Run axe-core per page/state; triage `violations` and `incomplete` ("needs review") buckets | axe-core, Lighthouse accessibility category, Playwright `@axe-core/playwright` | Presence of machine-detectable violations (~57% of issues by volume per Deque's study — see §4). The `incomplete` bucket is the explicit list of what a human must review. |
| Visual regressions | Baseline screenshot comparison per page/state/breakpoint | Playwright `toHaveScreenshot` (free, local baselines), Percy, Chromatic, Applitools, BackstopJS, Argos CI | That pixels changed beyond threshold. Cannot judge whether the change is a *bug* or an *intended redesign* — every diff needs human review. |
| Mobile overflow | Viewport sweep asserting no horizontal scroll; tap-target size measurement | Playwright viewport matrix + scrollWidth assertion; axe target-size rules (WCAG 2.2) | Mechanical overflow and undersized targets. Not whether the layout is *usable*. |

Notes on the tooling landscape (all Corroborated by 2026 practitioner sources):
- **Playwright vs Cypress for e2e:** Playwright's auto-waiting (attached, visible, stable, enabled, receiving events) eliminates the largest flake class — acting on elements that aren't ready. Both auto-wait; Playwright's actionability checks are more comprehensive, and retries/traces/sharding are built in and free. Flakiness usually comes from timing, test data, or environment drift, not the framework.
- **Visual regression:** hosted tools (Percy, Chromatic, Applitools) earn their cost in the *review workflow* (baselines, approvals, cross-browser rendering), not in raw diffing. Playwright's built-in screenshots are sufficient for small teams but lack a review UI and need consistent CI environments to avoid font-rendering false positives.
- **Anti-flake discipline:** assert on state, not time (no hard-coded sleeps); prefer role/test-id selectors over CSS classes; isolate tests with seeded state; mock third parties sparingly; capture traces/videos on CI failure. Google reported ~16% of its tests showed some flakiness (Google Testing Blog, 2016 — Corroborated); treat any test that only passes on retry as a bug, not a green result.

---

## 3. What automated scanning CANNOT prove — the human/e2e remainder

This is the most important section of the audit methodology. Each item below is something scanners structurally cannot decide; each needs realistic end-to-end testing or human inspection (Corroborated across Deque's coverage analysis, W3C WAI guidance, and practitioner sources):

1. **Whether alt text is meaningful.** Scanners check *presence*, not quality. A photo described as "image123" passes the machine check.
2. **Whether reading and focus order is logical.** Only a keyboard walk-through reveals a tab order that jumps across the page.
3. **Whether custom widgets are actually usable with assistive technology.** ARIA attributes can be present and wrong.
4. **Whether captions/transcripts are accurate.** Presence is checkable; correctness is not.
5. **Whether error messages are genuinely helpful and recoverable.** A scanner sees text; a human judges whether a user can act on it.
6. **Whether a visual change is a bug or an intended redesign.** Screenshot diffing flags pixels; humans judge intent.
7. **Whether empty/error/loading states are humane.** Fault injection can reach the state; only inspection judges it.
8. **Whether a multi-step flow (auth, checkout, onboarding) works for a real user.** Crawlers can't log in; scripted e2e can, but only realistic data, realistic timing, and realistic user behaviour expose race conditions and state bugs.
9. **Whether content is understandable** — plain language, consistent terminology, predictable behaviour.
10. **Whether the product is operable under realistic constraints:** slow networks, small screens, zoomed text, assistive tech, third-party outages.

**The agent "done" caveat:** an AI agent's green check is weaker evidence than a human's. LLM-generated tests reproduce the same anti-patterns found in human-written training data, including tests that pass without asserting anything, and the "iterate until green" loop pushes toward weakening assertions to vacuity rather than fixing code (arXiv:2410.10628; practitioner analysis — Corroborated). A passing suite written or iterated by an agent must be audited for assertion strength before it counts as evidence. See §23.

---

## 4. Coverage numbers to calibrate expectations

- Deque's study of 2,000+ audits / 13,000+ pages / ~300,000 issues found automated testing covered **~57% of accessibility issues by volume** — but only of the issues its rules could identify; it did not measure whether disabled users could complete tasks (Corroborated across multiple 2026 sources citing Deque, 2021/2023).
- Counted by share of WCAG success criteria a tool can even evaluate, the machine-decidable portion is closer to **30–40%** (Corroborated); one analysis puts reliably auto-flaggable WCAG 2.1 AA criteria at ~13% (single-source claim — treat as Inferred/uncertain, methodology unclear).
- WebAIM Million 2026 (Feb 2026 crawl): detectable WCAG 2 failures on **95.9% of home pages**, averaging **56.1 errors per page**; the six most common failure types (low contrast, missing alt, missing form labels, empty links, empty buttons, missing document language) account for ~96% of detected errors — and are exactly the failures scanners catch reliably (Verified via WebAIM Million reporting, Corroborated by secondary sources).

**Implication for the audit:** automation clears the high-volume, low-judgment defects cheaply. Budget the human pass for everything in §3 — roughly half the defects by any counting method.
