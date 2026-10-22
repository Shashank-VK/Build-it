# 05 — Builders (CSS Frameworks/Tokens/Primitives · PM/Bundlers/Compilers/Lint/Monorepo · Auth/Email/Payments/Maps/Media/Analytics/CMS/Datasets · Scaffolds · Architecture/DDD)

> Part 3 · B-category catalog · Core-Tech researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved

## Index (30 resources)

Styling: Tailwind CSS · Bootstrap · shadcn/ui · Radix Primitives · Headless UI · Style Dictionary (tokens)
JS supply chain: npm · pnpm · Yarn (Berry) · Vite (+Rolldown) · webpack · esbuild · SWC · Babel · ESLint · Prettier · Turborepo · Nx
Cross-cutting SaaS: Auth0 · Resend · Stripe · Mapbox/Leaflet · PostHog · Strapi · Sanity · data.gov (public datasets exemplar)
Scaffolds: create-next-app/create-vite · Yeoman (generator exemplar)
Architecture: DDD reference (Evans/Vernon) + C4

---

### 01 — Tailwind CSS (v4.x)
- **Canonical identity:** `npm:tailwindcss` — `github:tailwindlabs/tailwindcss`
- **Category:** Builders → Utility CSS framework
- **Type:** OSS (Tailwind Labs)
- **Official URL:** https://tailwindcss.com/ (docs: https://tailwindcss.com/docs/)
- **Description:** Utility-first; v4 (CSS-first `@theme`, Lightning CSS, `@tailwindcss/vite`, OKLCH); 4.3.x current mid-2026 (4.3.3 2026-07-16).
- **Contents inspected:** WebSearch-verified changelog corpus (whatsnew.fyi/releases.sh: 4.2–4.3 series, Vite 8 support, container/scrollbar utilities) + shadcn Tailwind-v4 guides (deprecation of `toast`→`sonner`, HSL→OKLCH).
- **Capabilities:** JIT, variants, container queries, typography/forms plugins, upgrade codemod.
- **Usage domain:** Default styling for Next/Nuxt/Astro + shadcn.
- **Integration:** official (`@tailwindcss/vite`, `@tailwindcss/postcss`, `prettier-plugin-tailwindcss`)
- **Compatibility:** Modern browsers (v4 bleeding-edge baseline); Vite 8 supported.
- **Deps:** `lightningcss`/`jiti` (v4).
- **Availability:** npm.
- **Maintenance:** Active (v4.3 2026).
- **License:** MIT.
- **Security/limits:** `content` globs determine shipped CSS; safelist dynamic classes explicitly.
- **Related:** UnoCSS, shadcn/ui, Radix.
- **Sources:** tailwindcss.com; whatsnew.fyi/releases.sh excerpts; ui.shadcn.com Tailwind-v4 docs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — Bootstrap (v5.3)
- **Canonical identity:** `npm:bootstrap` — `github:twbs/bootstrap`
- **Category:** Builders → Class CSS framework
- **Type:** OSS (Open Collective)
- **Official URL:** https://getbootstrap.com/ (docs: https://getbootstrap.com/docs/5.3/)
- **Description:** Prebuilt components + grid + utilities; RTL, dark mode, CSS vars; still fastest for admin CRUD without build deep-dives.
- **Contents inspected:** getbootstrap.com docs (getting started, components).
- **Capabilities:** Sass maps, JS plugins (no jQuery), Icons.
- **Usage domain:** Django/Rails/Laravel server-rendered + prototypes.
- **Integration:** official (`bootstrap` npm/CDN; `react-bootstrap`, `ng-bootstrap` adapters)
- **Compatibility:** Evergreen (IE dropped).
- **Deps:** `@popperjs/core`.
- **Availability:** CDN/npm.
- **Maintenance:** Active (5.3.x; v6 prep discussions).
- **License:** MIT.
- **Security/limits:** `data-bs-*` with user content — escape; keep Popper patched.
- **Related:** Tailwind, Bulma, Foundation (archived).
- **Sources:** getbootstrap.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 03 — shadcn/ui (registry + CLI, not a dependency)
- **Canonical identity:** `tool:shadcn-ui` — `github:shadcn-ui/ui`
- **Category:** Builders → Copy-paste component registry
- **Type:** OSS (shadcn @ Vercel)
- **Official URL:** https://ui.shadcn.com/ (docs: https://ui.shadcn.com/docs/)
- **Description:** Own-your-code primitives over Radix + Tailwind (CVA, `cn`, Lucide, Sonner); `npx shadcn@latest init/add`; Tailwind v4 + React 19 ready; namespaces/registries/MCP in 2026.
- **Contents inspected:** WebSearch-verified ui.shadcn.com docs (manual install, Tailwind-v4 page, Feb-2026 Blocks for Radix/Base UI, TanStack Start install, components.json).
- **Capabilities:** 50+ components/blocks, themes, dark mode, private registries.
- **Usage domain:** SaaS/admin default UI on Next/Vite/Astro/TanStack.
- **Integration:** official CLI (`shadcn init/add`; `@/components` alias; per-framework install guides: Next/Vite/Laravel/RR/Astro/TanStack)
- **Compatibility:** React 18/19 + Tailwind v3/v4.
- **Deps:** `class-variance-authority`, `clsx`+`tailwind-merge`, `lucide-react`, `@radix-ui/*` or Base UI.
- **Availability:** CLI + GitHub (code copied into repo).
- **Maintenance:** Active (2026 blocks/registry work).
- **License:** MIT.
- **Security/limits:** You own updates — track upstream diffs; form components need server validation.
- **Related:** Radix, Base UI, Tailwind, Tremor (dashboard blocks).
- **Sources:** ui.shadcn.com excerpts (search session).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 04 — Radix Primitives (+ Themes)
- **Canonical identity:** `npm:@radix-ui/react-*` — `github:radix-ui/primitives`
- **Category:** Builders → Headless a11y primitives
- **Type:** OSS (WorkOS)
- **Official URL:** https://www.radix-ui.com/primitives (themes: https://www.radix-ui.com/themes)
- **Description:** Unstyled Dialog/Dropdown/Slot/Toast with WAI-ARIA + focus management; base of shadcn.
- **Contents inspected:** radix-ui.com primitives docs + themes overview.
- **Capabilities:** Composable `Slot`, portals, roving tabindex.
- **Usage domain:** Design systems needing full style control.
- **Integration:** official (`@radix-ui/react-*`; shadcn wraps them)
- **Compatibility:** React 18/19.
- **Deps:** None heavy.
- **Availability:** npm.
- **Maintenance:** Active (1.x/2.x 2024-2026; Base UI as alt).
- **License:** MIT.
- **Security/limits:** Focus-trapping review in modals; no security claims beyond a11y.
- **Related:** Base UI, Headless UI, Ark UI.
- **Sources:** radix-ui.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 05 — Headless UI (Tailwind)
- **Canonical identity:** `npm:@headlessui/react` + `@headlessui/vue` — Tailwind Labs
- **Category:** Builders → Headless components
- **Type:** OSS
- **Official URL:** https://headlessui.com/
- **Description:** Tailwind-styled unstyled Combobox/Dialog/Popover fully keyboard-accessible; React+Vue.
- **Contents inspected:** headlessui.com React/Vue docs.
- **Capabilities:** Transitions API, SSR-safe.
- **Usage domain:** Tailwind teams not using Radix.
- **Integration:** official React/Vue packages
- **Compatibility:** React 18/19, Vue 3.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active (v2.x 2024-2026).
- **License:** MIT.
- **Security/limits:** Same modal/FocusTrap hygiene.
- **Related:** Radix, Ark UI.
- **Sources:** headlessui.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — Style Dictionary (design tokens)
- **Canonical identity:** `npm:style-dictionary` — `github:amzn/style-dictionary`
- **Category:** Builders → Token pipeline
- **Type:** OSS (Amazon)
- **Official URL:** https://amzn.github.io/style-dictionary/ (docs site)
- **Description:** W3C DTCG-aligned tokens (color/type/space) → CSS vars, Tailwind `@theme`, iOS/Android outputs; Style Dictionary 4.x.
- **Contents inspected:** Style Dictionary docs (config, transforms, formats).
- **Capabilities:** Multi-brand theming, dark-mode tokens, Figma Tokens sync.
- **Usage domain:** Multi-platform design systems.
- **Integration:** official (Style Dictionary CLI; `sd.config.json`; Tailwind `@theme inline` mapping)
- **Compatibility:** Node 18+.
- **Deps:** None heavy.
- **Availability:** npm.
- **Maintenance:** Active (4.x 2024-2026).
- **License:** Apache-2.0.
- **Security/limits:** Token JSON is public-by-design — keep secrets out.
- **Related:** Theo (legacy), Tokens Studio, Panda CSS.
- **Sources:** amzn.github.io/style-dictionary.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 07 — npm (10/11) — package manager baseline
- **Canonical identity:** `tool:npm` — GitHub/npm Inc.
- **Category:** Builders → Package manager + registry
- **Type:** OSS client + commercial registry
- **Official URLs:** https://www.npmjs.com/ · https://docs.npmjs.com/ (CLI: https://github.com/npm/cli)
- **Description:** Default Node PM; `package-lock.json`, workspaces, `npm stage` (11.15+/Node 22.14 per Vite+ docs); provenance/2FA.
- **Contents inspected:** npm docs (install/workspaces); Vite+ package-manager detection excerpt listing npm lockfiles.
- **Capabilities:** Workspaces, `overrides`, provenance attestations.
- **Usage domain:** Default JS supply chain.
- **Integration:** native (Node bundles npm; `packageManager` field / corepack)
- **Compatibility:** Node 18/20/22.
- **Deps:** None.
- **Availability:** nodejs.org + npmjs registry.
- **Maintenance:** Active.
- **License:** Artistic-2.0 (client).
- **Security/limits:** Lockfile + `npm audit/signatures`; require 2FA + provenance for publish.
- **Related:** pnpm, Yarn, Bun.
- **Sources:** docs.npmjs.com; npm package pages (vite/esbuild excerpts).
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — pnpm (10/11) — efficient monorepo PM
- **Canonical identity:** `tool:pnpm` — `github:pnpm/pnpm`
- **Category:** Builders → Package manager
- **Type:** OSS
- **Official URL:** https://pnpm.io/ (docs: https://pnpm.io/docs/)
- **Description:** Content-addressable store, strict `node_modules`, fast monorepos (`pnpm-workspace.yaml`, `onlyBuiltDependencies` approvals); default fallback in Vite+.
- **Contents inspected:** pnpm.io docs + Vite+ excerpt (pnpm v10 `rebuild`/`approve-builds`, stage behavior).
- **Capabilities:** `pnpm dlx`, `patch-package` flow, catalogs.
- **Usage domain:** Monorepos, CI speed, disk savings.
- **Integration:** official (`corepack enable`, `packageManager: pnpm@x`, `pnpm approve-builds`)
- **Compatibility:** Node 18+.
- **Deps:** None.
- **Availability:** corepack/npm standalone.
- **Maintenance:** Active (10.x/11.x 2025-2026).
- **License:** MIT.
- **Security/limits:** `onlyBuiltDependencies` gate review postinstall scripts.
- **Related:** npm, Yarn, Bun.
- **Sources:** pnpm.io; viteplus.dev excerpt.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — Yarn (Berry 4.x) — alternative PM
- **Canonical identity:** `tool:yarn-berry` — `github:yarnpkg/berry`
- **Category:** Builders → Package manager
- **Type:** OSS
- **Official URL:** https://yarnpkg.com/ (docs: https://yarnpkg.com/getting-started)
- **Description:** PnP/zip installs, constraints, `yarn npm publish --staged`; Vite+ detects `yarn.lock/.yarnrc.yml`.
- **Contents inspected:** yarnpkg.com Berry docs (PnP, workspaces).
- **Capabilities:** `yarn dlx`, SDKs (VS Code), release workflow.
- **Usage domain:** Plug'n'play zero-install repos.
- **Integration:** official (corepack; `.yarnrc.yml`)
- **Compatibility:** Node 18+.
- **Deps:** None.
- **Availability:** corepack.
- **Maintenance:** Active (4.x).
- **License:** BSD-2-Clause.
- **Security/limits:** PnP loose-mode review; checksum enforcement.
- **Related:** pnpm, npm.
- **Sources:** yarnpkg.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — Vite (8.x + Rolldown) — dev/build baseline
- **Canonical identity:** `npm:vite` (+ `npm:rolldown-vite`) — VoidZero
- **Category:** Builders → Build tool (dev server + bundler)
- **Type:** OSS
- **Official URL:** https://vite.dev/ (blog: https://vite.dev/blog/announcing-vite8)
- **Description:** Native-ESM dev + HMR; Vite 8 unifies on Rust Rolldown (10–30× faster, Rollup-plugin compatible); 65M weekly DLs; `registry.vite.dev` plugin directory; powers Astro/SvelteKit.
- **Contents inspected:** WebSearch-verified Vite 8 announcement (2026-03-12), features/why/comparisons docs, npm `vite@6.2.6` page.
- **Capabilities:** Pre-bundling (esbuild), lib mode, SSR, plugin API, `import.meta` env.
- **Usage domain:** Default for React/Vue/Svelte/solid starters.
- **Integration:** official plugins (`@vitejs/plugin-react/vue`, `@tailwindcss/vite`, `vite-plugin-pwa`)
- **Compatibility:** Node 18+; browsers per `build.target` (Chrome 107+/Safari 16+ defaults).
- **Deps:** `esbuild`, `postcss`, `rollup`→`rolldown`.
- **Availability:** npm `vite`; `pnpm create vite`/`vite.new`.
- **Maintenance:** Active (8.0 Mar-2026; ViteConf Oct-2026).
- **License:** MIT.
- **Security/limits:** `server.fs.allow` scoping; `.env` prefix (`VITE_`) exposure review.
- **Related:** Vitest, Rolldown, Astro.
- **Sources:** vite.dev/blog/announcing-vite8 + docs excerpts (search session).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 11 — webpack (5.x) — legacy/incumbent bundler
- **Canonical identity:** `npm:webpack` — OpenJS (`github:webpack/webpack`)
- **Category:** Builders → Bundler
- **Type:** OSS
- **Official URL:** https://webpack.js.org/ (guides: https://webpack.js.org/guides/)
- **Description:** Module federation, code-splitting, loaders; still under Next.js ≤15 prod builds (replaced by Turbopack in 16) + Storybook/legacy.
- **Contents inspected:** webpack.js.org concepts/guides.
- **Capabilities:** `HtmlWebpackPlugin`, MF remotes, persistent caching.
- **Usage domain:** Legacy enterprise, MF micro-frontends.
- **Integration:** official (`webpack-cli`, `webpack-dev-server`)
- **Compatibility:** Node 18+.
- **Deps:** `acorn`, `tapable`.
- **Availability:** npm.
- **Maintenance:** Maintenance-active (5.x; v6 slow-track).
- **License:** MIT.
- **Security/limits:** Loader code exec at build — pin + audit.
- **Related:** Rspack (Rust alt), Turbopack, Vite.
- **Sources:** webpack.js.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — esbuild (0.27/0.28) — fast transpiler/bundler
- **Canonical identity:** `npm:esbuild` — `github:evanw/esbuild`
- **Category:** Builders → Transpiler/minifier
- **Type:** OSS (Evan Wallace)
- **Official URL:** https://esbuild.github.io/ (api: https://esbuild.github.io/api/)
- **Description:** Go-based 10–100× transpile; Vite dev pre-bundling + TS/JSX; 0 runtime deps; Node ≥18.
- **Contents inspected:** WebSearch-verified npmx/npm pages (`esbuild@0.27.7`, Apr-2026; 0 deps; MIT; install size) + Vite "Why not bundle with esbuild" note.
- **Capabilities:** `esbuild.build/transform`, watch, plugins (limited vs Rollup).
- **Usage domain:** Scripts, Vite internals, tsup CLIs.
- **Integration:** official (`esbuild` binary; `tsx`, `tsup` wrap it)
- **Compatibility:** Node 18+; 26 arch-specific optionals.
- **Deps:** Zero (optionals per-arch).
- **Availability:** npm.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Transpile-only (no typecheck) — pair with `tsc --noEmit`.
- **Related:** SWC, Rolldown, Vite.
- **Sources:** npm/nppmx excerpts (search session).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 13 — SWC (Rust TS/babel successor)
- **Canonical identity:** `npm:@swc/core` — `github:swc-project/swc` (Vercel)
- **Category:** Builders → Compiler (parse/transform/minify)
- **Type:** OSS
- **Official URL:** https://swc.rs/ (docs: https://swc.rs/docs/)
- **Description:** Rust parser powering Next.js transpilation, Rollup v4 parser, Deno lints; 20× Babel.
- **Contents inspected:** swc.rs docs (config, plugins).
- **Capabilities:** `.swcrc`, Wasm plugins, minify.
- **Usage domain:** Next.js, Parcel, Rspack internals.
- **Integration:** official (`@swc/cli`, `swc-loader`, `unplugin-swc` for Vite)
- **Compatibility:** Node 18+; napi binaries.
- **Deps:** napi.
- **Availability:** npm.
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security/limits:** Wasm plugin sandbox review.
- **Related:** Babel, esbuild, Lightning CSS.
- **Sources:** swc.rs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — Babel (7.x) — compat transpiler
- **Canonical identity:** `npm:@babel/core` — `github:babel/babel`
- **Category:** Builders → Transpiler/polyfill orchestrator
- **Type:** OSS
- **Official URL:** https://babeljs.io/ (docs: https://babeljs.io/docs/)
- **Description:** Presets (`preset-env/react/ts`), `Browserslist` targets, polyfill via `core-js`; still needed for exotic transforms.
- **Contents inspected:** babeljs.io docs/setup.
- **Capabilities:** Plugins, `babel-loader`, macros.
- **Usage domain:** Legacy targets, codemods, Jest transform.
- **Integration:** official (`@babel/cli/preset-*`; Vite via `@vitejs/plugin-*` rarely needed)
- **Compatibility:** Node 14+.
- **Deps:** `@babel/*`, `core-js` (app dep).
- **Availability:** npm.
- **Maintenance:** Maintenance (7.x; 8 in prep).
- **License:** MIT.
- **Security/limits:** `browserslist` freshness; `core-js` version pinning.
- **Related:** SWC, esbuild, Browserslist.
- **Sources:** babeljs.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — ESLint (v9 flat config) + typescript-eslint
- **Canonical identity:** `npm:eslint` + `npm:typescript-eslint` — OpenJS
- **Category:** Builders → Linter
- **Type:** OSS
- **Official URLs:** https://eslint.org/ · https://typescript-eslint.io/
- **Description:** Flat `eslint.config.js`, stylistic split (`@stylistic`), framework configs (React/Vue/Astro); type-aware rules.
- **Contents inspected:** eslint.org + typescript-eslint docs (getting started, typed-linting).
- **Capabilities:** `eslint --fix`, codemods, `FlatCompat`.
- **Usage domain:** CI quality gates for all JS/TS.
- **Integration:** official (`@eslint/js`, `eslint-plugin-react-hooks`, `eslint-plugin-vue`, `eslint-config-*`)
- **Compatibility:** Node 18+ (v9).
- **Deps:** None (plugins per-stack).
- **Availability:** npm.
- **Maintenance:** Active (v9 2024-2026).
- **License:** MIT.
- **Security/limits:** Lint suppressions (`eslint-disable`) need justification + codeowner review.
- **Related:** Biome, Oxlint, Prettier.
- **Sources:** Official docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — Prettier (3.x) + Tailwind plugin
- **Canonical identity:** `npm:prettier` + `npm:prettier-plugin-tailwindcss`
- **Category:** Builders → Formatter
- **Type:** OSS
- **Official URL:** https://prettier.io/ (docs: https://prettier.io/docs/)
- **Description:** Opinionated format (JS/TS/CSS/MDX/YAML); Tailwind class sorting plugin; editor/CI integration.
- **Contents inspected:** prettier.io docs + plugin README (v0.7.x 2026 notes per releases.sh).
- **Capabilities:** `prettier --check/write`, `.editorconfig` interop.
- **Usage domain:** All repos (paired with ESLint).
- **Integration:** official (VS Code extension; `lint-staged`)
- **Compatibility:** Node 14+.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active (3.x).
- **License:** MIT.
- **Security/limits:** None (formatting only).
- **Related:** dprint, Biome formatter.
- **Sources:** prettier.io; releases.sh (plugin 0.7.x Apr-2026).
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 17 — Turborepo (2.x) — JS monorepo orchestrator
- **Canonical identity:** `npm:turbo` — Vercel (`github:vercel/turborepo`)
- **Category:** Builders → Monorepo build orchestration + cache
- **Type:** OSS (Rust/Go)
- **Official URL:** https://turbo.build/ (docs: https://turbo.build/repo/docs)
- **Description:** Task graph (`turbo.json`), remote caching, pruning (`turbo prune --docker`), Boundaries.
- **Contents inspected:** turbo.build docs (getting started, caching).
- **Capabilities:** Parallel pipelines, hash-based cache, Vercel Remote Cache.
- **Usage domain:** pnpm/npm monorepos (apps+packages).
- **Integration:** official (`turbo`, `create-turbo`, GH Actions)
- **Compatibility:** Node 18+.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active (2.x 2024-2026).
- **License:** MPL-2.0 (core).
- **Security/limits:** Remote-cache token scoping; task `outputs` exfiltration review.
- **Related:** Nx, Moon, Lage.
- **Sources:** turbo.build.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — Nx (20.x) — monorepo + CI platform
- **Canonical identity:** `npm:nx` — Nrwl (`github:nrwl/nx`)
- **Category:** Builders → Monorepo + affected analysis
- **Type:** OSS (+ Cloud)
- **Official URL:** https://nx.dev/ (docs: https://nx.dev/docs)
- **Description:** Generators, affected graph, module boundaries, `nx release` (versioning), Nx Cloud distribution.
- **Contents inspected:** nx.dev docs + plugin registry.
- **Capabilities:** `nx g`, `nx affected -t build/test`, Storybook/Cypress presets.
- **Usage domain:** Enterprise TS monorepos.
- **Integration:** official plugins (`@nx/next/react/node/vite/vitest`)
- **Compatibility:** Node 18+.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active.
- **License:** MIT (core).
- **Security/limits:** Generator code exec — review community plugins.
- **Related:** Turborepo, Bazel (heavy alt).
- **Sources:** nx.dev.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — Auth0 (Okta) — managed auth exemplar
- **Canonical identity:** `saas:auth0` — Okta
- **Category:** Builders → Managed identity
- **Type:** Commercial SaaS (+ OSS SDKs)
- **Official URL:** https://auth0.com/ (docs: https://auth0.com/docs)
- **Description:** Universal Login, Actions/Rules, Organizations (B2B), passkeys; SDKs for Next/SPA/native.
- **Contents inspected:** Auth0 docs (quickstarts, architecture scenarios).
- **Capabilities:** Social/enterprise connections, MFA, attack protection.
- **Usage domain:** SaaS auth without IdP ops (alternative to Clerk/Keycloak).
- **Integration:** official SDKs (`@auth0/nextjs-auth0`, `auth0-react`, `auth0-vue`)
- **Compatibility:** OIDC-conformant.
- **Deps:** Network.
- **Availability:** Free tier + paid.
- **Maintenance:** Active.
- **License:** SDKs MIT; service ToS.
- **Security/limits:** Tenant key rotation, Actions secrets vaulting, log-stream SIEM.
- **Related:** Clerk, Keycloak, Supabase Auth.
- **Sources:** auth0.com/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — Resend (+ react-email) — email exemplar
- **Canonical identities:** `saas:resend` · `npm:@react-email/components`
- **Category:** Builders → Transactional email
- **Type:** Commercial SaaS (+ OSS email components)
- **Official URLs:** https://resend.com/ (docs: https://resend.com/docs) · https://react.email/
- **Description:** Simple `POST /emails` API, DKIM/SPF onboarding, webhooks; react-email for Tailwind-templated JSX emails.
- **Contents inspected:** Resend docs (Node/Python SDKs) + react-email docs.
- **Capabilities:** Batch, idempotency keys, audiences (marketing add-on).
- **Usage domain:** Auth codes, receipts, notifications (with BullMQ/QStash producers).
- **Integration:** official SDKs (`resend`, `react-email`)
- **Compatibility:** HTTP API.
- **Deps:** Network.
- **Availability:** Free tier + paid.
- **Maintenance:** Active.
- **License:** SDKs MIT; service ToS.
- **Security/limits:** API-key scoping, webhook signing, suppression-list handling, no secrets in templates.
- **Related:** Postmark, SendGrid, SES.
- **Sources:** Official docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 21 — Stripe (payments exemplar)
- **Canonical identity:** `saas:stripe` — `npm:stripe` + `npm:@stripe/stripe-js`
- **Category:** Builders → Payments/billing
- **Type:** Commercial SaaS (+ OSS SDKs/CLI)
- **Official URL:** https://stripe.com/ (docs: https://docs.stripe.com/)
- **Description:** Checkout/Payment Links, Billing (subscriptions/meters), Connect (marketplaces), Radar, webhooks CLI.
- **Contents inspected:** Stripe docs (payments, billing, webhooks).
- **Capabilities:** SCA/3DS, invoices/tax, test clocks.
- **Usage domain:** SaaS checkout + recurring billing.
- **Integration:** official SDKs + Next.js/Remix guides
- **Compatibility:** PCI SAQ-A via Elements/Checkout (never touch PAN).
- **Deps:** Network.
- **Availability:** Global (coverage varies) + test mode.
- **Maintenance:** Active.
- **License:** SDKs MIT/FOSS; service ToS.
- **Security/limits:** Webhook signature verify, idempotency keys, restricted keys, PCI scope minimization.
- **Related:** Paddle/Lemon Squeezy (MoR), Adyen, PayPal.
- **Sources:** docs.stripe.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 22 — Mapbox GL JS + Leaflet (maps duo)
- **Canonical identities:** `npm:mapbox-gl` · `npm:leaflet`
- **Category:** Builders → Maps
- **Type:** Commercial (Mapbox) + OSS (Leaflet)
- **Official URLs:** https://www.mapbox.com/ (docs: https://docs.mapbox.com/) · https://leafletjs.com/ (docs: https://leafletjs.com/reference.html)
- **Description:** Mapbox (vector tiles, GL rendering, Geocoding/Directions APIs); Leaflet (lightweight OSS with OSM/CARTO tiles + plugins).
- **Contents inspected:** Mapbox GL + Leaflet quickstarts.
- **Capabilities:** Markers/clustering (`supercluster`), choropleths, offline packs.
- **Usage domain:** Store locators, logistics, geo-dashboards.
- **Integration:** official (`mapbox-gl`, `react-map-gl`; `leaflet` + `react-leaflet`)
- **Compatibility:** WebGL (Mapbox) / any (Leaflet).
- **Deps:** Tile/token provider.
- **Availability:** Tokens + free tiers; Leaflet BSD.
- **Maintenance:** Active (Mapbox v3; Leaflet 1.9/2.0 track).
- **License:** Mapbox ToS (lib BSD-ish v2/v3 nuance — check) / Leaflet BSD-2.
- **Security/limits:** Token URL restrictions, tile-usage quotas, location PII minimization.
- **Related:** Google Maps Platform, deck.gl, OpenLayers.
- **Sources:** Official docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 23 — PostHog (analytics exemplar, OSS + Cloud)
- **Canonical identity:** `tool:posthog` — `github:PostHog/posthog`
- **Category:** Builders → Product analytics/feature flags
- **Type:** OSS (+ Cloud)
- **Official URL:** https://posthog.com/ (docs: https://posthog.com/docs)
- **Description:** Autocapture, funnels/paths, session replay, experiments, flags, surveys; self-host (Hobby/Scale) or Cloud EU/US.
- **Contents inspected:** PostHog docs (JS/Web SDK, self-host).
- **Capabilities:** `posthog-js`, Next.js guide, data warehouse source/dest.
- **Usage domain:** Privacy-controllable GA alternative.
- **Integration:** official SDKs (`posthog-js`, `posthog-node`)
- **Compatibility:** All frameworks.
- **Deps:** ClickHouse/PG (self-host via Docker/K8s chart).
- **Availability:** GitHub + Cloud free tier.
- **Maintenance:** Active (weekly).
- **License:** MIT (core parts) + EE paid features (verify per-module).
- **Security/limits:** Cookie/consent + reverse-proxy (`/ingest`) to avoid adblock loss; PII masking in replay.
- **Related:** Plausible (light), GA4, Amplitude.
- **Sources:** posthog.com/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 24 — Strapi (headless CMS exemplar)
- **Canonical identity:** `npm:@strapi/strapi` — `github:strapi/strapi`
- **Category:** Builders → Headless CMS
- **Type:** OSS (+ Cloud/Enterprise)
- **Official URL:** https://strapi.io/ (docs: https://docs.strapi.io/)
- **Description:** Self-host content API (REST+GraphQL), RBAC, i18n, media library; Astro/Next starters.
- **Contents inspected:** Strapi docs (quickstart, content API).
- **Capabilities:** Components/dynamic zones, webhooks, audit logs (EE).
- **Usage domain:** Marketing/docs/commerce content backing Astro/Next.
- **Integration:** official SDKs + CMS webhooks to revalidate (Next ISR/Astro)
- **Compatibility:** Node 18/20; PG/MySQL/SQLite.
- **Deps:** Koa, Knex/bookshelf→Strapi ORM layer.
- **Availability:** npm/Docker + Cloud trial.
- **Maintenance:** Active (v4/v5 2024-2026).
- **License:** MIT (Community) / EE commercial.
- **Security/limits:** Admin path hardening, API-token scopes, media SVGs sanitized.
- **Related:** Sanity, Contentful, Payload.
- **Sources:** docs.strapi.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 25 — Sanity (structured-content SaaS)
- **Canonical identity:** `saas:sanity` — `npm:next-sanity`
- **Category:** Builders → Structured CMS
- **Type:** Commercial SaaS (+ OSS studio/editing libs)
- **Official URL:** https://www.sanity.io/ (docs: https://www.sanity.io/docs)
- **Description:** GROQ content lake, live preview, Presentation tool, Functions; Next/Astro loaders; Pay-as-you-go.
- **Contents inspected:** Sanity docs (studio, GROQ, Next integration).
- **Capabilities:** Real-time collab studio, webhooks, CDN-cached queries.
- **Usage domain:** Editorial + commerce storytelling.
- **Integration:** official (`next-sanity`, `@sanity/astro`, webhook revalidate)
- **Compatibility:** Hosted API + OSS studio.
- **Deps:** Network.
- **Availability:** Free tier + paid.
- **Maintenance:** Active.
- **License:** Studio MIT-ish; service ToS.
- **Security/limits:** Token scopes (viewer vs editor), CORS origins, webhook signing.
- **Related:** Contentful, Hygraph, Payload.
- **Sources:** sanity.io/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 26 — data.gov (+ World Bank API) — public datasets exemplar
- **Canonical identities:** `data:data.gov` · `api:world-bank-v2`
- **Category:** Builders → Public datasets
- **Type:** Open government data (reference-only)
- **Official URLs:** https://data.gov/ (API: https://api.data.gov/) · https://data.worldbank.org/ (API: https://datahelpdesk.worldbank.org/knowledgebase/articles/889392)
- **Description:** US federal catalog (300K+ datasets, CKAN API); World Bank v2 REST (indicators, countries) — no-key demos for charts/maps.
- **Contents inspected:** data.gov catalog + api.data.gov signup; WB API docs (format=json examples).
- **Capabilities:** CSV/JSON/GeoJSON downloads; Socrata/CKAN endpoints.
- **Usage domain:** Dashboards, viz demos, hackathons.
- **Integration:** open-standard (HTTPS/CSV; `api.data.gov` key for rate limits)
- **Compatibility:** Public.
- **Deps:** None.
- **Availability:** Free (rate-limited).
- **Maintenance:** Active (agency-published).
- **License:** CC0 / agency OGL (check per-dataset).
- **Security/limits:** Verify provenance + vintage; never treat demo data as production truth.
- **Related:** data.europa.eu, data.gov.uk, UN Data.
- **Sources:** Official portals.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 27 — create-next-app / create-vite (scaffolder duo)
- **Canonical identities:** `npm:create-next-app` · `npm:create-vite`
- **Category:** Builders → Scaffolding CLIs
- **Type:** OSS CLIs
- **Official URLs:** https://nextjs.org/docs/app/api-reference/cli/create-next-app · https://github.com/vitejs/vite/tree/main/packages/create-vite
- **Description:** Opinionated starters (TS/Tailwind/ESLint/App Router flags; React/Vue/Svelte/Solid templates); verified in Next.js fetch (`npx create-next-app@latest`) + Vite 8 scaffolding (`pnpm create vite`).
- **Contents inspected:** Next.js docs CLI page (WebFetch) + Vite 8 blog scaffolding snippet (search-verified).
- **Capabilities:** `--ts --tailwind --eslint --app --src-dir`; offline templates.
- **Usage domain:** Every new frontend.
- **Integration:** native (npx/pnpm dlx/bunx)
- **Compatibility:** Node 18+.
- **Deps:** Registry access.
- **Availability:** npm.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Review generated secrets/configs before commit.
- **Related:** Yeoman, degit, shadcn `init`.
- **Sources:** WebFetch nextjs.org; Vite 8 announcement.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 28 — Yeoman (`yo`) — generator framework exemplar
- **Canonical identity:** `npm:yo` + `npm:yeoman-generator` — Yeoman team
- **Category:** Builders → Scaffolding framework
- **Type:** OSS
- **Official URL:** https://yeoman.io/ (docs: https://yeoman.io/authoring/)
- **Description:** Composable `generator-*` packages (10K+ generators); still the generic answer for custom org scaffolds.
- **Contents inspected:** yeoman.io authoring/learning docs.
- **Capabilities:** Prompting (`inquirer`), composition, install mixins.
- **Usage domain:** Org-standard service templates.
- **Integration:** official (`yo`, `generator-generator`)
- **Compatibility:** Node 18+.
- **Deps:** `yeoman-environment`.
- **Availability:** npm.
- **Maintenance:** Maintenance (stable; 2024-2026 fixes).
- **License:** BSD-2-Clause.
- **Security/limits:** Generator code runs locally — use org-signed generators.
- **Related:** Plop, Hygen, Copier.
- **Sources:** yeoman.io.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 29 — Domain-Driven Design (Evans + Vernon) — architecture reference
- **Canonical identity:** `practice:ddd` — Evans 2003 + Vernon IDDD 2013
- **Category:** Builders → Architecture pattern family
- **Type:** Published practice (reference-only)
- **Official URLs:** https://www.domainlanguage.com/ddd/ (Evans) · https://vaughnvernon.com/ (Vernon/Vaughn Vernon IDDD)
- **Description:** Ubiquitous language, bounded contexts, aggregates/entities/VOs, context mapping; tactical patterns map to Nest/Spring modules.
- **Contents inspected:** domainlanguage.com reference + IDDD excerpts (no full-text copy).
- **Capabilities:** Strategic (subdomains, context map) + tactical (aggregate roots, repos, domain events).
- **Usage domain:** Backend module boundaries (Nest modules, Django apps, Rails engines).
- **Integration:** reference-only (implemented via framework modules + messaging: Kafka/NATS; docs via C4)
- **Compatibility:** Language-agnostic.
- **Deps:** None.
- **Availability:** Books + free reference sheets.
- **Maintenance:** Stable/historical (ongoing community).
- **License:** Publisher copyright (concepts free to apply).
- **Security/limits:** N/A (modeling only).
- **Related:** Clean/Hexagonal, CQRS/ES, Team Topologies.
- **Sources:** domainlanguage.com; vaughnvernon.com.
- **Verification date:** 2026-10-09 · **Confidence:** Historical

### 30 — C4 Model + Structurizr (architecture diagramming)
- **Canonical identity:** `practice:c4-model` + `tool:structurizr` — Simon Brown
- **Category:** Builders → Architecture documentation
- **Type:** Open method + OSS/commercial tooling
- **Official URLs:** https://c4model.com/ · https://structurizr.com/ (lite: https://github.com/structurizr/lite)
- **Description:** Context/Container/Component/Code views as code (DSL); `structurizr/lite` Docker for local docs; ADR companion.
- **Contents inspected:** c4model.com + Structurizr getting-started.
- **Capabilities:** DSL + PlantUML/Mermaid export; compliance views.
- **Usage domain:** DDD context maps made reviewable.
- **Integration:** official (GitHub Action to publish; Backstage plugin)
- **Compatibility:** Any stack.
- **Deps:** Java/Docker (lite).
- **Availability:** Free tier + DSL OSS (Apache).
- **Maintenance:** Active.
- **License:** CC-BY (C4); Apache-2.0 (Structurizr Lite/DSL).
- **Security/limits:** Redact secrets from diagrams committed to git.
- **Related:** ADRs (adr-tools/log4brains), IcePanel.
- **Sources:** Official sites.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

**Count: 30 resources** (meets 15–30 minimum). No install/execute performed.
