# 08 — Functional Completeness & Demo Honesty

*How teams systematically discover missing functionality in a product, and how to judge whether a demo represents the product. Synthesised from the quality stream (§21 route-by-route audit) and the ux-states stream (§20 demo authenticity). Claim labels — **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown** — are preserved; nothing upgraded.*

---

## 1. The closed-inventory principle

**Plain English:** a functional audit begins with a closed list of everything the product contains. Anything not on the list is not tested — so the first deliverable of an audit is the list itself, not the test results.

For each inventory item the audit records four fields:

| Field | Meaning |
|---|---|
| **Expected behaviour** | What the spec/design says the item must do (observable outcome, not implementation) |
| **Implemented behaviour** | What was actually observed when exercised (pass, fail, or partial — with the exact observed result) |
| **Verification method** | How the check was performed (which tool/manual step, on which build, at which route) |
| **Severity if broken** | What happens to users/revenue/legal standing when it fails |

## 2. The 16-class inventory

The research's recommended minimum inventory — 16 element classes every web product audit must enumerate (methods: **Proposed** synthesis of crawler/QA practice unless labeled otherwise):

| # | Class | What "expected" means | How it's verified | Severity if broken |
|---|---|---|---|---|
| 1 | **Routes / pages** | Every route in the routing table renders its intended page; no dead routes; no junk routes returning 200 | Extract the route manifest from code; crawl seeded from `sitemap.xml`; diff crawled URLs vs manifest; log 4xx/5xx | **S1** if a core-flow route 404s/500s |
| 2 | **Navigation links** | Every link navigates correctly, label matches destination, no link to a retired URL | Crawl + HTTP-check every `<a href>`; classify OK / redirect-chain / broken / error; >2-hop chains flagged (**Corroborated**) | **S2** broken primary nav |
| 3 | **Buttons** | Every button does something observable — never a visual dead end | Enumerate interactive nodes from the accessibility tree; click each; assert an observable change (URL, DOM, network, dialog); flag `<div onclick>` impostors | **S1** dead primary CTA |
| 4 | **Forms** | Visible associated labels; required/optional communicated; errors announced and recoverable; confirmation or clear error on submit; no data loss | axe-core flags missing labels (**Verified** — axe rule set); manual: submit empty/invalid/valid; check focus movement to error summary | **S1** if the form loses user data |
| 5 | **Modals / dialogs** | Open on trigger; trap focus while open; close on Escape/close/backdrop; return focus to trigger; accessible name + role | Keyboard-only open/close cycle; WAI-ARIA Authoring Practices dialog pattern as reference (**Verified** — W3C living document) | **S1** for a focus trap stranding keyboard users |
| 6 | **Menus** | Open/close via mouse, touch, keyboard; arrow-key navigation where the pattern calls for it; dismiss on Escape/outside click | Scripted keyboard walk-through against APG menu patterns (**Inferred** from APG coverage — mostly manual) | **S2** if keyboard users can't reach items |
| 7 | **Upload controls** | Type/size accepted/rejected with clear messaging; progress shown; mid-upload network failure handled; never silently drops a file | e2e with fixture files per type/size class, including an oversized file and a mid-upload abort (**Proposed** — standard technique) | **S2** for silent data loss |
| 8 | **Search & filtering** | Relevant results; empty sets explain themselves; filters combine correctly; pagination/sorting preserve filter state | Seeded-data matrix (known corpus, expected result sets); test the zero-result state explicitly (**Proposed**) | **S2** for filters silently dropping criteria |
| 9 | **Auth flows** | Sign-up, login, logout, password reset, session expiry, MFA all complete; sessions actually invalidate server-side on logout | Scripted credentialed e2e (crawlers can't log in — **Verified** crawler limitation); time-travel/short-lived tokens for expiry | **S1** for broken login/reset or session-invalidation failure |
| 10 | **Payment flows** | Full path completes in test mode; failures (declined card, 3-D Secure, timeout) recoverable; no double-charge on retry; amounts displayed = amounts charged | Gateway sandbox/test cards; idempotency-key check on retry; never against production (**Proposed**) | **S1** for charge/display mismatch or double-charge |
| 11 | **Integrations** | Each third-party degrades gracefully when slow or down; failures logged and surfaced, never silent | Fault-inject the third party in test (timeout, 500, malformed payload); verify fallback UI (**Proposed**) | **S1** if a vendor outage kills a core flow with no fallback |
| 12 | **Keyboard interactions** | Every interactive element reachable and operable; visible focus; no traps; logical tab order | Manual keyboard walk-through of every flow — "the single cheapest high-yield manual test" (**Corroborated**); no tool fully verifies order or trap-freedom | **S1** for traps or unreachable core controls |
| 13 | **Responsive behaviours** | At each breakpoint: no horizontal overflow, no overlapping hit targets, no clipped text, tap targets ≥ minimum | Viewport sweep: assert `scrollWidth ≤ innerWidth`, screenshot each width; visual regression for layout shifts | **S2** for unusable mobile layout on a core flow |
| 14 | **Empty / error states** | Every list/search/data view has a designed empty state; every failure mode shows a human-readable, recoverable message — never a blank page or raw stack trace | Fault injection (offline, forced 500s) + seeded empty datasets; screenshot each state. These are the states most often never designed or tested (**Corroborated** as recurring practitioner complaint) | **S2** for blank/500-exposing states on core flows |
| 15 | **External links** | Correct destination; clearly signals leaving the product; no link to compromised/parked domains | Same crawl as #2, plus periodic re-checks on a schedule — link rot is time-dependent (**Proposed**) | **S1** if a payment/support link points at a hijacked domain |
| 16 | **Destructive actions** | Explicit confirmation naming what will be destroyed; undo/recovery where promised; idempotent (double-click ≠ double-delete) | e2e double-submit test; verify confirmation copy and post-action state (**Proposed**) | **S1** for unconfirmed irreversible destruction |

## 3. The severity framework (Proposed, aligned with common QA practice)

| Level | Meaning | Release consequence |
|---|---|---|
| **S1 — Blocker** | Core task impossible (checkout, login, payment); or legal/compliance failure | Blocks release |
| **S2 — Critical** | Major function degraded or inaccessible to a user group; workaround painful | Must fix before release unless formally excepted |
| **S3 — Major** | Feature impaired but usable with effort; visual/content defect on a high-traffic surface | Fix on a tracked timeline |
| **S4 — Minor** | Cosmetic, edge-case, or low-traffic surface | Backlog |

## 4. Automated detection — methods and their hard limits

Automation clears the high-volume, low-judgment defects cheaply. The table below records both what each method proves and what it structurally cannot prove:

| Defect class | Automated method | What it reliably proves | What it cannot prove |
|---|---|---|---|
| Broken links | Full-site crawl; HEAD/GET every href/src | The URL resolves and returns non-error status | Whether the destination is *correct* |
| Dead buttons | a11y-tree enumeration + click each; assert observable change | A click produces *some* observable effect | That the effect is the *right* one |
| Missing routes | Diff route manifest vs crawled URL set | Coverage of declared routes | Orphan pages never linked (without the manifest) |
| JS errors | Console/pageerror listeners during crawl and e2e | An exception fired on exercised paths | Silent logic errors (no signal) |
| Failed requests | Intercept/log network traffic; flag 4xx/5xx/timeouts | Requests failed | Whether the UI handled the failure well |
| Inaccessible controls | axe-core per page/state | Machine-detectable violations | The `incomplete` ("needs review") bucket — the tool's own admission of limits |
| Visual regressions | Baseline screenshot comparison per page/state/breakpoint | Pixels changed beyond threshold | Whether the change is a *bug* or an *intended redesign* — every diff needs human review |
| Mobile overflow | Viewport sweep asserting no horizontal scroll | Mechanical overflow, undersized targets | Whether the layout is *usable* |

**What automation cannot prove — the human/e2e remainder** (the most important part of the methodology; **Corroborated** across Deque's coverage analysis, W3C WAI guidance, and practitioner sources):

1. Whether alt text is *meaningful* ("image123" passes the machine check).
2. Whether reading and focus order is logical.
3. Whether custom widgets are actually usable with assistive technology (ARIA can be present and wrong).
4. Whether captions/transcripts are accurate.
5. Whether error messages are genuinely helpful and recoverable.
6. Whether a visual change is a bug or an intended redesign.
7. Whether empty/error/loading states are humane.
8. Whether a multi-step flow works for a real user (crawlers can't log in; only realistic data, timing, and behaviour expose race conditions).
9. Whether content is understandable — plain language, consistent terminology, predictable behaviour.
10. Whether the product is operable under realistic constraints: slow networks, small screens, zoomed text, assistive tech, third-party outages.

**The agent "done" caveat:** an AI agent's green check is weaker evidence than a human's. LLM-generated tests reproduce the anti-patterns in their training data — including tests that pass without asserting anything — and the "iterate until green" loop pushes toward weakening assertions to vacuity rather than fixing code (arXiv:2410.10628 — **Corroborated**). A passing suite written or iterated by an agent must be audited for assertion strength before it counts as evidence.

## 5. Coverage numbers to calibrate expectations

- **Deque's analysis** of 2,000+ audits / ~300,000 issues: automation covered **~57% of accessibility issues by volume** — but only of the issues its rules could identify; it did not measure whether disabled users could complete tasks (**Corroborated**).
- **By share of WCAG success criteria** a tool can even evaluate, the machine-decidable portion is closer to **30–40%** (**Corroborated**); one analysis puts reliably auto-flaggable WCAG 2.1 AA criteria at ~13% (single-source — treat as **Inferred/uncertain**, methodology unclear).
- **WebAIM Million 2026** (Feb 2026 crawl): detectable WCAG 2 failures on **95.9% of home pages**, averaging **56.1 errors per page**; the six most common failure types (low contrast, missing alt, missing form labels, empty links, empty buttons, missing document language) account for ~96% of detected errors — exactly the failures scanners catch reliably (**Verified** via WebAIM reporting).

**Implication:** automation clears the cheap defects; budget the human pass for the remainder — roughly half the defects by any counting method.

## 6. The demo-authenticity checklist (condensed)

*Purpose:* judge whether a demo — live, recorded, walkthrough, or sandbox — accurately represents the product. Demo ≠ product is normal and often legitimate; *undisclosed* divergence is the problem. Score each category **Pass / Fail / N/A**. The operative question per item: **"Would knowing this change the evaluator's decision?"**

| # | Category | Pass criteria | Fail signal |
|---|---|---|---|
| 1 | **The demo runs the product** | Actions execute real code paths; failure is demonstrated (error states, retry, offline, bad input) | Clickable mockup, video masquerade, or Wizard-of-Oz behind the curtain undisclosed; every input produces suspiciously perfect output; "we can't show that part live" |
| 2 | **The data is honest** | Sample data realistic (messy, edge cases); mock data disclosed *in the demo*; performance claims measured (hardware, network, data volume, percentile stated) | Round numbers and perfect trends; alliterative/joke "customer" names; "loads instantly" on a warm local build with 10 rows |
| 3 | **Simulated vs real is labeled** | Human-in-the-loop steps disclosed where automation would be assumed; alpha/beta status plain; roadmap items labeled "planned," never present-tense as shipped | Present-tense feature lists for unbuilt features; "coming soon" with no date and no progress signal |
| 4 | **Onboarding, trials, sandboxes are real** | Interactive onboarding with real buttons and working sample data; demo accounts provision a working environment without a sales call; sandbox limits (rate limits, resets) stated up front | A tour that *pretends* to be interactive; no way to test anything before sign-in |
| 5 | **Social proof is genuine** | Customer logos are actual customers (with permission); testimonials from real, verifiable people; metrics measured and defined (what counts as a "user"? over what window?) | Stock-photo "customers"; unverifiable identities; uniform 5-star distributions; review counts absent from the cited platform. *Legal floor:* the FTC's fake-review rule (effective 21 Oct 2024 — **Corroborated**) |
| 6 | **Planned vs available is explicit** | Maintained distinction between available now / in beta (with access criteria) / planned (with horizon or "no date committed"); changelog consistent with what's demoed; demo pricing matches the pricing page | A feature demoed but absent from every release note; hidden tiers |
| 7 | **AI-specific honesty** | AI limitations stated (what it can't do, error modes, human review points, training-data use); the *demo path* (curated prompt, clean data, no guardrails) distinguished from the *production path* (input cleaning, hallucination checks, abuse detection, cost/latency budgets) | Implying a prototype's economics work at scale; silent on token cost, latency under load, abuse handling. *EU legal floor:* AI Act Art. 50 transparency duties effective 2 Aug 2026 (**Corroborated**) |
| 8 | **The boring completeness signals** | Real favicon; working footer links; no lorem ipsum; no dead "#" links; loading/empty/error states exist; works at phone width; reachable support path; published company identity | Happy-path-only demo; presenter-laptop-only viewport |

**Scoring:** *Authentic* — all applicable items pass, simulations disclosed, failures demonstrated. *Conditionally authentic* — minor gaps that don't affect a purchase/adoption decision. *Not authentic* — any fail in categories 1, 2, 5, or 6; these change decisions. Treat "we'll show you after the contract" for core functionality as a fail; evaluators are advised to demand production pilots over demos for anything load-bearing.

**Cautionary cases (factual, brief):** Ovation (1983) — announced software, showed a fake demo to raise funding; the software never existed (NYT via Built In — **Corroborated**). Magic Leap (reported 2016) — promotional demos allegedly overstated technological progress while years behind schedule (The Information via The Verge — **Corroborated**). Fake AI storefronts (2026) — a ~$249 toolkit enabled 100+ professional-looking AI-service sites with billing and Google sign-in; SSL, polished design, and familiar auth buttons are no longer trust signals (DeafNews dossier — **Corroborated**). Startup "façading" (academic, 2026) — Imperial/Emlyon research models the escalation from exaggerated metrics → falsified documents → fully staged demos under investor pressure (Innovation Village summary — **Corroborated**). On-stage demos generally — even legitimate companies rehearse heavily and fudge timing; rehearsal is normal; *concealment of material divergence* is the line (**Corroborated**).

## Sources

- Full evidence: `research/quality/01-functional-audit.md`, `research/ux-states/03-demo-authenticity.md`, plus evidence registers `research/quality/04-evidence-register.md` and `research/ux-states/04-evidence-register.md`.
- Legal spine: FTC Rule on the Use of Consumer Reviews and Testimonials, 16 CFR Part 465 (effective 21 Oct 2024); EU AI Act Art. 50 (transparency duties effective 2 Aug 2026).
- Related report sections: §07 (fake social proof in the anti-slop catalogue), §09 (the UX state matrix that categories 1 and 8 reference; block-release rules), §12 (Moffatt v. Air Canada — demo claims as legal statements).
