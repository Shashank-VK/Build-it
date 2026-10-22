# PART 7 — MCP SERVERS, EXTERNAL TOOLS, INTEROPERABILITY

Workstream #8 catalog. Read-only research: discover, inspect, identify, verify,
categorize, explain usage, record sources. Nothing was installed, executed, built,
or configured; no recommendations are made.

## Method and sources searched

Live web research (browser.search + browser.open), primary sources preferred:
the MCP specification site (modelcontextprotocol.io), the official
modelcontextprotocol/servers and modelcontextprotocol/inspector repositories,
the official MCP Registry docs (registry.modelcontextprotocol.io), vendor
repositories (brave/brave-search-mcp-server, stripe/agent-toolkit, awslabs/mcp,
stripe/ai, cloudflare, getsentry, supabase-community, neondatabase,
basicmachines-co/basic-memory, jlowin/fastmcp, vercel/mcp-handler,
snyk/agent-scan, trailofbits/mcp-context-protector, cisco-ai-defense/mcp-scanner),
registry/directory sites (mcp.so, mcp.directory, glama.ai, smithery.ai,
pulsemcp.com, mcpfind), and protocol specifications (A2A at a2aproject/A2A,
ACP at agentclientprotocol.com).

Search themes: "Model Context Protocol specification 2025-11",
"official MCP Registry", "modelcontextprotocol servers reference servers",
"MCP Inspector debugging", "mcp.so vs mcp.directory vs glama.ai vs smithery.ai",
"Figma Dev Mode MCP Server tools", "jlowin fastmcp README",
"brave-search-mcp-server tools", "MCP server database postgres mysql mongodb supabase",
"awslabs mcp monorepo", "basic-memory MCP server", "stripe agent-toolkit MCP",
"mcp security scanner prompt injection invariant mcp-scan", "Google A2A protocol
Linux Foundation", "Zed Agent Client Protocol ACP", "mcp-remote stdio bridge",
"AGENTS.md open standard AAIF", "tavily exa MCP server official",
"mcp.directory browse".

Deduplication: the following already-catalogued items are cross-referenced only,
not re-researched in depth: context7/upstash (+ Context7-style alternatives),
github/github-mcp-server (OpenCode install guide), microsoft/playwright-mcp,
AlaeddineMessadi/opencode-mcp, ajhcs/Better-OpenCodeMCP, Traves-Theberge/opencode-mcp,
Ejentum, SwarmVault, supamem, shadcn MCP, cnoe-io/openapi-mcp-codegen,
awslabs/openapi-mcp-server, sandbox-technologies/opencode-docs-mcp,
deliberation, n8n (no OpenCode integration), michaljach/opencode-browser /
browsermcp.io.

### How to read a record

Each record follows a Part-21-style schema: Resource name, Canonical identity,
Category, Type, Official URL, Description, Contents inspected, Actual capabilities
(read-only / write-capable / execute-command classification), Usage domain,
Integration method, Compatibility, Dependencies, Authentication, Availability,
Maintenance, License, Security, Limitations, Related resources, Sources,
Verification date, Confidence.

Verification labels used exactly: Verified / Partially verified / Unverified /
Corrected / Archived / Inaccessible / Historical / Unresolved. Unknowns are
"Not verified", "Not publicly documented", "Not applicable", or "Unresolved".
Verification date for all records: 2026-10-10.

Note on transport terminology used below: stdio (local process, client spawns
server), Streamable HTTP (remote MCP over HTTP), SSE (legacy remote transport).

---

## SECTION 1 — THE MCP SPECIFICATION AND GOVERNANCE

### Record 1 — Model Context Protocol (MCP) specification

- Resource name: Model Context Protocol (MCP) specification
- Canonical identity: `modelcontextprotocol.io` — spec repo modelcontextprotocol/specification (public spec at https://modelcontextprotocol.io/specification/latest)
- Category: A — MCP specification
- Type: Open protocol specification (JSON-RPC 2.0 based)
- Official URL: https://modelcontextprotocol.io
- Description: MCP is an open JSON-RPC 2.0 protocol standardizing how LLM agents
  reach external tools and data. Architecture has three roles: hosts, clients,
  servers. Servers expose resources, prompts, and tools; clients may offer
  sampling, roots, and elicitation back. A 1:1 client↔server relationship per
  client instance; a host may run many clients.
- Contents inspected: Spec changelog/vision docs via search results (2025-11-25
  revision changelog; 2026-07-28 revision note), modelcontextprotocol.io
  architecture and versioning pages (referenced), third-party spec timelines.
- Actual capabilities: Primitives — tools (model-callable functions with JSON
  Schema inputs; side-effect capable), resources (read-only data for context),
  prompts (reusable interaction templates). 2025-11-25 (Final): OpenID Connect
  Discovery 1.0 for authorization-server discovery; incremental scope consent
  via WWW-Authenticate; icons metadata for tools/resources/prompts; tool calling
  in sampling; OAuth Client ID Metadata Documents as recommended registration
  mechanism; experimental Tasks (durable requests with polling/deferred results);
  JSON Schema 2020-12 as default dialect. Current revision as of 2026-07-28 per
  versioning page (removed stateful initialize handshake / Mcp-Session-Id header;
  every request carries protocol version and capabilities) — noted from
  secondary source, not directly inspected.
- Usage domain: Agent↔tool/data integration for coding agents and AI assistants.
- Integration method: Protocol; implemented by SDKs; servers over stdio or
  Streamable HTTP (+ legacy SSE).
- Compatibility: Hosts/clients implement chosen spec revisions; 2025-11-25 is
  marked Final (complete, unchanging — a server speaking only it remains
  conformant).
- Dependencies: Not applicable (specification).
- Authentication: Authorization framework: OAuth 2.1 / OIDC discovery;
  incremental scope consent; Client ID Metadata Documents recommended.
- Availability: Open standard, no paywall.
- Maintenance: Stewarded by the Agentic AI Foundation (AAIF) at the Linux
  Foundation (donated by Anthropic 2025-12-09). AAIF grew from 49 founding
  members to 250+ within ~1 year. First official MCP extension: MCP Apps
  (server-rendered interactive UI), shipped 2026-01-26.
- License: Open specification (governance unchanged per donation announcement).
- Security: Trust principles require explicit user consent for all data access
  and tool invocation; hosts must not transmit resource data elsewhere without
  consent. Known ecosystem risks documented separately (see Security tooling).
- Limitations: Spec alone gives no discovery/quality guarantees — registries
  are metadata-only; advertised tool definitions are untrusted input.
- Related resources: AAIF (Record 2), official SDKs (Records 3–5), MCP Registry
  (Record 16), A2A (Record 73), ACP (Record 74).
- Sources: https://modelcontextprotocol.io ; https://hidekazu-konishi.com/entry/mcp_specification_version_timeline.html ; https://temperature2.com/p/2026-09-11-guide-what-is-mcp/ ; http://dev.to/aiarch_wibo/mcp-model-context-protocol-the-three-primitives-and-what-two-real-servers-actually-return-4m21 ; https://github.com/modelcontextprotocol/servers
- Verification date: 2026-10-10. Confidence: High.

### Record 2 — Agentic AI Foundation (AAIF) governance

- Resource name: Agentic AI Foundation (AAIF)
- Canonical identity: Linux Foundation–hosted foundation for agentic AI open standards
- Category: C — structured standards / governance (interoperability)
- Type: Industry foundation / open governance body
- Official URL: Not publicly documented (announcement via linuxfoundation.org; no dedicated canonical URL verified)
- Description: Neutral home for agent standards. Announced 2025-12-09; co-founded
  by OpenAI, Anthropic, and Block (earlier reports also name OpenAI+Anthropic as
  the MCP donors). Founding donated projects: Anthropic's MCP, OpenAI's AGENTS.md,
  Block's goose agent framework. Supporters at launch: Google, Microsoft, AWS,
  Bloomberg, Cloudflare. Google's A2A protocol joined as a hosted project
  2026-08-17/20, consolidating MCP (vertical agent↔tool) and A2A (horizontal
  agent↔agent) under one roof.
- Contents inspected: News reports (Forkast, dev.to, practallogix), AAIF
  knowledge-base docs, MCP Dev Summit (NYC, 2026-04-02/03) notes.
- Actual capabilities: Governance — roadmap stewardship, spec versioning,
  community process. Not a software artifact.
- Usage domain: Standards governance for agent interoperability.
- Integration method: Not applicable.
- Compatibility: Not applicable.
- Dependencies: None.
- Authentication: Not applicable.
- Availability: Active; accepting new projects (per 2026-05 brief).
- Maintenance: Linux Foundation; 250+ members by mid-2026.
- License: Not applicable.
- Security: Not applicable.
- Limitations: Does not itself standardize agent authorization — which data an
  authenticated agent may touch across org boundaries remains each enterprise's
  decision (per AAIF's own design).
- Related resources: MCP spec (Record 1), AGENTS.md (Record 75), A2A (Record 73).
- Sources: https://forkast.news/googles-a2a-protocol-joins-aaif-consolidating-the-agent-economys-protocol-layer-under-one-roof/ ; https://www.practicallogix.com/the-2026-agent-interoperability-reset-a2a-mcp-under-aaif/ ; https://github.com/archie0125/osop-spec/blob/HEAD/docs/strategy/2026-05-01-daily-brief.md ; https://gizmodo.com/openai-anthropic-and-others-create-foundation-for-standardizing-ai-agents-2000697488
- Verification date: 2026-10-10. Confidence: High.

---

## SECTION 2 — OFFICIAL MCP SDKs

### Record 3 — TypeScript MCP SDK

- Resource name: TypeScript MCP SDK
- Canonical identity: `@modelcontextprotocol/sdk` (npm), repo modelcontextprotocol/typescript-sdk
- Category: A — MCP SDKs
- Type: Official SDK (library)
- Official URL: https://github.com/modelcontextprotocol/typescript-sdk (implied by npm scope naming convention; exact repo path not opened — see Limitations)
- Description: Official TypeScript SDK for building MCP servers and clients.
  Reference servers in modelcontextprotocol/servers are implemented with it and
  run via `npx -y @modelcontextprotocol/server-*`.
- Contents inspected: modelcontextprotocol/servers README (SDK list section;
  usage docs); vercel/mcp-handler CLIENTS.md (imports `@modelcontextprotocol/sdk/client`).
- Actual capabilities: Server + client construction, stdio/SSE/Streamable HTTP
  transports; tools/resources/prompts definitions with JSON Schema. Capabilities
  not enumerated exhaustively — not fully inspected.
- Usage domain: Building MCP servers/clients in Node.js/TypeScript.
- Integration method: Library import.
- Compatibility: MCP spec revisions; Node.js runtime.
- Dependencies: Node.js.
- Authentication: Client ID Metadata Documents / OAuth per spec (framework-level).
- Availability: Open source, npm.
- Maintenance: MCP steering group (active; 97M+ monthly SDK downloads across all
  SDKs reported Dec 2025).
- License: Not publicly documented (servers repo new contributions Apache-2.0/existing MIT; SDK license not opened — Unverified).
- Security: Not publicly documented.
- Limitations: Exact repo URL and API surface not opened directly; classification
  as "official" rests on the modelcontextprotocol/servers README SDK list.
- Related resources: Python SDK (Record 4), FastMCP (Record 56).
- Sources: https://github.com/modelcontextprotocol/servers ; https://github.com/vercel/mcp-handler/blob/ce0f0cee3ce60f23746a5c5d28e19d22bed91770/docs/CLIENTS.md ; https://temperature2.com/p/2026-09-11-guide-what-is-mcp/
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 4 — Python MCP SDK

- Resource name: Python MCP SDK
- Canonical identity: `mcp` (PyPI), repo modelcontextprotocol/python-sdk
- Category: A — MCP SDKs
- Type: Official SDK (library)
- Official URL: https://github.com/modelcontextprotocol/python-sdk (implied; not opened — see Limitations)
- Description: Official Python SDK. Reference Python servers run via
  `uvx mcp-server-*` or `pip install`. FastMCP 1.0 (jlowin) was adopted into
  the official Python SDK in 2024.
- Contents inspected: modelcontextprotocol/servers README (uvx/pip usage);
  api-evangelist FastMCP mirror README (lineage statement); multiple community
  server READMEs using the SDK via FastMCP.
- Actual capabilities: Server/client construction over stdio/SSE/Streamable HTTP;
  tools/resources/prompts. FastMCP lineage provides decorator-based server
  definition, JSON Schema auto-generation from type hints, OAuth/OIDC, server
  composition/proxying, OpenAPI/FastAPI import, middleware, elicitation,
  sampling, OpenTelemetry.
- Usage domain: Building MCP servers/clients in Python.
- Integration method: Library import; `fastmcp run` CLI for serving.
- Compatibility: MCP spec revisions; Python ≥ 3.10.
- Dependencies: Python ≥ 3.10; uv/uvx recommended for distribution.
- Authentication: OAuth/OIDC support (via FastMCP lineage).
- Availability: Open source, PyPI.
- Maintenance: MCP steering group; FastMCP lineage maintained by PrefectHQ.
- License: Apache-2.0 (per FastMCP mirror; official SDK license file not opened — treat as Partially verified).
- Security: Stdio servers inherit host process privileges; logging must go to
  stderr (stdout is JSON-RPC framing).
- Limitations: Exact repo URL and current API not opened directly.
- Related resources: FastMCP (Record 56), TypeScript SDK (Record 3).
- Sources: https://github.com/modelcontextprotocol/servers ; https://github.com/api-evangelist/fastmcp/blob/HEAD/README.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 5 — Other official MCP SDKs (C#, Go, Java, Kotlin, PHP, Ruby, Rust, Swift)

- Resource name: Official MCP SDKs — C#, Go, Java, Kotlin, PHP, Ruby, Rust, Swift
- Canonical identity: Listed on modelcontextprotocol/servers README under
  "Typically, each MCP server is implemented with an MCP SDK"
- Category: A — MCP SDKs
- Type: Official SDKs (libraries), combined record
- Official URL: modelcontextprotocol.io documentation (exact per-language repo URLs not opened)
- Description: The steering group lists official SDKs for C#, Go, Java, Kotlin,
  PHP, Python, Ruby, Rust, Swift, and TypeScript. A Go SDK (mcp-go, ejji0113)
  is reported to implement spec 2025-11-25 with backward compatibility to
  2025-06-18, 2025-03-26, 2024-11-05 (community-maintained implementation).
- Contents inspected: modelcontextprotocol/servers README SDK section; ejji0113/mcp-go README (search-result text).
- Actual capabilities: Not inspected per language — Unresolved.
- Usage domain: Building MCP servers/clients in the respective languages.
- Integration method: Library import.
- Compatibility: Per-SDK spec revision support varies.
- Dependencies: Per language runtime.
- Authentication: Per spec authorization framework — Not verified per SDK.
- Availability: Open source (per listing).
- Maintenance: Steering group/community; per-SDK maintenance status Unresolved.
- License: Unresolved per SDK.
- Security: Not publicly documented.
- Limitations: This is a list-level record; no per-SDK repo was opened.
  mark3labs/mcp-go (Go framework) appears in awesome lists as a Go SDK/framework —
  not verified as "official".
- Related resources: Records 3, 4.
- Sources: https://github.com/modelcontextprotocol/servers ; https://github.com/ejji0113/mcp-go ; https://github.com/rohianon/awesome-mcp-servers/blob/HEAD/README.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

---

## SECTION 3 — OFFICIAL REFERENCE SERVERS (modelcontextprotocol/servers)

All maintained by the MCP steering group. Repo: https://github.com/modelcontextprotocol/servers
(~91K stars, ~4.2K commits, created 2024-11-19). Explicitly documented as
reference/educational implementations, NOT production-ready; 12 former servers
archived to modelcontextprotocol/servers-archived. MIT license for existing
code / Apache-2.0 for new contributions.

### Record 6 — Everything (reference/test server)

- Canonical identity: `src/everything` in modelcontextprotocol/servers
- Category: A — official MCP servers
- Type: Reference server (TypeScript)
- Official URL: https://github.com/modelcontextprotocol/servers/tree/main/src/everything
- Description: Reference/test server exercising prompts, resources, and tools;
  used for SDK feature demonstration and client testing.
- Contents inspected: servers README (entry line); modelcontextprotocol docs examples.mdx.
- Actual capabilities: Exposes all three primitives (tools/resources/prompts) —
  read/write classification Not publicly documented in inspected sources.
- Usage domain: SDK development, client conformance testing.
- Integration method: stdio via SDK client.
- Compatibility: Any MCP client.
- Dependencies: Not inspected.
- Authentication: None (local test server).
- Availability: Open source.
- Maintenance: Active (steering group).
- License: MIT/Apache-2.0 (repo-level).
- Security: Reference only; not hardened.
- Limitations: Not for production use per repo README warning.
- Related resources: MCP Inspector (Record 51).
- Sources: https://github.com/modelcontextprotocol/servers ; https://github.com/modelcontextprotocol/modelcontextprotocol/blob/HEAD/docs/examples.mdx
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 7 — Fetch (web content fetching)

- Canonical identity: `@modelcontextprotocol/server-fetch` (npm);
  `src/fetch` in modelcontextprotocol/servers; PyPI `mcp-server-fetch`
- Category: A — official MCP servers; B — browsing/searching, website inspection
- Type: Reference server (Python)
- Official URL: https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- Description: Web content fetching and conversion to markdown for efficient LLM
  usage. Read-only web retrieval (no browser automation).
- Contents inspected: servers README entry; agentic-orchestration mcp-catalog
  (fetch wired as `fetch_url` via `python -m mcp_server_fetch`).
- Actual capabilities: READ-ONLY — fetches a URL and converts content to
  markdown. No write, no command execution.
- Usage domain: Web research, documentation retrieval.
- Integration method: stdio (`uvx mcp-server-fetch` / `python -m mcp_server_fetch`).
- Compatibility: Any MCP client.
- Dependencies: Python, uvx/pip.
- Authentication: None (public web only).
- Availability: Open source.
- Maintenance: Active (steering group).
- License: MIT/Apache-2.0 (repo-level).
- Security: Fetches arbitrary URLs on the model's behalf — prompt-injection
  surface via returned content (untrusted input).
- Limitations: No JavaScript rendering; single-page fetch, no crawl.
- Related resources: Firecrawl (Record 30), Tavily/Exa (Records 28–29).
- Sources: https://github.com/modelcontextprotocol/servers ; https://github.com/zlatko-lakisic/agentic-orchestration/blob/HEAD/docs/mcp-catalog/index.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 8 — Filesystem (secure file operations)

- Canonical identity: `@modelcontextprotocol/server-filesystem` (npm);
  `src/filesystem`
- Category: A — official MCP servers; B — file access
- Type: Reference server (TypeScript)
- Official URL: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Description: Secure file operations with configurable access controls; access
  restricted to explicitly allowed directories passed as CLI args.
- Contents inspected: servers README + usage examples (`npx -y
  @modelcontextprotocol/server-filesystem /path/to/allowed/files`).
- Actual capabilities: READ + WRITE within allowed directories (read/write
  files, list directories). No command execution.
- Usage domain: Local file access for coding agents.
- Integration method: stdio via npx.
- Compatibility: Any MCP client; Windows requires `cmd /c` wrapper.
- Dependencies: Node.js/npx.
- Authentication: None; sandboxing via allowed-path args.
- Availability: Open source.
- Maintenance: Active.
- License: MIT/Apache-2.0 (repo-level).
- Security: HIGH RISK if allowed paths include sensitive dirs — the omnipilot
  docs mark it "risk: high". Write-capable by design.
- Limitations: Reference implementation; no production hardening.
- Related resources: Git server (Record 9).
- Sources: https://github.com/modelcontextprotocol/servers ; https://github.com/xrchris7/omnipilot/blob/HEAD/docs/mcp.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 9 — Git (repository operations)

- Canonical identity: `mcp-server-git` (PyPI); `src/git`
- Category: A — official MCP servers; B — GitHub operations / codebase search (local git)
- Type: Reference server (Python)
- Official URL: https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Description: Tools to read, search, and manipulate Git repositories
  (scoped to a `--repository` path).
- Contents inspected: servers README (`uvx mcp-server-git --repository path/to/git/repo`).
- Actual capabilities: READ + WRITE — read/search plus manipulation (commit etc.)
  within the target repo. No arbitrary command execution documented.
- Usage domain: Local git workflows for coding agents.
- Integration method: stdio via uvx/pip.
- Compatibility: Any MCP client.
- Dependencies: Python, git binary (implied — Not verified).
- Authentication: None (local).
- Availability: Open source.
- Maintenance: Active.
- License: MIT/Apache-2.0 (repo-level).
- Security: Can mutate the repository; "risk: medium" per omnipilot docs.
- Limitations: Local repos only; not a GitHub API client (that is github/github-mcp-server — dedup).
- Related resources: GitHub MCP (dedup cross-ref).
- Sources: https://github.com/modelcontextprotocol/servers
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 10 — Memory (knowledge graph)

- Canonical identity: `@modelcontextprotocol/server-memory` (npm); `src/memory`
- Category: A — official MCP servers; B — memory/retrieval
- Type: Reference server (TypeScript)
- Official URL: https://github.com/modelcontextprotocol/servers/tree/main/src/memory
- Description: Knowledge graph–based persistent memory: entities, relations,
  observations stored as local JSON/JSONL file (`MEMORY_FILE_PATH`).
- Contents inspected: servers README; Bridge integration PR text enumerating
  tools: `create_entities`, `create_relations`, `add_observations`,
  `search_nodes`, `open_nodes`; hazemhagrass/ai-compute mcp/memory.md
  (stdio, MIT, `MEMORY_FILE_PATH` config).
- Actual capabilities: READ + WRITE to local JSONL knowledge graph (create/read/
  search entities & relations). No command execution.
- Usage domain: Cross-session agent memory (per-user, cross-project, mutable facts).
- Integration method: stdio via npx.
- Compatibility: Any MCP client; Smithery install supported.
- Dependencies: Node.js/npx.
- Authentication: None (local file).
- Availability: Open source.
- Maintenance: Active.
- License: MIT (per ai-compute doc; repo-level MIT/Apache-2.0).
- Security: Local file; no network. Double-write risk when host has its own
  memory (two sources of truth).
- Limitations: Single-file JSONL; no vector search (keyword/semantic via search_nodes only as documented).
- Related resources: basic-memory (Record 40), Mimir (Record 41), Servex (Record 42).
- Sources: https://github.com/modelcontextprotocol/servers ; https://github.com/hazemhagrass/ai-compute/blob/HEAD/mcp/memory.md
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 11 — Sequential Thinking

- Canonical identity: `@modelcontextprotocol/server-sequential-thinking` (npm, presumed); `src/sequentialthinking`
- Category: A — official MCP servers
- Type: Reference server (TypeScript)
- Official URL: https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- Description: Dynamic, reflective problem-solving through structured thought
  sequences — a tool the model calls to externalize multi-step reasoning.
- Contents inspected: servers README entry line only.
- Actual capabilities: Tool(s) for thought sequencing — exact tool names Not
  publicly documented in inspected sources. No file/network side effects
  documented (presumed read-only — Unverified).
- Usage domain: Structured reasoning for agents.
- Integration method: stdio via npx (presumed).
- Compatibility: Any MCP client.
- Dependencies: Node.js (presumed).
- Authentication: None (presumed).
- Availability: Open source.
- Maintenance: Active.
- License: MIT/Apache-2.0 (repo-level).
- Security: Not publicly documented.
- Limitations: Entry-level record; tool definitions not inspected.
- Related resources: Everything (Record 6).
- Sources: https://github.com/modelcontextprotocol/servers
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 12 — Time

- Canonical identity: `@modelcontextprotocol/server-time` (npm, presumed); `src/time`
- Category: A — official MCP servers
- Type: Reference server
- Official URL: https://github.com/modelcontextprotocol/servers/tree/main/src/time
- Description: Time and timezone conversion capabilities.
- Contents inspected: servers README entry line only.
- Actual capabilities: READ-ONLY (time queries/conversions) — exact tools Not
  publicly documented in inspected sources.
- Usage domain: Timezone-aware agent tasks.
- Integration method: stdio (presumed).
- Compatibility: Any MCP client.
- Dependencies: Not verified.
- Authentication: None (presumed).
- Availability: Open source.
- Maintenance: Active.
- License: MIT/Apache-2.0 (repo-level).
- Security: Not publicly documented.
- Limitations: Entry-level record.
- Related resources: —
- Sources: https://github.com/modelcontextprotocol/servers
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Archived reference servers (note, not full records)

The following were reference servers and are now archived at
modelcontextprotocol/servers-archived (historical reference only, not actively
maintained): AWS KB Retrieval, Brave Search (replaced by brave/brave-search-mcp-server),
EverArt, GitHub (superseded by github/github-mcp-server — dedup), GitLab, Google Drive,
Google Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack (now maintained by Zencoder),
SQLite. Label: Archived. Sources: https://github.com/modelcontextprotocol/servers ;
https://github.com/modelcontextprotocol/modelcontextprotocol/blob/HEAD/docs/examples.mdx

---

## SECTION 4 — OFFICIAL / VENDOR-MAINTAINED MCP INTEGRATIONS

### Record 13 — Figma Dev Mode MCP Server (official)

- Resource name: Figma Dev Mode MCP Server
- Canonical identity: Built into Figma desktop app (Dev Mode) + remote hosted server
- Category: A — official MCP servers; B — Figma/design, website inspection
- Type: First-party MCP server (ships inside the product)
- Official URL: https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server ; https://developers.figma.com/docs/figma-mcp-server/local-server-installation/
- Description: Figma's official MCP server exposing design files to coding agents
  for design→code workflows. Two deployments: (1) Desktop server at
  `http://127.0.0.1:3845/mcp`, enabled via Figma → Preferences → "Enable Dev Mode
  MCP server", inheriting the desktop app's session (no separate auth; requires
  Dev or Full seat); (2) Remote server at `https://mcp.figma.com/mcp` with
  OAuth 2.1, broader features including write-to-canvas tools.
- Contents inspected: zyqxd/my-stuff ai/figma-mcp README (local vs remote table,
  OAuth registration observations); lucasschirm claude-marketplace skill
  (tool list); moh4696/50-essential-mcp-servers (remote vs desktop note);
  pixelcore1/colour-ramp-studio README (setup docs links).
- Actual capabilities: READ-ONLY on desktop: `get_metadata`, `get_variable_defs`,
  `get_code`, `get_code_connect_map`, `get_image`/`get_screenshot`
  (tool names may vary by Figma version). Remote adds WRITE (write-to-canvas).
  No command execution.
- Usage domain: Design systems, design-to-code, design inspection.
- Integration method: Streamable HTTP (local URL or remote URL); OAuth for remote.
- Compatibility: Any MCP client supporting Streamable HTTP + OAuth (remote);
  note one 2026-08 report that Figma's dynamic client registration allowlists
  specific client names (Claude Code registered; others 403 at that time) — treat as
  time-sensitive, Partially verified.
- Dependencies: Figma desktop app running with file open (desktop); Figma account (remote).
- Authentication: Desktop — none (inherits app session). Remote — OAuth 2.1,
  scope `mcp:connect`.
- Availability: GA (Dev/Full seat required for desktop server).
- Maintenance: Active (Figma).
- License: Proprietary service; server ships with Figma.
- Security: Desktop server binds localhost; remote uses per-user OAuth. Design
  data is proprietary — consent/scope considerations apply.
- Limitations: Desktop serves only the currently open file; write tools only on
  remote; OAuth client allowlist friction observed.
- Related resources: blueberry-team/figma-dev-mode-for-free (community bridge,
  Partially verified via search text).
- Sources: https://github.com/zyqxd/my-stuff/blob/HEAD/ai/figma-mcp/README.md ; https://github.com/lucasschirm/claude-marketplace/blob/HEAD/plugins/frontend-development/skills/figma-dev-mode-extraction/SKILL.md ; https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server ; https://github.com/moh4696/50-essential-mcp-servers/blob/HEAD/servers/08-creator-tools.md
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 14 — Brave Search MCP Server (official, Brave)

- Resource name: Brave Search MCP Server
- Canonical identity: `brave/brave-search-mcp-server` (GitHub); npm `@brave/brave-search-mcp-server`
- Category: A — official MCP servers; B — browsing/searching the internet
- Type: Vendor MCP server (TypeScript; Node/Bun dual runtime)
- Official URL: https://github.com/brave/brave-search-mcp-server
- Description: Brave's official MCP server for the Brave Search API. Supersedes
  the archived MCP reference server (`@modelcontextprotocol/server-brave-search`).
  Tools (v2.x): `brave_web_search`, `brave_local_search`, `brave_news_search`,
  `brave_video_search`, `brave_image_search`, `brave_place_search`,
  `brave_summarizer`, `brave_llm_context`, `brave_answers`, `brave_autosuggest`,
  `brave_spellcheck`. Parameters include query, country, count/offset, safesearch,
  freshness, result_filter, goggles; `--enabled-tools` flag narrows exposure.
- Contents inspected: tobiashochguertel mirror README (full tool table +
  per-endpoint API-key env vars); kbennett2000 mirror README (parameter docs);
  macabdul9/root browser-mcp doc (`--transport stdio`, `--enabled-tools` usage);
  mcp-bazaar pricing note (Aug 2025 AI Grounding update: $5/month free credits,
  card required — secondary).
- Actual capabilities: READ-ONLY — web/local/news/video/image search, AI
  summarization/answers, autosuggest, spellcheck. No write, no execution.
- Usage domain: Web research, grounding, local search.
- Integration method: stdio (`npx -y @brave/brave-search-mcp-server`) or Docker
  (`brave/brave-search-mcp-server:v2.1.3`, version-pinned, no `latest` tag).
- Compatibility: Any MCP client.
- Dependencies: Brave Search API key(s): `BRAVE_API_KEY` fallback;
  `BRAVE_SEARCH_API_KEY`, `BRAVE_AI_API_KEY`, `BRAVE_ANSWERS_API_KEY`,
  `BRAVE_AUTOSUGGEST_API_KEY`, `BRAVE_SPELLCHECK_API_KEY`.
- Authentication: API key (env vars).
- Availability: Free tier ($5/month credits) + paid plans; rate limits apply.
- Maintenance: Active (Brave).
- License: Not verified from opened sources (mirror READMEs; official repo
  license not opened — Unverified).
- Security: API key in env; returned web content is untrusted input (prompt
  injection surface).
- Limitations: Free-tier credits limited; Pro plan needed for full local search;
  paid tiers for summarizer/answers/autosuggest.
- Related resources: Tavily (Record 28), Exa (Record 29), Firecrawl (Record 30).
- Sources: https://github.com/tobiashochguertel/brave-search-mcp-server ; https://github.com/kbennett2000/brave-search-mcp-server/blob/HEAD/README.md ; https://github.com/macabdul9/root/blob/HEAD/docs/browser-mcp/README.md ; https://github.com/drvivek34/mcp-bazaar/blob/HEAD/search-web/brave-search-mcp/README.md
- Verification date: 2026-10-10. Confidence: High. Label: Verified.
  (Primary official repo page not opened; tool definitions verified via mirrors
  of the official docs. Treat mirror-derived details as Partially verified.)

### Record 15 — Stripe Agent Toolkit / Stripe MCP Server (official)

- Resource name: Stripe Agent Toolkit (`@stripe/mcp`)
- Canonical identity: `stripe/agent-toolkit` (GitHub); npm `@stripe/mcp`; remote `https://mcp.stripe.com`
- Category: A — official MCP servers; B — external business services (payments)
- Type: Vendor MCP server (TypeScript) + function-calling SDKs
- Official URL: https://github.com/stripe/agent-toolkit ; https://docs.stripe.com/mcp
- Description: Stripe's official MCP server exposing the Payments API as agent
  tools (~23–25 tools across ~13 categories: customers, products, prices,
  invoices, subscriptions, payment links, refunds, disputes, coupons, webhook
  events, Radar rules). Tool availability adapts to the API key's permissions.
  `--tools=` flag scopes exposure (e.g. `customers.read,products.read,
  payment_links.create`).
- Contents inspected: Secondary skill docs and scout reports (tool counts,
  setup, scoping); samotech/mcp-atlas server profile (auth model, risk notes).
  Official README not opened.
- Actual capabilities: READ + WRITE — read charges/customers/invoices/
  subscriptions; write refunds, payment links, customer metadata. Real financial
  side effects possible in live mode.
- Usage domain: Payments, billing, subscription management.
- Integration method: stdio (`npx -y @stripe/mcp --tools=all`) or remote
  (`https://mcp.stripe.com`, OAuth).
- Compatibility: MCP clients; also OpenAI Agent SDK, LangChain, CrewAI, Vercel
  AI SDK via function calling.
- Dependencies: `STRIPE_SECRET_KEY` (sk_live_/sk_test_); Restricted Keys
  (rk_live_) recommended.
- Authentication: API key / restricted key; OAuth on remote.
- Availability: Stripe account required; test vs live mode separation at key level.
- Maintenance: Active (Stripe).
- License: Not verified from opened sources.
- Security: HIGH — live-mode keys can trigger real financial transactions;
  use restricted keys with minimum scopes; all calls logged by Stripe API.
- Limitations: Blast radius must be managed via key scoping; refund/dispute
  writes need elevated scope.
- Related resources: —
- Sources: https://github.com/carloscape/octorato/blob/HEAD/skills/stripe-payments/SKILL.md ; https://github.com/hinvec/security-scanned-skills/blob/HEAD/skills/stripe-agent-toolkit-ai-payment-integration/SKILL.md ; https://github.com/samotech/mcp-atlas/blob/HEAD/data/servers/stripe-mcp.md ; https://github.com/chintanmehta21/claude-agents/issues/1
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 16 — AWS Labs MCP servers (awslabs/mcp monorepo)

- Resource name: AWS MCP Servers (awslabs/mcp)
- Canonical identity: `awslabs/mcp` (GitHub monorepo); PyPI namespace `awslabs.*`
- Category: A — official MCP servers; B — cloud infrastructure, documentation retrieval, logging/observability
- Type: Vendor MCP server collection (Python, ~60–61 servers as of 2026-07)
- Official URL: https://github.com/awslabs/mcp
- Description: AWS's official answer to agent access to AWS — not one server but
  ~60 specialized servers, one per service/workflow, so agents get only the
  permissions they need: `awslabs.aws-documentation-mcp-server` (docs search,
  markdown conversion, table search, recommendations), `awslabs.cloudwatch-mcp-server`
  (metrics, alarms, logs), `awslabs.dynamodb-mcp-server`, `awslabs.iam-mcp-server`,
  `awslabs.amazon-sns-sqs-mcp-server`, `awslabs.billing-cost-management-mcp-server`,
  `awslabs.bedrock-kb-retrieval-mcp-server` (Bedrock Knowledge Bases), `awslabs.core-mcp-server`
  (orchestrates other AWS servers), plus eks/postgres/pricing/iac/well-architected
  servers. Each publishes to PyPI independently (`awslabs.<server>`), versioned by
  release timestamp rather than SemVer. Separate AWS-managed remote server:
  `aws-mcp.us-east-1.api.aws/mcp` (GA 2026-05-06, ~10 tools: API exec, docs,
  Agent SOPs) reached via local `mcp-proxy-for-aws` SigV4-signing proxy, with
  CloudTrail attribution of every call; it supersedes `aws-api-mcp-server` and
  `aws-knowledge-mcp-server`.
- Contents inspected: marblo-app/marblo AWS MCP reference (monorepo layout,
  uvx install pattern, star counts); awslabs/mcp aws-documentation README
  (features, install config); richardsonjf mirror (core/documentation/bedrock-kb
  servers); mpurushotham/cloud-aws-platform-management docs (managed vs
  self-hosted comparison, SigV4 proxy architecture); hrushikesh-prog/aws_mcp
  (server table; notes no official EC2-management server exists).
- Actual capabilities: READ + WRITE — varies per server; documentation server is
  read-only, while service servers (IAM, SNS/SQS, DynamoDB, etc.) can mutate AWS
  resources under the configured credential chain.
- Usage domain: AWS cloud operations, docs retrieval, cost management, observability.
- Integration method: stdio via `uvx awslabs.<server>@latest` with AWS credential
  chain (env `AWS_PROFILE`, `AWS_REGION`); managed remote via mcp-proxy-for-aws.
- Compatibility: Any MCP client.
- Dependencies: uv/Python ≥3.10; AWS credentials.
- Authentication: AWS credential chain (IAM identity); SigV4 for the managed endpoint.
- Availability: Free (pay only for AWS resources used). No official general EC2
  management server (gap filled by community servers).
- Maintenance: Active (AWS Labs; ~9.5K stars, daily pushes as of 2026-07-29).
- License: Apache-2.0.
- Security: Servers act with whatever AWS credentials they find — never run from
  a root session. Least-privilege IAM policies essential; CloudTrail audits API
  calls (MCP-context attribution only on the managed endpoint).
- Limitations: One-service-per-server granularity (by design); versioning by
  timestamp is unusual; managed server is us-east-1 only per cited docs.
- Related resources: awslabs/openapi-mcp-server (dedup xref), mcp-proxy-for-aws
  (Record 72), Cloudflare (Record 21).
- Sources: https://github.com/awslabs/mcp ; https://github.com/awslabs/mcp/blob/main/src/aws-documentation-mcp-server/README.md ; https://github.com/marblo-app/marblo/blob/HEAD/mcp-servers/aws-mcp/README.md ; https://github.com/mpurushotham/cloud-aws-platform-management/blob/HEAD/docs/mcp/README.md ; https://github.com/hrushikesh-prog/aws_mcp/blob/HEAD/README.md
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 17 — Sentry MCP Server (official, getsentry/sentry-mcp)

- Resource name: Sentry MCP Server
- Canonical identity: `getsentry/sentry-mcp` (GitHub)
- Category: A — official MCP servers; B — logging/observability
- Type: Vendor MCP server
- Official URL: https://github.com/getsentry/sentry-mcp (named in security-researcher skill doc; repo page not opened)
- Description: Sentry's official MCP server for retrieving and analyzing issues
  from Sentry.io (supersedes the archived reference Sentry server).
- Contents inspected: ns-aisaichakaravarthi/claude-skills mcp-security-researcher
  SKILL.md (vendor table). Repo README not opened.
- Actual capabilities: READ-ONLY (issue retrieval/analysis) — presumed; not
  verified from primary source.
- Usage domain: Error tracking, observability.
- Integration method: Not verified.
- Compatibility: MCP clients.
- Dependencies: Sentry account/API token (presumed — Not verified).
- Authentication: Not verified.
- Availability: Not verified.
- Maintenance: Active (Sentry) — presumed from vendor table.
- License: Not verified.
- Security: Not publicly documented.
- Limitations: Entry-level record; capabilities/auth not inspected.
- Related resources: Datadog MCP (Record 18).
- Sources: https://github.com/ns-aisaichakaravarthi/claude-skills/blob/HEAD/mcp-security-researcher/SKILL.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 18 — Datadog MCP Server (official, DataDog/datadog-mcp-server)

- Resource name: Datadog MCP Server
- Canonical identity: `DataDog/datadog-mcp-server` (GitHub)
- Category: A — official MCP servers; B — logging/observability
- Type: Vendor MCP server
- Official URL: https://github.com/DataDog/datadog-mcp-server (named in skill doc; not opened)
- Description: Datadog's official MCP server for observability data access.
- Contents inspected: vendor table in mcp-security-researcher SKILL.md only.
- Actual capabilities: Not verified.
- Usage domain: Metrics, logs, traces (presumed).
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: Datadog account/API key (presumed).
- Authentication: Not verified.
- Availability: Not verified.
- Maintenance: Presumed active.
- License: Not verified.
- Security: Not publicly documented.
- Limitations: Entry-level record.
- Related resources: Sentry MCP (Record 17).
- Sources: https://github.com/ns-aisaichakaravarthi/claude-skills/blob/HEAD/mcp-security-researcher/SKILL.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 19 — GitLab MCP Server (official)

- Resource name: GitLab MCP Server (official)
- Canonical identity: GitLab-maintained; docs at docs.gitlab.com (exact repo/path not verified)
- Category: A — official MCP servers; B — GitHub operations (GitLab equivalent)
- Type: Vendor MCP server
- Official URL: https://docs.gitlab.com (MCP server docs; exact URL not verified)
- Description: GitLab's official MCP server for project management and GitLab
  API operations.
- Contents inspected: vortex-dev00/god-repo MCP ecosystem list only.
- Actual capabilities: READ + WRITE (project management) — presumed, not verified.
- Usage domain: GitLab DevOps workflows.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: GitLab token (presumed).
- Authentication: Not verified.
- Availability: Not verified.
- Maintenance: Presumed active.
- License: Not verified.
- Security: Not publicly documented.
- Limitations: Entry-level record.
- Related resources: GitHub MCP (dedup xref), Linear (Record 48).
- Sources: https://github.com/vortex-dev00/god-repo/blob/HEAD/developers/mcp-ecosystem/README.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 20 — Notion MCP Server (official, makenotion/notion-mcp-server)

- Resource name: Notion MCP Server (official)
- Canonical identity: `makenotion/notion-mcp-server` (GitHub)
- Category: A — official MCP servers; B — external business services (productivity)
- Type: Vendor MCP server
- Official URL: https://github.com/makenotion/notion-mcp-server (named in ecosystem list; not opened)
- Description: Notion's official MCP server for workspace/page/database access.
- Contents inspected: god-repo MCP ecosystem list only.
- Actual capabilities: READ + WRITE (pages/databases) — presumed, not verified.
- Usage domain: Knowledge management, productivity.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: Notion integration token (presumed).
- Authentication: Not verified.
- Availability: Not verified.
- Maintenance: Presumed active.
- License: Not verified.
- Security: Not publicly documented.
- Limitations: Entry-level record.
- Related resources: Linear (Record 48), Google Workspace MCP (Record 23).
- Sources: https://github.com/vortex-dev00/god-repo/blob/HEAD/developers/mcp-ecosystem/README.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 21 — Cloudflare MCP servers (official)

- Resource name: Cloudflare MCP servers
- Canonical identity: `cloudflare/mcp-server-cloudflare` (GitHub); Cloudflare
  Browser Rendering MCP at https://developers.cloudflare.com/browser-rendering/platform/playwright-mcp/
- Category: A — official MCP servers; B — cloud infrastructure, browser automation
- Type: Vendor MCP servers
- Official URL: https://developers.cloudflare.com/browser-rendering/platform/playwright-mcp/
- Description: Cloudflare's official MCP servers. The Browser Rendering MCP lets
  agents drive a headless browser via Cloudflare's infrastructure (Playwright-based).
  A general Cloudflare MCP server exists at cloudflare/mcp-server-cloudflare
  (per vendor table). Cloudflare is also an AAIF supporter/platinum member.
- Contents inspected: god-repo ecosystem list (Browser Rendering MCP URL);
  vendor table (mcp-server-cloudflare); mcp-remote example using
  `https://<account>.mcp.cloudflare.io/mcp` with Bearer <redacted>
- Actual capabilities: READ + WRITE/EXECUTE — browser control; account
  management (presumed) — not fully verified.
- Usage domain: Browser automation, Cloudflare account operations.
- Integration method: Remote Streamable HTTP with Bearer <redacted>
- Compatibility: MCP clients supporting Streamable HTTP + auth.
- Dependencies: Cloudflare account + API token.
- Authentication: Bearer <redacted> / account token.
- Availability: Cloudflare account required; rate limits apply (presumed).
- Maintenance: Active (Cloudflare).
- License: Not verified.
- Security: Browser automation can interact with arbitrary web content —
  prompt-injection surface; account-level write access.
- Limitations: Remote-only; auth required.
- Related resources: Browserbase (Record 22), microsoft/playwright-mcp (dedup xref).
- Sources: https://github.com/vortex-dev00/god-repo/blob/HEAD/developers/mcp-ecosystem/README.md ; https://github.com/ns-aisaichakaravarthi/claude-skills/blob/HEAD/mcp-security-researcher/SKILL.md ; https://github.com/xrchris7/omnipilot/blob/HEAD/docs/mcp.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 22 — Browserbase MCP Server (official, browserbase/mcp-server-browserbase)

- Resource name: Browserbase MCP Server
- Canonical identity: `browserbase/mcp-server-browserbase` (GitHub); npm `@browserbasehq/mcp`; hosted `https://mcp.browserbase.com/mcp`
- Category: A — official MCP servers; B — browser automation
- Type: Vendor MCP server (Stagehand-based browser control)
- Official URL: https://github.com/browserbase/mcp-server-browserbase
- Description: Official MCP server letting LLMs control a browser via Browserbase
  infrastructure and Stagehand. Two modes: SHTTP hosted (`https://mcp.browserbase.com/mcp`,
  recommended, includes hosted LLM costs for Gemini) and self-hosted STDIO via
  npm (`@browserbasehq/mcp`) or local clone.
- Contents inspected: browserbase/mcp-server-browserbase README (search-result
  text: SHTTP config, stdio config with BROWSERBASE_API_KEY,
  BROWSERBASE_PROJECT_ID, GEMINI_API_KEY; `--modelName` option).
- Actual capabilities: READ + WRITE/EXECUTE — full browser control (navigate,
  click, type, scrape). JS-rendered pages supported (unlike Fetch).
- Usage domain: Browser automation, web scraping, web testing.
- Integration method: Remote Streamable HTTP or stdio via npx.
- Compatibility: Any MCP client; clients without SHTTP use `mcp-remote` bridge.
- Dependencies: Browserbase API key + project ID (+ Gemini API key for
  self-hosted model choice).
- Authentication: API key.
- Availability: Hosted service; free tier/quotas per Browserbase pricing (not verified).
- Maintenance: Active (Browserbase).
- License: Not verified from opened sources.
- Security: Browser executes arbitrary web content — prompt-injection surface;
  API keys grant browser-session control.
- Limitations: Hosted dependency unless self-hosted.
- Related resources: Cloudflare Browser Rendering (Record 21), microsoft/playwright-mcp (dedup xref).
- Sources: https://github.com/browserbase/mcp-server-browserbase
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 23 — Google Workspace MCP servers (official)

- Resource name: Google Workspace MCP servers (Gmail, Drive, Calendar)
- Canonical identity: Google-maintained; docs at developers.google.com/workspace
- Category: A — official MCP servers; B — external business services
- Type: Vendor MCP servers
- Official URL: https://developers.google.com/workspace/guides/configure-mcp-servers (cited in ecosystem list; not opened)
- Description: Google's official MCP servers for Gmail, Drive, and Calendar
  (Workspace APIs exposed to agents).
- Contents inspected: god-repo ecosystem list only.
- Actual capabilities: READ + WRITE (email/drive/calendar operations) — presumed, not verified.
- Usage domain: Productivity, email, scheduling.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: Google account + OAuth (presumed).
- Authentication: OAuth (presumed).
- Availability: Not verified.
- Maintenance: Presumed active.
- License: Not verified.
- Security: High-sensitivity scopes (email/drive) — consent and scope
  minimization apply (general, not source-verified for these servers).
- Limitations: Entry-level record.
- Related resources: Notion MCP (Record 20).
- Sources: https://github.com/vortex-dev00/god-repo/blob/HEAD/developers/mcp-ecosystem/README.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 24 — GitHub MCP Server (official) — dedup cross-reference

- Resource name: GitHub MCP Server (official, github/github-mcp-server)
- Canonical identity: `github/github-mcp-server`
- Category: A — official MCP servers; B — GitHub operations
- Type: Vendor MCP server (dedup — already catalogued)
- Official URL: https://github.com/github/github-mcp-server
- Description: Already covered by the OpenCode ecosystem catalog (official
  OpenCode install guide exists). Cross-referenced here only: it is GitHub's
  official MCP server for repository management, file operations, and GitHub API
  integration, superseding the archived reference GitHub server.
- Contents inspected: Not re-inspected (dedup).
- Sources: https://github.com/modelcontextprotocol/servers ; https://github.com/vortex-dev00/god-repo/blob/HEAD/developers/mcp-ecosystem/README.md
- Verification date: 2026-10-10. Confidence: High. Label: Verified (as cross-reference).
- Note: Do NOT re-research; see the OpenCode catalog for the full record.

---

## SECTION 5 — MCP SERVER REGISTRIES AND DIRECTORIES

### Record 25 — Official MCP Registry (registry.modelcontextprotocol.io)

- Resource name: MCP Registry (official)
- Canonical identity: `registry.modelcontextprotocol.io`; repo modelcontextprotocol/registry
- Category: A — MCP server registries/directories
- Type: Canonical metadata registry (federated "metaregistry"); REST API only
- Official URL: https://registry.modelcontextprotocol.io
- Description: Launched in preview 2025-09-08. Open catalog and API for publicly
  available MCP servers — a "source of truth" metadata layer (no code or
  binaries of its own), designed as a federated metaregistry supporting public
  and private sub-registries (DNS-like). Backed by Anthropic, GitHub, PulseMCP,
  and Microsoft. Publishing via `mcp-publisher` CLI with `server.json`;
  authentication by GitHub or DNS verification; names are reverse-DNS
  (`io.github.owner/server-name`), URL-encoded in paths. Supports remote
  servers and sub-registries.
- Contents inspected: Registry API docs via skill docs (endpoints
  `/v0.1/servers`, search params `search`/`limit`/`cursor`/`updated_since`/
  `version=latest`); enclawed/omcp aggregator docs (aggregator guidance, hourly
  scraping expectation, no uptime/durability guarantees); omcp quickstart
  (publish flow, troubleshooting table); TechCommunity article (sub-registry model).
- Actual capabilities: READ-ONLY public API (list/search/get server metadata).
  Publishing is write via authenticated CLI.
- Usage domain: Server discovery, publishing, machine-readable metadata for clients.
- Integration method: REST API (no auth for reads); `mcp-publisher` CLI for publishing.
- Compatibility: Clients/aggregators consume the REST API.
- Dependencies: None for reads.
- Authentication: None for reads; GitHub/DNS verification for publishing.
- Availability: Preview (breaking changes/data resets possible per aggregator docs).
- Maintenance: Active (MCP steering group).
- License: Open (spec open; registry repo not inspected for license).
- Security: Namespace auth (GitHub/DNS) for publishing; no code hosting means
  no binary trust — listings are metadata, still require user audit.
- Limitations: API-only (no browse UI); ~9.6K servers (per MCPFind comparison);
  does not verify code quality or safety.
- Related resources: mcp-publisher CLI, MCP Harbor (Record 33), aggregators.
- Sources: https://registry.modelcontextprotocol.io ; https://github.com/enclawed/omcp/blob/HEAD/docs/registry/registry-aggregators.mdx ; https://github.com/enclawed/omcp/blob/HEAD/docs/registry/quickstart.mdx ; https://techcommunity.microsoft.com/discussions/appsonazure/how-to-use-the-newly-launched-mcp-registry/4452855 ; https://github.com/openclaw/skills (mcp-registry SKILL.md, search-result text) ; https://github.com/smartpropertychile-ai/seldonframe/blob/HEAD/skills/mcp-server/DISTRIBUTION.md
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 26 — mcp.so

- Resource name: mcp.so
- Canonical identity: https://mcp.so
- Category: A — MCP server registries/directories
- Type: Community directory (highest-volume free directory by listing count)
- Official URL: https://mcp.so
- Description: Large community MCP server directory (~20K–23K servers). Free to
  list and browse; no hosting; quality signal is GitHub star count; submit via
  its submit flow (repo/npm).
- Contents inspected: Directory comparisons (seosiri monetization analysis,
  mcpfind directory comparison, assurly submission docs, agora DIRECTORY-LISTINGS).
- Actual capabilities: Browsing/searching listings (read-only web UI).
- Usage domain: Server discovery.
- Integration method: Web UI; submit form at mcp.so/submit.
- Compatibility: Not applicable.
- Dependencies: None.
- Authentication: Not documented.
- Availability: Free.
- Maintenance: Active (per comparisons).
- License: Not open source (per comparison table).
- Security: Listings are unverified community submissions — audit before use.
- Limitations: No hosting, no install help beyond GitHub links; star-count
  quality signal is weak.
- Related resources: mcp.directory (Record 27), Glama (Record 28), Smithery (Record 29).
- Sources: https://www.seosiri.com/2026/09/mcp-monetization-gap-glama-smithery-developer-losses.html ; https://github.com/mcpfind/mcp-find/blob/HEAD/apps/web/content/blog/mcp-server-directories-compared.mdx ; https://github.com/assurly/assurly/blob/HEAD/docs/mcp-directory-submissions.md ; https://github.com/ritik200238/agora/blob/HEAD/mcp/DIRECTORY-LISTINGS.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 27 — mcp.directory

- Resource name: mcp.directory
- Canonical identity: https://mcp.directory
- Category: A — MCP server registries/directories
- Type: Community directory with web submission form
- Official URL: https://mcp.directory
- Description: Community MCP directory. Submission via web form at
  mcp.directory/submit: auto-detects metadata from the GitHub repo + npm
  package; listing appears within ~24 hours per its stated SLA (per a
  maintainer's distribution doc). Note: distinct from the similarly named
  GitHub scraper projects (luciferforge/mcp-directory, nandanhegde1/mcp-directory).
- Contents inspected: seldonframe DISTRIBUTION.md (submission flow). Directory
  homepage not opened.
- Actual capabilities: Listing submission + browsing (read-only).
- Usage domain: Server discovery/publishing.
- Integration method: Web form.
- Compatibility: Not applicable.
- Dependencies: None.
- Authentication: Email optional (notification).
- Availability: Presumed active.
- Maintenance: Not verified.
- License: Not verified.
- Security: Community listings — audit before use.
- Limitations: Listing counts, curation policy, and ownership not verified.
- Related resources: mcp.so (Record 26).
- Sources: https://github.com/smartpropertychile-ai/seldonframe/blob/HEAD/skills/mcp-server/DISTRIBUTION.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 28 — Glama (glama.ai/mcp)

- Resource name: Glama MCP directory + gateway
- Canonical identity: https://glama.ai/mcp
- Category: A — MCP server registries/directories; also A — MCP permission management
- Type: Curated directory + hosted gateway (freemium SaaS)
- Official URL: https://glama.ai
- Description: One of the largest curated directories (~33K–50K servers indexed
  depending on count date) with A–F quality grades, built-in inspector, and a
  hosted gateway offering OAuth, logging, and per-tool access control.
  Freemium SaaS ($9/$26/$80 tiers bundling AI credits and hosted server slots;
  open-source maintainers can host free). No published creator revenue-share
  program. Auto-discovers servers from npm + GitHub.
- Contents inspected: seosiri monetization analysis (tiers, model);
  mcpfind comparison (grades, inspector, gateway); obsidian-vault comparison
  (browsing experience, categorization); agora listing guide (auto-indexing).
- Actual capabilities: Directory browsing (read-only); hosted gateway with
  per-tool access control (permission management — admin-configured).
- Usage domain: Discovery, hosted MCP access with access control.
- Integration method: Web UI; hosted gateway endpoints; 3-client gateway support (per comparison).
- Compatibility: MCP clients.
- Dependencies: Account for hosting; OAuth for gateway.
- Authentication: OAuth on hosted gateway.
- Availability: Freemium; rate limits per tier.
- Maintenance: Active.
- License: Not open source.
- Security: Gateway adds OAuth + logging + per-tool access control — a
  permission-management layer; underlying server code still third-party.
- Limitations: Grading methodology not inspected; monetization terms for
  creators not published.
- Related resources: Smithery (Record 29), MCP Registry (Record 25).
- Sources: https://www.seosiri.com/2026/09/mcp-monetization-gap-glama-smithery-developer-losses.html ; https://github.com/mcpfind/mcp-find/blob/HEAD/apps/web/content/blog/mcp-server-directories-compared.mdx ; https://github.com/ole00007/obsidian-vault/blob/HEAD/03-Resources/Hermes-Setup-and-MCP/Point6_Skill_MCP_Marketplaces_Extended.md ; https://github.com/ritik200238/agora/blob/HEAD/mcp/DIRECTORY-LISTINGS.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 29 — Smithery (smithery.ai)

- Resource name: Smithery
- Canonical identity: https://smithery.ai
- Category: A — MCP server registries/directories; A — MCP configuration tools
- Type: Registry + one-click hosted deployment ("Toolbox" meta-MCP router)
- Official URL: https://smithery.ai
- Description: Popular hosted MCP catalog (~6K–7.3K servers) with one-click
  installs. Connect a GitHub repo; it reads package + README. CLI:
  `npx -y @smithery/cli install <server>`. Freemium with usage-based pricing on
  hosted servers. Creator monetization claims are inconsistent across sources
  (an 80% revenue-share claim appears in third-party listings; an independent
  2026 review says no creator monetization — Unresolved, verify terms directly).
- Contents inspected: seosiri analysis; mcpfind comparison (CLI + hosted
  endpoints, 4.79/5 user reviews); assurly/agora submission docs
  (GitHub-connect deploy flow, smithery.yaml).
- Actual capabilities: Browse/install (read-only directory); hosted deployment
  (runs servers remotely on user's behalf); "Toolbox" meta-MCP router
  (function not inspected in depth).
- Usage domain: Discovery, one-click install, hosted MCP.
- Integration method: Web UI; CLI (`@smithery/cli`); hosted endpoints.
- Compatibility: MCP clients.
- Dependencies: GitHub account for publishing; API usage for hosted.
- Authentication: GitHub sign-in for deploy; hosted usage metering.
- Availability: Freemium.
- Maintenance: Active.
- License: Not open source.
- Security: Hosted servers execute in Smithery's infrastructure — trust boundary
  includes the platform; review server code before deploying.
- Limitations: Smaller catalog than Glama/mcp.so; monetization terms disputed.
- Related resources: Glama (Record 28), fastmcp-remote (Record 71).
- Sources: https://www.seosiri.com/2026/09/mcp-monetization-gap-glama-smithery-developer-losses.html ; https://github.com/mcpfind/mcp-find/blob/HEAD/apps/web/content/blog/mcp-server-directories-compared.mdx ; https://github.com/assurly/assurly/blob/HEAD/docs/mcp-directory-submissions.md ; https://github.com/evoxmusic/awesome-mcp-servers/blob/HEAD/details/memory-mcp-server.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 30 — PulseMCP (pulsemcp.com)

- Resource name: PulseMCP
- Canonical identity: https://www.pulsemcp.com ; https://mcpcentral.io (API)
- Category: A — MCP server registries/directories
- Type: Discovery/news-focused index; official-registry backer
- Official URL: https://www.pulsemcp.com
- Description: Discovery- and news-focused MCP index, noted for launch-day
  visibility. One of the backers of the official MCP Registry (alongside
  Anthropic, GitHub, Microsoft). MCP Central API (`mcpcentral.io/api/servers`)
  browses servers sorted by stars with enrichment data.
- Contents inspected: seosiri analysis (role description); openclaw
  mcp-registry SKILL.md (MCP Central API endpoint); assurly docs (submit form).
- Actual capabilities: Browse/search (read-only); API for enrichment data.
- Usage domain: Discovery, launch visibility, registry enrichment.
- Integration method: Web UI; REST API.
- Compatibility: Not applicable.
- Dependencies: None.
- Authentication: None for reads (per skill doc).
- Availability: Free (presumed).
- Maintenance: Active (presumed).
- License: Not verified.
- Security: Index only — listings unverified.
- Limitations: Not a hosting/billing platform.
- Related resources: MCP Registry (Record 25), MCPFind (Record 31).
- Sources: https://www.seosiri.com/2026/09/mcp-monetization-gap-glama-smithery-developer-losses.html ; https://github.com/assurly/assurly/blob/HEAD/docs/mcp-directory-submissions.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 31 — MCPFind (mcpfind)

- Resource name: MCPFind
- Canonical identity: https://github.com/mcpfind/mcp-find
- Category: A — MCP server registries/directories
- Type: Open-source directory with live-link pruning and per-client install guides
- Official URL: https://github.com/mcpfind/mcp-find
- Description: Open-source directory (~13.9K servers) with 95 setup guides,
  5-client copy-paste configs, and live link pruning (reduces dead links). Also
  publishes a directory-comparison blog post used as a secondary source.
- Contents inspected: mcpfind directory comparison (own listing + methodology).
- Actual capabilities: Browse/search (read-only); install configs.
- Usage domain: Discovery with verified-live listings.
- Integration method: Web UI.
- Compatibility: 5 MCP clients (copy-paste configs).
- Dependencies: None.
- Authentication: Not documented.
- Availability: Open source.
- Maintenance: Active (updated ~16 days before 2026-10-10 per crawl).
- License: Open source (stated in comparison table).
- Security: Live-link pruning improves freshness; code still third-party.
- Limitations: Smaller than Glama/mcp.so.
- Related resources: mcp.so (Record 26), protodex (Record 34).
- Sources: https://github.com/mcpfind/mcp-find/blob/HEAD/apps/web/content/blog/mcp-server-directories-compared.mdx
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 32 — mcpservers.org, MCP Surge, claudemcp.com, cursor.directory, VS Code directory, Docker MCP Catalog

- Resource name: Secondary directories (combined record)
- Canonical identity: mcpservers.org; MCP Surge; https://www.claudemcp.com/servers;
  https://cursor.directory/mcp; https://code.visualstudio.com/mcp;
  Docker MCP Catalog (security-scanned containerized distribution)
- Category: A — MCP server registries/directories
- Type: Curated/community directories; Docker's is containerized distribution
- Official URL: As listed above
- Description: mcpservers.org — curated directory (~9.4K servers, some sponsored
  listings). MCP Surge — ~12.7K servers, 42+ category tags. claudemcp.com —
  Claude-curated list. cursor.directory/mcp — Cursor-curated directory.
  code.visualstudio.com/mcp — official VS Code MCP directory. Docker MCP
  Catalog — containerized, security-scanned server distribution bundled into
  Docker's platform pricing.
- Contents inspected: mcpfind comparison table; artificial-intelligence-universe
  list; seosiri analysis (Docker catalog row). No directory homepage opened.
- Actual capabilities: Browse/search (read-only); Docker's adds scanned
  container distribution.
- Usage domain: Discovery (Docker: trusted distribution).
- Integration method: Web UI; Docker containers.
- Compatibility: MCP clients; Docker runtime for catalog.
- Dependencies: None (Docker: Docker platform).
- Authentication: Not documented.
- Availability: Free browsing; Docker bundled in platform pricing.
- Maintenance: Presumed active.
- License: Not open source (per comparison).
- Security: Docker's security scanning is a differentiator; others are
  unverified listings.
- Limitations: Combined record; per-directory details not inspected.
- Related resources: MCP Registry (Record 25).
- Sources: https://github.com/mcpfind/mcp-find/blob/HEAD/apps/web/content/blog/mcp-server-directories-compared.mdx ; https://www.seosiri.com/2026/09/mcp-monetization-gap-glama-smithery-developer-losses.html ; https://github.com/internetcityhd/artificial-intelligence-universe
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 33 — MCP Harbor (ai.mcpharbor.dev) / luciferforge-mcp-directory (protodex.io) / nandanhegde1/mcp-directory

- Resource name: Registry mirrors and GitHub-scraper directories (combined record)
- Canonical identity: https://ai.mcpharbor.dev (MCP Harbor); https://github.com/LuciferForge/mcp-directory
  (browse at http://protodex.io); https://github.com/nandanhegde1/mcp-directory
- Category: A — MCP server registries/directories
- Type: Discoverability layers / scraper-built indexes
- Official URL: As above
- Description: MCP Harbor — discoverability layer on top of the official MCP
  Registry (re-syncs every 6 hours; includes every official listing, origin-tagged),
  with browse UI, MCP endpoint for agents, and HTTP API (`/api/v0/servers` with
  q/transport/tag/limit/offset). luciferforge/mcp-directory — GitHub-scraper
  index of 18,146 servers, 13 auto-categories, weekly scraper, static site at
  protodex.io, ranked by stars. nandanhegde1/mcp-directory — free static
  SEO-first directory (~1.8–2.1K metadata-verified servers), weekly GitHub
  Actions cron, MIT licensed, Cloudflare Workers hosted.
- Contents inspected: lbesecker195/mcp_registry README (Harbor API, sync claims);
  luciferforge/mcp-directory README (scraper queries, categories, data files);
  nandanhegde1/mcp-directory README (stack, cadence, license).
- Actual capabilities: Browse/search (read-only).
- Usage domain: Discovery; Harbor also serves agents via MCP.
- Integration method: Web UI; REST APIs.
- Compatibility: Not applicable.
- Dependencies: None.
- Authentication: None for reads.
- Availability: Free; open source (both scraper repos).
- Maintenance: Active (all updated within ~1 month of 2026-10-10).
- License: nandanhegde1 — MIT; others not verified.
- Security: Scraper indexes include anything matching heuristics (e.g. n8n,
  gemini-cli counted as "servers") — noisy; audit before use.
- Limitations: Scraper precision is heuristic; Harbor's sync claims are its own.
- Related resources: MCP Registry (Record 25).
- Sources: https://github.com/lbesecker195/mcp_registry ; https://github.com/luciferforge/mcp-directory/blob/HEAD/README.md ; https://github.com/nandanhegde1/mcp-directory
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 34 — awesome-mcp-servers lists (punkpeye, evoxmusic, rohianon, epicmotionsd)

- Resource name: awesome-mcp-servers curated lists
- Canonical identity: https://github.com/punkpeye/awesome-mcp-servers (canonical,
  referenced ~700–1K servers, ~90K list stars); forks/variants by evoxmusic,
  rohianon, epicmotionsd, dark-moon-x
- Category: A — MCP server registries/directories
- Type: Curated awesome-lists (GitHub)
- Official URL: https://github.com/punkpeye/awesome-mcp-servers
- Description: The reference community awesome-list for MCP servers
  (700–1,000 entries, ~89.9K stars per comparison). Variants add detail pages
  (evoxmusic/details/*), categorized tables (rohianon database servers,
  epicmotionsd data/databases/cloud lists), and debugging-tool tables
  (dark-moon-x).
- Contents inspected: mcpfind comparison (counts); rohianon/epicmotionsd README
  database sections; dark-moon-x debugging & testing tools table;
  evoxmusic/details/memory-mcp-server.md (basic-memory profile).
- Actual capabilities: Curated links (read-only).
- Usage domain: Discovery, ecosystem orientation.
- Integration method: GitHub browsing; PRs to add.
- Compatibility: Not applicable.
- Dependencies: None.
- Authentication: None.
- Availability: Open source lists.
- Maintenance: Community; punkpeye canonical list not directly opened (crawled 8 days prior).
- License: Varies/not verified.
- Security: Curated but not security-audited.
- Limitations: punkpeye list itself not opened; counts from secondary comparison.
- Related resources: All directories above.
- Sources: https://github.com/mcpfind/mcp-find/blob/HEAD/apps/web/content/blog/mcp-server-directories-compared.mdx ; https://github.com/rohianon/awesome-mcp-servers/blob/HEAD/README.md ; https://github.com/epicmotionsd/awesome-mcp/blob/HEAD/README.md ; https://github.com/dark-moon-x/dm-ethanyolo01-awesome-mcp
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

---

## SECTION 6 — FUNCTIONAL CATEGORIES: COMMUNITY MCP SERVERS

### 6.1 Browsing / searching the internet, documentation retrieval, website inspection

### Record 35 — Tavily MCP Server (official, tavily-ai/tavily-mcp)

- Resource name: Tavily MCP Server
- Canonical identity: `tavily-ai/tavily-mcp` (GitHub); npm `tavily-mcp`; hosted `https://mcp.tavily.com/mcp/`
- Category: B — browsing/searching the internet
- Type: Vendor MCP server
- Official URL: https://github.com/tavily-ai/tavily-mcp (named in catalogs; repo page not opened)
- Description: Official MCP server for Tavily's AI-optimized search API —
  web search with citation-ready results plus extraction/crawl endpoints.
  Hosted endpoint takes the key as a query parameter
  (`?tavilyApiKey=…`). Community alternatives: Tomatio13/mcp-server-tavily, kshern/mcp-tavily.
- Contents inspected: deep-research-skill comparison matrix (official MCP,
  npm package, free tier); swarms FREE_MCP_SERVERS.md (hosted endpoint format);
  agentic-orchestration catalog (tavily-ai/tavily-mcp + community forks);
  mcp-server-meta-search tool table (`search_tavily`, `crawl_tavily`, `check_tavily_usage`).
- Actual capabilities: READ-ONLY — web search, crawl/extract, usage queries.
- Usage domain: Research, citations, RAG pipelines.
- Integration method: Hosted Streamable HTTP or npm stdio.
- Compatibility: MCP clients.
- Dependencies: Tavily API key (free tier available).
- Authentication: API key (query param on hosted).
- Availability: Free tier + paid; rate limits apply.
- Maintenance: Active (Tavily) — presumed.
- License: Not verified.
- Security: API key handling; returned content is untrusted input.
- Limitations: Repo not opened; tool list from secondary sources.
- Related resources: Exa (Record 36), Brave (Record 14), Firecrawl (Record 37).
- Sources: https://github.com/muhsinunc/deep-research-skill/blob/HEAD/notes/research/04-thirdparty-tools.md ; https://github.com/dbosmrt/swarms/blob/HEAD/examples/mcp/agents/FREE_MCP_SERVERS.md ; https://github.com/zlatko-lakisic/agentic-orchestration/blob/HEAD/docs/mcp-catalog/index.md ; https://github.com/dylckh/mcp-server-meta-search
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 36 — Exa MCP Server (official, exa-labs/exa-mcp-server)

- Resource name: Exa MCP Server
- Canonical identity: `exa-labs/exa-mcp-server` (GitHub); npm `exa-mcp-server`; hosted `https://mcp.exa.ai/mcp`
- Category: B — browsing/searching the internet
- Type: Vendor MCP server
- Official URL: https://github.com/exa-labs/exa-mcp-server (named; not opened)
- Description: Official MCP server for Exa's neural/semantic search — AI-native
  search with neural, keyword, and hybrid modes plus content retrieval. Hosted
  endpoint: `https://mcp.exa.ai/mcp?exaApiKey=…`.
- Contents inspected: deep-research-skill matrix (official, npm, free tier);
  swarms doc (hosted endpoint); agentic-orchestration catalog (npm + hosted).
- Actual capabilities: READ-ONLY — semantic web search, content retrieval.
- Usage domain: Deep research, semantic search.
- Integration method: Hosted Streamable HTTP or npm stdio.
- Compatibility: MCP clients.
- Dependencies: Exa API key (free tier).
- Authentication: API key (query param on hosted).
- Availability: Free tier + paid.
- Maintenance: Active (Exa) — presumed.
- License: Not verified.
- Security: As Record 35.
- Limitations: Repo not opened.
- Related resources: Tavily (Record 35), mcp-server-meta-search (Record 39).
- Sources: https://github.com/muhsinunc/deep-research-skill/blob/HEAD/notes/research/04-thirdparty-tools.md ; https://github.com/dbosmrt/swarms/blob/HEAD/examples/mcp/agents/FREE_MCP_SERVERS.md ; https://github.com/zlatko-lakisic/agentic-orchestration/blob/HEAD/docs/mcp-catalog/index.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 37 — Firecrawl MCP Server (official, mendableai/firecrawl)

- Resource name: Firecrawl MCP Server
- Canonical identity: `@firecrawl/mcp-server` (npm); repo mendableai/firecrawl; docs https://docs.firecrawl.dev/mcp
- Category: B — browsing/searching, website inspection, data processing
- Type: Vendor MCP server
- Official URL: https://docs.firecrawl.dev/mcp
- Description: Official Firecrawl MCP: web scraping that transforms sites into
  clean markdown — full-site crawling, JavaScript rendering, structured data
  extraction, batch processing. (`FIRECRAWL_API_KEY`.)
- Contents inspected: agent-sensory-tools web-data README (feature list,
  install config); deep-research-skill scraping comparison (fastest avg 7s,
  free tier); swarms doc (hosted + key).
- Actual capabilities: READ-ONLY — scrape/crawl/extract (JS-rendered).
- Usage domain: Web-to-markdown, RAG ingestion, site extraction.
- Integration method: stdio (`npx -y @firecrawl/mcp-server`) or hosted.
- Compatibility: MCP clients.
- Dependencies: Firecrawl API key (free tier available).
- Authentication: API key.
- Availability: Free tier + paid; rate limits/retries built in.
- Maintenance: Active (Firecrawl; ~85K stars cited for the repo — secondary claim).
- License: Not verified.
- Security: Scraped content is untrusted input; anti-bot bypass is basic
  (per comparison) — coverage limits on hard targets.
- Limitations: Repo README not opened; details from secondary docs.
- Related resources: Fetch (Record 7), Browserbase (Record 22).
- Sources: https://github.com/dennis1874/agent-sensory-tools/blob/HEAD/categories/web-data/README.md ; https://github.com/muhsinunc/deep-research-skill/blob/HEAD/notes/research/04-thirdparty-tools.md ; https://github.com/dbosmrt/swarms/blob/HEAD/examples/mcp/agents/FREE_MCP_SERVERS.md ; https://github.com/vortex-dev00/god-repo/blob/HEAD/developers/mcp-ecosystem/README.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 38 — mcp-omnisearch (community unified search)

- Resource name: mcp-omnisearch
- Canonical identity: `vite-plus-ecosystem-ci/mcp-omnisearch` (GitHub)
- Category: B — browsing/searching the internet
- Type: Community MCP server (TypeScript)
- Official URL: https://github.com/vite-plus-ecosystem-ci/mcp-omnisearch
- Description: Unified MCP server over Tavily, Brave, Kagi, Exa, GitHub,
  Linkup, and Firecrawl through four consolidated tools: `web_search`,
  `ai_search` (+ two more per README). Providers without API keys are skipped.
- Contents inspected: Repo README (search-result text): tool list, config with
  seven provider env keys, Glama badge, vitest-tested.
- Actual capabilities: READ-ONLY — unified web/AI search and content extraction.
- Usage domain: Research agents needing multi-provider search behind one interface.
- Integration method: stdio (`node ./dist/index.js` after build).
- Compatibility: MCP clients.
- Dependencies: Node/pnpm; any subset of provider API keys
  (TAVILY_API_KEY, KAGI_API_KEY, BRAVE_API_KEY, GITHUB_API_KEY, EXA_API_KEY,
  LINKUP_API_KEY, FIRECRAWL_API_KEY).
- Authentication: Per-provider API keys.
- Availability: Open source; last updated ~65 days before 2026-10-10.
- Maintenance: Community (vite-plus-ecosystem-ci).
- License: Not verified.
- Security: Aggregates seven API keys in one process — key sprawl; outputs are
  untrusted web content.
- Limitations: README not fully opened; remaining two tools not enumerated.
- Related resources: mcp-server-meta-search (Record 39).
- Sources: https://github.com/vite-plus-ecosystem-ci/mcp-omnisearch
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 39 — mcp-server-meta-search (community)

- Resource name: mcp-server-meta-search
- Canonical identity: `dylckh/mcp-server-meta-search` (GitHub)
- Category: B — browsing/searching the internet
- Type: Community MCP server
- Official URL: https://github.com/dylckh/mcp-server-meta-search
- Description: Meta-search MCP combining Exa, Tavily, Perplexity, Jina Reader,
  and Cloudflare Browser Rendering fallback. Tools: `search_tavily`,
  `crawl_tavily`, `check_tavily_usage`, `search_exa`, `search_perplexity`,
  `fetch_jina_markdown`, `fetch_as_markdown`. Streamable HTTP endpoint `/mcp`
  with PAT auth; also health (`/healthz`), readiness (`/readyz`), and
  Prometheus metrics (`/metrics`) endpoints.
- Contents inspected: Repo README (search-result text): tool table, endpoint table.
- Actual capabilities: READ-ONLY — search, crawl, fetch-as-markdown.
- Usage domain: Research agents.
- Integration method: Streamable HTTP with Bearer <redacted>
- Compatibility: MCP clients supporting Streamable HTTP.
- Dependencies: Provider API keys.
- Authentication: PAT (Bearer).
- Availability: Open source; last updated ~152 days before 2026-10-10.
- Maintenance: Community (dylckh).
- License: Not verified.
- Security: Untrusted web content; PAT protects the endpoint.
- Limitations: README not fully opened.
- Related resources: mcp-omnisearch (Record 38).
- Sources: https://github.com/dylckh/mcp-server-meta-search
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### 6.2 Browser automation / website inspection (community + vendor)

Browser automation servers: Browserbase (Record 22), Cloudflare Browser
Rendering (Record 21), microsoft/playwright-mcp (dedup xref — official OpenCode
install guide exists), michaljach/opencode-browser / browsermcp.io (dedup xref),
archived Puppeteer reference (Historical). No new in-depth records warranted.

### 6.3 GitHub operations / codebase search / terminal operations

GitHub: github/github-mcp-server (dedup xref, Record 24). Local git: reference
Git server (Record 9). Terminal: GongRzhe/terminal-controller-mcp is named in
the god-repo ecosystem list as "Terminal Controller MCP" — entry-level mention
only (Not verified; Unresolved). Codebase search beyond dedup items: no
primary-source-verified standalone server found in this workstream — gap noted
in Coverage.

### 6.4 Databases

### Record 40 — qore-mcp (QoreDB read-only MCP server)

- Resource name: qore-mcp
- Canonical identity: `qoredb/qoredb` repo, crate `qore-mcp` (Rust)
- Category: B — databases
- Type: Community MCP server (Rust; companion to QoreDB desktop app)
- Official URL: https://github.com/qoredb/qoredb/blob/HEAD/src-tauri/crates/qore-mcp/README.md
- Description: Read-only MCP server for QoreDB. Lets an agent discover and query
  database connections saved in the QoreDB desktop app, reusing the same engine
  and safety gates — mutations blocked. Drivers selectable at build time:
  postgres, cockroachdb, motherduck, neon, supabase, timescaledb, mysql,
  mariadb, sqlite, mongodb, redis, sqlserver, clickhouse, elasticsearch,
  opensearch, duckdb.
- Contents inspected: qore-mcp README (full): tools table, build commands,
  config-dir behavior.
- Actual capabilities: READ-ONLY — `list_connections`, `list_namespaces`,
  `list_tables`, `describe_table`, `run_query`. Every session opened with
  `read_only = true`; preflight/execute gates reject mutations.
- Usage domain: Database exploration for agents.
- Integration method: stdio (binary; `claude mcp add qoredb -- /path/qore-mcp`).
- Compatibility: MCP clients.
- Dependencies: QoreDB desktop app config + OS keyring (credentials reused;
  `QOREDB_CONFIG_DIR` override).
- Authentication: Reuses desktop app's saved connections (OS keyring).
- Availability: Open source; updated ~22 days before 2026-10-10.
- Maintenance: Active (qoredb).
- License: Apache-2.0 (SPDX header in README).
- Security: Read-only by construction — strong safety posture; credentials live
  in OS keyring, not config files.
- Limitations: Read-only only (no migrations/writes); requires QoreDB desktop setup.
- Related resources: db_mcp_gateway (Record 41), mcp-alchemy (Record 43).
- Sources: https://github.com/qoredb/qoredb/blob/HEAD/src-tauri/crates/qore-mcp/README.md
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 41 — db_mcp_gateway (multi-database gateway)

- Resource name: db_mcp_gateway
- Canonical identity: `muhammedehab35/db_mcp_gateway` (GitHub)
- Category: B — databases
- Type: Community MCP gateway (Python, presumed)
- Official URL: https://github.com/muhammedehab35/db_mcp_gateway/blob/HEAD/README.md
- Description: Gateway exposing multiple databases through one MCP server:
  PostgreSQL (`@modelcontextprotocol/server-postgres`), MongoDB
  (`@executeautomation/mongodb-mcp-server`), MySQL (`@benborla29/mcp-server-mysql`),
  Redis (`@modelcontextprotocol/server-redis`), SQLite
  (`@modelcontextprotocol/server-sqlite`), Supabase (`@supabase/mcp`).
  Tools: `connect_database`, `execute_query`, `list_databases` (per examples).
  Configured via `config/databases.json` with per-database credentials.
- Contents inspected: README (search-result text): examples, supported-database
  table, config schema.
- Actual capabilities: READ + WRITE — `execute_query` runs arbitrary queries;
  write-capable by design.
- Usage domain: Multi-database agent access.
- Integration method: MCP server (transport not verified).
- Compatibility: MCP clients (presumed).
- Dependencies: Database credentials in config/databases.json.
- Authentication: Per-database credentials (config file).
- Availability: Open source; last updated ~270 days before 2026-10-10 (stale).
- Maintenance: Community; appears low-activity.
- License: Not verified.
- Security: Credentials in a JSON config file; arbitrary query execution —
  high blast radius; references archived reference packages
  (`@modelcontextprotocol/server-postgres` etc.) — Historical dependency risk.
- Limitations: Package references point at archived reference servers; freshness
  is a concern.
- Related resources: unified-db-mcp-server (Record 42).
- Sources: https://github.com/muhammedehab35/db_mcp_gateway/blob/HEAD/README.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 42 — unified-db-mcp-server (cross-database schema migration)

- Resource name: unified-db-mcp-server
- Canonical identity: `flotorch/unified-db-mcp-server` (GitHub)
- Category: B — databases, backend schemas
- Type: Community MCP service (Python)
- Official URL: https://github.com/flotorch/unified-db-mcp-server
- Description: Production-focused service for cross-database schema extraction
  and migration (Supabase, PostgreSQL, MySQL, MariaDB, SQLite, MongoDB,
  SQL Server, Cassandra). Exposes MCP tools over a single Streamable HTTP
  endpoint (`/unified-db/mcp`) plus a simple REST endpoint. Dockerized with
  healthcheck; dry-run and table-filtered migrations.
- Contents inspected: Repo README (search-result text): supported DBs, features,
  project structure.
- Actual capabilities: READ + WRITE — schema extraction (read) and schema
  migration (write/DDL) with dry-run option.
- Usage domain: Schema migration, cross-DB introspection.
- Integration method: Streamable HTTP (`/unified-db/mcp`); header-based credentials.
- Compatibility: MCP clients; Docker.
- Dependencies: Database credentials (headers); Docker.
- Authentication: Header-based credentials.
- Availability: Open source; last updated ~191 days before 2026-10-10.
- Maintenance: Community (flotorch).
- License: Not verified.
- Security: DDL-capable migrations — dry-run first; credential handling via headers.
- Limitations: README not fully opened; exact tool names not enumerated.
- Related resources: qore-mcp (Record 40).
- Sources: https://github.com/flotorch/unified-db-mcp-server
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 43 — mcp-alchemy (multi-DB SQLAlchemy server)

- Resource name: mcp-alchemy
- Canonical identity: `runekaagaard/mcp-alchemy` (GitHub)
- Category: B — databases
- Type: Community MCP server (Python/SQLAlchemy)
- Official URL: https://github.com/runekaagaard/mcp-alchemy (named in ecosystem list; not opened)
- Description: Multi-database MCP server (SQLite, PostgreSQL, MySQL, MariaDB,
  Oracle, MS-SQL) built on SQLAlchemy.
- Contents inspected: god-repo ecosystem list only.
- Actual capabilities: READ + WRITE (presumed) — not verified.
- Usage domain: SQL database access.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: SQLAlchemy + DB drivers (presumed).
- Authentication: Connection strings (presumed).
- Availability: Open source (presumed).
- Maintenance: Not verified.
- License: Not verified.
- Security: Not publicly documented.
- Limitations: Entry-level record.
- Related resources: qore-mcp (Record 40).
- Sources: https://github.com/vortex-dev00/god-repo/blob/HEAD/developers/mcp-ecosystem/README.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 44 — MongoDB official MCP Server

- Resource name: MongoDB MCP Server (official)
- Canonical identity: MongoDB-maintained (exact repo not verified; community
  forks include kiliczsh/mcp-mongo-server, executeautomation packages)
- Category: B — databases
- Type: Vendor MCP server
- Official URL: Not verified (no primary URL opened)
- Description: MongoDB's official MCP server: connect to MongoDB databases and
  Atlas clusters for querying, aggregation, and collection management (~40+
  tools per ecosystem list). Env: `MDB_MCP_CONNECTION_STRING`.
- Contents inspected: psabhinav/claude-plugins database pack table; god-repo
  ecosystem list (40+ tools claim).
- Actual capabilities: READ + WRITE — querying, aggregation, collection
  management (per secondary sources).
- Usage domain: MongoDB/Atlas operations.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: MongoDB connection string.
- Authentication: Connection string.
- Availability: Not verified.
- Maintenance: Presumed active (MongoDB).
- License: Not verified.
- Security: Write-capable; connection string is a full credential.
- Limitations: Official repo URL and tool list not verified from primary source.
- Related resources: qore-mcp (Record 40).
- Sources: https://github.com/psabhinav/claude-plugins/blob/HEAD/plugins/mcps-database/README.md ; https://github.com/vortex-dev00/god-repo/blob/HEAD/developers/mcp-ecosystem/README.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 45 — Supabase MCP (`@supabase/mcp` / supabase-community/supabase-mcp)

- Resource name: Supabase MCP
- Canonical identity: `@supabase/mcp` (npm); `supabase-community/supabase-mcp` (GitHub)
- Category: B — databases, backend schemas
- Type: Community/vendor-adjacent MCP server
- Official URL: https://github.com/supabase-community/supabase-mcp (named; not opened)
- Description: MCP server for Supabase — database, auth, storage, and edge
  functions (per awesome lists). Env: `SUPABASE_ACCESS_TOKEN`.
- Contents inspected: rohianon/epicmotionsd awesome lists; psabhinav database
  pack table; db_mcp_gateway supported-DB table.
- Actual capabilities: READ + WRITE (database/auth/storage/edge functions) — presumed.
- Usage domain: Supabase backend operations.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: Supabase access token.
- Authentication: Access token.
- Availability: Not verified.
- Maintenance: Not verified.
- License: Not verified.
- Security: Access token scopes determine blast radius (general, not source-verified).
- Limitations: Entry-level record; official vs community status ambiguous
  (supabase-community org).
- Related resources: Neon MCP (Record 46).
- Sources: https://github.com/rohianon/awesome-mcp-servers/blob/HEAD/README.md ; https://github.com/psabhinav/claude-plugins/blob/HEAD/plugins/mcps-database/README.md ; https://github.com/muhammedehab35/db_mcp_gateway/blob/HEAD/README.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 46 — Neon MCP (neondatabase/mcp-server-neon) + Postgres MCP Pro

- Resource name: Neon MCP Server; Postgres MCP Pro (community)
- Canonical identity: `neondatabase/mcp-server-neon` (GitHub)
- Category: B — databases
- Type: Vendor (Neon) + community MCP servers
- Official URL: https://github.com/neondatabase/mcp-server-neon (named; not opened)
- Description: Neon's MCP server for interacting with the Neon Management API
  and databases (branches, queries, management). Separately, "Postgres MCP Pro"
  is a community server (~2.3K stars cited) focused on industrial-strength
  index tuning.
- Contents inspected: psabhinav database pack; rohianon/epicmotionsd lists;
  god-repo list (star claim for Postgres MCP Pro).
- Actual capabilities: READ + WRITE (branch management, queries) — presumed.
- Usage domain: Serverless Postgres operations.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: Neon API key (presumed).
- Authentication: Not verified.
- Availability: Not verified.
- Maintenance: Not verified.
- License: Not verified.
- Security: Branch management is write-capable — scope keys carefully
  (general, not source-verified).
- Limitations: Entry-level record.
- Related resources: Supabase MCP (Record 45).
- Sources: https://github.com/psabhinav/claude-plugins/blob/HEAD/plugins/mcps-database/README.md ; https://github.com/rohianon/awesome-mcp-servers/blob/HEAD/README.md ; https://github.com/vortex-dev00/god-repo/blob/HEAD/developers/mcp-ecosystem/README.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 47 — ClickHouse (ClickHouse/mcp-clickhouse) + MotherDuck (motherduckdb/mcp-server-motherduck)

- Resource name: ClickHouse MCP; MotherDuck/DuckDB MCP
- Canonical identity: `ClickHouse/mcp-clickhouse`; `motherduckdb/mcp-server-motherduck`
- Category: B — databases, data processing
- Type: Vendor MCP servers
- Official URL: https://github.com/ClickHouse/mcp-clickhouse ; https://github.com/motherduckdb/mcp-server-motherduck (named; not opened)
- Description: Vendor MCP servers for ClickHouse analytical queries and
  DuckDB/MotherDuck queries.
- Contents inspected: rohianon awesome list only.
- Actual capabilities: READ (analytical queries) — presumed.
- Usage domain: Analytics, data engineering.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: Database credentials (presumed).
- Authentication: Not verified.
- Availability: Not verified.
- Maintenance: Presumed active (vendors).
- License: Not verified.
- Security: Not publicly documented.
- Limitations: Entry-level record.
- Related resources: qore-mcp (Record 40).
- Sources: https://github.com/rohianon/awesome-mcp-servers/blob/HEAD/README.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### 6.5 Cloud infrastructure and deployment

AWS: awslabs/mcp (Record 16). Railway MCP (railway-app/railway-mcp) named in
epicmotionsd list (entry-level, Not verified). Home Assistant official MCP
(home-assistant.io/integrations/mcp_server, Streamable HTTP /api/mcp, Bearer)
named in agentic-orchestration catalog (entry-level, Partially verified).

### Record 48 — mcp-kubernetes (Flux159)

- Resource name: mcp-kubernetes
- Canonical identity: `Flux159/mcp-kubernetes` (GitHub)
- Category: B — cloud infrastructure, deployment
- Type: Community MCP server
- Official URL: https://github.com/Flux159/mcp-kubernetes (named; not opened)
- Description: MCP server for Kubernetes cluster management.
- Contents inspected: epicmotionsd awesome list; alkofu/ai-tpk commit
  (kubernetes npx invocation referenced in installer).
- Actual capabilities: READ + WRITE (cluster management) — presumed.
- Usage domain: Kubernetes operations.
- Integration method: npx stdio (per installer reference).
- Compatibility: MCP clients.
- Dependencies: kubeconfig credentials (presumed).
- Authentication: Kubernetes credentials (presumed).
- Availability: Open source.
- Maintenance: Not verified.
- License: Not verified.
- Security: Cluster-admin-equivalent access possible — high blast radius
  (general, not source-verified).
- Limitations: Entry-level record.
- Related resources: docker-mcp-server (Record 49).
- Sources: https://github.com/epicmotionsd/awesome-mcp/blob/HEAD/README.md ; https://github.com/alkofu/ai-tpk/commit/18bd0f4e166729c481a74bc344429c322979cb01
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 49 — docker-mcp-server (QuantGeekDev)

- Resource name: docker-mcp-server
- Canonical identity: `QuantGeekDev/docker-mcp-server` (GitHub)
- Category: B — cloud infrastructure, deployment
- Type: Community MCP server
- Official URL: https://github.com/QuantGeekDev/docker-mcp-server (named; not opened)
- Description: MCP server for Docker container management.
- Contents inspected: epicmotionsd awesome list only.
- Actual capabilities: READ + WRITE/EXECUTE (container management implies
  exec) — presumed, not verified.
- Usage domain: Container operations.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: Docker socket access (presumed).
- Authentication: Docker daemon access (presumed).
- Availability: Open source.
- Maintenance: Not verified.
- License: Not verified.
- Security: Docker socket access is effectively host-root-equivalent —
  treat as maximum-risk (general, not source-verified for this server).
- Limitations: Entry-level record.
- Related resources: mcp-kubernetes (Record 48).
- Sources: https://github.com/epicmotionsd/awesome-mcp/blob/HEAD/README.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### 6.6 Memory / retrieval

Reference: Memory (Record 10).

### Record 50 — Basic Memory (basicmachines-co/basic-memory)

- Resource name: Basic Memory
- Canonical identity: `basicmachines-co/basic-memory` (GitHub); PyPI `basic-memory`
- Category: B — memory/retrieval
- Type: Community MCP server (Python) + CLI + optional cloud
- Official URL: https://github.com/basicmachines-co/basic-memory (named; repo page not opened)
- Description: Local-first persistent memory: saves conversations/notes as
  Markdown files (default `~/basic-memory`), building a searchable semantic
  knowledge graph agents read and write via MCP tools. Install via
  `uv tool install basic-memory`; run MCP server with `uvx basic-memory mcp`;
  CLI with `sync` / `sync --watch`; optional paid Basic Memory Cloud add-on.
  Claude Desktop / VS Code / Cursor / Claude Code setups documented; Smithery
  install supported.
- Contents inspected: evoxmusic awesome-mcp-servers details page (features,
  install, usage patterns, sync); mnemoverse/awesome-agent-memory (AGPL-3.0,
  Obsidian-compatible markdown note).
- Actual capabilities: READ + WRITE — knowledge-base CRUD + semantic search via
  MCP tools; CLI sync.
- Usage domain: Personal persistent memory, knowledge management.
- Integration method: stdio (`uvx basic-memory mcp`).
- Compatibility: Claude Desktop, VS Code, Cursor, Claude Code, any MCP client.
- Dependencies: Python/uv; local Markdown store.
- Authentication: None local; cloud add-on requires subscription.
- Availability: Open source (AGPL-3.0 per mnemoverse); cloud optional paid.
- Maintenance: Active (Basic Machines; ~80.9K PyPI downloads, ~2.2K stars per
  secondary source, Mar 2025 release).
- License: AGPL-3.0 (per mnemoverse/awesome-agent-memory — secondary).
- Security: Local-first; notes are plain Markdown on disk (no encryption noted).
- Limitations: Repo README not opened; exact tool list not enumerated.
- Related resources: Memory (Record 10), Mimir (Record 51), Servex (Record 52).
- Sources: https://github.com/evoxmusic/awesome-mcp-servers/blob/HEAD/details/memory-mcp-server.md ; https://github.com/mnemoverse/awesome-agent-memory
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 51 — Mimir (Perseus-Computing-LLC/mimir)

- Resource name: Mimir
- Canonical identity: `Perseus-Computing-LLC/mimir` (GitHub); `cargo install mimir-mcp`
- Category: B — memory/retrieval
- Type: Community MCP server (Rust, single static binary)
- Official URL: https://github.com/Perseus-Computing-LLC/mimir (named; not opened)
- Description: Local-first persistent memory server: 43 MCP tools, AES-256-GCM
  encryption at rest, Ebbinghaus decay scoring, FTS5 + dense-vector hybrid
  recall, bi-temporal entity history, Obsidian-compatible vault export, single
  binary on local SQLite, zero cloud dependencies.
- Contents inspected: ext-apps issue #692 showcase post (feature list, install).
- Actual capabilities: READ + WRITE — 43 tools for entity storage, relations,
  recall, export.
- Usage domain: Encrypted local agent memory.
- Integration method: stdio (single binary).
- Compatibility: Claude Desktop, Claude Code, Cursor, any MCP client.
- Dependencies: None (static binary).
- Authentication: Not documented.
- Availability: Open source (MIT per showcase post).
- Maintenance: Developer-alpha per related listing (mnemoverse calls
  "Hyperconsciousness" dev-alpha; Mimir status per showcase — treat as early).
- License: MIT (per showcase post).
- Security: AES-256-GCM at rest — strongest local-memory security posture found.
- Limitations: Showcase-post only; repo not opened.
- Related resources: Basic Memory (Record 50), Servex (Record 52).
- Sources: https://github.com/modelcontextprotocol/ext-apps/issues/692 ; https://github.com/mnemoverse/awesome-agent-memory
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 52 — Servex (teguhhardian12/servex)

- Resource name: Servex
- Canonical identity: `teguhhardian12/servex` (GitHub)
- Category: B — memory/retrieval
- Type: Community MCP server (Go, single binary)
- Official URL: https://github.com/teguhhardian12/servex
- Description: AI memory server: 12 MCP tools (memory CRUD + knowledge graph +
  stats), hybrid search (FTS5 BM25 + 256-dim TF-IDF + RRF fusion; three modes:
  hybrid/keyword/semantic), knowledge graph with JSON/Markdown export, SQLite
  WAL backend, zero model downloads, dual transport (stdio + HTTP+SSE),
  ~15MB static binary, fully offline.
- Contents inspected: Repo README (search-result text): features, architecture.
- Actual capabilities: READ + WRITE — memory CRUD, graph operations, export.
- Usage domain: Offline-capable agent memory.
- Integration method: stdio or HTTP+SSE.
- Compatibility: Claude Code, Cursor, Continue, any MCP client.
- Dependencies: None (static Go binary).
- Authentication: Not documented.
- Availability: Open source.
- Maintenance: Community.
- License: Not verified.
- Security: Fully offline — no network exfiltration surface; local SQLite.
- Limitations: README not fully opened; exact tool names not enumerated.
- Related resources: Mimir (Record 51), OpenMemory (Record 53).
- Sources: https://github.com/teguhhardian12/servex
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 53 — OpenMemory (mem0) / Mnemoverse / Firekeep / Memento / Hyperconsciousness / ReasonGraph (memory landscape)

- Resource name: Hosted & project memory servers (combined record)
- Canonical identity: OpenMemory (mem0 project); mnemoverse/awesome-agent-memory;
  Firekeep (BUSL-1.1); Memento (hosted); Hyperconsciousness (MIT, dev-alpha);
  ReasonGraph Cloud
- Category: B — memory/retrieval
- Type: Vendor/community MCP memory servers (local-first and hosted)
- Official URL: https://github.com/mnemoverse/awesome-agent-memory (landscape index)
- Description: OpenMemory — local-first private MCP memory server (Mem0
  project). Mnemoverse — hosted persistent memory with MIT local stdio server
  (API key) + remote HTTP endpoint (OAuth). Firekeep — BUSL-1.1 self-hosted MCP
  operating layer sharing durable knowledge, working state, coordination leases,
  replay evidence across Claude Code/Codex/Kiro/OpenCode. Memento — hosted MCP
  memory for coding agents (editable Markdown, team-shared, dashboard).
  Hyperconsciousness — MIT dev-alpha knowledge store, encrypted append-only
  records, MCP retrieval via scoped expiring grants. ReasonGraph Cloud — hosted
  graph memory over Streamable HTTP (API key); fact/connection/cause-effect tools.
- Contents inspected: mnemoverse/awesome-agent-memory MCP memory servers section.
- Actual capabilities: READ + WRITE (memory CRUD) — per listing.
- Usage domain: Agent persistent memory, team-shared context.
- Integration method: stdio (local) or Streamable HTTP (hosted).
- Compatibility: Varies by server.
- Dependencies: API keys for hosted offerings.
- Authentication: API key (hosted); OAuth (Mnemoverse remote).
- Availability: Mixed open-source/hosted.
- Maintenance: Varies; Firekeep is BUSL-1.1 (source-available, not OSI).
- License: Mixed (MIT / BUSL-1.1 / commercial).
- Security: Hosted memory = third-party data custody; scoped expiring grants
  (Hyperconsciousness) is the notable least-privilege pattern.
- Limitations: Combined record from a single landscape list; no primary repos opened.
- Related resources: Memory (Record 10), Basic Memory (Record 50).
- Sources: https://github.com/mnemoverse/awesome-agent-memory
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### 6.7 Testing, security (as MCP servers)

### Record 54 — Semgrep MCP Server (semgrep, hosted)

- Resource name: Semgrep MCP Server
- Canonical identity: `https://mcp.semgrep.ai/mcp`
- Category: B — testing, security
- Type: Vendor hosted MCP server
- Official URL: https://mcp.semgrep.ai/mcp (named; not opened)
- Description: Static-analysis security scanning exposed over MCP (was open,
  now requires Bearer <redacted> per swarms doc).
- Contents inspected: dbosmrt/swarms FREE_MCP_SERVERS.md (endpoint + auth note).
- Actual capabilities: READ-ONLY (scan analysis) — presumed.
- Usage domain: SAST for agents.
- Integration method: Streamable HTTP + Bearer.
- Compatibility: MCP clients.
- Dependencies: Semgrep API token.
- Authentication: Bearer <redacted>
- Availability: Hosted; free tier (per doc).
- Maintenance: Active (Semgrep) — presumed.
- License: Not verified.
- Security: Analysis results may include code findings — handle as sensitive.
- Limitations: Entry-level record.
- Related resources: Snyk Agent Scan (Record 59).
- Sources: https://github.com/dbosmrt/swarms/blob/HEAD/examples/mcp/agents/FREE_MCP_SERVERS.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 55 — Assurly (pre-deploy ship gate)

- Resource name: Assurly
- Canonical identity: `assurly/assurly` (GitHub)
- Category: B — testing, security, deployment
- Type: Community MCP server (pre-deploy gate)
- Official URL: https://github.com/assurly/assurly (named; not opened)
- Description: "A pre-deploy ship gate your AI agent calls before shipping —
  scans Next.js + Supabase + Stripe + Vercel for what will break in production."
- Contents inspected: assurly docs/mcp-directory-submissions.md (one-line pitch only).
- Actual capabilities: READ-ONLY (scan/analyze) — presumed.
- Usage domain: Pre-deploy checks for web apps.
- Integration method: Not verified.
- Compatibility: MCP clients (presumed).
- Dependencies: Not verified.
- Authentication: Not verified.
- Availability: Not verified.
- Maintenance: Not verified.
- License: Not verified.
- Security: Not publicly documented.
- Limitations: Single-pitch record; depth not established.
- Related resources: Semgrep MCP (Record 54).
- Sources: https://github.com/assurly/assurly/blob/HEAD/docs/mcp-directory-submissions.md
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### 6.8 External business services (community)

Official: Stripe (Record 15), Notion (Record 20), Google Workspace (Record 23).
Slack: archived reference Slack server now maintained by Zencoder (per servers
README) — Historical/Partially verified, repo not opened. Community: Linear
(jerhadf/linear-mcp-server), mcp-ticketer (bobmatnyc — Linear/GitHub/Jira/Asana),
Trello (delorenj/mcp-server-trello), Todoist (koki-develop/todoist-mcp-server;
official Doist todoist-ai at mcp/doist/todoist-ai), Discord/Telegram/Twilio —
all entry-level mentions from the god-repo ecosystem list (Not verified).
Linear also exposes an official remote endpoint `https://mcp.linear.app/mcp`
(per fastmcp-remote docs example) — Partially verified.

### 6.9 Public APIs, backend schemas, data processing, component registries

Public APIs: Ref Tools (ref.tools — fast documentation search, hosted + key;
dedup xref), Open-Meteo MCP (weather/air-quality/geocoding), arXiv/PubMed/
Wikipedia/DeepL servers — all entry-level mentions in openclaw/swarms docs
(Not verified). Backend schemas: unified-db-mcp-server (Record 42).
Data processing: pandas reference server noted as archived-adjacent in
epicmotionsd list (Historical — the archived list does not include pandas;
treat as Unresolved). Component registries: shadcn MCP (dedup xref).
No primary-source-verified standalone records established in this workstream
for 6.9 beyond cross-references — gap noted in Coverage.

---

## SECTION 7 — MCP DEVELOPMENT FRAMEWORKS, INSPECTION, SECURITY, OBSERVABILITY, CONFIGURATION

### Record 56 — FastMCP (jlowin/fastmcp, PrefectHQ)

- Resource name: FastMCP
- Canonical identity: `jlowin/fastmcp` (GitHub); maintained by PrefectHQ
- Category: A — MCP development frameworks
- Type: Python framework for MCP servers, clients, and apps
- Official URL: https://github.com/jlowin/fastmcp (named; repo page not opened — mirror README inspected)
- Description: The fast, Pythonic MCP framework. Created by Jeremiah Lowin;
  FastMCP 1.0 was adopted into the official Anthropic MCP Python SDK in 2024;
  standalone FastMCP (v3) is reported to power ~70% of MCP servers across all
  languages (project claim). Decorators turn Python functions into tools/
  resources/prompts/apps; JSON Schema auto-generated from type hints; transports
  stdio/Streamable HTTP/SSE; first-class OAuth/OIDC; server composition and
  proxying; OpenAPI/FastAPI import; CLI (`fastmcp run`, `fastmcp list`,
  `fastmcp call`, install into Claude Desktop/Claude Code/Cursor/ChatGPT/
  Gemini CLI/Goose); middleware; lifespan; elicitation; sampling; progress;
  OpenTelemetry; client library; apps runtime (interactive UIs in host conversations).
- Contents inspected: api-evangelist/fastmcp README mirror (full feature list,
  lineage, license, maintainer); lysandre001 skills-registry FastMCP CLI skill
  (`fastmcp list`/`call` usage); monoscope-tech opentelemetry-demo README
  (FastMCP server with OTLP export); vishalm/aethersearch README (FastMCP +
  FastAPI wrapper, bearer-auth MCP over HTTP).
- Actual capabilities: Framework — produces servers with any read/write/execute
  profile the author codes. CLI also acts as a universal MCP client for
  testing (`fastmcp list`/`call`).
- Usage domain: Building and testing MCP servers in Python.
- Integration method: `pip install fastmcp`; `fastmcp run server.py`.
- Compatibility: MCP spec; Python ≥ 3.10.
- Dependencies: Python ≥ 3.10.
- Authentication: OAuth/OIDC first-class; Bearer <redacted> HTTP patterns documented.
- Availability: Open source; active.
- Maintenance: PrefectHQ.
- License: Apache-2.0 (per mirror).
- Security: Framework inherits author-defined risk; OpenTelemetry export
  enables audit trails.
- Limitations: Repo page not opened; v3 feature claims from mirror.
- Related resources: Python SDK (Record 4), fastmcp-remote (Record 71).
- Sources: https://github.com/api-evangelist/fastmcp/blob/HEAD/README.md ; https://github.com/lysandre001/skills-registry/blob/HEAD/jlowin--fastmcp--fastmcp-client-cli/SKILL.md ; https://github.com/monoscope-tech/opentelemetry-demo/blob/HEAD/src/mcp/README.md ; https://github.com/vishalm/aethersearch/blob/HEAD/backend/aethersearch/mcp_server/README.md
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 57 — MCP Inspector (official, modelcontextprotocol/inspector)

- Resource name: MCP Inspector
- Canonical identity: `@modelcontextprotocol/inspector` (npm);
  repo modelcontextprotocol/inspector; Docker `ghcr.io/modelcontextprotocol/inspector`
- Category: A — MCP inspection/debugging tools; A — MCP server testing
- Type: Official developer tool (Web UI + CLI + TUI)
- Official URL: https://github.com/modelcontextprotocol/inspector (named in
  awesome list; repo page not opened — v2 README text via fork mirror)
- Description: Official visual testing/debugging tool for MCP servers. v2 ships
  three interfaces through one `mcp-inspector` binary: Web (Vite+React+Mantine
  SPA with Node backend/proxy), CLI (scriptable, for CI and agent feedback
  loops), TUI (Ink terminal UI). Connects via stdio/SSE/Streamable HTTP;
  built-in OAuth flow testing; exports Cursor/Claude Code config files.
  `npx @modelcontextprotocol/inspector --cli/--tui`. v1 line on `v1/main`
  (security fixes only, npm `v1-latest`); v2 developed on `v2/main`.
- Contents inspected: Fork-mirror README (v2 interfaces, commands, branch
  policy); dark-moon-x awesome list (usage commands, Docker command, security
  warning); artificial-intelligence-universe list (official tool description).
- Actual capabilities: READ + WRITE/EXECUTE — connects to any server and can
  invoke its tools (testing tool calls, including side-effecting ones).
- Usage domain: Server development, debugging, conformance testing, CI.
- Integration method: `npx @modelcontextprotocol/inspector [command]`; Docker.
- Compatibility: stdio/SSE/Streamable HTTP servers; OAuth testing built in.
- Dependencies: Node.js ^22.7.5 (v1 line).
- Authentication: Built-in OAuth flow testing.
- Availability: Open source; online instance at mcp.ziziyi.com/inspector
  (third-party, for quick remote-server tests).
- Maintenance: Active (steering group).
- License: Not verified from opened sources.
- Security: CVE-2025-49596 — `DANGEROUSLY_OMIT_AUTH` flag enables RCE risk;
  never use it. Binds localhost only by default; do not expose publicly.
- Limitations: Repo page not opened directly; v2 details via mirror text.
- Related resources: mcp-cli (Record 58), Snyk Agent Scan (Record 59).
- Sources: https://github.com/dark-moon-x/dm-ethanyolo01-awesome-mcp ; https://github.com/internetcityhd/artificial-intelligence-universe ; https://github.com/meskhidzeg4-create/inspector (fork mirror, search-result text)
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 58 — mcp-cli (chrishayuk) / MCP Discovery / Tester MCP Client (Apify) / MCP Inspector Online

- Resource name: Community inspection/testing CLIs (combined record)
- Canonical identity: `chrishayuk/mcp-cli`; "MCP Discovery" (Rust CLI);
  Apify Tester MCP Client; https://mcp.ziziyi.com/inspector
- Category: A — MCP inspection/debugging tools; A — MCP server testing
- Type: Community CLIs / web tools
- Official URL: https://github.com/chrishayuk/mcp-cli (named; not opened)
- Description: mcp-cli — CLI for direct interaction with MCP servers; granular
  exploration of tools/resources/prompts. MCP Discovery — lightweight Rust CLI
  for discovering/exploring server capabilities. Tester MCP Client (Apify) —
  lightweight open-source MCP client for functional smoke testing. MCP Inspector
  Online — browser-based Inspector, no install, for quick remote-server tests.
- Contents inspected: dark-moon-x awesome list table only.
- Actual capabilities: READ + EXECUTE (can invoke tools for testing).
- Usage domain: Manual/CI smoke testing of MCP servers.
- Integration method: CLI / web.
- Compatibility: MCP servers (transports vary).
- Dependencies: Varies.
- Authentication: Varies.
- Availability: Open source/community.
- Maintenance: Not verified.
- License: Not verified.
- Security: Testing tools can invoke side-effecting tools — use against dev servers.
- Limitations: Combined record; no primary repos opened.
- Related resources: MCP Inspector (Record 57), FastMCP CLI (Record 56).
- Sources: https://github.com/dark-moon-x/dm-ethanyolo01-awesome-mcp
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 59 — Snyk Agent Scan (formerly invariantlabs-ai/mcp-scan)

- Resource name: Snyk Agent Scan
- Canonical identity: `snyk/agent-scan` (GitHub); formerly `invariantlabs-ai/mcp-scan`
- Category: A — MCP security tools
- Type: Static security scanner (Python CLI, PyPI)
- Official URL: https://github.com/snyk/agent-scan
- Description: Security scanner purpose-built for the AI agent supply chain
  (acquired/evolved from Invariant Labs' mcp-scan). Auto-discovers agent
  configurations (Claude Code, Claude Desktop, Cursor, Windsurf, VS Code,
  Gemini CLI, OpenClaw, Kiro, Codex, others) and scans MCP servers, agent
  skills, and harnesses across 15+ risk categories: prompt injection, tool
  poisoning, tool shadowing, toxic flows, malware payloads in natural language,
  credential handling, hardcoded secrets, rug-pull (tool-definition drift via
  hashing), cross-origin escalation. `uvx snyk-agent-scan@latest` (full machine
  scan); `--skills` adds skill scanning; `--local-only` keeps analysis on-machine
  (some checks otherwise use Invariant's remote Guardrails API). Proxy mode can
  audit/log MCP traffic in real time and enforce guardrail policies (PII/secrets
  detection, tool restrictions, custom policies).
- Contents inspected: hinvec security-scanned-skills SKILL.md files (two:
  install, usage, what-it-scans); acacian/aegis vs-mcp-scan comparison
  (static vs runtime, trade-offs); samorrowdrums/mcp-security-workshop table
  (verified 2026-09-14; notes rename to Snyk Agent Scan); rhilgenkamp/mcp-scan
  mirror README (proxy mode, guardrails); security-phoenix-demo research doc
  (ecosystem scan stats: 5.5% of 1,899 servers with tool-poisoning patterns;
  VirusTotal 1,408/17,845 flagged).
- Actual capabilities: READ-ONLY analysis (static scanning + optional traffic
  proxy observation). Does not modify servers.
- Usage domain: Pre-deployment audit, CI security gates, incident triage.
- Integration method: `uvx snyk-agent-scan@latest` / `uvx mcp-scan@latest` (legacy name).
- Compatibility: File-based MCP client configs across major hosts.
- Dependencies: uv; SNYK_TOKEN for some flows (per skill doc).
- Authentication: API token for full features; `--local-only` avoids remote API.
- Availability: Open source (Snyk); PyPI.
- Maintenance: Active (Snyk; ~2K stars per skill docs).
- License: Not verified from opened sources.
- Security: Scanner itself reads your configs; `--local-only` for sensitive environments.
- Limitations: Static analysis only (point-in-time; no continuous runtime
  enforcement); pinning detects changes between scans, not during execution.
- Related resources: Cisco MCP Scanner (Record 60), mcp-context-protector (Record 61), MCP Shark (Record 62).
- Sources: https://github.com/hinvec/security-scanned-skills/blob/HEAD/skills/snyk-agent-scan-mcp-skill-security-scanner/SKILL.md ; https://github.com/hinvec/security-scanned-skills/blob/HEAD/skills/snyk-agent-scan/SKILL.md ; https://github.com/acacian/aegis/blob/HEAD/docs/comparisons/vs-mcp-scan.md ; https://github.com/sammorrowdrums/mcp-security-workshop ; https://github.com/security-phoenix-demo/ai-goat-ai-vulnerability-exploits-collection/blob/HEAD/Malicious%20MCP%20&%20Config%20File%20Repos%20for%20Security%20Scanner%20Testing.md
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 60 — Cisco AI Defense mcp-scanner

- Resource name: Cisco AI Defense MCP Scanner
- Canonical identity: `cisco-ai-defense/mcp-scanner` (GitHub)
- Category: A — MCP security tools
- Type: Security scanner (Python)
- Official URL: https://github.com/cisco-ai-defense/mcp-scanner (named; not opened)
- Description: Python-based scanner combining static rules, YARA and LLM
  analysis, dependency auditing, binary checks, and sandboxed package inspection.
- Contents inspected: samorrowdrums workshop table; tamish560/awesome-mcp-security list.
- Actual capabilities: READ-ONLY analysis.
- Usage domain: Deep security audit of MCP servers.
- Integration method: Not verified.
- Compatibility: Not verified.
- Dependencies: Python (presumed).
- Authentication: Not applicable.
- Availability: Open source (Cisco AI Defense).
- Maintenance: Not verified.
- License: Not verified.
- Security: Sandboxed package inspection is a differentiator.
- Limitations: Entry-level record.
- Related resources: Snyk Agent Scan (Record 59).
- Sources: https://github.com/sammorrowdrums/mcp-security-workshop ; https://github.com/tamish560/awesome-mcp-security
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 61 — Trail of Bits mcp-context-protector

- Resource name: mcp-context-protector
- Canonical identity: `trailofbits/mcp-context-protector` (GitHub)
- Category: A — MCP security tools
- Type: Security proxy (runtime protection)
- Official URL: https://github.com/trailofbits/mcp-context-protector (named; not opened)
- Description: Security proxy sitting between client and MCP servers: TOFU
  (trust-on-first-use) pinning of tool definitions, guardrail scanning, ANSI
  sanitization, quarantine for suspicious responses.
- Contents inspected: samorrowdrums workshop table only.
- Actual capabilities: Runtime traffic inspection/filtering (protective proxy).
- Usage domain: Runtime defense for MCP tool calls.
- Integration method: Proxy deployment (details not verified).
- Compatibility: MCP clients/servers (presumed).
- Dependencies: Not verified.
- Authentication: Not applicable.
- Availability: Open source (Trail of Bits).
- Maintenance: Not verified.
- License: Not verified.
- Security: TOFU pinning addresses rug-pull attacks at runtime (complements
  static scanners).
- Limitations: Entry-level record.
- Related resources: Snyk Agent Scan (Record 59), extensible-mcp (Record 64).
- Sources: https://github.com/sammorrowdrums/mcp-security-workshop
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 62 — MCP Shark / mcphound / mcprobe / mcpserver-audit / MCPGuard (scanner landscape)

- Resource name: Additional MCP security scanners (combined record)
- Canonical identity: `mcp-shark/mcp-shark`; `tayler-id/mcphound`;
  `tamish560/mcprobe`; `ModelContextProtocol-Security/mcpserver-audit`;
  usemcpguard.io (MCPGuard)
- Category: A — MCP security tools
- Type: Scanners/auditors
- Official URL: As above (named; not opened)
- Description: MCP Shark — local scanner + traffic proxy for MCP IDE configs;
  static rules, YARA-based traffic analysis, SARIF/HTML/JSON reports, optional
  cloud Smart Scan; source-available, non-commercial license (not OSI-approved).
  mcphound — covers attack paths, tool poisoning, typosquats, CVEs, trust
  scores, rug-pull detection. mcprobe — Go single-binary scanner; prompt
  injection in tool descriptions, tool shadowing, drift; text/JSON/SARIF output.
  mcpserver-audit — Cloud Security Alliance MCP Security initiative; pre-use
  audits. MCPGuard — commercial scanner with free tier.
- Contents inspected: samorrowdrums workshop table; tamish560/awesome-mcp-security
  scanners section.
- Actual capabilities: READ-ONLY analysis.
- Usage domain: Security auditing.
- Integration method: Varies.
- Compatibility: Varies.
- Dependencies: Varies.
- Authentication: Not applicable.
- Availability: Mixed open-source/commercial.
- Maintenance: Not verified.
- License: Mixed (MCP Shark: non-commercial source-available).
- Security: Not publicly documented beyond descriptions.
- Limitations: Combined record; no primary repos opened.
- Related resources: Snyk Agent Scan (Record 59).
- Sources: https://github.com/sammorrowdrums/mcp-security-workshop ; https://github.com/tamish560/awesome-mcp-security
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 63 — MCP Apps (official MCP extension)

- Resource name: MCP Apps
- Canonical identity: First official MCP extension (shipped 2026-01-26)
- Category: A — MCP specification extensions; A — MCP observability/interactivity
- Type: Protocol extension (server-rendered interactive UI)
- Official URL: Not verified (announcement via blog.modelcontextprotocol.io per timeline)
- Description: First official MCP extension: brings server-rendered interactive
  UI capabilities to MCP clients, ahead of the extensions framework being
  formalized in the next spec revision. FastMCP ships an apps runtime for
  building interactive UIs rendered inside MCP host conversations.
- Contents inspected: hidekazu-konishi spec timeline (extension note);
  api-evangelist FastMCP mirror (apps runtime mention).
- Actual capabilities: UI rendering primitives within MCP sessions (details not inspected).
- Usage domain: Interactive agent UIs.
- Integration method: Protocol extension; framework support (FastMCP).
- Compatibility: Clients implementing the extension.
- Dependencies: Not verified.
- Authentication: Per MCP auth framework.
- Availability: Shipped 2026-01-26.
- Maintenance: Steering group.
- License: Not verified.
- Security: Server-rendered UI is a new trust surface (not analyzed here).
- Limitations: Spec details not inspected.
- Related resources: MCP spec (Record 1), FastMCP (Record 56).
- Sources: https://hidekazu-konishi.com/entry/mcp_specification_version_timeline.html ; https://github.com/api-evangelist/fastmcp/blob/HEAD/README.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 64 — extensible-mcp (SenteLabsAI) — MCP proxy with filters

- Resource name: extensible-mcp
- Canonical identity: `SenteLabsAI/extensible-mcp` (GitHub)
- Category: A — MCP permission management; A — MCP adapters/bridges
- Type: MCP proxy (Python, presumed)
- Official URL: https://github.com/SenteLabsAI/extensible-mcp
- Description: MCP proxy with on-demand server loading, searchable tools, and
  pluggable filters for access control. Config uses Claude Desktop's
  `mcpServers` format plus a `filters` section: `similarity_threshold`,
  `access_control` (deny lists, deny patterns like `*__drop_*`/`*__delete_*`,
  allow_servers), `load_control` (allow/deny URL patterns). Servers can be
  local stdio or remote Streamable HTTP.
- Contents inspected: Repo README (search-result text): config example with
  filters.
- Actual capabilities: Proxy/filtering — can DENY tool calls by name/pattern
  and restrict server loading (permission management at the proxy layer).
- Usage domain: Least-privilege MCP deployments, tool allowlisting.
- Integration method: Proxy process configured with `mcpServers` + `filters`.
- Compatibility: MCP clients (presents as aggregated server).
- Dependencies: Python (presumed).
- Authentication: Not documented.
- Availability: Open source; last updated ~282 days before 2026-10-10.
- Maintenance: Community; low activity.
- License: Not verified.
- Security: Deny-patterns (`*__delete_*`) are a practical blast-radius control;
  proxy is a trust choke point.
- Limitations: README not fully opened.
- Related resources: Glama gateway (Record 28), mcp-context-protector (Record 61).
- Sources: https://github.com/SenteLabsAI/extensible-mcp
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 65 — MCP authentication & authorization framework (spec-level)

- Resource name: MCP authorization framework (OAuth 2.1 / OIDC)
- Canonical identity: Part of the MCP specification (2025-06-18 auth; 2025-11-25
  enhancements)
- Category: A — MCP authentication
- Type: Protocol security framework
- Official URL: https://modelcontextprotocol.io (spec; not opened directly)
- Description: MCP's authorization framework: OAuth 2.1-based; 2025-11-25 adds
  authorization-server discovery via OpenID Connect Discovery 1.0, incremental
  scope consent via `WWW-Authenticate`, and OAuth Client ID Metadata Documents
  as the recommended client registration mechanism. In practice: Figma remote
  server uses OAuth 2.1 (`mcp:connect` scope); Stripe remote uses OAuth;
  Mnemoverse remote uses OAuth; AWS managed endpoint bridges via
  `mcp-proxy-for-aws` (SigV4) because MCP clients speak OAuth, not SigV4;
  `mcp-remote` handles OAuth for stdio-only clients.
- Contents inspected: Spec changelog (via timeline); Figma OAuth notes;
  AWS proxy architecture doc; mcp-remote bridge docs.
- Actual capabilities: Standardized auth negotiation; NOT authorization policy
  (which data an authenticated agent may touch is left to enterprises — AAIF design).
- Usage domain: Securing remote MCP servers.
- Integration method: Protocol-level; client/bridge support required.
- Compatibility: Spec 2025-06-18+.
- Dependencies: OAuth/OIDC infrastructure.
- Authentication: OAuth 2.1 / OIDC.
- Availability: Spec-defined.
- Maintenance: Steering group.
- License: Not applicable.
- Security: Dynamic client registration allowlists (Figma case) can create
  vendor lock-in friction; tokens must be stored in OS keychains, not repos
  (per Figma community guidance).
- Limitations: Spec text not opened directly; synthesized from secondary sources.
- Related resources: MCP Inspector OAuth testing (Record 57), mcp-remote (Record 70).
- Sources: https://hidekazu-konishi.com/entry/mcp_specification_version_timeline.html ; https://github.com/zyqxd/my-stuff/blob/HEAD/ai/figma-mcp/README.md ; https://github.com/mpurushotham/cloud-aws-platform-management/blob/HEAD/docs/mcp/README.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 66 — MCP configuration tools (claude mcp CLI, Smithery CLI, mcp-publisher)

- Resource name: MCP configuration/install tooling (combined record)
- Canonical identity: `claude mcp` CLI (Anthropic); `@smithery/cli` (npm);
  `mcp-publisher` (modelcontextprotocol/registry)
- Category: A — MCP configuration tools
- Type: CLIs
- Official URL: https://github.com/modelcontextprotocol/registry (mcp-publisher); https://smithery.ai
- Description: `claude mcp add` — Anthropic's CLI for registering MCP servers
  (used across community docs: `claude mcp add --transport http figma-desktop
  http://127.0.0.1:3845/mcp`; `claude mcp add stripe --env-file … -- npx -y
  @stripe/mcp`). `@smithery/cli` — `npx -y @smithery/cli install <server>`
  one-click installs (e.g. brave). `mcp-publisher` — publishes servers to the
  official MCP Registry (`mcp-publisher login github`, `mcp-publisher publish`;
  requires `mcpName` in package.json matching server.json name; GitHub or DNS
  verification).
- Contents inspected: omcp quickstart (publisher flow); agora/seldonframe
  docs (smithery CLI); multiple skill docs (`claude mcp add` usage).
- Actual capabilities: Configuration management (read/write local config);
  publishing (registry write, authenticated).
- Usage domain: Installing, configuring, publishing MCP servers.
- Integration method: CLI.
- Compatibility: Respective clients/registry.
- Dependencies: Node/npm; GitHub account (publisher).
- Authentication: GitHub/DNS (publisher).
- Availability: Open tools.
- Maintenance: Active.
- License: Not verified.
- Security: `claude mcp add --env-file` keeps secrets out of chat/config repos
  (documented pattern).
- Limitations: Combined record; no CLI source opened.
- Related resources: MCP Registry (Record 25), Smithery (Record 29).
- Sources: https://github.com/enclawed/omcp/blob/HEAD/docs/registry/quickstart.mdx ; https://github.com/ritik200238/agora/blob/HEAD/mcp/DIRECTORY-LISTINGS.md ; https://github.com/carloscape/octorato/blob/HEAD/skills/stripe-payments/SKILL.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

---

## SECTION 8 — MCP CLIENTS

### Record 67 — MCP clients (ecosystem)

- Resource name: MCP clients (host applications)
- Canonical identity: Host applications implementing the MCP client role
  (spec: modelcontextprotocol.io)
- Category: A — MCP clients
- Type: Host applications (IDEs, CLIs, desktop apps, editors)
- Official URL: https://modelcontextprotocol.io (client documentation)
- Description: MCP clients are host-side components (1:1 with servers) that
  discover and invoke server tools/resources/prompts, with user-consent gates.
  Clients/hosts named across inspected sources: Claude Desktop
  (`claude_desktop_config.json`, `mcpServers` key), Claude Code
  (`.mcp.json`, `claude mcp` CLI, per-tool approval), Cursor (`~/.cursor/mcp.json`,
  SSE support since 0.48.0), Windsurf (`~/.codeium/windsurf/mcp_config.json`),
  VS Code (User Settings `mcp.servers` / `.vscode/mcp.json`; official directory
  at code.visualstudio.com/mcp), Zed, JetBrains IDEs, Neovim/Emacs (via ACP or
  plugins), Cline, Continue, Kiro, Gemini CLI, Codex CLI, Goose, ChatGPT
  (remote MCP connectors), OpenClaw/omnipilot (generic MCP YAML config).
- Contents inspected: vercel/mcp-handler CLIENTS.md (Claude Desktop/Cursor/
  Windsurf configs, mcp-remote usage); modelcontextprotocol/servers README
  (Claude Desktop config examples); evoxmusic memory details (client setup
  matrix); omnipilot docs (generic YAML + risk labels); snyk-agent-scan docs
  (config auto-discovery paths).
- Actual capabilities: Client capabilities — tool invocation with consent,
  sampling/roots/elicitation offered back to servers (per spec).
- Usage domain: Running agents against MCP servers.
- Integration method: JSON config files; CLI (`claude mcp add`); in-app UI.
- Compatibility: Transports vary by client (stdio universal; Streamable HTTP
  increasingly native; OAuth support varies — mcp-remote bridges gaps).
- Dependencies: Varies by host.
- Authentication: Per-server (API keys, OAuth, credential chains).
- Availability: Mixed commercial/open-source.
- Maintenance: Vendors.
- License: Per product.
- Security: Hosts are the consent/permission layer (Claude Code per-tool
  approval; extensible-mcp/Glama add proxy/gateway controls). Config files may
  hold secrets — prefer env files/keychains.
- Limitations: No single canonical client list was opened from the spec site;
  this is a synthesis of client mentions across sources. "Native integration
  with every compatible application" is NOT implied — support varies per client
  and per transport/auth method.
- Related resources: mcp-remote (Record 70), MCP Inspector (Record 57).
- Sources: https://github.com/vercel/mcp-handler/blob/ce0f0cee3ce60f23746a5c5d28e19d22bed91770/docs/CLIENTS.md ; https://github.com/modelcontextprotocol/servers ; https://github.com/xrchris7/omnipilot/blob/HEAD/docs/mcp.md ; https://github.com/hinvec/security-scanned-skills/blob/HEAD/skills/snyk-agent-scan-mcp-skill-security-scanner/SKILL.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

---

## SECTION 9 — MCP ADAPTERS AND BRIDGES

### Record 68 — mcp-remote (geoffreyhuntley)

- Resource name: mcp-remote
- Canonical identity: `mcp-remote` (npm); by Geoffrey Huntley
- Category: A — MCP adapters/bridges
- Type: stdio↔remote bridge (Node)
- Official URL: https://www.npmjs.com/package/mcp-remote (named in docs; page not opened)
- Description: The original stdio-to-remote bridge: lets MCP clients that only
  launch local stdio processes connect to remote MCP servers over Streamable
  HTTP/SSE, handling OAuth flows. Established the bridge pattern used across
  the ecosystem. Usage: `npx -y mcp-remote https://example.com/mcp` as the
  `command` in `mcpServers` config.
- Contents inspected: vercel/mcp-handler CLIENTS.md (usage pattern, Cursor
  OAuth note); browserbase README (fallback for clients without SHTTP);
  dbcode.io docs; fastmcp-remote PyPI page (credits mcp-remote as the originator
  of the pattern).
- Actual capabilities: Protocol translation (stdio JSON-RPC ↔ HTTP/SSE) +
  OAuth handling. No tools of its own.
- Usage domain: Connecting stdio-only clients to remote servers.
- Integration method: `npx -y mcp-remote <url>` as server command.
- Compatibility: Any stdio-capable client.
- Dependencies: Node.js/npx.
- Authentication: Handles OAuth on behalf of the client.
- Availability: Open source (npm).
- Maintenance: Community.
- License: Not verified.
- Security: Holds OAuth tokens for the remote server — runs locally, but is a
  credential-bearing process.
- Limitations: npm page/repo not opened.
- Related resources: fastmcp-remote (Record 71), vercel/mcp-handler (Record 69).
- Sources: https://github.com/vercel/mcp-handler/blob/ce0f0cee3ce60f23746a5c5d28e19d22bed91770/docs/CLIENTS.md ; https://github.com/browserbase/mcp-server-browserbase ; https://pypi.org/project/fastmcp-remote/4.0.0b2/ ; https://dbcode.io/docs/ai/mcp
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 69 — vercel/mcp-handler

- Resource name: mcp-handler
- Canonical identity: `vercel/mcp-handler` (GitHub)
- Category: A — MCP adapters/bridges; A — MCP development frameworks (TS)
- Type: Adapter library for serving MCP over HTTP (Next.js/Vercel)
- Official URL: https://github.com/vercel/mcp-handler
- Description: Vercel's handler making it easy to expose an MCP server from a
  web app (e.g. Next.js API route at `/api/mcp`). Docs include CLIENTS.md with
  per-client connection guidance (direct Streamable HTTP vs mcp-remote for
  stdio-only clients; Cursor SSE/OAuth notes).
- Contents inspected: vercel/mcp-handler docs/CLIENTS.md (search-result text).
- Actual capabilities: HTTP transport adapter for MCP servers (bridge between
  web frameworks and the MCP protocol).
- Usage domain: Deploying MCP servers as web endpoints.
- Integration method: Library import in a web app.
- Compatibility: Next.js/Vercel; clients via Streamable HTTP or mcp-remote.
- Dependencies: Node.js; Next.js (typical).
- Authentication: App-level (not verified).
- Availability: Open source (Vercel).
- Maintenance: Active (Vercel) — presumed.
- License: Not verified.
- Security: Exposes MCP over HTTP — requires authN/authZ design (not inspected).
- Limitations: Repo not fully opened.
- Related resources: mcp-remote (Record 68), FastMCP (Record 56).
- Sources: https://github.com/vercel/mcp-handler/blob/ce0f0cee3ce60f23746a5c5d28e19d22bed91770/docs/CLIENTS.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 70 — fastmcp-remote (PyPI)

- Resource name: fastmcp-remote
- Canonical identity: `fastmcp-remote` (PyPI; FastMCP project)
- Category: A — MCP adapters/bridges
- Type: Standalone Python stdio bridge for remote MCP servers
- Official URL: https://pypi.org/project/fastmcp-remote/
- Description: FastMCP's standalone Python stdio bridge: lets MCP clients that
  launch local stdio processes connect to remote MCP servers over Streamable
  HTTP or SSE. Intentionally smaller than the FastMCP CLI — builds one FastMCP
  client for the URL, exposes it as a local stdio proxy. Command shape inspired
  by the original mcp-remote npm project. Example: `uvx fastmcp-remote
  https://mcp.linear.app/mcp`.
- Contents inspected: PyPI page (search-result text).
- Actual capabilities: stdio↔HTTP/SSE bridging. No tools of its own.
- Usage domain: Same as mcp-remote, for Python/uv-based setups.
- Integration method: `uvx fastmcp-remote <url>` as server command.
- Compatibility: Any stdio-capable client.
- Dependencies: Python/uvx.
- Authentication: Not documented on inspected page.
- Availability: Open source (FastMCP/PrefectHQ).
- Maintenance: Active (presumed).
- License: Apache-2.0 (presumed from FastMCP; not verified on page).
- Security: Credential-bearing local process (as mcp-remote).
- Limitations: PyPI page only; repo not opened.
- Related resources: mcp-remote (Record 68), FastMCP (Record 56).
- Sources: https://pypi.org/project/fastmcp-remote/4.0.0b2/
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 71 — mcp-proxy-for-aws

- Resource name: mcp-proxy-for-aws
- Canonical identity: AWS-provided local proxy (part of AWS MCP offering)
- Category: A — MCP adapters/bridges; A — MCP authentication
- Type: Local auth bridge (SigV4 signing proxy)
- Official URL: Not verified (documented in mpurushotham/cloud-aws-platform-management docs)
- Description: Local process bridging the auth gap for the AWS-managed remote
  MCP server: MCP clients speak OAuth for remote servers, but AWS requires
  SigV4 — the proxy resolves credentials from the normal AWS credential chain
  (e.g. `aws login` sessions up to 12h) and signs each HTTPS request to
  `aws-mcp.us-east-1.api.aws/mcp`. Every call is attributed in CloudTrail with
  MCP context.
- Contents inspected: mpurushotham docs (architecture diagram, sequence
  diagram, auth section).
- Actual capabilities: Request signing/forwarding (stdio in, SigV4 HTTPS out).
- Usage domain: AWS-managed MCP access.
- Integration method: Local stdio process in `mcpServers` config.
- Compatibility: MCP clients (stdio).
- Dependencies: AWS CLI credential chain.
- Authentication: SigV4 via local credential chain.
- Availability: Part of AWS MCP offering (GA 2026-05-06 per docs).
- Maintenance: AWS.
- License: Not verified.
- Security: Acts with the user's IAM identity — run as non-root, least-privilege.
- Limitations: Docs-only record; proxy repo/URL not verified.
- Related resources: awslabs/mcp (Record 16), mcp-remote (Record 68).
- Sources: https://github.com/mpurushotham/cloud-aws-platform-management/blob/HEAD/docs/mcp/README.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

---

## SECTION 10 — MCP SERVERS DESIGNED FOR WEB DEVELOPMENT (composite)

### Record 72 — Web-development MCP servers (composite)

- Resource name: Web-development MCP server set (composite record)
- Canonical identity: Multiple (see members)
- Category: B — application-specific (web development)
- Type: Composite record
- Official URL: Not applicable (see member records)
- Description: MCP servers directly serving web-development workflows,
  verified in this workstream: Fetch (Record 7) — read-only page→markdown
  retrieval; Firecrawl (Record 37) — JS-rendered scraping/crawling/extraction;
  Browserbase (Record 22) / Cloudflare Browser Rendering (Record 21) —
  full browser automation; Figma Dev Mode (Record 13) — design→code;
  microsoft/playwright-mcp (dedup xref) — Microsoft's Playwright browser
  automation; Tavily/Exa/Brave (Records 35/36/14) — research/grounding;
  awslabs AWS servers (Record 16) — deploy/infra; Assurly (Record 55) —
  pre-deploy gate (Next.js/Supabase/Stripe/Vercel). Component registries:
  shadcn MCP (dedup xref). Documentation retrieval: Ref Tools (dedup xref),
  awslabs.aws-documentation-mcp-server (Record 16).
- Contents inspected: Member records (see Sources there).
- Actual capabilities: Mixed read-only (Fetch, search APIs) and write/execute
  (browser automation, AWS, Figma remote).
- Usage domain: Web development: research, design→code, scraping, testing,
  deployment.
- Integration method: stdio or Streamable HTTP per member.
- Compatibility: MCP clients.
- Dependencies: Per member (API keys, browsers, cloud credentials).
- Authentication: Per member.
- Availability: Mixed.
- Maintenance: Mixed.
- License: Mixed.
- Security: Browser automation + cloud write access are the high-risk members;
  scraped/fetched content is untrusted input everywhere.
- Limitations: Composite — see member records for verified detail.
- Related resources: Records 7, 13, 14, 16, 21, 22, 35, 36, 37, 55.
- Sources: (member records)
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

---

## SECTION 11 — ALTERNATIVES TO MCP (correctly classified)

### Record 73 — A2A (Agent2Agent Protocol)

- Resource name: Agent2Agent (A2A) Protocol
- Canonical identity: `a2aproject/A2A` (GitHub); spec v1.0.0 → v1.2
- Category: C — agent-to-agent communication mechanisms (other relevant open protocols)
- Type: Open protocol (NOT an MCP alternative at the same layer — complementary)
- Official URL: https://github.com/a2aproject/A2A
- Description: Google-originated open standard (launched 2025-04) for
  peer-to-peer agent collaboration; joined the AAIF as a hosted project
  2026-08-17/20 alongside MCP. Where MCP standardizes how an agent uses a tool
  or resource (vertical), A2A standardizes how one agent delegates work to
  another (horizontal): Agent Cards at `/.well-known/agent-card.json` for
  capability discovery (v1.2 adds signed Agent Cards with cryptographic domain
  verification), task-based messaging, multi-tenancy, JSON-RPC + gRPC bindings,
  version negotiation. Native support in LangGraph, CrewAI, LlamaIndex,
  Semantic Kernel, AutoGen; 150 orgs in production per 2026-05 brief.
- Contents inspected: Forkast analysis (AAIF consolidation, layer separation);
  dev.to explainer (HTTP-for-agents analogy, spec one-liner); deepinspect
  (signed Agent Cards, OAuth 2.0/OIDC identity; authorization gap);
  practallogix (complementary layers); osop-spec brief (v1.2 features,
  adoption); agentlistio awesome-agent-list (repo link, related protocols
  AGNTCY/ANP/NANDA).
- Actual capabilities: Agent discovery, task delegation, cross-org messaging
  with identity (OAuth 2.0/OIDC, signed cards).
- Usage domain: Multi-agent systems, cross-vendor agent handoffs.
- Integration method: Protocol; Agent Card well-known URL; JSON-RPC/gRPC.
- Compatibility: Framework-native support listed above.
- Dependencies: None (protocol).
- Authentication: OAuth 2.0 / OIDC; signed Agent Cards (v1.2).
- Availability: Open standard, Linux Foundation governance.
- Maintenance: AAIF; v1.2 current per 2026-05 brief.
- License: Open (Linux Foundation).
- Security: Standardizes authentication, NOT authorization — which data an
  authenticated agent may touch across org boundaries is each enterprise's
  decision (explicit AAIF design gap).
- Limitations: Repo/spec not opened directly; details from secondary analyses.
- Related resources: MCP spec (Record 1), ACP (Record 74), AGNTCY/ANP (named only).
- Sources: https://forkast.news/googles-a2a-protocol-joins-aaif-consolidating-the-agent-economys-protocol-layer-under-one-roof/ ; https://dev.to/alex_aslam/your-agents-cant-collaborate-if-they-only-speak-tool-calls-the-a2a-protocol-that-fixes-peer-4o0d ; https://www.deepinspect.ai/blog/agent-to-agent-authorization ; https://www.practicallogix.com/the-2026-agent-interoperability-reset-a2a-mcp-under-aaif/ ; https://github.com/archie0125/osop-spec/blob/HEAD/docs/strategy/2026-05-01-daily-brief.md ; https://github.com/agentlistio/awesome-agent-list
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 74 — ACP (Agent Client Protocol)

- Resource name: Agent Client Protocol (ACP)
- Canonical identity: `agentclientprotocol/agent-client-protocol` (GitHub);
  spec at https://agentclientprotocol.com
- Category: C — extension interfaces; other relevant open protocols
- Type: Open protocol (JSON-RPC 2.0 over stdio), editor↔agent
- Official URL: https://agentclientprotocol.com
- Description: Created by Zed Industries (2025-08), co-maintained with
  JetBrains; Apache 2.0. Standardizes communication between code editors and
  coding agents — "LSP for AI agents": one agent implementation works across
  Zed, JetBrains IDEs, Neovim, Emacs without per-editor plugins. Covers session
  management, streaming responses, tool approval, file/terminal delegation.
  Complements MCP: ACP connects editors→agents; MCP connects agents→tools.
  ACP Registry lists ~50 agents (Claude Code, Gemini CLI, Codex CLI, Copilot,
  Cursor, Goose, Kiro, OpenCode, …; auto-updates hourly). Adapters exist for
  Claude Code (`@agentclientprotocol/claude-agent-acp`) and Codex
  (`@agentclientprotocol/codex-acp`); Gemini CLI speaks it natively. SDKs:
  TypeScript `@agentclientprotocol/sdk`, Rust `agent-client-protocol` crate,
  JSON Schema, React hooks.
- Contents inspected: dev.to FAQ (comparison with MCP, editor/agent support);
  apx docs (stdio mechanics, Zed settings); coxswain ADR (session/permission
  flow, adapters); nanocoder issue (spec link, SDK, registry);
  JetBrains/agent-client-protocol README mirror (integrations, libraries).
- Actual capabilities: Editor↔agent sessions: initialize, session/new,
  session/prompt, session/cancel, streamed chunks, tool_call updates with diffs,
  plan updates, session/request_permission; a session can be given MCP servers
  by the client.
- Usage domain: Editor integration for coding agents.
- Integration method: Editor spawns agent over stdio; config
  (`~/.jetbrains/acp.json`, Zed `settings.json` `agent_servers`).
- Compatibility: Zed (native), JetBrains IDEs (native), Neovim/Emacs (community
  plugins), VS Code (community extensions; no native support).
- Dependencies: None (protocol).
- Authentication: Permission-request flow surfaces approvals in the editor UI.
- Availability: Open standard.
- Maintenance: Active (Zed + JetBrains).
- License: Apache-2.0.
- Security: Editor-native Allow/Reject dialogs for tool approvals — a
  permission UX improvement over terminal prompts.
- Limitations: Official repo page not opened; details from secondary docs.
- Related resources: LSP (Record 75), MCP clients (Record 67).
- Sources: https://dev.to/dmaxdev/agent-client-protocol-acp-connect-any-ai-agent-to-any-editor-2p0m ; https://github.com/agentprojectcontext/apx/blob/HEAD/docs/src/content/docs/surfaces/acp.mdx ; https://github.com/sladkoff/coxswain/blob/HEAD/docs/adr/0018-agents-over-acp.md ; https://github.com/nano-collective/nanocoder/issues/401
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 75 — LSP (Language Server Protocol) and MCP↔LSP bridges

- Resource name: Language Server Protocol (LSP)
- Canonical identity: Microsoft-originated open protocol (open standard)
- Category: C — Language Server Protocol integrations
- Type: Open protocol (editor↔language-server), predates MCP
- Official URL: Not verified in this workstream (no primary URL opened)
- Description: The established open protocol standardizing editor↔language
  intelligence (diagnostics, completions, go-to-definition, etc.). Relevant as
  (a) the architectural template ACP explicitly follows ("LSP for AI agents"),
  and (b) an integration surface: language servers can be wrapped/exposed to
  agents via MCP bridges (community "MCP language server" bridges exist but no
  primary-source-verified instance was established in this workstream —
  Unresolved). Classification: protocol, not an MCP server.
- Contents inspected: ACP docs (LSP analogy statements). No LSP spec or bridge
  repo opened.
- Actual capabilities: Language intelligence protocol (diagnostics, hover,
  completion, references, etc.) — general knowledge, not source-verified here.
- Usage domain: Editor language features; agent code intelligence via bridges.
- Integration method: JSON-RPC (stdio/TCP) between editor and language server.
- Compatibility: Universal editor support.
- Dependencies: Per language server.
- Authentication: Not applicable (local).
- Availability: Open standard.
- Maintenance: Microsoft + community.
- License: Not verified here.
- Security: Local process; language servers execute project code tooling.
- Limitations: No primary source opened; bridge projects Unresolved — flagged
  for follow-up rather than asserted.
- Related resources: ACP (Record 74).
- Sources: https://dev.to/dmaxdev/agent-client-protocol-acp-connect-any-ai-agent-to-any-editor-2p0m ; https://github.com/nano-collective/nanocoder/issues/401
- Verification date: 2026-10-10. Confidence: Low. Label: Partially verified.

### Record 76 — AGENTS.md / CLAUDE.md filesystem conventions

- Resource name: AGENTS.md (open standard); CLAUDE.md (Anthropic convention)
- Canonical identity: AGENTS.md — AAIF founding project (donated by OpenAI,
  2025-12-09); CLAUDE.md — Claude Code convention
- Category: C — filesystem conventions (AGENTS.md/CLAUDE.md)
- Type: Instruction-file convention / open standard (NOT a protocol, NOT MCP)
- Official URL: Not verified (AAIF pages; agents.md spec site not opened)
- Description: Plain-Markdown standing-instructions files that coding agents
  read natively — the "README for agents": project context, conventions,
  preferred tool usage. Originated at OpenAI (mid-2025) via industry working
  group (Google, Sourcegraph, Factory, Cursor); donated to AAIF 2025-12-09
  alongside MCP and goose. 60,000+ GitHub repos use it (Dec 2025). Read natively
  by Codex CLI, GitHub Copilot, Cursor, Windsurf, Amp, Devin. Claude Code reads
  CLAUDE.md; since v2.1.277 (Sept 2026) Claude Code falls back to AGENTS.md when
  no CLAUDE.md exists (toggleable via /config). Community workaround before
  that: symlink one to the other.
- Contents inspected: agentic-ai knowledge-base docs (donation, purpose);
  genno-whittlery agent-notes (adoption, Claude Code interplay, symlink
  workaround); theregister (Anthropic AGENTS.md support, v2.1.277);
  gend.co/gizmodo (AAIF founding donations).
- Actual capabilities: Static instruction files — no tools, no execution, no
  discovery protocol. Complements MCP (procedural knowledge vs tool access).
- Usage domain: Project-specific agent guidance, portability across agents.
- Integration method: File placed in repo root; agents read automatically.
- Compatibility: Per-agent (see readers above).
- Dependencies: None.
- Authentication: Not applicable.
- Availability: Open standard.
- Maintenance: AAIF community governance.
- License: Open.
- Security: Instructions files are trusted input to the agent — a malicious
  AGENTS.md in a cloned repo is a prompt-injection vector (general; treat
  accordingly).
- Limitations: Spec site not opened; counts from secondary sources.
- Related resources: Agent Skills (Record 81 — complementary per MCP wiki note).
- Sources: https://agentic-ai.readthedocs.io/en/latest/Standards/agents-md/ ; https://github.com/genno-whittlery/agent-notes/blob/HEAD/2026-agents-md-standard.md ; https://www.theregister.com/ai-and-ml/2026/09/18/anthropic-decides-to-support-openais-markdown-instructions-spec/5297588 ; https://www.gend.co/en-ca/blog/openai-agentic-ai-foundation-linux ; https://gizmodo.com/openai-anthropic-and-others-create-foundation-for-standardizing-ai-agents-2000697488
- Verification date: 2026-10-10. Confidence: High. Label: Verified.

### Record 77 — Native function calling / tool use (OpenAI Responses API et al.)

- Resource name: Native model function calling (tool use)
- Canonical identity: Provider APIs (OpenAI Responses/Chat Completions tools,
  Anthropic tool use, Gemini function calling)
- Category: C — SDKs / built-in model tool interfaces
- Type: Model API capability (NOT MCP)
- Official URL: Not verified in this workstream (no provider docs opened)
- Description: Models expose native tool-calling: the application defines
  function schemas and executes calls itself. MCP is a standardized,
  discoverable interface *on top of* such capabilities — an MCP server usually
  wraps existing APIs/services rather than replacing them. The win of MCP over
  bespoke function calling is write-once discovery across clients (M+N → M+N
  integration model). Stripe's agent toolkit ships both: function-calling SDKs
  AND an MCP server.
- Contents inspected: dev.to MCP-vs-API explainer (layer distinction);
  hinvec Stripe skill (toolkit supports OpenAI/LangChain/CrewAI/Vercel AI SDK
  through function calling AND MCP).
- Actual capabilities: Per-application tool definitions; app executes.
- Usage domain: Custom agent harnesses.
- Integration method: Provider SDK.
- Compatibility: Per provider.
- Dependencies: Provider API access.
- Authentication: Provider API keys.
- Availability: Per provider.
- Maintenance: Providers.
- License: Per provider.
- Security: App-controlled; no cross-client discovery.
- Limitations: No provider docs opened; conceptual record.
- Related resources: Stripe toolkit (Record 15), SDKs (Records 3–5).
- Sources: http://dev.to/aiarch_wibo/mcp-model-context-protocol-the-three-primitives-and-what-two-real-servers-actually-return-4m21 ; https://github.com/hinvec/security-scanned-skills/blob/HEAD/skills/stripe-agent-toolkit-ai-payment-integration/SKILL.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 78 — REST APIs (as integration mechanism)

- Resource name: REST APIs (direct integration)
- Canonical identity: Per-service HTTPS APIs
- Category: C — REST APIs
- Type: Integration mechanism (NOT MCP)
- Official URL: Not applicable
- Description: Direct HTTPS API integration — the underlying service layer that
  MCP servers typically wrap. Evidence from this workstream: toolforte.com
  exposes the same 150 tools as both a plain REST API and an MCP server;
  dylckh/mcp-server-meta-search exposes a REST admin API alongside its MCP
  endpoint; FastMCP supports OpenAPI/FastAPI import to generate MCP servers
  from REST APIs; AWS Bedrock AgentCore Gateway turns APIs and Lambda functions
  into MCP-compatible tools behind one secure endpoint (GA 2025-10-13).
  Classification: REST is the wrapped layer; MCP is the discoverable agent
  interface above it.
- Contents inspected: toolforte dev.to post (dual REST+MCP offering);
  dylckh README (REST admin API); api-evangelist FastMCP mirror (OpenAPI
  import); hidekazu-konishi timeline (AgentCore Gateway GA).
- Actual capabilities: Per-API CRUD/operations.
- Usage domain: Service integration where no MCP server exists or bespoke
  control is needed.
- Integration method: HTTPS + client code.
- Compatibility: Per service.
- Dependencies: Service credentials.
- Authentication: Per service (keys, OAuth).
- Availability: Per service.
- Maintenance: Service vendors.
- License: Per service.
- Security: Per-service auth; no agent-specific consent layer.
- Limitations: Conceptual record synthesized from workstream evidence.
- Related resources: FastMCP OpenAPI import (Record 56), AgentCore (Record 82).
- Sources: https://dev.to/tonietonie/i-gave-360-browser-tools-an-mcp-server-here-is-what-broke-39g6 ; https://github.com/dylckh/mcp-server-meta-search ; https://github.com/api-evangelist/fastmcp/blob/HEAD/README.md ; https://hidekazu-konishi.com/entry/mcp_specification_version_timeline.html
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 79 — CLI integrations and command-based tool wrappers

- Resource name: CLI integrations / command-based tool wrappers
- Canonical identity: Pattern (not a single product)
- Category: C — CLI integrations; command-based tool wrappers
- Type: Integration mechanism (NOT MCP)
- Official URL: Not applicable
- Description: Agents invoking ordinary CLIs (kubectl, gh, aws, docker, uvx/npx
  one-shot runs) directly instead of via MCP. Distinct from MCP: no
  discovery protocol, no schema negotiation, no consent layer — the harness
  defines commands. Evidence: FastMCP CLI (`fastmcp list`/`call`) itself wraps
  MCP servers as CLI commands; omnipilot one-shot pattern
  (`omnipilot "use the sqlite MCP server: …"`); alkofu/ai-tpk installer
  invoking kubernetes/cloudwatch MCP servers via npx/uvx. MCP stdio servers
  are *launched* via CLI but speak the MCP protocol — launching ≠ CLI
  integration (classification boundary).
- Contents inspected: lysandre001 FastMCP CLI skill; xrchris7/omnipilot docs;
  alkofu/ai-tpk commit.
- Actual capabilities: Arbitrary command execution by the harness.
- Usage domain: Scripting, CI, harnesses without MCP support.
- Integration method: Subprocess invocation.
- Compatibility: Any CLI.
- Dependencies: Installed CLIs + credentials.
- Authentication: Per CLI.
- Availability: Per tool.
- Maintenance: Tool vendors.
- License: Per tool.
- Security: Full shell-equivalent risk; no MCP consent semantics.
- Limitations: Pattern record.
- Related resources: FastMCP CLI (Record 56).
- Sources: https://github.com/lysandre001/skills-registry/blob/HEAD/jlowin--fastmcp--fastmcp-client-cli/SKILL.md ; https://github.com/xrchris7/omnipilot/blob/HEAD/docs/mcp.md ; https://github.com/alkofu/ai-tpk/commit/18bd0f4e166729c481a74bc344429c322979cb01
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 80 — Plugins and extension interfaces

- Resource name: Editor/IDE plugin and extension interfaces
- Canonical identity: Per-platform (VS Code extensions, JetBrains plugins, Figma plugins, etc.)
- Category: C — plugins, extension interfaces
- Type: Integration mechanism (NOT MCP)
- Official URL: Not applicable
- Description: Native plugin/extension APIs (VS Code Extension API, JetBrains
  Platform, Figma Plugin API) — the mechanism ACP was created to avoid
  re-implementing per editor. Distinct from MCP: plugins run inside the host
  with host APIs, not as protocol peers. Evidence: blueberry-team's Figma MCP
  Bridge is a *Figma plugin* (Desktop Plugin API) fronting an MCP server —
  plugin API and MCP composed, not confused. ACP's value proposition is
  precisely "one integration instead of per-editor plugins."
- Contents inspected: blueberry-team/figma-dev-mode-for-free README
  (plugin→WebSocket→MCP server architecture); nanocoder ACP issue (per-editor
  plugin motivation).
- Actual capabilities: Host-native UI and API access.
- Usage domain: Deep editor/product integration.
- Integration method: Platform SDK.
- Compatibility: Per platform.
- Dependencies: Host application.
- Authentication: Host-managed.
- Availability: Per platform.
- Maintenance: Platform vendors + plugin authors.
- License: Per platform/plugin.
- Security: Plugins run with host privileges — supply-chain risk distinct
  from MCP's consent model.
- Limitations: Pattern record.
- Related resources: ACP (Record 74), Figma (Record 13).
- Sources: https://github.com/blueberry-team/figma-dev-mode-for-free/blob/HEAD/README.md ; https://github.com/nano-collective/nanocoder/issues/401
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 81 — Agent Skills (complementary instruction layer)

- Resource name: Agent Skills (SKILL.md)
- Canonical identity: Agent Skills specification (complementary to MCP)
- Category: C — structured configuration standards
- Type: Instruction/packaging format (NOT MCP, NOT a tool protocol)
- Official URL: Not verified in this workstream
- Description: Per the MCP community wiki note found in research: "MCP and
  skills are complementary — MCP connects agents to external tools and data
  while Agent Skills encode procedural knowledge, including workflows that use
  those external tools." Skills are SKILL.md instruction bundles (often with
  scripts); registries include skills.sh, CladueSkills.info, awesome-claude-skills.
  Several inspected sources are skill repos documenting MCP servers (octorato,
  hinvec/security-scanned-skills), demonstrating the layering in practice.
- Contents inspected: fablesecondbrain MCP wiki entity (complementarity quote);
  multiple SKILL.md files (stripe-payments, snyk-agent-scan, figma-implement).
- Actual capabilities: Procedural knowledge delivery; scripts may execute via
  the agent (not a protocol capability).
- Usage domain: Reusable workflows, tool-use playbooks.
- Integration method: SKILL.md files loaded by agents.
- Compatibility: Per agent (Claude Code skills, etc.).
- Dependencies: None.
- Authentication: Not applicable.
- Availability: Open convention.
- Maintenance: Community.
- License: Per skill.
- Security: Skills are scanned by Snyk Agent Scan for prompt injection/malware
  — treat as untrusted input (see Record 59).
- Limitations: Spec not opened; definition from secondary wiki + usage evidence.
- Related resources: Snyk Agent Scan (Record 59), AGENTS.md (Record 76).
- Sources: https://github.com/agricidaniel/fablesecondbrain/blob/HEAD/wiki/entities/Model%20Context%20Protocol.md ; https://github.com/carloscape/octorato/blob/HEAD/skills/stripe-payments/SKILL.md ; https://github.com/ole00007/obsidian-vault/blob/HEAD/03-Resources/Hermes-Setup-and-MCP/Point6_Skill_MCP_Marketplaces_Extended.md
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

### Record 82 — API→MCP generation: OpenAPI import, AgentCore Gateway (dedup xrefs + note)

- Resource name: API→MCP generation mechanisms
- Canonical identity: FastMCP OpenAPI/FastAPI import; AWS Bedrock AgentCore Gateway;
  cnoe-io/openapi-mcp-codegen (dedup); awslabs/openapi-mcp-server (dedup)
- Category: C — structured configuration standards (OpenAPI as source)
- Type: Code generation / gateway mechanisms
- Official URL: https://github.com/jlowin/fastmcp (import feature); AWS AgentCore docs (not opened)
- Description: Mechanisms that derive MCP servers from existing API
  descriptions rather than hand-writing tools: FastMCP's OpenAPI/FastAPI
  import; AWS Bedrock AgentCore Gateway (GA 2025-10-13) connecting existing
  MCP servers and turning APIs/Lambda functions into MCP-compatible tools
  behind one secure endpoint. The OpenCode catalog already covers
  cnoe-io/openapi-mcp-codegen and awslabs/openapi-mcp-server — cross-referenced
  only (dedup).
- Contents inspected: api-evangelist FastMCP mirror (import feature);
  hidekazu-konishi timeline (AgentCore GA).
- Actual capabilities: Generation/gateway — output servers inherit the source
  API's read/write profile.
- Usage domain: Bootstrapping MCP coverage for existing APIs.
- Integration method: Import/generation at build time; gateway at runtime.
- Compatibility: OpenAPI-described services; AWS.
- Dependencies: OpenAPI specs; AWS account (AgentCore).
- Authentication: Per source API.
- Availability: Open source (FastMCP); AWS managed (AgentCore).
- Maintenance: PrefectHQ; AWS.
- License: Apache-2.0 (FastMCP); commercial (AgentCore).
- Security: Generated tools inherit API permissions — scope the source
  credentials.
- Limitations: AgentCore details from timeline only.
- Related resources: FastMCP (Record 56), awslabs/mcp (Record 16).
- Sources: https://github.com/api-evangelist/fastmcp/blob/HEAD/README.md ; https://hidekazu-konishi.com/entry/mcp_specification_version_timeline.html
- Verification date: 2026-10-10. Confidence: Medium. Label: Partially verified.

---

## COVERAGE NOTE

### Counts

- Total resource records: 82 (Records 1–82), plus the archived-reference-servers
  note (12 servers), plus combined sub-records inside Records 5, 32, 33, 34, 53,
  58, 62 (each naming 2–8 additional projects).
- Per-category counts:
  - Section 1 (spec/governance): 2
  - Section 2 (SDKs): 3 (covering 10 languages)
  - Section 3 (official reference servers): 7 + 12 archived (note)
  - Section 4 (official/vendor integrations): 12 (incl. 1 dedup xref)
  - Section 5 (registries/directories): 10 (covering ~20 named directories)
  - Section 6 (functional community servers): 21 records across search (5),
    browser (note), code/terminal (note), databases (8), cloud/infra (2),
    memory (4), testing/security (2), business (note), public APIs (note)
  - Section 7 (dev/debug/security/observability/config): 11
  - Section 8 (clients): 1 (covering ~15 named clients/hosts)
  - Section 9 (adapters/bridges): 4
  - Section 10 (web-dev composite): 1
  - Section 11 (alternatives): 10
- Verification labels: Verified: ~14 records. Partially verified: ~50 records.
  Entry-level/low-confidence: ~18 records. Archived: 12 (note). No record is
  presented above its evidence.

### Local-only vs remote, auth, rate limits (cross-cutting)

- Local-only (stdio, no auth, no rate limits beyond the machine): reference
  servers (Filesystem, Git, Memory, Time, Sequential Thinking, Everything),
  basic-memory, Mimir, Servex, qore-mcp, FastMCP-built local servers.
- Remote (Streamable HTTP/SSE, auth required, rate-limit-sensitive): Brave
  (API key, credit quotas), Tavily/Exa (API key, query-param auth), Firecrawl
  (API key), Stripe remote (OAuth), Figma remote (OAuth 2.1), Linear remote,
  Semgrep (Bearer), awslabs managed AWS (SigV4 via proxy), Cloudflare/Browserbase
  hosted (Bearer/API key), Glama/Smithery gateways (OAuth/usage metering),
  mcp-server-meta-search (PAT).
- Rate-limit-sensitive: all hosted search/scraping APIs (Brave/Tavily/Exa/
  Firecrawl), Stripe (API rate limits, financial side effects), AWS (API
  throttling + cost), database servers (connection limits).

### Key gaps and unresolved items (more work warranted)

1. Per-SDK API surfaces (Record 5): no SDK repo opened beyond README-level;
   C#/Java/Kotlin/PHP/Ruby/Rust/Swift SDK maintenance status Unresolved.
2. Database servers (Records 43–47): entry-level only; official MongoDB repo
   URL, Supabase/Neon tool lists, and auth details need primary-source
   inspection.
3. MCP↔LSP bridges (Record 75): existence asserted by analogy only — needs a
   dedicated search for concrete projects.
4. Terminal-operations servers (6.3 note): GongRzhe/terminal-controller-mcp
   named once; capabilities Unresolved.
5. Codebase-search servers beyond dedup: no primary-verified standalone server
   found — possible gap or adequately covered by dedup items.
6. MCP Apps extension spec (Record 63): announcement-level only.
7. Smithery creator-monetization terms: conflicting secondary claims — verify
   directly before relying.
8. Figma remote OAuth client-allowlist observation (2026-08): time-sensitive,
   single-source — re-verify before acting.
9. Security-scanner efficacy claims (5.5% poisoning rate, VirusTotal flags):
   single research doc — treat as indicative, not established fact.
10. Testing-category depth: only Semgrep + Assurly as servers; dedicated
    testing-framework MCP servers (if any) not found.

### Limitations of this workstream

- No live browser; no servers installed or executed. All capability claims come
  from READMEs, docs, and registry metadata — advertised, not exercised.
  `tools/list` output was never observed firsthand.
- Several vendor repos (stripe/agent-toolkit, brave/brave-search-mcp-server,
  awslabs/mcp sub READMEs except aws-documentation, supabase, neon) were
  reached via mirrors/secondary docs rather than the canonical README; those
  records are capped at Partially verified.
- Search-result text is a lossy proxy for full pages; exact tool parameter
  lists should be re-checked against primary sources before operational use.
- The ecosystem moves fast (weekly scraper updates, new spec revisions);
  counts (registry sizes, star counts) are point-in-time (2026-10-10).
