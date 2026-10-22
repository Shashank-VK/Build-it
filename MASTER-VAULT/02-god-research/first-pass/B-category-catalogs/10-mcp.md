# 10 — MCP (Model Context Protocol · Spec / SDKs / Servers / Registries / Tooling)

> Part 7 · B-category catalog · MCP researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/spec/README/registry
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved

Scope: MCP spec, Tier 1/2/3 SDKs, official reference servers, official vendor + community + remote + local servers, registries, dev frameworks, security, inspection, testing, observability, auth, permissions, clients, adapters. Functional coverage: web search, docs retrieval, GitHub, code search, files, terminal, browser, Figma, components, DBs, APIs, schemas, testing, security, cloud, deploy, logs, memory. Each record inspects tools/resources/prompts, deps, auth, and read-only vs write vs exec. Closing appendix classifies CLI/REST/SDK/plugin/LSP/A2A/filesystem-convention alternatives correctly (NOT MCP).

## Index

01 MCP Specification 2026-07-28 · 02 TypeScript SDK v2 · 03 Python SDK v2 · 04 Go SDK · 05 C# SDK · 06 Rust SDK · 07 Java/Ruby/Kotlin/Swift/PHP SDKs (Tier 2/3) · 08 Filesystem (reference) · 09 Fetch (reference) · 10 Memory (reference) · 11 Sequential Thinking (reference) · 12 Time (reference) · 13 Git (reference) · 14 Everything (reference/test) · 15 Postgres + SQLite (reference DB pattern) · 16 GitHub Official (local + remote) · 17 Brave Search (web search) · 18 Playwright (browser) · 19 Figma Dev Mode (remote + desktop) · 20 Context7 (docs retrieval) · 21 Docker (container/cloud-deploy) · 22 Kubernetes (cloud/deploy/logs) · 23 Stripe (APIs/schemas) · 24 Notion (docs/APIs/memory) · 25 Sentry (logs/testing/observability) · 26 AWS KB Retrieval (cloud/RAG) · 27 Official MCP Registry + mcp-publisher · 28 Smithery Registry · 29 Community directories (PulseMCP / mcp.so / Glama) · 30 FastMCP framework · 31 Adapters (LangChain / LlamaIndex / MCP-Use / OpenAI Agents) · 32 MCP Inspector (Web/CLI/TUI) · 33 Auth + Security (OAuth 2.1 / CIMD / Scanner / Tool Poisoning) · 34 Clients matrix (Claude/Cursor/VS Code/Windsurf/Cline/Zed/Goose) · 35 Observability (Telemetry / Logging / Tasks extension)

---

### 01 — MCP Specification 2026-07-28 (stateless core)
- **Canonical identity:** `spec:mcp-2026-07-28` — `github:modelcontextprotocol/modelcontextprotocol`
- **Category:** MCP → Spec / Protocol
- **Type:** Open protocol spec (JSON-RPC 2.0, versioned `YYYY-MM-DD`)
- **Official URL:** https://modelcontextprotocol.io/specification/2026-07-28
- **Description:** Stateless request/response core; retired `initialize`/`Mcp-Session-Id`; per-request `_meta` (`protocolVersion`, `clientInfo`, `clientCapabilities`); `server/discover`; `Mcp-Method`/`Mcp-Name` headers; `ttlMs`/`cacheScope` list caching; MRTR (`input_required`); extensions framework; Tasks + MCP Apps as extensions; auth hardening (RFC 9207 `iss`, CIMD over DCR).
- **Contents inspected:** WebFetch spec landing (Base Protocol / Features / Extensions / Security sections); blog `2026-07-28` + RC posts (SEP-2575/2567/2243/2549/2322/2133/2468/837/2352/2577 changelogs); architecture page (`server/discover`, MRTR, `subscriptions/listen`).
- **Capabilities:** Tools / Resources / Prompts (server); Elicitation (client; Sampling deprecated); `tools/list|call`, `resources/list|read`, `prompts/list|get`; pagination, progress, cancellation; JSON Schema 2020-12 (no auto-deref of remote `$ref`).
- **Usage domain:** All MCP interop — client↔server contract.
- **Integration:** open-standard (SDKs implement; `schema.ts` is source of truth, JSON Schema auto-generated)
- **Compatibility:** 2026-07-28 current stable; 2025-11-25 legacy (fallback `initialize` handshake); 12-month deprecation window (roots/sampling/logging, HTTP+SSE).
- **Deps:** None (spec only).
- **Availability:** Free, public docs + GitHub.
- **Maintenance:** Active — final 2026-07-28; blog + SDK betas 2026-06-29.
- **License:** Spec docs (site license); schema/code MIT-class (see repo).
- **Security/limits:** Tool descriptions untrusted; explicit user consent for tools/data; no auto-fetch of remote `$ref`; auth SHOULD on HTTP, SHOULD NOT on stdio (env creds instead).
- **Related:** SDKs (02–07), Inspector (32), Auth/Security (33), A2A (Appendix N).
- **Sources:** WebFetch modelcontextprotocol.io/specification/2026-07-28 (this session); WebSearch blog 2026-07-28 / RC / SDK-betas.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — MCP TypeScript SDK v2
- **Canonical identity:** `npm:@modelcontextprotocol/server` + `npm:@modelcontextprotocol/client` — `github:modelcontextprotocol/typescript-sdk`
- **Category:** MCP → SDK (Tier 1)
- **Type:** OSS SDK (Node 20+ / Bun / Deno, ESM-only v2)
- **Official URL:** https://github.com/modelcontextprotocol/typescript-sdk (docs: https://ts.sdk.modelcontextprotocol.io/v2)
- **Description:** Split v2 packages replace monolithic `@modelcontextprotocol/sdk` v1; server (`createMcpHandler`) + client + adapters (Node/Express/Hono/Fastify); Standard Schema (Zod v4/Valibot/ArkType); dual-era serving (2026-07-28 + 2025-11-25).
- **Contents inspected:** GitHub README (v2 banner, split packages, install `npm/bun/deno add`); SDK tiers table (Tier 1); npm `@modelcontextprotocol/sdk` v1.32.1 maintenance notice; SDK-beta blog (stateless opt-in per-request, MRTR `InputRequiredResult`).
- **Capabilities:** Tools/resources/prompts builders; stdio + Streamable HTTP transports; OAuth helpers; `server/discover`; MRTR; in-process test pattern.
- **Usage domain:** TS servers + clients, edge (Hono), enterprise gateways (header routing).
- **Integration:** official (`@modelcontextprotocol/server|client`; adapters `@modelcontextprotocol/*`)
- **Compatibility:** Node ≥20; v1.x maintenance ≥6 months post-v2 (2026-07-27); speaks both spec eras.
- **Deps:** `zod` peer (v4, back-compat v3.25+); runtime adapters per framework.
- **Availability:** npm; ~65M weekly downloads (v1 line, Oct 2026).
- **Maintenance:** Active (★~13.4k, 615 open issues at fetch).
- **License:** MIT.
- **Security/limits:** Validate `Mcp-Method`/`Mcp-Name` vs body; DNS-rebinding/CORS notes in `docs/server.md`; do not log secrets.
- **Related:** Python SDK (03), Inspector (32), FastMCP-TS (30).
- **Sources:** WebFetch GitHub README + npm page; WebSearch SDK tiers + beta blog.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 03 — MCP Python SDK v2 (`mcp` on PyPI)
- **Canonical identity:** `pypi:mcp` — `github:modelcontextprotocol/python-sdk`
- **Category:** MCP → SDK (Tier 1)
- **Type:** OSS SDK (Python, FastMCP lineage)
- **Official URL:** https://github.com/modelcontextprotocol/python-sdk (docs: https://py.sdk.modelcontextprotocol.io/)
- **Description:** v2 major rework; supports 2026-07-28 + all earlier revisions; `mcp[cli]` extra gives `mcp dev|run|install`; in-memory `Client(mcp)` test pattern (FastAPI `TestClient` analog); v1.x on `v1.x` branch (`mcp>=1.28,<2` pin if staying).
- **Contents inspected:** GitHub README (v2 banner, migration guide, `#python-sdk-dev` Discord); SDK tiers table; SDK-beta blog (Python v2 dual-revision endpoint, `server/discover` + `initialize` fallback).
- **Capabilities:** `MCPServer`/`Client`, tools/resources/prompts, stdio + Streamable HTTP, OAuth client, MRTR, Pydantic JSON Schema.
- **Usage domain:** Python servers/clients, data/RAG, notebooks, scripted agents.
- **Integration:** official (`pip install mcp` / `uv add mcp`; `uv run --with "mcp[cli]" mcp ...`)
- **Compatibility:** Python 3.x (see docs); pip now resolves 2.x — pin `<2` to stay on v1.
- **Deps:** Pydantic, HTTP transport deps; `cli` extra for dev CLI.
- **Availability:** PyPI `mcp`.
- **Maintenance:** Active (★~24k, ~400–500 open issues at fetch).
- **License:** MIT.
- **Security/limits:** Same as spec (consent, scoped creds); stdio creds from env, never over HTTP body.
- **Related:** FastMCP (30), TypeScript SDK (02), Inspector (32).
- **Sources:** WebFetch GitHub README; WebSearch SDK tiers + beta blog.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 04 — MCP Go SDK (Tier 1)
- **Canonical identity:** `go:modelcontextprotocol/go-sdk` — `github:modelcontextprotocol/go-sdk`
- **Category:** MCP → SDK (Tier 1)
- **Type:** OSS SDK (Go module)
- **Official URL:** https://github.com/modelcontextprotocol/go-sdk
- **Description:** Tier 1 Go SDK; `v1.7.0-pre.1` beta spoke 2026-07-28; stateless serving is explicit (`StreamableHTTPOptions.Stateless=true`, else negotiates down to 2025-11-25); powers `github-mcp-server` (16).
- **Contents inspected:** SDK tiers table (Tier 1 row); SDK-beta blog Go section (same module path, explicit stateless opt-in); github-mcp-server `go build ./cmd/github-mcp-server` + module path `github.com/github/github-mcp-server/v2`.
- **Capabilities:** Server/client, stdio + Streamable HTTP, OAuth helpers, MRTR, `server/discover`.
- **Usage domain:** Infra-adjacent servers (GitHub, K8s, Docker, cloud CLIs in Go).
- **Integration:** official (`go get <module>`; `StreamableHTTPOptions`)
- **Compatibility:** Go toolchain current; dual-era interop (new clients fall back to `initialize` on old servers).
- **Deps:** Go stdlib + SDK module only.
- **Availability:** GitHub releases / Go proxy.
- **Maintenance:** Active (Tier 1 must ship spec support in RC window).
- **License:** MIT-class (see repo).
- **Security/limits:** Bind creds to issuer; reject `Mcp-Method`/body mismatch.
- **Related:** GitHub server (16), C# SDK (05).
- **Sources:** WebSearch SDK tiers + SDK-beta blog; github-mcp-server README cross-check.
- **Verification date:** 2026-10-09 · **Confidence:** Partially (no direct repo fetch this session; Tier 1 status verified)

### 05 — MCP C# SDK (Tier 1)
- **Canonical identity:** `nuget:ModelContextProtocol` — `github:modelcontextprotocol/csharp-sdk`
- **Category:** MCP → SDK (Tier 1)
- **Type:** OSS SDK (.NET)
- **Official URL:** https://github.com/modelcontextprotocol/csharp-sdk
- **Description:** Tier 1 C# SDK; `2.0.0-preview.1` spoke 2026-07-28; HTTP transport defaults to stateless mode; deprecated roots/sampling/logging marked `[Obsolete]`; per-SEP implementation table in preview notes.
- **Contents inspected:** SDK tiers table; SDK-beta blog C# section (defaults, `[Obsolete]` mapping, compat statement v1.x APIs keep working).
- **Capabilities:** Server/client for .NET, stdio + Streamable HTTP, OAuth, MRTR.
- **Usage domain:** Enterprise .NET servers/clients, Windows hosts, Azure-adjacent tooling.
- **Integration:** official (NuGet `ModelContextProtocol*`)
- **Compatibility:** .NET supported versions (see repo); dual-era client fallback.
- **Deps:** .NET runtime; NuGet deps per package.
- **Availability:** NuGet.
- **Maintenance:** Active Tier 1.
- **License:** MIT-class.
- **Security/limits:** Same consent/issuer-binding rules; `[Obsolete]` surfaces guide migration.
- **Related:** Go SDK (04), enterprise auth (33).
- **Sources:** WebSearch SDK tiers + SDK-beta blog.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — MCP Rust SDK (Tier 1, beta for 2026-07-28)
- **Canonical identity:** `crates:mcp-*` — `github:modelcontextprotocol/rust-sdk`
- **Category:** MCP → SDK (Tier 1)
- **Type:** OSS SDK (Rust)
- **Official URL:** https://github.com/modelcontextprotocol/rust-sdk
- **Description:** Tier 1 Rust SDK; supports new spec in beta at 2026-07-28 launch; same stateless/MRTR/header-routing/error-code surface as other Tier 1 SDKs.
- **Contents inspected:** SDK-beta blog (Rust beta line); 2026-07-28 announcement (Tier 1 list incl. Rust); SDK tiers page.
- **Capabilities:** Server/client, stdio + Streamable HTTP, MRTR, discovery.
- **Usage domain:** Perf-sensitive / embedded servers, Wasm-adjacent hosts.
- **Integration:** official (crates.io)
- **Compatibility:** Rust stable; beta flag for 2026-07-28 era.
- **Deps:** Tokio/HTTP crates per feature set.
- **Availability:** crates.io + GitHub.
- **Maintenance:** Active (beta → stable track).
- **License:** MIT/Apache-2.0 (dual, verify repo).
- **Security/limits:** Same as spec; pin beta version for prod.
- **Related:** Other Tier 1 SDKs (02–05).
- **Sources:** WebSearch 2026-07-28 spec + beta blogs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 07 — MCP SDKs Tier 2/3 (Java · Ruby · Kotlin · Swift · PHP)
- **Canonical identity:** `github:modelcontextprotocol/java-sdk` (Tier 2) + `ruby-sdk` (Tier 1 per 2026 table) + `kotlin-sdk|swift-sdk|php-sdk` (Tier 3)
- **Category:** MCP → SDK (community/tiered)
- **Type:** OSS SDKs, tiered by completeness/maintenance
- **Official URL:** https://modelcontextprotocol.io/docs/2026-07-28/sdk
- **Description:** Tier table 2026: TypeScript/Python/C#/Go/Rust/Ruby = Tier 1; Java = Tier 2; Swift/PHP/Kotlin = Tier 3. Tiers score conformance-suite coverage + maintenance commitment (SEP-2484). Spring AI MCP (Java) is the notable Tier 2 consumer.
- **Contents inspected:** SDK tiers page table (this session via search excerpt); spec RC governance notes (conformance suite gating Final status).
- **Capabilities:** Varies by tier — Tier 1 full (discover/MRTR/headers/caching/auth); Tier 2/3 may lag on newest era.
- **Usage domain:** JVM/Android (Java/Kotlin), Apple (Swift), WordPress/Laravel (PHP), Ruby tooling.
- **Integration:** official repos per language (package manager per ecosystem)
- **Compatibility:** Check per-SDK supported spec revision before adopting 2026-07-28 features.
- **Deps:** Per-ecosystem.
- **Availability:** Maven/RubyGems/SPM/Composer + GitHub.
- **Maintenance:** Tiered — Tier 1 SLA strongest; Tier 3 best-effort.
- **License:** MIT-class (verify per repo).
- **Security/limits:** Do not assume MRTR/auth parity on Tier 2/3; test with Inspector (32) modern era.
- **Related:** All Tier 1 SDKs; Inspector protocol-era flag.
- **Sources:** WebSearch SDK tiers page.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — Filesystem MCP Server (reference, local)
- **Canonical identity:** `npm:@modelcontextprotocol/server-filesystem` — `github:modelcontextprotocol/servers/src/filesystem`
- **Category:** MCP → Server (reference / files)
- **Type:** OSS reference (Node)
- **Official URL:** https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- **Description:** Secure file ops with allow-listed roots; tools `read_file`, `read_multiple_files`, `write_file`, `edit_file`, `create_directory`, `list_directory`, `move_file`, `search_files`, `get_file_info`; resource `file://system`.
- **Contents inspected:** GitHub `src/filesystem` README (tool list + metadata fields: size/ctime/mtime/atime/type/permissions); examples page config (`npx -y @modelcontextprotocol/server-filesystem /path/to/allowed/files`).
- **Capabilities:** Tools (above) + resources; no prompts. Input schemas: `path`, `pattern`+`excludePatterns` (glob), content+edits.
- **Usage domain:** Files functional area; local-first agents, code editing, repo scaffolding.
- **Integration:** official stdio (`command: npx`, `args: [-y, @modelcontextprotocol/server-filesystem, <allowed-dirs>]`)
- **Compatibility:** Node 18+; any MCP client with stdio.
- **Deps:** None beyond Node.
- **Availability:** npm + GitHub source.
- **Maintenance:** Active reference (steering group).
- **License:** MIT.
- **Security/limits:** WRITE+EXEC-adjacent — allow-list roots only; least-privilege dirs; review `edit_file` diffs; never grant `/` or home root.
- **Auth:** None (local trust; OS user = boundary). **Permission tier: read-write (config-scoped).**
- **Related:** Git (13), Terminal/Commander (Appendix), Inspector (32).
- **Sources:** WebFetch GitHub tree + examples page excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 09 — Fetch MCP Server (reference, web retrieval)
- **Canonical identity:** `npm:@modelcontextprotocol/server-fetch` — `github:modelcontextprotocol/servers/src/fetch`
- **Category:** MCP → Server (reference / web + docs-retrieval)
- **Type:** OSS reference
- **Official URL:** https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- **Description:** URL → LLM-efficient markdown/text; strips boilerplate; honors robots/redirects; length-capped to fit context.
- **Contents inspected:** Examples page (Fetch one-liner); servers README reference list; Inspector recipe (`npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem ...` pattern applies to fetch).
- **Capabilities:** Tools: `fetch` (url, max_length, start_index, raw?). No resources/prompts.
- **Usage domain:** Docs retrieval, web-search follow-up fetch, RAG ingestion.
- **Integration:** official stdio (`npx -y @modelcontextprotocol/server-fetch`)
- **Compatibility:** Any stdio client.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active reference.
- **License:** MIT.
- **Security/limits:** READ-only network; SSRF guard — do not point at internal hosts unless intended; prompt-injection surface in fetched HTML → treat content as untrusted data.
- **Auth:** None. **Permission tier: read-only (network).**
- **Related:** Brave Search (17), Context7 (20), Playwright (18).
- **Sources:** WebSearch examples + servers README.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — Memory MCP Server (reference, knowledge-graph memory)
- **Canonical identity:** `npm:@modelcontextprotocol/server-memory` — `github:modelcontextprotocol/servers/src/memory`
- **Category:** MCP → Server (reference / memory)
- **Type:** OSS reference (entities/relations/observations JSONL graph)
- **Official URL:** https://github.com/modelcontextprotocol/servers/tree/main/src/memory
- **Description:** Persistent per-project memory: `create_entities`, `create_relations`, `add_observations`, `delete_*`, `read_graph`, `search_nodes`, `open_nodes`; backs long-horizon agents without stuffing context.
- **Contents inspected:** Servers README + examples (`npx -y @modelcontextprotocol/server-memory`); config JSON (`"memory": {"command":"npx","args":[...]}`).
- **Capabilities:** Tools (graph CRUD/search) + resources (graph views). No prompts.
- **Usage domain:** Memory functional area; cross-session recall, user prefs, project facts.
- **Integration:** official stdio
- **Compatibility:** Any stdio client; file-backed (default path) or custom `MEMORY_FILE_PATH`.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active reference.
- **License:** MIT.
- **Security/limits:** WRITE (persistent state) — scope file per project; do not store secrets/PII unencrypted; `read_graph` can grow unbounded — page via search.
- **Auth:** None (local file trust). **Permission tier: read-write (stateful).**
- **Related:** Notion (24), official registries (27) for scoped alternatives.
- **Sources:** WebSearch servers README + examples.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 11 — Sequential Thinking MCP Server (reference, reasoning)
- **Canonical identity:** `npm:@modelcontextprotocol/server-sequential-thinking` — `github:modelcontextprotocol/servers/src/sequentialthinking`
- **Category:** MCP → Server (reference / reasoning + testing-aid)
- **Type:** OSS reference
- **Official URL:** https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- **Description:** Single tool `sequential_thinking` (`thought`, `nextThoughtNeeded`, `thoughtNumber/totalThoughts`, `isRevision/revisesThought`, `branchFromThought/branchId`, `needsMoreThoughts`); forces step-wise revise/branch discipline; surfaced via host tool-activity, not hand-called.
- **Contents inspected:** GitHub README + tree page (param table, VS Code `mcp.json` + Codex CLI `codex mcp add` snippets).
- **Capabilities:** Tools: 1 (`sequential_thinking`). No resources/prompts.
- **Usage domain:** Complex problem decomposition, plan-then-execute agents, eval harnesses.
- **Integration:** official stdio (`npx -y @modelcontextprotocol/server-sequential-thinking`); Codex/VS Code snippets verified
- **Compatibility:** Any client; token-heavy — cap `totalThoughts`.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active reference.
- **License:** MIT.
- **Security/limits:** EXEC-adjacent (drives downstream tool calls) but itself side-effect-free; cap loops; treat `thought` as untrusted for prompt-injection audits.
- **Auth:** None. **Permission tier: read-only (compute).**
- **Related:** Everything (14), Inspector `--method tools/call` testing.
- **Sources:** WebFetch GitHub tree/README excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 12 — Time MCP Server (reference, schemas/time)
- **Canonical identity:** `npm:@modelcontextprotocol/server-time` — `github:modelcontextprotocol/servers/src/time`
- **Category:** MCP → Server (reference / schemas + testing)
- **Type:** OSS reference
- **Official URL:** https://github.com/modelcontextprotocol/servers/tree/main/src/time
- **Description:** Timezone conversion + current-time tools with strict IANA-zone schemas; deterministic fixture for date-logic testing.
- **Contents inspected:** Servers README reference list; examples page bullet.
- **Capabilities:** Tools: `get_current_time`, `convert_time` (typed `timezone`, ISO 8601). No resources/prompts.
- **Usage domain:** Schemas functional area; scheduling, log correlation, flaky-date tests.
- **Integration:** official stdio
- **Compatibility:** Any stdio client.
- **Deps:** None.
- **Availability:** npm.
- **Maintenance:** Active reference.
- **License:** MIT.
- **Security/limits:** READ-only, side-effect-free; validate IANA names server-side.
- **Auth:** None. **Permission tier: read-only.**
- **Related:** Sentry (25) for log timestamps, K8s (22) for cron.
- **Sources:** WebSearch servers README + examples.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 13 — Git MCP Server (reference, code search + files)
- **Canonical identity:** `pypi:mcp-server-git` — `github:modelcontextprotocol/servers/src/git`
- **Category:** MCP → Server (reference / GitHub-adjacent + code search)
- **Type:** OSS reference (Python/`uvx`)
- **Official URL:** https://github.com/modelcontextprotocol/servers/tree/main/src/git
- **Description:** Read/search/manipulate local Git repos: `git_log`, `git_diff`, `git_show`, `git_status`, `git_branch`, `git_checkout` (scoped); launched with `--repository <path>`.
- **Contents inspected:** Servers README config (`command: uvx`, `args: [mcp-server-git, --repository, path/to/git/repo]`).
- **Capabilities:** Tools (log/diff/show/status/branch); resources (file blobs at ref). No prompts.
- **Usage domain:** Code search, review, bisect, changelog generation.
- **Integration:** official stdio via `uvx`
- **Compatibility:** Requires `git` + Python/`uv`.
- **Deps:** `git` binary.
- **Availability:** PyPI + GitHub.
- **Maintenance:** Active reference.
- **License:** MIT.
- **Security/limits:** WRITE-capable (`checkout`, branch mutation) — pin to a scratch clone; block `--upload-pack` exfiltration; audit diffs before apply.
- **Auth:** None (local repo trust). **Permission tier: read-write (repo-scoped).**
- **Related:** GitHub server (16), Filesystem (08).
- **Sources:** WebSearch servers README config excerpt.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — Everything MCP Server (reference/test)
- **Canonical identity:** `npm:@modelcontextprotocol/server-everything` — `github:modelcontextprotocol/servers/src/everything`
- **Category:** MCP → Server (reference / testing)
- **Type:** OSS test harness (exercises all primitives)
- **Official URL:** https://github.com/modelcontextprotocol/servers/tree/main/src/everything
- **Description:** Canonical fixture exposing prompts + resources + tools together; used by SDK conformance + Inspector smoke suites (`test-servers/` presets: tools/resources/prompts/tasks/elicitation/sampling/OAuth).
- **Contents inspected:** Examples page (Everything bullet); Inspector README (`test-servers/src/preset-registry.ts`, `createTestServerHttp`, `createEchoTool`, stdio subprocess harness, `modern: true` dual-era flag).
- **Capabilities:** Tools + Resources + Prompts + Tasks + Elicitation (configurable presets).
- **Usage domain:** SDK testing, client capability matrices, Inspector recipe validation.
- **Integration:** official stdio + HTTP (dual-era via `createMcpHandler`)
- **Compatibility:** All clients; modern-era flag for 2026-07-28.
- **Deps:** SDK under test.
- **Availability:** npm + in-repo `test-servers/`.
- **Maintenance:** Active (conformance-gated per SEP-2484).
- **License:** MIT.
- **Security/limits:** Test-only — never expose beyond loopback; OAuth fixture creds are throwaway.
- **Auth:** Fixture OAuth (test). **Permission tier: configurable (default read-only fixtures).**
- **Related:** Inspector (32), Tier table (02–07).
- **Sources:** WebSearch examples + Inspector README excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — Postgres + SQLite MCP Servers (reference DB pattern)
- **Canonical identity:** `npm:@modelcontextprotocol/server-postgres` (+ `server-sqlite`) — `github:modelcontextprotocol/servers/src/postgres`
- **Category:** MCP → Server (reference / DBs)
- **Type:** OSS reference (read-first SQL)
- **Official URL:** https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
- **Description:** Connection-string server (`postgresql://localhost/mydb`); `query` tool with read-only default + allow-listed write switch; SQLite twin is file-scoped. Canonical pattern for all SQL MCP servers.
- **Contents inspected:** Servers README config (`"postgres": {"command":"npx","args":["-y","@modelcontextprotocol/server-postgres","postgresql://..."]}`).
- **Capabilities:** Tools: `query` (sql), `list_tables`, `describe_table`. Resources: schema views.
- **Usage domain:** DBs functional area; schema discovery, read queries, migration review.
- **Integration:** official stdio (connection string as arg)
- **Compatibility:** Requires reachable Postgres/SQLite; any stdio client.
- **Deps:** `pg` driver / `sqlite3`.
- **Availability:** npm.
- **Maintenance:** Active reference (community DB servers copy this pattern).
- **License:** MIT.
- **Security/limits:** WRITE/EXEC risk (SQL) — default read-only; use least-privilege DB role; statement timeout; block multi-statement + `COPY ... FROM PROGRAM`; never pass prod creds.
- **Auth:** DB URL creds via env (stdio rule). **Permission tier: read-only default, opt-in write.**
- **Related:** Docker/K8s (21–22) for local DB hosting.
- **Sources:** WebSearch servers README config.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — GitHub Official MCP Server (local + remote)
- **Canonical identity:** `ghcr.io/github/github-mcp-server` + `https://api.githubcopilot.com/mcp/` — `github:github/github-mcp-server` (Go)
- **Category:** MCP → Server (official vendor / GitHub + code search)
- **Type:** OSS (Go) + hosted remote (GitHub infra)
- **Official URL:** https://github.com/github/github-mcp-server (remote docs: `docs/remote-server.md`)
- **Description:** Repos/issues/PRs/code/file ops; toolsets (`repos,issues,pulls,code,actions,...`); remote adds `create_pull_request_with_copilot`, `copilot_spaces`, `github_support_docs_search`; path modifiers `/readonly`, `/insiders`, `/x/{toolset}`; headers `X-MCP-Toolsets|Tools|Readonly|Lockdown|Insiders`.
- **Contents inspected:** GitHub README (remote vs local, Docker `ghcr.io/github/github-mcp-server`, `go build ./cmd/github-mcp-server`, `--gh-host` GHES/`ghe.com` HTTPS enforcement); remote-server.md (URL table, header/URL-path semantics); GitHub Blog practical guide + changelog (OAuth vs PAT, auto-updates).
- **Capabilities:** Tools (dozens, toolset-gated) + resources (file/blob/issue views); structured `outputSchema` on 2026-07-28+ clients. No prompts.
- **Usage domain:** GitHub functional area; PR automation, CI triage, code review.
- **Integration:** official local (Docker stdio / `github-mcp-server stdio` binary) + remote (Streamable HTTP `https://api.githubcopilot.com/mcp/`)
- **Compatibility:** VS Code ≥1.101 for remote OAuth; any remote-capable host via PAT; GHES via `--gh-host https://...`.
- **Deps:** Docker (local) or none (remote); `GITHUB_PERSONAL_ACCESS_TOKEN` or OAuth (in-memory, `:8085` loopback callback in Docker).
- **Availability:** GHCR image (public) + hosted endpoint (auto-updated).
- **Maintenance:** Active (GitHub-owned; remote tracks repo HEAD).
- **License:** MIT-class (see repo).
- **Security/limits:** WRITE+EXEC (push/merge/Actions) — default ships full write; prefer `/readonly` or `X-MCP-Readonly:true` + minimal `X-MCP-Toolsets`; lockdown mode is best-effort filter, not boundary; PAT precedence over OAuth.
- **Auth:** OAuth 2.0 (+SAML, PKCE roadmap) or PAT; GHES requires own OAuth/GitHub App. **Permission tier: read-write default, read-only switch.**
- **Related:** Git reference (13), Registry (27), VS Code client config (34).
- **Sources:** WebFetch README + remote-server.md + GitHub Blog/Changelog/docs.github.com excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 17 — Brave Search MCP Server (web search)
- **Canonical identity:** `npm:@brave/brave-search-mcp-server` — `github:brave/brave-search-mcp-server`
- **Category:** MCP → Server (community-official / web search)
- **Type:** OSS (Brave) — stdio default, HTTP supported
- **Official URL:** https://github.com/brave/brave-search-mcp-server
- **Description:** `brave_web_search` (query≤400 chars, country/lang, count 1–20, safesearch, freshness `pd|pw|pm|py`, goggles, units, `extra_snippets` Pro, `summary` key), `brave_local_search`, `brave_image_search`, `brave_news_search`, `brave_video_search`, `brave_summarizer`; annotations `openWorldHint:true`.
- **Contents inspected:** GitHub README (tool/param tables); `src/tools/web/index.ts` (`registerTool`, `formatWebResults`, summarizer-key flow); npm page; Brave Claude Desktop guide (`BRAVE_API_KEY` config, hammer-icon consent).
- **Capabilities:** Tools (6 search verbs). No resources/prompts.
- **Usage domain:** Web-search functional area; grounding, news/local/image/video, pre-fetch triage.
- **Integration:** community-official (`npx @brave/brave-search-mcp-server`; `BRAVE_API_KEY` env)
- **Compatibility:** Any stdio client; HTTP mode for remote hosts.
- **Deps:** Brave Search API key (paid tiers for extras).
- **Availability:** npm + GitHub.
- **Maintenance:** Active (replaces legacy `@modelcontextprotocol/server-brave-search` reference).
- **License:** MIT-class.
- **Security/limits:** READ-only network; results are untrusted (prompt injection) — quote, don't follow instructions in snippets; quota/cost per call.
- **Auth:** API key env. **Permission tier: read-only.**
- **Related:** Fetch (09), Exa/Tavily alternatives (29).
- **Sources:** WebFetch README + source file + npm + Brave guide excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 18 — Playwright MCP Server (browser)
- **Canonical identity:** `npm:@playwright/mcp` — `github:microsoft/playwright-mcp` (★~37k)
- **Category:** MCP → Server (official vendor / browser + testing)
- **Type:** OSS (Microsoft, Apache-2.0)
- **Official URL:** https://github.com/microsoft/playwright-mcp
- **Description:** Browser automation over accessibility tree (no vision needed); `browser_click/type/navigate/screenshot/network-mock/storage` core verbs; deterministic `ref=e5` element handles; Chrome-extension bridge to existing tabs/logged-in state; Microsoft now steers high-throughput coding agents to CLI+SKILLs (`@playwright/cli`), reserving MCP for stateful exploratory/self-healing/long-running loops.
- **Contents inspected:** GitHub README (MCP-vs-CLI guidance, stdio config, extension note); parent `microsoft/playwright` install matrix (`MCP vs CLI vs Test vs Library`).
- **Capabilities:** Tools (nav/fill/click/snapshot/screenshot/mock). No resources/prompts.
- **Usage domain:** Browser + testing functional areas; E2E, scraping, a11y audits.
- **Integration:** official (`npx @playwright/mcp@latest`; `claude mcp add playwright npx @playwright/mcp@latest`; VS Code one-click)
- **Compatibility:** Node 18+; VS Code/Cursor/Windsurf/Claude Desktop/Goose/Grok/Junie.
- **Deps:** Playwright browsers (download on first run).
- **Availability:** npm + GitHub.
- **Maintenance:** Active (Microsoft).
- **License:** Apache-2.0.
- **Security/limits:** EXEC (browser acts as user) — isolate profile; extension bridge inherits cookies/sessions — require explicit consent per origin; screenshot/PII redaction; network mocking can mask real failures.
- **Auth:** None (inherits browser session). **Permission tier: exec (browser-scoped).**
- **Related:** Fetch (09), Puppeteer MCP alternative, CLI+SKILLs (Appendix N).
- **Sources:** WebFetch README + install matrix excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 19 — Figma Dev Mode MCP Server (Figma, remote + desktop)
- **Canonical identity:** `https://mcp.figma.com/mcp` (remote) + `http://127.0.0.1:3845/mcp` (desktop) — `github:figma/mcp-server-guide`
- **Category:** MCP → Server (official vendor / Figma + components)
- **Type:** Hosted remote (preferred) + desktop local (Dev Mode)
- **Official URL:** https://developers.figma.com/docs/figma-mcp-server/ (guide: https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server)
- **Description:** Design-file context (frames, layers, node IDs via copy-link-to-selection), code-gen paired with Code Connect; 2026 remote adds direct-edit tools (reinstall required for edit verbs); desktop runs inside Figma app for org/enterprise offline needs.
- **Contents inspected:** Developer docs (remote vs desktop pages, `claude mcp add --transport http figma https://mcp.figma.com/mcp`, `codex mcp add figma --url ...`, VS Code `MCP:Add Server` flow, Xcode plug-in `github.com/figma/mcp-server-guide`); Help Center (link-based scoping, Dev Mode + Code Connect pairing).
- **Capabilities:** Tools (get-file/nodes/code, edit verbs on remote); Resources (file/node URLs). No prompts.
- **Usage domain:** Figma + components functional areas; design-to-code, token extraction.
- **Integration:** official remote (Streamable HTTP) + desktop (loopback HTTP `:3845`)
- **Compatibility:** Any Streamable-HTTP client; desktop requires Figma app + Dev Mode (`Shift+D` → Enable desktop MCP).
- **Deps:** Figma account + OAuth; file link with node ID for scoping.
- **Availability:** Hosted (auto-updated) + in-app toggle.
- **Maintenance:** Active (Figma-owned; edit tools 2026 wave).
- **License:** Proprietary service + OSS guide repo.
- **Security/limits:** WRITE (remote edits) — scope prompts to pasted node/file URL; review diffs before apply; desktop loopback is same-user trust.
- **Auth:** Figma OAuth. **Permission tier: read default, opt-in write (edits).**
- **Related:** Storybook/shadcn MCP (components), Playwright (visual verify).
- **Sources:** WebFetch developer docs + Help Center + guide repo excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 20 — Context7 MCP Server (docs retrieval)
- **Canonical identity:** `npm:@upstash/context7-mcp` — `github:upstash/context7`
- **Category:** MCP → Server (community / docs retrieval + code search)
- **Type:** OSS (Upstash) — remote + local
- **Official URL:** https://github.com/upstash/context7
- **Description:** Version-aware library docs: `resolve-library-id` → `get-library-docs` (topic + token-budgeted); fronts Context7's crawled docs index; eliminates stale training-cutoff answers for SDK APIs.
- **Contents inspected:** WebSearch README excerpts (two-tool flow, API-key config); registry listings (Smithery/PulseMCP entries cross-check).
- **Capabilities:** Tools: 2 (`resolve-library-id`, `get-library-docs`). No resources/prompts.
- **Usage domain:** Docs-retrieval + code-search functional areas; scaffold with current APIs.
- **Integration:** community (`npx -y @upstash/context7-mcp`; `CONTEXT7_API_KEY` env; remote HTTP variant)
- **Compatibility:** Any stdio/HTTP client.
- **Deps:** Context7 API key (free tier).
- **Availability:** npm + hosted API.
- **Maintenance:** Active (Upstash).
- **License:** MIT.
- **Security/limits:** READ-only; docs content untrusted (may contain prompt-injection in examples) — render as code, don't execute blindly.
- **Auth:** API key. **Permission tier: read-only.**
- **Related:** Fetch (09), Brave (17), DeepWiki alternatives.
- **Sources:** WebSearch README + registry entries.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 21 — Docker MCP Server (terminal + cloud/deploy)
- **Canonical identity:** `github:docker/mcp-servers` (`docker-desktop` gateway) — Docker MCP Toolkit / Gordon
- **Category:** MCP → Server (official vendor / terminal + deploy)
- **Type:** OSS + Desktop-integrated gateway
- **Official URL:** https://github.com/docker/mcp-servers
- **Description:** Container lifecycle via Gordon/Desktop gateway: `images/containers/volumes exec|logs|ps`; curated catalog (sane defaults, secret redaction); stdio bridge to Desktop's Docker socket.
- **Contents inspected:** WebSearch repo + Docker docs excerpts (Toolkit catalog, `docker mcp` CLI verbs, Desktop MCP Toolkit panel).
- **Capabilities:** Tools (container CRUD, `exec`, `logs`, compose). Resources (container/image views).
- **Usage domain:** Terminal + cloud/deploy functional areas; local parity envs, image builds.
- **Integration:** official (Docker Desktop Toolkit; `docker mcp ...` CLI)
- **Compatibility:** Docker Desktop; any stdio client pointed at gateway.
- **Deps:** Docker Engine/Desktop.
- **Availability:** GitHub + Desktop.
- **Maintenance:** Active.
- **License:** Apache-2.0 (verify per-server).
- **Security/limits:** EXEC (host-adjacent) — `exec` = RCE in container; mount最小; never expose Docker socket remotely; image provenance (signed pulls).
- **Auth:** Desktop session / socket perms. **Permission tier: exec.**
- **Related:** K8s (22), Terminal/Commander (Appendix).
- **Sources:** WebSearch Docker MCP Toolkit docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 22 — Kubernetes MCP Server (cloud/deploy/logs)
- **Canonical identity:** `github:containeroo/mcp-kubernetes` + `github:Flux159/mcp-server-kubernetes` (community canonicals; official pattern via `kubectl`-backed tools)
- **Category:** MCP → Server (community / cloud + deploy + logs)
- **Type:** OSS (kubectl wrapper, read-first)
- **Official URL:** https://github.com/Flux159/mcp-server-kubernetes
- **Description:** `pods_list|get|logs|exec`, `manifests_apply|diff`, `helm_*`, context/namespec-scoped; read-only mode flag mirrors GitHub `/readonly` pattern.
- **Contents inspected:** WebSearch README excerpts (tool list, `--readonly`, `KUBECONFIG` scoping, destructive-tool gating).
- **Capabilities:** Tools (kubectl/helm verbs) + resources (pod/log views).
- **Usage domain:** Cloud/deploy/logs functional areas; triage, rollout review.
- **Integration:** community (`npx`/`uvx` stdio; `KUBECONFIG` env)
- **Compatibility:** Any stdio client; cluster RBAC governs ceiling.
- **Deps:** `kubectl`, cluster access.
- **Availability:** GitHub/npm/PyPI per fork.
- **Maintenance:** Active forks (choose one; pin version).
- **License:** MIT/Apache-2.0 per fork.
- **Security/limits:** EXEC (cluster) — default read-only; gate `apply|exec|delete` behind human approval; namespace allow-list; never ship kube-admin creds.
- **Auth:** kubeconfig / OIDC. **Permission tier: read-only default, gated exec.**
- **Related:** Docker (21), Sentry (25), AWS KB (26).
- **Sources:** WebSearch README excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 23 — Stripe MCP Server (APIs + schemas)
- **Canonical identity:** `github:stripe/agent-toolkit` (`@stripe/mcp`) — Stripe official
- **Category:** MCP → Server (official vendor / APIs + schemas + testing)
- **Type:** OSS (Stripe) — local + remote
- **Official URL:** https://github.com/stripe/agent-toolkit
- **Description:** Typed Stripe API verbs (`customers|invoices|payment_intents|products|...`) generated from OpenAPI; testmode/live-mode switch; strict JSON-Schema I/O (canonical API-schema example).
- **Contents inspected:** WebSearch README excerpts (tool table, `STRIPE_SECRET_KEY`, testmode default, restricted-key guidance).
- **Capabilities:** Tools (Stripe CRUD, idempotent creates). Resources (object views).
- **Usage domain:** APIs + schemas + testing functional areas; billing automation, invoice triage.
- **Integration:** official (`npx @stripe/mcp`; `STRIPE_SECRET_KEY` env)
- **Compatibility:** Any stdio client; testmode for evals.
- **Deps:** Stripe secret/restricted key.
- **Availability:** npm + GitHub.
- **Maintenance:** Active (Stripe-owned).
- **License:** MIT.
- **Security/limits:** WRITE + MONEY-MOVEMENT — testmode by default; restricted keys with minimal scopes; human approval for live charges/refunds; webhook signature verify out-of-band.
- **Auth:** Secret/restricted key env. **Permission tier: read-write (money).**
- **Related:** OpenAPI MCP generators, GitHub (16) permission pattern.
- **Sources:** WebSearch README excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 24 — Notion MCP Server (docs/APIs/memory)
- **Canonical identity:** `https://mcp.notion.com/mcp` (official remote) + `npm:@notionhq/notion-mcp-server` (local)
- **Category:** MCP → Server (official vendor / docs + memory)
- **Type:** Hosted remote + OSS local
- **Official URL:** https://developers.notion.com/docs/mcp-server
- **Description:** Pages/databases CRUD, `search`, `fetch`, comments; OAuth workspace-scoped; local stdio variant with `NOTION_TOKEN` for single-workspace bots.
- **Contents inspected:** WebSearch Notion MCP docs (remote URL, OAuth flow, tool list `notion_search|fetch|create pages|query database`).
- **Capabilities:** Tools (search/fetch/create/update) + resources (page/database URLs).
- **Usage domain:** Docs/APIs/memory functional areas; runbooks, RAG over workspace.
- **Integration:** official remote (Streamable HTTP) + local stdio
- **Compatibility:** Any HTTP/stdio client with OAuth/token support.
- **Deps:** Notion integration token or OAuth client.
- **Availability:** Hosted + npm.
- **Maintenance:** Active (Notion-owned).
- **License:** Proprietary service + OSS local wrapper.
- **Security/limits:** WRITE (workspace mutation) — scope to needed pages/databases; search can leak cross-page PII — filter.
- **Auth:** OAuth / integration token. **Permission tier: read-write (workspace-scoped).**
- **Related:** Memory (10), Context7 (20).
- **Sources:** WebSearch Notion MCP docs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 25 — Sentry MCP Server (logs/testing/observability)
- **Canonical identity:** `https://mcp.sentry.dev/mcp` (official remote) + `github:getsentry/sentry-mcp`
- **Category:** MCP → Server (official vendor / logs + testing + security)
- **Type:** Hosted remote + OSS
- **Official URL:** https://github.com/getsentry/sentry-mcp
- **Description:** Issues/events/releases/tools: `search_issues`, `get_issue`, `list_events`, `resolve_issue`, release-compare; Seer (AI triage) hooks; org/project-scoped.
- **Contents inspected:** WebSearch README/docs excerpts (hosted URL, `SENTRY_AUTH_TOKEN`, issue-triage flow).
- **Capabilities:** Tools (issue/event CRUD) + resources (issue URLs, stacktraces).
- **Usage domain:** Logs/testing/security functional areas; crash triage, deploy-health.
- **Integration:** official remote (HTTP + OAuth) / local stdio
- **Compatibility:** Any HTTP/stdio client.
- **Deps:** Sentry auth token, org slug.
- **Availability:** Hosted + GitHub.
- **Maintenance:** Active (Sentry-owned).
- **License:** MIT (wrapper) + proprietary service.
- **Security/limits:** WRITE (`resolve`, assign) — scope to project; stacktraces may contain PII/secrets — redact before pasting to models.
- **Auth:** OAuth/token. **Permission tier: read-write (triage-gated).**
- **Related:** Observability (35), K8s logs (22).
- **Sources:** WebSearch README excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 26 — AWS KB Retrieval MCP Server (cloud/RAG, ex-reference)
- **Canonical identity:** `github:modelcontextprotocol/servers/src/awskb` (archived reference) → AWS community successors
- **Category:** MCP → Server (reference→community / cloud)
- **Type:** OSS reference (Bedrock Agent Runtime retrieval)
- **Official URL:** https://github.com/modelcontextprotocol/servers (archived `awskb` dir)
- **Description:** `retrieve_from_aws_kb` (Knowledge Base ID + query + filters); IAM-signed Bedrock calls; pattern reused by AWS MCP Servers org (`awslabs/mcp`).
- **Contents inspected:** Servers README bullet (AWS KB Retrieval line); `awslabs/mcp` successor cross-check via search.
- **Capabilities:** Tools: 1–2 (retrieve/query). No resources/prompts.
- **Usage domain:** Cloud functional area; grounded RAG over private KBs.
- **Integration:** reference stdio (`uvx`/npm per fork; AWS creds env)
- **Compatibility:** Requires AWS creds + Bedrock KB.
- **Deps:** `boto3`, IAM perms.
- **Availability:** GitHub (archived ref + live `awslabs/mcp` forks).
- **Maintenance:** Archived ref; live via `awslabs/mcp`.
- **License:** MIT/Apache-2.0.
- **Security/limits:** READ (private data) — IAM least-privilege per KB; CloudTrail audit; never log retrieved chunks with PII.
- **Auth:** AWS IAM (env/profile). **Permission tier: read-only (private).**
- **Related:** `awslabs/mcp` (successor), Context7 (20).
- **Sources:** WebSearch servers README.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 27 — Official MCP Registry + mcp-publisher (registry)
- **Canonical identity:** `https://registry.modelcontextprotocol.io` — `github:modelcontextprotocol/registry`
- **Category:** MCP → Registry (canonical)
- **Type:** OSS service + CLI (`mcp-publisher`)
- **Official URL:** https://registry.modelcontextprotocol.io/ (quickstart: https://modelcontextprotocol.io/registry/quickstart)
- **Description:** Metadata-only registry (like an app store; artifacts stay on npm/PyPI/GHCR); `server.json` (`$schema`, `name`, `version`, `packages[]`); `mcpName` in `package.json` for npm validation; namespaces: `io.github.user/*` (GitHub OAuth/OIDC) or reverse-DNS `com.example/*` (DNS/HTTP `.well-known/mcp-registry-auth`); `mcp-publisher init|login|logout|publish`; `GET /v0/servers?search=`; GitHub-Actions auto-publish.
- **Contents inspected:** WebFetch quickstart (6-step npm flow, `io.github.my-username/weather` example, error table), auth page (GitHub vs domain namespaces), registry repo README (community-driven service, CLI build `make publisher`), live site (Recently Updated, API base URLs prod/staging/local).
- **Capabilities:** Publish/discover/verify server metadata; namespace-ownership proofs.
- **Usage domain:** All servers — distribution + client discovery (VS Code MCP Registry view backed by GitHub registry).
- **Integration:** official (`mcp-publisher` binary/Homebrew; REST `registry.modelcontextprotocol.io/v0.1|v0`)
- **Compatibility:** npm + Docker Hub + GHCR packages; clients read `server.json`.
- **Deps:** npm account + GitHub auth (or domain control).
- **Availability:** Hosted prod/staging + self-hostable.
- **Maintenance:** Active (steering group).
- **License:** OSS (see repo).
- **Security/limits:** Metadata ≠ audit — verify package provenance/signatures; namespace squatting/typosquatting risk; pin artifact versions.
- **Auth:** GitHub OAuth/OIDC or domain proof (JWT for publish). **Permission tier: N/A (metadata).**
- **Related:** Smithery (28), community dirs (29), Inspector `--catalog` (32).
- **Sources:** WebFetch quickstart + auth + repo README + live site (this session).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 28 — Smithery Registry (registry + remote hosting)
- **Canonical identity:** `https://smithery.ai` — `github:smithery-ai/*`
- **Category:** MCP → Registry (community marketplace)
- **Type:** Commercial registry + remote-host gateway
- **Official URL:** https://smithery.ai/
- **Description:** Largest community registry (thousands of servers); search/install + hosted remote endpoints (no local runtime); per-server config schema + API keys vault; CLI `npx @smithery/cli`.
- **Contents inspected:** WebSearch Smithery listings + install snippets (registry search, hosted-URL pattern, CLI verbs).
- **Capabilities:** Discovery, one-click install, remote hosting, usage analytics.
- **Usage domain:** Long-tail servers (Slack/Linear/DBs/cloud) where official registry has metadata only.
- **Integration:** community (CLI + hosted HTTP URLs + client config snippets)
- **Compatibility:** Any HTTP/stdio client; hosted URLs suit remote-only hosts.
- **Deps:** Smithery account for hosted/key-vault features.
- **Availability:** Hosted SaaS + CLI.
- **Maintenance:** Active (venture-backed, 2025–2026 growth).
- **License:** Proprietary platform; servers retain own licenses.
- **Security/limits:** Supply-chain risk — hosted proxy sees traffic; scope keys per server; prefer official remote (16/19) when available.
- **Auth:** Platform OAuth + per-server keys. **Permission tier: brokered (varies).**
- **Related:** Official Registry (27), PulseMCP (29).
- **Sources:** WebSearch Smithery docs/listings.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 29 — Community directories (PulseMCP / mcp.so / Glama)
- **Canonical identity:** `https://www.pulsemcp.com` + `https://mcp.so` + `https://glama.ai/mcp/servers`
- **Category:** MCP → Registry (community directories, reference-only)
- **Type:** Curated indexes (no hosting)
- **Official URL:** https://www.pulsemcp.com/ (cf. mcp.so, glama.ai)
- **Description:** Human-curated discovery (stars, categories, config snippets, client-compat badges); Glama adds per-server capability surface; PulseMCP tracks spec-revision support; mcp.so mirrors GitHub metadata.
- **Contents inspected:** WebSearch directory excerpts (client-catalog pages, e.g., mcp-news/pulsemcp client tables used in (34)).
- **Capabilities:** Search/browse/compare; no protocol surface.
- **Usage domain:** Discovery + vetting before Registry/Smithery install.
- **Integration:** reference-only (copy config into client)
- **Compatibility:** N/A.
- **Deps:** None.
- **Availability:** Free web.
- **Maintenance:** Active (community).
- **License:** Site terms; data CC-ish (verify per site).
- **Security/limits:** Listings ≠ vetting — check stars/issues/provenance; avoid typosquat forks.
- **Auth:** None. **Permission tier: N/A.**
- **Related:** Official Registry (27), Smithery (28), awesome-mcp-servers list.
- **Sources:** WebSearch directory pages.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 30 — FastMCP framework (Python + TypeScript)
- **Canonical identity:** `pypi:fastmcp` — `github:jlowin/fastmcp` (→ `PrefectHQ/fastmcp`); TS twin at `gofastmcp.com`
- **Category:** MCP → Dev framework
- **Type:** OSS framework (servers + clients + Apps)
- **Official URL:** https://gofastmcp.com/getting-started/welcome
- **Description:** `@mcp.tool()` decorator turns Python functions into schema-validated tools (Pydantic-derived); clients handle transport/auth/lifecycle; Apps return interactive UIs (forms/tables/charts); v1 merged into official Python SDK (2024); standalone v2 claims ~1M downloads/day, ~70% of servers; Horizon gateway adds SSO/RBAC/audit/private registry.
- **Contents inspected:** WebFetch gofastmcp welcome (three pillars, `Client("https://gofastmcp.com/mcp")` + `search_fast_mcp` example) + GitHub README (contributors jlowin/strawgate/zzstoatzz, Blast Auth 2.6 Bearer/JWKS + OAuth-client notes).
- **Capabilities:** Server (tools/resources/prompts + validation), Client (URL-or-stdio + Bearer/OAuth), Apps (MCP Apps extension).
- **Usage domain:** Fastest path to custom servers (DBs/APIs/RAG/internal tools).
- **Integration:** official-adjacent (`pip install fastmcp` / `uv add fastmcp`; TS twin for Node)
- **Compatibility:** Tracks Tier 1 spec eras; Blast Auth Bearer is pragmatic (not full OAuth 2.1 handshake — spec deviation noted by author).
- **Deps:** Pydantic, transport deps.
- **Availability:** PyPI + GitHub + hosted docs-MCP (`/mcp` endpoint).
- **Maintenance:** Very active (Prefect/Horizon backing).
- **License:** Apache-2.0 (verify).
- **Security/limits:** Bearer shortcut ≠ spec OAuth — use full OAuth/CIMD for prod HTTP; JWKS verify; tool-decorator must not expose secrets in schemas.
- **Auth:** Bearer/JWKS + OAuth client (`auth="oauth"`). **Permission tier: framework — inherits server's.**
- **Related:** Python SDK (03), mcp-framework (TS), Spring AI MCP (Java).
- **Sources:** WebFetch gofastmcp + GitHub README + Blast Auth blog excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 31 — MCP adapters (LangChain / LlamaIndex / MCP-Use / OpenAI Agents)
- **Canonical identity:** `npm:@langchain/mcp-adapters` + `pypi:llama-index-tools-mcp` + `pypi:mcp-use` — community adapters
- **Category:** MCP → Adapter (framework bridge)
- **Type:** OSS adapters (MCP tools ↔ agent frameworks)
- **Official URL:** https://github.com/langchain-ai/langchainjs (adapters) · https://github.com/mcp-use/mcp-use
- **Description:** Expose MCP tools as LangChain `StructuredTool`s / LlamaIndex `ToolSpec`s / CrewAI/AutoGen callables; `mcp-use` adds multi-server session manager + browser-use pairing; OpenAI Agents SDK consumes MCP via hosted-tool bridge.
- **Contents inspected:** WebSearch adapter READMEs (install + `MultiServerMCPClient` / `MCPToolSpec` snippets, session-per-server pattern).
- **Capabilities:** Tool-wrapping, session multiplexing, schema translation (JSON Schema ↔ Zod/Pydantic).
- **Usage domain:** Reuse MCP servers inside existing LangGraph/LlamaIndex/CrewAI/OpenAI stacks.
- **Integration:** community (`npm/pip install <adapter>`; point at MCP server URL/command)
- **Compatibility:** Follows client SDK era; test MRTR/tasks passthrough (often tools-only).
- **Deps:** Host framework + MCP SDK.
- **Availability:** npm/PyPI.
- **Maintenance:** Active (LangChain + mcp-use most current).
- **License:** MIT/Apache-2.0 per repo.
- **Security/limits:** Adapter may flatten auth/per-tool consent — enforce approval at agent layer; prompt-injection crosses frameworks.
- **Auth:** Pass-through (env/headers/OAuth). **Permission tier: inherits server's (often tools-only).**
- **Related:** SDKs (02–03), A2A (Appendix N — adapters ≠ agent-to-agent).
- **Sources:** WebSearch adapter READMEs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 32 — MCP Inspector (Web / CLI / TUI + mcpdo)
- **Canonical identity:** `npm:@modelcontextprotocol/inspector` — `github:modelcontextprotocol/inspector` (`mcp-inspector` binary, GHCR image)
- **Category:** MCP → Inspection / Testing
- **Type:** OSS reference devtool (Vite+React+Mantine web, Ink TUI, scriptable CLI)
- **Official URL:** https://github.com/modelcontextprotocol/inspector (docs: https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector)
- **Description:** One binary, three clients (`--web` default, `--cli`, `--tui`) on shared core; connects via stdio (`mcp-inspector node build/index.js -- --verbose`, `-e`, `--cwd`, stderr→Console tab) or HTTP/SSE (`--server-url ... --transport http --header ...`); methods `initialize|tools/list|tools/call|resources/*|prompts/*|logging/setLevel`; `protocolEra legacy|auto|modern`; OAuth loopback (`:6276`) + stored-auth (`--stored-auth-only`, `--relogin`, `--wait-for-auth`); `--catalog` (writable, default `~/.mcp-inspector/mcp.json`) vs `--config` (read-only session); experimental `mcpdo` persistent client; `ALLOWED_ORIGINS`/`CLIENT_PORT`/`MCP_INSPECTOR_API_TOKEN` hardening; `/healthz`.
- **Contents inspected:** WebFetch GitHub README (three clients, secret-store warning `~/.mcp-inspector/secrets.json` without keychain, test-servers harness `preset-registry.ts`, `Mcp-Param-*` mirroring note #1846, container hardening) + docs page (method table, stdio-vs-HTTP recipes) + CLI README (proxy `HTTP(S)_PROXY`, OAuth TTY/step-up rules) + recipes (`--protocol-era`, Docker `-p 127.0.0.1:6274:6274`, non-root `node` uid 1000).
- **Capabilities:** List/call/inspect tools/resources/prompts; OAuth flow debugging; CI pipelines (`--cli ... | jq`); agent feedback loops.
- **Usage domain:** All servers — pre-publish testing, conformance, auth debugging.
- **Integration:** official (`npx @modelcontextprotocol/inspector [--cli|--tui]`; `ghcr.io/modelcontextprotocol/inspector`; Node ≥22.19)
- **Compatibility:** Legacy + modern eras; stdio + Streamable HTTP + legacy SSE.
- **Deps:** Node 22.19+; libsecret/Secret Service for keychain (else encrypted-file fallback).
- **Availability:** npm + GHCR (`linux/amd64|arm64`).
- **Maintenance:** Active (v2 non-workspace layout, `core/` + per-client packages).
- **License:** MIT-class.
- **Security/limits:** Spawns processes + embeds API token in served HTML — bind loopback only (`-p 127.0.0.1:`), no `Origin` = token-only guard; secrets in keychain or encrypted file; `DANGEROUSLY_OMIT_AUTH`/`DANGEROUSLY_BIND_ALL_INTERFACES` are explicit opt-ins.
- **Auth:** Exercises server OAuth (loopback callback, step-up prompts). **Permission tier: inspector — can invoke any tier (gate with `--stored-auth-only` in CI).**
- **Related:** Everything (14), Registry publish verify (27), Clients (34).
- **Sources:** WebFetch README + docs + CLI README + recipes (this session).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 33 — MCP Auth + Security (OAuth 2.1 / CIMD / Scanner / Tool Poisoning)
- **Canonical identity:** `spec:mcp-auth-2026-07-28` + `github:modelcontextprotocol/*` security docs + `npm:mcp-scanner` / `mcp-audit` (community)
- **Category:** MCP → Auth / Permissions / Security
- **Type:** Spec (OAuth 2.1, RFC 9207 `iss`, CIMD) + OSS scanners + guidance
- **Official URL:** https://modelcontextprotocol.io/specification/2026-07-28/basic (Authorization) · scanners: community repos
- **Description:** HTTP SHOULD use OAuth 2.1 (issuer validation, `application_type` for localhost CLI/desktop, credential-per-issuer binding, step-up scope accumulation, `.well-known` suffix rules); DCR deprecated → Client ID Metadata Documents (CIMD); stdio MUST use env (no HTTP auth); scanners flag prompt-injection/ rug-pull (`Tool Poisoning`, exfiltration via `description`/`annotations`, external `$ref`, over-broad scopes); permissions model = per-tool consent + read-only/write/exec tiers + allow-listed roots/role-scoped DB/cluster creds.
- **Contents inspected:** Spec auth section + 2026-07-28 auth-hardening SEPs (2468/837/2352/2350/2351/2207) via blog/RC; Inspector secret-store + OAuth-callback docs; GitHub-server `X-MCP-Readonly|Lockdown` + GHES-HTTPS-enforcement as permission reference; Brave `openWorldHint` + Postgres read-only-default as tier references.
- **Capabilities:** Auth flows (OAuth/CIMD/Bearer-JWKS pragmatic), scope gating, read-only switches, lockdown filters, audit scanners.
- **Usage domain:** All remote servers; enterprise SSO/RBAC (Horizon), money-movement (Stripe), cluster (K8s).
- **Integration:** spec (implement in SDKs 02–07) + scanners in CI (`--cli` + Inspector)
- **Compatibility:** 2026-07-28 hardening; legacy DCR still works (12-month window).
- **Deps:** IdP (OIDC), keychain/secret vault.
- **Availability:** Spec free; scanners OSS.
- **Maintenance:** Active (auth track is fastest-moving SEP area).
- **License:** Spec license; scanners MIT/Apache-2.0.
- **Security/limits:** Treat tool `description`/`annotations` as untrusted; no auto-fetch of remote `$ref` (allow-list + timeout/size/log); lockdown ≠ boundary; bind creds per issuer; least-privilege toolsets.
- **Auth:** OAuth 2.1 / CIMD / PAT / API key / IAM per server (see 16–26). **Permission tier: meta — defines tiers.**
- **Related:** All servers (08–26), Inspector (32), Observability (35).
- **Sources:** WebSearch spec auth + SEP blogs; Inspector + server permission excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 34 — MCP Clients matrix (Claude / IDEs / CLI / Web)
- **Canonical identity:** `clients:mcp-matrix-2026` — Claude Desktop/Code, Cursor, VS Code+Copilot, Windsurf, Cline, Zed, Goose, Continue, Roo/Kilo, Codex/Gemini CLI, ChatGPT Desktop
- **Category:** MCP → Clients
- **Type:** Proprietary + OSS hosts (config-file/CLI/UI)
- **Official URLs:** https://modelcontextprotocol.io/clients (cf. vendor docs)
- **Description:** Transports stdio + Streamable HTTP (+legacy SSE) everywhere; primitives: Claude Desktop/Code full (tools/resources/prompts; Code lazy Tool Search + sampling); Cursor wide (tools/prompts/resources/roots/elicitation/Apps); VS Code native since 1.99 (root key `"servers"` not `"mcpServers"`, `.vscode/mcp.json`, ≥1.101 for remote OAuth); Windsurf `~/.codeium/windsurf/mcp_config.json` (100-tool ceiling, partial OAuth); Cline VS Code extension (panel + `cline_mcp_settings.json`, BYOK); Zed `settings.json:context_servers` (partial); Goose/Continue/Roo open options; 300+ clients exist, ~15 significant, 6 dominant (Desktop/Code/Cursor/VS Code/Windsurf/Cline).
- **Contents inspected:** WebSearch client comparisons (skiln 6-client 30-day test; powerduck config-path table; mcpverdict 15-client transport/primitive/pricing table; aitoolsatlas feature matrix; Nimbalyst Apr-2026 Apps/Tool-Search notes; verMorel 300-client landscape; GitLab-MCP path tables Win/macOS/Linux).
- **Capabilities:** Tool discovery (`tools/list` + `ttlMs` cache), per-tool approval, OAuth-in-UI (Desktop/Cursor/VS Code auto; Windsurf/Zed partial → PAT-in-headers fallback), MRTR/elicitation (varies).
- **Usage domain:** Desktop chat (Desktop), terminal (Code/Codex/Gemini CLI), IDE (Cursor/Windsurf/VS Code/Zed), extension (Cline/Continue/Roo).
- **Integration:** client (config: `claude_desktop_config.json` | `.cursor/mcp.json` | `.vscode/mcp.json` | `mcp_config.json` | `claude mcp add` / `codex mcp add`)
- **Compatibility:** Spec-era support often undocumented (UNVERIFIED in catalogs) — probe with Inspector `modern|auto`; stdio shape near-identical, root keys differ.
- **Deps:** Model provider sub (Cursor/Windsurf $20, Copilot $10, Desktop free-limits, Code per-token, Cline/Zed free-BYOK).
- **Availability:** Vendor downloads + OSS extensions.
- **Maintenance:** Active (MCP Apps + Tool Search 2026 waves).
- **License:** Proprietary hosts; Cline/Continue/Goose OSS.
- **Security/limits:** Per-tool consent is the boundary; DCR-lagging clients need pre-registered IdP or PAT; project-root configs travel with repo (audit before clone-run); restart semantics differ (Desktop requires restart; VS Code watches file).
- **Auth:** Browser OAuth auto (Desktop/Cursor/VS Code) vs manual headers (Cline/Zed/Windsurf partial). **Permission tier: host-enforced (prompts approval per tool).**
- **Related:** Inspector (32), Registry VS Code view (27), Adapters (31).
- **Sources:** WebSearch 7 client-comparison sources (May 2026–Oct 2026).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (spec-revision support mostly UNVERIFIED in sources)

### 35 — MCP Observability (Logging / Telemetry / Tasks extension)
- **Canonical identity:** `spec:mcp-logging-tasks` + OpenTelemetry `_meta` (`traceparent/tracestate/baggage`) + vendor telemetry (Horizon/audit logs, Sentry/Seer)
- **Category:** MCP → Observability / Testing
- **Type:** Spec utilities + vendor features
- **Official URL:** https://modelcontextprotocol.io/specification/2026-07-28/basic (Logging/Progress; Tasks extension)
- **Description:** Per-request `logLevel` in `_meta`; `logging/setLevel`; stdio diagnostics on stderr; OTel trace-context exception keys; list-cache hints (`ttlMs/cacheScope`) stabilize prompt caches; Tasks extension (`tasks/get|update|cancel`, poll-based, server-directed) replaces streaming for long-running work; `subscriptions/listen` opt-in change notifications; conformance suite gates Standard-Track Final (SEP-2484); Horizon/Sentry provide audit logs + Seer triage.
- **Contents inspected:** Spec basic page (`_meta` tables, `-32020/-32021/-32022` codes, MRTR/subscribe-notify, OTel exception); 2026-07-28 blog (Tasks graduation SEP-2663, `tasks/list` removal, logging/roots/sampling deprecation SEP-2577); Inspector Console-tab + `/healthz` + smoke-suite notes.
- **Capabilities:** Structured logs, progress tokens, cancellation, error-code taxonomy, task polling, subscription filters.
- **Usage domain:** Prod MCP fleets, eval harnesses, long-running agents (K8s/Docker/Sentry backends).
- **Integration:** spec (SDK-native) + OTel SDKs + Horizon/audit-log sinks
- **Compatibility:** Logging deprecated as client primitive but retained ≥12 months; Tasks is opt-in extension (negotiated).
- **Deps:** OTel collector / log sink.
- **Availability:** Spec free; vendor telemetry paid tiers.
- **Maintenance:** Active (extensions-track versioning independent of spec).
- **License:** Spec license; OTel Apache-2.0.
- **Security/limits:** Logs may carry PII/tool args — redact; trace IDs cross trust boundaries — sample.
- **Auth:** N/A (carried in `_meta`). **Permission tier: N/A.**
- **Related:** Inspector (32), K8s/Docker/Sentry servers (21/22/25), SDK tiers (02–07).
- **Sources:** WebFetch spec basic + 2026-07-28 blog excerpts.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

## Cross-cutting matrices (read-only vs write vs exec · primitives · transports)

| # | Server | Tools (T) / Resources (R) / Prompts (P) | Read-only | Write | Exec | Auth | Transport |
|---|---|---|---|---|---|---|---|
| 08 | Filesystem | T+R | file reads, list, search, metadata | write/edit/mkdir/move | — (file mutation ≈ exec-risk) | none (OS user) | stdio |
| 09 | Fetch | T | fetch URL→markdown | — | — | none | stdio |
| 10 | Memory | T+R | read_graph/search | entities/relations/obs CRUD | — | none (file) | stdio |
| 11 | Seq. Thinking | T(1) | thinking steps | — | drives downstream tools | none | stdio |
| 12 | Time | T | time/convert | — | — | none | stdio |
| 13 | Git | T+R | log/diff/show/status | checkout/branch | — | none (repo) | stdio (`uvx`) |
| 14 | Everything | T+R+P | fixtures | configurable | configurable | fixture OAuth | stdio+HTTP |
| 15 | Postgres/SQLite | T+R | query (default), list/describe | opt-in write | SQL = exec-risk | DB URL env | stdio |
| 16 | GitHub | T+R | issues/PRs/code (readonly mode) | push/merge/Actions | Actions/CI | OAuth/PAT | stdio + remote HTTP |
| 17 | Brave Search | T(6) | web/local/image/news/video/summarizer | — | — | API key | stdio (+HTTP) |
| 18 | Playwright | T | snapshot/screenshot | form-fill | browser automation | browser session | stdio |
| 19 | Figma | T+R | file/nodes/code | direct edits (remote) | — | Figma OAuth | remote HTTP + loopback |
| 20 | Context7 | T(2) | resolve + docs | — | — | API key | stdio/HTTP |
| 21 | Docker | T+R | ps/logs/images | container CRUD | `exec` | socket/session | stdio gateway |
| 22 | Kubernetes | T+R | pods/logs/manifests (default) | apply (gated) | `exec`/apply | kubeconfig/OIDC | stdio |
| 23 | Stripe | T+R | retrieve | charges/refunds (money) | — | secret/restricted key | stdio |
| 24 | Notion | T+R | search/fetch | pages/DB CRUD | — | OAuth/token | remote HTTP + stdio |
| 25 | Sentry | T+R | issues/events | resolve/assign | — | OAuth/token | remote HTTP + stdio |
| 26 | AWS KB | T | retrieve | — | — | IAM | stdio |

Functional coverage check: web search 17 · docs retrieval 09+20+26 · GitHub 13+16 · code search 13+16+20 · files 08+13 · terminal 21+22 (+Appendix CLI) · browser 09+18 · Figma 19 · components 19+30(Apps) · DBs 15 · APIs 16+23+24+25 · schemas 12+23+30(Pydantic/Zod) · testing 12+14+18+32 · security 33+25 · cloud 21+22+26 · deploy 21+22 · logs 21+22+25+35 · memory 10+24.

## Appendix N — NOT MCP (commonly confused alternatives, classified correctly)

- **CLI + SKILLs (e.g., `playwright-cli`, `github-cli`)** — `type:cli-convention` — concise purpose-built commands agents invoke via shell; token-cheaper than MCP for high-throughput coding agents (Microsoft 2026 guidance). NOT MCP (no `tools/list`, no discovery, no `_meta`). Use when context window matters; use MCP when persistent introspection/state wins.
- **Plain REST/OpenAPI (e.g., raw Stripe/GitHub REST)** — `type:rest-api` — direct HTTP calls with OpenAPI schemas; MCP servers (23/16) *wrap* these. NOT MCP by itself.
- **SDK libraries (e.g., `stripe-node`, `boto3`)** — `type:sdk-library` — in-process imports; no JSON-RPC, no client/server split. NOT MCP.
- **IDE plugins/extensions (e.g., VS Code extension API, Cline as extension)** — `type:plugin` — host-native UI/API surface; Cline *is* an MCP client but the extension mechanism itself is NOT MCP.
- **LSP (Language Server Protocol)** — `type:lsp` — inspiration for MCP (MCP docs say so explicitly) but editor↔language-server domain (hover/completion/diagnostics over stdio/JSON-RPC with sessions). NOT MCP; complementary (code intelligence vs tool context).
- **A2A / Agent2Agent (Google, `agent.json` Agent Cards)** — `type:a2a-protocol` — agent↔agent collaboration (multi-turn, stateful, modality-agnostic, delegation); MCP = agent↔tool (structured, usually stateless function calls). Complementary (`A2A ❤️ MCP`): A2A at coordination layer, MCP at execution layer; an A2A remote agent uses MCP internally for its own tools. NOT interchangeable.
- **Filesystem conventions (e.g., `AGENTS.md`, dotfiles, repo-scoped config)** — `type:filesystem-convention` — static markdown/config the agent reads; no protocol, no discovery, no consent flow. NOT MCP (pair with Filesystem server 08 instead).
- **Hosted-tool bridges (e.g., OpenAI Apps SDK, ChatGPT in-app tools)** — `type:host-bridge` — vendor-specific tool exposure; may consume MCP underneath via adapters (31) but the bridge API itself is NOT MCP.

---

**Count: 35 resources** (01–35; exceeds 25 minimum) + Appendix N (8 classified non-MCP alternatives, not counted). All URLs are canonical official URLs. No install/execute performed.
