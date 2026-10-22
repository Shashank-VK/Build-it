# 03 — Backend (Langs/Frameworks · REST/GraphQL/RPC · Gateways/OpenAPI/Auth/Serverless/Queues)

> Part 3 · B-category catalog · Core-Tech researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved

## Index (26 resources)

Runtimes: Node.js · Deno · Bun (see 01-core for detail; reused here as server runtimes)
Frameworks: Express · Fastify · NestJS · Hono · Django + DRF · FastAPI · Flask · Spring Boot · ASP.NET Core · Laravel · Rails · Phoenix · Gin
API styles: REST (Richardson) · GraphQL + Apollo · tRPC · gRPC
Contract/Gateway: OpenAPI + Swagger · Postman (reference) · Kong
Auth: Auth.js · Clerk · Keycloak
Serverless/Jobs/Queues: Serverless Framework · BullMQ (Redis) · RabbitMQ · Kafka · NATS

---

### 01 — Node.js (server runtime)
- **Canonical identity:** `runtime:nodejs` — OpenJS Foundation
- **Category:** Backend → Runtime
- **Type:** OSS runtime
- **Official URL:** https://nodejs.org/
- **Description:** Event-driven V8 runtime; most-used web tech 48.7% (SO 2025); LTS governance.
- **Contents inspected:** nodejs.org download/docs; SO 2025 chart excerpt (search-verified: Node 48.7%, Express 19.9%).
- **Capabilities:** HTTP/Undici, workers, streams, test runner, permissions (experimental).
- **Usage domain:** REST/GraphQL/realtime/SSR/edge functions.
- **Integration:** native (Docker `node:`, fnm/volta; Vercel/AWS Lambda adapters)
- **Compatibility:** LTS 20/22; ESM+CJS.
- **Deps:** None.
- **Availability:** Free.
- **Maintenance:** Active LTS.
- **License:** MIT.
- **Security/limits:** Prototype pollution via sloppy merges; keep LTS + npm audit; CPU-bound → worker threads/queue.
- **Related:** Express, NestJS, Deno, Bun.
- **Sources:** nodejs.org; SO Survey 2025.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 02 — Express.js (5.x)
- **Canonical identity:** `npm:express` — `github:expressjs/express`
- **Category:** Backend → Minimal web framework
- **Type:** OSS (OpenJS)
- **Official URL:** https://expressjs.com/
- **Description:** Unopinionated middleware routing; Express 5 stable (2024) — promise support, stricter routing.
- **Contents inspected:** expressjs.com guide/API/migration v5 notes.
- **Capabilities:** Routing, middleware, error handling, template adapters.
- **Usage domain:** Micro-APIs, prototypes, gateways, SSR servers.
- **Integration:** official (`express` + `@types/express`; NestJS can sit atop Express/Fastify)
- **Compatibility:** Node 18+.
- **Deps:** `body-parser` merged concepts, `router`, `qs`.
- **Availability:** npm.
- **Maintenance:** Active (5.x line; 19.9% SO usage).
- **License:** MIT.
- **Security/limits:** Manual helmet/cors/rate-limit needed (`helmet`, `express-rate-limit`); no built-in validation.
- **Related:** Fastify, Koa, Hono.
- **Sources:** expressjs.com; resourcifi/index.dev 2026 roundups.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 03 — Fastify (v5)
- **Canonical identity:** `npm:fastify` — `github:fastify/fastify`
- **Category:** Backend → High-perf framework
- **Type:** OSS (OpenJS)
- **Official URL:** https://fastify.dev/
- **Description:** Schema-driven (AJV), plugin encapsulation, 2–4K RPS class; NestJS-compatible adapter.
- **Contents inspected:** fastify.dev docs (routes/validation/plugins/benchmarks).
- **Capabilities:** JSON-schema validation/serialization, hooks, TS-first.
- **Usage domain:** Throughput APIs, gateways, BFFs.
- **Integration:** official (`@fastify/*`: cors, jwt, swagger; `@nestjs/platform-fastify`)
- **Compatibility:** Node 20+.
- **Deps:** `ajv`, `avvio`, `light-my-request`.
- **Availability:** npm.
- **Maintenance:** Active (v5 2024-2026).
- **License:** MIT.
- **Security/limits:** Schema everything; AJV options (`coerce/removeAdditional`) review.
- **Related:** Express, Hono, NestJS.
- **Sources:** fastify.dev.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 04 — NestJS (v10/v11)
- **Canonical identity:** `npm:@nestjs/core` — `github:nestjs/nest`
- **Category:** Backend → Structured Node framework
- **Type:** OSS (+ commercial support)
- **Official URL:** https://nestjs.com/ (docs: https://docs.nestjs.com/)
- **Description:** Angular-like DI/modules; Express/Fastify underlay; first-class OpenAPI/microservices/queues/GraphQL.
- **Contents inspected:** docs.nestjs.com (controllers/providers, microservices, GraphQL, websockets).
- **Capabilities:** Guards/interceptors/pipes, CQRS package, Bull/Redis, Prisma/TypeORM recipes.
- **Usage domain:** Team-scale APIs, enterprise Node, DDD layering.
- **Integration:** official adapters (`@nestjs/platform-fastify`, `@nestjs/graphql`, `@nestjs/bullmq`)
- **Compatibility:** Node 18/20+; TS 5+.
- **Deps:** `reflect-metadata`, `rxjs`.
- **Availability:** npm.
- **Maintenance:** Active (6.7% SO 2025; steady enterprise).
- **License:** MIT.
- **Security/limits:** DI mis-scoping (REQUEST scope leaks); guard ordering audits.
- **Related:** Spring Boot (spiritual analog), Fastify, tRPC.
- **Sources:** docs.nestjs.com; SO 2025.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 05 — Hono (v4, edge-first)
- **Canonical identity:** `npm:hono` — `github:honojs/hono`
- **Category:** Backend → Edge/standard-based framework
- **Type:** OSS
- **Official URL:** https://hono.dev/
- **Description:** Web-standards (`fetch` Request/Response) router running on Node/Bun/Deno/Cloudflare/Fastly; tiny, fast.
- **Contents inspected:** hono.dev docs (routing, middleware, adapters, RPC mode).
- **Capabilities:** JSX SSR, Zod validator, JWT, streaming SSE.
- **Usage domain:** Edge APIs, BFFs, multi-runtime codebases.
- **Integration:** official adapters (`hono/node-server`, `hono/cloudflare-workers`, `hono/bun`)
- **Compatibility:** Any WinterCG runtime.
- **Deps:** None.
- **Availability:** npm/jsr.
- **Maintenance:** Active (v4 2024-2026).
- **License:** MIT.
- **Security/limits:** Bring-your-own auth/rate-limit (hono-rate-limiter).
- **Related:** Elysia, Fastify, itty-router.
- **Sources:** hono.dev.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — Django (5.x/6.0) + Django REST Framework
- **Canonical identity:** `pypi:Django` + `pypi:djangorestframework` — DSF
- **Category:** Backend → Batteries-included framework
- **Type:** OSS (Django Software Foundation)
- **Official URLs:** https://www.djangoproject.com/ · https://www.django-rest-framework.org/
- **Description:** Admin/ORM/auth/forms/migrations; Django 6 adds `django.tasks` background abstraction; DRF for REST; async/ASGI maturing.
- **Contents inspected:** djangoproject.com docs (12.6% SO 2025); DRF tutorial; 2026 Django-vs-FastAPI production analyses (search-verified: `django.tasks`, ASGI RPS 800–1500 vs FastAPI 3–4.5K).
- **Capabilities:** ORM, migrations, admin, CBVs, Ninja/DRF serializers, channels/tasks.
- **Usage domain:** SaaS/e-commerce/content/data-driven products; fastest CRUD path.
- **Integration:** official (Gunicorn/Uvicorn/Daphne; `django-stubs`; DRF Spectacular for OpenAPI)
- **Compatibility:** Python 3.10–3.13; Postgres/MySQL/SQLite.
- **Deps:** `asgiref`, `sqlparse`, `tzdata`.
- **Availability:** PyPI.
- **Maintenance:** Active (LTS 4.2/5.x; 6.0 2026).
- **License:** BSD-3-Clause.
- **Security/limits:** Exemplary security releases; enforce `ALLOWED_HOSTS/CSRF_TRUSTED_ORIGINS`, `SECURE_*` flags; ORM injection safe if no `extra(raw)`.
- **Related:** FastAPI (companion microservice), Rails, Laravel.
- **Sources:** djangoproject.com; DEV/Medium 2026 comparisons.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 07 — FastAPI (0.1xx, Pydantic v2)
- **Canonical identity:** `pypi:fastapi` — `github:fastapi/fastapi`
- **Category:** Backend → Async API framework
- **Type:** OSS
- **Official URL:** https://fastapi.tiangolo.com/
- **Description:** ASGI + Pydantic v2 (Rust core); auto OpenAPI/Swagger+ReDoc; fastest-growing Python (14.8% SO 2025, +5pts YoY); rivals Node/Go on I/O.
- **Contents inspected:** fastapi.tiangolo.com tutorial (path ops, dependencies, WebSockets, background tasks); SO 2025 momentum table.
- **Capabilities:** DI dependencies, OAuth2/JWT helpers, streaming, Uvicorn/Gunicorn deploy.
- **Usage domain:** Microservices, ML-serving, realtime APIs, high-RPS gateways.
- **Integration:** official (Starlette/Pydantic; `fastapi-cli`; `fastapi-users`, `SQLModel`)
- **Compatibility:** Python 3.8+; ASGI servers.
- **Deps:** `starlette`, `pydantic>=2`.
- **Availability:** PyPI.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Async pitfalls (blocking calls in `async def`); dependency authz review; docs exposure (`/docs` disable in prod if needed).
- **Related:** Starlette, Django (hybrid pattern), Hono.
- **Sources:** fastapi.tiangolo.com; resourcifi/SO 2025.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — Flask (3.x)
- **Canonical identity:** `pypi:Flask` — Pallets
- **Category:** Backend → Microframework
- **Type:** OSS
- **Official URL:** https://flask.palletsprojects.com/
- **Description:** Minimal WSGI core + extensions (SQLAlchemy, Migrate, Login, RESTful); 14.4% SO 2025.
- **Contents inspected:** Pallets docs (quickstart, blueprints).
- **Capabilities:** Blueprints, Jinja, CLI.
- **Usage domain:** Small services, ML demos, teaching.
- **Integration:** official extensions (`Flask-SQLAlchemy`, `Flask-Migrate`)
- **Compatibility:** Python 3.9+; WSGI/ASGI (via asgiref).
- **Deps:** `Werkzeug`, `Jinja2`, `click`.
- **Availability:** PyPI.
- **Maintenance:** Active (3.x).
- **License:** BSD-3-Clause.
- **Security/limits:** Manual CSRF/CSP; escape Jinja unless `|safe` justified.
- **Related:** FastAPI (perf upgrade), Django (scale-up).
- **Sources:** Pallets docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — Spring Boot (3.x, Virtual Threads/Loom)
- **Canonical identity:** `mvn:org.springframework.boot:spring-boot` — Broadcom/VMware
- **Category:** Backend → Enterprise Java framework
- **Type:** OSS (+ commercial Tanzu)
- **Official URL:** https://spring.io/projects/spring-boot (docs: https://docs.spring.io/spring-boot/)
- **Description:** DI/auto-config, WebMVC/WebFlux, Data/Security/Batch; Java 21 Loom threads; top raw RPS tier with ASP.NET/Go.
- **Contents inspected:** spring.io docs index; 2026 roundups (14.7% SO; enterprise pick with ASP.NET).
- **Capabilities:** Profiles, Actuator observability, Test slices, GraalVM native.
- **Usage domain:** Banking/regulated/multi-team platforms.
- **Integration:** native (Maven/Gradle starters; Spring Cloud/Kafka; Docker/Buildpacks)
- **Compatibility:** Java 17/21; Boot 3.x.
- **Deps:** Spring Framework, Jackson, Tomcat/Netty.
- **Availability:** Maven Central.
- **Maintenance:** Active (OSS + commercial support).
- **License:** Apache-2.0.
- **Security/limits:** Spring Security config is the boundary — review method security + actuator exposure; cold-start/footprint vs Quarkus/Micronaut.
- **Related:** Quarkus, Micronaut, NestJS (Node analog).
- **Sources:** spring.io; 2026 backend guides.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — ASP.NET Core (8/9)
- **Canonical identity:** `nuget:Microsoft.AspNetCore.App` — Microsoft/.NET Foundation
- **Category:** Backend → Enterprise framework
- **Type:** OSS (+ commercial support)
- **Official URL:** https://dotnet.microsoft.com/apps/aspnet (docs: https://learn.microsoft.com/aspnet/core/)
- **Description:** Minimal APIs + MVC + Blazor; top throughput; Identity/EF Core/SignalR; 19.7% SO 2025.
- **Contents inspected:** learn.microsoft.com ASP.NET docs hub.
- **Capabilities:** Middleware, filters, gRPC, YARP gateway, AOT/native.
- **Usage domain:** Microsoft-ecosystem enterprise, high-RPS APIs.
- **Integration:** native (NuGet, Azure/container adapters)
- **Compatibility:** .NET 8 LTS / 9 STS.
- **Deps:** .NET runtime.
- **Availability:** dotnet SDK; GitHub dotnet/aspnetcore.
- **Maintenance:** Active LTS.
- **License:** MIT (framework).
- **Security/limits:** DataProtection key management; antiforgery on cookie handlers.
- **Related:** Spring Boot, YARP, SignalR (Socket.io analog).
- **Sources:** Microsoft Learn.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 11 — Laravel (11/12)
- **Canonical identity:** `packagist:laravel/framework` — Laravel Holdings
- **Category:** Backend → PHP framework
- **Type:** OSS (+ Forge/Vapor SaaS)
- **Official URL:** https://laravel.com/ (docs: https://laravel.com/docs/)
- **Description:** Eloquent, Blade, queues/horizon, Sanctum/Passport, Octane (RoadRunner/Swoole); 8.9% SO.
- **Contents inspected:** laravel.com docs (routing/eloquent/queues).
- **Capabilities:** Migrations/seeders, broadcasting, Scout search drivers.
- **Usage domain:** Artisan SMB SaaS, marketplaces, rapid MVPs.
- **Integration:** official (Forge/Envoyer/Vapor; Inertia.js for modern monoliths)
- **Compatibility:** PHP 8.2/8.3+.
- **Deps:** Symfony components, Composer.
- **Availability:** Packagist.
- **Maintenance:** Active (yearly majors).
- **License:** MIT.
- **Security/limits:** Mass-assignment guards (`$fillable`); signed URLs + throttle middleware.
- **Related:** Symfony, Rails, Django.
- **Sources:** laravel.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — Ruby on Rails (7.1/8)
- **Canonical identity:** `gem:rails` — `github:rails/rails`
- **Category:** Backend → Convention-over-configuration framework
- **Type:** OSS (37signals/Basecamp, DHH)
- **Official URL:** https://rubyonrails.org/ (guides: https://guides.rubyonrails.org/)
- **Description:** ActiveRecord/ActionCable/Hotwire; Rails 8 (Kamal deploy, Solid Queue/Cache/Cable); 5.9% SO but elite MVP velocity.
- **Contents inspected:** rubyonrails.org + guides TOC.
- **Capabilities:** Migrations, Turbo/Stimulus, Kamal Docker deploy.
- **Usage domain:** MVPs, SaaS, marketplaces.
- **Integration:** official (Kamal, Propshaft, Importmap)
- **Compatibility:** Ruby 3.2+.
- **Deps:** ActiveSupport et al.
- **Availability:** RubyGems.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Strong-params + CSP defaults; keep `rails-html-sanitizer` updated.
- **Related:** Django, Laravel, Hotwired (htmx analog).
- **Sources:** rubyonrails.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 13 — Phoenix (Elixir 1.1x)
- **Canonical identity:** `hex:phoenix` — `github:phoenixframework/phoenix`
- **Category:** Backend → Realtime BEAM framework
- **Type:** OSS
- **Official URL:** https://www.phoenixframework.org/ (docs: https://hexdocs.pm/phoenix/)
- **Description:** Channels/LiveView (server-rendered realtime without JS), Ecto, PubSub; best pick for realtime correctness.
- **Contents inspected:** phoenixframework.org guides.
- **Capabilities:** LiveView diffs, Presence, Oban jobs.
- **Usage domain:** Chat/collab/IoT, soft-realtime.
- **Integration:** official (Ecto adapters; Bandit/Cowboy; Fly.io presets)
- **Compatibility:** Elixir 1.15+; OTP 26+.
- **Deps:** `ecto`, `plug`, `cowlib`.
- **Availability:** Hex.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** LiveView assigns are server-trusted — authorize every event.
- **Related:** Oban, NATS, Socket.io (client counterpart).
- **Sources:** phoenixframework.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — Gin / Echo (Go)
- **Canonical identities:** `go:github.com/gin-gonic/gin` · `go:github.com/labstack/echo`
- **Category:** Backend → Go microframeworks
- **Type:** OSS
- **Official URLs:** https://gin-gonic.com/ · https://echo.labstack.com/
- **Description:** Minimal routers (5–7K RPS hello-world class); Go stdlib `net/http` + `slog/chi` often enough.
- **Contents inspected:** gin-gonic.com + echo docs (routing/middleware/bind).
- **Capabilities:** Binding/validation, groups, graceful shutdown.
- **Usage domain:** Sidecars, gateways, high-RPS simple services.
- **Integration:** official middleware (CORS/JWT/rate); OTEL
- **Compatibility:** Go 1.21+.
- **Deps:** Minimal.
- **Availability:** Go modules.
- **Maintenance:** Active (Gin 1.9/1.10; Echo v4).
- **License:** MIT.
- **Security/limits:** Manual timeouts/context; JSON decode limits.
- **Related:** Chi, Fiber, net/http stdlib.
- **Sources:** Official sites.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — REST (Richardson maturity) — practice reference
- **Canonical identity:** `practice:rest` (Roy Fielding dissertation + Richardson model)
- **Category:** Backend → Architectural style
- **Type:** Open practice (reference-only)
- **Official URL:** https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm (pragmatic: https://restfulapi.net/)
- **Description:** Resource/verb/status-code conventions; Level 2 (verbs+codes) is pragmatic default; HATEOAS rarely full.
- **Contents inspected:** Fielding Ch.5; restfulapi.net maturity guide.
- **Capabilities:** Cacheability, idempotency keys, pagination/filtering patterns.
- **Usage domain:** Default public APIs.
- **Integration:** reference-only (implemented by Express/FastAPI/etc.)
- **Compatibility:** HTTP/1.1–3.
- **Deps:** None.
- **Availability:** Free.
- **Maintenance:** Stable/historical.
- **License:** N/A.
- **Security/limits:** Method/authz matrix review; mass-assignment.
- **Related:** OpenAPI, JSON:API, gRPC.
- **Sources:** UCI dissertation; restfulapi.net.
- **Verification date:** 2026-10-09 · **Confidence:** Historical

### 16 — GraphQL + Apollo Server/Client
- **Canonical identities:** `spec:graphql-october2021` · `npm:@apollo/server` · `npm:@apollo/client`
- **Category:** Backend → Query language + runtime
- **Type:** Open spec (GraphQL Foundation) + OSS/commercial Apollo
- **Official URLs:** https://graphql.org/ · https://www.apollographql.com/docs/
- **Description:** Typed schema, single endpoint, deferred/streamed fragments; Apollo Router/federation for supergraphs.
- **Contents inspected:** graphql.org learn/best-practices; Apollo Server/Client docs.
- **Capabilities:** Codegen, DataLoader batching, subscriptions, persisted queries.
- **Usage domain:** Aggregated BFFs, mobile APIs, federated domains.
- **Integration:** official (`graphql-yoga`, `ApolloServerPlugin`, codegen `graphql-codegen`)
- **Compatibility:** Any language (reference `graphql-js`).
- **Deps:** `graphql`.
- **Availability:** npm/pip/gems.
- **Maintenance:** Active (GraphQL 2024-2025 drafts; Apollo 4.x/5).
- **License:** MIT (reference); Apollo Client MIT / Server MIT + Router source-available (Elastic-2.0 variant — check).
- **Security/limits:** Query-cost/complexity limits, depth caps, persisted queries, authz per-field.
- **Related:** tRPC, REST, Relay.
- **Sources:** graphql.org; Apollo docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 17 — tRPC (v10/v11)
- **Canonical identity:** `npm:@trpc/server` + `@trpc/client` — `github:trpc/trpc`
- **Category:** Backend → End-to-end typesafe RPC
- **Type:** OSS
- **Official URL:** https://trpc.io/ (docs: https://trpc.io/docs/)
- **Description:** TS procedures share types client↔server; Zod validators; React Query integration; no codegen.
- **Contents inspected:** trpc.io docs (routers, context, Next.js/App Router adapters).
- **Capabilities:** Batching, subscriptions (SSE/WS), middlewares.
- **Usage domain:** Full-stack TS monoliths (Next.js/TanStack Start).
- **Integration:** official adapters (`@trpc/next`, `@trpc/react-query`, Fastify fetch adapter)
- **Compatibility:** TS 5+; Node 18+.
- **Deps:** None heavy.
- **Availability:** npm.
- **Maintenance:** Active (v11 2024-2026).
- **License:** MIT.
- **Security/limits:** Procedure-level authz; input schemas mandatory; batch limits.
- **Related:** GraphQL (heavier alt), ts-rest, Hono RPC.
- **Sources:** trpc.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — gRPC (HTTP/2 + Protobuf)
- **Canonical identity:** `tool:grpc` — CNCF (`github:grpc/grpc`)
- **Category:** Backend → RPC framework
- **Type:** OSS (Google/CNCF)
- **Official URL:** https://grpc.io/ (docs: https://grpc.io/docs/)
- **Description:** IDL-first services, streaming, deadlines; grpc-gateway/Connect for REST/JSON bridge + OpenAPI.
- **Contents inspected:** grpc.io docs (concepts, languages, web).
- **Capabilities:** Unary/server/client/bidi streaming; interceptors; xDS.
- **Usage domain:** Service mesh internals, polyglot microservices.
- **Integration:** official stubs per language; `grpc-web`/Connect adapters for browsers
- **Compatibility:** HTTP/2 required (HTTP/3 in progress).
- **Deps:** `protobuf`.
- **Availability:** Multi-package (npm/pip/go/maven).
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security/limits:** mTLS + deadlines + message-size caps; reflection disable in prod.
- **Related:** ConnectRPC, Thrift, OpenAPI.
- **Sources:** grpc.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — OpenAPI (3.1/3.0) + Swagger Tooling
- **Canonical identity:** `spec:openapi-3.1` — OpenAPI Initiative (Linux Foundation)
- **Category:** Backend → API contract standard + tooling
- **Type:** Open standard + OSS tools
- **Official URLs:** https://www.openapis.org/ · https://swagger.io/ (editor/codegen: https://github.com/OAI/OpenAPI-Specification)
- **Description:** JSON-schema-based contracts; codegen, validators, portals; FastAPI/DRF/Nest emit it natively.
- **Contents inspected:** openapis.org spec repo + swagger.io tools overview.
- **Capabilities:** `openapi-generator`, Prism mocks, Spectral lint, Redoc/Scalar docs.
- **Usage domain:** Contract-first design, SDK generation.
- **Integration:** open-standard (emitters: `fastapi.openapi()`, `drf-spectacular`, `@nestjs/swagger`)
- **Compatibility:** 3.0 vs 3.1 (JSON Schema alignment) — tooling varies.
- **Deps:** None (YAML/JSON).
- **Availability:** Free.
- **Maintenance:** Active (Moonwalk 3.1/3.2 track 2024-2026).
- **License:** Apache-2.0.
- **Security/limits:** Contract ≠ enforcement — validate runtime; redact examples with secrets.
- **Related:** AsyncAPI, JSON Schema, Postman.
- **Sources:** openapis.org; swagger.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — Kong Gateway (OSS) — gateway exemplar
- **Canonical identity:** `tool:kong-gateway-oss` — `github:Kong/kong`
- **Category:** Backend → API gateway
- **Type:** OSS (+ Enterprise)
- **Official URL:** https://konghq.com/products/kong-gateway (docs: https://docs.konghq.com/gateway/)
- **Description:** Nginx/OpenResty-based ingress: routing, rate-limit, JWT/OIDC, transforms; decK/GitOps.
- **Contents inspected:** Kong Gateway docs (install, plugins, decK).
- **Capabilities:** 100+ plugins, vaults, AI gateway (2024-2026) for LLM proxying.
- **Usage domain:** Edge ingress for service fleets.
- **Integration:** official (Helm/Docker; ingress controller KIC)
- **Compatibility:** K8s/VM; Postgres/DB-less.
- **Deps:** OpenResty/Nginx, Postgres (optional).
- **Availability:** Docker `kong:`; source.
- **Maintenance:** Active (3.x).
- **License:** Apache-2.0 (OSS) / commercial (Enterprise).
- **Security/limits:** Admin API must be firewalled; plugin ordering audits.
- **Related:** Envoy, Traefik, APISIX, AWS API GW.
- **Sources:** docs.konghq.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 21 — Auth.js (NextAuth v5) — auth exemplar
- **Canonical identity:** `npm:next-auth` (v5 `auth`) / `npm:@auth/core` — `github:nextauthjs/next-auth`
- **Category:** Backend → Authentication framework
- **Type:** OSS
- **Official URL:** https://authjs.dev/
- **Description:** OAuth/OIDC/email/magic-link + adapters (Prisma/Drizzle); framework middlewares (Next/SvelteKit/Express).
- **Contents inspected:** authjs.dev guides/providers/adapters.
- **Capabilities:** JWT/database sessions, callbacks, events.
- **Usage domain:** SaaS login without building OAuth.
- **Integration:** official (`@auth/prisma-adapter`, `@auth/drizzle-adapter`)
- **Compatibility:** Node 18+; edge-compatible (jose).
- **Deps:** DB adapter optional.
- **Availability:** npm.
- **Maintenance:** Active (v5 Auth.js 2024-2026).
- **License:** ISC.
- **Security/limits:** `AUTH_SECRET` rotation; PKCE/OIDC `checks`; callback URL allowlist.
- **Related:** Clerk (SaaS), Keycloak (self-host IdP), Lucia (minimal alt).
- **Sources:** authjs.dev.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 22 — Clerk (SaaS auth) — managed alternative
- **Canonical identity:** `saas:clerk` — `npm:@clerk/nextjs`
- **Category:** Backend → Managed auth
- **Type:** Commercial SaaS (+ OSS SDKs)
- **Official URL:** https://clerk.com/ (docs: https://clerk.com/docs)
- **Description:** Drop-in sign-in/MFA/orgs/billing-gated routes; B2B SaaS default in Next.js templates.
- **Contents inspected:** clerk.com/docs quickstarts.
- **Capabilities:** `<SignIn/>`, webhooks, JWT templates for Hasura/Supabase.
- **Usage domain:** SaaS auth without IdP ops.
- **Integration:** official SDKs (Next, React, Expo, Chrome ext)
- **Compatibility:** Requires Clerk account; vendor lock-in tradeoff.
- **Deps:** Network dependency.
- **Availability:** SaaS (free tier + paid).
- **Maintenance:** Active.
- **License:** SDKs MIT/ISC; service ToS.
- **Security/limits:** Webhook signature verify; session claims short-lived; DPA/SOC2 review for regulated data.
- **Related:** Auth0, Supabase Auth, Keycloak.
- **Sources:** clerk.com/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 23 — Keycloak (self-host IdP)
- **Canonical identity:** `tool:keycloak` — `github:keycloak/keycloak` (CNCF-adjacent/Red Hat)
- **Category:** Backend → Identity provider
- **Type:** OSS (self-host)
- **Official URL:** https://www.keycloak.org/ (docs: https://www.keycloak.org/documentation)
- **Description:** OIDC/SAML/LDAP, realms, federation, admin console; Quarkus distro.
- **Contents inspected:** keycloak.org guides (getting started, authorization services).
- **Capabilities:** SSO, social brokers, fine-grained authz, user storage SPIs.
- **Usage domain:** Self-sovereign SSO for enterprise/regulated.
- **Integration:** official adapters (JS, Node, Spring, `keycloak-js`)
- **Compatibility:** Java 17+; Postgres/MySQL.
- **Deps:** Java, DB.
- **Availability:** Quay `keycloak/keycloak`; Operator.
- **Maintenance:** Active (24/25/26 2024-2026 quarterly).
- **License:** Apache-2.0.
- **Security/limits:** Harden admin console + brute-force detection; rotate realm keys; DB encryption.
- **Related:** Authentik, Zitadel, Ory.
- **Sources:** keycloak.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 24 — Serverless Framework (v3/v4)
- **Canonical identity:** `npm:serverless` — `github:serverless/serverless`
- **Category:** Backend → Serverless IaC/deploy
- **Type:** OSS (+ commercial Console)
- **Official URL:** https://www.serverless.com/ (docs: https://www.serverless.com/framework/docs)
- **Description:** `serverless.yml` functions/events/IAM for AWS (+ Azure/GCP/Knative); SST/CDK are IaC alternatives.
- **Contents inspected:** framework docs (providers, plugins registry).
- **Capabilities:** Packaging, stages, HTTP/API-GW events, Compose.
- **Usage domain:** Event APIs, cron, webhooks.
- **Integration:** official plugins (`serverless-offline`, `serverless-esbuild`)
- **Compatibility:** Node 18+; AWS-centric.
- **Deps:** Provider SDKs.
- **Availability:** npm.
- **Maintenance:** Active (v4 commercial pivot 2024 — license nuance: check current terms for v4).
- **License:** MIT (v3); v4 terms mixed — verify before pinning.
- **Security/limits:** Least-privilege `iamRoleStatements`; secrets via SSM/Secrets Manager, never env-plaintext in repo.
- **Related:** SST, SAM, Architect, OpenNext.
- **Sources:** serverless.com docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 25 — BullMQ + Redis (job queue exemplar)
- **Canonical identities:** `npm:bullmq` · `tool:redis` (BSD/SSPL nuance — see note)
- **Category:** Backend → Background jobs / broker
- **Type:** OSS library + OSS broker
- **Official URLs:** https://docs.bullmq.io/ · https://redis.io/
- **Description:** Redis-backed priority/delayed/repeatable jobs, flows, rate-limiters; NestJS `@nestjs/bullmq` wrapper; Django analog is `django.tasks`/Celery.
- **Contents inspected:** BullMQ guide (queues/workers/flows); redis.io docs.
- **Capabilities:** Concurrency, backoff, events, observability (Arena/Board).
- **Usage domain:** Email, webhooks fan-out, media pipelines.
- **Integration:** official (`bullmq`, `@nestjs/bullmq`; Redis Docker/official cloud)
- **Compatibility:** Redis 6.2+ (streams); Node 18+.
- **Deps:** `ioredis`.
- **Availability:** npm + redis.io downloads.
- **Maintenance:** Active (BullMQ 5.x 2024-2026).
- **License:** MIT (BullMQ); Redis: RSALv2/SSPLv1 + AGPLv3 (post-2024 relicense — self-host review; Valkey MIT fork exists).
- **Security/limits:** Redis AUTH + TLS; job-data PII minimization; idempotent handlers.
- **Related:** Celery, RabbitMQ, SQS.
- **Sources:** docs.bullmq.io; redis.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 26 — RabbitMQ + Apache Kafka + NATS (broker trio)
- **Canonical identities:** `tool:rabbitmq` · `tool:kafka` · `tool:nats`
- **Category:** Backend → Message brokers / streaming
- **Type:** OSS (self-host or managed)
- **Official URLs:** https://www.rabbitmq.com/ · https://kafka.apache.org/ · https://nats.io/
- **Description:** RabbitMQ (AMQP routing, quorum queues); Kafka (durable log, exactly-once, ksqlDB); NATS (lightweight JetStream, edge/mesh).
- **Contents inspected:** Official docs hubs (tutorials, ops guides).
- **Capabilities:** Exchanges/topics/partitions; DLQs; schema registry (Kafka); KV/ObjectStore (NATS).
- **Usage domain:** Order pipelines, event sourcing, fleet messaging.
- **Integration:** official clients (amqplib, kafkajs/librdkafka, nats.js/py/go)
- **Compatibility:** Erlang/JVM/Go servers; Docker/K8s operators.
- **Deps:** ZooKeeper-free (KRaft for Kafka); storage.
- **Availability:** Docker Hub images; managed (Confluent/CloudAMQP/Synadia).
- **Maintenance:** Active (RMQ 3.13/4.x; Kafka 3.7/4.0 KRaft; NATS 2.10/2.11).
- **License:** MPL-2.0 (RMQ) / Apache-2.0 (Kafka, NATS).
- **Security/limits:** mTLS/SASL, vhost/ACL scoping, quorum replication for HA.
- **Related:** SQS, Pulsar, Redpanda.
- **Sources:** Official docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

**Count: 26 resources** (meets 15–30 minimum). No install/execute performed.
