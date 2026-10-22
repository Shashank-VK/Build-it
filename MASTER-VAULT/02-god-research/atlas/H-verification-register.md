# Deliverable H — Verification and Discrepancy Register
**The Omniscient Resource Atlas · Built 2026-10-10**

Everything that could not be verified, was corrected, contradicts, or carries a warning. Preserved here so no uncertainty is silently resolved in the catalogs.

## H1. Unverified names (no canonical match established)

| Name as supplied | What was searched | Finding |
|---|---|---|
| `okjpg/llm-council` | GitHub handle + repo; karpathy/llm-council fork network | No public repo under this handle. Likely a voice-to-text distortion. Provide exact URL to resolve |
| "Designs" (watchlist #16) | Exact string; plausible related names | Too generic — no match. Plausible leads (anthropics `canvas-design`, taste-skill variants, awesome-design-md) cannot be tied to the bare name |
| "Backend design skill" (watchlist #8) | Exact string; 5 author implementations found | Genuinely ambiguous — 5 distinct projects, no canonical match. Candidates: ainnaziha/claude-atelier, keyvaluesoftwaresystems/kv-skills, firdausmntp/techneuma, majiayu000/claude-skill-registry, xsefirosus/sefi-agents |
| "Taste skill" variants | sprungundlandung/lamwon/taste-skill | Different project from Leonxlnx/taste-skill (reverse-engineers site taste vs design-taste enforcement) — recorded, not merged |
| Strix (watchlist #19) | Exact + variant names | Primary candidate usestrix/strix (AI pentest, 67k stars, Wikipedia article) — Partially verified; 3 alternatives recorded |
| Frontend design skill (watchlist #7) | Exact string | Partially verified — canonical candidate anthropics/skills `frontend-design`, verified only via mirrors, not on the canonical tree |
| R-60 Cover-Agent | — | Unverified in testing sweep; needs primary pass |
| Baton (mraza007), shire/tutti/opengoat | Curated-list claims | OpenCode support claimed but unverified |
| K-Dense-AI/science-superpowers | — | OpenCode path unverified |
| leohuang8688/self-improving-agent | — | OpenClaw-only; OpenCode path unverified |
| Nia (27% perf claim), Deepcon (90% vs 65% claim) | — | Self-reported metrics, unverified |
| labac-dev/cursor-system-prompts | Repo stats/license/activity | Metadata not captured — Unresolved |

## H2. Corrected identities (use the corrected form)

| Original (wrong/distorted) | Corrected | Evidence |
|---|---|---|
| "ruflo" | **ruvnet/ruflo** (formerly Claude Flow) | 00-verification.md (2026-08-09); watchlist #14 (2026-10-10) |
| "enilkowaski apple designs skill" | **emilkowalski/skills** | 00-verification.md |
| "Krim Shoair" | **Karim Shoair** (GitHub D4Vinci) | Watchlist #3 |
| "PizzaBox by AWS" | **Pizza Bot** (pizza-bot-app/pizza-bot; AWS Open Source Blog, Sept 2026) | Watchlist #2 |
| "Everything Claude Code" | **affaan-m/ECC** (name retired; plugin `ecc@ecc`, npm `ecc-universal`) | Watchlist #13 |
| vercel/deepsec | **vercel-labs/deepsec** | Watchlist #12 |
| "Astryx ships MCP server" | **WRONG — no MCP server** (CLI bash only) | 08-astryx-mcp.md (2026-08-11); re-confirmed 2026-10-10 |
| claude-fable-5.md "at repo root" | **`Anthropic/claude-fable-5.md`** (subfolder) | 00-verification.md |
| Gitingest canonical | **coderamp-labs** (ex-cyclotruc); 2 same-name forks separate | 06a-data-acquisition.md |
| Docling org | **docling-project** (from DS4SD; LF AI & Data) | 06a-data-acquisition.md |
| changedetection.io upstream | **dgtlmoon** (not the 5 forks) | 06a-data-acquisition.md |
| mcp-scan | **Snyk Agent Scan** (renamed) | 06b-quality.md |
| Serena license | **GPL-3.0-or-later** (README badge, primary read) — not MIT | 05b-context.md (2026-10-10) |

## H3. The 5 preserved contradictions (do NOT silently resolve)

1. **OpenCode sandbox.** First-pass Element 7: "no built-in sandboxing — permission system is UX, not isolation; use Docker." Second sweep: OpenCode has native OS-level sandbox (Bubblewrap/gVisor/Firecracker/Seatbelt, `packages/opencode/src/sandbox/`). Both preserved; practical reliance unassessed.
2. **Output styles.** Element 10 lists 8 themes under "Output Styles"; second sweep says genuine gap — TUI themes ≠ Claude-Code-style output-style switching (issue #5199 open). Both preserved.
3. **Official OpenCode SDK identity.** First pass: `anomalyco/opencode-sdk-js` (+go). Second sweep: official SDK is `@opencode-ai/sdk` (opencode.ai/docs/sdk). Relationship unclear — unresolved.
4. **garrytan/gstack status.** Phase-5: OpenCode-compatible (startup-role skills + headless Chromium `/qa`). Element-1 sweep: excluded as Claude-Code-only. Mixed evidence — unresolved.
5. **Issue #30295 (custom statusLine).** First pass: open. Second sweep: shows "Closed" with auto-close label — may be process-closure, not resolution. Unresolved.
6. *(Additional)* **Smithery monetization claims:** conflicting sources (04-mcp).
7. *(Additional)* **Backend Astryx equivalent:** still a genuine gap after 30 themed searches; closest: Convex, Encore, Hasura/Atlas declarative schemas (01c §3.6.11).

## H4. Broken, obsolete, or misleading URLs / names

- `jbeck018/agents-opencode` — misleading name; actually a Claude Code fork (wshobson/agents). Excluded.
- `spencermarx/open-code-review` — different Claude-Code-only project; do NOT confuse with `alibaba/open-code-review`.
- walkinglabs "five layers" URL — live, but the file at that path is a Template Guide, not the framework; canonical layer names: Instructions / State / Verification / Scope Boundaries / Lifecycle Handoff.
- R5 (system_prompts_leaks) has 10+ same-name forks/mirrors (`sanjayshuklazoho`, `whoamimi`, `markoko007`, …) — canonical is `asgeirtj/`; verify you are not reading a stale/tampered fork.
- R6 (CL4R1T4S) mirrors (`ljbudgie/cl4r1t4s`, `buyan-kh/sysprompts`) replicate the repo including embedded directive-style text.

## H5. Discontinued / archived / unsafe repositories

| Resource | Status | Detail |
|---|---|---|
| gsd-build/get-shit-done | **ARCHIVED June 2026 — SECURITY WARNING** | Deep shell permissions; trust ("rug-pull") reports. DO NOT USE. Safe fork: open-gsd/gsd-core |
| daytonaio/daytona (OpenCode plugin) | Repo no longer maintained | Plugin functional at research time |
| Opencode-DCP | Maintenance mode | Successor "Sleev" per README |
| MongoDB Atlas App Services | EOL 2025-09-30 | — |
| Dredd | Archived May 2024 | — |
| Optic | Archived Jan 2026 | — |
| BackstopJS | Dormant since 2024 (archived) | — |
| Bloop, Sourcetrail | Archived | — |
| Gemini CLI (consumer) | Serving ended 2026-06-18 | Successor: Antigravity CLI |
| IBM ACP | Merged into A2A (Aug 2025), archived | — |
| Microsoft AutoGen | Maintenance mode (README banner) | Successors: AG2 / Microsoft Agent Framework |
| Mocky.io | Gone 2026 | — |
| Locust Cloud | Closed 2025 | — |
| git-secrets | Stale since 2021 | — |
| MkDocs Material | Maintenance mode (Nov 2025) | — |
| Piwik PRO | Free Core sunset | — |
| Railway / Koyeb | Free tiers removed | — |
| Deno Deploy | Sunsets ~Apr 2027 (team → Cloudflare) | Runtime 1yr maintenance |

## H6. Unsupported or shaky claims (not presented as fact in the catalogs)

- thekishandev/ai-system-prompt README claims "official system prompts" — unsubstantiated marketing copy (single-commit repo, placeholder text).
- x1xhlol archive's "largest collection" framing — large by stars (~144k) but no per-file provenance.
- gitjfmd/prompt-hub "1,627 prompts across 70+ services" — tertiary consolidation; "official" labels unvetted; repo still has template placeholders.
- 4pixeltechbr/promptograph "20,475 prompts from 55 repos, ~94M tokens" — self-reported, not independently audited.
- xAI grok-prompts "regularly updated" — as observed 2026-10-10, HEAD commit dated 2025-11-17 (stale ~11 months).
- Anthropic's release-notes system-prompt page was found stale vs deployed prompts (2026-07-07 third-party analysis).
- "Designs" and "Backend design skill" — no supportable claim of identity exists.

## H7. License discrepancies (verify before legal reliance)

| Resource | Discrepancy | Resolution |
|---|---|---|
| Serena | MIT (secondary) vs **GPL-3.0-or-later** (README badge, primary read 2026-10-10) | Use GPL-3.0-or-later |
| pa11y | MIT (common claim) vs **LGPL-3.0-only** | Use LGPL-3.0-only |
| promptograph | Repo page NOASSERTION vs README badge MIT | Unresolved — treat license as unverified |
| nightwire | NOASSERTION (GitHub) vs MIT (claimed) | Unresolved |
| Astro | GitHub license field NOASSERTION vs README MIT badge | Unresolved |
| Directus | BSL 1.1 (reported) | Verify before legal reliance |
| Xata | Shutdown rumors vs active 2026 listings | Conflict — unresolved |
| openai/evals | Repo page NOASSERTION vs README "same MIT license" disclaimer | Minor inconsistency, flagged |
| xai-org/grok-prompts | AGPL-3.0 (copyleft) | Reuse implications noted |
| volcengine/OpenViking | AGPL-3.0 (copyleft) | Commercial/hosting implications noted |
| firecrawl/firecrawl | AGPL-3.0 (copyleft) | Noted |
| jujumilk3/leaked-system-prompts | No license stated (all-rights-reserved default) | Reuse caution |

## H8. Recorded security incidents (check advisories before use)

- **CVE-2026-33634 / GHSA-69fq-xp46-6x23** — 2026-03-19: TeamPCP hijack of `trivy-action` tags 75/76 + malicious v0.69.4 (exfil to scan.aquasecurtiy.org). Safe iff tag 0.35.0 or SHA-pinned post-2025-04-09. (06b)
- **CVE-2026-80521** — kernel container-escape disclosed 2026-09-22; undermines user-namespace sandboxes until patched. (06b)
- **CVE-2025-49596** — MCP Inspector v2. (04-mcp)
- **axios maintainer-account hijack** (Mar 2026, no CVE) — case study for behavioral scanning. (01a/06b)
- **Mixpanel Nov 2025 breach** (ShinyHunters, ~28M accounts); LiteLLM PyPI, Bitwarden CLI, KICS action incidents (secondary reporting only). (06b/06c)
- **gsd-build/get-shit-done** archival — see H5. Do not install the original package.

## H9. Incomplete compatibility claims / missing documentation

- garrytan/gstack OpenCode compatibility — mixed evidence (H3 #4).
- Antigravity CLI (`agy`) plugin/skill surface — primary JS docs not fetched; secondary evidence only.
- Factory Droid, Qwen Code, Pi agent extension internals — secondary evidence only.
- Xata status; Gitpod 2026 product direction; Directus license — unresolved (see H1/H7).
- R12 (labac-dev/cursor-system-prompts) repo metadata — not captured.
- R17 (promptograph) license field — unresolved.
- Slate archive status — single-sourced; needs primary check.
- Issue #28407 (opencode run headless session bug) — flagged, not resolved.

## H10. Important research limitations

- A live URL is not proof of maintenance; a README is not proof every advertised capability works; protocol support is not proof of a tested integration.
- A missing search result is not proof a project does not exist.
- Star counts are point-in-time figures from heterogeneous sources (page-reported, third-party trackers) — growth over time explains most variance (Context7 7k→39k, superpowers 89k→211k across 2026).
- Non-English archives, HuggingFace system-prompt datasets, commercial prompt marketplaces, and closed prompt-management platforms were out of scope.
- Prompt bodies were not reproduced (by design); records describe types, counts, filenames, and claimed provenance only.
- Text-fetch only (no JS-rendered tables fully enumerated); nothing requiring sign-in, purchase, or form interaction was attempted.
