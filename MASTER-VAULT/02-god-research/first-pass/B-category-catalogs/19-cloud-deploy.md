# 19 — Cloud Deploy (Hosting / Serverless / Edge / CDN / Secrets / Preview-Rollback / Observability / Telemetry / Scheduling / Headless Agents)

> Part 3 · B-category catalog · Infra-Ops researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved
> KIND LEGEND — [SERVICE] managed SaaS · [OSS] self-hostable · [UTILITY] CLI/lib · [INTEGRATION] adapter wiring systems.

Scope: hosting, serverless, edge, CDN, runtime secrets, preview/rollback, observability/telemetry, scheduling/cron, headless deploy agents. CI engines in 18-cicd.md.

## Index (20 resources)

01 Vercel · 02 Netlify · 03 Cloudflare Pages/Workers · 04 Render · 05 Fly.io · 06 Railway · 07 AWS Lambda + S3/CloudFront · 08 Kubernetes + Helm + Argo CD/Flux · 09 Supabase / Neon (data exemplar) · 10 HashiCorp Vault / Doppler (runtime secrets) · 11 Preview deploys + rollback (Vercel/Netlify/CF pattern) · 12 OpenTelemetry · 13 Prometheus + Grafana · 14 Sentry · 15 Datadog · 16 PostHog (product telemetry exemplar) · 17 Cron/scheduling (pg_cron / Trigger.dev / Inngest) · 18 Headless deploy agents (Replit/Vercel/Anthropic eval exemplar) · 19 Cloud CDN exemplar (CloudFront/Cloudflare) · 20 Serverless DB edge exemplar (D1 / Turso / PlanetScale note)

---

### 01 — Vercel (Next.js production) [SERVICE]
- **Canonical identity:** `service:vercel` — https://vercel.com/
- **Category:** Cloud-Deploy → Hosting (serverless + edge)
- **Type:** [SERVICE]
- **Official URL:** https://vercel.com/
- **Description:** Built by Next.js team: App Router/Server Actions/ISR/PPR/image-opt zero-config; Fluid Compute (active-CPU billing, 2025) cuts I/O-function cost up to 90%; Pro $20/seat/mo; external DB (Neon/Supabase) +$19–25/mo; test workload $40–45/mo.
- **Contents inspected:** 2026 hosting comparisons (build 48s mean; 1TB incl., $40–150/TB overage).
- **Capabilities:** Preview-per-PR, edge+regional functions, middleware, HIPAA BAA path.
- **Usage domain:** Next.js production where framework integration outweighs bandwidth premium.
- **Integration:** [SERVICE] (`git push` → URL; OIDC to AWS/GCP; `@opennextjs` for portability).
- **Compatibility:** Next/Nuxt/SvelteKit/Astro (Next first-class).
- **Deps:** External DB; image/function quotas.
- **Availability:** SaaS (Hobby free non-commercial; Pro commercial).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Bandwidth bills spike on viral/image-heavy; cache aggressively / CF-in-front common; lock-in via Server Actions/ISR needs exit plan.
- **Related:** Netlify, Cloudflare, Neon.
- **Sources:** vercel.com; WebSearch 2026 cost models.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — Netlify (Jamstack pluralism) [SERVICE]
- **Canonical identity:** `service:netlify` — https://www.netlify.com/
- **Category:** Cloud-Deploy → Hosting (build + edge)
- **Type:** [SERVICE]
- **Official URL:** https://www.netlify.com/
- **Description:** Astro/Hugo/Eleventy/Next/Nuxt/SvelteKit + static; Edge (Deno) + Functions (Lambda); Forms/Identity/Analytics built-in; credit pricing (Free 300, Personal $9/1k, Pro $20/3k; deploy 15cr, 20cr/GB, 2cr/10k reqs).
- **Contents inspected:** 2026 comparisons (build 67s mean; PPR unsupported in tests).
- **Capabilities:** Build plugins, branch previews, split testing.
- **Usage domain:** Marketing/docs/Jamstack diversity; editorial-friendly deploys.
- **Integration:** [SERVICE] (git → build → edge; adapters for Next).
- **Compatibility:** Broad frameworks (Gatsby/Hugo/Eleventy strongest).
- **Deps:** Build minutes blow up on monorepos (Turborepo 12-pkg caution).
- **Availability:** SaaS (legacy vs credit plans coexist).
- **Maintenance:** Active (post-Mautic velocity noted slower).
- **License:** Proprietary.
- **Security/limits:** Same bandwidth/build-minute watch as Vercel; pin Functions runtime; review Identity roles.
- **Related:** Vercel, Cloudflare.
- **Sources:** netlify.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 03 — Cloudflare Pages / Workers (edge-first) [SERVICE]
- **Canonical identity:** `service:cloudflare-workers` — https://workers.cloudflare.com/
- **Category:** Cloud-Deploy → Edge compute + static
- **Type:** [SERVICE]
- **Official URL:** https://workers.cloudflare.com/
- **Description:** V8 isolates at 300+ POPs, no cold starts, sub-20ms global; Pages Free: unlimited bandwidth/500 builds/100 sites; Workers Free 100k req/day; Paid $5/mo (10M req + D1 5GB); R2/KV/D1/Queues/DO/AI ecosystem.
- **Contents inspected:** 2026 comparisons (TTFB <60ms all regions; build 52s mean).
- **Capabilities:** Programmatic SEO at scale (25k+ pages), edge APIs, R2 storage.
- **Usage domain:** Read-heavy/content APIs, global static, cost-first scale.
- **Integration:** [SERVICE] (Wrangler CLI; `nodejs_compat` flag; `@opennextjs/cloudflare` adapter for Next).
- **Compatibility:** Workers runtime (not full Node — some npm/long-conn patterns need rework).
- **Deps:** D1 10GB hard cap, single-write SQLite concurrency.
- **Availability:** SaaS (free genuinely prod-viable).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Verify workload fits D1 limits before committing; dashboard sprawl (Pages/Workers/KV/D1/Access) needs runbook.
- **Related:** Vercel, Render, D1/Turso.
- **Sources:** cloudflare.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 04 — Render (full-stack PaaS + Postgres) [SERVICE]
- **Canonical identity:** `service:render` — https://render.com/
- **Category:** Cloud-Deploy → PaaS (web + DB + workers)
- **Type:** [SERVICE]
- **Official URL:** https://render.com/
- **Description:** Web services + managed Postgres + background workers + cron + static + private networking; flat pricing from $7/mo/service; test workload ~$13 Starter / $31 Standard+starter-PG; safest default 2026 for indie SaaS.
- **Contents inspected:** 2026 full-stack comparisons (3–5min deploys; predictable bills).
- **Capabilities:** One-dashboard full-stack; backups; autoscale (limited vs K8s).
- **Usage domain:** SaaS needing DB+runtime without AWS ops.
- **Integration:** [SERVICE] (`render.yaml` blueprint; git auto-deploy).
- **Compatibility:** Docker/Node/Python/Go/Ruby images.
- **Deps:** Per-service pricing accumulates (5 services ≈$35/mo pre-DB); free PG deleted after 30d+14d grace — WARNING.
- **Availability:** SaaS (free web 512MB sleep after 15min idle).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Free-tier sleep brutal for customer-facing; paid PG from day one for real apps; isolate preview DBs.
- **Related:** Railway, Fly.io, Neon.
- **Sources:** render.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 05 — Fly.io (global micro-VMs, Docker-native) [SERVICE]
- **Canonical identity:** `service:flyio` — https://fly.io/
- **Category:** Cloud-Deploy → Global containers
- **Type:** [SERVICE]
- **Official URL:** https://fly.io/
- **Description:** `fly deploy` Docker to 35+ regions; anycast routing, regional failover, scale-to-zero, GPU + volumes; usage-based (test ~$9/mo); self-managed PG (backups/pooling are yours).
- **Contents inspected:** 2026 comparisons (best latency-per-dollar multi-region).
- **Capabilities:** WebSockets/game backends/realtime, multi-region without enterprise wall.
- **Usage domain:** Latency-first global apps, Docker-comfortable teams.
- **Integration:** [SERVICE] (`fly.toml`, `flyctl`, Machines API).
- **Compatibility:** Any Dockerfile; Bun/Deno/custom Node.
- **Deps:** `fly.toml`/volumes/regions concepts; reliability history 2023–24 — verify SLA.
- **Availability:** SaaS (2h trial for new free; then pay-per-resource).
- **Maintenance:** Active (reliability improved 2025–26 per reports).
- **License:** Proprietary.
- **Security/limits:** More config than Render; block metadata egress; own PG ops burden.
- **Related:** Render, Railway, Cloudflare.
- **Sources:** fly.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — Railway (Docker DX) [SERVICE]
- **Canonical identity:** `service:railway` — https://railway.app/
- **Category:** Cloud-Deploy → Container PaaS (DX-first)
- **Type:** [SERVICE]
- **Official URL:** https://railway.app/
- **Description:** Cleanest Dockerfile deploy + native PG + preview envs + sane logs; $5 trial credit 2026; Hobby ~$26/mo test; best DX but 5 major incidents/6mo in 2026 reports — production liability flag.
- **Contents inspected:** 2026 full-stack write-ups (DX wins, reliability caveats).
- **Capabilities:** Hobby→startup velocity; PR environments.
- **Usage domain:** Hobby/small-startup; revisit at scale (private-net/managed ops lag Render).
- **Integration:** [SERVICE] (git/Docker auto-build).
- **Compatibility:** Docker + common stacks.
- **Deps:** Usage billing; production features thinner than Render.
- **Availability:** SaaS.
- **Maintenance:** Active (reliability watch).
- **License:** Proprietary.
- **Security/limits:** WARNING — verify status/SLA before prod; separate preview data; OIDC secret handling.
- **Related:** Render, Fly.io.
- **Sources:** railway.app via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 07 — AWS Lambda + S3/CloudFront (cloud primitives) [SERVICE]
- **Canonical identity:** `service:aws-lambda` — https://aws.amazon.com/lambda/
- **Category:** Cloud-Deploy → Serverless + CDN primitives
- **Type:** [SERVICE]
- **Official URL:** https://aws.amazon.com/lambda/
- **Description:** Event-driven functions + S3 static + CloudFront CDN (SideGuy 3400-file site ~$5/mo vs $50–200 on Vercel); pay-per-use; OIDC from GHA/GitLab.
- **Contents inspected:** 2026 S3+CloudFront stay-decisions.
- **Capabilities:** Full control, data-residency, scale without per-seat pricing.
- **Usage domain:** Regulated/EU-residency, flat-HTML at scale, AWS-resident estates.
- **Integration:** [SERVICE] (SAM/CDK/Terraform; CodePipeline or GHA+OIDC).
- **Compatibility:** All runtimes (Node/Python/Go/Rust).
- **Deps:** Infra-as-code + CloudFront cache design.
- **Availability:** SaaS pay-per-use.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** DX hit (no ISR-zero-config); own image-opt pipeline; least-privilege IAM per function.
- **Related:** Cloudflare Workers, Vercel.
- **Sources:** AWS docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — Kubernetes + Helm + Argo CD/Flux (GitOps CD) [OSS]
- **Canonical identity:** `oss:k8s-cd` — https://argo-cd.readthedocs.io/ ; https://fluxcd.io/
- **Category:** Cloud-Deploy → Orchestration + GitOps CD
- **Type:** [OSS]
- **Official URL:** https://argo-cd.readthedocs.io/
- **Description:** K8s deploy target; Helm charts; Argo CD/Flux sync Git→cluster; Rollouts/Flagger progressive delivery; separate from CI (GHA builds, Argo syncs).
- **Contents inspected:** 2026 layer doctrine (CI≠CD; Argo+Flux own CD).
- **Capabilities:** Previews (Preview Envs/Argo ApplicationSets), automated rollback (git revert = rollback), multi-cluster.
- **Usage domain:** Teams with K8s depth + compliance/audit needs.
- **Integration:** [OSS] (Image Updater, Sealed Secrets/External-Secrets).
- **Compatibility:** Any K8s (EKS/GKE/AKS/self-host).
- **Deps:** Cluster ops burden (heaviest of all options here).
- **Availability:** Free OSS.
- **Maintenance:** Active (CNCF).
- **License:** Apache-2.0 / MIT.
- **Security/limits:** RBAC + signed images (Cosign admission) + sealed secrets mandatory.
- **Related:** Tekton, Spinnaker/Harness.
- **Sources:** argoproj/flux docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — Supabase / Neon (managed Postgres exemplar) [SERVICE]
- **Canonical identity:** `service:supabase` — https://supabase.com/ ; `service:neon` — https://neon.tech/
- **Category:** Cloud-Deploy → Data layer for deploys
- **Type:** [SERVICE] (+ OSS Supabase self-host)
- **Official URL:** https://supabase.com/
- **Description:** Supabase: PG + Auth/Storage/Edge Functions/Realtime; Neon: serverless PG (branching, scale-to-zero) — default Vercel pairing ($19–25/mo baseline addition).
- **Contents inspected:** 2026 Vercel+Neon/Supabase total-cost notes.
- **Capabilities:** Branch-per-preview DBs, connection pooling, backups.
- **Usage domain:** Serverless apps needing PG without Render/Fly-managed PG.
- **Integration:** [SERVICE] (connection strings via secrets manager; preview branching).
- **Compatibility:** Postgres wire protocol.
- **Deps:** Egress/compute quotas.
- **Availability:** SaaS (free-limited → paid).
- **Maintenance:** Active.
- **License:** Proprietary SaaS; Supabase OSS Apache-2.0.
- **Security/limits:** Pool + rotate creds per env; never share prod PG with previews (branch/fork instead).
- **Related:** Render PG, Fly PG, D1/Turso.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — HashiCorp Vault / Doppler (runtime secrets) [SERVICE + OSS]
- **Canonical identity:** `service:vault` — https://www.vaultproject.io/
- **Category:** Cloud-Deploy → Runtime secrets injection
- **Type:** [SERVICE]/[OSS] (Vault BSL; Doppler SaaS; Infisical MIT alt)
- **Official URL:** https://www.vaultproject.io/
- **Description:** Dynamic leases, rotation, audit; External-Secrets Operator syncs to K8s; `doppler run --` injects at process start (no .env in image/git).
- **Contents inspected:** Search-verified category (see also 17-security §12).
- **Capabilities:** Short-TTL creds, revocation, per-env scoping.
- **Usage domain:** Prod/staging/preview secret parity.
- **Integration:** [INTEGRATION] (Vault Agent, ESO, Doppler CLI in buildpacks).
- **Compatibility:** K8s/Docker/serverless via SDK/CSI.
- **Deps:** SaaS or self-host cluster.
- **Availability:** Mixed (see 17 §12 for license nuance).
- **Maintenance:** Active.
- **License:** BSL / proprietary / MIT (by vendor).
- **Security/limits:** OIDC-brokered fetch only; forbid baked secrets in images; audit access per deploy.
- **Related:** OIDC, ESO/Sealed Secrets.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 11 — Preview deploys + rollback pattern [INTEGRATION]
- **Canonical identity:** `pattern:preview-rollback` (Vercel/Netlify/CF Previews + GitOps revert)
- **Category:** Cloud-Deploy → Release safety
- **Type:** [INTEGRATION] (platform feature used as gate)
- **Official URL:** https://vercel.com/docs/deployments/preview-deployments (exemplar)
- **Description:** Every PR gets URL + branched data + seeded auth; promote-to-prod or instant rollback (previous deployment / `git revert` for GitOps).
- **Contents inspected:** 2026 DX comparisons (Vercel/Netlify/CF previews seamless).
- **Capabilities:** Visual + E2E vs preview; one-click rollback.
- **Usage domain:** Required for marketing/commerce releases.
- **Integration:** [INTEGRATION] (GHA status checks block merge until preview E2E/visual/a11y pass).
- **Compatibility:** All major hosts + Argo Rollouts.
- **Deps:** Preview-env data seeding discipline.
- **Availability:** Built-in (retention varies by plan).
- **Maintenance:** Active.
- **License:** Platform terms.
- **Security/limits:** Previews are public-by-default on some plans — gate with auth/robots-noindex + throwaway data.
- **Related:** Argo Rollouts, Chromatic.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — OpenTelemetry (unified telemetry) [OSS]
- **Canonical identity:** `oss:otel` — https://opentelemetry.io/
- **Category:** Cloud-Deploy → Observability (traces/metrics/logs)
- **Type:** [OSS] standard + SDKs
- **Official URL:** https://opentelemetry.io/
- **Description:** Vendor-neutral traces/metrics/logs, propagators, Collector pipelines; auto-instrumentation (JS/Python/Java/Go); OTLP export.
- **Contents inspected:** Search-verified identity (2026 default).
- **Capabilities:** Distributed tracing, exemplars, tail-sampling.
- **Usage domain:** Baseline for every deploy (correlate release → error/latency shift).
- **Integration:** [OSS] (SDK + Collector → Grafana/Datadog/Honeycomb).
- **Compatibility:** All major langs/clouds.
- **Deps:** Backend (Tempo/Mimir/Loki or vendor).
- **Availability:** Free OSS (CNCF).
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security/limits:** Redact PII/headers/cookies in spans; sample aggressively at edge.
- **Related:** Prometheus/Grafana, Sentry, Datadog.
- **Sources:** opentelemetry.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 13 — Prometheus + Grafana (metrics/dashboards) [OSS]
- **Canonical identity:** `oss:prom-grafana` — https://prometheus.io/ ; https://grafana.com/
- **Category:** Cloud-Deploy → Observability (metrics)
- **Type:** [OSS] (+ Grafana Cloud [SERVICE])
- **Official URL:** https://prometheus.io/
- **Description:** Pull metrics, PromQL/alerts; Grafana dashboards (LGTM: Loki/Tempo/Mimir); kube-prometheus-stack standard.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** SLO burn-rate alerts, deploy markers, blackbox probes.
- **Usage domain:** K8s + VM estates; deploy-health gates.
- **Integration:** [OSS] (ServiceMonitor/PodMonitor; Alertmanager → PagerDuty/Opsgenie).
- **Compatibility:** K8s/VM/serverless (via pushgateway/OTLP).
- **Deps:** Retention storage planning.
- **Availability:** Free OSS; Cloud SaaS optional.
- **Maintenance:** Active (CNCF).
- **License:** Apache-2.0 / AGPL-3.0 (Grafana).
- **Security/limits:** Auth reverse-proxy for Grafana; cardinality guard on labels (deploy SHA, not user IDs).
- **Related:** OTel, Datadog.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — Sentry (error + performance) [SERVICE + OSS]
- **Canonical identity:** `service:sentry` — https://sentry.io/
- **Category:** Cloud-Deploy → Observability (errors)
- **Type:** [SERVICE] SaaS + [OSS] self-host
- **Official URL:** https://sentry.io/
- **Description:** Exception capture, source-maps, release health, profiling, cron check-ins; `SENTRY_RELEASE` ties errors to deploy SHA.
- **Contents inspected:** Search-verified identity.
- **Capabilities:** Issue grouping, suspect commits, alert-on-new-release-regression.
- **Usage domain:** Frontend + API error budgets per release.
- **Integration:** [INTEGRATION] (SDKs JS/Python/Go; GHA release action).
- **Compatibility:** All major stacks.
- **Deps:** DSN in secrets (public key + allowlisted origins).
- **Availability:** SaaS quota + OSS self-host.
- **Maintenance:** Active.
- **License:** BSL (self-host); SaaS proprietary.
- **Security/limits:** Scrub PII before send; restrict DSN origins; quota-guard SDK sampling.
- **Related:** OTel, Datadog.
- **Sources:** sentry.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — Datadog (full-stack observability) [SERVICE]
- **Canonical identity:** `service:datadog` — https://www.datadoghq.com/
- **Category:** Cloud-Deploy → Observability (platform)
- **Type:** [SERVICE]
- **Official URL:** https://www.datadoghq.com/
- **Description:** APM/logs/RUM/synthetics/ASM; DORA/deploy tracking; most complete but bill shock risk (custom metrics/logs volume).
- **Contents inspected:** Search-verified identity (enterprise staple in 2026 guides).
- **Capabilities:** Monitors/SLOs, incident + ASM runtime protection.
- **Usage domain:** Enterprises needing single-pane + compliance.
- **Integration:** [SERVICE] (agent/OTLP intake; GHA deploy markers).
- **Compatibility:** K8s/serverless/edge (via forwarder).
- **Deps:** High-volume pricing (tag/metric discipline required).
- **Availability:** Commercial SaaS.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Cost-control is security (blind spots from dropped telemetry); audit log retention/PII scrub.
- **Related:** OTel, Grafana, Sentry.
- **Sources:** datadoghq.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — PostHog (product telemetry exemplar) [SERVICE + OSS]
- **Canonical identity:** `service:posthog` — https://posthog.com/
- **Category:** Cloud-Deploy → Telemetry (product/analytics + experiments)
- **Type:** [SERVICE] Cloud + [OSS] self-host
- **Official URL:** https://posthog.com/
- **Description:** Events, funnels, session replay, feature flags/experiments, error tracking; EU/US hosting; generous free events tier.
- **Contents inspected:** Search-verified identity (also used for A/B in 20-seo file).
- **Capabilities:** Deploy-correlated funnel shifts; flag-gated rollouts.
- **Usage domain:** Product observability alongside infra telemetry.
- **Integration:** [INTEGRATION] (JS/Python SDKs; reverse-proxy for adblock/consent).
- **Compatibility:** Web/mobile/server.
- **Deps:** Consent mode (see 20) for regulated regions.
- **Availability:** SaaS + OSS.
- **Maintenance:** Active.
- **License:** MIT (OSS parts); SaaS proprietary.
- **Security/limits:** Proxy through first-party domain; respect DoNotTrack/consent; avoid session-replay on sensitive inputs (mask).
- **Related:** Plausible/Matomo, GrowthBook.
- **Sources:** posthog.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 17 — Cron/scheduling (pg_cron / Trigger.dev / Inngest) [SERVICE + OSS]
- **Canonical identity:** `tool:scheduler-exemplar` — https://trigger.dev/ ; https://www.inngest.com/
- **Category:** Cloud-Deploy → Scheduling
- **Type:** [SERVICE] + [OSS] SDKs
- **Official URL:** https://trigger.dev/
- **Description:** pg_cron in-PG schedules; Trigger.dev/Inngest durable background jobs with retries/concurrency; Render cron + CF Cron Triggers as host-native alts.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** At-least-once durable exec, idempotency keys, dead-letter.
- **Usage domain:** Nightly crawls, billing, digest emails, report builds.
- **Integration:** [INTEGRATION] (code-defined jobs; dashboard + alerts).
- **Compatibility:** TS/Python + PG.
- **Deps:** SaaS quota or PG extension.
- **Availability:** Mixed free/paid.
- **Maintenance:** Active.
- **License:** MIT/Apache (SDKs); SaaS proprietary.
- **Security/limits:** Idempotency + jitter + least-privilege job creds; alert on missed runs.
- **Related:** Uptime-Kuma/n8n (15-scraping §20).
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — Headless deploy agents (Replit/Vercel/Anthropic eval exemplar) [SERVICE/INTEGRATION]
- **Canonical identity:** `service:headless-deploy-agent-exemplar`
- **Category:** Cloud-Deploy → Headless agents (deploy automation)
- **Type:** [SERVICE] + [INTEGRATION]
- **Official URL:** N/A (vendor-eval pattern 2026)
- **Description:** Agents that plan→preview→promote (Dagger-evaluated flows at Replit/Vercel/Anthropic 2026); must run under preview URLs + required checks + human promote.
- **Contents inspected:** 2026 Dagger Series-B eval notes.
- **Capabilities:** Draft infra diffs, open preview deploys, summarize cost/risk.
- **Usage domain:** Supervised deploy assistance only.
- **Integration:** [INTEGRATION] (issue/PR trigger → preview → human approve → promote).
- **Compatibility:** Vercel/CF/Render/Fly/K8s targets.
- **Deps:** OIDC deployer roles (short-lived, per-env).
- **Availability:** Vendor-gated betas/enterprise.
- **Maintenance:** Fast-moving.
- **License:** Proprietary.
- **Security/limits:** WARNING — never auto-promote to prod; agent is [PROMPT-ONLY] until OIDC-scoped promote + human approve enforce it.
- **Related:** OIDC, preview/rollback, Dagger.
- **Sources:** Vendor blogs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — Cloud CDN exemplar (CloudFront / Cloudflare CDN) [SERVICE]
- **Canonical identity:** `service:cdn-exemplar` — https://aws.amazon.com/cloudfront/ ; https://www.cloudflare.com/cdn/
- **Category:** Cloud-Deploy → CDN / delivery
- **Type:** [SERVICE]
- **Official URL:** https://www.cloudflare.com/cdn/
- **Description:** 300+ POPs (CF) / global (CloudFront); cache-control + stale-while-revalidate; image transforms (CF Images / Vercel Image Opt); WAF/Access integration.
- **Contents inspected:** 2026 TTFB/CDN comparisons (CF <60ms global consistency).
- **Capabilities:** Edge cache, tiered cache, signed URLs, purge-by-tag.
- **Usage domain:** Static + ISR + image workloads in front of any host.
- **Integration:** [SERVICE] (DNS + cache rules; `revalidateTag` webhooks from CMS).
- **Compatibility:** Any origin (S3/Vercel/Render/Fly).
- **Deps:** Cache-key design (query/body discipline).
- **Availability:** SaaS (CF bandwidth-free advantage; CloudFront pay-per-GB).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Strip `Set-Cookie`/PII from cache keys; sign private assets; WAF managed rules + rate limits.
- **Related:** Vercel/Netlify/CF hosts, R2/S3 origins.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — Serverless/edge DB exemplar (D1 / Turso / PlanetScale note) [SERVICE]
- **Canonical identity:** `service:edge-db-exemplar` — https://developers.cloudflare.com/d1/ ; https://turso.tech/
- **Category:** Cloud-Deploy → Data at edge
- **Type:** [SERVICE]
- **Official URL:** https://developers.cloudflare.com/d1/
- **Description:** D1: SQLite-at-edge (5GB incl., 10GB hard cap, single-writer); Turso: libSQL edge replicas; PlanetScale: MySQL serverless (branching) — choose by write-concurrency + size.
- **Contents inspected:** 2026 D1 constraint notes (10GB cap, single-write contention).
- **Capabilities:** Read-heavy global low-latency; branch-per-preview.
- **Usage domain:** Content APIs/tools/utilities (not write-heavy SaaS >10GB — use Render/Neon PG instead).
- **Integration:** [SERVICE] (Wrangler/Drizzle/Prisma drivers).
- **Compatibility:** Workers/edge runtimes.
- **Deps:** Quota + backup discipline.
- **Availability:** SaaS (free→$5+ tiers).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Validate size/write fit pre-commit; PITR/backups + per-env branches.
- **Related:** Neon/Supabase, Render PG.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

## Decision shortcuts (same 5,000-page workload lens as sources)
- Next.js + Server Actions/ISR → Vercel (+Neon/Supabase). Static/Jamstack diversity → Netlify. Edge cost + programmatic SEO → Cloudflare. Full-stack+PG predictability → Render. Docker/global/realtime → Fly.io. Hobby Docker DX → Railway (verify reliability).
- Always: OTel + Sentry (+Prom/Grafana or Datadog) per release; preview-per-PR + branched data; OIDC secrets; CDN in front; rollback = previous deploy / git revert.
- Count: 20 resources (13 SERVICE · 4 OSS · 3 INTEGRATION/pattern mixes — see per-record KIND).
