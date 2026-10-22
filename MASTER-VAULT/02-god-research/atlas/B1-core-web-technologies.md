# B1 — Core Web Development Technologies
**Deliverable B — Category Catalogs · The Omniscient Resource Atlas**
**Built:** 2026-10-10 · Verification labels: Verified / Partially verified / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved / Not labeled (source record carried no explicit label)
**Scope honesty:** condensed from the 13 workstream catalogs in `catalogs/` — verified essentials only. Full Part-21 records (files inspected, capabilities, dependencies, limitations, sources) remain in the source catalog files. Cross-references point to the canonical record rather than duplicating it.


## 1. Core web development technologies — languages, browser technologies, standards

Languages, browser APIs, WebAssembly, standards, and the 2026 platform state. Source: `catalogs/01a-languages-build.md` §1.

- **ECMAScript (JavaScript) — ECMA-262 / TC39** — *Language specification (standard)* — The standardized specification of the JavaScript language. Annual edition cycle; ECMAScript 2026 (17th edition) approved 2026-06-30. Adds: Temporal API (Stage 4, Mar 2026), `Math.sumPrecise`, `Iterator.concat`, `Array.fromAsync`, `Error.isError`, `Map`/`WeakMap` getOrInsert-style defaults, `Uint8Array` base64/hex methods, `JSON.parse` source-text reviver … — [https://tc39.es/ecma262/](https://tc39.es/ecma262/) — *Partially verified*
- **Temporal API** — *Standard library API (spec)* — Modern date/time API replacing `Date`: immutable types (`PlainDate`, `ZonedDateTime`, `Instant`, `Duration`, etc.), built-in time-zone and calendar support. Reached TC39 Stage 4 in March 2026; included in ES2026. Described by champion as the biggest addition to ECMAScript since ES2015. — [https://tc39.es/proposal-temporal/docs/](https://tc39.es/proposal-temporal/docs/) — *Partially verified*
- **TypeScript 7 (native Go compiler)** — *Programming language + compiler toolchain (CLI binary + language server)* — Typed superset of JavaScript. TypeScript 7.0 shipped GA 2026-07-08 as a methodical port of the compiler/language service from TypeScript to Go (project "tsgo", preview package `@typescript/native-preview`). Reported 8–12× faster full builds (~10× headline; VS Code repo ~125.7s→10.6s per Microsoft). Type-checking semantics intended identical to 6.x. … — [https://www.typescriptlang.org](https://www.typescriptlang.org) — *Partially verified*
- **WebAssembly (core spec — Wasm 3.0)** — *Binary instruction format + virtual machine specification (standard)* — Portable low-level bytecode executed in browsers and standalone runtimes. Wasm 3.0 completed 2025-09-17 as a rolling "live standard"; includes memory64, GC, exceptions, tail calls, function references, relaxed SIMD, extended-const, multi-memory. Threads (shared-everything) still unimplemented in Wasmtime 47 per 2026 reports. wasi-threads proposal withdrawn … — [https://webassembly.org](https://webassembly.org) — *Partially verified*
- **WASI (WebAssembly System Interface)** — *System interface specification (standard)* — Standardized capability-based syscall interface for Wasm outside the browser (files, clocks, sockets, HTTP). 0.1: POSIX-like, witx IDL. 0.2 (Jan 2024): rebuilt on Component Model with WIT, modular `wasi:cli`, `wasi:http`, `wasi:sockets`. 0.3.0 ratified 2026-06-11: async becomes native to the Component Model canonical ABI (`async func`, `stream<T>`, … — [https://wasi.dev](https://wasi.dev) — *Verified*
- **WebAssembly Component Model + WIT** — *Interface/ABI specification + IDL (standard)* — Higher-level composition layer over core Wasm modules: components with typed interfaces described in WIT, canonical ABI for cross-language calls, resource types with ownership, shared-nothing linking. Enables Rust/Go/Python/JS components to interoperate through shared WIT worlds. Formal standardization expected to begin after the 0.3/1.0 cycle (per 2026 … — [https://component-model.bytecodealliance.org](https://component-model.bytecodealliance.org) — *Partially verified*
- **AssemblyScript** — *Programming language + compiler (TypeScript-like → WebAssembly)* — A TypeScript-flavored language that compiles to WebAssembly (strict subset: no closures over heap GC types, explicit memory model). Used for Wasm modules authored by JS/TS developers. — [https://www.assemblyscript.org](https://www.assemblyscript.org) — *Partially verified*
- **Emscripten** — *Compiler toolchain (C/C++ → WebAssembly/JavaScript)* — LLVM-to-WebAssembly compiler producing Wasm + JS glue for browsers and Node. Powers Pyodide (CPython-in-Wasm), many game/codec ports, SQLite WASM builds. Emits Emscripten runtime with virtual FS, SDL/OpenGL shims. — [https://emscripten.org](https://emscripten.org) — *Partially verified*
- **wasm-bindgen** — *Library + CLI facilitating JS↔Wasm interop (Rust)* — Generates bindings between Rust-compiled Wasm and JavaScript: exposes Rust structs/functions to JS and imports JS APIs into Rust. Companion `wasm-pack` builds npm-publishable packages. — [https://github.com/wasm-bindgen/wasm-bindgen](https://github.com/wasm-bindgen/wasm-bindgen) — *Partially verified*
- **ECMA-402 (Intl API)** — *Internationalization API specification (standard)* — Standardizes `Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.Collator`, `Intl.PluralRules`, `Intl.Segmenter`, `Intl.Locale`, etc. Underpins all JS i18n libraries and `Intl`-based formatting. TC39 March 2026 meeting also advanced i18n features per Socket.dev. — [https://tc39.es/ecma402/](https://tc39.es/ecma402/) — *Partially verified*
- **WHATWG HTML Living Standard** — *Markup + platform API specification (living standard)* — The definitive HTML specification: elements, parsing, forms, canvas, media, web workers, storage, history, and dozens of JS APIs. Continuously updated ("living standard", no version numbers since 2011). WHATWG develops; W3C HTML WG endorses review drafts as Recommendations under an MoU. — [https://html.spec.whatwg.org/multipage/](https://html.spec.whatwg.org/multipage/) — *Verified*
- **WHATWG companion standards (DOM · Fetch · Streams · URL · Encoding · MIME · Infra · Web IDL)** — *Platform specifications (living standards)* — The modular specs behind the web platform: DOM (nodes, events, mutation observers — replaced W3C DOM L3), Fetch (requests/responses, CORS, `fetch()` API), Streams (backpressured byte/object streams underpinning fetch bodies, compression, WebTransport), URL (parsing), Encoding (UTF-8/legacy), MIME sniffing, Infra (shared algorithms), Web IDL (IDL for browser … — [https://dom.spec.whatwg.org](https://dom.spec.whatwg.org) — *Partially verified*
- **W3C CSS specifications (CSS Snapshot 2026)** — *Style specification suite (modular Recommendations)* — CSS is developed as independent modules (Selectors, Flexbox, Grid, Custom Properties, Nesting, Cascade Layers, Container Queries, etc.) progressing WD→CR→REC. CSS Snapshot 2026 collects the stable set. Process requires two independent implementations to exit Candidate Recommendation. — [https://www.w3.org/TR/css-2026/](https://www.w3.org/TR/css-2026/) — *Partially verified*
- **IETF QUIC + HTTP/3** — *Transport protocol standards (RFCs)* — QUIC: UDP-based multiplexed secure transport (TLS 1.3 integrated). HTTP/3: HTTP semantics over QUIC. Underpin WebTransport (HTTP/3 CONNECT) and modern CDN/edge delivery. Browsers support HTTP/3; Node 24+ exposes QUIC module (experimental track — not directly verified this session). — [https://www.rfc-editor.org/rfc/rfc9000.html](https://www.rfc-editor.org/rfc/rfc9000.html) — *Partially verified*
- **V8** — *JavaScript + WebAssembly engine (library/embedding)* — Google's high-performance JS engine: Ignition interpreter + Sparkplug baseline + TurboFan optimizing compiler (Maglev mid-tier in newer versions — not verified this session). Powers Chrome/Edge/Opera, Node.js, Deno, Cloudflare workerd. First shipped 2008; Wasm support since 2015. — [https://v8.dev](https://v8.dev) — *Partially verified*
- **SpiderMonkey** — *JavaScript + WebAssembly engine* — Mozilla's engine, the first-ever JavaScript engine (Brendan Eich, 1995). Powers Firefox/Gecko and WinterJS. Implements Warp (optimizing JIT), GC, Wasm. — [https://spidermonkey.dev](https://spidermonkey.dev) — *Partially verified*
- **JavaScriptCore (JSC)** — *JavaScript + WebAssembly engine* — Apple's engine powering Safari/WebKit and Bun. Multi-tier JIT (LLInt/baseline/DFG/FTL). Bun 1.4 discards JIT code after idle periods to cut resident memory (per 2026 Bun release notes). — [https://webkit.org](https://webkit.org) — *Partially verified*
- **Hermes** — *JavaScript engine optimized for mobile (ahead-of-time bytecode)* — Meta's JS engine for React Native: precompiles JS to bytecode at build time for fast startup and small memory on mobile. No JIT (interpreter). Used by React Native (default since RN 0.70) and by react-native-workers (separate Hermes runtime per worker thread). — [https://hermesengine.dev](https://hermesengine.dev) — *Partially verified*
- **QuickJS (+ quickjs-ng fork)** — *Small embeddable JavaScript engine (C)* — Tiny (~few hundred KB), fast-startup ES2023-capable interpreter in C. Bellard's upstream and the community quickjs-ng fork are diverging (both active; PRs traded occasionally). Powers LLRT (AWS Lambda runtime), txiki.js, and many embedded/plugin sandboxes. 28 CVEs noted in sandbox research (context, not a safety claim about current state). — [https://bellard.org/quickjs/](https://bellard.org/quickjs/) — *Partially verified*
- **Node.js 24 "Krypton" (Active LTS) / 26 (Current)** — *Server-side JavaScript runtime (application platform)* — V8 + libuv + Chromium-derived network stack. Node 24 (released 2025-05-06, Active LTS 2025-10-28, EOL 2028-04-30) is the 2026 production default: npm 11, stable permission model (`--allow-fs-read`, `--allow-net`, ...), stable type-stripping for TS, Undici 7 (30% faster fetch), newer V8. Node 22 "Jod" in Maintenance LTS until 2027-04-30. Node 26 is the last … — [https://nodejs.org](https://nodejs.org) — *Verified*
- **Bun** — *All-in-one JavaScript runtime + toolkit (runtime, bundler, package manager, test runner)* — JavaScriptCore-based runtime (originally Zig; experimental Zig→Rust rewrite in progress, ~99.8% test compat on Linux x64 per 2026 notes; production stays on current build). Acquired by Anthropic December 2025. Ships: runtime with `Bun.*` APIs (`Bun.serve`, `Bun.file`, `Bun.SQL` for Postgres/MySQL/SQLite, built-in Redis client), bundler, package manager … — [https://bun.sh](https://bun.sh) — *Partially verified*
- **Deno** — *Secure JavaScript/TypeScript/WebAssembly runtime + integrated toolchain* — V8 + Rust (Tokio) runtime, secure by default (explicit `--allow-read/net/env/run` permissions; never deploy `--allow-all`). Native TypeScript (type-checks; no config), built-in formatter/linter/test runner/`deno compile` (standalone executables), `deno outdated`/`--update`, workspaces. Deno 2: full npm compatibility (`npm:` specifiers, `package.json` … — [https://deno.com](https://deno.com) — *Partially verified*
- **workerd / Cloudflare Workers (runtime)** — *Edge serverless runtime (V8 isolates) + platform* — Open-source V8-isolate runtime behind Cloudflare Workers. Sub-millisecond cold starts; event-driven `fetch()` entry point (no listening sockets); bindings for KV, R2, D1 (SQLite), Durable Objects, Queues, Workers AI. `wrangler` CLI deploys; `miniflare`/`wrangler dev` local emulation. Python Workers run CPython-on-Wasm (Pyodide) inside isolates as GA-track … — [https://workers.cloudflare.com](https://workers.cloudflare.com) — *Partially verified*
- **LLRT (Low Latency Runtime)** — *Lightweight JavaScript runtime for AWS Lambda (QuickJS + Tokio + Rust)* — AWS Labs runtime optimized for Lambda cold starts: QuickJS engine, Rust core, small binary (~tens of MB). Implements a useful subset of Node/WHATWG APIs. Benchmark tables show it among the smallest/fastest-starting JS runtimes. — [https://github.com/awslabs/llrt](https://github.com/awslabs/llrt) — *Partially verified*
- **WinterJS** — *JavaScript edge/server runtime (SpiderMonkey + hyper + Rust)* — Wasmer's runtime built on SpiderMonkey ("Spiderfire") with Hyper HTTP, targeting WinterCG web-interoperable APIs. 1.0 claimed 58k req/s single-core in vendor-adjacent coverage. Cloudflare-Apps-compatible packaging story. — [https://github.com/wasmerio/winterjs](https://github.com/wasmerio/winterjs) — *Partially verified*
- **tsx** — *TypeScript/ESM executor CLI (esbuild-based)* — Runs `.ts`/`.tsx`/ESM directly with esbuild transform; `tsx watch` is the 2026 default TS dev-loop runner. Faster and simpler than ts-node; no loader flags; resolves `.js` specifiers in TS sources. — [https://github.com/privatenumber/tsx](https://github.com/privatenumber/tsx) — *Partially verified*
- **ts-node** — *TypeScript execution engine for Node.js (JIT transform + REPL)* — The long-standing TS runner (tsc-based transform, ESM loader). In 2026 it is legacy for new setups: the ESM loader broke on Node 20+ (empty-object loader error), prompting migrations to tsx or Node native type stripping. Still present in many repos. — [https://github.com/TypeStrong/ts-node](https://github.com/TypeStrong/ts-node) — *Partially verified*
- **amaro (Node.js type stripping)** — *TypeScript type-stripping transform library (SWC-based; powers Node's native TS support)* — Node's reference TS-stripping implementation: converts TS to JS by erasing types (no type checking). Used by Node 22.6+ `--experimental-strip-types` and stable type stripping in Node 24. Evaluated tsgo as an engine and rejected it ("not possible by design": tsgo lacks blank-spacing mode; Go runtime doesn't fit Node distribution) — will keep SWC for the … — [https://github.com/nodejs/amaro](https://github.com/nodejs/amaro) — *Partially verified*
- **Web Workers (dedicated) + SharedWorker + worklets** — *Browser platform APIs (standards)* — Dedicated workers: one-per-page background threads, no DOM, `postMessage` + structured clone / transferables. SharedWorker: one instance shared across same-origin tabs (Safari iOS <16 lacked support historically). Worklets: lightweight threads in the rendering/audio pipeline (PaintWorklet for custom CSS paint, AudioWorklet for audio DSP, AnimationWorklet). … — [https://html.spec.whatwg.org/multipage/workers.html](https://html.spec.whatwg.org/multipage/workers.html) — *Partially verified*
- **Service Workers + Cache Storage + Background Sync + Push** — *Browser platform APIs (standards)* — Origin-scoped programmable network proxy: intercepts fetch, enables offline-first caching strategies, push notifications (via Push API + Notification API), background sync. Event-driven lifecycle (install/activate/fetch/message); HTTPS-only; one registration per scope. Workbox (Google) is the dominant helper library (out of scope detail). — [https://w3c.github.io/ServiceWorker/](https://w3c.github.io/ServiceWorker/) — *Partially verified*
- **Web Components (Custom Elements · Shadow DOM · Declarative Shadow DOM · ElementInternals)** — *Browser platform APIs (standards)* — Framework-agnostic component model: `customElements.define`, shadow DOM encapsulation (slots, `::part`), HTML templates, and form-associated custom elements via `ElementInternals` (widely available since Mar 2023). Declarative Shadow DOM (`<template shadowrootmode="open|closed">`) reached Baseline "widely available" on 2026-08-20, enabling SSR without JS … — [https://html.spec.whatwg.org/multipage/custom-elements.html](https://html.spec.whatwg.org/multipage/custom-elements.html) — *Partially verified*
- **Browser storage suite (Web Storage · IndexedDB · Cache API · OPFS · Storage API)** — *Browser platform APIs (standards)* — localStorage/sessionStorage: ~5MB synchronous string KV (main thread only; not visible in service workers). IndexedDB: transactional object store, indexes/cursors, Blobs, GB-scale — verbose API (Dexie.js/`idb` wrappers popular). Cache API: Request/Response store for HTTP caching (service-worker-driven). OPFS (Origin Private File System): real file … — *Partially verified*
- **WebGPU** — *Browser platform API + shading language (standard)* — Modern GPU API (compute + render pipelines, WGSL shaders) mapping to D3D12/Metal/Vulkan via Dawn (Chromium) and wgpu (Firefox). Now ships in all major browsers: Chrome/Edge 113+ (2023), Safari 26 (June 2025), Firefox 141 Windows (July 2025)/145 macOS (Nov 2025). three.js r170+ has production WebGPURenderer (+TSL shader language, WebGL2 fallback); Babylon.js … — [https://www.w3.org/TR/webgpu/](https://www.w3.org/TR/webgpu/) — *Partially verified*
- **WebGL** — *Browser 3D graphics API (standard)* — OpenGL ES-based immediate-mode 3D API; WebGL2 is the stable workhorse renderer (three.js, Babylon, PlayCanvas default). WebGL1 contexts still universal. Being gradually succeeded by WebGPU for new high-end work but remains the compatibility baseline. — [https://www.khronos.org/webgl/](https://www.khronos.org/webgl/) — *Partially verified*
- **WebRTC** — *Realtime peer-to-peer communication APIs + protocols (standard)* — `RTCPeerConnection` (audio/video/data channels), `getUserMedia`, ICE/STUN/TURN NAT traversal, DTLS-SRTP encryption. Supported by all modern browsers (Chrome 28+, Firefox 22+, Safari 11+). SFU servers (LiveKit, mediasoup, Janus) scale it; 0.2–0.5s latency typical. Signaling is app-defined (WebSocket commonly). — [https://webrtc.org](https://webrtc.org) — *Partially verified*
- **WebSocket API + protocol (RFC 6455)** — *Full-duplex messaging protocol + browser API (standard)* — Bidirectional message protocol over a single TCP connection (ws/wss). Browser `WebSocket` API; Node libraries: `ws` (RFC-6455, fastest Node impl, passes Autobahn suite; server+client; optional bufferutil/utf-8-validate native addons), `uWebSockets.js`/`eiows`. Higher-level: Socket.IO 4.8.4 (Sept 2026) — event-based framework with … — [https://www.rfc-editor.org/rfc/rfc6455](https://www.rfc-editor.org/rfc/rfc6455) — *Verified*
- **WebTransport** — *Browser transport API (standard)* — QUIC-based transport: reliable streams + unreliable datagrams, bidirectional/unidirectional, connection migration (Wi-Fi→cellular). MDN marks it "Baseline 2026 — Newly available". Secure context (HTTPS) mandatory — limits local-dev/offline use. Positioned for cloud gaming, trading, low-latency streaming; NOT a wholesale WebSocket replacement per 2026 … — [https://www.w3.org/TR/webtransport/](https://www.w3.org/TR/webtransport/) — *Partially verified*
- **Fetch API / WHATWG Fetch (+ axios, ky, undici, redaxios)** — *Platform API (standard) + HTTP client libraries* — `fetch()` is the universal HTTP primitive (browsers + Node 18+ via undici, Deno, Bun, workers). undici is Node's built-in HTTP/1.1 client powering global fetch (Undici 7 in Node 24: ~30% faster). axios remains the most-used library (interceptors, defaults, wider compat); ky is a small fetch wrapper; redaxios is an 800-byte axios-API-compatible fetch wrapper … — [https://fetch.spec.whatwg.org/](https://fetch.spec.whatwg.org/) — *Partially verified*
- **WebCodecs** — *Low-level media codec API (standard)* — Direct access to browser audio/video encoders/decoders (`VideoDecoder`, `VideoEncoder`, `AudioDecoder`, `AudioEncoder`) for custom media pipelines without `<video>` overhead. Used by conferencing/streaming apps, cloud gaming, browser-based editors. — [https://www.w3.org/TR/webcodecs/](https://www.w3.org/TR/webcodecs/) — *Unverified*
- **WebAuthn** — *Authentication API (standard)* — Public-key credential API for passwordless auth (security keys, platform authenticators, passkeys). `navigator.credentials.create()/get()`. Server libraries verify attestation/assertion. — [https://www.w3.org/TR/webauthn-3/](https://www.w3.org/TR/webauthn-3/) — *Unverified*
- **File System Access API (+ File API)** — *Browser API for user-visible files (standard-track)* — `showOpenFilePicker`/`showSaveFilePicker`/`showDirectoryPicker` give web apps read/write access to user-chosen files with permission prompts. Chrome/Edge only for pickers; Safari/Firefox support the underlying OPFS portions. Portable fallback: `<input type=file>` + drag-drop. — [https://wicg.github.io/file-system-access/](https://wicg.github.io/file-system-access/) — *Partially verified*
- **Constraint Validation API (HTML forms)** — *Built-in browser validation API (standard)* — Native form validation: `required`, `pattern`, `min/max`, `type=email|url`, `setCustomValidity()`, `checkValidity()`, `reportValidity()`, `:valid`/`:invalid` CSS pseudo-classes, `validationMessage` localization. Works without JS; enhanced with JS. — [https://html.spec.whatwg.org/multipage/form-control-infrastructure.html](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html) — *Partially verified*
- **Notifications API (+ VAPID Web Push)** — *System notification + push messaging standards* — `Notification` API shows system notifications (permission-gated); Web Push delivers them from servers via push services (VAPID keys) to service workers even when the page is closed. — [https://notifications.spec.whatwg.org/](https://notifications.spec.whatwg.org/) — *Partially verified*
- **WCAG (Web Content Accessibility Guidelines)** — *Accessibility standard/guidelines* — The normative accessibility requirements for web content, organized A/AA/AAA. WCAG 2.2 added 9 criteria: 2.4.11 Focus Not Obscured, 2.5.7 Dragging Movements, 2.5.8 Target Size (Minimum 24×24 CSS px), 3.2.6 Consistent Help, 3.3.7 Redundant Entry, 3.3.8 Accessible Authentication, 2.4.12/2.4.13 Focus Appearance (AAA), 4.1.1 removed. WCAG 2.2 AA is the 2026 … — [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/) — *Partially verified*
- **ARIA (Accessible Rich Internet Applications)** — *Accessibility semantics specification* — Roles, states, and properties that expose UI semantics to assistive tech (`role=dialog`, `aria-expanded`, `aria-live`, etc.). Rule #1: prefer native HTML semantics; ARIA fills gaps. axe-core rules heavily target ARIA misuse. — [https://www.w3.org/TR/wai-aria-1.2/](https://www.w3.org/TR/wai-aria-1.2/) — *Partially verified*
- **axe-core** — *Accessibility testing engine (library + CLI)* — The industry-standard automated a11y engine (~15k+ GitHub stars per 2026 index; MPL-2.0). Rule tags map to WCAG levels (`wcag2a`, `wcag2aa`, `wcag21aa`, `wcag22aa`). Powers Google Lighthouse a11y audits, Microsoft Accessibility Insights, `@axe-core/playwright`, `@axe-core/cli`, `jest-axe`. Deque claims ~57% of violations detectable automatically (per agent … — [https://github.com/dequelabs/axe-core](https://github.com/dequelabs/axe-core) — *Partially verified*
- **Lighthouse (accessibility auditing)** — *Automated page-audit tool (CLI + DevTools + CI)* — Audits pages across performance, accessibility, best practices, SEO. Accessibility category is axe-core-powered. Used via Chrome DevTools, `npx lighthouse --only-categories=accessibility`, and LHCI (`@lhci/cli`) in CI with budgets/assertions. — [https://github.com/GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) — *Partially verified*
- **pa11y (+ pa11y-ci)** — *CLI accessibility testing tool (CI-focused)* — Command-line a11y tester with multiple runners (default `htmlcs`/HTML_CodeSniffer — WCAG 2.0-era; `--runner axe` for axe-core-backed WCAG 2.1/2.2 coverage), multiple reporters, `pa11y-ci` for sweeping URL lists in CI. ~4.5k stars, LGPL-3.0 per 2026 index. Note: pa11y's `WCAG2AA` standard maps only to wcag2a/wcag21a/wcag2aa/wcag21aa axe tags — no 2.2 … — [https://github.com/pa11y/pa11y](https://github.com/pa11y/pa11y) — *Partially verified*
- **WAVE (WebAIM)** — *Visual accessibility evaluation tool (browser extension + online)* — Injects visual feedback icons directly onto the page (errors, alerts, features, structural elements, ARIA). Browser extensions + online tester + API. Complements engine-based tools with human-readable visual overlay. — [https://wave.webaim.org](https://wave.webaim.org) — *Partially verified*
- **eslint-plugin-jsx-a11y** — *ESLint plugin (static lint rules)* — Lint-time a11y rules for JSX: missing `alt`, click handlers without keyboard equivalents, missing label associations, ARIA prop validity, etc. Standard in the 2026 a11y toolchain (ESLint flat config: `plugins: {"jsx-a11y": jsxA11y}`, `rules: jsxA11y.configs.recommended.rules`). Also consumable via oxlint's `jsx-a11y` plugin (oxlint 1.x includes jsx-a11y … — [https://github.com/jsx-eslint/eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y) — *Partially verified*
- **Screen readers (NVDA · JAWS · VoiceOver · TalkBack · Orca)** — *Assistive technology (manual testing tools)* — The manual-testing half of a11y: NVDA (free, Windows), JAWS (commercial, Windows), VoiceOver (built-in macOS/iOS), TalkBack (Android), Orca (Linux). 2026 audit guides prescribe minimum matrix: NVDA+Firefox (Win), VoiceOver+Safari (Mac/iOS); full matrix adds JAWS+Chrome, TalkBack+Chrome. Verify names/roles/states announcement, landmarks, aria-live, focus … — [https://www.nvaccess.org](https://www.nvaccess.org) — *Partially verified*
- **Nu HTML Checker (validator.w3.org/nu)** — *Markup validation service + CLI/JAR* — The official HTML conformance checker: validates documents against the HTML Living Standard (+ ARIA in HTML rules). Available as hosted service, `vnu.jar` CLI, and Docker image for CI. — [https://validator.w3.org/nu/](https://validator.w3.org/nu/) — *Unverified*
- **Unicode CLDR + ICU + BCP 47** — *Locale data + libraries + tag standard* — CLDR is the canonical locale dataset (date/number formats, plurals, territories) consumed by ECMA-402 implementations, ICU4X/ICU4C/ICU4J libraries, and OSes. BCP 47 defines language tags (`en-US`, `pt-BR`, `zh-Hant-TW`). i18n libraries ultimately format via `Intl` (CLDR-backed) or ICU MessageFormat. — [https://cldr.unicode.org](https://cldr.unicode.org) — *Partially verified*
- **i18next (+ react-i18next)** — *Internationalization framework (library)* — The most widely used JS i18n framework: translation function `t()`, namespaces, plurals, interpolation, language detection, backend connectors (HTTP, FS), ecosystem (react-i18next, next-i18next, ICU plugin `i18next-icu`). Own interpolation/plural format by default (ICU via plugin). Tolgee provides an i18next bridge (`@tolgee/i18next`) for in-context editing. — [https://www.i18next.com](https://www.i18next.com) — *Partially verified*
- **FormatJS (react-intl)** — *ICU MessageFormat i18n library suite* — Yahoo/Verizon-originated suite built on ICU MessageFormat: `react-intl` components/hooks, `@formatjs/cli` for message extraction, ESLint plugin. Heavier compile step than i18next but standards-based message syntax shared with Java/PHP ecosystems. — [https://formatjs.github.io](https://formatjs.github.io) — *Partially verified*
- **Lingui** — *i18n library + message extraction CLI (compile-time catalogs)* — Lightweight (~3kb core claim) i18n with ICU MessageFormat, build-time message extraction (`lingui extract`), catalog validation, React/Vue bindings, `eslint-plugin-lingui`. v6.x line in 2026 (`@lingui/core@6.6.0` referenced). Uses source text as key by default (editing English invalidates translations — noted as a rejection reason in one ADR). Works in any … — [https://lingui.dev](https://lingui.dev) — *Partially verified*
- **Tolgee** — *Open-source localization platform + in-context JS SDKs* — Self-hostable translation management with in-context editing: translators edit strings directly in the running app (invisible-text key marking), screenshots, machine-translation pre-fill. JS SDKs (`@tolgee/react`, `@tolgee/i18next` bridge, `@tolgee/ui`). OSS (Apache-2.0 per 2026 listings). Positioned as the OSS alternative to Lokalise/Phrase/Crowdin for … — [https://tolgee.io](https://tolgee.io) — *Partially verified*
- **next-intl** — *Next.js-focused i18n library (ICU MessageFormat)* — The trendiest Next.js i18n option in 2026 (`next-intl@4.14.2` referenced): App Router integration, `useTranslations`, `setRequestLocale()`, ICU messages. Critiques in 2026 benchmark: heavier client bundle (~14.7kb provider+hook), static-rendering pitfalls with namespaced dictionaries, optimization complexity. — [https://next-intl.dev](https://next-intl.dev) — *Partially verified*

*58 records in this category.*

## Build, compile, and package tooling

Package managers, runtimes, bundlers, compilers, linters, monorepo and release tooling. Source: `catalogs/01a-languages-build.md` §2. (CI/CD platforms themselves: see B5 §18.)

- **npm** — *Package manager CLI + client for the npm registry* — The default JS package manager, bundled with Node.js. v11: faster installs, `package-lock.json` lockfile, workspaces, `npm audit`, `npm outdated/update`, `npx`. npm 11.19+ skips dependency install scripts by default (allowScripts allowlist) — supply-chain hardening that broke some postinstall flows in 2026 upgrades. — [https://www.npmjs.com](https://www.npmjs.com) — *Partially verified*
- **pnpm** — *Fast, disk-efficient package manager (content-addressable store + hard links)* — Stores each package version once in a global content-addressable store, hard-linking into projects — massive disk savings and fast installs (~28s cold / 6s warm Next.js in 2026 comparison). Strict non-flat `node_modules` prevents phantom dependencies. pnpm 10+: `manage-package-manager-versions` on by default (auto-switches to the `packageManager`-pinned … — [https://pnpm.io](https://pnpm.io) — *Partially verified*
- **Yarn (Classic 1.x + Berry 2/3/4)** — *Package manager — two distinct generations* — Yarn Classic 1.22: the 2016 original; maintenance/security-patches-only since 2020 — "a museum piece that runs your build" (2026 commentary). Yarn Berry (v2–v4, current 4.x): complete rewrite with Plug'n'Play (no node_modules; `.pnp.cjs` loader), zero-installs (check in `.yarn/cache`), constraints, plugin system, `yarn.lock`. Strongest for large enterprise … — [https://yarnpkg.com](https://yarnpkg.com) — *Partially verified*
- **Bun (package manager)** — *Package manager (subcommand of Bun runtime)* — Native-speed installer (fastest in 2026 comparisons: ~8s cold / 2s warm Next.js): global module cache, binary lockfile `bun.lockb` (text `bun.lock` also supported), `bunx` runner, `trustedDependencies` install-script allowlist, isolated installs option, accepts pnpm `catalog:` in overrides. Primary choice for greenfield speed; lockfile differs from npm/pnpm. — [https://bun.sh/docs/installation](https://bun.sh/docs/installation) — *Partially verified*
- **Corepack** — *Package-manager version manager/shim (experimental)* — Ships with Node; activates the exact package manager + version from `packageManager` in package.json (`corepack enable`, `corepack use`). 2026 status: still experimental in Node 24; REMOVED in Node 25+ (per 2026 workflow docs); pnpm 10+ self-manages versions via `manage-package-manager-versions`, reducing Corepack's role. — [https://github.com/nodejs/corepack](https://github.com/nodejs/corepack) — *Partially verified*
- **Volta (status: stood down)** — *JavaScript toolchain version manager (Node/npm/Yarn/pnpm pinning)* — Pinned Node + package-manager versions per project via `volta` key in package.json, with transparent shims (no shell hook). 2026 status: maintainers have stood the project down; mise is the recommended successor (per techearl 2026 guide). pnpm support stayed experimental behind `VOLTA_FEATURE_PNPM=1`. — [https://volta.sh](https://volta.sh) — *Partially verified*
- **fnm** — *Node.js version manager (Rust)* — Rust rewrite of nvm's model: fast shell startup, `.nvmrc`/`.node-version` support, `--use-on-cd` auto-switching, Windows support, `--corepack-enabled` flag. 2026 verdict across guides: "fnm for a personal machine, mise for a team monorepo." — [https://github.com/Schniz/fnm](https://github.com/Schniz/fnm) — *Partially verified*
- **mise (mise-en-place)** — *Polyglot runtime version manager (Rust; asdf successor)* — Manages Node, Python, Go, Rust, etc. versions per project (`mise.toml`/`.node-version`/`.tool-versions`); Volta's recommended successor; 2026 team-monorepo default ("mise for a team monorepo"). Also handles env vars and tasks. — [https://mise.jdx.dev](https://mise.jdx.dev) — *Partially verified*
- **nvm (+ nvm.fish, n)** — *Node.js version manager (bash script)* — The most widely documented Node version manager: bash script shimming node/npm/npx; `.nvmrc` per-project; manual `nvm use`. Slow shell startup (subshell per cd hook) vs fnm/mise. `n` (tj/n) is a simpler no-hook alternative; nvm.fish is a Fish port. — [https://github.com/nvm-sh/nvm](https://github.com/nvm-sh/nvm) — *Partially verified*
- **uv** — *Python package + project manager (Rust, single binary)* — Astral's Rust tool consolidating venv creation + resolution + locking + install + Python-version management + tool running (`uv tool install` ≈ pipx) + build/publish. 10–100× faster than pip (parallel resolver, global cache). `uv.lock` committed; `uv sync --frozen` for reproducible installs; PEP 621/735-native `pyproject.toml`; `uv python install 3.14` (own … — [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/) — *Partially verified*
- **pip** — *Python package installer (baseline)* — The default installer since 2011: installs from PyPI, no venv/lockfile/version management of its own (paired with `venv`, `pyenv`, `pip-tools`). Still the universal baseline; `requirements.txt` interop target (`uv export` generates it). — [https://pip.pypa.io](https://pip.pypa.io) — *Partially verified*
- **Poetry** — *Python dependency management + packaging/publishing* — Mature (pre-uv default) tool bundling dependency resolution, venvs, `poetry.lock`, and PyPI publishing. Historically used its own `[tool.poetry]` pyproject table (PEP 621 support added later). 2026 verdict: mature but slower resolver; overkill for applications; losing new-project share to uv. — [https://python-poetry.org](https://python-poetry.org) — *Partially verified*
- **PDM** — *PEP-582/621-native Python package manager* — Standards-compliant manager (PEP 621 project metadata, PEP 582 `__pypackages__` local packages dir), `pdm.lock` lockfile. "Good but less community momentum" vs uv in 2026 ADRs; still viable for standards-purist teams. — [https://pdm-project.org](https://pdm-project.org) — *Partially verified*
- **Hatch** — *Python project manager + build backend (PyPA)* — PyPA's project manager: environments (`hatch env`), versioning, build backend (`hatchling`), publishing. Matrix-based env management is its distinctive strength. Listed among viable alternatives in 2026 uv ADRs. — [https://hatch.pypa.io](https://hatch.pypa.io) — *Partially verified*
- **pipx** — *Isolated Python CLI-app installer* — Installs Python CLI tools into isolated venvs and exposes their binaries (`pipx install black`). The use case uv now covers with `uv tool install`; pipx remains the PyPA-standard standalone option. — [https://pipx.pypa.io](https://pipx.pypa.io) — *Partially verified*
- **Rye (Archived / deprecated)** — *Python project manager (unified experience) — DEPRECATED* — Armin Ronacher's "hassle-free Python experience": unified Python installs, pyproject projects, venvs, global tools. Astral (which hired/adopted it) officially discontinued it: "Rye is no longer developed... use uv, the successor project." Migration guide published; no further updates including security updates. — [https://github.com/astral-sh/rye](https://github.com/astral-sh/rye) — *Verified*
- **npm registry (npmjs.com)** — *Package registry (default for JS)* — The canonical JS package registry (millions of packages). All JS package managers resolve against it (or mirrors). Supports provenance attestations, trusted publishing (OIDC), deprecation, two-factor auth. Supply-chain incidents (e.g., March 2026 axios maintainer-account hijack publishing a backdoor within 40 minutes, no CVE at the time) drive 2026 … — [https://www.npmjs.com](https://www.npmjs.com) — *Partially verified*
- **JSR (JavaScript Registry)** — *TypeScript-native package registry* — Deno's TS-first registry: publish TypeScript source directly (no build step); "slow types" constraint (explicit export types) enables instant docs/type generation; ESM-only; cross-runtime (Deno, Node, Bun, browsers via publishing to npm compat layer); Sigstore transparency log + GitHub Actions OIDC provenance built in from day one. Hosts Deno's `@std` … — [https://jsr.io](https://jsr.io) — *Partially verified*
- **esm.sh** — *No-build ESM CDN (npm/JSR/GitHub → browser-native ES modules)* — Import npm/JSR/GitHub packages as ES modules via URL with zero build step: `import React from "https://esm.sh/react@19.2.4"`; CJS→ESM transform, deep subpath exports, `?dev`/`?bundle` modes, TypeScript type headers (`X-TypeScript-Types`), import-map friendly. Registries: `/` npm, `/jsr/`, `/gh/`, `/pr/` (pkg.pr.new). Best "browser-native ESM resolver" in … — [https://esm.sh](https://esm.sh) — *Partially verified*
- **jsDelivr** — *Public CDN for npm (+ GitHub, WordPress)* — Multi-CDN (DNS steering + health checks) serving npm packages, GitHub tags, WP plugins; `+esm` on-demand ESM; version resolution API (`data.jsdelivr.com/v1/packages/npm/<name>/resolved`); immutable 1-year caching on pinned versions; published SRI hashes; Brotli + optional minify. 2026 benchmark: P50 18ms / P95 55ms global TTFB; 99.99% trailing availability … — [https://www.jsdelivr.com](https://www.jsdelivr.com) — *Partially verified*
- **unpkg** — *npm CDN (convenience layer)* — Serves any npm package file via URL (`unpkg.com/pkg@version/file`). Single-provider fronting a small origin; cold paths can hit the live npm registry (P95 140ms in 2026 benchmark — worst tail of the three). Immutable 1-year caching on pinned versions; no published SRI hashes (compute yourself). 2026 verdict: convenience for READMEs/CodePen, not for … — [https://unpkg.com](https://unpkg.com) — *Partially verified*
- **cdnjs** — *Curated public CDN (~4k libraries allowlist)* — Cloudflare-hosted CDN with human-curated allowlist (~4,000 libraries); publishes SRI hashes per asset; pre-minified Brotli assets; 1-year immutable caching; static object-store origin. Safest choice when you need a handful of famous libraries with verifiable hashes; cannot serve arbitrary npm packages (requires submission PR). — [https://cdnjs.com](https://cdnjs.com) — *Partially verified*
- **Vite** — *Frontend build tool (dev server + production bundler) + plugin ecosystem* — The default frontend build tool in 2026 (~65M weekly downloads per Vite 8 announcement; ~132M in one third-party table — treat exact numbers as reported). Vite 8 is the biggest architectural change since Vite 2: esbuild+Rollup replaced by a single unified Rust bundler, Rolldown, with full Rollup plugin compatibility; Oxc replaces esbuild for transforms … — [https://vite.dev](https://vite.dev) — *Verified*
- **Rolldown** — *JavaScript/TypeScript bundler (Rust, Rollup-compatible API)* — VoidZero's Rust bundler: Rollup-compatible plugin interface with esbuild-like scope; intended as the future bundler of Vite (achieved in Vite 8). Uses Oxc for parsing/transform/minify; napi-rs Node bindings; ships per-platform npm binaries (+ wasm32-wasi). 13,968 stars, MIT. Benchmarks: 8–30× faster than Rollup on production builds (variance by project). — [https://rolldown.rs](https://rolldown.rs) — *Verified*
- **webpack (+ webpack-dev-server)** — *Module bundler (JS) + dev server* — The decade-dominant bundler (loaders + plugins, code splitting, federation). In 2026: mature/maintenance posture; 41M weekly downloads (still huge installed base); even webpack 5.97-era docs point migrators at Rspack. webpack-dev-server provides HMR dev serving. No webpack 6 announced in sources surveyed. — [https://webpack.js.org](https://webpack.js.org) — *Partially verified*
- **Rspack** — *Rust bundler with webpack API/config compatibility* — ByteDance/WebInfra's Rust bundler prioritizing webpack compatibility (~95% config reuse claimed) over raw speed: the lowest-friction upgrade for legacy webpack codebases; webpack loaders/plugins largely work. ~6M weekly downloads. Rsbuild is its Vite-like wrapper (out of scope detail). — [https://rspack.rs](https://rspack.rs) — *Partially verified*
- **Turbopack** — *Incremental Rust bundler (Next.js-only distribution)* — Vercel's Rust bundler, default in Next.js 16 (Oct 2025): incremental architecture caching to function level with persistent disk cache; 5–10× faster Fast Refresh, 2–5× faster builds (vendor claims). Cannot be adopted standalone — no Vue/Svelte/standalone usage; Next.js docs retain a "Using Webpack instead" escape hatch. Shipped as part of Next.js (MIT). — [https://nextjs.org/docs/app/api-reference/turbopack](https://nextjs.org/docs/app/api-reference/turbopack) — *Partially verified*
- **Rollup** — *ES module bundler (JS; native Rust port in progress as rollup@5/swc-line — see note)* — The ESM-focused library bundler whose plugin API became the ecosystem standard (Vite, tsdown, unbuild all speak it). In 2026, production-bundling mindshare moved to Rolldown (its API-compatible Rust successor); Rollup itself continues for compatibility. Note: Rollup 5 development explored native bindings; exact 2026 version not pinned in sources — record … — [https://rollupjs.org](https://rollupjs.org) — *Partially verified*
- **esbuild** — *Extremely fast JS/TS/CSS bundler + transformer (Go)* — Evan Wallace's Go bundler: still the fastest TS→JS transform and ubiquitous as a library inside other tools (tsx, tsup historically, test runners, CLIs, Lambda packaging). 201M weekly downloads. "Didn't lose — moved": no longer the app assembler of choice (Vite 8 dropped it), but the transform layer everywhere. Deliberately narrow plugin API (no full AST) … — [https://esbuild.github.io](https://esbuild.github.io) — *Partially verified*
- **Parcel** — *Zero-config web application bundler (Rust core + JS)* — Zero-config bundler (HTML entry, auto transforms); v2 rewrote core in Rust. Niche in 2026 vs Vite/Next dominance but maintained; valued for no-config setups. — [https://parceljs.org](https://parceljs.org) — *Unverified*
- **Farm** — *Rust-based web build tool (Vite-compatible plugin API)* — Rust bundler claiming Vite plugin compatibility with faster cold starts via lazy compilation. Community-driven; smaller adoption than Rspack/Rolldown. — [https://farmfe.org](https://farmfe.org) — *Unverified*
- **tsdown** — *TypeScript library bundler (Rolldown + Oxc powered; tsup successor)* — "The elegant bundler for libraries powered by Rolldown": drop-in tsup replacement with compatible options; ESM/CJS/IIFE outputs, `.d.ts` via Oxc isolated-declarations, unbundle mode, watch mode, CSS pipeline (Lightning CSS/PostCSS/CSS modules), WASM support, shims, publint+attw package validation built in (`publint: 'ci-only'`), executable bundling … — [https://tsdown.dev](https://tsdown.dev) — *Partially verified*
- **tsup (maintenance mode — use tsdown)** — *TypeScript library bundler (esbuild-powered) — NOT ACTIVELY MAINTAINED* — "Bundle your TypeScript library with no config, powered by esbuild" (MIT © EGOIST). The README now carries an explicit warning: "This project is not actively maintained anymore. Please consider using tsdown instead" (+ migration guide). Still widely present in older repos. — [https://github.com/egoist/tsup](https://github.com/egoist/tsup) — *Verified*
- **unbuild** — *Library build tool (Rollup-based, auto config)* — UnJS's "zero-config" library builder: auto-detects entries/exports, Rollup under the hood, DTS rollup. Recommended in 2026 skill docs "for complex cases" where tsdown's conventions don't fit. Used across the UnJS/Nuxt ecosystem. — [https://github.com/unjs/unbuild](https://github.com/unjs/unbuild) — *Partially verified*
- **pkgroll** — *Minimalist package bundler (distributes via package.json `exports`)* — Builds packages straight from `package.json` exports map (no config file): ESM/CJS/DTS, targeting privatenumber's minimal-tooling philosophy. Niche but respected for tiny libs. — [https://github.com/privatenumber/pkgroll](https://github.com/privatenumber/pkgroll) — *Unverified*
- **dnt (Deno to Node Transform)** — *Deno→npm package build tool* — Builds npm-compatible packages from Deno-first TypeScript sources: transforms Deno specifiers, generates package.json, shims. The bridge for publishing Deno-authored libs to npm. — [https://github.com/denoland/dnt](https://github.com/denoland/dnt) — *Unverified*
- **Babel** — *JavaScript compiler/transform pipeline (plugins + presets)* — The original pluggable JS transform toolchain (2014–): parses with `@babel/parser`, transforms via plugins/presets (`@babel/preset-env`, `-typescript`, `-react`), generates code. In 2026 still the compat fallback (Babel 7 docs referenced in Vite 8 migration for transform plugins that don't support Oxc); preset-env + browserslist remains the legacy-targeting … — [https://babeljs.io](https://babeljs.io) — *Partially verified*
- **SWC** — *JS/TS compiler platform (Rust): transform, minify, bundle, plugins (WASM)* — Rust-based compiler used in production at scale (Next.js Turbopack-era transforms, Deno historically, many CLIs). 2026 status: "production-proven default"; Deno is migrating transform workloads to Oxc; still the plugin-capable choice (WASM plugins) where Oxc's API is narrower. Also offers minification and (historical) bundling. — [https://swc.rs](https://swc.rs) — *Partially verified*
- **Sucrase** — *Fast JS/TS/JSX dev transform (JS, single-pass)* — "Super-fast" single-pass transforms for dev (no type checking, scope-limited transforms). Historically used by Jest-adjacent tooling and older dev servers; largely superseded by esbuild/Oxc but still embedded in places. — [https://sucrase.io](https://sucrase.io) — *Unverified*
- **Lightning CSS** — *CSS parser/transformer/bundler/minifier (Rust)* — Rust CSS toolchain: parsing, nesting lowering, custom-media, logical properties, `color-mix`, modules scoping, minification — with proper browser-target handling (browserslist). Adopted as Vite 8's CSS minifier (replacing esbuild) and inside tsdown's CSS pipeline. The 2026 default for serious CSS builds. — [https://lightningcss.dev](https://lightningcss.dev) — *Partially verified*
- **PostCSS** — *CSS transformation framework (plugin pipeline)* — The plugin API through which most CSS transforms run (autoprefixer, postcss-preset-env, cssnano historically, Tailwind v3). Vite still supports PostCSS config; Tailwind v4 replaced the PostCSS plugin with a native Vite plugin (PostCSS integration remains for non-Vite builds). Stable/mature in 2026. — [https://postcss.org](https://postcss.org) — *Partially verified*
- **Tailwind CSS** — *Utility-first CSS framework with Rust compiler (v4)* — v4 rewrote the engine: CSS-first configuration (`@theme` in CSS replaces `tailwind.config.js`), Rust-powered compiler (~5× faster builds), native Vite plugin, automatic content detection, modern CSS features (cascade layers, `@property`, container queries). The dominant styling approach in 2026 greenfield work; v3 (PostCSS plugin) still in maintenance. — [https://tailwindcss.com](https://tailwindcss.com) — *Partially verified*
- **Dart Sass** — *CSS preprocessor (Dart implementation; JS API via `sass` npm package)* — The canonical Sass/SCSS implementation after LibSass/node-sass deprecation: `@use`/`@forward` module system, built-in modules (`sass:color`, `sass:math`), compiled to JS for the `sass` npm package (plus Dart VM native). Still standard in design-system codebases and Angular (which bundles Sass). — [https://sass-lang.com](https://sass-lang.com) — *Unverified*
- **typescript-eslint (tseslint)** — *TypeScript ESLint tooling (parser + plugin + configs)* — The standard bridge making ESLint understand TS: typed linting via type-aware rules (`recommended-type-checked`), project service, `tseslint.config()` flat-config helper. v8 line current in 2026; pairs with ESLint 10. — [https://typescript-eslint.io](https://typescript-eslint.io) — *Partially verified*
- **mypy + pyright (Python type checking)** — *Static type checkers for Python* — The two dominant Python checkers: mypy (the reference implementation, plugin/daemon `dmypy`) and pyright (Microsoft's Node-based checker, faster, powers Pylance; community fork basedpyright). 2026: type-annotated Python is standard in typed codebases; `ty` (Astral's Rust checker, in preview) is the emerging third option — recorded here as emerging, not … — [https://mypy-lang.org](https://mypy-lang.org) — *Unverified*
- **publint** — *npm package correctness linter* — Lints packed npm tarballs for publishing mistakes (missing files, broken exports, ESM/CJS mismatches). Built into tsdown (`publint: 'ci-only'`) as a release gate. — [https://publint.dev](https://publint.dev) — *Partially verified*
- **attw (Are The Types Wrong)** — *TypeScript package types-resolution checker* — Analyzes a package's published types under multiple module-resolution modes (node10/node16/bundler) and reports resolution failures. Paired with publint in tsdown release gates. — [https://arethetypeswrong.github.io](https://arethetypeswrong.github.io) — *Partially verified*
- **ESLint** — *JavaScript/TypeScript linter (pluggable rules)* — The long-standard JS linter; v9+ moved to flat config (`eslint.config.js`) and v10 continues it. The choice when the ecosystem's plugin universe is needed (framework plugins, `eslint-plugin-jsx-a11y`, import sorting, security rules). Slower than Rust linters; "ESLint's slowness is its biggest remaining tax" in 2026 analyses. — [https://eslint.org](https://eslint.org) — *Partially verified*
- **Biome** — *All-in-one JS/TS linter + formatter (Rust)* — Single binary replacing ESLint+Prettier for many teams: formatter (Prettier-compatible-ish), linter with 300+ rules, import organizer, `biome check`, `biome migrate`. 25,912 stars, MIT. v2 continues the "one tool" push. Trade-off: rule coverage narrower than ESLint's plugin universe; Prettier-parity edge cases remain. — [https://biomejs.dev](https://biomejs.dev) — *Verified*
- **oxlint + oxfmt (+ Vite+ unified CLI)** — *Rust linter/formatter (part of Oxc toolchain)* — oxlint: ESLint-compatible Rust linter (1.x line; hundreds of rules, ESLint-plugin compat layer growing). oxfmt: new Rust formatter challenging Prettier/Biome. Vite+ (vite-plus): unified CLI combining Oxc's toolchain — the "one binary" answer from the Oxc/Vite side. Positioned as the speed-max choice; ecosystem rule parity still catching up. — [https://oxc.rs](https://oxc.rs) — *Partially verified*
- **Prettier** — *Opinionated code formatter (JS/TS/CSS/HTML/JSON/Markdown/YAML...)* — The de-facto formatter: zero-config opinionated output, editor/CI integration, `.prettierrc`. Still the formatting baseline even where Biome/oxfmt compete; pairs with ESLint (format) or typescript-eslint. v3 line current. — [https://prettier.io](https://prettier.io) — *Partially verified*
- **dprint** — *Pluggable multi-language formatter (Rust core, WASM plugins)* — Rust formatting host with WASM plugins per language (TS, JSON, Markdown, TOML, etc.); config-driven, fast, popular in Deno-adjacent and polyglot setups. — [https://dprint.dev](https://dprint.dev) — *Unverified*
- **Ruff** — *Python linter + formatter (Rust; ESLint/Black replacement)* — Astral's Rust tool consolidating Python linting (pyflakes/pycodestyle/isort/flake8 plugins → 800+ rules) and formatting (Black-compatible). The default Python lint/format choice in 2026; pairs with uv in the Astral stack. — [https://docs.astral.sh/ruff/](https://docs.astral.sh/ruff/) — *Partially verified*
- **Stylelint** — *CSS/SCSS linter* — The CSS linter: 170+ rules, sharable configs (`stylelint-config-standard`), SCSS/Less support via custom syntax. Relevant wherever design systems enforce CSS conventions; Tailwind v4 era reduced but didn't eliminate its role. — [https://stylelint.io](https://stylelint.io) — *Unverified*
- **HTMLHint** — *HTML linter* — Static analysis for HTML (tag pairing, attribute rules, inline config comments). Lightweight; used in static-site pipelines. — [https://htmlhint.com](https://htmlhint.com) — *Unverified*
- **markdownlint** — *Markdown linter* — Style enforcement for Markdown docs (line length, heading increments, fenced code languages). Common in docs-heavy repos and atlas-adjacent documentation workflows. — [https://github.com/DavidAnson/markdownlint](https://github.com/DavidAnson/markdownlint) — *Unverified*
- **commitlint (+ Conventional Commits)** — *Commit-message linter (Conventional Commits)* — Enforces Conventional Commits (`feat:`, `fix:`, scopes) at commit time (with Husky/Lefthook hooks); feeds changesets/semantic-release versioning. — [https://commitlint.js.org](https://commitlint.js.org) — *Unverified*
- **cspell** — *Code spell checker* — Spell-checks identifiers, comments, and docs with project dictionaries; CI-friendly. Common in large repos and docs pipelines. — [https://cspell.org](https://cspell.org) — *Unverified*
- **EditorConfig** — *Cross-editor whitespace/style convention (spec + plugins)* — `.editorconfig` declares indent style/size, EOL, charset, trailing-whitespace rules honored by editors natively or via plugins. Not a linter — the baseline every formatter config assumes. — [https://editorconfig.org](https://editorconfig.org) — *Unverified*
- **Orval** — *TypeScript client generator from OpenAPI specs* — Generates type-safe TS clients (fetch/axios hooks) plus Zod schemas, React Query/SWR hooks, and MSW mocks from OpenAPI 3.x. v8 (2026): framework hooks for Angular/Vue/Solid/Svelte, fetch-client improvements. The favored TS-first OpenAPI client generator in 2026 React/TS stacks. — [https://orval.dev](https://orval.dev) — *Partially verified*
- **openapi-typescript** — *OpenAPI → TypeScript types generator (types only, no client)* — Generates pure TS types from OpenAPI schemas (no runtime client — pair with `openapi-fetch`, now in maintenance mode, or any fetch wrapper). v8: "the fastest and lightest way to get types"; schema-object output. Preferred when you want types without a client framework. — [https://openapi-ts.dev](https://openapi-ts.dev) — *Partially verified*
- **Hey API** — *OpenAPI → TypeScript client generator (plugin-based)* — Plugin-architecture TS client generator (formerly openapi-typescript-codegen lineage): tree-shakeable clients, Zod/Valibot schemas, TanStack Query integration. Positioned between Orval (batteries-included) and openapi-typescript (types-only). — [https://heyapi.dev](https://heyapi.dev) — *Partially verified*
- **OpenAPI Generator** — *Multi-language OpenAPI code generator (Java-based CLI)* — The heavyweight: generates clients AND servers in 50+ languages from OpenAPI specs (Mustache templates, highly customizable). Java-based; slower/heavier than TS-native tools; the enterprise default when polyglot generation matters. 2026 commentary notes TS output quality lags the TS-native tools. — [https://openapi-generator.tech](https://openapi-generator.tech) — *Partially verified*
- **GraphQL Code Generator** — *GraphQL schema/documents → typed code generator (plugin system)* — Generates TS types, typed document nodes, and framework hooks (React/Urql/Vue/Apollo) from GraphQL schemas + operations. Plugin architecture (`@graphql-codegen/typescript`, `-operations`, `-typescript-react-apollo`, etc.). Still the standard GraphQL-typed-client pipeline in 2026. — [https://the-guild.dev/graphql/codegen](https://the-guild.dev/graphql/codegen) — *Unverified*
- **Kiota** — *OpenAPI → multi-language API client generator (Microsoft)* — Microsoft's OpenAPI client generator (C#, Java, TS, Go, Python, PHP, Ruby, CLI): generates fluent clients on the Microsoft Graph client model. Used for Microsoft APIs and enterprise SDKs. — [https://learn.microsoft.com/en-us/openapi/kiota/](https://learn.microsoft.com/en-us/openapi/kiota/) — *Unverified*
- **Hygen** — *Scalable code generator (templates + prompts)* — Template-based generator for scaffolding components/files (`hygen component new`): EJS templates in `_templates/`, prompt support, inject/append actions. The codegen-for-humans complement to API codegen tools. — [https://www.hygen.io](https://www.hygen.io) — *Unverified*
- **protoc (+ buf)** — *Protocol Buffers compiler (+ modern Buf toolchain)* — `protoc` compiles `.proto` schemas to typed code in 10+ languages (gRPC stubs). Buf is the modern toolchain: linting, breaking-change detection, schema registry (BSR), remote generation — the 2026 default for serious protobuf workflows. — [https://protobuf.dev](https://protobuf.dev) — *Unverified*
- **Dependabot** — *Automated dependency update service (GitHub-native)* — GitHub's built-in updater: version-update PRs (npm, pip, GitHub Actions, Docker, etc.) + security alerts/PRs for vulnerable deps. Strengths: zero config, GitHub-native; weaknesses: rigid config, grouped-update UX, no automerge policies as flexible as Renovate's. Free for public/private repos. — [https://github.com/dependabot](https://github.com/dependabot) — *Partially verified*
- **Renovate** — *Universal automated dependency updater (self-hostable)* — The power-user updater: 100+ managers (npm, pip, uv, Docker, Terraform...), presets, automerge policies, grouping, stability-day/cooldown scheduling, vulnerability alerts. 2026 verdict: "Renovate for control, Dependabot for convenience." Mend hosts it; fully self-hostable. — [https://docs.renovatebot.com](https://docs.renovatebot.com) — *Partially verified*
- **Socket.dev (Socket)** — *Behavioral supply-chain security (package firewall/scanner)* — Scans packages for risky BEHAVIORS (install scripts, network access, obfuscation, typosquats, protestware) rather than just known CVEs: the 2026-standard answer to the npm-audit gap (audit only knows published CVEs — the axios hijack had none). GitHub app + CLI + firewall proxy; free for open source. — [https://socket.dev](https://socket.dev) — *Partially verified*
- **Snyk** — *Vulnerability scanning platform (deps, code, containers, IaC)* — Developer security platform: `snyk test` (vuln scan), `snyk monitor`, fix PRs, license checks, container/IaC scanning. Own vulnerability DB (often faster than NVD). Freemium; enterprise staple. — [https://snyk.io](https://snyk.io) — *Partially verified*
- **osv-scanner** — *Vulnerability scanner on the OSV database (Google)* — Open-source scanner querying the distributed OSV.dev vulnerability database across lockfiles/SBOMs (npm, pip, Go, Rust, containers). The free, CI-friendly CVE scanner; basis for many GitHub Action vuln gates. — [https://google.github.io/osv-scanner/](https://google.github.io/osv-scanner/) — *Partially verified*
- **npm audit (+ pip-audit)** — *Built-in vulnerability auditors* — `npm audit` checks the dependency tree against the GitHub Advisory DB (`audit fix`, `--omit=dev`). `pip-audit` is the PyPA equivalent for Python (OSV-backed). Both share the fundamental limit: they only know published advisories — no protection against novel malicious packages (the axios case). — [https://docs.npmjs.com/cli/v11/commands/npm-audit](https://docs.npmjs.com/cli/v11/commands/npm-audit) — *Partially verified*
- **knip** — *Unused dependency/export/file finder* — Finds unused dependencies, devDependencies, exports, files, and config in JS/TS projects — the 2026 replacement for depcheck: understands workspaces, entry patterns, plugin configs. CI gate against dependency rot. — [https://knip.dev](https://knip.dev) — *Partially verified*
- **depcheck (legacy)** — *Unused-dependency checker (legacy)* — The original unused-dep finder; largely superseded by knip in 2026 (weaker workspace/monorepo understanding). Still present in older CI configs. — [https://github.com/depcheck/depcheck](https://github.com/depcheck/depcheck) — *Partially verified*
- **npm-check-updates** — *Interactive dependency update planner* — Shows/updates outdated deps beyond semver ranges (`ncu -u`, interactive mode, doctor mode running tests per upgrade). The manual counterpart to Dependabot/Renovate. — [https://github.com/raineorshine/npm-check-updates](https://github.com/raineorshine/npm-check-updates) — *Unverified*
- **syncpack** — *Monorepo dependency version consistency enforcer* — Enforces consistent dependency versions/ranges across monorepo packages (`syncpack lint`, `fix`, `list-mismatches`); firstMatch version-group policies. Standard monorepo hygiene alongside Changesets. — [https://github.com/JamBalaya56562/syncpack](https://github.com/JamBalaya56562/syncpack) — *Unverified*
- **manypkg** — *Monorepo package.json linter (checks)* — Lints monorepo package.json files for common errors (missing/mismatched internal deps, inconsistent fields); `manypkg check` + `fix`. Thinkmill's companion to Changesets. — [https://github.com/Thinkmill/manypkg](https://github.com/Thinkmill/manypkg) — *Unverified*
- **Turborepo** — *Monorepo task runner + remote cache (Rust)* — The 2026 default monorepo orchestrator for JS: task graph (`turbo.json`), content-hash caching, Remote Caching (Vercel), affected-package filtering. Pairs with pnpm workspaces. "Turborepo's job is to figure out which packages need rebuilding and which can use cached results." — [https://turborepo.dev](https://turborepo.dev) — *Partially verified*
- **Nx** — *Monorepo build system + plugins/generators (TS/Rust)* — The batteries-included monorepo platform: affected commands, computation caching, code generators, 100+ plugins (React, Node, Python, Go...), Nx Cloud remote caching, module federation support. Heavier/opinionated vs Turborepo's thin task-runner; the choice for large orgs wanting generators + conventions. — [https://nx.dev](https://nx.dev) — *Partially verified*
- **Changesets** — *Monorepo versioning + changelog workflow* — The 2026 standard for versioning JS monorepos: PRs include changeset markdown files (`.changeset/*.md`) declaring bump type; the Changesets GitHub Action consumes them into version PRs + changelogs + npm publishes. Pairs with Turborepo/Nx. — [https://github.com/changesets/changesets](https://github.com/changesets/changesets) — *Partially verified*
- **Lerna (legacy mode)** — *Monorepo versioning/publishing (legacy; now Nx-maintained)* — The original JS monorepo publisher (independent/fixed versioning). Now maintained by the Nx team in low-churn legacy mode; new projects choose Changesets. Still present in older monorepos. — [https://lerna.js.org](https://lerna.js.org) — *Partially verified*
- **Rush** — *Enterprise monorepo manager (Microsoft)* — Microsoft's monorepo orchestrator: deterministic installs (shrinkwrap), phased builds, change-file versioning, repo-wide policies. The choice for very large/regulated JS monorepos; heavier ceremony than Turbo/Nx. — [https://rushjs.io](https://rushjs.io) — *Unverified*
- **Moon** — *Polyglot monorepo task runner (Rust)* — Rust task runner for polyglot monorepos (JS, Rust, Go, Python): task inheritance, hashing, remote caching via moonbase. The polyglot alternative to Turbo's JS-centrism. — [https://moonrepo.dev](https://moonrepo.dev) — *Unverified*
- **Bazel** — *Hermetic polyglot build system (Google)* — Google's hermetic, reproducible build system with JS rules (rules_js / aspect rules). Maximum correctness/caching at maximum configuration cost; used by Google-scale monorepos. 2026: still the ceiling for reproducibility, rarely chosen for typical web apps. — [https://bazel.build](https://bazel.build) — *Unverified*
- **semantic-release** — *Fully automated versioning from Conventional Commits* — Derives next version from commit messages (Conventional Commits): generates changelog, GitHub release, npm publish with zero human version decisions. The single-package automation standard; monorepos usually prefer Changesets or multi-semantic-release. — [https://semantic-release.gitbook.io](https://semantic-release.gitbook.io) — *Unverified*
- **release-please** — *Release-PR automation from Conventional Commits (Google)* — Google's releaser: opens/updates a Release PR (version bumps + changelog from commits); merging it creates the GitHub release and publishes. Human-gated where semantic-release is fully automatic; polyglot (strategies per language). — [https://github.com/googleapis/release-please](https://github.com/googleapis/release-please) — *Unverified*
- **nodemon** — *Node.js file-watcher auto-restarter* — The classic "restart node on file change" dev tool (`nodemon server.js`); configurable watch/ignore/exec. 2026: largely displaced by `node --watch` (built-in since Node 18.11/20) and framework dev servers, but still embedded in countless tutorials and legacy setups. — [https://nodemon.io](https://nodemon.io) — *Unverified*
- **node --watch** — *Built-in file-watching restart mode* — `node --watch server.js` restarts on file changes with zero dependencies (stable since Node 22). The 2026 default for simple Node dev loops — no nodemon needed. — [https://nodejs.org/api/cli.html#--watch](https://nodejs.org/api/cli.html#--watch) — *Unverified*
- **PM2** — *Node.js process manager (production)* — Production process manager: clustering, auto-restart, log management, monitoring, startup scripts, `ecosystem.config.js`. Still the default "keep my Node app alive on a VPS" answer; PaaS/containers reduced but didn't eliminate its niche. — [https://pm2.keymetrics.io](https://pm2.keymetrics.io) — *Unverified*
- **concurrently** — *Parallel npm-script runner* — Runs multiple dev commands in one terminal (`concurrently "vite" "tsc -w"`): prefixed/colored output, kill-others behavior. The standard `dev` script glue. — [https://github.com/open-cli-tools/concurrently](https://github.com/open-cli-tools/concurrently) — *Unverified*
- **Husky** — *Git hooks manager* — The standard git-hooks installer: `husky init` writes hook scripts into `.husky/` (pre-commit → lint-staged, commit-msg → commitlint). v9 removed the old `.huskyrc` JS config in favor of plain shell hook files. 2026: still the default, though Lefthook gains on speed. — [https://typicode.github.io/husky/](https://typicode.github.io/husky/) — *Unverified*
- **lint-staged** — *Staged-files task runner (pre-commit)* — Runs linters/formatters ONLY on staged files at commit time (`lint-staged` config mapping globs → commands). The standard Husky pre-commit companion; v15+ requires Node 18.12+. — [https://github.com/lint-staged/lint-staged](https://github.com/lint-staged/lint-staged) — *Unverified*
- **Lefthook** — *Fast polyglot git-hooks manager (Go binary)* — Evil Martians' Go-based hooks runner: parallel execution, per-file commands, `lefthook.yml` config, faster than Husky+lint-staged for big repos; polyglot (not Node-bound). Growing 2026 adoption. — [https://github.com/evilmartians/lefthook](https://github.com/evilmartians/lefthook) — *Unverified*
- **simple-git-hooks** — *Minimal git-hooks setter (package.json config)* — Zero-dependency hooks via `simple-git-hooks` key in package.json — the lightweight Husky alternative for small projects. — [https://github.com/toplenboren/simple-git-hooks](https://github.com/toplenboren/simple-git-hooks) — *Unverified*
- **sccache** — *Compiler cache (ccache-like, with cloud backends)* — Mozilla's compiler cache: wraps C/C++/Rust (and other) compiler invocations, caching to local disk or cloud (S3/GCS/Redis/Azure). The standard CI accelerator for native/Rust/WASM build steps (e.g., caching wasm-pack/Rust builds in JS toolchains). — [https://github.com/mozilla/sccache](https://github.com/mozilla/sccache) — *Unverified*
- **reproducible-builds / SOURCE_DATE_EPOCH** — *Practice + specification for bit-identical builds* — The discipline of producing bit-for-bit identical artifacts from identical sources: `SOURCE_DATE_EPOCH` standardizes embedded timestamps; deterministic file ordering, fixed locales, and normalized paths complete it. Relevant to npm package publishing (provenance/attestations), supply-chain verification, and distro packaging. Debian/Fedora document … — [https://reproducible-builds.org](https://reproducible-builds.org) — *Unverified*

*97 records in this category.*

## 2. Frontend frameworks and components

UI frameworks, meta-frameworks, SSGs, islands architectures, routing, state, forms, tables, charts, editors, visualization, animation, 2D/3D graphics, real-time UI, accessibility; styling systems, component primitives, registries, icon/typography/theme resources, design-system generators, screenshot-to-code tools. Source: `catalogs/01b-frontend.md`.

### A1. UI frameworks / libraries

- **— React** — *Library (not framework; routing/state/build chosen separately)* — Meta's JavaScript library for building web and native user interfaces; component-based, JSX, hooks; React 19 line includes Server Components, `use()` hook; React Compiler 1.0 (Oct 2025) adds automatic memoization. — [https://react.dev](https://react.dev) — *Verified*
- **— Vue.js (Vue 3)** — *Framework (core) with official companion libs* — Progressive JS framework; Composition API, single-file components, compiler-optimized reactivity; Vue 3.5 cut memory usage ~56% via reactivity refactor; Vue 3.6 stages "Vapor Mode" (compiler-level fine-grained reactivity, per secondary sources). — [https://vuejs.org](https://vuejs.org) — *Verified*
- **— Svelte (Svelte 5)** — *Framework (compiler + runtime)* — Compiler-based UI framework; Svelte 5 introduces Runes (signals-based reactivity). Compiles components to vanilla JS; small bundles, high developer satisfaction (91% retention reported in secondary sources). — [https://svelte.dev](https://svelte.dev) — *Partially verified*
- **— SolidJS** — *Library/framework* — Fine-grained compile-time reactivity (signals); JSX without VDOM diffing; highest satisfaction in State of JS surveys for 5 consecutive years per secondary sources despite ~10% usage. — [https://www.solidjs.com](https://www.solidjs.com) — *Partially verified*
- **— Angular** — *Framework (batteries-included: router, forms, DI, i18n, SSR)* — Google's full platform framework; TypeScript-first, dependency injection, signals stable; Angular 21 made zoneless change detection default and dropped zone.js from new apps (per secondary sources). — [https://angular.dev](https://angular.dev) — *Partially verified*
- **— Preact** — *Library* — 3KB React-compatible library; signals proposed/available; used as the UI layer under Deno Fresh. — [https://preactjs.com](https://preactjs.com) — *Partially verified*
- **— Qwik** — *Framework* — Resumability model: fine-grained lazy execution, near-zero startup JS; Qwik City meta-framework. — [https://qwik.dev](https://qwik.dev) — *Partially verified*
- **— Alpine.js** — *Library* — Lightweight declarative behavior directly in markup (`x-data`, `x-on`); official Astro integration (`@astrojs/alpinejs` seen in Astro repo directory listing, inspected 2026-10-10). — [https://alpinejs.dev](https://alpinejs.dev) — *Partially verified*
- **— htmx** — *Library* — Extends HTML with attributes (`hx-get`, `hx-post`, …) for AJAX/WebSocket/SSE-driven partial updates; pairs with server-rendered backends and meta-frameworks (listed among meta-framework test fixtures in a 2026 repo as `html-esm`/`html-global` alternatives). — [https://htmx.org](https://htmx.org) — *Partially verified*
- **— Lit** — *Library* — Google's lightweight library for web components; reactive properties, declarative templates; Storybook lists web components as a supported renderer (verified in storybookjs/storybook README 2026-10-10). — [https://lit.dev](https://lit.dev) — *Partially verified*
- **— Marko** — *Framework* — eBay's UI language; streaming SSR and resumable/partial hydration; Marko Run meta-framework (referenced in a 2026 meta-framework support matrix as detected framework). — [https://markojs.com](https://markojs.com) — *Partially verified*

### A2. Meta-frameworks / full-stack frameworks

- **— Next.js** — *Meta-framework (framework over React)* — The dominant React meta-framework; App Router with React Server Components default, Server Actions stable, `next/image`; file-based routing, middleware, caching primitives. — [https://nextjs.org](https://nextjs.org) — *Partially verified*
- **— Nuxt** — *Meta-framework (framework over Vue)* — "The full-stack Vue framework"; Nuxt 4 line: SSR, static generation, hybrid and edge-side rendering, automatic routing with code-splitting, data fetching/state, auto-imports, zero-config TypeScript, `server/` directory, 300+ modules. — [https://nuxt.com](https://nuxt.com) — *Verified*
- **— SvelteKit** — *Meta-framework* — Official Svelte app framework; SSR/SSG, file-based routing, server load functions, form actions, deployment adapters; native View Transitions via `onNavigate` (per secondary). — [https://kit.svelte.dev](https://kit.svelte.dev) — *Partially verified*
- **— Astro** — *Meta-framework (multi-framework islands)* — "The web framework for content-driven websites"; zero-JS-by-default, Islands Architecture, multi-framework islands (React/Vue/Svelte/Solid/Preact via `@astrojs/*` integrations), Server Islands (`server:defer`), Content Layer; Starlight docs theme maintained in-repo. — [https://astro.build](https://astro.build) — *Verified*
- **— Remix → React Router v7 (framework mode)** — *Library + framework mode (actual category: router library with full-stack framework mode)* — React Router v7 unifies the router library with Remix's framework features (per secondary). Web-fetch style loaders/actions, SSR. — [https://reactrouter.com](https://reactrouter.com) — *Partially verified*
- **— SolidStart** — *Meta-framework* — Solid's full-stack framework; fine-grained compile-time reactivity; high SSR throughput, low memory; pre-1.0 API stability risk (per secondary). — [https://start.solidjs.com](https://start.solidjs.com) — *Partially verified*
- **— TanStack Start** — *Meta-framework* — Full-stack React framework built on TanStack Router; SSR + streaming + type-safe server functions (`createServerFn`); Vite-powered; RC/stable during 2025 per secondary sources; positioned as lighter Next.js alternative without Vercel coupling. — [https://tanstack.com/start](https://tanstack.com/start) — *Partially verified*
- **— Analog** — *Meta-framework* — Angular meta-framework on Vite; file-based routing, SSR/SSG. — [https://analogjs.org](https://analogjs.org) — *Partially verified*
- **— Fresh (Deno)** — *Meta-framework* — Deno's web framework; Preact + islands, zero build step, edge deployment. — [https://fresh.deno.dev](https://fresh.deno.dev) — *Partially verified*
- **— Waku** — *Meta-framework* — Minimal RSC framework with file-based routing (from Zustand/Jotai author Daishi Kato's org). — [https://waku.gg](https://waku.gg) — *Partially verified*
- **— Vike** — *Meta-framework (Vite plugin architecture)* — Successor/rename of `vite-plugin-ssr`; "do-one-thing-do-it-well" composable SSR/SSG over Vite with React (and Vue/Solid) support. — [https://vike.dev](https://vike.dev) — *Partially verified*
- **— RedwoodJS** — *Framework* — Opinionated full-stack React framework (Cells data-fetching pattern, GraphQL API side, Prisma). — [https://redwoodjs.com](https://redwoodjs.com) — *Partially verified*
- **— One (Tamagui)** — *Meta-framework* — From the Tamagui team; unifies web + native routing. — [https://onestack.dev](https://onestack.dev) — *Partially verified*

### A3. Static site generators & docs-site builders

- **— Starlight** — *Framework theme (Astro integration)* — Official Astro docs theme: i18n, search, sidebar nav, dark mode out of the box. — [https://starlight.astro.build](https://starlight.astro.build) — *Partially verified*
- **— Docusaurus** — *Framework (SSG)* — Meta's React-based docs SSG; MDX, versioning, i18n, blog; widely used for OSS project docs. — [https://docusaurus.io](https://docusaurus.io) — *Partially verified*
- **— VitePress** — *Framework (SSG)* — Vue team's Vite-powered docs SSG; markdown-centered, fast; powers Vue/Vite docs themselves. — [https://vitepress.dev](https://vitepress.dev) — *Partially verified*
- **— Eleventy (11ty)** — *Framework (SSG)* — Flexible zero-client-JS SSG supporting many template languages; still deployed widely (Netlify agent skill documents Eleventy build gotchas, accessed 2026-10-10). — [https://www.11ty.dev](https://www.11ty.dev) — *Partially verified*
- **— Hugo** — *Tool/framework (SSG)* — Extremely fast Go-based SSG; single binary; theme ecosystem via git submodules. — [https://gohugo.io](https://gohugo.io) — *Partially verified*
- **— Gatsby** — *Framework (SSG)* — React SSG with GraphQL data layer and plugin ecosystem; multiple 2026 sources advise against it for new projects ("don't use Gatsby for new projects"). — [https://www.gatsbyjs.com](https://www.gatsbyjs.com) — *Historical*

### A5. Routing

- **— React Router** — *Library (+ framework mode, see A2.5)* — De-facto React router; v7 unifies with Remix framework features; data routers with loaders/actions. — [https://reactrouter.com](https://reactrouter.com) — *Partially verified*
- **— TanStack Router** — *Library* — Fully type-safe router: typed routes/params/search params, built-in loaders with caching, file-based routing via Vite plugin (`@tanstack/router-plugin`), devtools, auto code-splitting; basis of TanStack Start. Skill metadata in the wild references v1.166.2 (2026). — [https://tanstack.com/router](https://tanstack.com/router) — *Partially verified*
- **— Vue Router** — *Library* — Official Vue router; nested routes, navigation guards, lazy loading. — [https://router.vuejs.org](https://router.vuejs.org) — *Partially verified*
- **— Wouter** — *Library (~2KB)* — Tiny (~1–2KB) React router; hooks API (`useRoute`, `useLocation`). — [https://github.com/molefrog/wouter](https://github.com/molefrog/wouter) — *Partially verified*

### A6. State management (client state)

- **— Zustand** — *Library* — "Bear necessities for state management in React" — small, fast, scalable; hook-first, no providers; middleware (persist, devtools, immer, subscribeWithSelector); vanilla (`zustand/vanilla`) usable without React. — [https://zustand.docs.pmnd.rs](https://zustand.docs.pmnd.rs) — *Verified*
- **— Jotai** — *Library* — Primitive, flexible atomic state for React (`atom`, `useAtom`); native Suspense/async atoms; same Pmndrs team as Zustand/Valtio. — [https://jotai.org](https://jotai.org) — *Partially verified*
- **— Redux Toolkit (RTK)** — *Library* — Official Redux opinionated toolset: `configureStore`, `createSlice`, `createAsyncThunk`, `createEntityAdapter`; RTK Query built in for data fetching. — [https://redux-toolkit.js.org](https://redux-toolkit.js.org) — *Partially verified*
- **— Valtio** — *Library* — Proxy-based state (`proxy`, `useSnapshot`, `subscribe`); mutable-style code with automatic snapshots. — [https://github.com/pmndrs/valtio](https://github.com/pmndrs/valtio) — *Partially verified*
- **— XState** — *Library (framework-agnostic core + framework bindings)* — State machines/statecharts and actor model for workflow-heavy UI; visual tooling via Stately. — [https://stately.ai](https://stately.ai) — *Partially verified*
- **— MobX** — *Library* — Observable-based reactivity (`observable`, `makeAutoObservable`, `observer`); long-standing alternative to Redux. — [https://mobx.js.org](https://mobx.js.org) — *Partially verified*
- **— Pinia** — *Library* — Official Vue state management (successor to Vuex); Composition-API-friendly stores, DevTools. — [https://pinia.vuejs.org](https://pinia.vuejs.org) — *Partially verified*
- **— TanStack Store / TanStack DB** — *Library (framework-agnostic core + adapters)* — TanStack Store — "reactive data store"; TanStack DB — "reactive sync client store" (per TanStack/query README ecosystem listing, inspected 2026-10-10). — [https://tanstack.com/store](https://tanstack.com/store) — *Partially verified*
- **— Recoil (historical)** — *Library — UNMAINTAINED* — Meta's atomic state library; multiple 2026 sources advise avoiding for new projects (unmaintained). — [https://github.com/facebookexperimental/Recoil](https://github.com/facebookexperimental/Recoil) — *Historical*

### A7. Server state / data fetching

- **— TanStack Query** — *Library (framework-agnostic core + React/Solid/Svelte/Vue adapters)* — "Powerful asynchronous state management, server-state utilities and data fetching"; protocol-agnostic (REST/GraphQL/promises); caching, refetching, pagination/infinite scroll, mutations, dependent queries, prefetching, cancellation, Suspense support. — [https://tanstack.com/query](https://tanstack.com/query) — *Verified*
- **— SWR** — *Library (React hooks)* — Vercel's React hooks for data fetching with stale-while-revalidate strategy; lighter/simpler than TanStack Query (~4KB per secondary). — [https://swr.vercel.app](https://swr.vercel.app) — *Partially verified*
- **— RTK Query** — *Library (data-fetching layer of RTK)* — `createApi`/`injectEndpoints`; codegen from OpenAPI; cache management integrated with Redux store. — [https://redux-toolkit.js.org/rtk-query/overview](https://redux-toolkit.js.org/rtk-query/overview) — *Partially verified*
- **— Apollo Client** — *Library* — Full-featured GraphQL client: normalized cache, `useQuery(gql)`, mutations, subscriptions. — [https://www.apollographql.com/docs/react](https://www.apollographql.com/docs/react) — *Partially verified*
- **— urql** — *Library* — Lightweight, extensible GraphQL client (exchanges architecture). — [https://commerce.nearform.com/open-source/urql](https://commerce.nearform.com/open-source/urql) — *Partially verified*

### A8. Forms & validation

- **— React Hook Form** — *Library* — Performant, uncontrolled-input-based form library (`useForm`, `register`, `Controller`); delegates validation to schema resolvers via `@hookform/resolvers` (supports Zod 3+4, Valibot, Yup, ArkType, Standard Schema, etc.). — [https://react-hook-form.com](https://react-hook-form.com) — *Partially verified*
- **— Formik** — *Library* — Long-standing React form library; multiple 2026 sources describe it as "legacy but stable". — [https://formik.org](https://formik.org) — *Partially verified*
- **— TanStack Form** — *Library* — "Type‑safe form state" per TanStack/query README ecosystem listing (inspected 2026-10-10). — [https://tanstack.com/form](https://tanstack.com/form) — *Partially verified*
- **— Zod** — *Library* — TypeScript-first schema validation with static type inference; Zod 4 line current in 2026 (resolvers handle both v3/v4 per secondary); Standard Schema participant. — [https://zod.dev](https://zod.dev) — *Partially verified*
- **— Valibot** — *Library* — Modular schema library; tree-shakeable functions; significantly smaller bundles than Zod; Standard Schema compatible. — [https://valibot.dev](https://valibot.dev) — *Partially verified*
- **— Yup** — *Library* — Long-standing object-schema validator; historically paired with Formik. — [https://github.com/jquense/yup](https://github.com/jquense/yup) — *Partially verified*

### A9. Tables / data grids

- **— TanStack Table** — *Library (headless — bring your own markup/styles)* — "Headless datagrids" per TanStack/query README ecosystem listing (inspected 2026-10-10); sorting, filtering, pagination, row selection, virtualization hooks. — [https://tanstack.com/table](https://tanstack.com/table) — *Partially verified*
- **— AG Grid** — *Library (community + enterprise tiers)* — Full-featured datagrid: grouping, pivoting, server-side row model, Excel export; community (MIT) + enterprise (commercial) split. — [https://www.ag-grid.com](https://www.ag-grid.com) — *Partially verified*
- **— MUI X Data Grid** — *Library* — MUI's datagrid; community MIT tier plus Pro/Premium commercial features (row grouping, Excel export, etc.). — [https://mui.com/x/react-data-grid/](https://mui.com/x/react-data-grid/) — *Partially verified*
- **— TanStack Virtual** — *Library* — "Virtualized rendering" per TanStack/query README ecosystem listing (inspected 2026-10-10); row/column virtualization for lists, tables, grids. — [https://tanstack.com/virtual](https://tanstack.com/virtual) — *Partially verified*

### A10. Charting & data visualization

- **— Recharts** — *Library* — Declarative composable React chart components (`<LineChart>`, `<XAxis>`, `<Tooltip>`); SVG rendering; highest-download React chart library (~50M weekly npm downloads per Sep 2026 secondary); built on D3 submodules. — [https://recharts.org](https://recharts.org) — *Partially verified*
- **— Apache ECharts** — *Library (framework-agnostic; wrappers exist per framework)* — Feature-rich charting via single `option` config object; Canvas default, SVG renderer available; huge chart-type coverage incl. geo/3D. — [https://echarts.apache.org](https://echarts.apache.org) — *Partially verified*
- **— Nivo** — *Library* — 50+ chart types, strong theming system, SVG default with Canvas variants (`*Canvas`) for large datasets; built on D3. — [https://nivo.rocks](https://nivo.rocks) — *Partially verified*
- **— Victory** — *Library* — Composable chart components with built-in zoom/pan/brush containers; ~25 chart types; also Victory Native for React Native. — [https://commerce.nearform.com/open-source/victory](https://commerce.nearform.com/open-source/victory) — *Partially verified*
- **— visx** — *Library (collection of primitives)* — Airbnb's set of low-level viz primitives combining D3 math with React rendering; build your own charts from tested parts. — [https://airbnb.io/visx](https://airbnb.io/visx) — *Partially verified*
- **— Chart.js / react-chartjs-2** — *Library* — Canvas-based config-object charts; strong large-data performance; react-chartjs-2 is the React binding (~3.8M weekly downloads per 2026 secondary snapshot). — [https://www.chartjs.org](https://www.chartjs.org) — *Partially verified*
- **— Tremor** — *Component library (chart-focused blocks)* — Prebuilt Tailwind dashboard components (KPI cards, charts) built on Recharts; Apache-2.0. — [https://www.tremor.so](https://www.tremor.so) — *Partially verified*
- **— D3.js** — *Library (modular)* — The foundational toolkit: selections, scales, shapes, layouts, transitions; powers Recharts/Nivo/visx under the hood. — [https://d3js.org](https://d3js.org) — *Partially verified*
- **— Observable Plot** — *Library* — Concise API for exploratory charts (`Plot.plot({marks: […]})`); SVG output. — [https://observablehq.com/plot](https://observablehq.com/plot) — *Partially verified*

### A11. Code editors (embeddable)

- **— Monaco Editor** — *Library* — The VS Code editor surfaced as a web library: IntelliSense, multi-cursor, diff editor, command palette, language workers; ~0.5–2MB gzip; worker-based architecture. — [https://microsoft.github.io/monaco-editor](https://microsoft.github.io/monaco-editor) — *Partially verified*
- **— CodeMirror 6** — *Library (extension-based)* — Ground-up rewrite (2021); composable extensions (state/view/history/language packs/themes); ~130–150KB; ESM-native, no workers; used by Obsidian/GitHub/Notion (per secondary). — [https://codemirror.net](https://codemirror.net) — *Partially verified*

### A12. Rich-text / markdown / block editors

- **— Tiptap** — *Library/framework* — Headless editor on ProseMirror; extension packages (StarterKit etc.); React/Vue/Svelte/headless bindings; v3 line in 2026; official shadcn editor component uses Tiptap (per secondary); Pro extensions/cloud commercial (free plan removed June 2025 per secondary). — [https://tiptap.dev](https://tiptap.dev) — *Partially verified*
- **— Lexical** — *Library/framework* — Meta's editor framework (~22–25KB core); command-based, custom nodes, React-first with framework-agnostic core; production-proven (Facebook/Instagram/Threads); Yjs collaboration; markdown import/export. — [https://lexical.dev](https://lexical.dev) — *Partially verified*
- **— Plate** — *Library (framework over Slate)* — 50+ plugins on Slate; AIKit (AIPlugin/AIChatPlugin, markdown streaming), SlashKit, Yjs collaboration, Markdown plugin; MIT core with Plate Plus commercial. — [https://platejs.org](https://platejs.org) — *Partially verified*
- **— ProseMirror** — *Library (modular toolkit)* — De-facto standard toolkit: strict schema, immutable document model, transactions, collab module; foundation of Tiptap/BlockNote/Remirror/Milkdown. — [https://prosemirror.net](https://prosemirror.net) — *Partially verified*
- **— BlockNote** — *Library (product layer)* — Notion-like block editor with React UI out of the box; built-in AI extension (`@blocknote/xl-ai`); Yjs collab; markdown export explicitly lossy. — [https://www.blocknotejs.org](https://www.blocknotejs.org) — *Partially verified*
- **— Slate** — *Library* — Once-flexible React editor framework; one 2026 secondary source reports the repo was archived on 2026-02-04. — [https://github.com/ianstormtaylor/slate](https://github.com/ianstormtaylor/slate) — *Unresolved*
- **— Quill** — *Library (vanilla; community React wrappers)* — Long-standing WYSIWYG editor; Quill 2 line; ~45KB; API/format-based deltas. — [https://quilljs.com](https://quilljs.com) — *Partially verified*
- **— Milkdown** — *Library (plugin-driven)* — Markdown-first editing on ProseMirror+Remark; React/Vue/Solid/vanilla bindings. — [https://milkdown.dev](https://milkdown.dev) — *Partially verified*
- **— MDXEditor** — *Library* — Notion-like WYSIWYG with native markdown support; code blocks with syntax highlighting; TypeScript. — [https://mdxeditor.dev](https://mdxeditor.dev) — *Partially verified*
- **— Novel (AI editor demo)** — *Demo site / starter template (actual category: demo, not framework)* — Notion-style AI autocomplete editor built on Tiptap; Apache-2.0; widely forked as a starter, but "more demo than product" per secondary. — [https://github.com/steven-tey/novel](https://github.com/steven-tey/novel) — *Partially verified*

### A13. Animation / interaction systems

- **— Motion (Framer Motion)** — *Library* — Springs, gestures, `layout` (automatic FLIP) animations, `AnimatePresence` exit animations, scroll utilities; Motion One is the WAAPI-backed lightweight subset (~4KB); `motion/react` import path current. — [https://motion.dev](https://motion.dev) — *Partially verified*
- **— GSAP** — *Library* — Timelines, scroll sequencing (ScrollTrigger), SVG morphing, text splitting, precise orchestration; ~23KB core + plugins. Webflow acquired GreenSock; since GSAP 3.13 all plugins free incl. commercial use — but NOT OSI/MIT licensed (no forking/redistribution; bars competing visual-animation tools per secondary license analysis). — [https://gsap.com](https://gsap.com) — *Partially verified*
- **— Anime.js** — *Library* — v4 line; CSS/SVG/DOM/object animation, spring eases, timelines, stagger; ~17KB; no React coupling. — [https://animejs.com](https://animejs.com) — *Partially verified*
- **— React Spring** — *Library* — Physics-only animation model; strong for gesture-driven and 3D-adjacent work; ~25KB. — [https://www.react-spring.dev](https://www.react-spring.dev) — *Partially verified*
- **— Lottie / dotLottie** — *Library/player* — Renders After Effects animations as JSON (Lottie) or compressed `.lottie` (dotLottie, ThorVG WASM); designer-handoff workflow. — [https://airbnb.io/lottie](https://airbnb.io/lottie) — *Partially verified*
- **— Rive** — *Tool + runtimes (editor commercial; runtimes open)* — Designer-authored interactive animations with state machines; small runtimes for web/iOS/Android/React Native/Flutter. — [https://rive.app](https://rive.app) — *Partially verified*
- **— AutoAnimate (FormKit)** — *Library (~2KB)* — One line animates add/remove/reorder of list items; framework-agnostic. — [https://auto-animate.formkit.com](https://auto-animate.formkit.com) — *Partially verified*
- **— Lenis** — *Library* — Inertial smooth scrolling; often paired with GSAP ScrollTrigger; hijacks native scroll — use only as a locked design decision, disable under reduced-motion (per secondary guidance). — [https://lenis.darkroom.engineering](https://lenis.darkroom.engineering) — *Partially verified*
- **— Theatre.js** — *Library + dev tool (studio is dev-only)* — Timeline/keyframe editing UI for complex sequences and 3D camera work. — [https://www.theatrejs.com](https://www.theatrejs.com) — *Partially verified*
- **— Remotion** — *Library/framework* — Write videos in React; render to MP4/WebM via headless Chromium; data-driven video generation. — [https://www.remotion.dev](https://www.remotion.dev) — *Partially verified*

### A14. 2D/3D browser graphics

- **— Three.js** — *Library* — The standard WebGL/WebGPU 3D library; scenes, cameras, materials, loaders, postprocessing. — [https://threejs.org](https://threejs.org) — *Partially verified*
- **— React Three Fiber** — *Library* — Declarative React bindings for Three.js; drei adds helpers (controls, loaders, environment). — [https://r3f.docs.pmnd.rs](https://r3f.docs.pmnd.rs) — *Partially verified*
- **— PixiJS** — *Library* — Fast 2D sprite/scene rendering on WebGL/WebGPU; v8 line. — [https://pixijs.com](https://pixijs.com) — *Partially verified*
- **— Babylon.js** — *Framework/engine* — Microsoft-backed full 3D engine: physics, audio, GUI, XR; more batteries-included than Three.js. — [https://www.babylonjs.com](https://www.babylonjs.com) — *Partially verified*
- **— p5.js** — *Library* — Processing's JS port; beginner-friendly creative coding, 2D + WEBGL modes. — [https://p5js.org](https://p5js.org) — *Partially verified*

### A15. Real-time interfaces

- **— Socket.IO** — *Library (client + server)* — WebSocket-based real-time with fallbacks, rooms, multiplexing; client + Node server. — [https://socket.io](https://socket.io) — *Partially verified*
- **— PartyTown** — *Library (actual category: performance tool, not UI framework)* — Relocates third-party scripts into a web worker to unblock main thread; Astro ships an official integration. — [https://partytown.qwik.dev](https://partytown.qwik.dev) — *Partially verified*

### A16. Accessibility resources

- **— axe-core** — *Library/tool* — Automated a11y rule engine; powers Lighthouse a11y audits, jest-axe, Storybook a11y addon, eslint-plugin-jsx-a11y-adjacent flows. — [https://github.com/dequelabs/axe-core](https://github.com/dequelabs/axe-core) — *Partially verified*
- **— eslint-plugin-jsx-a11y** — *ESLint plugin* — Lint rules for accessible JSX (alt text, roles, keyboard handlers, etc.). — [https://github.com/jsx-eslint/eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y) — *Partially verified*

### B1. CSS frameworks (utility-first & class-based)

- **— Tailwind CSS** — *Framework (build-time CSS engine)* — Utility-first CSS for rapid custom UI; v4 line is a Rust-based engine (`crates/` in repo), CSS-first config via `@theme`, native Vite plugin; zero client runtime. — [https://tailwindcss.com](https://tailwindcss.com) — *Verified*
- **— Bootstrap** — *Framework* — The classic component-class framework (grid, buttons, modals…); v5 line; Bootstrap Icons separate MIT set. — [https://getbootstrap.com](https://getbootstrap.com) — *Partially verified*
- **— Bulma** — *Framework* — Pure-CSS framework, readable class names, no JS. — [https://bulma.io](https://bulma.io) — *Partially verified*
- **— Pico.css** — *Framework* — Semantic-HTML styling with minimal classes; tiny footprint; dark mode built in. — [https://picocss.com](https://picocss.com) — *Partially verified*
- **— UnoCSS** — *Framework/engine* — Instant on-demand atomic CSS with presets (incl. Tailwind/Windi-compatible); attributify mode; faster than WindiCSS lineage. — [https://unocss.dev](https://unocss.dev) — *Partially verified*
- **— Panda CSS** — *Build-time styling engine* — Write styles in JS/TS (`css()`, `cva` recipes, patterns); extracts to static CSS at build; type-safe tokens; v2 removed tagged-template styling; Chakra's styling roadmap target. Ships `@pandacss/mcp` (MCP server exposing live tokens/recipes/patterns) and `@pandacss/eslint-plugin`; agent skill exists (`graphieros/panda` skills/panda-css/SKILL.md). — [https://panda-css.com](https://panda-css.com) — *Partially verified*
- **— Open Props** — *Token set (no build step)* — Ready-made CSS variables (colors, spacing, shadows, animations) + optional normalize; framework-agnostic. — [https://open-props.style](https://open-props.style) — *Partially verified*

### B2. CSS-in-JS & build-time styling

- **— styled-components** — *Library* — The original popular CSS-in-JS (`styled.button\`\``); one secondary research report states it is in **maintenance mode as of 2025-03-17**, with its own maintainer recommending against it for new projects. — [https://styled-components.com](https://styled-components.com) — *Partially verified*
- **— Emotion** — *Library* — Widely used CSS-in-JS (MUI v5's engine); css prop, styled API; supports static extraction. — [https://emotion.sh](https://emotion.sh) — *Partially verified*
- **— vanilla-extract** — *Build-time library* — Type-safe, locally scoped classes/variables/themes in TS; generates static CSS at build time. — [https://vanilla-extract.style](https://vanilla-extract.style) — *Partially verified*
- **— Linaria** — *Build-time library* — styled-components-like syntax with zero runtime; extracts CSS at build. — [https://linaria.dev](https://linaria.dev) — *Partially verified*
- **— Pigment CSS** — *Build-time library* — MUI's static-extraction styling (benchmarks cited in secondary: −20% First-Load JS, −25% TBT vs runtime emotion); MUI's forward path from runtime CSS-in-JS. — [https://github.com/mui/pigment-css](https://github.com/mui/pigment-css) — *Partially verified*
- **— Stitches (historical)** — *Library* — Near-zero-runtime CSS-in-JS with variants API; project ended (maintainers moved on); do not adopt. — [https://github.com/stitchesjs/stitches](https://github.com/stitchesjs/stitches) — *Historical*

### B3/B4. Design tokens & theming primitives

- **— Style Dictionary** — *Tool/library* — Transforms W3C-format design tokens into platform outputs (CSS vars, iOS, Android, JS). — [https://amzn.github.io/style-dictionary](https://amzn.github.io/style-dictionary) — *Partially verified*
- **— Tokens Studio (for Figma)** — *Tool (plugin; some open-source components)* — Figma plugin for creating/managing W3C design tokens; syncs to GitHub/JSON; feeds Style Dictionary pipelines. — [https://tokens.studio](https://tokens.studio) — *Partially verified*
- **— Radix Colors** — *Token set (CSS/JS)* — 30 color families × 12 steps designed for UI (incl. dark-mode pairs, alpha variants); widely reused as token base. — [https://www.radix-ui.com/colors](https://www.radix-ui.com/colors) — *Partially verified*

### B5. Accessible component primitives (headless)

- **— Radix Primitives** — *Library (per-part packages)* — ~30-34 unstyled primitives (Dialog, Popover, Select, Tabs, Toast…) with `asChild` composition; WAI-ARIA aligned; the layer shadcn/ui was built on (default until shadcn switched default to Base UI in July 2026 per secondary). — [https://www.radix-ui.com/primitives](https://www.radix-ui.com/primitives) — *Partially verified*
- **— Base UI** — *Library (single package)* — Built by people from Radix/MUI/Floating UI teams; 37 components + 4 utilities at v1.0 (Dec 2025 per secondary); render-prop pattern instead of `asChild`; shadcn/ui's default primitive layer since July 2026; broader component set than Radix; gaps: no calendar/date picker/table/tree, no localized strings (per secondary). — [https://base-ui.com](https://base-ui.com) — *Partially verified*
- **— React Aria Components (Adobe)** — *Library* — 50+ unstyled components (incl. 6 date components, 7 color components, Table, Tree, GridList, TagGroup, accessible drag-and-drop); deepest WAI-ARIA conformance; 30+ locales; RTL automatic from locale; multiple calendar systems; ~3.11M weekly downloads (per secondary); Apache-2.0. — [https://react-spectrum.adobe.com/react-aria](https://react-spectrum.adobe.com/react-aria) — *Partially verified*
- **— Ark UI** — *Library* — 45+ components built on Zag.js state machines; single API across React/Vue/Solid/Svelte; Chakra UI v3 is built on Ark UI; MIT. — [https://ark-ui.com](https://ark-ui.com) — *Partially verified*
- **— Headless UI (Tailwind Labs)** — *Library* — Tailwind Labs' headless components; ~16 components; small surface; good for simple needs. — [https://headlessui.com](https://headlessui.com) — *Partially verified*
- **— Ariakit** — *Library* — Accessible primitives with strong coverage and many real examples; good for comboboxes, menus, dialogs, command menus, search/filter UIs. — [https://ariakit.org](https://ariakit.org) — *Partially verified*
- **— Melt UI / Bits UI (Svelte)** — *Library* — Melt UI = headless builders for Svelte; Bits UI = styled-adjacent layer over Melt (shadcn-svelte lineage). — [https://www.melt-ui.com](https://www.melt-ui.com) — *Partially verified*
- **— Kobalte (Solid)** — *Library* — Solid's headless primitive set (Radix-like API for Solid). — [https://kobalte.dev](https://kobalte.dev) — *Partially verified*
- **— Floating UI** — *Library* — The positioning engine under most headless libraries; use directly for bespoke anchored surfaces. — [https://floating-ui.com](https://floating-ui.com) — *Partially verified*
- **— Zag.js** — *Library* — Raw state machines powering Ark UI; use when you want no framework opinion. — [https://zagjs.com](https://zagjs.com) — *Partially verified*

### B6. Component registries (shadcn-compatible distribution model)

- **— shadcn/ui** — *Registry + CLI that copies source into the consumer repo* — "Composable, accessible components with thoughtful defaults… Build your own component library." 50+ components on Radix/Base UI/React Aria primitives + Tailwind; theming via CSS vars; charts/docs patterns; repo contains `skills/` dir, `.claude/` dir (agent-facing). — [https://ui.shadcn.com](https://ui.shadcn.com) — *Verified*
- **— Magic UI** — *Registry (remote index `https://magicui.design/r/index.json`)* — 200+ animated items (marquees, bento grids, animated beam, number tickers, shimmer buttons, canvas shaders); Tailwind + Motion; install via `shadcn add "https://magicui.design/r/{name}.json"`. — [https://magicui.design](https://magicui.design) — *Partially verified*
- **— Aceternity UI** — *Registry (`https://ui.aceternity.com/r/index.json`) — NO public source repo* — Cinematic effects (spotlight, 3D cards/pin, lamp effect, beams, parallax); heaviest/boldest of the registries; use sparingly. — [https://ui.aceternity.com](https://ui.aceternity.com) — *Partially verified*
- **— Cult UI** — *Registry (`https://cult-ui.com/r/index.json`)* — AI-chat/agent-surface-friendly components; Motion-based; tasteful. — [https://cult-ui.com](https://cult-ui.com) — *Partially verified*
- **— Origin UI → cosscom/coss (relicensed)** — *Registry (actual category post-transfer: AGPL-3.0 monorepo with MIT-carved UI dirs)* — Origin UI was transferred to `cosscom/coss` (Cal.com) and relicensed **AGPL-3.0**, with `apps/ui/` and `apps/origin/` carved out MIT (per 2026 license analysis). — [https://github.com/cosscom/coss](https://github.com/cosscom/coss) — *Partially verified*
- **— Kibo UI** — *Registry* — Complex app components: kanban, gantt, editors, data-table patterns. — [https://www.kibo-ui.com](https://www.kibo-ui.com) — *Partially verified*
- **— Animate UI** — *Registry* — Animated versions of familiar primitives — swap-in upgrades for existing components. — [https://animate-ui.com](https://animate-ui.com) — *Partially verified*
- **— React Bits** — *Registry (`https://reactbits.dev/r/index.json`)* — 44.8k★ (GitHub stars per secondary); physics text, magnetic cursor, ballpit, animated backgrounds. — [https://reactbits.dev](https://reactbits.dev) — *Partially verified*
- **— ReUI** — *Registry (`https://reui.io/r/index.json`) — some items gated* — SaaS hero blocks, notification banners; repo MIT but hosted registry freemium — some items return 401 "Provide your license key" (per secondary). — [https://reui.io](https://reui.io) — *Partially verified*
- **— Tailark** — *Registry* — Marketing sections with distinct look. — [https://tailark.com](https://tailark.com) — *Partially verified*
- **— 21st.dev** — *Marketplace (actual category: marketplace with shadcn-registry export + AI generation + MCP)* — Thousands of community components/themes/templates; `21st add <user>/<slug>` installs via its shadcn registry; `21st get`/`generate` for bespoke/AI-generated code; MCP server for search+generation; needs account + token; free quota small; generation costs credits. — [https://21st.dev](https://21st.dev) — *Partially verified*
- **— uishelf** — *CLI tool (actual category: agent-facing discovery/install tool, not a component source itself)* — CLI (`uishelf providers list`, `uishelf libs`) + MCP platform unifying shadcn/ui, Magic UI, Aceternity, 21st.dev, React Bits, Ruixen UI, Cult UI, ReUI registries with search schema/endpoints and install commands; compatibility resolver across Tailwind v3/v4, React 19, Radix/Base UI, Motion. — [https://github.com/sh20raj/uishelf](https://github.com/sh20raj/uishelf) — *Partially verified*

### B7. Styled component libraries (batteries-included)

- **— MUI (Material UI)** — *Library* — "Comprehensive library of React components… independent implementation of Google's Material Design"; 60+ components; theming object; MUI X extends with complex components; Joy UI (alternative design) in org. — [https://mui.com](https://mui.com) — *Verified*
- **— Mantine** — *Library* — 100+ components, hooks library, props-based styling + overrides, notifications, forms, dates; custom CSS-in-JS with static extraction; Mantine MCP exists (per secondary skill docs). — [https://mantine.dev](https://mantine.dev) — *Partially verified*
- **— Ant Design** — *Library* — Alibaba's enterprise design system; huge component coverage; v6 defaults to pure CSS-variable mode (per secondary); theme tokens. — [https://ant.design](https://ant.design) — *Partially verified*
- **— Chakra UI** — *Library* — Style-props component library; v3 built on Ark UI; styling roadmap targets Panda CSS. — [https://chakra-ui.com](https://chakra-ui.com) — *Partially verified*
- **— HeroUI (formerly NextUI)** — *Library* — Tailwind-based React component library (renamed from NextUI); beautiful defaults. — [https://www.heroui.com](https://www.heroui.com) — *Partially verified*
- **— Radix Themes** — *Library* — Cohesive styled React kit with theme provider/tokens; use when you want a packaged system quickly rather than copy-owned shadcn source. — [https://www.radix-ui.com/themes](https://www.radix-ui.com/themes) — *Partially verified*

### B8. Reusable page sections & block libraries

- **— daisyUI** — *Tailwind plugin (actual category: class-based component layer + 30+ themes)* — Component classes for Tailwind (`btn`, `card`, `modal`…); 30+ built-in themes; semantic color names. — [https://daisyui.com](https://daisyui.com) — *Partially verified*
- **— HyperUI** — *Block gallery (actual category: marketing/component snippets, not a library)* — Free Tailwind components/sections (marketing, e-commerce, application UI) to copy-paste. — [https://www.hyperui.dev](https://www.hyperui.dev) — *Partially verified*
- **— Tailblocks** — *Block gallery* — Ready-made Tailwind blocks (by the Tailwind CSS team lineage — mertsabinov). — [https://tailblocks.cc](https://tailblocks.cc) — *Partially verified*
- **— Flowbite (components + blocks)** — *Library + blocks* — Tailwind components with JS behaviors; Flowbite Blocks section gallery; React/Svelte/Vue wrappers. — [https://flowbite.com](https://flowbite.com) — *Partially verified*
- **— Tailwind UI (commercial)** — *Paid product (actual category: commercial snippet library, not open source)* — Official paid component kit from Tailwind Labs (500+ components, templates). — [https://tailwindui.com](https://tailwindui.com) — *Partially verified*

### B9. Dashboard kits & admin frameworks

- **— Refine** — *Framework* — Headless React framework for CRUD/admin: data providers (REST/GraphQL/Supabase…), auth providers, routers; UI-agnostic (MUI/AntD/shadcn integrations). — [https://refine.dev](https://refine.dev) — *Partially verified*
- **— AdminJS** — *Tool/framework* — Generates admin UI from backend models (Mongoose/Sequelize/Prisma adapters). — [https://adminjs.co](https://adminjs.co) — *Partially verified*

### B10. Icon systems

- **— Lucide** — *Icon library (SVG + framework packages)* — 1,500–1,800+ ultra-consistent 24×24 stroke icons; first-party React/Vue/Svelte/Angular/Flutter packages; the safe default (and the "AI-slop default" per one 2026 skill — consider Phosphor for distinctiveness). — [https://lucide.dev](https://lucide.dev) — *Partially verified*
- **— Tabler Icons** — *Icon library* — 5,800–6,100+ stroke icons; React/Vue/Svelte/webfont packages; best coverage of obscure glyphs. — [https://tabler.io/icons](https://tabler.io/icons) — *Partially verified*
- **— Phosphor Icons** — *Icon library* — 7,000–9,000+ icons in six weights (thin, light, regular, bold, fill, duotone); tree-shakable; ~1KB/icon; TypeScript-first React package. — [https://phosphoricons.com](https://phosphoricons.com) — *Partially verified*
- **— Heroicons** — *Icon library* — 300–1,200+ icons (counts vary by source/date); 24px outline/solid + 20px mini (+ micro); pairs with Tailwind sizing. — [https://heroicons.com](https://heroicons.com) — *Partially verified*
- **— Iconoir** — *Icon library* — 1,500–1,600 pristine geometric icons; no paywalls; React/Vue/Svelte/Flutter. — [https://iconoir.com](https://iconoir.com) — *Partially verified*
- **— Remix Icon** — *Icon library* — 2,800 neutral system symbols; line + fill variants; React/webfont. — [https://remixicon.com](https://remixicon.com) — *Partially verified*
- **— Material Symbols (Google)** — *Icon font + SVG* — 2,500–15,000+ (counts vary) variable icons; optical sizing; React/Vue wrappers community. — [https://fonts.google.com/icons](https://fonts.google.com/icons) — *Partially verified*
- **— Radix Icons** — *Icon library* — 318 icons on a 15×15 grid; designed by WorkOS; crisp at small sizes; natural fit with Radix primitives. — [https://www.radix-ui.com/icons](https://www.radix-ui.com/icons) — *Partially verified*
- **— Bootstrap Icons** — *Icon library* — 2,000+ icons; standalone (no Bootstrap needed); SVG/webfont. — [https://icons.getbootstrap.com](https://icons.getbootstrap.com) — *Partially verified*
- **— Iconify (aggregator)** — *Meta-library (unified access to 150+ sets incl. all above)* — Single component/API serving 200,000+ icons from 150+ sets (Lucide, Tabler, Phosphor, Material, etc.); on-demand loading; offline JSON via `@iconify-json/*`. — [https://iconify.design](https://iconify.design) — *Partially verified*
- **— Simple Icons (brand logos)** — *Icon library* — 3,200+ vector SVGs of tech brands/dev tools/social; CC0; React/Vue/Svelte packages. — [https://simpleicons.org](https://simpleicons.org) — *Partially verified*
- **— SVGL** — *Gallery + API* — Curated SVG brand logos for developers; API + Figma. — [https://svgl.app](https://svgl.app) — *Partially verified*

### B11. Typography resources

- **— Fontsource** — *Font distribution (npm packages per font/weight/subset)* — npm-packaged Google Fonts (and others) for self-hosting: per-weight/subset imports, no Google CDN dependency. — [https://fontsource.org](https://fontsource.org) — *Partially verified*
- **— Google Fonts / Geist** — *Service + font* — Google Fonts: largest free font catalog (Inter, Roboto, etc.). Geist: Vercel's typeface (sans + mono), default in many AI-generated UIs. — [https://fonts.google.com](https://fonts.google.com) — *Partially verified*

### B12. Theme systems

- **— next-themes** — *Library* — `ThemeProvider` + `useTheme`; class/attribute strategy; no-flash script; system preference support. — [https://github.com/pacocoursey/next-themes](https://github.com/pacocoursey/next-themes) — *Partially verified*
- **— tweakcn (shadcn theme editor)** — *Web tool (actual category: theme generator, not a library)* — Visual editor generating shadcn CSS-var themes (OKLCH); copy theme CSS. — [https://tweakcn.com](https://tweakcn.com) — *Partially verified*

### B13. Animation utilities (CSS-level)

- **— tailwindcss-animate / tw-animate-css** — *Tailwind plugin / CSS package* — `animate-in`/`animate-out` utilities (fade/slide/zoom) for Tailwind; `tw-animate-css` is the v4-native successor using CSS-first config. — [https://github.com/jamiebuilds/tailwindcss-animate](https://github.com/jamiebuilds/tailwindcss-animate) — *Partially verified*

### B14. Design-system generators & visual builders

- **— Plasmic** — *SaaS tool + open-source runtime* — Visual page/component builder generating React code; design-system-aware; content + code integration. — [https://www.plasmic.app](https://www.plasmic.app) — *Partially verified*
- **— Locofy** — *Commercial tool (Figma plugin + Lightning/Classic engines)* — Converts structured Figma designs to React/Next.js/Vue/Angular/HTML/CSS/React Native/Flutter; Lightning = one-click AI pass, Classic = step-by-step; quality proportional to design discipline; MCP for AI copilots on paid tiers; token-based pricing. — [https://www.locofy.ai](https://www.locofy.ai) — *Partially verified*
- **— Builder.io (Visual Copilot)** — *SaaS platform (parts open source)* — Visual Copilot 2.0 (2026): Figma selection → React/Next/Vue/Angular/Svelte/Qwik; trained on 2M+ data points (per vendor); visual editor + enterprise CMS. — [https://www.builder.io](https://www.builder.io) — *Partially verified*
- **— Anima** — *Commercial tool* — Figma → functional React components with prop types; follows existing component patterns; strong when team already has a React component library. — [https://www.animaapp.com](https://www.animaapp.com) — *Partially verified*
- **— Onlook** — *Tool (Electron app; actual category: visual code editor, not a library)* — Visually edit a real React/Next.js + Tailwind codebase; 25,900+ GitHub stars by June 2026 (per secondary); MIT, self-hostable; free. — [https://onlook.com](https://onlook.com) — *Partially verified*
- **— Puck** — *Library (drag-and-drop editor you embed)* — Embeddable drag-and-drop page editor for React; you define components, editors get visual editing; serializes to JSON. — [https://puckeditor.com](https://puckeditor.com) — *Partially verified*
- **— Figma Dev Mode MCP** — *MCP server (agent tool)* — Figma's MCP server exposes designs/code to IDE agents; free during beta on Dev/Full seats (per 2026 secondary). — [https://www.figma.com/dev-mode](https://www.figma.com/dev-mode) — *Partially verified*

### B15. AI screenshot/prompt-to-code tools

- **— v0 (Vercel)** — *SaaS product (actual category: AI product, not a library)* — Generates React + Tailwind (shadcn-style) components from text prompts, screenshots, mockups, or Figma; visual iteration editor; exports to Vercel projects/GitHub/CLI; token-based pricing (free $5 credits; Team $30/user/mo; Figma import gated to paid per secondary). — [https://v0.app](https://v0.app) — *Partially verified*
- **— screenshot-to-code (open source)** — *Tool (actual category: open-source app, not a library)* — Upload a screenshot → HTML/Tailwind (or React) via vision models; the canonical open-source reference for the pattern. — [https://github.com/abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) — *Partially verified*
- **— Bolt.new / Lovable (full-stack prompt-to-app)** — *SaaS products* — Bolt.new: full-stack from a prompt (frontend + backend scaffolding, sandboxed runtime) — strong for MVPs. Lovable: solo-founder-focused, Supabase-native backend; output quality varies more on complex UIs (per secondary). — [https://bolt.new](https://bolt.new) — *Partially verified*
- **— Magic Patterns / Uizard (ideation)** — *SaaS products* — Magic Patterns: UI patterns (cards, dashboards, layouts) in React + Tailwind for assembling pages. Uizard: wireframes/mockups/prototypes — better for ideation than production code. — [https://www.magicpatterns.com](https://www.magicpatterns.com) — *Partially verified*

### B16. Component documentation tools

- **— Storybook** — *Tool/framework* — "Industry standard workshop for building, documenting, and testing UI components in isolation"; renderers for React/Vue/Angular/Svelte/Web Components/React Native/HTML/Ember/Preact/Qwik/Solid; addons (a11y, docs, actions, viewport, interactions); test-runner + Vitest integration; Chromatic for visual regression. — [https://storybook.js.org](https://storybook.js.org) — *Verified*
- **— Ladle** — *Tool* — Extremely lightweight (~5 deps), Vite-native, fast startup (~1.2s cold); stories format; React-only. — [https://ladle.dev](https://ladle.dev) — *Partially verified*
- **— Histoire** — *Tool* — Vite-native stories; Vue 3 and Svelte primary; React experimental/community; markdown docs, props tables, playgrounds; snapshots via Vitest. — [https://histoire.dev](https://histoire.dev) — *Partially verified*
- **— Chromatic** — *SaaS (actual category: hosted service, not a library)* — Cloud visual testing + review for Storybook; UI regression diffs, TurboSnap. — [https://www.chromatic.com](https://www.chromatic.com) — *Partially verified*
- **— Docz (historical)** — *Tool (unmaintained)* — Once-popular MDX docs tooling; project archived/unmaintained; superseded by Storybook docs mode / Docusaurus. — [https://github.com/doczjs/docz](https://github.com/doczjs/docz) — *Historical*

### B17. Agent-discoverability resources for frontend work

- **— frontend-nexus (thegbosstv/frontend-nexus)** — *Knowledge base (actual category: docs site for agents/humans, not a library)* — Per-library MDX entries (react-hook-form, zod, etc.) written for agent consumption: API patterns, resolver matrices, Proxy/subscription semantics. — [https://github.com/thegbosstv/frontend-nexus](https://github.com/thegbosstv/frontend-nexus) — *Partially verified*
- **— ai-web-design-codex (eneryleen/ai-web-design-codex)** — *Knowledge base* — Curated chapters: frameworks-for-design, component-libraries-headless, css-styling-and-tailwind, design-systems-and-tokens, accessibility, webgl-3d-shaders, animation-libraries-stack; includes "rules at a glance" (e.g., headless-library selection rules, the shadcn "beige problem"). — [https://github.com/eneryleen/ai-web-design-codex](https://github.com/eneryleen/ai-web-design-codex) — *Partially verified*
- **— ui-forager-skill (helix98/ui-forager-skill)** — *Skill (references/libraries.md)* — Curated library reference (shadcn, Base UI, Ark UI, Ariakit, Headless UI, React Aria, Radix Themes) guiding agents to install real components from registries instead of rebuilding. — [https://github.com/helix98/ui-forager-skill](https://github.com/helix98/ui-forager-skill) — *Partially verified*
- **— ai-skills-full-stack ui-registries (darrencasper/ai-skills-full-stack)** — *Skill* — "Which library for what" mapping across Aceternity/Magic UI/Cult/Origin/Animate/Kibo/Tailark/21st.dev with install routes and coexistence rules. — [https://github.com/darrencasper/ai-skills-full-stack](https://github.com/darrencasper/ai-skills-full-stack) — *Partially verified*
- **— plief-lobster library/ (emanueldssss/plief-lobster)** — *Knowledge base* — `library/ui-primitives.md` (headless comparison table) and `library/motion.md` (animation ladder incl. native-first checks) written as agent-consumable references. — [https://github.com/emanueldssss/plief-lobster](https://github.com/emanueldssss/plief-lobster) — *Partially verified*
- **— ericks-design-store (erickalfaro/ericks-design-store)** — *Tool + skill (actual category: agent-facing icon sourcing tool)* — 44k+ icons across Lucide/Phosphor/Tabler/Heroicons/Material Symbols/etc.; CLI outputs SVG/React/Vue/Svelte; browsable gallery; `.claude/skills/design-icons/`; Iconify JSON as source of truth. — [https://github.com/erickalfaro/ericks-design-store](https://github.com/erickalfaro/ericks-design-store) — *Partially verified*
- **— devpantry icons (allwin-antony/devpantry)** — *Knowledge base + scripts* — Catalog of 100%-open icon libraries with comparison matrix, license guide (attribution traps), fetch/sync/export scripts, web integration guide. — [https://github.com/allwin-antony/devpantry](https://github.com/allwin-antony/devpantry) — *Partially verified*
- **— stealthis resources (foodhy/stealthis)** — *Knowledge base* — Structured resource entries (name/url/description/bestFor/pros/cons/attributes/license) for animation and 3D web libraries. — [https://github.com/foodhy/stealthis](https://github.com/foodhy/stealthis) — *Partially verified*

*190 records in this category.*

## 3. Backend frameworks and APIs

Backend languages/frameworks, GraphQL, RPC, API gateways, OpenAPI/schema-first tooling, auth/identity, serverless & edge, real-time servers/queues/workflow engines, OpenAPI→MCP conversion. Source: `catalogs/01c-backend-data-platforms.md` §§3.5.x.

### 3.5.1 Backend languages & frameworks

- **Express.js** — *Open-source library/framework (npm)* — Minimal, unopinionated Node.js HTTP framework; the de facto standard server framework for Node.js and the backend of MERN/MEAN stacks. — [https://expressjs.com](https://expressjs.com) — *Partially verified*
- **Fastify** — *Open-source library/framework (npm)* — Performance-focused Node.js framework with a plugin architecture and built-in JSON-schema validation/serialization. — [https://fastify.io](https://fastify.io) — *Partially verified*
- **Hono** — *Open-source library/framework (npm)* — Ultralight, dependency-free TypeScript framework on Web Standard APIs; multi-runtime (Cloudflare Workers, Deno, Bun, Node, AWS Lambda). — [https://github.com/honojs/hono/](https://github.com/honojs/hono/) — *Partially verified*
- **NestJS** — *Open-source framework (npm, CLI)* — Opinionated, Angular-inspired TypeScript framework with modules, dependency injection, guards, interceptors; ships adapters for Express and Fastify. — [https://nestjs.com](https://nestjs.com) — *Partially verified*
- **FastAPI** — *Open-source library/framework (PyPI)* — Type-hint-driven Python framework with automatic request validation (Pydantic) and auto-generated OpenAPI docs (Swagger UI at `/docs`, ReDoc at `/redoc`). — [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com) — *Partially verified*
- **Django** — *Open-source framework (PyPI)* — Batteries-included Python framework: ORM, admin panel, auth, migrations, security defaults (CSRF/XSS/SQL-injection protections). — [https://www.djangoproject.com](https://www.djangoproject.com) — *Partially verified*
- **Flask** — *Open-source library/framework (PyPI)* — Minimal WSGI framework; routing + request handling, everything else via extensions. — [https://flask.palletsprojects.com](https://flask.palletsprojects.com) — *Partially verified*
- **Ruby on Rails** — *Open-source framework (RubyGems)* — Convention-over-configuration full-stack framework: ActiveRecord ORM, Action Pack, Hotwire; scaffold-driven productivity. — *Partially verified*
- **Laravel** — *Open-source framework (Composer)* — Expressive PHP framework with Artisan CLI, Eloquent ORM, queues, Blade templates; Octane for high performance. — [https://laravel.com](https://laravel.com) — *Partially verified*
- **Spring Boot** — *Open-source framework (Maven/Gradle)* — Opinionated Java framework with auto-configuration, embedded servers (Tomcat/Jetty/Undertow), and "starters" for web, data, security, messaging (Kafka/RabbitMQ), batch. — [https://spring.io/projects/spring-boot](https://spring.io/projects/spring-boot) — *Partially verified*
- **ASP.NET Core** — *Open-source framework (NuGet)* — High-performance C# framework (Kestrel server) for APIs and web apps; first-class OpenAPI support in recent versions. — *Partially verified*
- **Gin** — *Open-source library/framework (Go modules)* — Minimal, fast Go framework with martini-like routing, middleware, JSON binding/validation. — [https://gin-gonic.com](https://gin-gonic.com) — *Partially verified*
- **Encore** — *Open-source framework + optional hosted cloud* — Type-safe backend framework where infrastructure (databases, pub/sub, caches, cron, object storage, secrets) is declared as typed code primitives; the framework provisions matching infra locally and in cloud. Auto-generates API docs, OpenAPI, and typed client SDKs from the same types. Ships an MCP server for AI agents (per third-party API directory). — [https://encore.dev](https://encore.dev) — *Partially verified*

### 3.5.2 GraphQL servers & backends

- **Apollo Server** — *Open-source library (npm) + commercial platform (Apollo GraphOS)* — Self-hosted GraphQL server for Node.js; pairs with Apollo Client and the Apollo GraphOS platform (schema registry, gateway/federation). — *Partially verified*
- **Hasura** — *Open-source engine (Haskell/Go) + hosted cloud (Hasura Cloud)* — Generates type-safe GraphQL and REST APIs from database schemas (Postgres-first, plus others); metadata-driven with console UI, auth webhooks, remote schemas, event triggers. — *Partially verified*
- **PostGraphile** — *Open-source library/CLI (npm)* — Introspects a Postgres schema and serves a full GraphQL API (CRUD, relations, RLS-aware auth) with plugin extensibility. — *Partially verified*
- **GraphQL Yoga** — *Open-source library (npm)* — Lightweight, plugin-based GraphQL server on modern fetch/Web Standards; Envelop plugin ecosystem. — *Partially verified*

### 3.5.3 RPC & service-to-service

- **tRPC** — *Open-source library (npm)* — TypeScript RPC framework: define procedures server-side, get fully typed client calls with no codegen step; uses JSON over HTTP, integrates with React Query. — *Partially verified*
- **gRPC / ConnectRPC** — *Open-source frameworks + spec (protobuf)* — gRPC: contract-first RPC with Protocol Buffers, codegen for many languages, streaming. ConnectRPC: simpler protocol (Connect/Connect-ES) that works over HTTP/1.1 with browser-friendly semantics and gRPC compatibility. — *Partially verified*

### 3.5.5 OpenAPI, schema-first design, codegen, contract testing

- **OpenAPI Specification** — *Open specification (machine-readable API contracts: JSON/YAML)* — Standard description format for REST APIs: paths, operations, schemas, security; versions 3.0/3.1 (JSON Schema aligned). — *Partially verified*
- **Swagger UI / ReDoc / Scalar** — *Open-source tools (Swagger UI — SmartBear/Apache 2* — Interactive API reference UIs generated from OpenAPI documents; Scalar also publishes OpenAPI→MCP guidance. — *Partially verified*
- **openapi-generator** — *Open-source CLI/tool (Java)* — Community-driven generator producing client SDKs, server stubs, and docs for 50+ languages/frameworks from OpenAPI specs. — *Partially verified*
- **Fern & Speakeasy (modern API SDK platforms)** — *Commercial platforms with open-source generators* — Next-gen codegen: Fern generates docs + idiomatic SDKs (TS/Python/Go/Java/Ruby/C#) from OpenAPI; Speakeasy similar, with Terraform providers and MCP-relevant outputs. — *Partially verified*
- **Kiota & Orval (lightweight client generators)** — *Open-source CLIs* — Kiota: Microsoft's OpenAPI→typed-client generator (.NET/Java/TS/Python/Go/PHP/Ruby/Swift). Orval: generates TypeScript clients, mock handlers (MSW), and Zod schemas from OpenAPI. — *Partially verified*
- **Spectral** — *Open-source CLI (npm)* — Ruleset-driven linter for API description documents: style, consistency, and breaking-change rules. — *Partially verified*
- **Schemathesis** — *Open-source CLI (Python) + commercial* — Generates test cases from OpenAPI/GraphQL schemas (Hypothesis-powered), finds crashes, validation and spec-conformance errors. — *Partially verified*
- **Prism** — *Open-source CLI/server (npm)* — Turns an OpenAPI document into a mock API server (example/dynamic responses) and a contract validator/proxy. — *Partially verified*
- **Pact** — *Open-source framework + PactFlow (commercial)* — Consumer-driven contracts: consumers define expected interactions, providers verify; language-specific implementations; PactFlow broker for CI. — *Partially verified*
- **MSW (Mock Service Worker)** — *Open-source library (npm)* — Intercepts network requests at the network level (browser Service Worker / Node interceptor) for tests, Storybook, and local dev. — *Partially verified*
- **Microcks** — *Open-source platform (containers)* — Imports OpenAPI/AsyncAPI/Postman collections to serve mocks and run contract tests; K8s-native, Testcontainers-friendly. — *Partially verified*
- **oasdiff** — *Open-source CLI* — Diffs two OpenAPI specs, flags breaking changes, renders changelogs; CI-friendly. — *Partially verified*

### 3.5.6 Identity, auth/authz, sessions

- **Keycloak** — *Open-source server (Java/Quarkus) + admin UI* — Self-hosted identity and access management: SSO, OAuth2/OIDC, SAML, LDAP/AD federation, user federation, social login, fine-grained authorization services. — [https://www.keycloak.org](https://www.keycloak.org) — *Partially verified*
- **Ory (Kratos / Hydra / Keto / Oathkeeper)** — *Open-source services (Go) + Ory Cloud (managed)* — Modular IAM: Kratos (user management/login/registration/MFA), Hydra (OAuth2/OIDC provider), Keto (permissions, Zanzibar-style), Oathkeeper (identity-aware proxy). — [https://www.ory.sh/kratos](https://www.ory.sh/kratos) — *Partially verified*
- **ZITADEL** — *Open-source platform (Go) + ZITADEL Cloud* — Identity management with organizations/projects multi-tenancy, OIDC/OAuth2/SAML, passwordless, machine users, APIs-first. — [https://zitadel.com](https://zitadel.com) — *Partially verified*
- **better-auth** — *Open-source library (npm)* — Framework-agnostic TS auth library (email/password, social OAuth, magic links, passkeys, 2FA, organizations, admin); plugin architecture; the Auth.js team recommends new projects start with Better Auth (see 3.5.6.5). — [https://www.better-auth.com](https://www.better-auth.com) — *Partially verified*
- **Auth.js (next-auth) — Corrected** — *Open-source library (npm)* — The long-standard Next.js/Auth.js authentication library. **Correction (Verified, 2026-10-10):** the `nextauthjs/next-auth` README (opened this session) states Auth.js is now part of Better Auth; maintainers recommend new projects start with Better Auth instead, except specific gaps (notably stateless sessions without a database). — [https://authjs.dev](https://authjs.dev) — *Verified*
- **Lucia — Historical note** — *Open-source library (was npm)* — Minimal session-management library popular in 2023–2024. Project was discontinued by its author (widely reported; community forks exist). **Status: Historical** — do not adopt for new work; see better-auth. — *Historical*

### 3.5.7 Serverless & edge compute

- **Cloudflare Workers** — *Hosted platform (proprietary runtime, open Workers SDK/tooling)* — V8-Isolate-based functions at Cloudflare's edge; bindings to KV, R2, D1, Durable Objects, Queues; Wrangler CLI. — *Partially verified*
- **AWS Lambda** — *Hosted service* — Event-driven functions (many runtimes incl. custom), wired to API Gateway/SQS/EventBridge/S3 events. — *Partially verified*
- **Vercel Functions** — *Hosted platform (tied to Vercel deployments)* — Functions co-located with frontend deployments (`/api` routes, Server Actions); Fluid compute model. — *Partially verified*

### 3.5.8 Real-time servers, queues, brokers, workflow engines

- **Socket.IO** — *Open-source library (npm) — client + server* — Event-based bidirectional communication with fallbacks (WebSocket → polling), rooms/namespaces, multiplexing; adapters for Redis/Postgres scaling. — *Partially verified*
- **Ably & Pusher — hosted real-time** — *Hosted services with SDKs* — Managed WebSocket pub/sub with channels, presence, history, push integrations; Pusher Channels/Beams; Ably emphasizes guarantees (ordering, exactly-once-ish semantics) and protocol adapters (MQTT/SSE). — *Partially verified*
- **Temporal** — *Open-source server (Go) + SDKs + Temporal Cloud* — Workflows-as-code with durable state: write workflows in code (TS/Python/Go/Java/.NET/PHP), survive crashes/restarts; event history, timers, signals. — *Partially verified*
- **Inngest** — *Open-source (core) + hosted platform* — Durable execution via `step.run`/`step.sleep` in plain functions; events trigger workflows; works on serverless. — *Partially verified*
- **Trigger.dev** — *Open-source platform (self-host or cloud)* — Define jobs in code with retries, delays, schedules, concurrency; dashboard + integrations (AI providers, etc.). — *Partially verified*
- **Restate** — *Open-source runtime + SDKs* — Durable workflows/virtual objects over HTTP services; journaled execution, exactly-once semantics, Kafka integration. — *Partially verified*
- **Hatchet** — *Open-source engine (Go) + Hatchet Cloud* — Durable task queue with workflows (DAGs), retries, rate limits, cron, workers in TS/Python/Go. — *Partially verified*
- **BullMQ** — *Open-source library (npm) + BullMQ Pro (commercial)* — Redis-backed job queue: priorities, delays, retries, rate limiting, flows (parent/child), repeatable jobs; dashboard (Arena/own UI). — *Partially verified*
- **Celery** — *Open-source library (PyPI)* — Python task queue with brokers (RabbitMQ/Redis/SQS), beat scheduler, canvas workflows, result backends. — *Partially verified*
- **Sidekiq** — *Open-source (core) + Pro/Enterprise* — Multithreaded Ruby job processor backed by Redis; web UI, retries, scheduled jobs; Rails integration via Active Job. — *Partially verified*
- **QStash** — *Hosted service (HTTP API)* — HTTP-based queue for serverless: publish to any HTTPS endpoint with retries, delays, schedules, DLQ; no broker to run. — *Partially verified*
- **Message brokers: Kafka / RabbitMQ / NATS / Redpanda / Pulsar** — *Open-source brokers (+ managed clouds)* — - **Apache Kafka:** distributed event streaming log; high throughput, partitioning, retention; ecosystem (Kafka Streams, ksqlDB, Connect). — *Partially verified*

### 3.5.9 OpenAPI → MCP conversion tools (machine-readable API contracts)

- **bbonnin/openapi-to-mcp — Verified** — *Open-source CLI (npm: `openapi-to-mcp`)* — Generates a stdio MCP server from an OpenAPI 3.x spec (YAML/JSON, local or remote URL) so agents can call any REST API as tools. `npx openapi-to-mcp <spec>` scaffolds a ready-to-run server; supports auth headers, server variables, operation filtering; Docker image available. — [https://github.com/bbonnin/openapi-to-mcp](https://github.com/bbonnin/openapi-to-mcp) — *Verified*
- **TykTechnologies/api-to-mcp — Verified** — *Open-source tool (Go)* — Tyk's OpenAPI→MCP converter: generates MCP servers/tools from OpenAPI definitions; positioned alongside Tyk's API gateway/MCP offering. — [https://github.com/TykTechnologies/api-to-mcp](https://github.com/TykTechnologies/api-to-mcp) — *Verified*
- **Taskade @taskade/mcp-openapi-codegen** — *Open-source generator (npm) + blog documentation* — Generates MCP server code from OpenAPI specs; Taskade's blog documents the workflow. — *Unverified*
- **Speakeasy OpenAPI→MCP** — *Commercial platform feature (generator open source)* — Speakeasy generates MCP servers alongside SDKs/Terraform providers from OpenAPI specs. — *Unverified*
- **FastMCP.from_openapi() & openapi-mcp-generator (npm)** — *Open-source library helpers* — FastMCP exposes helpers to build MCP servers directly from OpenAPI specs in Python; the npm `openapi-mcp-generator` package offers a JS-side generator. — *Unverified*
- **HelpCode-ai/anythingmcp** — *Open-source repo (per search listing)* — Appears in OpenAPI→MCP tooling discussions as a generic/adapter MCP server project. — *Unresolved*
- **Apollo MCP Server** — *Open-source tool (per Apollo announcements)* — Exposes GraphQL operations as MCP tools, letting agents query federated graphs through the Model Context Protocol. — *Unverified*

### 3.5.4 API gateways

- **Kong Gateway** — *Open source (core) + Enterprise* — Kong Inc. — Lua/OpenResty-based gateway; Kong Ingress Controller for K8s — Traffic control, auth plugins, rate limiting, transformations — *Partially verified*
- **Apache APISIX** — *Open source (Apache 2.0)* — Apache Software Foundation — dynamic, etcd-backed gateway — Dynamic routing, hot-reload plugins, gRPC/GraphQL proxying; comparison guide at https://apisix.apache.org/learning-center/open-source-api-gateway-comparison/ (verbatim URL as returned; includes tracking params) — [https://apisix.apache.org/learning-center/open-source-api-gateway-comparison/](https://apisix.apache.org/learning-center/open-source-api-gateway-comparison/) — *Partially verified*
- **Traefik** — *Open source (MIT) + Enterprise* — Traefik Labs — cloud-native reverse proxy / ingress — Auto service discovery (Docker/K8s), Let's Encrypt, middleware chain — *Partially verified*
- **KrakenD** — *Open source (Apache 2.0) + Enterprise* — KrakenD (ex-Lura) — declarative, stateless API gateway — JSON config, request aggregation/composition, no DB required — *Partially verified*
- **Tyk** — *Open source (MPL) + Cloud/Enterprise* — Tyk — API gateway & management platform — Gateway, dashboard, developer portal; also ships an OpenAPI→MCP tool (see 3.5.9.2) — *Partially verified*

*64 records in this category.*

## 4. Databases and data infrastructure

Relational, serverless Postgres, NoSQL, vector DBs, search engines, ORMs, migrations, caching/object storage, admin UIs, database MCP servers and agent-readable schema resources. Source: `catalogs/01c-backend-data-platforms.md` §§3.6.x.

### 3.6.1 Relational databases

- **PostgreSQL** — *Open-source database server* — The default serious open-source RDBMS: ACID, JSONB, full-text search, PostGIS, extensions (pgvector, Timescale), logical replication, RLS. — [https://www.postgresql.org](https://www.postgresql.org) — *Partially verified*
- **MySQL** — *Open-source DBMS (GPL) + commercial editions* — Widely deployed RDBMS (WordPress/LAMP heritage); InnoDB engine; MySQL 8.x line; HeatWave in OCI. — [https://www.mysql.com](https://www.mysql.com) — *Partially verified*
- **SQLite / libSQL** — *Open-source embedded library + (libSQL) server mode* — Serverless, zero-config, single-file SQL database; ubiquitous in mobile/edge/desktop. libSQL adds server mode + replication (Turso's fork). — [https://www.sqlite.org](https://www.sqlite.org) — *Partially verified*
- **CockroachDB** — *Database (source-available license) + CockroachDB Cloud* — Postgres-wire-compatible distributed database: horizontal scale, multi-region survivability. — *Partially verified*
- **TimescaleDB** — *Postgres extension (open source core) + Timescale Cloud* — Hypertables, compression, continuous aggregates, retention policies on Postgres. — *Partially verified*

### 3.6.2 Serverless / hosted Postgres

- **Neon** — *Hosted database service (open-source components)* — Serverless Postgres with autoscaling, branching (DB branching for dev/preview), scale-to-zero; storage/compute separation. **Corrected status:** acquired by Databricks (announced May 2025 — widely reported). — *Partially verified*
- **Supabase** — *Open-source platform (self-hostable) + hosted cloud* — Postgres + auto-generated REST (PostgREST) & GraphQL (pg_graphql) + Auth (GoTrue) + Storage + Realtime + Edge Functions + pgvector. — *Partially verified*
- **PlanetScale** — *Hosted database service* — MySQL-compatible serverless platform with branching; **status change:** free tier removed March 2024 (widely reported) — now paid-focused with usage pricing. — *Partially verified*
- **Turso (libSQL)** — *Hosted database service (libSQL open source)* — Replicated SQLite at the edge; **status change:** scale-to-zero deprecated January 2026 (secondary reports) — always-on model now. — *Partially verified*
- **Prisma Postgres** — *Hosted database service* — Prisma's managed Postgres (formerly Accelerate/Optimize lineage), paired with Prisma ORM; connection pooling, edge caching. — *Partially verified*
- **PostgREST** — *Open-source server (Haskell binary)* — Serves a REST API directly from the Postgres schema (tables/views → routes), RLS-aware; the engine behind Supabase's REST layer. — *Partially verified*

### 3.6.3 NoSQL: document, key-value, wide-column, graph

- **MongoDB** — *Database (SSPL) + Atlas (managed)* — BSON document store: flexible schemas, aggregation pipeline, Atlas Search, transactions; Atlas is the managed cloud. **Archived:** MongoDB Atlas App Services (serverless backend/BaaS) reached end-of-life 2025-09-30 — confirmed by the official EOL notice on the Atlas App Services Admin API docs page; Atlas continues as a managed database. — [https://www.mongodb.com](https://www.mongodb.com) — *Partially verified*
- **Redis** — *Database (source-available) + Redis Cloud* — In-memory data structures server: strings/hashes/lists/sets/sorted sets, streams, pub/sub, Lua scripting, Redis Stack modules (JSON, search, vector, time-series, graph, Bloom). — [https://redis.io](https://redis.io) — *Partially verified*
- **Apache Cassandra** — *Open-source database* — Masterless wide-column store: linear write scale, tunable consistency, CQL. — *Partially verified*
- **Neo4j** — *Database (GPL community / commercial) + Aura (managed)* — Native property-graph DB with Cypher query language; Graph Data Science library; Aura managed cloud. — *Partially verified*
- **SurrealDB** — *Open-source database (Rust) + SurrealDB Cloud* — Single binary combining document, graph, relational tables, full-text and vector search; SurrealQL; live queries/real-time. — *Partially verified*
- **Kùzu** — *Open-source embedded library (C++)* — DuckDB-style embedded property-graph DB with Cypher; in-process analytics on graphs. — *Partially verified*

### 3.6.6 ORMs, query builders, data-access layers

- **Prisma** — *Open-source ORM (npm) + Prisma Postgres/Accelerate (hosted)* — Schema-first ORM: `schema.prisma` → typed client + migrations; supports Postgres/MySQL/SQLite/SQL Server/MongoDB/Cockroach. **Status change:** Prisma 7 is Rust-free (new TS engine lineage) — reported in 2026 ecosystem content. — *Partially verified*
- **Drizzle** — *Open-source library (npm)* — SQL-like, thin-layer TS ORM: schema in TS, relational queries, no heavy codegen; serverless-driver friendly. — *Partially verified*
- **SQLAlchemy** — *Open-source library (PyPI)* — Python's standard data-access layer: Core (SQL expression) + ORM (unit of work), Alembic migrations; pairs with FastAPI/Django-alternatives. — *Partially verified*
- **TypeORM** — *Open-source library (npm)* — Decorator-based TS ORM supporting many DBs; historically the NestJS default. — *Partially verified*

### 3.6.10 Database MCP servers & agent-readable schema resources

- **Convex — agent-grounded backend platform (gap-analysis candidate)** — *Open-source backend (Rust) + Convex Cloud (hosted)* — TypeScript-defined backend: `schema.ts` data model, queries/mutations/actions in TS with end-to-end type safety, realtime subscriptions, file storage, cron, full-text/vector search. The backend (`get-convex/convex-backend`, ~11k stars per fork README) was open-sourced; a community fork (`bulk-platform/convex-backend`) exists. Publishes official `convex-*` … — [https://docs.convex.dev](https://docs.convex.dev) — *Partially verified*
- **mongodb-mcp-server** — *Open source MCP server* — `mongodb-js/mongodb-mcp-server` — official MongoDB MCP — Schema exploration, query execution, Atlas admin — *Partially verified*
- **mcp-clickhouse** — *Open source MCP server* — `ClickHouse/mcp-clickhouse` — official ClickHouse MCP — Query ClickHouse, inspect schemas — *Partially verified*
- **mcp-server-neon** — *Open source MCP server* — `neondatabase/mcp-server-neon` — official Neon MCP — Branching, SQL, project mgmt via MCP — [https://github.com/neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) — *Partially verified*
- **supabase/mcp** — *Open source MCP server* — `supabase/mcp` (supabase-community) — Supabase project/SQL/storage via MCP — *Partially verified*
- **mcp-redis** — *Open source MCP server* — `redis/mcp-redis` — official Redis MCP — Redis commands/data via MCP — *Partially verified*
- **mcp-server-elasticsearch** — *Open source MCP server* — `elastic/mcp-server-elasticsearch` — ES queries/mappings via MCP — *Partially verified*
- **mcp-server-qdrant** — *Open source MCP server* — `qdrant/mcp-server-qdrant` — Vector search ops via MCP — *Partially verified*
- **chroma-mcp** — *Open source MCP server* — `chroma-core/chroma-mcp` — Chroma collections via MCP — *Partially verified*
- **pinecone-mcp** — *Open source MCP server* — `pinecone-io/pinecone-mcp` — Pinecone index ops via MCP — *Partially verified*
- **mcp-server-motherduck** — *Open source MCP server* — `motherduckdb/mcp-server-motherduck` — DuckDB cloud MCP — Query MotherDuck/DuckDB via MCP — *Partially verified*
- **postgres-mcp** — *Open source MCP server* — `crystaldba/postgres-mcp` — community Postgres MCP — Schema + SQL via MCP — *Partially verified*
- **hf-mcp-server** — *Open source MCP server* — `olaservo/hf-mcp-server` — Hugging Face MCP (fs tools) — HF dataset/model file ops via MCP — [https://github.com/olaservo/hf-mcp-server/blob/HEAD/packages/mcp/content/hf-fs/README.md](https://github.com/olaservo/hf-mcp-server/blob/HEAD/packages/mcp/content/hf-fs/README.md) — *Partially verified*

### 3.6.4 Vector databases & embeddings infra

- **Qdrant** — *Open source (Apache 2.0) + Cloud* — Qdrant — vector search engine (Rust) — HNSW, filtering, payload indexes, quantization; `qdrant/mcp-server-qdrant` for agents — *Partially verified*
- **Weaviate** — *Open source (BSD-3) + Cloud* — Weaviate — vector DB with modules — Hybrid search, modules (rerankers, generative), multi-tenancy — *Partially verified*
- **Pinecone** — *Hosted service* — Pinecone — managed vector DB — Serverless indexes, namespaces, metadata filtering; `pinecone-io/pinecone-mcp` — *Partially verified*
- **pgvector** — *Open-source Postgres extension* — pgvector — vector extension for Postgres — `vector` type, HNSW/IVFFlat indexes; zero new infra for Postgres users — *Partially verified*
- **Chroma** — *Open source (Apache 2.0)* — Chroma — embedding DB (Python-first) — Simple API, local/server modes; `chroma-core/chroma-mcp` — *Partially verified*
- **Milvus** — *Open source (Apache 2.0)* — Milvus — distributed vector DB (LF AI & Data) — Billion-scale, GPU indexes, Attu UI; Zilliz Cloud managed — *Partially verified*

### 3.6.5 Search engines

- **Elasticsearch** — *Source-available (SSPL/Elastic License) + Elastic Cloud* — Elastic — distributed search/analytics (Java) — Full-text, aggregations, ESQL, vector (dense_vector); `elastic/mcp-server-elasticsearch` — *Partially verified*
- **OpenSearch** — *Open source (Apache 2.0) + AWS managed* — OpenSearch — Apache-2.0 fork of Elasticsearch (AWS-led) — Full-text + vector (k-NN), security, alerting — *Partially verified*
- **Typesense** — *Open source (GPLv3) + Cloud* — Typesense — typo-tolerant search API (C++) — Instant search, faceting, geo, vector; simple API — *Partially verified*
- **Meilisearch** — *Open source (MIT) + Cloud* — Meilisearch — instant search engine (Rust) — Typo tolerance, ranking rules, multi-index; easy self-host — *Partially verified*
- **Algolia** — *Hosted service* — Algolia — hosted search & discovery APIs — Hosted indexes, NeuralSearch, Recommend; dashboards + SDKs (see also 3.7.7) — *Partially verified*

### 3.6.7 Schema migrations & database DevOps

- **Atlas (ariga)** — *Open source (Apache 2.0 core) + Cloud* — Ariga Atlas — "Like Terraform, for databases" — Declarative schema-as-code, versioned migrations, drift detection, CI; docs: https://atlasgo.io/?ref=blef.fr (verbatim) — [https://atlasgo.io/?ref=blef.fr](https://atlasgo.io/?ref=blef.fr) — *Partially verified*
- **Flyway** — *Open source (Apache 2.0 community) + Teams/Enterprise* — Redgate Flyway — versioned SQL migrations (Java) — Plain-SQL migrations, repeatable migrations, Teams features — *Partially verified*
- **Liquibase** — *Open source (Apache 2.0) + commercial* — Liquibase — DB change management (Java) — XML/YAML/SQL changelogs, contexts/labels, policy checks — *Partially verified*
- **Alembic** — *Open source (MIT)* — Alembic — SQLAlchemy migrations (Python) — Autogenerate diffs, versioned scripts — *Partially verified*
- **golang-migrate** — *Open source (MIT)* — golang-migrate/migrate — Go migration CLI/library — CLI + library, many DB/source drivers — *Partially verified*
- **dbmate** — *Open source (MIT)* — dbmate — lightweight migration tool — Single binary, plain SQL, framework-agnostic — *Partially verified*
- **Skeema** — *Open source (Apache 2.0; premium)* — Skeema — MySQL schema management — Declarative MySQL schemas, diff/push, lint — *Partially verified*

### 3.6.8 Caching & object/file storage

- **Dragonfly** — *Source-available (BSL) + Cloud* — Dragonfly — Redis-compatible in-memory store (C++) — Multi-threaded, Redis API compat, snapshots — *Partially verified*
- **Garnet** — *Open source (MIT)* — Garnet — .NET remote cache-store (Microsoft Research) — RESP compatible, high throughput, extensible — *Partially verified*
- **Upstash** — *Hosted service* — Upstash — serverless Redis/Kafka/QStash — Per-request pricing, REST API, edge replication (context7/skill dedup noted) — *Partially verified*
- **Memcached** — *Open source (BSD)* — Memcached — distributed memory cache — Simple KV sharding, minimal ops — *Partially verified*
- **Amazon S3** — *Hosted service* — AWS S3 — object storage — Buckets, versioning, lifecycle, presigned URLs — *Partially verified*
- **Cloudflare R2** — *Hosted service* — R2 — S3-compatible object storage, zero egress — S3 API compat, no egress fees — *Partially verified*
- **MinIO** — *Open source (AGPLv3) + commercial* — MinIO — self-hosted S3-compatible storage (Go) — Single binary, erasure coding, console — *Partially verified*
- **Supabase Storage** — *Open source (self-host) + hosted* — Supabase Storage — file storage on Postgres — Buckets, RLS policies, image transforms — *Partially verified*
- **Uploadthing** — *Hosted service + SDK* — Uploadthing — file upload APIs for TS apps — Upload components, callbacks, infra abstraction (see also 3.7.6) — *Partially verified*

### 3.6.9 Admin UIs, seed data, test environments

- **DBeaver** — *Open source (Apache 2.0 CE) + Pro* — DBeaver — universal DB client (Java) — SQL editor, ER diagrams, many drivers — *Partially verified*
- **pgAdmin** — *Open source (PostgreSQL licence)* — pgAdmin — Postgres administration — Web UI, query tool, server management — *Partially verified*
- **DataGrip** — *Commercial IDE* — DataGrip — JetBrains DB IDE — Refactoring, inspections, multi-DB — *Partially verified*
- **TablePlus** — *Commercial (freemium)* — TablePlus — native DB GUI (macOS/Windows) — Fast native client, plugins — *Partially verified*
- **Prisma Studio / Drizzle Studio** — *Bundled with ORMs* — ORM data browsers — Visual data editing for Prisma/Drizzle projects — *Partially verified*
- **Faker / factory_boy** — *Open source (Python/JS ports)* — Fake-data / fixture generators — Seed data, factories for tests — *Partially verified*
- **Testcontainers** — *Open source (MIT)* — Testcontainers — throwaway containers for tests — Postgres/Redis/Kafka etc. in integration tests — *Partially verified*
- **awesome-db-tools** — *Awesome-list (docs)* — `datlechin/awesome-db-tools` — curated DB tools list — CLI/GUI/backup/migration tool index — [https://github.com/datlechin/awesome-db-tools/blob/HEAD/README.md](https://github.com/datlechin/awesome-db-tools/blob/HEAD/README.md) — *Partially verified*

*69 records in this category.*

## Application services and reusable capabilities

Auth services, email, payments, notifications, maps, scheduling, media processing, search/analytics/flags, headless commerce, headless CMS, i18n, public datasets, API integration libraries. Additional category (beyond the Part-24 list, discovered during research). Source: `catalogs/01c-backend-data-platforms.md` §§3.7.x.

### 3.7.6 Scheduling

- **Cal.com — Corrected (closed-source, Apr 2026)** — *Hosted service (closed-source since 2026-04-14)* — Scheduling/booking platform. **Correction:** the production repo was privatized on 2026-04-14; the prior MIT repo (41.2k stars) is no longer public. The company published an MIT community fork `calcom/cal.diy`, feature-stripped: no Teams/Organizations, SAML/SCIM, Workflows, Routing Forms, Insights, AI agent (per cal.com blog, pinggy-io article, dayotter … — [https://cal.com/blog/cal-diy-open-source-to-closed-source](https://cal.com/blog/cal-diy-open-source-to-closed-source) — *Partially verified*
- **Cal.diy** — *Open-source app (Next* — The open MIT fork published by Cal.com at privatization; individual scheduling without enterprise modules. — *Partially verified*

### 3.7.1 Auth services (managed)

- **Clerk** — *Hosted service + SDKs* — Clerk — hosted auth (clerk.com) — Drop-in sign-in/user mgmt, orgs, passkeys; Supabase third-party-auth guide: http://supabase.com/docs/guides/auth/third-party/clerk (verbatim) — [http://supabase.com/docs/guides/auth/third-party/clerk](http://supabase.com/docs/guides/auth/third-party/clerk) — *Partially verified*
- **Auth0** — *Hosted service + SDKs* — Auth0 (Okta) — identity platform — Universal Login, Actions, orgs, MFA, attack protection — *Partially verified*
- **WorkOS** — *Hosted service + APIs* — WorkOS — B2B auth/SSO infra — SSO (SAML/OIDC), SCIM directory sync, admin portal — *Partially verified*
- **Supabase Auth** — *Open source (self-host) + hosted* — Supabase Auth (GoTrue) — Email/social/phone auth, RLS integration, MFA — [https://supabase.com/docs/guides/auth/auth-email-templates](https://supabase.com/docs/guides/auth/auth-email-templates) — *Partially verified*
- **Firebase Authentication** — *Hosted service + SDKs* — Google Firebase Auth — Phone/social/email, Identity Platform, App Check — *Partially verified*
- **Stytch — Corrected (Twilio)** — *Hosted service + SDKs* — Stytch — auth APIs, now a Twilio company — Passwordless, MFA, B2B; **acquisition announced 2025-10-30, closed 2025-11-14, $104.1M cash** (per druce/governance vendor wiki citing Twilio SEC filings twlo-20250930.htm, twlo-20251231.htm); brand/APIs continue under Twilio — [https://github.com/druce/governance/blob/HEAD/wiki/vendors/stytch.md](https://github.com/druce/governance/blob/HEAD/wiki/vendors/stytch.md) — *Partially verified*
- **Descope** — *Hosted service + SDKs* — Descope — drag-drop auth workflows — No-code auth flows, passkeys, MFA — *Partially verified*
- **FusionAuth** — *Open source (community) + Cloud* — FusionAuth — self-hostable CIAM — SSO, MFA, multi-tenancy, on-prem option — *Partially verified*
- **SuperTokens** — *Open source (core) + managed* — SuperTokens — open-source auth — Session mgmt, email/password, social, MFA; self-host — *Partially verified*
- **Kinde** — *Hosted service + SDKs* — Kinde — auth for SaaS — Orgs, billing hooks, fast integration — *Partially verified*
- **AWS Cognito** — *Hosted service (AWS)* — Amazon Cognito — user pools/identity pools — Hosted UI, federation, device tracking — *Partially verified*
- **MojoAuth** — *Hosted service + SDKs* — MojoAuth — passwordless auth — Magic links/OTP focused — *Partially verified*
- **Logto** — *Open source (core) + Cloud* — Logto — open-source Auth0 alternative — OIDC, organizations, RBAC, console — *Partially verified*
- **SSOJet** — *Hosted service + API* — SSOJet — SSO-as-API — Drop-in enterprise SSO — *Partially verified*

### 3.7.2 Email delivery

- **Resend** — *Hosted service + SDKs* — Resend — developer email API — React Email, deliverability, Supabase SMTP guide: https://resend.com/docs/send-with-supabase-smtp (verbatim) — [https://resend.com/docs/send-with-supabase-smtp](https://resend.com/docs/send-with-supabase-smtp) — *Partially verified*
- **Postmark** — *Hosted service + API* — Postmark — transactional email — Templates, inbound parsing, DMARC tooling — *Partially verified*
- **SendGrid** — *Hosted service + SDKs* — Twilio SendGrid — email API — Marketing + transactional, templates, stats — *Partially verified*
- **Mailgun** — *Hosted service + API* — Mailgun (Sinch) — email API — Validation, routes, deliverability — *Partially verified*
- **Amazon SES** — *Hosted service (AWS)* — AWS Simple Email Service — Low-cost SMTP/API, reputation dashboards — *Partially verified*
- **Mailtrap** — *Hosted service* — Mailtrap — email testing + sending — Fake SMTP for dev, templates, sending API — *Partially verified*
- **Plunk** — *Open source + hosted* — Plunk — open-source email platform (AGPL-3.0) — Campaigns + transactional; self-hostable — *Partially verified*
- **Brevo** — *Hosted service* — Brevo (ex-Sendinblue) — CRM + email — Marketing automation, SMS, chat — *Partially verified*

### 3.7.3 Payments & merchant-of-record

- **Stripe** — *Hosted service + SDKs/APIs* — Stripe — payments platform — Payments, Billing, Connect, webhooks, Radar — *Partially verified*
- **Paddle** — *Hosted service (MoR)* — Paddle — merchant of record — Handles tax/VAT, subscriptions, checkout — *Partially verified*
- **Lemon Squeezy — Corrected (Stripe)** — *Hosted service (MoR)* — Lemon Squeezy — MoR for SaaS, **acquired by Stripe (July 2024)** — Being folded into **Stripe Managed Payments** (Feb 2026 release per reports) — *Partially verified*
- **Polar** — *Open source + hosted MoR* — Polar — MoR for developers (open source) — Digital products, checkout, license keys — *Partially verified*
- **Dodo Payments** — *Hosted service (MoR)* — Dodo — MoR for global SaaS — Tax compliance, subscriptions — *Partially verified*
- **Creem** — *Hosted service (MoR)* — Creem — MoR for SaaS — Checkout, tax handling — *Partially verified*
- **Whop** — *Hosted service* — Whop — digital product marketplace/payments — Storefronts, affiliates, Discord gating — *Partially verified*
- **Stripe Managed Payments** — *Hosted service (MoR)* — Stripe's MoR offering (2026) — Successor surface for Lemon Squeezy merchants — *Partially verified*

### 3.7.4 Notifications

- **Knock** — *Hosted service + SDKs* — Knock — notification infrastructure — Workflows, preferences, batching, multi-channel — *Partially verified*
- **Courier** — *Hosted service + APIs* — Courier — notification orchestration — Designer, routing, providers abstraction — *Partially verified*
- **Novu** — *Open source (core) + Cloud* — Novu — open-source notification infra — Workflows, inbox, providers; docs: https://docs.novu.co (verbatim) — [https://docs.novu.co](https://docs.novu.co) — *Partially verified*
- **OneSignal** — *Hosted service + SDKs* — OneSignal — push/email/SMS — Journeys, segmentation, in-app — *Partially verified*
- **MagicBell** — *Hosted service + SDKs* — MagicBell — notification inbox — In-app inbox, preferences — *Partially verified*
- **Pingram** — *Hosted service (per listings)* — Pingram — notification service — Notification delivery — *Partially verified*
- **Customer.io** — *Hosted service* — Customer.io — lifecycle messaging — Behavioral triggers, campaigns — *Partially verified*

### 3.7.5 Maps & geolocation

- **Mapbox** — *Hosted service + SDKs* — Mapbox — maps platform — GL maps, geocoding, directions, Studio — *Partially verified*
- **Google Maps Platform** — *Hosted service + SDKs* — Google — maps APIs — Places, routes, geocoding, JS SDK — *Partially verified*
- **MapLibre** — *Open source (BSD-3)* — MapLibre — open map rendering (fork of Mapbox GL) — GL JS/Native, community-driven — *Partially verified*
- **Leaflet** — *Open source (BSD-2)* — Leaflet — lightweight JS map library — Simple interactive maps, plugins — *Partially verified*
- **OpenLayers** — *Open source (BSD-2)* — OpenLayers — full-featured JS mapping — Projections, WMS/WMTS, vector tiles — *Partially verified*
- **MapTiler** — *Hosted service + SDKs* — MapTiler — map tiles/hosting — Vector tiles, geocoding, self-host option — *Partially verified*
- **Stadia Maps** — *Hosted service* — Stadia — map tiles/APIs — Tiles, routing, static maps — *Partially verified*
- **LocationIQ** — *Hosted service* — LocationIQ — geocoding API — Forward/reverse geocode, autocomplete — *Partially verified*
- **HERE** — *Hosted service + SDKs* — HERE — location platform — Maps, routing, traffic, fleet — *Partially verified*
- **OpenCage** — *Hosted service* — OpenCage — geocoding API — Aggregated geocoders, generous free tier — *Partially verified*
- **Protomaps** — *Open source (BSD) + hosted* — Protomaps — open map stack — Single-file PMTiles, basemap, self-host — *Partially verified*

### 3.7.7 Media & file processing

- **Cloudinary** — *Hosted service + SDKs* — Cloudinary — media management — Upload, transforms, optimization, DAM — *Partially verified*
- **Mux** — *Hosted service + SDKs* — Mux — video API — Upload/encode/stream, player, analytics — *Partially verified*
- **Uploadthing** — *Hosted service + SDK* — Uploadthing — file uploads for TS — Components, callbacks (see 3.6.8.9) — *Partially verified*
- **ImageKit** — *Hosted service + SDKs* — ImageKit — image/video optimization — Real-time transforms, DAM, CDN — *Partially verified*
- **Shotstack** — *Hosted service + API* — Shotstack — video editing API — Templated video rendering — *Partially verified*
- **Creatomate** — *Hosted service + API* — Creatomate — video/image automation API — Template-based rendering — *Partially verified*
- **SammaPix** — *Hosted service (per listings)* — SammaPix — media service (per listings) — Media processing — *Partially verified*

### 3.7.9 E-commerce integrations (headless commerce)

- **Medusa** — *Open source (MIT) + Cloud* — Medusa — headless commerce (Node) — Modules (cart/order/payment), admin, storefront starters — [https://github.com/torkiv-labs/nexuq/blob/HEAD/docs/research/competitive-analysis-headless-commerce-2026-08-27.md](https://github.com/torkiv-labs/nexuq/blob/HEAD/docs/research/competitive-analysis-headless-commerce-2026-08-27.md) — *Partially verified*
- **Saleor** — *Open source (BSD-3) + Cloud* — Saleor — headless commerce (Python/Django) — GraphQL-first, channels, apps — *Partially verified*
- **Shopify / Hydrogen** — *Hosted + open-source Hydrogen (MIT)* — Shopify — commerce platform; Hydrogen (Remix storefront) — Storefront API, checkout, Hydrogen framework — *Partially verified*
- **Vendure** — *Open source (MIT) + Cloud* — Vendure — headless commerce (NestJS/TS) — Plugin architecture, admin UI, GraphQL — *Partially verified*
- **BigCommerce** — *Hosted service* — BigCommerce — SaaS commerce — Headless APIs, multi-storefront — *Partially verified*
- **commercetools** — *Hosted service (SaaS)* — commercetools — composable commerce — API-first, enterprise — *Partially verified*
- **Spree / Solidus** — *Open source (MIT/BSD)* — Spree/Solidus — Rails commerce — Rails storefronts, long-lived OSS — *Partially verified*

### 3.7.10 Headless CMS

- **Sanity** — *Hosted + open-source Studio (MIT)* — Sanity — structured content platform — GROQ queries, live preview, Studio editor — *Partially verified*
- **Contentful** — *Hosted service* — Contentful — headless CMS — Content APIs, Compose/Launch apps — *Partially verified*
- **Strapi** — *Open source (SEE license v5) + Cloud* — Strapi — open headless CMS (Node) — Admin panel, REST/GraphQL, plugins — *Partially verified*
- **Payload — Corrected (Figma)** — *Open source (MIT)* — Payload CMS — TS headless CMS, **acquired by Figma (June 2025)** — Admin UI auto-generated, Postgres/Mongo; MIT intact; Payload Cloud paused new sign-ups (per reports) — *Partially verified*
- **Directus** — *Open source (GPLv3) + Cloud* — Directus — headless data platform — Wraps SQL DBs with APIs + no-code app — *Partially verified*
- **Storyblok** — *Hosted service* — Storyblok — visual headless CMS — Visual editor, components — *Partially verified*
- **Hygraph** — *Hosted service* — Hygraph (ex-GraphCMS) — GraphQL CMS — GraphQL-native content APIs — *Partially verified*

### 3.7.11 i18n & localization services

- **Crowdin** — *Hosted service + API/CLI* — Crowdin — localization platform — Workflows, MT, translators marketplace — *Partially verified*
- **Lokalise** — *Hosted service + API* — Lokalise — localization platform — Keys, OTA, Figma plugin — *Partially verified*
- **Tolgee** — *Open source (Apache 2.0) + Cloud* — Tolgee — open-source i18n — In-context editing, SDKs — *Partially verified*
- **Transifex** — *Hosted service* — Transifex — localization platform — Workflows, native SDKs — *Partially verified*
- **Phrase** — *Hosted service* — Phrase (ex-Memsource) — localization suite — TMS + strings, MT — *Partially verified*
- **Localize** — *Hosted service* — Localize — JS translation — In-context JS library — *Partially verified*

### 3.7.12 Public datasets & data directories

- **Hugging Face Datasets** — *Open source (Apache 2.0) + Hub* — `datasets` library + Hub — 100k+ datasets, `hf://` URI scheme (newer), streaming, `hf-mcp-server` fs tools — [https://github.com/olaservo/hf-mcp-server/blob/HEAD/packages/mcp/content/hf-fs/README.md](https://github.com/olaservo/hf-mcp-server/blob/HEAD/packages/mcp/content/hf-fs/README.md) — *Partially verified*
- **Kaggle** — *Hosted platform* — Kaggle — datasets/competitions (Google) — Datasets, notebooks, competitions — *Partially verified*
- **Common Crawl** — *Open data (nonprofit)* — Common Crawl — web crawl corpus — Petabyte-scale crawls, columnar indexes — *Partially verified*
- **OpenAlex** — *Open data (nonprofit) + API* — OpenAlex — scholarly data API — Works/authors/venues graph, free API — *Partially verified*
- **awesome-public-datasets** — *Awesome-list (docs)* — `awesomedata/awesome-public-datasets` — Topic-indexed public datasets — [https://github.com/awesomedata/awesome-public-datasets/](https://github.com/awesomedata/awesome-public-datasets/) — *Partially verified*

### 3.7.13 API integration libraries

- **Composio** — *Platform + `composiohq/skills` (dedup)* — Composio — managed tool integrations (see skills workstream — cross-ref only) — 250+ app integrations as agent tools — *Not labeled*
- **Nango** — *Open source (MIT) + Cloud* — Nango — product integrations platform (OAuth/proxy) — 300+ integrations, unified APIs, sync — *Partially verified*
- **Merge** — *Hosted service + SDKs* — Merge — unified B2B APIs (HR/ATS/CRM) — Normalized HR/accounting/CRM APIs — *Partially verified*
- **Apideck** — *Hosted service + SDKs* — Apideck — unified APIs — CRM/HR/accounting normalization, Vault — *Partially verified*

*86 records in this category.*

## 5. Website builders and application generators

AI website/app builders, visual/low-no-code platforms, scaffolding code generators, screenshot/design-to-code, CRUD/admin generators, boilerplates/starters, landing-page and e-commerce builders. Source: `catalogs/01c-backend-data-platforms.md` §§3.8.x.

### 3.8.1 AI website/app builders (prompt-to-app)

- **Lovable** — *Hosted service* — Lovable — AI app builder — Prompt → full-stack app, Supabase/GitHub integration — *Partially verified*
- **Bolt.new (+ bolt.diy)** — *Hosted service + open fork* — Bolt.new (StackBlitz) — prompt-to-app; `bolt.diy` community fork — In-browser dev (WebContainers), fork self-hostable — *Partially verified*
- **v0** — *Hosted service* — v0 (Vercel) — AI UI generation — Prompt → React/shadcn components, Vercel deploy — *Partially verified*
- **Replit Agent** — *Hosted service* — Replit — AI agent workspace — Agent builds/deploys apps in Replit — *Partially verified*
- **Taskade Genesis** — *Hosted service* — Taskade — AI agents/workspace builder — Agent workflows + app generation — *Partially verified*
- **Dyad** — *Open-source-ish app (per listings; license not verified)* — Dyad — local AI app builder — Local-first AI builder, Supabase connect — *Partially verified*
- **Massvai** — *Hosted service (per listings)* — Massvai — AI website builder (per listings) — AI site generation — *Partially verified*
- **Onlook** — *Open source (MIT)* — Onlook — open-source visual AI builder (MIT, ~25.9k stars) — Visual editor + AI, Next.js/Tailwind — *Partially verified*
- **Google Stitch** — *Hosted (Google Labs)* — Google Stitch (Labs) — AI UI design — Prompt → UI designs, Figma export — *Partially verified*

### 3.8.2 Visual dev & low/no-code platforms

- **Webflow** — *Hosted service* — Webflow — visual web builder — Designer, CMS, Logic, hosting — *Partially verified*
- **Framer** — *Hosted service* — Framer — design-to-site — Figma-like canvas → site, CMS, effects — *Partially verified*
- **Bubble** — *Hosted service* — Bubble — no-code web apps — Visual programming, DB, plugins — *Partially verified*
- **FlutterFlow** — *Hosted service* — FlutterFlow — visual Flutter builder — Firebase/Supabase backends, code export — *Partially verified*
- **Softr** — *Hosted service* — Softr — Airtable/Sheets → apps — Portals, internal tools — *Partially verified*
- **Glide** — *Hosted service* — Glide — spreadsheets → apps — Mobile/web apps from data — *Partially verified*
- **Retool** — *Hosted/self-host* — Retool — internal tools builder — Drag-drop admin panels, 100+ integrations — *Partially verified*
- **Appsmith** — *Open source (Apache 2.0) + Cloud* — Appsmith — open internal tools — Widgets, JS queries, self-host — *Partially verified*
- **Budibase** — *Open source (GPLv3) + Cloud* — Budibase — open low-code — Internal apps, automations — *Partially verified*
- **NocoBase** — *Open source (AGPLv3) + commercial* — NocoBase — open no-code platform — Data-model-driven apps, plugins — *Partially verified*
- **ToolJet** — *Open source (GPLv3) + Cloud* — ToolJet — open low-code — App builder, workflows — *Partially verified*

### 3.8.3 Code generators (scaffolding)

- **Yeoman** — *Open source (BSD-2)* — Yeoman — scaffolding system (`yo`) — Generators ecosystem (`generator-*`) — *Partially verified*
- **Plop** — *Open source (MIT)* — Plop — micro-generator — In-repo templates, CLI prompts — *Partially verified*
- **Hygen** — *Open source (MIT)* — Hygen — code generator — Templates + CLI, Rails-like generators — *Partially verified*
- **Cookiecutter** — *Open source (BSD-3)* — Cookiecutter — project templates (Python) — Cross-language templating — *Partially verified*

### 3.8.4 Screenshot/design-to-code

- **screenshot-to-code** — *Open source (per repo)* — `abi/screenshot-to-code` — GPT-4 Vision → code — Screenshot/mockup → HTML/Tailwind/React — [https://github.com/abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) — *Partially verified*
- **Builder.io Visual Copilot** — *Hosted service + open parts* — Builder.io — visual headless CMS + AI — Figma → code, Visual Copilot — *Partially verified*
- **Anima** — *Hosted service + plugin* — Anima — design-to-code — Figma → React/HTML — *Partially verified*
- **Locofy** — *Hosted service + plugin* — Locofy — design-to-code — Figma/XD → React/Next/Vue — *Partially verified*
- **TeleportHQ** — *Hosted service + open codegen* — TeleportHQ — low-code front-end — Design → code, open-source generators — *Partially verified*
- **Uizard** — *Hosted service* — Uizard — AI wireframe/design — Screenshot/sketch → editable UI — *Partially verified*
- **Fronty** — *Hosted service* — Fronty — image-to-HTML — Screenshot → HTML/CSS — *Partially verified*
- **Figma Dev Mode MCP** — *Hosted feature (Figma)* — Figma — official MCP server — Design context → code agents — *Partially verified*
- **Magic Patterns** — *Hosted service* — Magic Patterns — AI prototyping — Prompt → prototypes — *Partially verified*

### 3.8.5 CRUD/admin & backend scaffolding generators

- **Refine** — *Open source (MIT)* — Refine — React CRUD framework (34.8k stars) — Data providers, auth, auto UI from APIs — *Partially verified*
- **Amplication** — *Open source + Cloud* — Amplication — backend codegen — DB schema → Node/NestJS/Prisma backend + admin — *Partially verified*
- **JHipster** — *Open source (Apache 2.0)* — JHipster — full-stack generator (Java+JS) — Spring Boot + Angular/React/Vue scaffolds — *Partially verified*
- **AdminLTE** — *Open source (MIT)* — AdminLTE — admin dashboard template (45k stars) — Bootstrap admin theme — *Partially verified*
- **Forest Admin** — *Hosted service* — Forest Admin — admin panel as service — Auto admin from DB, roles — *Partially verified*

### 3.8.6 Boilerplates, starters, full-stack templates

- **ShipFast** — *Commercial template* — ShipFast — Next.js SaaS boilerplate — Auth/payments/email wired — *Partially verified*
- **Supastarter** — *Commercial template* — Supastarter — SaaS starter (Next/Nuxt/Svelte) — Multi-framework starters — *Partially verified*
- **MakerKit** — *Commercial template* — MakerKit — SaaS kits (Next/Remix) — Supabase/Firebase variants — *Partially verified*
- **SaaS Pegasus** — *Commercial template* — SaaS Pegasus — Django SaaS boilerplate — Django all-in-one — *Partially verified*
- **open-saas** — *Open source (MIT)* — `wasp-lang/open-saas` — free SaaS template — Wasp + React + Node SaaS starter — [https://github.com/wasp-lang/open-saas](https://github.com/wasp-lang/open-saas) — *Partially verified*
- **create-t3-app** — *Open source (MIT)* — `t3-oss/create-t3-app` — T3 stack CLI — Next.js + tRPC + Tailwind + Prisma/NextAuth — *Partially verified*
- **create-next-app** — *Open source (MIT)* — Next.js official scaffolder — `create-next-app` templates — *Partially verified*
- **LaunchKit** — *Commercial template* — LaunchKit — PHP/Laravel kits (per listings) — Laravel starters — *Partially verified*
- **Gravity** — *Commercial template* — Gravity — Rails SaaS boilerplate (per listings) — Rails + Stripe — *Partially verified*
- **LaraCopilot** — *Product (per listings)* — LaraCopilot — Laravel AI starter (per listings) — Laravel scaffolding — *Partially verified*
- **NuxSaaS** — *Commercial/open (per listings)* — NuxSaaS — Nuxt SaaS template — Nuxt + Supabase — *Partially verified*
- **GoVueKit** — *Template (per listings)* — GoVueKit — Go+Vue starter (per listings) — Go backend + Vue — *Partially verified*
- **RedwoodJS** — *Open source (MIT)* — RedwoodJS — full-stack React framework — Opinionated GraphQL+Prisma+React — *Partially verified*
- **Wasp** — *Open source (MIT)* — Wasp — full-stack DSL (see open-saas) — Config-as-code full-stack — *Partially verified*
- **AdonisJS** — *Open source (MIT)* — AdonisJS — Node MVC framework — Laravel-like Node, Lucid ORM — *Partially verified*
- **Nuxt** — *Open source (MIT)* — Nuxt — Vue full-stack framework — SSR, server engine (Nitro) — *Partially verified*
- **Ant Design Pro** — *Open source (MIT)* — `ant-design/ant-design-pro` (38.3k stars) — admin template — Enterprise admin scaffolding — *Partially verified*

### 3.8.7 Landing-page & e-commerce builders

- **Unicorn Platform** — *Hosted service* — Unicorn Platform — landing pages for startups — AI copy, templates, blog — *Partially verified*
- **Carrd** — *Hosted service (freemium)* — Carrd — one-page sites — Simple landing pages — *Partially verified*
- **Typedream** — *Hosted service* — Typedream — Notion-like site builder — Doc-style websites — *Partially verified*
- **Shopify** — *Hosted service* — Shopify — commerce platform (hosted) — Storefronts, checkout, apps — *Partially verified*
- **WooCommerce** — *Open source (GPL) plugin* — WooCommerce — WordPress commerce — Self-hosted stores on WP — *Partially verified*

*60 records in this category.*

## Architecture and software engineering references

System-design guides, design patterns, domain modeling, ADRs, architecture modeling/documentation, dependency analysis. Additional category discovered during research. Source: `catalogs/01c-backend-data-platforms.md` §§3.9.x.

### 3.9.1 System design & architecture guides

- **system-design-primer** — *Reference repo (docs)* — `donnemartin/system-design-primer` (367k stars) — Org of topics, Anki cards, interview prep — [https://github.com/donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) — *Partially verified*
- **nodebestpractices** — *Reference repo (docs)* — `goldbergyoni/nodebestpractices` (106k stars) — 80+ Node best practices, translations — *Partially verified*
- **bulletproof-react** — *Reference repo (docs + example)* — `alan2207/bulletproof-react` (36k stars) — Scalable React architecture, project structure doc: https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md (verbatim) — [https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md](https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md) — *Partially verified*
- **realworld (Conduit)** — *Example spec + impl repos* — `gothinkster/realworld` — full-stack "Medium clone" specs + impls — Same API spec in 100+ stacks; frontend-decomp Conduit example: https://github.com/frontend-decomp/conduit-realworld-example-app (verbatim) — [https://github.com/frontend-decomp/conduit-realworld-example-app](https://github.com/frontend-decomp/conduit-realworld-example-app) — *Partially verified*
- **Microsoft API Guidelines** — *Reference (docs)* — `microsoft/api-guidelines` — REST API design guidance — *Partially verified*
- **Google API Design Guide** — *Reference (docs)* — Google AIP (aip.dev) — API design patterns (AIPs) — *Partially verified*
- **12factor.net** — *Reference (docs)* — 12-Factor App methodology — SaaS app principles — *Partially verified*
- **DDIA** — *Book reference* — "Designing Data-Intensive Applications" (dataintensive.net) — Storage/replication/partitioning foundations — *Partially verified*
- **Google SRE Book** — *Reference (books/docs)* — Google SRE (sre.google) — Reliability engineering practices — *Partially verified*
- **AWS Well-Architected** — *Reference (docs)* — AWS Well-Architected Framework — 6 pillars, lenses, labs — *Partially verified*
- **Azure Architecture Center** — *Reference (docs)* — Microsoft Cloud Adoption/Architecture guidance — Patterns, reference architectures — *Partially verified*

### 3.9.2 Design patterns & domain modeling

- **martinfowler.com** — *Reference (articles)* — Martin Fowler — patterns/essays — Refactoring, DDD, microservices, EDA — *Partially verified*
- **refactoring.guru** — *Reference (interactive docs)* — Refactoring.Guru — patterns catalog — Design patterns, refactoring, SOLID — *Partially verified*
- **Enterprise Integration Patterns** — *Book reference* — EIP (Hohpe/Woolf) — messaging patterns — 65 integration patterns — *Partially verified*
- **awesome-software-design** — *Awesome-list* — `Vaskivskyi/awesome-software-design`-style lists (generic) — Curated design resources — *Partially verified*

### 3.9.3 Architecture decision records (ADRs)

- **adr-tools** — *Open source tool (MIT)* — `npryce/adr-tools` — ADR CLI — Init/new/link/list ADRs as Markdown — [https://github.com/npryce/adr-tools](https://github.com/npryce/adr-tools) — *Partially verified*
- **adr-kit** — *Open source (per repo)* — `luochang212/adr-kit` — ADR templates/toolkit — Templates + guidance — [https://github.com/luochang212/adr-kit](https://github.com/luochang212/adr-kit) — *Partially verified*
- **adrs (Rust)** — *Open source tool* — `joshrotenberg/adrs` — ADR tool in Rust, ships MCP server — ADR management + MCP server for agents — [https://github.com/joshrotenberg/adrs](https://github.com/joshrotenberg/adrs) — *Partially verified*
- **log4brains** — *Open source (MIT)* — log4brains — ADR knowledge base generator — Static site from ADRs — *Partially verified*

### 3.9.4 Architecture modeling & documentation

- **Structurizr / C4** — *Open source (Apache 2.0) + Cloud* — Structurizr — C4 model tooling — Diagrams-as-code, workspaces — *Partially verified*
- **arc42** — *Open template (CC-BY-SA)* — arc42 — architecture doc template — 12-section arch documentation — *Partially verified*

### 3.9.5 Dependency analysis & modular architecture tooling

- **dependency-cruiser** — *Open source (MIT)* — dependency-cruiser — JS/TS dep linting — Enforce module boundaries, detect cycles — *Partially verified*
- **madge** — *Open source (MIT)* — madge — module dependency graphs — Circular dep detection, graphs — *Partially verified*
- **ArchUnit family** — *Open source test libs* — ArchUnit (Java), ArchUnitNET, ArchUnitTS, konsist (Kotlin), tach (Python) — Architecture-as-unit-tests — *Partially verified*

*24 records in this category.*

---

*B1 — Core Web Development Technologies: 648 condensed records. Full evidence in the source catalogs under `catalogs/`.*