# 20 — SEO / CMS / Commerce (Metadata · Sitemap · Vitals · Analytics · Consent · A/B · Headless/Blog · E-comm/Cart/Payments/Email · Localization · Search · Feedback · Monitoring)

> Part 3 · B-category catalog · Infra-Ops researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved

Scope: SEO, metadata, sitemap/robots, Core Web Vitals, analytics, consent, A/B, CMS/headless/blog, e-commerce/cart/payments/email, localization, site search, feedback, uptime monitoring.

## Index (22 resources)

SEO/foundations: 01 Next Metadata API + OG · 02 sitemap.xml/robots.txt spec · 03 Schema.org/JSON-LD · 04 Google Search Console · 05 Lighthouse/Core Web Vitals
Analytics/consent/A-B: 06 GA4 · 07 Plausible/Matomo · 08 PostHog · 09 Cookie consent (Cookiebot/Osano/Didomi exemplar) · 10 GrowthBook/Optimizely (A/B)
CMS/blog: 11 WordPress (headless exemplar) · 12 Contentful · 13 Sanity (+Shopify Connect) · 14 Strapi · 15 Ghost · 16 Payload/Directus note
Commerce: 17 Shopify (+Hydrogen) · 18 WooCommerce · 19 Medusa/Saleor (OSS commerce) · 20 Stripe (payments) + cart-pricing rule · 21 Resend/SendGrid/Mailchimp (email) · 22 Localization/search/feedback/monitoring (next-intl + Algolia/Meilisearch/Typesense + feedback + Uptime-Kuma)

---

### 01 — Next Metadata API + Open Graph [UTILITY/STANDARD]
- **Canonical identity:** `util:next-metadata` — https://nextjs.org/docs/app/building-your-application/optimizing/metadata
- **Category:** SEO → Metadata
- **Type:** Framework API (OSS Next.js)
- **Official URL:** https://nextjs.org/docs/app/building-your-application/optimizing/metadata
- **Description:** File+code metadata (`layout.tsx export const metadata`, `opengraph-image`, `twitter-image`, `robots.ts`, JSON-LD components); per-locale alternates/canonicals.
- **Contents inspected:** Next docs pattern via WebSearch.
- **Capabilities:** Title/description templates, canonical/hreflang, OG/Twitter cards, `metadataBase`.
- **Usage domain:** Every App-Router page (Crawl4AI/SEO-scraper reads these first).
- **Integration:** utility (code; validated by SEO crawlers + Rich Results).
- **Compatibility:** Next 13+ App Router.
- **Deps:** None.
- **Availability:** Free OSS.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Noindex previews/staging; absolute URLs via metadataBase or social cards break.
- **Related:** Sitemap/robots, Schema.org.
- **Sources:** nextjs.org via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 02 — sitemap.xml / robots.txt (+ RSS) [STANDARD]
- **Canonical identity:** `spec:sitemaps-robots` — https://www.sitemaps.org/ · https://www.rfc-editor.org/rfc/rfc9309.html
- **Category:** SEO → Discovery/crawl control
- **Type:** Open standards
- **Official URL:** https://www.sitemaps.org/
- **Description:** `sitemap_index.xml` (50k URLs/50MB per file), `<lastmod>/<changefreq>`, image/video/news extensions; `robots.txt` (RFC 9309) Allow/Disallow + `Sitemap:` directive; RSS/Atom as lightweight discovery.
- **Contents inspected:** Spec identities via WebSearch (Cheerio extraction guides list these as first scrape targets).
- **Capabilities:** Crawl budgeting, preview-exclusion, Hreflang sitemaps.
- **Usage domain:** Every production host (Next `sitemap.ts` / `robots.ts` generators).
- **Integration:** standard (generated routes; Search Console submission).
- **Compatibility:** All crawlers (Googlebot/GPTBot/ClaudeBot vary in robots respect — verify).
- **Deps:** None.
- **Availability:** Free.
- **Maintenance:** Active (RFC 9309 2022; sitemaps.org stable).
- **License:** Spec free.
- **Security/limits:** robots ≠ access control — enforce auth server-side; never list private preview URLs.
- **Related:** Search Console, Common Crawl/CDX.
- **Sources:** sitemaps.org/IETF via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 03 — Schema.org + JSON-LD (rich results) [STANDARD]
- **Canonical identity:** `spec:schema-org` — https://schema.org/ (validators: Rich Results Test, Schema Validator)
- **Category:** SEO → Structured data
- **Type:** Open standard
- **Official URL:** https://schema.org/
- **Description:** Product/Article/BreadcrumbList/FAQ/Organization/Review vocabularies; single richest deterministic extraction + SERP eligibility signal.
- **Contents inspected:** SEO-scraping guides (parse ld+json before CSS) + headless-CMS SEO notes (SSR/AEO).
- **Capabilities:** Rich snippets, merchant listings, AI-crawler (GPTBot/Claude) comprehension.
- **Usage domain:** Product/articles/breadcrumbs on every template.
- **Integration:** standard (React JSON-LD per content type; ISR revalidate on CMS publish).
- **Compatibility:** Google/Bing/LLM crawlers.
- **Deps:** None.
- **Availability:** Free.
- **Maintenance:** Active (Schema 20+).
- **License:** CC-BY-SA.
- **Security/limits:** Stale/spammy markup penalized — resolve live price/availability from commerce API (reference pattern).
- **Related:** Metadata API, CMS reference pattern.
- **Sources:** schema.org via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 04 — Google Search Console (index + health) [SERVICE]
- **Canonical identity:** `service:gsc` — https://search.google.com/search-console
- **Category:** SEO → Index/health
- **Type:** Service (free, Google)
- **Official URL:** https://search.google.com/search-console
- **Description:** Index coverage, sitemaps, Core Web Vitals (CrUX), HTTPS/security, manual actions, link reports; Bing Webmaster Tools counterpart.
- **Contents inspected:** Search-verified identity.
- **Capabilities:** URL inspection, crawl-stats, page-experience signals.
- **Usage domain:** Post-deploy SEO gate (submit sitemap, watch coverage deltas).
- **Integration:** service (DNS/HTML verification; API for automation).
- **Compatibility:** Any public site.
- **Deps:** Verified property.
- **Availability:** Free.
- **Maintenance:** Active.
- **License:** Google terms.
- **Security/limits:** Data delayed/sampled; pair with server logs + RUM for truth.
- **Related:** Lighthouse/CrUX, Bing Webmaster.
- **Sources:** Google docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 05 — Lighthouse / Core Web Vitals (lab + field) [UTILITY]
- **Canonical identity:** `util:lighthouse` — https://developer.chrome.com/docs/lighthouse ; vitals: LCP/INP/CLS via CrUX/RUM
- **Category:** SEO → Performance signals
- **Type:** OSS utility + field dataset
- **Official URL:** https://developer.chrome.com/docs/lighthouse
- **Description:** Lab audits (perf/a11y/best-practices/SEO); field vitals targets 2026: LCP <2.5s (<1.5s headless-Next exemplar), INP <200ms, CLS <0.1; Next RSC+ISR green path.
- **Contents inspected:** Headless-CMS SEO notes (100/100 exemplar) + hosting TTFB tables.
- **Capabilities:** `lhci` CI gates, Treo/CrUX history, RUM (Vercel Speed Insights / Sentry).
- **Usage domain:** Per-PR lab gate + prod field watch.
- **Integration:** utility (`lhci autorun`; `next dev` + RUM snippet).
- **Compatibility:** Chromium lab; CrUX field (Chrome users).
- **Deps:** None / RUM snippet.
- **Availability:** Free OSS (+CrUX API free).
- **Maintenance:** Active (Lighthouse 12.x 2026).
- **License:** Apache-2.0.
- **Security/limits:** Lab ≠ field — gate lab, alert on field regression (p75).
- **Related:** Search Console, Sentry RUM.
- **Sources:** Chrome docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — GA4 (analytics incumbent) [SERVICE]
- **Canonical identity:** `service:ga4` — https://support.google.com/analytics/answer/10089681
- **Category:** Analytics → Event analytics
- **Type:** Service (Google)
- **Official URL:** https://analytics.google.com/
- **Description:** Event-based model, consent mode v2, BigQuery export, server-side GTM option; most complete free funnel but heaviest privacy/consent burden (EU).
- **Contents inspected:** Search-verified identity.
- **Capabilities:** Audiences, explorations, ads linkage.
- **Usage domain:** Ad-driven orgs needing Google-ads closed loop.
- **Integration:** service (gtag/GTM/server-GTM; consent-mode wiring).
- **Compatibility:** Web/app.
- **Deps:** Consent banner (09) for EEA/UK.
- **Availability:** Free (360 paid for enterprise).
- **Maintenance:** Active.
- **License:** Google terms.
- **Security/limits:** IP/anonymization + data-retention + DPA review; first-party proxy if adblock loss high.
- **Related:** Plausible/Matomo, PostHog.
- **Sources:** Google docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 07 — Plausible / Matomo (privacy-first analytics) [SERVICE + OSS]
- **Canonical identity:** `service:plausible` — https://plausible.io/ ; `oss:matomo` — https://matomo.org/
- **Category:** Analytics → Privacy-first
- **Type:** Service (Plausible) + OSS self-host (Matomo)
- **Official URL:** https://plausible.io/
- **Description:** Cookieless options, EU hosting, lightweight scripts (<1KB–45KB vs GA), no cross-site sharing; Matomo self-host for data-residency/GDPR strict.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Funnels/goals, Search Console integration (Plausible), log import (Matomo).
- **Usage domain:** SMB/content sites avoiding consent-wall friction where legitimate-interest assessment allows.
- **Integration:** service/utility (script tag; reverse-proxy for adblock).
- **Compatibility:** Any site.
- **Deps:** DPA + hosting region choice.
- **Availability:** SaaS from ~$9/mo / OSS free self-host.
- **Maintenance:** Active.
- **License:** Proprietary SaaS / GPL-3.0 (Matomo).
- **Security/limits:** Still needs consent assessment for cookies/identifiers — document lawful basis; cookieless ≠ consent-free in all jurisdictions.
- **Related:** PostHog, GA4.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — PostHog (product analytics + replay + flags) [SERVICE + OSS]
- **Canonical identity:** `service:posthog` — https://posthog.com/
- **Category:** Analytics/Telemetry → Product
- **Type:** Service Cloud + OSS self-host
- **Official URL:** https://posthog.com/
- **Description:** Events/funnels/replay/experiments/surveys + error tracking; EU/US clouds; reverse-proxy recommended; generous free events.
- **Contents inspected:** Search-verified identity (also 19-cloud-deploy §16).
- **Capabilities:** Deploy-correlated funnel shifts; flag-gated rollouts (pairs with 10).
- **Usage domain:** Product-led SaaS telemetry.
- **Integration:** service (JS/Python SDKs; proxy for consent/adblock).
- **Compatibility:** Web/mobile/server.
- **Deps:** Consent wiring.
- **Availability:** SaaS + OSS.
- **Maintenance:** Active.
- **License:** MIT (parts); SaaS proprietary.
- **Security/limits:** Mask sensitive inputs in replay; honor consent before init.
- **Related:** GrowthBook, Plausible.
- **Sources:** posthog.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — Cookie consent exemplar (Cookiebot / Osano / Didomi / c15t) [SERVICE/UTILITY]
- **Canonical identity:** `service:consent-exemplar` — https://www.cookiebot.com/ ; OSS alt: `oss:c15t` — https://c15t.com/
- **Category:** Compliance → Consent
- **Type:** Service (+ OSS alt)
- **Official URL:** https://www.cookiebot.com/
- **Description:** IAB TCF v2.2, Google Consent Mode v2, geo-rules, DSAR logs, banner A/B; c15t self-host OSS for code-owned banners.
- **Contents inspected:** Search-verified category.
- **Capabilities:** Prior-blocking of tags, proof-of-consent audit trail.
- **Usage domain:** EEA/UK/CA publishing/commerce (mandatory with GA4/ads/replay).
- **Integration:** service (CMP snippet + GTM/CSP wiring; `data-cookieconsent` attributes).
- **Compatibility:** Any CMP-aware tag manager.
- **Deps:** Tag inventory (analytics/ads/replay/pixels).
- **Availability:** SaaS (free-limited) / OSS free.
- **Maintenance:** Active (TCF/Consent-Mode churn 2024–26).
- **License:** Proprietary / MIT (c15t).
- **Security/limits:** CMP ≠ lawful basis — map each purpose; test that Deny truly blocks network calls (proxy-verify).
- **Related:** GA4, PostHog, Plausible.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — GrowthBook / Optimizely (A/B + flags) [SERVICE + OSS]
- **Canonical identity:** `service:growthbook` — https://www.growthbook.io/ ; `service:optimizely` — https://www.optimizely.com/
- **Category:** Experimentation → A/B + feature management
- **Type:** Service (GrowthBook OSS self-host available; Optimizely commercial)
- **Official URL:** https://www.growthbook.io/
- **Description:** Visual/URL-split/code experiments, Bayesian stats, warehouse-native (BigQuery/Snowflake) — GrowthBook from ~free self-host; Optimizely enterprise governance.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Sticky bucketing, guardrail metrics, CMS-driven audiences.
- **Usage domain:** Pricing/hero/checkout tests tied to CMS campaign pages.
- **Integration:** service (JS/edge SDKs; Next middleware bucketing).
- **Compatibility:** Web/server/edge.
- **Deps:** Analytics warehouse for power.
- **Availability:** SaaS + OSS (GrowthBook MIT).
- **Maintenance:** Active.
- **License:** MIT (GrowthBook) / proprietary (Optimizely).
- **Security/limits:** Flicker/SEO-cloaking risk — prefer server/edge bucketing + `Vary` discipline; exclude bots.
- **Related:** PostHog experiments, CMS previews.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 11 — WordPress (monolith + headless exemplar) [OSS + SERVICE]
- **Canonical identity:** `oss:wordpress` — https://wordpress.org/ (headless via WPGraphQL + Next)
- **Category:** CMS → Monolith/blog (headless-capable)
- **Type:** OSS self-host (+ WordPress.com SaaS)
- **Official URL:** https://wordpress.org/
- **Description:** 43% web share; 60k plugins/11k themes; cheapest SMB path (~$150/yr hosting); 80%-of-hacks surface note → harden; headless (WP backend + Next front + Yoast/RankMath) keeps SEO plugins + modern FE.
- **Contents inspected:** 2026 headless-vs-WP guide (when-WP vs when-headless split).
- **Capabilities:** Gutenberg, Yoast/RankMath, WPGraphQL/REST, WPML/Polylang.
- **Usage domain:** SMB/blog/portfolio/client-self-edits/budget <$2500; headless-WP where years of content exist (with WooCommerce).
- **Integration:** OSS (PHP/MySQL; headless via WPGraphQL [INTEGRATION]).
- **Compatibility:** LAMP hosts; front any (Next/Astro).
- **Deps:** Update + backup + WAF discipline.
- **Availability:** Free OSS (+hosting).
- **Maintenance:** Active.
- **License:** GPL-2.0.
- **Security/limits:** Patch cadence + least-privilege plugins + 2FA + disable XML-RPC/file-edit where unused.
- **Related:** Ghost, headless CMSs, WooCommerce.
- **Sources:** wordpress.org; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — Contentful (enterprise headless) [SERVICE]
- **Canonical identity:** `service:contentful` — https://www.contentful.com/
- **Category:** CMS → Headless (enterprise governance)
- **Type:** Service (managed SaaS)
- **Official URL:** https://www.contentful.com/
- **Description:** UI-first modeling, REST+GraphQL, Live Preview, roles/approvals/audit, translation-vendor pipelines; from $300/mo; ~$3500/mo at 200k records/5 editors exemplar.
- **Contents inspected:** 2026 Sanity-vs-Contentful-vs-Strapi matrix + Shopify guide.
- **Capabilities:** Multi-brand/multi-region governance, scheduled publishing, commerce field plugins (IDs only).
- **Usage domain:** Enterprise where content-ops governance > DX.
- **Integration:** service (SDKs; Shopify/commercetools connectors; Next/Nuxt previews).
- **Compatibility:** Hydrogen/Next/Nuxt frontends.
- **Deps:** SaaS quota (records/users/API calls).
- **Availability:** SaaS.
- **Maintenance:** Active (oldest, Spotify/Heineken exemplar).
- **License:** Proprietary.
- **Security/limits:** Schema lives outside git (use `contentful migration` CLI + review); SSO/SCIM +Least-privilege spaces.
- **Related:** Sanity, Strapi, Shopify.
- **Sources:** contentful.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 13 — Sanity (DX-led headless) [SERVICE]
- **Canonical identity:** `service:sanity` — https://www.sanity.io/
- **Category:** CMS → Headless (structured content)
- **Type:** Service (managed SaaS; Studio OSS)
- **Official URL:** https://www.sanity.io/
- **Description:** Schema-as-code (`sanity.config.ts` in git/PRs), GROQ, real-time collab, Visual Editing + Hydrogen integration, Shopify Connect (references, never price copies); Free/Growth $99–1400/mo exemplars.
- **Contents inspected:** Sanity e-commerce page + 2026 matrices (Sanity+Shopify+Next default stack).
- **Capabilities:** Reference pattern (handle/ID only; live resolve at render; `revalidateTag('sanity')` + 60s product cache), AI draft/translate/scheduled drops.
- **Usage domain:** Engineering-led commerce/content (default 2026 pick).
- **Integration:** service (GROQ/REST; webhooks → ISR; Visual Editing).
- **Compatibility:** Next/Hydrogen/Astro.
- **Deps:** SaaS quota (documents/users).
- **Availability:** SaaS (free→Growth→Enterprise).
- **Maintenance:** Active.
- **License:** Proprietary (Studio MIT-ish OSS).
- **Security/limits:** Webhook-secret verify + preview-auth; market-tax/shipping modeled per-market, not duplicated.
- **Related:** Contentful, Strapi, Shopify/Medusa.
- **Sources:** sanity.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 14 — Strapi (self-host OSS headless) [OSS + SERVICE]
- **Canonical identity:** `oss:strapi` — `github:strapi/strapi`
- **Category:** CMS → Headless (self-host)
- **Type:** OSS (MIT v5) + Strapi Cloud ($19/mo+)
- **Official URL:** https://strapi.io/
- **Description:** Node+PG, REST+GraphQL (plugin), Content-Type Builder (UI↔code JSON), i18n v5; self-host infra ~$300–800/mo exemplar; right when residency/control genuine, not mere cost-save.
- **Contents inspected:** 2026 matrices (45min first-type; 2-week CF+Vercel integration tax noted).
- **Capabilities:** Custom admin, roles, webhooks; asset via S3/Cloudinary (no native CDN).
- **Usage domain:** GDPR-EU self-host, custom admin, full data control.
- **Integration:** OSS (self-host PG+S3+app; Cloud option).
- **Compatibility:** Next/Astro/commerce fronts.
- **Deps:** You operate PG/storage/app/CDN/auth.
- **Availability:** Free OSS / Cloud SaaS.
- **Maintenance:** Active (v5).
- **License:** MIT (see Enterprise-Edition nuance for EE features).
- **Security/limits:** Harden admin (SSO, IP-allowlist, backups, asset-signed URLs); keep UI-vs-code schema drift disciplined.
- **Related:** Payload/Directus, Sanity, Medusa.
- **Sources:** strapi.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 15 — Ghost (blog/newsletter headless-capable) [OSS + SERVICE]
- **Canonical identity:** `oss:ghost` — https://ghost.org/
- **Category:** CMS → Blog/newsletter
- **Type:** OSS self-host + Ghost(Pro) SaaS
- **Official URL:** https://ghost.org/
- **Description:** Markdown editor, memberships/paid newsletters, Content/Admin APIs for headless Next front; simpler than WP for pubs.
- **Contents inspected:** Search-verified identity.
- **Capabilities:** SEO/social cards built-in, AMP/RSS, webhooks/Zapier.
- **Usage domain:** Blogs/pubs where newsletter+SEO matter more than page-builder freedom.
- **Integration:** OSS/service (Content API → ISR front).
- **Compatibility:** Node + SQLite/MySQL.
- **Deps:** Mail provider (Mailgun default) for bulk.
- **Availability:** Free OSS / Pro SaaS.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Lock staff invites + API keys per integration; backup SQLite/MySQL + images.
- **Related:** WordPress, Sanity, Resend/Mailchimp.
- **Sources:** ghost.org via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — Payload / Directus note (code-first / DB-first OSS) [OSS]
- **Canonical identity:** `oss:payload` — https://payloadcms.com/ ; `oss:directus` — https://directus.io/
- **Category:** CMS → Headless (dev/DB-first)
- **Type:** OSS (self-host; Clouds available)
- **Official URL:** https://payloadcms.com/
- **Description:** Payload: TS, Mongo/PG, code-first collections + admin; rising star 2024+; Directus: DB-first (wraps existing SQL) for data+content hybrids.
- **Contents inspected:** 2026 Top-7 headless table (Payload free OSS; Directus free).
- **Capabilities:** Versioned collections, access control, REST/GraphQL.
- **Usage domain:** Custom-dev (Payload) / existing-DB augmentation (Directus).
- **Integration:** OSS (Next front via API).
- **Compatibility:** Node + PG/Mongo.
- **Deps:** Self-host ops.
- **Availability:** Free OSS (+Cloud SaaS).
- **Maintenance:** Active.
- **License:** MIT (Payload) / GPL-3.0 (Directus — note copyleft for extensions).
- **Security/limits:** Same admin-hardening + backup discipline as Strapi.
- **Related:** Strapi, Sanity.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 17 — Shopify (+ Hydrogen headless) [SERVICE]
- **Canonical identity:** `service:shopify` — https://www.shopify.com/ (headless: https://hydrogen.shopify.dev/)
- **Category:** Commerce → Store platform (products/cart/checkout)
- **Type:** Service (SaaS; Hydrogen OSS)
- **Official URL:** https://www.shopify.com/
- **Description:** Products/prices/inventory/cart/checkout/orders — source of truth; CMS stores references only (anti-duplication rule); Hydrogen (React/Remix) + Storefront API; $39/mo+fees exemplar.
- **Contents inspected:** 2026 headless-CMS-ecommerce guides (reference pattern + cache split: content-long/webhook-revalidate, commerce-short/60s).
- **Capabilities:** Checkout extensibility, Markets (tax/shipping/compliance per-market), Shopify Connect apps.
- **Usage domain:** Fastest time-to-market; campaign/lookbook/SEO scale via Sanity/Contentful/Prismic front.
- **Integration:** service (Storefront/Admin APIs; Hydrogen + Next/Astro fronts).
- **Compatibility:** Hydrogen/Next/Astro + CMS reference fields.
- **Deps:** Transaction fees + app costs.
- **Availability:** SaaS.
- **Maintenance:** Active.
- **License:** Proprietary (Hydrogen MIT).
- **Security/limits:** Never copy prices into CMS; resolve live at render; webhook-invalidate content, short-cache commerce; PCI scope stays with Shopify/Stripe.
- **Related:** Medusa/Saleor, WooCommerce, Sanity/Contentful.
- **Sources:** shopify.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 18 — WooCommerce (WP-native commerce) [OSS]
- **Canonical identity:** `oss:woocommerce` — https://woocommerce.com/
- **Category:** Commerce → Store (WP-native)
- **Type:** OSS plugin (+ Automattic SaaS/extensions)
- **Official URL:** https://woocommerce.com/
- **Description:** WP content + commerce monolith; cheapest SMB full-stack (~$60/mo hosting exemplar vs ~$250/mo headless exemplar); headless-WP+Woo where content history dominates.
- **Contents inspected:** 2026 cost/stack comparisons.
- **Capabilities:** Coupons/subscriptions/bookings extensions, Stripe/PayPal, REST/GraphQL (WooGraphQL).
- **Usage domain:** Small stores with few pages (monolith ships faster than headless below content-velocity threshold).
- **Integration:** OSS (WP plugin; headless via API to Next).
- **Compatibility:** WordPress/PHP/MySQL.
- **Deps:** Extension sprawl costs/perf.
- **Availability:** Free plugin (+paid extensions/hosting).
- **Maintenance:** Active.
- **License:** GPL-3.0.
- **Security/limits:** Extension audit + staged updates + backups; PCI via hosted checkout (Stripe) where possible.
- **Related:** Shopify, Medusa, WordPress.
- **Sources:** woocommerce.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — Medusa / Saleor (OSS headless commerce) [OSS]
- **Canonical identity:** `oss:medusa` — https://medusajs.com/ ; `oss:saleor` — https://saleor.io/
- **Category:** Commerce → Headless commerce (self-host)
- **Type:** OSS (Medusa MIT; Saleor Apache/BSL mix — verify per module) + Clouds ($49/mo exemplar)
- **Official URL:** https://medusajs.com/
- **Description:** Products/carts/promotions/regions + admin; full-open-source exemplar stack: Strapi+Medusa+Astro; enterprise GraphQL alt: Saleor (Python, Polish-founded).
- **Contents inspected:** 2026 headless stacks (Medusa Cloud $49 + Vercel + Sanity $99 + Stripe 2.9% + Algolia $30 ≈$250/mo exemplar).
- **Capabilities:** Composable modules, multi-region, Stripe/Adyen plugins.
- **Usage domain:** Scale where Shopify fees/control chafe + team can operate infra.
- **Integration:** OSS (Node/PG/Redis; Next/Astro front + Sanity refs).
- **Compatibility:** PG/Redis; Docker/K8s.
- **Deps:** You operate DB/cache/search/payments wiring (2–3wk deploy exemplar).
- **Availability:** Free OSS (+Cloud SaaS).
- **Maintenance:** Active (Medusa v2 2024–26).
- **License:** MIT (Medusa core) / mixed (Saleor — check EE).
- **Security/limits:** Own PCI scope review (prefer hosted payment elements); sign webhooks; isolate admin.
- **Related:** Shopify, commercetools, Stripe.
- **Sources:** medusajs.com/saleor.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — Stripe (payments) + cart-pricing rule [SERVICE]
- **Canonical identity:** `service:stripe` — https://stripe.com/ (Payment Element / Checkout / webhooks)
- **Category:** Commerce → Payments
- **Type:** Service (2.9%+30¢ exemplar US)
- **Official URL:** https://stripe.com/
- **Description:** Hosted Checkout/Payment Element (SAQ-A PCI path), webhooks (`checkout.session.completed`), idempotency keys, 3DS/SCA; cart math authoritative server-side (never trust client totals).
- **Contents inspected:** Search-verified standard; headless stacks all terminate at Stripe.
- **Capabilities:** Subscriptions, coupons, multi-party (Connect), dispute flow.
- **Usage domain:** Every headless/monolith checkout (Shopify/Woo/Medusa all offer Stripe).
- **Integration:** service (SDK + webhook endpoint + signing secret in Vault).
- **Compatibility:** All stacks.
- **Deps:** Webhook idempotency + reconciliation job.
- **Availability:** SaaS (per-transaction).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Verify `stripe-signature`; price server-side from commerce source; never oversell — disable Add-to-cart at zero inventory (Sanity event pattern).
- **Related:** Shopify Payments, PayPal/Adyen alts.
- **Sources:** stripe.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 21 — Resend / SendGrid / Mailchimp (transactional + lifecycle email) [SERVICE]
- **Canonical identity:** `service:resend` — https://resend.com/ ; `service:sendgrid` — https://sendgrid.com/ ; `service:mailchimp` — https://mailchimp.com/
- **Category:** Commerce → Email
- **Type:** Service (API + SaaS)
- **Official URL:** https://resend.com/
- **Description:** Resend: dev-first transactional (React Email); SendGrid: scale SMTP/API + templates; Mailchimp: lifecycle/brand campaigns; all need SPF/DKIM/DMARC + bounce handling.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Order/receipt/shipping triggers, double-opt-in, suppression lists.
- **Usage domain:** Receipts + abandon + drops coordinated with CMS scheduled publishing.
- **Integration:** service (API key in Vault; webhook → suppression; Inngest/Trigger.dev for durability).
- **Compatibility:** Any stack.
- **Deps:** DNS auth + warmup for bulk.
- **Availability:** SaaS (free-limited → paid).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Never expose keys client-side; sign webhooks; honor unsub/consent per campaign.
- **Related:** Ghost/Mailgun, Supabase Auth emails.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 22 — Localization + site-search + feedback + monitoring bundle [UTILITY/SERVICE mix]
- **Canonical identity:** `bundle:l10n-search-feedback-monitor` (next-intl/i18next/Crowdin + Algolia/Meilisearch/Typesense + feedback + Uptime-Kuma)
- **Category:** Growth → L10n / search / feedback / monitoring
- **Type:** OSS utilities + services
- **Official URL:** https://next-intl.dev/ · https://www.algolia.com/ · https://www.meilisearch.com/ · https://typesense.org/
- **Description:** L10n: next-intl (App-Router native) / i18next + Crowdin vendor pipeline (Contentful strongest for vendor flow; Sanity per-field/per-doc native); Search: Algolia SaaS ($30/mo exemplar) / Meilisearch+Typesense self-host OSS; Feedback: PostHog surveys/Canny/Featurebase; Monitoring: Uptime-Kuma self-host + GSC/CrUX watch.
- **Contents inspected:** 2026 CMS/headless guides (localization + search cost exemplars) + monitoring patterns.
- **Capabilities:** hreflang routing, translated slugs, typo-tolerant faceted search, NPS/bug loops, 5xx/keyword-rank alerts.
- **Usage domain:** Every content/commerce site post-MVP.
- **Integration:** utility/service (next-intl middleware; search index built from CMS+commerce refs on publish webhook; feedback snippet behind consent).
- **Compatibility:** Next/Astro + CMS webhooks.
- **Deps:** Translation memory + index quota.
- **Availability:** OSS free + SaaS quotas.
- **Maintenance:** Active (all lines).
- **License:** MIT/Apache (OSS parts); proprietary (Algolia Cloud).
- **Security/limits:** Never index PII/private previews; gate search replicas per locale/market; monitor index drift after CMS schema changes.
- **Related:** Sanity/Contentful L10n, Shopify Markets, PostHog, Uptime-Kuma.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

## Architecture rule (reference pattern — do not duplicate product data)
- CMS owns content (pages/stories/SEO); commerce owns catalogue (products/prices/inventory/checkout); frontend resolves refs live. Content caches long + webhook-revalidate; commerce caches short (or per-request for price-sensitive fields).
- When headless: Sanity+Shopify+Next (most common) · Strapi+Medusa+Astro (full OSS) · Contentful+commercetools (enterprise) · headless-WP+Woo (content-history pragmatic). Below content-velocity threshold, monolith (Shopify few-pages / Woo+WP) ships faster.
- Count: 22 resources.
