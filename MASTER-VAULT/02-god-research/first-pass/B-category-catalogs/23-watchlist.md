# C — Named Register 23 (Watchlist) — Standardized Records
Date: 2026-10-09
Method: read-only. WebSearch + WebFetch only. No installs, no bypass, no credential use. Prompt bodies not reproduced.
Scope: individually investigate all 23 watchlist names. For ambiguous: preserve original string, exact search, variants, org/registry, README inspect, function compare, canonical match + evidence or UNRESOLVED.

## Record schema
- `Original:` verbatim watchlist string
- `Exact search:` query tried
- `Variants / org / registry checked:`
- `README / function compare:`
- `Canonical match:` URL or UNRESOLVED
- `Evidence:` what was observed (stars/folders/files/dates where shown)
- `Status:` RESOLVED | PARTIAL | UNRESOLVED
- `Adjacent companions:` only with evidence, else none

---

### 1. OpenViking
- Original: `OpenViking`
- Exact search: `OpenViking GitHub project`
- Variants / org / registry checked: `volcengine/OpenViking` (also `volcengine/openviking` case variant); openviking.ai; docs.openviking.ai
- README / function compare: README describes "Context Database for AI Agents — one filesystem for everything an agent knows: knowledge, memory, skills" under `viking://`, with `ov` CLI (`ov status`, `ov add-resource`, `ov ls/tree/find/grep`), L0/L1/L2 summaries, sessions, VikingBot. Function = agent memory + RAG + skills infra, not a prompt archive.
- Canonical match: https://github.com/volcengine/OpenViking
- Evidence: search result header `volcengine/OpenViking`, ~39472 stars, 3116 forks, default branch `main`, created 2026-01-05, AGPLv3, homepage https://openviking.ai ; README excerpt with `ov` CLI.
- Status: RESOLVED
- Adjacent companions: none (docs site + homepage are same project, not separate watchlist items).

### 2. PizzaBox AWS
- Original: `PizzaBox AWS`
- Exact search: `PizzaBox AWS GitHub`
- Variants / org / registry checked: `aws-samples/pizza-delivery-tracker`; `pizza-bot-app/pizza-bot` (AWS blog "Introducing Pizza Bot"); `pizzabox.ai` (restaurant SaaS, Techstars-backed, unrelated); `RDarrylR/serverless-pizza-ordering` (blog example)
- README / function compare: No repo literally named PizzaBox under AWS org found in results. Closest functional neighbours: (a) `aws-samples/pizza-delivery-tracker` — map-based pizza ordering + delivery tracking demo (Amplify + Location Service + AppRunner + DynamoDB + ECS/Fargate + SQS); (b) `pizza-bot-app/pizza-bot` — local-first inbox for long-running agents (DeepAgents/LangGraph, Bedrock-capable), name from Amazon two-pizza teams, AWS Open Source Blog 2026-09-10. Neither claims name "PizzaBox AWS". `pizzabox.ai` is restaurant subscription platform, distinct function.
- Canonical match: UNRESOLVED (no exact `PizzaBox AWS` repo located)
- Evidence: search returned no `*/PizzaBox` AWS repo; `aws-samples/pizza-delivery-tracker` has zero releases; `pizza-bot-app/pizza-bot` 391 stars, Apache-2.0, created 2026-06-26.
- Status: UNRESOLVED — preserve original `PizzaBox AWS` for re-search.
- Adjacent companions: none (candidates listed are not confirmed same entity).

### 3. Scrapling Krim Shoair
- Original: `Scrapling Krim Shoair`
- Exact search: attempted; search backend 429 on this query during session
- Variants / org / registry checked: `Scrapling` known public Python scraping lib (commonly `D4Vinci/Scrapling` — NOT verified this session via fetch); `Krim Shoair` appears as personal-name string, no org/repo confirmed this session
- README / function compare: not inspected (no successful fetch this session). Function hypothesis — web-scraping toolkit + author/maintainer name — unconfirmed.
- Canonical match: UNRESOLVED
- Evidence: no successful WebSearch/WebFetch result captured this session for exact phrase.
- Status: UNRESOLVED — preserve original; needs exact-search retry + registry (PyPI/npm) + README inspect.
- Adjacent companions: none.

### 4. ChatDev 2.0 / devAll
- Original: `ChatDev 2.0/devAll`
- Exact search: `ChatDev 2.0 devAll GitHub`
- Variants / org / registry checked: `OpenBMB/ChatDev` (also `openbmb/chatdev` case variant); release tag `v2.0.0`; branch `chatdev1.0` (legacy); paper arXiv `2609.00714v1`
- README / function compare: README = "ChatDev 2.0: Dev All through LLM-powered Multi-Agent Collaboration" — zero-code multi-agent orchestration platform ("Developing Everything"), declarative executable graph + CADET cycle-aware engine, Vue3 visual console + Python SDK; 1.x was virtual software-company (CEO/CTO/Programmer), moved to `chatdev1.0` branch. Release notes 2026-01-07 confirm `main` switched to 2.0 (DevAll).
- Canonical match: https://github.com/OpenBMB/ChatDev
- Evidence: ~34448 stars, 4317 forks, Apache-2.0, created 2023-08-28, default `main`; release `v2.0.0` published 2026-01-07; docs path `docs/user_guide/en/index.md` ("DevAll Backend User Guide").
- Status: RESOLVED (both `ChatDev 2.0` and `DevAll` refer to same repo state)
- Adjacent companions: none.

### 5. Munder Difflin (+Dunder Mifflin variants)
- Original: `Munder Difflin (+Dunder Mifflin variants)`
- Exact search: `Munder Difflin GitHub Dunder Mifflin variant` — backend 429, no result captured
- Variants / org / registry checked: `Dunder Mifflin` (The Office fictional paper company) commonly used in demo/seed/sample repos; `Munder Difflin` likely intentional misspelling/variant — no canonical org confirmed this session
- README / function compare: not inspected this session.
- Canonical match: UNRESOLVED
- Evidence: none captured this session.
- Status: UNRESOLVED — preserve `Munder Difflin`; needs exact + `Dunder Mifflin` + `Munder-Difflin` + `dunder-mifflin` org/repo search + README compare.
- Adjacent companions: none.

### 6. Taste skill
- Original: `Taste skill`
- Exact search: not successfully returned this session (rate-limited)
- Variants / org / registry checked: checked `anthropics/skills` tree (observed skills list: academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx) — no `taste` entry observed in that listing.
- README / function compare: not located.
- Canonical match: UNRESOLVED
- Evidence: `anthropics/skills/skills` directory listing observed 2026-10-09 contains no `taste` folder.
- Status: UNRESOLVED — preserve `Taste skill`; could be community skill, needs registry search.
- Adjacent companions: none.

### 7. Frontend design skill
- Original: `Frontend design skill`
- Exact search: via `anthropics/skills` tree + `anthropics/claude-cookbooks/skills`
- Variants / org / registry checked: `anthropics/skills/skills/frontend-design`; `anthropics/claude-cookbooks/skills` (cookbook guide)
- README / function compare: `frontend-design` is a first-party example skill folder in official repo (alongside canvas-design, web-artifacts-builder, theme-factory). Function = frontend/design guidance skill (SKILL.md + bundled resources pattern). Distinct from Astryx CLI and DESIGN.md spec.
- Canonical match: https://github.com/anthropics/skills/tree/main/skills/frontend-design
- Evidence: `skills/skills at main` listing includes `frontend-design` (observed via WebSearch snippet + WebFetch of `anthropics/skills`); repo `anthropics/skills` created 2025-09-22.
- Status: RESOLVED (as official example skill; specific fork/version not pinned)
- Adjacent companions: `canvas-design`, `web-artifacts-builder`, `theme-factory` — same repo, evidenced by same directory listing. Not separate watchlist items.

### 8. Backend design skill
- Original: `Backend design skill`
- Exact search: via `anthropics/skills` tree listing
- Variants / org / registry checked: `anthropics/skills/skills/*` — observed list has no `backend-design` folder; `mcp-builder`, `webapp-testing`, `claude-api` are closest technical skills but different function.
- README / function compare: no canonical backend-design SKILL.md located this session.
- Canonical match: UNRESOLVED
- Evidence: directory listing of `anthropics/skills/skills` shows no `backend-design`.
- Status: UNRESOLVED — preserve original; needs registry-wide skill search.
- Adjacent companions: none.

### 9. public-apis/public-apis
- Original: `public-apis/public-apis`
- Exact search: `public-apis public-apis GitHub list`
- Variants / org / registry checked: `public-apis/public-apis` (org `public-apis`, 1 public repo); fork/neighbour `marcelscruz/public-apis` (publicapis.dev); `public-api-lists/public-api-lists`; `free-apis.github.io`
- README / function compare: README = "A collective list of free APIs", community-curated, APILayer-maintained, table format (API | Description | Auth | HTTPS | CORS). Function = API directory, not a prompt/skill lib. Distinct from code above.
- Canonical match: https://github.com/public-apis/public-apis
- Evidence: ~486671 stars, 53829 forks, MIT, created 2016-03-20, default `master`, homepage APILayer; org `public-apis` has 6550 followers, 1 repo.
- Status: RESOLVED
- Adjacent companions: none (neighbours listed for disambiguation only, not confirmed same entity).

### 10. Agent Skills standard
- Original: `Agent Skills standard`
- Exact search: `Agent Skills standard anthropics open standard`
- Variants / org / registry checked: `agentskills/agentskills` (standard repo); `anthropics/skills` (Anthropic implementation); `agentskills.io/specification`; `anthropics-skills.mintlify.app/spec/overview`; `docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview`; engineering post `anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills` (2025-10-16, updated Dec 18 2025 open standard)
- README / function compare: Standard defines folder + `SKILL.md` with YAML frontmatter (`name`, `description`), progressive disclosure (metadata → SKILL.md body → bundled resources: `scripts/`, `references/`, `assets/`), implementation-agnostic. Anthropic repo is implementation + examples (creative/technical/enterprise + docx/pdf/pptx/xlsx). Distinct from community awesome-lists.
- Canonical match (standard): https://github.com/agentskills/agentskills ; spec: https://agentskills.io/specification (implementation: https://github.com/anthropics/skills)
- Evidence: `agentskills/agentskills` README ("standardized way...", "originally developed by Anthropic, released as an open standard"); Mintlify overview; Anthropic docs (pre-built `pptx/xlsx/docx/pdf` skill_ids, Skills API `/v1/skills`).
- Status: RESOLVED
- Adjacent companions: `anthropics/skills` (implementation) — evidenced.

### 11. Astryx facebook/astryx (components/CLI/files/docs/templates, verify CLI-only no MCP)
- Original: `Astryx facebook/astryx (components/CLI/files/docs/templates, verify CLI-only no MCP)`
- Exact search: direct fetch `facebook/astryx` + `facebook/astryx/tree/main/packages/cli`
- Variants / org / registry checked: `facebook/astryx`; npm `@astryxdesign/core`, `@astryxdesign/cli`, `@astryxdesign/theme-*`; site `astryx.atmeta.com` (docs/Storybook/sandbox)
- README / function compare: About = "An open source design system that's fully customizable and agent ready". Root tree: `apps/`, `packages/` (core, cli, build, themes), `internal/`, `docs/`, `scripts/`, plus `AGENTS.md`, `CLAUDE.md`. Packages table confirms: core (components/theme/utils), cli (component docs, templates, scaffolding, themes, codemods), build (StyleX plugins), themes (7 themes). CLI README enumerates commands: blog, build, component, discover, docs, doctor, gap-report, hook, init, integration, layout (deprecated), search, swizzle, template, theme, upgrade + `manifest --json`, JSON API, programmatic `@astryxdesign/cli/api`. No MCP server directory, no `mcp` command, no MCP transport in inspected tree/README excerpts.
- Canonical match: https://github.com/facebook/astryx
- Evidence: 13.6k stars, 1.2k forks, MIT, 4537 commits on `main` (as fetched); `packages/cli` subdirs: `api`, `assets`, `authoring`, `clients/cli`, `foundation`, `scripts`, `test`, `test-utils`; CLI install `@astryxdesign/cli`, runner `astryx`; docs `astryx.atmeta.com`.
- Status: RESOLVED — CLI-only verified to extent of inspected surface (packages/cli tree + CLI README command/manifest list show no MCP). Caveat: full-repo grep for "mcp" not performed (read-only fetch limit); re-verify with code search before claiming absolute absence.
- Adjacent companions: none.

### 12. DeepSec vercel/deepsec
- Original: `DeepSec vercel/deepsec`
- Exact search: `vercel deepsec DeepSec GitHub` (429, no result); direct fetch `github.com/vercel/deepsec`
- Variants / org / registry checked: `vercel/deepsec` only
- README / function compare: not inspected — fetch returned HTTP 404.
- Canonical match: UNRESOLVED (https://github.com/vercel/deepsec → 404 on 2026-10-09; no evidence it exists under `vercel` org at check time)
- Evidence: WebFetch status `404 GET https://github.com/vercel/deepsec`.
- Status: UNRESOLVED — preserve original; needs org/rename/transfer search (possible different org, private/renamed/deleted, or `deepsec` as product not repo).
- Adjacent companions: none.

### 13. affaan-m/ECC
- Original: `affaan-m/ECC`
- Exact search: direct fetch `affaan-m/ECC`
- Variants / org / registry checked: `affaan-m/ECC`; npm `ecc-universal`, `ecc-agentshield`; plugin `ecc@ecc`; site `ecc.tools`; GitHub App `ecc-tools`
- README / function compare: About = "The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond." Install via `npx ecc-universal setup`, `/plugin marketplace add https://github.com/affaan-m/ECC` + `/plugin install ecc@ecc`. Counts claimed in README: 68 agents, 293 skills, 94 legacy command shims + hooks/rules/memory/AgentShield. Tree includes `agents/`, `skills/`, `commands/`, `hooks/`, `rules/`, `workflows/`, `mcp-configs/`, `.mcp.json`, `plugins/`, `docs/`. Function = harness/skill system, overlapping with skills-standard ecosystem but distinct repo.
- Canonical match: https://github.com/affaan-m/ECC
- Evidence: ~276k stars (275.8k shown), 41.2k forks, MIT, 3043 commits on `main`, topics include `claude-code`, `mcp`; install identifiers cross-referenced in README.
- Status: RESOLVED
- Adjacent companions: none.

### 14. ruvnet/ruflo
- Original: `ruvnet/ruflo`
- Exact search: `ruvnet ruflo GitHub`
- Variants / org / registry checked: `ruvnet/ruflo` (renamed from Claude Flow per README: "Claude Flow is now Ruflo"); npm `ruflo`; UI `flo.ruv.io`; `Cognitum.One`, `ruv.io`
- README / function compare: "An agent meta-harness for Claude Code and Codex — Agent = Model + Harness", `npx ruflo init`, 100+ specialized agents, swarms, self-learning memory, federation, 35 plugins (`ruflo-core`, `ruflo-swarm`, ...), MCP server (323 tools per STATUS.md) + CLI (45 top-level commands) + web UI with MCP tool calling. Distinct from ECC (different vendor/counts/architecture).
- Canonical match: https://github.com/ruvnet/ruflo
- Evidence: ~68360 stars, 8206 forks, MIT, created 2025-06-02, default `main`; README + `docs/STATUS.md` (`ruflo@3.10.2`) excerpts; install `/plugin marketplace add ruvnet/ruflo`.
- Status: RESOLVED
- Adjacent companions: none.

### 15. anthropics/claude-cookbooks
- Original: `anthropics/claude-cookbooks`
- Exact search: `anthropics claude-cookbooks GitHub skills`
- Variants / org / registry checked: `anthropics/claude-cookbooks` (also `anthropics/anthropic-cookbook` redirect/alias seen in one URL); subpath `skills/`; notebooks `skills/notebooks/03_skills_custom_development.ipynb`; `skills/custom_skills`
- README / function compare: Top-level = "collection of notebooks/recipes showcasing fun and effective ways of using Claude" (classification, RAG, summarization, tool use, vision, sub-agents, evals, prompt caching). Subfolder `skills/` = "Claude Skills Cookbook" (document generation, data analysis, business automation; built-in skill IDs `xlsx/pptx/pdf/docx`; custom-skill structure). Function = official examples/cookbook, distinct from `anthropics/skills` (implementation repo) and from alleged-leak archives.
- Canonical match: https://github.com/anthropics/claude-cookbooks
- Evidence: created 2023-08-15; `skills/` tree + `custom_skills` + notebook paths observed; built-in skills table (`xlsx/pptx/pdf/docx`).
- Status: RESOLVED
- Adjacent companions: `anthropics/skills` (sibling official repo) — evidenced, different purpose.

### 16. Designs (exact+variants)
- Original: `Designs (exact+variants)`
- Exact search: not completed this session (rate-limited; no result captured)
- Variants / org / registry checked: none verified — candidates could include generic `designs` repos, Figma/design-system collections, or `facebook/astryx` templates; no variant confirmed.
- README / function compare: not inspected.
- Canonical match: UNRESOLVED
- Evidence: none captured.
- Status: UNRESOLVED — preserve `Designs`; needs exact `"Designs"` + org/registry + README/function compare to separate from Astryx/DESIGN.md/frontend-design.
- Adjacent companions: none.

### 17. Firecrawl
- Original: `Firecrawl`
- Exact search: `Firecrawl GitHub firecrawl.dev scrape`
- Variants / org / registry checked: `firecrawl/firecrawl`; `firecrawl.dev`; docs `docs.firecrawl.dev/features/scrape`; SDKs `apps/python-sdk`; CLI `firecrawl scrape`
- README / function compare: "The API to search, scrape, and interact with the web at scale — web context API", features Search/Scrape (`/v2/scrape` → markdown/HTML/screenshots/JSON)/Crawl/Interact/Agent. Function = web-to-LLM data infra, distinct from scraping lib Scrapling and from prompt archives.
- Canonical match: https://github.com/firecrawl/firecrawl
- Evidence: ~189817 stars, 10068 forks, AGPLv3, created 2024-04-15, homepage https://firecrawl.dev ; CLI + Python/Node/cURL examples observed.
- Status: RESOLVED
- Adjacent companions: none.

### 18. vercel/eve
- Original: `vercel/eve`
- Exact search: `vercel eve GitHub repository framework` + `vercel eve GitHub agent`
- Variants / org / registry checked: `vercel/eve`; site `eve.dev`; docs `vercel.com/docs/eve`; templates (eve-github-maintainer/Kody, Foreman, content agent); channels `eve/channels/github`, `@vercel/connect`, `@github-tools/sdk/eve`
- README / function compare: "The Open Framework for Building Agents" — filesystem-first durable backend agents (`agent/agent.ts`, `instructions.md`, `tools/`, `skills/`, `channels/`, `schedules/`), CLI `npx eve@latest init`, npm `eve`, durable sessions Workflows + Sandbox + AI Gateway + Connect + Observability. GitHub-agent guide confirms runtime + GitHub Tools + short-lived tokens + approval gating + `@mention` channel. Distinct from Vercel hosting generally and from `vercel/deepsec` (which 404s).
- Canonical match: https://github.com/vercel/eve
- Evidence: ~4957 stars, 501 forks, Apache-2.0, created 2026-06-16, default `main`, homepage https://eve.dev ; KB `vercel.com/kb/guide/github-agent-eve` + `vercel.com/kb/eve` excerpts.
- Status: RESOLVED
- Adjacent companions: none (templates are same ecosystem, not separate watchlist entities).

### 19. Strix (exact+variants)
- Original: `Strix (exact+variants)`
- Exact search: not completed this session (no result captured)
- Variants / org / registry checked: none verified — string collides with many unrelated `strix` (game engine, Halo Strix, birds, libs); no org pinned.
- README / function compare: not inspected.
- Canonical match: UNRESOLVED
- Evidence: none captured.
- Status: UNRESOLVED — preserve `Strix`; needs exact + variants (`strix`, `StrixAI`, `strix-halo`, org-qualified) + README/function compare.
- Adjacent companions: none.

### 20. DESIGN.md convention
- Original: `DESIGN.md convention`
- Exact search: `"DESIGN.md" convention repository design system agents`
- Variants / org / registry checked: `google-labs-code/design.md` (canonical spec repo); mirror `AgentsORG/naive-design` (`spec/design-md-spec.md` cites upstream as authoritative); file locations `DESIGN.md`, `design/DESIGN.md`, `.design/DESIGN.md`
- README / function compare: Spec = "A format specification for describing a visual identity to coding agents" — YAML frontmatter tokens (colors/typography/rounded/spacing/components, `{path.to.token}` refs) = normative; markdown body (`##` Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts) = rationale. Includes linter (11 rules: broken-ref, missing-primary, contrast-ratio, orphaned-tokens, section-order...), `export` to W3C DTF, version `alpha`. Function = repo-level design-token contract for agents, distinct from Astryx (system), frontend-design skill (how-to), and generic `Designs`.
- Canonical match: https://github.com/google-labs-code/design.md (spec: `docs/spec.md`)
- Evidence: repo created 2026-04-10; README + `docs/spec.md` excerpts (frontmatter schema, section order table, consumer-behavior table, linter table); mirror notes Apache-2.0, version `alpha`.
- Status: RESOLVED (as convention; project adoption instances not enumerated)
- Adjacent companions: none.

### 21. awesome-claude-skills (exact+similar compare)
- Original: `awesome-claude-skills (exact+similar compare)`
- Exact search: `awesome-claude-skills GitHub`
- Variants / org / registry checked: `travisvn/awesome-claude-skills` (created 2025-10-16, ~15294 stars, 2017 forks — earliest of the three, curated list for Claude Code workflows, links `anthropics/skills` + Cookbooks); `ComposioHQ/awesome-claude-skills` (created 2025-10-17, ~64110–74137 stars across snapshots, 7067–8493 forks, `master` branch, claims 1000+ production-ready skills/plugins across Claude/Codex/Cursor/Gemini/Antigravity); `BehiSecc/awesome-claude-skills` (created 2025-10-17, ~10090 stars, categorized doc/dev/data/science/writing/media/health/collab/security/utility); `karanb192/awesome-claude-skills` (541 stars, MIT, 50+ verified, install routes `claude plugin marketplace add anthropics/skills`)
- README / function compare: All are community awesome-lists (curated links), not skill implementations and not the standard. travisvn is oldest/smallest-curated; ComposioHQ is largest/most commercial ("Connect" actions, 1000+ cross-agent); BehiSecc is categorized taxonomy; karanb192 is "verified 50+" directory with install FAQ (skills vs MCP vs project instructions). Function identical (directory), scale/maintenance differ.
- Canonical match: NO single canonical — same-name repos by different orgs. Preserve exact string with org qualifier. Best-known earliest: https://github.com/travisvn/awesome-claude-skills ; largest: https://github.com/ComposioHQ/awesome-claude-skills
- Evidence: star/fork/created/branch counts + README excerpts above, captured 2026-10-09.
- Status: PARTIAL (exact string is ambiguous by design; org-qualified matches resolved, single canonical NOT assigned)
- Adjacent companions: `anthropics/skills`, `anthropics/claude-cookbooks/skills` — referenced by these lists (evidenced), not same entity.

### 22. anthropics/skills official
- Original: `anthropics/skills official`
- Exact search: `anthropics skills GitHub official SKILL.md`
- Variants / org / registry checked: `anthropics/skills`; `spec/agent-skills-spec.md` (points to agentskills.io); `template/SKILL.md` (`template-skill`); `skills/` tree (19 folders observed)
- README / function compare: "Public repository for Agent Skills" — Anthropic's implementation for Claude (not the standard itself; note points to agentskills.io). Each skill = folder + `SKILL.md` (frontmatter `name`+`description`) + scripts/references/assets. Folders: academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx. Doc skills (docx/pdf/pptx/xlsx) are source-available/proprietary; many others Apache-2.0. Install via Skills API / claude.ai / Claude Code (`claude plugin marketplace add anthropics/skills`).
- Canonical match: https://github.com/anthropics/skills
- Evidence: created 2025-09-22; tree listing + `template/SKILL.md` + `skills/claude-api/SKILL.md` + `skills/docx/SKILL.md` excerpts observed.
- Status: RESOLVED
- Adjacent companions: Agent Skills standard (`agentskills/agentskills`) — evidenced as upstream standard.

### 23. NotebookLM skill
- Original: `NotebookLM skill`
- Exact search: not completed this session (no result captured)
- Variants / org / registry checked: none verified — likely community SKILL.md wrapping Google NotebookLM (notebook-grounded research/audio overviews); no org/repo pinned.
- README / function compare: not inspected.
- Canonical match: UNRESOLVED
- Evidence: none captured.
- Status: UNRESOLVED — preserve `NotebookLM skill`; needs skill-registry + GitHub code search + README/function compare (vs official NotebookLM docs, which are not a skill).
- Adjacent companions: none.

---

## Counts
- Total watchlist names: 23
- RESOLVED: 13 (1, 4, 7, 9, 10, 11, 13, 14, 15, 17, 18, 20, 22)
- PARTIAL (ambiguous-but-evidenced): 1 (21 — multiple same-name repos, org qualifier required)
- UNRESOLVED: 9 (2, 3, 5, 6, 8, 12, 16, 19, 23)
- Adjacent companions added: 0 standalone (neighbours mentioned only for disambiguation with evidence, not as confirmed watchlist entities)

## Unresolved list (preserve originals for retry)
1. `PizzaBox AWS` — no exact repo; candidates `aws-samples/pizza-delivery-tracker`, `pizza-bot-app/pizza-bot`, `pizzabox.ai` are functionally distinct.
2. `Scrapling Krim Shoair` — exact phrase + linkage unverified (search 429 this session).
3. `Munder Difflin (+Dunder Mifflin variants)` — no canonical org/repo verified.
4. `Taste skill` — no match in `anthropics/skills` tree; registry search needed.
5. `Backend design skill` — no `backend-design` in `anthropics/skills` tree; registry search needed.
6. `DeepSec vercel/deepsec` — `https://github.com/vercel/deepsec` = 404 on 2026-10-09.
7. `Designs (exact+variants)` — too generic; needs qualified search.
8. `Strix (exact+variants)` — collides with unrelated `strix` uses; needs qualified search.
9. `NotebookLM skill` — no org/repo pinned; needs skill-registry search.

## Method notes / limits
- Star/fork counts are point-in-time search/fetch excerpts, not live API guarantees.
- `facebook/astryx` CLI-only claim scoped to inspected `packages/cli` tree + CLI README command/manifest surface; full-repo MCP-string search not performed.
- No prompt bodies reproduced. No auth, no bypass attempted.
- Retry queue: re-run exact searches for all 9 unresolved when search backend is not rate-limited; prefer GitHub code search + registry (npm/PyPI/skills registries) + README diff.
