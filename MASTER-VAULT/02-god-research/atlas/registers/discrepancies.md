# Verification and Discrepancy Register

**Maintained by:** Atlas coordinator · **Last updated:** 2026-10-10

## A. Identity corrections (confirmed — use the corrected form)

| Original | Corrected | Evidence |
|---|---|---|
| "ruflo" | **ruvnet/ruflo** (formerly Claude Flow) | 00-verification.md (2026-08-09); re-confirmed watchlist 2026-10-10 |
| "enilkowaski apple designs skill" | **emilkowalski/skills** (Emil Kowalski) | 00-verification.md |
| "Krim Shoair" (Scrapling author) | **Karim Shoair** (GitHub D4Vinci) | named-watchlist.md (2026-10-10) |
| "PizzaBox by AWS" | **AWS Pizza Bot** (Sept 2026) — no PizzaBox project found | named-watchlist.md (2026-10-10) |
| "Everything Claude Code" | **affaan-m/ECC** (name officially retired; plugin `ecc@ecc`, npm `ecc-universal`) | named-watchlist.md (2026-10-10) |
| vercel/deepsec | **vercel-labs/deepsec** | named-watchlist.md (2026-10-10) |
| "NotebookLM skill" (generic) | distinct skill **stefandsl/notebooklm-skill** exists beyond teng-lin/notebooklm-py | named-watchlist.md (2026-10-10) |
| "Astryx ships MCP server" | **WRONG — no MCP server** (CLI bash integration only; `npx @astryxdesign/cli <cmd> --dense`) | 08-astryx-mcp.md (2026-08-11); re-confirmed 2026-10-10 |
| claude-fable-5.md "at repo root" | Actually at **`Anthropic/claude-fable-5.md`** (subfolder) | 00-verification.md |
| Gitingest canonical | **coderamp-labs** (ex-cyclotruc); 2 same-name forks are separate | 06a-data-acquisition.md |
| Docling org | **docling-project** (moved from DS4SD; LF AI & Data Foundation) | 06a-data-acquisition.md |
| Zyte | formerly **Scrapinghub** | 06a-data-acquisition.md |
| ScrapingBee | joined **Oxylabs** group (Jan 2026) | 06a-data-acquisition.md |
| mcp-scan | renamed **Snyk Agent Scan** | 06b-quality.md |
| changedetection.io upstream | **dgtlmoon** (not the 5 forks) | 06a-data-acquisition.md |
| Gemini CLI | folded into **Antigravity CLI** (`agy`); consumer serving ended 2026-06-18 | 03b-agents.md (Google Developers Blog, primary) |
| Windsurf (Cascade host) | now branded **Devin Desktop**; `.devin/rules/` preferred | 03b-agents.md (primary docs) |
| Kimi CLI | legacy alias of **Kimi Code CLI** (MoonshotAI/kimi-code, MIT) | 03b-agents.md |
| Gitpod | → **Ona** (OpenAI acquisition Jun 2026; Classic sunset 2026-10-15) | 06b-quality.md |
| IBM ACP | merged into **A2A** (Aug 2025, archived) | 05a-orchestration.md |

## B. License discrepancies (use the primary-read value)

| Resource | Claim A | Claim B | Resolution |
|---|---|---|---|
| Serena | MIT (secondary sources) | **GPL-3.0-or-later** (README badge, primary read) | Use GPL-3.0-or-later |
| pa11y | MIT (common claim) | **LGPL-3.0-only** | Use LGPL-3.0-only |
| promptograph | Repo page: NOASSERTION | README badge: MIT | Unresolved — flagged |
| nightwire | NOASSERTION (GitHub) | MIT (claimed) | Unresolved — flagged |
| Astro | GitHub license field: NOASSERTION | README: MIT badge | Unresolved — flagged |
| Slate | Archive status single-sourced | — | Unresolved — needs primary check |
| Directus | BSL 1.1 (reported) | — | Verify before legal reliance |
| Xata | Shutdown rumors | 2026 listings active | Conflict — unresolved |

## C. 2026 acquisition / status changes (recorded, primary-check advised for legal reliance)

- Auth.js → Better Auth migration recommendation (01c)
- Cal.com closed-source 2026-04-14; MIT fork **cal.diy** (01c)
- Stytch acquired by Twilio ($104.1M, closed 2025-11-14) (01c)
- Lemon Squeezy acquired by Stripe → folding into Stripe Managed Payments (01c)
- Payload CMS acquired by Figma (June 2025) (01c)
- Langfuse acquired by ClickHouse (Jan 2026) (06c)
- Statsig → OpenAI → Amplitude brand takeover (06c)
- Intercom rebranded to **Fin**; Salesforce acquisition pending (06c)
- Deno team → Cloudflare; Deno Deploy sunsets ~Apr 2027; runtime 1yr maintenance (06c)
- MkDocs Material maintenance mode (Nov 2025); Piwik PRO free Core sunset; Railway/Koyeb free tiers removed (06c)
- MongoDB Atlas App Services EOL 2025-09-30 (01c); Dredd archived May 2024 (01c/06b); Optic archived Jan 2026 (01c/06b); BackstopJS dormant since 2024 (02a/06b); Lost Pixel sunsetting into Figma (02a/06b); git-secrets stale 2021; Locust Cloud closed 2025 (06b); Mocky.io gone 2026 (06a)

## D. Security incidents recorded (do not re-verify blindly; check advisories before use)

- **CVE-2026-33634 / GHSA-69fq-xp46-6x23** — 2026-03-19 TeamPCP hijack of `trivy-action` 75/76 tags + malicious v0.69.4 (exfil scan.aquasecurtiy.org). Safe iff tag 0.35.0 or SHA-pinned post-2025-04-09. (06b)
- **CVE-2026-80521** — kernel container-escape disclosed 2026-09-22; undermines user-namespace sandboxes until patched. (06b)
- **CVE-2025-49596** — MCP Inspector v2. (04-mcp)
- March 2026 **axios** maintainer-account hijack (no CVE) — case study for behavioral scanning (01a/06b)
- Mixpanel Nov 2025 breach (ShinyHunters, ~28M accounts); LiteLLM PyPI, Bitwarden CLI, KICS action incidents (secondary-reporting only). (06b/06c)
- **gsd-build/get-shit-done** — archived June 2026, security concerns over deep shell permissions. DO NOT USE. Safe fork: open-gsd/gsd-core.

## E. Contradictions still unresolved (do not silently resolve in final assembly)

1. **OpenCode sandbox:** "no built-in sandboxing" (first-pass Element 7) vs native OS-level sandbox (Bubblewrap/gVisor/Firecracker/Seatbelt, second sweep). Both preserved.
2. **Output styles:** 8 themes listed under "Output Styles" vs genuine gap (themes ≠ Claude-Code output-style switching; issue #5199 open). Both preserved.
3. **Official OpenCode SDK identity:** anomalyco/opencode-sdk-js (+go) vs `@opencode-ai/sdk` (opencode.ai/docs/sdk). Relationship unclear.
4. **garrytan/gstack:** OpenCode-compatible (Phase 5) vs Claude-Code-only excluded (Element 1) — mixed evidence.
5. **Issue #30295 (custom statusLine):** open vs Closed-by-process — may be auto-close, not resolution.
6. **Smithery monetization claims:** conflicting sources (04-mcp).
7. **Backend Astryx equivalent:** still a genuine gap after 30 themed searches; closest candidates Convex, Encore, Hasura/Atlas declarative schemas (01c §3.6.11).
8. **Surrealism / Victorian styles:** no dedicated interface resources verified (02b).
9. **"Designs"** and **backend design skill** watchlist items: unresolved (named-watchlist.md).

## F. Dedup notes (one canonical record; folded at index build)

- Munder Difflin: recorded in 05a (harness) and named-watchlist.md — index keeps one; watchlist holds the canonical Part-19 record.
- DeepWiki: 05b + 04-mcp cross-refs folded.
- anthropics/skills, anthropics/claude-cookbooks, public-apis/public-apis, upstash/context7: Phase 0 base + workstream cross-refs folded to the best-verified record.
- Master index folded 71 duplicates (1,281 raw → 1,210 canonical) preferring the highest verification status.
