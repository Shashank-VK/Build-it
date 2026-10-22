# §30 — Coding Agents & Harnesses (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.
Sibling register `cases-product/12-tool-intelligence.md` covers Codex CLI, Claude Code, GitHub Copilot, Replit Agent, MCP at TI-04/05/20/21/22/06; this file goes BEYOND with additional tools and deeper controversy/deprecation coverage.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## EA-01 — Cursor (Anysphere) — ACTIVE / CONTROVERSIAL
- Purpose / problem: AI-first code editor (VS Code fork) with agent mode, tab completion, codebase chat; agent workflows for multi-step tasks.
- OSS/commercial: Commercial, proprietary. Pricing: $20/mo Pro (metered credits since Jun 2025); Teams $40/user/mo; Enterprise custom.
- Integration: VS Code extension ecosystem compatible; MCP; GitHub PR integration via Bugbot (launched Jul 2025); `@cursor/sdk` TypeScript SDK (public beta, 2026) for spawning agents from CI/CD.
- Maintenance: Active. Cursor 2.0 released Oct 2025 (parallel agents via git worktrees/remote machines). Claude Code v2.1.x-era comparisons list it at $20/mo Pro.
- Availability: Public SaaS; acquired by SpaceX — see below.
- Version/doc date: 2.0 Oct 2025; pricing system current as of Sep 2026 (per lowcode.agency review).
- Limitations: Agent cost is metered — heavy manual model selection drains the $20 credit pool in days; overage billed at API rates (no markup).
- Security: Proprietary cloud processes code; enterprise privacy mode available on Teams+. Post-acquisition data-flow questions (see below).
- Alternatives: Windsurf/Devin Desktop, GitHub Copilot, Cline, Aider, Claude Code, Codex CLI.
- Switching costs: Low–medium (editor-level; workflow/prompts portable-ish).
- **Controversies (both sides evidenced):**
  1. **June–July 2025 pricing backlash.** On 16 Jun 2025 Cursor changed the $20 Pro plan from ~500 requests to usage-metered credits while keeping "unlimited" language on the pricing page; users reported rate limits after few Claude 4 Sonnet requests, unexpected overage bills, and forum complaint threads hidden by AI moderation. On 5 Jul 2025 Cursor published "Clarifying our pricing," admitted misleading communication, offered refunds for 16 Jun–4 Jul charges (~225 Sonnet 4 requests/mo clarified). Mechanic stayed: $20 = $20 of credits; Auto mode unlimited-ish. (Corroborated: consumerrights.wiki incident page; lowcode.agency Sep 2026 pricing review; startupfortune analysis.)
  2. **Composer 2 model provenance (Mar 2026).** Cursor's Composer 2 model was built on Kimi 2.5 (Moonshot AI, Jan 2026 open-weights LLM); not disclosed until users identified it on X in week one. VP Lee Robinson acknowledged; co-founder Aman Sanger called non-disclosure "a miss"; Moonshot confirmed authorized commercial partnership via Fireworks AI. TechCrunch speculated non-disclosure related to US–China AI tensions. (Corroborated via Wikipedia citing TechCrunch.)
  3. **April 2025 "Sam" support-agent incident.** AI help-desk program "Sam" invented a non-existent login policy, triggering user cancellations before staff intervened with refunds. (Wikipedia, single-source — treat as Corroborated-weak.)
- **M&A: acquired by SpaceX, $60B all-stock (2026).** Timeline: Apr 21, 2026 — SpaceX/Cursor announce compute partnership + SpaceX right to acquire for $60B or pay $10B for joint work; Jun 16, 2026 — SpaceX exercises purchase right (all-stock) days after SpaceX IPO; **closed Aug 14, 2026** (389,289,254 SpaceX Class A shares). Cursor survives as wholly owned subsidiary integrated into SpaceXAI. Context: SpaceX merged with xAI Feb 2026 (~$1.25T combined); Grok V9-Medium trained on Cursor workflow data. Nov 2025: $2.3B Series D @ $29.3B (Accel/Coatue; Google, Nvidia participated); ARR >$1B end-2025, ~$2.6–3B mid-2026. Co-founder Arvid Lunnemark departed Oct 2025 (Integrous Research). (Corroborated: TechCrunch 2026-06-16 via ai-news tracker; Wikipedia; SatellitePro ME 2026-08; thingshavehistory.)
- Use: U(Verified) — Nvidia, Adobe, Uber, Shopify named as clients (thingshavehistory, 2026); ~4M active developers, ~50k enterprise customers (ai-news tracker citing TechCrunch).

## EA-02 — Windsurf (Codeium) → Devin Desktop (Cognition) — ACTIVE (acquired, rebranded) / CONTROVERSIAL
- Purpose / problem: Agentic IDE (VS Code fork lineage from Codeium); Cascade agent, multi-file editing; enterprise distribution.
- OSS/commercial: Commercial, proprietary. Was Free (25 credits/mo) / Pro $15/mo.
- Integration: VS Code extension marketplace lineage; MCP; enterprise SSO.
- Maintenance: Active under Cognition. **Rebranded to Devin Desktop June 2026.**
- **The 2025 three-way saga (all corroborated):**
  - May 2025: OpenAI agrees to acquire Windsurf ~$3B.
  - **Jul 11, 2025: deal collapses** — exclusivity expired; reported cause: Microsoft (OpenAI's largest investor) demanded IP access; Windsurf refused to grant Microsoft access to proprietary tech (Microsoft owns rival GitHub Copilot). (ultrathink.ai; winbuzzer.)
  - Same day: **Google DeepMind reverse-acquihire** — $2.4B non-exclusive tech license; CEO Varun Mohan + co-founder Douglas Chen + R&D cohort join Google. (CNBC via Wikipedia; marketbusinessnews.)
  - **Jul 14, 2025: Cognition acquires remainder** — IP, product, brand, ~240 remaining employees; 100% financial participation/vesting honored. (Cognition announcement; CNBC.)
  - Fallout: early Aug 2025 — Cognition laid off ~30 Windsurf staff, offered remaining ~200 nine-month-salary buyouts; those staying faced reported 80+-hour weeks. (femaleswitch, single-source — Corroborated-weak.)
  - During OpenAI talks, **Anthropic withdrew Claude access** from Windsurf (June 2025), degrading the product mid-negotiation; Cognition later restored it. (marketbusinessnews.)
  - At acquisition: ~$82M ARR, 350 enterprise customers. FedRAMP High certification cited as strategic asset for government Devin deployments. (winbuzzer.)
- Alternatives: Cursor, GitHub Copilot, Cline, Aider, Claude Code.
- Switching costs: Low–medium.
- Use: U(Verified) — 350 enterprises pre-acquisition; Cognizant partnership Jan 2026 integrating Devin + Windsurf into Flowsource (Cognition blog).

## EA-03 — Devin (Cognition) — ACTIVE
- Purpose / problem: Autonomous cloud "AI software engineer": ticket→PR on dedicated microVMs (own kernel, hypervisor-level snapshot/restore), plus Devin CLI/Local, Devin Desktop (ex-Windsurf IDE), API/MCP surface.
- OSS/commercial: Commercial, proprietary. No third-party LLM API keys supported (compound AI system; Cognition's own SWE-model line: SWE-1.5 Oct 2025, SWE-1.6 Apr 2026, SWE-1.7 Jul 2026, SWE-2 Sep 2026).
- Integration: GitHub/Slack/Linear; MCP; `blockdiff` disk-snapshot tooling open-sourced Jun 2025; Hypervisors API v3.
- Maintenance: Active. Series E Sep 2026: $2B+ raised @ **$48B valuation** (a16z, Accel); run-rate revenue $73M (Jul 2025) → $492M (May 2026) → ~$900M (Sep 2026) — company-reported, unaudited.
- Availability: SaaS + enterprise; FedRAMP High via Windsurf acquisition.
- Limitations: Closed model stack (no BYO keys); cloud-only brain (hosted on Azure); premium pricing.
- Security: MicroVM isolation per session; enterprise SSO/audit; code processed in Cognition cloud by design.
- Alternatives: OpenHands (OSS), Cursor/SpaceX, Claude Code, Codex, Jules.
- Switching costs: Medium (workflow + vendor model stack).
- Use: U(Verified) — Goldman Sachs (first AI software engineer Jul 2025, scaling to thousands of instances per Forkast/CNBC); NVIDIA, GE Aerospace, Citi, Mercedes-Benz, Itaú (17k engineers); Cognizant (30% of code AI-generated, targeting 50%). RSA-260 factored Sep 2026 using GPU implementation built with Devin (Cognition).

## EA-04 — Amazon Q Developer → Kiro — DEPRECATED (sunset in progress)
- Purpose / problem: AWS AI coding assistant (ex-CodeWhisperer): completions, chat, security scanning in IDE.
- OSS/commercial: Commercial (AWS). Was $19/user/mo Pro; free tier.
- Integration: VS Code/JetBrains IDE plugins; AWS console.
- Maintenance: **DEPRECATED.** Primary source (AWS DevOps Blog): IDE plugins + paid subscriptions reach **end of support April 30, 2027**; **new signups blocked May 15, 2026** (free tier via Builder ID + new subscriptions); Opus 4.6 removed from Q Pro May 29, 2026 (Opus 4.5 remains; Opus 4.7+ exclusive to Kiro). Plugins remain listed with deprecation notice; critical bugfixes only through window.
- Successor: **Kiro** — spec-driven agentic IDE (announced Jul 2025, GA May 7, 2026): structured specs/requirements/design/task lists as living docs, hooks, steering files, custom subagents, "Powers"; Q Developer CLI rebranded Kiro CLI.
- Lineage: CodeWhisperer → Q Developer → Kiro (third identity in ~3 years).
- Alternatives: Kiro (official path), Claude Code, Cursor, GitHub Copilot.
- Switching costs: Low–medium; but model-access degradation (Opus 4.6 removal) forces timeline.
- Use: U(Verified) — AWS's own product; enterprise AWS shops.

## EA-05 — Continue.dev — SUPERSEDED (acquired, product discontinued)
- Purpose / problem: Open-source AI coding assistant (VS Code/JetBrains extensions): autocomplete, chat, edit; connect any model; custom context (Jira/Confluence); "Hub" for sharing assistants.
- OSS/commercial: Was OSS Apache-2.0 + commercial hub. Raised $5M seed (Heavybit, YC; angels incl. Hugging Face co-founder).
- Maintenance: **Product discontinued after acquisition by Cursor** (reported Jun 24, 2026): users given **July 15 export deadline** before data deletion; recurring billing disabled; **codebase remains Apache-2.0** for community. Co-founder Nate Sesti joined Cursor; Ty Dunn had departed earlier. (Corroborated: startupnews.fyi; dev.to Jun 2026.)
- Note: earlier "Continue @Codebase deprecated" — docs now point to agent mode + rules/MCP (desplega.ai FAQ).
- Alternatives: Cline, Aider, OpenCode, Cursor.
- Use: U(Proposed) — was "loved by hundreds of thousands of developers" per company (vendor claim).

## EA-06 — Sourcegraph Cody / Amp — ACTIVE (enterprise-only; consumer tiers DEPRECATED)
- Purpose / problem: Codebase-aware AI chat/completions/edits grounded in Sourcegraph code search; Amp is the agentic coding agent (split into separate company Dec 2025).
- OSS/commercial: Commercial. **Cody Free and Pro ended July 23, 2025** (new signups stopped Jun 25, 2025); Cody Enterprise only ($59/user/mo per battle-card; median $66,600/yr per Vendr data). Amp credit-based.
- Integration: VS Code, JetBrains, experimental Neovim/Visual Studio, web, CLI; GitHub/GitLab repo context; MCP.
- Maintenance: Active for enterprise. Dec 2025: Sourcegraph and Amp became separate companies (Amp Inc. = coding agents; Sourcegraph = code search).
- Limitations: No standalone/free tier; enterprise-contract only; plan discontinuation alienated individual developers (community criticism).
- Security: Self-hosted option enables data sovereignty; enterprise SSO/audit.
- Alternatives: Copilot, Cursor, Cline, Unblocked (context layer), Augment.
- Use: U(Verified) — 4/6 top US banks, 15+ government agencies, Palo Alto Networks, Qualtrics (battle-card; treat customer claims as vendor-corroborated).

## EA-07 — Cline (ex-Claude Dev) — ACTIVE
- Purpose / problem: Open-source autonomous coding agent as IDE extension (VS Code/JetBrains) + CLI; plan→act loop with human-in-the-loop approvals; MCP extensible.
- OSS/commercial: Open source, Apache-2.0. Free (bring your own API key); company raised $32M seed+Series A by Jul 2025 (founder Saoud Rizwan; hackathon origin Jun 2024).
- Integration: VS Code/JetBrains marketplaces; any model provider (Anthropic, OpenAI, Google, Ollama, LM Studio).
- Maintenance: Active. May 14, 2026: extracted `@cline/sdk` open-source TypeScript agent runtime (powers CLI + Kanban products); Terminal-Bench 2.0: Cline CLI 74.2% on claude-opus-4.7 vs 69.4% published for Claude Code (vendor/press claim — treat as Corroborated-weak).
- Limitations: BYO-key cost exposure; approval-gating adds friction at scale.
- Security: Explicit per-action approval model; local execution; audit-conscious positioning.
- Alternatives: Aider, OpenCode, Cursor, Roo Code (fork lineage).
- Switching costs: Low.
- Use: U(Proposed) — broad community adoption; no named enterprise customers located.

## EA-08 — Aider — ACTIVE
- Purpose / problem: Terminal AI pair programmer; git-native (AI edits committed with auto messages; diff/undo via git); repo-map via tree-sitter; any LLM via BYO key; polyglot benchmark leaderboard.
- OSS/commercial: Open source, Apache-2.0. Free + your API costs. Independent maintainer (Paul Gauthier).
- Integration: CLI; pip/pipx/Docker; works with Claude/GPT/Gemini/DeepSeek/local via LiteLLM.
- Maintenance: Active — weekly release cadence (v0.82.1 era Apr 2026; 0.x versioning with occasional breaking CLI-flag changes). ~44k GitHub stars; ~6.8M PyPI installs; ~15B tokens/wk (per 2026 video review — Corroborated-weak). One-person bus factor is the structural risk; no SOC 2 (matters for team adoption).
- Limitations: 0.x instability; terminal-only; single maintainer.
- Security: Runs shell commands with user approval; API keys local.
- Alternatives: OpenCode, Claude Code, Codex CLI, Cline.
- Switching costs: Low.
- Use: U(Proposed) — individual developers; no named enterprise customers located. NOTE: one tracker (ai-whatchelin, 2026-08-12) claimed "no releases since Aug 2025" — contradicts weekly-cadence evidence; treat that claim as unreliable.

## EA-09 — OpenHands (ex-OpenDevin) — ACTIVE (architecture in transition)
- Purpose / problem: Open-source autonomous software-development agent platform (plan/code/test/PR in sandboxed Docker runtimes); event-sourced architecture; microagents; GitHub resolver action.
- OSS/commercial: Open source, MIT (enterprise/ dir separately licensed). Model-agnostic via LiteLLM. Optional managed cloud.
- Integration: Web UI, CLI, headless, GitHub Action (`@openhands-agent` mention), SDK.
- Maintenance: Active but **mid-transition V0→V1**: Python harness last shipped tag 0.62.0; main repo repurposed into "Agent Canvas" (TypeScript/Electron control center); V1 agent core extracted to `software-agent-sdk` repo; V0 marked legacy with removal scheduled April 2026 (per Sep 2026 survey; treat date as Reported). SWE-bench 77.6% claimed (vendor/community). 25k+ stars.
- Limitations: Heavyweight architecture (maximal-harness design); transition creates migration uncertainty; Docker-socket access = root-equivalent (run on disposable infra).
- Security: Per-task sandbox containers; but host Docker socket usage must be isolated.
- Alternatives: Devin (commercial), SWE-agent/mini-swe-agent (minimal), Claude Code.
- Switching costs: Low–medium (self-hosted).
- Use: U(Proposed) — research/community; no named enterprise production customers located.

## EA-10 — Tabnine — ACTIVE (enterprise-only pivot)
- Purpose / problem: Privacy-first AI code assistant: completions, chat, agents; private models; four deployment modes incl. fully air-gapped.
- OSS/commercial: Commercial, proprietary. **Sunset free and standalone Pro plans in 2026** (per saganote comparison); Agentic tier $59/user/mo; Enterprise Context Engine GA Feb 2026; BYO-model (Self-Managed Models) Apr 2026. (One source still lists a Starter free tier — mixed evidence; treat current free availability as Unknown.)
- Integration: VS Code, JetBrains, Eclipse, Neovim; MCP support; admin analytics/SSO.
- Maintenance: Active; Gartner 2026 Magic Quadrant "Visionary" for Enterprise AI Coding Agents (vendor-credited claim).
- Limitations: Weaker raw generation vs Copilot/Cursor per third-party reviews; premium pricing.
- Security: Strongest story in class: never trains on customer code (contractual), VPC/on-prem/air-gapped; SOC 2/GDPR.
- Alternatives: Copilot, Cursor, Cody Enterprise (regulated shops).
- Switching costs: Medium (enterprise deployment).
- Use: U(Proposed) — defense/finance/healthcare positioning; no named customers located in this pass.

## EA-11 — Kiro (AWS) — ACTIVE (successor product)
- Purpose / problem: Spec-driven agentic IDE: write structured spec (requirements/design/tasks) → agent executes task graph; hooks, steering files, custom subagents, Powers; autonomous background agents opening PRs.
- OSS/commercial: Commercial (AWS).
- Integration: Successor to Q Developer; Kiro CLI (ex-Q CLI); AWS DevOps Agent mitigation specs → Kiro CLI implements fix → opens PR.
- Maintenance: Active. Announced Jul 2025; GA May 7, 2026. Latest models (Opus 4.7) exclusive to Kiro.
- Limitations: New product (2026); AWS-centric; pricing/migration tooling still maturing (per aitechconnect FAQ).
- Security: AWS IAM; standard cloud shared responsibility.
- Alternatives: Cursor, Claude Code, Copilot.
- Switching costs: Low–medium for Q Developer users (official migration path).
- Use: U(Verified) — AWS's strategic successor; adoption data not yet public.

## EA-12 — Supermaven — SUPERSEDED (acquired, wound down)
- Purpose / problem: AI code completion startup (fast inference).
- OSS/commercial: Was commercial.
- Maintenance: **Acquired by Cursor Nov 2024** (undisclosed sum); team folded in; **standalone product wound down late 2025**. (Wikipedia.)
- Alternatives: Copilot, Cursor Tab, Tabnine.
- Use: Historical.

## EA-13 — Gemini CLI — ACTIVE (with tier changes)
- Purpose / problem: Google's open-source terminal coding agent (Apache-2.0); Gemini 2.5/3.x; built-in Google Search grounding; generous free tier (1,000 req/day personal).
- OSS/commercial: OSS Apache-2.0 + Google account free tier + API billing.
- Maintenance: Active; bi-weekly releases. **Legacy individual tiers stop serving Jun 18, 2026** (per securityboulevard comparison, Jun 2026 — Corroborated-weak; verify before citing).
- Alternatives: Codex CLI, Claude Code, Aider.
- Use: U(Proposed).

## EA-14 — OpenCode — ACTIVE
- Purpose / problem: Open-source terminal coding agent (MIT); 75+ models via BYO key; provider-agnostic.
- OSS/commercial: OSS MIT; free + API costs.
- Maintenance: Active (2026).
- Alternatives: Aider, Cline, Codex CLI.
- Use: U(Proposed). (Lightly researched — depth debt.)

## EA-15 — SWE-agent / mini-swe-agent — ACTIVE (research reference)
- Purpose / problem: Minimal academic agent harness (~190-line core for mini) for software-engineering tasks; the "minimal-harness" pole vs OpenHands' maximal design.
- OSS/commercial: OSS (research).
- Maintenance: Maintained as research artifact; widely forked.
- Use: U(Verified) — research community standard baseline. (Lightly researched — depth debt.)

## Notable status findings (coding agents)
- Amazon Q Developer — **DEPRECATED**, EOS Apr 30 2027, signups blocked May 15 2026 → Kiro.
- Continue.dev — **SUPERSEDED**, acquired by Cursor, product discontinued Jul 2025, code stays Apache-2.0.
- Cody Free/Pro — **DEPRECATED** Jul 2025; enterprise-only.
- Supermaven — **SUPERSEDED** (Cursor acquisition, wound down late 2025).
- Windsurf — acquired by Cognition Jul 2025 after OpenAI $3B collapse + Google $2.4B acquihire; **rebranded Devin Desktop Jun 2026**.
- Cursor — **$60B SpaceX acquisition closed Aug 14, 2026**; pricing backlash Jun–Jul 2025; Composer 2/Kimi provenance controversy Mar 2026.
- Microsoft's AutoGen → maintenance mode (covered in 02-agent-frameworks.md).
