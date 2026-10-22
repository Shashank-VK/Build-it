# Deliverable G — Resource Relationship Index
**The Omniscient Resource Atlas · Built 2026-10-10**

Forks, successors, renames, companion repositories, and tool↔skill↔framework↔protocol relationships. Only evidenced relationships are listed; name collisions are called out as **not** relationships.

## G1. Renames and successor chains (one canonical record each)

| From | To | Relationship | Evidence |
|---|---|---|---|
| Claude Flow | **ruvnet/ruflo** | Renamed successor ("Claude Flow is now Ruflo — named by rUv"; Cognitum.One engine) | Watchlist #14, 2026-10-10 |
| gsd-build/get-shit-done | **open-gsd/gsd-core** | Safe community fork (original archived June 2026, security concerns; do NOT use original) | Phase-0, re-confirmed 2026-10-10 |
| "Everything Claude Code" | **affaan-m/ECC** | Official rename (Oct 2026); plugin id `ecc@ecc`, npm `ecc-universal` — three non-interchangeable identifiers | Watchlist #13 |
| Gemini CLI | **Antigravity CLI (`agy`)** | Google successor; consumer Gemini CLI serving ended 2026-06-18 | 03b-agents (Google Developers Blog) |
| Windsurf / Cascade | **Devin Desktop** | Rebrand; `.devin/rules/` preferred | 03b-agents (primary docs) |
| Kimi CLI | **Kimi Code CLI** (MoonshotAI/kimi-code, MIT) | Legacy alias | 03b-agents |
| Gitpod | **Ona** | OpenAI acquisition Jun 2026; Gitpod Classic sunset 2026-10-15 | 06b-quality |
| Microsoft AutoGen | **AG2 / Microsoft Agent Framework** | Successor chain; AutoGen in maintenance mode (README banner) | 05a-orchestration |
| IBM ACP | **A2A** | Merged Aug 2025; ACP archived | 05a-orchestration |
| vercel/deepsec | **vercel-labs/deepsec** | Org correction (Vercel Labs) | Watchlist #12 |
| tsup | **tsdown** | 2026 succession in TS build tooling | 01a-languages-build |
| Rye | **uv** | 2026 succession in Python packaging | 01a-languages-build |
| Volta | **mise** | 2026 succession in toolchain management | 01a-languages-build |
| mcp-scan | **Snyk Agent Scan** | Renamed | 06b-quality |
| Opencode-DCP (opencode-dynamic-context-pruning) | **"Sleev"** | Successor per README; DCP in maintenance mode | Phase-0 |
| DS4SD (docling org) | **docling-project** | Org moved under LF AI & Data Foundation | 06a-data-acquisition |
| Scrapinghub | **Zyte** | Company rename | 06a-data-acquisition |
| ScrapingBee | **Oxylabs** group | Joined Jan 2026 | 06a-data-acquisition |
| Cal.com (open-source) | **cal.diy** (MIT fork) | Cal.com closed-source 2026-04-14; community fork | 01c-backend-data-platforms |
| Auth.js | **Better Auth** | Migration recommendation | 01c-backend-data-platforms |
| Stytch | **Twilio** | Acquired ($104.1M, closed 2025-11-14) | 01c-backend-data-platforms |
| Lemon Squeezy | **Stripe** | Acquired → folding into Stripe Managed Payments | 01c-backend-data-platforms |
| Payload CMS | **Figma** | Acquired June 2025 | 01c-backend-data-platforms |
| Langfuse | **ClickHouse** | Acquired Jan 2026 | 06c-operations |
| Statsig | **OpenAI → Amplitude** | Acquisition chain; Amplitude brand takeover | 06c-operations |
| Intercom | **Fin** | Rebrand; Salesforce acquisition pending | 06c-operations |
| Deno (team) | **Cloudflare** | Team move; Deno Deploy sunsets ~Apr 2027; runtime 1yr maintenance | 06c-operations |
| Lost Pixel | **Figma** | Sunsetting into Figma | 02a/06b |
| promptfoo | **OpenAI** | "Promptfoo is now part of OpenAI" per README; remains MIT | prompt-archives R18 |

## G2. Companion and dependency relationships

- **Agent Skills standard**: `agentskills/agentskills` (spec repo) → `agentskills.io` (docs site) → `anthropics/skills` (reference implementation + `spec/` + `template/` + `skill-creator`) → vendor skill repos (vercel-labs, supabase, stripe, expo, angular, cloudflare, hashicorp, getsentry, huggingface, neondatabase, netlify, microsoft, openai/plugins) → `skills.sh` / `vercel-labs/skills` CLI (install tooling) → validators (`fchastanet/ai-linter`, `spiritualhost/clinter`, `google/skills_lint.dart`) → marketplaces (`Agent Skill Exchange`, `trailofbits/skills`).
- **anthropics/skills `frontend-design`** → widely mirrored (idwong/dev-skills, evolve, dotfiles, turbo, skills-registry copies) — mirrors, not forks of record.
- **ngmeyer/council-review** ↔ **ngmeyer/skills** — parallel repos (standalone council skill vs personal monorepo); both live.
- **KanakMalpani/Loop-Engineering** (framework) vs **KanakMalpani/LoopBench** (benchmark suite) — same author, separate projects, not versions of each other.
- **teng-lin/notebooklm-py** (unofficial library) → **stefandsl/notebooklm-skill** (skill built on top of it).
- **facebook/astryx** → `@astryxdesign/cli` + `@astryxdesign/core` + `@astryxdesign/build` + `@astryxdesign/theme-*` (npm packages); agent surface = CLI only.
- **shadcn/ui** → official remote MCP (`shadcn.io/api/mcp`) + community `@jpisnice/shadcn-ui-mcp-server`.
- **OpenAPI specs** → `cnoe-io/openapi-mcp-codegen` / `awslabs/openapi-mcp-server` → MCP servers consumable by any MCP client (the DIY "backend Astryx" pattern).
- **google-labs-code/design.md** (spec + CLI) → `VoltAgent/awesome-design-md` (73+ brand files) → `getdesign.md` (300+ reverse-engineered files); consumer skills: `hermes-design-md`, `design-md-author`, `design-md-visual-system`, anthropics `design-system` skill.
- **Prompt-archive upstream flow**: original extractions concentrate in `elder-plinius/CL4R1T4S` → mirrored/repackaged by `asgeirtj/system_prompts_leaks`, `x1xhlol/system-prompts-and-models-of-ai-tools`, `moirania/openai-system-prompts`, `thekishandev/ai-system-prompt`, `gitjfmd/prompt-hub` → indexed by `4pixeltechbr/promptograph`. `asgeirtj`'s `Anthropic/Official/` subfolder archives Anthropic's own release-notes page (provenance-clean). `Piebald-AI/claude-code-system-prompts` is independent (script-extracted from the public npm package). `eonedgeproject-code/the-brief` tags entries by acquisition method.
- **Munder Difflin**: canonical `jeffreycayao/munder-difflin`; forks `cartychris/munder-difflin`, `chaitanyagiri/munder-difflin`; related blog `gulum/munder-difflin`.
- **Pizza Bot**: `pizza-bot-app/pizza-bot` — community project (not AWS-supported); announced via AWS Open Source Blog Sept 2026.
- **Taste Skill**: `Leonxlnx/taste-skill` (design-taste skills) → companion product **TasteCode** (tastecode.dev, separate desktop workspace).
- **OpenCode prior catalog (163 resources)**: mega-harness `code-yeongyu/oh-my-openagent` appears across 5+ elements; `kdcokenny/opencode-workspace` spans permissions + agents; `deliberation` plugin bridges multi-model consensus via MCP; `boxpositron/envsitter-guard` and `remorses/opencode-injection-guard` are complementary guard layers.
- **Context/memory**: `upstash/context7` (docs MCP) is cross-referenced by context, skills, and agent catalogs — one canonical record.
- **Firecrawl**: repo `firecrawl/firecrawl` (AGPL-3.0) → hosted service (firecrawl.dev) + self-host (Docker) + `firecrawl-mcp` + `firecrawl-cli` + skill dirs.

## G3. Name collisions — NOT the same project (do not merge)

| Name A | Name B | Why they are distinct |
|---|---|---|
| `alibaba/open-code-review` | `spencermarx/open-code-review` | Different orgs; Alibaba's is OpenCode-compatible, Spencer Marx's is Claude-Code-only |
| `Leonxlnx/taste-skill` (design taste) | `sprungundlandung/taste-skill`, `lamwon/taste-skill` (reverse-engineer any site's taste) | Different authors, different functions |
| `usestrix/strix` (AI pentest tool) | `strixgov/strix` (agent execution-control), `strixproject/Strix` (pentest assistant), `mythicalsign/strix` (fork) | Four distinct projects sharing a name |
| `ComposioHQ/awesome-claude-skills` | `jculberson/`, `arturayupov/`, `travisvn/`, `BehiSecc/`, `mingrath/` awesome-claude-skills | Same repo name, distinct repos (dominant: ComposioHQ, ~76k stars) |
| `jbeck018/agents-opencode` | OpenCode agent collections | Misleading name — actually a Claude Code fork (wshobson/agents); excluded |
| `dgtlmoon/changedetection.io` | 5 same-name forks | Upstream is dgtlmoon; forks are separate |
| `coderamp-labs` Gitingest | 2 same-name forks | Canonical is coderamp-labs (ex-cyclotruc) |
| Serena (GPL-3.0) | secondary sources claiming MIT | License discrepancy — primary README read wins (G3 license note in H) |
