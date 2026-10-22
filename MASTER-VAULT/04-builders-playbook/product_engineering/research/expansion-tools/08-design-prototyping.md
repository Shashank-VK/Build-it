# §30 — Design, Prototyping & Front-End Generation (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## DS-01 — Figma — ACTIVE (post-IPO, post-Adobe-deal, CONTROVERSIAL on trust/AI)
- Purpose / problem: Browser-based collaborative product design + prototyping + design systems; now expanding into a full "idea → product" platform (Design, FigJam, Dev Mode, Slides, Draw, Make, Sites, Buzz).
- OSS/commercial: Commercial SaaS, proprietary. Pricing: Starter free; Professional from $16/editor/mo (annual) or $20 monthly; Organization/Enterprise tiers.
- Integration: Figma API; Dev Mode MCP server (beta 2025–2026 — feeds design context to Copilot, Cursor, Claude Code); GitHub repo drag-in (Config 2026 code layers).
- Maintenance: Active. Timeline of verified events:
  - **Adobe $20B acquisition (announced Sep 2022) → terminated Dec 18, 2023** under UK CMA/EU/US antitrust pressure; **$1B reverse termination fee paid by Adobe**.
  - Figma AI launched at Config Jun 2024 ("Make Design" prompt-to-UI); **accusation went viral on X that it reproduced existing apps (Apple Weather cited)**; CEO Dylan Field rolled the feature back pending redesign.
  - Confidential IPO filing Apr 2025; **IPO Jul 31, 2025 at $33/share (NYSE: FIG), closed first day at $115.50 → ~$68B market cap**; 52-week high $142.92.
  - Q2 2026: revenue +41% YoY, net dollar retention 129%, FY2025 revenue $1.056B (+41%); stock fell to ~$19 by Jun 2026 on AI-displacement fears and AI inference cost concerns.
  - Config 2026 (Jun 2026): code layers (edit code on the canvas; push back to GitHub), AI motion graphics/shader tools (Nvidia Triton + Llama 3), Weave AI platform (20+ tools), 30+ starter plugins/shaders.
  - **Acquisitions 2026: Modyfi (motion design) and Payload (headless CMS)** — the latter backing Figma Sites CMS.
- 2025 launches: **Figma Make** (prompt-to-app builder, Claude 3.7-powered, available to Full Seats), **Figma Sites** (design → live website publishing; CMS built-in), **Figma Draw** (advanced vector), **Figma Buzz** (brand asset production). 2026 community assessment: Sites and Buzz still in beta a year on, "not ready for production" — maintainability and core CMS gaps cited (Medium teardown, Jul 2026).
- **CONTROVERSY (trust): Khan v. Figma Inc., proposed class action filed Nov 2025**, alleging customer design files were used to train generative AI models without consent. Figma denies; says it does not train on customer data without permission, with de-identification where authorized use occurs. Status: pending (per TechTimes Jun 2026).
- Limitations: Proprietary file format; vendor lock-in; seat-based pricing; AI features priced on paid tiers; sprawling product surface (trust concern about beta features ever maturing).
- Security: Browser-native collaboration; data residency options (Australia Q4 2025); enterprise SSO/audit on upper tiers.
- Alternatives: Penpot (OSS), Framer, Webflow, Sketch, Lunacy, v0/Lovable/Bolt (AI generation overlap).
- Switching costs: High (design systems, component libraries, org workflows).
- Use: U(Verified) — dominant share (80%+ vs Adobe XD 5–10% per 2026 analyses); named enterprise users: NAB, SafetyCulture, Atlassian (AU data residency); 80%+ of customers use 2+ products.

## DS-02 — Penpot — ACTIVE (open-source challenger, EU-backed)
- Purpose / problem: Open-source, self-hostable design + prototyping platform on open web standards (SVG/CSS/HTML/JSON); "design as code"; W3C-aligned design tokens (DTCG), CSS Grid/Flex layouts; official MCP server for AI-agent read/write of design files (merged into main monorepo at v2.16).
- OSS/commercial: Open-source (MPL-2.0 historically — verify current); by Kaleidos (Spain, founded 2011; Penpot as internal innovation project, beta 2021).
- Integration: REST API (personal access tokens), plugin API, browser extensions, native DTCG token export; works with Style Dictionary pipelines.
- Maintenance: Active. GitHub Trending Jun 21, 2026; releases through 2026 (self-host via Docker).
- **Public backing: Spanish Ministry for Digital Transformation €1.92M investment (Jul 21, 2026)** as part of a €6.9M public+private round — explicitly framed as European digital sovereignty vs "dominant foreign design software."
- Pricing (self-published): Cloud Professional free up to 8 people (10GB); Unlimited $7/user/mo (bill capped at $175/mo); Enterprise $25/user/mo (SSO, audit); Private Server ~$50k/yr. Self-hosted Professional free indefinitely; self-hosted Enterprise $25/user/mo.
- Limitations: Plugin/third-party ecosystem smaller than Figma's; MCP rides a browser session (no persistent server process — CI-driven sync must use REST, per a Jul 2026 ADR).
- Security: Self-hostable = full data control; no outbound AI required.
- Alternatives: Figma, Lunacy, Framer.
- Switching costs: Medium (import/export via open formats; design-system rebuild).
- Use: U(Verified) — ADRs in real repos (penpot-throughline, 2026-07-14: "remove Figma license dependency"; RallyOn design-token workflow, Jul 2026).

## DS-03 — v0 (Vercel) — ACTIVE
- Purpose / problem: Prompt-to-UI generation tuned for React/Next.js: production-ready React + Tailwind + shadcn/ui components; Design Mode visual edits; GitHub sync; deploys to Vercel.
- OSS/commercial: Commercial (Vercel). Credit-based billing at per-model token rates; free $5 credits/mo; Plus $30/user/mo (the $20 Premium plan is being sunsetted — not sold to new users); Business $100/user/mo.
- Maintenance: Active (2026); part of Vercel's AI platform push.
- Limitations: Frontend-only (no backend generation); Vercel deployment lock-in for one-click flow (hosting billed separately).
- Security: Generated code reviewed by user; standard Vercel platform controls.
- Alternatives: Lovable, Bolt.new, Figma Make.
- Switching costs: Low (code export/GitHub sync).
- Use: U(Proposed) — considered the code-quality reference in the category.

## DS-04 — Lovable — ACTIVE
- Purpose / problem: Prompt-to-full-stack-app: frontend + backend + auth + database (auto-wired Supabase), hosting included; aimed at non-technical builders.
- OSS/commercial: Commercial, proprietary. Founded Stockholm (Anton Osika; evolved from open-source GPT Engineer side project, 55k+ stars, Jun 2023). **$330M Series B at $6.6B valuation (Dec 2025); $400M Series C at $13.3B valuation (Aug 2026); $500M ARR Jun 2026 with 146 employees; ~8M users; 60M+ projects; TIME100 2026; SOC 2 Type 2 + ISO 27001.** Fastest to $20M ARR in European startup history (2 months).
- Pricing: Free 5 build credits/day; Pro $25/mo (100 credits); Business $50/mo (same credits + SSO/RBAC); credit ladder to 10,000 ($2,250/mo).
- Maintenance: Active (2026).
- Limitations: Generated apps can be "monolithic," need refactoring at scale; credit-burn cost complaints; vendor lock-in for hosting (code export available).
- Security: SOC 2 Type 2, ISO 27001; standard multi-tenant SaaS data handling.
- Alternatives: Bolt.new, v0, Replit Agent, Base44.
- Switching costs: Low–medium (export exists; Supabase backend is portable).
- Use: U(Proposed) — massive user base; no named enterprise verified in this pass.

## DS-05 — Bolt.new (StackBlitz) — ACTIVE
- Purpose / problem: AI web-dev agent in the browser (WebContainers): full filesystem access, live code execution, error self-repair; multi-framework (React, React Native/Expo — the only one in class supporting mobile).
- OSS/commercial: Commercial (StackBlitz); repo stackblitz/bolt.new (~15–16k stars). **$40M ARR in 6 months post-launch (Oct 2024)**. **bolt.diy is the open-source fork for self-hosting with any LLM.**
- Pricing: Free 1M tokens/mo (300k/day cap); Pro $25/mo (10M tokens; $18 annual); Teams $30/user/mo.
- Maintenance: Active (2026).
- Limitations: Token metering scales with project size; backend partial (BYO).
- Security: Browser-sandboxed execution.
- Alternatives: Lovable, v0, bolt.diy (self-hosted).
- Switching costs: Low.
- Use: U(Proposed).

## DS-06 — bolt.diy — ACTIVE (community OSS fork)
- Purpose / problem: Self-hosted, any-LLM variant of the Bolt.new prompt-to-app builder.
- OSS/commercial: OSS community project.
- Maintenance: Active (2026).
- Limitations: Community support; feature lag vs commercial Bolt.new.
- Alternatives: Dyad, gpte (open-source Lovable clones).
- Use: U(Proposed).

## DS-07 — Dyad — ACTIVE
- Purpose / problem: Local-first open-source AI app builder (dyad-sh/dyad); alternatives to cloud vibe-coding tools.
- OSS/commercial: OSS.
- Maintenance: Active (2026; HN Show HN traction).
- Alternatives: bolt.diy, v0.
- Use: U(Proposed). (Lightly researched — depth debt.)

## DS-08 — Replit Agent — ACTIVE
- Purpose / problem: Cloud IDE + AI agent (Agent 4, parallel tasks): writes, tests, deploys full-stack apps; zero-setup built-in services (auth, DB, hosting); imports from Bolt/Lovable/Figma.
- OSS/commercial: Commercial. $253M ARR (Oct 2025, per trackers).
- Maintenance: Active (2026).
- Limitations: **Pricing complaints — ~$55 per app generation cited as expensive vs competitors**; 2025 effort-pricing + Agent 3 credit-burn backlash (per summary).
- Security: Cloud IDE; code executes on Replit infra.
- Alternatives: Lovable, Bolt.new, v0.
- Switching costs: Medium.
- Use: U(Proposed).

## DS-09 — Base44 — ACTIVE (acquired by Wix)
- Purpose / problem: Prompt-to-app builder (no-code AI apps).
- OSS/commercial: Commercial. **Acquired by Wix (2025)**; $150M ARR (May 2026, per trackers).
- Maintenance: Active under Wix.
- Alternatives: Lovable, Bolt.new.
- Use: U(Proposed). (Lightly researched — depth debt.)

## DS-10 — Framer — ACTIVE
- Purpose / problem: Design-to-site publishing (Figma-like canvas → live site), CMS, AI generation features.
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026).
- Alternatives: Figma Sites, Webflow, Penpot.
- Use: U(Proposed). (Lightly researched — depth debt.)

## DS-11 — Webflow — ACTIVE
- Purpose / problem: Visual web development platform (designer → CMS → hosting).
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026).
- Alternatives: Framer, Figma Sites, WordPress.
- Use: U(Proposed). (Lightly researched — depth debt.)

## DS-12 — Sketch — MAINTAINED (niche)
- Purpose / problem: Mac-native vector UI design (the pre-Figma incumbent).
- OSS/commercial: Commercial, proprietary.
- Maintenance: Maintained (2026); cross-platform reach lost to Figma/Penpot.
- Limitations: Mac-only; file-lock-in; plugin ecosystem aging.
- Alternatives: Figma, Penpot, Lunacy.
- Use: U(Proposed).

## DS-13 — Lunacy (Icons8) — ACTIVE
- Purpose / problem: Free native design app (Windows/macOS/Linux) reading .sketch files.
- OSS/commercial: Commercial freeware.
- Maintenance: Active (2026).
- Alternatives: Sketch, Penpot, Figma.
- Use: U(Proposed). (Lightly researched — depth debt.)

## DS-14 — Modyfi — SUPERSEDED (acquired by Figma)
- Purpose / problem: Browser-based motion design tool.
- Maintenance: **Acquired by Figma (2026)** — standalone future uncertain; folded into Figma's motion push.
- Use: Historical.

## DS-15 — Payload CMS — SUPERSEDED (acquired by Figma)
- Purpose / problem: Headless CMS (TypeScript).
- Maintenance: **Acquired by Figma (2026)** — backing Figma Sites' CMS.
- Alternatives: Strapi, Sanity, Contentful.
- Use: U(Proposed).

## DS-16 — Adobe XD — DEPRECATED (effectively)
- Purpose / problem: Adobe's desktop UI design tool.
- Maintenance: Effectively abandoned post-Figma-deal-collapse (5–10% share vs Figma 80%+); Adobe's design focus shifted to competing via other products.
- Alternatives: Figma, Penpot.
- Use: U(Verified) — legacy enterprise installs.

## Notable status findings (design)
- Figma — **$20B Adobe deal killed Dec 2023 ($1B fee)** → **$68B IPO Jul 2025** → stock collapsed to ~$19 by Jun 2026 (AI-displacement fears); **class action Nov 2025** alleging AI training on customer files; Make Design rolled back after copy accusations; Sites/Buzz still beta after a year.
- Penpot — **€1.92M Spanish government investment Jul 2026** (EU digital sovereignty framing); official MCP server merged at v2.16; GitHub Trending Jun 2026.
- Lovable — **$500M ARR / $13.3B valuation** (Aug 2026) from a 2023 OSS side project — the steepest ramp in the class.
- Modyfi + Payload — **both acquired by Figma (2026)**.
- Adobe XD — effectively dead.

---

### Per-record metadata (condensed)
- Figma/Adobe deal + IPO: Financial Express (Jul 2025), antoncoop, creativetell, YouTube documentary (Sep 2026), SiliconANGLE (Apr 2025), securityonline. Confidence: High. Corroboration: unanimous across outlets.
- Figma AI copy controversy: Forbes mirror (2024). Confidence: Medium. Corroboration: consistent with Field rollback reporting.
- Khan v. Figma class action: TechTimes (Jun 2026). Confidence: Medium (single outlet; verify docket).
- Config 2026 + stock: aidailypost, TechRadar, techtimes, mexc. Confidence: Medium–High. Contradiction: one source says $1.2B IPO raise vs $1.2B at $19.3B valuation in another — consistent.
- Sites/Buzz beta criticism: Medium (adam-barta, Jul 2026) — single author; treat as opinion.
- Penpot: penpot.app (self), dig.watch (Jul 21, 2026), singulism (Jun 2026), gizmodo (Oct 2026), GitHub ADRs (penpot-throughline, rallyon). Confidence: High.
- v0/Lovable/Bolt pricing + valuations: dev.to pricing table (Oct 2026), demandsage (Oct 2026), bra1nDump skillpack findings (Mar 2026), nxcode. Confidence: Medium–High (valuation numbers from TechCrunch/Bloomberg via secondary).
- Base44/Wix, Replit ARR: demandsage trackers. Confidence: Medium.
