# §18 — Small Details That Make Products Feel Complete

- **Workstream:** ux-states (user prompt §§18–20), research only — discover, inspect, identify, verify, categorize, explain usage, record sources. No installs, builds, configuration, ranking, or recommendations.
- **Researched:** 2026-10-10. All sources accessed 2026-10-10.
- **Method:** official design-system / standards docs (web.dev, WCAG), engineering blogs, plus unofficial sources (designer blogs, practitioner skill repos, teardowns, community essays, failure write-ups). Per-finding source metadata lives in `04-evidence-register.md`.
- **Claim labels used below:** **Verified** = confirmed by an authoritative/official source · **Corroborated** = consistent across ≥2 independent sources · **Inferred** = logical extension from evidence, not directly stated · **Proposed** = practice recommended by practitioner sources but without hard evidence · **Unknown** = no reliable source found.

## Guiding principle (evaluating each item)

Do not require every app to implement every detail below. The research consensus is consistent: effort should be proportional to user needs, task frequency, action complexity, accessibility impact, and product context. Over-applying patterns is itself a defect — one practitioner source calls the bloat failure mode "applying all of these to a 4-field form." A login form does not need skeleton screens; a read-only marketing page does not need offline queuing. The audit question is never "is it present?" but "is its absence costing users here?"

---

## A. Interaction / state completeness

### A1. Keyboard shortcuts & command-key behaviour
Keyboard-operable alternatives for the most frequent actions, discoverable without a manual. **Corroborated.** Sources agree on the discoverability ladder:
- **Command palette (Cmd/Ctrl+K)** as the universal, searchable action surface — doubles as a self-updating cheat sheet since every row shows its binding.
- **Cheat-sheet overlay** on `?` (Figma, Slack, Notion, Linear, GitHub pattern).
- **Tooltip hints** showing the shortcut after a short hover (Figma's tool-icon pattern).
- **Modifier discipline:** Cmd/Ctrl = system actions (save, undo, copy, find); never override the OS/browser standards like Cmd+C/V/A/S or browser chrome shortcuts.
- Scope rules: global vs view-level vs component-level registration, cleaned up on unmount; shortcuts must not fire while the user is typing in a text field.
- **Accessibility hard floor (Verified, WCAG 2.1.1):** every pointer action needs a keyboard path; no keyboard traps.

### A2. Undo + notifications
Prefer reversible actions with undo over modal confirmations for anything recoverable. **Corroborated.**
- The Gmail pattern: act immediately, show a toast with an inline Undo link, commit only when the window expires. Practitioner consensus puts the undo window at **5–10 seconds** (some sources say 5–8s). **Proposed** (no primary study found on exact seconds).
- Severity-based persistence: success/info toasts auto-dismiss in ~3–6s; errors and actionable toasts persist until dismissed. Timer pauses on hover/focus. **Corroborated.**
- Toasts are a **live region** (`role="status"` / `aria-live="polite"` for info; `role="alert"` for blocking errors), never steal focus, and are never the sole channel for critical outcomes — duplicate in persistent UI or a notification log. Max ~3 visible, stacked, each with a manual dismiss. **Corroborated.**

### A3. Empty states with next steps
Never render "No data." as a dead end. **Corroborated.**
- Structure: what will live here + why it matters + one primary action (verb-first label: "Create project", not "Submit"). A template/sample-data option raises activation further.
- **The four empty variants are genuinely different designs** (first-use, filtered/no-results, cleared/completed, error). Collapsing them into one message is cited as the most common UX shortcut in generated interfaces. Filtered-zero states echo the query and offer "Clear filters."
- One primary action, not a menu of options; keep copy short; `aria-labelledby` on the region.

### A4. Skeleton loaders
Skeleton screens that mirror the final layout reduce perceived wait time (practitioner sources cite 30–40% perceived-speed improvement tracing back to LinkedIn's 2013 studies; the exact percentage is **Inferred** — the original LinkedIn writeup by Luke Wroblewski described the effect qualitatively). **Corroborated** usage rules:
- Skeletons for content-heavy loads in the ~1–10s range; spinners for brief bounded waits or operations of unpredictable duration; **no indicator at all under ~100ms–1s** (flashing indicators are worse than none — classic Nielsen response-time thresholds).
- Skeleton must match final geometry (same approximate heights/widths) or the "fix" becomes a layout jump; mark the region `aria-busy="true"`; never use skeletons on small components like buttons where they imply interactivity that isn't there.
- **Counterexample / debate:** for unpredictable AI-generated waits, a looping shimmer communicates no progress; contextual loading copy ("Searching 47 sources…") outperforms generic shimmer (one 2026 practitioner essay claims 40% lower perceived load and 60% fewer support tickets from contextual copy — **Proposed**, single-source, treat as directional not measured). For refresh of already-loaded data, keep old data visible with a subtle indicator instead of blanking to skeleton.

### A5. Progress indicators
Determinate progress (bars with real percentages) wherever completion is estimable; non-linear/easing bars feel faster than linear ones (Harrison et al., CHI 2010, cited via practitioner sources — **Corroborated** but second-hand). Indeterminate spinners only when duration is unknowable. Long waits (>10s) need a time estimate plus a cancel option and ideally a notification on completion so the user can leave.

### A6. Drag-and-drop uploads
Large, clearly-highlighted drop zones; full-window drop overlay optional. **Corroborated** engineering detail: model each file as an explicit state machine (queued → uploading → success/error), report progress via XHR `upload.onprogress` (fetch has no upload-progress event), wire cancel through `AbortController`, and offer **retry** that reuses the `File` object. Client-side type/size validation is for fast feedback only — the server must re-validate, since the `accept` attribute and MIME types are trivially spoofed (security boundary, **Verified** as standard practice). Generate thumbnails with `URL.createObjectURL` and revoke on removal to avoid memory leaks. Always provide a keyboard/click alternative — drag-and-drop is never the only path (accessibility).

### A7. Autosave + save confirmation
Two production philosophies, both legitimate — pick the honest one for your product (**Corroborated** via Google Docs vs Figma analysis):
- **Positive confirmation:** Google Docs' header chip cycling "Saving…" → "Saved to Drive" (clickable into version history). Gmail/Medium use the same subtle pattern.
- **Silence-when-fine:** Figma shows nothing while autosaving, and only surfaces a bottom notification when offline or sync fails — while storing edits locally and syncing on reconnect.
- Honesty rule: never claim "saved" for data that isn't durable (e.g., localStorage-only drafts should say "stored in this browser — export to keep", per Excalidraw precedent). Include a persistent "Last saved" timestamp for long-form work.

### A8. Offline banners + recovery
**Corroborated** pattern: detect via `navigator.onLine` plus `online`/`offline` events (and heartbeat for finer-grained truth).
- Persistent, non-dismissible top banner ("You're offline — changes will sync when you reconnect"), self-clearing on reconnect, announced via `role="alert"`.
- Queue mutations locally (IndexedDB/localStorage), replay on reconnect, resolve conflicts (last-write-wins or user-chosen merge), and show a discard summary if anything couldn't be replayed.
- Show a "Last synced: N minutes ago" staleness indicator; lock or degrade server-dependent controls while offline but keep purely local elements working.

### A9. Focus rings
**Verified** (WCAG 2.x + vendor/accessibility guidance):
- **2.4.7 Focus Visible (Level AA):** any keyboard-operable interface must show a visible focus indicator — the legal/accessibility floor (also part of EN 301 549 behind the European Accessibility Act and ADA-referenced practice).
- Contrast comes from **1.4.11 Non-text Contrast:** the indicator needs 3:1 against adjacent colors. Use `:focus-visible` (not `:focus`) so rings show for keyboard users without appearing on mouse clicks. Never `outline: none` without a replacement (W3C failure F78).
- **2.4.11 Focus Not Obscured (AA):** sticky headers/banners must not cover the focused control entirely.
- Practical baseline: ~2px outline with ~2px offset, driven by design tokens, verified in both light and dark themes.

### A10. Hover / pressed / disabled / selected / loading states
Every interactive element needs a defined visual for each reachable state, or an explicit opt-out. **Corroborated** conventions: hover = subtle elevation/border/background shift (desktop only — never hover-only critical info, since touch/keyboard users miss it); pressed = inset/depressed shift; selected = clear marker (checkbox, border, accent fill, not color alone); **disabled = reduced opacity plus a reason** (tooltip or text explaining why and how to enable — a disabled button with no explanation is a dead end); loading = control-local busy state, never a full-screen spinner for a single mutation.

### A11. Dark mode
**Corroborated** as a preference, not a requirement: offer Light / Dark / System — never forced.
- Don't invert naively: use dark grays (e.g., #121212 family) rather than pure black, desaturate accent colors to avoid visual vibration, rebuild elevation with lighter surfaces rather than shadows, and re-verify all WCAG contrast ratios in both themes (poorly built dark mode can be less accessible than light).
- Thin fonts and low-contrast grays are the most common dark-mode failures; test in varied lighting.

### A12. Sticky headers, back-to-top, scroll progress
Sticky headers keep primary navigation/actions reachable on long pages — but must not obscure focused content (see A9) or eat the viewport on mobile. Back-to-top and scroll-progress indicators belong on long, scroll-heavy content (articles, docs, feeds); on short transactional screens they're clutter. Keep them subtle, reduced-motion aware, and out of the thumb zone on mobile.

### A13. Copy buttons with feedback
**Corroborated:** click → icon morphs to checkmark and/or label swaps to "Copied", reverts after ~2–2.5s. The label/icon change *is* the feedback — a toast on top of it is redundant (one source argues explicitly "no toast; the label change is the feedback"). Announce politely for screen readers; handle clipboard-permission denial with a fallback (select-the-text path).

### A14. Expandable FAQs
Accordions with proper semantics (button + `aria-expanded`, region association), one-or-many-open policy stated, deep-linkable anchors per question, chevron rotation + content reveal in ~200–280ms. Never use them to hide legally-required disclosures that users must see.

### A15. Confirmation dialogs
Reserve blocking dialogs for **irreversible, high-cost actions**. **Corroborated** severity pattern (reversibility × blast radius): reversible actions act immediately with undo; soft-deletable actions get act + undo toast + trash; irreversible actions get a confirmation dialog that names the consequence on the button ("Delete 3 files", never "OK"), with the destructive action visually distinct and **not** the default focus; catastrophic scope (account/workspace, affects others) gets type-to-confirm, re-authentication, or delayed execution with a cancel window. Destructive controls live in a separated "danger zone", away from routine settings. Anti-pattern: confirming every delete trains reflexive "OK" clicks (habituation), which is why undo is preferred where possible.

### A16. Last-updated timestamps
Show data freshness next to the data ("Updated 2m ago"), especially on dashboards and anything cached or polled. It's the cheapest trust signal in the product and the prerequisite for the stale-data state (§19).

### A17. Contextual support
Help at the moment of need beats upfront tours: contextual tooltips, inline links to relevant docs, and empty-state guidance outperform long welcome modals and carousels (which users skip). Keep nudges one-click dismissible, never modal. For agentic/AI flows, visible checkpoints where the user can review, approve, or cancel agent actions.

### A18. Form success states
Confirm with specificity — "Report saved to your dashboard", not "Done!" — and name what changed plus the next step. For major actions (purchase, submission) a full confirmation surface is appropriate; for micro-actions the inline acknowledgment suffices. See also §C.

### A19. Recoverable errors, retry, and error surfaces
Match the surface to the severity (**Corroborated** taxonomy): inline field errors for input problems; toasts/banners for transient failures with a retry action; modals for blocking errors with next steps; full-page for system outages with a status-page link. Every error message should carry (1) what happened in plain language, (2) why it matters (was data saved or lost?), (3) how to recover — never raw codes or stack traces in the UI (offer "Copy error details" for support instead). Auto-retry with exponential backoff (1s, 2s, 4s…) then hand control to the user; never auto-retry non-idempotent POSTs without an idempotency key (duplicate orders/charges risk).

### A20. Empty / partial / failed / stale data states
See §19 matrix. Key rules: partial failure shows what loaded, marks what didn't, and offers per-section retry (one broken widget must not blank the viewport); stale data gets a timestamp plus refresh control, never silent staleness; failed loads preserve user input/drafts.

### A21. Unsaved-change warnings
Warn on navigation/close only when there are genuinely unsaved changes (`beforeunload` gated on dirty state — warning unconditionally is itself an annoyance and browsers have restricted the custom message anyway). Per-document dirty indicators (VS Code's dirty dot + Explorer badge) scale the pattern to multi-document products. With autosave (§A7), the need for these warnings largely disappears — which is the point.

### A22. Session expiry
**Proposed** (practitioner consensus, no primary study): warn before expiry with a countdown and a one-click "Stay signed in" that extends the session; on actual expiry, preserve the user's in-progress work, redirect through re-authentication, and return them to where they were — never silently drop form state across a 401. For idle timeouts on sensitive products, the warning is a security requirement, not a nicety.

### A23. Cancellation / recovery paths
Every long or multi-step flow needs a way out that preserves dignity: cancel, back, save-draft-and-resume, and — where cancellation has side effects — a plain-language statement of what cancellation does and doesn't undo. (For subscription cancellation specifically, see §E legal notes.)

---

## B. Navigation / responsive completeness

### B1. No page-level horizontal scrolling
**Corroborated** as a hard rule: `html, body` never scroll horizontally; wide content (tables, code) scrolls inside its own `overflow-x: auto` container. Horizontal page scroll is consistently cited as the fastest way to make a product feel broken.

### B2. Mobile navigation
Bottom tab bar for the top 3–5 destinations (thumb-zone research supports this; one source cites hidden-menu task-completion drops of ~21% — **Proposed**, attributed to NN/g second-hand). Hamburger/drawer only for genuinely secondary items on marketing sites; hybrid tab-bar + drawer for content-heavy apps. Never hide critical actions behind menus. Modals become bottom sheets on phones.

### B3. Responsive tables
Tables don't shrink gracefully — pick per data type (**Corroborated**): reference/comparison data keeps horizontal scroll inside the table's own container with a sticky first column (don't reflow); record lists (orders, transactions) reflow into card stacks; dense/analytical data acknowledges tablet+ as the floor and shows a phone-friendly summary with a "View full data" link. Never squeeze columns; keep sticky headers; define column priority for narrow widths. Sortable columns show current sort state; filters show their state with one-click reset; bulk actions appear on selection.

### B4. Page titles & metadata
Unique `<title>` per page (~50–60 chars), unique meta descriptions (~120–160 chars) matching on-page content, canonical URLs, correct `lang`, viewport, and `theme-color`. Titles must match user intent when shared — no bait-and-switch.

### B5. Footer links & copyright
A complete footer: primary nav echoes, legal pages (privacy, terms, cookies), contact/support, status page link, and a current copyright notice. The footer is also where status-page and legal links must live so users can always find them (status-page discoverability is a documented best practice).

### B6. Custom 404s
**Corroborated** essentials: plain-language message ("We can't find this page" — no jargon, no blame), keep the full site header/footer navigation, add a search box, suggest likely destinations, return a real HTTP 404 (a 200 response is a "soft 404" that confuses search engines), keep it lightweight and accessible. Prevention first: 301 redirects for moved/renamed pages, regular internal-link audits, and never blanket-redirect all 404s to the homepage.

### B7. Clickable logo, click-to-call / click-to-email
Logo always links home. Phone numbers use `tel:` links and email addresses use `mailto:` — on mobile these are the difference between a contact detail and a contact action. **Inferred** as high-value, low-cost.

### B8. Internal navigation & link validity
Consistent nav placement on every page; breadcrumb or highlighted nav item always shows "you are here"; back-button behavior respected (never hijack browser history); deep links survive refresh (client-side routers must handle direct URL entry). External links validated — dead links and leftover placeholder links ("Lorem ipsum", "#" hrefs) are repeatedly cited as demo-vs-product tells.

### B9. Search / filter / sort / pagination
Search is a primary interaction for sites with more than ~50 pages or large datasets. Filters display their current state; empty search results are their own designed state (echo the query, suggest broadening, offer "Clear filters" — see A3). Pagination vs infinite scroll is a per-context choice; cursor-based pagination for large sets; never both competing on one surface.

### B10. Favicon & sharing previews
**Corroborated** checklist: real `favicon.ico` + SVG icon + 180×180 apple-touch-icon (a 6-byte placeholder or missing icon is a documented launch-QA failure); `theme-color`; Open Graph tags (`og:title`, `og:description`, `og:image` as an absolute URL at 1200×630, `og:url`, `og:type`, `og:site_name`) and Twitter/X card tags (`summary_large_image`); a fallback OG image so no page shares a broken-image icon. Verify with the platform debuggers (Facebook Sharing Debugger, X Card Validator, LinkedIn Post Inspector).

---

## C. Forms / input

### C1. Labels
Visible `<label>` above every input, always. **Verified** accessibility floor (WCAG 3.3.2 Labels or Instructions) and usability consensus: top-aligned labels scan fastest; placeholder-as-label fails on multiple counts (vanishes on input, fails contrast/size, breaks assistive tech). Size fields to the expected answer.

### C2. Required vs optional
Mark the minority explicitly and consistently — if most fields are required, mark the *optional* ones, and vice versa. Use the `required` attribute, not color or placeholder alone.

### C3. Inline + server validation
**Corroborated** timing consensus: validate on blur (after the user finishes the field), not on keystroke; once a field has been marked invalid, re-validate on change so the error clears the moment it's fixed. Validate on submit for everything, including what only the server can know. Keep client and server rules in one shared schema — drift between them produces errors the form promised wouldn't happen. Debounce async checks (~300–500ms) to cut server load. Live requirement checklists are the accepted exception for passwords.

### C4. Clear messages & accessible relationships
Error messages sit next to the field (below or inline), in plain, blameless, specific language: what happened + how to fix, one line, never truncated. Color + icon + text — never color alone (WCAG 1.4.1). Associate via `aria-describedby` and `aria-invalid="true"`; announce with `role="alert"`. On failed submit, move focus to the first error; for long forms add a summary at the top with links to each field.

### C5. Preserve valid input
**Verified** (WCAG 3.3.7 Redundant Entry at AA; also basic decency): never clear a form on submit failure — preserve everything, including what was invalid. Losing typed input is cited as the single worst thing a form can do.

### C6. Autosave, submission loading, duplicate prevention
Draft autosave for long or multi-step forms (localStorage + periodic backend sync, with a visible "Last saved" indicator). On submit: inline loading state on the button itself, button disabled during the request, and duplicate-submission prevention — one source flags never auto-retrying non-idempotent POSTs without an idempotency key (double-charge risk). Submit labels are action verbs ("Place order", "Create account"), never "Submit".

### C7. Success / failure feedback
All three button states designed: loading, clear success message, and polite, informative failure message. Mind security: don't reveal which credential was wrong on login failures. Server errors land in the same visual place as client errors — the user doesn't care which side rejected them.

### C8. Upload constraints, progress, cancellation, recovery
State constraints up front (accepted types, size limits, count limits); show per-file progress; allow cancel; offer retry on failure; confirm success. See A6 for the engineering pattern.

### C9. Destructive-action confirmation
See A15 — same severity framework applies inside forms (e.g., "Discard draft" with unsaved work gets the undo/confirm treatment; "Reset to defaults" is a destructive action).

---

## D. Performance / visual stability

### D1. Core Web Vitals — current authoritative guidance (Verified, web.dev, page last updated 2024-10-31, fetched 2026-10-10)
The current set is **LCP, INP, CLS** (INP replaced FID in March 2024), all measured at the **75th percentile** of page loads, segmented mobile vs desktop. A page passes when all three are "Good":

| Metric | Measures | Good | Needs improvement | Poor |
|---|---|---|---|---|
| LCP (Largest Contentful Paint) | Loading | ≤ 2.5 s | 2.5–4.0 s | > 4.0 s |
| INP (Interaction to Next Paint) | Interactivity | ≤ 200 ms | 200–500 ms | > 500 ms |
| CLS (Cumulative Layout Shift) | Visual stability | ≤ 0.1 | 0.1–0.25 | > 0.25 |

web.dev explicitly recommends sites set up their **own real-user monitoring** (via the `web-vitals` JS library) because CrUX alone lacks the per-pageview telemetry needed to diagnose and react to regressions. Lab tools (Lighthouse, DevTools) are for catching regressions pre-release, not a substitute for field data.

### D2. Images
Compress and serve modern formats (AVIF/WebP with fallbacks); responsive images via `srcset`/`sizes` with the `sizes` attribute specified correctly; eager-load + `fetchpriority="high"` only the true LCP image; lazy-load below-the-fold media — but **never lazy-load the LCP element** (documented audit failure).

### D3. Fonts
`font-display: swap` (or optional) with a metric-matched fallback to avoid invisible text and layout shift; subset and preload only critical fonts. Web-font-induced shift is a named above-the-fold audit flag.

### D4. Code splitting & caching
Split by route and by heavy below-fold components; defer non-critical CSS/JS; cache static assets aggressively with content-hashed filenames. Delivery decisions — not "slow code" — are where most CWV failures originate, per 2026 engineering guidance.

### D5. Layout-shift prevention
Reserve space for everything that loads late: explicit `width`/`height` or `aspect-ratio` on images, embeds, and ads; skeleton geometry matching final layout (§A4); no late-injected banners pushing content down after first paint. CLS ≤ 0.1 is the "good" threshold (§D1).

### D6. Performance budgets & RUM
Set per-template budgets (e.g., JS payload, image weight, LCP/INP/CLS at p75) and enforce them in CI; monitor real-user distributions continuously, not just lab scores. Budgets turn performance from a launch activity into a maintained property.

---

## E. Content / trust completeness

### Legal classification
Not everything in this section is required of every product. The research supports a three-tier classification:

**Tier 1 — Legally required (jurisdiction-dependent, get counsel):**
- **Privacy policy** — required whenever you collect personal information (names, emails, IP addresses, cookies), under GDPR (EU), CCPA/CPRA and state laws (US), and equivalents worldwide. **Corroborated.**
- **Cookie consent** — EU ePrivacy/GDPR requires *prior opt-in consent* for non-essential cookies (analytics, marketing, embeds); strictly-necessary cookies are exempt. Note: the UK changed PECR on 5 Feb 2026 to allow a simple opt-out for low-risk statistics/appearance cookies — that exception does **not** apply to EU visitors. Google Consent Mode v2 has been mandatory since March 2024 for sites using Google Ads/Analytics with EEA visitors. **Corroborated.**
- **Genuine reviews/testimonials** — the FTC's Rule on the Use of Consumer Reviews and Testimonials took effect **21 Oct 2024**: businesses may not create, buy, or disseminate fake reviews/testimonials (including AI-generated ones), condition incentives on sentiment, use undisclosed insider reviews, or suppress honest negative reviews; civil penalties up to ~$51.7k per violation at issuance (later inflation-adjusted figures ~$53k reported in 2025–26). The UK's DMCC Act separately outlaws fake reviews. **Corroborated.**
- **AI transparency** — EU AI Act Article 50 transparency obligations took effect **2 Aug 2026**: users must be told when interacting with AI; providers must machine-mark synthetic content; deployers must disclose deepfakes and AI-generated text published on matters of public interest — in a clear, distinguishable, accessible manner at first exposure. Fines up to €15M or 3% of global turnover. **Corroborated.**
- **E-commerce disclosures** — EU Consumer Rights Directive requires pre-purchase disclosure of price, returns, cancellation, and delivery terms. **Corroborated.**

**Tier 2 — Platform / contractual (required by the rules of the channel you're on):**
- App-store listing requirements, ad-platform policies (Google/Meta ad disclosures), payment-processor terms (Stripe etc. require refund/dispute policies), and consent-signal frameworks like Google Consent Mode v2 and IAB TCF where applicable. These are not law, but violating them removes your distribution or your money flow. **Inferred** as a category from multiple sources.

**Tier 3 — Trust-building (not legally required, but absence costs conversions and retention):**
- Honest pricing (no drip pricing / junk fees — note the FTC has pursued junk-fee enforcement even as specific rules shifted), accurate claims, real screenshots that match the implementation, named company identity with real contact/support info, public status page with incident history, transparent AI limitations (what the AI can't do, where humans take over), published data-retention and deletion flows, and clear refund/cancellation/data-deletion paths.
- **Subscription cancellation UX note:** the FTC's 2024 "click-to-cancel" Negative Option Rule (cancel as easy as signup) was **vacated by the Eighth Circuit in July 2025** on procedural grounds; the FTC signaled a new rulemaking proposal in Jan 2026. Meanwhile ROSCA, FTC Act Section 5, and state auto-renewal laws impose substantially similar disclosure-and-easy-cancellation duties — so easy, same-channel cancellation remains the required posture in practice even without the federal rule. **Corroborated.**

### E-item notes
- **Testimonials:** only genuine, verifiable customers; disclose any material connection or compensation (FTC Endorsement Guides); never invent logos, metrics, or quotes. Fabricated social proof is simultaneously a trust-killer and — since Oct 2024 in the US — a regulatory violation.
- **Screenshots:** must match the shipped implementation; a marketing screenshot of a feature that doesn't exist is the visual form of a fake demo (§20).
- **Pricing:** all-in pricing visible before commitment; trial/renewal terms disclosed at enrollment, not in fine print.
- **AI limitations:** disclose AI involvement, error modes, data usage for training, and the path to a human. Since Aug 2026 this is partly Tier 1 in the EU.
- **Contact/support:** a real, reachable support path; "Contact us" that goes nowhere is a documented fraud signal.
- **Status communication:** public status page (linked from the footer), incident updates every 15–30 minutes during outages, plain language, impact-first, conservative ETAs, post-incident summaries. Atlassian's Statuspage guidance: communicate early, often, precisely, consistently across channels, and own the problem.
- **Data deletion & retention:** a self-serve deletion path where feasible; published retention periods; honor access/correction/deletion requests per applicable privacy law.

---

## Cross-cutting notes

- **Accessibility is not a polish item** — focus visibility, labels, live regions, and contrast are legal-grade requirements (WCAG AA is the referenced standard in the EU Accessibility Act, ADA practice, and procurement). They appear throughout A–D above rather than in a separate section.
- **Consistency rule:** one primary action per view; one toast at a time (queue the rest); one pattern per state across the product. Inconsistency between screens is itself a completeness defect.
- **Counter-patterns to watch:** skeletons that don't match final layout (layout jump); toasts that auto-dismiss before screen-reader users can reach them; confirmation dialogs on reversible actions (habituation); disabled buttons with no reason given; "saved" claims for non-durable storage; 200-status 404 pages; OG images that don't exist.

*Evidence register: `04-evidence-register.md`. State matrix: `02-ux-state-matrix.md`. Demo checklist: `03-demo-authenticity.md`.*
