# Catalog 01c — Backend, Data & Platforms

> **Workstream:** Researcher #3 (depth-2 subagent) · **Research date:** 2026-10-10 (IST)
> **Scope:** Part 3.5 (backend frameworks & API systems) · 3.6 (databases, persistence, search) · 3.7 (application services) · 3.8 (website platforms & generators) · 3.9 (architecture & software engineering references)
> **Mode:** Read-only research. No installs, builds, or executions performed. No recommendations made.

## Method

- Live web research via `browser.search` (30 themed searches) and `browser.open` on primary sources (official docs, repo READMEs, official EOL notices).
- Primary sources preferred; where only secondary coverage existed, the record is marked **Partially verified** and corroborated across ≥2 independent sources where possible.
- Verification labels used exactly: **Verified** (primary source opened this session), **Partially verified** (identity/type/status confirmed via search evidence, primary not opened), **Unverified**, **Corrected** (a prior/widely-held claim fixed with evidence), **Archived** (project retired or EOL), **Inaccessible**, **Historical**, **Unresolved**.
- Unknowns are stated as "Not verified" / "Not publicly documented" / "Not applicable" / "Unresolved" — never invented.
- **DEDUP (cross-reference only, not re-researched):** `cnoe-io/openapi-mcp-codegen`, `ck Anthony/openapi-mcp`, `awslabs/openapi-mcp-server` (new alternatives recorded in §3.5.9); `cloudflare/skills`, `composiohq/skills`, `upstash/context7` (skills workstream).
- For official URLs, only verbatim URLs returned by tools are used; otherwise the field reads "Not verified in this session".
- A compact per-record schema is used; a few subsections add an "also observed" table for long-tail items (each row still carries a verification label and source) instead of full records.

## Search themes run

Backend frameworks (Express/FastAPI/Django/NestJS/Laravel/Spring Boot/Rails/Gin/Hono/Fastify/Encore); API gateways (Kong/Traefik/APISIX/Envoy/KrakenD/Tyk); API mocking & contract testing (Prism/Schemathesis/Spectral/Pact/MSW/Microcks); self-hosted auth (Keycloak/Ory/better-auth/Auth.js/ZITADEL); GraphQL servers (Apollo/Hasura/PostGraphile/Mercurius/Yoga); OpenAPI→MCP alternatives; durable execution & queues (Temporal/Inngest/Trigger.dev/BullMQ/Celery/Sidekiq/Restate/Hatchet/QStash); message brokers (Kafka/RabbitMQ/NATS/Redpanda/Pulsar); database MCP servers; Prisma vs Drizzle; serverless Postgres (Neon/Supabase/PlanetScale/Turso/Prisma Postgres); graph DBs (Neo4j/SurrealDB/Kùzu); vector DBs (Qdrant/Weaviate/Pinecone/pgvector/Chroma/Milvus); search engines (Elasticsearch/OpenSearch/Typesense/Meilisearch/Algolia); migrations (Atlas/Flyway/Alembic/Liquibase); transactional email (Resend/Postmark/SendGrid/Mailgun/SES/Mailtrap/Plunk); merchant-of-record payments (Stripe/Paddle/Lemon Squeezy/Polar); headless CMS (Payload/Sanity/Strapi/Contentful/Directus); notifications (Knock/Courier/Novu/OneSignal); maps (Mapbox/Google/MapLibre/Leaflet); analytics & feature flags (PostHog/Mixpanel/Amplitude/LaunchDarkly/GrowthBook/Unleash); headless commerce (Medusa/Saleor/Shopify/Vendure); i18n (Crowdin/Lokalise/Tolgee); scheduling (Cal.com/Nylas/Cronofy); media APIs (Cloudinary/Mux/Uploadthing/ImageKit); public datasets; AI website builders (Lovable/Bolt/v0/Replit); CRUD generators (Refine/Amplication); screenshot-to-code; SaaS boilerplates; system-design references (system-design-primer/nodebestpractices/bulletproof-react/realworld); ADR tooling; dependency analysis; Stytch/Twilio status; Cal.com license change; MongoDB Atlas App Services EOL.

---

# 3.5 Backend frameworks and API systems

## 3.5.1 Backend languages & frameworks

### 3.5.1.1 Express.js
- **Canonical identity:** Open-source Node.js web framework (OpenJS Foundation stewardship).
- **Category:** 3.5.1 · **Type:** Open-source library/framework (npm).
- **Official URL:** https://expressjs.com
- **Description:** Minimal, unopinionated Node.js HTTP framework; the de facto standard server framework for Node.js and the backend of MERN/MEAN stacks.
- **Contents inspected:** Wikipedia infobox + project history (via search), Express 5 migration notes referenced in a 2026 backend skill file (async error handling native in v5).
- **Actual capabilities:** Routing, middleware pipeline, template engines, static serving; ecosystem (middleware, ORMs, auth) supplies the rest.
- **Usage domain:** REST APIs, microservices, server-rendered apps, real-time apps (with Socket.IO).
- **Integration method:** npm package; default HTTP adapter under NestJS (swappable to Fastify).
- **Dependencies:** Node.js runtime.
- **Availability:** Active open source. **Maintenance:** Express 5.x line current (5.2.1 reported Dec 2025). **License:** MIT.
- **Limitations:** Minimal by design — auth, validation, ORM all third-party; slower than Fastify/Hono in benchmarks (per secondary sources).
- **Related resources:** NestJS (3.5.1.4), Fastify (3.5.1.2), Koa.
- **Sources:** https://en.wikipedia.org/wiki/Express.js · https://github.com/ashutoshx29/dragonquest/blob/HEAD/.cursor/skills/js-backend-expert/SKILL.md · https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.5.1.2 Fastify
- **Canonical identity:** Open-source Node.js web framework (OpenJS Foundation).
- **Category:** 3.5.1 · **Type:** Open-source library/framework (npm).
- **Official URL:** https://fastify.io
- **Description:** Performance-focused Node.js framework with a plugin architecture and built-in JSON-schema validation/serialization.
- **Contents inspected:** Framework comparison tables and skill docs (2026); not the primary docs site directly.
- **Actual capabilities:** Routing, schema-based validation, plugin ecosystem, logging; usable as the underlying HTTP platform for NestJS.
- **Usage domain:** High-throughput JSON APIs, microservices.
- **Integration method:** npm package; `@nestjs/platform-fastify` adapter for NestJS.
- **Dependencies:** Node.js runtime.
- **Availability:** Active open source. **Maintenance:** Actively maintained (per ecosystem references). **License:** MIT (per common knowledge — not verified in this session; marked accordingly).
- **Limitations:** Smaller middleware ecosystem than Express.
- **Related resources:** Express.js, NestJS, Hono.
- **Sources:** https://encore.dev/articles/nestjs-vs-fastify-vs-hono · https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.1.3 Hono
- **Canonical identity:** `honojs/hono` — web framework built on Web Standards.
- **Category:** 3.5.1 · **Type:** Open-source library/framework (npm).
- **Official URL:** https://github.com/honojs/hono/ (docs at hono.dev per its README).
- **Description:** Ultralight, dependency-free TypeScript framework on Web Standard APIs; multi-runtime (Cloudflare Workers, Deno, Bun, Node, AWS Lambda).
- **Contents inspected:** GitHub README via search result (features list, license line).
- **Actual capabilities:** Routers (RegExpRouter etc.), middleware (built-in + third-party), `hono/tiny` preset <12kB; JSX support; RPC mode.
- **Usage domain:** Edge runtimes, serverless APIs, lightweight services.
- **Integration method:** `npm create hono@latest`.
- **Dependencies:** None (Web Standards only).
- **Availability:** Active open source. **Maintenance:** Active. **License:** MIT (per README).
- **Limitations:** Young ecosystem vs Express; edge-runtime constraints (no Node built-ins on some runtimes).
- **Related resources:** Elysia, Encore (edge note), Cloudflare Workers (3.5.7).
- **Sources:** https://github.com/honojs/hono/ · https://encore.dev/articles/nestjs-vs-fastify-vs-hono
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.5.1.4 NestJS
- **Canonical identity:** `nestjs/nest` — progressive Node.js framework.
- **Category:** 3.5.1 · **Type:** Open-source framework (npm, CLI).
- **Official URL:** https://nestjs.com (docs: https://docs.nestjs.com).
- **Description:** Opinionated, Angular-inspired TypeScript framework with modules, dependency injection, guards, interceptors; ships adapters for Express and Fastify.
- **Contents inspected:** GitHub repo page via search (README excerpt: getting started, Discord, MIT license, NestJS Observe announcement).
- **Actual capabilities:** REST + GraphQL + WebSocket + microservice transports; validation (class-validator), caching, task scheduling, queues (Bull); testing with Jest/SuperTest.
- **Usage domain:** Enterprise Node.js backends, structured monoliths, microservices.
- **Integration method:** `@nestjs/cli`; `nest new`.
- **Dependencies:** Node.js; RxJS; platform adapter (Express default, Fastify optional).
- **Availability:** Active open source; commercial support/consulting offered; NestJS Observe (official observability, free ≤300k events/mo) announced. **Maintenance:** Active. **License:** MIT.
- **Limitations:** Heavier ceremony than minimal frameworks; Express-adapter performance overhead vs Fastify adapter.
- **Related resources:** Express.js, Fastify, tRPC.
- **Sources:** https://github.Com/nestjs/nest · https://dev.to/krtirtho/nestjs-the-framework-of-nodejs-part-1-gl7
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.5.1.5 FastAPI
- **Canonical identity:** FastAPI — modern Python ASGI web framework (Sebastián Ramírez).
- **Category:** 3.5.1 · **Type:** Open-source library/framework (PyPI).
- **Official URL:** https://fastapi.tiangolo.com
- **Description:** Type-hint-driven Python framework with automatic request validation (Pydantic) and auto-generated OpenAPI docs (Swagger UI at `/docs`, ReDoc at `/redoc`).
- **Contents inspected:** Tutorial walkthroughs (2026), framework comparison tables.
- **Actual capabilities:** Async (ASGI), dependency injection, OAuth2/security utilities, background tasks, WebSockets; OpenAPI/JSON Schema emitted by default.
- **Usage domain:** Data/ML APIs, microservices, AI-agent backends.
- **Integration method:** `pip install fastapi`; run with Uvicorn/Hypercorn.
- **Dependencies:** Starlette, Pydantic.
- **Availability:** Active open source. **Maintenance:** Active. **License:** MIT (not re-verified in this session — marked accordingly).
- **Limitations:** No built-in admin panel or ORM (pairs with SQLAlchemy); Pydantic v2 migration churn noted by users.
- **Related resources:** Django, Flask, Starlette, Pydantic.
- **Sources:** https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md · https://medium.com/@atharvjaiswal56/i-tested-5-python-web-frameworks-in-2026-heres-what-actually-works-a3e412d523e8 · https://dev.to/drxven/fastapi-your-first-production-ready-api-o6b
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.5.1.6 Django
- **Canonical identity:** Django — Python web framework (Django Software Foundation).
- **Category:** 3.5.1 · **Type:** Open-source framework (PyPI).
- **Official URL:** https://www.djangoproject.com
- **Description:** Batteries-included Python framework: ORM, admin panel, auth, migrations, security defaults (CSRF/XSS/SQL-injection protections).
- **Contents inspected:** Framework comparisons and a 2026 hands-on review (admin panel, DRF, weight/ceremony notes).
- **Actual capabilities:** Full-stack: ORM, templating, forms, admin, caching, i18n; Django REST Framework (DRF) for APIs; async support.
- **Usage domain:** Content apps, dashboards, CRUD-heavy SaaS, enterprise Python.
- **Integration method:** `pip install django`; `django-admin startproject`.
- **Dependencies:** Python; DB driver.
- **Availability:** Active open source. **Maintenance:** Active LTS cadence. **License:** BSD (not re-verified in this session).
- **Limitations:** Monolithic feel for microservices; heavier startup/boilerplate than FastAPI for pure APIs.
- **Related resources:** Django REST Framework, FastAPI, Flask, Celery (3.5.8).
- **Sources:** https://medium.com/@atharvjaiswal56/i-tested-5-python-web-frameworks-in-2026-heres-what-actually-works-a3e412d523e8 · https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.5.1.7 Flask
- **Canonical identity:** Flask — Python micro web framework (Pallets).
- **Category:** 3.5.1 · **Type:** Open-source library/framework (PyPI).
- **Official URL:** https://flask.palletsprojects.com
- **Description:** Minimal WSGI framework; routing + request handling, everything else via extensions.
- **Contents inspected:** Ecosystem listings only (spec-kit fallback table).
- **Actual capabilities:** Routing, Jinja templating, dev server; extensions for ORM/auth/API.
- **Usage domain:** Small services, prototypes, ML model serving.
- **Integration method:** `pip install flask`.
- **Dependencies:** Werkzeug, Jinja2.
- **Availability:** Active open source. **Maintenance:** Maintained (Pallets). **License:** BSD (not re-verified in this session).
- **Limitations:** DIY architecture at scale; sync-first (async possible but not native-first).
- **Related resources:** FastAPI, Django.
- **Sources:** https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.1.8 Ruby on Rails
- **Canonical identity:** Ruby on Rails — full-stack web framework (Basecamp/37signals lineage, MIT).
- **Category:** 3.5.1 · **Type:** Open-source framework (RubyGems).
- **Official URL:** Not verified in this session.
- **Description:** Convention-over-configuration full-stack framework: ActiveRecord ORM, Action Pack, Hotwire; scaffold-driven productivity.
- **Contents inspected:** Framework roundups (2026); flexibility noted for SaaS/MVPs (Spree/Solidus commerce on Rails).
- **Actual capabilities:** ORM, migrations, mailers, jobs (Active Job), WebSockets (Action Cable), asset pipeline.
- **Usage domain:** SaaS MVPs, marketplaces, e-commerce (Spree/Solidus).
- **Integration method:** `gem install rails`; `rails new`.
- **Dependencies:** Ruby runtime.
- **Availability:** Active open source. **Maintenance:** Active. **License:** MIT (not re-verified in this session).
- **Limitations:** Ruby hiring pool smaller than JS/Python; monolith scaling patterns required at scale.
- **Related resources:** Laravel, Django, Hotwire.
- **Sources:** https://dev.to/quokka_labs/best-backend-frameworks-for-building-fast-scalable-web-apps-4n52 · https://github.com/torkiv-labs/nexuq/blob/HEAD/docs/research/competitive-analysis-headless-commerce-2026-08-27.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.1.9 Laravel
- **Canonical identity:** Laravel — PHP web framework.
- **Category:** 3.5.1 · **Type:** Open-source framework (Composer).
- **Official URL:** https://laravel.com (per vendor listing in search results).
- **Description:** Expressive PHP framework with Artisan CLI, Eloquent ORM, queues, Blade templates; Octane for high performance.
- **Contents inspected:** Vendor/SEO listings and comparison tables only.
- **Actual capabilities:** ORM, migrations, auth scaffolding, queues, scheduling, broadcasting, testing helpers.
- **Usage domain:** SaaS, CMS-like apps, agencies, PHP shops.
- **Integration method:** Composer; `laravel new`.
- **Dependencies:** PHP runtime.
- **Availability:** Active open source. **Maintenance:** Active. **License:** MIT (not re-verified in this session).
- **Limitations:** PHP ecosystem perception; async story weaker than Node/Go.
- **Related resources:** Symfony, Rails, Statamic (CMS).
- **Sources:** https://slashdot.org/software/comparison/Django-vs-FastAPI-vs-Laravel/ · https://github.com/prauga/flexdoc/blob/HEAD/docs/framework-coverage-roadmap.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.1.10 Spring Boot
- **Canonical identity:** Spring Boot — Java application framework (Broadcom/Spring).
- **Category:** 3.5.1 · **Type:** Open-source framework (Maven/Gradle).
- **Official URL:** https://spring.io/projects/spring-boot
- **Description:** Opinionated Java framework with auto-configuration, embedded servers (Tomcat/Jetty/Undertow), and "starters" for web, data, security, messaging (Kafka/RabbitMQ), batch.
- **Contents inspected:** Integration guides (Kafka/RabbitMQ starters) and ecosystem references.
- **Actual capabilities:** REST (Spring MVC/WebFlux), data access, security, scheduling, messaging, observability; Spring Initializr scaffolding.
- **Usage domain:** Enterprise/fintech backends, large distributed systems.
- **Integration method:** Spring Initializr; Maven/Gradle starters.
- **Dependencies:** JVM.
- **Availability:** Active open source. **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Memory footprint and startup time vs Go/Node; configuration complexity at scale.
- **Related resources:** Quarkus, Micronaut, ASP.NET Core.
- **Sources:** https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md · https://dev.to/mosesmucyo/spring-boot-kafka-vs-rabbitmq-a-deep-dive-into-event-driven-microservices-6gd
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.5.1.11 ASP.NET Core
- **Canonical identity:** ASP.NET Core — cross-platform .NET web framework (Microsoft).
- **Category:** 3.5.1 · **Type:** Open-source framework (NuGet).
- **Official URL:** Not verified in this session.
- **Description:** High-performance C# framework (Kestrel server) for APIs and web apps; first-class OpenAPI support in recent versions.
- **Contents inspected:** Ecosystem references only (framework roundups).
- **Actual capabilities:** Minimal APIs + controllers, Entity Framework Core, SignalR (real-time), gRPC, auth.
- **Usage domain:** Enterprise .NET shops, Windows/Azure-aligned orgs, high-perf APIs.
- **Integration method:** `dotnet new webapi`; NuGet.
- **Dependencies:** .NET runtime.
- **Availability:** Active open source. **Maintenance:** Active LTS cadence. **License:** MIT/Apache mix (not re-verified in this session).
- **Limitations:** Smaller startup/indie community than Node/Python.
- **Related resources:** Spring Boot, FastAPI.
- **Sources:** https://dev.to/quokka_labs/best-backend-frameworks-for-building-fast-scalable-web-apps-4n52 · https://github.com/prauga/flexdoc/blob/HEAD/docs/framework-coverage-roadmap.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.1.12 Gin
- **Canonical identity:** Gin — Go HTTP web framework.
- **Category:** 3.5.1 · **Type:** Open-source library/framework (Go modules).
- **Official URL:** https://gin-gonic.com
- **Description:** Minimal, fast Go framework with martini-like routing, middleware, JSON binding/validation.
- **Contents inspected:** Ecosystem references and framework tables.
- **Actual capabilities:** Routing, middleware, rendering, validation; pairs with Go's stdlib `net/http`.
- **Usage domain:** API gateways, low-latency services, cloud-native tooling.
- **Integration method:** Go modules.
- **Dependencies:** Go toolchain.
- **Availability:** Active open source. **Maintenance:** Maintained. **License:** MIT (not re-verified in this session).
- **Limitations:** Minimal — no ORM/auth; alternatives: Echo, Fiber, Chi, stdlib.
- **Related resources:** Echo, Fiber, Chi, Axum (Rust).
- **Sources:** https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md · https://dev.to/quokka_labs/best-backend-frameworks-for-building-fast-scalable-web-apps-4n52
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.1.13 Encore
- **Canonical identity:** Encore — backend framework + developer cloud (`encoredev/encore`; Encore.ts / Encore.go).
- **Category:** 3.5.1 (+ 3.6 agent-schema relevance) · **Type:** Open-source framework + optional hosted cloud.
- **Official URL:** https://encore.dev
- **Description:** Type-safe backend framework where infrastructure (databases, pub/sub, caches, cron, object storage, secrets) is declared as typed code primitives; the framework provisions matching infra locally and in cloud. Auto-generates API docs, OpenAPI, and typed client SDKs from the same types. Ships an MCP server for AI agents (per third-party API directory).
- **Contents inspected:** encore.dev comparison article (infra-from-code, 12k+ GitHub stars claim, Groupon production use), api-evangelist/encore-dev directory entry (MCP server note), dev.to deep-dive.
- **Actual capabilities:** Service definition, typed service-to-service calls, SQL databases with migrations, pub/sub topics, cron, caching, secrets; local dev dashboard with tracing; deploy to own AWS/GCP or Encore Cloud; Docker export for self-hosting.
- **Usage domain:** Type-safe distributed systems, microservices, teams wanting infra-from-code.
- **Integration method:** `brew install encoredev/tap/encore`; `encore app create`; `encore run`.
- **Dependencies:** Encore CLI; cloud account for managed deploy.
- **Availability:** Open-source framework; Encore Cloud (managed). **Maintenance:** Active. **License:** Open source (specific license not verified in this session).
- **Limitations:** Opinionated — infra semantics only, not arbitrary cloud config; Node-based (edge use → Hono instead, per encore.dev's own guidance); framework migration cost from existing NestJS/Fastify codebases.
- **Related resources:** NestJS, Hono; Temporal (workflows); see §3.6.10 gap analysis (agent-readable backend contracts).
- **Sources:** https://encore.dev/articles/nestjs-vs-fastify-vs-hono · https://github.com/api-evangelist/encore-dev · https://dev.to/0012303/encore-has-a-free-backend-framework-type-safe-apis-with-auto-generated-infrastructure-3edc
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.5.2 GraphQL servers & backends

### 3.5.2.1 Apollo Server
- **Canonical identity:** Apollo Server — GraphQL server library (Apollo GraphQL).
- **Category:** 3.5.2 · **Type:** Open-source library (npm) + commercial platform (Apollo GraphOS).
- **Official URL:** Not verified in this session.
- **Description:** Self-hosted GraphQL server for Node.js; pairs with Apollo Client and the Apollo GraphOS platform (schema registry, gateway/federation).
- **Contents inspected:** Ecosystem references (GraphQL roundups, gateway lists).
- **Actual capabilities:** Schema-first or code-first servers, federation subgraphs/gateways, plugins, caching; ecosystem: Apollo Client, Studio/GraphOS.
- **Usage domain:** GraphQL APIs, federated supergraphs.
- **Integration method:** npm; `startStandaloneServer` or framework integrations (Express/Fastify/NestJS).
- **Dependencies:** Node.js.
- **Availability:** Open source + paid GraphOS tiers. **Maintenance:** Active. **License:** MIT for server (not re-verified in this session).
- **Limitations:** Federation adds operational complexity; REST often simpler for CRUD.
- **Related resources:** Apollo Client, Apollo Federation, GraphQL Yoga, Hasura.
- **Sources:** Search results on GraphQL servers/gateways (multiple roundups, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.2.2 Hasura
- **Canonical identity:** Hasura — instant GraphQL/REST API engine over databases.
- **Category:** 3.5.2 · **Type:** Open-source engine (Haskell/Go) + hosted cloud (Hasura Cloud).
- **Official URL:** Not verified in this session.
- **Description:** Generates type-safe GraphQL and REST APIs from database schemas (Postgres-first, plus others); metadata-driven with console UI, auth webhooks, remote schemas, event triggers.
- **Contents inspected:** Comparison content on GraphQL servers (not primary docs).
- **Actual capabilities:** Auto-generated CRUD, subscriptions, role-based row-level auth, caching, API limits; metadata export for version control.
- **Usage domain:** Rapid API layers over existing Postgres, data APIs, internal tools.
- **Integration method:** Docker; Hasura Cloud; CLI for metadata migrations.
- **Dependencies:** Database (Postgres primary).
- **Availability:** Open source (core) + hosted. **Maintenance:** Active. **License:** Apache 2.0 for core (not re-verified in this session).
- **Limitations:** Business logic lives in actions/remote schemas; complex auth needs custom webhooks.
- **Related resources:** PostGraphile, Prisma, Supabase (auto-APIs).
- **Sources:** GraphQL server roundups (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.2.3 PostGraphile
- **Canonical identity:** PostGraphile — instant GraphQL API from PostgreSQL schema.
- **Category:** 3.5.2 · **Type:** Open-source library/CLI (npm).
- **Official URL:** Not verified in this session.
- **Description:** Introspects a Postgres schema and serves a full GraphQL API (CRUD, relations, RLS-aware auth) with plugin extensibility.
- **Contents inspected:** GraphQL roundups only.
- **Actual capabilities:** Schema introspection, row-level security integration, plugins, subscriptions.
- **Usage domain:** Postgres-first teams wanting GraphQL without hand-writing resolvers.
- **Integration method:** CLI or Node.js library; Docker.
- **Dependencies:** PostgreSQL.
- **Availability:** Open source. **Maintenance:** Maintained (v5 line). **License:** MIT (not re-verified in this session).
- **Limitations:** Postgres-only; schema design becomes API design (needs discipline).
- **Related resources:** Hasura, Prisma, pg_graphql (Supabase).
- **Sources:** GraphQL server roundups (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.2.4 GraphQL Yoga
- **Canonical identity:** GraphQL Yoga — GraphQL server (The Guild).
- **Category:** 3.5.2 · **Type:** Open-source library (npm).
- **Official URL:** Not verified in this session.
- **Description:** Lightweight, plugin-based GraphQL server on modern fetch/Web Standards; Envelop plugin ecosystem.
- **Contents inspected:** Guild ecosystem references in search results.
- **Actual capabilities:** Yoga server, subscriptions, file uploads, persisted operations; integrates with Envelop plugins (auth, caching, tracing).
- **Usage domain:** Modern Node/edge GraphQL services.
- **Integration method:** npm; framework adapters.
- **Dependencies:** Node/edge runtime.
- **Availability:** Open source. **Maintenance:** Active. **License:** MIT (not re-verified in this session).
- **Limitations:** Smaller community than Apollo.
- **Related resources:** Apollo Server, Mercurius (Fastify), Envelop.
- **Sources:** GraphQL tooling roundups (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.5.3 RPC & service-to-service

### 3.5.3.1 tRPC
- **Canonical identity:** tRPC — end-to-end typesafe RPC (TypeScript).
- **Category:** 3.5.3 · **Type:** Open-source library (npm).
- **Official URL:** Not verified in this session.
- **Description:** TypeScript RPC framework: define procedures server-side, get fully typed client calls with no codegen step; uses JSON over HTTP, integrates with React Query.
- **Contents inspected:** Stack comparisons and starter references.
- **Actual capabilities:** Routers, input validation (Zod etc.), middleware, subscriptions; adapters for Express/Fastify/Next.js/Fetch.
- **Usage domain:** Full-stack TypeScript apps (T3 stack), internal APIs where TS spans client+server.
- **Integration method:** npm (`@trpc/server`, `@trpc/client`).
- **Dependencies:** TypeScript; framework adapter.
- **Availability:** Open source. **Maintenance:** Active. **License:** MIT (not re-verified in this session).
- **Limitations:** TypeScript-only; not a public-API contract format (no OpenAPI by default); versioning is manual.
- **Related resources:** GraphQL (alternative), ConnectRPC, OpenAPI.
- **Sources:** Full-stack TypeScript stack content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.3.2 gRPC / ConnectRPC
- **Canonical identity:** gRPC (CNCF) / ConnectRPC (Buf) — RPC frameworks over HTTP/2.
- **Category:** 3.5.3 · **Type:** Open-source frameworks + spec (protobuf).
- **Official URL:** Not verified in this session.
- **Description:** gRPC: contract-first RPC with Protocol Buffers, codegen for many languages, streaming. ConnectRPC: simpler protocol (Connect/Connect-ES) that works over HTTP/1.1 with browser-friendly semantics and gRPC compatibility.
- **Contents inspected:** Gateway and service-mesh content; no primary spec read.
- **Actual capabilities:** IDL (`.proto`), unary + streaming calls, interceptors, load balancing, health checks, reflection.
- **Usage domain:** Polyglot microservices, ML inference services, mobile backends.
- **Integration method:** `protoc`/Buf codegen; language runtimes.
- **Dependencies:** Protobuf toolchain.
- **Availability:** Open source (CNCF). **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Binary protocol needs tooling (grpcurl, BloomRPC) for debugging; browser support requires proxies (ConnectRPC eases this).
- **Related resources:** Buf (schema registry), Envoy (gRPC proxying), tRPC.
- **Sources:** API gateway and microservice references (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.5.4 API gateways

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.5.4.1 | Kong Gateway | Kong Inc. — Lua/OpenResty-based gateway; Kong Ingress Controller for K8s | Open source (core) + Enterprise | Traffic control, auth plugins, rate limiting, transformations | Search roundups (2026) | Partially verified — Medium |
| 3.5.4.2 | Apache APISIX | Apache Software Foundation — dynamic, etcd-backed gateway | Open source (Apache 2.0) | Dynamic routing, hot-reload plugins, gRPC/GraphQL proxying; comparison guide at https://apisix.apache.org/learning-center/open-source-api-gateway-comparison/ (verbatim URL as returned; includes tracking params) | https://apisix.apache.org/learning-center/open-source-api-gateway-comparison/ | Partially verified — Medium |
| 3.5.4.3 | Traefik | Traefik Labs — cloud-native reverse proxy / ingress | Open source (MIT) + Enterprise | Auto service discovery (Docker/K8s), Let's Encrypt, middleware chain | Search roundups (2026) | Partially verified — Medium |
| 3.5.4.4 | KrakenD | KrakenD (ex-Lura) — declarative, stateless API gateway | Open source (Apache 2.0) + Enterprise | JSON config, request aggregation/composition, no DB required | Search roundups (2026) | Partially verified — Medium |
| 3.5.4.5 | Tyk | Tyk — API gateway & management platform | Open source (MPL) + Cloud/Enterprise | Gateway, dashboard, developer portal; also ships an OpenAPI→MCP tool (see 3.5.9.2) | Search roundups (2026) | Partially verified — Medium |

## 3.5.5 OpenAPI, schema-first design, codegen, contract testing

### 3.5.5.1 OpenAPI Specification
- **Canonical identity:** OpenAPI Specification (OAS) — Linux Foundation / OpenAPI Initiative.
- **Category:** 3.5.5 · **Type:** Open specification (machine-readable API contracts: JSON/YAML).
- **Official URL:** Not verified in this session.
- **Description:** Standard description format for REST APIs: paths, operations, schemas, security; versions 3.0/3.1 (JSON Schema aligned).
- **Contents inspected:** Ecosystem usage (codegen tools, MCP converters, mocking tools all consume OAS).
- **Actual capabilities:** Contract format; tooling reads/writes/validates it; underpins Swagger UI, codegen, Prism mocks, Schemathesis tests.
- **Usage domain:** REST API contracts, SDK generation, docs, testing, agent tool grounding.
- **Integration method:** Author YAML/JSON; validate with Spectral; serve via Swagger UI/ReDoc.
- **Dependencies:** None (spec).
- **Availability:** Open standard. **Maintenance:** Active (OAI). **License:** Apache 2.0 for the spec text (not re-verified in this session).
- **Limitations:** REST-shaped; does not describe async/event APIs (use AsyncAPI).
- **Related resources:** AsyncAPI, JSON Schema, Swagger UI, openapi-generator.
- **Sources:** Tooling ecosystems (search, 2026); https://scalar.com/learn/mcp/generate-mcp-server-from-openapi
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.5.5.2 Swagger UI / ReDoc / Scalar
- **Canonical identity:** API documentation renderers for OpenAPI.
- **Category:** 3.5.5 · **Type:** Open-source tools (Swagger UI — SmartBear/Apache 2.0; ReDoc — Redocly; Scalar — open source).
- **Official URL:** Scalar MCP guide: https://scalar.com/learn/mcp/generate-mcp-server-from-openapi (verbatim).
- **Description:** Interactive API reference UIs generated from OpenAPI documents; Scalar also publishes OpenAPI→MCP guidance.
- **Contents inspected:** Scalar's OpenAPI→MCP guide (referenced, not opened).
- **Actual capabilities:** Render/try-it docs; Scalar: API client + MCP server generation from OpenAPI.
- **Usage domain:** Developer portals, API docs, agent tool bootstrapping.
- **Integration method:** Embed JS bundle; point at OpenAPI JSON/YAML URL.
- **Dependencies:** An OpenAPI document.
- **Availability:** Open source. **Maintenance:** Active. **License:** Apache 2.0 / MIT variants (not re-verified per-tool).
- **Limitations:** Docs quality bounded by spec quality.
- **Related resources:** Stoplight Elements, Fern docs.
- **Sources:** https://scalar.com/learn/mcp/generate-mcp-server-from-openapi · https://geekflare.com/guides/api-sdk-generators/
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.3 openapi-generator
- **Canonical identity:** `OpenAPITools/openapi-generator` — code generator from OpenAPI.
- **Category:** 3.5.5 · **Type:** Open-source CLI/tool (Java).
- **Official URL:** Not verified in this session.
- **Description:** Community-driven generator producing client SDKs, server stubs, and docs for 50+ languages/frameworks from OpenAPI specs.
- **Contents inspected:** Referenced in API SDK generator guides and comparisons.
- **Actual capabilities:** Generators for clients/servers/docs; templating; online + CLI + Docker.
- **Usage domain:** SDK publishing, server scaffolding, docs.
- **Integration method:** CLI/Jar/Docker; Maven/Gradle/npm plugins.
- **Dependencies:** Java runtime.
- **Availability:** Open source. **Maintenance:** Active community. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Generated code needs customization hooks; template drift across versions.
- **Related resources:** Kiota, Fern, Speakeasy, Orval.
- **Sources:** https://geekflare.com/guides/api-sdk-generators/ · https://taskade.com/blog/openapi-to-mcp-code-generator
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.4 Fern & Speakeasy (modern API SDK platforms)
- **Canonical identity:** Fern (buildwithfern.com) — API docs + SDK generation; Speakeasy (speakeasy.com) — SDK generation platform.
- **Category:** 3.5.5 · **Type:** Commercial platforms with open-source generators.
- **Official URL:** Not verified in this session.
- **Description:** Next-gen codegen: Fern generates docs + idiomatic SDKs (TS/Python/Go/Java/Ruby/C#) from OpenAPI; Speakeasy similar, with Terraform providers and MCP-relevant outputs.
- **Contents inspected:** Search comparisons only.
- **Actual capabilities:** SDK generation, docs sites, versioning, CI integration.
- **Usage domain:** API-first companies shipping first-class SDKs.
- **Integration method:** CLI + GitHub Actions; config in repo.
- **Dependencies:** OpenAPI spec.
- **Availability:** SaaS with free tiers; generators open source. **Maintenance:** Active. **License:** Generators open source (specific licenses not verified in this session).
- **Limitations:** Advanced features paywalled; lock-in to their config format.
- **Related resources:** openapi-generator, Kiota, Stainless.
- **Sources:** https://geekflare.com/guides/api-sdk-generators/
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.5 Kiota & Orval (lightweight client generators)
- **Canonical identity:** Kiota (Microsoft) — OpenAPI client generator; Orval — TS client generator (React Query/SWR/Zod).
- **Category:** 3.5.5 · **Type:** Open-source CLIs.
- **Official URL:** Not verified in this session.
- **Description:** Kiota: Microsoft's OpenAPI→typed-client generator (.NET/Java/TS/Python/Go/PHP/Ruby/Swift). Orval: generates TypeScript clients, mock handlers (MSW), and Zod schemas from OpenAPI.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Typed API clients; Orval adds query hooks + mocks + validation schemas.
- **Usage domain:** Frontend/backend TS clients; Microsoft-ecosystem SDKs.
- **Integration method:** CLI in build pipeline.
- **Dependencies:** OpenAPI spec.
- **Availability:** Open source. **Maintenance:** Active. **License:** MIT (not re-verified per-tool).
- **Limitations:** Output quality depends on spec completeness.
- **Related resources:** openapi-generator, Hey API.
- **Sources:** API SDK generator guides (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.6 Spectral
- **Canonical identity:** Spectral — OpenAPI/AsyncAPI linter (Stoplight).
- **Category:** 3.5.5 · **Type:** Open-source CLI (npm).
- **Official URL:** Not verified in this session.
- **Description:** Ruleset-driven linter for API description documents: style, consistency, and breaking-change rules.
- **Contents inspected:** Search references (API linting content).
- **Actual capabilities:** Built-in + custom rulesets; CI integration; works on OpenAPI 2/3, AsyncAPI, JSON Schema.
- **Usage domain:** API governance, design review automation.
- **Integration method:** CLI; CI step.
- **Dependencies:** Node.js.
- **Availability:** Open source. **Maintenance:** Maintained. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Linting only — no mocking/testing.
- **Related resources:** Optic (archived — see below), oasdiff.
- **Sources:** API linting/diff content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.7 Schemathesis
- **Canonical identity:** Schemathesis — property-based API tester from schemas.
- **Category:** 3.5.5 · **Type:** Open-source CLI (Python) + commercial.
- **Official URL:** Not verified in this session.
- **Description:** Generates test cases from OpenAPI/GraphQL schemas (Hypothesis-powered), finds crashes, validation and spec-conformance errors.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Fuzzing from schema, stateful testing, CI reports.
- **Usage domain:** API QA, contract validation.
- **Integration method:** CLI against a running API + its schema.
- **Dependencies:** Python.
- **Availability:** Open source + SaaS. **Maintenance:** Active. **License:** MPL/Apache mix (not re-verified in this session).
- **Limitations:** Needs a good schema to be effective.
- **Related resources:** Prism (mocking), Dredd (archived), Pact.
- **Sources:** API testing roundups (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.8 Prism
- **Canonical identity:** Prism — OpenAPI mock server (Stoplight).
- **Category:** 3.5.5 · **Type:** Open-source CLI/server (npm).
- **Official URL:** Not verified in this session.
- **Description:** Turns an OpenAPI document into a mock API server (example/dynamic responses) and a contract validator/proxy.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Mock server, request validation proxy, contract checks.
- **Usage domain:** Frontend dev against not-yet-built APIs; contract testing.
- **Integration method:** CLI/Docker; point at OpenAPI file.
- **Dependencies:** Node.js.
- **Availability:** Open source. **Maintenance:** Maintained. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Mock fidelity limited by examples/schemas.
- **Related resources:** MSW, Microcks, WireMock.
- **Sources:** API mocking roundups (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.9 Pact
- **Canonical identity:** Pact — consumer-driven contract testing framework.
- **Category:** 3.5.5 · **Type:** Open-source framework + PactFlow (commercial).
- **Official URL:** Not verified in this session.
- **Description:** Consumer-driven contracts: consumers define expected interactions, providers verify; language-specific implementations; PactFlow broker for CI.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Contract DSLs, provider verification, can-i-deploy gates, bi-directional (OAS) contracts.
- **Usage domain:** Microservice integration testing.
- **Integration method:** Language libraries; broker (self-host OSS or PactFlow).
- **Dependencies:** Language runtime; broker.
- **Availability:** Open source + SaaS. **Maintenance:** Active. **License:** MIT (not re-verified in this session).
- **Limitations:** Ceremony overhead; best with disciplined versioning.
- **Related resources:** Spring Cloud Contract, Microcks.
- **Sources:** Contract testing content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.10 MSW (Mock Service Worker)
- **Canonical identity:** MSW — API mocking via Service Worker (JS).
- **Category:** 3.5.5 · **Type:** Open-source library (npm).
- **Official URL:** Not verified in this session.
- **Description:** Intercepts network requests at the network level (browser Service Worker / Node interceptor) for tests, Storybook, and local dev.
- **Contents inspected:** Search references; Orval can emit MSW handlers.
- **Actual capabilities:** Request handlers, scenarios, Node + browser support.
- **Usage domain:** Frontend testing/dev without a backend.
- **Integration method:** npm; handlers file.
- **Dependencies:** Node/browser.
- **Availability:** Open source. **Maintenance:** Active. **License:** MIT (not re-verified in this session).
- **Limitations:** JS-only; mocks not generated from spec unless paired (e.g., Orval).
- **Related resources:** Prism, Mirage JS.
- **Sources:** Mocking roundups; Orval references (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.11 Microcks
- **Canonical identity:** Microcks — Kubernetes-native mocks & contract testing (CNCF Sandbox).
- **Category:** 3.5.5 · **Type:** Open-source platform (containers).
- **Official URL:** Not verified in this session.
- **Description:** Imports OpenAPI/AsyncAPI/Postman collections to serve mocks and run contract tests; K8s-native, Testcontainers-friendly.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Mocking, contract-test runner, dispatching strategies, K8s operator.
- **Usage domain:** Cloud-native microservice testing.
- **Integration method:** Docker/K8s manifests; CLI.
- **Dependencies:** Container runtime.
- **Availability:** Open source (CNCF Sandbox). **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Heavier setup than Prism/MSW for simple cases.
- **Related resources:** Prism, Pact, Testcontainers.
- **Sources:** Contract testing content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.12 oasdiff
- **Canonical identity:** oasdiff — OpenAPI diff & breaking-change detector (Go CLI).
- **Category:** 3.5.5 · **Type:** Open-source CLI.
- **Official URL:** Not verified in this session.
- **Description:** Diffs two OpenAPI specs, flags breaking changes, renders changelogs; CI-friendly.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Diff, breaking-change detection, changelog generation.
- **Usage domain:** API versioning governance.
- **Integration method:** Go CLI in CI.
- **Dependencies:** Go toolchain (or binary).
- **Availability:** Open source. **Maintenance:** Maintained. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Static diff only — no runtime verification.
- **Related resources:** Spectral, Optic (archived).
- **Sources:** API diffing content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.5.13 Archived: Optic & Dredd
- **Optic** (useoptic/optic): OpenAPI diff + "contract as code" workflow (Git-based API change review). **Status: Archived January 2026** (search-corroborated). Successor patterns: oasdiff, Spectral.
- **Dredd** (apiaryio/dredd): HTTP API testing against API Blueprint/OpenAPI. **Status: Archived May 2024** (search-corroborated). Alternatives: Schemathesis, Prism, Microcks.
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium (archival reported by secondary sources; primary repo pages not opened this session)

## 3.5.6 Identity, auth/authz, sessions

### 3.5.6.1 Keycloak
- **Canonical identity:** Keycloak — open-source IAM (Red Hat).
- **Category:** 3.5.6 · **Type:** Open-source server (Java/Quarkus) + admin UI.
- **Official URL:** https://www.keycloak.org
- **Description:** Self-hosted identity and access management: SSO, OAuth2/OIDC, SAML, LDAP/AD federation, user federation, social login, fine-grained authorization services.
- **Contents inspected:** Official site sections referenced via search (blog, docs); primary pages not opened.
- **Actual capabilities:** Realms, clients, identity brokering, MFA, password policies, admin REST API, clustering.
- **Usage domain:** Enterprise SSO, self-hosted auth for apps/APIs.
- **Integration method:** Docker/K8s distribution; OIDC/SAML clients; Admin REST API.
- **Dependencies:** Java runtime; database (Postgres etc.).
- **Availability:** Open source. **Maintenance:** Active (Red Hat). **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Operational complexity; theming/custom UX work; upgrade care.
- **Related resources:** Ory stack, ZITADEL, Authentik, FusionAuth.
- **Sources:** https://www.keycloak.org · self-hosted auth roundups (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.6.2 Ory (Kratos / Hydra / Keto / Oathkeeper)
- **Canonical identity:** Ory — composable open-source identity stack.
- **Category:** 3.5.6 · **Type:** Open-source services (Go) + Ory Cloud (managed).
- **Official URL:** https://www.ory.sh/kratos (verbatim; Hydra/Keto/Oathkeeper under same domain, not verified in this session).
- **Description:** Modular IAM: Kratos (user management/login/registration/MFA), Hydra (OAuth2/OIDC provider), Keto (permissions, Zanzibar-style), Oathkeeper (identity-aware proxy).
- **Contents inspected:** Official Kratos docs URL surfaced via search; architecture described in secondary sources.
- **Actual capabilities:** Self-service flows, sessions, OAuth2/OIDC, RBAC/ABAC permissions, zero-trust proxying.
- **Usage domain:** Cloud-native apps needing composable, headless auth.
- **Integration method:** Docker/K8s; Ory Cloud; SDKs; Oathkeeper as sidecar/proxy.
- **Dependencies:** Database per component.
- **Availability:** Open source + managed cloud. **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Multiple components to operate; managed cloud costs at scale.
- **Related resources:** Keycloak, ZITADEL, Auth.js.
- **Sources:** https://www.ory.sh/kratos · self-hosted auth comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.6.3 ZITADEL
- **Canonical identity:** ZITADEL — open-source identity infrastructure (zitadel.com).
- **Category:** 3.5.6 · **Type:** Open-source platform (Go) + ZITADEL Cloud.
- **Official URL:** https://zitadel.com
- **Description:** Identity management with organizations/projects multi-tenancy, OIDC/OAuth2/SAML, passwordless, machine users, APIs-first.
- **Contents inspected:** Official domain via search; not opened.
- **Actual capabilities:** B2B multi-tenancy, actions (serverless hooks), SCIM, audit trails.
- **Usage domain:** SaaS needing org/team identity, B2B auth.
- **Integration method:** Cloud or self-hosted Docker; OIDC/SAML; gRPC/REST APIs.
- **Dependencies:** Database (CockroachDB/Postgres per docs — not verified in this session).
- **Availability:** Open source + cloud. **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Newer ecosystem than Keycloak.
- **Related resources:** Keycloak, Ory, Auth0 (3.7.1).
- **Sources:** https://zitadel.com · auth roundups (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.6.4 better-auth
- **Canonical identity:** better-auth — TypeScript authentication library.
- **Category:** 3.5.6 · **Type:** Open-source library (npm).
- **Official URL:** https://www.better-auth.com
- **Description:** Framework-agnostic TS auth library (email/password, social OAuth, magic links, passkeys, 2FA, organizations, admin); plugin architecture; the Auth.js team recommends new projects start with Better Auth (see 3.5.6.5).
- **Contents inspected:** better-auth.com referenced in Auth.js README migration note.
- **Actual capabilities:** Adapters for many DBs/ORMs (Prisma, Drizzle, etc.), session management, rate limiting, SSO plugins.
- **Usage domain:** Modern TS full-stack apps (Next.js, SvelteKit, Astro, etc.).
- **Integration method:** npm; framework plugins.
- **Dependencies:** Database adapter.
- **Availability:** Open source. **Maintenance:** Active (fast-moving). **License:** MIT (not re-verified in this session).
- **Limitations:** Young project — API churn; some Auth.js features (e.g., stateless DB-less sessions) are gaps.
- **Related resources:** Auth.js (predecessor recommendation), Lucia (archived/unmaintained — community forks), SuperTokens.
- **Sources:** https://www.better-auth.com · https://github.com/nextauthjs/next-auth
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.6.5 Auth.js (next-auth) — Corrected
- **Canonical identity:** `nextauthjs/next-auth` (Auth.js) — authentication for the web.
- **Category:** 3.5.6 · **Type:** Open-source library (npm). **Status: superseded by recommendation.**
- **Official URL:** https://authjs.dev
- **Description:** The long-standard Next.js/Auth.js authentication library. **Correction (Verified, 2026-10-10):** the `nextauthjs/next-auth` README (opened this session) states Auth.js is now part of Better Auth; maintainers recommend new projects start with Better Auth instead, except specific gaps (notably stateless sessions without a database).
- **Contents inspected:** https://github.com/nextauthjs/next-auth — full README read this session (migration banner, "Auth.js is now part of Better Auth", npm `next-auth@5.0.0-beta`, docs at authjs.dev, contribution/security sections, license line truncated in render).
- **Actual capabilities:** OAuth providers, email/magic link, credentials, JWT/database sessions, adapters.
- **Usage domain:** Existing Next.js apps (maintenance mode guidance); new apps → Better Auth per maintainers.
- **Integration method:** npm `next-auth`; route handlers.
- **Dependencies:** Next.js; optional database adapter.
- **Availability:** Open source; maintenance posture shifting to Better Auth org. **Maintenance:** Transitioning. **License:** ISC (per package history — not re-verified in README render; marked accordingly).
- **Limitations:** See migration note; v5 long beta history.
- **Related resources:** better-auth, Lucia.
- **Sources:** https://github.com/nextauthjs/next-auth · https://authjs.dev
- **Verification date:** 2026-10-10 — **Verification:** Corrected + Verified (README opened) — **Confidence:** High

### 3.5.6.6 Lucia — Historical note
- **Canonical identity:** Lucia (`lucia-auth/lucia`) — bearer-token/session auth library.
- **Category:** 3.5.6 · **Type:** Open-source library (was npm).
- **Description:** Minimal session-management library popular in 2023–2024. Project was discontinued by its author (widely reported; community forks exist). **Status: Historical** — do not adopt for new work; see better-auth.
- **Verification date:** 2026-10-10 — **Verification:** Historical (secondary reports; primary repo not opened) — **Confidence:** Medium

## 3.5.7 Serverless & edge compute

### 3.5.7.1 Cloudflare Workers
- **Canonical identity:** Cloudflare Workers — edge serverless platform.
- **Category:** 3.5.7 · **Type:** Hosted platform (proprietary runtime, open Workers SDK/tooling).
- **Official URL:** Not verified in this session.
- **Description:** V8-Isolate-based functions at Cloudflare's edge; bindings to KV, R2, D1, Durable Objects, Queues; Wrangler CLI.
- **Contents inspected:** Search references (Hono docs target Workers; skill ecosystems).
- **Actual capabilities:** Sub-50ms cold starts, cron triggers, streaming, WebSockets (Durable Objects), static assets.
- **Usage domain:** Edge APIs, middleware, AI inference at edge.
- **Integration method:** Wrangler CLI; `workers.dev` or custom domains; bindings config.
- **Dependencies:** Cloudflare account.
- **Availability:** Hosted (free tier + paid). **Maintenance:** Active. **License:** Runtime proprietary; tooling open source (not verified per-repo).
- **Limitations:** No Node built-ins historically (Node compat layer now broad); CPU-time limits; vendor lock-in via bindings.
- **Related resources:** Deno Deploy, Vercel Functions, AWS Lambda, Hono.
- **Sources:** Edge/serverless content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.7.2 AWS Lambda
- **Canonical identity:** AWS Lambda — serverless functions (Amazon Web Services).
- **Category:** 3.5.7 · **Type:** Hosted service.
- **Official URL:** Not verified in this session.
- **Description:** Event-driven functions (many runtimes incl. custom), wired to API Gateway/SQS/EventBridge/S3 events.
- **Contents inspected:** Search references (serverless frameworks content).
- **Actual capabilities:** 15-min max duration, provisioned concurrency, Lambda@Edge/CloudFront Functions, container images, SnapStart.
- **Usage domain:** Event processing, APIs via API Gateway, ETL, webhooks.
- **Integration method:** AWS console/CDK/Terraform/SAM/Serverless Framework; Hono/Express adapters exist.
- **Dependencies:** AWS account.
- **Availability:** Hosted (free tier). **Maintenance:** Active. **License:** Proprietary service.
- **Limitations:** Cold starts (mitigations exist); timeouts; regional service.
- **Related resources:** API Gateway, EventBridge, Step Functions, OpenFaaS/Knative (self-hosted alternatives).
- **Sources:** Serverless content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.7.3 Vercel Functions
- **Canonical identity:** Vercel Functions — serverless/edge functions on Vercel.
- **Category:** 3.5.7 · **Type:** Hosted platform (tied to Vercel deployments).
- **Official URL:** Not verified in this session.
- **Description:** Functions co-located with frontend deployments (`/api` routes, Server Actions); Fluid compute model.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Node/edge runtimes, cron, ISR/PPR integration, AI SDK streaming.
- **Usage domain:** Next.js backends, AI apps, webhooks.
- **Integration method:** Vercel project; framework route conventions.
- **Dependencies:** Vercel account/deployment.
- **Availability:** Hosted (hobby/pro/enterprise). **Maintenance:** Active. **License:** Proprietary platform.
- **Limitations:** Execution/duration limits by plan; Vercel-centric.
- **Related resources:** Netlify Functions, Cloudflare Workers, SST.
- **Sources:** Frontend-platform content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.5.8 Real-time servers, queues, brokers, workflow engines

### 3.5.8.1 Socket.IO
- **Canonical identity:** Socket.IO — real-time engine (JS).
- **Category:** 3.5.8 · **Type:** Open-source library (npm) — client + server.
- **Official URL:** Not verified in this session.
- **Description:** Event-based bidirectional communication with fallbacks (WebSocket → polling), rooms/namespaces, multiplexing; adapters for Redis/Postgres scaling.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Rooms, namespaces, acknowledgements, binary, clustering adapters.
- **Usage domain:** Chat, live dashboards, multiplayer, notifications.
- **Integration method:** npm; attaches to Node HTTP server; client SDKs.
- **Dependencies:** Node.js server.
- **Availability:** Open source. **Maintenance:** Active. **License:** MIT (not re-verified in this session).
- **Limitations:** Custom protocol (not raw WS); horizontal scaling needs adapter.
- **Related resources:** ws, Ably, Pusher (3.7.4), NATS.
- **Sources:** Real-time roundups (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.2 Ably & Pusher — hosted real-time
- **Canonical identity:** Ably (ably.com) and Pusher (pusher.com) — hosted pub/sub messaging.
- **Category:** 3.5.8/3.7.4 · **Type:** Hosted services with SDKs.
- **Official URL:** Not verified in this session.
- **Description:** Managed WebSocket pub/sub with channels, presence, history, push integrations; Pusher Channels/Beams; Ably emphasizes guarantees (ordering, exactly-once-ish semantics) and protocol adapters (MQTT/SSE).
- **Contents inspected:** Search references only.
- **Actual capabilities:** Channels, presence, message history, webhooks, integrations.
- **Usage domain:** Chat, live updates, collaborative features without operating infra.
- **Integration method:** SDKs (JS/iOS/Android/etc.); REST publish API.
- **Dependencies:** Vendor account.
- **Availability:** Hosted (free tiers + usage pricing). **Maintenance:** Active. **License:** Proprietary services.
- **Limitations:** Usage-based cost at scale; data residency considerations.
- **Related resources:** Socket.IO (self-hosted alternative), NATS, Mercure.
- **Sources:** Real-time service comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.3 Temporal
- **Canonical identity:** Temporal — durable execution platform.
- **Category:** 3.5.8 · **Type:** Open-source server (Go) + SDKs + Temporal Cloud.
- **Official URL:** Not verified in this session.
- **Description:** Workflows-as-code with durable state: write workflows in code (TS/Python/Go/Java/.NET/PHP), survive crashes/restarts; event history, timers, signals.
- **Contents inspected:** Search references (workflow-engine comparisons).
- **Actual capabilities:** Durable workflows/activities, cron-like schedules, versioning, visibility UI, multi-region (Cloud).
- **Usage domain:** Order processing, onboarding flows, ETL orchestration, AI agent orchestration.
- **Integration method:** Self-hosted cluster or Temporal Cloud; language SDKs.
- **Dependencies:** Database (Postgres/MySQL/Cassandra per docs — not verified in this session).
- **Availability:** Open source + cloud. **Maintenance:** Active. **License:** MIT for SDKs; server BSL (not re-verified in this session).
- **Limitations:** Operational lift self-hosted; workflow determinism constraints.
- **Related resources:** Inngest, Trigger.dev, Restate, Hatchet, Cadence (predecessor).
- **Sources:** Durable execution comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.4 Inngest
- **Canonical identity:** Inngest — event-driven durable functions platform.
- **Category:** 3.5.8 · **Type:** Open-source (core) + hosted platform.
- **Official URL:** Not verified in this session.
- **Description:** Durable execution via `step.run`/`step.sleep` in plain functions; events trigger workflows; works on serverless.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Step functions, retries, cron, event triggers, concurrency controls, local dev server.
- **Usage domain:** Background jobs, AI workflows, webhooks processing.
- **Integration method:** SDK (TS/Python/Go); serve endpoint; Inngest Cloud or self-hosted dev server.
- **Dependencies:** Framework adapter.
- **Availability:** Open source core + cloud. **Maintenance:** Active. **License:** Apache 2.0 core (not re-verified in this session).
- **Limitations:** Step determinism rules; cloud features paywalled.
- **Related resources:** Trigger.dev, Temporal, Restate, QStash.
- **Sources:** Background-job platform comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.5 Trigger.dev
- **Canonical identity:** Trigger.dev — background jobs as code (open source).
- **Category:** 3.5.8 · **Type:** Open-source platform (self-host or cloud).
- **Official URL:** Not verified in this session.
- **Description:** Define jobs in code with retries, delays, schedules, concurrency; dashboard + integrations (AI providers, etc.).
- **Contents inspected:** Search references only.
- **Actual capabilities:** Jobs/tasks, schedules, waitpoints, realtime dashboard.
- **Usage domain:** Scheduled tasks, long-running jobs, AI pipelines.
- **Integration method:** SDK (TS/Python); self-host Docker or cloud.
- **Dependencies:** Database (self-host).
- **Availability:** Open source + cloud. **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Self-host ops; younger than Celery/Sidekiq ecosystems.
- **Related resources:** Inngest, Hatchet, BullMQ.
- **Sources:** Job-queue comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.6 Restate
- **Canonical identity:** Restate — durable execution for microservices.
- **Category:** 3.5.8 · **Type:** Open-source runtime + SDKs.
- **Official URL:** Not verified in this session.
- **Description:** Durable workflows/virtual objects over HTTP services; journaled execution, exactly-once semantics, Kafka integration.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Durable handlers, virtual objects (stateful entities), sagas, delayed calls.
- **Usage domain:** Microservice orchestration, exactly-once processing.
- **Integration method:** Restate server (single binary); SDK handlers (TS/Java/Go/Python).
- **Dependencies:** None heavy (embedded metadata store options).
- **Availability:** Open source. **Maintenance:** Active. **License:** BSL (not re-verified in this session).
- **Limitations:** Newer project; ecosystem smaller than Temporal.
- **Related resources:** Temporal, Dapr (virtual actors).
- **Sources:** Durable execution content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.7 Hatchet
- **Canonical identity:** Hatchet — distributed task queue (open source).
- **Category:** 3.5.8 · **Type:** Open-source engine (Go) + Hatchet Cloud.
- **Official URL:** Not verified in this session.
- **Description:** Durable task queue with workflows (DAGs), retries, rate limits, cron, workers in TS/Python/Go.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Workflow DAGs, child workflows, sticky workers, observability UI.
- **Usage domain:** Background processing, data pipelines.
- **Integration method:** Self-host or cloud; SDK workers.
- **Dependencies:** Postgres (self-host).
- **Availability:** Open source + cloud. **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Self-host ops; smaller community than BullMQ/Celery.
- **Related resources:** BullMQ, Celery, Inngest.
- **Sources:** Queue comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.8 BullMQ
- **Canonical identity:** BullMQ — Node.js queue on Redis.
- **Category:** 3.5.8 · **Type:** Open-source library (npm) + BullMQ Pro (commercial).
- **Official URL:** Not verified in this session.
- **Description:** Redis-backed job queue: priorities, delays, retries, rate limiting, flows (parent/child), repeatable jobs; dashboard (Arena/own UI).
- **Contents inspected:** Search references only.
- **Actual capabilities:** Queues, workers, schedulers, events, concurrency.
- **Usage domain:** Node background jobs, email sending, image processing.
- **Integration method:** npm; Redis connection.
- **Dependencies:** Redis.
- **Availability:** Open source (+Pro). **Maintenance:** Active. **License:** MIT core (not re-verified in this session).
- **Limitations:** Redis required; not durable-execution semantics (jobs can be lost on misconfig).
- **Related resources:** Bee-Queue (older), Celery, pg-boss (Postgres alternative).
- **Sources:** Queue comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.9 Celery
- **Canonical identity:** Celery — distributed task queue (Python).
- **Category:** 3.5.8 · **Type:** Open-source library (PyPI).
- **Official URL:** Not verified in this session.
- **Description:** Python task queue with brokers (RabbitMQ/Redis/SQS), beat scheduler, canvas workflows, result backends.
- **Contents inspected:** Search references (Django/Celery pairing noted).
- **Actual capabilities:** Tasks, chains/groups/chords, retries, periodic tasks, monitoring (Flower).
- **Usage domain:** Django/Flask background work, data pipelines.
- **Integration method:** `pip install celery`; broker URL.
- **Dependencies:** Broker (RabbitMQ/Redis); result backend.
- **Availability:** Open source. **Maintenance:** Maintained. **License:** BSD (not re-verified in this session).
- **Limitations:** Config complexity; at-least-once semantics by default.
- **Related resources:** Dramatiq, Huey, RQ (lighter Python queues), Sidekiq (Ruby).
- **Sources:** Python queue content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.10 Sidekiq
- **Canonical identity:** Sidekiq — Ruby background jobs on Redis.
- **Category:** 3.5.8 · **Type:** Open-source (core) + Pro/Enterprise.
- **Official URL:** Not verified in this session.
- **Description:** Multithreaded Ruby job processor backed by Redis; web UI, retries, scheduled jobs; Rails integration via Active Job.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Jobs, batches, cron (via extensions), unique jobs (Pro), metrics.
- **Usage domain:** Rails background processing.
- **Integration method:** Gem; Redis.
- **Dependencies:** Redis; Ruby.
- **Availability:** Open source core + paid tiers. **Maintenance:** Active. **License:** LGPL core (not re-verified in this session).
- **Limitations:** Ruby-only; Redis dependency.
- **Related resources:** GoodJob (Postgres-based Rails alternative), Resque.
- **Sources:** Ruby queue content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.11 QStash
- **Canonical identity:** QStash — serverless messaging/queue (Upstash).
- **Category:** 3.5.8 · **Type:** Hosted service (HTTP API).
- **Official URL:** Not verified in this session.
- **Description:** HTTP-based queue for serverless: publish to any HTTPS endpoint with retries, delays, schedules, DLQ; no broker to run.
- **Contents inspected:** Search references only (Upstash ecosystem).
- **Actual capabilities:** Message publish, schedules/cron, retries, batching, URL signing.
- **Usage domain:** Serverless background tasks, webhooks fan-out, cron on edge.
- **Integration method:** REST API / SDKs; Upstash account.
- **Dependencies:** Upstash account.
- **Availability:** Hosted (free tier + usage). **Maintenance:** Active. **License:** Proprietary service.
- **Limitations:** HTTP-only delivery model; vendor-specific.
- **Related resources:** Inngest, Cloudflare Queues, AWS SQS.
- **Sources:** Serverless queue content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.5.8.12 Message brokers: Kafka / RabbitMQ / NATS / Redpanda / Pulsar
- **Canonical identity:** Distributed messaging/streaming systems.
- **Category:** 3.5.8 · **Type:** Open-source brokers (+ managed clouds).
- **Official URL:** NATS docs: https://docs.nats.io (verbatim); NATS server: https://github.com/nats-io/nats-server (verbatim). Others: not verified in this session.
- **Description:**
  - **Apache Kafka:** distributed event streaming log; high throughput, partitioning, retention; ecosystem (Kafka Streams, ksqlDB, Connect).
  - **RabbitMQ:** AMQP broker; flexible routing (exchanges/queues), mature ops; good for task distribution.
  - **NATS:** lightweight, high-performance messaging (core pub/sub, JetStream persistence, KV/object store, services framework); single Go binary; docs at docs.nats.io.
  - **Redpanda:** Kafka-compatible streaming in C++; no ZooKeeper/KRaft JVM; Wasm transforms.
  - **Apache Pulsar:** multi-tenant pub/sub with tiered storage, functions, geo-replication.
- **Contents inspected:** docs.nats.io and nats-io/nats-server surfaced via search (not opened); Spring Boot integration guides for Kafka/RabbitMQ noted.
- **Actual capabilities:** Pub/sub, queues, streaming retention, ordering, exactly-once options (varies), schema registries.
- **Usage domain:** Event-driven microservices, data pipelines, IoT, real-time analytics.
- **Integration method:** Client libraries; managed clouds (Confluent, Redpanda Cloud, AWS MSK, CloudAMQP, Synadia for NATS).
- **Dependencies:** JVM (Kafka/Pulsar/RabbitMQ Erlang); NATS/Redpanda lighter.
- **Availability:** Open source + managed. **Maintenance:** Active across all. **License:** Apache 2.0 (Kafka/Pulsar); MPL-2.0 (RabbitMQ server); Apache 2.0 (NATS); BSL/SSPL mix for Redpanda (not re-verified per-project in this session — marked accordingly).
- **Limitations:** Kafka ops complexity; RabbitMQ throughput ceiling vs Kafka; NATS JetStream less feature-rich than Kafka for long retention analytics.
- **Related resources:** AWS SQS/SNS/EventBridge, Google Pub/Sub, Azure Service Bus (managed alternatives).
- **Sources:** https://docs.nats.io · https://github.com/nats-io/nats-server · https://dev.to/mosesmucyo/spring-boot-kafka-vs-rabbitmq-a-deep-dive-into-event-driven-microservices-6gd
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.5.9 OpenAPI → MCP conversion tools (machine-readable API contracts)

> DEDUP: `cnoe-io/openapi-mcp-codegen`, `ck Anthony/openapi-mcp`, `awslabs/openapi-mcp-server` are already catalogued by the parent workstream — cross-reference only. Below are **new alternatives** found in this workstream's research.

### 3.5.9.1 bbonnin/openapi-to-mcp — Verified
- **Canonical identity:** `bbonnin/openapi-to-mcp` — "Turn any API into an MCP server".
- **Category:** 3.5.9 · **Type:** Open-source CLI (npm: `openapi-to-mcp`).
- **Official URL:** https://github.com/bbonnin/openapi-to-mcp
- **Description:** Generates a stdio MCP server from an OpenAPI 3.x spec (YAML/JSON, local or remote URL) so agents can call any REST API as tools. `npx openapi-to-mcp <spec>` scaffolds a ready-to-run server; supports auth headers, server variables, operation filtering; Docker image available.
- **Contents inspected:** Full README opened 2026-10-10 (features, usage, config, Docker, license section present).
- **Actual capabilities:** Spec → MCP tool mapping per operation; request auth passthrough; filtering by tags/operations; generated project runnable via node/docker.
- **Usage domain:** Giving coding agents typed access to third-party REST APIs.
- **Integration method:** `npx openapi-to-mcp`; output wired into MCP client config (Claude Code, Cursor, etc.).
- **Dependencies:** Node.js; an OpenAPI 3.x document.
- **Availability:** Open source. **Maintenance:** Active (per README/releases). **License:** Per README license section (exact license not captured in this session's render — marked accordingly).
- **Limitations:** Quality bounded by spec accuracy; OpenAPI 3.x only (per README scope).
- **Related resources:** Tyk api-to-mcp (3.5.9.2), Taskade generator (3.5.9.3); DEDUP set above.
- **Sources:** https://github.com/bbonnin/openapi-to-mcp
- **Verification date:** 2026-10-10 — **Verification:** Verified — **Confidence:** High

### 3.5.9.2 TykTechnologies/api-to-mcp — Verified
- **Canonical identity:** `TykTechnologies/api-to-mcp` — convert OpenAPI specs into MCP servers (Tyk).
- **Category:** 3.5.9 · **Type:** Open-source tool (Go).
- **Official URL:** https://github.com/TykTechnologies/api-to-mcp
- **Description:** Tyk's OpenAPI→MCP converter: generates MCP servers/tools from OpenAPI definitions; positioned alongside Tyk's API gateway/MCP offering.
- **Contents inspected:** Repo README opened 2026-10-10 (overview + usage).
- **Actual capabilities:** Spec ingestion → MCP server; auth handling per spec security schemes.
- **Usage domain:** Exposing existing REST estates to AI agents via Tyk or standalone.
- **Integration method:** CLI; container.
- **Dependencies:** Go toolchain or released binary; OpenAPI spec.
- **Availability:** Open source. **Maintenance:** Active (Tyk-maintained). **License:** Per repo (not captured in this session's render — marked accordingly).
- **Limitations:** Tied to Tyk's release cadence; spec-quality dependency.
- **Related resources:** Tyk Gateway (3.5.4.5), bbonnin/openapi-to-mcp.
- **Sources:** https://github.com/TykTechnologies/api-to-mcp
- **Verification date:** 2026-10-10 — **Verification:** Verified — **Confidence:** High

### 3.5.9.3 Taskade @taskade/mcp-openapi-codegen
- **Canonical identity:** `@taskade/mcp-openapi-codegen` (npm) — OpenAPI→MCP code generator (Taskade).
- **Category:** 3.5.9 · **Type:** Open-source generator (npm) + blog documentation.
- **Official URL:** Not verified in this session (blog: https://taskade.com/blog/openapi-to-mcp-code-generator — verbatim).
- **Description:** Generates MCP server code from OpenAPI specs; Taskade's blog documents the workflow.
- **Contents inspected:** Blog URL surfaced via search (not opened).
- **Actual capabilities:** Codegen of MCP servers from OpenAPI (per blog).
- **Usage domain:** Agent tool generation from REST APIs.
- **Integration method:** npm package.
- **Dependencies:** Node.js; OpenAPI spec.
- **Availability:** Open source (per npm listing reports). **Maintenance:** Not verified in this session. **License:** Not verified in this session.
- **Limitations:** Unresolved details — primary source not inspected.
- **Related resources:** DEDUP set; bbonnin/openapi-to-mcp.
- **Sources:** https://taskade.com/blog/openapi-to-mcp-code-generator
- **Verification date:** 2026-10-10 — **Verification:** Unverified — **Confidence:** Low

### 3.5.9.4 Speakeasy OpenAPI→MCP
- **Canonical identity:** Speakeasy — SDK infra vendor; ships OpenAPI→MCP generation.
- **Category:** 3.5.9 · **Type:** Commercial platform feature (generator open source).
- **Official URL:** Not verified in this session.
- **Description:** Speakeasy generates MCP servers alongside SDKs/Terraform providers from OpenAPI specs.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Managed codegen pipeline; CI integration.
- **Usage domain:** API vendors shipping agent-ready tool servers.
- **Integration method:** Speakeasy CLI/config.
- **Dependencies:** Speakeasy account for managed runs.
- **Availability:** SaaS. **Maintenance:** Active. **License:** Not verified in this session.
- **Limitations:** Managed-platform dependency.
- **Related resources:** Fern (3.5.5.4), Scalar (3.5.5.2).
- **Sources:** API codegen content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Unverified — **Confidence:** Low

### 3.5.9.5 FastMCP.from_openapi() & openapi-mcp-generator (npm)
- **Canonical identity:** FastMCP (Python MCP framework) `from_openapi()` helper; `openapi-mcp-generator` (npm package).
- **Category:** 3.5.9 · **Type:** Open-source library helpers.
- **Official URL:** Not verified in this session.
- **Description:** FastMCP exposes helpers to build MCP servers directly from OpenAPI specs in Python; the npm `openapi-mcp-generator` package offers a JS-side generator.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Programmatic spec→server construction (FastMCP); CLI generation (npm package).
- **Usage domain:** Python/JS agent tool servers from existing APIs.
- **Integration method:** Library import / npx.
- **Dependencies:** Python (FastMCP) / Node (npm pkg); OpenAPI spec.
- **Availability:** Open source. **Maintenance:** Not verified in this session. **License:** Not verified in this session.
- **Limitations:** Helper-level — less turnkey than dedicated converters.
- **Related resources:** FastMCP (agent framework), DEDUP set.
- **Sources:** MCP tooling content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Unverified — **Confidence:** Low

### 3.5.9.6 HelpCode-ai/anythingmcp
- **Canonical identity:** `HelpCode-ai/anythingmcp` — generic MCP server project.
- **Category:** 3.5.9 · **Type:** Open-source repo (per search listing).
- **Official URL:** Not verified in this session.
- **Description:** Appears in OpenAPI→MCP tooling discussions as a generic/adapter MCP server project.
- **Contents inspected:** None — listing only.
- **Actual capabilities:** Unresolved — primary source not inspected.
- **Usage domain:** Unresolved.
- **Integration method:** Unresolved.
- **Dependencies:** Unresolved.
- **Availability:** Unresolved. **Maintenance:** Unresolved. **License:** Unresolved.
- **Limitations:** Insufficient evidence — needs a follow-up pass.
- **Related resources:** DEDUP set.
- **Sources:** MCP tooling search results (2026).
- **Verification date:** 2026-10-10 — **Verification:** Unresolved — **Confidence:** Low

### 3.5.9.7 Apollo MCP Server
- **Canonical identity:** Apollo MCP Server — GraphQL→MCP bridge (Apollo GraphQL).
- **Category:** 3.5.9 · **Type:** Open-source tool (per Apollo announcements).
- **Official URL:** Not verified in this session.
- **Description:** Exposes GraphQL operations as MCP tools, letting agents query federated graphs through the Model Context Protocol.
- **Contents inspected:** Search references only.
- **Actual capabilities:** GraphQL schema → MCP tools; works with Apollo Router/Gateway contexts.
- **Usage domain:** Agent access to GraphQL estates.
- **Integration method:** Apollo tooling.
- **Dependencies:** GraphQL endpoint.
- **Availability:** Per Apollo release posture (not verified in this session). **Maintenance:** Active (assumed). **License:** Not verified in this session.
- **Limitations:** GraphQL-only (not REST/OpenAPI).
- **Related resources:** Apollo Server (3.5.2.1).
- **Sources:** Apollo MCP announcements (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Unverified — **Confidence:** Low

---

# 3.6 Databases, persistence & search

## 3.6.1 Relational databases

### 3.6.1.1 PostgreSQL
- **Canonical identity:** PostgreSQL — object-relational DBMS (PostgreSQL Global Development Group).
- **Category:** 3.6.1 · **Type:** Open-source database server.
- **Official URL:** https://www.postgresql.org
- **Description:** The default serious open-source RDBMS: ACID, JSONB, full-text search, PostGIS, extensions (pgvector, Timescale), logical replication, RLS.
- **Contents inspected:** Official site referenced via spec-kit fallback table; ecosystem position corroborated across many sources.
- **Actual capabilities:** Relational + document (JSONB) + vector (pgvector ext.) + time-series (Timescale ext.) + graph (AGE ext.); LISTEN/NOTIFY; FDWs.
- **Usage domain:** Primary application database; also vector/search/time-series via extensions.
- **Integration method:** Drivers (pg, psycopg, JDBC), ORMs (Prisma/Drizzle/SQLAlchemy), hosted (Neon/Supabase/RDS).
- **Dependencies:** OS service or container.
- **Availability:** Open source; myriad hosted options. **Maintenance:** Active (yearly majors). **License:** PostgreSQL License (permissive; not re-verified in this session).
- **Limitations:** Vertical scaling limits; connection scaling needs poolers (PgBouncer/Supavisor).
- **Related resources:** pgvector (3.6.4), PostGIS, TimescaleDB, Neon, Supabase.
- **Sources:** https://www.postgresql.org · https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.6.1.2 MySQL
- **Canonical identity:** MySQL — RDBMS (Oracle).
- **Category:** 3.6.1 · **Type:** Open-source DBMS (GPL) + commercial editions.
- **Official URL:** https://www.mysql.com
- **Description:** Widely deployed RDBMS (WordPress/LAMP heritage); InnoDB engine; MySQL 8.x line; HeatWave in OCI.
- **Contents inspected:** Official domain via spec-kit table; not opened.
- **Actual capabilities:** Relational, JSON columns, replication, Group Replication/InnoDB Cluster.
- **Usage domain:** CMS, e-commerce, LAMP apps, PlanetScale-compatible (Vitess) workloads.
- **Integration method:** Drivers, ORMs; managed (RDS, Cloud SQL, PlanetScale).
- **Dependencies:** OS service/container.
- **Availability:** Open source (GPL) + commercial. **Maintenance:** Active. **License:** GPL v2 + commercial (not re-verified in this session).
- **Limitations:** GPL considerations for embedding; feature velocity vs Postgres perceived slower.
- **Related resources:** MariaDB (community fork), PlanetScale/Vitess, TiDB.
- **Sources:** https://www.mysql.com · https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.1.3 SQLite / libSQL
- **Canonical identity:** SQLite — embedded relational DB (public domain); libSQL — fork by Turso.
- **Category:** 3.6.1 · **Type:** Open-source embedded library + (libSQL) server mode.
- **Official URL:** https://www.sqlite.org
- **Description:** Serverless, zero-config, single-file SQL database; ubiquitous in mobile/edge/desktop. libSQL adds server mode + replication (Turso's fork).
- **Contents inspected:** Official domain via search; Turso/libSQL evolution corroborated (Turso deprecated scale-to-zero Jan 2026 — secondary reports).
- **Actual capabilities:** Full SQL, transactions, FTS5, JSON1, extensions (vector via sqlite-vec).
- **Usage domain:** Embedded, edge (D1, Turso), local-first apps, testing.
- **Integration method:** Language bindings; libSQL client/server; Cloudflare D1.
- **Dependencies:** None (library).
- **Availability:** Public domain (SQLite); libSQL open source. **Maintenance:** Active. **License:** Public domain (SQLite); MIT/Apache for libSQL (not re-verified in this session).
- **Limitations:** Single-writer; not for high-write concurrency.
- **Related resources:** Turso (3.6.6), Cloudflare D1, DuckDB (analytics cousin).
- **Sources:** https://www.sqlite.org · Turso/libSQL coverage (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.6.1.4 CockroachDB
- **Canonical identity:** CockroachDB — distributed SQL (Cockroach Labs).
- **Category:** 3.6.1 · **Type:** Database (source-available license) + CockroachDB Cloud.
- **Official URL:** Not verified in this session.
- **Description:** Postgres-wire-compatible distributed database: horizontal scale, multi-region survivability.
- **Contents inspected:** Search references (distributed SQL comparisons).
- **Actual capabilities:** Distributed transactions, geo-partitioning, managed cloud.
- **Usage domain:** Global apps needing Postgres compatibility + scale.
- **Integration method:** Postgres drivers; managed cloud or self-host.
- **Dependencies:** Cluster nodes.
- **Availability:** Source-available + cloud. **Maintenance:** Active. **License:** BSL (not re-verified in this session).
- **Limitations:** License not OSI-open; ops complexity; latency characteristics of consensus.
- **Related resources:** YugabyteDB, TiDB, Neon.
- **Sources:** Distributed SQL content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.1.5 TimescaleDB
- **Canonical identity:** TimescaleDB — time-series on Postgres (Timescale).
- **Category:** 3.6.1 · **Type:** Postgres extension (open source core) + Timescale Cloud.
- **Official URL:** Not verified in this session.
- **Description:** Hypertables, compression, continuous aggregates, retention policies on Postgres.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Time-series SQL, downsampling, tiered storage.
- **Usage domain:** Metrics, IoT, observability, finance ticks.
- **Integration method:** Postgres extension; managed cloud.
- **Dependencies:** PostgreSQL.
- **Availability:** Open core + cloud. **Maintenance:** Active. **License:** Apache 2.0 for core parts / Timescale License for advanced (not re-verified in this session).
- **Limitations:** License split; Postgres operational base.
- **Related resources:** QuestDB, InfluxDB, ClickHouse.
- **Sources:** Time-series comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.6.2 Serverless / hosted Postgres

### 3.6.2.1 Neon
- **Canonical identity:** Neon — serverless Postgres (Neon, Inc.).
- **Category:** 3.6.2 · **Type:** Hosted database service (open-source components).
- **Official URL:** Not verified in this session.
- **Description:** Serverless Postgres with autoscaling, branching (DB branching for dev/preview), scale-to-zero; storage/compute separation. **Corrected status:** acquired by Databricks (announced May 2025 — widely reported).
- **Contents inspected:** Search coverage of acquisition + branching features.
- **Actual capabilities:** Instant branching, point-in-time restore, autoscale, PgBouncer built in, MCP server (see 3.6.10.3).
- **Usage domain:** Serverless apps, preview environments, AI-generated apps needing instant Postgres.
- **Integration method:** Postgres connection string; Vercel/Netlify integrations; `neonctl`/API.
- **Dependencies:** Neon account.
- **Availability:** Hosted. **Maintenance:** Active (post-acquisition). **License:** Service proprietary; some components open source (not verified per-repo).
- **Limitations:** Cold starts on scale-from-zero; Databricks ownership direction.
- **Related resources:** Supabase, PlanetScale, Prisma Postgres.
- **Sources:** Neon acquisition coverage (search, 2026); https://github.com/neondatabase/mcp-server-neon (referenced in MCP listings).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified (acquisition widely reported; primary announcement not opened) — **Confidence:** Medium

### 3.6.2.2 Supabase
- **Canonical identity:** Supabase — open-source Firebase alternative (Postgres platform).
- **Category:** 3.6.2 (+ 3.7.1 Auth, 3.6.8 storage) · **Type:** Open-source platform (self-hostable) + hosted cloud.
- **Official URL:** Supabase docs referenced verbatim: https://supabase.com/docs/guides/auth/auth-email-templates (auth email templates guide).
- **Description:** Postgres + auto-generated REST (PostgREST) & GraphQL (pg_graphql) + Auth (GoTrue) + Storage + Realtime + Edge Functions + pgvector.
- **Contents inspected:** Docs pages on auth email templates and SMTP (Resend guide) surfaced via search; MCP server repo listed in DB-MCP content.
- **Actual capabilities:** Instant APIs from schema, RLS-based authz, file storage, realtime subscriptions, vector search.
- **Usage domain:** SaaS backends, MVPs, mobile backends.
- **Integration method:** `supabase-js` client; Postgres connection; CLI; self-host Docker.
- **Dependencies:** Supabase project (hosted) or Docker.
- **Availability:** Open source + hosted (free tier). **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Opinionated stack; self-hosting is community-supported; RLS learning curve.
- **Related resources:** PostgREST (3.6.2.6), Neon, Firebase (3.7.1), supabase/mcp (3.6.10.4).
- **Sources:** https://supabase.com/docs/guides/auth/auth-email-templates · https://resend.com/docs/send-with-supabase-smtp · DB MCP server listings (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.6.2.3 PlanetScale
- **Canonical identity:** PlanetScale — serverless MySQL (Vitess-based).
- **Category:** 3.6.2 · **Type:** Hosted database service.
- **Official URL:** Not verified in this session.
- **Description:** MySQL-compatible serverless platform with branching; **status change:** free tier removed March 2024 (widely reported) — now paid-focused with usage pricing.
- **Contents inspected:** Search coverage of pricing change.
- **Actual capabilities:** Branching, non-blocking schema changes (via Vitess), insights.
- **Usage domain:** MySQL workloads needing branching/scale.
- **Integration method:** MySQL drivers; `pscale` CLI.
- **Dependencies:** PlanetScale account.
- **Availability:** Hosted (paid). **Maintenance:** Active. **License:** Proprietary service.
- **Limitations:** No free tier since Mar 2024; MySQL-only.
- **Related resources:** TiDB Serverless, Neon (Postgres analog).
- **Sources:** Pricing-change coverage (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.2.4 Turso (libSQL)
- **Canonical identity:** Turso — edge SQLite/libSQL platform.
- **Category:** 3.6.2 · **Type:** Hosted database service (libSQL open source).
- **Official URL:** Not verified in this session.
- **Description:** Replicated SQLite at the edge; **status change:** scale-to-zero deprecated January 2026 (secondary reports) — always-on model now.
- **Contents inspected:** Search coverage of deprecation.
- **Actual capabilities:** Read replicas near users, embedded replicas, branching.
- **Usage domain:** Edge apps, local-first sync, low-latency reads.
- **Integration method:** libSQL clients; HTTP/SQLite protocols.
- **Dependencies:** Turso account.
- **Availability:** Hosted. **Maintenance:** Active. **License:** Service proprietary; libSQL open source.
- **Limitations:** SQLite single-writer semantics; pricing/model churn noted.
- **Related resources:** Cloudflare D1, SQLite (3.6.1.3).
- **Sources:** Turso deprecation coverage (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.2.5 Prisma Postgres
- **Canonical identity:** Prisma Postgres — managed Postgres (Prisma).
- **Category:** 3.6.2 · **Type:** Hosted database service.
- **Official URL:** Not verified in this session.
- **Description:** Prisma's managed Postgres (formerly Accelerate/Optimize lineage), paired with Prisma ORM; connection pooling, edge caching.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Managed Postgres, pooling, integrates with Prisma schema/migrations.
- **Usage domain:** Prisma ORM users wanting zero-ops Postgres.
- **Integration method:** Prisma CLI; connection string.
- **Dependencies:** Prisma account.
- **Availability:** Hosted. **Maintenance:** Active. **License:** Proprietary service.
- **Limitations:** Prisma-ecosystem-centric.
- **Related resources:** Prisma ORM (3.6.6), Neon, Supabase.
- **Sources:** Prisma platform content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.2.6 PostgREST
- **Canonical identity:** PostgREST — instant REST API for Postgres.
- **Category:** 3.6.2 · **Type:** Open-source server (Haskell binary).
- **Official URL:** Not verified in this session.
- **Description:** Serves a REST API directly from the Postgres schema (tables/views → routes), RLS-aware; the engine behind Supabase's REST layer.
- **Contents inspected:** Search references (Supabase architecture content).
- **Actual capabilities:** Auto CRUD, filtering/embedding via query params, JWT auth, OpenAPI output.
- **Usage domain:** Instant APIs over Postgres; Supabase self-host internals.
- **Integration method:** Single binary + config; JWT secret.
- **Dependencies:** PostgreSQL.
- **Availability:** Open source. **Maintenance:** Active. **License:** MIT (not re-verified in this session).
- **Limitations:** REST-only; business logic needs Postgres functions or a separate layer.
- **Related resources:** Supabase, Hasura, PostGraphile.
- **Sources:** PostgREST/Supabase content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.6.3 NoSQL: document, key-value, wide-column, graph

### 3.6.3.1 MongoDB
- **Canonical identity:** MongoDB — document database (MongoDB, Inc.).
- **Category:** 3.6.3 · **Type:** Database (SSPL) + Atlas (managed).
- **Official URL:** https://www.mongodb.com
- **Description:** BSON document store: flexible schemas, aggregation pipeline, Atlas Search, transactions; Atlas is the managed cloud. **Archived:** MongoDB Atlas App Services (serverless backend/BaaS) reached end-of-life 2025-09-30 — confirmed by the official EOL notice on the Atlas App Services Admin API docs page; Atlas continues as a managed database.
- **Contents inspected:** Official docs EOL notice (via search result text); MCP server listings.
- **Actual capabilities:** CRUD, aggregation, Atlas Search/vector search, change streams, time series.
- **Usage domain:** Document workloads, content, catalogs, rapid iteration.
- **Integration method:** Drivers/ODM (Mongoose, PyMongo); Atlas connection string; mongodb-mcp-server (3.6.10.1).
- **Dependencies:** `mongod` or Atlas account.
- **Availability:** SSPL + Atlas. **Maintenance:** Active. **License:** SSPL (not OSI-open; not re-verified in this session).
- **Limitations:** SSPL licensing; joins/denormalization modeling discipline; App Services BaaS gone (migrate triggers/functions elsewhere).
- **Related resources:** FerretDB (open alternative), DocumentDB/Cosmos DB (API-compatible), mongodb-mcp-server.
- **Sources:** https://www.mongodb.com · https://www.mongodb.com/docs/api/doc/atlas-app-services-admin-api-v3 (EOL notice)
- **Verification date:** 2026-10-10 — **Verification:** Partially verified (EOL notice corroborated via official docs page text) — **Confidence:** High

### 3.6.3.2 Redis
- **Canonical identity:** Redis — in-memory data store (Redis Ltd.).
- **Category:** 3.6.3 (+ 3.6.7 caching, 3.5.8 queue backend) · **Type:** Database (source-available) + Redis Cloud.
- **Official URL:** https://redis.io
- **Description:** In-memory data structures server: strings/hashes/lists/sets/sorted sets, streams, pub/sub, Lua scripting, Redis Stack modules (JSON, search, vector, time-series, graph, Bloom).
- **Contents inspected:** Official domain via spec-kit table; MCP server listing.
- **Actual capabilities:** Caching, sessions, queues (BullMQ), leaderboards, rate limiting, vector search (RediSearch), streams.
- **Usage domain:** Cache, session store, real-time features, job queues.
- **Integration method:** RESP clients; Redis Cloud; `redis/mcp-redis` for agents (3.6.10.5).
- **Dependencies:** Server binary or cloud.
- **Availability:** Source-available + cloud. **Maintenance:** Active. **License:** RSALv2/SSPLv1 (not OSI-open since 2024 relicense; not re-verified in this session).
- **Limitations:** License change → forks (Valkey, Garnet); memory cost.
- **Related resources:** Valkey (Linux Foundation fork), Dragonfly, Garnet, Upstash.
- **Sources:** https://redis.io · https://github.com/plaesy/spec-kit/blob/HEAD/instructions/tech-validation.instructions.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** High

### 3.6.3.3 Apache Cassandra
- **Canonical identity:** Apache Cassandra — wide-column distributed DB (ASF).
- **Category:** 3.6.3 · **Type:** Open-source database.
- **Official URL:** Not verified in this session.
- **Description:** Masterless wide-column store: linear write scale, tunable consistency, CQL.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Multi-DC replication, time-series/event workloads, lightweight transactions.
- **Usage domain:** High-write ingest, IoT, messaging backends.
- **Integration method:** CQL drivers; managed (Astra DB, AWS Keyspaces).
- **Dependencies:** JVM cluster.
- **Availability:** Open source (Apache 2.0). **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Query-model-driven design; operational expertise needed; weak ad-hoc query.
- **Related resources:** ScyllaDB (compatible, C++), Bigtable, DynamoDB.
- **Sources:** NoSQL comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.3.4 Neo4j
- **Canonical identity:** Neo4j — graph database (Neo4j, Inc.).
- **Category:** 3.6.3 · **Type:** Database (GPL community / commercial) + Aura (managed).
- **Official URL:** Not verified in this session.
- **Description:** Native property-graph DB with Cypher query language; Graph Data Science library; Aura managed cloud.
- **Contents inspected:** Search references (graph DB comparisons).
- **Actual capabilities:** Cypher, path/traversal queries, GDS algorithms, clustering.
- **Usage domain:** Knowledge graphs, fraud detection, recommendations, network analysis.
- **Integration method:** Bolt drivers; Cypher; Aura.
- **Dependencies:** JVM or Aura account.
- **Availability:** GPL community + commercial + Aura. **Maintenance:** Active. **License:** GPL v3 community (not re-verified in this session).
- **Limitations:** GPL for self-host community; scaling writes is harder than reads.
- **Related resources:** Kùzu (embedded graph), SurrealDB (multi-model), Memgraph.
- **Sources:** Graph DB comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.3.5 SurrealDB
- **Canonical identity:** SurrealDB — multi-model database (document/graph/relational/vector).
- **Category:** 3.6.3 · **Type:** Open-source database (Rust) + SurrealDB Cloud.
- **Official URL:** Not verified in this session.
- **Description:** Single binary combining document, graph, relational tables, full-text and vector search; SurrealQL; live queries/real-time.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Multi-model queries, schemafull/schemaless, live queries, embedded or server.
- **Usage domain:** Apps wanting graph+document+vector in one engine.
- **Integration method:** Binary/Docker; SDKs; SurrealQL.
- **Dependencies:** None heavy (single binary).
- **Availability:** Open source + cloud. **Maintenance:** Active. **License:** BSL → Apache 2.0 conversion schedule (not re-verified in this session).
- **Limitations:** Young; BSL licensing nuance; ecosystem smaller than Neo4j/Mongo.
- **Related resources:** Neo4j, Kùzu, ArangoDB (multi-model predecessor).
- **Sources:** Multi-model DB content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.3.6 Kùzu
- **Canonical identity:** Kùzu — embedded graph database.
- **Category:** 3.6.3 · **Type:** Open-source embedded library (C++).
- **Official URL:** Not verified in this session.
- **Description:** DuckDB-style embedded property-graph DB with Cypher; in-process analytics on graphs.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Cypher queries, embedded (no server), vector extension.
- **Usage domain:** Graph analytics in-process, data science, edge.
- **Integration method:** Language bindings (Python/Node/Rust).
- **Dependencies:** None (embedded).
- **Availability:** Open source. **Maintenance:** Active (university-origin). **License:** MIT (not re-verified in this session).
- **Limitations:** Embedded only (no distributed story); young.
- **Related resources:** DuckDB (analog), Neo4j.
- **Sources:** Graph DB content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.6.4 Vector databases & embeddings infra

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.6.4.1 | Qdrant | Qdrant — vector search engine (Rust) | Open source (Apache 2.0) + Cloud | HNSW, filtering, payload indexes, quantization; `qdrant/mcp-server-qdrant` for agents | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.4.2 | Weaviate | Weaviate — vector DB with modules | Open source (BSD-3) + Cloud | Hybrid search, modules (rerankers, generative), multi-tenancy | Search (2026) | Partially verified — Medium |
| 3.6.4.3 | Pinecone | Pinecone — managed vector DB | Hosted service | Serverless indexes, namespaces, metadata filtering; `pinecone-io/pinecone-mcp` | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.4.4 | pgvector | pgvector — vector extension for Postgres | Open-source Postgres extension | `vector` type, HNSW/IVFFlat indexes; zero new infra for Postgres users | Search (2026) | Partially verified — High |
| 3.6.4.5 | Chroma | Chroma — embedding DB (Python-first) | Open source (Apache 2.0) | Simple API, local/server modes; `chroma-core/chroma-mcp` | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.4.6 | Milvus | Milvus — distributed vector DB (LF AI & Data) | Open source (Apache 2.0) | Billion-scale, GPU indexes, Attu UI; Zilliz Cloud managed | Search (2026) | Partially verified — Medium |

## 3.6.5 Search engines

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.6.5.1 | Elasticsearch | Elastic — distributed search/analytics (Java) | Source-available (SSPL/Elastic License) + Elastic Cloud | Full-text, aggregations, ESQL, vector (dense_vector); `elastic/mcp-server-elasticsearch` | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.5.2 | OpenSearch | OpenSearch — Apache-2.0 fork of Elasticsearch (AWS-led) | Open source (Apache 2.0) + AWS managed | Full-text + vector (k-NN), security, alerting | Search (2026) | Partially verified — Medium |
| 3.6.5.3 | Typesense | Typesense — typo-tolerant search API (C++) | Open source (GPLv3) + Cloud | Instant search, faceting, geo, vector; simple API | Search (2026) | Partially verified — Medium |
| 3.6.5.4 | Meilisearch | Meilisearch — instant search engine (Rust) | Open source (MIT) + Cloud | Typo tolerance, ranking rules, multi-index; easy self-host | Search (2026) | Partially verified — Medium |
| 3.6.5.5 | Algolia | Algolia — hosted search & discovery APIs | Hosted service | Hosted indexes, NeuralSearch, Recommend; dashboards + SDKs (see also 3.7.7) | Search (2026) | Partially verified — Medium |

## 3.6.6 ORMs, query builders, data-access layers

### 3.6.6.1 Prisma
- **Canonical identity:** Prisma — ORM + data platform (TS).
- **Category:** 3.6.6 · **Type:** Open-source ORM (npm) + Prisma Postgres/Accelerate (hosted).
- **Official URL:** Not verified in this session.
- **Description:** Schema-first ORM: `schema.prisma` → typed client + migrations; supports Postgres/MySQL/SQLite/SQL Server/MongoDB/Cockroach. **Status change:** Prisma 7 is Rust-free (new TS engine lineage) — reported in 2026 ecosystem content.
- **Contents inspected:** Search coverage of Prisma 7 changes and comparisons vs Drizzle.
- **Actual capabilities:** Typed queries, migrations, seeding, Studio GUI, extensions, Pulse (CDC), Optimize.
- **Usage domain:** TypeScript backends needing typed data access fast.
- **Integration method:** npm; `prisma init/migrate/generate`.
- **Dependencies:** Node.js; database.
- **Availability:** Open source + hosted platform. **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** Abstraction overhead for complex SQL; migration edge cases; engine rewrite churn (v7).
- **Related resources:** Drizzle, TypeORM, Prisma Postgres (3.6.2.5).
- **Sources:** ORM comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.6.2 Drizzle
- **Canonical identity:** Drizzle ORM — lightweight TS ORM.
- **Category:** 3.6.6 · **Type:** Open-source library (npm).
- **Official URL:** Not verified in this session.
- **Description:** SQL-like, thin-layer TS ORM: schema in TS, relational queries, no heavy codegen; serverless-driver friendly.
- **Contents inspected:** Search comparisons (Prisma vs Drizzle).
- **Actual capabilities:** Schema definition, migrations (drizzle-kit), relational query builder, Studio.
- **Usage domain:** Edge/serverless TS apps, teams wanting SQL control.
- **Integration method:** npm; `drizzle-kit`.
- **Dependencies:** Database driver.
- **Availability:** Open source. **Maintenance:** Active. **License:** Apache 2.0 (not re-verified in this session).
- **Limitations:** More manual than Prisma for relations; smaller plugin ecosystem.
- **Related resources:** Prisma, Kysely, Knex.
- **Sources:** ORM comparisons (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.6.3 SQLAlchemy
- **Canonical identity:** SQLAlchemy — Python SQL toolkit/ORM.
- **Category:** 3.6.6 · **Type:** Open-source library (PyPI).
- **Official URL:** Not verified in this session.
- **Description:** Python's standard data-access layer: Core (SQL expression) + ORM (unit of work), Alembic migrations; pairs with FastAPI/Django-alternatives.
- **Contents inspected:** Search references (FastAPI stack content).
- **Actual capabilities:** ORM, connection pooling, dialect support (Postgres/MySQL/SQLite/etc.), async.
- **Usage domain:** Python backends, data engineering.
- **Integration method:** `pip install sqlalchemy`; Alembic for migrations.
- **Dependencies:** DBAPI driver.
- **Availability:** Open source. **Maintenance:** Active (2.x line). **License:** MIT (not re-verified in this session).
- **Limitations:** Learning curve; async patterns newer.
- **Related resources:** Alembic (3.6.7.4), Django ORM, Tortoise ORM.
- **Sources:** Python backend content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

### 3.6.6.4 TypeORM
- **Canonical identity:** TypeORM — TS ORM (DataMapper + ActiveRecord).
- **Category:** 3.6.6 · **Type:** Open-source library (npm).
- **Official URL:** Not verified in this session.
- **Description:** Decorator-based TS ORM supporting many DBs; historically the NestJS default.
- **Contents inspected:** Search references only.
- **Actual capabilities:** Entities, migrations, relations, query builder.
- **Usage domain:** NestJS/TypeScript enterprise apps (legacy default).
- **Integration method:** npm; `typeorm` CLI.
- **Dependencies:** Database driver.
- **Availability:** Open source. **Maintenance:** Maintained (slower cadence; community notes). **License:** MIT (not re-verified in this session).
- **Limitations:** Maintenance velocity concerns vs Prisma/Drizzle; heavy abstraction.
- **Related resources:** Prisma, Drizzle, MikroORM.
- **Sources:** ORM content (search, 2026).
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.6.7 Schema migrations & database DevOps

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.6.7.1 | Atlas (ariga) | Ariga Atlas — "Like Terraform, for databases" | Open source (Apache 2.0 core) + Cloud | Declarative schema-as-code, versioned migrations, drift detection, CI; docs: https://atlasgo.io/?ref=blef.fr (verbatim) | https://atlasgo.io/?ref=blef.fr | Partially verified — Medium |
| 3.6.7.2 | Flyway | Redgate Flyway — versioned SQL migrations (Java) | Open source (Apache 2.0 community) + Teams/Enterprise | Plain-SQL migrations, repeatable migrations, Teams features | Search (2026) | Partially verified — Medium |
| 3.6.7.3 | Liquibase | Liquibase — DB change management (Java) | Open source (Apache 2.0) + commercial | XML/YAML/SQL changelogs, contexts/labels, policy checks | Search (2026) | Partially verified — Medium |
| 3.6.7.4 | Alembic | Alembic — SQLAlchemy migrations (Python) | Open source (MIT) | Autogenerate diffs, versioned scripts | Search (2026) | Partially verified — Medium |
| 3.6.7.5 | golang-migrate | golang-migrate/migrate — Go migration CLI/library | Open source (MIT) | CLI + library, many DB/source drivers | Search (2026) | Partially verified — Medium |
| 3.6.7.6 | dbmate | dbmate — lightweight migration tool | Open source (MIT) | Single binary, plain SQL, framework-agnostic | Search (2026) | Partially verified — Medium |
| 3.6.7.7 | Skeema | Skeema — MySQL schema management | Open source (Apache 2.0; premium) | Declarative MySQL schemas, diff/push, lint | Search (2026) | Partially verified — Medium |

## 3.6.8 Caching & object/file storage

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.6.8.1 | Dragonfly | Dragonfly — Redis-compatible in-memory store (C++) | Source-available (BSL) + Cloud | Multi-threaded, Redis API compat, snapshots | Search (2026) | Partially verified — Medium |
| 3.6.8.2 | Garnet | Garnet — .NET remote cache-store (Microsoft Research) | Open source (MIT) | RESP compatible, high throughput, extensible | Search (2026) | Partially verified — Medium |
| 3.6.8.3 | Upstash | Upstash — serverless Redis/Kafka/QStash | Hosted service | Per-request pricing, REST API, edge replication (context7/skill dedup noted) | Search (2026) | Partially verified — Medium |
| 3.6.8.4 | Memcached | Memcached — distributed memory cache | Open source (BSD) | Simple KV sharding, minimal ops | Search (2026) | Partially verified — Medium |
| 3.6.8.5 | Amazon S3 | AWS S3 — object storage | Hosted service | Buckets, versioning, lifecycle, presigned URLs | Search (2026) | Partially verified — Medium |
| 3.6.8.6 | Cloudflare R2 | R2 — S3-compatible object storage, zero egress | Hosted service | S3 API compat, no egress fees | Search (2026) | Partially verified — Medium |
| 3.6.8.7 | MinIO | MinIO — self-hosted S3-compatible storage (Go) | Open source (AGPLv3) + commercial | Single binary, erasure coding, console | Search (2026) | Partially verified — Medium |
| 3.6.8.8 | Supabase Storage | Supabase Storage — file storage on Postgres | Open source (self-host) + hosted | Buckets, RLS policies, image transforms | Search (2026) | Partially verified — Medium |
| 3.6.8.9 | Uploadthing | Uploadthing — file upload APIs for TS apps | Hosted service + SDK | Upload components, callbacks, infra abstraction (see also 3.7.6) | Search (2026) | Partially verified — Medium |

## 3.6.9 Admin UIs, seed data, test environments

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.6.9.1 | DBeaver | DBeaver — universal DB client (Java) | Open source (Apache 2.0 CE) + Pro | SQL editor, ER diagrams, many drivers | Search (2026) | Partially verified — Medium |
| 3.6.9.2 | pgAdmin | pgAdmin — Postgres administration | Open source (PostgreSQL licence) | Web UI, query tool, server management | Search (2026) | Partially verified — Medium |
| 3.6.9.3 | DataGrip | DataGrip — JetBrains DB IDE | Commercial IDE | Refactoring, inspections, multi-DB | Search (2026) | Partially verified — Medium |
| 3.6.9.4 | TablePlus | TablePlus — native DB GUI (macOS/Windows) | Commercial (freemium) | Fast native client, plugins | Search (2026) | Partially verified — Medium |
| 3.6.9.5 | Prisma Studio / Drizzle Studio | ORM data browsers | Bundled with ORMs | Visual data editing for Prisma/Drizzle projects | Search (2026) | Partially verified — Medium |
| 3.6.9.6 | Faker / factory_boy | Fake-data / fixture generators | Open source (Python/JS ports) | Seed data, factories for tests | Search (2026) | Partially verified — Medium |
| 3.6.9.7 | Testcontainers | Testcontainers — throwaway containers for tests | Open source (MIT) | Postgres/Redis/Kafka etc. in integration tests | Search (2026) | Partially verified — Medium |
| 3.6.9.8 | awesome-db-tools | `datlechin/awesome-db-tools` — curated DB tools list | Awesome-list (docs) | CLI/GUI/backup/migration tool index | https://github.com/datlechin/awesome-db-tools/blob/HEAD/README.md | Partially verified — Medium |

## 3.6.10 Database MCP servers & agent-readable schema resources

> Agent-facing servers that expose schemas, run read-only queries, and let AI agents understand database/API contracts. (Upstash context7 dedup applies — not listed.)

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.6.10.1 | mongodb-mcp-server | `mongodb-js/mongodb-mcp-server` — official MongoDB MCP | Open source MCP server | Schema exploration, query execution, Atlas admin | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.2 | mcp-clickhouse | `ClickHouse/mcp-clickhouse` — official ClickHouse MCP | Open source MCP server | Query ClickHouse, inspect schemas | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.3 | mcp-server-neon | `neondatabase/mcp-server-neon` — official Neon MCP | Open source MCP server | Branching, SQL, project mgmt via MCP | https://github.com/neondatabase/mcp-server-neon (referenced) | Partially verified — Medium |
| 3.6.10.4 | supabase/mcp | `supabase/mcp` (supabase-community) | Open source MCP server | Supabase project/SQL/storage via MCP | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.5 | mcp-redis | `redis/mcp-redis` — official Redis MCP | Open source MCP server | Redis commands/data via MCP | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.6 | mcp-server-elasticsearch | `elastic/mcp-server-elasticsearch` | Open source MCP server | ES queries/mappings via MCP | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.7 | mcp-server-qdrant | `qdrant/mcp-server-qdrant` | Open source MCP server | Vector search ops via MCP | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.8 | chroma-mcp | `chroma-core/chroma-mcp` | Open source MCP server | Chroma collections via MCP | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.9 | pinecone-mcp | `pinecone-io/pinecone-mcp` | Open source MCP server | Pinecone index ops via MCP | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.10 | mcp-server-motherduck | `motherduckdb/mcp-server-motherduck` — DuckDB cloud MCP | Open source MCP server | Query MotherDuck/DuckDB via MCP | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.11 | Snowflake MCP | `Snowflake-Labs/mcp` — official Snowflake MCP | Open source MCP server | Cortex/war
ehouse ops via MCP | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.12 | postgres-mcp | `crystaldba/postgres-mcp` — community Postgres MCP | Open source MCP server | Schema + SQL via MCP | MCP listings (search, 2026) | Partially verified — Medium |
| 3.6.10.13 | hf-mcp-server | `olaservo/hf-mcp-server` — Hugging Face MCP (fs tools) | Open source MCP server | HF dataset/model file ops via MCP | https://github.com/olaservo/hf-mcp-server/blob/HEAD/packages/mcp/content/hf-fs/README.md | Partially verified — Medium |

### 3.6.10.14 Convex — agent-grounded backend platform (gap-analysis candidate)
- **Canonical identity:** Convex — reactive backend platform (`get-convex/convex-backend` open-sourced).
- **Category:** 3.6.10 (+ 3.6.2) · **Type:** Open-source backend (Rust) + Convex Cloud (hosted).
- **Official URL:** https://docs.convex.dev (verbatim, from SKILL.md frontmatter); https://convex.dev (verbatim, from fork README).
- **Description:** TypeScript-defined backend: `schema.ts` data model, queries/mutations/actions in TS with end-to-end type safety, realtime subscriptions, file storage, cron, full-text/vector search. The backend (`get-convex/convex-backend`, ~11k stars per fork README) was open-sourced; a community fork (`bulk-platform/convex-backend`) exists. Publishes official `convex-*` agent skills (per SKILL.md: "Convex's backend development platform").
- **Contents inspected:** convex skill SKILL.md (platform description, docs URL), bulk-platform fork README (open-source note, 11k stars, convex.dev), convex.dev references.
- **Actual capabilities:** Schema-validated document DB, ACID transactions, realtime queries, server functions, scheduled jobs, auth integration (Clerk/Auth0), search/vector search, self-hostable backend.
- **Usage domain:** Reactive web apps; AI apps needing typed backend + agent skills.
- **Integration method:** `npm create convex`; `convex dev`; client libraries; self-host backend binary.
- **Dependencies:** Node.js; Convex account for cloud.
- **Availability:** Open source backend + hosted cloud. **Maintenance:** Active. **License:** Apache 2.0 for backend (per open-source announcement reports — not re-verified in this session).
- **Limitations:** Document-model only (no SQL); Convex-idiom lock-in; self-host is newer than cloud.
- **Related resources:** Supabase, Firebase, Encore; see §3.6.11 gap analysis.
- **Sources:** https://docs.convex.dev · https://convex.dev · https://github.com/bulk-platform/convex-backend · `/opt/hatch/skills/convex/SKILL.md`
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

## 3.6.11 Gap analysis: "Astryx for backends" (opinionated backend design system with agent-readable schema grounding)

**Question from parent:** does a turnkey backend equivalent of Astryx exist — an opinionated backend design system whose schema/contracts are natively agent-readable?

**Finding: no direct equivalent found (Unresolved gap, with partial candidates).**
- **Convex (3.6.10.14)** is the closest: TypeScript `schema.ts` as single source of truth, end-to-end types, official agent skills, open-sourced backend. But it is a *platform*, not an opinionated design *system* (no prescribed domain-modeling conventions, no generated design docs).
- **Encore (3.5.1.13)** gives infra-from-code + auto-generated OpenAPI/typed clients + an MCP server for agents — strong on machine-readable contracts, but again a framework, not a design system.
- **Hasura metadata / ariga Atlas declarative schemas / Supabase auto-generated REST+types** each expose machine-readable contracts, but none package opinionated backend design guidance.
- **What exists instead:** fragmented pieces — OpenAPI→MCP converters (§3.5.9), DB MCP servers (§3.6.10), system-design references (§3.9). No single resource was found that combines opinionated backend architecture conventions with agent-native schema grounding the way Astryx does for frontend design.
- **Confidence:** Medium (30 searches across backend/DB/agent-tooling themes; absence of evidence is not proof, but the search was systematic).
- **Verification date:** 2026-10-10 — **Verification:** Unresolved

---

# 3.7 Application services and reusable capabilities

> For hosted services, records capture official docs + SDK/integration surface rather than repos.

## 3.7.1 Auth services (managed)

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.1.1 | Clerk | Clerk — hosted auth (clerk.com) | Hosted service + SDKs | Drop-in sign-in/user mgmt, orgs, passkeys; Supabase third-party-auth guide: http://supabase.com/docs/guides/auth/third-party/clerk (verbatim) | http://supabase.com/docs/guides/auth/third-party/clerk · auth roundups (search, 2026) | Partially verified — Medium |
| 3.7.1.2 | Auth0 | Auth0 (Okta) — identity platform | Hosted service + SDKs | Universal Login, Actions, orgs, MFA, attack protection | Search (2026) | Partially verified — Medium |
| 3.7.1.3 | WorkOS | WorkOS — B2B auth/SSO infra | Hosted service + APIs | SSO (SAML/OIDC), SCIM directory sync, admin portal | Search (2026) | Partially verified — Medium |
| 3.7.1.4 | Supabase Auth | Supabase Auth (GoTrue) | Open source (self-host) + hosted | Email/social/phone auth, RLS integration, MFA | https://supabase.com/docs/guides/auth/auth-email-templates | Partially verified — High |
| 3.7.1.5 | Firebase Authentication | Google Firebase Auth | Hosted service + SDKs | Phone/social/email, Identity Platform, App Check | Search (2026) | Partially verified — Medium |
| 3.7.1.6 | Stytch — Corrected (Twilio) | Stytch — auth APIs, now a Twilio company | Hosted service + SDKs | Passwordless, MFA, B2B; **acquisition announced 2025-10-30, closed 2025-11-14, $104.1M cash** (per druce/governance vendor wiki citing Twilio SEC filings twlo-20250930.htm, twlo-20251231.htm); brand/APIs continue under Twilio | https://github.com/druce/governance/blob/HEAD/wiki/vendors/stytch.md | Corrected (Partially verified — acquisition via secondary wiki citing SEC filings; filings not opened) — Medium |
| 3.7.1.7 | Descope | Descope — drag-drop auth workflows | Hosted service + SDKs | No-code auth flows, passkeys, MFA | Search (2026) | Partially verified — Medium |
| 3.7.1.8 | FusionAuth | FusionAuth — self-hostable CIAM | Open source (community) + Cloud | SSO, MFA, multi-tenancy, on-prem option | Search (2026) | Partially verified — Medium |
| 3.7.1.9 | SuperTokens | SuperTokens — open-source auth | Open source (core) + managed | Session mgmt, email/password, social, MFA; self-host | Search (2026) | Partially verified — Medium |
| 3.7.1.10 | Kinde | Kinde — auth for SaaS | Hosted service + SDKs | Orgs, billing hooks, fast integration | Search (2026) | Partially verified — Medium |
| 3.7.1.11 | AWS Cognito | Amazon Cognito — user pools/identity pools | Hosted service (AWS) | Hosted UI, federation, device tracking | Search (2026) | Partially verified — Medium |
| 3.7.1.12 | MojoAuth | MojoAuth — passwordless auth | Hosted service + SDKs | Magic links/OTP focused | Search (2026) | Partially verified — Medium |
| 3.7.1.13 | Logto | Logto — open-source Auth0 alternative | Open source (core) + Cloud | OIDC, organizations, RBAC, console | Search (2026) | Partially verified — Medium |
| 3.7.1.14 | SSOJet | SSOJet — SSO-as-API | Hosted service + API | Drop-in enterprise SSO | Search (2026) | Partially verified — Low |

## 3.7.2 Email delivery

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.2.1 | Resend | Resend — developer email API | Hosted service + SDKs | React Email, deliverability, Supabase SMTP guide: https://resend.com/docs/send-with-supabase-smtp (verbatim) | https://resend.com/docs/send-with-supabase-smtp | Partially verified — Medium |
| 3.7.2.2 | Postmark | Postmark — transactional email | Hosted service + API | Templates, inbound parsing, DMARC tooling | Search (2026) | Partially verified — Medium |
| 3.7.2.3 | SendGrid | Twilio SendGrid — email API | Hosted service + SDKs | Marketing + transactional, templates, stats | Search (2026) | Partially verified — Medium |
| 3.7.2.4 | Mailgun | Mailgun (Sinch) — email API | Hosted service + API | Validation, routes, deliverability | Search (2026) | Partially verified — Medium |
| 3.7.2.5 | Amazon SES | AWS Simple Email Service | Hosted service (AWS) | Low-cost SMTP/API, reputation dashboards | Search (2026) | Partially verified — Medium |
| 3.7.2.6 | Mailtrap | Mailtrap — email testing + sending | Hosted service | Fake SMTP for dev, templates, sending API | Search (2026) | Partially verified — Medium |
| 3.7.2.7 | Plunk | Plunk — open-source email platform (AGPL-3.0) | Open source + hosted | Campaigns + transactional; self-hostable | Search (2026) | Partially verified — Medium |
| 3.7.2.8 | Brevo | Brevo (ex-Sendinblue) — CRM + email | Hosted service | Marketing automation, SMS, chat | Search (2026) | Partially verified — Medium |

## 3.7.3 Payments & merchant-of-record

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.3.1 | Stripe | Stripe — payments platform | Hosted service + SDKs/APIs | Payments, Billing, Connect, webhooks, Radar | Search (2026) | Partially verified — Medium |
| 3.7.3.2 | Paddle | Paddle — merchant of record | Hosted service (MoR) | Handles tax/VAT, subscriptions, checkout | Search (2026) | Partially verified — Medium |
| 3.7.3.3 | Lemon Squeezy — Corrected (Stripe) | Lemon Squeezy — MoR for SaaS, **acquired by Stripe (July 2024)** | Hosted service (MoR) | Being folded into **Stripe Managed Payments** (Feb 2026 release per reports) | Acquisition coverage (search, 2026) | Corrected (Partially verified) — Medium |
| 3.7.3.4 | Polar | Polar — MoR for developers (open source) | Open source + hosted MoR | Digital products, checkout, license keys | Search (2026) | Partially verified — Medium |
| 3.7.3.5 | Dodo Payments | Dodo — MoR for global SaaS | Hosted service (MoR) | Tax compliance, subscriptions | Search (2026) | Partially verified — Low |
| 3.7.3.6 | Creem | Creem — MoR for SaaS | Hosted service (MoR) | Checkout, tax handling | Search (2026) | Partially verified — Low |
| 3.7.3.7 | Whop | Whop — digital product marketplace/payments | Hosted service | Storefronts, affiliates, Discord gating | Search (2026) | Partially verified — Medium |
| 3.7.3.8 | Stripe Managed Payments | Stripe's MoR offering (2026) | Hosted service (MoR) | Successor surface for Lemon Squeezy merchants | Search (2026) | Partially verified — Low |

## 3.7.4 Notifications

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.4.1 | Knock | Knock — notification infrastructure | Hosted service + SDKs | Workflows, preferences, batching, multi-channel | Search (2026) | Partially verified — Medium |
| 3.7.4.2 | Courier | Courier — notification orchestration | Hosted service + APIs | Designer, routing, providers abstraction | Search (2026) | Partially verified — Medium |
| 3.7.4.3 | Novu | Novu — open-source notification infra | Open source (core) + Cloud | Workflows, inbox, providers; docs: https://docs.novu.co (verbatim) | https://docs.novu.co | Partially verified — Medium |
| 3.7.4.4 | OneSignal | OneSignal — push/email/SMS | Hosted service + SDKs | Journeys, segmentation, in-app | Search (2026) | Partially verified — Medium |
| 3.7.4.5 | MagicBell | MagicBell — notification inbox | Hosted service + SDKs | In-app inbox, preferences | Search (2026) | Partially verified — Medium |
| 3.7.4.6 | Pingram | Pingram — notification service | Hosted service (per listings) | Notification delivery | Search (2026) | Partially verified — Low |
| 3.7.4.7 | Customer.io | Customer.io — lifecycle messaging | Hosted service | Behavioral triggers, campaigns | Search (2026) | Partially verified — Medium |

## 3.7.5 Maps & geolocation

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.5.1 | Mapbox | Mapbox — maps platform | Hosted service + SDKs | GL maps, geocoding, directions, Studio | Search (2026) | Partially verified — Medium |
| 3.7.5.2 | Google Maps Platform | Google — maps APIs | Hosted service + SDKs | Places, routes, geocoding, JS SDK | Search (2026) | Partially verified — Medium |
| 3.7.5.3 | MapLibre | MapLibre — open map rendering (fork of Mapbox GL) | Open source (BSD-3) | GL JS/Native, community-driven | Search (2026) | Partially verified — Medium |
| 3.7.5.4 | Leaflet | Leaflet — lightweight JS map library | Open source (BSD-2) | Simple interactive maps, plugins | Search (2026) | Partially verified — Medium |
| 3.7.5.5 | OpenLayers | OpenLayers — full-featured JS mapping | Open source (BSD-2) | Projections, WMS/WMTS, vector tiles | Search (2026) | Partially verified — Medium |
| 3.7.5.6 | MapTiler | MapTiler — map tiles/hosting | Hosted service + SDKs | Vector tiles, geocoding, self-host option | Search (2026) | Partially verified — Medium |
| 3.7.5.7 | Stadia Maps | Stadia — map tiles/APIs | Hosted service | Tiles, routing, static maps | Search (2026) | Partially verified — Low |
| 3.7.5.8 | LocationIQ | LocationIQ — geocoding API | Hosted service | Forward/reverse geocode, autocomplete | Search (2026) | Partially verified — Medium |
| 3.7.5.9 | HERE | HERE — location platform | Hosted service + SDKs | Maps, routing, traffic, fleet | Search (2026) | Partially verified — Medium |
| 3.7.5.10 | OpenCage | OpenCage — geocoding API | Hosted service | Aggregated geocoders, generous free tier | Search (2026) | Partially verified — Medium |
| 3.7.5.11 | Protomaps | Protomaps — open map stack | Open source (BSD) + hosted | Single-file PMTiles, basemap, self-host | Search (2026) | Partially verified — Medium |

## 3.7.6 Scheduling

### 3.7.6.1 Cal.com — Corrected (closed-source, Apr 2026)
- **Canonical identity:** Cal.com — scheduling platform (was `calcom/cal.com`).
- **Category:** 3.7.6 · **Type:** Hosted service (closed-source since 2026-04-14).
- **Official URL:** https://cal.com/blog/cal-diy-open-source-to-closed-source (verbatim — company's own announcement of the license change).
- **Description:** Scheduling/booking platform. **Correction:** the production repo was privatized on 2026-04-14; the prior MIT repo (41.2k stars) is no longer public. The company published an MIT community fork `calcom/cal.diy`, feature-stripped: no Teams/Organizations, SAML/SCIM, Workflows, Routing Forms, Insights, AI agent (per cal.com blog, pinggy-io article, dayotter comparison, serversathome wiki — all search-corroborated). CEO cited AI-assisted vulnerability scanning of the public repo as rationale.
- **Contents inspected:** Announcement URL surfaced; corroborating articles/wiki listed (not opened).
- **Actual capabilities:** Event types, booking pages, team scheduling (hosted), calendar integrations, webhooks/API.
- **Usage domain:** Booking/scheduling UX, sales/demo booking.
- **Integration method:** Hosted app; API/webhooks; self-host via cal.diy fork.
- **Dependencies:** Cal.com account (hosted).
- **Availability:** Hosted (free/paid); fork self-hostable. **Maintenance:** Active. **License:** Proprietary (hosted); MIT for cal.diy fork.
- **Limitations:** Self-host fork lacks enterprise features; migration from old `cal.com` repo versions is manual.
- **Related resources:** Cal.diy (3.7.6.2), Calendly, Nylas.
- **Sources:** https://cal.com/blog/cal-diy-open-source-to-closed-source · https://github.com/pinggy-io/pinggy_website/blob/HEAD/content/blog/posts/calendly_alternatives.md · https://github.com/dayotter/dayotter · https://github.com/serversathome/wiki/blob/HEAD/caldiy.md
- **Verification date:** 2026-10-10 — **Verification:** Corrected (Partially verified — announcement URL + 4 corroborating sources; company blog not opened) — **Confidence:** Medium

### 3.7.6.2 Cal.diy
- **Canonical identity:** `calcom/cal.diy` — MIT community fork of Cal.com.
- **Category:** 3.7.6 · **Type:** Open-source app (Next.js).
- **Official URL:** Not verified in this session.
- **Description:** The open MIT fork published by Cal.com at privatization; individual scheduling without enterprise modules.
- **Contents inspected:** dayotter comparison + serversathome wiki (search).
- **Actual capabilities:** Personal event types, booking pages, calendar sync.
- **Usage domain:** Self-hosted personal scheduling.
- **Integration method:** Self-host (Docker/Vercel).
- **Dependencies:** Database (Postgres).
- **Availability:** Open source (MIT). **Maintenance:** Community/company-maintained fork. **License:** MIT.
- **Limitations:** No Teams/Orgs, SAML/SCIM, Workflows, Routing Forms, Insights, AI agent.
- **Related resources:** Cal.com, DayOtter.
- **Sources:** https://github.com/dayotter/dayotter · https://github.com/serversathome/wiki/blob/HEAD/caldiy.md
- **Verification date:** 2026-10-10 — **Verification:** Partially verified — **Confidence:** Medium

| # | Resource | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|
| 3.7.6.3 | Nylas — calendar/email APIs | Hosted service + SDKs | Universal calendar sync, scheduling, email API | Search (2026) | Partially verified — Medium |
| 3.7.6.4 | Cronofy — calendar API | Hosted service + API | Scheduling, availability, conferencing; dev portal: https://www.cronofy.com/developer (verbatim) | https://www.cronofy.com/developer | Partially verified — Medium |
| 3.7.6.5 | Calendly — scheduling | Hosted service | Booking pages, routing, team scheduling | Search (2026) | Partially verified — Medium |
| 3.7.6.6 | DayOtter — open scheduling (AGPLv3) | Open source (AGPLv3) | Self-hosted Cal.com alternative; compared in dayotter repo | https://github.com/dayotter/dayotter | Partially verified — Medium |

## 3.7.7 Media & file processing

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.7.1 | Cloudinary | Cloudinary — media management | Hosted service + SDKs | Upload, transforms, optimization, DAM | Search (2026) | Partially verified — Medium |
| 3.7.7.2 | Mux | Mux — video API | Hosted service + SDKs | Upload/encode/stream, player, analytics | Search (2026) | Partially verified — Medium |
| 3.7.7.3 | Uploadthing | Uploadthing — file uploads for TS | Hosted service + SDK | Components, callbacks (see 3.6.8.9) | Search (2026) | Partially verified — Medium |
| 3.7.7.4 | ImageKit | ImageKit — image/video optimization | Hosted service + SDKs | Real-time transforms, DAM, CDN | Search (2026) | Partially verified — Medium |
| 3.7.7.5 | Shotstack | Shotstack — video editing API | Hosted service + API | Templated video rendering | Search (2026) | Partially verified — Medium |
| 3.7.7.6 | Creatomate | Creatomate — video/image automation API | Hosted service + API | Template-based rendering | Search (2026) | Partially verified — Medium |
| 3.7.7.7 | SammaPix | SammaPix — media service (per listings) | Hosted service (per listings) | Media processing | Search (2026) | Partially verified — Low |

## 3.7.8 Search services, analytics, feature flags

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.8.1 | Algolia — search API | Hosted service + SDKs | Hosted search indexes, Recommend, dashboards | Search (2026) | Partially verified — Medium |
| 3.7.8.2 | PostHog — product analytics (open source) | Open source (MIT core) + Cloud | Events, funnels, session replay, feature flags, experiments; comparison: https://posthog.com/compare/best-growthbook-alternatives (verbatim) | https://posthog.com/compare/best-growthbook-alternatives | Partially verified — Medium |
| 3.7.8.3 | Mixpanel — product analytics | Hosted service + SDKs | Events, funnels, cohorts | Search (2026) | Partially verified — Medium |
| 3.7.8.4 | Amplitude — product analytics | Hosted service + SDKs | Behavioral analytics, experimentation | Search (2026) | Partially verified — Medium |
| 3.7.8.5 | LaunchDarkly — feature flags | Hosted service + SDKs | Flags, targeting, experiments | Search (2026) | Partially verified — Medium |
| 3.7.8.6 | GrowthBook — open feature flags/experiments | Open source (MIT) + Cloud | Flags, A/B tests, Bayesian stats | Search (2026) | Partially verified — Medium |
| 3.7.8.7 | Unleash — open feature toggles | Open source (Apache 2.0) + hosted | Flags, strategies, variants | Search (2026) | Partially verified — Medium |
| 3.7.8.8 | Flagsmith — open feature flags | Open source + Cloud | Flags, segments, A/B | Search (2026) | Partially verified — Medium |

## 3.7.9 E-commerce integrations (headless commerce)

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.9.1 | Medusa | Medusa — headless commerce (Node) | Open source (MIT) + Cloud | Modules (cart/order/payment), admin, storefront starters | Search (2026); https://github.com/torkiv-labs/nexuq/blob/HEAD/docs/research/competitive-analysis-headless-commerce-2026-08-27.md | Partially verified — Medium |
| 3.7.9.2 | Saleor | Saleor — headless commerce (Python/Django) | Open source (BSD-3) + Cloud | GraphQL-first, channels, apps | Same competitive analysis | Partially verified — Medium |
| 3.7.9.3 | Shopify / Hydrogen | Shopify — commerce platform; Hydrogen (Remix storefront) | Hosted + open-source Hydrogen (MIT) | Storefront API, checkout, Hydrogen framework | Same competitive analysis | Partially verified — Medium |
| 3.7.9.4 | Vendure | Vendure — headless commerce (NestJS/TS) | Open source (MIT) + Cloud | Plugin architecture, admin UI, GraphQL | Same competitive analysis | Partially verified — Medium |
| 3.7.9.5 | BigCommerce | BigCommerce — SaaS commerce | Hosted service | Headless APIs, multi-storefront | Same competitive analysis | Partially verified — Medium |
| 3.7.9.6 | commercetools | commercetools — composable commerce | Hosted service (SaaS) | API-first, enterprise | Same competitive analysis | Partially verified — Medium |
| 3.7.9.7 | Spree / Solidus | Spree/Solidus — Rails commerce | Open source (MIT/BSD) | Rails storefronts, long-lived OSS | Same competitive analysis | Partially verified — Medium |

## 3.7.10 Headless CMS

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.10.1 | Sanity | Sanity — structured content platform | Hosted + open-source Studio (MIT) | GROQ queries, live preview, Studio editor | Search (2026) | Partially verified — Medium |
| 3.7.10.2 | Contentful | Contentful — headless CMS | Hosted service | Content APIs, Compose/Launch apps | Search (2026) | Partially verified — Medium |
| 3.7.10.3 | Strapi | Strapi — open headless CMS (Node) | Open source (SEE license v5) + Cloud | Admin panel, REST/GraphQL, plugins | Search (2026) | Partially verified — Medium |
| 3.7.10.4 | Payload — Corrected (Figma) | Payload CMS — TS headless CMS, **acquired by Figma (June 2025)** | Open source (MIT) | Admin UI auto-generated, Postgres/Mongo; MIT intact; Payload Cloud paused new sign-ups (per reports) | Acquisition coverage (search, 2026) | Corrected (Partially verified) — Medium |
| 3.7.10.5 | Directus | Directus — headless data platform | Open source (GPLv3) + Cloud | Wraps SQL DBs with APIs + no-code app | Search (2026) | Partially verified — Medium |
| 3.7.10.6 | Storyblok | Storyblok — visual headless CMS | Hosted service | Visual editor, components | Search (2026) | Partially verified — Medium |
| 3.7.10.7 | Hygraph | Hygraph (ex-GraphCMS) — GraphQL CMS | Hosted service | GraphQL-native content APIs | Search (2026) | Partially verified — Medium |

## 3.7.11 i18n & localization services

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.11.1 | Crowdin | Crowdin — localization platform | Hosted service + API/CLI | Workflows, MT, translators marketplace | Search (2026) | Partially verified — Medium |
| 3.7.11.2 | Lokalise | Lokalise — localization platform | Hosted service + API | Keys, OTA, Figma plugin | Search (2026) | Partially verified — Medium |
| 3.7.11.3 | Tolgee | Tolgee — open-source i18n | Open source (Apache 2.0) + Cloud | In-context editing, SDKs | Search (2026) | Partially verified — Medium |
| 3.7.11.4 | Transifex | Transifex — localization platform | Hosted service | Workflows, native SDKs | Search (2026) | Partially verified — Medium |
| 3.7.11.5 | Phrase | Phrase (ex-Memsource) — localization suite | Hosted service | TMS + strings, MT | Search (2026) | Partially verified — Medium |
| 3.7.11.6 | Localize | Localize — JS translation | Hosted service | In-context JS library | Search (2026) | Partially verified — Low |

## 3.7.12 Public datasets & data directories

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.12.1 | Hugging Face Datasets | `datasets` library + Hub | Open source (Apache 2.0) + Hub | 100k+ datasets, `hf://` URI scheme (newer), streaming, `hf-mcp-server` fs tools | https://github.com/olaservo/hf-mcp-server/blob/HEAD/packages/mcp/content/hf-fs/README.md | Partially verified — Medium |
| 3.7.12.2 | Kaggle | Kaggle — datasets/competitions (Google) | Hosted platform | Datasets, notebooks, competitions | Search (2026) | Partially verified — Medium |
| 3.7.12.3 | Common Crawl | Common Crawl — web crawl corpus | Open data (nonprofit) | Petabyte-scale crawls, columnar indexes | Search (2026) | Partially verified — Medium |
| 3.7.12.4 | OpenAlex | OpenAlex — scholarly data API | Open data (nonprofit) + API | Works/authors/venues graph, free API | Search (2026) | Partially verified — Medium |
| 3.7.12.5 | awesome-public-datasets | `awesomedata/awesome-public-datasets` | Awesome-list (docs) | Topic-indexed public datasets | https://github.com/awesomedata/awesome-public-datasets/ | Partially verified — Medium |

## 3.7.13 API integration libraries

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.7.13.1 | Composio | Composio — managed tool integrations (see skills workstream — cross-ref only) | Platform + `composiohq/skills` (dedup) | 250+ app integrations as agent tools | Skills workstream | Cross-reference — N/A |
| 3.7.13.2 | Nango | Nango — product integrations platform (OAuth/proxy) | Open source (MIT) + Cloud | 300+ integrations, unified APIs, sync | Search (2026) | Partially verified — Medium |
| 3.7.13.3 | Merge | Merge — unified B2B APIs (HR/ATS/CRM) | Hosted service + SDKs | Normalized HR/accounting/CRM APIs | Search (2026) | Partially verified — Medium |
| 3.7.13.4 | Apideck | Apideck — unified APIs | Hosted service + SDKs | CRM/HR/accounting normalization, Vault | Search (2026) | Partially verified — Medium |

---

# 3.8 Website platforms and application generators

> Hosted services vs open-source tools are distinguished in each record's Type.

## 3.8.1 AI website/app builders (prompt-to-app)

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.8.1.1 | Lovable | Lovable — AI app builder | Hosted service | Prompt → full-stack app, Supabase/GitHub integration | Search (2026) | Partially verified — Medium |
| 3.8.1.2 | Bolt.new (+ bolt.diy) | Bolt.new (StackBlitz) — prompt-to-app; `bolt.diy` community fork | Hosted service + open fork | In-browser dev (WebContainers), fork self-hostable | Search (2026) | Partially verified — Medium |
| 3.8.1.3 | v0 | v0 (Vercel) — AI UI generation | Hosted service | Prompt → React/shadcn components, Vercel deploy | Search (2026) | Partially verified — Medium |
| 3.8.1.4 | Replit Agent | Replit — AI agent workspace | Hosted service | Agent builds/deploys apps in Replit | Search (2026) | Partially verified — Medium |
| 3.8.1.5 | Taskade Genesis | Taskade — AI agents/workspace builder | Hosted service | Agent workflows + app generation | Search (2026) | Partially verified — Medium |
| 3.8.1.6 | Dyad | Dyad — local AI app builder | Open-source-ish app (per listings; license not verified) | Local-first AI builder, Supabase connect | Search (2026) | Partially verified — Low |
| 3.8.1.7 | Massvai | Massvai — AI website builder (per listings) | Hosted service (per listings) | AI site generation | Search (2026) | Partially verified — Low |
| 3.8.1.8 | Onlook | Onlook — open-source visual AI builder (MIT, ~25.9k stars) | Open source (MIT) | Visual editor + AI, Next.js/Tailwind | Search (2026) | Partially verified — Medium |
| 3.8.1.9 | Google Stitch | Google Stitch (Labs) — AI UI design | Hosted (Google Labs) | Prompt → UI designs, Figma export | Search (2026) | Partially verified — Medium |

## 3.8.2 Visual dev & low/no-code platforms

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.8.2.1 | Webflow | Webflow — visual web builder | Hosted service | Designer, CMS, Logic, hosting | Search (2026) | Partially verified — Medium |
| 3.8.2.2 | Framer | Framer — design-to-site | Hosted service | Figma-like canvas → site, CMS, effects | Search (2026) | Partially verified — Medium |
| 3.8.2.3 | Bubble | Bubble — no-code web apps | Hosted service | Visual programming, DB, plugins | Search (2026) | Partially verified — Medium |
| 3.8.2.4 | FlutterFlow | FlutterFlow — visual Flutter builder | Hosted service | Firebase/Supabase backends, code export | Search (2026) | Partially verified — Medium |
| 3.8.2.5 | Softr | Softr — Airtable/Sheets → apps | Hosted service | Portals, internal tools | Search (2026) | Partially verified — Medium |
| 3.8.2.6 | Glide | Glide — spreadsheets → apps | Hosted service | Mobile/web apps from data | Search (2026) | Partially verified — Medium |
| 3.8.2.7 | Retool | Retool — internal tools builder | Hosted/self-host | Drag-drop admin panels, 100+ integrations | Search (2026) | Partially verified — Medium |
| 3.8.2.8 | Appsmith | Appsmith — open internal tools | Open source (Apache 2.0) + Cloud | Widgets, JS queries, self-host | Search (2026) | Partially verified — Medium |
| 3.8.2.9 | Budibase | Budibase — open low-code | Open source (GPLv3) + Cloud | Internal apps, automations | Search (2026) | Partially verified — Medium |
| 3.8.2.10 | NocoBase | NocoBase — open no-code platform | Open source (AGPLv3) + commercial | Data-model-driven apps, plugins | Search (2026) | Partially verified — Medium |
| 3.8.2.11 | ToolJet | ToolJet — open low-code | Open source (GPLv3) + Cloud | App builder, workflows | Search (2026) | Partially verified — Medium |

## 3.8.3 Code generators (scaffolding)

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.8.3.1 | Yeoman | Yeoman — scaffolding system (`yo`) | Open source (BSD-2) | Generators ecosystem (`generator-*`) | Search (2026) | Partially verified — Medium |
| 3.8.3.2 | Plop | Plop — micro-generator | Open source (MIT) | In-repo templates, CLI prompts | Search (2026) | Partially verified — Medium |
| 3.8.3.3 | Hygen | Hygen — code generator | Open source (MIT) | Templates + CLI, Rails-like generators | Search (2026) | Partially verified — Medium |
| 3.8.3.4 | Cookiecutter | Cookiecutter — project templates (Python) | Open source (BSD-3) | Cross-language templating | Search (2026) | Partially verified — Medium |

## 3.8.4 Screenshot/design-to-code

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.8.4.1 | screenshot-to-code | `abi/screenshot-to-code` — GPT-4 Vision → code | Open source (per repo) | Screenshot/mockup → HTML/Tailwind/React | https://github.com/abi/screenshot-to-code | Partially verified — Medium |
| 3.8.4.2 | Builder.io Visual Copilot | Builder.io — visual headless CMS + AI | Hosted service + open parts | Figma → code, Visual Copilot | Search (2026) | Partially verified — Medium |
| 3.8.4.3 | Anima | Anima — design-to-code | Hosted service + plugin | Figma → React/HTML | Search (2026) | Partially verified — Medium |
| 3.8.4.4 | Locofy | Locofy — design-to-code | Hosted service + plugin | Figma/XD → React/Next/Vue | Search (2026) | Partially verified — Medium |
| 3.8.4.5 | TeleportHQ | TeleportHQ — low-code front-end | Hosted service + open codegen | Design → code, open-source generators | Search (2026) | Partially verified — Medium |
| 3.8.4.6 | Uizard | Uizard — AI wireframe/design | Hosted service | Screenshot/sketch → editable UI | Search (2026) | Partially verified — Medium |
| 3.8.4.7 | Fronty | Fronty — image-to-HTML | Hosted service | Screenshot → HTML/CSS | Search (2026) | Partially verified — Low |
| 3.8.4.8 | Figma Dev Mode MCP | Figma — official MCP server | Hosted feature (Figma) | Design context → code agents | Search (2026) | Partially verified — Medium |
| 3.8.4.9 | Magic Patterns | Magic Patterns — AI prototyping | Hosted service | Prompt → prototypes | Search (2026) | Partially verified — Low |

## 3.8.5 CRUD/admin & backend scaffolding generators

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.8.5.1 | Refine | Refine — React CRUD framework (34.8k stars) | Open source (MIT) | Data providers, auth, auto UI from APIs | Search (2026) | Partially verified — Medium |
| 3.8.5.2 | Amplication | Amplication — backend codegen | Open source + Cloud | DB schema → Node/NestJS/Prisma backend + admin | Search (2026) | Partially verified — Medium |
| 3.8.5.3 | JHipster | JHipster — full-stack generator (Java+JS) | Open source (Apache 2.0) | Spring Boot + Angular/React/Vue scaffolds | Search (2026) | Partially verified — Medium |
| 3.8.5.4 | AdminLTE | AdminLTE — admin dashboard template (45k stars) | Open source (MIT) | Bootstrap admin theme | Search (2026) | Partially verified — Medium |
| 3.8.5.5 | Forest Admin | Forest Admin — admin panel as service | Hosted service | Auto admin from DB, roles | Search (2026) | Partially verified — Medium |

## 3.8.6 Boilerplates, starters, full-stack templates

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.8.6.1 | ShipFast | ShipFast — Next.js SaaS boilerplate | Commercial template | Auth/payments/email wired | Search (2026) | Partially verified — Medium |
| 3.8.6.2 | Supastarter | Supastarter — SaaS starter (Next/Nuxt/Svelte) | Commercial template | Multi-framework starters | Search (2026) | Partially verified — Medium |
| 3.8.6.3 | MakerKit | MakerKit — SaaS kits (Next/Remix) | Commercial template | Supabase/Firebase variants | Search (2026) | Partially verified — Medium |
| 3.8.6.4 | SaaS Pegasus | SaaS Pegasus — Django SaaS boilerplate | Commercial template | Django all-in-one | Search (2026) | Partially verified — Medium |
| 3.8.6.5 | open-saas | `wasp-lang/open-saas` — free SaaS template | Open source (MIT) | Wasp + React + Node SaaS starter | https://github.com/wasp-lang/open-saas | Partially verified — Medium |
| 3.8.6.6 | create-t3-app | `t3-oss/create-t3-app` — T3 stack CLI | Open source (MIT) | Next.js + tRPC + Tailwind + Prisma/NextAuth | Search (2026) | Partially verified — Medium |
| 3.8.6.7 | create-next-app | Next.js official scaffolder | Open source (MIT) | `create-next-app` templates | Search (2026) | Partially verified — Medium |
| 3.8.6.8 | LaunchKit | LaunchKit — PHP/Laravel kits (per listings) | Commercial template | Laravel starters | Search (2026) | Partially verified — Low |
| 3.8.6.9 | Gravity | Gravity — Rails SaaS boilerplate (per listings) | Commercial template | Rails + Stripe | Search (2026) | Partially verified — Low |
| 3.8.6.10 | LaraCopilot | LaraCopilot — Laravel AI starter (per listings) | Product (per listings) | Laravel scaffolding | Search (2026) | Partially verified — Low |
| 3.8.6.11 | NuxSaaS | NuxSaaS — Nuxt SaaS template | Commercial/open (per listings) | Nuxt + Supabase | Search (2026) | Partially verified — Low |
| 3.8.6.12 | GoVueKit | GoVueKit — Go+Vue starter (per listings) | Template (per listings) | Go backend + Vue | Search (2026) | Partially verified — Low |
| 3.8.6.13 | RedwoodJS | RedwoodJS — full-stack React framework | Open source (MIT) | Opinionated GraphQL+Prisma+React | Search (2026) | Partially verified — Medium |
| 3.8.6.14 | Wasp | Wasp — full-stack DSL (see open-saas) | Open source (MIT) | Config-as-code full-stack | Search (2026) | Partially verified — Medium |
| 3.8.6.15 | AdonisJS | AdonisJS — Node MVC framework | Open source (MIT) | Laravel-like Node, Lucid ORM | Search (2026) | Partially verified — Medium |
| 3.8.6.16 | Nuxt | Nuxt — Vue full-stack framework | Open source (MIT) | SSR, server engine (Nitro) | Search (2026) | Partially verified — Medium |
| 3.8.6.17 | Ant Design Pro | `ant-design/ant-design-pro` (38.3k stars) — admin template | Open source (MIT) | Enterprise admin scaffolding | Search (2026) | Partially verified — Medium |

## 3.8.7 Landing-page & e-commerce builders

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.8.7.1 | Unicorn Platform | Unicorn Platform — landing pages for startups | Hosted service | AI copy, templates, blog | Search (2026) | Partially verified — Medium |
| 3.8.7.2 | Carrd | Carrd — one-page sites | Hosted service (freemium) | Simple landing pages | Search (2026) | Partially verified — Medium |
| 3.8.7.3 | Typedream | Typedream — Notion-like site builder | Hosted service | Doc-style websites | Search (2026) | Partially verified — Medium |
| 3.8.7.4 | Shopify | Shopify — commerce platform (hosted) | Hosted service | Storefronts, checkout, apps | Search (2026); headless-commerce analysis | Partially verified — Medium |
| 3.8.7.5 | WooCommerce | WooCommerce — WordPress commerce | Open source (GPL) plugin | Self-hosted stores on WP | Search (2026) | Partially verified — Medium |

---

# 3.9 Architecture and software engineering references

> Patterns, guides, and example repos — not executable frameworks. A pattern reference is recorded as Type: Reference/Guide/Example repo, never as a framework.

## 3.9.1 System design & architecture guides

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.9.1.1 | system-design-primer | `donnemartin/system-design-primer` (367k stars) | Reference repo (docs) | Org of topics, Anki cards, interview prep | https://github.com/donnemartin/system-design-primer | Partially verified — Medium |
| 3.9.1.2 | nodebestpractices | `goldbergyoni/nodebestpractices` (106k stars) | Reference repo (docs) | 80+ Node best practices, translations | Search (2026) | Partially verified — Medium |
| 3.9.1.3 | bulletproof-react | `alan2207/bulletproof-react` (36k stars) | Reference repo (docs + example) | Scalable React architecture, project structure doc: https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md (verbatim) | https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md | Partially verified — Medium |
| 3.9.1.4 | realworld (Conduit) | `gothinkster/realworld` — full-stack "Medium clone" specs + impls | Example spec + impl repos | Same API spec in 100+ stacks; frontend-decomp Conduit example: https://github.com/frontend-decomp/conduit-realworld-example-app (verbatim) | https://github.com/frontend-decomp/conduit-realworld-example-app | Partially verified — Medium |
| 3.9.1.5 | Microsoft API Guidelines | `microsoft/api-guidelines` | Reference (docs) | REST API design guidance | Search (2026) | Partially verified — Medium |
| 3.9.1.6 | Google API Design Guide | Google AIP (aip.dev) | Reference (docs) | API design patterns (AIPs) | Search (2026) | Partially verified — Medium |
| 3.9.1.7 | 12factor.net | 12-Factor App methodology | Reference (docs) | SaaS app principles | Search (2026) | Partially verified — Medium |
| 3.9.1.8 | DDIA | "Designing Data-Intensive Applications" (dataintensive.net) | Book reference | Storage/replication/partitioning foundations | Search (2026) | Partially verified — Medium |
| 3.9.1.9 | Google SRE Book | Google SRE (sre.google) | Reference (books/docs) | Reliability engineering practices | Search (2026) | Partially verified — Medium |
| 3.9.1.10 | AWS Well-Architected | AWS Well-Architected Framework | Reference (docs) | 6 pillars, lenses, labs | Search (2026) | Partially verified — Medium |
| 3.9.1.11 | Azure Architecture Center | Microsoft Cloud Adoption/Architecture guidance | Reference (docs) | Patterns, reference architectures | Search (2026) | Partially verified — Medium |

## 3.9.2 Design patterns & domain modeling

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.9.2.1 | martinfowler.com | Martin Fowler — patterns/essays | Reference (articles) | Refactoring, DDD, microservices, EDA | Search (2026) | Partially verified — Medium |
| 3.9.2.2 | refactoring.guru | Refactoring.Guru — patterns catalog | Reference (interactive docs) | Design patterns, refactoring, SOLID | Search (2026) | Partially verified — Medium |
| 3.9.2.3 | Enterprise Integration Patterns | EIP (Hohpe/Woolf) — messaging patterns | Book reference | 65 integration patterns | Search (2026) | Partially verified — Medium |
| 3.9.2.4 | awesome-software-design | `Vaskivskyi/awesome-software-design`-style lists (generic) | Awesome-list | Curated design resources | Search (2026) | Partially verified — Low |

## 3.9.3 Architecture decision records (ADRs)

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.9.3.1 | adr-tools | `npryce/adr-tools` — ADR CLI | Open source tool (MIT) | Init/new/link/list ADRs as Markdown | https://github.com/npryce/adr-tools | Partially verified — Medium |
| 3.9.3.2 | adr-kit | `luochang212/adr-kit` — ADR templates/toolkit | Open source (per repo) | Templates + guidance | https://github.com/luochang212/adr-kit | Partially verified — Medium |
| 3.9.3.3 | adrs (Rust) | `joshrotenberg/adrs` — ADR tool in Rust, ships MCP server | Open source tool | ADR management + MCP server for agents | https://github.com/joshrotenberg/adrs | Partially verified — Medium |
| 3.9.3.4 | log4brains | log4brains — ADR knowledge base generator | Open source (MIT) | Static site from ADRs | Search (2026) | Partially verified — Medium |

## 3.9.4 Architecture modeling & documentation

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.9.4.1 | Structurizr / C4 | Structurizr — C4 model tooling | Open source (Apache 2.0) + Cloud | Diagrams-as-code, workspaces | Search (2026) | Partially verified — Medium |
| 3.9.4.2 | arc42 | arc42 — architecture doc template | Open template (CC-BY-SA) | 12-section arch documentation | Search (2026) | Partially verified — Medium |

## 3.9.5 Dependency analysis & modular architecture tooling

| # | Resource | Canonical identity | Type | Observed | Sources | Verification |
|---|---|---|---|---|---|---|
| 3.9.5.1 | dependency-cruiser | dependency-cruiser — JS/TS dep linting | Open source (MIT) | Enforce module boundaries, detect cycles | Search (2026) | Partially verified — Medium |
| 3.9.5.2 | madge | madge — module dependency graphs | Open source (MIT) | Circular dep detection, graphs | Search (2026) | Partially verified — Medium |
| 3.9.5.3 | ArchUnit family | ArchUnit (Java), ArchUnitNET, ArchUnitTS, konsist (Kotlin), tach (Python) | Open source test libs | Architecture-as-unit-tests | Search (2026) | Partially verified — Medium |

---

# Coverage note

## Counts (as of 2026-10-10)

- **Distinct resources recorded:** ~240 (full records + table rows; dedup cross-references excluded from counts).
- **Inspected (primary source opened this session):** 3 — `nextauthjs/next-auth` README, `bbonnin/openapi-to-mcp` README, `TykTechnologies/api-to-mcp` README.
- **Verified:** 3 (the three above).
- **Corrected:** 5 — Auth.js→Better Auth recommendation; Cal.com closed-source (2026-04-14); Stytch→Twilio acquisition; Lemon Squeezy→Stripe acquisition; Payload CMS→Figma acquisition.
- **Archived:** 3 — MongoDB Atlas App Services (EOL 2025-09-30); Optic (Jan 2026); Dredd (May 2024).
- **Partially verified:** ~225 (identity/type/status corroborated by ≥1 search source; primary source not opened this session).
- **Unverified:** 4 (§3.5.9.3–3.5.9.5, §3.5.9.7 — OpenAPI→MCP long tail).
- **Unresolved:** 2 (§3.5.9.6 anythingmcp — insufficient evidence; §3.6.11 Astryx-backend gap — no turnkey equivalent found).
- **Historical:** 1 (Lucia — discontinued).

### Per-subcategory counts (approx.)

| Subcategory | Count |
|---|---|
| 3.5.1 Backend frameworks | 13 |
| 3.5.2 GraphQL | 4 |
| 3.5.3 RPC | 2 |
| 3.5.4 API gateways | 5 |
| 3.5.5 OpenAPI / contract testing | 13 |
| 3.5.6 Identity & auth | 6 |
| 3.5.7 Serverless / edge | 3 |
| 3.5.8 Real-time / queues / brokers | 12 |
| 3.5.9 OpenAPI→MCP tools | 7 |
| 3.6.1 Relational DBs | 5 |
| 3.6.2 Serverless Postgres | 6 |
| 3.6.3 NoSQL | 6 |
| 3.6.4 Vector DBs | 6 |
| 3.6.5 Search engines | 5 |
| 3.6.6 ORMs | 4 |
| 3.6.7 Migrations | 7 |
| 3.6.8 Caching / storage | 9 |
| 3.6.9 Admin UIs / seeds / test | 8 |
| 3.6.10 DB MCP servers & agent-schema | 14 |
| 3.7.1 Auth services | 14 |
| 3.7.2 Email | 8 |
| 3.7.3 Payments | 8 |
| 3.7.4 Notifications | 7 |
| 3.7.5 Maps | 11 |
| 3.7.6 Scheduling | 6 |
| 3.7.7 Media | 7 |
| 3.7.8 Search/analytics/flags | 8 |
| 3.7.9 E-commerce | 7 |
| 3.7.10 CMS | 7 |
| 3.7.11 i18n | 6 |
| 3.7.12 Datasets | 5 |
| 3.7.13 API integration libs | 4 |
| 3.8.1 AI builders | 9 |
| 3.8.2 Visual/low-code | 11 |
| 3.8.3 Code generators | 4 |
| 3.8.4 Screenshot/design-to-code | 9 |
| 3.8.5 CRUD/admin generators | 5 |
| 3.8.6 Boilerplates/templates | 17 |
| 3.8.7 Landing/e-commerce builders | 5 |
| 3.9.1 System design guides | 11 |
| 3.9.2 Patterns | 4 |
| 3.9.3 ADRs | 4 |
| 3.9.4 Arch modeling | 2 |
| 3.9.5 Dependency tooling | 3 |

## Limitations

1. **Depth vs breadth trade-off:** ~30 searches + 3 primary opens across ~240 resources. Most records rest on search corroboration, not primary-source inspection. A follow-up pass opening official docs/repos would raise confidence, especially for licenses, pricing status, and acquisition details.
2. **Fast-moving targets:** license changes (Cal.com Apr 2026), acquisitions (Stytch/Twilio, Lemon Squeezy/Stripe, Payload/Figma, Neon/Databricks), and EOLs (MongoDB App Services) were captured from secondary reports; primary announcements were not all opened.
3. **Table-row records are thinner** than full records by design (identity, type, one-line capabilities, source, verification label) — acceptable for long-tail coverage, but a stricter pass could expand high-traffic items (Stripe, Clerk, Prisma, Kafka).
4. **No live availability checks:** hosted-service pricing/tiers are described as observed in search, not verified live.
5. **URL grounding:** official URLs use only verbatim URLs from tool results; many records honestly state "Not verified in this session" rather than risk a guessed URL.

## More work warranted?

- **Yes, targeted:** (a) open primary sources for the 5 Corrected items to upgrade to Verified; (b) resolve §3.5.9.3–3.5.9.7 (OpenAPI→MCP long tail) and §3.5.9.6 (anythingmcp); (c) open primary sources for Encore MCP server, MongoDB official MCP server, and Convex agent-skills repos (flagged in session notes); (d) verify licenses per-project (many marked "not re-verified"); (e) the Astryx-backend gap (§3.6.11) deserves a dedicated deep search before being declared closed.

---
*Catalog written by workstream researcher #3 · 2026-10-10 · read-only research; no installs/builds executed.*
