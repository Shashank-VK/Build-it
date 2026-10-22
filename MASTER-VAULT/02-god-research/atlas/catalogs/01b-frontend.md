# 01b — Frontend Frameworks & Application Development; Styling, UI Primitives & Component Systems

**Workstream:** Researcher #2 (Part 3.2, 3.3 of THE OMNISCIENT RESOURCE ATLAS)
**Research date:** 2026-10-10
**Mode:** Read-only research — discover, inspect, identify, verify, categorize, explain usage, record sources. No install/execute/build/configure/rank/recommend.

## Research approach

- **Live web research:** `browser.search` for discovery across ~14 search themes; `browser.open` on PRIMARY sources (official GitHub repos: README.md, repo metadata, release/license data) for the highest-weight items.
- **Primary-verified (repo README + metadata inspected 2026-10-10):** shadcn-ui/ui, mui/material-ui, pmndrs/zustand, TanStack/query, facebook/react, vuejs/core, storybookjs/storybook, tailwindlabs/tailwindcss, withastro/astro, nuxt/nuxt.
- **Secondary-verified:** items corroborated by 2+ independent sources (reviews, ADRs, skill docs, registry indexes) — labeled accordingly with per-record confidence.
- **Dedup (not re-researched in depth, cross-referenced only):** facebook/astryx (`@astryxdesign/cli`, no MCP), shadcn MCP (official + community), keysjoao/laws-of-ux-skills, alexpate/awesome-design-systems, gztchan/awesome-design, VoltAgent/awesome-design-md (DESIGN.md).
- **Agent-discovery lens:** each record notes how a coding agent discovers real props/APIs/examples (registry indexes, MCP servers, llms.txt-style docs, in-repo skills, registry JSON), per the brief.

## Search themes used

1. `most popular React Vue Svelte Solid UI frameworks 2026 comparison`
2. `Next.js Nuxt SvelteKit Astro SolidStart TanStack Start meta-frameworks 2026`
3. `shadcn ui component registries 21st.dev Magic UI Aceternity Kibo UI 2026`
4. `Radix UI Headless UI Ark UI Base UI React Aria accessible component primitives 2026`
5. `Zustand Jotai Redux Toolkit XState React state management 2026 most used`
6. `TanStack Query SWR RTK Query Apollo client server state data fetching React 2026`
7. `React Router TanStack Router Vue Router Wouter routing libraries 2026 type-safe`
8. `React Hook Form Zod Valibot Yup form validation libraries 2026`
9. `Recharts ECharts Nivo Tremor Victory charting libraries React comparison 2026`
10. `GSAP Framer Motion Motion library React Spring anime.js animation libraries 2026`
11. `Monaco Editor CodeMirror web code editor embed 2026`
12. `Tiptap Lexical Slate Plate rich text editor framework React 2026`
13. `Lucide Heroicons Tabler Phosphor icons React Vue 2026 open source`
14. `Storybook Ladle Histoire component documentation tools 2026`
15. `v0 screenshot-to-code Locofy Plasmic Builder.io AI UI generation design-to-code tools 2026`
16. `styled-components Emotion CSS-in-JS status 2026 vanilla-extract Panda CSS UnoCSS daisyUI`

---

# PART A — FRONTEND FRAMEWORKS AND APPLICATION DEVELOPMENT

## A1. UI frameworks / libraries

### A1.1 — React
- **Canonical identity:** `facebook/react` (npm: `react`)
- **Category:** UI framework (library) — declarative component model
- **Type:** Library (not framework; routing/state/build chosen separately)
- **Official URL:** https://react.dev · https://github.com/facebook/react
- **Description:** Meta's JavaScript library for building web and native user interfaces; component-based, JSX, hooks; React 19 line includes Server Components, `use()` hook; React Compiler 1.0 (Oct 2025) adds automatic memoization.
- **Contents inspected:** GitHub repo root, README.md, repo metadata (2026-10-10). Root contains `compiler/` directory, `CLAUDE.md`, `.claude/` dir.
- **Actual capabilities:** Client rendering with virtual DOM (Fiber reconciler), SSR via `react-dom/server`, React Server Components, Native via React Native; compiler-based auto-memoization.
- **Usage domain:** General-purpose UI for web apps; broadest ecosystem and hiring pool.
- **Integration method:** npm package; typically via meta-framework (Next.js) or Vite.
- **Dependencies:** Not verified in depth (scheduler etc. via package.json — not inspected).
- **Availability:** Open source, npm.
- **Maintenance:** Active — 250,771 stars, 21,722 commits; default branch main.
- **License:** MIT (per GitHub license metadata).
- **Limitations:** Library only — no router, state manager, or SSR story built in; most production React apps use Next.js.
- **Related resources:** Next.js (A2.1), TanStack Start (A2.7), Zustand (A6.1), TanStack Query (A7.1).
- **Sources:** https://github.com/facebook/react (inspected 2026-10-10); https://Strapi.io/blog/best-javascript-frameworks (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified

### A1.2 — Vue.js (Vue 3)
- **Canonical identity:** `vuejs/core` (npm: `vue`)
- **Category:** UI framework — progressive, incrementally adoptable
- **Type:** Framework (core) with official companion libs
- **Official URL:** https://vuejs.org · https://github.com/vuejs/core
- **Description:** Progressive JS framework; Composition API, single-file components, compiler-optimized reactivity; Vue 3.5 cut memory usage ~56% via reactivity refactor; Vue 3.6 stages "Vapor Mode" (compiler-level fine-grained reactivity, per secondary sources).
- **Contents inspected:** GitHub repo root, README.md, repo metadata (2026-10-10).
- **Actual capabilities:** Reactive components, SFC compilation, built-in transitions, official router (Vue Router) and state (Pinia) companions; SSR/hydration supported.
- **Usage domain:** Product teams wanting approachable structure; strong in incremental-adoption scenarios.
- **Integration method:** npm; `npm create vue@latest` (not verified live — documented pattern) or Nuxt meta-framework.
- **Dependencies:** Not inspected.
- **Availability:** Open source, npm.
- **Maintenance:** Active — 54,602 stars, 7,198 commits.
- **License:** MIT.
- **Limitations:** Smaller package/hiring ecosystem than React.
- **Related resources:** Nuxt (A2.2), Vue Router (A5.3), Pinia (A6.7).
- **Sources:** https://github.com/vuejs/core (inspected 2026-10-10); https://www.designveloper.com/blog/front-end-frameworks/ (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified

### A1.3 — Svelte (Svelte 5)
- **Canonical identity:** `sveltejs/svelte` (npm: `svelte`)
- **Category:** UI framework — compiler-based, no virtual DOM
- **Type:** Framework (compiler + runtime)
- **Official URL:** https://svelte.dev · https://github.com/sveltejs/svelte (URL from public knowledge; not opened this session)
- **Description:** Compiler-based UI framework; Svelte 5 introduces Runes (signals-based reactivity). Compiles components to vanilla JS; small bundles, high developer satisfaction (91% retention reported in secondary sources).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Compiled reactivity, transitions/animations built in, SSR; SvelteKit meta-framework.
- **Usage domain:** Lean products, interaction-heavy UI, small teams optimizing bundle size.
- **Integration method:** npm; SvelteKit for full-stack.
- **Dependencies:** Not verified.
- **Availability:** Open source, npm.
- **Maintenance:** Active per multiple 2026 sources. Not directly inspected — Partially verified.
- **License:** MIT (per public knowledge; not re-verified this session).
- **Limitations:** Smaller ecosystem and hiring pool than React/Vue.
- **Related resources:** SvelteKit (A2.3), Melt UI / Bits UI (B5.7).
- **Sources:** https://www.merchtbpn.com/blog/javascript-frameworks-comparison-2026 (accessed 2026-10-10); https://medium.com/@genildocs/the-2026-frontend-framework-guide-nobody-asked-for-but-everyone-needs-a58a9f1cb5e2 (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A1.4 — SolidJS
- **Canonical identity:** `solidjs/solid` (npm: `solid-js`)
- **Category:** UI framework — fine-grained reactivity, no virtual DOM
- **Type:** Library/framework
- **Official URL:** https://www.solidjs.com · https://github.com/solidjs/solid (URL from public knowledge; not opened this session)
- **Description:** Fine-grained compile-time reactivity (signals); JSX without VDOM diffing; highest satisfaction in State of JS surveys for 5 consecutive years per secondary sources despite ~10% usage.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Signals/effects/stores, SSR streaming, high SSR throughput, low memory.
- **Usage domain:** Performance-sensitive apps, data-heavy dashboards.
- **Integration method:** npm; SolidStart meta-framework.
- **Dependencies:** Not verified.
- **Availability:** Open source, npm.
- **Maintenance:** Active per secondary sources; SolidStart pre-1.0 API-stability risk noted. Partially verified.
- **License:** MIT (per public knowledge; not re-verified this session).
- **Limitations:** Small ecosystem, rare job listings; SolidStart young.
- **Related resources:** SolidStart (A2.6), Kobalte (B5.8), Ark UI Solid package (B5.4).
- **Sources:** https://medium.com/@genildocs/the-2026-frontend-framework-guide-nobody-asked-for-but-everyone-needs-a58a9f1cb5e2 (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A1.5 — Angular
- **Canonical identity:** `angular/angular` (npm: `@angular/core`)
- **Category:** UI framework — full, opinionated platform
- **Type:** Framework (batteries-included: router, forms, DI, i18n, SSR)
- **Official URL:** https://angular.dev · https://github.com/angular/angular (URL from public knowledge; not opened this session)
- **Description:** Google's full platform framework; TypeScript-first, dependency injection, signals stable; Angular 21 made zoneless change detection default and dropped zone.js from new apps (per secondary sources).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Components, signals, SSR/incremental hydration (Angular Universal), forms, router, PWA tooling.
- **Usage domain:** Large enterprise apps, structured multi-team codebases.
- **Integration method:** npm; Angular CLI.
- **Dependencies:** Not verified.
- **Availability:** Open source, npm.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified this session).
- **Limitations:** Steeper concepts, heavier platform weight.
- **Related resources:** Analog (A2.10).
- **Sources:** https://Strapi.io/blog/best-javascript-frameworks (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A1.6 — Preact
- **Canonical identity:** `preactjs/preact` (npm: `preact`)
- **Category:** UI library — lightweight React-compatible alternative
- **Type:** Library
- **Official URL:** https://preactjs.com (URL from public knowledge; not opened this session)
- **Description:** 3KB React-compatible library; signals proposed/available; used as the UI layer under Deno Fresh.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** React API subset, hooks, compat layer.
- **Usage domain:** Bundle-size-constrained widgets, Fresh apps.
- **Integration method:** npm; alias `react` → `preact/compat`.
- **Dependencies:** Not verified. **Availability:** Open source, npm.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Not 1:1 React; some ecosystem libs incompatible.
- **Related resources:** Fresh (A2.9).
- **Sources:** Secondary framework roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A1.7 — Qwik
- **Canonical identity:** `QwikDev/qwik` (npm: `@builder.io/qwik`)
- **Category:** UI framework — resumable, edge-oriented
- **Type:** Framework
- **Official URL:** https://qwik.dev (URL from public knowledge; not opened this session)
- **Description:** Resumability model: fine-grained lazy execution, near-zero startup JS; Qwik City meta-framework.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Resumable components (QRLs), SSR-first, Qwik City routing.
- **Usage domain:** Edge-oriented interactive apps optimizing startup.
- **Integration method:** npm.
- **Dependencies:** Not verified. **Availability:** Open source, npm.
- **Maintenance:** Active per secondary sources; newer mental model, ecosystem constraints. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Small ecosystem and talent pool; measure startup/serialization/hosting before choosing (per secondary guidance).
- **Related resources:** None in this catalog.
- **Sources:** https://www.designveloper.com/blog/front-end-frameworks/ (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A1.8 — Alpine.js
- **Canonical identity:** `alpinejs/alpine` (npm: `alpinejs`)
- **Category:** Minimal JS behavior layer (progressive enhancement)
- **Type:** Library
- **Official URL:** https://alpinejs.dev (URL from public knowledge; not opened this session)
- **Description:** Lightweight declarative behavior directly in markup (`x-data`, `x-on`); official Astro integration (`@astrojs/alpinejs` seen in Astro repo directory listing, inspected 2026-10-10).
- **Contents inspected:** Presence of `@astrojs/alpinejs` integration confirmed in withastro/astro README package directory (2026-10-10). Core repo not opened.
- **Actual capabilities:** Reactive attributes/directives without build step.
- **Usage domain:** Sprinkling interactivity on server-rendered pages.
- **Integration method:** npm or CDN script tag.
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Active per ecosystem presence. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Not for complex SPAs.
- **Related resources:** htmx (A1.9), Astro (A2.4).
- **Sources:** https://github.com/withastro/astro (package directory listing, inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A1.9 — htmx
- **Canonical identity:** `bigskysoftware/htmx` (npm: `htmx.org`)
- **Category:** Hypermedia-driven interactivity (HTML-first)
- **Type:** Library
- **Official URL:** https://htmx.org (URL from public knowledge; not opened this session)
- **Description:** Extends HTML with attributes (`hx-get`, `hx-post`, …) for AJAX/WebSocket/SSE-driven partial updates; pairs with server-rendered backends and meta-frameworks (listed among meta-framework test fixtures in a 2026 repo as `html-esm`/`html-global` alternatives).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Declarative HTTP swaps, morphing, history, extensions.
- **Usage domain:** Server-rendered apps wanting interactivity without SPA JS.
- **Integration method:** CDN script or npm.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** BSD-2-Clause (per public knowledge; not re-verified).
- **Limitations:** Server-centric model; not a component framework.
- **Related resources:** Alpine.js (A1.8), Fresh (A2.9) for islands alternative.
- **Sources:** https://github.com/amir-abushanab/favicon-env/blob/HEAD/test/frameworks/README.md (accessed 2026-10-10, lists plain-HTML fixtures as framework alternatives).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A1.10 — Lit
- **Canonical identity:** `lit/lit` (npm: `lit`)
- **Category:** Web-components UI library
- **Type:** Library
- **Official URL:** https://lit.dev (URL from public knowledge; not opened this session)
- **Description:** Google's lightweight library for web components; reactive properties, declarative templates; Storybook lists web components as a supported renderer (verified in storybookjs/storybook README 2026-10-10).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Custom elements, scoped styles, SSR via declarative shadow DOM.
- **Usage domain:** Design-system component implementations, framework-agnostic widgets.
- **Integration method:** npm.
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** BSD-3-Clause (per public knowledge; not re-verified).
- **Limitations:** Smaller app-level ecosystem.
- **Related resources:** Storybook web-components renderer (B16.1).
- **Sources:** https://github.com/storybookjs/storybook (README supported-frameworks table, inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A1.11 — Marko
- **Canonical identity:** `marko-js/marko` (npm: `marko`)
- **Category:** UI language/framework — streaming SSR, partial hydration
- **Type:** Framework
- **Official URL:** https://markojs.com (URL from public knowledge; not opened this session)
- **Description:** eBay's UI language; streaming SSR and resumable/partial hydration; Marko Run meta-framework (referenced in a 2026 meta-framework support matrix as detected framework).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Tags-based components, async streaming, fine-grained updates.
- **Usage domain:** High-throughput SSR storefronts.
- **Integration method:** npm; Marko Run for apps.
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Niche ecosystem.
- **Related resources:** None in this catalog.
- **Sources:** https://github.com/avinash-1994/lunx/commit/0685e61d41975aca2764f7da8f8d501fcff23a33 (meta-framework detection list, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## A2. Meta-frameworks / full-stack frameworks

### A2.1 — Next.js
- **Canonical identity:** `vercel/next.js` (npm: `next`)
- **Category:** Meta-framework — React full-stack (SSR/SSG/ISR/PPR/streaming)
- **Type:** Meta-framework (framework over React)
- **Official URL:** https://nextjs.org · https://github.com/vercel/next.js (URL from public knowledge; not opened this session)
- **Description:** The dominant React meta-framework; App Router with React Server Components default, Server Actions stable, `next/image`; file-based routing, middleware, caching primitives.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** SSR, SSG, ISR, PPR, streaming, Server Components/Actions, route handlers, image optimization.
- **Usage domain:** React teams; app+marketing hybrids; e-commerce; best on Vercel per secondary sources.
- **Integration method:** npm (`create-next-app`).
- **Dependencies:** React 19 line. **Availability:** Open source, npm.
- **Maintenance:** Active per secondary sources (Next.js 15/16 line in 2026). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** App Router complexity drew developer pushback (satisfaction drop 68%→55% in State of JS 2025, per secondary); cache/runtime/server-client complexity; overkill for pure content sites.
- **Related resources:** React (A1.1), TanStack Start (A2.7) as lighter alternative, Vercel v0 (B15.1).
- **Sources:** https://github.com/eneryleen/ai-web-design-codex/blob/HEAD/04-libraries-and-tools/frameworks-for-design.md (accessed 2026-10-10); https://medium.com/@genildocs/the-2026-frontend-framework-guide-nobody-asked-for-but-everyone-needs-a58a9f1cb5e2 (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A2.2 — Nuxt
- **Canonical identity:** `nuxt/nuxt` (npm: `nuxt`)
- **Category:** Meta-framework — Vue full-stack (SSR/SSG/hybrid/edge)
- **Type:** Meta-framework (framework over Vue)
- **Official URL:** https://nuxt.com · https://github.com/nuxt/nuxt
- **Description:** "The full-stack Vue framework"; Nuxt 4 line: SSR, static generation, hybrid and edge-side rendering, automatic routing with code-splitting, data fetching/state, auto-imports, zero-config TypeScript, `server/` directory, 300+ modules.
- **Contents inspected:** GitHub repo root, README.md, repo metadata (2026-10-10). Root contains `AGENTS.md`.
- **Actual capabilities:** As described; Nitro server engine; per-route `routeRules`.
- **Usage domain:** Vue teams blending shell + dashboard; SEO-friendly apps.
- **Integration method:** npm (`npm create nuxt@latest`).
- **Dependencies:** Vue 3, Vite, Nitro (per README claims; package.json not inspected).
- **Availability:** Open source, npm.
- **Maintenance:** Active — 60,926 stars, 15,769 commits, 292 releases.
- **License:** MIT.
- **Limitations:** Server/hydration operational learning curve (per secondary).
- **Related resources:** Vue (A1.2); agent note: `AGENTS.md` at repo root aids coding agents.
- **Sources:** https://github.com/nuxt/nuxt (inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified

### A2.3 — SvelteKit
- **Canonical identity:** `sveltejs/kit` (npm: `@sveltejs/kit`)
- **Category:** Meta-framework — Svelte full-stack
- **Type:** Meta-framework
- **Official URL:** https://kit.svelte.dev · https://github.com/sveltejs/kit (URL from public knowledge; not opened this session)
- **Description:** Official Svelte app framework; SSR/SSG, file-based routing, server load functions, form actions, deployment adapters; native View Transitions via `onNavigate` (per secondary).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** SSR, prerendering, adapters (Node/Cloudflare/Vercel), type-safe data loading.
- **Usage domain:** Svelte teams; high-performance content + app hybrids.
- **Integration method:** npm (`npm create svelte@latest`).
- **Dependencies:** Svelte 5. **Availability:** Open source, npm.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Deployment-adapter model adds operational surface.
- **Related resources:** Svelte (A1.3).
- **Sources:** https://github.com/eneryleen/ai-web-design-codex/blob/HEAD/04-libraries-and-tools/frameworks-for-design.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A2.4 — Astro
- **Canonical identity:** `withastro/astro` (npm: `astro`)
- **Category:** Meta-framework — content-driven websites; islands architecture (also static site generator)
- **Type:** Meta-framework (multi-framework islands)
- **Official URL:** https://astro.build · https://github.com/withastro/astro
- **Description:** "The web framework for content-driven websites"; zero-JS-by-default, Islands Architecture, multi-framework islands (React/Vue/Svelte/Solid/Preact via `@astrojs/*` integrations), Server Islands (`server:defer`), Content Layer; Starlight docs theme maintained in-repo.
- **Contents inspected:** GitHub repo root, README.md, repo metadata (2026-10-10). Package directory lists `@astrojs/react|preact|solid-js|svelte|vue|alpinejs|mdx|…`; root has `AGENTS.md`.
- **Actual capabilities:** Static output default, SSR/hybrid modes, content collections/layer, MDX, sitemap/RSS integrations.
- **Usage domain:** Content/marketing/docs/portfolio sites — default choice per secondary sources.
- **Integration method:** npm (`npm create astro@latest`).
- **Dependencies:** Vite-based (Vite 6 in Astro 5 per secondary).
- **Availability:** Open source, npm.
- **Maintenance:** Active — 63,136 stars, 15,230 commits, 3,295 releases. (GitHub license field showed NOASSERTION; README badges assert MIT — discrepancy noted.)
- **License:** MIT per README badges (GitHub metadata says NOASSERTION — Unresolved discrepancy).
- **Limitations:** Less natural for pervasive shared client state (per secondary).
- **Related resources:** Starlight (A3.2); agent note: `AGENTS.md` at repo root.
- **Sources:** https://github.com/withastro/astro (inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified (license field discrepancy noted)

### A2.5 — Remix → React Router v7 (framework mode)
- **Canonical identity:** `remix-run/react-router` (npm: `react-router`) — Remix merged into React Router v7
- **Category:** Meta-framework capability inside React Router v7 (framework mode)
- **Type:** Library + framework mode (actual category: router library with full-stack framework mode)
- **Official URL:** https://reactrouter.com (URL from public knowledge; not opened this session)
- **Description:** React Router v7 unifies the router library with Remix's framework features (per secondary). Web-fetch style loaders/actions, SSR.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Data APIs (loaders/actions), SSR framework mode, file-based routes via config.
- **Usage domain:** React teams wanting web-standards data loading.
- **Integration method:** npm.
- **Dependencies:** Not verified. **Availability:** Open source, npm.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Smaller ecosystem than Next.js.
- **Related resources:** TanStack Router (A5.2).
- **Sources:** https://github.com/mtrense/lineup/blob/HEAD/data/react-routing/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A2.6 — SolidStart
- **Canonical identity:** `solidjs/solid-start` (npm: `@solidjs/start`)
- **Category:** Meta-framework — Solid full-stack
- **Type:** Meta-framework
- **Official URL:** https://start.solidjs.com (URL from public knowledge; not opened this session)
- **Description:** Solid's full-stack framework; fine-grained compile-time reactivity; high SSR throughput, low memory; pre-1.0 API stability risk (per secondary).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** SSR streaming, file-based routing, server functions.
- **Usage domain:** Raw SSR throughput over ecosystem breadth.
- **Integration method:** npm. **Availability:** Open source, npm.
- **Maintenance:** Active but pre-1.0; ecosystem emerging. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** API stability risk; rare hiring pool.
- **Related resources:** SolidJS (A1.4).
- **Sources:** https://github.com/eneryleen/ai-web-design-codex/blob/HEAD/04-libraries-and-tools/frameworks-for-design.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A2.7 — TanStack Start
- **Canonical identity:** `TanStack/router` monorepo, package `@tanstack/react-start` (docs: tanstack.com/start)
- **Category:** Meta-framework — React full-stack over TanStack Router
- **Type:** Meta-framework
- **Official URL:** https://tanstack.com/start (URL from public knowledge; not opened this session)
- **Description:** Full-stack React framework built on TanStack Router; SSR + streaming + type-safe server functions (`createServerFn`); Vite-powered; RC/stable during 2025 per secondary sources; positioned as lighter Next.js alternative without Vercel coupling.
- **Contents inspected:** Not inspected directly this session (ecosystem listing seen in TanStack/query README 2026-10-10).
- **Actual capabilities:** SSR, streaming, server functions with validators (e.g., Zod), file-based routing via router plugin.
- **Usage domain:** New React apps wanting type-safe routing + SSR without Next.js.
- **Integration method:** npm (`@tanstack/react-start`, `@tanstack/router-plugin`).
- **Dependencies:** TanStack Router, Vite. **Availability:** Open source, npm.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Younger than Next.js; smaller deployment-adapter matrix.
- **Related resources:** TanStack Router (A5.2), TanStack Query (A7.1).
- **Sources:** https://github.com/TanStack/query (ecosystem listing in README, inspected 2026-10-10); https://github.com/eboot/vibes-plug/blob/HEAD/skills/tanstack-query-expert/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A2.8 — Analog
- **Canonical identity:** `analogjs/analog` (npm: `@analogjs/platform`)
- **Category:** Meta-framework — Angular full-stack (Vite-powered)
- **Type:** Meta-framework
- **Official URL:** https://analogjs.org (URL from public knowledge; not opened this session)
- **Description:** Angular meta-framework on Vite; file-based routing, SSR/SSG.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** As described (per secondary).
- **Usage domain:** Angular teams wanting Vite-era DX.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Community-driven (not Google-official).
- **Related resources:** Angular (A1.5).
- **Sources:** https://github.com/fyodorio/metaframeworks-newsletter-website/blob/HEAD/src/content/blog/what-is-a-metaframework.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A2.9 — Fresh (Deno)
- **Canonical identity:** `denoland/fresh` (npm n/a — Deno/JSR)
- **Category:** Meta-framework — Preact full-stack on Deno; islands architecture
- **Type:** Meta-framework
- **Official URL:** https://fresh.deno.dev (URL from public knowledge; not opened this session)
- **Description:** Deno's web framework; Preact + islands, zero build step, edge deployment.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Islands, SSR, file routing, Deno Deploy.
- **Usage domain:** Deno-ecosystem apps, edge-first.
- **Integration method:** Deno (`deno run -A -r https://fresh.deno.dev`).
- **Dependencies:** Deno runtime. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Deno-ecosystem coupling.
- **Related resources:** Preact (A1.6).
- **Sources:** https://github.com/fyodorio/metaframeworks-newsletter-website/blob/HEAD/src/content/blog/what-is-a-metaframework.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A2.10 — Waku
- **Canonical identity:** `dai-shi/waku` (npm: `waku`)
- **Category:** Meta-framework — minimal React Server Components framework
- **Type:** Meta-framework
- **Official URL:** https://waku.gg (URL from public knowledge; not opened this session)
- **Description:** Minimal RSC framework with file-based routing (from Zustand/Jotai author Daishi Kato's org).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** RSC-first routing/rendering.
- **Usage domain:** Minimal RSC experiments.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Minimal — bring your own data layer.
- **Related resources:** React (A1.1).
- **Sources:** https://github.com/fyodorio/metaframeworks-newsletter-website/blob/HEAD/src/content/blog/what-is-a-metaframework.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A2.11 — Vike
- **Canonical identity:** `vikejs/vike` (npm: `vike`; formerly `vite-plugin-ssr`)
- **Category:** Meta-framework — flexible, framework-agnostic SSR/SSG (Vite plugin)
- **Type:** Meta-framework (Vite plugin architecture)
- **Official URL:** https://vike.dev (URL from public knowledge; not opened this session)
- **Description:** Successor/rename of `vite-plugin-ssr`; "do-one-thing-do-it-well" composable SSR/SSG over Vite with React (and Vue/Solid) support.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** SSR/SSG/pre-rendering, routing, data fetching hooks.
- **Usage domain:** Teams wanting SSR control without a batteries-included framework.
- **Integration method:** npm Vite plugin.
- **Dependencies:** Vite. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** More assembly required than Next/Nuxt.
- **Related resources:** None in this catalog.
- **Sources:** https://github.com/mtrense/lineup/blob/HEAD/data/react-routing/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A2.12 — RedwoodJS
- **Canonical identity:** `redwoodjs/redwood` (npm: `@redwoodjs/core`)
- **Category:** Full-stack framework — React + GraphQL + Prisma
- **Type:** Framework
- **Official URL:** https://redwoodjs.com (URL from public knowledge; not opened this session)
- **Description:** Opinionated full-stack React framework (Cells data-fetching pattern, GraphQL API side, Prisma).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Web side + API side, generators, auth integrations.
- **Usage domain:** Full-stack React+GraphQL startups.
- **Integration method:** npm/CLI (`yarn create redwood-app`).
- **Dependencies:** React, GraphQL Yoga, Prisma (per public knowledge; not re-verified).
- **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Opinionated GraphQL-centrism.
- **Related resources:** None in this catalog.
- **Sources:** Meta-framework detection lists (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A2.13 — One (Tamagui)
- **Canonical identity:** `tamagui/tamagui`, package `one`
- **Category:** Meta-framework — React (+ React Native) file-based routing across web and native
- **Type:** Meta-framework
- **Official URL:** https://onestack.dev (URL from public knowledge; not opened this session)
- **Description:** From the Tamagui team; unifies web + native routing.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** File-based routing for React web and React Native (per secondary).
- **Usage domain:** Cross-platform React teams.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Niche; Tamagui-ecosystem coupling.
- **Related resources:** None in this catalog.
- **Sources:** https://github.com/mtrense/lineup/blob/HEAD/data/react-routing/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified

## A3. Static site generators & docs-site builders

### A3.1 — Astro (as SSG)
Cross-reference: A2.4. Astro doubles as the leading modern static site generator (zero-JS default, Content Layer). Verified 2026-10-10.

### A3.2 — Starlight
- **Canonical identity:** `withastro/starlight` (npm: `@astrojs/starlight`)
- **Category:** Docs-site theme/generator on Astro
- **Type:** Framework theme (Astro integration)
- **Official URL:** https://starlight.astro.build · https://github.com/withastro/starlight (URL from public knowledge; not opened this session; referenced in withastro/astro README as official external project, inspected 2026-10-10)
- **Description:** Official Astro docs theme: i18n, search, sidebar nav, dark mode out of the box.
- **Contents inspected:** Referenced as official project in withastro/astro README directory table (2026-10-10). Repo itself not opened.
- **Actual capabilities:** Per secondary: full docs-site scaffolding on Astro.
- **Usage domain:** Technical documentation sites.
- **Integration method:** Astro integration (`@astrojs/starlight`).
- **Dependencies:** Astro. **Availability:** Open source.
- **Maintenance:** Active (official Astro project). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Astro-coupled.
- **Related resources:** Astro (A2.4), Docusaurus (A3.3), VitePress (A3.4).
- **Sources:** https://github.com/withastro/astro (README directory table, inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A3.3 — Docusaurus
- **Canonical identity:** `facebook/docusaurus` (npm: `@docusaurus/core`)
- **Category:** Static docs-site generator (React/MDX)
- **Type:** Framework (SSG)
- **Official URL:** https://docusaurus.io (URL from public knowledge; not opened this session)
- **Description:** Meta's React-based docs SSG; MDX, versioning, i18n, blog; widely used for OSS project docs.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Versioned docs, search (Algolia), blog, MDX components.
- **Usage domain:** OSS/library documentation sites.
- **Integration method:** npm (`npx create-docusaurus@latest`).
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Docs-shaped; interactive component controls absent (per secondary comparison — use Storybook for components).
- **Related resources:** Starlight (A3.2), VitePress (A3.4).
- **Sources:** https://webfield.io/storybook/alternatives (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A3.4 — VitePress
- **Canonical identity:** `vuejs/vitepress` (npm: `vitepress`)
- **Category:** Static docs-site generator (Vue/Vite)
- **Type:** Framework (SSG)
- **Official URL:** https://vitepress.dev (URL from public knowledge; not opened this session)
- **Description:** Vue team's Vite-powered docs SSG; markdown-centered, fast; powers Vue/Vite docs themselves.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Markdown→site, theming, i18n (community), Vue components in markdown.
- **Usage domain:** Library docs (Vue ecosystem and beyond).
- **Integration method:** npm.
- **Dependencies:** Vue, Vite. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Vue-flavored theming.
- **Related resources:** Docusaurus (A3.3), Starlight (A3.2).
- **Sources:** Meta-framework detection lists including VitePress (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A3.5 — Eleventy (11ty)
- **Canonical identity:** `11ty/eleventy` (npm: `@11ty/eleventy`)
- **Category:** Static site generator (multi-template)
- **Type:** Framework (SSG)
- **Official URL:** https://www.11ty.dev (URL from public knowledge; not opened this session)
- **Description:** Flexible zero-client-JS SSG supporting many template languages; still deployed widely (Netlify agent skill documents Eleventy build gotchas, accessed 2026-10-10).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Multi-engine templates, collections, transforms.
- **Usage domain:** Content sites, blogs.
- **Integration method:** npm.
- **Dependencies:** Node. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** No component-islands model; bring your own interactivity.
- **Related resources:** Hugo (A3.6).
- **Sources:** https://github.com/practicalswan/agent-skills/blob/HEAD/netlify-frameworks/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A3.6 — Hugo
- **Canonical identity:** `gohugoio/hugo`
- **Category:** Static site generator (Go binary)
- **Type:** Tool/framework (SSG)
- **Official URL:** https://gohugo.io (URL from public knowledge; not opened this session)
- **Description:** Extremely fast Go-based SSG; single binary; theme ecosystem via git submodules.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Sub-second builds for large sites, taxonomies, shortcodes.
- **Usage domain:** Blogs, docs, marketing sites.
- **Integration method:** Binary download / package manager.
- **Dependencies:** None (Go binary). **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Apache-2.0 (per public knowledge; not re-verified).
- **Limitations:** Go-template learning curve.
- **Related resources:** Eleventy (A3.5).
- **Sources:** https://github.com/practicalswan/agent-skills/blob/HEAD/netlify-frameworks/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A3.7 — Gatsby
- **Canonical identity:** `gatsbyjs/gatsby` (npm: `gatsby`)
- **Category:** Static site generator (React/GraphQL data layer) — declining for new projects
- **Type:** Framework (SSG)
- **Official URL:** https://www.gatsbyjs.com (URL from public knowledge; not opened this session)
- **Description:** React SSG with GraphQL data layer and plugin ecosystem; multiple 2026 sources advise against it for new projects ("don't use Gatsby for new projects").
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** SSG/DSG/SSR, image pipeline, plugin ecosystem.
- **Usage domain:** Legacy maintenance; existing Gatsby sites.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Maintenance-mode posture per secondary sources; Netlify skill still documents it. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Build-time scaling issues; ecosystem momentum moved to Astro/Next.
- **Related resources:** Astro (A2.4).
- **Sources:** https://github.com/eneryleen/ai-web-design-codex/blob/HEAD/04-libraries-and-tools/frameworks-for-design.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Historical (declining; verify before greenfield use)

## A4. Islands / partial hydration / resumability

- **Astro Islands** (A2.4, Verified): selective hydration via `client:*` directives; multi-framework islands. Primary-verified via repo.
- **Fresh islands** (A2.9, Partially verified): Preact islands on Deno.
- **Marko** (A1.11, Partially verified): streaming + partial hydration.
- **Qwik resumability** (A1.7, Partially verified): resumable QRLs rather than hydration.
- **Server Islands (`server:defer`)** — Astro feature for deferred server-rendered islands (per secondary; Partially verified).
- **Preact signals / Vue Vapor Mode / Svelte Runes** — compiler-level reactivity reducing hydration cost (per secondary; Partially verified).

## A5. Routing

### A5.1 — React Router
- **Canonical identity:** `remix-run/react-router` (npm: `react-router`)
- **Category:** Routing library for React (with v7 framework mode)
- **Type:** Library (+ framework mode, see A2.5)
- **Official URL:** https://reactrouter.com (URL from public knowledge; not opened this session)
- **Description:** De-facto React router; v7 unifies with Remix framework features; data routers with loaders/actions.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Declarative routes, nested layouts, data loading, SSR framework mode.
- **Usage domain:** React SPAs and full-stack (framework mode).
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Not type-safe by default (contrast TanStack Router).
- **Related resources:** TanStack Router (A5.2).
- **Sources:** https://github.com/mtrense/lineup/blob/HEAD/data/react-routing/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A5.2 — TanStack Router
- **Canonical identity:** `TanStack/router` (npm: `@tanstack/react-router`, plus solid/vue adapters)
- **Category:** Type-safe routing library (React/Solid/Vue) with data loading
- **Type:** Library
- **Official URL:** https://tanstack.com/router (URL from public knowledge; not opened this session)
- **Description:** Fully type-safe router: typed routes/params/search params, built-in loaders with caching, file-based routing via Vite plugin (`@tanstack/router-plugin`), devtools, auto code-splitting; basis of TanStack Start. Skill metadata in the wild references v1.166.2 (2026).
- **Contents inspected:** Not inspected directly this session (ecosystem presence confirmed in TanStack/query README 2026-10-10).
- **Actual capabilities:** Type-safe navigation, search-param validation (Zod), route loaders, preloading, code splitting.
- **Usage domain:** SPAs and TanStack Start apps needing type-safe routing.
- **Integration method:** npm + Vite plugin.
- **Dependencies:** Framework adapter. **Availability:** Open source.
- **Maintenance:** Active; very frequent releases per skill metadata. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Vite-plugin codegen adds build coupling; client-first loaders by default.
- **Related resources:** TanStack Start (A2.7), TanStack Query (A7.1); agent note: multiple agent skills document it (eboot/vibes-plug, albo-club).
- **Sources:** https://github.com/TanStack/query (ecosystem listing, inspected 2026-10-10); https://github.com/albo-club/albo-ouvre-boite/blob/HEAD/.agents/skills/tanstack-react-router/SKILL.md (accessed 2026-10-10); https://dev.to/0012303/tanstack-router-has-a-free-api-you-should-know-about-429i (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### A5.3 — Vue Router
- **Canonical identity:** `vuejs/router` (npm: `vue-router`)
- **Category:** Official routing library for Vue
- **Type:** Library
- **Official URL:** https://router.vuejs.org (URL from public knowledge; not opened this session)
- **Description:** Official Vue router; nested routes, navigation guards, lazy loading.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** As described.
- **Usage domain:** Vue SPAs (Nuxt provides its own file-based routing).
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active (official Vue project). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Vue-only.
- **Related resources:** Nuxt (A2.2).
- **Sources:** Secondary framework roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A5.4 — Wouter
- **Canonical identity:** `molefrog/wouter` (npm: `wouter`)
- **Category:** Minimalist hook-based router for React/Preact
- **Type:** Library (~2KB)
- **Official URL:** https://github.com/molefrog/wouter (URL from public knowledge; not opened this session)
- **Description:** Tiny (~1–2KB) React router; hooks API (`useRoute`, `useLocation`).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Route matching, links, redirects; no data loading.
- **Usage domain:** Small SPAs where bundle size matters.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** No built-in data loading, nested layouts are manual.
- **Related resources:** React Router (A5.1).
- **Sources:** https://github.com/mtrense/lineup/blob/HEAD/data/react-routing/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## A6. State management (client state)

### A6.1 — Zustand
- **Canonical identity:** `pmndrs/zustand` (npm: `zustand`)
- **Category:** Client state management — minimal hook-based store
- **Type:** Library
- **Official URL:** https://zustand.docs.pmnd.rs · https://github.com/pmndrs/zustand
- **Description:** "Bear necessities for state management in React" — small, fast, scalable; hook-first, no providers; middleware (persist, devtools, immer, subscribeWithSelector); vanilla (`zustand/vanilla`) usable without React.
- **Contents inspected:** GitHub repo root, full README.md (recipes: transient updates, persist/immer middleware, TypeScript usage), repo metadata (2026-10-10).
- **Actual capabilities:** External stores with selector subscriptions, transient (non-reactive) updates, persistence, Redux DevTools integration, SSR guidance (README notes client-only usage; not for React Server Components).
- **Usage domain:** App-wide client store for small/medium React apps; UI chrome state.
- **Integration method:** npm (`create()` hook).
- **Dependencies:** React (peer). **Availability:** Open source, npm.
- **Maintenance:** Active — 58,801 stars, 1,382 commits, 105 releases.
- **License:** MIT.
- **Limitations:** Client-only; README explicitly warns against use in React Server Components; async patterns are hand-rolled.
- **Related resources:** Jotai (A6.2), Redux Toolkit (A6.3), TanStack Store (A6.8).
- **Sources:** https://github.com/pmndrs/zustand (README + metadata inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified

### A6.2 — Jotai
- **Canonical identity:** `pmndrs/jotai` (npm: `jotai`)
- **Category:** Client state management — atomic model
- **Type:** Library
- **Official URL:** https://jotai.org · https://github.com/pmndrs/jotai (URL from public knowledge; not opened this session)
- **Description:** Primitive, flexible atomic state for React (`atom`, `useAtom`); native Suspense/async atoms; same Pmndrs team as Zustand/Valtio.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Atoms, derived atoms, async atoms, storage atoms, SSR provider scoping.
- **Usage domain:** Fine-grained state, derived computations.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active per secondary sources (~2M weekly downloads per 2026 secondary). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Atomic mental model differs from single-store familiarity.
- **Related resources:** Zustand (A6.1), Valtio (A6.4).
- **Sources:** https://github.com/dushyanthb27/react-interview-guide-by-dushyanth/blob/HEAD/sections/04-state-management/08-zustand-jotai-valtio.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A6.3 — Redux Toolkit (RTK)
- **Canonical identity:** `reduxjs/redux-toolkit` (npm: `@reduxjs/toolkit`)
- **Category:** Client state management — opinionated Redux
- **Type:** Library
- **Official URL:** https://redux-toolkit.js.org · https://github.com/reduxjs/redux-toolkit (URL from public knowledge; not opened this session)
- **Description:** Official Redux opinionated toolset: `configureStore`, `createSlice`, `createAsyncThunk`, `createEntityAdapter`; RTK Query built in for data fetching.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Slices, thunks, entity adapters, DevTools/time-travel, RTK Query data layer.
- **Usage domain:** Large coordinated teams; orgs with Redux templates/training; action transcripts during incidents.
- **Integration method:** npm + `react-redux`.
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** More boilerplate/structure than Zustand; don't duplicate server data in it (use TanStack Query/RTK Query).
- **Related resources:** RTK Query (A7.3), Redux Saga/Thunk (legacy async).
- **Sources:** http://reliasoftware.com/blog/react-state-management-libraries (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A6.4 — Valtio
- **Canonical identity:** `pmndrs/valtio` (npm: `valtio`)
- **Category:** Client state management — proxy-based mutable API
- **Type:** Library
- **Official URL:** https://github.com/pmndrs/valtio (URL from public knowledge; not opened this session)
- **Description:** Proxy-based state (`proxy`, `useSnapshot`, `subscribe`); mutable-style code with automatic snapshots.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** As described; DevTools available.
- **Usage domain:** Teams preferring mutable-style (Vue/MobX-like) code.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active per secondary sources (~800K weekly downloads). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** SSR needs care (`proxyWithComputed` awareness per secondary).
- **Related resources:** Zustand (A6.1), Jotai (A6.2).
- **Sources:** https://github.com/dushyanthb27/react-interview-guide-by-dushyanth/blob/HEAD/sections/04-state-management/08-zustand-jotai-valtio.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A6.5 — XState
- **Canonical identity:** `statelyai/xstate` (npm: `xstate`)
- **Category:** State management — actor/statechart model
- **Type:** Library (framework-agnostic core + framework bindings)
- **Official URL:** https://stately.ai · https://github.com/statelyai/xstate (URL from public knowledge; not opened this session)
- **Description:** State machines/statecharts and actor model for workflow-heavy UI; visual tooling via Stately.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Machines, actors, visual editor, framework bindings.
- **Usage domain:** Complex workflows, wizards, orchestration-heavy features.
- **Integration method:** npm. **Availability:** Open source core; commercial Stately tooling.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT core (per public knowledge; not re-verified).
- **Limitations:** Heavier mental model; overkill for simple UI state.
- **Related resources:** Zag.js (B5.10) — state machines for headless components.
- **Sources:** http://reliasoftware.com/blog/react-state-management-libraries (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A6.6 — MobX
- **Canonical identity:** `mobxjs/mobx` (npm: `mobx`)
- **Category:** Client state management — transparent reactive (observables)
- **Type:** Library
- **Official URL:** https://mobx.js.org (URL from public knowledge; not opened this session)
- **Description:** Observable-based reactivity (`observable`, `makeAutoObservable`, `observer`); long-standing alternative to Redux.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Observables, actions, computed, reactions.
- **Usage domain:** Teams preferring transparent reactivity.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Less explicit data flow than Redux; magic-by-convention critique.
- **Related resources:** Valtio (A6.4).
- **Sources:** http://reliasoftware.com/blog/react-state-management-libraries (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A6.7 — Pinia
- **Canonical identity:** `vuejs/pinia` (npm: `pinia`)
- **Category:** Client state management — official Vue store
- **Type:** Library
- **Official URL:** https://pinia.vuejs.org (URL from public knowledge; not opened this session)
- **Description:** Official Vue state management (successor to Vuex); Composition-API-friendly stores, DevTools.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Define stores, SSR support, plugins.
- **Usage domain:** Vue apps (Nuxt has its own data/state conventions).
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active (official Vue project). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Vue-only.
- **Related resources:** Vue (A1.2), Nuxt (A2.2).
- **Sources:** Secondary framework roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A6.8 — TanStack Store / TanStack DB
- **Canonical identity:** `TanStack/store` (npm: `@tanstack/store`); `TanStack/db` (npm: `@tanstack/db`)
- **Category:** Reactive data store / sync client store
- **Type:** Library (framework-agnostic core + adapters)
- **Official URL:** https://tanstack.com/store · https://tanstack.com/db (URLs from public knowledge; not opened this session)
- **Description:** TanStack Store — "reactive data store"; TanStack DB — "reactive sync client store" (per TanStack/query README ecosystem listing, inspected 2026-10-10).
- **Contents inspected:** Ecosystem listing in TanStack/query README only (2026-10-10). Repos not opened.
- **Actual capabilities:** Not verified in depth — Unresolved.
- **Usage domain:** TanStack-ecosystem apps.
- **Integration method:** npm.
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Active (listed as current ecosystem members). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Newer; smaller community than Zustand/Redux.
- **Related resources:** TanStack Query (A7.1).
- **Sources:** https://github.com/TanStack/query (ecosystem listing, inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A6.9 — Recoil (historical)
- **Canonical identity:** `facebookexperimental/Recoil` (npm: `recoil`)
- **Category:** Client state management — atomic (Meta experiment)
- **Type:** Library — UNMAINTAINED
- **Official URL:** https://github.com/facebookexperimental/Recoil (URL from public knowledge; not opened this session)
- **Description:** Meta's atomic state library; multiple 2026 sources advise avoiding for new projects (unmaintained).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Atoms/selectors (historical).
- **Usage domain:** Legacy only.
- **Integration method:** npm (not recommended).
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Unmaintained per multiple secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Do not adopt; migrate to Jotai.
- **Related resources:** Jotai (A6.2).
- **Sources:** http://reliasoftware.com/blog/react-state-management-libraries (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Historical

## A7. Server state / data fetching

### A7.1 — TanStack Query
- **Canonical identity:** `TanStack/query` (npm: `@tanstack/react-query` + core/framework adapters)
- **Category:** Async state management / server-state data fetching
- **Type:** Library (framework-agnostic core + React/Solid/Svelte/Vue adapters)
- **Official URL:** https://tanstack.com/query · https://github.com/TanStack/query
- **Description:** "Powerful asynchronous state management, server-state utilities and data fetching"; protocol-agnostic (REST/GraphQL/promises); caching, refetching, pagination/infinite scroll, mutations, dependent queries, prefetching, cancellation, Suspense support.
- **Contents inspected:** GitHub repo root, README.md, repo metadata (2026-10-10). Root contains `AGENTS.md` and `AI_POLICY.md`; ecosystem listing documents TanStack DB/Form/Pacer/Router/Start/Store/Table/Virtual/DevTools.
- **Actual capabilities:** Query/mutation caches, query-key invalidation, background refetch, optimistic updates, devtools.
- **Usage domain:** Server state in any JS app (~80% of app state per secondary); dominant data layer for React.
- **Integration method:** npm (`QueryClientProvider` + `useQuery`).
- **Dependencies:** Framework adapter. **Availability:** Open source, npm.
- **Maintenance:** Active — 50,407 stars, 5,517 commits, 2,685 releases.
- **License:** MIT.
- **Limitations:** ~13KB gzip (per secondary); learning curve on cache semantics; not a replacement for client UI state.
- **Related resources:** SWR (A7.2), RTK Query (A7.3); agent note: `AGENTS.md` + `AI_POLICY.md` in repo root; multiple agent skills document query-key factories.
- **Sources:** https://github.com/TanStack/query (inspected 2026-10-10); https://github.com/yiheng0221/yihengwu-jko-interview/blob/HEAD/docs/decisions/0009-tanstack-query-as-data-layer.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified

### A7.2 — SWR
- **Canonical identity:** `vercel/swr` (npm: `swr`)
- **Category:** Server-state data fetching — stale-while-revalidate
- **Type:** Library (React hooks)
- **Official URL:** https://swr.vercel.app · https://github.com/vercel/swr (URL from public knowledge; not opened this session)
- **Description:** Vercel's React hooks for data fetching with stale-while-revalidate strategy; lighter/simpler than TanStack Query (~4KB per secondary).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** `useSWR`, `useSWRMutation`, `useSWRInfinite`, caching, revalidation on focus.
- **Usage domain:** Next.js apps; simpler single-resource fetching.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources (Vercel-driven maintenance noted as vendor consideration by one source). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Infinite-query ergonomics clunkier than TanStack Query; less capable devtools (per secondary).
- **Related resources:** TanStack Query (A7.1).
- **Sources:** https://github.com/yiheng0221/yihengwu-jko-interview/blob/HEAD/docs/decisions/0009-tanstack-query-as-data-layer.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A7.3 — RTK Query
- **Canonical identity:** Part of `reduxjs/redux-toolkit` (npm: `@reduxjs/toolkit/query`)
- **Category:** Server-state data fetching inside Redux Toolkit
- **Type:** Library (data-fetching layer of RTK)
- **Official URL:** https://redux-toolkit.js.org/rtk-query/overview (URL from public knowledge; not opened this session)
- **Description:** `createApi`/`injectEndpoints`; codegen from OpenAPI; cache management integrated with Redux store.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Endpoints, caching, invalidation tags, polling.
- **Usage domain:** Redux-heavy teams wanting data fetching without a new dependency.
- **Integration method:** npm (part of RTK).
- **Dependencies:** Redux Toolkit. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Tied to Redux store.
- **Related resources:** Redux Toolkit (A6.3), TanStack Query (A7.1).
- **Sources:** https://github.com/cajasmota/archigraph/issues/2894 (React ecosystem extraction spec, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A7.4 — Apollo Client
- **Canonical identity:** `apollographql/apollo-client` (npm: `@apollo/client`)
- **Category:** GraphQL data management (client state + fetching)
- **Type:** Library
- **Official URL:** https://www.apollographql.com/docs/react (URL from public knowledge; not opened this session)
- **Description:** Full-featured GraphQL client: normalized cache, `useQuery(gql)`, mutations, subscriptions.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Normalized cache, optimistic UI, pagination helpers, devtools.
- **Usage domain:** GraphQL-first apps.
- **Integration method:** npm.
- **Dependencies:** GraphQL. **Availability:** Open source core.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** GraphQL-only; heavier than REST fetchers.
- **Related resources:** urql (A7.5), TanStack Query (A7.1, protocol-agnostic incl. GraphQL).
- **Sources:** https://github.com/q-penc-ai/q-penc.ai/blob/HEAD/.claude/skills/react-frontend/references/state-and-data.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A7.5 — urql
- **Canonical identity:** `urql-graphql/urql` (npm: `@urql/core`, framework bindings)
- **Category:** GraphQL client — lightweight
- **Type:** Library
- **Official URL:** https://commerce.nearform.com/open-source/urql (URL from public knowledge; not opened this session)
- **Description:** Lightweight, extensible GraphQL client (exchanges architecture).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Queries/mutations/subscriptions via exchanges.
- **Usage domain:** Teams wanting smaller GraphQL client than Apollo.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Smaller ecosystem than Apollo.
- **Related resources:** Apollo Client (A7.4).
- **Sources:** Secondary state/data roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## A8. Forms & validation

### A8.1 — React Hook Form
- **Canonical identity:** `react-hook-form/react-hook-form` (npm: `react-hook-form`)
- **Category:** Form state management (React)
- **Type:** Library
- **Official URL:** https://react-hook-form.com · https://github.com/react-hook-form/react-hook-form (URL from public knowledge; not opened this session)
- **Description:** Performant, uncontrolled-input-based form library (`useForm`, `register`, `Controller`); delegates validation to schema resolvers via `@hookform/resolvers` (supports Zod 3+4, Valibot, Yup, ArkType, Standard Schema, etc.).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Field registration, validation modes, error handling, form state subscriptions.
- **Usage domain:** React forms of any complexity; most common choice per 2026 agent skills.
- **Integration method:** npm + `@hookform/resolvers`.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** React-only; validation language is external (by design).
- **Related resources:** Zod (A8.4), TanStack Form (A8.3), Formik (A8.2); agent note: `frontend-nexus` documents RHF patterns for agents.
- **Sources:** https://github.com/thegbosstv/frontend-nexus/blob/HEAD/app/content/libraries/react-hook-form.mdx (accessed 2026-10-10); https://github.com/aratkruglik/claude-sdlc/blob/HEAD/plugins/react-plugin/skills/react-forms/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### A8.2 — Formik
- **Canonical identity:** `jaredpalmer/formik` (npm: `formik`)
- **Category:** Form state management (React) — legacy but stable
- **Type:** Library
- **Official URL:** https://formik.org (URL from public knowledge; not opened this session)
- **Description:** Long-standing React form library; multiple 2026 sources describe it as "legacy but stable".
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Form state, validation (Yup integration), field components.
- **Usage domain:** Existing Formik codebases.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Stable/legacy posture per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Heavier re-render model than RHF; prefer RHF for new work per secondary consensus.
- **Related resources:** React Hook Form (A8.1).
- **Sources:** https://github.com/aratkruglik/claude-sdlc/blob/HEAD/plugins/react-plugin/skills/react-forms/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A8.3 — TanStack Form
- **Canonical identity:** `TanStack/form` (npm: `@tanstack/react-form` + adapters)
- **Category:** Type-safe form state (framework adapters)
- **Type:** Library
- **Official URL:** https://tanstack.com/form (URL from public knowledge; not opened this session)
- **Description:** "Type‑safe form state" per TanStack/query README ecosystem listing (inspected 2026-10-10).
- **Contents inspected:** Ecosystem listing only. Repo not opened.
- **Actual capabilities:** Not verified in depth — Unresolved.
- **Usage domain:** TanStack-ecosystem apps.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active (current ecosystem member). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Newer; smaller community than RHF.
- **Related resources:** React Hook Form (A8.1).
- **Sources:** https://github.com/TanStack/query (ecosystem listing, inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A8.4 — Zod
- **Canonical identity:** `colinhacks/zod` (npm: `zod`)
- **Category:** Schema declaration & validation (TypeScript-first)
- **Type:** Library
- **Official URL:** https://zod.dev · https://github.com/colinhacks/zod (URL from public knowledge; not opened this session)
- **Description:** TypeScript-first schema validation with static type inference; Zod 4 line current in 2026 (resolvers handle both v3/v4 per secondary); Standard Schema participant.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Object/string/number schemas, transforms, coercion, inference.
- **Usage domain:** Form validation, API input validation, server-function validators (TanStack Start), tRPC.
- **Integration method:** npm; `@hookform/resolvers/zod`.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Bundle heavier than Valibot for validation-only use.
- **Related resources:** Valibot (A8.5), Yup (A8.6).
- **Sources:** https://github.com/thegbosstv/frontend-nexus/blob/HEAD/app/content/libraries/react-hook-form.mdx (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A8.5 — Valibot
- **Canonical identity:** `fabian-hiller/valibot` (npm: `valibot`)
- **Category:** Schema validation — modular, bundle-size-focused
- **Type:** Library
- **Official URL:** https://valibot.dev · https://github.com/fabian-hiller/valibot (URL from public knowledge; not opened this session)
- **Description:** Modular schema library; tree-shakeable functions; significantly smaller bundles than Zod; Standard Schema compatible.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Schemas, actions/transforms, i18n error messages.
- **Usage domain:** Size-conscious validation; forms via resolvers.
- **Integration method:** npm; `@hookform/resolvers/valibot`.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Smaller ecosystem of examples than Zod.
- **Related resources:** Zod (A8.4).
- **Sources:** https://github.com/janstevens/react-hook-form-resolvers (resolver list, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A8.6 — Yup
- **Canonical identity:** `jquense/yup` (npm: `yup`)
- **Category:** Schema validation (established)
- **Type:** Library
- **Official URL:** https://github.com/jquense/yup (URL from public knowledge; not opened this session)
- **Description:** Long-standing object-schema validator; historically paired with Formik.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Object schemas, async validation, locale customization.
- **Usage domain:** Legacy Formik stacks.
- **Integration method:** npm; `@hookform/resolvers/yup`.
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Weaker TS inference than Zod/Valibot.
- **Related resources:** Zod (A8.4).
- **Sources:** https://github.com/janstevens/react-hook-form-resolvers (resolver list, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## A9. Tables / data grids

### A9.1 — TanStack Table
- **Canonical identity:** `TanStack/table` (npm: `@tanstack/react-table` + adapters)
- **Category:** Headless datagrid logic
- **Type:** Library (headless — bring your own markup/styles)
- **Official URL:** https://tanstack.com/table (URL from public knowledge; not opened this session)
- **Description:** "Headless datagrids" per TanStack/query README ecosystem listing (inspected 2026-10-10); sorting, filtering, pagination, row selection, virtualization hooks.
- **Contents inspected:** Ecosystem listing only. Repo not opened.
- **Actual capabilities:** Headless table state machine (per public knowledge; features not re-verified in depth).
- **Usage domain:** Custom-styled data tables in React/Solid/Vue/Svelte.
- **Integration method:** npm adapter package.
- **Dependencies:** Framework adapter. **Availability:** Open source.
- **Maintenance:** Active (current ecosystem member). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Headless — UI/markup is your job (often paired with shadcn Table).
- **Related resources:** AG Grid (A9.2), TanStack Virtual (A9.4).
- **Sources:** https://github.com/TanStack/query (ecosystem listing, inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A9.2 — AG Grid
- **Canonical identity:** `ag-grid/ag-grid` (npm: `ag-grid-community`, `ag-grid-react` etc.)
- **Category:** Enterprise data grid (feature-complete)
- **Type:** Library (community + enterprise tiers)
- **Official URL:** https://www.ag-grid.com (URL from public knowledge; not opened this session)
- **Description:** Full-featured datagrid: grouping, pivoting, server-side row model, Excel export; community (MIT) + enterprise (commercial) split.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Per public knowledge — not re-verified in depth.
- **Usage domain:** Data-dense enterprise grids.
- **Integration method:** npm framework packages.
- **Dependencies:** Framework adapter. **Availability:** Dual-license.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (community) / commercial (enterprise) — per public knowledge; not re-verified.
- **Limitations:** Enterprise features paywalled; heavier than headless options.
- **Related resources:** MUI X Data Grid (A9.3), TanStack Table (A9.1).
- **Sources:** Secondary grid comparisons (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A9.3 — MUI X Data Grid
- **Canonical identity:** `mui/mui-x` (npm: `@mui/x-data-grid`)
- **Category:** React data grid (MIT + commercial Pro/Premium)
- **Type:** Library
- **Official URL:** https://mui.com/x/react-data-grid/ (URL from public knowledge; not opened this session)
- **Description:** MUI's datagrid; community MIT tier plus Pro/Premium commercial features (row grouping, Excel export, etc.).
- **Contents inspected:** Not inspected directly this session. (MUI core repo inspected 2026-10-10 confirms org activity.)
- **Actual capabilities:** Per public knowledge — not re-verified in depth.
- **Usage domain:** React enterprise tables in MUI apps.
- **Integration method:** npm.
- **Dependencies:** MUI core. **Availability:** Dual-license.
- **Maintenance:** Active (MUI org active, verified via mui/material-ui 2026-10-10). Partially verified.
- **License:** MIT (community) / commercial (Pro/Premium) — per public knowledge; not re-verified.
- **Limitations:** Advanced features commercial.
- **Related resources:** AG Grid (A9.2), MUI (B7.1).
- **Sources:** https://github.com/mui/material-ui (org activity, inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A9.4 — TanStack Virtual
- **Canonical identity:** `TanStack/virtual` (npm: `@tanstack/react-virtual` + adapters)
- **Category:** Headless UI virtualization (windowing)
- **Type:** Library
- **Official URL:** https://tanstack.com/virtual (URL from public knowledge; not opened this session)
- **Description:** "Virtualized rendering" per TanStack/query README ecosystem listing (inspected 2026-10-10); row/column virtualization for lists, tables, grids.
- **Contents inspected:** Ecosystem listing only.
- **Actual capabilities:** Not verified in depth — Unresolved.
- **Usage domain:** Large lists/tables.
- **Integration method:** npm. **Availability:** Open source.
- **Maintenance:** Active (current ecosystem member). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Headless — rendering is your job.
- **Related resources:** TanStack Table (A9.1).
- **Sources:** https://github.com/TanStack/query (ecosystem listing, inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## A10. Charting & data visualization

### A10.1 — Recharts
- **Canonical identity:** `recharts/recharts` (npm: `recharts`)
- **Category:** Charting library — declarative React components (SVG)
- **Type:** Library
- **Official URL:** https://recharts.org · https://github.com/recharts/recharts (URL from public knowledge; not opened this session)
- **Description:** Declarative composable React chart components (`<LineChart>`, `<XAxis>`, `<Tooltip>`); SVG rendering; highest-download React chart library (~50M weekly npm downloads per Sep 2026 secondary); built on D3 submodules.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Line/bar/area/pie/composed charts, responsive containers, tooltips.
- **Usage domain:** Standard React dashboards.
- **Integration method:** npm.
- **Dependencies:** D3 submodules, React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** SVG per-data-point DOM nodes — comfortable ceiling ~8–10k points; not for real-time streaming (per secondary).
- **Related resources:** Tremor (A10.7, built on Recharts), Nivo (A10.3).
- **Sources:** http://dev.to/charttech/best-react-chart-libraries-ranked-by-performance-and-use-case-30cb (accessed 2026-10-10); https://github.com/luirzy/react-chart (comparison PoC, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A10.2 — Apache ECharts
- **Canonical identity:** `apache/echarts` (npm: `echarts`)
- **Category:** Charting library — canvas/SVG, config-object driven
- **Type:** Library (framework-agnostic; wrappers exist per framework)
- **Official URL:** https://echarts.apache.org · https://github.com/apache/echarts (URL from public knowledge; not opened this session)
- **Description:** Feature-rich charting via single `option` config object; Canvas default, SVG renderer available; huge chart-type coverage incl. geo/3D.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** 20+ chart types, visual encoding, large-data optimizations.
- **Usage domain:** Complex/large-data dashboards across frameworks.
- **Integration method:** npm; `echarts-for-react` wrapper for React.
- **Dependencies:** None (core). **Availability:** Open source (Apache).
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Apache-2.0 (per public knowledge; not re-verified).
- **Limitations:** Config-object API less React-idiomatic; imperative updates.
- **Related resources:** Recharts (A10.1), AG Charts (enterprise alt, not catalogued in depth).
- **Sources:** https://github.com/luirzy/react-chart (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A10.3 — Nivo
- **Canonical identity:** `plouc/nivo` (npm: `@nivo/*`)
- **Category:** Charting library — declarative React, heavily themed (SVG + Canvas variants)
- **Type:** Library
- **Official URL:** https://nivo.rocks · https://github.com/plouc/nivo (URL from public knowledge; not opened this session)
- **Description:** 50+ chart types, strong theming system, SVG default with Canvas variants (`*Canvas`) for large datasets; built on D3.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Bar/line/pie/treemap/sankey/chord/etc., responsive wrappers, pattern/gradient defs.
- **Usage domain:** Beautiful themed dataviz in React.
- **Integration method:** npm per-chart packages.
- **Dependencies:** D3, React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Bundle weight when many chart types imported; theming API learning curve.
- **Related resources:** Recharts (A10.1), visx (A10.5).
- **Sources:** https://github.com/luirzy/react-chart (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A10.4 — Victory
- **Canonical identity:** `FormidableLabs/victory` (npm: `victory`)
- **Category:** Charting library — composable React components (SVG)
- **Type:** Library
- **Official URL:** https://commerce.nearform.com/open-source/victory (URL from public knowledge; not opened this session)
- **Description:** Composable chart components with built-in zoom/pan/brush containers; ~25 chart types; also Victory Native for React Native.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Composable chart primitives, animation, containers.
- **Usage domain:** Custom interactive charts in React/React Native.
- **Integration method:** npm.
- **Dependencies:** D3, React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** SVG perf ceiling similar to Recharts.
- **Related resources:** Recharts (A10.1).
- **Sources:** https://github.com/luirzy/react-chart (accessed 2026-10-10); https://stackshare.io/stackups/recharts-vs-victory (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A10.5 — visx
- **Canonical identity:** `airbnb/visx` (npm: `@visx/*`)
- **Category:** Low-level visualization primitives for React (D3 + React)
- **Type:** Library (collection of primitives)
- **Official URL:** https://airbnb.io/visx · https://github.com/airbnb/visx (URL from public knowledge; not opened this session)
- **Description:** Airbnb's set of low-level viz primitives combining D3 math with React rendering; build your own charts from tested parts.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Scales, shapes, axes, grids, tooltips, zoom — unstyled primitives.
- **Usage domain:** Bespoke chart systems, design-system chart kits.
- **Integration method:** npm per-package.
- **Dependencies:** D3 submodules, React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** You compose everything; no ready-made charts.
- **Related resources:** D3 (A10.8), Nivo (A10.3).
- **Sources:** https://github.com/luirzy/react-chart (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A10.6 — Chart.js / react-chartjs-2
- **Canonical identity:** `chartjs/Chart.js` (npm: `chart.js`); `reactchartjs/react-chartjs-2` (npm: `react-chartjs-2`)
- **Category:** Charting library — Canvas, config-driven; React wrapper
- **Type:** Library
- **Official URL:** https://www.chartjs.org · https://github.com/chartjs/Chart.js (URLs from public knowledge; not opened this session)
- **Description:** Canvas-based config-object charts; strong large-data performance; react-chartjs-2 is the React binding (~3.8M weekly downloads per 2026 secondary snapshot).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Line/bar/pie/radar/scatter etc.; plugins; animation.
- **Usage domain:** Performance-sensitive canvas charts.
- **Integration method:** npm.
- **Dependencies:** None (core). **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Config-object API; canvas a11y needs extra work.
- **Related resources:** Apache ECharts (A10.2).
- **Sources:** https://github.com/one-learning-community/rozie.js/blob/HEAD/docs/components/chartjs-comparison.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A10.7 — Tremor
- **Canonical identity:** `tremorlabs/tremor` (npm: `@tremor/react`)
- **Category:** Dashboard chart/UI blocks (React + Tailwind; Recharts under the hood)
- **Type:** Component library (chart-focused blocks)
- **Official URL:** https://www.tremor.so (URL from public knowledge; not opened this session)
- **Description:** Prebuilt Tailwind dashboard components (KPI cards, charts) built on Recharts; Apache-2.0.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Chart + layout blocks for dashboards.
- **Usage domain:** Quick React dashboards.
- **Integration method:** npm.
- **Dependencies:** Recharts, Tailwind. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Apache-2.0 (per secondary license-harvest table; not re-verified).
- **Limitations:** Opinionated styling; Recharts perf ceiling inherited.
- **Related resources:** Recharts (A10.1), shadcn charts (docs pattern).
- **Sources:** https://github.com/luirzy/react-chart (accessed 2026-10-10); https://github.com/justinfowler925/justinfowler.com/blob/HEAD/assets/cowork-skills/shine/references/ecosystem.md (license table, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A10.8 — D3.js
- **Canonical identity:** `d3/d3` (npm: `d3`)
- **Category:** Data-driven documents — low-level viz toolkit
- **Type:** Library (modular)
- **Official URL:** https://d3js.org · https://github.com/d3/d3 (URL from public knowledge; not opened this session)
- **Description:** The foundational toolkit: selections, scales, shapes, layouts, transitions; powers Recharts/Nivo/visx under the hood.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** DOM/SVG/Canvas data binding, 30+ modules.
- **Usage domain:** Custom visualizations of any kind.
- **Integration method:** npm (modular imports).
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Stable/mature per secondary sources. Partially verified.
- **License:** ISC (per public knowledge; not re-verified).
- **Limitations:** Low-level; you build everything.
- **Related resources:** Observable Plot (A10.9), visx (A10.5).
- **Sources:** Secondary chart comparisons (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A10.9 — Observable Plot
- **Canonical identity:** `observablehq/plot` (npm: `@observablehq/plot`)
- **Category:** High-level declarative dataviz (grammar-of-graphics-ish)
- **Type:** Library
- **Official URL:** https://observablehq.com/plot · https://github.com/observablehq/plot (URL from public knowledge; not opened this session)
- **Description:** Concise API for exploratory charts (`Plot.plot({marks: […]})`); SVG output.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Marks, transforms, faceting.
- **Usage domain:** Exploratory/analytical charts, notebooks.
- **Integration method:** npm.
- **Dependencies:** D3 modules. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** ISC (per public knowledge; not re-verified).
- **Limitations:** Less app-framework integration than Recharts.
- **Related resources:** D3 (A10.8).
- **Sources:** https://github.com/justinfowler925/justinfowler.com/blob/HEAD/assets/cowork-skills/shine/references/ecosystem.md (license table, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## A11. Code editors (embeddable)

### A11.1 — Monaco Editor
- **Canonical identity:** `microsoft/monaco-editor` (npm: `monaco-editor`); React wrapper `@monaco-editor/react`; Codingame fork `@codingame/monaco-vscode-editor-api`
- **Category:** Embeddable code editor (VS Code's editor as a library)
- **Type:** Library
- **Official URL:** https://microsoft.github.io/monaco-editor · https://github.com/microsoft/monaco-editor (URL from public knowledge; not opened this session)
- **Description:** The VS Code editor surfaced as a web library: IntelliSense, multi-cursor, diff editor, command palette, language workers; ~0.5–2MB gzip; worker-based architecture.
- **Contents inspected:** Not inspected directly this session; evaluated via 2026 ADRs comparing it with CodeMirror 6.
- **Actual capabilities:** Syntax/semantic highlighting, completions, hover, diff, minimap.
- **Usage domain:** IDE-grade in-browser editing (playgrounds, admin code fields, notebooks).
- **Integration method:** npm or CDN AMD loader; Vite worker config needed.
- **Dependencies:** Web workers. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Heavy bundle; worker/CSP complexity; overkill for simple inputs (multiple 2026 ADRs chose CodeMirror 6 instead for these reasons).
- **Related resources:** CodeMirror (A11.2).
- **Sources:** https://github.com/blueshork/maestro-deck/commit/d55cce01ac018b583478c91545c77a7b5baad503 (accessed 2026-10-10); https://github.com/pidbid/hyac/commit/dadba8252cff56c6000f1d174a775cc9acb76f86 (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A11.2 — CodeMirror 6
- **Canonical identity:** `codemirror/dev` (npm: `@codemirror/*`, `codemirror`); React wrapper `@uiw/react-codemirror`
- **Category:** Embeddable code editor — modular, tree-shakeable
- **Type:** Library (extension-based)
- **Official URL:** https://codemirror.net · https://github.com/codemirror/dev (URL from public knowledge; not opened this session)
- **Description:** Ground-up rewrite (2021); composable extensions (state/view/history/language packs/themes); ~130–150KB; ESM-native, no workers; used by Obsidian/GitHub/Notion (per secondary).
- **Contents inspected:** Not inspected directly this session; evaluated via 2026 ADRs.
- **Actual capabilities:** Syntax highlighting (20–50+ langs via packs), autocomplete, search/replace, multiple cursors, themes; LSP is bring-your-own.
- **Usage domain:** Embeddable editors where bundle/CSP matter (query editors, markdown source mode, AI chat code surfaces).
- **Integration method:** npm modular packages.
- **Dependencies:** None core. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** No built-in command palette/diff editor; IntelliSense is BYO via LSP.
- **Related resources:** Monaco Editor (A11.1); used as Tiptap source-mode companion (A12.1 notes).
- **Sources:** https://github.com/ibrahemid/writ/blob/HEAD/docs/adr/003-codemirror-over-monaco.md (accessed 2026-10-10); https://github.com/swarajbachu/zuse/blob/HEAD/specs/0.02-MVP/decisions/0009-codemirror-over-monaco.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

## A12. Rich-text / markdown / block editors

### A12.1 — Tiptap
- **Canonical identity:** `ueberdosis/tiptap` (npm: `@tiptap/*`)
- **Category:** Headless rich-text editor framework (ProseMirror-based)
- **Type:** Library/framework
- **Official URL:** https://tiptap.dev · https://github.com/ueberdosis/tiptap (URL from public knowledge; not opened this session)
- **Description:** Headless editor on ProseMirror; extension packages (StarterKit etc.); React/Vue/Svelte/headless bindings; v3 line in 2026; official shadcn editor component uses Tiptap (per secondary); Pro extensions/cloud commercial (free plan removed June 2025 per secondary).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Schema-based documents, extensions, collaboration (Pro), comments (Pro), AI toolkit (Pro), markdown import/export.
- **Usage domain:** Document editors, CMS fields, comment systems.
- **Integration method:** npm extension packages.
- **Dependencies:** ProseMirror. **Availability:** MIT core; commercial Pro/cloud.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT core; Pro extensions commercial (per secondary; not re-verified).
- **Limitations:** Collaboration/comments/AI are paid; extension-per-package install surface (~19 packages noted in one 2026 analysis).
- **Related resources:** ProseMirror (A12.4), BlockNote (A12.5), Plate (A12.3).
- **Sources:** https://github.com/csdev19/hiring-tool/blob/HEAD/apps/fumadocs/content/docs/research/rich-text-editor.mdx (accessed 2026-10-10); https://github.com/wachterjohannes/primavista/blob/HEAD/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A12.2 — Lexical
- **Canonical identity:** `facebook/lexical` (npm: `lexical`, `@lexical/react`)
- **Category:** Extensible text-editor framework (Meta)
- **Type:** Library/framework
- **Official URL:** https://lexical.dev · https://github.com/facebook/lexical (URL from public knowledge; not opened this session)
- **Description:** Meta's editor framework (~22–25KB core); command-based, custom nodes, React-first with framework-agnostic core; production-proven (Facebook/Instagram/Threads); Yjs collaboration; markdown import/export.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Nodes/commands/plugins, `DecoratorNode` for React UI blocks, collaboration plugin.
- **Usage domain:** AI-native editing surfaces (prompt inputs, artifact blocks, inline suggestions), comment editors.
- **Integration method:** npm.
- **Dependencies:** None core. **Availability:** Open source.
- **Maintenance:** Active per secondary sources (0.x with occasional breaking changes noted). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Smaller plugin ecosystem than Tiptap; UI is bring-your-own.
- **Related resources:** Tiptap (A12.1); agent note: command system maps naturally to agent tools (per 2026 analysis).
- **Sources:** https://github.com/ryuever/react-tapable-editor/blob/HEAD/codebase-wiki/discussion/20260519-editor-kernel-selection.md (accessed 2026-10-10); https://github.com/recoletas/pinax/blob/HEAD/docs/plan/block-editors-research-20260615.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A12.3 — Plate
- **Canonical identity:** `udecode/plate` (npm: `platejs` / `@platejs/*`)
- **Category:** Rich-text editor kit on Slate (React) — plugin ecosystem
- **Type:** Library (framework over Slate)
- **Official URL:** https://platejs.org · https://github.com/udecode/plate (URL from public knowledge; not opened this session)
- **Description:** 50+ plugins on Slate; AIKit (AIPlugin/AIChatPlugin, markdown streaming), SlashKit, Yjs collaboration, Markdown plugin; MIT core with Plate Plus commercial.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Per secondary comparison matrix.
- **Usage domain:** Feature-rich React editors with AI features, minimal setup.
- **Integration method:** npm.
- **Dependencies:** Slate (inherits Slate risk — see A12.6). **Availability:** MIT core / commercial Plus.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT core; Plate Plus commercial (per secondary; not re-verified).
- **Limitations:** React-only; inherits Slate core maintenance risk.
- **Related resources:** Slate (A12.6), Tiptap (A12.1).
- **Sources:** https://github.com/recoletas/pinax/blob/HEAD/docs/plan/block-editors-research-20260615.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A12.4 — ProseMirror
- **Canonical identity:** `ProseMirror/prosemirror` (npm: `prosemirror-*`)
- **Category:** Toolkit for structured rich-text editing (low-level)
- **Type:** Library (modular toolkit)
- **Official URL:** https://prosemirror.net · https://github.com/ProseMirror/prosemirror (URL from public knowledge; not opened this session)
- **Description:** De-facto standard toolkit: strict schema, immutable document model, transactions, collab module; foundation of Tiptap/BlockNote/Remirror/Milkdown.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Schema, state, view, transforms, collab, markdown serialization.
- **Usage domain:** Custom editors needing strict document models.
- **Integration method:** npm modules.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Stable/mature per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Very low-level; steep learning curve; no UI.
- **Related resources:** Tiptap (A12.1).
- **Sources:** https://github.com/wachterjohannes/primavista/blob/HEAD/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A12.5 — BlockNote
- **Canonical identity:** `TypeCell/blocknote` (npm: `@blocknote/*`)
- **Category:** Block-based Notion-like editor (ProseMirror+Tiptap)
- **Type:** Library (product layer)
- **Official URL:** https://www.blocknotejs.org · https://github.com/TypeCell/blocknote (URL from public knowledge; not opened this session)
- **Description:** Notion-like block editor with React UI out of the box; built-in AI extension (`@blocknote/xl-ai`); Yjs collab; markdown export explicitly lossy.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Blocks, slash menu, AI menu, collab.
- **Usage domain:** Fast product validation of Notion-like editing.
- **Integration method:** npm.
- **Dependencies:** ProseMirror/Tiptap. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MPL-2.0 core; XL packages GPL-3.0 (per secondary; not re-verified — check copyleft).
- **Limitations:** React-only; thicker product-layer encapsulation; copyleft on XL packages.
- **Related resources:** Tiptap (A12.1), Plate (A12.3).
- **Sources:** https://github.com/wachterjohannes/primavista/blob/HEAD/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A12.6 — Slate
- **Canonical identity:** `ianstormtaylor/slate` (npm: `slate`, `slate-react`)
- **Category:** Rich-text editor framework (React) — REPORTED ARCHIVED
- **Type:** Library
- **Official URL:** https://github.com/ianstormtaylor/slate (URL from public knowledge; not opened this session)
- **Description:** Once-flexible React editor framework; one 2026 secondary source reports the repo was archived on 2026-02-04.
- **Contents inspected:** Not inspected directly this session — archive claim NOT primary-verified.
- **Actual capabilities:** Historical.
- **Usage domain:** Legacy only; Plate inherits its risk.
- **Integration method:** npm (not recommended).
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Reported archived 2026-02-04 by one secondary source — Unresolved (primary not checked).
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Do not adopt for new work pending verification.
- **Related resources:** Plate (A12.3).
- **Sources:** https://github.com/wachterjohannes/primavista/blob/HEAD/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Unresolved (archive status needs primary check)

### A12.7 — Quill
- **Canonical identity:** `quilljs/quill` (npm: `quill`)
- **Category:** Rich-text editor (Parchment document model)
- **Type:** Library (vanilla; community React wrappers)
- **Official URL:** https://quilljs.com · https://github.com/quilljs/quill (URL from public knowledge; not opened this session)
- **Description:** Long-standing WYSIWYG editor; Quill 2 line; ~45KB; API/format-based deltas.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Formats, modules (toolbar, history), deltas.
- **Usage domain:** Simple WYSIWYG fields.
- **Integration method:** npm; community React bindings.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** BSD-3-Clause (per public knowledge; not re-verified).
- **Limitations:** Collaboration and block-level features limited.
- **Related resources:** Tiptap (A12.1).
- **Sources:** https://github.com/wachterjohannes/primavista/blob/HEAD/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A12.8 — Milkdown
- **Canonical identity:** `Milkdown/milkdown` (npm: `@milkdown/*`)
- **Category:** Markdown-native WYSIWYG editor (ProseMirror + Remark)
- **Type:** Library (plugin-driven)
- **Official URL:** https://milkdown.dev · https://github.com/Milkdown/milkdown (URL from public knowledge; not opened this session)
- **Description:** Markdown-first editing on ProseMirror+Remark; React/Vue/Solid/vanilla bindings.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Markdown round-trip editing, plugins.
- **Usage domain:** Markdown-centric apps.
- **Integration method:** npm.
- **Dependencies:** ProseMirror, Remark. **Availability:** Open source.
- **Maintenance:** Active per secondary sources (niche). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Niche community.
- **Related resources:** Tiptap (A12.1), MDXEditor (A12.9).
- **Sources:** https://github.com/wachterjohannes/primavista/blob/HEAD/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A12.9 — MDXEditor
- **Canonical identity:** `mdx-editor/editor` (npm: `@mdxeditor/editor`)
- **Category:** Markdown WYSIWYG editor (React)
- **Type:** Library
- **Official URL:** https://mdxeditor.dev · https://github.com/mdx-editor/editor (URL from public knowledge; not opened this session)
- **Description:** Notion-like WYSIWYG with native markdown support; code blocks with syntax highlighting; TypeScript.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Rich markdown editing UI.
- **Usage domain:** Notion-like markdown experiences.
- **Integration method:** npm.
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** More opinionated UI; heavier; less flexible.
- **Related resources:** Milkdown (A12.8).
- **Sources:** https://github.com/csdev19/hiring-tool/blob/HEAD/apps/fumadocs/content/docs/research/rich-text-editor.mdx (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A12.10 — Novel (AI editor demo)
- **Canonical identity:** `steven-tey/novel` (npm n/a — template/demo)
- **Category:** AI-autocomplete editor showcase (Tiptap-based) — DEMO/TEMPLATE, not a library
- **Type:** Demo site / starter template (actual category: demo, not framework)
- **Official URL:** https://github.com/steven-tey/novel (URL from public knowledge; not opened this session)
- **Description:** Notion-style AI autocomplete editor built on Tiptap; Apache-2.0; widely forked as a starter, but "more demo than product" per secondary.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** AI completion UI patterns on Tiptap.
- **Usage domain:** Reference/starting point for AI writing features.
- **Integration method:** Clone/fork.
- **Dependencies:** Tiptap. **Availability:** Open source.
- **Maintenance:** Template posture. Partially verified.
- **License:** Apache-2.0 (per secondary; not re-verified).
- **Limitations:** Demo, not a maintained library.
- **Related resources:** Tiptap (A12.1).
- **Sources:** https://github.com/wachterjohannes/primavista/blob/HEAD/RESEARCH.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## A13. Animation / interaction systems

### A13.1 — Motion (Framer Motion)
- **Canonical identity:** `framer/motion` (npm: `motion`, legacy `framer-motion`)
- **Category:** Animation library — React-first declarative motion
- **Type:** Library
- **Official URL:** https://motion.dev · https://github.com/framer/motion (URL from public knowledge; not opened this session)
- **Description:** Springs, gestures, `layout` (automatic FLIP) animations, `AnimatePresence` exit animations, scroll utilities; Motion One is the WAAPI-backed lightweight subset (~4KB); `motion/react` import path current.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Declarative animations, drag gestures, scroll-linked motion, layout animations.
- **Usage domain:** React product UI motion — the default choice per 2026 sources.
- **Integration method:** npm (`motion`).
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Active (v13.4.0 Sep 2026, extremely active per secondary; ~15.4M weekly downloads). Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** React-flavored; heavier than WAAPI subset; don't pair with a second spring engine.
- **Related resources:** GSAP (A13.2), React Spring (A13.4); agent note: `motion/react` import path is the current convention agents should use.
- **Sources:** https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/motion.md (accessed 2026-10-10); https://github.com/yashop965/sih2026-ps171-browser-agent/blob/HEAD/docs/research/mouse-animation-libraries.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### A13.2 — GSAP
- **Canonical identity:** `greensock/GSAP` (npm: `gsap`); React binding `@gsap/react`
- **Category:** Animation engine — framework-agnostic timelines
- **Type:** Library
- **Official URL:** https://gsap.com · https://github.com/greensock/GSAP (URL from public knowledge; not opened this session)
- **Description:** Timelines, scroll sequencing (ScrollTrigger), SVG morphing, text splitting, precise orchestration; ~23KB core + plugins. Webflow acquired GreenSock; since GSAP 3.13 all plugins free incl. commercial use — but NOT OSI/MIT licensed (no forking/redistribution; bars competing visual-animation tools per secondary license analysis).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Tweens/timelines/stagger, 20+ eases, ScrollTrigger, SplitText, Inertia.
- **Usage domain:** Scroll-driven storytelling, marketing/brand motion, complex choreography.
- **Integration method:** npm; `@gsap/react` (`useGSAP`) required for React StrictMode safety per secondary.
- **Dependencies:** None. **Availability:** Free incl. commercial (post-Webflow 2025); not open-source licensed.
- **Maintenance:** Active (3.15.0 Apr 2026 per secondary). Partially verified.
- **License:** Proprietary "Standard no-charge" license — free for commercial use, NOT OSI-approved (per secondary; verify current terms before embedding/redistributing).
- **Limitations:** License restricts forking/redistribution and competing tools; don't mix with Motion in one project (pick by component-state vs timeline need).
- **Related resources:** Motion (A13.1), Anime.js (A13.3).
- **Sources:** https://github.com/eazyapp-tech/module-redesign-pipeline/blob/HEAD/references/motion-and-reference-libraries.md (accessed 2026-10-10); https://github.com/justinfowler925/justinfowler.com/blob/HEAD/assets/cowork-skills/shine/references/ecosystem.md (license table, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified (license terms need primary check)

### A13.3 — Anime.js
- **Canonical identity:** `juliangarnier/anime` (npm: `animejs`)
- **Category:** Animation engine — lightweight, timeline-based
- **Type:** Library
- **Official URL:** https://animejs.com · https://github.com/juliangarnier/anime (URL from public knowledge; not opened this session)
- **Description:** v4 line; CSS/SVG/DOM/object animation, spring eases, timelines, stagger; ~17KB; no React coupling.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** As described.
- **Usage domain:** Lightweight SVG/CSS animation without GSAP weight; non-React pages.
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active (4.5.0 Jun 2026, sponsored per secondary). Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** Less scroll tooling than GSAP; smaller ecosystem.
- **Related resources:** GSAP (A13.2).
- **Sources:** https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/motion.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A13.4 — React Spring
- **Canonical identity:** `pmndrs/react-spring` (npm: `@react-spring/web`)
- **Category:** Animation library — physics-based (springs)
- **Type:** Library
- **Official URL:** https://www.react-spring.dev · https://github.com/pmndrs/react-spring (URL from public knowledge; not opened this session)
- **Description:** Physics-only animation model; strong for gesture-driven and 3D-adjacent work; ~25KB.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Springs, trails, transitions, gesture integration.
- **Usage domain:** Physics-feel interactions.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Overlaps Motion; don't install both.
- **Related resources:** Motion (A13.1).
- **Sources:** https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/motion.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A13.5 — Lottie / dotLottie
- **Canonical identity:** `airbnb/lottie-web` (npm: `lottie-web`); `lottiefiles/dotlottie-web`
- **Category:** Vector animation playback (After Effects exports)
- **Type:** Library/player
- **Official URL:** https://airbnb.io/lottie · https://dotlottie.io (URLs from public knowledge; not opened this session)
- **Description:** Renders After Effects animations as JSON (Lottie) or compressed `.lottie` (dotLottie, ThorVG WASM); designer-handoff workflow.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Play-once/looped vector animations; React wrappers (`lottie-react`).
- **Usage domain:** Splash/onboarding/marketing animations from designers.
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open source (lottie-web).
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (lottie-web, per public knowledge; not re-verified).
- **Limitations:** Not interactive state machines (use Rive for that).
- **Related resources:** Rive (A13.6).
- **Sources:** https://github.com/marktantongco/opencode-os/blob/HEAD/skills/motion-system-playbook/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A13.6 — Rive
- **Canonical identity:** `rive-app/rive` (runtimes; npm: `@rive-app/react-canvas` etc.)
- **Category:** Interactive animation — real-time state machines
- **Type:** Tool + runtimes (editor commercial; runtimes open)
- **Official URL:** https://rive.app · https://github.com/rive-app/rive (URL from public knowledge; not opened this session)
- **Description:** Designer-authored interactive animations with state machines; small runtimes for web/iOS/Android/React Native/Flutter.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** State-machine-driven interactive graphics.
- **Usage domain:** Interactive characters, animated UI states.
- **Integration method:** npm runtimes; Rive editor for authoring.
- **Dependencies:** Runtime per platform. **Availability:** Runtimes open source; editor SaaS.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (runtimes, per public knowledge; not re-verified).
- **Limitations:** Authoring tool is proprietary.
- **Related resources:** Lottie (A13.5).
- **Sources:** https://github.com/dantetekanem/leo-personal-pi/blob/HEAD/skills/frontend-animator/references/motion-library-guide.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A13.7 — AutoAnimate (FormKit)
- **Canonical identity:** `formkit/auto-animate` (npm: `@formkit/auto-animate`)
- **Category:** Zero-config list/layout animation utility
- **Type:** Library (~2KB)
- **Official URL:** https://auto-animate.formkit.com · https://github.com/formkit/auto-animate (URL from public knowledge; not opened this session)
- **Description:** One line animates add/remove/reorder of list items; framework-agnostic.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Automatic FLIP-ish transitions on DOM mutations.
- **Usage domain:** List changes, accordions.
- **Integration method:** npm; single directive/hook.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Narrow scope by design.
- **Related resources:** Motion (A13.1).
- **Sources:** https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/motion.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A13.8 — Lenis
- **Canonical identity:** `darkroomengineering/lenis` (npm: `lenis`)
- **Category:** Smooth-scroll library
- **Type:** Library
- **Official URL:** https://lenis.darkroom.engineering (URL from public knowledge; not opened this session)
- **Description:** Inertial smooth scrolling; often paired with GSAP ScrollTrigger; hijacks native scroll — use only as a locked design decision, disable under reduced-motion (per secondary guidance).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Smooth wheel/touch scroll, scroll callbacks.
- **Usage domain:** Marketing/brand pages.
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Scroll hijacking harms UX if misapplied; never on product UI per secondary guidance.
- **Related resources:** GSAP (A13.2).
- **Sources:** https://github.com/eazyapp-tech/module-redesign-pipeline/blob/HEAD/references/motion-and-reference-libraries.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A13.9 — Theatre.js
- **Canonical identity:** `theatre-js/theatre` (npm: `@theatre/core`, `@theatre/studio`)
- **Category:** Visual keyframe editor + animation runtime
- **Type:** Library + dev tool (studio is dev-only)
- **Official URL:** https://www.theatrejs.com (URL from public knowledge; not opened this session)
- **Description:** Timeline/keyframe editing UI for complex sequences and 3D camera work.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Keyframe sequences, studio editor.
- **Usage domain:** Complex choreographed sequences, 3D scenes.
- **Integration method:** npm.
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** Apache-2.0 (per public knowledge; not re-verified).
- **Limitations:** Studio is dev-only; niche.
- **Related resources:** GSAP (A13.2).
- **Sources:** https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/motion.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified

### A13.10 — Remotion
- **Canonical identity:** `remotion-dev/remotion` (npm: `remotion`)
- **Category:** Programmatic video rendering with React
- **Type:** Library/framework
- **Official URL:** https://www.remotion.dev (URL from public knowledge; not opened this session)
- **Description:** Write videos in React; render to MP4/WebM via headless Chromium; data-driven video generation.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** React reconciler → video frames; templating, audio.
- **Usage domain:** Programmatic marketing/product videos.
- **Integration method:** npm.
- **Dependencies:** Not verified. **Availability:** Open source core; commercial license for some uses.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Check current terms — core open with commercial licensing for companies (per public knowledge; not re-verified — Unresolved).
- **Limitations:** Rendering compute cost; license nuance for commercial use.
- **Related resources:** None in this catalog.
- **Sources:** https://github.com/marktantongco/opencode-os/blob/HEAD/skills/motion-system-playbook/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified (license unresolved)

## A14. 2D/3D browser graphics

### A14.1 — Three.js
- **Canonical identity:** `mrdoob/three.js` (npm: `three`)
- **Category:** 3D graphics library (WebGL/WebGPU)
- **Type:** Library
- **Official URL:** https://threejs.org · https://github.com/mrdoob/three.js (URL from public knowledge; not opened this session)
- **Description:** The standard WebGL/WebGPU 3D library; scenes, cameras, materials, loaders, postprocessing.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Full 3D engine features in the browser.
- **Usage domain:** 3D scenes, product configurators, immersive experiences, particles.
- **Integration method:** npm; CDN modules.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** ~130KB+; imperative API (use R3F for React).
- **Related resources:** React Three Fiber (A14.2), Babylon.js (A14.4).
- **Sources:** https://github.com/marktantongco/opencode-os/blob/HEAD/skills/motion-system-playbook/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A14.2 — React Three Fiber
- **Canonical identity:** `pmndrs/react-three-fiber` (npm: `@react-three/fiber`); ecosystem: `@react-three/drei`
- **Category:** React renderer for Three.js
- **Type:** Library
- **Official URL:** https://r3f.docs.pmnd.rs · https://github.com/pmndrs/react-three-fiber (URL from public knowledge; not opened this session)
- **Description:** Declarative React bindings for Three.js; drei adds helpers (controls, loaders, environment).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Reconciler mapping Three objects to JSX; ecosystem of helpers.
- **Usage domain:** React 3D scenes.
- **Integration method:** npm.
- **Dependencies:** three, React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** React-only; still ships Three.js weight.
- **Related resources:** Three.js (A14.1), React Spring (A13.4, gesture/3D-adjacent).
- **Sources:** Secondary 3D roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A14.3 — PixiJS
- **Canonical identity:** `pixijs/pixi.js` (npm: `pixi.js`)
- **Category:** 2D WebGL rendering engine
- **Type:** Library
- **Official URL:** https://pixijs.com · https://github.com/pixijs/pixi.js (URL from public knowledge; not opened this session)
- **Description:** Fast 2D sprite/scene rendering on WebGL/WebGPU; v8 line.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Sprites, filters, particles, asset loading.
- **Usage domain:** 2D games, interactive canvases, data-dense 2D viz.
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** 2D-focused; imperative.
- **Related resources:** p5.js (A14.5).
- **Sources:** Secondary graphics roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A14.4 — Babylon.js
- **Canonical identity:** `BabylonJS/Babylon.js` (npm: `@babylonjs/core`)
- **Category:** 3D game/graphics engine (WebGL/WebGPU)
- **Type:** Framework/engine
- **Official URL:** https://www.babylonjs.com · https://github.com/BabylonJS/Babylon.js (URL from public knowledge; not opened this session)
- **Description:** Microsoft-backed full 3D engine: physics, audio, GUI, XR; more batteries-included than Three.js.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Engine features incl. XR and physics integrations.
- **Usage domain:** 3D games/apps needing engine features.
- **Integration method:** npm modular packages.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Apache-2.0 (per public knowledge; not re-verified).
- **Limitations:** Heavier and more opinionated than Three.js.
- **Related resources:** Three.js (A14.1).
- **Sources:** Secondary graphics roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### A14.5 — p5.js
- **Canonical identity:** `processing/p5.js` (npm: `p5`)
- **Category:** Creative coding library (2D/3D sketching)
- **Type:** Library
- **Official URL:** https://p5js.org · https://github.com/processing/p5.js (URL from public knowledge; not opened this session)
- **Description:** Processing's JS port; beginner-friendly creative coding, 2D + WEBGL modes.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Drawing primitives, interaction, WEBGL 3D.
- **Usage domain:** Creative coding, education, generative art.
- **Integration method:** npm/CDN.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** LGPL-2.1 (per public knowledge; not re-verified — note copyleft nuance).
- **Limitations:** Not a production app framework; LGPL licensing nuance.
- **Related resources:** PixiJS (A14.3).
- **Sources:** Secondary graphics roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified (license needs check)

## A15. Real-time interfaces

### A15.1 — Socket.IO
- **Canonical identity:** `socketio/socket.io` (npm: `socket.io`)
- **Category:** Real-time bidirectional communication
- **Type:** Library (client + server)
- **Official URL:** https://socket.io · https://github.com/socketio/socket.io (URL from public knowledge; not opened this session)
- **Description:** WebSocket-based real-time with fallbacks, rooms, multiplexing; client + Node server.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Events, rooms/namespaces, reconnection, binary.
- **Usage domain:** Chat, live dashboards, multiplayer, notifications.
- **Integration method:** npm (client + server).
- **Dependencies:** ws/engine.io. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Needs server component; consider native WebSocket/SSE/EventSource for simple cases.
- **Related resources:** htmx SSE/WebSocket extensions (A1.9), PartyTown (below, script offloading — different concern).
- **Sources:** Secondary real-time roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A15.2 — PartyTown
- **Canonical identity:** `QwikDev/partytown` (npm: `@builder.io/partytown`); Astro integration `@astrojs/partytown` seen in withastro/astro README (inspected 2026-10-10)
- **Category:** Third-party script offloading to web worker
- **Type:** Library (actual category: performance tool, not UI framework)
- **Official URL:** https://partytown.qwik.dev · https://github.com/QwikDev/partytown (URL from public knowledge; not opened this session)
- **Description:** Relocates third-party scripts into a web worker to unblock main thread; Astro ships an official integration.
- **Contents inspected:** `@astrojs/partytown` integration confirmed in withastro/astro README package directory (2026-10-10). Core repo not opened.
- **Actual capabilities:** Worker-based script sandboxing with DOM proxying.
- **Usage domain:** Analytics/ads-heavy pages.
- **Integration method:** npm; framework integrations.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Not all scripts are worker-compatible.
- **Related resources:** Astro (A2.4).
- **Sources:** https://github.com/withastro/astro (package directory listing, inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

## A16. Accessibility resources

### A16.1 — React Aria / React Aria Components
Cross-reference: B5.3. Adobe's hooks + components: deepest WAI-ARIA conformance, 30+ locales, RTL, multiple calendar systems, accessible drag-and-drop; ~50+ components; Apache-2.0. Partially verified (via Untitled UI comparison + skill docs, 2026-10-10).

### A16.2 — axe-core
- **Canonical identity:** `dequelabs/axe-core` (npm: `axe-core`)
- **Category:** Accessibility testing engine
- **Type:** Library/tool
- **Official URL:** https://github.com/dequelabs/axe-core (URL from public knowledge; not opened this session)
- **Description:** Automated a11y rule engine; powers Lighthouse a11y audits, jest-axe, Storybook a11y addon, eslint-plugin-jsx-a11y-adjacent flows.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** ~90+ WCAG rules, integrates with test runners.
- **Usage domain:** CI a11y testing, component audits.
- **Integration method:** npm; `@axe-core/react`, `jest-axe`, Storybook addon.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MPL-2.0 (per public knowledge; not re-verified).
- **Limitations:** Automated checks catch ~30–50% of issues; manual testing still needed.
- **Related resources:** Storybook a11y addon (B16.1), eslint-plugin-jsx-a11y (A16.3).
- **Sources:** Secondary a11y roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### A16.3 — eslint-plugin-jsx-a11y
- **Canonical identity:** `jsx-eslint/eslint-plugin-jsx-a11y` (npm: `eslint-plugin-jsx-a11y`)
- **Category:** Static a11y linting for JSX
- **Type:** ESLint plugin
- **Official URL:** https://github.com/jsx-eslint/eslint-plugin-jsx-a11y (URL from public knowledge; not opened this session)
- **Description:** Lint rules for accessible JSX (alt text, roles, keyboard handlers, etc.).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** ~30+ rules.
- **Usage domain:** React lint pipelines.
- **Integration method:** npm ESLint plugin.
- **Dependencies:** ESLint. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Static only.
- **Related resources:** axe-core (A16.2).
- **Sources:** Secondary a11y roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

---

# PART B — STYLING, UI PRIMITIVES & COMPONENT SYSTEMS

## B1. CSS frameworks (utility-first & class-based)

### B1.1 — Tailwind CSS
- **Canonical identity:** `tailwindlabs/tailwindcss` (npm: `tailwindcss`)
- **Category:** Utility-first CSS framework
- **Type:** Framework (build-time CSS engine)
- **Official URL:** https://tailwindcss.com · https://github.com/tailwindlabs/tailwindcss
- **Description:** Utility-first CSS for rapid custom UI; v4 line is a Rust-based engine (`crates/` in repo), CSS-first config via `@theme`, native Vite plugin; zero client runtime.
- **Contents inspected:** GitHub repo root, README.md, repo metadata (2026-10-10). `crates/`, `packages/`, `integrations/` present; no AGENTS.md/skill dirs seen.
- **Actual capabilities:** On-demand utility generation, variants, `@theme` design tokens in CSS, container queries, typography/forms plugins (separate packages).
- **Usage domain:** Default styling layer for most new web apps; required by shadcn/ui.
- **Integration method:** npm (`@tailwindcss/vite` plugin or PostCSS); CDN Play for prototypes.
- **Dependencies:** Build tooling. **Availability:** Open source, npm.
- **Maintenance:** Active — 97,812 stars, 6,852 commits, 307 releases.
- **License:** MIT.
- **Limitations:** Utility-class verbosity; needs discipline/tokens to avoid "beige" sameness; v4 migration from v3 config.
- **Related resources:** UnoCSS (B1.5), Panda CSS (B1.6), daisyUI (B8.1); agent note: `tailwindcss-animate`/`tw-animate-css` (B13.1).
- **Sources:** https://github.com/tailwindlabs/tailwindcss (inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified

### B1.2 — Bootstrap
- **Canonical identity:** `twbs/bootstrap` (npm: `bootstrap`)
- **Category:** Class-based CSS framework + JS plugins
- **Type:** Framework
- **Official URL:** https://getbootstrap.com (URL from public knowledge; not opened this session)
- **Description:** The classic component-class framework (grid, buttons, modals…); v5 line; Bootstrap Icons separate MIT set.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Layout grid, components, utilities, JS plugins.
- **Usage domain:** Rapid admin/prototype UI; legacy maintenance.
- **Integration method:** npm/CDN.
- **Dependencies:** None (v5 dropped jQuery). **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Opinionated look ("Bootstrap look"); heavier than utility-first for custom design.
- **Related resources:** Bootstrap Icons (B10.9).
- **Sources:** Secondary CSS framework roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B1.3 — Bulma
- **Canonical identity:** `jgthms/bulma` (npm: `bulma`)
- **Category:** Class-based CSS framework (Flexbox, no JS)
- **Type:** Framework
- **Official URL:** https://bulma.io (URL from public knowledge; not opened this session)
- **Description:** Pure-CSS framework, readable class names, no JS.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Grid, components, modifiers.
- **Usage domain:** Simple sites wanting clean CSS-only components.
- **Integration method:** npm/CDN.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** No JS behaviors; smaller ecosystem.
- **Related resources:** Pico.css (B1.4).
- **Sources:** Secondary CSS framework roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B1.4 — Pico.css
- **Canonical identity:** `picocss/pico` (npm: `@picocss/pico`)
- **Category:** Minimal classless-ish CSS framework
- **Type:** Framework
- **Official URL:** https://picocss.com (URL from public knowledge; not opened this session)
- **Description:** Semantic-HTML styling with minimal classes; tiny footprint; dark mode built in.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Elegant defaults for native elements + optional components.
- **Usage domain:** Docs, prototypes, class-averse projects.
- **Integration method:** npm/CDN.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Limited component depth.
- **Related resources:** Open Props (B1.7).
- **Sources:** Secondary CSS framework roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B1.5 — UnoCSS
- **Canonical identity:** `unocss/unocss` (npm: `unocss`)
- **Category:** Utility-first CSS engine (atomic, on-demand)
- **Type:** Framework/engine
- **Official URL:** https://unocss.dev · https://github.com/unocss/unocss (URL from public knowledge; not opened this session)
- **Description:** Instant on-demand atomic CSS with presets (incl. Tailwind/Windi-compatible); attributify mode; faster than WindiCSS lineage.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Presets, transformers, variants; framework-agnostic.
- **Usage domain:** Utility-first styling with custom engine needs.
- **Integration method:** npm Vite/Webpack plugins.
- **Dependencies:** Build tooling. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Smaller community/preset ecosystem than Tailwind.
- **Related resources:** Tailwind CSS (B1.1); WindiCSS (historical, archived — not catalogued in depth).
- **Sources:** Secondary CSS-engine roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B1.6 — Panda CSS
- **Canonical identity:** `chakra-ui/panda` (npm: `@pandacss/dev`)
- **Category:** Utility-first CSS-in-JS ergonomics → build-time static CSS
- **Type:** Build-time styling engine
- **Official URL:** https://panda-css.com · https://github.com/chakra-ui/panda (URL from public knowledge; not opened this session)
- **Description:** Write styles in JS/TS (`css()`, `cva` recipes, patterns); extracts to static CSS at build; type-safe tokens; v2 removed tagged-template styling; Chakra's styling roadmap target. Ships `@pandacss/mcp` (MCP server exposing live tokens/recipes/patterns) and `@pandacss/eslint-plugin`; agent skill exists (`graphieros/panda` skills/panda-css/SKILL.md).
- **Contents inspected:** Not inspected directly this session; agent-facing surface verified via skill doc.
- **Actual capabilities:** Tokens, recipes (CVA), patterns, conditions, JSX style props.
- **Usage domain:** Type-safe design-system styling; Chakra v3+ styling layer.
- **Integration method:** npm; `panda codegen`/`panda dev`; PostCSS.
- **Dependencies:** Build tooling. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Codegen step; extraction requires static values (dynamic recipes need `recipe_variant_dynamic` care per skill doc).
- **Related resources:** vanilla-extract (B2.3), Chakra UI (B7.4); agent note: `@pandacss/mcp` for agent token discovery.
- **Sources:** https://github.com/graphieros/panda/blob/HEAD/skills/panda-css/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### B1.7 — Open Props
- **Canonical identity:** `argyleink/open-props` (npm: `open-props`)
- **Category:** CSS custom-property design tokens
- **Type:** Token set (no build step)
- **Official URL:** https://open-props.style · https://github.com/argyleink/open-props (URL from public knowledge; not opened this session)
- **Description:** Ready-made CSS variables (colors, spacing, shadows, animations) + optional normalize; framework-agnostic.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Token variables, OKLCH palettes.
- **Usage domain:** Token foundation for custom CSS.
- **Integration method:** npm/CDN import.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Tokens only — no components.
- **Related resources:** Style Dictionary (B4.1), Radix Colors (B4.3).
- **Sources:** Secondary token roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## B2. CSS-in-JS & build-time styling

### B2.1 — styled-components
- **Canonical identity:** `styled-components/styled-components` (npm: `styled-components`)
- **Category:** CSS-in-JS — runtime tagged-template components
- **Type:** Library
- **Official URL:** https://styled-components.com · https://github.com/styled-components/styled-components (URL from public knowledge; not opened this session)
- **Description:** The original popular CSS-in-JS (`styled.button\`\``); one secondary research report states it is in **maintenance mode as of 2025-03-17**, with its own maintainer recommending against it for new projects.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Scoped component styles, theming, SSR style registry.
- **Usage domain:** Legacy React codebases.
- **Integration method:** npm; Next.js `compiler.styledComponents` option.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Maintenance mode per secondary source (2025-03-17) — Partially verified (needs primary confirmation).
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Runtime cost; RSC friction; not recommended for new projects per maintainer (secondary claim).
- **Related resources:** Emotion (B2.2).
- **Sources:** https://github.com/niceprototypes/nice-manifest/blob/HEAD/reports/research/token-emit-competitive-analysis.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified (maintenance-mode claim needs primary check)

### B2.2 — Emotion
- **Canonical identity:** `emotion-js/emotion` (npm: `@emotion/react`, `@emotion/css`, `@emotion/styled`)
- **Category:** CSS-in-JS — performant, flexible
- **Type:** Library
- **Official URL:** https://emotion.sh · https://github.com/emotion-js/emotion (URL from public knowledge; not opened this session)
- **Description:** Widely used CSS-in-JS (MUI v5's engine); css prop, styled API; supports static extraction.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Runtime injection, labels, theming, SSR.
- **Usage domain:** MUI apps; legacy CSS-in-JS codebases.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Runtime cost; RSC friction; industry converging on static extraction.
- **Related resources:** styled-components (B2.1), Pigment CSS (B2.5).
- **Sources:** https://dev.to/uicoded/css-in-js-pros-and-cons-35ll (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B2.3 — vanilla-extract
- **Canonical identity:** `vanilla-extract-css/vanilla-extract` (npm: `@vanilla-extract/css`)
- **Category:** Zero-runtime stylesheets in TypeScript
- **Type:** Build-time library
- **Official URL:** https://vanilla-extract.style · https://github.com/vanilla-extract-css/vanilla-extract (URL from public knowledge; not opened this session)
- **Description:** Type-safe, locally scoped classes/variables/themes in TS; generates static CSS at build time.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** `style()`, themes/contracts, sprinkles, recipes.
- **Usage domain:** Type-safe static styling.
- **Integration method:** npm + bundler plugin.
- **Dependencies:** Build tooling. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Build integration required; dynamic styles need CSS vars.
- **Related resources:** Panda CSS (B1.6), Linaria (B2.4).
- **Sources:** https://webcodingcenter.com/next.js/CSS-in-JS.html (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B2.4 — Linaria
- **Canonical identity:** `callstack/linaria` (npm: `@linaria/core`, `@linaria/react`)
- **Category:** Zero-runtime CSS-in-JS (styled-like syntax, extracts to CSS)
- **Type:** Build-time library
- **Official URL:** https://linaria.dev · https://github.com/callstack/linaria (URL from public knowledge; not opened this session)
- **Description:** styled-components-like syntax with zero runtime; extracts CSS at build.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** `styled`, `css` with static extraction.
- **Usage domain:** Teams wanting styled-API without runtime cost (e.g., Airbnb migration story per secondary).
- **Integration method:** npm + bundler.
- **Dependencies:** Build tooling. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Dynamic values limited to CSS vars; build complexity.
- **Related resources:** vanilla-extract (B2.3).
- **Sources:** https://dev.to/hypeddev/the-react-core-team-finally-have-opinions-about-css-16f0 (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B2.5 — Pigment CSS
- **Canonical identity:** `mui/pigment-css` (npm: `@pigment-css/react`)
- **Category:** Zero-runtime CSS-in-JS from MUI team (static extraction)
- **Type:** Build-time library
- **Official URL:** https://github.com/mui/pigment-css (URL from public knowledge; not opened this session)
- **Description:** MUI's static-extraction styling (benchmarks cited in secondary: −20% First-Load JS, −25% TBT vs runtime emotion); MUI's forward path from runtime CSS-in-JS.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** `styled`, `css`, `sx`-like APIs compiled away.
- **Usage domain:** MUI ecosystem moving off runtime CSS-in-JS.
- **Integration method:** npm + bundler.
- **Dependencies:** Build tooling. **Availability:** Open source.
- **Maintenance:** Active (MUI org). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Newer; MUI-ecosystem-centric.
- **Related resources:** Emotion (B2.2), MUI (B7.1).
- **Sources:** https://github.com/niceprototypes/nice-manifest/blob/HEAD/reports/research/token-emit-competitive-analysis.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B2.6 — Stitches (historical)
- **Canonical identity:** `stitchesjs/stitches` (npm: `@stitches/react`)
- **Category:** CSS-in-JS (near-zero runtime) — ARCHIVED/UNMAINTAINED
- **Type:** Library
- **Official URL:** https://github.com/stitchesjs/stitches (URL from public knowledge; not opened this session)
- **Description:** Near-zero-runtime CSS-in-JS with variants API; project ended (maintainers moved on); do not adopt.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Historical.
- **Usage domain:** Legacy only.
- **Integration method:** npm (not recommended).
- **Dependencies:** Not verified. **Availability:** Open source.
- **Maintenance:** Ended per public knowledge. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Unmaintained.
- **Related resources:** Panda CSS (B1.6, variant-recipe successor concept).
- **Sources:** Secondary CSS-in-JS roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Historical

## B3/B4. Design tokens & theming primitives

### B4.1 — Style Dictionary
- **Canonical identity:** `amzn/style-dictionary` (npm: `style-dictionary`)
- **Category:** Design-token build pipeline (Amazon)
- **Type:** Tool/library
- **Official URL:** https://amzn.github.io/style-dictionary · https://github.com/amzn/style-dictionary (URL from public knowledge; not opened this session)
- **Description:** Transforms W3C-format design tokens into platform outputs (CSS vars, iOS, Android, JS).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Token transforms, formats, multi-platform output.
- **Usage domain:** Multi-platform design systems.
- **Integration method:** npm; config file.
- **Dependencies:** Node. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Apache-2.0 (per public knowledge; not re-verified).
- **Limitations:** Pipeline config complexity.
- **Related resources:** Tokens Studio (B4.2).
- **Sources:** Secondary token roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B4.2 — Tokens Studio (for Figma)
- **Canonical identity:** Tokens Studio (Figma plugin + `tokens-studio-for-figma` repo)
- **Category:** Design-token authoring/management (Figma plugin)
- **Type:** Tool (plugin; some open-source components)
- **Official URL:** https://tokens.studio (URL from public knowledge; not opened this session)
- **Description:** Figma plugin for creating/managing W3C design tokens; syncs to GitHub/JSON; feeds Style Dictionary pipelines.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Token sets, themes, Git sync.
- **Usage domain:** Designer→developer token handoff.
- **Integration method:** Figma plugin.
- **Dependencies:** Figma. **Availability:** Freemium SaaS + plugin.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Mixed (plugin partly open; verify per component).
- **Limitations:** Figma-coupled; SaaS tiers for teams.
- **Related resources:** Style Dictionary (B4.1), Figma Dev Mode MCP (B14.7 note).
- **Sources:** Secondary token roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified

### B4.3 — Radix Colors
- **Canonical identity:** `radix-ui/colors` (npm: `@radix-ui/colors`)
- **Category:** Accessible color system (12-step scales, OKLCH-era)
- **Type:** Token set (CSS/JS)
- **Official URL:** https://www.radix-ui.com/colors · https://github.com/radix-ui/colors (URL from public knowledge; not opened this session)
- **Description:** 30 color families × 12 steps designed for UI (incl. dark-mode pairs, alpha variants); widely reused as token base.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** CSS custom properties, P3 wide-gamut variants.
- **Usage domain:** Token palettes for design systems.
- **Integration method:** npm import.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Palette-only.
- **Related resources:** Open Props (B1.7), Tailwind `@theme` (B1.1).
- **Sources:** https://www.untitledui.com/blog/untitled-ui-vs-react-aria (comparison context, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## B5. Accessible component primitives (headless)

### B5.1 — Radix Primitives
- **Canonical identity:** `radix-ui/primitives` (npm: `@radix-ui/react-*` / umbrella `radix-ui`)
- **Category:** Unstyled accessible React primitives
- **Type:** Library (per-part packages)
- **Official URL:** https://www.radix-ui.com/primitives · https://github.com/radix-ui/primitives (URL from public knowledge; not opened this session)
- **Description:** ~30-34 unstyled primitives (Dialog, Popover, Select, Tabs, Toast…) with `asChild` composition; WAI-ARIA aligned; the layer shadcn/ui was built on (default until shadcn switched default to Base UI in July 2026 per secondary).
- **Contents inspected:** Not inspected directly this session; corroborated by 4+ secondary sources incl. a detailed 2026 comparison table.
- **Actual capabilities:** Focus management, layering/dismissal, roving tabindex, ARIA relationships.
- **Usage domain:** React design systems owning their styles.
- **Integration method:** npm per-part or umbrella.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Maintained but slowing (WorkOS acquisition context per secondary); shadcn still supports it, "not deprecated" per secondary. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** React-only; team moved on to Base UI — new projects pointed there.
- **Related resources:** Base UI (B5.2), shadcn/ui (B6.1), Radix Themes (B7.6), Radix Icons (B10.8).
- **Sources:** https://www.untitledui.com/blog/untitled-ui-vs-react-aria (accessed 2026-10-10); https://github.com/amirkabiri/qalam/blob/HEAD/docs/uikit-research.md (comparison table, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### B5.2 — Base UI
- **Canonical identity:** `mui/base-ui` (npm: `@base-ui-components/react`)
- **Category:** Unstyled accessible React primitives (Radix successor lineage)
- **Type:** Library (single package)
- **Official URL:** https://base-ui.com · https://github.com/mui/base-ui (URL from public knowledge; not opened this session)
- **Description:** Built by people from Radix/MUI/Floating UI teams; 37 components + 4 utilities at v1.0 (Dec 2025 per secondary); render-prop pattern instead of `asChild`; shadcn/ui's default primitive layer since July 2026; broader component set than Radix; gaps: no calendar/date picker/table/tree, no localized strings (per secondary).
- **Contents inspected:** Not inspected directly this session; corroborated by multiple secondary sources.
- **Actual capabilities:** Unstyled primitives with `data-*` state attributes, CSS keyframe vars.
- **Usage domain:** New React design systems wanting full style control.
- **Integration method:** npm single package.
- **Dependencies:** React; 5 runtime deps (per secondary). **Availability:** Open source.
- **Maintenance:** Active, fast-moving. Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** React-only; coverage gaps listed above.
- **Related resources:** Radix Primitives (B5.1), shadcn/ui (B6.1); agent note: shadcn registry supports it as a base.
- **Sources:** https://www.untitledui.com/blog/untitled-ui-vs-react-aria (accessed 2026-10-10); https://github.com/eneryleen/ai-web-design-codex/blob/HEAD/04-libraries-and-tools/component-libraries-headless.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### B5.3 — React Aria Components (Adobe)
- **Canonical identity:** `adobe/react-spectrum` monorepo (npm: `react-aria-components`, `react-aria`)
- **Category:** Accessible React components + hooks (behavior + a11y + i18n)
- **Type:** Library
- **Official URL:** https://react-spectrum.adobe.com/react-aria · https://github.com/adobe/react-spectrum (URL from public knowledge; not opened this session)
- **Description:** 50+ unstyled components (incl. 6 date components, 7 color components, Table, Tree, GridList, TagGroup, accessible drag-and-drop); deepest WAI-ARIA conformance; 30+ locales; RTL automatic from locale; multiple calendar systems; ~3.11M weekly downloads (per secondary); Apache-2.0.
- **Contents inspected:** Not inspected directly this session; corroborated by detailed 2026 comparison.
- **Actual capabilities:** Behavior + a11y + i18n; data-attr styling; Tailwind plugin examples.
- **Usage domain:** Accessibility-critical/government/i18n-heavy React apps; enterprise design systems.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Active (Adobe). Partially verified.
- **License:** Apache-2.0 (per secondary; not re-verified).
- **Limitations:** React-only; larger bundle (~268KB min+gz whole pkg pre-tree-shake per secondary).
- **Related resources:** Radix (B5.1), Base UI (B5.2), shadcn/ui (B6.1, supports React Aria as base).
- **Sources:** https://www.untitledui.com/blog/untitled-ui-vs-react-aria (accessed 2026-10-10); https://github.com/amirkabiri/qalam/blob/HEAD/docs/uikit-research.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### B5.4 — Ark UI
- **Canonical identity:** `chakra-ui/ark` (npm: `@ark-ui/react`, `@ark-ui/vue`, `@ark-ui/solid`, `@ark-ui/svelte`)
- **Category:** Headless accessible components — multi-framework (Zag.js state machines)
- **Type:** Library
- **Official URL:** https://ark-ui.com · https://github.com/chakra-ui/ark (URL from public knowledge; not opened this session)
- **Description:** 45+ components built on Zag.js state machines; single API across React/Vue/Solid/Svelte; Chakra UI v3 is built on Ark UI; MIT.
- **Contents inspected:** Not inspected directly this session; corroborated by multiple secondary sources.
- **Actual capabilities:** Combobox, date picker, color picker, carousel, etc.; unstyled parts + machine context.
- **Usage domain:** Non-React projects, multi-framework teams, complex widgets.
- **Integration method:** npm per-framework package.
- **Dependencies:** @zag-js. **Availability:** Open source.
- **Maintenance:** Active (Chakra team). Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** Larger bundle (~290KB min+gz whole pkg pre-tree-shake per secondary).
- **Related resources:** Zag.js (B5.10), Chakra UI (B7.4), Kobalte (B5.8, Solid).
- **Sources:** https://www.untitledui.com/blog/untitled-ui-vs-react-aria (accessed 2026-10-10); https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/ui-primitives.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### B5.5 — Headless UI (Tailwind Labs)
- **Canonical identity:** `tailwindlabs/headlessui` (npm: `@headlessui/react`, `@headlessui/vue`)
- **Category:** Unstyled accessible primitives (React + Vue)
- **Type:** Library
- **Official URL:** https://headlessui.com · https://github.com/tailwindlabs/headlessui (URL from public knowledge; not opened this session)
- **Description:** Tailwind Labs' headless components; ~16 components; small surface; good for simple needs.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Menu, Dialog, Disclosure, Combobox, etc.
- **Usage domain:** Tailwind projects not using shadcn/Radix; Vue support matters.
- **Integration method:** npm.
- **Dependencies:** React or Vue. **Availability:** Open source.
- **Maintenance:** Slow — one 2026 source reports no release/commit since April 2026; Vue package on v1.7.23 since Sep 2024. Partially verified (needs primary check).
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** Small surface; maintenance pace concern.
- **Related resources:** Radix (B5.1).
- **Sources:** https://www.untitledui.com/blog/untitled-ui-vs-react-aria (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified (maintenance pace needs primary check)

### B5.6 — Ariakit
- **Canonical identity:** `ariakit/ariakit` (npm: `ariakit`)
- **Category:** Unstyled React primitives + hooks (a11y-focused)
- **Type:** Library
- **Official URL:** https://ariakit.org · https://github.com/ariakit/ariakit (URL from public knowledge; not opened this session)
- **Description:** Accessible primitives with strong coverage and many real examples; good for comboboxes, menus, dialogs, command menus, search/filter UIs.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Composite widgets, focus management.
- **Usage domain:** React apps needing combobox/command-menu depth outside shadcn patterns.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** React-only; smaller community than Radix.
- **Related resources:** Radix (B5.1), Base UI (B5.2).
- **Sources:** https://github.com/helix98/ui-forager-skill/blob/HEAD/references/libraries.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B5.7 — Melt UI / Bits UI (Svelte)
- **Canonical identity:** `melt-ui/melt-ui` (npm: `melt`); `huntabyte/bits-ui` (npm: `bits-ui`)
- **Category:** Headless accessible components for Svelte
- **Type:** Library
- **Official URL:** https://www.melt-ui.com · https://github.com/melt-ui/melt-ui (URLs from public knowledge; not opened this session)
- **Description:** Melt UI = headless builders for Svelte; Bits UI = styled-adjacent layer over Melt (shadcn-svelte lineage).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Headless builders (Melt); pre-styled components (Bits).
- **Usage domain:** Svelte design systems.
- **Integration method:** npm.
- **Dependencies:** Svelte. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Svelte-only.
- **Related resources:** Svelte (A1.3), shadcn-svelte (B6.x note).
- **Sources:** https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/ui-primitives.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B5.8 — Kobalte (Solid)
- **Canonical identity:** `kobaltedev/kobalte` (npm: `@kobalte/core`)
- **Category:** Unstyled accessible UI toolkit for Solid
- **Type:** Library
- **Official URL:** https://kobalte.dev · https://github.com/kobaltedev/kobalte (URL from public knowledge; not opened this session)
- **Description:** Solid's headless primitive set (Radix-like API for Solid).
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Accessible primitives for Solid.
- **Usage domain:** Solid design systems.
- **Integration method:** npm.
- **Dependencies:** Solid. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Solid-only.
- **Related resources:** SolidJS (A1.4), Ark UI Solid (B5.4).
- **Sources:** Secondary headless roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified

### B5.9 — Floating UI
- **Canonical identity:** `floating-ui/floating-ui` (npm: `@floating-ui/react`, `@floating-ui/dom`)
- **Category:** Positioning engine (tooltips, popovers, dropdowns)
- **Type:** Library
- **Official URL:** https://floating-ui.com · https://github.com/floating-ui/floating-ui (URL from public knowledge; not opened this session)
- **Description:** The positioning engine under most headless libraries; use directly for bespoke anchored surfaces.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Collision-aware placement, middleware (flip, shift, arrow), auto-update.
- **Usage domain:** Custom overlays/anchored UI.
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Positioning only — no component behavior.
- **Related resources:** Radix (B5.1), Base UI (B5.2).
- **Sources:** https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/ui-primitives.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B5.10 — Zag.js
- **Canonical identity:** `chakra-ui/zag` (npm: `@zag-js/*`)
- **Category:** Framework-agnostic state machines for UI components
- **Type:** Library
- **Official URL:** https://zagjs.com · https://github.com/chakra-ui/zag (URL from public knowledge; not opened this session)
- **Description:** Raw state machines powering Ark UI; use when you want no framework opinion.
- **Contents inspected:** Not inspected directly this session.
- **Actual capabilities:** Machine definitions per component pattern.
- **Usage domain:** Custom headless component systems.
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active (powers Ark). Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Low-level; you build rendering.
- **Related resources:** Ark UI (B5.4), XState (A6.5).
- **Sources:** https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/ui-primitives.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## B6. Component registries (shadcn-compatible distribution model)

> Model note: shadcn/ui is NOT a package — it is a CLI + registry schema (`components.json`, `registries.json`, `/r/{name}.json` remote indexes) that copies versioned source into your repo. Third-party registries plug in under `registries` with namespaces (`shadcn add @magicui/shimmer-button`). Agent discovery: **shadcn MCP server** (official, free, no API key), remote registry indexes (`https://ui.shadcn.com/r/index.json` et al.), `21st.dev` MCP.

### B6.1 — shadcn/ui
- **Canonical identity:** `shadcn-ui/ui` (npm CLI: `shadcn`)
- **Category:** Component registry / distribution system (actual category: registry + CLI, NOT a library)
- **Type:** Registry + CLI that copies source into the consumer repo
- **Official URL:** https://ui.shadcn.com · https://github.com/shadcn-ui/ui
- **Description:** "Composable, accessible components with thoughtful defaults… Build your own component library." 50+ components on Radix/Base UI/React Aria primitives + Tailwind; theming via CSS vars; charts/docs patterns; repo contains `skills/` dir, `.claude/` dir (agent-facing).
- **Contents inspected:** GitHub repo root, README.md, repo metadata (2026-10-10). Root: `apps/v4`, `packages/`, `templates/`, `skills/`, `.claude/`, `.cursor-plugin/`; topics include `base-ui`, `radix-ui`, `react-aria`, `ai`, `gen-ui`.
- **Actual capabilities:** CLI add/install, namespaced third-party registries, MCP server for discovery/install, theme CSS-var system.
- **Usage domain:** Baseline for React SaaS/dashboards/admin; default stack shadcn + Tailwind v4.
- **Integration method:** `pnpm dlx shadcn@latest add <component>` / `mcp init`.
- **Dependencies:** Tailwind, primitive layer (Radix/Base UI/React Aria). **Availability:** Open source.
- **Maintenance:** Active — 125,200 stars, 2,545 commits, 131 releases; not archived.
- **License:** MIT.
- **Limitations:** You own the copied code (bugs/upstream fixes are yours); "beige problem" — defaults look identical everywhere, customize tokens.
- **Related resources:** Base UI (B5.2), Radix (B5.1), Magic UI (B6.2), Kibo UI (B6.6); DEDUP note: shadcn MCP already catalogued (cross-ref only).
- **Sources:** https://github.com/shadcn-ui/ui (inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified

### B6.2 — Magic UI
- **Canonical identity:** Magic UI (registry at magicui.design)
- **Category:** Animated component registry (shadcn-compatible)
- **Type:** Registry (remote index `https://magicui.design/r/index.json`)
- **Official URL:** https://magicui.design (URL from search results; site not opened this session)
- **Description:** 200+ animated items (marquees, bento grids, animated beam, number tickers, shimmer buttons, canvas shaders); Tailwind + Motion; install via `shadcn add "https://magicui.design/r/{name}.json"`.
- **Contents inspected:** Not inspected directly; registry index URL corroborated by uishelf discovery matrix.
- **Actual capabilities:** Animated marketing components.
- **Usage domain:** Landing-page polish alongside a shadcn base.
- **Integration method:** shadcn CLI with registry URL.
- **Dependencies:** Tailwind, Motion. **Availability:** Open registry.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per secondary license-harvest table; not re-verified).
- **Limitations:** Marketing-focused; verify animation engine per component.
- **Related resources:** shadcn/ui (B6.1), Aceternity UI (B6.3).
- **Sources:** https://github.com/sh20raj/uishelf (discovery matrix, accessed 2026-10-10); https://github.com/darrencasper/ai-skills-full-stack/blob/HEAD/skills/ui-registries/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B6.3 — Aceternity UI
- **Canonical identity:** Aceternity UI (registry at ui.aceternity.com)
- **Category:** Visual-effect component registry (shadcn-compatible)
- **Type:** Registry (`https://ui.aceternity.com/r/index.json`) — NO public source repo
- **Official URL:** https://ui.aceternity.com (URL from search results; site not opened this session)
- **Description:** Cinematic effects (spotlight, 3D cards/pin, lamp effect, beams, parallax); heaviest/boldest of the registries; use sparingly.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Hero/effect components.
- **Usage domain:** Marketing heroes.
- **Integration method:** shadcn CLI with registry URL.
- **Dependencies:** Tailwind, Motion. **Availability:** Hosted registry.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** ⚠️ NO license grant — no public repo, no LICENSE file; `/licence` covers Pro only (proprietary); widely assumed MIT but unsourced. Treat as all-rights-reserved for redistribution; using in your own app is the lower-risk interpretation but NOT verified legal advice.
- **Limitations:** No source repo; many components visually-only (add ARIA/keyboard); licensing ambiguity is the key limitation.
- **Related resources:** Magic UI (B6.2).
- **Sources:** https://github.com/sh20raj/uishelf (accessed 2026-10-10); https://github.com/justinfowler925/justinfowler.com/blob/HEAD/assets/cowork-skills/shine/references/ecosystem.md (license table, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium (existence) / Low (license) · **Label:** Partially verified (license: Unresolved — verify before reuse)

### B6.4 — Cult UI
- **Canonical identity:** Cult UI (registry at cult-ui.com)
- **Category:** Component registry — tactile/neumorphic/cyberpunk blocks (shadcn-compatible)
- **Type:** Registry (`https://cult-ui.com/r/index.json`)
- **Official URL:** https://cult-ui.com (URL from search results; not opened this session)
- **Description:** AI-chat/agent-surface-friendly components; Motion-based; tasteful.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** App-pattern components.
- **Usage domain:** AI chat, agent surfaces, modern app patterns.
- **Integration method:** shadcn CLI.
- **Dependencies:** Tailwind, Motion. **Availability:** Open registry.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per secondary license table; not re-verified).
- **Limitations:** Smaller catalog.
- **Related resources:** assistant-ui / AI Elements (chat threads) — mentioned in secondary, not catalogued in depth.
- **Sources:** https://github.com/sh20raj/uishelf (accessed 2026-10-10); https://github.com/darrencasper/ai-skills-full-stack/blob/HEAD/skills/ui-registries/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B6.5 — Origin UI → cosscom/coss (relicensed)
- **Canonical identity:** formerly Origin UI (originui.com); now `cosscom/coss` monorepo
- **Category:** Component registry — RELICENSED
- **Type:** Registry (actual category post-transfer: AGPL-3.0 monorepo with MIT-carved UI dirs)
- **Official URL:** https://github.com/cosscom/coss (URL from public knowledge; not opened this session)
- **Description:** Origin UI was transferred to `cosscom/coss` (Cal.com) and relicensed **AGPL-3.0**, with `apps/ui/` and `apps/origin/` carved out MIT (per 2026 license analysis).
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Input/primitive variants, micro-interactions.
- **Usage domain:** Filling gaps in shadcn coverage.
- **Integration method:** shadcn CLI / copy.
- **Dependencies:** Tailwind. **Availability:** Open (AGPL).
- **Maintenance:** Active under new org per secondary. Partially verified.
- **License:** AGPL-3.0 overall; `apps/ui/`, `apps/origin/` MIT (per secondary; not re-verified — check before embedding).
- **Limitations:** AGPL copyleft on surrounding monorepo; components dir safe per secondary.
- **Related resources:** shadcn/ui (B6.1).
- **Sources:** https://github.com/justinfowler925/justinfowler.com/blob/HEAD/assets/cowork-skills/shine/references/ecosystem.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified (license: needs primary check)

### B6.6 — Kibo UI
- **Canonical identity:** Kibo UI (registry; `kibo-ui` org)
- **Category:** Complex app-component registry (shadcn-compatible)
- **Type:** Registry
- **Official URL:** https://www.kibo-ui.com (URL from public knowledge; not opened this session)
- **Description:** Complex app components: kanban, gantt, editors, data-table patterns.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** App-level composite components.
- **Usage domain:** Complex app surfaces.
- **Integration method:** shadcn CLI.
- **Dependencies:** Tailwind, Motion. **Availability:** Open registry.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per secondary license table; not re-verified).
- **Limitations:** Newer; smaller catalog.
- **Related resources:** shadcn/ui (B6.1).
- **Sources:** https://github.com/darrencasper/ai-skills-full-stack/blob/HEAD/skills/ui-registries/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B6.7 — Animate UI
- **Canonical identity:** Animate UI (registry at animate-ui.com)
- **Category:** Animated primitive-variant registry (shadcn-compatible)
- **Type:** Registry
- **Official URL:** https://animate-ui.com (URL from public knowledge; not opened this session)
- **Description:** Animated versions of familiar primitives — swap-in upgrades for existing components.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Animated button/input/etc. variants.
- **Usage domain:** Micro-interaction upgrades.
- **Integration method:** shadcn CLI.
- **Dependencies:** Tailwind, Motion. **Availability:** Open registry.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT + Commons Clause (no resale/redistribution of the components themselves; use in products fine — per secondary license table; not re-verified).
- **Limitations:** Commons Clause restricts redistribution/harvesting.
- **Related resources:** Magic UI (B6.2).
- **Sources:** https://github.com/justinfowler925/justinfowler.com/blob/HEAD/assets/cowork-skills/shine/references/ecosystem.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B6.8 — React Bits
- **Canonical identity:** React Bits (registry at reactbits.dev)
- **Category:** Animated background/effect component registry (shadcn-compatible)
- **Type:** Registry (`https://reactbits.dev/r/index.json`)
- **Official URL:** https://reactbits.dev (URL from search results; not opened this session)
- **Description:** 44.8k★ (GitHub stars per secondary); physics text, magnetic cursor, ballpit, animated backgrounds.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Background/effect components.
- **Usage domain:** Marketing backgrounds and playful effects.
- **Integration method:** shadcn CLI.
- **Dependencies:** Tailwind, Motion. **Availability:** Open registry.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT + Commons Clause (per secondary license table; not re-verified).
- **Limitations:** Commons Clause redistribution restriction.
- **Related resources:** Magic UI (B6.2).
- **Sources:** https://github.com/sh20raj/uishelf (accessed 2026-10-10); https://github.com/justinfowler925/justinfowler.com/blob/HEAD/assets/cowork-skills/shine/references/ecosystem.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B6.9 — ReUI
- **Canonical identity:** ReUI (registry at reui.io)
- **Category:** SaaS block registry (shadcn-compatible) — freemium
- **Type:** Registry (`https://reui.io/r/index.json`) — some items gated
- **Official URL:** https://reui.io (URL from public knowledge; not opened this session)
- **Description:** SaaS hero blocks, notification banners; repo MIT but hosted registry freemium — some items return 401 "Provide your license key" (per secondary).
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Marketing/SaaS blocks.
- **Usage domain:** SaaS landing pages.
- **Integration method:** shadcn CLI; license key for gated items.
- **Dependencies:** Tailwind. **Availability:** Freemium.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Repo MIT; hosted registry freemium (per secondary; not re-verified).
- **Limitations:** Paywalled items.
- **Related resources:** Tailark (B6.10).
- **Sources:** https://github.com/justinfowler925/justinfowler.com/blob/HEAD/assets/cowork-skills/shine/references/ecosystem.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified

### B6.10 — Tailark
- **Canonical identity:** Tailark (registry at tailark.com)
- **Category:** Marketing block library (shadcn-compatible)
- **Type:** Registry
- **Official URL:** https://tailark.com (URL from public knowledge; not opened this session)
- **Description:** Marketing sections with distinct look.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Page-section blocks.
- **Usage domain:** Marketing pages.
- **Integration method:** shadcn CLI / copy.
- **Dependencies:** Tailwind. **Availability:** Open registry (per secondary).
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Not verified — Unresolved.
- **Limitations:** Unresolved license.
- **Related resources:** HyperUI (B8.2), Tailblocks (B8.3).
- **Sources:** https://github.com/darrencasper/ai-skills-full-stack/blob/HEAD/skills/ui-registries/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified (license Unresolved)

### B6.11 — 21st.dev
- **Canonical identity:** 21st.dev (marketplace + registry + MCP)
- **Category:** Community component marketplace ("npm for design engineers") — NOT a pure registry
- **Type:** Marketplace (actual category: marketplace with shadcn-registry export + AI generation + MCP)
- **Official URL:** https://21st.dev (URL from search results; not opened this session)
- **Description:** Thousands of community components/themes/templates; `21st add <user>/<slug>` installs via its shadcn registry; `21st get`/`generate` for bespoke/AI-generated code; MCP server for search+generation; needs account + token; free quota small; generation costs credits.
- **Contents inspected:** Not inspected directly; corroborated by 3+ secondary sources.
- **Actual capabilities:** Search, install, publish, AI-generate components matching project style.
- **Usage domain:** Largest general catalog; one-off AI-generated components.
- **Integration method:** `npx 21st@latest add`; MCP server.
- **Dependencies:** Tailwind, React. **Availability:** Freemium SaaS.
- **Maintenance:** Active. Partially verified.
- **License:** Varies per component — check each item.
- **Limitations:** Account/quota/credits; quality varies (community); distinguish registry installs (versioned) from bespoke pastes.
- **Related resources:** shadcn MCP (dedup cross-ref); uishelf (B6.12).
- **Sources:** https://github.com/darrencasper/ai-skills-full-stack/blob/HEAD/skills/ui-registries/SKILL.md (accessed 2026-10-10); https://github.com/abdulmalekalshugaa/claude-agents-fullstack/blob/HEAD/skills/shadcn-ui/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B6.12 — uishelf
- **Canonical identity:** `sh20raj/uishelf`
- **Category:** Universal React UI registry — discovery engine, compatibility resolver, installer & MCP platform (agent tool)
- **Type:** CLI tool (actual category: agent-facing discovery/install tool, not a component source itself)
- **Official URL:** https://github.com/sh20raj/uishelf (from search results; repo page not opened this session)
- **Description:** CLI (`uishelf providers list`, `uishelf libs`) + MCP platform unifying shadcn/ui, Magic UI, Aceternity, 21st.dev, React Bits, Ruixen UI, Cult UI, ReUI registries with search schema/endpoints and install commands; compatibility resolver across Tailwind v3/v4, React 19, Radix/Base UI, Motion.
- **Contents inspected:** Discovery matrix quoted in search results (2026-10-10). Repo not opened.
- **Actual capabilities:** Multi-registry search, compatibility matrix, background install.
- **Usage domain:** Coding agents discovering/installing UI across registries.
- **Integration method:** CLI / MCP.
- **Dependencies:** Node. **Availability:** Open source (per listing).
- **Maintenance:** Active (updated ~24 days ago per search). Partially verified.
- **License:** Not verified — Unresolved.
- **Limitations:** Meta-tool; component quality depends on underlying registries.
- **Related resources:** shadcn MCP (dedup), 21st.dev MCP (B6.11).
- **Sources:** https://github.com/sh20raj/uishelf (search-result excerpt, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## B7. Styled component libraries (batteries-included)

### B7.1 — MUI (Material UI)
- **Canonical identity:** `mui/material-ui` (npm: `@mui/material`)
- **Category:** Comprehensive React component library (Material Design implementation)
- **Type:** Library
- **Official URL:** https://mui.com · https://github.com/mui/material-ui
- **Description:** "Comprehensive library of React components… independent implementation of Google's Material Design"; 60+ components; theming object; MUI X extends with complex components; Joy UI (alternative design) in org.
- **Contents inspected:** GitHub repo root, README.md, repo metadata (2026-10-10). Root contains `.agents/skills`, `.claude/skills`, `skills/`, `AGENTS.md`, `CLAUDE.md` — agent-facing docs present.
- **Actual capabilities:** Full component suite, theme system, system props, data grid via MUI X.
- **Usage domain:** Enterprise React apps, Material Design products, dashboards.
- **Integration method:** npm; path imports recommended (`@mui/material/Button`) — barrel imports slow dev startup up to 6× (per secondary).
- **Dependencies:** Emotion (v5+ styling), React. **Availability:** Open source core; commercial tiers (MUI X Pro/Premium, Toolpad).
- **Maintenance:** Active — 99,151 stars, 28,804 commits, 574 releases.
- **License:** MIT (core).
- **Limitations:** Material aesthetic lock-in unless themed; Emotion runtime cost (Pigment CSS is the static future).
- **Related resources:** Base UI (B5.2, same team), Pigment CSS (B2.5), MUI X Data Grid (A9.3).
- **Sources:** https://github.com/mui/material-ui (inspected 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified

### B7.2 — Mantine
- **Canonical identity:** `mantine-ui/mantine` (npm: `@mantine/core`)
- **Category:** Full-featured React component library (100+ components)
- **Type:** Library
- **Official URL:** https://mantine.dev · https://github.com/mantine-ui/mantine (URL from public knowledge; not opened this session)
- **Description:** 100+ components, hooks library, props-based styling + overrides, notifications, forms, dates; custom CSS-in-JS with static extraction; Mantine MCP exists (per secondary skill docs).
- **Contents inspected:** Not inspected directly; corroborated by multiple secondary sources.
- **Actual capabilities:** Components + `@mantine/hooks`, spotlight, charts.
- **Usage domain:** Enterprise dashboards; rapid full-featured React UI.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Opinionated styling system.
- **Related resources:** MUI (B7.1); agent note: Mantine MCP for agent discovery.
- **Sources:** https://github.com/omernesh/openclaw-waha-plugin/blob/HEAD/.planning/research/ui-framework-research.md (accessed 2026-10-10); https://github.com/raphael-hund/raphael-skills (skill mentions Mantine MCP, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B7.3 — Ant Design
- **Canonical identity:** `ant-design/ant-design` (npm: `antd`)
- **Category:** Enterprise React UI library (70+ components)
- **Type:** Library
- **Official URL:** https://ant.design · https://github.com/ant-design/ant-design (URL from public knowledge; not opened this session)
- **Description:** Alibaba's enterprise design system; huge component coverage; v6 defaults to pure CSS-variable mode (per secondary); theme tokens.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Tables, forms, data entry/display, feedback, layouts.
- **Usage domain:** Enterprise/admin, strong in Chinese market.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Bundle weight (~500KB+ per secondary); strong aesthetic opinions.
- **Related resources:** MUI (B7.1).
- **Sources:** https://github.com/omernesh/openclaw-waha-plugin/blob/HEAD/.planning/research/ui-framework-research.md (accessed 2026-10-10); https://github.com/niceprototypes/nice-manifest/blob/HEAD/reports/research/token-emit-competitive-analysis.md (antd v6 CSS-var note, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B7.4 — Chakra UI
- **Canonical identity:** `chakra-ui/chakra-ui` (npm: `@chakra-ui/react`)
- **Category:** Accessible React component library (theme-object)
- **Type:** Library
- **Official URL:** https://chakra-ui.com · https://github.com/chakra-ui/chakra-ui (URL from public knowledge; not opened this session)
- **Description:** Style-props component library; v3 built on Ark UI; styling roadmap targets Panda CSS.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Themed components, style props.
- **Usage domain:** General-purpose React apps.
- **Integration method:** npm.
- **Dependencies:** Ark UI (v3), Emotion (v2). **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** v2→v3 migration surface; Emotion runtime in v2.
- **Related resources:** Ark UI (B5.4), Panda CSS (B1.6).
- **Sources:** https://www.untitledui.com/blog/untitled-ui-vs-react-aria (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B7.5 — HeroUI (formerly NextUI)
- **Canonical identity:** `heroui-inc/heroui` (npm: `@heroui/react`)
- **Category:** Styled React component library (Tailwind-based)
- **Type:** Library
- **Official URL:** https://www.heroui.com (URL from public knowledge; not opened this session)
- **Description:** Tailwind-based React component library (renamed from NextUI); beautiful defaults.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Themed components on Tailwind.
- **Usage domain:** Polished React marketing/app UI fast.
- **Integration method:** npm + Tailwind plugin.
- **Dependencies:** Tailwind, React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Tailwind-coupled; aesthetic opinions.
- **Related resources:** shadcn/ui (B6.1).
- **Sources:** Secondary component-library roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B7.6 — Radix Themes
- **Canonical identity:** `radix-ui/themes` (npm: `@radix-ui/themes`)
- **Category:** Styled component kit from Radix (packaged design system)
- **Type:** Library
- **Official URL:** https://www.radix-ui.com/themes · https://github.com/radix-ui/themes (URL from public knowledge; not opened this session)
- **Description:** Cohesive styled React kit with theme provider/tokens; use when you want a packaged system quickly rather than copy-owned shadcn source.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** 40+ styled components, theming tokens.
- **Usage domain:** Quick cohesive React design system.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Brings its own theme provider — avoid mixing with an established shadcn theme (per secondary).
- **Related resources:** Radix Primitives (B5.1).
- **Sources:** https://github.com/helix98/ui-forager-skill/blob/HEAD/references/libraries.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## B8. Reusable page sections & block libraries

### B8.1 — daisyUI
- **Canonical identity:** `saadeghi/daisyui` (npm: `daisyui`)
- **Category:** Tailwind component-class plugin + theme system
- **Type:** Tailwind plugin (actual category: class-based component layer + 30+ themes)
- **Official URL:** https://daisyui.com · https://github.com/saadeghi/daisyui (URL from public knowledge; not opened this session)
- **Description:** Component classes for Tailwind (`btn`, `card`, `modal`…); 30+ built-in themes; semantic color names.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Component classes, theme switching via `data-theme`.
- **Usage domain:** Fast Tailwind UI with theming.
- **Integration method:** npm Tailwind plugin.
- **Dependencies:** Tailwind. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Class-based opinions; less composable than headless.
- **Related resources:** Tailwind CSS (B1.1), next-themes (B12.1).
- **Sources:** Secondary theme-system roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B8.2 — HyperUI
- **Canonical identity:** HyperUI (hyperui.dev)
- **Category:** Copy-paste Tailwind page sections/blocks
- **Type:** Block gallery (actual category: marketing/component snippets, not a library)
- **Official URL:** https://www.hyperui.dev (URL from public knowledge; not opened this session)
- **Description:** Free Tailwind components/sections (marketing, e-commerce, application UI) to copy-paste.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Snippet gallery.
- **Usage domain:** Landing pages, marketing sections.
- **Integration method:** Copy-paste.
- **Dependencies:** Tailwind. **Availability:** Free.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Snippets, not maintained components.
- **Related resources:** Tailblocks (B8.3), Flowbite Blocks (B8.4).
- **Sources:** Secondary block-library roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B8.3 — Tailblocks
- **Canonical identity:** Tailblocks (tailblocks.cc)
- **Category:** Copy-paste Tailwind blocks
- **Type:** Block gallery
- **Official URL:** https://tailblocks.cc (URL from public knowledge; not opened this session)
- **Description:** Ready-made Tailwind blocks (by the Tailwind CSS team lineage — mertsabinov).
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Snippet gallery.
- **Usage domain:** Quick Tailwind page assembly.
- **Integration method:** Copy-paste.
- **Dependencies:** Tailwind. **Availability:** Free.
- **Maintenance:** Stable per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Snippets only.
- **Related resources:** HyperUI (B8.2).
- **Sources:** Secondary block-library roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B8.4 — Flowbite (components + blocks)
- **Canonical identity:** `themesberg/flowbite` (npm: `flowbite`, `flowbite-react`)
- **Category:** Tailwind component library + block sections
- **Type:** Library + blocks
- **Official URL:** https://flowbite.com · https://github.com/themesberg/flowbite (URL from public knowledge; not opened this session)
- **Description:** Tailwind components with JS behaviors; Flowbite Blocks section gallery; React/Svelte/Vue wrappers.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** 50+ components, blocks, Figma kit.
- **Usage domain:** Tailwind apps wanting Bootstrap-like completeness.
- **Integration method:** npm.
- **Dependencies:** Tailwind. **Availability:** Open core; Pro blocks commercial.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT core; Pro commercial (per public knowledge; not re-verified).
- **Limitations:** Pro blocks paywalled.
- **Related resources:** daisyUI (B8.1).
- **Sources:** Secondary component-library roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B8.5 — Tailwind UI (commercial)
- **Canonical identity:** Tailwind UI (tailwindui.com) — by Tailwind Labs
- **Category:** Commercial Tailwind component/section library
- **Type:** Paid product (actual category: commercial snippet library, not open source)
- **Official URL:** https://tailwindui.com (URL from public knowledge; not opened this session)
- **Description:** Official paid component kit from Tailwind Labs (500+ components, templates).
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Components, templates, AI-era additions per marketing.
- **Usage domain:** Teams buying quality Tailwind components.
- **Integration method:** Licensed copy-paste.
- **Dependencies:** Tailwind. **Availability:** Commercial.
- **Maintenance:** Active (Tailwind Labs). Partially verified.
- **License:** Commercial (per public knowledge; not re-verified).
- **Limitations:** Paid; not open source.
- **Related resources:** HyperUI (B8.2, free alternative).
- **Sources:** Secondary roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

## B9. Dashboard kits & admin frameworks

### B9.1 — Refine
- **Canonical identity:** `refinedev/refine` (npm: `@refinedev/core`)
- **Category:** React admin/dashboard meta-framework (headless, data-provider based)
- **Type:** Framework
- **Official URL:** https://refine.dev · https://github.com/refinedev/refine (URL from public knowledge; not opened this session)
- **Description:** Headless React framework for CRUD/admin: data providers (REST/GraphQL/Supabase…), auth providers, routers; UI-agnostic (MUI/AntD/shadcn integrations).
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Resources, data/auth/access-control providers, inferencer codegen.
- **Usage domain:** Internal tools, admin panels, dashboards.
- **Integration method:** npm; CLI scaffolder.
- **Dependencies:** React. **Availability:** Open source core; commercial cloud.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** CRUD-shaped; custom UX needs work.
- **Related resources:** AdminJS (B9.2), shadcn admin dashboard templates (generic).
- **Sources:** Secondary dashboard-kit roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B9.2 — AdminJS
- **Canonical identity:** `SoftwareBrothers/adminjs` (npm: `adminjs`)
- **Category:** Auto-generated admin panel (Node backend-driven)
- **Type:** Tool/framework
- **Official URL:** https://adminjs.co · https://github.com/SoftwareBrothers/adminjs (URL from public knowledge; not opened this session)
- **Description:** Generates admin UI from backend models (Mongoose/Sequelize/Prisma adapters).
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Auto CRUD UI, auth, actions.
- **Usage domain:** Quick Node admin panels.
- **Integration method:** npm (server-side).
- **Dependencies:** Node ORM adapter. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Backend-coupled; customization ceiling.
- **Related resources:** Refine (B9.1).
- **Sources:** Secondary dashboard-kit roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## B10. Icon systems

> License note (from a 2026 license guide): Lucide (ISC), Tabler/Phosphor/Heroicons/Iconoir (MIT), Material Symbols/Remix Icon (Apache-2.0), Simple Icons (CC0) are clean for commercial use without attribution. Font Awesome Free requires attribution (CC BY 4.0 on SVGs); Flaticon/Icons8 free tiers require attribution. Brand logos carry trademark constraints regardless of icon license.

### B10.1 — Lucide
- **Canonical identity:** `lucide-icons/lucide` (npm: `lucide-react`, `lucide-vue-next`, etc.)
- **Category:** Icon set — community fork of Feather
- **Type:** Icon library (SVG + framework packages)
- **Official URL:** https://lucide.dev · https://github.com/lucide-icons/lucide (URL from public knowledge; not opened this session)
- **Description:** 1,500–1,800+ ultra-consistent 24×24 stroke icons; first-party React/Vue/Svelte/Angular/Flutter packages; the safe default (and the "AI-slop default" per one 2026 skill — consider Phosphor for distinctiveness).
- **Contents inspected:** Not inspected directly; corroborated by 4+ secondary sources.
- **Actual capabilities:** Tree-shakable per-icon components; Figma assets.
- **Usage domain:** Default UI iconography.
- **Integration method:** npm framework package or raw SVG.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active. Partially verified.
- **License:** ISC (per secondary; not re-verified).
- **Limitations:** Single weight/stroke; ubiquitous look.
- **Related resources:** Phosphor (B10.3), Tabler (B10.2); agent note: `erickalfaro/ericks-design-store` bundles Lucide + skill for agent icon sourcing.
- **Sources:** https://github.com/allwin-antony/devpantry/blob/HEAD/src/data/opensource/Icons/guides/licenses_explained.md (accessed 2026-10-10); https://github.com/iah-uch/clanker-pack/blob/HEAD/plugins/ui-pack/skills/design-asset-sourcing/references/icons-and-logos.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### B10.2 — Tabler Icons
- **Canonical identity:** `tabler/tabler-icons` (npm: `@tabler/icons-react` etc.)
- **Category:** Icon set — massive stroke-based
- **Type:** Icon library
- **Official URL:** https://tabler.io/icons · https://github.com/tabler/tabler-icons (URL from public knowledge; not opened this session)
- **Description:** 5,800–6,100+ stroke icons; React/Vue/Svelte/webfont packages; best coverage of obscure glyphs.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Per-icon components, webfont, SVG sprite.
- **Usage domain:** SaaS dashboards needing broad glyph coverage.
- **Integration method:** npm or webfont.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active. Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** Stroke-only aesthetic.
- **Related resources:** Lucide (B10.1), Iconify (B10.10).
- **Sources:** https://github.com/allwin-antony/devpantry/blob/HEAD/src/data/opensource/Icons/README.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B10.3 — Phosphor Icons
- **Canonical identity:** `phosphor-icons/core` (+ `phosphor-icons/react` etc.)
- **Category:** Icon set — 6 weights (thin→fill)
- **Type:** Icon library
- **Official URL:** https://phosphoricons.com · https://github.com/phosphor-icons/core (URL from public knowledge; not opened this session)
- **Description:** 7,000–9,000+ icons in six weights (thin, light, regular, bold, fill, duotone); tree-shakable; ~1KB/icon; TypeScript-first React package.
- **Contents inspected:** Not inspected directly; corroborated by 4+ secondary sources.
- **Actual capabilities:** Weight variants as a design device; React/Vue/Svelte/Flutter packages.
- **Usage domain:** Distinctive iconography; weight variation.
- **Integration method:** npm (`@phosphor-icons/react`).
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active. Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** Filled variants don't respond to stroke-width styling.
- **Related resources:** Lucide (B10.1).
- **Sources:** https://github.com/iah-uch/clanker-pack/blob/HEAD/plugins/ui-pack/skills/design-asset-sourcing/references/icons-and-logos.md (accessed 2026-10-10); https://github.com/wealthior-group/marketplace/blob/HEAD/wealthior-frontend/skills/no-lucide-react-icons/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium-High · **Label:** Partially verified

### B10.4 — Heroicons
- **Canonical identity:** `tailwindlabs/heroicons` (npm: `@heroicons/react`, `@heroicons/vue`)
- **Category:** Icon set — handcrafted by Tailwind team
- **Type:** Icon library
- **Official URL:** https://heroicons.com · https://github.com/tailwindlabs/heroicons (URL from public knowledge; not opened this session)
- **Description:** 300–1,200+ icons (counts vary by source/date); 24px outline/solid + 20px mini (+ micro); pairs with Tailwind sizing.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** React/Vue components, Figma.
- **Usage domain:** Tailwind projects.
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Maintained. Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** Smallest catalog of the majors.
- **Related resources:** Lucide (B10.1).
- **Sources:** https://github.com/iah-uch/clanker-pack/blob/HEAD/plugins/ui-pack/skills/design-asset-sourcing/references/icons-and-logos.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B10.5 — Iconoir
- **Canonical identity:** `iconoir-icons/iconoir` (npm: `@iconoir/react` etc.)
- **Category:** Icon set — geometric, 24×24
- **Type:** Icon library
- **Official URL:** https://iconoir.com · https://github.com/iconoir-icons/iconoir (URL from public knowledge; not opened this session)
- **Description:** 1,500–1,600 pristine geometric icons; no paywalls; React/Vue/Svelte/Flutter.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Per-icon components.
- **Usage domain:** Clean geometric iconography.
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active. Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** Smaller catalog.
- **Related resources:** Lucide (B10.1).
- **Sources:** https://github.com/allwin-antony/devpantry/blob/HEAD/src/data/opensource/Icons/README.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B10.6 — Remix Icon
- **Canonical identity:** `Remix-Design/RemixIcon` (npm: `remixicon`)
- **Category:** Icon set — neutral system symbols, line + fill pairs
- **Type:** Icon library
- **Official URL:** https://remixicon.com · https://github.com/Remix-Design/RemixIcon (URL from public knowledge; not opened this session)
- **Description:** 2,800 neutral system symbols; line + fill variants; React/webfont.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Line/fill pairs.
- **Usage domain:** Enterprise-neutral iconography.
- **Integration method:** npm/webfont.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Maintained. Partially verified.
- **License:** Apache-2.0 (per secondary; not re-verified).
- **Limitations:** Less trendy aesthetic.
- **Related resources:** Material Symbols (B10.7).
- **Sources:** https://github.com/allwin-antony/devpantry/blob/HEAD/src/data/opensource/Icons/README.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B10.7 — Material Symbols (Google)
- **Canonical identity:** Google Fonts / `google/material-design-icons` variable set
- **Category:** Icon set — variable font (weight/fill/grade/optical-size axes)
- **Type:** Icon font + SVG
- **Official URL:** https://fonts.google.com/icons (URL from public knowledge; not opened this session)
- **Description:** 2,500–15,000+ (counts vary) variable icons; optical sizing; React/Vue wrappers community.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Variable axes; ligature or codepoint usage.
- **Usage domain:** Material-design products.
- **Integration method:** Font CDN / npm.
- **Dependencies:** None. **Availability:** Open.
- **Maintenance:** Active (Google). Partially verified.
- **License:** Apache-2.0 (per secondary; not re-verified).
- **Limitations:** Material aesthetic; font-based rendering quirks.
- **Related resources:** Remix Icon (B10.6).
- **Sources:** https://github.com/iah-uch/clanker-pack/blob/HEAD/plugins/ui-pack/skills/design-asset-sourcing/references/icons-and-logos.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B10.8 — Radix Icons
- **Canonical identity:** `radix-ui/icons` (npm: `@radix-ui/react-icons`)
- **Category:** Icon set — crisp 15×15 for compact UI
- **Type:** Icon library
- **Official URL:** https://www.radix-ui.com/icons · https://github.com/radix-ui/icons (URL from public knowledge; not opened this session)
- **Description:** 318 icons on a 15×15 grid; designed by WorkOS; crisp at small sizes; natural fit with Radix primitives.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** React components.
- **Usage domain:** Compact UI next to Radix/shadcn.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Maintained. Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** Small catalog; 15px grid only.
- **Related resources:** Radix Primitives (B5.1).
- **Sources:** https://github.com/iah-uch/clanker-pack/blob/HEAD/plugins/ui-pack/skills/design-asset-sourcing/references/icons-and-logos.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B10.9 — Bootstrap Icons
- **Canonical identity:** `twbs/icons` (npm: `bootstrap-icons`)
- **Category:** Icon set — 2,000+ MIT icons
- **Type:** Icon library
- **Official URL:** https://icons.getbootstrap.com · https://github.com/twbs/icons (URL from public knowledge; not opened this session)
- **Description:** 2,000+ icons; standalone (no Bootstrap needed); SVG/webfont.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** SVG sprites, webfont.
- **Usage domain:** General iconography.
- **Integration method:** npm/CDN.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Maintained. Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** No official React tree-shaken package (community wrappers).
- **Related resources:** Bootstrap (B1.2).
- **Sources:** https://github.com/iah-uch/clanker-pack/blob/HEAD/plugins/ui-pack/skills/design-asset-sourcing/references/icons-and-logos.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B10.10 — Iconify (aggregator)
- **Canonical identity:** `iconify/iconify` (npm: `@iconify/react`, data `@iconify-json/*`)
- **Category:** Icon aggregator — 200k+ icons, one API
- **Type:** Meta-library (unified access to 150+ sets incl. all above)
- **Official URL:** https://iconify.design · https://github.com/iconify/iconify (URL from public knowledge; not opened this session)
- **Description:** Single component/API serving 200,000+ icons from 150+ sets (Lucide, Tabler, Phosphor, Material, etc.); on-demand loading; offline JSON via `@iconify-json/*`.
- **Contents inspected:** Not inspected directly; referenced as aggregator in `ericks-design-store` docs.
- **Actual capabilities:** Unified `<Icon icon="lucide:home"/>` across sets; offline bundles.
- **Usage domain:** Apps needing multi-set icon access; agent tooling (`ericks-design-store` uses Iconify JSON as source of truth).
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (Iconify code; icon licenses vary per set — noted in docs).
- **Limitations:** Per-set licenses still apply; runtime API calls unless bundled.
- **Related resources:** All B10 icon sets; agent note: `erickalfaro/ericks-design-store` CLI for agent icon sourcing.
- **Sources:** https://github.com/erickalfaro/ericks-design-store (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B10.11 — Simple Icons (brand logos)
- **Canonical identity:** `simple-icons/simple-icons` (npm: `simple-icons`)
- **Category:** Brand/tech-logo SVG set
- **Type:** Icon library
- **Official URL:** https://simpleicons.org · https://github.com/simple-icons/simple-icons (URL from public knowledge; not opened this session)
- **Description:** 3,200+ vector SVGs of tech brands/dev tools/social; CC0; React/Vue/Svelte packages.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Brand SVGs with slugs, hex colors.
- **Usage domain:** "Built with" rows, integration logos.
- **Integration method:** npm.
- **Dependencies:** None. **Availability:** Open (CC0).
- **Maintenance:** Active. Partially verified.
- **License:** CC0 1.0 (per secondary; trademark law still applies to logos — not re-verified).
- **Limitations:** Logos only; trademark constraints apply.
- **Related resources:** SVGL (B10.12).
- **Sources:** https://github.com/allwin-antony/devpantry/blob/HEAD/src/data/opensource/Icons/guides/licenses_explained.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B10.12 — SVGL
- **Canonical identity:** SVGL (svgl.app; `pheralb/svgl`)
- **Category:** Brand logo SVG library
- **Type:** Gallery + API
- **Official URL:** https://svgl.app (URL from public knowledge; not opened this session)
- **Description:** Curated SVG brand logos for developers; API + Figma.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Logo SVGs, API.
- **Usage domain:** Tech brand logos in UIs.
- **Integration method:** Copy/API.
- **Dependencies:** None. **Availability:** Free.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Varies per logo (check) — Unresolved in detail.
- **Limitations:** Trademark constraints.
- **Related resources:** Simple Icons (B10.11).
- **Sources:** https://github.com/justinfowler925/justinfowler.com/blob/HEAD/assets/cowork-skills/shine/references/ecosystem.md (license table lists SVGL as clean-to-harvest, accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified

## B11. Typography resources

### B11.1 — Fontsource
- **Canonical identity:** `fontsource-org/fontsource` (npm: `@fontsource/*`)
- **Category:** Self-hostable webfont packaging
- **Type:** Font distribution (npm packages per font/weight/subset)
- **Official URL:** https://fontsource.org · https://github.com/fontsource-org/fontsource (URL from public knowledge; not opened this session)
- **Description:** npm-packaged Google Fonts (and others) for self-hosting: per-weight/subset imports, no Google CDN dependency.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** `@fontsource/inter`, variable fonts, unicode subsets.
- **Usage domain:** Privacy/performance-conscious font loading.
- **Integration method:** npm per-font package.
- **Dependencies:** Bundler. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** OFL-1.1 for fonts (varies per font; packaging MIT — per public knowledge; not re-verified).
- **Limitations:** Adds npm weight per font.
- **Related resources:** Google Fonts (B11.2).
- **Sources:** Secondary typography roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B11.2 — Google Fonts / Geist
- **Canonical identity:** Google Fonts (fonts.google.com); Vercel Geist (npm: `geist`)
- **Category:** Font distribution / typeface
- **Type:** Service + font
- **Official URL:** https://fonts.google.com · https://vercel.com/font (URLs from public knowledge; not opened this session)
- **Description:** Google Fonts: largest free font catalog (Inter, Roboto, etc.). Geist: Vercel's typeface (sans + mono), default in many AI-generated UIs.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** CDN or self-host.
- **Usage domain:** Default web typography.
- **Integration method:** `<link>` / `next/font` / npm.
- **Dependencies:** None. **Availability:** Free.
- **Maintenance:** Active. Partially verified.
- **License:** OFL-1.1 (most Google Fonts); Geist OFL (per public knowledge; not re-verified).
- **Limitations:** CDN privacy considerations (use Fontsource to self-host).
- **Related resources:** Fontsource (B11.1).
- **Sources:** Secondary typography roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

## B12. Theme systems

### B12.1 — next-themes
- **Canonical identity:** `pacocoursey/next-themes` (npm: `next-themes`)
- **Category:** Theme switching (dark/light) for Next.js/React
- **Type:** Library
- **Official URL:** https://github.com/pacocoursey/next-themes (URL from public knowledge; not opened this session)
- **Description:** `ThemeProvider` + `useTheme`; class/attribute strategy; no-flash script; system preference support.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Dark/light/system themes, forced themes per page.
- **Usage domain:** Next.js apps with shadcn-style CSS-var themes.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** React/Next-focused.
- **Related resources:** shadcn/ui theming (B6.1), daisyUI themes (B8.1).
- **Sources:** Secondary theme roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B12.2 — tweakcn (shadcn theme editor)
- **Canonical identity:** tweakcn (tweakcn.com)
- **Category:** Visual shadcn theme builder
- **Type:** Web tool (actual category: theme generator, not a library)
- **Official URL:** https://tweakcn.com (URL from public knowledge; not opened this session)
- **Description:** Visual editor generating shadcn CSS-var themes (OKLCH); copy theme CSS.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Theme preview + CSS export.
- **Usage domain:** Customizing shadcn "beige" defaults.
- **Integration method:** Copy generated CSS.
- **Dependencies:** None. **Availability:** Free tool.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Tool; output yours — not verified in detail.
- **Limitations:** shadcn-specific.
- **Related resources:** shadcn/ui (B6.1).
- **Sources:** Secondary theme roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## B13. Animation utilities (CSS-level)

### B13.1 — tailwindcss-animate / tw-animate-css
- **Canonical identity:** `jamiebuilds/tailwindcss-animate` (npm: `tailwindcss-animate`); `tw-animate-css` (v4-native)
- **Category:** Tailwind animation utilities
- **Type:** Tailwind plugin / CSS package
- **Official URL:** https://github.com/jamiebuilds/tailwindcss-animate (URL from public knowledge; not opened this session)
- **Description:** `animate-in`/`animate-out` utilities (fade/slide/zoom) for Tailwind; `tw-animate-css` is the v4-native successor using CSS-first config.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Enter/exit animation utilities.
- **Usage domain:** shadcn/Tailwind micro-animations.
- **Integration method:** npm plugin (v3) / CSS import (v4).
- **Dependencies:** Tailwind. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** CSS-only; for complex choreography use Motion/GSAP.
- **Related resources:** Motion (A13.1), Tailwind CSS (B1.1).
- **Sources:** Secondary Tailwind ecosystem roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

## B14. Design-system generators & visual builders

### B14.1 — Plasmic
- **Canonical identity:** Plasmic (plasmic.app; `plasmicapp/plasmic`)
- **Category:** Visual builder + design-system codegen (React)
- **Type:** SaaS tool + open-source runtime
- **Official URL:** https://www.plasmic.app (URL from public knowledge; not opened this session)
- **Description:** Visual page/component builder generating React code; design-system-aware; content + code integration.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Drag-drop builder, codegen to repo, CMS.
- **Usage domain:** Teams wanting visual editing on real React code.
- **Integration method:** SaaS + npm runtime.
- **Dependencies:** React. **Availability:** Freemium SaaS; runtime open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Mixed (verify per part).
- **Limitations:** Platform coupling for visual editing.
- **Related resources:** Builder.io (B14.3), Locofy (B14.2).
- **Sources:** Secondary design-to-code roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B14.2 — Locofy
- **Canonical identity:** Locofy (locofy.ai)
- **Category:** Design-to-code plugin (Figma/XD/Penpot → code)
- **Type:** Commercial tool (Figma plugin + Lightning/Classic engines)
- **Official URL:** https://www.locofy.ai (URL from search results; not opened this session)
- **Description:** Converts structured Figma designs to React/Next.js/Vue/Angular/HTML/CSS/React Native/Flutter; Lightning = one-click AI pass, Classic = step-by-step; quality proportional to design discipline; MCP for AI copilots on paid tiers; token-based pricing.
- **Contents inspected:** Not inspected directly; corroborated by 4+ secondary sources.
- **Actual capabilities:** Component detection, responsive hints, reusable component tagging.
- **Usage domain:** Figma→first-draft-code handoff.
- **Integration method:** Figma plugin; GitHub/Vercel/Netlify handoff.
- **Dependencies:** Figma. **Availability:** Commercial (free tier + trial).
- **Maintenance:** Active. Partially verified.
- **License:** Commercial (per secondary; terms not re-verified).
- **Limitations:** Messy Figma → messy code; state/data still need developers; pricing varies across listings — confirm live SKU.
- **Related resources:** Anima (B14.4), Builder.io Visual Copilot (B14.3).
- **Sources:** https://www.youtube.com/watch?v=ndyzwEVhxkU (review summary, accessed 2026-10-10); https://design-rise.com/top-ai-tools-for-ui-ux-designers-in-2026-from-prototyping-to-user-research/ (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B14.3 — Builder.io (Visual Copilot)
- **Canonical identity:** Builder.io (builder.io; `BuilderIO/builder`)
- **Category:** Visual development platform + Figma-to-code AI
- **Type:** SaaS platform (parts open source)
- **Official URL:** https://www.builder.io (URL from public knowledge; not opened this session)
- **Description:** Visual Copilot 2.0 (2026): Figma selection → React/Next/Vue/Angular/Svelte/Qwik; trained on 2M+ data points (per vendor); visual editor + enterprise CMS.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Design-to-code, visual editing, CMS, A/B.
- **Usage domain:** Design-system-aware Figma exports; marketing teams.
- **Integration method:** Figma plugin + SDKs.
- **Dependencies:** Framework SDK. **Availability:** Seat-based SaaS + free tier.
- **Maintenance:** Active. Partially verified.
- **License:** Mixed (verify per part).
- **Limitations:** Seat pricing; platform coupling.
- **Related resources:** Plasmic (B14.1), Locofy (B14.2).
- **Sources:** https://dupple.com/blog/screenshot-to-code (accessed 2026-10-10); https://securityboulevard.com/2026/06/7-design-to-code-ai-tools-for-frontend-developers/ (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B14.4 — Anima
- **Canonical identity:** Anima (animaapp.com)
- **Category:** Figma-to-code (React/HTML/Vue)
- **Type:** Commercial tool
- **Official URL:** https://www.animaapp.com (URL from public knowledge; not opened this session)
- **Description:** Figma → functional React components with prop types; follows existing component patterns; strong when team already has a React component library.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Codegen honoring design-system components.
- **Usage domain:** Designer→frontend handoff.
- **Integration method:** Figma plugin.
- **Dependencies:** Figma. **Availability:** Commercial (free tier; enterprise ~$500/mo per secondary).
- **Maintenance:** Active. Partially verified.
- **License:** Commercial (per secondary; not re-verified).
- **Limitations:** Price; output still needs review.
- **Related resources:** Locofy (B14.2).
- **Sources:** https://dupple.com/blog/screenshot-to-code (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B14.5 — Onlook
- **Canonical identity:** `onlook-dev/onlook`
- **Category:** Open-source visual editor on real React/Next.js+Tailwind code
- **Type:** Tool (Electron app; actual category: visual code editor, not a library)
- **Official URL:** https://onlook.com · https://github.com/onlook-dev/onlook (URL from public knowledge; not opened this session)
- **Description:** Visually edit a real React/Next.js + Tailwind codebase; 25,900+ GitHub stars by June 2026 (per secondary); MIT, self-hostable; free.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Click-to-edit UI writing back to source files.
- **Usage domain:** Designer-developer collaboration on real code.
- **Integration method:** Desktop app on repo.
- **Dependencies:** React/Next + Tailwind project. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per secondary; not re-verified).
- **Limitations:** React/Tailwind-only.
- **Related resources:** v0 (B15.1), Plasmic (B14.1).
- **Sources:** https://securityboulevard.com/2026/06/7-design-to-code-ai-tools-for-frontend-developers/ (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B14.6 — Puck
- **Canonical identity:** `measuredco/puck` (npm: `@measured/puck`)
- **Category:** Open-source visual page-builder SDK (React)
- **Type:** Library (drag-and-drop editor you embed)
- **Official URL:** https://puckeditor.com · https://github.com/measuredco/puck (URL from public knowledge; not opened this session)
- **Description:** Embeddable drag-and-drop page editor for React; you define components, editors get visual editing; serializes to JSON.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Editor UI, component config schema, JSON output.
- **Usage domain:** CMS-like page building inside your app.
- **Integration method:** npm.
- **Dependencies:** React. **Availability:** Open source.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** You build the component library it edits.
- **Related resources:** Plasmic (B14.1).
- **Sources:** Secondary visual-builder roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B14.7 — Figma Dev Mode MCP
- **Canonical identity:** Figma Dev Mode MCP server (Figma)
- **Category:** Design-to-code bridge for AI agents (MCP)
- **Type:** MCP server (agent tool)
- **Official URL:** https://www.figma.com/dev-mode (URL from public knowledge; not opened this session)
- **Description:** Figma's MCP server exposes designs/code to IDE agents; free during beta on Dev/Full seats (per 2026 secondary).
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Design context + code connect for agents.
- **Usage domain:** Agent-assisted Figma→code workflows.
- **Integration method:** MCP config in IDE.
- **Dependencies:** Figma seat. **Availability:** Beta.
- **Maintenance:** Active. Partially verified.
- **License:** Figma terms.
- **Limitations:** Beta; seat-gated.
- **Related resources:** Locofy MCP (B14.2), Tokens Studio (B4.2).
- **Sources:** https://securityboulevard.com/2026/06/7-design-to-code-ai-tools-for-frontend-developers/ (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified

## B15. AI screenshot/prompt-to-code tools

### B15.1 — v0 (Vercel)
- **Canonical identity:** v0 by Vercel (v0.app)
- **Category:** Prompt/screenshot-to-React UI generator
- **Type:** SaaS product (actual category: AI product, not a library)
- **Official URL:** https://v0.app (URL from search results; not opened this session)
- **Description:** Generates React + Tailwind (shadcn-style) components from text prompts, screenshots, mockups, or Figma; visual iteration editor; exports to Vercel projects/GitHub/CLI; token-based pricing (free $5 credits; Team $30/user/mo; Figma import gated to paid per secondary).
- **Contents inspected:** Not inspected directly; corroborated by 4+ secondary sources.
- **Actual capabilities:** Prompt/image→code, iteration chat, deploy.
- **Usage domain:** Greenfield UI prototyping; fast shadcn-style interfaces.
- **Integration method:** Web app + CLI export.
- **Dependencies:** None (output is React/Tailwind). **Availability:** Freemium SaaS.
- **Maintenance:** Active. Partially verified.
- **License:** Output licensing per Vercel terms (not re-verified).
- **Limitations:** Vercel/Next/React/Tailwind/shadcn-centric; generated components often need manual a11y corrections (per secondary); tokens deplete fast on iteration.
- **Related resources:** screenshot-to-code (B15.2, open-source alt), Bolt.new (B15.3).
- **Sources:** https://dupple.com/blog/screenshot-to-code (accessed 2026-10-10); https://www.scriptbyai.com/best-free-ai-tools-frontend/ (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B15.2 — screenshot-to-code (open source)
- **Canonical identity:** `abi/screenshot-to-code`
- **Category:** Open-source screenshot-to-code (GPT-4V + Tailwind)
- **Type:** Tool (actual category: open-source app, not a library)
- **Official URL:** https://github.com/abi/screenshot-to-code (URL from public knowledge; not opened this session)
- **Description:** Upload a screenshot → HTML/Tailwind (or React) via vision models; the canonical open-source reference for the pattern.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Image→code with iterative refinement.
- **Usage domain:** Experiments, self-hosted screenshot-to-code.
- **Integration method:** Clone; bring your own API key.
- **Dependencies:** Vision-model API key. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Rough starts; needs judgment-driven fixes (spacing, fonts, a11y, responsive).
- **Related resources:** v0 (B15.1).
- **Sources:** https://dupple.com/blog/screenshot-to-code (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B15.3 — Bolt.new / Lovable (full-stack prompt-to-app)
- **Canonical identity:** Bolt.new (bolt.new, StackBlitz); Lovable (lovable.dev)
- **Category:** Prompt-to-full-stack-app generators
- **Type:** SaaS products
- **Official URL:** https://bolt.new · https://lovable.dev (URLs from public knowledge; not opened this session)
- **Description:** Bolt.new: full-stack from a prompt (frontend + backend scaffolding, sandboxed runtime) — strong for MVPs. Lovable: solo-founder-focused, Supabase-native backend; output quality varies more on complex UIs (per secondary).
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Prompt→runnable app.
- **Usage domain:** MVPs, prototypes.
- **Integration method:** Web apps.
- **Dependencies:** None. **Availability:** Credit-based SaaS.
- **Maintenance:** Active. Partially verified.
- **License:** Output per terms (not re-verified).
- **Limitations:** Token/credit burn on iteration; not a component library.
- **Related resources:** v0 (B15.1), Replit Agent (below).
- **Sources:** https://dupple.com/blog/screenshot-to-code (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B15.4 — Magic Patterns / Uizard (ideation)
- **Canonical identity:** Magic Patterns (magicpatterns.com); Uizard (uizard.io)
- **Category:** AI UI pattern/ideation generators
- **Type:** SaaS products
- **Official URL:** https://www.magicpatterns.com · https://uizard.io (URLs from public knowledge; not opened this session)
- **Description:** Magic Patterns: UI patterns (cards, dashboards, layouts) in React + Tailwind for assembling pages. Uizard: wireframes/mockups/prototypes — better for ideation than production code.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Pattern generation; wireframe→mockup.
- **Usage domain:** Early-stage UI exploration.
- **Integration method:** Web apps.
- **Dependencies:** None. **Availability:** SaaS.
- **Maintenance:** Active per secondary sources. Partially verified.
- **License:** Per terms (not re-verified).
- **Limitations:** Ideation-grade output.
- **Related resources:** v0 (B15.1).
- **Sources:** https://dupple.com/blog/screenshot-to-code (accessed 2026-10-10); https://techsive.com/image-to-code-anima-vs-locofy-and-other-tools-for-turning-ui-images-into-frontend-code/ (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified

## B16. Component documentation tools

### B16.1 — Storybook
- **Canonical identity:** `storybookjs/storybook` (npm: `storybook`, `@storybook/react-vite` etc.)
- **Category:** UI workshop — isolated component development, docs, testing
- **Type:** Tool/framework
- **Official URL:** https://storybook.js.org · https://github.com/storybookjs/storybook
- **Description:** "Industry standard workshop for building, documenting, and testing UI components in isolation"; renderers for React/Vue/Angular/Svelte/Web Components/React Native/HTML/Ember/Preact/Qwik/Solid; addons (a11y, docs, actions, viewport, interactions); test-runner + Vitest integration; Chromatic for visual regression.
- **Contents inspected:** GitHub repo root, README.md, repo metadata (2026-10-10). Root contains `.agents/`, `.claude/skills`, `AGENTS.md`, `CLAUDE.md`, `agent-eval/` — strong agent-facing surface. Default branch `next`.
- **Actual capabilities:** Stories (CSF), MDX docs, controls, play functions, visual/a11y/interaction testing.
- **Usage domain:** Design-system development, component documentation, visual regression.
- **Integration method:** npm (`storybook init`); dev server :6006; static export.
- **Dependencies:** Framework renderer + builder (Vite/Webpack). **Availability:** Open source.
- **Maintenance:** Active — 91,209 stars, 88,192 commits, 1,852 releases.
- **License:** MIT.
- **Limitations:** Heavier install than alternatives (~30 deps); cold start ~8s vs Ladle's ~1.2s (per secondary benchmarks).
- **Related resources:** Ladle (B16.2), Histoire (B16.3), Chromatic (B16.4).
- **Sources:** https://github.com/storybookjs/storybook (inspected 2026-10-10); https://github.com/hhs/opre-ops/blob/HEAD/docs/adr/031-storybook-for-component-documentation.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** High · **Label:** Verified

### B16.2 — Ladle
- **Canonical identity:** `tajo/ladle` (npm: `@ladle/react`)
- **Category:** Lightweight Vite-native React component workshop
- **Type:** Tool
- **Official URL:** https://ladle.dev · https://github.com/tajo/ladle (URL from public knowledge; not opened this session)
- **Description:** Extremely lightweight (~5 deps), Vite-native, fast startup (~1.2s cold); stories format; React-only.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Component preview, controls (basic), static export.
- **Usage domain:** React-only prototyping where Storybook overhead isn't justified.
- **Integration method:** npm.
- **Dependencies:** Vite, React. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** No a11y addon, no play functions, tiny addon ecosystem, React-only.
- **Related resources:** Storybook (B16.1), Histoire (B16.3).
- **Sources:** https://www.pkgpulse.com/guides/storybook-8-vs-ladle-vs-histoire-2026 (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B16.3 — Histoire
- **Canonical identity:** `histoire-dev/histoire` (npm: `histoire`)
- **Category:** Vite-native component workshop (Vue-first)
- **Type:** Tool
- **Official URL:** https://histoire.dev · https://github.com/histoire-dev/histoire (URL from public knowledge; not opened this session)
- **Description:** Vite-native stories; Vue 3 and Svelte primary; React experimental/community; markdown docs, props tables, playgrounds; snapshots via Vitest.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Stories, controls, visual regression via plugins.
- **Usage domain:** Vue/Svelte component development.
- **Integration method:** npm.
- **Dependencies:** Vite. **Availability:** Open source.
- **Maintenance:** Maintained per secondary sources. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** React support experimental; limited addon ecosystem vs Storybook.
- **Related resources:** Storybook (B16.1), Ladle (B16.2).
- **Sources:** https://www.pkgpulse.com/guides/storybook-8-vs-ladle-vs-histoire-2026 (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Partially verified

### B16.4 — Chromatic
- **Canonical identity:** Chromatic (chromatic.com) — by Storybook maintainers
- **Category:** Visual regression testing cloud for Storybook
- **Type:** SaaS (actual category: hosted service, not a library)
- **Official URL:** https://www.chromatic.com (URL from public knowledge; not opened this session)
- **Description:** Cloud visual testing + review for Storybook; UI regression diffs, TurboSnap.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Snapshot diffing, PR review workflows.
- **Usage domain:** Design-system visual regression.
- **Integration method:** npm (`chromatic`) + CI.
- **Dependencies:** Storybook. **Availability:** Freemium SaaS.
- **Maintenance:** Active. Partially verified.
- **License:** Commercial SaaS (per public knowledge; not re-verified).
- **Limitations:** Paid beyond free snapshots; Storybook-coupled.
- **Related resources:** Storybook (B16.1).
- **Sources:** https://github.com/hhs/opre-ops/blob/HEAD/docs/adr/031-storybook-for-component-documentation.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B16.5 — Docz (historical)
- **Canonical identity:** `doczjs/docz`
- **Category:** MDX component documentation — ARCHIVED
- **Type:** Tool (unmaintained)
- **Official URL:** https://github.com/doczjs/docz (URL from public knowledge; not opened this session)
- **Description:** Once-popular MDX docs tooling; project archived/unmaintained; superseded by Storybook docs mode / Docusaurus.
- **Contents inspected:** Not inspected directly.
- **Actual capabilities:** Historical.
- **Usage domain:** Legacy only.
- **Integration method:** n/a.
- **Dependencies:** n/a. **Availability:** Archived.
- **Maintenance:** Archived per public knowledge. Partially verified.
- **License:** MIT (per public knowledge; not re-verified).
- **Limitations:** Do not adopt.
- **Related resources:** Storybook (B16.1), Docusaurus (A3.3).
- **Sources:** Secondary docs-tooling roundups (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Medium · **Label:** Historical

## B17. Agent-discoverability resources for frontend work

These repos/skills help coding agents discover real props/APIs/examples for the libraries above (per the brief — "not just the libraries themselves"):

### B17.1 — Context7 (upstash/context7)
Cross-reference (dedup: covered by another workstream — MCP servers). The de-facto docs MCP: version-specific library documentation fetched from source on demand. Relevant to every library in this catalog. Status per prior Atlas research: verified, active.

### B17.2 — shadcn MCP (official + community)
Cross-reference (dedup: already catalogued). Official: `pnpm dlx shadcn@latest mcp init`. Community server also exists. Verified 2026-08-11 per prior research.

### B17.3 — frontend-nexus (thegbosstv/frontend-nexus)
- **Canonical identity:** `thegbosstv/frontend-nexus`
- **Category:** Agent-facing frontend library encyclopedia (Next.js app + MDX entries)
- **Type:** Knowledge base (actual category: docs site for agents/humans, not a library)
- **Official URL:** https://github.com/thegbosstv/frontend-nexus (from search results; repo not opened this session)
- **Description:** Per-library MDX entries (react-hook-form, zod, etc.) written for agent consumption: API patterns, resolver matrices, Proxy/subscription semantics.
- **Contents inspected:** One entry (react-hook-form.mdx) excerpt via search (2026-10-10). Repo not opened.
- **Actual capabilities:** Library usage references.
- **Usage domain:** Agent reference for frontend library APIs.
- **Integration method:** Read docs.
- **Dependencies:** n/a. **Availability:** Open source (per listing).
- **Maintenance:** Active (updated ~49 days ago per search). Partially verified.
- **License:** Not verified — Unresolved.
- **Limitations:** Secondary knowledge; verify against primary docs.
- **Related resources:** Context7 (B17.1).
- **Sources:** https://github.com/thegbosstv/frontend-nexus/blob/HEAD/app/content/libraries/react-hook-form.mdx (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B17.4 — ai-web-design-codex (eneryleen/ai-web-design-codex)
- **Canonical identity:** `eneryleen/ai-web-design-codex`
- **Category:** AI web-design knowledge codex (curated markdown)
- **Type:** Knowledge base
- **Official URL:** https://github.com/eneryleen/ai-web-design-codex (from search results; repo not opened this session)
- **Description:** Curated chapters: frameworks-for-design, component-libraries-headless, css-styling-and-tailwind, design-systems-and-tokens, accessibility, webgl-3d-shaders, animation-libraries-stack; includes "rules at a glance" (e.g., headless-library selection rules, the shadcn "beige problem").
- **Contents inspected:** Two chapter excerpts via search (2026-10-10). Repo not opened.
- **Actual capabilities:** Curated guidance for AI-assisted web design.
- **Usage domain:** Agent reference for stack decisions.
- **Integration method:** Read docs.
- **Dependencies:** n/a. **Availability:** Open source (per listing).
- **Maintenance:** Active (updated ~110 days ago per search). Partially verified.
- **License:** Not verified — Unresolved.
- **Limitations:** Opinionated curation; verify claims.
- **Related resources:** frontend-nexus (B17.3).
- **Sources:** https://github.com/eneryleen/ai-web-design-codex/blob/HEAD/04-libraries-and-tools/frameworks-for-design.md (accessed 2026-10-10); https://github.com/eneryleen/ai-web-design-codex/blob/HEAD/04-libraries-and-tools/component-libraries-headless.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B17.5 — ui-forager-skill (helix98/ui-forager-skill)
- **Canonical identity:** `helix98/ui-forager-skill`
- **Category:** Agent skill — UI library references for foraging components
- **Type:** Skill (references/libraries.md)
- **Official URL:** https://github.com/helix98/ui-forager-skill (from search results; repo not opened this session)
- **Description:** Curated library reference (shadcn, Base UI, Ark UI, Ariakit, Headless UI, React Aria, Radix Themes) guiding agents to install real components from registries instead of rebuilding.
- **Contents inspected:** references/libraries.md excerpt via search (2026-10-10). Repo not opened.
- **Actual capabilities:** Library selection guidance.
- **Usage domain:** Agent UI component sourcing.
- **Integration method:** Skill install.
- **Dependencies:** n/a. **Availability:** Open source (per listing).
- **Maintenance:** Active (updated ~22 days ago per search). Partially verified.
- **License:** Not verified — Unresolved.
- **Limitations:** Guidance only.
- **Related resources:** ai-skills-full-stack ui-registries (B17.6).
- **Sources:** https://github.com/helix98/ui-forager-skill/blob/HEAD/references/libraries.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B17.6 — ai-skills-full-stack ui-registries (darrencasper/ai-skills-full-stack)
- **Canonical identity:** `darrencasper/ai-skills-full-stack` → `skills/ui-registries/SKILL.md`
- **Category:** Agent skill — shadcn-ecosystem registry guide
- **Type:** Skill
- **Official URL:** https://github.com/darrencasper/ai-skills-full-stack (from search results; repo not opened this session)
- **Description:** "Which library for what" mapping across Aceternity/Magic UI/Cult/Origin/Animate/Kibo/Tailark/21st.dev with install routes and coexistence rules.
- **Contents inspected:** SKILL.md excerpt via search (2026-10-10). Repo not opened.
- **Actual capabilities:** Registry selection + install guidance.
- **Usage domain:** Agent UI assembly.
- **Integration method:** Skill install.
- **Dependencies:** n/a. **Availability:** Open source (per listing).
- **Maintenance:** Active (updated ~16 days ago per search). Partially verified.
- **License:** Not verified — Unresolved.
- **Limitations:** Guidance only; registry facts need re-verification over time.
- **Related resources:** ui-forager-skill (B17.5).
- **Sources:** https://github.com/darrencasper/ai-skills-full-stack/blob/HEAD/skills/ui-registries/SKILL.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B17.7 — plief-lobster library/ (emanueldssss/plief-lobster)
- **Canonical identity:** `emanueldssss/plief-lobster` → `library/` markdown references
- **Category:** Agent reference library (ui-primitives, motion)
- **Type:** Knowledge base
- **Official URL:** https://github.com/emanueldssss/plief-lobster (from search results; repo not opened this session)
- **Description:** `library/ui-primitives.md` (headless comparison table) and `library/motion.md` (animation ladder incl. native-first checks) written as agent-consumable references.
- **Contents inspected:** Excerpts via search (2026-10-10). Repo not opened.
- **Actual capabilities:** Selection guidance.
- **Usage domain:** Agent stack decisions.
- **Integration method:** Read docs.
- **Dependencies:** n/a. **Availability:** Open source (per listing).
- **Maintenance:** Active (updated ~10 days ago per search). Partially verified.
- **License:** Not verified — Unresolved.
- **Limitations:** Guidance only.
- **Related resources:** frontend-nexus (B17.3).
- **Sources:** https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/ui-primitives.md (accessed 2026-10-10); https://github.com/emanueldssss/plief-lobster/blob/HEAD/library/motion.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B17.8 — ericks-design-store (erickalfaro/ericks-design-store)
- **Canonical identity:** `erickalfaro/ericks-design-store`
- **Category:** Offline icon compendium + CLI + Claude skill (44k+ icons, 11 open-source sets)
- **Type:** Tool + skill (actual category: agent-facing icon sourcing tool)
- **Official URL:** https://github.com/erickalfaro/ericks-design-store (from search results; repo not opened this session)
- **Description:** 44k+ icons across Lucide/Phosphor/Tabler/Heroicons/Material Symbols/etc.; CLI outputs SVG/React/Vue/Svelte; browsable gallery; `.claude/skills/design-icons/`; Iconify JSON as source of truth.
- **Contents inspected:** README excerpt via search (2026-10-10). Repo not opened.
- **Actual capabilities:** Icon search/render across sets for agents.
- **Usage domain:** Agent icon sourcing without web access.
- **Integration method:** CLI + skill.
- **Dependencies:** Node (dev tooling only). **Availability:** Open source (per listing).
- **Maintenance:** Updated ~82 days ago per search. Partially verified.
- **License:** Per-set licenses documented in `docs/` (per README; not re-verified).
- **Limitations:** Snapshot-based; resync needed for newest icons.
- **Related resources:** Iconify (B10.10), devpantry icons (below).
- **Sources:** https://github.com/erickalfaro/ericks-design-store (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B17.9 — devpantry icons (allwin-antony/devpantry)
- **Canonical identity:** `allwin-antony/devpantry` → `src/data/opensource/Icons/`
- **Category:** Open-source icon catalog + license guides + fetch CLI
- **Type:** Knowledge base + scripts
- **Official URL:** https://github.com/allwin-antony/devpantry (from search results; repo not opened this session)
- **Description:** Catalog of 100%-open icon libraries with comparison matrix, license guide (attribution traps), fetch/sync/export scripts, web integration guide.
- **Contents inspected:** License guide + README excerpts via search (2026-10-10). Repo not opened.
- **Actual capabilities:** Icon discovery + legal guidance.
- **Usage domain:** Agent/human icon selection with license safety.
- **Integration method:** Read docs; run scripts.
- **Dependencies:** Python 3 (scripts). **Availability:** Open source (per listing).
- **Maintenance:** Active (updated ~18 days ago per search). Partially verified.
- **License:** Not verified — Unresolved.
- **Limitations:** Secondary curation.
- **Related resources:** ericks-design-store (B17.8).
- **Sources:** https://github.com/allwin-antony/devpantry/blob/HEAD/src/data/opensource/Icons/guides/licenses_explained.md (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low-Medium · **Label:** Partially verified

### B17.10 — stealthis resources (foodhy/stealthis)
- **Canonical identity:** `foodhy/stealthis` → `packages/content/resources/`
- **Category:** Curated web resource index (MDX) incl. web-animation-libraries, 3d-web-libraries
- **Type:** Knowledge base
- **Official URL:** https://github.com/foodhy/stealthis (from search results; repo not opened this session)
- **Description:** Structured resource entries (name/url/description/bestFor/pros/cons/attributes/license) for animation and 3D web libraries.
- **Contents inspected:** web-animation-libraries/index.mdx excerpt via search (2026-10-10). Repo not opened.
- **Actual capabilities:** Library discovery metadata.
- **Usage domain:** Agent library selection.
- **Integration method:** Read docs.
- **Dependencies:** n/a. **Availability:** Open source (per listing).
- **Maintenance:** Active (updated ~13 days ago per search). Partially verified.
- **License:** Not verified — Unresolved.
- **Limitations:** Secondary curation.
- **Related resources:** frontend-nexus (B17.3).
- **Sources:** https://github.com/foodhy/stealthis/blob/HEAD/packages/content/resources/web-animation-libraries/index.mdx (accessed 2026-10-10).
- **Verification date:** 2026-10-10 · **Confidence:** Low · **Label:** Partially verified

### B17.11 — In-repo agent surfaces (primary-verified)
Primary-verified 2026-10-10 via repo root inspection:
- **shadcn-ui/ui**: `skills/` + `.claude/` directories; topics include `ai`, `gen-ui`.
- **mui/material-ui**: `.agents/skills`, `.claude/skills`, `skills/`, `AGENTS.md`, `CLAUDE.md`.
- **TanStack/query**: `AGENTS.md`, `AI_POLICY.md` at root.
- **facebook/react**: `CLAUDE.md`, `.claude/` directory; `compiler/` directory.
- **storybookjs/storybook**: `.agents/`, `.claude/skills`, `AGENTS.md`, `CLAUDE.md`, `agent-eval/`.
- **withastro/astro**: `AGENTS.md`, `.agents/`.
- **nuxt/nuxt**: `AGENTS.md`.
- **pmndrs/zustand**: docs/ directory (no agent-specific dir seen at root).
These in-repo surfaces are the most durable agent-discovery mechanism: version-pinned, maintained alongside the code.

---

# COVERAGE NOTE

## Counts
- **Distinct entries:** 195 (Part A: 100; Part B: 95). **Full Part-21 records:** 190. **Cross-reference/mini entries:** 5 (A3.1 Astro-as-SSG, A16.1 React Aria, B17.1 Context7, B17.2 shadcn MCP, B17.11 in-repo agent surfaces).
- **Primary-inspected (repo README + metadata opened 2026-10-10):** 10 (shadcn-ui/ui, mui/material-ui, pmndrs/zustand, TanStack/query, facebook/react, vuejs/core, storybookjs/storybook, tailwindlabs/tailwindcss, withastro/astro, nuxt/nuxt).
- **Verified:** 10 (same as above).
- **Partially verified:** 175 (2+ independent secondary sources or single strong source; repo not opened this session).
- **Historical:** 4 (Recoil, Gatsby, Stitches, Docz; Slate is Unresolved rather than Historical).
- **Unresolved items:**
  1. Slate archive status (reported archived 2026-02-04 by one secondary source — needs primary check of ianstormtaylor/slate).
  2. Astro GitHub license field showed `NOASSERTION` while README badges assert MIT — discrepancy unresolved.
  3. styled-components "maintenance mode as of 2025-03-17" — single secondary source; needs primary confirmation.
  4. Headless UI maintenance pace ("no release/commit since April 2026") — single secondary source; needs primary check.
  5. GSAP license terms post-Webflow (free incl. commercial but not OSI; redistribution/forking restrictions) — needs primary check of current license text.
  6. Aceternity UI license — no public repo/LICENSE; unresolved redistribution risk.
  7. Licenses not re-verified for ~175 secondary-sourced items (recorded from public knowledge/secondary tables — marked "per public knowledge/secondary; not re-verified").
  8. p5.js LGPL-2.1 nuance; BlockNote XL GPL-3.0 copyleft scope; Remotion commercial-license nuance; Origin UI AGPL carve-outs — all need primary license-file checks before reuse advice.
  9. uishelf license; Tailark license; SVGL per-logo licensing — unresolved.
  10. TanStack Store/DB/Form/Virtual actual capabilities — only ecosystem-listing level; repos not opened.

## Limitations of this research
- Only 10 of 195 entries had their primary repo opened; the rest rely on secondary sources (reviews, ADRs, skill docs, registry indexes). Secondary claims about versions, download counts, and release dates were NOT independently re-verified against npm/GitHub APIs.
- No browser-based live checks of docs sites (react.dev, tailwindcss.com, etc.) were performed — availability of docs URLs is assumed from public knowledge.
- Commercial tools (v0, Locofy, Builder.io, Anima, Plasmic, Tailwind UI, Chromatic) were assessed from reviews, not vendor docs or trials; pricing/feature claims may be stale.
- Search-result excerpts are snapshots; fast-moving projects (TanStack ecosystem, Base UI, Panda CSS) may have shipped newer versions since the cited sources.

## More work warranted?
- **Yes, targeted:** (a) primary verification pass over the ~35 highest-weight secondary items (Radix, Base UI, React Aria, Ark UI, TanStack Router/Table, Zod, React Hook Form, Tiptap, Lexical, Motion, GSAP, Three.js, Lucide, Panda CSS, Mantine); (b) resolve the 10 Unresolved items above; (c) license-file audit for the flagged items before any reuse guidance; (d) check npm registry for current versions of the TanStack ecosystem packages; (e) verify Slate's archive status directly.
- The dedup list was honored: astryx, shadcn MCP, laws-of-ux-skills, awesome-design-systems, gztchan/awesome-design, awesome-design-md were not re-researched (cross-referenced only).
