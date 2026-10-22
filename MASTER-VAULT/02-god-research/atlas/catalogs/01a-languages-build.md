# OMNISCIENT RESOURCE ATLAS — Catalog 01a
## Languages & browser technologies · Build, compile & package tooling

- **Researcher:** Workstream #1 (subagent 7663c8a1)
- **Verification date:** 2026-10-10
- **Mission scope:** Part 3.1 (Languages and browser technologies) and Part 3.4 (Build, compile, and package tooling)
- **Method:** Read-only web research. No installation, execution, building, ranking, or recommending. Records describe what the resource IS (implementation vs claims), not marketing.
- **Verification labels used:** Verified / Partially verified / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved
- **Cross-reference (not re-researched):** facebook/astryx (@astryxdesign/cli — no MCP server, verified 2026-08-11), shadcn MCP, upstash/context7, code-yeongyu/oh-my-openagent, anomalyco/opencode, opencode.ai docs.

### Search themes run (discovery log)
1. ECMAScript 2026 features / TC39 finished proposals → ES2026 approved 2026-06-30; Temporal Stage 4
2. TypeScript native Go port status → TS 7.0 GA 2026-07-08 (Go port, "Corsa"); community Rust port ferrotype/tsr
3. WebAssembly Component Model / WASI 0.3 → WASI 0.3.0 ratified 2026-06-11; 0.3.1/0.3.2 schedule
4. Node.js 2026 release lines → 24 "Krypton" Active LTS; 26 Current→LTS 2026-10-28; annual cycle from 27
5. Bun 2026 → 1.4.1, Anthropic acquisition Dec 2025, Zig→Rust rewrite, Bun.SQL/Redis built-ins, Cruller fork
6. Deno 2 2026 → 2.7.x, npm compatibility, JSR, permissions model, Deno KV/Deploy
7. Vite/Rolldown → Vite 8 (Mar 2026) unified on Rolldown (Rust); Oxc transformer; Lightning CSS; registry.vite.dev
8. Turbopack/Rspack/webpack/esbuild → Turbopack Next.js-only default (Next 16); Rspack webpack-compatible; webpack 5.x maintenance; esbuild transform-layer
9. npm/pnpm/yarn/bun package managers → npm 11, pnpm 10/11 (build scripts blocked by default), Yarn Berry 4.x, Yarn Classic frozen
10. ESLint/Biome/Oxlint/Ruff → ESLint 10.8 flat config; Biome 2.x (Rust); oxlint 1.x + oxfmt; Vite+ (vite-plus) unified CLI
11. Tailwind v4 / Lightning CSS / PostCSS / dart-sass → Tailwind v4.3.x CSS-first @theme; Lightning CSS engine; PostCSS still the plugin host
12. SWC/Oxc/Babel → SWC production-proven (Deno migrating to Oxc); Oxc Q3-2026 push to 1.0; Babel plugin-ecosystem compatibility
13. axe-core/WCAG/ARIA/a11y toolchain → WCAG 2.2 AA floor; axe-core engine; pa11y; Lighthouse; eslint-plugin-jsx-a11y; screen readers
14. i18next/FormatJS/Lingui/Tolgee/next-intl → i18next dominant; ICU MessageFormat variants; Tolgee OSS in-context; Intlayer/Paraglide lighter alternatives
15. Web/service/shared workers & worklets → dedicated/shared/service worker taxonomy; CSP worker-src; Comlink RPC pattern
16. WebGPU → all major browsers shipping (Chrome 113+, Safari 26, Firefox 141/145); three.js r170+ WebGPURenderer; Babylon 8 WGSL
17. WebRTC/WebTransport → WebRTC all browsers; WebTransport Baseline 2026 (newly available), HTTPS-only; Socket.IO 4.8.4 with WebTransport transport
18. Turborepo/Nx/Changesets/Lerna → pnpm+Turborepo+Changesets default; Lerna life support; Nx 23.x; semantic-release vs release-please both active
19. JSR/esm.sh/unpkg/jsDelivr/cdnjs → JSR TS-native + Sigstore provenance; esm.sh no-build ESM CDN (npm/JSR/GitHub); jsDelivr best general CDN
20. tsx/ts-node/nodemon/PM2 → tsx (esbuild) modern default; ts-node ESM loader broken on Node 20+; nodemon dev-only; PM2 active supervisor
21. Corepack/Volta/fnm/mise/nvm → Volta stood down (mise recommended successor); Corepack experimental in Node 24, removed 25+; fnm personal default; pnpm 11 self-manages versions
22. Renovate/Dependabot/Socket/osv-scanner → Renovate flexible automerge; Dependabot GitHub-native; Socket behavioral supply-chain; osv-scanner OSV DB; axios Mar-2026 hijack incident
23. knip/depcheck/publint/attw/ncu → knip (unused exports/deps) replacing depcheck; publint + attw package validation (built into tsdown)
24. husky/lint-staged/lefthook → husky+lint-staged standard; lefthook (Go) faster parallel alternative; Biome --staged flag
25. uv/pip/Poetry/PDM/Hatch/pipx/Rye → uv (Astral, Rust) default for new Python; Rye deprecated→uv; uv.lock committed; uv 0.11.x; pip still baseline
26. Orval/openapi-generator/GraphQL Codegen → Orval 8.x TS clients; openapi-fetch in maintenance (2025-12-29); Hey API; Kiota (Microsoft); Speakeasy AGPL
27. ws/socket.io/axios/ky/undici → ws RFC-6455; Socket.IO 4.8.4; axios still dominant; ky/redaxios fetch-based; undici is Node's fetch engine
28. V8/SpiderMonkey/JavaScriptCore/Hermes/QuickJS → V8 (Chrome/Node/workerd), JSC (Safari/Bun), SpiderMonkey (Firefox/WinterJS), Hermes (React Native), QuickJS (LLRT/edge)
29. IndexedDB/OPFS/Cache API/localStorage → OPFS sync handles worker-only; Cache API for HTTP responses; IndexedDB structured; all share origin quota
30. Web Components/DSD → custom elements + shadow DOM widely available; declarative shadow DOM Baseline widely available 2026-08-20; ElementInternals form-associated
31. WHATWG/W3C/TC39/IETF standards → HTML Living Standard; CSS Snapshot 2026; ECMA-262 ES2026; IETF QUIC/HTTP-3
32. tsup/tsdown/unbuild/parcel → tsup unmaintained (use tsdown); tsdown Rolldown+Oxc library bundler with publint/attw; unbuild for complex cases
33. Stylelint/HTMLHint/markdownlint/commitlint/cspell/editorconfig/dprint/Ruff → all active in 2026 stacks; Ruff (Astral) Python lint+format
34. workerd/LLRT/WinterJS/edge → workerd (Cloudflare, V8 isolates, open source); LLRT (AWS, QuickJS, Lambda); WinterJS (SpiderMonkey, WinterCG)
35. axios/ky/redaxios/tanstack-fetch → fetch-native trend; many ADRs replacing axios with fetch wrappers (2026)

### Primary sources inspected directly (browser.open)
- https://github.com/rolldown/rolldown — README (MIT, VoidZero, Rollup-compatible Rust bundler, uses oxc; 13,968 stars)
- https://github.com/oxc-project/oxc — README (MIT, "Oxidation Compiler" Rust toolchain: parser/transformer/minifier/resolver/oxlint/oxfmt; 22,982 stars)
- https://github.com/biomejs/biome — README (MIT/Apache-2.0, Rust formatter+linter for JS/TS/JSX/JSON/CSS/GraphQL/Markdown/YAML/SCSS; 25,912 stars)

---

## 1. Languages and browser technologies

### 1.1 Core languages, language specs, and WebAssembly

### ECMAScript (JavaScript) — ECMA-262 / TC39
- **Canonical identity:** ECMA-262, maintained by Ecma TC39
- **Category:** Languages & browser tech › Languages & standards
- **Type:** Language specification (standard)
- **Official URL:** https://tc39.es/ecma262/ (spec); https://github.com/tc39/ecma262 (spec repo)
- **Description:** The standardized specification of the JavaScript language. Annual edition cycle; ECMAScript 2026 (17th edition) approved 2026-06-30. Adds: Temporal API (Stage 4, Mar 2026), `Math.sumPrecise`, `Iterator.concat`, `Array.fromAsync`, `Error.isError`, `Map`/`WeakMap` getOrInsert-style defaults, `Uint8Array` base64/hex methods, `JSON.parse` source-text reviver parameter, `JSON.rawJSON`, decorators.
- **Contents inspected:** Search-result excerpts of InfoWorld approval article, Socket.dev TC39 March-2026 report, two 2026 guides listing ES2026 features; babel/proposals tracking table.
- **Actual capabilities:** Defines language semantics; engines (V8, SpiderMonkey, JavaScriptCore) implement it. Test262 is the conformance suite.
- **Usage domain:** All JavaScript execution environments (browsers, Node.js, Deno, Bun, edge runtimes).
- **Integration method:** Implemented by engines; consumed via language use. Not installed.
- **Dependencies:** Not applicable.
- **Availability:** Specification freely available; implementations ship in browsers/runtimes.
- **Maintenance:** Active — annual editions; proposals tracked in tc39/proposals.
- **License:** Not verified (Ecma royalty-free policy; exact doc license not checked).
- **Limitations:** Spec approval ≠ engine implementation; feature availability varies by engine version (e.g., Temporal shipping in Firefox 139+/Chrome 144 per 2026 reports — single-source claims).
- **Related resources:** TypeScript, Test262, V8, SpiderMonkey, JavaScriptCore, Babel, SWC, Oxc.
- **Sources:** https://www.infoworld.com/article/4193461/ecmascript-2026-specification-approved.html ; https://socket.dev/blog/tc39-advances-temporal-to-stage-4 ; https://github.com/babel/proposals
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (spec approval corroborated by 2+ outlets; engine-ship claims single-sourced)

### Temporal API
- **Canonical identity:** TC39 proposal-temporal (now part of ECMA-262 / ES2026)
- **Category:** Languages & browser tech › Languages & standards
- **Type:** Standard library API (spec)
- **Official URL:** https://tc39.es/proposal-temporal/docs/ (proposal docs; spec now merged into ECMA-262)
- **Description:** Modern date/time API replacing `Date`: immutable types (`PlainDate`, `ZonedDateTime`, `Instant`, `Duration`, etc.), built-in time-zone and calendar support. Reached TC39 Stage 4 in March 2026; included in ES2026. Described by champion as the biggest addition to ECMAScript since ES2015.
- **Contents inspected:** Search excerpts (Socket.dev TC39 report; 2026 guides noting Firefox 139/Chrome 144 shipping).
- **Actual capabilities:** Date/time arithmetic, time-zone conversion, ISO/calendar-aware types, no mutation.
- **Usage domain:** Any JS environment implementing ES2026; polyfills exist (not verified in depth).
- **Integration method:** Built-in global (`Temporal`) where implemented; otherwise polyfill library.
- **Dependencies:** IANA time-zone data supplied by host environment.
- **Availability:** Spec-final; engine rollout in progress through 2026.
- **Maintenance:** Active (TC39).
- **License:** Not applicable (spec).
- **Limitations:** Not yet universal across engines; `Date` remains for legacy interop.
- **Related resources:** ECMA-262, ECMA-402 (Intl), date-fns/luxon/dayjs (libraries, out of scope for this workstream).
- **Sources:** https://socket.dev/blog/tc39-advances-temporal-to-stage-4 ; https://javascript.plainenglish.io/8-new-javascript-features-that-finally-fix-what-was-always-broken-ccfb91e7cc27?gi=885d54b5656b
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (Stage 4 corroborated; per-browser ship versions single-sourced)

### TypeScript 7 (native Go compiler)
- **Canonical identity:** microsoft/TypeScript — v7.x "Corsa" (native Go port); 6.x "Strada" is the last JS-based line
- **Category:** Languages & browser tech › Languages & standards
- **Type:** Programming language + compiler toolchain (CLI binary + language server)
- **Official URL:** https://www.typescriptlang.org (canonical site); repo: github.com/microsoft/TypeScript
- **Description:** Typed superset of JavaScript. TypeScript 7.0 shipped GA 2026-07-08 as a methodical port of the compiler/language service from TypeScript to Go (project "tsgo", preview package `@typescript/native-preview`). Reported 8–12× faster full builds (~10× headline; VS Code repo ~125.7s→10.6s per Microsoft). Type-checking semantics intended identical to 6.x. Programmatic compiler API (ts.createProgram etc.) NOT available in 7.0 — targeted for 7.1; API-dependent tools (typescript-eslint, ts-morph, Vue/Svelte/Astro template checkers) stay on 6.x meanwhile. Incremental build artifacts incompatible between JS tsc and native tsc.
- **Contents inspected:** Search excerpts: TS 7 migration notes (dev.to, monorepo measurements 38s→4.1s), syntackle.com Go-port writeup, dotfiles ts7-release reference, seed repo TS7_NATIVE_PREP (measured 3.4–6.1× on real repos).
- **Actual capabilities:** Static type checking, type-stripping emit, language server (editor), project build orchestration (`tsc --build`), declaration emit.
- **Usage domain:** Type-safe application and library development across web frontend/backend; editor intelligence.
- **Integration method:** `npm install -D typescript`; `tsc` CLI; editor extensions (VS Code dedicated TS 7 extension); build tools consume it.
- **Dependencies:** Go toolchain only at build time for the TS team; distributed as native binaries per platform via npm.
- **Availability:** npm `typescript` package (7.x); `@typescript/native-preview` discontinued at GA; TS 6.x line maintained for API consumers.
- **Maintenance:** Active (Microsoft).
- **License:** Apache-2.0 (not re-verified this session; long-standing).
- **Limitations:** No stable programmatic API in 7.0; Go binary distribution per-platform (no more pure-JS fallback in the main package); incremental cache incompatibility across 6/7.
- **Related resources:** tsgo (preview), typescript-eslint, tsx, Oxc transformer, amaro, ferrotype/tsr (community Rust port, Phase 4/7 — CLI works, no LSP yet), Deno (native TS).
- **Sources:** https://dev.to/zeybek/typescript-7-migration-notes-from-a-monorepo-1k04 ; https://syntackle.com/blog/typescript-go-port/ ; https://github.com/remcostoeten/dotfiles/blob/HEAD/configs/agents/skills/incremental-typescript/references/ts7-release.md ; https://github.com/mustardseednetworks/seed/blob/HEAD/docs/TS7_NATIVE_PREP.md ; https://github.com/ferrotype/tsr
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (GA date, codenames, speedup range, API gap all corroborated by 3+ independent sources; official announcement URL not captured)

### WebAssembly (core spec — Wasm 3.0)
- **Canonical identity:** WebAssembly Core Specification; community group WebAssembly/spec
- **Category:** Languages & browser tech › Languages & standards
- **Type:** Binary instruction format + virtual machine specification (standard)
- **Official URL:** https://webassembly.org ; spec repo: github.com/WebAssembly/spec
- **Description:** Portable low-level bytecode executed in browsers and standalone runtimes. Wasm 3.0 completed 2025-09-17 as a rolling "live standard"; includes memory64, GC, exceptions, tail calls, function references, relaxed SIMD, extended-const, multi-memory. Threads (shared-everything) still unimplemented in Wasmtime 47 per 2026 reports. wasi-threads proposal withdrawn Aug 2023.
- **Contents inspected:** Search excerpts (WASI release docs; research notes citing webassembly.org Wasm 3.0 completion; wasmtime 47 feature matrix notes).
- **Actual capabilities:** Near-native sandboxed execution; language target for Rust, Go, C/C++, Python (via Emscripten/Pyodide), AssemblyScript; runs in browsers (JS API) and server runtimes.
- **Usage domain:** Browser compute (games, codecs, crypto, SQLite-in-browser), plugins, edge compute, portable modules.
- **Integration method:** Compiled `.wasm` modules loaded via JS `WebAssembly` API in browsers; standalone runtimes execute WASI components.
- **Dependencies:** Producing toolchain per source language (Emscripten, wasm-pack, AssemblyScript, TinyGo, etc.).
- **Availability:** All modern browsers; many standalone runtimes.
- **Maintenance:** Active (W3C WebAssembly WG + Community Group).
- **License:** Not applicable (spec; Apache-2.0/CC0 for spec text — not re-verified).
- **Limitations:** No DOM access (browser JS interop required); threading story incomplete; 4GB memory limit without memory64.
- **Related resources:** WASI, Component Model, Emscripten, wasm-bindgen, AssemblyScript, Wasmtime, WasmEdge, Wasmer.
- **Sources:** https://github.com/michaels1011/ephemora-cell/blob/HEAD/docs/threads_roadmap.md (citing webassembly.org + wasmtime 47) ; https://github.com/yaasiinmd1/rust-project-goals/blob/HEAD/src/2026/wasm-components.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (3.0 completion + feature list corroborated; threads status from a single detailed source)

### WASI (WebAssembly System Interface)
- **Canonical identity:** WebAssembly/WASI — Preview 1 (0.1), Preview 2 (0.2), Preview 3 (0.3)
- **Category:** Languages & browser tech › Languages & standards
- **Type:** System interface specification (standard)
- **Official URL:** https://wasi.dev ; repo: github.com/WebAssembly/WASI
- **Description:** Standardized capability-based syscall interface for Wasm outside the browser (files, clocks, sockets, HTTP). 0.1: POSIX-like, witx IDL. 0.2 (Jan 2024): rebuilt on Component Model with WIT, modular `wasi:cli`, `wasi:http`, `wasi:sockets`. 0.3.0 ratified 2026-06-11: async becomes native to the Component Model canonical ABI (`async func`, `stream<T>`, `future<T>`); old `wasi:io` package removed. 0.3.1 shipped 2026-08-11; 0.3.2 scheduled 2026-10-13; quarterly cadence into 2027. Security model: zero ambient authority, capabilities granted by host.
- **Contents inspected:** Search excerpts of WebAssembly/WASI docs/Release.md (release schedule), Medium WASI 0.3 analysis, research report table.
- **Actual capabilities:** Portable CLI/HTTP/server components across Wasmtime, WasmEdge, Wasmer, WAMR, wazero, wasmi.
- **Usage domain:** Serverless/edge functions, plugins, portable CLIs, sandboxed compute.
- **Integration method:** Compile to `wasm32-wasip2`/`wasip3` targets; run under a WASI-capable host.
- **Dependencies:** Language toolchain with WASI target (Rust tier-3 wasip3 target; Go/TinyGo; C via wasi-sdk).
- **Availability:** Runtimes listed above; Rust wasi 0.3 target tier 3 (not via rustup stable per 2026 notes).
- **Maintenance:** Active (WASI Subgroup; Bytecode Alliance).
- **License:** Not applicable (spec; Apache-2.0/CC0 — not re-verified).
- **Limitations:** 0.3 ecosystem young (Wasmtime 46+ enables by default); async host support still rolling out; Rust target maturity tier 3.
- **Related resources:** Component Model/WIT, Wasmtime, WasmEdge, Wasmer, WAMR, wazero, StarlingMonkey, Spin, Fermyon.
- **Sources:** https://github.com/webassembly/wasi/blob/HEAD/docs/Release.md ; https://medium.com/@thesoftix.com/webassembly-components-and-wasi-0-3-a-practical-smb-pilot-path-03a421011087 ; https://github.com/asterrzep/astra/blob/HEAD/Documentacion/research/RESEARCH_REPORT.md
- **Verification date:** 2026-10-10
- **Confidence:** Verified (release dates/schedule from primary repo docs)

### WebAssembly Component Model + WIT
- **Canonical identity:** WebAssembly/component-model (spec); WIT = WebAssembly Interface Types (IDL)
- **Category:** Languages & browser tech › Languages & standards
- **Type:** Interface/ABI specification + IDL (standard)
- **Official URL:** https://component-model.bytecodealliance.org ; repo: github.com/WebAssembly/component-model
- **Description:** Higher-level composition layer over core Wasm modules: components with typed interfaces described in WIT, canonical ABI for cross-language calls, resource types with ownership, shared-nothing linking. Enables Rust/Go/Python/JS components to interoperate through shared WIT worlds. Formal standardization expected to begin after the 0.3/1.0 cycle (per 2026 industry notes). WIT example pattern: `package astra:math; interface linear-algebra { ... }`.
- **Contents inspected:** Search excerpts (research report; Hexana IDE issue; Rust 2026 goals doc noting missing first-class component tooling).
- **Actual capabilities:** Language-agnostic component composition; capability-safe sandboxing via WASI worlds.
- **Usage domain:** Plugin systems, portable services, edge functions, polyglot microservices.
- **Integration method:** `wit-bindgen` generates guest/host bindings; `wasm-tools compose` links components.
- **Dependencies:** Component-aware toolchain + runtime (Wasmtime 46+).
- **Availability:** Tooling maturing; spec pre-1.0.
- **Maintenance:** Active (Bytecode Alliance).
- **License:** Not applicable (spec).
- **Limitations:** Pre-standardization; async model changed under WASI 0.3; tooling churn.
- **Related resources:** WASI, wit-bindgen, wasm-tools, Wasmtime, jco (JS component tooling).
- **Sources:** https://github.com/yaasiinmd1/rust-project-goals/blob/HEAD/src/2026/wasm-components.md ; https://github.com/asterrzep/astra/blob/HEAD/Documentacion/research/RESEARCH_REPORT.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### AssemblyScript
- **Canonical identity:** AssemblyScript/assemblyscript
- **Category:** Languages & browser tech › Languages & standards
- **Type:** Programming language + compiler (TypeScript-like → WebAssembly)
- **Official URL:** https://www.assemblyscript.org ; repo: github.com/AssemblyScript/assemblyscript
- **Description:** A TypeScript-flavored language that compiles to WebAssembly (strict subset: no closures over heap GC types, explicit memory model). Used for Wasm modules authored by JS/TS developers.
- **Contents inspected:** Search mentions only (toolchain listings).
- **Actual capabilities:** Compiles `.ts`-like sources to `.wasm` with WASI or bare imports; loader library for JS interop.
- **Usage domain:** Browser Wasm modules, WinterJS/Wasm-target server code.
- **Integration method:** `asc` compiler CLI; npm package `assemblyscript`.
- **Dependencies:** Node.js for the compiler; binaryen (bundled).
- **Availability:** npm; open source.
- **Maintenance:** Active (community; slower cadence than 2021 peak — not precisely verified).
- **License:** Apache-2.0 (not re-verified this session).
- **Limitations:** Strict language subset; GC proposal integration ongoing; smaller ecosystem than Rust/C++ Wasm.
- **Related resources:** Emscripten, wasm-bindgen, wasm-pack, WASI.
- **Sources:** Secondary mentions in Wasm toolchain research (no dedicated primary read this session).
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (existence/capabilities long-established; 2026 maintenance state not directly verified)

### Emscripten
- **Canonical identity:** emscripten-core/emscripten
- **Category:** Languages & browser tech › Languages & standards
- **Type:** Compiler toolchain (C/C++ → WebAssembly/JavaScript)
- **Official URL:** https://emscripten.org ; repo: github.com/emscripten-core/emscripten
- **Description:** LLVM-to-WebAssembly compiler producing Wasm + JS glue for browsers and Node. Powers Pyodide (CPython-in-Wasm), many game/codec ports, SQLite WASM builds. Emits Emscripten runtime with virtual FS, SDL/OpenGL shims.
- **Contents inspected:** Search mentions (Pyodide-in-Workers architecture; SQLite WASM + OPFS pattern).
- **Actual capabilities:** Compiles C/C++ to wasm with JS interop bindings (Embind/WebIDL), pthreads (SharedArrayBuffer), virtual filesystem layers (including OPFS-backed).
- **Usage domain:** Porting native codebases to web; language runtimes in Wasm (Python, Ruby, Lua).
- **Integration method:** `emcc` compiler driver; CMake toolchain file.
- **Dependencies:** LLVM/Clang (bundled), Node.js, Python (build).
- **Availability:** Open source; SDK downloads.
- **Maintenance:** Active.
- **License:** MIT/Apache-2.0 dual for compiler; Emscripten runtime under MIT/Apache — exact split not re-verified.
- **Limitations:** Large runtime glue; pthreads require cross-origin isolation headers; not a general WASI toolchain (own ABI).
- **Related resources:** wasm-bindgen, wasm-pack, WASI SDK, Pyodide, wa-sqlite.
- **Sources:** Secondary mentions (Workers Python runtime analysis; OPFS/SQLite research notes).
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### wasm-bindgen
- **Canonical identity:** wasm-bindgen/wasm-bindgen (Rust project)
- **Category:** Languages & browser tech › Languages & standards
- **Type:** Library + CLI facilitating JS↔Wasm interop (Rust)
- **Official URL:** https://github.com/wasm-bindgen/wasm-bindgen ; docs at rustwasm.github.io/wasm-bindgen
- **Description:** Generates bindings between Rust-compiled Wasm and JavaScript: exposes Rust structs/functions to JS and imports JS APIs into Rust. Companion `wasm-pack` builds npm-publishable packages.
- **Contents inspected:** Search mentions (wasm-bindgen output referenced in biome/oxlint interop notes).
- **Actual capabilities:** `#[wasm_bindgen]` macros; JS glue generation; TypeScript declaration emit; works with bundlers.
- **Usage domain:** Rust→web libraries (e.g., SWC/Oxc napi-adjacent builds, parsers, crypto).
- **Integration method:** Cargo dependency + `wasm-pack build` or `wasm-bindgen` CLI post-processing.
- **Dependencies:** Rust toolchain targeting `wasm32-unknown-unknown`.
- **Availability:** crates.io; open source.
- **Maintenance:** Active (Rust Wasm WG).
- **License:** MIT/Apache-2.0 (not re-verified).
- **Limitations:** Rust-specific; JS-side glue adds size; async interop via wasm-bindgen-futures.
- **Related resources:** wasm-pack, Emscripten, Component Model (successor interop story).
- **Sources:** Secondary mentions only.
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### ECMA-402 (Intl API)
- **Canonical identity:** ECMA-402, maintained by Ecma TC39
- **Category:** Languages & browser tech › Languages & standards
- **Type:** Internationalization API specification (standard)
- **Official URL:** https://tc39.es/ecma402/ ; repo: github.com/tc39/ecma402
- **Description:** Standardizes `Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.Collator`, `Intl.PluralRules`, `Intl.Segmenter`, `Intl.Locale`, etc. Underpins all JS i18n libraries and `Intl`-based formatting. TC39 March 2026 meeting also advanced i18n features per Socket.dev.
- **Contents inspected:** Search excerpts (i18n library docs referencing `Intl`; Socket.dev TC39 i18n note).
- **Actual capabilities:** Locale-aware number/date/currency formatting, collation, pluralization, segmentation, display names.
- **Usage domain:** All JS environments; basis for i18next/FormatJS/Lingui formatting.
- **Integration method:** Built-in `Intl` namespace; CLDR data bundled by host.
- **Dependencies:** Host-supplied ICU/CLDR data.
- **Availability:** All modern browsers and runtimes.
- **Maintenance:** Active.
- **License:** Not applicable (spec).
- **Limitations:** CLDR version varies by engine; time-zone-heavy use now partly superseded by Temporal.
- **Related resources:** Temporal, CLDR, ICU, i18next, FormatJS, BCP 47.
- **Sources:** https://socket.dev/blog/tc39-advances-temporal-to-stage-4 ; i18n library docs (FormatJS/Lingui references to Intl)
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### WHATWG HTML Living Standard
- **Canonical identity:** whatwg/html — HTML Living Standard
- **Category:** Languages & browser tech › Web standards
- **Type:** Markup + platform API specification (living standard)
- **Official URL:** https://html.spec.whatwg.org/multipage/ ; repo: github.com/whatwg/html
- **Description:** The definitive HTML specification: elements, parsing, forms, canvas, media, web workers, storage, history, and dozens of JS APIs. Continuously updated ("living standard", no version numbers since 2011). WHATWG develops; W3C HTML WG endorses review drafts as Recommendations under an MoU.
- **Contents inspected:** Search excerpts (whatwg/html FAQ on WHATWG↔W3C relationship; api-evangelist web-standards index).
- **Actual capabilities:** Defines conformance for browsers; implemented by all engines.
- **Usage domain:** All web content.
- **Integration method:** Implemented by browsers; validated via Nu HTML Checker.
- **Dependencies:** Not applicable.
- **Availability:** Public; free.
- **Maintenance:** Active (WHATWG, multi-vendor editors).
- **License:** CC0 for spec text (not re-verified).
- **Limitations:** Living-standard model means no fixed snapshot; some features long-incubating.
- **Related resources:** WHATWG DOM/Fetch/Streams/URL/Encoding, W3C CSS, Nu HTML Checker, web.dev.
- **Sources:** https://github.com/whatwg/html/blob/main/FAQ.md ; https://github.com/api-evangelist/web-standards
- **Verification date:** 2026-10-10
- **Confidence:** Verified (identity/role corroborated by primary FAQ)

### WHATWG companion standards (DOM · Fetch · Streams · URL · Encoding · MIME · Infra · Web IDL)
- **Canonical identity:** whatwg/dom, whatwg/fetch, whatwg/streams, whatwg/url, whatwg/encoding, whatwg/mimesniff, whatwg/infra, whatwg/webidl
- **Category:** Languages & browser tech › Web standards
- **Type:** Platform specifications (living standards)
- **Official URL:** https://dom.spec.whatwg.org ; https://fetch.spec.whatwg.org ; https://streams.spec.whatwg.org ; https://url.spec.whatwg.org ; https://encoding.spec.whatwg.org
- **Description:** The modular specs behind the web platform: DOM (nodes, events, mutation observers — replaced W3C DOM L3), Fetch (requests/responses, CORS, `fetch()` API), Streams (backpressured byte/object streams underpinning fetch bodies, compression, WebTransport), URL (parsing), Encoding (UTF-8/legacy), MIME sniffing, Infra (shared algorithms), Web IDL (IDL for browser APIs).
- **Contents inspected:** Search excerpts (Wikipedia WHATWG spec list; web-standards index entries for HTML + Fetch).
- **Actual capabilities:** Normative definitions implemented by all browsers; Fetch/Streams/URL directly usable as JS APIs.
- **Usage domain:** Browser internals and web developers (fetch, Response, ReadableStream, URL).
- **Integration method:** Built into browsers; Node.js implements Fetch/Streams/URL via undici + native modules.
- **Dependencies:** Not applicable.
- **Availability:** Public.
- **Maintenance:** Active.
- **License:** Not applicable.
- **Limitations:** Living-standard churn; Node's implementations occasionally lag browser semantics.
- **Related resources:** undici, WinterCG (server-side web-API alignment), MDN Web Docs.
- **Sources:** https://en.wikipedia.org/wiki/WHATWG ; https://github.com/api-evangelist/web-standards
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### W3C CSS specifications (CSS Snapshot 2026)
- **Canonical identity:** W3C CSS Working Group; CSS Snapshot 2026
- **Category:** Languages & browser tech › Web standards
- **Type:** Style specification suite (modular Recommendations)
- **Official URL:** https://www.w3.org/TR/css-2026/ (snapshot) ; https://www.w3.org/Style/CSS/
- **Description:** CSS is developed as independent modules (Selectors, Flexbox, Grid, Custom Properties, Nesting, Cascade Layers, Container Queries, etc.) progressing WD→CR→REC. CSS Snapshot 2026 collects the stable set. Process requires two independent implementations to exit Candidate Recommendation.
- **Contents inspected:** Search excerpt of w3.org/TR/css-2026/ (process description: WD/CR/REC levels).
- **Actual capabilities:** Styling/layout/animation of web documents; implemented by all browser engines.
- **Usage domain:** All web UI.
- **Integration method:** Authored in stylesheets; processed by PostCSS/Lightning CSS/Tailwind toolchains.
- **Dependencies:** Not applicable.
- **Availability:** Public.
- **Maintenance:** Active (CSSWG).
- **License:** Not applicable.
- **Limitations:** Module-by-module rollout means uneven cross-browser support for newer modules; snapshot is informational, not a version.
- **Related resources:** PostCSS, Lightning CSS, Tailwind CSS, Sass, Stylelint, MDN CSS reference, Baseline (web.dev).
- **Sources:** https://www.w3.org/TR/css-2026/
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (primary snapshot page located; module details not enumerated this session)

### IETF QUIC + HTTP/3
- **Canonical identity:** IETF QUIC WG — RFC 9000 (QUIC), RFC 9114 (HTTP/3)
- **Category:** Languages & browser tech › Web standards › Networking/transport
- **Type:** Transport protocol standards (RFCs)
- **Official URL:** https://www.rfc-editor.org/rfc/rfc9000.html ; https://www.rfc-editor.org/rfc/rfc9114.html
- **Description:** QUIC: UDP-based multiplexed secure transport (TLS 1.3 integrated). HTTP/3: HTTP semantics over QUIC. Underpin WebTransport (HTTP/3 CONNECT) and modern CDN/edge delivery. Browsers support HTTP/3; Node 24+ exposes QUIC module (experimental track — not directly verified this session).
- **Contents inspected:** Search excerpts (WebTransport guides describing HTTP/3 substrate; Bun HTTP/3 serve support notes).
- **Actual capabilities:** 0-RTT/1-RTT connection setup, per-stream flow control, connection migration (mobile network switching).
- **Usage domain:** Web delivery, real-time media/data (WebTransport), DNS-over-QUIC.
- **Integration method:** Implemented by browsers, CDNs, servers (nginx, Cloudflare); JS APIs: WebTransport, fetch (browser-managed).
- **Dependencies:** TLS 1.3; UDP reachability.
- **Availability:** Standard-track RFCs; broad deployment.
- **Maintenance:** Active (IETF).
- **License:** Not applicable.
- **Limitations:** UDP blocking on some networks; local-dev HTTPS requirement for WebTransport.
- **Related resources:** WebTransport, WebSockets (RFC 6455), WebRTC, nghttp2/ngtcp2.
- **Sources:** https://www.archyworldys.com/webtransport-beyond-websockets-fosdem-2026-guide/ ; https://developer.mozilla.org/en-US/docs/Web/API/WebTransport
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### 1.2 JavaScript engines

### V8
- **Canonical identity:** v8/v8 (Google, Chromium project)
- **Category:** Languages & browser tech › Engines
- **Type:** JavaScript + WebAssembly engine (library/embedding)
- **Official URL:** https://v8.dev ; repo: https://chromium.googlesource.com/v8/v8 (mirror: github.com/v8/v8)
- **Description:** Google's high-performance JS engine: Ignition interpreter + Sparkplug baseline + TurboFan optimizing compiler (Maglev mid-tier in newer versions — not verified this session). Powers Chrome/Edge/Opera, Node.js, Deno, Cloudflare workerd. First shipped 2008; Wasm support since 2015.
- **Contents inspected:** Search excerpts (Wikipedia history: Ignition 2016, TurboFan pipeline, Sparkplug 2021; engine taxonomy listings).
- **Actual capabilities:** JIT compilation tiers, garbage collection (Oilpan/heap), Wasm compilation, snapshotting, embeddable C++ API.
- **Usage domain:** Browsers (Chromium), servers (Node/Deno/workerd), edge isolates.
- **Integration method:** Embedded by host (Chrome, Node); `d8` developer shell; embedders use C++ API.
- **Dependencies:** Not applicable (self-contained C++).
- **Availability:** BSD-licensed open source.
- **Maintenance:** Active (Google).
- **License:** BSD-3-Clause (not re-verified this session).
- **Limitations:** Large binary; memory/CVE surface (hundreds of CVEs historically — cited in sandbox research as ~443).
- **Related resources:** Node.js, Deno, workerd, SpiderMonkey, JavaScriptCore, Hermes, QuickJS, JSVU (version manager for engines).
- **Sources:** http://en.wikipedia.org/wiki/V8_(JavaScript_engine) ; https://github.com/errilaz/awesome-js-runtimes/blob/master/README.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### SpiderMonkey
- **Canonical identity:** mozilla/firefox — SpiderMonkey (spidermonkey.dev)
- **Category:** Languages & browser tech › Engines
- **Type:** JavaScript + WebAssembly engine
- **Official URL:** https://spidermonkey.dev ; repo: mozilla-central (github.com/mozilla/firefox)
- **Description:** Mozilla's engine, the first-ever JavaScript engine (Brendan Eich, 1995). Powers Firefox/Gecko and WinterJS. Implements Warp (optimizing JIT), GC, Wasm.
- **Contents inspected:** Search excerpts (engine taxonomy; WinterJS SpiderMonkey basis; StarlingMonkey SpiderMonkey-for-Wasm-components runtime).
- **Actual capabilities:** Full ECMA-262 + Wasm; embeddable; basis for StarlingMonkey (WASI 0.2-targeted component runtime used by Fastly Compute and Fermyon Spin).
- **Usage domain:** Firefox browser; WinterJS server; Fastly/Fermyon Wasm component hosts.
- **Integration method:** Embedded in Firefox; standalone `js` shell; StarlingMonkey embedding for components.
- **Dependencies:** Not applicable.
- **Availability:** Open source (MPL-2.0).
- **Maintenance:** Active (Mozilla).
- **License:** MPL-2.0 (not re-verified this session).
- **Limitations:** Smaller embedder ecosystem than V8.
- **Related resources:** V8, JavaScriptCore, WinterJS, StarlingMonkey, Firefox.
- **Sources:** https://news.ycombinator.com/item?id=44701574 ; https://github.com/errilaz/awesome-js-runtimes/blob/master/README.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### JavaScriptCore (JSC)
- **Canonical identity:** WebKit JavaScriptCore (Apple)
- **Category:** Languages & browser tech › Engines
- **Type:** JavaScript + WebAssembly engine
- **Official URL:** https://webkit.org ; repo: github.com/WebKit/WebKit (Source/JavaScriptCore)
- **Description:** Apple's engine powering Safari/WebKit and Bun. Multi-tier JIT (LLInt/baseline/DFG/FTL). Bun 1.4 discards JIT code after idle periods to cut resident memory (per 2026 Bun release notes).
- **Contents inspected:** Search excerpts (engine taxonomy; Bun-on-JSC architecture notes; Bun 1.4 idle-JIT-discard).
- **Actual capabilities:** JIT tiers, concurrent GC (Riptide), Wasm, embeddable C API (JavaScriptCore framework).
- **Usage domain:** Safari (macOS/iOS — the only engine allowed on iOS), Bun runtime.
- **Integration method:** Embedded in WebKit; Bun embeds it server-side; `jsc` shell in WebKit builds.
- **Dependencies:** Not applicable.
- **Availability:** Open source (LGPL-2+/BSD mix — exact not re-verified).
- **Maintenance:** Active (Apple/WebKit).
- **License:** Not verified this session (historically LGPL-2.1+/BSD).
- **Limitations:** iOS mandates WebKit (no engine choice); embedder docs sparser than V8.
- **Related resources:** V8, SpiderMonkey, Bun, Safari/WebKit.
- **Sources:** https://medium.com/@onix_react/whats-new-in-bun-v1-4-1-298fe3eb5ba4 ; https://github.com/errilaz/awesome-js-runtimes/blob/master/README.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Hermes
- **Canonical identity:** facebook/hermes
- **Category:** Languages & browser tech › Engines
- **Type:** JavaScript engine optimized for mobile (ahead-of-time bytecode)
- **Official URL:** https://hermesengine.dev ; repo: github.com/facebook/hermes
- **Description:** Meta's JS engine for React Native: precompiles JS to bytecode at build time for fast startup and small memory on mobile. No JIT (interpreter). Used by React Native (default since RN 0.70) and by react-native-workers (separate Hermes runtime per worker thread).
- **Contents inspected:** Search excerpts (engine taxonomy: React Native/Hermes; react-native-workers architecture: one Hermes runtime per worker OS thread).
- **Actual capabilities:** AOT bytecode compilation, compact GC, ES2020+ language coverage (growing).
- **Usage domain:** React Native apps (iOS/Android); RN worker threads.
- **Integration method:** Bundled with React Native; `hermesc` compiler CLI.
- **Dependencies:** Not applicable.
- **Availability:** Open source (MIT).
- **Maintenance:** Active (Meta).
- **License:** MIT (not re-verified this session).
- **Limitations:** No JIT (slower peak throughput than V8/JSC); language feature lag vs browsers.
- **Related resources:** React Native, V8, JavaScriptCore, QuickJS.
- **Sources:** https://github.com/ammarahm-ed/react-native-workers/blob/HEAD/docs/blog/2026-07-26-introducing-react-native-workers/index.md ; https://github.com/errilaz/awesome-js-runtimes/blob/master/README.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### QuickJS (+ quickjs-ng fork)
- **Canonical identity:** bellard/quickjs (Fabrice Bellard); community fork quickjs-ng/quickjs
- **Category:** Languages & browser tech › Engines
- **Type:** Small embeddable JavaScript engine (C)
- **Official URL:** https://bellard.org/quickjs/ ; fork: github.com/quickjs-ng/quickjs
- **Description:** Tiny (~few hundred KB), fast-startup ES2023-capable interpreter in C. Bellard's upstream and the community quickjs-ng fork are diverging (both active; PRs traded occasionally). Powers LLRT (AWS Lambda runtime), txiki.js, and many embedded/plugin sandboxes. 28 CVEs noted in sandbox research (context, not a safety claim about current state).
- **Contents inspected:** Search excerpts (HN discussion of Bellard vs ng fork; LLRT/txiki.js engine listings; sandbox CVE comparison).
- **Actual capabilities:** Full ES2023-ish language, modules, typed arrays; embeddable C API; `qjs` CLI.
- **Usage domain:** Embedded scripting, serverless (LLRT), CLI tools, plugin sandboxes.
- **Integration method:** C library embedding; `qjs` binary.
- **Dependencies:** C toolchain.
- **Availability:** Open source (MIT).
- **Maintenance:** Active on both lines (diverging).
- **License:** MIT (not re-verified).
- **Limitations:** Interpreter only (no JIT); slower than V8/JSC on compute; fork divergence risk.
- **Related resources:** LLRT, txiki.js, V8, Hermes, Duktape/JerryScript (smaller engines).
- **Sources:** https://news.ycombinator.com/item?id=44701574 ; https://github.com/errilaz/awesome-js-runtimes/blob/master/README.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### 1.3 JavaScript runtimes

### Node.js 24 "Krypton" (Active LTS) / 26 (Current)
- **Canonical identity:** nodejs/node — v24.x LTS "Krypton"; v26.x Current (LTS from 2026-10-28)
- **Category:** Languages & browser tech › Runtimes
- **Type:** Server-side JavaScript runtime (application platform)
- **Official URL:** https://nodejs.org ; releases: https://nodejs.org/en/about/previous-releases
- **Description:** V8 + libuv + Chromium-derived network stack. Node 24 (released 2025-05-06, Active LTS 2025-10-28, EOL 2028-04-30) is the 2026 production default: npm 11, stable permission model (`--allow-fs-read`, `--allow-net`, ...), stable type-stripping for TS, Undici 7 (30% faster fetch), newer V8. Node 22 "Jod" in Maintenance LTS until 2027-04-30. Node 26 is the last even/odd-cycle release; from Node 27 the project moves to one major/year with every major intended for LTS. npm 11.19+ skips install scripts by default (`allowScripts` allowlist) — a supply-chain hardening.
- **Contents inspected:** Search excerpts: pkgpulse LTS guide (release table), techearl version guide, nodesource update guide, multiple 2026 upgrade commits/PRs pinning node:24.
- **Actual capabilities:** Event-loop I/O, ESM+CJS modules, Web APIs (fetch, WebSocket, WebCrypto, streams), worker_threads, cluster, built-in test runner, `--watch`, permission model, `node:sqlite` (not verified in depth this session).
- **Usage domain:** Servers, CLIs, build tooling, SSR.
- **Integration method:** Installer/package managers; `nvm`/`fnm`/`mise`; Docker `node:24-alpine`; `engines.node` in package.json.
- **Dependencies:** V8, libuv, llhttp, c-ares, OpenSSL, ICU, zlib-ng (via deps).
- **Availability:** nodejs.org; all major OSes; package managers.
- **Maintenance:** Active (OpenJS Foundation; predictable LTS cadence).
- **License:** MIT (not re-verified this session).
- **Limitations:** Single-threaded event loop (worker_threads/cluster for CPU); npm-install-scripts policy change breaks some postinstall flows; EOL lines (20/21/23/25) unpatched.
- **Related resources:** Deno, Bun, undici, amaro (TS type stripping), Corepack, libuv.
- **Sources:** https://www.pkgpulse.com/guides/nodejs-22-vs-nodejs-24-2026 ; https://techearl.com/how-to-update-node-js-version ; http://nodesource.com/blog/Update-nodejs-versions-on-windows ; https://github.com/resetshop/angular-nx-standalone-starter/issues/535
- **Verification date:** 2026-10-10
- **Confidence:** Verified (release table corroborated by 3+ sources; npm-11 script policy from a detailed issue report)

### Bun
- **Canonical identity:** oven-sh/bun — v1.4.x (1.4.1 Sept 2026); 1.3 Oct 2025
- **Category:** Languages & browser tech › Runtimes
- **Type:** All-in-one JavaScript runtime + toolkit (runtime, bundler, package manager, test runner)
- **Official URL:** https://bun.sh ; repo: github.com/oven-sh/bun
- **Description:** JavaScriptCore-based runtime (originally Zig; experimental Zig→Rust rewrite in progress, ~99.8% test compat on Linux x64 per 2026 notes; production stays on current build). Acquired by Anthropic December 2025. Ships: runtime with `Bun.*` APIs (`Bun.serve`, `Bun.file`, `Bun.SQL` for Postgres/MySQL/SQLite, built-in Redis client), bundler, package manager (fast installs, `bun.lock`), Jest-compatible test runner (`bun test` with --isolate/--shard), transpiler (native TS/JSX), `bunx`, single-file executables, full-stack dev server with HMR + React Fast Refresh, native HTTP/2 in `Bun.serve` (1.4), zlib-ng compression, memory-allocator improvements (Libpas scavenger). Community fork "Cruller" ports the last Zig-based Bun to Zig 0.16 as a runtime-only build (~18% smaller).
- **Contents inspected:** Search excerpts: The Register/DevClass 1.1.13 + 1.3 articles; Medium 1.4/1.4.1 feature rundowns; cli-jaw-skills bun-runtime SKILL.md (1.3.x feature list); HeadlinesBriefing Cruller summary.
- **Actual capabilities:** Runs TS/JSX natively (transpile only, type-check via tsc); npm-compatible installs; Node API compat (~98% claimed by third party — treat as claim); serves HTTP/WS; DB clients built in.
- **Usage domain:** Servers, CLIs, frontend tooling, scripts.
- **Integration method:** Single binary install; `bun run/install/test/build`; `bunx`.
- **Dependencies:** JavaScriptCore, libuv-ish event loop (own), zlib-ng.
- **Availability:** bun.sh; npm (`bun` package is a stub installer); macOS/Linux/Windows.
- **Maintenance:** Active (Oven, post-Anthropic-acquisition).
- **License:** MIT for runtime (Bun's license split — not re-verified in depth; JSC under its own license).
- **Limitations:** Memory-leak complaints in long-running production (addressed across 1.1.13→1.4); native-addon ABI gaps vs Node; Zig→Rust rewrite is experimental.
- **Related resources:** Node.js, Deno, esbuild, Vite, Hono/Elysia (frameworks, out of scope), Cruller (fork).
- **Sources:** https://www.theregister.com/software/2026/04/21/bun-1113-out-with-memory-fixes-as-dev-complain-of-leaks/5221154 ; https://medium.com/@onix_react/whats-new-in-bun-v1-4-1-298fe3eb5ba4 ; https://medium.com/@onix_react/whats-new-in-bun-v1-4-c9f2d85923db ; https://github.com/parkjs101/cli-jaw-skills/blob/HEAD/bun-runtime/SKILL.md ; https://headlinesbriefing.com/dev/hacker-news/cruller-bun-runtime-ported-to-zig-016-56ae9951
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (version/feature claims from secondary press + community docs; acquisition Dec 2025 reported by The Register/DevClass)

### Deno
- **Canonical identity:** denoland/deno — 2.7.x line (2.7.14 referenced mid-2026)
- **Category:** Languages & browser tech › Runtimes
- **Type:** Secure JavaScript/TypeScript/WebAssembly runtime + integrated toolchain
- **Official URL:** https://deno.com ; repo: github.com/denoland/deno ; registry: https://jsr.io
- **Description:** V8 + Rust (Tokio) runtime, secure by default (explicit `--allow-read/net/env/run` permissions; never deploy `--allow-all`). Native TypeScript (type-checks; no config), built-in formatter/linter/test runner/`deno compile` (standalone executables), `deno outdated`/`--update`, workspaces. Deno 2: full npm compatibility (`npm:` specifiers, `package.json` support, Node builtins), JSR registry (TS-first, Sigstore provenance), stabilized `@std` standard library, `Deno.serve`, Deno KV, Deno Deploy. 2.7.x notes: llhttp-based node:http rewrite, native TLSWrap, V8 146, OpenTelemetry exporter, `deno doc` for npm packages.
- **Contents inspected:** Search excerpts: terminalskills deno SKILL.md; tangled-skills deno-2-7-14 SKILL.md (changelog detail); pkgpulse Deno-2 overview; dev.to runtime comparison.
- **Actual capabilities:** Runs TS/JS/WSM; permission sandbox; npm+JSR+URL imports; compiles to single binaries; KV/cron/queues primitives.
- **Usage domain:** Servers, CLIs, edge (Deno Deploy), untrusted-code sandboxing.
- **Integration method:** Install script / Homebrew / npm; `deno run/test/fmt/lint/compile/serve`; `deno.json` config.
- **Dependencies:** V8, Tokio, Rustls.
- **Availability:** deno.land; GitHub releases; all major OSes.
- **Maintenance:** Active (Deno Land Inc).
- **License:** MIT (not re-verified this session).
- **Limitations:** CJS-only npm packages need adapters; native addons via npm compat layer have edge cases; smaller ecosystem than Node.
- **Related resources:** Node.js, Bun, JSR, workerd, WinterCG, Deno Deploy, Deno KV.
- **Sources:** https://github.com/terminalskills/skills/blob/HEAD/skills/deno/SKILL.md ; https://github.com/tangledgroup/tangled-skills/blob/HEAD/misc/deno-2-7-14/SKILL.md ; https://www.pkgpulse.com/guides/bun-2-vs-nodejs-24-vs-deno-3-2026 ; https://dev.to/zeybek/picking-a-javascript-runtime-in-2026-cho
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### workerd / Cloudflare Workers (runtime)
- **Canonical identity:** cloudflare/workerd (open-source runtime); Cloudflare Workers (hosted platform)
- **Category:** Languages & browser tech › Runtimes
- **Type:** Edge serverless runtime (V8 isolates) + platform
- **Official URL:** https://workers.cloudflare.com ; repo: github.com/cloudflare/workerd
- **Description:** Open-source V8-isolate runtime behind Cloudflare Workers. Sub-millisecond cold starts; event-driven `fetch()` entry point (no listening sockets); bindings for KV, R2, D1 (SQLite), Durable Objects, Queues, Workers AI. `wrangler` CLI deploys; `miniflare`/`wrangler dev` local emulation. Python Workers run CPython-on-Wasm (Pyodide) inside isolates as GA-track work. 2026 platform additions: Dynamic Workers, Facets (per research notes — single-sourced).
- **Contents inspected:** Search excerpts: dev.to Python Workers architecture (workerd + Pyodide); awesome-edge-computing-platform table (pricing/scale figures — vendor claims); concile spike notes (wrangler/workerd version pins).
- **Actual capabilities:** Runs JS/TS (and Python via Wasm) at 300+ PoPs; Web-standard APIs; zero-downtime deploys.
- **Usage domain:** Edge APIs, auth/rate-limiting/routing, SSR, cron, realtime fan-out.
- **Integration method:** `wrangler` CLI; `wrangler.toml`; local dev via workerd/miniflare.
- **Dependencies:** V8; cap'n proto RPC internally.
- **Availability:** Hosted (free tier 100k req/day per 2026 table — vendor claim); runtime Apache-2.0 open source.
- **Maintenance:** Active (Cloudflare).
- **License:** Apache-2.0 for workerd (not re-verified this session).
- **Limitations:** CPU-time limits per request; no raw TCP listen (use `connect()`); platform API differences vs Node (WinterCG alignment ongoing).
- **Related resources:** Deno Deploy, Vercel Edge Functions, Fastly Compute, WinterCG, Miniflare, Wrangler.
- **Sources:** https://dev.to/0xgosu/how-python-workers-turn-cpython-into-an-edge-runtime-3f92 ; https://github.com/ishandutta2007/awesome-edge-computing-platform ; https://medium.com/@Modexa/javascript-at-the-edge-is-becoming-the-default-b9e438214e88
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (Corrected: workerd uses V8 — not a custom engine — per HN correction thread)

### LLRT (Low Latency Runtime)
- **Canonical identity:** awslabs/llrt
- **Category:** Languages & browser tech › Runtimes
- **Type:** Lightweight JavaScript runtime for AWS Lambda (QuickJS + Tokio + Rust)
- **Official URL:** https://github.com/awslabs/llrt
- **Description:** AWS Labs runtime optimized for Lambda cold starts: QuickJS engine, Rust core, small binary (~tens of MB). Implements a useful subset of Node/WHATWG APIs. Benchmark tables show it among the smallest/fastest-starting JS runtimes.
- **Contents inspected:** Search excerpts (awesome-js-runtimes listing: LLRT/QuickJS/tokio; engine benchmark size table).
- **Actual capabilities:** Runs JS on Lambda with fast init; fetch, streams, subset of Node APIs.
- **Usage domain:** AWS Lambda functions where cold start dominates.
- **Integration method:** Lambda custom runtime / layer; `llrt` binary.
- **Dependencies:** QuickJS, Tokio, Rust.
- **Availability:** Open source (AWS Labs).
- **Maintenance:** Active (AWS Labs; experimental label historically).
- **License:** Apache-2.0 (not re-verified).
- **Limitations:** API subset (not full Node compat); AWS-Lambda-centric.
- **Related resources:** QuickJS, Node.js, workerd, WinterCG.
- **Sources:** https://github.com/errilaz/awesome-js-runtimes/blob/master/README.md ; https://dev.to/ahaoboy/js-engine-benchmark-2025-7-8-163b
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### WinterJS
- **Canonical identity:** wasmerio/winterjs
- **Category:** Languages & browser tech › Runtimes
- **Type:** JavaScript edge/server runtime (SpiderMonkey + hyper + Rust)
- **Official URL:** https://github.com/wasmerio/winterjs
- **Description:** Wasmer's runtime built on SpiderMonkey ("Spiderfire") with Hyper HTTP, targeting WinterCG web-interoperable APIs. 1.0 claimed 58k req/s single-core in vendor-adjacent coverage. Cloudflare-Apps-compatible packaging story.
- **Contents inspected:** Search excerpts (daily.dev 1.0 analysis; awesome-js-runtimes listing).
- **Actual capabilities:** Serves JS with web-standard Request/Response; Wasm-component-friendly direction.
- **Usage domain:** Edge/server JS where SpiderMonkey or Wasmer integration is wanted.
- **Integration method:** Binary; Wasmer integration.
- **Dependencies:** SpiderMonkey, hyper, Tokio.
- **Availability:** Open source.
- **Maintenance:** Active-ish (Wasmer; 1.0 covered early 2026 — precise current cadence not verified).
- **License:** MIT/Apache-2.0 (not re-verified).
- **Limitations:** Young ecosystem; performance claims vendor-adjacent (treat as claims).
- **Related resources:** SpiderMonkey, workerd, Deno, Wasmer, WinterCG.
- **Sources:** https://daily.dev/it/blog/winterjs-10-is-it-really-the-fastest-javascript-web-server ; https://github.com/errilaz/awesome-js-runtimes/blob/master/README.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### tsx
- **Canonical identity:** privatenumber/tsx (also esprit/tsx fork line — canonical is privatenumber/tsx)
- **Category:** Languages & browser tech › Runtimes
- **Type:** TypeScript/ESM executor CLI (esbuild-based)
- **Official URL:** https://github.com/privatenumber/tsx ; docs: https://tsx.is
- **Description:** Runs `.ts`/`.tsx`/ESM directly with esbuild transform; `tsx watch` is the 2026 default TS dev-loop runner. Faster and simpler than ts-node; no loader flags; resolves `.js` specifiers in TS sources.
- **Contents inspected:** Search excerpts (world-wide-lab migration ts-node→tsx; system-design-books watch-tools table: "tsx watch — most popular modern choice").
- **Actual capabilities:** Execute TS without compile step; watch mode; ESM+CJS interop.
- **Usage domain:** Dev servers, scripts, CLIs in TypeScript.
- **Integration method:** `npx tsx src/index.ts`; `tsx watch`; package.json scripts.
- **Dependencies:** esbuild.
- **Availability:** npm `tsx`; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Transpile-only (no type checking — pair with `tsc --noEmit`).
- **Related resources:** ts-node, esbuild, Node.js type stripping, Bun, Deno.
- **Sources:** https://github.com/world-wide-lab/world-wide-lab/commit/1ac13e9048e1198777ac88ed25776a201f375ddb ; https://github.com/naman830/system-design-books/blob/HEAD/Libraries_Depth/nodemon/nodemon.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### ts-node
- **Canonical identity:** TypeStrong/ts-node
- **Category:** Languages & browser tech › Runtimes
- **Type:** TypeScript execution engine for Node.js (JIT transform + REPL)
- **Official URL:** https://github.com/TypeStrong/ts-node ; docs: https://typestrong.org/ts-node
- **Description:** The long-standing TS runner (tsc-based transform, ESM loader). In 2026 it is legacy for new setups: the ESM loader broke on Node 20+ (empty-object loader error), prompting migrations to tsx or Node native type stripping. Still present in many repos.
- **Contents inspected:** Search excerpts (world-wide-lab commit: ts-node ESM loader broken on Node 20+; metamask/utils PR removing unused ts-node).
- **Actual capabilities:** `ts-node` CLI, programmatic API, REPL, ESM loader (legacy), transpile-only mode.
- **Usage domain:** Legacy TS scripts/tests; gradually replaced.
- **Integration method:** npm `ts-node`; `node --loader ts-node/esm` (legacy).
- **Dependencies:** TypeScript.
- **Availability:** npm; MIT.
- **Maintenance:** Maintenance mode in practice (not officially archived — label carefully).
- **License:** MIT (not re-verified).
- **Limitations:** ESM loader incompatible with Node 20+; slower than esbuild-based runners.
- **Related resources:** tsx, typescript, amaro, ts-node-dev.
- **Sources:** https://github.com/world-wide-lab/world-wide-lab/commit/1ac13e9048e1198777ac88ed25776a201f375ddb ; https://github.com/metamask/utils/commit/d65c1c1ebf11826b2702db7dff1626cbe5582166
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### amaro (Node.js type stripping)
- **Canonical identity:** nodejs/amaro
- **Category:** Languages & browser tech › Runtimes
- **Type:** TypeScript type-stripping transform library (SWC-based; powers Node's native TS support)
- **Official URL:** https://github.com/nodejs/amaro
- **Description:** Node's reference TS-stripping implementation: converts TS to JS by erasing types (no type checking). Used by Node 22.6+ `--experimental-strip-types` and stable type stripping in Node 24. Evaluated tsgo as an engine and rejected it ("not possible by design": tsgo lacks blank-spacing mode; Go runtime doesn't fit Node distribution) — will keep SWC for the foreseeable future (per 2025-05-26 maintainer note).
- **Contents inspected:** Search excerpts (nub wiki research citing amaro#200 maintainer decision).
- **Actual capabilities:** Fast type erasure with source-map-friendly blank spacing; enum/namespace handling per erasableSyntaxOnly semantics.
- **Usage domain:** Node.js native TypeScript execution.
- **Integration method:** Bundled in Node; library usable standalone.
- **Dependencies:** SWC (Rust via napi).
- **Availability:** Open source (MIT).
- **Maintenance:** Active (Node.js org).
- **License:** MIT (not re-verified).
- **Limitations:** Erasable syntax only (no enums with runtime behavior, no parameter properties); no type checking.
- **Related resources:** Node.js, SWC, tsx, TypeScript.
- **Sources:** https://github.com/1st1/nub/blob/HEAD/wiki/research/tsgo-vs-oxc-for-transpile.md (citing nodejs/amaro#200)
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (single detailed source for the tsgo-rejection rationale)

### 1.4 Browser APIs

### Web Workers (dedicated) + SharedWorker + worklets
- **Canonical identity:** WHATWG HTML — Web Workers; W3C Worklets (AudioWorklet, PaintWorklet, AnimationWorklet)
- **Category:** Languages & browser tech › Browser APIs › Concurrency
- **Type:** Browser platform APIs (standards)
- **Official URL:** https://html.spec.whatwg.org/multipage/workers.html ; MDN: https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API
- **Description:** Dedicated workers: one-per-page background threads, no DOM, `postMessage` + structured clone / transferables. SharedWorker: one instance shared across same-origin tabs (Safari iOS <16 lacked support historically). Worklets: lightweight threads in the rendering/audio pipeline (PaintWorklet for custom CSS paint, AudioWorklet for audio DSP, AnimationWorklet). CSP `worker-src` governs worker/serviceworker/sharedworker; worklets fall under `script-src-elem`. Module workers (`{type:'module'}`) and `import.meta.url`-based bundler chunk splitting are the 2026-standard build integration.
- **Contents inspected:** Search excerpts: dev.to worker comparison table; tighten.com web-workers explainer (structured clone vs transferables); kumaratul60 worker taxonomy; CSP research (worker-src mapping); Angular KB (Comlink, SharedArrayBuffer+Atomics, COOP/COEP).
- **Actual capabilities:** Off-main-thread compute; cross-tab shared state; low-latency audio/paint hooks.
- **Usage domain:** Heavy compute (parsing, crypto, image), cross-tab coordination, audio DSP, custom CSS painting.
- **Integration method:** `new Worker(url)`, `new SharedWorker(url)`, `CSS.paintWorklet.addModule()`, `audioContext.audioWorklet.addModule()`; bundlers emit worker chunks (Vite `?worker`, webpack `new URL(..., import.meta.url)`).
- **Dependencies:** Secure context for some features; COOP+COEP headers for `SharedArrayBuffer`.
- **Availability:** All modern browsers (SharedWorker gaps on older iOS Safari).
- **Maintenance:** Active standards.
- **License:** Not applicable.
- **Limitations:** No DOM; structured-clone costs (use transferables); worklet APIs are narrow/pipeline-specific.
- **Related resources:** Service Workers, Comlink (RPC library), BroadcastChannel, SharedArrayBuffer/Atomics, OffscreenCanvas.
- **Sources:** https://dev.to/zeeshanali0704/comparison-of-web-worker-sharedworker-and-service-worke-3ff0 ; https://tighten.com/insights/web-workers-a-second-thread-for-your-javascript/ ; https://github.com/kumaratul60/system-design/blob/HEAD/cheatsheets/service-workers-and-web-workers.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Service Workers + Cache Storage + Background Sync + Push
- **Canonical identity:** W3C Service Workers / WHATWG Fetch integration; Push API; Background Sync
- **Category:** Languages & browser tech › Browser APIs › Offline/network
- **Type:** Browser platform APIs (standards)
- **Official URL:** https://w3c.github.io/ServiceWorker/ ; MDN: https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API
- **Description:** Origin-scoped programmable network proxy: intercepts fetch, enables offline-first caching strategies, push notifications (via Push API + Notification API), background sync. Event-driven lifecycle (install/activate/fetch/message); HTTPS-only; one registration per scope. Workbox (Google) is the dominant helper library (out of scope detail).
- **Contents inspected:** Search excerpts (worker taxonomy tables listing SW capabilities; PWA/storage research notes; IndexedDB/Cache API comparisons).
- **Actual capabilities:** Request interception, precaching/runtime caching, offline fallback, push receipt, deferred sync.
- **Usage domain:** PWAs, offline-first apps, installable web apps.
- **Integration method:** `navigator.serviceWorker.register('/sw.js')`; build plugins (Vite PWA plugin, Workbox CLI/precaching).
- **Dependencies:** HTTPS (or localhost); Cache API/IndexedDB for persistence.
- **Availability:** All modern browsers.
- **Maintenance:** Active.
- **License:** Not applicable.
- **Limitations:** No DOM; event-driven kills (no long compute); debugging harder; iOS historically lagged (largely caught up — not re-verified in detail).
- **Related resources:** Cache API, IndexedDB, Web Push (VAPID), Workbox, Periodic Background Sync.
- **Sources:** https://dev.to/zeeshanali0704/comparison-of-web-worker-sharedworker-and-service-worke-3ff0 ; https://github.com/the-cyber-boardroom/sgraph-ai__app__send/blob/HEAD/library/sgraph-send/file-transfer-engine/research/03-browser-storage-apis.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Web Components (Custom Elements · Shadow DOM · Declarative Shadow DOM · ElementInternals)
- **Canonical identity:** WHATWG HTML custom elements + W3C/DOM shadow DOM; DSD via `<template shadowrootmode>`
- **Category:** Languages & browser tech › Browser APIs › Components
- **Type:** Browser platform APIs (standards)
- **Official URL:** https://html.spec.whatwg.org/multipage/custom-elements.html ; MDN: https://developer.mozilla.org/en-US/docs/Web/API/Web_components
- **Description:** Framework-agnostic component model: `customElements.define`, shadow DOM encapsulation (slots, `::part`), HTML templates, and form-associated custom elements via `ElementInternals` (widely available since Mar 2023). Declarative Shadow DOM (`<template shadowrootmode="open|closed">`) reached Baseline "widely available" on 2026-08-20, enabling SSR without JS for first paint + progressive hydration. Scoped custom-element registries remain experimental. React 19 scores 100% on custom-elements-everywhere interop.
- **Contents inspected:** Search excerpts: web-components SKILL.md (Baseline table verified 2026-05-19); formancy.ai ADR (DSD Baseline date 2026-08-20); FAST docs (DSD SSR hydration contract); Anza toolkit README (DSD-based SSG).
- **Actual capabilities:** Encapsulated reusable elements usable in any framework; SSR-friendly markup; native form participation.
- **Usage domain:** Design-system primitives, embeddable widgets, micro-frontends.
- **Integration method:** Native browser APIs; SSR emits DSD templates; libraries (Lit, FAST, Stencil) add reactivity sugar.
- **Dependencies:** None (platform).
- **Availability:** All modern browsers; DSD baseline-wide since Aug 2026.
- **Maintenance:** Active.
- **License:** Not applicable.
- **Limitations:** Styling across shadow boundaries needs `::part`/CSS vars; SSR hydration contracts are library-specific; a11y of slotted content needs care.
- **Related resources:** Lit, FAST, Stencil, Shadow DOM CSS (`::part`, `:host`), HTML templates/slots.
- **Sources:** https://github.com/pvds/nicefortourism (SKILL.md excerpt via search) ; https://github.com/sharkysan/formancy.ai/blob/HEAD/docs/decisions/0005-not-web-components.md ; https://github.com/guden/fast/blob/HEAD/sites/website/src/docs/3.x/declarative-templates/server-rendering.md ; https://github.com/anzaui/anza/blob/HEAD/README.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (DSD Baseline date from one ADR citing web-platform data)

### Browser storage suite (Web Storage · IndexedDB · Cache API · OPFS · Storage API)
- **Canonical identity:** WHATWG HTML Web Storage; W3C IndexedDB; Cache Storage; File System (OPFS); Storage Standard
- **Category:** Languages & browser tech › Browser APIs › Storage
- **Type:** Browser platform APIs (standards)
- **Official URL:** MDN hubs: https://developer.mozilla.org/en-US/docs/Web/API/Storage_API ; https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API
- **Description:** localStorage/sessionStorage: ~5MB synchronous string KV (main thread only; not visible in service workers). IndexedDB: transactional object store, indexes/cursors, Blobs, GB-scale — verbose API (Dexie.js/`idb` wrappers popular). Cache API: Request/Response store for HTTP caching (service-worker-driven). OPFS (Origin Private File System): real file semantics, random byte-range access, sync access handles inside dedicated workers (~90ms/100MB writes vs ~850ms IndexedDB in cited benchmarks — single source), ideal for SQLite-WASM (wa-sqlite). All share the origin quota pool (`navigator.storage.estimate()`); `persist()` requests eviction protection.
- **Contents inspected:** Search excerpts: OPFS explainer (support table: Chrome 102+, FF 111+, Safari 15.2+), storage comparison tables, SQLite+OPFS best-practice notes, File System Access picker limitation (Chrome/Edge-only).
- **Actual capabilities:** Offline data, large binary/blob storage, HTTP response caching, relational data via SQLite/WASM.
- **Usage domain:** Offline-first apps, media apps, PWA data layers.
- **Integration method:** Native async APIs; wrappers (Dexie, idb-keyval); SQLite compiled to WASM on OPFS.
- **Dependencies:** Quota availability; secure context for some.
- **Availability:** All modern browsers (OPFS since ~2023 across engines).
- **Maintenance:** Active.
- **License:** Not applicable.
- **Limitations:** iOS Safari quota/persist() strictness; OPFS sync handles worker-only; File System Access pickers not in Firefox/Safari.
- **Related resources:** Dexie.js, idb, wa-sqlite, File System Access API, Quota Management.
- **Sources:** https://dev.to/helloashish99/opfs-the-browsers-built-in-filesystem-explained-o5i ; https://github.com/the-cyber-boardroom/sgraph-ai__app__send/blob/HEAD/library/sgraph-send/file-transfer-engine/research/03-browser-storage-apis.md ; https://github.com/mayouni/ringscript/blob/HEAD/docs/PARTITION-FOUNDATIONS.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (benchmark numbers single-sourced)

### WebGPU
- **Canonical identity:** W3C GPU for the Web WG — WebGPU + WGSL
- **Category:** Languages & browser tech › Browser APIs › Graphics/compute
- **Type:** Browser platform API + shading language (standard)
- **Official URL:** https://www.w3.org/TR/webgpu/ ; https://gpuweb.github.io/gpuweb/
- **Description:** Modern GPU API (compute + render pipelines, WGSL shaders) mapping to D3D12/Metal/Vulkan via Dawn (Chromium) and wgpu (Firefox). Now ships in all major browsers: Chrome/Edge 113+ (2023), Safari 26 (June 2025), Firefox 141 Windows (July 2025)/145 macOS (Nov 2025). three.js r170+ has production WebGPURenderer (+TSL shader language, WebGL2 fallback); Babylon.js 8 rewrote core shaders in WGSL; PixiJS v8 defaults to WebGL with WebGPU opt-in.
- **Contents inspected:** Search excerpts: TechSpot cross-browser availability article; game-engine matrix (Sept 2026); WebGPU-readiness SKILL (per-library recommendations); native-GPU-testing article (Dawn/ANGLE reuse in Node tests).
- **Actual capabilities:** GPU compute shaders, render bundles, instancing, storage textures; powers ML inference (Transformers.js, ONNX Runtime Web).
- **Usage domain:** 3D/games, GPU compute, ML inference in browser.
- **Integration method:** `navigator.gpu.requestAdapter()`; libraries (three, Babylon, PlayCanvas) abstract it.
- **Dependencies:** OS GPU drivers; secure context.
- **Availability:** All major browsers (2025–2026 rollout); Linux/Android mostly manual flags per reports.
- **Maintenance:** Active (GPU for the Web WG).
- **License:** Not applicable.
- **Limitations:** Not automatically faster than WebGL (scene-dependent; some regressions reported); spec + implementations still evolving.
- **Related resources:** WebGL, WGSL, Dawn, wgpu, three.js, Babylon.js, WebNN (separate spec).
- **Sources:** https://www.techspot.com/news/110456-webgpu-now-brings-desktop-quality-graphics-all-major.html ; https://app.cinevva.com/blog/2026-06-09-web-game-engines-2026-comparison ; https://github.com/dedperdedev/speedrungg (webgpu-readiness SKILL.md excerpt via search)
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (browser-version claims from press; per-library status from community docs)

### WebGL
- **Canonical identity:** Khronos WebGL 1.0/2.0
- **Category:** Languages & browser tech › Browser APIs › Graphics/compute
- **Type:** Browser 3D graphics API (standard)
- **Official URL:** https://www.khronos.org/webgl/
- **Description:** OpenGL ES-based immediate-mode 3D API; WebGL2 is the stable workhorse renderer (three.js, Babylon, PlayCanvas default). WebGL1 contexts still universal. Being gradually succeeded by WebGPU for new high-end work but remains the compatibility baseline.
- **Contents inspected:** Search excerpts (engine matrix: WebGL2 primary renderer; ANGLE-based Node testing).
- **Actual capabilities:** Hardware-accelerated 3D/2D rendering via GLSL shaders.
- **Usage domain:** Web games, data viz, creative coding.
- **Integration method:** `<canvas>.getContext('webgl2')`; libraries abstract it.
- **Dependencies:** GPU drivers.
- **Availability:** Universal in modern browsers.
- **Maintenance:** Maintenance (Khronos); new features go to WebGPU.
- **License:** Not applicable.
- **Limitations:** No compute shaders; state-machine API showing age.
- **Related resources:** WebGPU, three.js, Babylon.js, PlayCanvas, ANGLE.
- **Sources:** https://app.cinevva.com/blog/2026-06-09-web-game-engines-2026-comparison ; https://ben3d.ca/blog/native-gpu-testing-for-vitest-and-jest
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### WebRTC
- **Canonical identity:** W3C WebRTC 1.0 (+ IETF protocol suite); webrtc.github.io
- **Category:** Languages & browser tech › Browser APIs › Realtime
- **Type:** Realtime peer-to-peer communication APIs + protocols (standard)
- **Official URL:** https://webrtc.org ; spec: https://www.w3.org/TR/webrtc/
- **Description:** `RTCPeerConnection` (audio/video/data channels), `getUserMedia`, ICE/STUN/TURN NAT traversal, DTLS-SRTP encryption. Supported by all modern browsers (Chrome 28+, Firefox 22+, Safari 11+). SFU servers (LiveKit, mediasoup, Janus) scale it; 0.2–0.5s latency typical. Signaling is app-defined (WebSocket commonly).
- **Contents inspected:** Search excerpts: WebRTC-vs-HLS matrix (latency/cost/device table); PeerJS-based React tutorial; LiveKit comparisons.
- **Actual capabilities:** P2P/sub-second media + `RTCDataChannel` arbitrary data.
- **Usage domain:** Video calls, live streaming, conferencing, P2P data.
- **Integration method:** Native browser APIs; SFU SDKs (livekit-client, mediasoup-client); wrappers (PeerJS, simple-peer).
- **Dependencies:** STUN/TURN for NAT; HTTPS for getUserMedia.
- **Availability:** All modern browsers; native mobile SDKs.
- **Maintenance:** Active (W3C/IETF; Google libwebrtc).
- **License:** Not applicable (spec); libwebrtc BSD.
- **Limitations:** Needs SFU for multiparty scale; no built-in signaling; smart-TV reach weaker than HLS.
- **Related resources:** LiveKit, mediasoup, PeerJS, WebTransport, WHIP/WHEP (ingest/playout protocols).
- **Sources:** https://www.forasoft.com/blog/article/webrtc-video-steaming-app-vs-hls ; https://dev.to/kgbadao/demystifying-webrtc-a-step-by-step-guide-to-peer-to-peer-video-in-react-4k3b
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### WebSocket API + protocol (RFC 6455)
- **Canonical identity:** IETF RFC 6455; WHATWG HTML WebSocket API
- **Category:** Languages & browser tech › Browser APIs › Realtime
- **Type:** Full-duplex messaging protocol + browser API (standard)
- **Official URL:** https://www.rfc-editor.org/rfc/rfc6455 ; MDN: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
- **Description:** Bidirectional message protocol over a single TCP connection (ws/wss). Browser `WebSocket` API; Node libraries: `ws` (RFC-6455, fastest Node impl, passes Autobahn suite; server+client; optional bufferutil/utf-8-validate native addons), `uWebSockets.js`/`eiows`. Higher-level: Socket.IO 4.8.4 (Sept 2026) — event-based framework with polling→WebSocket→WebTransport upgrade, rooms/namespaces; server uses `ws` by default. WebSocketStream (newer promise-based API) also listed on MDN.
- **Contents inspected:** Search excerpts: MDN WebSockets API page listing ws/Socket.IO/µWebSockets; Socket.IO 4.8.4 docs (transports table incl. WebTransport, dependency tree with ws@8.17.1); socket.dev ws analysis.
- **Actual capabilities:** Low-latency bidirectional messaging; subprotocols; binary frames.
- **Usage domain:** Chat, live dashboards, gaming, collaboration, signaling.
- **Integration method:** `new WebSocket(url)`; `ws` npm package server-side; Socket.IO client+server.
- **Dependencies:** HTTP upgrade handshake; proxies must allow it.
- **Availability:** Universal.
- **Maintenance:** Active (protocol stable; libraries maintained).
- **License:** Not applicable (protocol); ws: MIT; Socket.IO: MIT (not re-verified).
- **Limitations:** Head-of-line blocking on single TCP connection; no multiplexing (use WebTransport/HTTP-2+SSE where needed).
- **Related resources:** Socket.IO, ws, WebTransport, SSE, MQTT-over-WS, AsyncAPI.
- **Sources:** https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API?ref=blog.krum.io ; https://socket.io/docs/v4/client-options/ ; https://socket.io/docs/v4/server-installation/ ; https://socket.dev/npm/package/ws/overview/0.4.5
- **Verification date:** 2026-10-10
- **Confidence:** Verified (Socket.IO docs + MDN primary pages)

### WebTransport
- **Canonical identity:** W3C WebTransport (over HTTP/3)
- **Category:** Languages & browser tech › Browser APIs › Realtime
- **Type:** Browser transport API (standard)
- **Official URL:** https://www.w3.org/TR/webtransport/ ; MDN: https://developer.mozilla.org/en-US/docs/Web/API/WebTransport
- **Description:** QUIC-based transport: reliable streams + unreliable datagrams, bidirectional/unidirectional, connection migration (Wi-Fi→cellular). MDN marks it "Baseline 2026 — Newly available". Secure context (HTTPS) mandatory — limits local-dev/offline use. Positioned for cloud gaming, trading, low-latency streaming; NOT a wholesale WebSocket replacement per 2026 analysis.
- **Contents inspected:** Search excerpts: MDN WebTransport reference (constructor, datagrams, streams, close); FOSDEM 2026 guide (adoption hurdles, HTTPS mandate).
- **Actual capabilities:** `new WebTransport(url)`; datagram + stream multiplexing over HTTP/3.
- **Usage domain:** Latency-sensitive realtime (gaming, media contribution, live data).
- **Integration method:** Native browser API; server needs HTTP/3 endpoint (e.g., Node experimental, Cloudflare, custom Quiche).
- **Dependencies:** HTTP/3 server; HTTPS.
- **Availability:** Baseline 2026 (newly available across engines — exact per-engine versions not enumerated this session).
- **Maintenance:** Active (W3C WebTransport WG).
- **License:** Not applicable.
- **Limitations:** HTTPS-only; server ecosystem young; complexity vs WebSocket.
- **Related resources:** HTTP/3/QUIC, WebSockets, WebRTC data channels, Socket.IO (WebTransport transport option).
- **Sources:** https://developer.mozilla.org/en-US/docs/Web/API/WebTransport ; https://www.archyworldys.com/webtransport-beyond-websockets-fosdem-2026-guide/
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (Baseline 2026 status from MDN)

### Fetch API / WHATWG Fetch (+ axios, ky, undici, redaxios)
- **Canonical identity:** WHATWG Fetch Standard; libraries: axios/axios, sindresorhus/ky, nodejs/undici, developit/redaxios
- **Category:** Languages & browser tech › Browser APIs › Networking
- **Type:** Platform API (standard) + HTTP client libraries
- **Official URL:** https://fetch.spec.whatwg.org/ ; axios: https://github.com/axios/axios ; ky: https://github.com/sindresorhus/ky ; undici: https://github.com/nodejs/undici
- **Description:** `fetch()` is the universal HTTP primitive (browsers + Node 18+ via undici, Deno, Bun, workers). undici is Node's built-in HTTP/1.1 client powering global fetch (Undici 7 in Node 24: ~30% faster). axios remains the most-used library (interceptors, defaults, wider compat); ky is a small fetch wrapper; redaxios is an 800-byte axios-API-compatible fetch wrapper (developit; community forks e.g. kouhin/redaxios maintain TS types). 2026 trend: ADRs replacing axios with centralized fetch wrappers or ky to cut bundle size; tanstack-fetch (community, not official TanStack) targets TanStack Query users with migration CLI.
- **Contents inspected:** Search excerpts: axios-vs-fetch ADR (2026-05-10, accepted); redaxios README (API list, 800 bytes); ky/axios/tanstack-fetch comparison; undici WebSocket usage in wirebench spec.
- **Actual capabilities:** HTTP requests with streaming bodies, abort, interceptors (axios), retries/timeout (ky).
- **Usage domain:** All client-server communication.
- **Integration method:** Native `fetch`; npm packages for axios/ky/redaxios; undici `Dispatcher`/`WebSocket` in Node.
- **Dependencies:** None for fetch; libraries are zero/low-dep.
- **Availability:** Universal (fetch); npm for libraries.
- **Maintenance:** axios active; ky active; undici active (Node core team); redaxios original repo low-activity (forks active).
- **License:** MIT (all; not re-verified).
- **Limitations:** fetch lacks interceptors/timeout natively (AbortController needed); axios adds bundle weight.
- **Related resources:** openapi-fetch, ofetch (Nitro/unjs), SSE/EventSource, Beacon API.
- **Sources:** https://github.com/isw2-unileon/focuscafe-project/blob/HEAD/docs/adr/003-fetch-api-over-axios.md ; https://github.com/developit/redaxios ; http://dev.to/mwmdgmb/tanstack-fetch-vs-ky-vs-axios-which-http-client-fits-tanstack-query-34g7
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### WebCodecs
- **Canonical identity:** W3C WebCodecs
- **Category:** Languages & browser tech › Browser APIs › Media
- **Type:** Low-level media codec API (standard)
- **Official URL:** https://www.w3.org/TR/webcodecs/
- **Description:** Direct access to browser audio/video encoders/decoders (`VideoDecoder`, `VideoEncoder`, `AudioDecoder`, `AudioEncoder`) for custom media pipelines without `<video>` overhead. Used by conferencing/streaming apps, cloud gaming, browser-based editors.
- **Contents inspected:** Not deeply covered in searches; included for systematic coverage.
- **Actual capabilities:** Frame-level encode/decode with hardware acceleration where available.
- **Usage domain:** Custom players, conferencing SFUs, media processing.
- **Integration method:** Native browser API; often paired with WebTransport/WebRTC.
- **Dependencies:** Codec support varies by platform.
- **Availability:** Chromium + Safari (Firefox partial — not verified in detail).
- **Maintenance:** Active (W3C Media WG).
- **License:** Not applicable.
- **Limitations:** Codec availability varies; no container muxing (use mp4box.js etc.).
- **Related resources:** WebRTC, Media Source Extensions, WebGPU (video upload), Insertable Streams.
- **Sources:** Not directly sourced this session — spec existence is long-established.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified (2026 support matrix not checked)

### WebAuthn
- **Canonical identity:** W3C WebAuthn Level 2/3
- **Category:** Languages & browser tech › Browser APIs › Identity/security
- **Type:** Authentication API (standard)
- **Official URL:** https://www.w3.org/TR/webauthn-3/
- **Description:** Public-key credential API for passwordless auth (security keys, platform authenticators, passkeys). `navigator.credentials.create()/get()`. Server libraries verify attestation/assertion.
- **Contents inspected:** Not deeply covered in searches; included for systematic coverage.
- **Actual capabilities:** Passkey registration/authentication; conditional mediation (autofill).
- **Usage domain:** Passwordless login, 2FA.
- **Integration method:** Native browser API + server-side verification (SimpleWebAuthn and similar libraries).
- **Dependencies:** Authenticator hardware/platform support; HTTPS.
- **Availability:** All modern browsers.
- **Maintenance:** Active (W3C WebAuthn WG).
- **License:** Not applicable.
- **Limitations:** UX/recovery flows are app responsibilities; attestation formats vary.
- **Related resources:** Passkeys, FIDO2/CTAP2, SimpleWebAuthn.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified (2026 spec level not checked)

### File System Access API (+ File API)
- **Canonical identity:** WICG File System Access (now File System Standard)
- **Category:** Languages & browser tech › Browser APIs › Storage
- **Type:** Browser API for user-visible files (standard-track)
- **Official URL:** https://wicg.github.io/file-system-access/ ; https://fs.spec.whatwg.org/
- **Description:** `showOpenFilePicker`/`showSaveFilePicker`/`showDirectoryPicker` give web apps read/write access to user-chosen files with permission prompts. Chrome/Edge only for pickers; Safari/Firefox support the underlying OPFS portions. Portable fallback: `<input type=file>` + drag-drop.
- **Contents inspected:** Search excerpt (wine-assembly design doc: "File System Access pickers — No [in Safari] — Chrome/Edge only").
- **Actual capabilities:** Read/write real user files; origin-private FS root via `navigator.storage.getDirectory()`.
- **Usage domain:** Editors, IDEs, media tools as web apps.
- **Integration method:** Native picker methods; async iteration of directory handles.
- **Dependencies:** User gesture; permission grant; HTTPS.
- **Availability:** Chromium full; others partial.
- **Maintenance:** Active (WHATWG File System Standard absorbs it).
- **License:** Not applicable.
- **Limitations:** No Firefox/Safari picker support (2026) — design portable fallbacks.
- **Related resources:** OPFS, File API, drag-and-drop.
- **Sources:** https://github.com/vgrichina/wine-assembly/blob/HEAD/docs/design-byo-media.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Constraint Validation API (HTML forms)
- **Canonical identity:** WHATWG HTML — client-side form validation
- **Category:** Languages & browser tech › Browser APIs › Forms
- **Type:** Built-in browser validation API (standard)
- **Official URL:** https://html.spec.whatwg.org/multipage/form-control-infrastructure.html
- **Description:** Native form validation: `required`, `pattern`, `min/max`, `type=email|url`, `setCustomValidity()`, `checkValidity()`, `reportValidity()`, `:valid`/`:invalid` CSS pseudo-classes, `validationMessage` localization. Works without JS; enhanced with JS.
- **Contents inspected:** Accessibility SKILL excerpts referencing form validation requirements (labels, required state, error association via aria-describedby).
- **Actual capabilities:** Declarative constraints + imperative validation API + localized default messages.
- **Usage domain:** All web forms (progressive enhancement baseline).
- **Integration method:** HTML attributes; JS validity API; CSS hooks.
- **Dependencies:** None.
- **Availability:** Universal.
- **Maintenance:** Active (WHATWG).
- **License:** Not applicable.
- **Limitations:** Styling of native bubbles limited; complex rules need JS; server-side validation still required.
- **Related resources:** ElementInternals (custom elements), ARIA form roles, Zod/Valibot (JS schema validation — validation workstream).
- **Sources:** https://github.com/mejbaurbahar/software-tester-skills/blob/HEAD/skills/accessibility-testing/SKILL.md (form requirements context)
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Notifications API (+ VAPID Web Push)
- **Canonical identity:** W3C Notifications API; IETF RFC 8030 (WebPush) + VAPID RFC 8292
- **Category:** Languages & browser tech › Browser APIs › Engagement
- **Type:** System notification + push messaging standards
- **Official URL:** https://notifications.spec.whatwg.org/ ; https://www.rfc-editor.org/rfc/rfc8030
- **Description:** `Notification` API shows system notifications (permission-gated); Web Push delivers them from servers via push services (VAPID keys) to service workers even when the page is closed.
- **Contents inspected:** Search excerpts (service worker capability tables list push notifications).
- **Actual capabilities:** Local + push notifications with actions, icons, badges.
- **Usage domain:** Messaging apps, alerts, re-engagement.
- **Integration method:** `Notification.requestPermission()`; Push API `subscribe()` in SW; server sends via Web Push libraries.
- **Dependencies:** Service worker (for push); HTTPS; platform push service.
- **Availability:** All modern browsers (iOS added Web Push for installed PWAs — not re-verified in detail).
- **Maintenance:** Active.
- **License:** Not applicable.
- **Limitations:** Permission UX; payload encryption (ECE); iOS constraints.
- **Related resources:** Service Workers, Push API, Badging API.
- **Sources:** https://dev.to/zeeshanali0704/comparison-of-web-worker-sharedworker-and-service-worke-3ff0
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### 1.5 Accessibility (WCAG/ARIA) and testing tools

### WCAG (Web Content Accessibility Guidelines)
- **Canonical identity:** W3C WAI — WCAG 2.2 (REC 2023-10-05); WCAG 3.0 draft in progress
- **Category:** Languages & browser tech › Accessibility
- **Type:** Accessibility standard/guidelines
- **Official URL:** https://www.w3.org/TR/WCAG22/ ; https://www.w3.org/WAI/standards-guidelines/wcag/
- **Description:** The normative accessibility requirements for web content, organized A/AA/AAA. WCAG 2.2 added 9 criteria: 2.4.11 Focus Not Obscured, 2.5.7 Dragging Movements, 2.5.8 Target Size (Minimum 24×24 CSS px), 3.2.6 Consistent Help, 3.3.7 Redundant Entry, 3.3.8 Accessible Authentication, 2.4.12/2.4.13 Focus Appearance (AAA), 4.1.1 removed. WCAG 2.2 AA is the 2026 legal/ethical floor cited across audit guides. WCAG 3.0 (new scoring model) remains draft.
- **Contents inspected:** Search excerpts: software-tester SKILL (new-in-2.2 list), accessibility-tester agent docs (2.2 rule coverage via axe tags `wcag22aa`), formancy/audit docs.
- **Actual capabilities:** Testable success criteria; conformance claims; basis for legislation (ADA, EAA 2025-06-28 enforcement in EU).
- **Usage domain:** All public web content; procurement/compliance.
- **Integration method:** Audit checklists; automated tools map rules to tags.
- **Dependencies:** Not applicable.
- **Availability:** Public W3C Recommendations.
- **Maintenance:** Active (AG WG; WCAG 3.0 drafting).
- **License:** W3C document license (not re-verified).
- **Limitations:** Guidelines, not code — interpretation needed; automated tools catch ~30–57% of violations (human audit mandatory).
- **Related resources:** ARIA, axe-core, Section 508, EN 301 549, EAA.
- **Sources:** https://github.com/mejbaurbahar/software-tester-skills/blob/HEAD/skills/accessibility-testing/SKILL.md ; https://github.com/cj-ant/claude-code-templates/blob/HEAD/cli-tool/components/agents/accessibility/accessibility-tester.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### ARIA (Accessible Rich Internet Applications)
- **Canonical identity:** W3C ARIA 1.2 (REC); ARIA 1.3 in CR/draft; ARIA in HTML; DPUB/Graphics modules
- **Category:** Languages & browser tech › Accessibility
- **Type:** Accessibility semantics specification
- **Official URL:** https://www.w3.org/TR/wai-aria-1.2/ ; https://www.w3.org/TR/wai-aria-1.3/
- **Description:** Roles, states, and properties that expose UI semantics to assistive tech (`role=dialog`, `aria-expanded`, `aria-live`, etc.). Rule #1: prefer native HTML semantics; ARIA fills gaps. axe-core rules heavily target ARIA misuse.
- **Contents inspected:** Search excerpts (axe-core violation classes: "ARIA errors"; audit checklists for names/roles/states, aria-live regions).
- **Actual capabilities:** Semantic enrichment; live regions; widget patterns (APG).
- **Usage domain:** Custom components, SPAs, dynamic content.
- **Integration method:** HTML attributes; validated by axe-core/eslint-plugin-jsx-a11y.
- **Dependencies:** Correct usage (misused ARIA is worse than none).
- **Availability:** Public specs; implemented by browsers + screen readers.
- **Maintenance:** Active (ARIA WG; 1.3 progressing).
- **License:** W3C document license.
- **Limitations:** Does not add behavior/keyboard support — only semantics.
- **Related resources:** WCAG, APG (ARIA Authoring Practices Guide), axe-core, ElementInternals.
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/frontend-engineer/skills/accessibility-wcag-22-aa-axe-core/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### axe-core
- **Canonical identity:** dequelabs/axe-core
- **Category:** Languages & browser tech › Accessibility
- **Type:** Accessibility testing engine (library + CLI)
- **Official URL:** https://github.com/dequelabs/axe-core ; https://www.deque.com/axe/
- **Description:** The industry-standard automated a11y engine (~15k+ GitHub stars per 2026 index; MPL-2.0). Rule tags map to WCAG levels (`wcag2a`, `wcag2aa`, `wcag21aa`, `wcag22aa`). Powers Google Lighthouse a11y audits, Microsoft Accessibility Insights, `@axe-core/playwright`, `@axe-core/cli`, `jest-axe`. Deque claims ~57% of violations detectable automatically (per agent docs citing Deque benchmark).
- **Contents inspected:** Search excerpts: static-analysis index entry (15K+ stars, MPL-2.0, WCAG 2.0/2.1/2.2); agent audit guides (`npx @axe-core/cli <url> --exit --tags wcag2a,wcag2aa,wcag22aa`); Playwright integration pattern.
- **Actual capabilities:** DOM scanning for contrast, ARIA, labels, heading order, keyboard traps (partial), with violation nodes + remediation help URLs.
- **Usage domain:** CI gates, E2E tests, manual audits via DevTools extensions.
- **Integration method:** npm `@axe-core/cli`, `@axe-core/playwright`, `@axe-core/puppeteer`, `jest-axe`; browser extensions.
- **Dependencies:** A DOM (browser/jsdom).
- **Availability:** npm; open source.
- **Maintenance:** Active (Deque).
- **License:** MPL-2.0 (per 2026 index — not re-verified against repo).
- **Limitations:** Cannot catch ~half of WCAG issues (needs manual testing); false positives possible on custom widgets.
- **Related resources:** Lighthouse, pa11y, WAVE, Accessibility Insights, eslint-plugin-jsx-a11y.
- **Sources:** https://github.com/analysis-tools-dev/static-analysis/commit/53620bcf10fa4b07863027ea2ab8c2f7b01daaf ; https://github.com/cj-ant/claude-code-templates/blob/HEAD/cli-tool/components/agents/accessibility/accessibility-tester.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Lighthouse (accessibility auditing)
- **Canonical identity:** GoogleChrome/lighthouse
- **Category:** Languages & browser tech › Accessibility (+ performance/SEO)
- **Type:** Automated page-audit tool (CLI + DevTools + CI)
- **Official URL:** https://github.com/GoogleChrome/lighthouse ; https://developer.chrome.com/docs/lighthouse
- **Description:** Audits pages across performance, accessibility, best practices, SEO. Accessibility category is axe-core-powered. Used via Chrome DevTools, `npx lighthouse --only-categories=accessibility`, and LHCI (`@lhci/cli`) in CI with budgets/assertions.
- **Contents inspected:** Search excerpts (audit recipes: `npx lighthouse <url> --only-categories=accessibility`; LHCI in CI; perf-budget contexts).
- **Actual capabilities:** Scored audits with opportunities/diagnostics; CI gating via LHCI.
- **Usage domain:** Pre-launch audits, CI quality gates, perf budgets.
- **Integration method:** DevTools panel; CLI; Node API; CI action.
- **Dependencies:** Chromium.
- **Availability:** Open source (Apache-2.0).
- **Maintenance:** Active (Google).
- **License:** Apache-2.0 (not re-verified).
- **Limitations:** Lab data (not field); a11y score ≠ conformance.
- **Related resources:** axe-core, PageSpeed Insights, web-vitals, LHCI.
- **Sources:** https://github.com/mejbaurbahar/software-tester-skills/blob/HEAD/skills/accessibility-testing/SKILL.md ; https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/frontend-engineer/skills/accessibility-wcag-22-aa-axe-core/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### pa11y (+ pa11y-ci)
- **Canonical identity:** pa11y/pa11y
- **Category:** Languages & browser tech › Accessibility
- **Type:** CLI accessibility testing tool (CI-focused)
- **Official URL:** https://github.com/pa11y/pa11y ; https://pa11y.org
- **Description:** Command-line a11y tester with multiple runners (default `htmlcs`/HTML_CodeSniffer — WCAG 2.0-era; `--runner axe` for axe-core-backed WCAG 2.1/2.2 coverage), multiple reporters, `pa11y-ci` for sweeping URL lists in CI. ~4.5k stars, LGPL-3.0 per 2026 index. Note: pa11y's `WCAG2AA` standard maps only to wcag2a/wcag21a/wcag2aa/wcag21aa axe tags — no 2.2 coverage by default (needs runnerConfig override).
- **Contents inspected:** Search excerpts: static-analysis index (4.5K stars, LGPL-3.0); accessibility-tester agent doc (runner caveat in detail).
- **Actual capabilities:** URL-by-URL scans with thresholds (`--threshold 0` to fail on any issue); CI-friendly JSON/CSV.
- **Usage domain:** CI gates, static page sweeps.
- **Integration method:** `npx pa11y <url> --standard WCAG2AA --runner axe`; `.pa11yrc` config.
- **Dependencies:** Headless Chromium (bundled via puppeteer).
- **Availability:** npm; open source.
- **Maintenance:** Active-ish (community; slower cadence — exact 2026 state not verified).
- **License:** LGPL-3.0 (per 2026 index — not re-verified).
- **Limitations:** Default runner is dated; 2.2 coverage needs manual config; page-state coverage limited (use Playwright+axe for app states).
- **Related resources:** axe-core, @axe-core/cli, Lighthouse.
- **Sources:** https://github.com/analysis-tools-dev/static-analysis/commit/53620bcf10fa4b07863027ea2ab8c2f7b01daaf ; https://github.com/cj-ant/claude-code-templates/blob/HEAD/cli-tool/components/agents/accessibility/accessibility-tester.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### WAVE (WebAIM)
- **Canonical identity:** WebAIM WAVE (Utah State University)
- **Category:** Languages & browser tech › Accessibility
- **Type:** Visual accessibility evaluation tool (browser extension + online)
- **Official URL:** https://wave.webaim.org
- **Description:** Injects visual feedback icons directly onto the page (errors, alerts, features, structural elements, ARIA). Browser extensions + online tester + API. Complements engine-based tools with human-readable visual overlay.
- **Contents inspected:** Search excerpts (tool tables listing WAVE browser extension).
- **Actual capabilities:** In-page visual audit overlay; contrast checking; structure outline.
- **Usage domain:** Manual audits, designer/developer feedback.
- **Integration method:** Browser extension; wave.webaim.org URL tester; WAVE API (commercial).
- **Dependencies:** None (extension).
- **Availability:** Free extensions; API is paid.
- **Maintenance:** Active (WebAIM).
- **License:** Proprietary (free tools).
- **Limitations:** Manual workflow; not CI-native.
- **Related resources:** axe DevTools, Accessibility Insights, TPGi Contrast Analyzer.
- **Sources:** https://github.com/thebeardedbearsas/claude-craft/blob/HEAD/docs/ACCESSIBILITY.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### eslint-plugin-jsx-a11y
- **Canonical identity:** jsx-eslint/eslint-plugin-jsx-a11y
- **Category:** Languages & browser tech › Accessibility
- **Type:** ESLint plugin (static lint rules)
- **Official URL:** https://github.com/jsx-eslint/eslint-plugin-jsx-a11y
- **Description:** Lint-time a11y rules for JSX: missing `alt`, click handlers without keyboard equivalents, missing label associations, ARIA prop validity, etc. Standard in the 2026 a11y toolchain (ESLint flat config: `plugins: {"jsx-a11y": jsxA11y}`, `rules: jsxA11y.configs.recommended.rules`). Also consumable via oxlint's `jsx-a11y` plugin (oxlint 1.x includes jsx-a11y rules).
- **Contents inspected:** Search excerpts: accessibility SKILL setup (`pnpm add -D eslint-plugin-jsx-a11y`, flat-config recipe); oxlint config templates listing `jsx-a11y` plugin.
- **Actual capabilities:** ~30 static rules catching common JSX a11y bugs at author time.
- **Usage domain:** React/Preact/Solid JSX codebases; CI lint gates.
- **Integration method:** ESLint flat config or oxlint `plugins: ["jsx-a11y"]`.
- **Dependencies:** ESLint (or oxlint).
- **Availability:** npm; MIT.
- **Maintenance:** Active (community).
- **License:** MIT (not re-verified).
- **Limitations:** Static-only; JSX-only (not plain HTML/Vue templates).
- **Related resources:** ESLint, oxlint, axe-core, react-aria.
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/frontend-engineer/skills/accessibility-wcag-22-aa-axe-core/SKILL.md ; https://github.com/jeportie/tskickstart/blob/HEAD/docs/superpowers/plans/2026-08-11-oxlint-linter-option.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Screen readers (NVDA · JAWS · VoiceOver · TalkBack · Orca)
- **Canonical identity:** NVDA (nvaccess.org), JAWS (Freedom Scientific), VoiceOver (Apple), TalkBack (Google), Orca (GNOME)
- **Category:** Languages & browser tech › Accessibility
- **Type:** Assistive technology (manual testing tools)
- **Official URL:** https://www.nvaccess.org (NVDA)
- **Description:** The manual-testing half of a11y: NVDA (free, Windows), JAWS (commercial, Windows), VoiceOver (built-in macOS/iOS), TalkBack (Android), Orca (Linux). 2026 audit guides prescribe minimum matrix: NVDA+Firefox (Win), VoiceOver+Safari (Mac/iOS); full matrix adds JAWS+Chrome, TalkBack+Chrome. Verify names/roles/states announcement, landmarks, aria-live, focus movement on SPA route changes.
- **Contents inspected:** Search excerpts (accessibility SKILLs with screen-reader matrices + VoiceOver/NVDA command references).
- **Actual capabilities:** Speech/braille output; browse/focus modes; rotor/elements lists.
- **Usage domain:** Manual verification of real assistive-tech UX.
- **Integration method:** Installed apps; no code integration.
- **Dependencies:** OS platform.
- **Availability:** NVDA/Orca free; VoiceOver/TalkBack built-in; JAWS commercial.
- **Maintenance:** Active (respective vendors).
- **License:** Varies (NVDA: GPL-2.0).
- **Limitations:** Manual, slow; behavior differs per SR+browser pair.
- **Related resources:** ARIA APG, Accessibility Object Model (AOM proposals).
- **Sources:** https://github.com/majiayu000/claude-skill-registry/blob/HEAD/skills/other/other/accessibility-testing-jlaws-dotfiles/SKILL.md ; https://github.com/mejbaurbahar/software-tester-skills/blob/HEAD/skills/accessibility-testing/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Nu HTML Checker (validator.w3.org/nu)
- **Canonical identity:** validator/validator (W3C)
- **Category:** Languages & browser tech › Accessibility-adjacent › HTML conformance
- **Type:** Markup validation service + CLI/JAR
- **Official URL:** https://validator.w3.org/nu/ ; repo: github.com/validator/validator
- **Description:** The official HTML conformance checker: validates documents against the HTML Living Standard (+ ARIA in HTML rules). Available as hosted service, `vnu.jar` CLI, and Docker image for CI.
- **Contents inspected:** Not directly searched this session; long-established tool included for systematic coverage.
- **Actual capabilities:** Parse + conformance error reporting; a11y-adjacent checks (duplicate IDs, bad ARIA).
- **Usage domain:** CI HTML validation, authoring QA.
- **Integration method:** Web UI; `java -jar vnu.jar`; npm `vnu-jar` wrapper.
- **Dependencies:** Java (for JAR).
- **Availability:** Free; open source.
- **Maintenance:** Active (W3C).
- **License:** MIT (not re-verified).
- **Limitations:** Conformance ≠ accessibility; some valid-but-inaccessible patterns pass.
- **Related resources:** HTMLHint, axe-core, WHATWG HTML.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified (2026 maintenance not checked)

### 1.6 Internationalization (i18n) standards and libraries

### Unicode CLDR + ICU + BCP 47
- **Canonical identity:** Unicode CLDR (Common Locale Data Repository); ICU (International Components for Unicode); BCP 47 (IETF language tags)
- **Category:** Languages & browser tech › i18n standards
- **Type:** Locale data + libraries + tag standard
- **Official URL:** https://cldr.unicode.org ; https://icu.unicode.org ; https://www.rfc-editor.org/info/bcp47
- **Description:** CLDR is the canonical locale dataset (date/number formats, plurals, territories) consumed by ECMA-402 implementations, ICU4X/ICU4C/ICU4J libraries, and OSes. BCP 47 defines language tags (`en-US`, `pt-BR`, `zh-Hant-TW`). i18n libraries ultimately format via `Intl` (CLDR-backed) or ICU MessageFormat.
- **Contents inspected:** Search excerpts (i18n template docs referencing BCP-47 tags, fallback chains `pt-BR → pt → en`, ICU MessageFormat usage).
- **Actual capabilities:** Authoritative locale data; formatting/collation libraries; tag parsing.
- **Usage domain:** Every localized product.
- **Integration method:** Bundled in browsers/runtimes (ICU); CLDR JSON via npm (`cldr-core`) for custom pipelines.
- **Dependencies:** Version alignment (CLDR release vs runtime).
- **Availability:** Open (Unicode license).
- **Maintenance:** Active (Unicode Consortium; ~2 CLDR releases/year).
- **License:** Unicode License (not re-verified).
- **Limitations:** Data size (subset for web); version skew across engines.
- **Related resources:** ECMA-402, FormatJS, Globalize.js (historical), ICU4X.
- **Sources:** https://github.com/siliconyouth/project-architect/blob/HEAD/skills/project-architect/references/templates/INTERNATIONALIZATION.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### i18next (+ react-i18next)
- **Canonical identity:** i18next/i18next; i18next/react-i18next
- **Category:** Languages & browser tech › i18n libraries
- **Type:** Internationalization framework (library)
- **Official URL:** https://www.i18next.com ; repo: github.com/i18next/i18next
- **Description:** The most widely used JS i18n framework: translation function `t()`, namespaces, plurals, interpolation, language detection, backend connectors (HTTP, FS), ecosystem (react-i18next, next-i18next, ICU plugin `i18next-icu`). Own interpolation/plural format by default (ICU via plugin). Tolgee provides an i18next bridge (`@tolgee/i18next`) for in-context editing.
- **Contents inspected:** Search excerpts: firsthandjs i18n guide (i18next init + `t('greeting')`); databasus ADR (required config: `returnNull:false`, `nsSeparator:false`, `escapeValue:false` for React); Tolgee-i18next bridge article.
- **Actual capabilities:** Runtime translation lookup, lazy namespace loading, plural rules, formatting, missing-key handling.
- **Usage domain:** SPAs, SSR apps, Node CLIs — any JS project needing translations.
- **Integration method:** npm `i18next` (+ framework binding); JSON/PO resource files.
- **Dependencies:** None core (plugins optional).
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Runtime lookup cost; bundle size heavier than compile-time extractors (intlayer benchmark claims 3–8× lighter alternatives — vendor-adjacent claim).
- **Related resources:** react-i18next, next-i18next, Tolgee, FormatJS, Lingui, i18next-icu.
- **Sources:** https://github.com/firsthandjs/firsthand/blob/HEAD/docs/guide/12-internationalisation.md ; https://github.com/databasus/databasus/blob/HEAD/openspec/changes/translate-frontend-ui/design.md ; https://DEV.to/tolgee_i18n/taking-localization-to-i18next-level-146a
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### FormatJS (react-intl)
- **Canonical identity:** formatjs/formatjs (react-intl is the React binding)
- **Category:** Languages & browser tech › i18n libraries
- **Type:** ICU MessageFormat i18n library suite
- **Official URL:** https://formatjs.github.io ; repo: github.com/formatjs/formatjs
- **Description:** Yahoo/Verizon-originated suite built on ICU MessageFormat: `react-intl` components/hooks, `@formatjs/cli` for message extraction, ESLint plugin. Heavier compile step than i18next but standards-based message syntax shared with Java/PHP ecosystems.
- **Contents inspected:** Search excerpts (comparisons: "heavier compile step for ICU messages"; listed alongside i18next/Lingui as plain-JS compatible).
- **Actual capabilities:** ICU message parsing/formatting, rich-text elements in messages, locale data loading, extraction CLI.
- **Usage domain:** React apps needing ICU-standard messages.
- **Integration method:** npm `@formatjs/*`, `react-intl`; Babel/SWC plugin for extraction.
- **Dependencies:** `intl-messageformat` parser.
- **Availability:** npm; BSD-3-Clause.
- **Maintenance:** Active.
- **License:** BSD-3-Clause (not re-verified).
- **Limitations:** Heavier toolchain; React-centric mindshare declining vs next-intl/Lingui per 2026 commentary (single-source opinion).
- **Related resources:** i18next, Lingui, next-intl, ICU.
- **Sources:** https://github.com/databasus/databasus/blob/HEAD/openspec/changes/translate-frontend-ui/design.md ; https://github.com/firsthandjs/firsthand/blob/HEAD/docs/guide/12-internationalisation.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Lingui
- **Canonical identity:** lingui/js-lingui
- **Category:** Languages & browser tech › i18n libraries
- **Type:** i18n library + message extraction CLI (compile-time catalogs)
- **Official URL:** https://lingui.dev ; repo: github.com/lingui/js-lingui
- **Description:** Lightweight (~3kb core claim) i18n with ICU MessageFormat, build-time message extraction (`lingui extract`), catalog validation, React/Vue bindings, `eslint-plugin-lingui`. v6.x line in 2026 (`@lingui/core@6.6.0` referenced). Uses source text as key by default (editing English invalidates translations — noted as a rejection reason in one ADR). Works in any JS project.
- **Contents inspected:** Search excerpts: thenaubit ADR-006 (adopted Lingui + expo-localization; `lingui:extract` workflow; oxlint JS-plugin lint); databasus ADR (rejected: source-text keys); intlayer benchmark (version reference).
- **Actual capabilities:** `t` macro / `useLingui`, PO/JSON catalogs, plural/gender ICU macros, pseudo-localization.
- **Usage domain:** React/Vue/Node apps wanting small runtime + extraction workflow.
- **Integration method:** npm `@lingui/core @lingui/react @lingui/cli`; SWC/Babel macro plugin; `lingui extract/compile`.
- **Dependencies:** Build plugin for macros.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Source-as-key default is controversial; smaller ecosystem than i18next.
- **Related resources:** i18next, FormatJS, next-intl, Tolgee.
- **Sources:** https://github.com/thenaubit/explora-app-example/blob/HEAD/docs/decisions/adr-006-lingui-i18n.md ; https://github.com/yangguan-xue/intlayer/blob/HEAD/docs/docs/en-GB/benchmark/nextjs.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Tolgee
- **Canonical identity:** tolgee/tolgee-platform (+ tolgee-js SDKs)
- **Category:** Languages & browser tech › i18n platforms
- **Type:** Open-source localization platform + in-context JS SDKs
- **Official URL:** https://tolgee.io ; repo: github.com/tolgee/tolgee-platform
- **Description:** Self-hostable translation management with in-context editing: translators edit strings directly in the running app (invisible-text key marking), screenshots, machine-translation pre-fill. JS SDKs (`@tolgee/react`, `@tolgee/i18next` bridge, `@tolgee/ui`). OSS (Apache-2.0 per 2026 listings). Positioned as the OSS alternative to Lokalise/Phrase/Crowdin for teams wanting in-context workflows.
- **Contents inspected:** Search excerpts: Bablic-alternatives discussion (Tolgee = closest OSS drop-in); intlayer benchmark (`@tolgee/react@7.2.0` — no type safety noted); Tolgee-i18next bridge article.
- **Actual capabilities:** Key management, in-context editor, translation memory, MT integrations, REST API, webhooks.
- **Usage domain:** Teams localizing web apps with non-developer translators.
- **Integration method:** Self-host (Docker) or Tolgee Cloud; SDK wraps i18next or standalone.
- **Dependencies:** Backend service (Java/Postgres) for self-host.
- **Availability:** OSS + cloud.
- **Maintenance:** Active.
- **License:** Apache-2.0 (platform; not re-verified).
- **Limitations:** Heavier adoption than file-based libraries; type safety gaps noted in 2026 review (single source).
- **Related resources:** i18next, Weblate, Pontoon, Crowdin, Lokalise, Phrase.
- **Sources:** https://DEV.to/tolgee_i18n/taking-localization-to-i18next-level-146a ; https://github.com/yangguan-xue/intlayer/blob/HEAD/docs/docs/en-GB/benchmark/nextjs.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### next-intl
- **Canonical identity:** amannn/next-intl
- **Category:** Languages & browser tech › i18n libraries
- **Type:** Next.js-focused i18n library (ICU MessageFormat)
- **Official URL:** https://next-intl.dev ; repo: github.com/amannn/next-intl
- **Description:** The trendiest Next.js i18n option in 2026 (`next-intl@4.14.2` referenced): App Router integration, `useTranslations`, `setRequestLocale()`, ICU messages. Critiques in 2026 benchmark: heavier client bundle (~14.7kb provider+hook), static-rendering pitfalls with namespaced dictionaries, optimization complexity.
- **Contents inspected:** Search excerpts (intlayer benchmark: version, bundle weight, static-rendering caveat).
- **Actual capabilities:** Server/client translation hooks, locale routing middleware, timezone-aware formatting.
- **Usage domain:** Next.js App Router apps.
- **Integration method:** npm `next-intl`; middleware + provider setup.
- **Dependencies:** Next.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Next.js-only; bundle/static-render trade-offs per 2026 benchmark (single source — treat as perspective).
- **Related resources:** next-i18next, Lingui, Intlayer, Paraglide JS.
- **Sources:** https://github.com/yangguan-xue/intlayer/blob/HEAD/docs/docs/en-GB/benchmark/nextjs.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (single detailed source)

---

## 2. Build, compile, and package tooling

### 2.1 Package managers (JS/TS)

### npm
- **Canonical identity:** npm/cli — v11.x (11.19.0 bundled with Node 24.20.0)
- **Category:** Build tooling › Package managers
- **Type:** Package manager CLI + client for the npm registry
- **Official URL:** https://www.npmjs.com ; repo: github.com/npm/cli ; docs: https://docs.npmjs.com
- **Description:** The default JS package manager, bundled with Node.js. v11: faster installs, `package-lock.json` lockfile, workspaces, `npm audit`, `npm outdated/update`, `npx`. npm 11.19+ skips dependency install scripts by default (allowScripts allowlist) — supply-chain hardening that broke some postinstall flows in 2026 upgrades.
- **Contents inspected:** Search excerpts: package-manager comparisons (npm 11 as "safe default"); Node 24 upgrade issue (npm 11.19.0 allowScripts behavior); install-speed benchmarks (slowest of the four, ~45s cold Next.js install in one 2026 comparison).
- **Actual capabilities:** Install/resolve/publish; `npm ci` frozen installs; workspaces; provenance publishing (`--provenance` via OIDC trusted publishing); `packageManager` field honored by Corepack.
- **Usage domain:** Default for libraries, tutorials, solo projects, maximal ecosystem compat.
- **Integration method:** Bundled with Node; `npm install`; CI via `npm ci`.
- **Dependencies:** Node.js; npm registry.
- **Availability:** Bundled; open source.
- **Maintenance:** Active (GitHub/Microsoft).
- **License:** Artistic-2.0 (not re-verified).
- **Limitations:** Flat node_modules (phantom dependencies possible); slowest installs; highest disk use (full copies per project).
- **Related resources:** pnpm, Yarn, Bun, Deno, JSR, Corepack, npm registry.
- **Sources:** https://dev.to/hamidrazadev/pnpm-vs-npm-vs-yarn-which-package-manager-should-you-actually-use-3ke3 ; https://github.com/resetshop/angular-nx-standalone-starter/issues/535 ; https://dev.to/dudychmarian/npm-vs-yarn-vs-pnpm-vs-bun-which-package-manager-should-you-use-in-2026-3j2o
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### pnpm
- **Canonical identity:** pnpm/pnpm — v10.x stable; v11.x current stable (11.23.0 referenced); v12 RC
- **Category:** Build tooling › Package managers
- **Type:** Fast, disk-efficient package manager (content-addressable store + hard links)
- **Official URL:** https://pnpm.io ; repo: github.com/pnpm/pnpm
- **Description:** Stores each package version once in a global content-addressable store, hard-linking into projects — massive disk savings and fast installs (~28s cold / 6s warm Next.js in 2026 comparison). Strict non-flat `node_modules` prevents phantom dependencies. pnpm 10+: `manage-package-manager-versions` on by default (auto-switches to the `packageManager`-pinned pnpm); build scripts blocked by default (`allowBuilds` map / `strictDepBuilds`); `pnpm-workspace.yaml` with `catalog:` protocol for shared version pinning; `pnpm dlx` (`pnx`) can provision other package managers/runtimes. Workspaces are the monorepo default pairing with Turborepo.
- **Contents inspected:** Search excerpts: comparisons (pnpm 10/11, catalogs, allowBuilds); valorjesson pnpm changeset (package-manager-of-package-managers feature); mq-yuan workflow doc (pnpm 11.23.0, manage-package-manager-versions, allowScripts policy).
- **Actual capabilities:** Install/link/publish; workspaces; catalogs; `pnpm outdated/update`; `pnpm audit`; `pnpm dedupe`; `pnpm deploy`; patch-package workflow.
- **Usage domain:** Monorepos, multi-project machines, CI cost control, correctness-focused teams.
- **Integration method:** `pnpm install`; `pnpm-workspace.yaml`; `packageManager: pnpm@x.y.z`.
- **Dependencies:** Node.js; npm registry (or mirrors).
- **Availability:** Open source; standalone installers.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Strictness breaks packages relying on phantom deps (needs `public-hoist-pattern`/`shamefully-hoist`); build-script allowlist is a new 2026 workflow to learn.
- **Related resources:** npm, Yarn, Bun, Turbo, Changesets, Corepack.
- **Sources:** https://dev.to/hamidrazadev/pnpm-vs-npm-vs-yarn-which-package-manager-should-you-actually-use-3ke3 ; https://github.com/valorjesson-commits/pnpm/blob/HEAD/.changeset/package-manager-of-package-managers.md ; https://github.com/mq-yuan/mq-yuan.github.io/blob/HEAD/docs/plan/Init/10_Development_Workflow.md ; https://github.com/jackmcpickle/mailclad/blob/HEAD/docs/research-2026-08-21-package-manager-qol-agentic.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Yarn (Classic 1.x + Berry 2/3/4)
- **Canonical identity:** yarnpkg/berry (v4.x current); yarnpkg/yarn (Classic 1.22.x, frozen)
- **Category:** Build tooling › Package managers
- **Type:** Package manager — two distinct generations
- **Official URL:** https://yarnpkg.com ; repos: github.com/yarnpkg/berry, github.com/yarnpkg/yarn
- **Description:** Yarn Classic 1.22: the 2016 original; maintenance/security-patches-only since 2020 — "a museum piece that runs your build" (2026 commentary). Yarn Berry (v2–v4, current 4.x): complete rewrite with Plug'n'Play (no node_modules; `.pnp.cjs` loader), zero-installs (check in `.yarn/cache`), constraints, plugin system, `yarn.lock`. Strongest for large enterprise monorepos; steeper learning curve; PnP breaks some tooling (needs `nodeLinker: node-modules` escape hatch).
- **Contents inspected:** Search excerpts: tech-insider Yarn-vs-npm 2026 (three-way framing npm 11 / Berry 4 / Classic 1.22); dev.to comparisons; mailclad research (Yarn ≥4.14 `enableScripts:false` default, `dependenciesMeta.<pkg>.built` allowlist).
- **Actual capabilities:** Install/resolve/publish; workspaces; PnP; `yarn dedupe --check`; `yarn constraints`; release workflow plugin.
- **Usage domain:** Large team monorepos (Berry); legacy projects (Classic).
- **Integration method:** Corepack (`yarn@4`); `yarn install`; `.yarnrc.yml`.
- **Dependencies:** Node.js.
- **Availability:** Open source.
- **Maintenance:** Berry active; Classic frozen.
- **License:** BSD-2-Clause (not re-verified).
- **Limitations:** PnP incompatibilities (native addons, some CLIs); Berry's pnpm support in Volta-era tooling uneven.
- **Related resources:** npm, pnpm, Bun, Corepack, Turbo.
- **Sources:** https://tech-insider.org/yarn-vs-npm-2026/ ; https://dev.to/hamidrazadev/pnpm-vs-npm-vs-yarn-which-package-manager-should-you-actually-use-3ke3 ; https://github.com/jackmcpickle/mailclad/blob/HEAD/docs/research-2026-08-21-package-manager-qol-agentic.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Bun (package manager)
- **Canonical identity:** oven-sh/bun — `bun install` (part of Bun toolkit)
- **Category:** Build tooling › Package managers
- **Type:** Package manager (subcommand of Bun runtime)
- **Official URL:** https://bun.sh/docs/installation ; repo: github.com/oven-sh/bun
- **Description:** Native-speed installer (fastest in 2026 comparisons: ~8s cold / 2s warm Next.js): global module cache, binary lockfile `bun.lockb` (text `bun.lock` also supported), `bunx` runner, `trustedDependencies` install-script allowlist, isolated installs option, accepts pnpm `catalog:` in overrides. Primary choice for greenfield speed; lockfile differs from npm/pnpm.
- **Contents inspected:** Search excerpts: dev.to install-speed table; package-manager comparisons; mailclad script-policy table.
- **Actual capabilities:** `bun install/add/remove/update/outdated`; workspaces; `bun pm`; lifecycle-script trust model.
- **Usage domain:** Greenfield projects, scripts, CI speed.
- **Integration method:** `bun install`; `bun.lockb` committed.
- **Dependencies:** Bun binary.
- **Availability:** Bundled with Bun.
- **Maintenance:** Active.
- **License:** MIT (Bun).
- **Limitations:** Lockfile not interchangeable with npm/pnpm; some registries/tooling assume package-lock.
- **Related resources:** Bun (runtime), npm, pnpm, Yarn.
- **Sources:** https://dev.to/pockit_tools/deno-2-vs-nodejs-vs-bun-in-2026-the-complete-javascript-runtime-comparison-1elm ; https://dev.to/dudychmarian/npm-vs-yarn-vs-pnpm-vs-bun-which-package-manager-should-you-use-in-2026-3j2o
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Corepack
- **Canonical identity:** nodejs/corepack (ships with Node.js)
- **Category:** Build tooling › Package managers
- **Type:** Package-manager version manager/shim (experimental)
- **Official URL:** https://github.com/nodejs/corepack ; docs: https://nodejs.org/api/corepack.html
- **Description:** Ships with Node; activates the exact package manager + version from `packageManager` in package.json (`corepack enable`, `corepack use`). 2026 status: still experimental in Node 24; REMOVED in Node 25+ (per 2026 workflow docs); pnpm 10+ self-manages versions via `manage-package-manager-versions`, reducing Corepack's role.
- **Contents inspected:** Search excerpts: mq-yuan workflow ("Do not use corepack — still experimental in Node 24, removed in Node 25+"); package-manager comparisons (`packageManager` field supported by corepack).
- **Actual capabilities:** Shim `yarn`/`pnpm`/`npm` to pinned versions without global installs.
- **Usage domain:** Teams pinning PM versions (declining use).
- **Integration method:** `corepack enable`; `packageManager` field.
- **Dependencies:** Node.js 16–24.
- **Availability:** Bundled (Node ≤24).
- **Maintenance:** Effectively end-of-life path (removed 25+).
- **License:** MIT (not re-verified).
- **Limitations:** Experimental; gone in Node 25+; superseded by pnpm self-management and mise.
- **Related resources:** Volta, mise, fnm, pnpm.
- **Sources:** https://github.com/mq-yuan/mq-yuan.github.io/blob/HEAD/docs/plan/Init/10_Development_Workflow.md ; https://dev.to/_d7eb1c1703182e3ce1782/npm-vs-pnpm-vs-yarn-package-manager-showdown-2026-benchmarks-2c38
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Volta (status: stood down)
- **Canonical identity:** volta-cli/volta
- **Category:** Build tooling › Package managers
- **Type:** JavaScript toolchain version manager (Node/npm/Yarn/pnpm pinning)
- **Official URL:** https://volta.sh ; repo: github.com/volta-cli/volta
- **Description:** Pinned Node + package-manager versions per project via `volta` key in package.json, with transparent shims (no shell hook). 2026 status: maintainers have stood the project down; mise is the recommended successor (per techearl 2026 guide). pnpm support stayed experimental behind `VOLTA_FEATURE_PNPM=1`.
- **Contents inspected:** Search excerpts: techearl nvm-vs-fnm-vs-Volta ("maintainers have stood it down"); mise recommended successor.
- **Actual capabilities:** (Historical) `volta install/pin`; per-project toolchain switching.
- **Usage domain:** Legacy team repos still carrying `volta` pins.
- **Integration method:** `volta` key in package.json.
- **Dependencies:** Rust binary.
- **Availability:** Open source (existing releases).
- **Maintenance:** Stood down (2026) — treat as unmaintained.
- **License:** BSD-2-Clause (not re-verified).
- **Limitations:** No future updates; migrate to mise/fnm.
- **Related resources:** mise, fnm, asdf, Corepack.
- **Sources:** https://techearl.com/nvm-vs-fnm-vs-volta ; https://techearl.com/how-to-update-node-js-version
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (stand-down from one detailed guide; corroborated by mise-successor framing)

### fnm
- **Canonical identity:** Schniz/fnm (Fast Node Manager)
- **Category:** Build tooling › Package managers
- **Type:** Node.js version manager (Rust)
- **Official URL:** https://github.com/Schniz/fnm
- **Description:** Rust rewrite of nvm's model: fast shell startup, `.nvmrc`/`.node-version` support, `--use-on-cd` auto-switching, Windows support, `--corepack-enabled` flag. 2026 verdict across guides: "fnm for a personal machine, mise for a team monorepo."
- **Contents inspected:** Search excerpts: techearl comparison (hook mechanism, speed); phillip-le setup docs (install, fish hook, corepack flag); mq-yuan workflow (fnm 1.39.0 + `.node-version` pin).
- **Actual capabilities:** Install/switch Node versions; auto-switch on cd; `.node-version` resolution.
- **Usage domain:** Individual developers' machines.
- **Integration method:** Shell hook `eval "$(fnm env --use-on-cd)"`.
- **Dependencies:** Shell.
- **Availability:** Open source; all OSes.
- **Maintenance:** Active.
- **License:** GPL-3.0 (not re-verified — fnm is GPL; flag as not verified).
- **Limitations:** Per-user (not per-project enforcement); needs shell hook.
- **Related resources:** nvm, mise, Volta, asdf.
- **Sources:** https://techearl.com/nvm-vs-fnm-vs-volta ; https://github.com/phillip-le/phillip-le.github.io/blob/HEAD/src/content/docs/setup/managing-node-version.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### mise (mise-en-place)
- **Canonical identity:** jdx/mise
- **Category:** Build tooling › Package managers
- **Type:** Polyglot runtime version manager (Rust; asdf successor)
- **Official URL:** https://mise.jdx.dev ; repo: github.com/jdx/mise
- **Description:** Manages Node, Python, Go, Rust, etc. versions per project (`mise.toml`/`.node-version`/`.tool-versions`); Volta's recommended successor; 2026 team-monorepo default ("mise for a team monorepo"). Also handles env vars and tasks.
- **Contents inspected:** Search excerpts: techearl ("Volta's recommended successor"; "mise for a team monorepo"); devhelp WHY-NOT-MISE (mise manages runtime versions); nodepilot changelog (mise.toml support).
- **Actual capabilities:** `mise install/use`; shims; per-directory env; task runner.
- **Usage domain:** Team repos, polyglot stacks.
- **Integration method:** `mise.toml`; shims in PATH.
- **Dependencies:** Rust binary.
- **Availability:** Open source (MIT).
- **Maintenance:** Active (jdx).
- **License:** MIT (not re-verified).
- **Limitations:** Broader scope than needed for Node-only shops; shim overhead.
- **Related resources:** asdf, Volta, fnm, direnv.
- **Sources:** https://techearl.com/how-to-update-node-js-version ; https://github.com/sshivanshg/devhelp/blob/HEAD/docs/WHY-NOT-MISE.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### nvm (+ nvm.fish, n)
- **Canonical identity:** nvm-sh/nvm
- **Category:** Build tooling › Package managers
- **Type:** Node.js version manager (bash script)
- **Official URL:** https://github.com/nvm-sh/nvm
- **Description:** The most widely documented Node version manager: bash script shimming node/npm/npx; `.nvmrc` per-project; manual `nvm use`. Slow shell startup (subshell per cd hook) vs fnm/mise. `n` (tj/n) is a simpler no-hook alternative; nvm.fish is a Fish port.
- **Contents inspected:** Search excerpts: techearl guide (install/use/.nvmrc; slowness note); which-where commit (fnm/nvm/volta command routing).
- **Actual capabilities:** Install/switch/alias Node versions.
- **Usage domain:** Legacy docs, tutorials, existing setups.
- **Integration method:** Sourced bash script; `.nvmrc`.
- **Dependencies:** bash/curl.
- **Availability:** Open source.
- **Maintenance:** Active (slow cadence).
- **License:** MIT (not re-verified).
- **Limitations:** Slow; bash-only (Windows needs nvm-windows, separate project).
- **Related resources:** fnm, mise, n, nvm.fish.
- **Sources:** https://techearl.com/how-to-update-node-js-version ; https://github.com/akarachen/which-where/commit/f87552d52ca8d9e12381285d734de115a5f6b3a3
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### 2.1b Python package managers

### uv
- **Canonical identity:** astral-sh/uv — 0.11.x (0.11.3 referenced Apr 2026); 0.4 added workspaces, 0.5 stabilized `uv build`/`uv publish`
- **Category:** Build tooling › Package managers (Python)
- **Type:** Python package + project manager (Rust, single binary)
- **Official URL:** https://docs.astral.sh/uv/ ; repo: github.com/astral-sh/uv ; install: https://astral.sh/uv/install.sh
- **Description:** Astral's Rust tool consolidating venv creation + resolution + locking + install + Python-version management + tool running (`uv tool install` ≈ pipx) + build/publish. 10–100× faster than pip (parallel resolver, global cache). `uv.lock` committed; `uv sync --frozen` for reproducible installs; PEP 621/735-native `pyproject.toml`; `uv python install 3.14` (own Python builds, no pyenv); `exclude-newer` freshness floor for supply-chain safety. 82k+ GitHub stars; the default recommendation for new Python projects in 2026. Replaces pip+pip-tools+virtualenv+pyenv+pipx and much of Poetry/PDM.
- **Contents inspected:** Search excerpts: two 2026 ADRs choosing uv (lockfile policy, alternatives analysis); bb-plugins uv SKILL (commands, versions); Medium pieces (0.11.3, star count); rye deprecation note (uv is the successor).
- **Actual capabilities:** `uv init/add/remove/sync/lock/run/tool/build/publish/python`; workspaces; dependency groups (PEP 735).
- **Usage domain:** Python applications, libraries, scripts, CI.
- **Integration method:** Standalone binary; `pyproject.toml` + `uv.lock`; `.python-version`.
- **Dependencies:** None (static binary; downloads its own Pythons).
- **Availability:** Open source; all OSes.
- **Maintenance:** Very active (Astral; releases every ~2–3 days per 2026 press).
- **License:** MIT/Apache-2.0 (not re-verified).
- **Limitations:** Young (no LTS series); `uv pip` retains pip semantics quirks; conda-style non-Python deps out of scope (see pixi).
- **Related resources:** pip, Poetry, PDM, Hatch, pipx, Rye (deprecated→uv), pixi, Ruff (same vendor).
- **Sources:** https://github.com/dgrauet/intendant/blob/HEAD/docs/adr/0002-uv-as-dependency-manager.md ; https://github.com/pangamu1/fintech-medallion-portfolio/blob/HEAD/docs/adr/0003-uv-for-python-dependency-management.md ; https://github.com/k0d3r1s/bb-plugins/blob/HEAD/plugins/devkit/content/skills/python-uv/SKILL.md ; https://medium.com/the-pythonworld/the-python-package-manager-nobody-is-talking-about-yet-e0b4cfb177cd
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### pip
- **Canonical identity:** pypa/pip (ships with Python)
- **Category:** Build tooling › Package managers (Python)
- **Type:** Python package installer (baseline)
- **Official URL:** https://pip.pypa.io ; repo: github.com/pypa/pip
- **Description:** The default installer since 2011: installs from PyPI, no venv/lockfile/version management of its own (paired with `venv`, `pyenv`, `pip-tools`). Still the universal baseline; `requirements.txt` interop target (`uv export` generates it).
- **Contents inspected:** Search excerpts (uv ADRs: "pip + venv + pip-tools — three tools, no standard lockfile verb").
- **Actual capabilities:** `pip install/uninstall/freeze/list/check`; wheel/sdist builds via build backends.
- **Usage domain:** Legacy projects, containers, simple scripts.
- **Integration method:** `python -m pip`; requirements files.
- **Dependencies:** Python; PyPI.
- **Availability:** Bundled with Python.
- **Maintenance:** Active (PyPA).
- **License:** MIT (not re-verified).
- **Limitations:** No locking (needs pip-tools), no venv management, slow resolver on big trees.
- **Related resources:** uv, pip-tools, virtualenv, PyPI, pip-audit.
- **Sources:** https://medium.com/@mansi.patel7279s/part-2-why-uv-is-replacing-pip-and-poetry-and-you-should-let-it-7f78f94b6b3c ; https://github.com/dgrauet/intendant/blob/HEAD/docs/adr/0002-uv-as-dependency-manager.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Poetry
- **Canonical identity:** python-poetry/poetry
- **Category:** Build tooling › Package managers (Python)
- **Type:** Python dependency management + packaging/publishing
- **Official URL:** https://python-poetry.org ; repo: github.com/python-poetry/poetry
- **Description:** Mature (pre-uv default) tool bundling dependency resolution, venvs, `poetry.lock`, and PyPI publishing. Historically used its own `[tool.poetry]` pyproject table (PEP 621 support added later). 2026 verdict: mature but slower resolver; overkill for applications; losing new-project share to uv.
- **Contents inspected:** Search excerpts (uv ADRs: "mature but slow; non-PEP-621 config until recently").
- **Actual capabilities:** `poetry add/install/lock/publish/build`; dependency groups; plugin system.
- **Usage domain:** Existing Python libraries/apps; teams standardized pre-2024.
- **Integration method:** `pyproject.toml` + `poetry.lock`.
- **Dependencies:** Python.
- **Availability:** Open source.
- **Maintenance:** Active (slower than uv).
- **License:** MIT (not re-verified).
- **Limitations:** Slower resolver; publishing-centric workflow heavier than needed for apps.
- **Related resources:** uv, PDM, Hatch, pip.
- **Sources:** https://github.com/pangamu1/fintech-medallion-portfolio/blob/HEAD/docs/adr/0003-uv-for-python-dependency-management.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### PDM
- **Canonical identity:** pdm-project/pdm
- **Category:** Build tooling › Package managers (Python)
- **Type:** PEP-582/621-native Python package manager
- **Official URL:** https://pdm-project.org ; repo: github.com/pdm-project/pdm
- **Description:** Standards-compliant manager (PEP 621 project metadata, PEP 582 `__pypackages__` local packages dir), `pdm.lock` lockfile. "Good but less community momentum" vs uv in 2026 ADRs; still viable for standards-purist teams.
- **Contents inspected:** Search excerpts (uv ADR alternatives: "good but less community momentum").
- **Actual capabilities:** `pdm add/install/lock/publish`; venv or `__pypackages__` layouts.
- **Usage domain:** Standards-focused Python projects.
- **Integration method:** `pyproject.toml` + `pdm.lock`.
- **Dependencies:** Python.
- **Availability:** Open source.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Mindshare loss to uv; smaller plugin ecosystem.
- **Related resources:** uv, Poetry, Hatch.
- **Sources:** https://github.com/dgrauet/intendant/blob/HEAD/docs/adr/0002-uv-as-dependency-manager.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (thin sourcing)

### Hatch
- **Canonical identity:** pypa/hatch
- **Category:** Build tooling › Package managers (Python)
- **Type:** Python project manager + build backend (PyPA)
- **Official URL:** https://hatch.pypa.io ; repo: github.com/pypa/hatch
- **Description:** PyPA's project manager: environments (`hatch env`), versioning, build backend (`hatchling`), publishing. Matrix-based env management is its distinctive strength. Listed among viable alternatives in 2026 uv ADRs.
- **Contents inspected:** Search excerpts (uv ADR tool listings).
- **Actual capabilities:** `hatch new/env/run/build/publish`; `hatchling` build backend.
- **Usage domain:** Libraries wanting a PyPA-blessed workflow; build backend for others.
- **Integration method:** `pyproject.toml` (`[tool.hatch]`); `hatch.toml`.
- **Dependencies:** Python.
- **Availability:** Open source.
- **Maintenance:** Active (PyPA).
- **License:** MIT (not re-verified).
- **Limitations:** Less mindshare than uv/Poetry for app dependency management.
- **Related resources:** uv, PDM, Poetry, flit (historical).
- **Sources:** https://github.com/pangamu1/fintech-medallion-portfolio/blob/HEAD/docs/adr/0003-uv-for-python-dependency-management.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (thin sourcing)

### pipx
- **Canonical identity:** pypa/pipx
- **Category:** Build tooling › Package managers (Python)
- **Type:** Isolated Python CLI-app installer
- **Official URL:** https://pipx.pypa.io ; repo: github.com/pypa/pipx
- **Description:** Installs Python CLI tools into isolated venvs and exposes their binaries (`pipx install black`). The use case uv now covers with `uv tool install`; pipx remains the PyPA-standard standalone option.
- **Contents inspected:** Search excerpts (uv docs: "replaces pipx"; uv SKILL: `uv tool install`).
- **Actual capabilities:** `pipx install/uninstall/upgrade/run`.
- **Usage domain:** Installing Python CLIs without polluting environments.
- **Integration method:** `pipx install <pkg>`; `~/.local/bin`.
- **Dependencies:** Python.
- **Availability:** Open source.
- **Maintenance:** Active (PyPA).
- **License:** MIT (not re-verified).
- **Limitations:** Single-purpose; uv subsumes it for uv users.
- **Related resources:** uv tool, pip, Homebrew (for CLIs).
- **Sources:** https://github.com/k0d3r1s/bb-plugins/blob/HEAD/plugins/devkit/content/skills/python-uv/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (thin sourcing)

### Rye (Archived / deprecated)
- **Canonical identity:** astral-sh/rye (originally mitsuhiko/rye)
- **Category:** Build tooling › Package managers (Python)
- **Type:** Python project manager (unified experience) — DEPRECATED
- **Official URL:** https://github.com/astral-sh/rye (archived note); was https://rye.astral.sh
- **Description:** Armin Ronacher's "hassle-free Python experience": unified Python installs, pyproject projects, venvs, global tools. Astral (which hired/adopted it) officially discontinued it: "Rye is no longer developed... use uv, the successor project." Migration guide published; no further updates including security updates.
- **Contents inspected:** Search excerpt of the archived README deprecation note (verbatim).
- **Actual capabilities:** (Historical) `rye init/sync/add`; Python version management.
- **Usage domain:** None going forward — migrate.
- **Integration method:** N/A (deprecated).
- **Dependencies:** N/A.
- **Availability:** Binaries still downloadable; unmaintained.
- **Maintenance:** None — deprecated by maintainer.
- **License:** MIT (not re-verified).
- **Limitations:** No security updates; do not adopt.
- **Related resources:** uv (successor), pyenv, Poetry.
- **Sources:** https://github.com/khlaifiabilel/rye (README deprecation note, primary)
- **Verification date:** 2026-10-10
- **Confidence:** Verified (primary deprecation notice)

### 2.2 Registries, CDNs, and module delivery

### npm registry (npmjs.com)
- **Canonical identity:** npm, Inc. registry — registry.npmjs.org
- **Category:** Build tooling › Registries
- **Type:** Package registry (default for JS)
- **Official URL:** https://www.npmjs.com ; API: https://registry.npmjs.org
- **Description:** The canonical JS package registry (millions of packages). All JS package managers resolve against it (or mirrors). Supports provenance attestations, trusted publishing (OIDC), deprecation, two-factor auth. Supply-chain incidents (e.g., March 2026 axios maintainer-account hijack publishing a backdoor within 40 minutes, no CVE at the time) drive 2026 hardening: install-script blocking, minimumReleaseAge/cooldown policies.
- **Contents inspected:** Search excerpts: supply-chain analyses (axios hijack, npm audit limits); provenance/Sigstore notes; GitHub Packages npm-protocol alternative.
- **Actual capabilities:** Publish/install with semver; access tokens/OIDC; audit advisories feed; download stats API.
- **Usage domain:** All JS distribution.
- **Integration method:** Registry API; `npm publish --provenance`; `.npmrc` scoping.
- **Dependencies:** Not applicable.
- **Availability:** Hosted (free public; paid private scopes); SLA none on free tier.
- **Maintenance:** Active (GitHub).
- **License:** Not applicable (service).
- **Limitations:** "Blind trust" legacy model being retrofitted (trusted publishing newer than JSR's built-in provenance); no SLA on free tier.
- **Related resources:** JSR, GitHub Packages, esm.sh, Socket.dev.
- **Sources:** https://github.com/g-baskin/the-god-skill/blob/HEAD/skills/dependency-audit-weapon/SKILL.md ; https://www.infoworld.com/article/4124615/beyond-npm-what-you-need-to-know-about-jsr.html
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### JSR (JavaScript Registry)
- **Canonical identity:** jsr.io (Deno)
- **Category:** Build tooling › Registries
- **Type:** TypeScript-native package registry
- **Official URL:** https://jsr.io
- **Description:** Deno's TS-first registry: publish TypeScript source directly (no build step); "slow types" constraint (explicit export types) enables instant docs/type generation; ESM-only; cross-runtime (Deno, Node, Bun, browsers via publishing to npm compat layer); Sigstore transparency log + GitHub Actions OIDC provenance built in from day one. Hosts Deno's `@std` standard library. Usable from npm/yarn/pnpm via compat layer. Open governance board (Evan You, Ryan Dahl involved); nonprofit-foundation direction discussed.
- **Contents inspected:** Search excerpts: InfoWorld deep dive (slow-types tradeoff, Sigstore provenance, npm/yarn/pnpm compat); Deno 2 docs (JSR as first-party registry); esm.sh `/jsr/` path support.
- **Actual capabilities:** `deno publish`; `jsr:` specifiers; npm-compat tarballs; provenance verification.
- **Usage domain:** New TS libraries; Deno ecosystem; security-sensitive consumers.
- **Integration method:** `deno add jsr:@scope/pkg`; npm compat via `npm i jsr:@scope/pkg` (compat layer).
- **Dependencies:** None.
- **Availability:** Hosted; open governance.
- **Maintenance:** Active.
- **License:** Not applicable (service; registry code open).
- **Limitations:** Smaller catalog than npm; ESM-only excludes CJS packages; "slow types" is a real authoring constraint.
- **Related resources:** npm registry, Deno, esm.sh, Socket.dev.
- **Sources:** https://www.infoworld.com/article/4124615/beyond-npm-what-you-need-to-know-about-jsr.html ; https://github.com/esm-dev/esm.sh/pkgs/container/esm.sh ; https://www.pkgpulse.com/guides/bun-2-vs-nodejs-24-vs-deno-3-2026
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### esm.sh
- **Canonical identity:** esm-dev/esm.sh
- **Category:** Build tooling › Registries/CDN
- **Type:** No-build ESM CDN (npm/JSR/GitHub → browser-native ES modules)
- **Official URL:** https://esm.sh ; repo: github.com/esm-dev/esm.sh
- **Description:** Import npm/JSR/GitHub packages as ES modules via URL with zero build step: `import React from "https://esm.sh/react@19.2.4"`; CJS→ESM transform, deep subpath exports, `?dev`/`?bundle` modes, TypeScript type headers (`X-TypeScript-Types`), import-map friendly. Registries: `/` npm, `/jsr/`, `/gh/`, `/pr/` (pkg.pr.new). Best "browser-native ESM resolver" in 2026 CDN comparisons; SRI impractical (transform output can change).
- **Contents inspected:** Search excerpts: GitHub container package page (usage, registries, import maps); blazingcdn comparison (ESM default, type hints, immutable caching on pinned build IDs).
- **Actual capabilities:** On-the-fly bundling/transpilation; version resolution; build pinning via build IDs.
- **Usage domain:** Prototyping, import-map apps, Deno/browsers, docs demos.
- **Integration method:** URL imports; import maps; `?deps` pinning.
- **Dependencies:** Upstream registries.
- **Availability:** Hosted (no SLA); self-hostable.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** No contractual SLA; transform output drift complicates SRI; single-provider edge cache.
- **Related resources:** jsDelivr (+esm), unpkg, skypack (historical), JSPM.
- **Sources:** https://github.com/esm-dev/esm.sh/pkgs/container/esm.sh ; https://blog.blazingcdn.com/en-us/choose-best-js-cdn-compare-npm-alternatives-skypack-jsdelivr-unpkg
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### jsDelivr
- **Canonical identity:** jsdelivr/jsdelivr (Prospect One)
- **Category:** Build tooling › Registries/CDN
- **Type:** Public CDN for npm (+ GitHub, WordPress)
- **Official URL:** https://www.jsdelivr.com ; API: https://data.jsdelivr.com
- **Description:** Multi-CDN (DNS steering + health checks) serving npm packages, GitHub tags, WP plugins; `+esm` on-demand ESM; version resolution API (`data.jsdelivr.com/v1/packages/npm/<name>/resolved`); immutable 1-year caching on pinned versions; published SRI hashes; Brotli + optional minify. 2026 benchmark: P50 18ms / P95 55ms global TTFB; 99.99% trailing availability — best general-purpose JS CDN in 2026 comparisons.
- **Contents inspected:** Search excerpts: blazingcdn CDN benchmark (methodology + numbers); importmap-plus packager (jsDelivr data API usage).
- **Actual capabilities:** File serving with version ranges; ESM conversion; API for resolution/stats.
- **Usage domain:** Production `<script>` delivery, libraries' CDN builds.
- **Integration method:** URLs; `+esm` suffix; data API.
- **Dependencies:** Upstream npm/GitHub.
- **Availability:** Free; no contractual SLA.
- **Maintenance:** Active.
- **License:** Not applicable (service).
- **Limitations:** No SLA; abuse/rate policies; ESM conversion less complete than esm.sh.
- **Related resources:** unpkg, cdnjs, esm.sh.
- **Sources:** https://blog.blazingcdn.com/en-us/jsdelivr-vs-unpkg-vs-cdnjs-best-free-cdn-for-open-source-projects ; https://github.com/zoolutions/importmap-plus/blob/HEAD/lode/packager/summary.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (benchmark is vendor-adjacent — treat numbers as reported)

### unpkg
- **Canonical identity:** mjackson/unpkg
- **Category:** Build tooling › Registries/CDN
- **Type:** npm CDN (convenience layer)
- **Official URL:** https://unpkg.com ; repo: github.com/mjackson/unpkg
- **Description:** Serves any npm package file via URL (`unpkg.com/pkg@version/file`). Single-provider fronting a small origin; cold paths can hit the live npm registry (P95 140ms in 2026 benchmark — worst tail of the three). Immutable 1-year caching on pinned versions; no published SRI hashes (compute yourself). 2026 verdict: convenience for READMEs/CodePen, not for production critical paths.
- **Contents inspected:** Search excerpts: blazingcdn comparison table + benchmark.
- **Actual capabilities:** Direct file serving; `?meta` JSON directory listings.
- **Usage domain:** Demos, docs, quick prototyping.
- **Integration method:** URLs.
- **Dependencies:** npm registry.
- **Availability:** Free; 99.87% trailing availability (2026 benchmark — vendor-adjacent).
- **Maintenance:** Active (low cadence).
- **License:** MIT (not re-verified).
- **Limitations:** Tail latency; no SLA; no SRI publishing.
- **Related resources:** jsDelivr, esm.sh, cdnjs.
- **Sources:** https://blog.blazingcdn.com/en-us/choose-best-js-cdn-compare-npm-alternatives-skypack-jsdelivr-unpkg ; https://blog.blazingcdn.com/en-us/jsdelivr-vs-unpkg-vs-cdnjs-best-free-cdn-for-open-source-projects
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### cdnjs
- **Canonical identity:** cdnjs/cdnjs (Cloudflare)
- **Category:** Build tooling › Registries/CDN
- **Type:** Curated public CDN (~4k libraries allowlist)
- **Official URL:** https://cdnjs.com ; repo: github.com/cdnjs/cdnjs
- **Description:** Cloudflare-hosted CDN with human-curated allowlist (~4,000 libraries); publishes SRI hashes per asset; pre-minified Brotli assets; 1-year immutable caching; static object-store origin. Safest choice when you need a handful of famous libraries with verifiable hashes; cannot serve arbitrary npm packages (requires submission PR).
- **Contents inspected:** Search excerpts: blazingcdn comparison (curated allowlist, SRI published, P95 68ms); sh1pt commit (cdnjs = only CDN requiring explicit submission PR).
- **Actual capabilities:** Versioned library files with SRI; API.
- **Usage domain:** Production script tags for popular libs.
- **Integration method:** URLs; SRI attributes.
- **Dependencies:** Curation queue.
- **Availability:** Free (Cloudflare); no SLA.
- **Maintenance:** Active.
- **License:** Not applicable (service).
- **Limitations:** Allowlist only; update lag for new releases.
- **Related resources:** jsDelivr, unpkg.
- **Sources:** https://blog.blazingcdn.com/en-us/choose-best-js-cdn-compare-npm-alternatives-skypack-jsdelivr-unpkg ; https://github.com/profullstack/sh1pt/commit/81c1e659f11112e4512dc4f4699ddfac1eb5ade1
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### 2.3 Bundlers

### Vite
- **Canonical identity:** vitejs/vite — v8.x (8.0 Mar 2026; 8.3.x Sept 2026)
- **Category:** Build tooling › Bundlers
- **Type:** Frontend build tool (dev server + production bundler) + plugin ecosystem
- **Official URL:** https://vite.dev ; repo: github.com/vitejs/vite ; plugin registry: https://registry.vite.dev
- **Description:** The default frontend build tool in 2026 (~65M weekly downloads per Vite 8 announcement; ~132M in one third-party table — treat exact numbers as reported). Vite 8 is the biggest architectural change since Vite 2: esbuild+Rollup replaced by a single unified Rust bundler, Rolldown, with full Rollup plugin compatibility; Oxc replaces esbuild for transforms (`transformWithOxc`); Lightning CSS replaces esbuild for CSS minification; Environment API (from v7); `build.rolldownOptions`, `advancedChunks` code-splitting; dropped `system`/`amd` outputs; baseline Chrome 111/FF 114/Safari 16.4. Features: native-ESM dev server + HMR, `import.meta.glob`, asset queries, library mode, SSR (`ssrLoadModule`), `vite preview`.
- **Contents inspected:** Primary: vitejs/vite announcing-vite8.md (via search excerpt — full release notes). Secondary: migration notes (rollupOptions→rolldownOptions), skill docs (v8.3.1, Oxc transformer), bundle benchmarks (mid-size app 94s→11s in one report).
- **Actual capabilities:** Dev server with instant HMR; optimized production builds; plugin API (Rollup-compatible); SSR primitives; library builds.
- **Usage domain:** React/Vue/Svelte/Solid/Astro SPAs and libraries.
- **Integration method:** `npm create vite@latest`; `vite.config.ts`; `vite build/serve/preview` JS API.
- **Dependencies:** Rolldown, Oxc, Lightning CSS (bundled as deps).
- **Availability:** npm `vite`; MIT.
- **Maintenance:** Very active (VoidZero team; Evan You).
- **License:** MIT.
- **Limitations:** Rolldown migration edge cases (plugins touching Rollup internals; chunk-boundary/output-shape changes); dev/prod parity improved but not absolute.
- **Related resources:** Rolldown, Vitest, registry.vite.dev, @vitejs/plugin-react/vue, Vite+ (vite-plus).
- **Sources:** https://github.com/vitejs/vite/blob/HEAD/docs/blog/announcing-vite8.md ; https://github.com/yonatangross/orchestkit/blob/HEAD/src/skills/vite-advanced/SKILL.md ; https://dev.to/rudratosh/rust-quietly-ate-my-javascript-toolchain-in-2026-and-my-builds-are-20x-faster-for-it-pn0
- **Verification date:** 2026-10-10
- **Confidence:** Verified (primary release announcement)

### Rolldown
- **Canonical identity:** rolldown/rolldown — v1.x (1.0 RC Jan 2026; 1.2.9 Sept 2026)
- **Category:** Build tooling › Bundlers
- **Type:** JavaScript/TypeScript bundler (Rust, Rollup-compatible API)
- **Official URL:** https://rolldown.rs ; repo: https://github.com/rolldown/rolldown
- **Description:** VoidZero's Rust bundler: Rollup-compatible plugin interface with esbuild-like scope; intended as the future bundler of Vite (achieved in Vite 8). Uses Oxc for parsing/transform/minify; napi-rs Node bindings; ships per-platform npm binaries (+ wasm32-wasi). 13,968 stars, MIT. Benchmarks: 8–30× faster than Rollup on production builds (variance by project).
- **Contents inspected:** Primary: GitHub repo page + README via browser.open (tagline, VoidZero ownership, Rollup/esbuild credits, oxc/napi-rs dependencies, MIT license, star count).
- **Actual capabilities:** App + library bundling; code splitting (`advancedChunks`/`output.codeSplitting.groups`); tree-shaking; HMR-capable dev usage via Vite.
- **Usage domain:** Vite 8 builds; standalone library/app bundling; tsdown's engine.
- **Integration method:** npm `rolldown`; JS API mirroring Rollup; Vite consumes it internally.
- **Dependencies:** Oxc, napi-rs (build-time).
- **Availability:** npm; MIT.
- **Maintenance:** Very active (VoidZero).
- **License:** MIT (verified via repo page).
- **Limitations:** Young (1.x); Rollup-internals-dependent plugins may break; output shape differences vs Rollup.
- **Related resources:** Vite, Rollup, Oxc, tsdown, esbuild.
- **Sources:** https://github.com/rolldown/rolldown (primary, opened 2026-10-10) ; https://github.com/vitejs/vite/blob/HEAD/docs/blog/announcing-vite8.md
- **Verification date:** 2026-10-10
- **Confidence:** Verified

### webpack (+ webpack-dev-server)
- **Canonical identity:** webpack/webpack — v5.x (5.97+); webpack-dev-server v5.x
- **Category:** Build tooling › Bundlers
- **Type:** Module bundler (JS) + dev server
- **Official URL:** https://webpack.js.org ; repo: github.com/webpack/webpack
- **Description:** The decade-dominant bundler (loaders + plugins, code splitting, federation). In 2026: mature/maintenance posture; 41M weekly downloads (still huge installed base); even webpack 5.97-era docs point migrators at Rspack. webpack-dev-server provides HMR dev serving. No webpack 6 announced in sources surveyed.
- **Contents inspected:** Search excerpts: bundler comparisons (41.2M weekly downloads, MIT); "pure webpack era is over" analyses; Rspack-as-migration-path guidance.
- **Actual capabilities:** Full app bundling, loaders for any asset, Module Federation, persistent caching.
- **Usage domain:** Legacy/enterprise apps; Module Federation micro-frontends.
- **Integration method:** `webpack.config.js`; `webpack serve`; framework CLIs (Next.js escape hatch, Angular).
- **Dependencies:** Node.js; tapable/acorn ecosystem.
- **Availability:** npm; MIT.
- **Maintenance:** Maintenance (OpenJS; low feature velocity).
- **License:** MIT.
- **Limitations:** Slow vs Rust bundlers; config complexity; ecosystem migrating.
- **Related resources:** Rspack, Turbopack, Vite, Module Federation, rspack-dev-server.
- **Sources:** https://devtoollab.com/blog/webpack-alternatives ; https://dev.to/thedailyagent/javascript-bundlers-in-2026-vite-rspack-turbopack-and-the-end-of-an-era-16hk
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Rspack
- **Canonical identity:** web-infra-dev/rspack — v2.0 (2026)
- **Category:** Build tooling › Bundlers
- **Type:** Rust bundler with webpack API/config compatibility
- **Official URL:** https://rspack.rs (canonical per ecosystem); repo: github.com/web-infra-dev/rspack
- **Description:** ByteDance/WebInfra's Rust bundler prioritizing webpack compatibility (~95% config reuse claimed) over raw speed: the lowest-friction upgrade for legacy webpack codebases; webpack loaders/plugins largely work. ~6M weekly downloads. Rsbuild is its Vite-like wrapper (out of scope detail).
- **Contents inspected:** Search excerpts: comparisons (Rust, webpack-compatible, 6,017,306 weekly downloads, MIT); migration guidance ("config is older than the team → Rspack").
- **Actual capabilities:** Drop-in-ish webpack replacement; fast Rust core; HMR; Module Federation support.
- **Usage domain:** Enterprise webpack migrations.
- **Integration method:** Point at existing webpack config; `rspack.config.js`.
- **Dependencies:** Rust core via napi bindings.
- **Availability:** npm `@rspack/core`; MIT.
- **Maintenance:** Active (ByteDance).
- **License:** MIT.
- **Limitations:** Not 100% webpack-identical (custom loaders touching internals need work); smaller plugin ecosystem than webpack proper.
- **Related resources:** webpack, Rsbuild, Turbopack, Rolldown.
- **Sources:** https://devtoollab.com/blog/webpack-alternatives ; https://dev.to/thedailyagent/javascript-bundlers-in-2026-vite-rspack-turbopack-and-the-end-of-an-era-16hk ; https://acetrum.com/blog/rolldown-vs-turbopack-vs-rspack-plugin-migration
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Turbopack
- **Canonical identity:** vercel/turbo (monorepo) — Turbopack ships inside Next.js 16.x
- **Category:** Build tooling › Bundlers
- **Type:** Incremental Rust bundler (Next.js-only distribution)
- **Official URL:** https://nextjs.org/docs/app/api-reference/turbopack ; repo: github.com/vercel/turbo (crates)
- **Description:** Vercel's Rust bundler, default in Next.js 16 (Oct 2025): incremental architecture caching to function level with persistent disk cache; 5–10× faster Fast Refresh, 2–5× faster builds (vendor claims). Cannot be adopted standalone — no Vue/Svelte/standalone usage; Next.js docs retain a "Using Webpack instead" escape hatch. Shipped as part of Next.js (MIT).
- **Contents inspected:** Search excerpts: devtoollab ("only bundler you cannot adopt on its own"); Next 16.3.5 sidebar docs; Turbopack-vs-esbuild/Rspack tables.
- **Actual capabilities:** Next.js dev + build; incremental HMR; persistent cache.
- **Usage domain:** Next.js applications exclusively.
- **Integration method:** `next dev --turbopack` (default in 16); `next.config.js` turbo options.
- **Dependencies:** Next.js.
- **Availability:** Bundled with Next.js; MIT.
- **Maintenance:** Active (Vercel).
- **License:** MIT.
- **Limitations:** Next.js-only; limited customization surface; memory tuning sometimes needed.
- **Related resources:** Next.js, webpack, Rspack, Rolldown.
- **Sources:** https://devtoollab.com/blog/webpack-alternatives ; https://dev.to/pockit_tools/turbopack-in-2026-the-complete-guide-to-nextjss-rust-powered-bundler-oda
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Rollup
- **Canonical identity:** rollup/rollup — v4.x/v5.x line
- **Category:** Build tooling › Bundlers
- **Type:** ES module bundler (JS; native Rust port in progress as rollup@5/swc-line — see note)
- **Official URL:** https://rollupjs.org ; repo: github.com/rollup/rollup
- **Description:** The ESM-focused library bundler whose plugin API became the ecosystem standard (Vite, tsdown, unbuild all speak it). In 2026, production-bundling mindshare moved to Rolldown (its API-compatible Rust successor); Rollup itself continues for compatibility. Note: Rollup 5 development explored native bindings; exact 2026 version not pinned in sources — record conservatively.
- **Contents inspected:** Search excerpts: Rolldown README credits ("heavily inspired by Rollup, created by Rich Harris, maintained by Lukas Taegert-Atkinson"); Vite 7→8 migration (Rollup→Rolldown).
- **Actual capabilities:** Library bundling, tree-shaking, rich plugin API.
- **Usage domain:** Libraries; Vite ≤7 production builds.
- **Integration method:** `rollup.config.js`; JS API; Vite pre-8.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active but slower (maintainer-limited); ecosystem moving to Rolldown.
- **License:** MIT.
- **Limitations:** JS-speed ceiling (the reason for Rolldown); large-project build times.
- **Related resources:** Rolldown, Vite, esbuild, tsup (historical).
- **Sources:** https://github.com/rolldown/rolldown (credits section, primary) ; https://github.com/vitejs/vite/blob/HEAD/docs/blog/announcing-vite8.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### esbuild
- **Canonical identity:** evanw/esbuild — v0.x (0.2x line)
- **Category:** Build tooling › Bundlers / Transpilers
- **Type:** Extremely fast JS/TS/CSS bundler + transformer (Go)
- **Official URL:** https://esbuild.github.io ; repo: github.com/evanw/esbuild
- **Description:** Evan Wallace's Go bundler: still the fastest TS→JS transform and ubiquitous as a library inside other tools (tsx, tsup historically, test runners, CLIs, Lambda packaging). 201M weekly downloads. "Didn't lose — moved": no longer the app assembler of choice (Vite 8 dropped it), but the transform layer everywhere. Deliberately narrow plugin API (no full AST) is the source of its speed.
- **Contents inspected:** Search excerpts: acetrum ("still the fastest way to turn TypeScript into JavaScript... plugin API deliberately narrow"); tsx architecture (esbuild-based); 201.7M weekly downloads figure.
- **Actual capabilities:** Bundle/transform/minify JS/TS/JSX/CSS; `esbuild serve` (basic).
- **Usage domain:** Library/CLI builds, transpile steps, dev transforms.
- **Integration method:** `esbuild` CLI; JS/Go API.
- **Dependencies:** Go binary (self-contained).
- **Availability:** npm; MIT.
- **Maintenance:** Active (Evan Wallace; steady, not rapid).
- **License:** MIT.
- **Limitations:** No type checking; limited plugin power (by design); CSS handling weaker than Lightning CSS.
- **Related resources:** Oxc, SWC, tsx, tsup, Vite (historical).
- **Sources:** https://acetrum.com/blog/rolldown-vs-turbopack-vs-rspack-plugin-migration ; https://devtoollab.com/blog/webpack-alternatives
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Parcel
- **Canonical identity:** parcel-bundler/parcel — v2.x
- **Category:** Build tooling › Bundlers
- **Type:** Zero-config web application bundler (Rust core + JS)
- **Official URL:** https://parceljs.org ; repo: github.com/parcel-bundler/parcel
- **Description:** Zero-config bundler (HTML entry, auto transforms); v2 rewrote core in Rust. Niche in 2026 vs Vite/Next dominance but maintained; valued for no-config setups.
- **Contents inspected:** Not deeply searched; included for systematic coverage.
- **Actual capabilities:** App bundling from HTML; HMR; code splitting; built-in transforms.
- **Usage domain:** Simple apps, prototypes, no-config builds.
- **Integration method:** `parcel index.html`; zero config.
- **Dependencies:** Rust core napi + JS plugins.
- **Availability:** npm; MIT.
- **Maintenance:** Active (lower velocity).
- **License:** MIT (not re-verified).
- **Limitations:** Smaller ecosystem; plugin authoring less documented than Vite/Rollup.
- **Related resources:** Vite, Farm, WMR (archived).
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified (2026 state not checked)

### Farm
- **Canonical identity:** farm-fe/farm
- **Category:** Build tooling › Bundlers
- **Type:** Rust-based web build tool (Vite-compatible plugin API)
- **Official URL:** https://farmfe.org ; repo: github.com/farm-fe/farm
- **Description:** Rust bundler claiming Vite plugin compatibility with faster cold starts via lazy compilation. Community-driven; smaller adoption than Rspack/Rolldown.
- **Contents inspected:** Not deeply searched; included for systematic coverage.
- **Actual capabilities:** Dev server + build; partial Vite plugin compat.
- **Usage domain:** Teams wanting Rust speed with Vite-like config.
- **Integration method:** `farm.config.ts`.
- **Dependencies:** Rust core.
- **Availability:** npm; MIT.
- **Maintenance:** Active-ish (community).
- **License:** MIT (not re-verified).
- **Limitations:** Compatibility gaps; small ecosystem.
- **Related resources:** Vite, Rspack, Rolldown.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### tsdown
- **Canonical identity:** rolldown/tsdown (community; Rolldown org)
- **Category:** Build tooling › Bundlers › Library bundlers
- **Type:** TypeScript library bundler (Rolldown + Oxc powered; tsup successor)
- **Official URL:** https://tsdown.dev (canonical per docs); repo: github.com/rolldown/tsdown
- **Description:** "The elegant bundler for libraries powered by Rolldown": drop-in tsup replacement with compatible options; ESM/CJS/IIFE outputs, `.d.ts` via Oxc isolated-declarations, unbundle mode, watch mode, CSS pipeline (Lightning CSS/PostCSS/CSS modules), WASM support, shims, publint+attw package validation built in (`publint: 'ci-only'`), executable bundling (experimental `@tsdown/exe`), framework recipes (React/Vue/Solid/Svelte). The 2026 default for new TS libraries.
- **Contents inspected:** Search excerpts: three independent SKILL.md references (config, features, patterns, publint/attw integration, CSS/WASM recipes); Medium review (Rolldown-powered, tsup migration).
- **Actual capabilities:** Zero-config-ish library builds; dual-format + types; validation gates.
- **Usage domain:** npm library authors.
- **Integration method:** `tsdown.config.ts`; `tsdown` CLI.
- **Dependencies:** Rolldown, Oxc.
- **Availability:** npm `tsdown`; MIT.
- **Maintenance:** Active.
- **License:** MIT (per SKILL metadata — not re-verified against repo).
- **Limitations:** Young; advanced Rollup-plugin edge cases may differ.
- **Related resources:** tsup, unbuild, Rolldown, publint, attw.
- **Sources:** https://github.com/onmax/nuxt-skills/blob/HEAD/skills/tsdown/SKILL.md ; https://github.com/h3y6e/agent-skills/blob/HEAD/.vendor/skills/tsdown/SKILL.md ; https://medium.com/@ramunarasinga/tsdown-the-elegant-bundler-for-libraries-powered-by-rolldown-bddee176882d
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### tsup (maintenance mode — use tsdown)
- **Canonical identity:** egoist/tsup
- **Category:** Build tooling › Bundlers › Library bundlers
- **Type:** TypeScript library bundler (esbuild-powered) — NOT ACTIVELY MAINTAINED
- **Official URL:** https://github.com/egoist/tsup
- **Description:** "Bundle your TypeScript library with no config, powered by esbuild" (MIT © EGOIST). The README now carries an explicit warning: "This project is not actively maintained anymore. Please consider using tsdown instead" (+ migration guide). Still widely present in older repos.
- **Contents inspected:** Primary README via yarnpkg mirror page (warning banner verbatim; feature list; install/usage).
- **Actual capabilities:** (Historical) zero-config TS lib bundling, DTS, watch, shims.
- **Usage domain:** Legacy library builds — migrate.
- **Integration method:** `tsup` CLI (existing setups).
- **Dependencies:** esbuild.
- **Availability:** npm (existing versions).
- **Maintenance:** None — unmaintained (maintainer statement).
- **License:** MIT.
- **Limitations:** No new features/fixes; use tsdown.
- **Related resources:** tsdown (successor), unbuild, esbuild.
- **Sources:** https://classic.yarnpkg.com/en/package/tsup (README mirror, primary text)
- **Verification date:** 2026-10-10
- **Confidence:** Verified (maintainer's own deprecation banner)

### unbuild
- **Canonical identity:** unjs/unbuild
- **Category:** Build tooling › Bundlers › Library bundlers
- **Type:** Library build tool (Rollup-based, auto config)
- **Official URL:** https://github.com/unjs/unbuild
- **Description:** UnJS's "zero-config" library builder: auto-detects entries/exports, Rollup under the hood, DTS rollup. Recommended in 2026 skill docs "for complex cases" where tsdown's conventions don't fit. Used across the UnJS/Nuxt ecosystem.
- **Contents inspected:** Search excerpts (nuxt-skills ts-library guide: "tsdown for most builds, unbuild for complex cases").
- **Actual capabilities:** Auto entry detection; CJS/ESM + DTS; stub mode for dev (jiti).
- **Usage domain:** UnJS-ecosystem libraries; complex multi-entry packages.
- **Integration method:** `unbuild` CLI; `build.config.ts`.
- **Dependencies:** Rollup, rollup plugins, mkdist.
- **Availability:** npm; MIT.
- **Maintenance:** Active (UnJS).
- **License:** MIT (not re-verified).
- **Limitations:** Rollup-speed (slower than tsdown); magic conventions can surprise.
- **Related resources:** tsdown, mkdist, jiti, Rollup.
- **Sources:** https://github.com/onmax/nuxt-skills/blob/HEAD/skills/ts-library/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (thin sourcing)

### pkgroll
- **Canonical identity:** privatenumber/pkgroll
- **Category:** Build tooling › Bundlers › Library bundlers
- **Type:** Minimalist package bundler (distributes via package.json `exports`)
- **Official URL:** https://github.com/privatenumber/pkgroll
- **Description:** Builds packages straight from `package.json` exports map (no config file): ESM/CJS/DTS, targeting privatenumber's minimal-tooling philosophy. Niche but respected for tiny libs.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Exports-driven bundling; types; minification optional.
- **Usage domain:** Small utility libraries.
- **Integration method:** `pkgroll` CLI reads package.json.
- **Dependencies:** Rollup/esbuild internals (not verified).
- **Availability:** npm; MIT.
- **Maintenance:** Active-ish (privatenumber).
- **License:** MIT (not re-verified).
- **Limitations:** Opinionated; not for complex builds.
- **Related resources:** tsdown, unbuild, tsup.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### dnt (Deno to Node Transform)
- **Canonical identity:** denoland/dnt
- **Category:** Build tooling › Bundlers › Cross-runtime publishers
- **Type:** Deno→npm package build tool
- **Official URL:** https://github.com/denoland/dnt
- **Description:** Builds npm-compatible packages from Deno-first TypeScript sources: transforms Deno specifiers, generates package.json, shims. The bridge for publishing Deno-authored libs to npm.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Deno module → npm tarball with CJS/ESM shims.
- **Usage domain:** Deno-first library authors publishing to npm.
- **Integration method:** `dnt.build()` in a build script.
- **Dependencies:** Deno.
- **Availability:** Open source (MIT).
- **Maintenance:** Active (Deno).
- **License:** MIT (not re-verified).
- **Limitations:** Mapping edge cases (Node builtins, npm deps) need config.
- **Related resources:** JSR (alternative: publish TS directly), tsdown.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### 2.4 Transpilers, transforms, and CSS tooling

### Babel
- **Canonical identity:** babel/babel — v7.x line (7.2x)
- **Category:** Build tooling › Transpilers
- **Type:** JavaScript compiler/transform pipeline (plugins + presets)
- **Official URL:** https://babeljs.io ; repo: github.com/babel/babel
- **Description:** The original pluggable JS transform toolchain (2014–): parses with `@babel/parser`, transforms via plugins/presets (`@babel/preset-env`, `-typescript`, `-react`), generates code. In 2026 still the compat fallback (Babel 7 docs referenced in Vite 8 migration for transform plugins that don't support Oxc); preset-env + browserslist remains the legacy-targeting answer. Notable cost: startup/transform speed vs native tools.
- **Contents inspected:** Search excerpts: Vite 8 migration (Babel fallback path); TypeScript-7.1 compat notes (Babel transform support for TS 7.1 via `@babel/plugin-transform-typescript`); dev.to comparisons (Babel slower than SWC/Oxc).
- **Actual capabilities:** Syntax transforms, polyfill injection (core-js via preset-env), code generation, parser-as-a-service for codemods.
- **Usage domain:** Legacy-browser targeting, codemods, projects with custom AST plugins.
- **Integration method:** `.babelrc`/`babel.config.js`; bundler plugins.
- **Dependencies:** Node.js; plugin packages.
- **Availability:** npm; MIT.
- **Maintenance:** Active (maintenance cadence; Babel 8 long-discussed, not shipped per sources).
- **License:** MIT.
- **Limitations:** Slow relative to native; plugin maintenance burden.
- **Related resources:** SWC, Oxc, esbuild, TypeScript, core-js.
- **Sources:** https://github.com/vitejs/vite/blob/HEAD/docs/blog/announcing-vite8.md ; https://github.com/davidpvilalta/dev-environment-files/blob/HEAD/dot_config/claude/skills/typescript-expert/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### SWC
- **Canonical identity:** swc-project/swc (Speedy Web Compiler) — Rust
- **Category:** Build tooling › Transpilers
- **Type:** JS/TS compiler platform (Rust): transform, minify, bundle, plugins (WASM)
- **Official URL:** https://swc.rs ; repo: github.com/swc-project/swc
- **Description:** Rust-based compiler used in production at scale (Next.js Turbopack-era transforms, Deno historically, many CLIs). 2026 status: "production-proven default"; Deno is migrating transform workloads to Oxc; still the plugin-capable choice (WASM plugins) where Oxc's API is narrower. Also offers minification and (historical) bundling.
- **Contents inspected:** Search excerpts: Deno→Oxc migration notes; "production-proven" framing; comparisons noting WASM plugin support.
- **Actual capabilities:** Parse/transform/minify JS/TS/JSX; `.swcrc`; WASM plugin system.
- **Usage domain:** Framework internals, high-throughput transform services.
- **Integration method:** `@swc/core` napi bindings; loaders.
- **Dependencies:** Rust core via napi.
- **Availability:** npm; Apache-2.0.
- **Maintenance:** Active (Vercel-linked; kdy1).
- **License:** Apache-2.0.
- **Limitations:** API complexity; docs thinner than Babel's; Oxc competition.
- **Related resources:** Oxc, esbuild, Babel, Turbopack.
- **Sources:** https://dev.to/rudratosh/rust-quietly-ate-my-javascript-toolchain-in-2026-and-my-builds-are-20x-faster-for-it-pn0 ; https://github.com/yun-kun/telescope/blob/HEAD/.claude/skills/deno/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Sucrase
- **Canonical identity:** alangpierce/sucrase
- **Category:** Build tooling › Transpilers
- **Type:** Fast JS/TS/JSX dev transform (JS, single-pass)
- **Official URL:** https://sucrase.io ; repo: github.com/alangpierce/sucrase
- **Description:** "Super-fast" single-pass transforms for dev (no type checking, scope-limited transforms). Historically used by Jest-adjacent tooling and older dev servers; largely superseded by esbuild/Oxc but still embedded in places.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** TS/JSX/Flow/legacy transforms; no bundling/minification.
- **Usage domain:** Dev-only transpile steps in older stacks.
- **Integration method:** JS API; jest/bundler plugins.
- **Dependencies:** None.
- **Availability:** npm; MIT.
- **Maintenance:** Low (stable/maintenance).
- **License:** MIT (not re-verified).
- **Limitations:** Dev-only semantics; incomplete transforms by design.
- **Related resources:** esbuild, SWC, tsx.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified (2026 state not checked)

### Lightning CSS
- **Canonical identity:** parcel-bundler/lightningcss (Rust)
- **Category:** Build tooling › Transpilers (CSS)
- **Type:** CSS parser/transformer/bundler/minifier (Rust)
- **Official URL:** https://lightningcss.dev ; repo: github.com/parcel-bundler/lightningcss
- **Description:** Rust CSS toolchain: parsing, nesting lowering, custom-media, logical properties, `color-mix`, modules scoping, minification — with proper browser-target handling (browserslist). Adopted as Vite 8's CSS minifier (replacing esbuild) and inside tsdown's CSS pipeline. The 2026 default for serious CSS builds.
- **Contents inspected:** Search excerpts: Vite 8 announcement (Lightning CSS replaces esbuild for minification); tsdown SKILL (CSS pipeline with Lightning CSS/PostCSS).
- **Actual capabilities:** Transform/lower/minify/bundle CSS; CSS modules; custom drafts.
- **Usage domain:** Build pipelines needing modern CSS features + targets.
- **Integration method:** JS API/napi; Vite/tsdown/PostCSS integrations.
- **Dependencies:** None (native binary).
- **Availability:** npm `lightningcss`; MPL-2.0.
- **Maintenance:** Active (Devon Govett/Parcel).
- **License:** MPL-2.0 (per public docs — not re-verified).
- **Limitations:** MPL copyleft on the library (weaker ecosystem adoption in some corps); PostCSS plugin interop via compat layer.
- **Related resources:** PostCSS, Tailwind CSS, Parcel.
- **Sources:** https://github.com/vitejs/vite/blob/HEAD/docs/blog/announcing-vite8.md ; https://github.com/h3y6e/agent-skills/blob/HEAD/.vendor/skills/tsdown/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### PostCSS
- **Canonical identity:** postcss/postcss — v8.x
- **Category:** Build tooling › Transpilers (CSS)
- **Type:** CSS transformation framework (plugin pipeline)
- **Official URL:** https://postcss.org ; repo: github.com/postcss/postcss
- **Description:** The plugin API through which most CSS transforms run (autoprefixer, postcss-preset-env, cssnano historically, Tailwind v3). Vite still supports PostCSS config; Tailwind v4 replaced the PostCSS plugin with a native Vite plugin (PostCSS integration remains for non-Vite builds). Stable/mature in 2026.
- **Contents inspected:** Search excerpts: Tailwind v4 migration (PostCSS plugin vs Vite plugin); Vite docs (PostCSS config support).
- **Actual capabilities:** Parse→plugin chain→stringify; source maps.
- **Usage domain:** Autoprefixing, future-CSS transpilation, Tailwind v3 pipelines.
- **Integration method:** `postcss.config.js`; bundler plugins.
- **Dependencies:** Node.js; plugins.
- **Availability:** npm; MIT.
- **Maintenance:** Active (Andrey Sitnik; low churn).
- **License:** MIT.
- **Limitations:** JS-speed; plugin quality varies.
- **Related resources:** autoprefixer, Lightning CSS, Tailwind CSS.
- **Sources:** https://tailwindcss.com/docs ; https://vite.dev/guide/features.html
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Tailwind CSS
- **Canonical identity:** tailwindlabs/tailwindcss — v4.3.x (v4.0 Jan 2025)
- **Category:** Build tooling › CSS tooling (framework + compiler)
- **Type:** Utility-first CSS framework with Rust compiler (v4)
- **Official URL:** https://tailwindcss.com ; repo: github.com/tailwindlabs/tailwindcss
- **Description:** v4 rewrote the engine: CSS-first configuration (`@theme` in CSS replaces `tailwind.config.js`), Rust-powered compiler (~5× faster builds), native Vite plugin, automatic content detection, modern CSS features (cascade layers, `@property`, container queries). The dominant styling approach in 2026 greenfield work; v3 (PostCSS plugin) still in maintenance.
- **Contents inspected:** Search excerpts: v4 feature summaries; upgrade tool (`@tailwindcss/upgrade`); Vite plugin docs.
- **Actual capabilities:** Utility generation, theming via `@theme`, dark mode, typography/forms plugins.
- **Usage domain:** Utility-first styling in any framework.
- **Integration method:** `@tailwindcss/vite` plugin; PostCSS plugin; CLI.
- **Dependencies:** None heavy (native binary in v4).
- **Availability:** npm; MIT.
- **Maintenance:** Very active (Tailwind Labs).
- **License:** MIT.
- **Limitations:** v3→v4 migration (config → CSS); opinionated HTML.
- **Related resources:** Lightning CSS, PostCSS, UnoCSS, daisyUI.
- **Sources:** https://tailwindcss.com/docs ; https://github.com/tailwindlabs/tailwindcss
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Dart Sass
- **Canonical identity:** sass/dart-sass (canonical Sass implementation)
- **Category:** Build tooling › CSS tooling (preprocessor)
- **Type:** CSS preprocessor (Dart implementation; JS API via `sass` npm package)
- **Official URL:** https://sass-lang.com ; repo: github.com/sass/dart-sass
- **Description:** The canonical Sass/SCSS implementation after LibSass/node-sass deprecation: `@use`/`@forward` module system, built-in modules (`sass:color`, `sass:math`), compiled to JS for the `sass` npm package (plus Dart VM native). Still standard in design-system codebases and Angular (which bundles Sass).
- **Contents inspected:** Not deeply searched; included for systematic coverage.
- **Actual capabilities:** SCSS/Sass compilation; modules; source maps; `--watch`.
- **Usage domain:** SCSS codebases, design systems, Angular.
- **Integration method:** `sass` npm package; Vite `css.preprocessorOptions`.
- **Dependencies:** Dart runtime (or compiled JS).
- **Availability:** npm `sass`; MIT.
- **Maintenance:** Active (Sass team; slower cadence).
- **License:** MIT (not re-verified).
- **Limitations:** Separate language to learn; slower than native CSS pipelines for big trees.
- **Related resources:** Less (historical), Stylus (historical), Lightning CSS.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified (2026 state not checked)

### 2.5 Type checking and package validation

### typescript-eslint (tseslint)
- **Canonical identity:** typescript-eslint/typescript-eslint — v8.x
- **Category:** Build tooling › Type checking (lint-integrated)
- **Type:** TypeScript ESLint tooling (parser + plugin + configs)
- **Official URL:** https://typescript-eslint.io ; repo: github.com/typescript-eslint/typescript-eslint
- **Description:** The standard bridge making ESLint understand TS: typed linting via type-aware rules (`recommended-type-checked`), project service, `tseslint.config()` flat-config helper. v8 line current in 2026; pairs with ESLint 10.
- **Contents inspected:** Search excerpts: tseslint v8 migration notes; flat-config helper docs.
- **Actual capabilities:** Type-aware lint rules; `no-floating-promises`, `no-unsafe-*`, naming conventions.
- **Usage domain:** TS codebases using ESLint.
- **Integration method:** `tseslint.config()` in `eslint.config.mjs`; `parserOptions.projectService`.
- **Dependencies:** ESLint, TypeScript.
- **Availability:** npm; MIT.
- **Maintenance:** Very active.
- **License:** MIT (not re-verified).
- **Limitations:** Type-aware rules are slow on huge repos (needs project service tuning).
- **Related resources:** ESLint, TypeScript, Biome (alternative).
- **Sources:** https://typescript-eslint.io ; https://eslint.org
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### mypy + pyright (Python type checking)
- **Canonical identity:** python/mypy; microsoft/pyright (+ basedpyright fork)
- **Category:** Build tooling › Type checking (Python)
- **Type:** Static type checkers for Python
- **Official URL:** https://mypy-lang.org ; https://github.com/microsoft/pyright ; basedpyright: https://docs.basedpyright.com
- **Description:** The two dominant Python checkers: mypy (the reference implementation, plugin/daemon `dmypy`) and pyright (Microsoft's Node-based checker, faster, powers Pylance; community fork basedpyright). 2026: type-annotated Python is standard in typed codebases; `ty` (Astral's Rust checker, in preview) is the emerging third option — recorded here as emerging, not cataloged in depth.
- **Contents inspected:** Not directly searched this session; included for systematic coverage of the Python toolchain half of the mission.
- **Actual capabilities:** Static type errors, narrowing, generics/protocols checking; pyright also fast LSP.
- **Usage domain:** Typed Python codebases.
- **Integration method:** `mypy`/CLI; `pyrightconfig.json`; editor LSP.
- **Dependencies:** Python (mypy); Node.js (pyright).
- **Availability:** Open source; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Gradual typing gaps; plugin ecosystems differ.
- **Related resources:** ty (Astral, emerging), pyright LSP, pydantic (runtime).
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified (2026 state not checked)

### publint
- **Canonical identity:** privatenumber/publint
- **Category:** Build tooling › Package validation
- **Type:** npm package correctness linter
- **Official URL:** https://publint.dev ; repo: github.com/privatenumber/publint
- **Description:** Lints packed npm tarballs for publishing mistakes (missing files, broken exports, ESM/CJS mismatches). Built into tsdown (`publint: 'ci-only'`) as a release gate.
- **Contents inspected:** Search excerpts (tsdown SKILL: publint+attw integration).
- **Actual capabilities:** `publint` CLI; programmatic API; checks exports/resolution.
- **Usage domain:** Library release pipelines.
- **Integration method:** CI step; tsdown built-in.
- **Dependencies:** None heavy.
- **Availability:** npm; MIT.
- **Maintenance:** Active (privatenumber).
- **License:** MIT (not re-verified).
- **Limitations:** Heuristic; can't catch runtime bugs.
- **Related resources:** attw, tsdown, unbuild.
- **Sources:** https://github.com/h3y6e/agent-skills/blob/HEAD/.vendor/skills/tsdown/SKILL.md ; https://publint.dev
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### attw (Are The Types Wrong)
- **Canonical identity:** arethetypeswrong/arethetypeswrong
- **Category:** Build tooling › Package validation
- **Type:** TypeScript package types-resolution checker
- **Official URL:** https://arethetypeswrong.github.io ; repo: github.com/arethetypeswrong/arethetypeswrong
- **Description:** Analyzes a package's published types under multiple module-resolution modes (node10/node16/bundler) and reports resolution failures. Paired with publint in tsdown release gates.
- **Contents inspected:** Search excerpts (tsdown SKILL integration).
- **Actual capabilities:** `attw --pack`; resolution-mode matrix checks.
- **Usage domain:** Library release pipelines.
- **Integration method:** CI step; tsdown built-in.
- **Dependencies:** TypeScript.
- **Availability:** npm; MIT/Apache.
- **Maintenance:** Active (TS team-adjacent).
- **License:** Not verified.
- **Limitations:** Types-only; doesn't test runtime.
- **Related resources:** publint, tsdown, TypeScript.
- **Sources:** https://github.com/h3y6e/agent-skills/blob/HEAD/.vendor/skills/tsdown/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (thin sourcing)

### 2.6 Linting and formatting

### ESLint
- **Canonical identity:** eslint/eslint — v10.x (10.8 referenced; flat config default)
- **Category:** Build tooling › Lint/format
- **Type:** JavaScript/TypeScript linter (pluggable rules)
- **Official URL:** https://eslint.org ; repo: github.com/eslint/eslint
- **Description:** The long-standard JS linter; v9+ moved to flat config (`eslint.config.js`) and v10 continues it. The choice when the ecosystem's plugin universe is needed (framework plugins, `eslint-plugin-jsx-a11y`, import sorting, security rules). Slower than Rust linters; "ESLint's slowness is its biggest remaining tax" in 2026 analyses.
- **Contents inspected:** Search excerpts: v10/flat-config status; typescript-eslint v8 pairing; comparisons (oxlint/Biome speed claims).
- **Actual capabilities:** AST-rule linting; autofix; flat config; massive plugin ecosystem.
- **Usage domain:** Teams needing specific rules/plugins; legacy configs.
- **Integration method:** `eslint.config.js`; editor extensions; CI.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active (OpenJS).
- **License:** MIT.
- **Limitations:** Speed; flat-config migration cost for old repos.
- **Related resources:** typescript-eslint, Biome, oxlint, Prettier.
- **Sources:** https://eslint.org ; https://dev.to/rudratosh/rust-quietly-ate-my-javascript-toolchain-in-2026-and-my-builds-are-20x-faster-for-it-pn0
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Biome
- **Canonical identity:** biomejs/biome — v2.x (2.x line current)
- **Category:** Build tooling › Lint/format
- **Type:** All-in-one JS/TS linter + formatter (Rust)
- **Official URL:** https://biomejs.dev ; repo: github.com/biomejs/biome
- **Description:** Single binary replacing ESLint+Prettier for many teams: formatter (Prettier-compatible-ish), linter with 300+ rules, import organizer, `biome check`, `biome migrate`. 25,912 stars, MIT. v2 continues the "one tool" push. Trade-off: rule coverage narrower than ESLint's plugin universe; Prettier-parity edge cases remain.
- **Contents inspected:** Primary: repo page + README via browser.open (star count, one-toolchain claim, formatter/linter/organizer/migrate features, MIT, sponsors).
- **Actual capabilities:** Format + lint + organize imports + migrate from ESLint/Prettier; JSON/CSS/GraphQL support.
- **Usage domain:** Teams wanting one fast tool; monorepos standardizing format.
- **Integration method:** `biome.json`; `biome check --write`; editor extensions.
- **Dependencies:** None (single binary).
- **Availability:** npm `@biomejs/biome`; MIT.
- **Maintenance:** Active (Biome team; funded).
- **License:** MIT (verified via repo page).
- **Limitations:** Not every ESLint rule has an equivalent; some Prettier formatting differences.
- **Related resources:** ESLint, Prettier, oxlint/oxfmt, dprint.
- **Sources:** https://github.com/biomejs/biome (primary, opened 2026-10-10)
- **Verification date:** 2026-10-10
- **Confidence:** Verified

### oxlint + oxfmt (+ Vite+ unified CLI)
- **Canonical identity:** oxc-project/oxc — `oxlint` v1.x; `oxfmt` (new); `vite-plus` ("Vite+") unified CLI
- **Category:** Build tooling › Lint/format
- **Type:** Rust linter/formatter (part of Oxc toolchain)
- **Official URL:** https://oxc.rs ; repo: https://github.com/oxc-project/oxc
- **Description:** oxlint: ESLint-compatible Rust linter (1.x line; hundreds of rules, ESLint-plugin compat layer growing). oxfmt: new Rust formatter challenging Prettier/Biome. Vite+ (vite-plus): unified CLI combining Oxc's toolchain — the "one binary" answer from the Oxc/Vite side. Positioned as the speed-max choice; ecosystem rule parity still catching up.
- **Contents inspected:** Search excerpts: skill docs (oxlint 1.x, oxfmt, Vite+ CLI); comparisons (50–100× faster than ESLint claims — vendor-adjacent, treat as reported).
- **Actual capabilities:** Lint with ESLint-rule compat; format JS/TS/JSON/CSS (oxfmt scope growing); unified CLI.
- **Usage domain:** Speed-focused teams; Vite 8/Rolldown stacks.
- **Integration method:** `oxlint`, `oxfmt`, `vite-plus` binaries; `.oxlintrc.json`.
- **Dependencies:** None.
- **Availability:** npm; MIT.
- **Maintenance:** Very active (VoidZero).
- **License:** MIT.
- **Limitations:** Rule/plugin parity vs ESLint incomplete; formatter newer than Prettier/Biome.
- **Related resources:** Oxc, ESLint, Biome, Prettier, Vite.
- **Sources:** https://github.com/yonatangross/orchestkit/blob/HEAD/src/skills/vite-advanced/SKILL.md ; https://oxc.rs
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Prettier
- **Canonical identity:** prettier/prettier — v3.x
- **Category:** Build tooling › Lint/format
- **Type:** Opinionated code formatter (JS/TS/CSS/HTML/JSON/Markdown/YAML...)
- **Official URL:** https://prettier.io ; repo: github.com/prettier/prettier
- **Description:** The de-facto formatter: zero-config opinionated output, editor/CI integration, `.prettierrc`. Still the formatting baseline even where Biome/oxfmt compete; pairs with ESLint (format) or typescript-eslint. v3 line current.
- **Contents inspected:** Search excerpts: formatter comparisons; Biome migration notes (Prettier-parity notes).
- **Actual capabilities:** Format 20+ languages; `--check` CI gate; plugins (e.g., Tailwind class sorting).
- **Usage domain:** Universal formatting standard.
- **Integration method:** `.prettierrc`; editor format-on-save; `prettier --check`.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active (steady cadence).
- **License:** MIT.
- **Limitations:** Opinionated (config surface intentionally small); JS-speed on huge repos.
- **Related resources:** Biome, oxfmt, dprint, ESLint.
- **Sources:** https://prettier.io ; https://github.com/biomejs/biome
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### dprint
- **Canonical identity:** dprint/dprint
- **Category:** Build tooling › Lint/format
- **Type:** Pluggable multi-language formatter (Rust core, WASM plugins)
- **Official URL:** https://dprint.dev ; repo: github.com/dprint/dprint
- **Description:** Rust formatting host with WASM plugins per language (TS, JSON, Markdown, TOML, etc.); config-driven, fast, popular in Deno-adjacent and polyglot setups.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Format via plugins; `dprint check/fmt`; editor extensions.
- **Usage domain:** Polyglot repos wanting one formatter binary.
- **Integration method:** `dprint.json`; plugins per language.
- **Dependencies:** None (binary + WASM plugins).
- **Availability:** Open source; MIT.
- **Maintenance:** Active (David Sherret/Deno-adjacent).
- **License:** MIT (not re-verified).
- **Limitations:** Plugin maturity varies by language.
- **Related resources:** Prettier, Biome, oxfmt.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### Ruff
- **Canonical identity:** astral-sh/ruff
- **Category:** Build tooling › Lint/format (Python)
- **Type:** Python linter + formatter (Rust; ESLint/Black replacement)
- **Official URL:** https://docs.astral.sh/ruff/ ; repo: github.com/astral-sh/ruff
- **Description:** Astral's Rust tool consolidating Python linting (pyflakes/pycodestyle/isort/flake8 plugins → 800+ rules) and formatting (Black-compatible). The default Python lint/format choice in 2026; pairs with uv in the Astral stack.
- **Contents inspected:** Search excerpts (uv ADR stack references: "uv + Ruff" as the 2026 Python default).
- **Actual capabilities:** `ruff check --fix`; `ruff format`; LSP; per-file-ignores.
- **Usage domain:** All Python projects.
- **Integration method:** `pyproject.toml`/`ruff.toml`; pre-commit; editor.
- **Dependencies:** None (binary).
- **Availability:** Open source; MIT.
- **Maintenance:** Very active (Astral).
- **License:** MIT (not re-verified).
- **Limitations:** Some niche flake8 plugins lack equivalents.
- **Related resources:** uv, Black (historical), flake8 (historical), mypy.
- **Sources:** https://github.com/dgrauet/intendant/blob/HEAD/docs/adr/0002-uv-as-dependency-manager.md ; https://github.com/pangamu1/fintech-medallion-portfolio/blob/HEAD/docs/adr/0003-uv-for-python-dependency-management.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Stylelint
- **Canonical identity:** stylelint/stylelint — v16.x
- **Category:** Build tooling › Lint/format (CSS)
- **Type:** CSS/SCSS linter
- **Official URL:** https://stylelint.io ; repo: github.com/stylelint/stylelint
- **Description:** The CSS linter: 170+ rules, sharable configs (`stylelint-config-standard`), SCSS/Less support via custom syntax. Relevant wherever design systems enforce CSS conventions; Tailwind v4 era reduced but didn't eliminate its role.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Lint CSS/SCSS; autofix some rules; custom rules.
- **Usage domain:** Design systems, SCSS codebases.
- **Integration method:** `.stylelintrc`; editor; CI.
- **Dependencies:** Node.js; PostCSS.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Tailwind-utility-heavy codebases get less value.
- **Related resources:** ESLint, Lightning CSS, Tailwind CSS.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified (2026 state not checked)

### HTMLHint
- **Canonical identity:** htmlhint/HTMLHint
- **Category:** Build tooling › Lint/format (HTML)
- **Type:** HTML linter
- **Official URL:** https://htmlhint.com ; repo: github.com/htmlhint/HTMLHint
- **Description:** Static analysis for HTML (tag pairing, attribute rules, inline config comments). Lightweight; used in static-site pipelines.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Rule-based HTML linting; `.htmlhintrc`.
- **Usage domain:** Static HTML, email templates, legacy pages.
- **Integration method:** CLI; config file.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Low cadence.
- **License:** MIT (not re-verified).
- **Limitations:** Not a full accessibility checker (see axe-core/pa11y).
- **Related resources:** Nu HTML Checker, axe-core.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### markdownlint
- **Canonical identity:** DavidAnson/markdownlint (Node CLI; also VS Code ext)
- **Category:** Build tooling › Lint/format (Markdown)
- **Type:** Markdown linter
- **Official URL:** https://github.com/DavidAnson/markdownlint
- **Description:** Style enforcement for Markdown docs (line length, heading increments, fenced code languages). Common in docs-heavy repos and atlas-adjacent documentation workflows.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** 60+ rules; fixable subset; config inheritance.
- **Usage domain:** Documentation repos.
- **Integration method:** `.markdownlint.json`; editor; CI.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Opinionated defaults need tuning per repo.
- **Related resources:** Prettier (formats md), dprint markdown plugin.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### commitlint (+ Conventional Commits)
- **Canonical identity:** conventional-changelog/commitlint
- **Category:** Build tooling › Lint/format (git messages)
- **Type:** Commit-message linter (Conventional Commits)
- **Official URL:** https://commitlint.js.org ; repo: github.com/conventional-changelog/commitlint
- **Description:** Enforces Conventional Commits (`feat:`, `fix:`, scopes) at commit time (with Husky/Lefthook hooks); feeds changesets/semantic-release versioning.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Lint commit messages; shareable configs (`@commitlint/config-conventional`).
- **Usage domain:** Repos with automated versioning/changelogs.
- **Integration method:** `commit-msg` git hook via Husky/Lefthook.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Only as good as the team's discipline.
- **Related resources:** Husky, Lefthook, Changesets, semantic-release.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### cspell
- **Canonical identity:** streetsidesoftware/cspell
- **Category:** Build tooling › Lint/format (spelling)
- **Type:** Code spell checker
- **Official URL:** https://cspell.org ; repo: github.com/streetsidesoftware/cspell
- **Description:** Spell-checks identifiers, comments, and docs with project dictionaries; CI-friendly. Common in large repos and docs pipelines.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** `cspell lint`; custom dictionaries; per-language settings.
- **Usage domain:** Any repo with prose/identifiers.
- **Integration method:** `cspell.json`; editor; CI.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Dictionary maintenance overhead.
- **Related resources:** None close.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### EditorConfig
- **Canonical identity:** editorconfig/editorconfig (spec + core)
- **Category:** Build tooling › Lint/format (convention)
- **Type:** Cross-editor whitespace/style convention (spec + plugins)
- **Official URL:** https://editorconfig.org ; repo: github.com/editorconfig/editorconfig
- **Description:** `.editorconfig` declares indent style/size, EOL, charset, trailing-whitespace rules honored by editors natively or via plugins. Not a linter — the baseline every formatter config assumes.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Declarative style file; editor support.
- **Usage domain:** Universal.
- **Integration method:** `.editorconfig` at repo root.
- **Dependencies:** None.
- **Availability:** Spec + plugins; MIT.
- **Maintenance:** Stable spec.
- **License:** Not verified.
- **Limitations:** Limited rule surface by design.
- **Related resources:** Prettier, Biome.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### 2.7 Code generation

### Orval
- **Canonical identity:** orval-labs/orval — v8.x
- **Category:** Build tooling › Codegen (API clients)
- **Type:** TypeScript client generator from OpenAPI specs
- **Official URL:** https://orval.dev ; repo: github.com/orval-labs/orval
- **Description:** Generates type-safe TS clients (fetch/axios hooks) plus Zod schemas, React Query/SWR hooks, and MSW mocks from OpenAPI 3.x. v8 (2026): framework hooks for Angular/Vue/Solid/Svelte, fetch-client improvements. The favored TS-first OpenAPI client generator in 2026 React/TS stacks.
- **Contents inspected:** Search excerpts: orval-vs-openapi-generator-vs-openapi-typescript comparisons (TS quality, Zod output); v8 framework notes; SKILL docs.
- **Actual capabilities:** Client + hooks + schemas + mocks generation; config file `orval.config.ts`.
- **Usage domain:** TS frontends consuming OpenAPI backends.
- **Integration method:** `orval` CLI in build step; generated files committed or built.
- **Dependencies:** Node.js; OpenAPI spec.
- **Availability:** npm `orval`; MIT.
- **Maintenance:** Very active.
- **License:** MIT (not re-verified).
- **Limitations:** OpenAPI-spec quality determines output quality; spec-first workflow required.
- **Related resources:** openapi-typescript, Hey API, openapi-generator, openapi-fetch (maintenance mode).
- **Sources:** https://www.speakeasy.com/openapi/frameworks/typescript ; https://github.com/ferdinandbujanor/skills/blob/HEAD/plugins/frontend-development/skills/react-best-practices/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### openapi-typescript
- **Canonical identity:** openapi-ts/openapi-typescript — v8.x
- **Category:** Build tooling › Codegen (API types)
- **Type:** OpenAPI → TypeScript types generator (types only, no client)
- **Official URL:** https://openapi-ts.dev ; repo: github.com/openapi-ts/openapi-typescript
- **Description:** Generates pure TS types from OpenAPI schemas (no runtime client — pair with `openapi-fetch`, now in maintenance mode, or any fetch wrapper). v8: "the fastest and lightest way to get types"; schema-object output. Preferred when you want types without a client framework.
- **Contents inspected:** Search excerpts: comparisons (types-only philosophy, v8 speed); openapi-fetch maintenance-mode notice (Dec 2025) affecting the pairing.
- **Actual capabilities:** Spec → `.d.ts`-style type files; CLI + programmatic.
- **Usage domain:** TS projects wanting spec-derived types only.
- **Integration method:** `openapi-typescript schema.yaml -o schema.d.ts`.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Types only — bring your own client; openapi-fetch pairing now maintenance-mode.
- **Related resources:** Orval, Hey API, openapi-fetch, openapi-generator.
- **Sources:** https://www.speakeasy.com/openapi/frameworks/typescript ; https://zuplo.com/blog/the-rise-and-fall-of-openapi-client-generators
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Hey API
- **Canonical identity:** hey-api/openapi-ts
- **Category:** Build tooling › Codegen (API clients)
- **Type:** OpenAPI → TypeScript client generator (plugin-based)
- **Official URL:** https://heyapi.dev ; repo: github.com/hey-api/openapi-ts
- **Description:** Plugin-architecture TS client generator (formerly openapi-typescript-codegen lineage): tree-shakeable clients, Zod/Valibot schemas, TanStack Query integration. Positioned between Orval (batteries-included) and openapi-typescript (types-only).
- **Contents inspected:** Search excerpts: comparisons listing Hey API among 2026 options.
- **Actual capabilities:** Client + schema generation; plugin system.
- **Usage domain:** TS frontends wanting modular generated clients.
- **Integration method:** `@hey-api/openapi-ts` CLI/config.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Plugin ecosystem smaller than openapi-generator's.
- **Related resources:** Orval, openapi-typescript, openapi-generator.
- **Sources:** https://www.speakeasy.com/openapi/frameworks/typescript
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (thin sourcing)

### OpenAPI Generator
- **Canonical identity:** OpenAPITools/openapi-generator — v7.x
- **Category:** Build tooling › Codegen (API clients/servers)
- **Type:** Multi-language OpenAPI code generator (Java-based CLI)
- **Official URL:** https://openapi-generator.tech ; repo: github.com/OpenAPITools/openapi-generator
- **Description:** The heavyweight: generates clients AND servers in 50+ languages from OpenAPI specs (Mustache templates, highly customizable). Java-based; slower/heavier than TS-native tools; the enterprise default when polyglot generation matters. 2026 commentary notes TS output quality lags the TS-native tools.
- **Contents inspected:** Search excerpts: comparisons (polyglot breadth vs TS quality); zuplo analysis of generator landscape.
- **Actual capabilities:** Client+server+docs generation; custom templates.
- **Usage domain:** Polyglot orgs; generated server stubs.
- **Integration method:** Java CLI / Docker; config files.
- **Dependencies:** Java runtime.
- **Availability:** Open source; Apache-2.0.
- **Maintenance:** Active (OpenAPI Tools org).
- **License:** Apache-2.0 (not re-verified).
- **Limitations:** Heavy; TS output less idiomatic than Orval/Hey API; template customization is its own skill.
- **Related resources:** Orval, Hey API, Kiota, autorest (historical).
- **Sources:** https://zuplo.com/blog/the-rise-and-fall-of-openapi-client-generators ; https://www.speakeasy.com/openapi/frameworks/typescript
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### GraphQL Code Generator
- **Canonical identity:** dotansimha/graphql-code-generator (The Guild)
- **Category:** Build tooling › Codegen (GraphQL)
- **Type:** GraphQL schema/documents → typed code generator (plugin system)
- **Official URL:** https://the-guild.dev/graphql/codegen ; repo: github.com/dotansimha/graphql-code-generator
- **Description:** Generates TS types, typed document nodes, and framework hooks (React/Urql/Vue/Apollo) from GraphQL schemas + operations. Plugin architecture (`@graphql-codegen/typescript`, `-operations`, `-typescript-react-apollo`, etc.). Still the standard GraphQL-typed-client pipeline in 2026.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Schema+documents → types/hooks; watch mode; near-operation-file preset.
- **Usage domain:** GraphQL frontends.
- **Integration method:** `codegen.ts` config; CLI in build.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active (The Guild).
- **License:** MIT (not re-verified).
- **Limitations:** Config complexity at scale; codegen step in dev loop.
- **Related resources:** gql.tada (emerging alternative), Apollo Client, urql.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified (2026 state not checked)

### Kiota
- **Canonical identity:** microsoft/kiota
- **Category:** Build tooling › Codegen (API clients)
- **Type:** OpenAPI → multi-language API client generator (Microsoft)
- **Official URL:** https://learn.microsoft.com/en-us/openapi/kiota/ ; repo: github.com/microsoft/kiota
- **Description:** Microsoft's OpenAPI client generator (C#, Java, TS, Go, Python, PHP, Ruby, CLI): generates fluent clients on the Microsoft Graph client model. Used for Microsoft APIs and enterprise SDKs.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Multi-language fluent clients; language refiners.
- **Usage domain:** Microsoft-ecosystem SDKs; enterprise API clients.
- **Integration method:** `kiota generate` CLI.
- **Dependencies:** .NET runtime.
- **Availability:** Open source; MIT.
- **Maintenance:** Active (Microsoft).
- **License:** MIT (not re-verified).
- **Limitations:** Fluent-client style is opinionated; smaller community than openapi-generator.
- **Related resources:** openapi-generator, Microsoft Graph SDKs.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### Hygen
- **Canonical identity:** jondot/hygen
- **Category:** Build tooling › Codegen (scaffolding)
- **Type:** Scalable code generator (templates + prompts)
- **Official URL:** https://www.hygen.io ; repo: github.com/jondot/hygen
- **Description:** Template-based generator for scaffolding components/files (`hygen component new`): EJS templates in `_templates/`, prompt support, inject/append actions. The codegen-for-humans complement to API codegen tools.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Template scaffolding; file injection; interactive prompts.
- **Usage domain:** Component/page scaffolding in teams.
- **Integration method:** `_templates/` dir; CLI.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Low cadence (stable).
- **License:** MIT (not re-verified).
- **Limitations:** Template maintenance burden; no longer trendy.
- **Related resources:** Plop (alternative), Yeoman (historical).
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### protoc (+ buf)
- **Canonical identity:** protocolbuffers/protobuf (`protoc`); bufbuild/buf
- **Category:** Build tooling › Codegen (schemas/RPC)
- **Type:** Protocol Buffers compiler (+ modern Buf toolchain)
- **Official URL:** https://protobuf.dev ; https://buf.build ; repos: github.com/protocolbuffers/protobuf, github.com/bufbuild/buf
- **Description:** `protoc` compiles `.proto` schemas to typed code in 10+ languages (gRPC stubs). Buf is the modern toolchain: linting, breaking-change detection, schema registry (BSR), remote generation — the 2026 default for serious protobuf workflows.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Codegen per language; buf lint/breaking/generate; BSR registry.
- **Usage domain:** gRPC services, schema-first APIs.
- **Integration method:** `buf generate`; `protoc` plugins.
- **Dependencies:** None (binaries).
- **Availability:** Open source; BSD-3-Clause (protobuf).
- **Maintenance:** Active.
- **License:** BSD-3-Clause (not re-verified).
- **Limitations:** Schema-first discipline required; generated code review burden.
- **Related resources:** gRPC, Connect (connectrpc), Orval (REST analog).
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### 2.8 Dependency management and supply-chain security

### Dependabot
- **Canonical identity:** GitHub Dependabot (dependabot/dependabot-core)
- **Category:** Build tooling › Dep mgmt/security
- **Type:** Automated dependency update service (GitHub-native)
- **Official URL:** https://github.com/dependabot ; docs: https://docs.github.com/en/code-security/dependabot
- **Description:** GitHub's built-in updater: version-update PRs (npm, pip, GitHub Actions, Docker, etc.) + security alerts/PRs for vulnerable deps. Strengths: zero config, GitHub-native; weaknesses: rigid config, grouped-update UX, no automerge policies as flexible as Renovate's. Free for public/private repos.
- **Contents inspected:** Search excerpts: Renovate-vs-Dependabot 2026 comparisons (native convenience vs flexibility).
- **Actual capabilities:** Scheduled update PRs; security PRs; `dependabot.yml` config.
- **Usage domain:** GitHub repos wanting built-in updates.
- **Integration method:** `.github/dependabot.yml`; GitHub settings.
- **Dependencies:** GitHub.
- **Availability:** Hosted (GitHub).
- **Maintenance:** Active.
- **License:** Not applicable (service; core is open source).
- **Limitations:** Config expressiveness; monorepo grouping pain; GitHub-only.
- **Related resources:** Renovate, Socket.dev, Snyk.
- **Sources:** https://github.com/g-baskin/the-god-skill/blob/HEAD/skills/dependency-audit-weapon/SKILL.md ; https://dev.to/search?q=renovate+vs+dependabot+2026
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Renovate
- **Canonical identity:** renovatebot/renovate (Mend)
- **Category:** Build tooling › Dep mgmt/security
- **Type:** Universal automated dependency updater (self-hostable)
- **Official URL:** https://docs.renovatebot.com ; repo: github.com/renovatebot/renovate ; hosted: https://www.mend.io/renovate
- **Description:** The power-user updater: 100+ managers (npm, pip, uv, Docker, Terraform...), presets, automerge policies, grouping, stability-day/cooldown scheduling, vulnerability alerts. 2026 verdict: "Renovate for control, Dependabot for convenience." Mend hosts it; fully self-hostable.
- **Contents inspected:** Search excerpts: comparisons (manager breadth, presets, automerge); Mend docs.
- **Actual capabilities:** PR automation with policies; dependency dashboard issue; lockfile maintenance.
- **Usage domain:** Teams wanting update policy-as-config; multi-ecosystem repos.
- **Integration method:** `renovate.json`; GitHub/GitLab/Bitbucket app.
- **Dependencies:** None (bot).
- **Availability:** Open source; Mend-hosted free tier.
- **Maintenance:** Very active.
- **License:** AGPL-3.0 (not re-verified).
- **Limitations:** Config learning curve; noisy without presets.
- **Related resources:** Dependabot, Mend, Socket.dev.
- **Sources:** https://docs.renovatebot.com ; https://github.com/g-baskin/the-god-skill/blob/HEAD/skills/dependency-audit-weapon/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Socket.dev (Socket)
- **Canonical identity:** Socket (socket.dev)
- **Category:** Build tooling › Dep mgmt/security
- **Type:** Behavioral supply-chain security (package firewall/scanner)
- **Official URL:** https://socket.dev ; CLI: `socket` npm package
- **Description:** Scans packages for risky BEHAVIORS (install scripts, network access, obfuscation, typosquats, protestware) rather than just known CVEs: the 2026-standard answer to the npm-audit gap (audit only knows published CVEs — the axios hijack had none). GitHub app + CLI + firewall proxy; free for open source.
- **Contents inspected:** Search excerpts: dependency-audit SKILL (Socket behavioral model; axios case study); 2026 tooling guides.
- **Actual capabilities:** `socket audit`/`socket optimize`; PR risk reports; firewall blocking.
- **Usage domain:** Supply-chain-sensitive teams.
- **Integration method:** GitHub app; CLI in CI; `socket.yml`.
- **Dependencies:** None.
- **Availability:** Hosted (freemium).
- **Maintenance:** Active (Socket Inc.).
- **License:** Not applicable (service).
- **Limitations:** Behavioral heuristics can false-positive; coverage breadth vs depth trade-offs.
- **Related resources:** Snyk, npm audit, osv-scanner, JSR (provenance).
- **Sources:** https://github.com/g-baskin/the-god-skill/blob/HEAD/skills/dependency-audit-weapon/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Snyk
- **Canonical identity:** Snyk (snyk.io)
- **Category:** Build tooling › Dep mgmt/security
- **Type:** Vulnerability scanning platform (deps, code, containers, IaC)
- **Official URL:** https://snyk.io ; CLI: `snyk`
- **Description:** Developer security platform: `snyk test` (vuln scan), `snyk monitor`, fix PRs, license checks, container/IaC scanning. Own vulnerability DB (often faster than NVD). Freemium; enterprise staple.
- **Contents inspected:** Search excerpts: dependency-audit SKILL listings.
- **Actual capabilities:** Vuln scanning + fix PRs; policies; SBOM.
- **Usage domain:** Enterprise AppSec; compliance.
- **Integration method:** CLI; Git integrations; `snyk` config.
- **Dependencies:** None.
- **Availability:** Hosted (freemium).
- **Maintenance:** Active.
- **License:** Not applicable (service; CLI open).
- **Limitations:** Cost at scale; alert fatigue without tuning.
- **Related resources:** Socket.dev, Dependabot, osv-scanner.
- **Sources:** https://github.com/g-baskin/the-god-skill/blob/HEAD/skills/dependency-audit-weapon/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified (thin sourcing)

### osv-scanner
- **Canonical identity:** google/osv-scanner
- **Category:** Build tooling › Dep mgmt/security
- **Type:** Vulnerability scanner on the OSV database (Google)
- **Official URL:** https://google.github.io/osv-scanner/ ; repo: github.com/google/osv-scanner
- **Description:** Open-source scanner querying the distributed OSV.dev vulnerability database across lockfiles/SBOMs (npm, pip, Go, Rust, containers). The free, CI-friendly CVE scanner; basis for many GitHub Action vuln gates.
- **Contents inspected:** Search excerpts: dependency-audit SKILL (OSV as the free CVE layer).
- **Actual capabilities:** `osv-scanner` CLI; lockfile/SBOM/container scanning.
- **Usage domain:** CI vuln gates; SBOM workflows.
- **Integration method:** CLI; GitHub Action.
- **Dependencies:** OSV.dev API.
- **Availability:** Open source; Apache-2.0.
- **Maintenance:** Active (Google).
- **License:** Apache-2.0 (not re-verified).
- **Limitations:** CVE-knowledge only (same blind spot as npm audit for novel malicious packages).
- **Related resources:** npm audit, pip-audit, Snyk, OSV.dev.
- **Sources:** https://github.com/g-baskin/the-god-skill/blob/HEAD/skills/dependency-audit-weapon/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### npm audit (+ pip-audit)
- **Canonical identity:** npm CLI `audit` (GitHub Advisory Database); pypa/pip-audit
- **Category:** Build tooling › Dep mgmt/security
- **Type:** Built-in vulnerability auditors
- **Official URL:** https://docs.npmjs.com/cli/v11/commands/npm-audit ; https://github.com/pypa/pip-audit
- **Description:** `npm audit` checks the dependency tree against the GitHub Advisory DB (`audit fix`, `--omit=dev`). `pip-audit` is the PyPA equivalent for Python (OSV-backed). Both share the fundamental limit: they only know published advisories — no protection against novel malicious packages (the axios case).
- **Contents inspected:** Search excerpts: audit-limit analyses; axios hijack writeups.
- **Actual capabilities:** Advisory matching; fix suggestions; JSON output for CI.
- **Usage domain:** Baseline CI hygiene.
- **Integration method:** `npm audit --audit-level=high`; `pip-audit -r requirements.txt`.
- **Dependencies:** Advisory DBs.
- **Availability:** Bundled/open.
- **Maintenance:** Active.
- **License:** npm: Artistic-2.0; pip-audit: Apache-2.0 (not re-verified).
- **Limitations:** Advisory-only; false confidence risk.
- **Related resources:** osv-scanner, Socket.dev, Snyk.
- **Sources:** https://github.com/g-baskin/the-god-skill/blob/HEAD/skills/dependency-audit-weapon/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### knip
- **Canonical identity:** webpro/knip
- **Category:** Build tooling › Dep mgmt
- **Type:** Unused dependency/export/file finder
- **Official URL:** https://knip.dev ; repo: github.com/webpro/knip
- **Description:** Finds unused dependencies, devDependencies, exports, files, and config in JS/TS projects — the 2026 replacement for depcheck: understands workspaces, entry patterns, plugin configs. CI gate against dependency rot.
- **Contents inspected:** Search excerpts: "knip replacing depcheck" framing; monorepo hygiene guides.
- **Actual capabilities:** `knip` report; `--fix`-ish remediation guidance; production-mode strictness.
- **Usage domain:** Monorepo hygiene; dependency audits.
- **Integration method:** `knip.json`; CI step.
- **Dependencies:** Node.js.
- **Availability:** npm; ISC.
- **Maintenance:** Active (Lars Kappert/webpro).
- **License:** ISC (not re-verified).
- **Limitations:** Heuristic (dynamic imports need config); false positives on plugin-style usage.
- **Related resources:** depcheck (legacy), publint.
- **Sources:** https://knip.dev ; https://github.com/g-baskin/the-god-skill/blob/HEAD/skills/dependency-audit-weapon/SKILL.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### depcheck (legacy)
- **Canonical identity:** depcheck/depcheck
- **Category:** Build tooling › Dep mgmt
- **Type:** Unused-dependency checker (legacy)
- **Official URL:** https://github.com/depcheck/depcheck
- **Description:** The original unused-dep finder; largely superseded by knip in 2026 (weaker workspace/monorepo understanding). Still present in older CI configs.
- **Contents inspected:** Not directly searched; status from knip comparisons.
- **Actual capabilities:** `depcheck` unused/missing dep report.
- **Usage domain:** Legacy CI configs.
- **Integration method:** CLI; `.depcheckrc`.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT/Apache.
- **Maintenance:** Low (community).
- **License:** Not verified.
- **Limitations:** Superseded; use knip for new setups.
- **Related resources:** knip.
- **Sources:** https://knip.dev
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### npm-check-updates
- **Canonical identity:** raineorshine/npm-check-updates (`ncu`)
- **Category:** Build tooling › Dep mgmt
- **Type:** Interactive dependency update planner
- **Official URL:** https://github.com/raineorshine/npm-check-updates
- **Description:** Shows/updates outdated deps beyond semver ranges (`ncu -u`, interactive mode, doctor mode running tests per upgrade). The manual counterpart to Dependabot/Renovate.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Outdated analysis; interactive upgrade; per-package test runs.
- **Usage domain:** Manual upgrade sessions.
- **Integration method:** `npx npm-check-updates -i`.
- **Dependencies:** Node.js.
- **Availability:** npm; Apache-2.0.
- **Maintenance:** Active.
- **License:** Apache-2.0 (not re-verified).
- **Limitations:** Manual; no policy engine.
- **Related resources:** pnpm outdated, yarn upgrade-interactive, taze.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### syncpack
- **Canonical identity:** JamBalaya56562/syncpack
- **Category:** Build tooling › Dep mgmt (monorepo)
- **Type:** Monorepo dependency version consistency enforcer
- **Official URL:** https://github.com/JamBalaya56562/syncpack
- **Description:** Enforces consistent dependency versions/ranges across monorepo packages (`syncpack lint`, `fix`, `list-mismatches`); firstMatch version-group policies. Standard monorepo hygiene alongside Changesets.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Version/range linting + autofix; semver-group policies.
- **Usage domain:** pnpm/npm monorepos.
- **Integration method:** `.syncpackrc`; CI step.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Policy config needed per repo.
- **Related resources:** manypkg, pnpm catalogs, Changesets.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### manypkg
- **Canonical identity:** Thinkmill/manypkg
- **Category:** Build tooling › Dep mgmt (monorepo)
- **Type:** Monorepo package.json linter (checks)
- **Official URL:** https://github.com/Thinkmill/manypkg
- **Description:** Lints monorepo package.json files for common errors (missing/mismatched internal deps, inconsistent fields); `manypkg check` + `fix`. Thinkmill's companion to Changesets.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** `check`/`fix` rules for internal linking.
- **Usage domain:** Yarn/pnpm monorepos.
- **Integration method:** CLI in CI.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Low cadence (stable).
- **License:** MIT (not re-verified).
- **Limitations:** Narrow scope (package.json correctness only).
- **Related resources:** syncpack, Changesets.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### 2.9 Monorepo tooling and version management

### Turborepo
- **Canonical identity:** vercel/turbo — v2.x
- **Category:** Build tooling › Monorepo
- **Type:** Monorepo task runner + remote cache (Rust)
- **Official URL:** https://turborepo.dev ; repo: github.com/vercel/turbo
- **Description:** The 2026 default monorepo orchestrator for JS: task graph (`turbo.json`), content-hash caching, Remote Caching (Vercel), affected-package filtering. Pairs with pnpm workspaces. "Turborepo's job is to figure out which packages need rebuilding and which can use cached results."
- **Contents inspected:** Search excerpts: monorepo-stack 2026 guides (Turborepo+pnpm as the default pairing); Remote Caching notes.
- **Actual capabilities:** `turbo run build`; pipeline config; remote cache; `turbo prune`.
- **Usage domain:** JS/TS monorepos.
- **Integration method:** `turbo.json`; workspace manager (pnpm/npm/yarn).
- **Dependencies:** Workspace tool.
- **Availability:** npm `turbo`; MPL-2.0.
- **Maintenance:** Very active (Vercel).
- **License:** MPL-2.0 (not re-verified).
- **Limitations:** JS-centric; versioning needs Changesets alongside.
- **Related resources:** Nx, Changesets, pnpm workspaces, Vercel Remote Cache.
- **Sources:** https://dev.to/medianova/javascript-monorepo-tools-comparison-2026-turborepo-vs-nx-vs-others ; https://github.com/oleksiiprofessor/Digital-Marketing-Automation/blob/HEAD/.ai/rules/stacks/monorepo.md
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Nx
- **Canonical identity:** nrwl/nx — v21.x/22.x line
- **Category:** Build tooling › Monorepo
- **Type:** Monorepo build system + plugins/generators (TS/Rust)
- **Official URL:** https://nx.dev ; repo: github.com/nrwl/nx
- **Description:** The batteries-included monorepo platform: affected commands, computation caching, code generators, 100+ plugins (React, Node, Python, Go...), Nx Cloud remote caching, module federation support. Heavier/opinionated vs Turborepo's thin task-runner; the choice for large orgs wanting generators + conventions.
- **Contents inspected:** Search excerpts: 2026 comparisons (Nx vs Turborepo: "batteries-included vs thin"); plugin ecosystem notes.
- **Actual capabilities:** `nx affected/build/test`; generators; `nx release`; remote caching.
- **Usage domain:** Large org monorepos, polyglot.
- **Integration method:** `nx.json`; `npx nx init`.
- **Dependencies:** Node.js.
- **Availability:** npm `nx`; MIT (+ Nx Cloud hosted).
- **Maintenance:** Very active (Nx team).
- **License:** MIT (not re-verified).
- **Limitations:** Opinionated; migration/incremental adoption heavier than Turbo.
- **Related resources:** Turborepo, Lerna (legacy), Moon, Bazel.
- **Sources:** https://dev.to/medianova/javascript-monorepo-tools-comparison-2026-turborepo-vs-nx-vs-others ; https://nx.dev
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Changesets
- **Canonical identity:** changesets/changesets
- **Category:** Build tooling › Version management
- **Type:** Monorepo versioning + changelog workflow
- **Official URL:** https://github.com/changesets/changesets
- **Description:** The 2026 standard for versioning JS monorepos: PRs include changeset markdown files (`.changeset/*.md`) declaring bump type; the Changesets GitHub Action consumes them into version PRs + changelogs + npm publishes. Pairs with Turborepo/Nx.
- **Contents inspected:** Search excerpts: monorepo-stack docs (Changesets Action flow); versioning comparisons.
- **Actual capabilities:** `changeset add/version/publish`; linked/fixed packages; snapshot releases.
- **Usage domain:** Versioned JS monorepos.
- **Integration method:** `.changeset/config.json`; GitHub Action.
- **Dependencies:** Node.js; git host.
- **Availability:** npm `@changesets/cli`; MIT.
- **Maintenance:** Active (Thinkmill/community).
- **License:** MIT (not re-verified).
- **Limitations:** Human discipline (changeset per PR); not for non-npm artifacts.
- **Related resources:** semantic-release, release-please, manypkg, syncpack.
- **Sources:** https://github.com/oleksiiprofessor/Digital-Marketing-Automation/blob/HEAD/.ai/rules/stacks/monorepo.md ; https://dev.to/medianova/javascript-monorepo-tools-comparison-2026-turborepo-vs-nx-vs-others
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Lerna (legacy mode)
- **Canonical identity:** lerna/lerna — v8.x/v9.x
- **Category:** Build tooling › Version management (legacy)
- **Type:** Monorepo versioning/publishing (legacy; now Nx-maintained)
- **Official URL:** https://lerna.js.org ; repo: github.com/lerna/lerna
- **Description:** The original JS monorepo publisher (independent/fixed versioning). Now maintained by the Nx team in low-churn legacy mode; new projects choose Changesets. Still present in older monorepos.
- **Contents inspected:** Not directly searched; status from 2026 monorepo comparisons.
- **Actual capabilities:** `lerna version/publish`; bootstrapping (legacy).
- **Usage domain:** Existing Lerna monorepos.
- **Integration method:** `lerna.json`.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Low (legacy).
- **License:** MIT (not re-verified).
- **Limitations:** Superseded patterns; use Changesets for new work.
- **Related resources:** Changesets, Nx, semantic-release.
- **Sources:** https://dev.to/medianova/javascript-monorepo-tools-comparison-2026-turborepo-vs-nx-vs-others
- **Verification date:** 2026-10-10
- **Confidence:** Partially verified

### Rush
- **Canonical identity:** microsoft/rushstack (rush)
- **Category:** Build tooling › Monorepo
- **Type:** Enterprise monorepo manager (Microsoft)
- **Official URL:** https://rushjs.io ; repo: github.com/microsoft/rushstack
- **Description:** Microsoft's monorepo orchestrator: deterministic installs (shrinkwrap), phased builds, change-file versioning, repo-wide policies. The choice for very large/regulated JS monorepos; heavier ceremony than Turbo/Nx.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** `rush install/build/rebuild`; change files; publish flow.
- **Usage domain:** Large enterprise monorepos.
- **Integration method:** `rush.json`; common/config.
- **Dependencies:** Node.js; pnpm/npm/yarn under the hood.
- **Availability:** npm `@microsoft/rush`; MIT.
- **Maintenance:** Active (Microsoft).
- **License:** MIT (not re-verified).
- **Limitations:** Ceremony; smaller community than Turbo/Nx.
- **Related resources:** Turborepo, Nx, Changesets.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### Moon
- **Canonical identity:** moonrepo/moon
- **Category:** Build tooling › Monorepo
- **Type:** Polyglot monorepo task runner (Rust)
- **Official URL:** https://moonrepo.dev ; repo: github.com/moonrepo/moon
- **Description:** Rust task runner for polyglot monorepos (JS, Rust, Go, Python): task inheritance, hashing, remote caching via moonbase. The polyglot alternative to Turbo's JS-centrism.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** `.moon/tasks.yml`; affected runs; caching.
- **Usage domain:** Polyglot monorepos.
- **Integration method:** `.moon/workspace.yml`.
- **Dependencies:** Rust binary.
- **Availability:** Open source; MIT.
- **Maintenance:** Active (moonrepo).
- **License:** MIT (not re-verified).
- **Limitations:** Smaller ecosystem than Turbo/Nx.
- **Related resources:** Turborepo, Bazel, Pants.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### Bazel
- **Canonical identity:** bazelbuild/bazel (+ rules_js)
- **Category:** Build tooling › Monorepo/build system
- **Type:** Hermetic polyglot build system (Google)
- **Official URL:** https://bazel.build ; repo: github.com/bazelbuild/bazel
- **Description:** Google's hermetic, reproducible build system with JS rules (rules_js / aspect rules). Maximum correctness/caching at maximum configuration cost; used by Google-scale monorepos. 2026: still the ceiling for reproducibility, rarely chosen for typical web apps.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Hermetic actions; remote execution/caching; query language.
- **Usage domain:** Google-scale/polyglot monorepos; reproducibility requirements.
- **Integration method:** `MODULE.bazel`/`BUILD` files.
- **Dependencies:** JVM (launcher); toolchains.
- **Availability:** Open source; Apache-2.0.
- **Maintenance:** Active (Google).
- **License:** Apache-2.0 (not re-verified).
- **Limitations:** Steep learning curve; JS DX poorer than Turbo/Nx.
- **Related resources:** Buck2, Pants, Nix, reproducible-builds.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### semantic-release
- **Canonical identity:** semantic-release/semantic-release
- **Category:** Build tooling › Version management
- **Type:** Fully automated versioning from Conventional Commits
- **Official URL:** https://semantic-release.gitbook.io ; repo: github.com/semantic-release/semantic-release
- **Description:** Derives next version from commit messages (Conventional Commits): generates changelog, GitHub release, npm publish with zero human version decisions. The single-package automation standard; monorepos usually prefer Changesets or multi-semantic-release.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** CI-driven release; plugin ecosystem (npm, GitHub, changelog).
- **Usage domain:** Single-package automated releases.
- **Integration method:** `.releaserc`; CI job.
- **Dependencies:** Node.js; git host.
- **Availability:** npm; MIT.
- **Maintenance:** Active (community).
- **License:** MIT (not re-verified).
- **Limitations:** Commit-discipline required; monorepo needs multi-semantic-release.
- **Related resources:** release-please, Changesets, commitlint.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### release-please
- **Canonical identity:** googleapis/release-please
- **Category:** Build tooling › Version management
- **Type:** Release-PR automation from Conventional Commits (Google)
- **Official URL:** https://github.com/googleapis/release-please
- **Description:** Google's releaser: opens/updates a Release PR (version bumps + changelog from commits); merging it creates the GitHub release and publishes. Human-gated where semantic-release is fully automatic; polyglot (strategies per language).
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Release PRs; manifest mode for monorepos; language strategies.
- **Usage domain:** Teams wanting a human merge gate on releases.
- **Integration method:** GitHub Action; `release-please-config.json`.
- **Dependencies:** GitHub.
- **Availability:** Open source; Apache-2.0.
- **Maintenance:** Active (Google).
- **License:** Apache-2.0 (not re-verified).
- **Limitations:** Commit-discipline required; GitHub-centric.
- **Related resources:** semantic-release, Changesets, commitlint.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### 2.10 Dev servers and process management

### nodemon
- **Canonical identity:** remy/nodemon
- **Category:** Build tooling › Dev servers/process
- **Type:** Node.js file-watcher auto-restarter
- **Official URL:** https://nodemon.io ; repo: github.com/remy/nodemon
- **Description:** The classic "restart node on file change" dev tool (`nodemon server.js`); configurable watch/ignore/exec. 2026: largely displaced by `node --watch` (built-in since Node 18.11/20) and framework dev servers, but still embedded in countless tutorials and legacy setups.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Watch + restart; exec arbitrary commands; config file.
- **Usage domain:** Legacy Node dev loops; tutorials.
- **Integration method:** `nodemon.json`; npm script.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Low cadence (stable).
- **License:** MIT (not re-verified).
- **Limitations:** Restart-based (no HMR); superseded by `node --watch` for simple cases.
- **Related resources:** node --watch, tsx watch, PM2 (prod).
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### node --watch
- **Canonical identity:** Node.js built-in `--watch` (nodejs/node)
- **Category:** Build tooling › Dev servers/process
- **Type:** Built-in file-watching restart mode
- **Official URL:** https://nodejs.org/api/cli.html#--watch
- **Description:** `node --watch server.js` restarts on file changes with zero dependencies (stable since Node 22). The 2026 default for simple Node dev loops — no nodemon needed.
- **Contents inspected:** Not directly searched; standard Node docs knowledge.
- **Actual capabilities:** Watch-mode restart; `--watch-path`/`--watch-preserve-output`.
- **Usage domain:** Simple Node services/scripts dev.
- **Integration method:** CLI flag; `package.json` script.
- **Dependencies:** Node.js ≥18.11 (stable ≥22).
- **Availability:** Built in.
- **Maintenance:** Active (Node core).
- **License:** MIT.
- **Limitations:** Restart-only; no TS without type stripping flags.
- **Related resources:** nodemon, tsx, Vite (frontend).
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### PM2
- **Canonical identity:** Unitech/pm2
- **Category:** Build tooling › Dev servers/process
- **Type:** Node.js process manager (production)
- **Official URL:** https://pm2.keymetrics.io ; repo: github.com/Unitech/pm2
- **Description:** Production process manager: clustering, auto-restart, log management, monitoring, startup scripts, `ecosystem.config.js`. Still the default "keep my Node app alive on a VPS" answer; PaaS/containers reduced but didn't eliminate its niche.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Cluster mode; watch+reload; log rotation; keymetrics monitoring.
- **Usage domain:** VPS/bare-metal Node deployments.
- **Integration method:** `pm2 start`; ecosystem file.
- **Dependencies:** Node.js.
- **Availability:** npm; AGPL-3.0.
- **Maintenance:** Active (low churn).
- **License:** AGPL-3.0 (not re-verified).
- **Limitations:** AGPL licensing; containers/PaaS often make it redundant.
- **Related resources:** systemd, Docker, nodemon (dev).
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### concurrently
- **Canonical identity:** open-cli-tools/concurrently
- **Category:** Build tooling › Dev servers/process
- **Type:** Parallel npm-script runner
- **Official URL:** https://github.com/open-cli-tools/concurrently
- **Description:** Runs multiple dev commands in one terminal (`concurrently "vite" "tsc -w"`): prefixed/colored output, kill-others behavior. The standard `dev` script glue.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Parallel/sequential runs; output prefixing; exit-code policies.
- **Usage domain:** Multi-process dev scripts.
- **Integration method:** npm script.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Output interleaving at scale.
- **Related resources:** npm-run-all (legacy), mise tasks.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### 2.11 Git hooks

### Husky
- **Canonical identity:** typicode/husky — v9.x
- **Category:** Build tooling › Git hooks
- **Type:** Git hooks manager
- **Official URL:** https://typicode.github.io/husky/ ; repo: github.com/typicode/husky
- **Description:** The standard git-hooks installer: `husky init` writes hook scripts into `.husky/` (pre-commit → lint-staged, commit-msg → commitlint). v9 removed the old `.huskyrc` JS config in favor of plain shell hook files. 2026: still the default, though Lefthook gains on speed.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Hook installation/management; plain-script hooks.
- **Usage domain:** Pre-commit lint/format/test gates.
- **Integration method:** `.husky/` scripts; `prepare` script.
- **Dependencies:** Git; Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** Per-developer install (can be skipped with --no-verify); shell-script hooks.
- **Related resources:** lint-staged, Lefthook, simple-git-hooks, commitlint.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### lint-staged
- **Canonical identity:** lint-staged/lint-staged — v16.x
- **Category:** Build tooling › Git hooks
- **Type:** Staged-files task runner (pre-commit)
- **Official URL:** https://github.com/lint-staged/lint-staged
- **Description:** Runs linters/formatters ONLY on staged files at commit time (`lint-staged` config mapping globs → commands). The standard Husky pre-commit companion; v15+ requires Node 18.12+.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Glob→command mapping on staged files; autofix + re-stage.
- **Usage domain:** Pre-commit formatting/linting.
- **Integration method:** `lint-staged.config.js`; Husky pre-commit hook.
- **Dependencies:** Node.js; git.
- **Availability:** npm; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** JS-only runner (use Lefthook for polyglot/speed).
- **Related resources:** Husky, Lefthook, Biome, Prettier.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### Lefthook
- **Canonical identity:** evilmartians/lefthook (Go)
- **Category:** Build tooling › Git hooks
- **Type:** Fast polyglot git-hooks manager (Go binary)
- **Official URL:** https://github.com/evilmartians/lefthook
- **Description:** Evil Martians' Go-based hooks runner: parallel execution, per-file commands, `lefthook.yml` config, faster than Husky+lint-staged for big repos; polyglot (not Node-bound). Growing 2026 adoption.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Parallel hook commands; file templates; remote config.
- **Usage domain:** Fast pre-commit/pre-push gates; polyglot repos.
- **Integration method:** `lefthook.yml`; `lefthook install`.
- **Dependencies:** Go binary.
- **Availability:** Open source; MIT.
- **Maintenance:** Active.
- **License:** MIT (not re-verified).
- **Limitations:** YAML config learning curve; smaller mindshare than Husky.
- **Related resources:** Husky, lint-staged, pre-commit (Python).
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### simple-git-hooks
- **Canonical identity:** toplenboren/simple-git-hooks
- **Category:** Build tooling › Git hooks
- **Type:** Minimal git-hooks setter (package.json config)
- **Official URL:** https://github.com/toplenboren/simple-git-hooks
- **Description:** Zero-dependency hooks via `simple-git-hooks` key in package.json — the lightweight Husky alternative for small projects.
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Hook installation from package.json config.
- **Usage domain:** Small projects wanting minimal hook setup.
- **Integration method:** package.json key.
- **Dependencies:** Node.js.
- **Availability:** npm; MIT.
- **Maintenance:** Low cadence.
- **License:** MIT (not re-verified).
- **Limitations:** Minimal features vs Husky/Lefthook.
- **Related resources:** Husky, Lefthook.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### 2.12 Build caching and reproducible builds

### sccache
- **Canonical identity:** mozilla/sccache
- **Category:** Build tooling › Build caching
- **Type:** Compiler cache (ccache-like, with cloud backends)
- **Official URL:** https://github.com/mozilla/sccache
- **Description:** Mozilla's compiler cache: wraps C/C++/Rust (and other) compiler invocations, caching to local disk or cloud (S3/GCS/Redis/Azure). The standard CI accelerator for native/Rust/WASM build steps (e.g., caching wasm-pack/Rust builds in JS toolchains).
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Compiler output caching; S3/GCS/Redis backends; statistics.
- **Usage domain:** CI for Rust/C++/WASM components.
- **Integration method:** `RUSTC_WRAPPER=sccache`; env config.
- **Dependencies:** None (binary).
- **Availability:** Open source; Apache-2.0.
- **Maintenance:** Active (Mozilla).
- **License:** Apache-2.0 (not re-verified).
- **Limitations:** Cache correctness depends on proper input hashing; setup overhead.
- **Related resources:** ccache, Turborepo Remote Caching, Nx Cloud.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

### reproducible-builds / SOURCE_DATE_EPOCH
- **Canonical identity:** reproducible-builds.org (project); SOURCE_DATE_EPOCH (spec)
- **Category:** Build tooling › Reproducible builds
- **Type:** Practice + specification for bit-identical builds
- **Official URL:** https://reproducible-builds.org ; spec: https://reproducible-builds.org/specs/source-date-epoch/
- **Description:** The discipline of producing bit-for-bit identical artifacts from identical sources: `SOURCE_DATE_EPOCH` standardizes embedded timestamps; deterministic file ordering, fixed locales, and normalized paths complete it. Relevant to npm package publishing (provenance/attestations), supply-chain verification, and distro packaging. Debian/Fedora document per-ecosystem guidance; JS-ecosystem adoption is partial (bundler output determinism varies).
- **Contents inspected:** Not directly searched; included for systematic coverage.
- **Actual capabilities:** Spec + tooling guidance (`diffoscope` for diagnosing nondeterminism).
- **Usage domain:** Supply-chain security; distro/regulated builds.
- **Integration method:** `SOURCE_DATE_EPOCH` env; deterministic build flags.
- **Dependencies:** None.
- **Availability:** Open spec.
- **Maintenance:** Active (project).
- **License:** Not applicable (spec; docs CC).
- **Limitations:** JS bundler determinism is not guaranteed across versions; partial ecosystem buy-in.
- **Related resources:** SLSA, Sigstore, JSR provenance, diffoscope.
- **Sources:** Not directly sourced this session.
- **Verification date:** 2026-10-10
- **Confidence:** Unverified

---

## Coverage note

**Counts.** 155 distinct resource records across 19 subcategories: 9 Verified, 107 Partially verified, 39 Unverified, 0 Archived/Inaccessible/Historical (two deprecated-but-present records — Rye and tsup — are labeled via their Verified confidence lines noting deprecation; Volta is flagged "stood down" in its Partially verified record). Per-subcategory: 1.1=14, 1.2=5, 1.3=9, 1.4=15, 1.5=9, 1.6=6, 2.1=9, 2.1b=7, 2.2=6, 2.3=14, 2.4=7, 2.5=4, 2.6=12, 2.7=8, 2.8=11, 2.9=9, 2.10=4, 2.11=4, 2.12=2.

**Search limitations.** 35 discovery search themes were run (logged above) plus 3 primary-source opens (rolldown, oxc, biome READMEs). Records labeled Partially verified rest on search-result excerpts (titles/snippets/URLs) from 2+ independent sources or single detailed secondary sources; per instructions, search-result URLs were used verbatim in Source fields. 39 Unverified records were included for systematic breadth (mission: "not just the famous names") without a 2026-state check this session — they are long-established tools whose existence/capabilities are stable knowledge, flagged honestly.

**Whether more work is warranted.** High value: primary-source pass on the 39 Unverified records (official docs/READMEs) to confirm 2026 status, especially fast-moving ones (Turbo/Nx versions, Stylelint v17, Biome v2.x line). Medium value: pinning exact 2026 version numbers for Parcel, Farm, dprint, Hygen. Low value: further depth on deprecated items (Rye, tsup, Volta). A follow-up session could also verify license fields currently marked "not re-verified."

**Known gaps / unresolved items.**
- Exact TypeScript 7.1+ programmatic-API status and `tsgo` naming finalization: unresolved (tracked in the TS 7 record).
- WASI 0.3.2 release (scheduled 2026-10-13, after this catalog's date): unresolved — needs a later check.
- Node 26 LTS transition (2026-10-28): upcoming at catalog date; status will change.
- Deno 3 / Bun 2 version claims appear in some secondary sources but were not independently corroborated — recorded conservatively at Deno 2.7.x / Bun 1.4.x.
- Vendor-adjacent benchmark numbers (CDN TTFB, install speeds, bundler speedups) are reported as-reported, not independently measured.
- Dedup cross-references honored: @astryxdesign/cli (no MCP server), shadcn MCP, upstash/context7, code-yeongyu/oh-my-openagent, anomalyco/opencode, opencode.ai docs — none cataloged here.
