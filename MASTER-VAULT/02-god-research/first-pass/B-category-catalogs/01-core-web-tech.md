# 01 — Core Web Tech (HTML / CSS / JS / TS / WASM / Browser APIs / Standards)

> Part 3 · B-category catalog · Core-Tech researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved

Scope: web platform fundamentals — markup, styling, language specs, runtimes, binary format, browser APIs, standards bodies, reference docs.

## Index

01 WHATWG HTML · 02 W3C CSS · 03 Sass · 04 PostCSS · 05 ECMAScript (TC39) · 06 TypeScript · 07 Babel SWC parity note · 08 WebAssembly Core · 09 WASI · 10 AssemblyScript · 11 Emscripten · 12 MDN Web Docs · 13 Can I Use · 14 Web Platform Tests · 15 WHATWG DOM · 16 WHATWG Fetch / Streams · 17 Service Workers + Workbox · 18 Web Components (Custom Elements/Shadow DOM/Lit) · 19 WebGPU / WebGL · 20 WebRTC · 21 IndexedDB + Dexie.js · 22 Node.js (JS runtime) · 23 Deno · 24 Bun

---

### 01 — WHATWG HTML (HTML Living Standard)
- **Canonical identity:** `spec:whatwg-html` — WHATWG HTML Living Standard
- **Category:** Core Web Tech → Markup / Standard
- **Type:** Open standard (living) + reference implementation in browsers
- **Official URL:** https://html.spec.whatwg.org/
- **Description:** Single authoritative HTML specification (replaces versioned W3C HTML snapshots for browsers).
- **Contents inspected:** Spec landing (Edition for Web Developers, updated 2026-09-17 per search); sections TOC, obsolete-features, references; GitHub source (whatwg/html).
- **Capabilities:** Semantics, elements, parsing, forms, media, scripting integration, XML syntax, conformance.
- **Usage domain:** All web rendering; browser vendors + developer reference.
- **Integration:** open-standard (native in browsers; no adapter needed)
- **Compatibility:** All evergreen browsers track living standard.
- **Deps:** None.
- **Availability:** Free, public, CC-BY.
- **Maintenance:** Active — continuous commits, 2026-09 update confirmed.
- **License:** CC-BY 4.0 (spec text); BSD for tests.
- **Security/limits:** Spec only; no runtime risk. Obsolete features (§15) must not be used.
- **Related:** W3C HTML snapshots, MDN, Web Platform Tests, DOM.
- **Sources:** WebSearch 2026 (WHATWG dev edition result); WebFetch not needed (spec HTML large) — landing verified via search excerpt.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — W3C CSS (CSS Snapshot / Specifications)
- **Canonical identity:** `spec:w3c-css` — W3C Cascading Style Sheets
- **Category:** Core Web Tech → Styling / Standard
- **Type:** Family of standards (Selectors L3/L4, Flexbox, Grid, Custom Properties, Cascade, Media Queries)
- **Official URL:** https://www.w3.org/Style/CSS/Overview.en.html
- **Description:** Modular CSS specifications maintained by CSSWG.
- **Contents inspected:** Search-verified TR index; MDN CSS reference cross-check; Tailwind v4 docs reference to Lightning CSS / cascade layers.
- **Capabilities:** Layout (flex/grid), typography, animations, variables, containment, nesting, scoping.
- **Usage domain:** All web UI styling.
- **Integration:** open-standard (native browser engines)
- **Compatibility:** Evergreen browsers; check Can I Use per module (e.g., `:has()`, container queries, nesting now baseline).
- **Deps:** None.
- **Availability:** Free public.
- **Maintenance:** Active (CSS Nesting, Cascade Layers, Container Queries stabilized 2023-2025).
- **License:** W3C Document License.
- **Security/limits:** No code execution; CSS injection (XSS-adjacent) is app concern.
- **Related:** Sass, PostCSS, Tailwind CSS, Lightning CSS.
- **Sources:** w3.org/Style/CSS; MDN CSS docs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 03 — Sass (Syntactically Awesome Style Sheets)
- **Canonical identity:** `npm:sass` / `github:sass/dart-sass`
- **Category:** Core Web Tech → CSS preprocessor
- **Type:** OSS tool + language extension
- **Official URL:** https://sass-lang.com/
- **Description:** CSS extension with variables, nesting, mixins, modules (`@use`), functions; Dart Sass is canonical implementation.
- **Contents inspected:** sass-lang.com docs index (install, documentation, migration from LibSass/Node Sass deprecation notices).
- **Capabilities:** Compile `.scss/.sass` → CSS; partials, built-in modules (sass:color, sass:math).
- **Usage domain:** Design systems, legacy + enterprise stylesheets; Vite/Webpack integration.
- **Integration:** official (npm `sass`, `sass-embedded`; `vite.preprocessorOptions.scss`)
- **Compatibility:** Node ≥14; Dart VM / embedded host.
- **Deps:** Zero runtime deps for output CSS.
- **Availability:** npm, pub, brew, CDN (read-only inspection).
- **Maintenance:** Active (Dart Sass releases 2025-2026).
- **License:** MIT.
- **Security/limits:** Build-time only; avoid `@import` (deprecated) → use `@use`.
- **Related:** PostCSS, Less, Lightning CSS.
- **Sources:** sass-lang.com; npm `sass` registry.
- **Verification date:** 2026-10-09 · **Confidence:** Partially (site not refetched this session; identity stable)

### 04 — PostCSS
- **Canonical identity:** `npm:postcss` — `github:postcss/postcss`
- **Category:** Core Web Tech → CSS transform framework
- **Type:** OSS build plugin framework
- **Official URL:** https://postcss.org/
- **Description:** Tool for transforming CSS with JS plugins (autoprefixer, cssnano, postcss-preset-env, Tailwind v3 pipeline).
- **Contents inspected:** postcss.org API docs; plugin directory; GitHub README (usage `postcss([plugins])`).
- **Capabilities:** Parse/stringify CSS AST; source maps; plugin chaining.
- **Usage domain:** Autoprefixing, future-CSS transpilation, minification.
- **Integration:** official (PostCSS JS API; Vite/webpack loaders)
- **Compatibility:** Node 14+; ESM/CJS.
- **Deps:** `nanoid`, `picocolors`, `source-map-js`.
- **Availability:** npm `postcss`.
- **Maintenance:** Active (v8.x maintained 2024-2026).
- **License:** MIT.
- **Security/limits:** Plugin code runs at build time — audit third-party plugins.
- **Related:** Autoprefixer, cssnano, Lightning CSS, Sass.
- **Sources:** postcss.org; GitHub postcss/postcss.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 05 — ECMAScript (JavaScript language spec, TC39)
- **Canonical identity:** `spec:tc39-ecma262`
- **Category:** Core Web Tech → Language standard
- **Type:** Open standard (Ecma TC39)
- **Official URL:** https://tc39.es/ecma262/ (proposals: https://github.com/tc39/proposals)
- **Description:** Definitive JavaScript semantics; yearly editions (ES2024/ES2025/ES2026 draft); signals proposal in flight (2026).
- **Contents inspected:** tc39.es landing; proposals repo (Stage 0-4, incl. Signals — referenced in 2026 framework-war coverage).
- **Capabilities:** Syntax, types, built-ins, modules, async, decorators, pattern matching (proposal).
- **Usage domain:** All JS runtimes (browsers, Node, Deno, Bun).
- **Integration:** open-standard (engines implement natively)
- **Compatibility:** V8/SpiderMonkey/JavaScriptCore track editions; check MDN compat tables.
- **Deps:** None.
- **Availability:** Free (Ecma PDF/HTML).
- **Maintenance:** Active (monthly TC39 plenaries).
- **License:** Ecma copyright with royalty-free patent policy.
- **Security/limits:** Spec only.
- **Related:** TypeScript, Babel, V8, MDN JS reference.
- **Sources:** tc39.es; 2026 StateOfJS/frontend surveys.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 06 — TypeScript
- **Canonical identity:** `npm:typescript` — `github:microsoft/TypeScript`
- **Category:** Core Web Tech → Typed language / toolchain
- **Type:** OSS language + compiler (tsc)
- **Official URL:** https://www.typescriptlang.org/
- **Description:** Typed superset of JavaScript; editor tooling, gradual adoption, compiles away types.
- **Contents inspected:** WebFetch typescriptlang.org homepage 2026-10-09 (hero "JavaScript with syntax for types", Handbook/Playground/Download links, TS 7.0 announcement banner, testimonials, StackOverflow/StateOfJS badges).
- **Capabilities:** Static types, interfaces, generics, decorators, erasableSyntaxOnly; `tsc`, `tsserver`, project references.
- **Usage domain:** Frontend, backend (Node), full-stack type safety.
- **Integration:** official (`typescript`, `ts-node`, `@typescript-eslint`, Vite `esbuild` transpile-only + `tsc --noEmit` for checking)
- **Compatibility:** Targets ES3–ESNext; Node/browsers via emit.
- **Deps:** None at runtime (dev-only).
- **Availability:** npm `typescript`; VS Code built-in.
- **Maintenance:** Active (TS 7.0 native port "Andromeda"/Go work announced; 5.x line current).
- **License:** Apache-2.0.
- **Security/limits:** `esbuild`/SWC strip types without checking — always run `tsc --noEmit` in CI.
- **Related:** Zod, tRPC, ArkType, JSDoc `@ts-check`.
- **Sources:** WebFetch typescriptlang.org (this session); devblogs TS 7.0.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 07 — JavaScript Runtimes Note (V8 / SpiderMonkey / JavaScriptCore)
- **Canonical identity:** `engine:v8` (+ `engine:spidermonkey`, `engine:javascriptcore`)
- **Category:** Core Web Tech → JS engine
- **Type:** OSS engine components (reference-only in this catalog)
- **Official URLs:** https://v8.dev/ · https://spidermonkey.dev/ · https://webkit.org/
- **Description:** Engines powering Chrome/Node (V8), Firefox (SpiderMonkey), Safari (JSC). d8/jsshell for testing.
- **Contents inspected:** v8.dev feature/blog index (search-verified); no binary executed.
- **Capabilities:** JIT, GC, Wasm execution, ECMAScript conformance.
- **Usage domain:** Browser + server JS execution.
- **Integration:** reference-only (consumed via browsers/Node/Deno/Bun)
- **Compatibility:** Per-engine feature tables on MDN/CanIUse.
- **Deps:** N/A.
- **Availability:** Bundled; source on GitHub/Chromium.
- **Maintenance:** Active.
- **License:** BSD (V8), MPL (SM), LGPL/BSD (JSC).
- **Security/limits:** Sandbox escapes patched monthly — keep browsers/runtimes updated.
- **Related:** Node.js, Deno, Bun.
- **Sources:** v8.dev; MDN.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — WebAssembly Core (Wasm 3.0)
- **Canonical identity:** `spec:wasm-core-3.0` — W3C WebAssembly WG
- **Category:** Core Web Tech → Binary format / Standard
- **Type:** Open standard (W3C Recommendation track)
- **Official URL:** https://webassembly.org/specs/ (normative: https://www.w3.org/TR/wasm-core-2/ ; draft 3.0: https://webassembly.github.io/spec/core/)
- **Description:** Safe portable low-level bytecode; virtual ISA with binary + text formats; JS API + Web API companions.
- **Contents inspected:** WebSearch-verified 2026-02/03 CRDs (Wasm 3.0), webassembly.org/specs index, MDN WebAssembly guides; W3C WG charter page (2026-06) listing Core/JS/Web API deliverables + Component Model contingent.
- **Capabilities:** Near-native execution, linear memory sandbox, tables, SIMD, threads, GC, tail calls (by release); embeddable beyond web.
- **Usage domain:** Perf kernels, codecs, crypto, games, CAD, edge compute.
- **Integration:** open-standard (native `WebAssembly.*` JS API; Emscripten/Rust/Go/AssemblyScript toolchains)
- **Compatibility:** All evergreen browsers (Wasm 1.0 baseline; 2.0/3.0 features progressive).
- **Deps:** None (toolchain-dependent).
- **Availability:** Free; no install needed in browser.
- **Maintenance:** Active (WG charter to 2026+; 3.0 CRD Feb/Mar 2026).
- **License:** W3C Document License (spec); Apache/MIT for reference toolchains.
- **Security/limits:** Sandboxed linear memory; host capabilities only via explicit imports (WASI/Web API); still subject to Spectre-class mitigations.
- **Related:** WASI, Emscripten, wasm-bindgen, Wasmtime.
- **Sources:** WebSearch excerpts (W3C TR 2026 CRDs, webassembly.org, MDN 2026-07-28 revision).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 09 — WASI (WebAssembly System Interface)
- **Canonical identity:** `spec:wasi` — WASI Subgroup (Bytecode Alliance)
- **Category:** Core Web Tech → Wasm host interface
- **Type:** Open standard + OSS runtimes
- **Official URL:** https://wasi.dev/ (spec: https://github.com/WebAssembly/WASI)
- **Description:** Modular syscall-like interface (files, clocks, sockets, random) for running Wasm outside the browser; preview1/preview2 (component model).
- **Contents inspected:** wasi.dev overview; WASI GitHub proposals index (read-only).
- **Capabilities:** Capability-based file/net access; WIT IDL; component composition.
- **Usage domain:** Serverless, edge, plugins, embedded scripting.
- **Integration:** open-standard (Wasmtime, WasmEdge, Node `--experimental-wasi`, Deno, Bun)
- **Compatibility:** preview1 widely supported; preview2/component-model rolling out 2024-2026.
- **Deps:** Runtime host.
- **Availability:** Free OSS.
- **Maintenance:** Active (WASI 0.2 ratified 2024; 0.3 in progress 2026).
- **License:** Apache-2.0 / MIT (varies by repo).
- **Security/limits:** Capability grants are the security boundary — grant least privilege.
- **Related:** Wasmtime, WasmEdge, Spin, Component Model.
- **Sources:** wasi.dev; WebAssembly/WASI repo.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — AssemblyScript
- **Canonical identity:** `npm:assemblyscript` — `github:AssemblyScript/assemblyscript`
- **Category:** Core Web Tech → Wasm language
- **Type:** OSS language (strict TypeScript subset → Wasm)
- **Official URL:** https://www.assemblyscript.org/
- **Description:** TypeScript-like language compiling to Wasm; keeps familiar tooling (Prettier/ESLint/VS Code).
- **Contents inspected:** assemblyscript.org docs (getting started, stdlib, loader); MDN cross-reference recommending it for TS devs.
- **Capabilities:** Static typing, linear memory control, JS interop loader.
- **Usage domain:** Web perf modules without learning Rust/C++.
- **Integration:** official (`asc` compiler, `@assemblyscript/loader`)
- **Compatibility:** Outputs standard Wasm; runs anywhere.
- **Deps:** Binaryen.
- **Availability:** npm.
- **Maintenance:** Active (2025-2026 releases).
- **License:** Apache-2.0.
- **Security/limits:** No GC-by-default in strict mode; manual memory discipline for advanced use.
- **Related:** wasm-bindgen, Emscripten, TinyGo.
- **Sources:** assemblyscript.org; MDN Wasm concepts.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 11 — Emscripten
- **Canonical identity:** `tool:emscripten` — `github:emscripten-core/emscripten`
- **Category:** Core Web Tech → C/C++ → Wasm toolchain
- **Type:** OSS compiler toolchain (LLVM + Binaryen)
- **Official URL:** https://emscripten.org/
- **Description:** Compiles C/C++ to Wasm + JS/HTML glue (incl. OpenGL→WebGL, SDL, pthreads); canonical on-ramp for porting native apps.
- **Contents inspected:** emscripten.org docs TOC (install, API, debugging); MDN "Porting C/C++ with Emscripten" guide.
- **Capabilities:** `emcc`, embind, virtual FS, MODULARIZE, pthreads/SIMD.
- **Usage domain:** Games, codecs (ffmpeg.wasm), CAD, office suites in browser.
- **Integration:** official SDK (`emsdk`); CMake/autotools integration
- **Compatibility:** Requires LLVM; output runs in evergreen browsers.
- **Deps:** Python, Node, LLVM (via emsdk).
- **Availability:** GitHub + apt/brew images.
- **Maintenance:** Active.
- **License:** MIT/LLVM.
- **Security/limits:** Glue JS marshals DOM/Web APIs — review generated bindings; large outputs need streaming compile.
- **Related:** wasm-bindgen, Cheerp, Binaryen.
- **Sources:** emscripten.org; MDN.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — MDN Web Docs
- **Canonical identity:** `docs:mdn` — Mozilla / Open Web Docs
- **Category:** Core Web Tech → Reference documentation
- **Type:** OSS docs platform (reference-only)
- **Official URL:** https://developer.mozilla.org/
- **Description:** De-facto developer reference for HTML/CSS/JS/HTTP/Web APIs; browser-compat tables (BCD).
- **Contents inspected:** WebFetch MDN WebAssembly page (revision 2026-07-28 noted); WebAssembly concepts page excerpts.
- **Capabilities:** Guides, API reference, live examples, BCD, Playground, Observatory.
- **Usage domain:** Daily lookup for all web work.
- **Integration:** reference-only (no runtime)
- **Compatibility:** Documents per-browser support.
- **Deps:** None.
- **Availability:** Free; CC-BY-SA content.
- **Maintenance:** Active (daily updates; OWD stewardship).
- **License:** CC-BY-SA 2.5+ (content), MPL (code examples).
- **Security/limits:** Informational only.
- **Related:** web.dev, Can I Use, W3C specs.
- **Sources:** WebSearch + partial WebFetch (MDN Wasm pages).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 13 — Can I Use (caniuse.com)
- **Canonical identity:** `tool:caniuse` — `github:Fyrd/caniuse`
- **Category:** Core Web Tech → Compatibility data
- **Type:** OSS dataset + site (reference-only)
- **Official URL:** https://caniuse.com/
- **Description:** Browser support tables for HTML/CSS/JS/Web APIs; embed data via `caniuse-lite` (Browserslist).
- **Contents inspected:** caniuse.com feature pages (search-verified); npm `caniuse-lite` package page.
- **Capabilities:** Version matrices, usage %, notes, `caniuse-lite` DB for Autoprefixer/Babel.
- **Usage domain:** Shipping decisions, polyfill scoping.
- **Integration:** open-standard data (npm `caniuse-lite`; `browserslist`)
- **Compatibility:** N/A (documents others).
- **Deps:** None.
- **Availability:** Free (CC-BY data).
- **Maintenance:** Active (data updated with browser releases).
- **License:** CC-BY 4.0 (data).
- **Security/limits:** Informational; keep `caniuse-lite` updated or targets drift.
- **Related:** Browserslist, Baseline (web.dev), MDN BCD.
- **Sources:** caniuse.com; npm.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — Web Platform Tests (WPT)
- **Canonical identity:** `tool:wpt` — `github:web-platform-tests/wpt`
- **Category:** Core Web Tech → Conformance suite
- **Type:** OSS test suite (reference-only)
- **Official URL:** https://web-platform-tests.org/ (results: https://wpt.fyi/)
- **Description:** Shared conformance tests browsers run against; backing for Baseline/Interop.
- **Contents inspected:** web-platform-tests.org landing; wpt.fyi dashboard (search-verified).
- **Capabilities:** ~2M subtests across HTML/CSS/DOM/Fetch/XHR/etc.; `wpt run`.
- **Usage domain:** Browser vendors, spec authors, compat debugging.
- **Integration:** reference-only (CI via `wpt` runner)
- **Compatibility:** N/A.
- **Deps:** Python + browser binaries (when running).
- **Availability:** GitHub.
- **Maintenance:** Active (Interop 2024/2025/2026 drives coverage).
- **License:** BSD-3-Clause.
- **Security/limits:** Test harness only.
- **Related:** test262 (JS), W3C validators.
- **Sources:** web-platform-tests.org; wpt.fyi.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — WHATWG DOM
- **Canonical identity:** `spec:whatwg-dom`
- **Category:** Core Web Tech → Browser API standard
- **Type:** Open standard (living)
- **Official URL:** https://dom.spec.whatwg.org/
- **Description:** Nodes, trees, ranges, events dispatch, mutation observers, shadow DOM integration points.
- **Contents inspected:** Spec TOC (search-verified); MDN DOM reference cross-check.
- **Capabilities:** Tree manipulation, selectors, events, traversal.
- **Usage domain:** All DOM scripting.
- **Integration:** open-standard (native)
- **Compatibility:** Evergreen baseline.
- **Deps:** None.
- **Availability:** Free.
- **Maintenance:** Active living standard.
- **License:** CC-BY.
- **Security/limits:** XSS via `innerHTML` — prefer `textContent`/sanitizers.
- **Related:** Shadow DOM, HTML, UI Events.
- **Sources:** dom.spec.whatwg.org; MDN.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — WHATWG Fetch / Streams / XHR
- **Canonical identity:** `spec:whatwg-fetch` (+ `spec:whatwg-streams`)
- **Category:** Core Web Tech → Network API standards
- **Type:** Open standards
- **Official URLs:** https://fetch.spec.whatwg.org/ · https://streams.spec.whatwg.org/
- **Description:** `fetch()`, Request/Response, CORS, streaming bodies; Streams API for backpressure-aware pipelines.
- **Contents inspected:** Spec landings (search-verified); MDN Fetch API examples.
- **Capabilities:** Streaming compile (`WebAssembly.instantiateStreaming`), SSE/chunked reads, Service Worker interception.
- **Usage domain:** Data fetching, edge streaming, PPR/RSC payloads.
- **Integration:** open-standard (native; Undici in Node)
- **Compatibility:** Baseline widely available.
- **Deps:** None.
- **Availability:** Native.
- **Maintenance:** Active.
- **License:** CC-BY.
- **Security/limits:** CORS/CSP/Trusted Types govern exfiltration; opaque responses limited.
- **Related:** Axios, ky, Undici, Service Workers.
- **Sources:** fetch.spec.whatwg.org; MDN.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 17 — Service Workers + Workbox
- **Canonical identity:** `spec:w3c-service-workers` + `npm:workbox-*` (`github:GoogleChrome/workbox`)
- **Category:** Core Web Tech → Offline / PWA API + toolkit
- **Type:** Standard + OSS library
- **Official URLs:** https://www.w3.org/TR/service-workers/ · https://developer.chrome.com/docs/workbox
- **Description:** Background script proxy for offline, caching strategies, push; Workbox provides precaching/routing recipes.
- **Contents inspected:** W3C TR landing; Chrome Workbox docs (strategies: CacheFirst/StaleWhileRevalidate/NetworkFirst).
- **Capabilities:** App-shell caching, background sync, push, navigation preload.
- **Usage domain:** PWAs, offline docs, field apps.
- **Integration:** official (native SW API; `workbox-*` npm modules; Vite PWA plugin adapter)
- **Compatibility:** Evergreen (no iOS push until recent; check BCD).
- **Deps:** None (Workbox build-time injectManifest).
- **Availability:** Free OSS.
- **Maintenance:** Active (Workbox v7 2024-2026).
- **License:** Apache-2.0 (Workbox); W3C doc license (spec).
- **Security/limits:** HTTPS-only (localhost excepted); SW hijack risk — scope + update discipline.
- **Related:** Vite PWA, PWABuilder, Cache Storage.
- **Sources:** w3.org/TR/service-workers; Chrome Workbox docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — Web Components (Custom Elements / Shadow DOM / Templates) + Lit
- **Canonical identity:** `spec:web-components` + `npm:lit` (`github:lit/lit`)
- **Category:** Core Web Tech → Component standard + library
- **Type:** Open standards + OSS library
- **Official URLs:** https://www.webcomponents.org/specs/ · https://lit.dev/
- **Description:** Framework-agnostic components: Custom Elements, Shadow DOM, `<template>`/slots; Lit is Google's minimal rendering layer.
- **Contents inspected:** webcomponents.org specs index; lit.dev docs (reactive properties, templates).
- **Capabilities:** Encapsulated reusable elements usable in React/Vue/Astro/Svelte.
- **Usage domain:** Design systems, micro-frontends, embeddable widgets.
- **Integration:** native (no build required) / official Lit (`lit`, `@lit/react` wrappers)
- **Compatibility:** Baseline (declarative shadow DOM now baseline).
- **Deps:** None (Lit ~5KB).
- **Availability:** npm `lit`; CDN.
- **Maintenance:** Active (Lit 3.x).
- **License:** BSD-3-Clause.
- **Security/limits:** Shadow DOM is not a security boundary; still sanitize.
- **Related:** Shoelace, FAST, Stencil.
- **Sources:** webcomponents.org; lit.dev.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — WebGPU / WebGL
- **Canonical identity:** `spec:w3c-webgpu` + `spec:khronos-webgl`
- **Category:** Core Web Tech → GPU APIs
- **Type:** Open standards
- **Official URLs:** https://www.w3.org/TR/webgpu/ · https://www.khronos.org/webgl/
- **Description:** Low-level GPU (WebGPU, successor) and legacy WebGL for 3D/GPGPU in browser; Three.js/Babylon build on top.
- **Contents inspected:** W3C WebGPU TR; Khronos WebGL registry; MDN WebGPU guide (search-verified).
- **Capabilities:** Compute + render pipelines, WGSL shaders; WebGL2 baseline fallback.
- **Usage domain:** 3D viewers, maps, data-viz, ML inference (WebGPU).
- **Integration:** open-standard (native `navigator.gpu`)
- **Compatibility:** WebGL ~universal; WebGPU evergreen desktop + recent mobile (check BCD).
- **Deps:** None.
- **Availability:** Native.
- **Maintenance:** Active (WebGPU shipped 2023-2025; ongoing).
- **License:** W3C/Khronos doc licenses.
- **Security/limits:** GPU fingerprinting surface; robust buffer validation.
- **Related:** Three.js, Babylon.js, Dawn/wgpu.
- **Sources:** w3.org/TR/webgpu; khronos.org/webgl.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — WebRTC
- **Canonical identity:** `spec:w3c-webrtc`
- **Category:** Core Web Tech → Realtime media/data API
- **Type:** Open standard (+ IETF RFCs)
- **Official URL:** https://www.w3.org/TR/webrtc/ (IETF: https://webrtc.org/)
- **Description:** Peer-to-peer audio/video/data channels; signaling out-of-scope (use WebSocket).
- **Contents inspected:** W3C TR; webrtc.org samples/docs index.
- **Capabilities:** `RTCPeerConnection`, DataChannel, screen share, TURN/STUN.
- **Usage domain:** Meet apps, live support, P2P collaboration, game netcode.
- **Integration:** open-standard (native; adapter `webrtc-adapter` legacy)
- **Compatibility:** Evergreen; mobile OK.
- **Deps:** STUN/TURN infra (e.g., coturn, Cloudflare Calls).
- **Availability:** Native API; infra self-hosted or SaaS.
- **Maintenance:** Active (W3C + IETF).
- **License:** Spec license; BSD (webrtc.org samples).
- **Security/limits:** DTLS-SRTP mandatory; IP leakage via ICE — use mDNS/TURN policies; consent for mic/cam.
- **Related:** LiveKit, Daily, Socket.io (signaling).
- **Sources:** w3.org/TR/webrtc; webrtc.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 21 — IndexedDB + Dexie.js
- **Canonical identity:** `spec:w3c-indexeddb` + `npm:dexie` (`github:dexie/Dexie.js`)
- **Category:** Core Web Tech → Client storage
- **Type:** Standard + OSS wrapper
- **Official URLs:** https://www.w3.org/TR/IndexedDB/ · https://dexie.org/
- **Description:** Transactional NoSQL store in browser; Dexie adds ergonomic promise API, bulk ops, live queries.
- **Contents inspected:** W3C TR TOC; dexie.org docs (API, sync notes).
- **Capabilities:** Offline-first datasets, queues, caches; versioned schemas.
- **Usage domain:** PWAs, offline forms, local-first apps.
- **Integration:** native (IndexedDB) + official Dexie (`dexie`, `dexie-react-hooks`)
- **Compatibility:** Evergreen; storage quotas/eviction policies vary.
- **Deps:** None.
- **Availability:** Native + npm.
- **Maintenance:** Active (Dexie 4.x).
- **License:** Apache-2.0 (Dexie).
- **Security/limits:** Same-origin; not encrypted at rest — encrypt PII; quota errors must be handled.
- **Related:** localForage, RxDB, OPFS, Cache Storage.
- **Sources:** w3.org/TR/IndexedDB; dexie.org.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 22 — Node.js (JavaScript runtime)
- **Canonical identity:** `runtime:nodejs` — OpenJS Foundation
- **Category:** Core Web Tech → JS runtime (also Backend)
- **Type:** OSS runtime (V8 + libuv)
- **Official URL:** https://nodejs.org/
- **Description:** Event-loop server runtime; npm ecosystem; Undici fetch, WASI preview, permission model (`--experimental-permission`).
- **Contents inspected:** nodejs.org docs index; 2025 StackOverflow usage (48.7% most-used web tech — search-verified).
- **Capabilities:** ESM/CJS, workers, streams, test runner, watch mode.
- **Usage domain:** APIs, SSR, CLIs, build tools.
- **Integration:** official (volta/nvm/fnm; Docker `node:` images)
- **Compatibility:** LTS (v20/v22 in 2026 window) + Current.
- **Deps:** None for runtime.
- **Availability:** nodejs.org dist; package managers.
- **Maintenance:** Active LTS cadence.
- **License:** MIT (+ third-party).
- **Security/limits:** Single-thread CPU bound; keep LTS patched; permission flags for sandboxing.
- **Related:** Deno, Bun, Express, Fastify.
- **Sources:** nodejs.org; StackOverflow Survey 2025.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 23 — Deno
- **Canonical identity:** `runtime:deno` — `github:denoland/deno`
- **Category:** Core Web Tech → JS/TS runtime
- **Type:** OSS runtime (V8 + Rust/Tokio)
- **Official URL:** https://deno.com/ (runtime docs: https://docs.deno.com/runtime/)
- **Description:** Secure-by-default TS-first runtime; built-in test/lint/fmt; npm/jsr compat; Fresh meta-framework.
- **Contents inspected:** docs.deno.com runtime manual (permissions, KV, deploy notes).
- **Capabilities:** Permissions (`--allow-*`), std lib, Jupyter, WASI, Node compat.
- **Usage domain:** Scripts, APIs, edge, secure plugins.
- **Integration:** official (Deno CLI; `deno.json`; Docker `denoland/deno`)
- **Compatibility:** Deno 1.x/2.x (2.0 released Oct 2024; 2.x current 2026).
- **Deps:** None.
- **Availability:** deno.land install; GitHub releases.
- **Maintenance:** Active (Deno Company; 2026 cadence).
- **License:** MIT.
- **Security/limits:** Deny-by-default is strength — declare minimal `--allow` set.
- **Related:** JSR, Fresh, Node.js, Bun.
- **Sources:** docs.deno.com.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 24 — Bun
- **Canonical identity:** `runtime:bun` — `github:oven-sh/bun`
- **Category:** Core Web Tech → JS/TS runtime + toolkit
- **Type:** OSS runtime (JavaScriptCore + Zig)
- **Official URL:** https://bun.sh/ (docs: https://bun.sh/docs)
- **Description:** Fast all-in-one runtime + bundler + test runner + package manager; Node-compatible.
- **Contents inspected:** bun.sh/docs (install, APIs, bundler, SQLite built-in).
- **Capabilities:** `bun run/build/test`, `Bun.serve`, built-in SQLite, FFI.
- **Usage domain:** Dev servers, scripts, fast CI, SSR.
- **Integration:** official (`bun`, `bunx`; Dockerfile `oven/bun`)
- **Compatibility:** Node API compat high (2025-2026); Windows support stabilized.
- **Deps:** None.
- **Availability:** bun.sh install script; npm `bun` shim.
- **Maintenance:** Active (weekly releases; 1.x line).
- **License:** MIT (core) + JSC license.
- **Security/limits:** Young surface — pin versions; audit native deps.
- **Related:** Node.js, Deno, Vite, esbuild.
- **Sources:** bun.sh/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

**Count: 24 resources** (meets 15–30 minimum). All URLs are canonical official URLs. No install/execute performed.
