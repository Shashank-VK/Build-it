# §30 — PaaS, Deploy Platforms & Self-Hosted Alternatives (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## PA-01 — Vercel — ACTIVE (CONTROVERSIAL: pricing)
- Purpose / problem: Frontend cloud: git-push deploys, preview environments, serverless/edge functions, image optimization; home of Next.js and v0.
- OSS/commercial: Commercial SaaS. Hobby free (100GB bandwidth, 100 function exec/day in some configs); Pro $20/seat/mo (1TB bandwidth); Enterprise custom. Compute: $0.60/M requests, GB-hours metered; **bandwidth overage $0.15/GB** (vs Hetzner ~$1.20/TB — a >100x markup cited in 2026 teardown analyses).
- **CONTROVERSY (pricing backlash, 2024–2026, ongoing):** recurring viral bill-shock cases — $46k static-site bill analysis (Feb 2026); $300→$3,550/month after moving client-side requests server-side (99% "serverless function duration"); bot-traffic amplifying Fluid Compute bills (Dec 2025, dev.to "Why We Left Vercel"). Vercel's counter: **Fluid Compute** (concurrent-request reuse on Lambda; "up to 95% compute savings" claimed) and the **Spend Management tool** (hard cost caps — credited with saving one team from a bot-driven Christmas bill). The recurring community thesis ("deployment arbitrage"): above ~1TB/month egress the economics invert sharply and the lever is bandwidth pricing, not compute; per-seat pricing bites teams of 5+ (per nextship ADR costs.md, Sep 2026 — primary source).
- Maintenance: Active (2026); massive scale; Next.js recommended by React team for RSC.
- Limitations: Aggressive pricing at scale; proprietary Next.js features (ISR behavior, Edge Config, Vercel KV) create lock-in; AI streaming/agent loops chew bandwidth and invocations; Hobby function duration limits (5 min default, up to 800s Pro, 30 min extended beta).
- Security: Standard SaaS; preview URLs can leak (deploy-protection settings).
- Alternatives: Netlify, Cloudflare Pages/Workers, Fly.io, Render, Coolify/Dokploy self-hosted, SST.
- Switching costs: Medium–high if deep on Vercel-specific features.
- Use: U(Verified) — dominant Next.js host; v0 deploys.

## PA-02 — Netlify — ACTIVE
- Purpose / problem: The original git-push-to-deploy platform (JAMstack): forms, identity, split testing, edge functions.
- OSS/commercial: Commercial SaaS (free tier; Pro/Team/Enterprise).
- Maintenance: Active (2026); most feature-complete in class per 2026 comparisons.
- Alternatives: Vercel, Cloudflare Pages.
- Switching costs: Medium.
- Use: U(Proposed). (Lightly researched — depth debt.)

## PA-03 — Cloudflare Pages / Workers — ACTIVE
- Purpose / problem: Static hosting + edge compute on Cloudflare's network; famously **no egress fees** on typical CDN usage; unlimited bandwidth on free tier for static.
- OSS/commercial: Commercial (generous free tier); Workers paid for compute.
- Maintenance: Active (2026).
- Limitations: Workers runtime is not Node (compatibility shims); Durable Objects/ KV have their own semantics.
- Alternatives: Vercel, Netlify, Fly.io.
- Switching costs: Low–medium.
- Use: U(Proposed).

## PA-04 — Fly.io — ACTIVE
- Purpose / problem: Run containers close to users globally (Firecracker microVMs "Machines"); Heroku-Procfiles-friendly (`flyctl` builds with buildpacks; Procfile → fly.toml [processes]); published Migrate-from-Heroku guide.
- OSS/commercial: Commercial, usage-based (Machines billing); trial/usage model in 2026 (no longer "always free" per awesome-web-hosting-2026).
- Maintenance: Active (2026).
- Limitations: DIY-er than Heroku (more knobs); usage-based bills need monitoring.
- Security: Standard.
- Alternatives: Render, Railway, Koyeb.
- Switching costs: Low (Dockerfile/Procfile portable).
- Use: U(Proposed).

## PA-05 — Render — ACTIVE
- Purpose / problem: Heroku-style managed PaaS with predictable pricing: web services, Postgres, Redis, cron; render.yaml; native runtimes (no Procfile — Dockerfile or prebuilt for custom).
- OSS/commercial: Commercial; free tier (750 hrs/mo, sleeps after 15 min idle); Standard $25/mo (2GB) vs Heroku Standard-2X $50 (1GB).
- Maintenance: Active (2026).
- Alternatives: Railway, Fly.io, Heroku.
- Switching costs: Low.
- Use: U(Proposed).

## PA-06 — Railway — ACTIVE
- Purpose / problem: Developer-UX-first PaaS; per-second usage billing; Railpack builder (Nixpacks successor) detects Procfiles; per-service model like old Heroku dashboard.
- OSS/commercial: Commercial; $5 trial credit; usage-based (stopped services cost nothing). 2026: trial/usage model, not "always free."
- Maintenance: Active (2026).
- Alternatives: Render, Fly.io, Northflank.
- Switching costs: Low.
- Use: U(Proposed).

## PA-07 — Koyeb — ACTIVE
- Purpose / problem: Global edge deployment PaaS; free Nano instance (no sleep); serverless containers.
- OSS/commercial: Commercial freemium.
- Maintenance: Active (2026).
- Alternatives: Fly.io, Render.
- Use: U(Proposed). (Lightly researched — depth debt.)

## PA-08 — Zeabur — ACTIVE
- Purpose / problem: Simple-deploy PaaS; $5/mo free credit, no sleep; "Top Pick 2026" in community hosting guides.
- OSS/commercial: Commercial freemium.
- Maintenance: Active (2026).
- Alternatives: Railway, Render.
- Use: U(Proposed). (Lightly researched — depth debt.)

## PA-09 — Northflank — ACTIVE
- Purpose / problem: Container/K8s-style control with managed UX; free plan (1 service + 1 DB); BYOC path.
- OSS/commercial: Commercial.
- Maintenance: Active (2026).
- Alternatives: Qovery, Porter.
- Use: U(Proposed). (Lightly researched — depth debt.)

## PA-10 — Dokku — ACTIVE (OSS Heroku clone)
- Purpose / problem: "Open source PaaS alternative to Heroku" — push Heroku-compatible apps over Git to your own single host; herokuish + Cloud Native Buildpacks; Procfile respected; Postgres/Redis via official plugins.
- OSS/commercial: OSS MIT (~32k GitHub stars); self-hosted on your VPS.
- Maintenance: Active, mature (2026).
- Limitations: Single-host model (not HA); you own the ops.
- Security: Your infra, your patching.
- Alternatives: Coolify, Dokploy, CapRover.
- Switching costs: Low (leaving = your server already).
- Use: U(Proposed) — "closest thing to Heroku that exists" per 2026 migration guides.

## PA-11 — Coolify — ACTIVE (OSS)
- Purpose / problem: Self-hosted Heroku/Netlify alternative (VPS → push-to-deploy, DBs, previews).
- OSS/commercial: OSS (license: verify — historically Apache-2.0 with fair-code discussions; check current).
- Maintenance: Active (2026); central to the "deployment arbitrage" movement off Vercel.
- Alternatives: Dokku, Dokploy, CapRover.
- Switching costs: Low.
- Use: U(Proposed).

## PA-12 — Dokploy — ACTIVE (OSS)
- Purpose / problem: Self-hosted PaaS (Docker-based, VPS-friendly); chosen by teams leaving Vercel in 2025–2026 teardowns.
- OSS/commercial: OSS.
- Maintenance: Active (2026).
- Alternatives: Coolify, Dokku.
- Use: U(Proposed). (Lightly researched — depth debt.)

## PA-13 — Qovery — ACTIVE (BYOC)
- Purpose / problem: Heroku-like DX deploying into YOUR cloud account (BYOC): managed control plane + your AWS/GCP.
- OSS/commercial: Commercial; open-source engine components (Qovery Engine in Rust, OSS).
- Maintenance: Active (2026).
- Limitations: Per-cluster floor cost; needs your cloud account.
- Alternatives: Porter, Cloud 66, Northflank.
- Switching costs: Low (infra already in your account).
- Use: U(Proposed).

## PA-14 — Porter — ACTIVE (BYOC)
- Purpose / problem: PaaS on your own AWS/GCP (deploy into your cloud).
- OSS/commercial: Commercial + OSS components.
- Maintenance: Active (2026).
- Alternatives: Qovery, Northflank.
- Use: U(Proposed). (Lightly researched — depth debt.)

## PA-15 — Heroku — MAINTAINED (post-free-tier)
- Purpose / problem: The original git-push PaaS (Salesforce).
- OSS/commercial: Commercial; **free tier ended Nov 28, 2022** (forced the great migration; ecosystem above is its aftermath).
- Maintenance: Maintained; dynos restart ~24h (masks memory leaks — migration gotcha documented in 2026 guides).
- Alternatives: Render, Railway, Dokku, Fly.io.
- Switching costs: Medium (add-ons, pipelines).
- Use: U(Verified) — legacy installs; renewals drive BYOC evaluations.

## PA-16 — Cloud 66 — ACTIVE
- Purpose / problem: Deploy/manage apps on your own cloud (Rails/node focus).
- OSS/commercial: Commercial.
- Maintenance: Active (2026).
- Alternatives: Qovery, Porter.
- Use: U(Proposed). (Lightly researched — depth debt.)

## Notable status findings (PaaS)
- Vercel — **pricing backlash is structural and ongoing**: $0.15/GB bandwidth vs ~$1.20/TB VPS; the community's "1TB inversion rule" (below it Vercel Pro $20 is unbeatable; above it self-host wins); Fluid Compute + Spend Management are Vercel's answers.
- Heroku free tier end (Nov 2022) → the 2026 landscape: Render/Railway/Fly.io (vendor-hosted), Dokku/Coolify/Dokploy (self-hosted), Qovery/Porter/Northflank (BYOC).
- "Deployment arbitrage" (Coolify on bare metal/Hetzner) is a named 2026 movement, not just forum grumbling.

---

### Per-record metadata (condensed)
- Vercel bill shock: Medium (Soumyadip Ghosh, Feb 2026); dev.to "Why We Left Vercel" (Dec 2025); Medium deployment-arbitrage (Jan 2026); The Register on Fluid Compute (Jul 2025); dev.to Vercel AI SDK alternatives (Sep 2026); nextship docs/costs.md (GitHub, Sep 2026 — primary ADR). Confidence: Medium–High (multiple independent first-hand accounts + one ADR).
- Heroku-alternative landscape: qovery.com migration/pricing/BYOC guides (Oct 2026); awesome-web-hosting-2026 (GitHub, keksmd/el-kalima). Confidence: Medium (vendor-authored guides + community lists).
- Heroku free-tier end Nov 28, 2022: established record (summary). Confidence: High.
