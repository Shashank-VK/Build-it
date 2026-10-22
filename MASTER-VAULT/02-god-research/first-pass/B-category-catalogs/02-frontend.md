# 02 — Frontend (UI Frameworks · Meta-Frameworks · SSG · Routing · State · Forms · Tables · Charts · Editors · Viz · Animation · 3D · Realtime)

> Part 3 · B-category catalog · Core-Tech researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved

## Index (28 resources)

UI runtimes: React · Vue · Svelte · SolidJS · Angular · Preact · Qwik · Lit
Meta/SSG: Next.js · Nuxt · SvelteKit · Astro · React Router (Remix) · Docusaurus
Routing/State/Data: TanStack Router · TanStack Query · Redux Toolkit · Zustand · Pinia
Forms/Tables/Charts: React Hook Form · TanStack Form · TanStack Table · AG Grid · ECharts · Recharts · D3.js
Editors/Animation/3D/Realtime: TipTap · Monaco · Three.js · Framer Motion · GSAP · Socket.io

---

### 01 — React (incl. React Compiler, RSC)
- **Canonical identity:** `npm:react` + `npm:react-dom` — `github:facebook/react`
- **Category:** Frontend → UI runtime
- **Type:** OSS library (Meta)
- **Official URL:** https://react.dev/
- **Description:** Component UI library; React 19 (Compiler stable, Server Components, Actions, `use()`); largest ecosystem/jobs pool.
- **Contents inspected:** Search-verified react.dev docs structure + 2026 comparisons (React 19.1/19.2, Compiler GA; 68M npm weekly DLs Jan-2026 per DEV survey; 44.7% SO 2025 usage).
- **Capabilities:** JSX, hooks, Suspense, RSC, streaming SSR, Compiler auto-memoization.
- **Usage domain:** SPAs, full-stack (Next.js), design systems, CMS integrations.
- **Integration:** native (Vite CRA successor `create-vite`, Next.js, Astro islands via `@astrojs/react`)
- **Compatibility:** Evergreen; RSC requires compatible meta-framework.
- **Deps:** `scheduler`; ecosystem (Router, Query).
- **Availability:** npm `react`; UMD/CDN.
- **Maintenance:** Active (19.x 2025-2026).
- **License:** MIT.
- **Security/limits:** XSS via `dangerouslySetInnerHTML`; RSC flight-data exposure — don't leak secrets in server components.
- **Related:** Next.js, React Router, TanStack Query, Zustand.
- **Sources:** WebFetch attempt react.dev (returned 404 on bare `/` in this session — SPA shell; identity confirmed via search + npm); DEV/InfoWorld 2025-2026 surveys.
- **Verification date:** 2026-10-09 · **Confidence:** Partially (site SPA blocked fetch; package identity undisputed)

### 02 — Vue.js (3.x + Vapor Mode preview)
- **Canonical identity:** `npm:vue` — `github:vuejs/core`
- **Category:** Frontend → UI runtime
- **Type:** OSS framework (Evan You / Vue team, Open Source Collective)
- **Official URL:** https://vuejs.org/
- **Description:** Progressive framework; SFCs, Composition API, `<script setup>`; Vue 3.5/3.6 + Vapor Mode (no-VDOM compilation) in 2026.
- **Contents inspected:** vuejs.org docs (guide, API, examples); 2026 framework-war coverage (Vapor Mode, 8.4M weekly DLs).
- **Capabilities:** Reactivity (`ref/reactive`), SFC compiler, Teleport/Suspense, SSR (`@vue/server-renderer`).
- **Usage domain:** Rapid delivery, SME apps, strong CN market, Nuxt full-stack.
- **Integration:** official (`create-vue`, Vite plugin `@vitejs/plugin-vue`, Nuxt, Astro `@astrojs/vue`)
- **Compatibility:** Evergreen; Vapor opt-in per component.
- **Deps:** `@vue/shared/reactivity` split packages.
- **Availability:** npm `vue`; CDN `vue.global.js`.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** `v-html` XSS; template injection if compiling untrusted templates client-side.
- **Related:** Nuxt, Pinia, Vue Router, Vite.
- **Sources:** vuejs.org; StateOfJS/SO surveys.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 03 — Svelte (5.x Runes)
- **Canonical identity:** `npm:svelte` — `github:sveltejs/svelte`
- **Category:** Frontend → Compiler-based UI runtime
- **Type:** OSS compiler + runtime (Svelte team / Vercel)
- **Official URL:** https://svelte.dev/
- **Description:** Compiles components to vanilla JS (~1.6–28KB); Svelte 5 Runes (`$state/$derived/$effect`); highest satisfaction (62–73% admired).
- **Contents inspected:** svelte.dev docs/blog (Runes, SvelteKit); 2026 comparisons (Lighthouse 96, ~28KB).
- **Capabilities:** No VDOM, scoped CSS, stores, SSR, custom elements output.
- **Usage domain:** Perf-critical dashboards, content + interactive hybrids.
- **Integration:** official (SvelteKit, `@astrojs/svelte`, Vite plugin)
- **Compatibility:** Evergreen; compiles to ES2018+.
- **Deps:** None at runtime (compiler dev-only).
- **Availability:** npm `svelte`.
- **Maintenance:** Active (5.x 2024-2026; SvelteKit 2/3).
- **License:** MIT.
- **Security/limits:** `{@html}` XSS; same hygiene as others.
- **Related:** SvelteKit, Astro, Vite.
- **Sources:** svelte.dev; solid-web.com 2026-03 guide.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 04 — SolidJS (2.0)
- **Canonical identity:** `npm:solid-js` — `github:solidjs/solid`
- **Category:** Frontend → Fine-grained reactive runtime
- **Type:** OSS library
- **Official URL:** https://www.solidjs.com/
- **Description:** JSX + signals, no VDOM, surgical DOM updates; benchmark leader (Lighthouse 98, 42.8 ops/s 1K-rows).
- **Contents inspected:** solidjs.com docs/tutorial; 2026 benchmark tables.
- **Capabilities:** Signals/effects/stores, SSR streaming, SolidStart.
- **Usage domain:** Max-perf SPAs, embedded widgets.
- **Integration:** official (SolidStart, `@astrojs/solid-js`, Vite plugin `vite-plugin-solid`)
- **Compatibility:** Evergreen.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active (2.0 2025-2026).
- **License:** MIT.
- **Security/limits:** `innerHTML` helpers need sanitizing.
- **Related:** Svelte, Qwik, SolidStart.
- **Sources:** solidjs.com; DEV 2026-03 benchmarks.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 05 — Angular (v20/v21, Signals)
- **Canonical identity:** `npm:@angular/core` — `github:angular/angular`
- **Category:** Frontend → Full framework
- **Type:** OSS platform (Google)
- **Official URL:** https://angular.dev/
- **Description:** Opinionated batteries-included (DI, router, forms, HttpClient); Signals + deferred loading + AI tooling in v20/v21.
- **Contents inspected:** angular.dev docs/tutorials; 2026 coverage (enterprise 12k+ jobs, bundle ~85KB).
- **Capabilities:** Standalone components, SSR/hydration, zoneless change detection.
- **Usage domain:** Enterprise suites, regulated/long-life apps.
- **Integration:** official (Angular CLI, Analog meta-framework, Astro community integration)
- **Compatibility:** Evergreen; Node LTS for CLI.
- **Deps:** RxJS, zone.js (optional zoneless).
- **Availability:** npm `@angular/*`.
- **Maintenance:** Active (6-month majors; LTS 18 months).
- **License:** MIT.
- **Security/limits:** Built-in sanitizer; bypass via `bypassSecurityTrust*` must be audited.
- **Related:** Analog, NgRx, RxJS.
- **Sources:** angular.dev; DEV 2026-01/03.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — Preact
- **Canonical identity:** `npm:preact` — `github:preactjs/preact`
- **Category:** Frontend → Lightweight React-compatible runtime
- **Type:** OSS library
- **Official URL:** https://preactjs.com/
- **Description:** 3KB React API subset; `preact/compat` alias; Islands-friendly.
- **Contents inspected:** preactjs.com guide/API; Astro `@astrojs/preact` docs.
- **Capabilities:** Hooks, Suspense, SSR (`preact-render-to-string`).
- **Usage domain:** Widgets, edge, perf-constrained bundles.
- **Integration:** official compat alias; Vite/Astro/Next (via alias) adapter
- **Compatibility:** React API ~parity for common subset.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active (10.x/11.x).
- **License:** MIT.
- **Security/limits:** Same XSS hygiene.
- **Related:** React, Astro islands, Vite.
- **Sources:** preactjs.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 07 — Qwik (2.x, resumability)
- **Canonical identity:** `npm:@builder.io/qwik` — `github:QwikDev/qwik`
- **Category:** Frontend → Resumable runtime
- **Type:** OSS framework (Builder.io)
- **Official URL:** https://qwik.dev/
- **Description:** Zero-hydration resumability; `component$`/`useSignal`; Qwik City meta-framework.
- **Contents inspected:** qwik.dev docs (resumability, optimizer).
- **Capabilities:** Lazy execution, SSR-first, Qwik City routing.
- **Usage domain:** E-commerce/media with instant interactivity.
- **Integration:** official (Qwik City; Vite plugin)
- **Compatibility:** Evergreen.
- **Deps:** Optimizer (Rust).
- **Availability:** npm.
- **Maintenance:** Active (2.x 2025-2026).
- **License:** MIT.
- **Security/limits:** Serialization boundaries — validate resumable state.
- **Related:** SolidJS, Astro, Partytown.
- **Sources:** qwik.dev.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — Lit (Web Components rendering)
- **Canonical identity:** `npm:lit` — `github:lit/lit`
- **Category:** Frontend → Web Components library
- **Type:** OSS (Google)
- **Official URL:** https://lit.dev/
- **Description:** Minimal reactive base for custom elements; SSR (`@lit-labs/ssr`).
- **Contents inspected:** lit.dev docs/playground.
- **Capabilities:** Templates, reactivity, scoped styles, IDE plugin.
- **Usage domain:** Design systems shared across frameworks.
- **Integration:** official (`@lit/react` wrappers; Astro/Vite native CE support)
- **Compatibility:** Baseline custom elements.
- **Deps:** None.
- **Availability:** npm/CDN.
- **Maintenance:** Active (3.x).
- **License:** BSD-3-Clause.
- **Security/limits:** Sanitize HTML templates with user data.
- **Related:** Shoelace, FAST, Stencil.
- **Sources:** lit.dev.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — Next.js (16.x, App Router, Turbopack, PPR)
- **Canonical identity:** `npm:next` — `github:vercel/next.js`
- **Category:** Frontend → React meta-framework (full-stack)
- **Type:** OSS framework (Vercel)
- **Official URL:** https://nextjs.org/
- **Description:** File routing, RSC, Server Actions, SSG/SSR/ISR/PPR; Turbopack default in v16; largest share (~6M weekly DLs, ~130K stars).
- **Contents inspected:** WebFetch nextjs.org 2026-10-09 (v16.4.0 banner, App/Pages Router split, `npx create-next-app`, llms.txt catalog, governance/telemetry links).
- **Capabilities:** Cache Components/PPR, streaming, middleware, image/font optimization, Vercel/Node adapters.
- **Usage domain:** SaaS, e-commerce, enterprise full-stack React.
- **Integration:** native (Vercel; `next start`; Docker; open-next for AWS)
- **Compatibility:** Node 18.18+; React 19.
- **Deps:** React, React-DOM, SWC/Turbopack.
- **Availability:** npm `next`; MIT.
- **Maintenance:** Active (15→16 Oct 2025; 16.x 2026).
- **License:** MIT.
- **Security/limits:** Cache-poisoning/misconfigured `fetch` caching; Server Action authz must be explicit; keep `next` patched (RSC CVEs 2024-2025 history).
- **Related:** React, Vercel, React Router, Astro (alternative for content).
- **Sources:** WebFetch nextjs.org; PkgPulse/DEV 2026 guides.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 10 — Nuxt (3.x, Nitro)
- **Canonical identity:** `npm:nuxt` — `github:nuxt/nuxt`
- **Category:** Frontend → Vue meta-framework
- **Type:** OSS framework (Nuxt team)
- **Official URL:** https://nuxt.com/
- **Description:** File routing, auto-imports, server engine Nitro (edge presets), layers for multi-site reuse, Nuxt UI.
- **Contents inspected:** nuxt.com docs (guide, Nitro, layers); Nunuqs 2026 audit note (50% faster multi-brand delivery vs porting to Next).
- **Capabilities:** SSR/SSG/ISR/hybrid, server routes, modules ecosystem.
- **Usage domain:** Vue SaaS, e-commerce groups, content + app hybrids.
- **Integration:** native (Nitro presets: Node/Vercel/Netlify/Cloudflare)
- **Compatibility:** Vue 3; Vite + Rollup.
- **Deps:** Vue, Vite, Nitro (h3).
- **Availability:** npm `nuxt`.
- **Maintenance:** Active (3.x; 4 compat in progress 2026).
- **License:** MIT.
- **Security/limits:** `useAsyncData` key/auth hygiene; Nitro route rules review.
- **Related:** Vue, Nitro/h3, Nuxt UI, Astro.
- **Sources:** nuxt.com; 2026 meta-framework comparisons.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 11 — SvelteKit (2.x)
- **Canonical identity:** `npm:@sveltejs/kit` — `github:sveltejs/kit`
- **Category:** Frontend → Svelte meta-framework
- **Type:** OSS framework
- **Official URL:** https://kit.svelte.dev/
- **Description:** File routes, load/actions, form actions, adapters; most-loved in StateOfJS 2024; lean bundles (15-30KB).
- **Contents inspected:** kit.svelte.dev docs (routing, adapters).
- **Capabilities:** SSR/SSG/CSR per-route, streaming, edge adapters.
- **Usage domain:** Interactive dashboards, SaaS with minimal JS.
- **Integration:** native (adapters: node/vercel/netlify/cloudflare)
- **Compatibility:** Svelte 5; Vite.
- **Deps:** Svelte, Vite.
- **Availability:** npm.
- **Maintenance:** Active (2.x).
- **License:** MIT.
- **Security/limits:** Form-action CSRF protection built-in — don't disable origin check blindly.
- **Related:** Svelte, Astro, Next.js.
- **Sources:** kit.svelte.dev; PkgPulse 2026-03.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — Astro (5.x, Islands + Content Layer)
- **Canonical identity:** `npm:astro` — `github:withastro/astro`
- **Category:** Frontend → Content-first meta-framework / SSG
- **Type:** OSS framework (Astro Technology Co.; joined Cloudflare Jan-2026 per 2026 reports)
- **Official URL:** https://astro.build/ (docs: https://docs.astro.build/)
- **Description:** Zero-JS default, Islands (`client:*`), Content Layer, server islands/actions; mixes React/Vue/Svelte/Solid.
- **Contents inspected:** docs.astro.build framework-components + migrate-from-Nuxt pages (search-verified: official integrations list, islands directives).
- **Capabilities:** SSG/SSR/hybrid, MDX, image optimization, Cloudflare edge integration (2026).
- **Usage domain:** Docs, blogs, marketing, SEO-first sites.
- **Integration:** official integrations (`@astrojs/react/vue/svelte/solid/mdx/tailwind`)
- **Compatibility:** Any Node 18+; bring-your-framework.
- **Deps:** Vite under the hood.
- **Availability:** npm `astro`.
- **Maintenance:** Active (5.x late-2024 → 6 beta 2026).
- **License:** MIT.
- **Security/limits:** `set:html` needs sanitizing; server endpoints need auth.
- **Related:** Starlight, SvelteKit, Next.js (heavier alternative).
- **Sources:** docs.astro.build excerpts (search session); DEV/PkgPulse 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 13 — React Router (v7, ex-Remix)
- **Canonical identity:** `npm:react-router` — `github:remix-run/react-router` (Remix → RR v7 merge)
- **Category:** Frontend → Routing + full-stack framework
- **Type:** OSS (Shopify/Remix team)
- **Official URL:** https://reactrouter.com/
- **Description:** Web-standards routing (loaders/actions/fetchers); Remix merged into RR v7 (2024-2025); Remix v3 "bundler-free" reimagined 2026.
- **Contents inspected:** reactrouter.com docs (framework/data modes); DEV 2026-02 decision guide excerpt.
- **Capabilities:** Nested routes, SSR/streaming, middleware, RSC-friendly.
- **Usage domain:** React SPAs + full-stack (Vite plugin / Hydrogen).
- **Integration:** official (`@react-router/node/express/serve`, Vite plugin)
- **Compatibility:** React 18/19; Node 18+.
- **Deps:** None heavy.
- **Availability:** npm.
- **Maintenance:** Active (v7 2025-2026).
- **License:** MIT.
- **Security/limits:** Loader/action authz per-route; CSRF on cookie actions.
- **Related:** Next.js, TanStack Router, Remix history.
- **Sources:** reactrouter.com; DEV 2026-02.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — Docusaurus
- **Canonical identity:** `npm:@docusaurus/core` — `github:facebook/docusaurus`
- **Category:** Frontend → Docs SSG
- **Type:** OSS (Meta)
- **Official URL:** https://docusaurus.io/
- **Description:** React/MDX docs sites; versioning, i18n, search (Algolia), blog.
- **Contents inspected:** docusaurus.io docs (getting started, deployment).
- **Capabilities:** MDX, swizzling, plugins (content-docs/blog/pages).
- **Usage domain:** OSS docs, internal knowledge bases.
- **Integration:** official (Vercel/Netlify/GitHub Pages presets; `docusaurus deploy`)
- **Compatibility:** Node 18+.
- **Deps:** React, MDX.
- **Availability:** npm.
- **Maintenance:** Active (3.x).
- **License:** MIT.
- **Security/limits:** Static output — low risk; sanitize MDX components.
- **Related:** Starlight, VitePress, Nextra.
- **Sources:** docusaurus.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — TanStack Router + Start
- **Canonical identity:** `npm:@tanstack/react-router` + `npm:@tanstack/start` — `github:TanStack/router`
- **Category:** Frontend → Type-safe routing / meta-framework
- **Type:** OSS (TanStack)
- **Official URL:** https://tanstack.com/router
- **Description:** Fully type-safe routes, search-param state, loaders; Start adds SSR/streaming/file routes.
- **Contents inspected:** tanstack.com/router docs; shadcn TanStack install guides referencing `createFileRoute`.
- **Capabilities:** Code-based + file routes, preloading, SSR.
- **Usage domain:** Type-safe SPAs/full-stack React.
- **Integration:** official (Vite plugin, Start Nitro-like server)
- **Compatibility:** React 18/19; Vite.
- **Deps:** None heavy.
- **Availability:** npm.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Loader data exposure — shape payloads minimally.
- **Related:** React Router, Next.js, TanStack Query.
- **Sources:** tanstack.com; ui.shadcn.com TanStack guides.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — TanStack Query (v5)
- **Canonical identity:** `npm:@tanstack/react-query` — `github:TanStack/query`
- **Category:** Frontend → Server-state manager
- **Type:** OSS
- **Official URL:** https://tanstack.com/query/latest
- **Description:** Cache + lifecycle for async data (dedup, retries, bg refetch, GC); 2.7B DLs / 50K stars per homepage.
- **Contents inspected:** WebSearch excerpt of tanstack.com/query (cache lifecycle, mutations, devtools) — verified live copy.
- **Capabilities:** `useQuery/useMutation`, infinite, offline, framework adapters (React/Vue/Solid/Svelte/Angular).
- **Usage domain:** All data-heavy frontends.
- **Integration:** official adapters; devtools
- **Compatibility:** All major frameworks.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active (v5).
- **License:** MIT.
- **Security/limits:** Cache holds sensitive data — scope keys, clear on logout.
- **Related:** SWR, RTK Query, Zustand (client state split).
- **Sources:** WebSearch homepage excerpt.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 17 — Redux Toolkit (RTK + RTK Query)
- **Canonical identity:** `npm:@reduxjs/toolkit` — `github:reduxjs/redux-toolkit`
- **Category:** Frontend → Predictable state + data
- **Type:** OSS
- **Official URL:** https://redux-toolkit.js.org/
- **Description:** Official Redux: slices, `configureStore`, RTK Query codegen; still dominant in large React codebases.
- **Contents inspected:** redux-toolkit.js.org tutorials/RTK Query docs.
- **Capabilities:** Immer reducers, thunks/listeners, normalized caching.
- **Usage domain:** Large long-lived React/enterprise apps.
- **Integration:** official (`react-redux`, Next.js provider patterns)
- **Compatibility:** React 18/19.
- **Deps:** `immer`, `reselect`.
- **Availability:** npm.
- **Maintenance:** Active (2.x).
- **License:** MIT.
- **Security/limits:** Never store tokens unencrypted in persisted stores without care.
- **Related:** Zustand, Jotai, TanStack Query.
- **Sources:** redux-toolkit.js.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — Zustand
- **Canonical identity:** `npm:zustand` — `github:pmndrs/zustand`
- **Category:** Frontend → Minimal client-state store
- **Type:** OSS (Poimandres)
- **Official URL:** https://zustand.docs.pmnd.rs/ (repo: https://github.com/pmndrs/zustand)
- **Description:** Tiny hook-based store (no boilerplate); persist/middleware slices; default pick in 2026 Next.js guides.
- **Contents inspected:** Zustand docs (getting started, persist middleware).
- **Capabilities:** Transient updates, subscribeWithSelector, immer.
- **Usage domain:** SPA client state alongside Query.
- **Integration:** official (React; vanilla `zustand/vanilla`)
- **Compatibility:** React 18/19.
- **Deps:** None (optional immer).
- **Availability:** npm.
- **Maintenance:** Active (5.x).
- **License:** MIT.
- **Security/limits:** Persisted storage review (localStorage exposure).
- **Related:** Jotai, Valtio, Redux.
- **Sources:** zustand docs; solid-web 2026 table (Zustand/Jotai/Redux listed).
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — Pinia (Vue store)
- **Canonical identity:** `npm:pinia` — `github:vuejs/pinia`
- **Category:** Frontend → Vue state manager
- **Type:** OSS (official Vue)
- **Official URL:** https://pinia.vuejs.org/
- **Description:** Official Vue 3 store (Composition API, SSR-safe, devtools); replaces Vuex.
- **Contents inspected:** pinia.vuejs.org guide/SSR docs.
- **Capabilities:** Setup stores, plugins, persistedstate via plugin.
- **Usage domain:** All Vue/Nuxt apps.
- **Integration:** native (Nuxt module `@pinia/nuxt`)
- **Compatibility:** Vue 3.
- **Deps:** `vue-demi` legacy only.
- **Availability:** npm.
- **Maintenance:** Active (2.x/3.x).
- **License:** MIT.
- **Security/limits:** Same persist hygiene.
- **Related:** Vuex (legacy), Zustand, Nuxt.
- **Sources:** pinia.vuejs.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — React Hook Form + Zod resolvers
- **Canonical identity:** `npm:react-hook-form` — `github:react-hook-form/react-hook-form`
- **Category:** Frontend → Forms
- **Type:** OSS
- **Official URL:** https://react-hook-form.com/
- **Description:** Performant uncontrolled forms + validation resolvers (Zod/Yup); minimal re-renders.
- **Contents inspected:** react-hook-form.com docs/API/get-started.
- **Capabilities:** `useForm/register/Controller`, DevTools, `ajv/zod` resolvers.
- **Usage domain:** All React forms (paired with shadcn/ui).
- **Integration:** official resolvers (`@hookform/resolvers`); shadcn form pattern
- **Compatibility:** React 18/19.
- **Deps:** None core.
- **Availability:** npm.
- **Maintenance:** Active (7.x).
- **License:** MIT.
- **Security/limits:** Client validation is UX only — always validate server-side (Zod/shared schema).
- **Related:** TanStack Form, Formik (legacy).
- **Sources:** react-hook-form.com; ui.shadcn.com forms section.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 21 — TanStack Form + TanStack Table
- **Canonical identity:** `npm:@tanstack/react-form` + `npm:@tanstack/react-table` — `github:TanStack/form|table`
- **Category:** Frontend → Forms + headless tables
- **Type:** OSS
- **Official URLs:** https://tanstack.com/form · https://tanstack.com/table
- **Description:** Headless, framework-agnostic form state and datagrid core (sorting/filtering/pagination/virtualization); UI-agnostic.
- **Contents inspected:** tanstack.com/form+table docs (adapters for React/Vue/Solid/Angular).
- **Capabilities:** Validators (Zod), field arrays; table column defs, row selection/expansion.
- **Usage domain:** Admin panels, data grids.
- **Integration:** official adapters; pairs with shadcn Table/AG Grid UI
- **Compatibility:** All frameworks.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active (v8 table; form v0/v1 2024-2026).
- **License:** MIT.
- **Security/limits:** Large client datasets — paginate server-side; sanitize cell HTML.
- **Related:** AG Grid, React Hook Form.
- **Sources:** tanstack.com/form|table.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 22 — AG Grid (Community/Enterprise)
- **Canonical identity:** `npm:ag-grid-react` (+ `-vue3`, `-angular`) — AG Grid Ltd
- **Category:** Frontend → Enterprise datagrid
- **Type:** Commercial OSS (dual)
- **Official URL:** https://www.ag-grid.com/
- **Description:** Full datagrid (grouping/pivoting, server-side row model, Excel export, charts integration).
- **Contents inspected:** ag-grid.com React/Vue/Angular grid docs.
- **Capabilities:** 100+ features; SSRM, clipboard, theming.
- **Usage domain:** Finance/ops/admin heavy tables.
- **Integration:** official framework components
- **Compatibility:** React/Vue/Angular/TS.
- **Deps:** Framework peer.
- **Availability:** npm (Community MIT; Enterprise license).
- **Maintenance:** Active (v31/32 2024-2026 cadence).
- **License:** MIT (Community) / Commercial (Enterprise).
- **Security/limits:** Enterprise key management; cell-renderer XSS review.
- **Related:** TanStack Table, MUI DataGrid.
- **Sources:** ag-grid.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 23 — ECharts + Recharts + D3.js (chart/viz trio)
- **Canonical identities:** `npm:echarts` (Apache) · `npm:recharts` · `npm:d3`
- **Category:** Frontend → Charts / visualization
- **Type:** OSS libraries
- **Official URLs:** https://echarts.apache.org/ · https://recharts.org/ · https://d3js.org/
- **Description:** ECharts (canvas/SVG, big-data, geo); Recharts (React/ComposedChart wrappers); D3 (low-level data→DOM).
- **Contents inspected:** echarts examples/handbook; recharts API; d3 gallery (search-verified).
- **Capabilities:** Line/bar/geo/graph/3D (echarts-gl), responsive containers, a11y plugins.
- **Usage domain:** Dashboards, analytics, Layer Cake alternative (Svelte).
- **Integration:** official React wrappers (`echarts-for-react`, `recharts` native); Svelte/Vue adapters community
- **Compatibility:** Evergreen + SSR guards (dynamic import).
- **Deps:** None heavy (d3 modular).
- **Availability:** npm/CDN.
- **Maintenance:** Active (ECharts 5.x/6 2026; D3 7.x).
- **License:** Apache-2.0 (ECharts), MIT (Recharts/D3 ISC).
- **Security/limits:** Never inject untrusted SVG/HTML into tooltips without sanitizing.
- **Related:** Chart.js, Victory, Nivo, Visx.
- **Sources:** Official sites (search-verified).
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 24 — TipTap + Monaco + CodeMirror (editors)
- **Canonical identities:** `npm:@tiptap/react` · `npm:monaco-editor` · `npm:@codemirror/*`
- **Category:** Frontend → Editors
- **Type:** OSS
- **Official URLs:** https://tiptap.dev/ · https://microsoft.github.io/monaco-editor/ · https://codemirror.net/
- **Description:** TipTap (ProseMirror headless rich-text, collab via Yjs); Monaco (VS Code engine); CodeMirror 6 (modular code editor).
- **Contents inspected:** tiptap.dev guides; monaco docs; CM6 system guide.
- **Capabilities:** Marks/extensions, CRDT collab, syntax themes, diffs.
- **Usage domain:** CMS, docs, notebooks, admin rich-text, code playgrounds.
- **Integration:** official React/Vue/Svelte wrappers
- **Compatibility:** Evergreen; SSR dynamic-only.
- **Deps:** ProseMirror (TipTap); none (CM6).
- **Availability:** npm (TipTap Cloud optional SaaS).
- **Maintenance:** Active (TipTap v2/v3; CM 6.x).
- **License:** MIT (core; Pro collaboration extensions commercial).
- **Security/limits:** Paste/HTML sanitization + stored-XSS review; collab auth.
- **Related:** Slate, Lexical, ProseMirror.
- **Sources:** Official docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 25 — Three.js (WebGL/WebGPU 3D)
- **Canonical identity:** `npm:three` — `github:mrdoob/three.js`
- **Category:** Frontend → 3D
- **Type:** OSS library
- **Official URL:** https://threejs.org/ (docs: https://threejs.org/docs/ ; manual: https://threejs.org/manual/)
- **Description:** Scene graph, geometries, materials, loaders (glTF), postprocessing; WebGPU renderer path + R3F wrapper.
- **Contents inspected:** threejs.org docs/manual/examples index.
- **Capabilities:** PBR, shadows, instancing, XR, `react-three-fiber`/`drei`.
- **Usage domain:** Configurators, maps, viz, games.
- **Integration:** official examples/jsm; R3F adapter
- **Compatibility:** WebGL2 baseline; WebGPU opt-in.
- **Deps:** None.
- **Availability:** npm/CDN (unpkg/jsdelivr), MIT.
- **Maintenance:** Active (monthly r1xx releases).
- **License:** MIT.
- **Security/limits:** glTF/texture parsing of untrusted assets — validate; GPU perf budgets.
- **Related:** Babylon.js, PlayCanvas, R3F.
- **Sources:** threejs.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 26 — Framer Motion (Motion) + GSAP
- **Canonical identities:** `npm:motion`/`framer-motion` · `npm:gsap`
- **Category:** Frontend → Animation
- **Type:** OSS (+ commercialextensions GSAP Club)
- **Official URLs:** https://motion.dev/ · https://gsap.com/
- **Description:** Motion (React declarative gestures/layout); GSAP (timeline, ScrollTrigger, framework-agnostic).
- **Contents inspected:** motion.dev docs; gsap.com docs/demos.
- **Capabilities:** Springs, drag, exit, scroll-linked, SVG morph.
- **Usage domain:** Marketing, onboarding, micro-interactions.
- **Integration:** official React/Vue/vanilla APIs
- **Compatibility:** Evergreen; SSR-safe (`useInView` guards).
- **Deps:** None.
- **Availability:** npm (Motion MIT; GSAP Standard MIT, Club commercial).
- **Maintenance:** Active.
- **License:** MIT (core).
- **Security/limits:** `prefers-reduced-motion` respect; perf budgets.
- **Related:** Auto-Animate, Lottie.
- **Sources:** Official sites.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 27 — Socket.io (realtime transport)
- **Canonical identity:** `npm:socket.io` (+ `socket.io-client`) — `github:socketio/socket.io`
- **Category:** Frontend → Realtime (paired with backend)
- **Type:** OSS
- **Official URL:** https://socket.io/
- **Description:** Event-based WebSocket (+polling fallback), rooms/namespaces, adapters (Redis), admin UI.
- **Contents inspected:** socket.io docs (server/client API, adapters).
- **Capabilities:** Acks, binary, multiplexing, scaling via `@socket.io/redis-adapter`.
- **Usage domain:** Chat, presence, live dashboards, collab signaling.
- **Integration:** official client/server; NestJS gateway adapter
- **Compatibility:** All browsers; Node 18+ server.
- **Deps:** `engine.io`, `ws`.
- **Availability:** npm.
- **Maintenance:** Active (4.x).
- **License:** MIT.
- **Security/limits:** Auth handshake + origin check; rate-limit events; Redis adapter TLS.
- **Related:** ws, Liveblocks, PartyKit, Ably/Pusher (SaaS alt).
- **Sources:** socket.io docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 28 — htmx + Alpine.js (HTML-first interactivity)
- **Canonical identities:** `github:bigskysoftware/htmx` · `npm:alpinejs`
- **Category:** Frontend → Hypermedia / micro-interactivity
- **Type:** OSS libraries
- **Official URLs:** https://htmx.org/ · https://alpinejs.dev/
- **Description:** htmx (AJAX via attributes, 47K stars 2026, anti-JS-movement rep); Alpine (declarative `x-data` sprinkles).
- **Contents inspected:** htmx.org docs/essays; alpinejs.dev directives/magic docs.
- **Capabilities:** Partial swaps, boosts, SSE/WS extensions; Alpine stores/transitions.
- **Usage domain:** Server-rendered apps (Django/Rails/Laravel/Nuxt server routes) with minimal JS.
- **Integration:** native (script tag / npm; works with any backend)
- **Compatibility:** Evergreen (IE legacy dropped in htmx 2).
- **Deps:** None.
- **Availability:** CDN/npm.
- **Maintenance:** Active (htmx 2.x; Alpine 3.x).
- **License:** BSD-2 (htmx) / MIT (Alpine).
- **Security/limits:** Server must enforce authz — client attributes are not a boundary; escape swaps.
- **Related:** Unpoly, Hotwired Turbo/Stimulus.
- **Sources:** Official sites; DEV 2026 ecosystem table (htmx 47.3K stars).
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

**Count: 28 resources** (meets 15–30 minimum). No install/execute performed.
