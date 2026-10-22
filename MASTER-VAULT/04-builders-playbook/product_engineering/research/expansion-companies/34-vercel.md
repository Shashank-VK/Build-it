# Vercel — product engineering case study (framework-defined infrastructure + the App Router reckoning)

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Vercel is the deployment-platform exemplar: **framework-defined infrastructure** (the framework declares infra needs; the platform provisions it), **preview deployments per PR**, and instant rollbacks. It's also the case study in *framework stewardship failure*: the Next.js App Router launch — declared stable before it was ready, admitted by Vercel's own VP of Engineering. Both halves are documented below.

## 1. Forensic reconstruction — how the machine actually works

### Framework-defined infrastructure (FDI)
- Claim: Vercel's core idea is **framework-defined infrastructure**: the framework (Next.js) declares what it needs (routes, ISR/edge caching rules, functions, middleware) and the platform builds the infrastructure from those declarations — developers don't configure CDN, functions, or cache headers directly. Label: **Corroborated** — vercel.com resources; focusreactive overview; rczamor's Vercel-docs corpus (GitHub). Confidence: high on the concept; medium on internals.
- Claim: **Preview deployments per PR** — every pull request gets a production-like URL — plus **instant rollbacks** and **ISR (Incremental Static Regeneration)/edge caching**. Label: **Corroborated** (same sources). The forensic point: preview-per-PR collapses the "works on my machine" gap and makes design review deployable — it's as much a *collaboration* feature as an infra one.

### The Next.js stewardship machine
- Claim: Vercel *is* the Next.js steward (employs the core team; the framework is the platform's moat). This vertical integration — framework + platform + edge network — is the business model: the framework's conventions (App Router, Server Components, caching) drive platform usage. Label: **Corroborated** (widely documented; the FDI model implies it). Engineering implication: framework design decisions are *also* infrastructure business decisions — a conflict the App Router story makes visible.

## 2. Postmortem record — the App Router reckoning
- **What happened:** Next.js 13 (2022) introduced the **App Router** (React Server Components, new data-fetching/caching model) and Vercel made it the default. Developers hit: aggressive default caching (fetch cached unless opted out — dashboards showing yesterday's data), the `"use client"`/`"use server"` boundary confusion (build failures, secrets leaking into client bundles), Server Actions' rough edges, dev/prod behavior divergence, and migration pain (14→15). The HN threads ("It's not just you, Next.js is getting harder to use"; "Why has there been a recent surge in criticism toward Next.js?") document sustained practitioner frustration. Label: **Corroborated** — HN items 40828610, 43882337; dev.to migration postmortems; medium retrospectives. Confidence: high on the complaint pattern.
- **The admission (the rarest artifact in this file):** **Tom Occhino, Vercel's VP of Engineering (Frameworks)**, told The New Stack: *"[App] Router was a Next.js rewrite, and it wasn't really finished yet when the team made it available"* — and that making it the default early was a mistake: *"it wasn't really ready yet for us to switch the default… in retrospect, it might have been better to delay until the app router was 'unequivocally better' than Page Router."* He added the team "underplayed just how different it really was from Pages Router." Label: **Verified** — thenewstack.io interview. Confidence: high. This is a primary-source self-postmortem from the executive owner.
- **The correction:** Next.js 15 flipped caching defaults (fetch fresh unless told to cache — "stopped trying to be smarter than the browser"), stabilized Server Actions, and made Turbopack the default dev server. Practitioners report the framework "grew up" by 2026. Label: **Corroborated** — medium/@frankdotdev (Jan 2026); dev.to migration guides. Confidence: medium-high.

## 3. Narrative audit — dismantling with receipts
- **"Framework-defined infrastructure" vs. who defines the framework.** The elegant story: the framework declares needs, the platform serves them. The receipts (App Router): the framework is *also the platform vendor's product*, so "framework-defined" can mean "vendor-defined" — caching defaults that made Vercel's edge story shine created dashboard-staleness bugs for users. The dismantling: FDI is genuinely good architecture *and* a lock-in vector; the framework's conventions are the platform's moat wearing a developer-experience costume. Evaluate every framework default for whose interests it serves. Label: **Inferred** (audit synthesis) on **Corroborated** facts.
- **The default-switch as the original sin.** Occhino's admission pinpoints the failure precisely: not the rewrite (rewrites can be fine — see the Vista file's nuance) but **switching the default before it was "unequivocally better."** Defaults are the most powerful product decision in a framework — they define what millions of developers get without choosing. The transferable rule: new architectures ship as *opt-in* until they're unambiguously better than the old default; the team that built it is the least qualified to judge readiness (they "underplayed just how different it really was" — the curse of knowledge, confessed). Label: **Inferred** on **Verified** admission.
- **Caching defaults as a case study in "smart" vs. predictable.** Next.js 13/14 "cache everything unless told otherwise" vs. 15's "fetch fresh unless told to cache" (web-standard behavior). The audit: the framework tried to be *smarter than the browser* and lost to the principle of least surprise. "Smart defaults" that surprise are bugs with good intentions. The correction's framing ("stopped trying to be smarter than the browser") is the lesson, stated by a practitioner. Label: **Inferred** on **Corroborated** accounts.
- **Preview-per-PR: credit where due.** Amid the audit, the preview-deployment model is genuinely excellent and widely copied — it changed what "review" means (review the *running thing*, not the diff). The dismantling doesn't touch this; it's the durable contribution. Label: **Corroborated**.
- **Negative evidence:** no evidence was found of a Vercel *platform* outage at the Atlassian/Cloudflare scale in the fetched material — the failures are framework-stewardship failures, not infrastructure ones. The platform's reliability record is the quiet success here.

## Transferable lessons
1. **Never switch the default until the new thing is "unequivocally better."** (Occhino's own standard.) New architectures ship opt-in; defaults are earned.
2. **The team that built it can't judge its readiness.** "Underplayed how different it was" is the curse of knowledge — require external beta evidence before default-switching.
3. **Smart defaults must not surprise.** When the framework is smarter than the platform conventions (browser caching), developers debug the framework instead of their app. Prefer least surprise.
4. **Preview-per-PR changes review itself.** Review running deployments, not diffs — collapse the environment gap and the collaboration gap together.
5. **Framework defaults are business decisions.** When the framework vendor is the platform vendor, audit every default for whose interests it serves.

## Sources
| ID | Claim | URL (verbatim) | Type | Author/Org | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| VC1 | FDI; preview deployments; ISR/edge; rollbacks | https://vercel.com/resources/simplify-your-kubernetes-frontend-deployment-with-vercel | Primary (vendor) | Vercel | n.d. | 2026-10-10 | Medium (vendor) |
| VC2 | Vercel platform overview | https://focusreactive.com/what-is-vercel/ | Secondary | focusreactive | n.d. | 2026-10-10 | Low-medium |
| VC3 | Vercel docs corpus (GitHub) | https://github.com/rczamor/rz-agent-team/blob/HEAD/corpus/devops-eng/vercel-docs-lee-robinson.md | Community (GitHub) | rczamor | n.d. | 2026-10-10 | Low-medium |
| VC4 | Occhino admission: App Router "wasn't really finished," default switched too early | https://thenewstack.io/why-developers-should-give-next-js-app-router-another-chance/ | Primary (exec interview) | The New Stack | ~2024 | 2026-10-10 | High |
| VC5 | App Router criticism surge; practitioner pain (caching, use-client, env vars) | https://news.ycombinator.com/item?id=43882337 | Community observations | Hacker News | ~2025 | 2026-10-10 | Medium |
| VC6 | "Getting harder to use": dev/prod divergence, auth caching footguns, ecosystem limbo | https://news.ycombinator.com/item?id=40828610 | Community observations | Hacker News | 2024 | 2026-10-10 | Medium |
| VC7 | Next.js 15: caching flip, Server Actions mature, "stopped fighting me" | https://medium.com/@frankdotdev/next-js-15-the-app-router-finally-stopped-fighting-me-bde8847181e0 | Practitioner | frankdotdev (Medium) | Jan 2026 | 2026-10-10 | Medium |
| VC8 | Migration breakages: getServerSideProps, use-client boundaries, server-only leaks | https://dev.to/abubakarfarooq/what-broke-when-i-moved-client-projects-to-the-nextjs-app-router-4g3d | Practitioner | dev.to | ~2026 | 2026-10-10 | Medium |

**Gaps:** Vercel platform outage history (not found — absence noted, not proven); ISR/edge internals (Unknown); Turbopack development history (mentioned, not deep-dived).
