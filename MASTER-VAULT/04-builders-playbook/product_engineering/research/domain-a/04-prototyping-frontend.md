# Domain A — Area 4: Prototyping and Frontend Generation (AI-assisted)

*How AI generates working frontend prototypes and full-stack starter apps from prompts — AI used in the process of building the product's interface and scaffolding.*

> Read-only research. No installation, ranking, or recommendations. Accessed 2026-10-10 unless noted.

## 1. What teams demonstrably do

### Head-to-head: what each builder actually produces
- **Claim (Corroborated):** Independent testers building the *same* SaaS dashboard (auth, dashboard stats, project CRUD, team management, settings) on four AI builders measured: time-to-first-render (v0 30s, Bolt 2min, Lovable 3min, Forge 2min), time to working auth (Bolt 5min, Lovable 8min, Forge 5min; v0 N/A — no backend), lines of code (400–2,100), design scores (v0 9/10, Bolt 5/10, Lovable 8/10, Forge 8/10), code cleanliness (v0 9, Bolt 5, Lovable 8, Forge 9).
- Source: https://designrevision.com/blog/forge-vs-bolt-vs-lovable-vs-v0-comparison (DesignRevision; evidence class: first-hand practitioner test; ~Dec 2025)

### Tool roles (convergent across roundups)
- **v0 (Vercel):** cleanest component code — proper TypeScript types, shadcn/ui conventions, minimal cleanup before merging into a production codebase. Scope is narrow: components/UI only; no databases, auth flows, or backend logic out of the box (needs Supabase/Neon/own API layer). **Corroborated.**
- **Bolt (StackBlitz):** real Node.js in the browser via WebContainers — scaffolds, installs deps, runs dev server, live preview. Broadest framework support (React, Vue, Svelte, vanilla; Angular experimental); only one of the three with React Native/Expo. Output is a real project (zip export), not a snippet. **Corroborated.**
- **Lovable:** full-stack app via chat with tightest Supabase integration and easiest deployment; generates more code with more variability; components sometimes need cleanup; gates full codebase download to paid plans but offers genuine two-way Git sync. **Corroborated.**
- **Concrete mechanism difference:** Bolt is a real dev environment (runs code), the others are generators with deployment integrations. **Verified from architecture descriptions.**

### The security gap in generated apps — quantified
- **Claim (Corroborated, high concern):** Independent 2026 testing found all three major builders ship code with a **40–45% vulnerability rate** (missing input validation, exposed API keys, SQL injection risk). Pattern: "great at making things work, bad at making things safe." Default Supabase configs from Lovable often skip row-level security on certain tables; Bolt-generated APIs sometimes lack rate limiting; v0 forms often don't sanitize input.
- **Practitioner prescription:** budget 20–30% of build time for a security review before any AI-generated app reaches real users.
- Source: https://publorai.com/lovable-vs-bolt-vs-v0/ (PublorAI; evidence class: first-hand practitioner; ~Sep 2026)
- **Convergent larger study:** Symbiotic Security's "State of Cyber" lab analyzed 1,072 vibe-coded apps across five platforms: 98% had ≥1 vulnerability, 29% high/critical, 16% allowed a stranger to delete/change data with no login. See file 07 for detail. **Corroborated.**

### The multi-tenant SaaS "30% you still write yourself"
- **Claim (Corroborated):** A practitioner building governed multi-tenant SaaS on top of generated apps reports the durable split: builders win on visual quality, speed of first result, and iteration feel; the team still hand-writes the governed backend (authz, tenancy, adversarially tested code) the generated app runs on top of. Generated apps are the presentation layer; the trust layer is human-written.
- Source: https://dev.to/supero/ai-app-builders-and-multi-tenant-saas-the-30-you-still-write-yourself-2clg (dev.to; evidence class: first-hand practitioner; Oct 2026)

## 2. Tools and workflows
| Tool | Output | Ownership/portability |
|---|---|---|
| v0 | React/Next.js components, shadcn/ui | Clean code, merges into existing repos |
| Bolt.new | Full-stack Node projects in-browser | Zip export; two-way GitHub sync; Bolt's copy wins edit conflicts |
| Lovable | Full-stack React + Supabase apps | Two-way Git sync (GitHub/GitLab/Bitbucket); full download gated to paid |
| Base44 | All-in-one (DB, logins, workflows, hosting) | True all-in-one vs Lovable's external Supabase |
| Figma Make | Prompt → interactive code-backed prototype | Publishing still in beta; different handoff path than Dev Mode |

**Typical workflow:** prompt → iterate in chat (tight prompt-see-adjust loop) → export/sync to Git → human security + architecture review → rebuild the trust layer by hand.

## 3. Failure modes
1. **Insecure defaults.** 40–45% vulnerability rate in generated code; missing RLS, rate limiting, input sanitization. **Corroborated.**
2. **Credit burn on iteration.** Users report burning 60–150 credits on a single layout issue ($10–$25 unplanned/month on Pro); heavy users exhaust monthly allocation in 2–3 days. **First-hand reports.**
3. **Backend inflexibility.** Limited integrations, minimal backend automation, few enterprise security features — unsuitable for large-scale production systems per multiple roundups. **Corroborated.**
4. **"Works" ≠ "correct".** Full-stack generation introduces more variables: DB queries needing optimization, fragile API error handling. **Corroborated.**
5. **Lock-in asymmetries.** Export/sync terms differ per tool (read each tool's terms); some gate full download to paid tiers. **Verified from tool docs as reported.**

## 4. Costs / latency / reliability
- Entry pricing ~$20–25/month; heavy use burns allocation in days. Bolt's free tier is the most generous (1M free tokens/month reported). **Corroborated.**
- Generation latency: 30 seconds (components) to ~35 minutes (full app). **Measured in head-to-head test.**
- Reliability: fine for prototypes/MVPs; production-grade use requires the 20–30% security-review budget. **Corroborated.**

## 5. Human correction burden
- The correction burden is *architectural*, not just line-level: the team re-builds authz/tenancy/validation by hand while keeping the generated UI. Per-file cleanup is lightest with v0, heaviest with the broadest generators. **Corroborated.**

## 6. Where AI genuinely helps vs where it creates rework
- **Genuinely helps:** speed to first visible result (seconds); stakeholder demos; UI component code clean enough to merge (v0); scaffolding full-stack MVPs for validation.
- **Creates rework:** insecure defaults that must be audited; messy generated code (Bolt scored 5/10 cleanliness) that must be restructured; backend logic that must be rewritten against real requirements.

## 7. Boundary notes (A vs B vs C)
- **Domain A:** using these builders to prototype *your* product. **Domain B:** the builder product itself (Lovable, v0 as SaaS products with AI features) — and any AI feature *inside* what you ship (e.g., your app's "AI assistant" for end users). **Domain C:** using a generated app to run business operations (e.g., an AI-built internal CRM) — the *use* is C, the *building* was A. Note the blur explicitly when a source mixes "AI app builder" (B-product) with "built with AI" (A-process).

## Evidence register (this file)
| # | Claim | URL | Source type | Author/org | Pub date | Confidence | Class |
|---|---|---|---|---|---|---|---|
| 4.1 | Same-app head-to-head metrics (time, LOC, design/cleanliness scores) | https://designrevision.com/blog/forge-vs-bolt-vs-lovable-vs-v0-comparison | Practitioner test | DesignRevision | ~Dec 2025 | Medium | first-hand practitioner |
| 4.2 | Architecture differences (Bolt = real env via WebContainers; Lovable = Supabase project model; v0 = components) | https://anuragwagh.com/blog/lovable-vs-bolt-vs-v0-ai-app-builder-comparison | Roundup | Anurag Wagh | ~Jul 2026 | Medium | corroborating |
| 4.3 | 40–45% vulnerability rate; insecure defaults per tool; 20–30% security-review budget | https://publorai.com/lovable-vs-bolt-vs-v0/ | Practitioner test | PublorAI | ~Sep 2026 | Medium | first-hand practitioner |
| 4.4 | Governed-backend split: generated presentation layer over hand-written trust layer | https://dev.to/supero/ai-app-builders-and-multi-tenant-saas-the-30-you-still-write-yourself-2clg | Practitioner essay | supero (dev.to) | Oct 2026 | Medium | first-hand practitioner |
| 4.5 | Enterprise limitations: integrations, backend automation, security features | https://blog.tooljet.com/lovable-vs-bolt-vs-v0/ | Vendor-adjacent blog | ToolJet | ~Mar 2026 | Low–Medium | secondary interpretation |
| 4.6 | Export/sync terms per tool; Bolt two-way GitHub sync semantics | https://dev.to/supero/ai-app-builders-and-multi-tenant-saas-the-30-you-still-write-yourself-2clg | Practitioner essay | supero (dev.to) | Oct 2026 | Medium | first-hand practitioner |
