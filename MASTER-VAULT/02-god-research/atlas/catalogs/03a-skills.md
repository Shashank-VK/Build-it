# Atlas Catalog 03a — The Agent Skills Ecosystem (Part 6)

**Workstream:** Researcher #6 — SKILLS ecosystem
**Verification date:** 2026-10-10
**Scope:** The Agent Skills standard (cross-referenced), official company skill collections, community skill collections by domain, skill infrastructure (discovery/installation), validators/linters, security scanners, skill generators/meta-skills, evaluators, and skill marketplaces/directories.
**Already catalogued (cross-referenced only, NOT re-researched):** agentskills/agentskills (official spec), anthropics/skills (official Anthropic repo), obra/superpowers, mattpocock/skills, addyosmani/agent-skills, [REDACTED-caveman], cloudflare/skills, composiohq/skills, Gentleman-Programming/Gentleman-Skills, VoltAgent/awesome-agent-skills (1000+ index), waybarrios/opencode-power-pack, hqhq1025/skill-optimizer, glebis/claude-skills, emilkowalski/skills (apple-design), keysjoao/laws-of-ux-skills, mvanhorn/last30days-skill, Forward-Future/loopy, garrytan/gstack, teng-lin/notebooklm-py, cobusgreyling/loop-engineering, remorses/opencode-injection-guard, DietrichGebert/ponytail, meaningfy-ws/skillery, alirezarezvani/claude-skills, steipete/agent-rules, FrancyJGLisboa/agent-skill-creator, tripleyak/SkillForge, K-Dense-AI/science-superpowers, Kenryu42/cc-safety-net, alonw0/secure-skills, Pantheon-Security/medusa, openguardrails, thousandflowers/skillreaper, Kulaxyz/self-learning-skills, okdk7788/opencode-self-improving-skills.

## Discovery method

Primary-source-first web research, 2026-10-10. Sources searched: official repo READMEs on github.com (fetched directly), official docs (agentskills.io, developers.openai.com/codex, docs.stripe.com, docs.expo.dev, help.figma.com, supabase.com), skill-registry front pages (skills.sh, agentskillexchange.com, claude.com/skills), and GitHub code search results via web search for SKILL.md-bearing repos.

Search themes used: (1) official company skills — `"<company>" official agent skill SKILL.md github` (Vercel, Stripe, Sentry, Expo, Hugging Face, Figma, Trail of Bits, Microsoft, Netlify, Supabase, Neon, ClickHouse, HashiCorp, Better Auth, LambdaTest, Capgo, Angular, OpenAI); (2) the installer ecosystem — `skills.sh skills CLI npx skills add ecosystem registry`, `skillkit install skills CLI`; (3) quality infrastructure — `SKILL.md validator linter skill validation tool github`, `agent skill security scanner skill-scanner SKILL.md malicious github`; (4) registries — `agentskillexchange.com Agent Skill Exchange skill marketplace`, `agentskills-sdk`, `Cap-go capgo-skills`, `agentskills-sdk cuoicungtui`, `claude.com skills gallery`; (5) lead-following from discovered repos (skillkit listings revealed better-auth/skills, supabase/agent-skills, neondatabase/agent-skills, clickhouse/agent-skills, angular/skills, LambdaTest/agent-skills, cloudflare/agent-skills, netlify/agent-skills, hashicorp/skills; Figma discovery revealed the Figma plugin skills set; podo/design-agent-skills stubs revealed openai-skills, google-stitch-skills, software-mansion-skills, callstack-agent-skills).

Contents were inspected for: SKILL.md frontmatter fields (name, description, license, compatibility, metadata, allowed-tools), directory layouts (skills/, scripts/, references/, assets/, agents/openai.yaml), install docs, plugin/marketplace manifests (.claude-plugin, .cursor-plugin, gemini-extension.json), CI validation workflows, verification tiers, and compatibility claims (checked against each vendor's documented install paths — Claude Code plugin marketplaces, Codex plugin compatibility, skills.sh/npx skills, .agents/skills, Cursor/GitHub Copilot/Gemini CLI/VS Code paths).

---

## 1. The Agent Skills standard (cross-reference)

> **Resource name:** Agent Skills (official standard)
> **Canonical identity:** agentskills/agentskills (Anthropic-maintained open format)
> **Category:** Standard / specification
> **Type:** Open format specification
> **Official URL:** https://agentskills.io
> **Description:** The open Agent Skills format: a skill is a directory containing a required `SKILL.md` (YAML frontmatter with `name` and `description`, followed by Markdown instructions) plus optional `scripts/`, `references/`, `assets/` subdirectories. Progressive disclosure: agents see only name/description/path until the skill is invoked, then load the body on demand.
> **Contents inspected:** This workstream treats the spec repo as already catalogued; it was used as the compatibility baseline. All records below ground their compatibility claims against this format plus vendor-specific install surfaces documented by each publisher.
> **Actual capabilities:** Defines portable skill packaging, frontmatter schema, and progressive-disclosure loading model.
> **Usage domain:** Cross-agent skill packaging.
> **Integration method:** SKILL.md format adoption by agents (Claude Code, Codex, Cursor, OpenCode, Gemini CLI, Copilot, and 70+ more per vercel-labs/skills docs).
> **Compatibility (with evidence):** The SKILL.md format is shared between Claude Code and Codex explicitly (Codex docs state skills are "built on the open agent skills standard (agentskills.io / github.com/openai/skills), the same SKILL.md spec Claude Code uses — so skills are cross-compatible in principle"; OpenAI's skill-creator sample lives at openai/codex `codex-rs/skills/src/assets/samples/skill-creator`). Codex adds `agents/openai.yaml` interface metadata and ships its own plugin packaging (`.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`).
> **Dependencies:** None.
> **Availability:** Open, free.
> **Maintenance:** Active; Anthropic-maintained with community contributions.
> **License:** Code Apache-2.0; documentation CC-BY-4.0 (per cuoicungtui/agentskills README).
> **Limitations:** The standard defines the format, not distribution, discovery, versioning, or trust — those are provided by registries (skills.sh, agentskillexchange.com), installers (npx skills), and scanners.
> **Related resources:** vercel-labs/skills (reference CLI), openai/skills (deprecated examples), agentskills-sdk.
> **Sources:** https://agentskills.io; https://github.com/agentskills/agentskills; https://developers.openai.com/codex/skills (redirects to learn.chatgpt.com/docs/build-skills); https://github.com/cuoicungtui/agentskills
> **Verification date:** 2026-10-10
> **Confidence:** High (cross-reference to prior catalog entry).

Also catalogued elsewhere: anthropics/skills (Anthropic's official examples: documents, creative, development tools — document skills `pdf`/`docx`/`pptx`/`xlsx`, `frontend-design`, `mcp-builder`, `webapp-testing`; surfaced in this workstream only via the Claude Skills gallery context and Microsoft skill references) and cloudflare/skills (official Cloudflare collection: agents-sdk, cloudflare, cloudflare-email-service, durable-objects, sandbox-sdk, turnstile-spin, web-perf, workers-best-practices, wrangler — referenced in this workstream via consumer imports and podo/design-agent-skills stubs; not re-inspected).

---

## 2. Official company skill collections

### 2.1 Vercel — vercel-labs/agent-skills

> **Resource name:** Vercel Labs Agent Skills (vercel-labs/agent-skills)
> **Canonical identity:** vercel-labs/agent-skills on GitHub (Vercel Labs)
> **Category:** Official company skills — frontend design, React/Next.js, deployment
> **Type:** Skill collection repository
> **Official URL:** https://github.com/vercel-labs/agent-skills
> **Description:** Vercel's official collection of agent skills: 8 skills covering Vercel project optimization, React/Next.js performance, web design guidelines, writing guidelines, React Native, React View Transitions, composition patterns, and claimable deployments to Vercel.
> **Contents inspected:** README (fetched 2026-10-10) lists all 8 skills with rule counts and usage triggers: `vercel-optimize` (metrics-first Vercel project audit for cost/perf/reliability/caching/billing; backed by `vercel-optimize-tests` package with `.mjs` tests and real-CLI-output fixtures), `react-best-practices` (40+ rules in 8 impact-ranked categories: waterfalls, bundle size, server-side perf, client data fetching, re-renders, rendering, JS micro-opts, advanced), `web-design-guidelines` (100+ rules: a11y, focus states, forms, animation, typography, images, perf, navigation/state, dark mode, touch, i18n), `writing-guidelines` (80+ rules from the Vercel writing handbook), `react-native-guidelines` (16 rules/7 sections), `react-view-transitions` (View Transition API + Next.js `transitionTypes`), `composition-patterns` (compound components, state lifting), `vercel-deploy-claimable` (deploy from chat; auto-detects 40+ frameworks; claim URL transfers ownership). Repo layout: `skills/` (one dir per skill with SKILL.md, scripts/, references/), `packages/`, `scripts/` (incl. `build-discovery-index.mjs` publishing an immutable GitHub release with a discovery index on every main change), `skills.sh.json`, AGENTS.md/CLAUDE.md.
> **Actual capabilities:** Guideline/audit skills that teach agents Vercel-stack best practices and a metrics-first Vercel cost/perf audit; a deploy skill that packages and uploads projects to Vercel.
> **Usage domain:** Frontend development, React/Next.js performance, web design review, Vercel deployment and optimization.
> **Integration method:** `npx skills add vercel-labs/agent-skills` (whole collection) or per-skill (`npx skills add vercel-labs/agent-skills/react-best-practices`); skills auto-activate when relevant tasks are detected.
> **Compatibility (with evidence):** Native: any agent reading Agent Skills SKILL.md. Documented: installable via skills.sh ecosystem (skills.sh badge and `skills.sh.json` in repo). No Claude Code plugin marketplace manifest observed in root listing.
> **Dependencies:** None for guideline skills; `vercel-optimize` uses Vercel metrics (requires Vercel project access); `vercel-deploy-claimable` uploads via Vercel's deployment service.
> **Availability:** Public, free, open source.
> **Maintenance:** Active — 32,119 stars, 2,813 forks, 275 commits, created 2025-12-08, MIT license; 3 releases.
> **License:** MIT
> **Limitations:** Guideline-style skills (advisory prompts); `vercel-optimize` is the only evidence-driven/audit skill. Not verified whether Vercel supports skill-scoped install natively in v0 (not documented in README).
> **Related resources:** vercel-labs/skills (the `npx skills` CLI), skills.sh registry, anthropics/skills `frontend-design` (alternative).
> **Sources:** https://github.com/vercel-labs/agent-skills (README fetched 2026-10-10)
> **Verification date:** 2026-10-10
> **Confidence:** High. **Verification: Verified.**

### 2.2 Sentry — getsentry/skills

> **Resource name:** Sentry Skills (getsentry/skills)
> **Canonical identity:** getsentry/skills on GitHub — "Agent Skills used by the Sentry team for development"
> **Category:** Official company skills — code review, security, docs, workflow
> **Type:** Skill collection + Claude Code plugin marketplace + subagent library
> **Official URL:** https://github.com/getsentry/skills
> **Description:** Sentry's official internal-turned-public skill collection for Sentry engineering: ~30 skills (code-review, security-review, django-access-review, django-perf-review, gha-security-review, find-bugs, secret-serialization, pr-writer, iterate-pr, doc-coauthoring, agents-md, commit, create-branch, skill-writer, skill-scanner, prompt-optimizer, claude-settings-audit, triage-frontend-issues, sred-project-organizer, etc.) plus two subagents (`code-simplifier`, `senpai`). Explicitly points users to getsentry/sentry-for-ai for Sentry product setup/debugging skills.
> **Contents inspected:** README fetched 2026-10-10. Canonical tree: `skills/<name>/SKILL.md` with a required root-level `SPEC.md` (maintenance contract) for new/materially changed skills; `.agents/skills` symlinks to `skills/`; `agents/` (subagents). Skill template specifies frontmatter `name`/`description`/`license`/`compatibility`/`allowed-tools`/`metadata`, naming conventions (kebab-case 1–64 chars), and SKILL.md < 500 lines. Notable meta-skill: `skill-writer` — "Canonical workflow to synthesize, create, and iteratively improve agent skills for this repository" with `skills/skill-writer/EVAL.md` evaluation prompts. Notable validator: `skill-scanner` — "Scan agent skills for security issues." Vendoring policy documented (consistency, customization, reliability) with attribution rules. Scope guidance: global vs domain-specific (e.g., `infra-skills` plugin with `gcp-logs`, `terraform-review`) vs repo-specific.
> **Actual capabilities:** Engineering-workflow skills (review, commit, PR, docs, security) codifying Sentry's internal practices; plus a meta-skill for authoring skills and a scanner skill for auditing untrusted skills.
> **Usage domain:** Software engineering workflows (review, git, docs, security), skill authoring, skill security scanning.
> **Integration method:** Claude Code plugin marketplace (`claude plugin marketplace add getsentry/skills`, `claude plugin install sentry-skills@sentry-skills`, also `infra-skills`); skills.sh (`npx skills add getsentry/skills`).
> **Compatibility (with evidence):** Documented: Claude Code (marketplace + plugin), plus "Claude Code, Cursor, Cline, GitHub Copilot, and other compatible agents" via skills.sh. `allowed-tools` frontmatter is Claude-Code-specific and was noted by Sentry as Warden-sensitive.
> **Dependencies:** git/GitHub/CLI tooling per skill (e.g., `gh` for PR skills); Notion for sred skills.
> **Availability:** Public, free, open source.
> **Maintenance:** Active — 1,043 stars, 53 forks, 249 commits, created 2026-01-05, Apache-2.0.
> **License:** Apache-2.0
> **Limitations:** Internal-tooling flavored; Sentry product skills live in the separate getsentry/sentry-for-ai repo (not inspected here — noted as lead).
> **Related resources:** getsentry/sentry-for-ai, trailofbits/skills (security overlap), obra/superpowers (methodology alternative).
> **Sources:** https://github.com/getsentry/skills (README fetched 2026-10-10)
> **Verification date:** 2026-10-10
> **Confidence:** High. **Verification: Verified.**

### 2.3 Expo — expo/skills

> **Resource name:** Expo Skills (expo/skills)
> **Canonical identity:** expo/skills on GitHub — official Expo team skills
> **Category:** Official company skills — mobile (React Native/Expo)
> **Type:** Skill collection repository (+ plugin packaging)
> **Official URL:** https://github.com/expo/skills
> **Description:** Official AI agent skills from the Expo team for building, deploying, upgrading, and debugging Expo apps: `building-native-ui`, `expo-api-routes`, `expo-cicd-workflows`, `expo-deployment`, `expo-dev-client`, `expo-module`, `expo-tailwind-setup`, `expo-ui-jetpack-compose`, `expo-ui-swift-ui`, `native-data-fetching`, `upgrading-expo`, `use-dom` (12 skills). Expo documentation, Expo CLI, and EAS CLI remain the stated source of truth; skills teach agents to apply them.
> **Contents inspected:** README (fetched via search-result mirror deepuchauhan4728-sys/skills and expo/skills README snippet, 2026-10-10). Installation table: plugin install for Claude Code/Codex (official plugin marketplaces handle updates) vs skills CLI for Cursor/OpenCode/GitHub Copilot/Windsurf/Gemini/Cline/AMP/Factory Droid/Antigravity/Kiro CLI (`npx skills@latest add expo/skills --skill '*'`, optionally `--agent <agent>`). A skill-catalog entry (shabirkhan-dev/personal-os) confirms the same 12 skills with descriptions. MIT license badge; skills.sh badge (skills.sh/expo/skills).
> **Actual capabilities:** Procedural knowledge skills for Expo Router UI, API routes, EAS CI/CD, deployment, dev clients, native modules/config plugins, Tailwind/NativeWind setup, SwiftUI/Jetpack Compose integration, data fetching, SDK upgrades, DOM components.
> **Usage domain:** React Native / Expo app development and deployment.
> **Integration method:** Claude Code/Codex plugin marketplaces; `npx skills add expo/skills` for other agents; Cursor remote rules via `https://github.com/expo/skills.git`.
> **Compatibility (with evidence):** Documented: Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Windsurf, Gemini, Cline, AMP, Factory Droid, Antigravity, Kiro CLI. Verified from README install table; individual skill bodies not fetched directly (Partially verified).
> **Dependencies:** Expo CLI, EAS CLI for deploy/build skills.
> **Availability:** Public, free; MIT.
> **Maintenance:** Active (README updated ~15 days before 2026-10-10).
> **License:** MIT (per badge)
> **Limitations:** README itself not fully fetched (snippet-level inspection); skill-count and install table verified via two independent secondary mirrors plus skills.sh badge.
> **Related resources:** vercel-labs/agent-skills `react-native-guidelines`, Cap-go/capgo-skills, callstack/software-mansion RN skills (leads), thenaubit/explora-app-example `expo-skill-eval` (evaluator lead).
> **Sources:** https://github.com/expo/skills; https://docs.expo.dev/skills/; https://github.com/deepuchauhan4728-sys/skills (mirror README)
> **Verification date:** 2026-10-10
> **Confidence:** Medium-high. **Verification: Partially verified.**

### 2.4 Hugging Face — huggingface/skills

> **Resource name:** Hugging Face Skills (huggingface/skills)
> **Canonical identity:** huggingface/skills on GitHub — "Give your agents the power of the Hugging Face ecosystem"
> **Category:** Official company skills — ML/AI (datasets, training, evals, serving)
> **Type:** Skill collection + multi-agent plugin packaging + Hub marketplace
> **Official URL:** https://github.com/huggingface/skills
> **Description:** Official Hugging Face skills for AI/ML tasks: `hf-cli` (the bootstrap skill — Hub CLI generated from the locally installed CLI so it stays current), 6 `hf-cloud-*` SageMaker/AWS skills, `hf-mem`, `huggingface-best`, `huggingface-community-evals`, `huggingface-datasets`, `huggingface-gradio`, `huggingface-llm-trainer`, `huggingface-local-models`, `huggingface-lora-space-builder`, `huggingface-paper-publisher`, `huggingface-papers`, `huggingface-spaces`, `huggingface-tool-builder`, `huggingface-trackio`, `huggingface-vision-trainer`, `huggingface-zerogpu`, `train-sentence-transformers`, `transformers-js`, `trl-training` (~28 skills).
> **Contents inspected:** README fetched 2026-10-10. Install paths: Claude Code plugin marketplace (`/plugin marketplace add huggingface/skills`, `/plugin install hf-cli@huggingface/skills`, extra skills via `hf skills add <skill-name>`); Codex (copy/symlink into `.agents/skills`); Gemini CLI (`gemini extensions install https://github.com/huggingface/skills.git`); Cursor plugin manifests (`.cursor-plugin/plugin.json`, `.mcp.json` with the HF MCP server URL); `hf skills add/list/preview/update` CLI from the Hub CLI itself; AGENTS.md fallback (`agentsmd/AGENTS.md`); publish script `./scripts/publish.sh` regenerating manifests; internal marketplace `marketplace-internal.json` uploaded to the Hub so `hf skills` commands see every skill; Skills-over-MCP discovery work noted.
> **Actual capabilities:** Executable-workflow skills that teach agents Hub operations (CLI), SageMaker deployment planning, model training (TRL/Unsloth), evals (inspect-ai/lighteval), datasets, Spaces/Gradio, papers, and serving-image selection — with helper scripts per skill.
> **Usage domain:** Machine learning engineering (training, evaluation, serving, dataset and Hub operations).
> **Integration method:** Plugin marketplaces (Claude Code, Cursor), Gemini extension, Codex `.agents/skills`, `hf skills add` CLI, MCP integrations.
> **Compatibility (with evidence):** Documented: Claude Code, Codex, Gemini CLI, Cursor. Verified from README install sections.
> **Dependencies:** `hf` CLI (huggingface_hub), cloud CLIs/SDKs per workflow skill (AWS/SageMaker), Python ML stack.
> **Availability:** Public, free, open source.
> **Maintenance:** Active — 11,150 stars, 763 forks, 350 commits, created 2025-11-24, Apache-2.0.
> **License:** Apache-2.0
> **Limitations:** Cursor/Copilot marketplace surfaces intentionally expose only `hf-cli`; full set requires `hf skills add`.
> **Related resources:** vercel-labs/skills CLI, skills.sh, K-Dense-AI/science-superpowers (catalogued; adjacent domain).
> **Sources:** https://github.com/huggingface/skills (README fetched 2026-10-10); https://aws.amazon.com/blogs/machine-learning/deploy-hugging-face-models-on-amazon-sagemaker-ai-with-coding-agents/ (usage example)
> **Verification date:** 2026-10-10
> **Confidence:** High. **Verification: Verified.**

### 2.5 Stripe — stripe/ai

> **Resource name:** Stripe AI (stripe/ai)
> **Canonical identity:** stripe/ai on GitHub — "One-stop shop for building AI-powered products and businesses with Stripe"
> **Category:** Official company skills — payments/billing
> **Type:** Skill collection + agent SDKs + plugin packaging + MCP server docs
> **Official URL:** https://github.com/stripe/ai
> **Description:** Stripe's official repo for AI integration: SDKs (`@stripe/ai-sdk` for Vercel AI SDK, `@stripe/token-meter` for OpenAI/Anthropic/Gemini native SDKs), a remote MCP server (https://mcp.stripe.com), and a `skills/` directory of official Agent Skills — including `stripe-best-practices` (integration decisions: Checkout vs PaymentIntents, Connect, billing, tax, Treasury, webhooks, restricted API keys; version-pinned with latest API/SDK versions) — plus agent plugins for Claude Code, Codex, Cursor, Grok Build, and the Agent Plugins standard.
> **Contents inspected:** README fetched 2026-10-10. Install paths: `claude plugin install stripe@claude-plugins-official`; `codex plugin add stripe@openai-curated`; Cursor `/add-plugin stripe` / Cursor marketplace; `grok plugin install stripe --trust`; Agent Plugins standard via git URL + `providers/agent-plugins/plugin/` subdirectory; manual `npx skills add https://docs.stripe.com`. Search results confirm `skills/stripe-best-practices` carries MIT license, Copyright Stripe, is vendored widely (vendored copies carry PROVENANCE.md with commit refs), and is described as "Stripe's official Codex skill."
> **Actual capabilities:** Skills that teach agents current Stripe integration best practices; SDKs for LLM billing integration; MCP server for live Stripe API access.
> **Usage domain:** Payments and billing integration for AI products.
> **Integration method:** Official plugins per agent; `npx skills add https://docs.stripe.com`; docs.stripe.com/agents.
> **Compatibility (with evidence):** Documented: Claude Code, Codex, Cursor, Grok Build, Agent Plugins standard (agent-plugins.org). Verified from README install matrix.
> **Dependencies:** Stripe account / Stripe CLI (`stripe sandbox create` for no-registration sandbox keys); SDKs per language.
> **Availability:** Public, free; MCP server via OAuth.
> **Maintenance:** Active — 1,865 stars, 353 forks, 429 commits, MIT.
> **License:** MIT
> **Limitations:** Skill content itself (beyond `stripe-best-practices` metadata) inspected via vendored copies only; skills emphasize Stripe's latest API versions and go stale quickly.
> **Related resources:** https://docs.stripe.com/agents, https://docs.stripe.com/mcp, agentskillexchange.com Stripe skill entries.
> **Sources:** https://github.com/stripe/ai (README fetched 2026-10-10); vendored SKILL.md copies at e.g. https://github.com/jimmyzhu7/coverage/blob/HEAD/.agents/skills/stripe-best-practices/SKILL.md
> **Verification date:** 2026-10-10
> **Confidence:** High. **Verification: Verified.**

### 2.6 Trail of Bits — trailofbits/skills

> **Resource name:** Trail of Bits Skills Marketplace (trailofbits/skills)
> **Canonical identity:** trailofbits/skills on GitHub — "Trail of Bits Claude Code skills for security research, vulnerability detection, and audit workflows"
> **Category:** Official company skills — security
> **Type:** Claude Code plugin marketplace (each plugin bundles skills)
> **Official URL:** https://github.com/trailofbits/skills
> **Description:** Trail of Bits' security skill marketplace: plugins spanning Smart Contract Security (`building-secure-contracts` with scanners for 6+ blockchains, `entry-point-analyzer`, `token-integration-analyzer`), Code Auditing (`differential-review`, `variant-analysis`, `static-analysis` with CodeQL/Semgrep/SARIF, `audit-context-building`, `supply-chain-risk-auditor`, `testing-handbook-skills`, `trailmark`, `c-review`, `rust-review`, `semgrep-rule-creator`, `sharp-edges`, `insecure-defaults`, `agentic-actions-auditor`, `fp-check`, `dimensional-analysis`, `vulnerability-triage-brocards`), Malware Analysis (`yara-authoring`), Verification (`constant-time-analysis`, `mutation-testing`, `post-patch-validation`, `property-based-testing`, `spec-to-code-compliance`, `writing-lean-proofs`, `zeroize-audit`), Reverse Engineering (`dwarf-expert`), Mobile Security (`firebase-apk-scanner`), Development (`modern-cpp`, `modern-python`, `gh-cli`, `git-cleanup`, `github-triage`, `code-improver`, `second-opinion`, `review-walkthrough`, `open-sourcing`, `devcontainer-setup`, `goal-prompt`), Team Management (`culture-index`), Tooling (`chrome-mcp-troubleshooting`). Includes a "Trophy Case" of bugs found using the skills (e.g., timing side-channel in ML-DSA signing).
> **Contents inspected:** README fetched 2026-10-10 — full plugin table with descriptions; `plugins/` directory layout; `AGENTS.md` authoring guidelines; `make check` CI; `agents/openai.yaml` noted for ChatGPT workspace imports.
> **Actual capabilities:** Advisory prompt/skill packs for security auditing, variant analysis, fuzzing, static analysis, YARA authoring, smart-contract scanning — Codex/Claude "reasons with them, nothing auto-blocks" (per consumer skill metadata).
> **Usage domain:** Security research, vulnerability detection, audit workflows, secure development.
> **Integration method:** Claude Code marketplace (`/plugin marketplace add trailofbits/skills`, `/plugin menu`); Codex marketplace compatibility (`codex plugin marketplace add trailofbits/skills`); ChatGPT Workspace Marketplace via `.claude-plugin/marketplace.json`.
> **Compatibility (with evidence):** Documented: Claude Code natively; Codex via Claude marketplace compatibility; ChatGPT workspace with `agents/openai.yaml` metadata requirements. NOT packaged for skills.sh `npx skills add` (no evidence).
> **Dependencies:** Security tooling per skill (Slither, Echidna, Medusa, CodeQL, Semgrep, YARA-X, etc.).
> **Availability:** Public, free, open source.
> **Maintenance:** Active — 7,450 stars, 634 forks, 207 commits, created 2026-01-14.
> **License:** CC-BY-SA-4.0 (notable: share-alike, not MIT/Apache)
> **Limitations:** Plugin-marketplace distribution is Claude/Codex-centric; skills are advisory (no automated enforcement); consumers warn against bulk-installing all ~50 plugins ("catalogue tax").
> **Related resources:** getsentry/skills (security-review overlap), Pantheon-Security/medusa and alonw0/secure-skills (catalogued), cisco-ai-defense/skill-scanner.
> **Sources:** https://github.com/trailofbits/skills (README fetched 2026-10-10); https://github.com/prekzursil/agent-skills-toolchain (consumer metadata)
> **Verification date:** 2026-10-10
> **Confidence:** High. **Verification: Verified.**

### 2.7 Microsoft — microsoft/skills

> **Resource name:** Microsoft Agent Skills (microsoft/skills)
> **Canonical identity:** microsoft/skills on GitHub — "Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents"
> **Category:** Official company skills — cloud (Azure/Foundry), language SDKs
> **Type:** Skill collection (174–175 skills) + custom agents + MCP configs + docs site + evals
> **Official URL:** https://github.com/microsoft/skills
> **Description:** Microsoft's official skills for Azure SDK and Microsoft AI Foundry development: Core (11 — `cloud-solution-architect`, `copilot-sdk`, `mcp-builder`, `frontend-design-review`, `github-primer-brand`, `skill-creator`, `entra-agent-id`, etc.), Foundry language-agnostic (11 — `microsoft-foundry` router, projects/resources, models, hosted agents, toolboxes, workflows, IQ knowledge bases, managed skills, memory, observability, governance), and per-language Azure SDK skills: Python (39), .NET (28), TypeScript (25), Java (25), Rust (7) — each named `<service>-<lang>` (e.g., `azure-cosmos-db-py`). Also ships custom agents (backend/frontend/infrastructure/planner), AGENTS.md templates, MCP configs, a Skill Explorer site (175 skills, 1-click install), and test coverage including Vally evaluations and Ralph Loop/Sensei patterns.
> **Contents inspected:** README fetched 2026-10-10 (first ~460 of 1120 lines): full skill catalog tables with descriptions, language counts, repo structure, install methods, testing section. Explicitly marked "Work in Progress."
> **Actual capabilities:** Domain knowledge activation for Azure SDKs/Foundry — service-specific skills per language; architecture/design skills; a `skill-creator` meta-skill.
> **Usage domain:** Azure cloud development, AI Foundry agent platform, per-language SDK usage.
> **Integration method:** `npx skills add microsoft/skills` (wizard); manual copy/symlink into agent dirs (`.github/skills/` for Copilot, `.opencode/skills`, `.claude/skills`); Skill Explorer 1-click install.
> **Compatibility (with evidence):** Documented: GitHub Copilot (VS Code + CLI), Claude Code, Codex, Cursor, OpenCode via skills.sh. README warns "Use skills selectively — loading all skills causes context rot."
> **Dependencies:** Azure SDKs, Azure CLI/`azd`, Foundry MCP per skill.
> **Availability:** Public, free, open source.
> **Maintenance:** Active WIP — 3,095 stars, 350 forks, 778 commits, created 2026-01-16, MIT.
> **License:** MIT
> **Limitations:** Explicitly work-in-progress; skills being updated to latest SDK patterns; largest collection risks context bloat (their own docs warn about it).
> **Related resources:** vercel-labs/skills CLI, microsoft skill explorer (microsoft.github.io), hashicorp/skills (adjacent IaC domain).
> **Sources:** https://github.com/microsoft/skills (README fetched 2026-10-10); https://devblogs.microsoft.com (blog post referenced)
> **Verification date:** 2026-10-10
> **Confidence:** High. **Verification: Verified.**

### 2.8 Figma — figma/mcp-server-guide (+ Figma plugin skills)

> **Resource name:** Figma MCP Server Guide skills (figma/mcp-server-guide)
> **Canonical identity:** figma/mcp-server-guide on GitHub (Figma official)
> **Category:** Official company skills — design/UI (Figma canvas operations)
> **Type:** Skill collection + MCP server guide + standalone workflow skills
> **Official URL:** https://github.com/figma/mcp-server-guide
> **Description:** Figma's official guide repo for the Figma MCP server, containing: `skills/` (skills bundled with the Figma plugin — `figma-use`, `figma-generate-design`, `figma-generate-library`, `figma-code-connect`, plus `figma-implement-design`, `figma-create-design-system-rules`, `figma-create-new-file` per consumer indexes), standalone `workflow-skills/` (`video-interaction-mapper` — UI recordings to annotated Figma storyboards; `generate-project-plan` — PRD to FigJam project plan), plus `figma-power` and `skills-figquery` directories. A companion community surface exists at figma.com/community/skills. The Figma Help Center documents the same skill set for "supported agents" under the terms connector/extension/power depending on agent.
> **Contents inspected:** README fetched 2026-10-10 — repo tree (`skills/`, `workflow-skills/`, `figma-power/`, `skills-figquery/`, `.claude-plugin`, `.cursor-plugin`, `.mcp.json`, `gemini-extension.json`, `server.json`); install sections for VS Code, Cursor (`/add-plugin figma`), Claude Code (`claude plugin install figma@claude-plugins-official`), Gemini CLI; "Tools and skills" section distinguishing plugin-bundled skills vs standalone workflow skills. Secondary index (atebit/ai-product-design-resources) describes individual skill bodies as "dense operational SKILL.mds, not vibes" (e.g., `figma-generate-design` mandates a six-step workflow with hard gates). Individual SKILL.md bodies not fetched directly.
> **Actual capabilities:** Skills that teach agents to act on the Figma canvas via the Figma MCP server (generate screens from component libraries, generate libraries from code, Code Connect mappings, implement designs as code) — the only skills in this survey that make an agent a Figma operator rather than a code generator.
> **Usage domain:** Design-to-code, code-to-design, design-system management in Figma.
> **Integration method:** Bundled with the Figma plugin for Claude Code/Cursor; manual MCP server connection (`https://mcp.figma.com/mcp`); Gemini extension; standalone skills copied from repo.
> **Compatibility (with evidence):** Documented: Claude Code (via claude-plugins-official), Cursor (`/add-plugin figma`), VS Code (GitHub Copilot), Gemini CLI. The MCP connection is required for skills to "actually do anything." Rate limits noted: Starter/View/Collab seats limited to ~6 tool calls/month; Dev/Full seats on paid plans get per-minute limits.
> **Dependencies:** Figma MCP server connection; Figma account/seat; skills are in Beta.
> **Availability:** Public repo; write-to-canvas is a beta feature, planned as usage-based paid eventually.
> **Maintenance:** Active — 2,058 stars, 202 forks, 81 commits, created 2025-08-05. License not shown in fetched portion — **Not verified**.
> **License:** Not verified (not shown in fetched README portion)
> **Limitations:** Beta status; seat/plan-gated MCP usage; individual skill bodies verified only via secondary descriptions.
> **Related resources:** https://www.figma.com/community/skills; Figma Help Center Dev Mode MCP Server guide; nanlabs/agent-toolkit Figma skill family (consumer).
> **Sources:** https://github.com/figma/mcp-server-guide (README fetched 2026-10-10); https://github.com/atebit/ai-product-design-resources (skill-content description)
> **Verification date:** 2026-10-10
> **Confidence:** Medium-high. **Verification: Partially verified.**

### 2.9 Netlify — netlify/context-and-tools

> **Resource name:** Netlify Context and Tools (netlify/context-and-tools)
> **Canonical identity:** netlify/context-and-tools on GitHub — "Public Netlify skills for AI coding agents"
> **Category:** Official company skills — deployment/hosting platform
> **Type:** Skill collection (15 skills) + multi-agent plugin packaging + npm distribution + hosted manifest
> **Official URL:** https://github.com/netlify/context-and-tools
> **Description:** Netlify's official skill collection: 15 factual platform-primitive skills — `netlify-functions`, `netlify-edge-functions`, `netlify-blobs`, `netlify-database` (managed Postgres via Neon + Drizzle), `netlify-image-cdn`, `netlify-forms`, `netlify-config` (netlify.toml), `netlify-frameworks` (Vite/Astro/TanStack/Next.js), `netlify-caching`, `netlify-ai-gateway` (LLM proxy), `netlify-identity`, `netlify-deploy`, `netlify-access-control`, `netlify-agent-runner` (run Claude/Codex/Gemini tasks remotely), `netlify-mcp-servers`. Each skill is a focused factual reference designed so agents "build correctly on Netlify without needing to search docs."
> **Contents inspected:** README fetched 2026-10-10 — full skill table with coverage notes, `references/` per skill, install matrix per agent, hosted distribution design (`https://netlify-agent-skills.netlify.app` manifest.json + immutable `v/<version>/` git-archive bytes, per-file SHA-256, `tree_hash` staleness check, per-skill independent versioning), `@netlify/skills` npm package with `netlify-skills` install CLI (`add`/`check`/`update`), multi-agent generation (Cursor `.mdc` rules, Codex `AGENTS.md` router auto-generated by CI — never hand-edited), plugin marketplace entries per agent, bundled Netlify MCP server (OAuth, https://netlify-mcp.netlify.app/mcp).
> **Actual capabilities:** Reference skills for Netlify platform primitives; an installer CLI; version-pinned hosted skill distribution with integrity hashes.
> **Usage domain:** Deploying and operating sites/apps on Netlify.
> **Integration method:** `npx @netlify/skills@latest add --all` (writes into detected agent dir); Claude Code marketplace (`netlify-skills@netlify-context-and-tools`); VS Code agent plugins; Cursor plugin marketplace; Codex plugin directory; Grok Build xAI marketplace; Gemini CLI extension; manual copy.
> **Compatibility (with evidence):** Documented per-agent table: Claude Code (`.claude/skills/`), Cursor/Codex/Gemini CLI/GitHub Copilot/VS Code (`.agents/skills/`), Grok Build (`.grok/skills/`), anything else via `--dest`. Verified from README install matrix.
> **Dependencies:** Netlify CLI for deploy skills; Netlify account; MCP server OAuth.
> **Availability:** Public, free; MIT; 25 releases via release-please.
> **Maintenance:** Active — 299 commits, created 2025-11-26, MIT (star count low at fetch: 39 — README data; treat as approximate).
> **License:** MIT
> **Limitations:** Skills are deliberately factual/non-opinionated (no framework/ORM opinions); generated Cursor/Codex outputs lag the `skills/` source of truth.
> **Related resources:** netlify-labs/nax (Agent Runner workflows skill), vercel-labs/agent-skills `vercel-deploy-claimable` (adjacent).
> **Sources:** https://github.com/netlify/context-and-tools (README fetched 2026-10-10); https://www.npmjs.com/package/@netlify/skills
> **Verification date:** 2026-10-10
> **Confidence:** High. **Verification: Verified.**

### 2.10 Angular — angular/skills

> **Resource name:** Angular Skills (angular/skills)
> **Canonical identity:** angular/skills on GitHub (Angular team)
> **Category:** Official company skills — frontend framework (Angular)
> **Type:** Skill collection (2 skills)
> **Official URL:** https://github.com/angular/skills
> **Description:** The Angular team's official agent skills: `angular-developer` (idiomatic Angular code generation and architectural guidance — signals, linkedSignal, resource/httpResource, forms, DI, routing, SSR, a11y/ARIA, animations, styling, testing, CLI) and `angular-new-app` (scaffolding new apps with modern best practices). Contributions are made in the angular/angular repo and mirrored here by infrastructure.
> **Contents inspected:** README via search-result snippet (2026-10-10); corroborated by independent consumers (georgeshani/skills stack guide, saschb2b/skills commit, dzebovski/kolss-crm-angular AGENTS.md). Targets Gemini CLI, Antigravity "and more"; install via `npx skills add https://github.com/angular/skills`. Individual SKILL.md bodies not fetched.
> **Actual capabilities:** Framework-authoritative guidance skills for modern (signal-based, standalone) Angular development and app scaffolding.
> **Usage domain:** Angular application development.
> **Integration method:** `npx skills add https://github.com/angular/skills`; skills.sh ecosystem.
> **Compatibility (with evidence):** Documented: Gemini CLI, Antigravity, "more"; skills.sh-compatible (per README). Consumer AGENTS.md shows Codex/Cursor usage via `.agents/skills`.
> **Dependencies:** Angular CLI for scaffolding skill.
> **Availability:** Public, free.
> **Maintenance:** Active (updated ~4 days before 2026-10-10). License not verified from snippet.
> **License:** Not verified
> **Limitations:** Only 2 skills; content freshness tied to angular/angular release cadence; individual skill bodies not directly inspected.
> **Related resources:** analogjs/angular-skills (Analog official, finer-grained: angular-component/signals/forms/routing/http/di — lead, partially verified via awesome-frontend-skills table), vercel-labs/agent-skills (React counterpart).
> **Sources:** https://github.com/angular/skills; https://github.com/jwv123/awesome-frontend-skills (Analog entry)
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 2.11 Supabase — supabase/agent-skills

> **Resource name:** Supabase Agent Skills (supabase/agent-skills)
> **Canonical identity:** supabase/agent-skills on GitHub — "Agent Skills to help developers using AI agents with Supabase"
> **Category:** Official company skills — backend/database
> **Type:** Skill collection (2 skills) + Claude Code plugin + `.well-known` distribution
> **Official URL:** https://github.com/supabase/agent-skills
> **Description:** Supabase's official skills: `supabase` (comprehensive skill covering Postgres, Auth, Storage, Realtime, Edge Functions, RLS, migrations, supabase CLI/MCP, vectors, cron, queues; security-first patterns like service-role vs anon key separation) and `supabase-postgres-best-practices` (Postgres performance guidelines in 8 impact-ranked categories: query perf, connection management, schema design, concurrency/locking, security & RLS, data access patterns, monitoring, advanced features). Compatible with 18+ AI agents.
> **Contents inspected:** README fetched 2026-10-10 — skill descriptions, usage triggers, skill structure (SKILL.md + references/), and a `.well-known` discovery mechanism: each release uploads `dist/index.json` conforming to the agent-skills `.well-known` URI spec (schema v0.2.0), consumed by supabase.com at `https://supabase.com/.well-known/agent-skills/`; release artifacts built by `scripts/build-release.ts` via Release Please. A planned migration to a `agentskills/build-for-well-known` GitHub Action (intended for transfer to the agentskills org) is documented.
> **Actual capabilities:** Backend/database skills for correct Supabase usage; machine-readable `.well-known` skill index for agent discovery.
> **Usage domain:** Supabase/Postgres backend development.
> **Integration method:** `npx skills add supabase/agent-skills` (all or `--skill supabase` / `--skill supabase-postgres-best-practices`); Claude Code plugin marketplace (`supabase@supabase-agent-skills`, `postgres-best-practices@supabase-agent-skills`); `.well-known` discovery.
> **Compatibility (with evidence):** Documented: "Compatible with 18+ AI agents including Claude Code, GitHub Copilot, Cursor, Cline, and many others." Verified from README.
> **Dependencies:** Supabase CLI + Docker for local dev; Supabase project for live work.
> **Availability:** Public, free; MIT; 9 releases.
> **Maintenance:** Active — 2,706 stars, 217 forks, 96 commits, created 2026-01-16, MIT.
> **License:** MIT
> **Limitations:** Only 2 skills; individual SKILL.md bodies not fetched (descriptions verified from README + consumer copies).
> **Related resources:** neondatabase/agent-skills, ClickHouse/agent-skills (adjacent database skills), supabase.com AI skills docs.
> **Sources:** https://github.com/supabase/agent-skills (README fetched 2026-10-10); https://github.com/jonathanhefner/agentskills-build-for-well-known (referenced action)
> **Verification date:** 2026-10-10
> **Confidence:** High. **Verification: Verified.**

### 2.12 Neon — neondatabase/agent-skills (+ neondatabase/neon-for-agent-platforms)

> **Resource name:** Neon Agent Skills (neondatabase/agent-skills)
> **Canonical identity:** neondatabase/agent-skills on GitHub (Neon, now Databricks "Lakebase Postgres")
> **Category:** Official company skills — database/backend platform
> **Type:** Skill collection + plugin manifests
> **Official URL:** https://github.com/neondatabase/agent-skills
> **Description:** Neon's official agent skills: `neon-postgres` (SQL dev, schema design, perf, autoscaling), `neon-postgres-branches` (branch types for dev/preview/test/CI), `neon-object-storage`, `neon-functions` (long-running/streaming serverless), `neon-ai-gateway` (one-credential LLM routing via OpenAI-compatible `/v1/models`), `claimable-postgres` (instant claimable temp databases), `neon-postgres-egress-optimizer` (egress cost diagnosis), plus `neon-auth` (managed Better Auth) and `neon-postgres-agent-platforms` in the sibling repo neondatabase/neon-for-agent-platforms.
> **Contents inspected:** Secondary sources only (mirrored AGENTS.md files and consumer SKILL.md tables, 2026-10-10). Notable: CI validates every skill via a `skills-ref` validator tool (`npm run validate:skills` / `validate:ci`), with SHA-pinned Actions, exact-pinned deps, and `harden-runner` egress audit; Cursor and Claude plugin manifests under `plugins/`.
> **Actual capabilities:** Database/backend platform skills for Neon/Lakebase Postgres workflows.
> **Usage domain:** Serverless Postgres, branching, AI gateway, object storage on Neon.
> **Integration method:** skills.sh ecosystem (`skillkit install neondatabase/agent-skills`); Claude/Cursor plugin manifests in-repo.
> **Compatibility (with evidence):** Partially documented via mirrors: Claude Code, Cursor, Codex agent dirs. Not verified from primary README.
> **Dependencies:** Neon account/API; network access for docs.
> **Availability:** Public, free. License not verified from inspected sources.
> **License:** Not verified
> **Maintenance:** Active (mirrors updated within days of 2026-10-10); two-repo shared CI kept in sync.
> **Limitations:** Primary README not fetched; skill list assembled from two independent consumer mirrors.
> **Related resources:** neondatabase/neon-for-agent-platforms, supabase/agent-skills, netlify/context-and-tools `netlify-database` (Neon-backed).
> **Sources:** https://github.com/neondatabase/agent-skills; https://github.com/neondatabase/neon-for-agent-platforms; mirrored AGENTS.md at https://github.com/yavasdev/skills-collection/blob/HEAD/skills/neondatabase--agent-skills/AGENTS.md
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 2.13 ClickHouse — ClickHouse/agent-skills

> **Resource name:** ClickHouse Agent Skills (ClickHouse/agent-skills)
> **Canonical identity:** ClickHouse/agent-skills on GitHub — "The official Agent Skills for ClickHouse and ClickHouse Cloud"
> **Category:** Official company skills — database/analytics
> **Type:** Skill collection
> **Official URL:** https://github.com/ClickHouse/agent-skills
> **Description:** Official ClickHouse skills for open-source ClickHouse and ClickHouse Cloud plus `chdb` (in-process ClickHouse for Python): schema design, query optimization, data ingestion patterns, in-process analytics.
> **Contents inspected:** README via search-result snippet (2026-10-10). Install: `npx skills add clickhouse/agent-skills` or via the `clickhousectl` CLI (`clickhousectl skills`). Follows the agentskills.io spec. Individual SKILL.md bodies not fetched.
> **Actual capabilities:** Analytics-database best-practice skills.
> **Usage domain:** ClickHouse schema/query/ingestion work.
> **Integration method:** `npx skills add clickhouse/agent-skills`; `clickhousectl skills`.
> **Compatibility (with evidence):** Skills.sh ecosystem (npx skills) documented; "Claude Code, Cursor, Copilot, etc." named in README snippet.
> **Dependencies:** ClickHouse instance or Cloud account for live work.
> **Availability:** Public, free. License/maintenance metrics not verified from snippet.
> **License:** Not verified
> **Maintenance:** Active (updated ~29 days before 2026-10-10).
> **Limitations:** Snippet-level inspection only; skill inventory not enumerated.
> **Related resources:** https://github.com/ClickHouse/clickhousectl, supabase/agent-skills, neondatabase/agent-skills.
> **Sources:** https://github.com/ClickHouse/agent-skills
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 2.14 HashiCorp — hashicorp/agent-skills

> **Resource name:** HashiCorp Agent Skills (hashicorp/agent-skills)
> **Canonical identity:** hashicorp/agent-skills on GitHub
> **Category:** Official company skills — infrastructure as code
> **Type:** Skill collection organized as Claude Code/Codex product plugins
> **Official URL:** https://github.com/hashicorp/agent-skills
> **Description:** HashiCorp's official agent skills for Terraform and Packer, distributed as product plugins: `terraform-code-generation` (terraform-style-guide, terraform-test, azure-verified-modules, terraform-search-import), `terraform-module-generation` (refactor-module, terraform-stacks), `terraform-provider-development` (new-terraform-provider, run-acceptance-tests, provider-actions, provider-resources, provider-test-patterns), `terraform-policy-code` (tfpolicy-author, tfpolicy-test), plus Packer plugins (packer-builders, packer-hcp). A dedicated `@hashicorp/team-agent-skills-ecosystem` team owns conventions; every skill requires `name`, `description`, and `metadata.lifecycle-status` (active/deprecation-candidate/deprecated/retired) and passes structural validation plus "private Waza evaluation."
> **Contents inspected:** terraform/README.md and consumer AGENTS.md via search results (2026-10-10); vendored skill bodies (terraform-style-guide, terraform-search-import, refactor-module) inspected via consumer mirrors — each carries `metadata.github-repo` provenance fields (repo, path, ref, tree SHA, version).
> **Actual capabilities:** IaC skills for generating/validating HCL, module refactoring, provider development, policy-as-code, Packer image builds.
> **Usage domain:** Terraform/Packer infrastructure development.
> **Integration method:** `npx skills add hashicorp/agent-skills` (list) or deep path install; Claude Code marketplace plugins (`terraform-code-generation@hashicorp` etc.); Codex plugin manifests at product roots.
> **Compatibility (with evidence):** Documented: GitHub Copilot, Claude Code, OpenCode, Cursor via npx skills; Claude Code plugin marketplace; Codex manifests.
> **Dependencies:** Terraform/OpenTofu CLIs, provider credentials for live work.
> **Availability:** Public, free. License not verified from inspected sources.
> **License:** Not verified
> **Maintenance:** Active (updated ~43 days before 2026-10-10); ecosystem team with CODEOWNERS review.
> **Limitations:** Primary repo README not fetched; skill inventory from terraform/README.md snippet + mirrors.
> **Related resources:** microsoft/skills (Azure skills overlap via azure-verified-modules), ekipo/hashicorp-agent-skills (community mirror).
> **Sources:** https://github.com/hashicorp/agent-skills/blob/HEAD/terraform/README.md; mirrored skill bodies via https://github.com/h3y6e/agent-skills
> **Verification date:** 2026-10-10
> **Confidence:** Medium-high. **Verification: Partially verified.**

### 2.15 Better Auth — better-auth/skills

> **Resource name:** Better Auth Skills (better-auth/skills)
> **Canonical identity:** better-auth/skills on GitHub (Better Auth official)
> **Category:** Official company skills — authentication
> **Type:** Skill collection (6 skills)
> **Official URL:** https://github.com/better-auth/skills
> **Description:** Official Better Auth skill pack (documented at better-auth.com/docs/ai-resources/skills): `best-practices`, `create-auth`, `emailAndPassword`/`email-and-password-best-practices`, `organization`/`organization-best-practices`, `twoFactor`/`two-factor-authentication-best-practices`, and `security`/`better-auth-security-best-practices`.
> **Contents inspected:** Secondary sources only (2026-10-10): provider-registry issue (dmgrok/agent_skills_directory#22) listing skills; consumer docs (socialrobot-io/reflow SKILLS.md, sprioleau/flock commit, miinhho/setup-project-skills auth table) confirming the six skills and install commands (`npx skills add better-auth/skills -y -p -s '*'`; Codex skill-installer with pinned refs).
> **Actual capabilities:** Auth scaffolding and best-practice skills for Better Auth (TypeScript auth framework).
> **Usage domain:** Authentication/authorization implementation in TypeScript apps.
> **Integration method:** `npx skills add better-auth/skills`; Codex skill installer (pinned git refs).
> **Compatibility (with evidence):** skills.sh ecosystem; Codex installer documented by consumers. Not verified from primary README.
> **Dependencies:** better-auth npm package.
> **Availability:** Public, free. License/maintenance not verified from primary.
> **License:** Not verified
> **Limitations:** No primary README fetched; inventory from three independent consumers (consistent).
> **Related resources:** auth0/agent-skills, clerk/skills (adjacent official auth skills — leads), https://better-auth.com/docs/ai-resources/skills
> **Sources:** https://github.com/better-auth/skills; https://github.com/dmgrok/agent_skills_directory/issues/22; https://github.com/socialrobot-io/reflow/blob/HEAD/docs/SKILLS.md
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 2.16 TestMu AI (LambdaTest) — LambdaTest/agent-skills

> **Resource name:** LambdaTest Agent Skills (LambdaTest/agent-skills)
> **Canonical identity:** LambdaTest/agent-skills on GitHub (TestMu AI, formerly LambdaTest)
> **Category:** Official company skills — testing/QA
> **Type:** Skill collection (per-framework skills)
> **Official URL:** https://github.com/LambdaTest/agent-skills
> **Description:** TestMu AI's official per-framework test-automation skills: `selenium-skill`, `appium-skill`, `playwright-skill`, `cypress-skill`, `webdriverio-skill`, `jest-skill`, `junit-5-skill`, `pytest-skill`, `testng-skill`, `puppeteer-skill`, `mocha-skill`, `smartui-skill` (visual regression), `hyperexecute-skill` (orchestration), `cicd-pipeline-skill`, `test-framework-migration-skill` — a "senior QA automation architect" skill per framework, targeting the TestMu AI cloud (5000+ real devices, 10,000+ browser/device combos) or local execution.
> **Contents inspected:** Secondary sources (2026-10-10): TestMu AI docs SKILL.md (maheshr-lambdatest/documentation) with install commands (`npx skills add ... --skill selenium-skill`; `npx agentskillsforall add ...`) and the framework routing table; community registry (arnauaregall/lambdatest-agent-skills) with the 46-entry skill registry table; skillkit vendor table.
> **Actual capabilities:** QA automation skills that generate and run framework tests locally or on the TestMu AI cloud grid.
> **Usage domain:** Test automation (E2E, unit, mobile, visual regression, CI wiring).
> **Integration method:** `npx skills add https://github.com/LambdaTest/agent-skills.git --skill <name>`; `npx agentskillsforall add ...`.
> **Compatibility (with evidence):** Named: Claude Code, Copilot, Cursor, Gemini CLI. Not verified from primary README.
> **Dependencies:** Test framework CLIs; TestMu AI cloud account for cloud execution.
> **Availability:** Public repo; cloud execution is a commercial service. License not verified.
> **License:** Not verified (consumer copy declares MIT for the docs skill)
> **Maintenance:** Active (docs updated ~11 days before 2026-10-10).
> **Limitations:** No primary README fetched; inventory from docs + community registry.
> **Related resources:** https://www.testmuai.com/support/docs/llms.txt, vostride/agent-qa (adjacent, from awesome-agent-skills directory).
> **Sources:** https://github.com/LambdaTest/agent-skills; https://github.com/maheshr-lambdatest/documentation/blob/HEAD/static/docs/SKILL.md; https://github.com/arnauaregall/lambdatest-agent-skills
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 2.17 Capgo — Cap-go/capgo-skills

> **Resource name:** Capacitor Agent Skills (Cap-go/capgo-skills)
> **Canonical identity:** Cap-go/capgo-skills on GitHub (Capgo; formerly @capgo/capacitor-skills)
> **Category:** Official company skills — mobile (Capacitor)
> **Type:** Skill collection (49 skills)
> **Official URL:** https://github.com/Cap-go/capgo-skills
> **Description:** Capgo's collection of 49 skills for AI coding agents working with Capacitor (cross-platform native runtime): core dev (capgo-cli-usage, capgo-cloud, capacitor-plugins — catalog of 80+ Capgo plugins, capacitor-best-practices, capgo-live-updates OTA), security (capacitor-security with Capsec 63+ rules), testing & CI/CD, debugging & tooling (capacitor-mcp, ios-android-logs), UI & design (ionic-design, konsta-ui, tailwind-capacitor, safe-area-handling, splash screens), features (push notifications, deep linking, offline-first, keyboard, app-store). Each skill ships SKILL.md + metadata.json. Compatibility table tracks Capacitor major versions (v8 maintained, v7 on-demand, v6/v5 unmaintained).
> **Contents inspected:** README via search snippet (2026-10-10); install via `npx skills add Cap-go/capgo-skills` (also `bunx skills add`). Individual SKILL.md bodies not fetched.
> **Actual capabilities:** Mobile-development skills for Capacitor apps including OTA live updates, plugin selection, security scanning, and store submission.
> **Usage domain:** Capacitor/Capgo mobile development.
> **Integration method:** `npx skills add Cap-go/capgo-skills`.
> **Compatibility (with evidence):** skills.sh ecosystem; README compatibility table is about Capacitor versions, not agents. Agent compatibility not documented in inspected portion.
> **Dependencies:** Capacitor/Capgo CLIs, native toolchains for device work.
> **Availability:** Public, free. License not verified.
> **License:** Not verified
> **Maintenance:** Active (README updated ~88 days before 2026-10-10); 53 stars at initial commit snapshot.
> **Limitations:** Snippet-level inspection; agent-compatibility claims not found.
> **Related resources:** expo/skills, saeid-tavazani/capacitor-capgo-skill (community single-skill alternative).
> **Sources:** https://github.com/Cap-go/capgo-skills
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 2.18 OpenAI — openai/skills (legacy), openai/plugins, Codex skills docs

> **Resource name:** OpenAI Skills / Plugins (openai/skills legacy; openai/plugins current)
> **Canonical identity:** github.com/openai/skills (deprecated legacy catalog); github.com/openai/plugins (current official examples); Codex skills documentation
> **Category:** Official company — skills standard participation + examples
> **Type:** Example catalog (legacy) + plugin examples + documentation
> **Official URL:** https://github.com/openai/plugins (current); https://github.com/openai/skills (legacy, deprecated); https://developers.openai.com/codex/skills (docs, redirects to learn.chatgpt.com/docs/build-skills)
> **Description:** OpenAI's `openai/skills` catalog is explicitly deprecated for current examples (legacy/discovery source only). Current official examples live at `openai/plugins`; the Codex CLI repo ships a skill-creator sample at `codex-rs/skills/src/assets/samples/skill-creator`. Codex implements the open Agent Skills standard: SKILL.md with name/description frontmatter, optional `scripts/`, `references/`, `assets/`, and `agents/openai.yaml` interface metadata; discovery from `.agents/skills` (repo, walked to root), `$HOME/.agents/skills`, `/etc/codex/skills`, and bundled system skills; `$skill-name` invocation or `/skills` TUI; custom prompts deprecated in favor of skills; reusable distribution "should prefer Plugins" (`.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`).
> **Contents inspected:** Secondary research notes only (kanadek/codex-skill-harvester research.md, sociotechnica-org/skillmaker-studio competitive scan, ashfordeou/aero-agent-skills harness-integration.md, ucsahinn/codex-enterprise-starter research-notes.md) — all citing developers.openai.com/codex/skills and the openai/codex repo. No primary fetch of the docs or plugin examples.
> **Actual capabilities:** Documentation/specification of Codex's skill support; example plugins.
> **Usage domain:** Codex skill authoring and distribution.
> **Integration method:** `.agents/skills` directories; `.codex-plugin` plugin packaging.
> **Compatibility (with evidence):** Codex natively supports the Agent Skills standard (same SKILL.md spec as Claude Code) — stated in multiple secondary sources citing official docs; cross-compatibility described as "in principle" with Codex-specific `agents/openai.yaml` extensions.
> **Dependencies:** Codex CLI.
> **Availability:** Docs public; openai/skills deprecated.
> **Maintenance:** Active (Codex docs current as of 2026-08).
> **License:** Not verified
> **Limitations:** No primary fetch; the legacy repo is deprecated, not dead — it remains a discovery source.
> **Related resources:** agentskills/agentskills, kanadek/codex-skill-harvester (skill derivation workflow for Codex).
> **Sources:** https://developers.openai.com/codex/skills; https://github.com/openai/plugins; https://github.com/openai/skills; https://github.com/openai/codex
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 2.19 Anthropic — Claude Skills gallery + anthropics/knowledge-work-plugins

> **Resource name:** Claude Skills gallery (claude.com/skills); anthropics/knowledge-work-plugins
> **Canonical identity:** Anthropic official — https://claude.com/skills ; https://github.com/anthropics/knowledge-work-plugins
> **Category:** Official company skills — knowledge work / document skills
> **Type:** Managed skill gallery + plugin repository (11 plugins)
> **Official URL:** https://claude.com/skills
> **Description:** Anthropic's official gallery of prebuilt skills (PowerPoint, Excel, Word, PDF "and more") for Claude apps/API/Code — Pro/Max/Team/Enterprise, admin approval for Team/Enterprise. The API exposes Anthropic-managed skills (`api.anthropic.com/v1/skills?source=anthropic`: pptx, xlsx, docx, pdf). Separately, `anthropics/knowledge-work-plugins` is Anthropic's open-source repo of 11 plugins built for knowledge workers using Claude Cowork (desktop app), with connectors for Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 — a ~44-skill "small business" bundle is also reported in the ecosystem press. Distinct from `anthropics/skills` (developer/terminal-focused, already catalogued).
> **Contents inspected:** Secondary sources only (computerworld.com article on the 4 prebuilt API skills; seangsisg/claude-code-docs API quickstart; medium.com article on knowledge-work-plugins; artificiallyintimidating.com on the small-business plugin). No primary fetch of claude.com/skills.
> **Actual capabilities:** Managed document skills (create/edit Office docs and PDFs) and knowledge-work plugins with third-party connectors.
> **Usage domain:** Document creation/editing, knowledge-work automation in Claude.
> **Integration method:** Claude settings/plugins UI; Skills API (`source=anthropic`); Cowork plugin discovery.
> **Compatibility (with evidence):** Claude apps, Claude Code, API — per Anthropic docs cited in secondaries. Portability to other agents not documented (managed skills, not file-based SKILL.md distribution).
> **Dependencies:** Claude Pro/Max/Team/Enterprise subscription; admin approval on Team/Enterprise.
> **Availability:** Commercial (subscription-gated).
> **Maintenance:** Active. License: proprietary/managed (not open source).
> **License:** Not applicable (proprietary managed skills)
> **Limitations:** Not file-based open skills; secondary-source verification only; exact gallery inventory not enumerated from primary.
> **Related resources:** anthropics/skills (catalogued), platform.claude.com Agent Skills Cookbook.
> **Sources:** https://claude.com/skills; https://www.computerworld.com/article/4074959/claude-just-got-a-skill-upgrade-and-it-s-coming-for-your-workflows.html; https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

**Further official-company leads (not verified, noted for follow-up):** `auth0/agent-skills`, `clerk/skills` (multiple clerk-* skills: setup, backend-api, cli, orgs, webhooks, testing, nextjs-patterns, expo, android), `resend/resend-skills`, `temporalio/skill-temporal-developer`, `software-mansion` RN skills, `callstack` agent skills, `getsentry/sentry-for-ai` (Sentry product skills), `google/stitch` skills (design), `openai` Figma/frontend/slides/imagegen skills (referenced in podo/design-agent-skills `openai-skills` stub).

---

## 3. Skill infrastructure — discovery and installation

### 3.1 skills.sh + `npx skills` CLI (vercel-labs/skills)

> **Resource name:** skills / skills.sh (the open agent skills tool)
> **Canonical identity:** vercel-labs/skills on GitHub; npm package `skills`; registry at https://skills.sh
> **Category:** Infrastructure — discovery + installation
> **Type:** CLI tool + web registry/leaderboard
> **Official URL:** https://github.com/vercel-labs/skills ; https://skills.sh
> **Description:** The CLI for the open agent skills ecosystem. Commands: `skills add <source>` (install from GitHub shorthand, full URL, tree path, GitLab/Azure DevOps URLs, any git URL, local path, private repos, or direct SKILL.md/archive download URLs with size limits), `skills use` (use one skill without installing — generates a prompt or starts an agent), `skills find` (keyword/interactive search, `--owner` filter), `skills list/ls`, `skills update`, `skills init` (scaffold a new SKILL.md), `skills remove/rm`, `skills check`. Supports OpenCode, Claude Code, Codex, Cursor, "and 75 more" agents — the README documents per-agent project/global skill paths for ~80 agents (e.g., `.claude/skills/`, `.agents/skills/`, `~/.codex/skills`). Installs via symlink (recommended) or copy; project vs global scope (`-g`); per-agent targeting (`-a`); skill selection (`-s`, `--list`). Also ships a `find-skills` skill (`skills/find-skills`) that teaches agents to search the registry before solving tasks from scratch. Includes a "Creating Skills" section documenting required/optional frontmatter fields and skill/plugin-manifest discovery.
> **Contents inspected:** README fetched 2026-10-10 (first ~559 of 1038 lines): full command reference with options/examples, source-format matrix, private-repo auth behavior, supported-agents table, telemetry and env-var sections noted.
> **Actual capabilities:** Universal skill installer, updater, finder, scaffolder, and remover across git hosts and ~80 agents; registry at skills.sh with install leaderboard and per-skill pages (skills.sh/<owner>/<repo>/<skill>).
> **Usage domain:** Skill discovery, installation, lifecycle management for any agent.
> **Integration method:** `npx skills` / `npx skills@latest`; npm package `skills`.
> **Compatibility (with evidence):** Documented: ~80 agents with explicit skill directories (Claude Code, Codex, Cursor, OpenCode, Gemini CLI, Copilot, Cline, Windsurf, Zed, Antigravity, OpenClaw, etc.). Verified from README agents table.
> **Dependencies:** Node.js/npx; git + credentials for private repos.
> **Availability:** Public, free; MIT.
> **Maintenance:** Very active — 33,551 stars, 2,873 forks, 570 commits, 49 releases, created 2026-01-14, MIT.
> **License:** MIT
> **Limitations:** No built-in trust/security scanning (treat added skills as untrusted — multiple consumer skills document this rule); telemetry present (documented in README); install UX varies by agent.
> **Related resources:** skills.sh registry, alex-1q84/skillkit and rohitg00/skillkit (alternative managers), agentskillexchange.com (alternative registry).
> **Sources:** https://github.com/vercel-labs/skills (README fetched 2026-10-10); https://skills.sh
> **Verification date:** 2026-10-10
> **Confidence:** High. **Verification: Verified.**

### 3.2 skillkit variants (multi-agent skill managers)

Four distinct projects share the name "skillkit" — recorded separately to avoid conflation:

**(a) rohitg00/skillkit — `@skillkit/cli` (npm).** "Command-line interface for SkillKit — install, manage, translate, and sync skills across 46 AI coding agents." Commands: `skillkit install <source>` (GitHub/GitLab/Bitbucket/local), `remove`, `update`, `list`, `enable`/`disable`, `sync`, `read`, `recommend` (project-based, stack-detected with quality scores), `marketplace` (browse/search/tags/refresh), `translate my-skill --to cursor` (format translation between agents), `ui` (interactive TUI), `serve` (API server + `@skillkit/mcp` MCP server for runtime discovery). Apache-2.0. **Verification: Partially verified** (README via search snippet). Source: https://github.com/rohitg00/skillkit

**(b) alex-1q84/skillkit (Rust).** Single-binary unified skill manager (Chinese-language README): `skillkit source add owner/repo`, `skillkit install add <source> <skill> [--scope global|local]`, `skillkit find <query>` (searches skills.sh registry, `--json` for agents), `skillkit list`, `skillkit project status/apply` (per-project desired-state management, idempotent apply to agent dirs), `skillkit serve` (local web GUI sharing the same core). Zero runtime deps. **Verification: Partially verified** (README via search snippet). Source: https://github.com/alex-1q84/skillkit

**(c) rfxlamia/skillkit (meta-skill toolkit, formerly claude-skillkit).** "The toolkit for creating reusable skills for AI coding agents" — ships two meta-skills: `skillkit` (create & validate skills/subagents, fast 12-step or full 15-step mode, 5-layer validation, quality target 9.0+/10) and `skillkit-help` (orientation: skills vs subagents). Install via `npx @rfxlamia/skillkit`; community distribution via SkillKit Marketplace (`npx @rfxlamia/sm`). Works with Claude Code, GitHub Copilot, OpenCode, Codex. **Verification: Partially verified** (README via search snippet). Source: https://github.com/rfxlamia/skillkit

**(d) saanjaypatil78/skillkit.** Documentation site variant of the SkillKit concept ("write a skill once, deploy it to all 32 agents") with REST API/MCP server/Python client docs. **Verification: Partially verified** (docs snippet). Source: https://github.com/saanjaypatil78/skillkit

**Common note:** Skill vendors increasingly document both `npx skills add <repo>` and `skillkit install <repo>` install paths (e.g., uglyrobot/docsbot-agent-skills, 222bhavesh-tech/opencode-system's skillkit vendor table listing better-auth, trailofbits, supabase, neondatabase, clickhouse, LambdaTest, vercel-labs, angular, expo, cloudflare, netlify, hashicorp vendors).

### 3.3 Hugging Face `hf skills` CLI (marketplace inside the Hub CLI)

Covered in §2.4 (huggingface/skills): `hf skills add/list/preview/update` manage Hub skills; the `hf-cli` SKILL.md is generated from the locally installed CLI (`hf skills add --force` regenerates). This is the only vendor CLI that both generates its own skill and operates a skill marketplace. **Verification: Verified** (via huggingface/skills README + generated-skill evidence in fogmoe/necro).

### 3.4 agentskillsforall CLI

Referenced by TestMu AI docs: `npx agentskillsforall list <git-url>` / `npx agentskillsforall add <git-url> --skill <name>`. No primary source located; treated as a lead. **Verification: Unverified.**

---

## 4. Validators, linters, and security scanners

### 4.1 fchastanet/ai-linter (AI Linter)

> **Resource name:** AI Linter (fchastanet/ai-linter)
> **Canonical identity:** fchastanet/ai-linter on GitHub
> **Category:** Infrastructure — validator/linter
> **Type:** Python validation tool (PyPI-installable, setuptools)
> **Official URL:** https://github.com/fchastanet/ai-linter
> **Description:** Validation tool for AI skills and agent configurations: validates `SKILL.md`/`AGENTS.md` against the Agent Skills Specification (agentskills.io/specification) with checks for YAML frontmatter, content length and token-count limits (500 lines, 5000 tokens), file-reference existence, code-snippet size, unreferenced resources, `.github/prompts` and `.github/agents` directories, project structure, skill-name format (hyphen-case, 1–64 chars), and description length (1–1024 chars). Purpose-built to enforce spec compliance and progressive-disclosure token efficiency.
> **Contents inspected:** `.github/copilot-instructions.md` via search snippet (2026-10-10) — project overview, Python 3.10+ stack (tiktoken, PyYAML, pyparsing, tabulate, pathspec), dev tooling (black, mypy strict, pytest, pre-commit). Tool itself not executed (read-only research).
> **Actual capabilities:** Static validation of skill repos against the spec.
> **Usage domain:** Skill authoring CI / pre-publish checks.
> **Integration method:** Python package (pip); CLI.
> **Compatibility (with evidence):** Validates against agentskills.io spec; checks `.github/prompts` and `.github/agents` (GitHub Copilot-oriented). Primary README not fetched.
> **Dependencies:** Python 3.10+; tiktoken, PyYAML, pyparsing, tabulate, pathspec.
> **Availability:** Public, free. License not verified from inspected sources.
> **License:** Not verified
> **Maintenance:** Active (updated ~179 days before 2026-10-10 — aging; flag as possibly stale).
> **Limitations:** Snippet-level inspection; no security scanning (format validation only).
> **Related resources:** spiritualhost/clinter, google/skills_lint.dart, skills-ref, agentskills.io/specification.
> **Sources:** https://github.com/fchastanet/ai-linter
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 4.2 spiritualhost/clinter

> **Resource name:** Clinter — a validator/linter for Claude Skills
> **Canonical identity:** spiritualhost/clinter on GitHub
> **Category:** Infrastructure — validator/linter
> **Type:** Python CLI (pipx-installable)
> **Official URL:** https://github.com/spiritualhost/clinter
> **Description:** Early Python linter for Claude skills: `clinter -f {path/to/SKILL.md}` validates SKILL.md format; includes a "Complete Guide to Writing Claude Skills" reference. Known gaps documented by the author: multi-line descriptions and optional frontmatter fields.
> **Contents inspected:** README via search snippet (2026-10-10). Not executed.
> **Actual capabilities:** Single-file/directory SKILL.md format validation.
> **Usage domain:** Skill authoring checks.
> **Integration method:** pipx install; CLI.
> **Compatibility (with evidence):** Claude Skills format (pre-standardization era tool).
> **Dependencies:** Python 3.
> **Availability:** Public, free. License not verified.
> **License:** Not verified
> **Maintenance:** Stale — last updated ~151 days before 2026-10-10; predates the agentskills.io spec. **Historical interest mainly.**
> **Limitations:** Outdated relative to the current spec; documented feature gaps.
> **Related resources:** fchastanet/ai-linter (successor concept), Anthropic's skill-creation docs.
> **Sources:** https://github.com/spiritualhost/clinter
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified (staleness noted).**

### 4.3 google/skills_lint.dart (Google)

> **Resource name:** skills_lint (google/skills_lint.dart)
> **Canonical identity:** google/skills_lint.dart on GitHub — Dart package `skills_lint`
> **Category:** Infrastructure — validator/linter (official Google)
> **Type:** Dart static-analysis linter + companion usage skills
> **Official URL:** https://github.com/google/skills_lint.dart
> **Description:** Google's static-analysis linter for Agent Skills, designed for presubmit checks: validates mandatory SKILL.md presence, YAML frontmatter constraints (naming, length), flat directory structure (no deep nesting), and relative-path integrity. CLI: `dart run skills_lint -d .agents/skills` (or globally activated); `--fix`/`--dry-run` auto-fixes fixable rules (`check-absolute-paths`, `check-trailing-whitespace`, `invalid-skill-name`); custom `SkillRule` classes authorable in Dart; full rule reference in RULES.md. Uniquely, the repo ships its own skills teaching agents to use it: `skills-lint-validation` (day-to-day use, failure workflows) and `skills-lint-setup` (first-time wiring, baseline generation).
> **Contents inspected:** Package skills (`skills/skills-lint-validation/SKILL.md`, `dart-skills-lint-validation` variant) and tool README via search snippets (2026-10-10); mirrored in flutter-tizen/skills (`tool/dart_skills_lint`) and qaison/agent-plugins. Tool not executed.
> **Actual capabilities:** Spec validation with auto-fix and custom rules; meta-skills for operating the linter.
> **Usage domain:** Skill repo presubmit/CI validation.
> **Integration method:** Dart pub dependency or global activation; CLI.
> **Compatibility (with evidence):** Agent Skills spec; used in Dart/Flutter-adjacent repos. Not verified from primary README.
> **Dependencies:** Dart SDK.
> **Availability:** Public, free. License not verified.
> **License:** Not verified
> **Maintenance:** Active (updated ~8 days before 2026-10-10).
> **Limitations:** Dart-ecosystem tool; snippet-level inspection.
> **Related resources:** fchastanet/ai-linter, skills-ref, flutter-tizen/skills.
> **Sources:** https://github.com/google/skills_lint.dart; https://github.com/flutter-tizen/skills/blob/HEAD/tool/dart_skills_lint/README.md
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 4.4 skills-ref (Neon CI validator)

> **Resource name:** skills-ref
> **Canonical identity:** npm tool used by neondatabase/agent-skills CI (`npm run validate:skills` → `skills-ref validate ./my-skill`)
> **Category:** Infrastructure — validator
> **Type:** npm validation tool (referenced, not directly located)
> **Official URL:** Not verified (referenced from https://github.com/neondatabase/agent-skills CI docs via mirrors)
> **Description:** Validator invoked in Neon's hardened CI (`validate.yml`) to validate every skill under `skills/` plus Cursor/Claude plugin manifests. No standalone repo page was located during this workstream.
> **Contents inspected:** Referenced in mirrored AGENTS.md files only.
> **Actual capabilities:** Unresolved beyond CI usage.
> **Usage domain:** Skill CI validation.
> **Integration method:** npm.
> **Compatibility:** Not verified.
> **Dependencies:** Not verified.
> **Availability:** Not verified.
> **Maintenance:** Not verified.
> **License:** Not verified
> **Limitations:** Existence inferred from CI references; primary source not found — needs follow-up.
> **Sources:** https://github.com/yavasdev/skills-collection/blob/HEAD/skills/neondatabase--agent-skills/AGENTS.md (mirror)
> **Verification date:** 2026-10-10
> **Confidence:** Low. **Verification: Unresolved.**

### 4.5 Security scanners for skills

Skill supply-chain risk is a live concern (malicious-skill incident research documented by AIR via lemmaoracle/lemma: a `brand-landingpage` skill cleared Cisco, Nvidia, and skills.sh scanners because the payload lived at a mutable external URL — a time-of-check/time-of-use gap). Scanners found:

**(a) cisco-ai-defense/skill-scanner (Cisco).** "Security Scanner for Agent Skills" — detects prompt injection, data exfiltration, malicious code patterns; combines pattern-based detection (YAML + YARA-X), AST/dataflow analysis, optional LLM-as-judge, and a CEL decision layer. Supports OpenAI Codex Skills and Cursor Agent Skills formats per the Agent Skills spec; `--lenient` also covers Claude Code `.claude/commands/*.md` and flat markdown repos. Apache-2.0, PyPI (`cisco-ai-skill-scanner`), CPython 3.11–3.14, CI-tested. Best-effort disclaimer. **Verification: Partially verified** (README via search snippet). Source: https://github.com/cisco-ai-defense/skill-scanner

**(b) francoischastel/skill-scanner.** Offline static analysis for prompt injection, hidden text, exfiltration, remote code; install gates for Claude Code, Codex, OpenCode, Pi, and npx skills; optional TypeSafe `jev` judge and integrations (SkillSpector, Cisco, gitleaks, osv-scanner, semgrep). Published benchmark: 250 malicious + 851 harmless skills; rules+gitleaks+jev flags 79% malicious with 0.35% false-block rate, 0.65 s/skill, $0.28/1k skills; rules-only 42% offline. Tuned with `skill-factory`'s loop. **Verification: Partially verified** (README via search snippet). Source: https://github.com/francoischastel/skill-scanner

**(c) ctrl-adam/husk.** Offline, free, no-account skill scanner; benchmark claims a full verdict on Snyk's own malicious-skill fixture where `snyk/agent-scan` v0.6.4 required a paid token to produce any verdict. **Verification: Partially verified** (BENCHMARK.md via search snippet). Source: https://github.com/ctrl-adam/husk

**(d) the-swarm-corporation/skillscanner.** Skill-format scanner producing structured REJECT/ACCEPT verdicts with risk scores, signal overviews, and rule evidence (e.g., invisible-Unicode, base64, credential-exfil rules). **Verification: Partially verified** (examples.md via search snippet). Source: https://github.com/the-swarm-corporation/skillscanner

**(e) getsentry/skills `skill-scanner` skill.** Sentry's own skill for scanning agent skills for security issues (advisory skill, not an executable scanner). Covered in §2.2. **Verification: Verified.**

**(f) lev-os/agents `security-scanner` skill.** Skill analyzing Claude Code plugins/skills for malicious content via AI semantic analysis; documents multi-agent skill paths (claude/codex/gemini/agents). **Verification: Partially verified** (SKILL.md via search snippet). Source: https://github.com/lev-os/agents

**(g) snyk/agent-scan.** Snyk's scanner; requires SNYK_TOKEN (paid account) for verdicts; token-free `inspect` only lists files without verification. Noted for the access-model contrast. **Verification: Partially verified** (via husk BENCHMARK.md). Source: https://github.com/snyk/agent-scan

**(h) agentskillexchange/agent-skill-exchange verification framework.** Open-source verification + security review framework behind AgentSkillExchange.com: `verification/checklist.md`, `security/tools/scan.sh`, `submission/SKILL_TEMPLATE.md`, verification tiers (Listed / Verified / Security Reviewed). **Verification: Partially verified.** Source: https://github.com/agentskillexchange/agent-skill-exchange

---

## 5. Meta-skills and skill generators

> **Scope note:** FrancyJGLisboa/agent-skill-creator is already catalogued (cross-reference only).

**(a) `skill-creator` meta-skill (microsoft/skills).** "Guide for creating effective skills for AI coding agents" — one of 11 Core skills in Microsoft's official repo. **Verification: Verified** (via microsoft/skills README). Source: https://github.com/microsoft/skills

**(b) `skill-writer` meta-skill (getsentry/skills).** "Canonical workflow to synthesize, create, and iteratively improve agent skills for this repository" with `skills/skill-writer/EVAL.md` repeatable evaluation prompts. **Verification: Verified** (via getsentry/skills README). Source: https://github.com/getsentry/skills

**(c) rfxlamia/skillkit `skillkit` + `skillkit-help` meta-skills.** Covered in §3.2(c): 12-step/15-step creation workflows with dual-mode validation, quality target 9.0+/10. **Verification: Partially verified.** Source: https://github.com/rfxlamia/skillkit

**(d) openai/codex `skill-creator` sample.** Creator sample shipped in the Codex CLI repo (`codex-rs/skills/src/assets/samples/skill-creator`); referenced as an official implementation sample. **Verification: Partially verified** (via kanadek/codex-skill-harvester research notes). Source: https://github.com/openai/codex

**(e) `npx skills init`.** The vercel-labs/skills CLI scaffolds a new SKILL.md template (`skills init [name]`). **Verification: Verified** (via vercel-labs/skills README). Source: https://github.com/vercel-labs/skills

**(f) FrancoisChastel/skill-factory.** Tuning loop used to improve the `jev` judge for francoischastel/skill-scanner (read training misses → rewrite → keep changes beating a validation set; took jev from 29% to 81% malicious-skill detection on validation). A skill-generation/tuning harness rather than a skill template. **Verification: Partially verified** (via skill-scanner benchmark docs). Source: https://github.com/FrancoisChastel/skill-factory

**(g) kanadek/codex-skill-harvester.** Maintainer workflow for incrementally deriving and updating original skills from authoritative docs, release info, APIs, and demand signals — with explicit Codex decision gates before publishing synthesized skills; contrasts itself with bulk corpora (EverMind-AI/SkillCorpus). **Verification: Partially verified** (research.md via search snippet). Source: https://github.com/kanadek/codex-skill-harvester

**(h) Expo `expo-skill-eval` (thenaubit/explora-app-example).** Evaluator skill (see §7): evaluates Expo skills end-to-end — trigger accuracy, generated code quality, runtime screenshots on iOS simulator/Android emulator via Expo Go. **Verification: Partially verified.** Source: https://github.com/thenaubit/explora-app-example

---

## 6. Marketplaces, registries, and directories

### 6.1 Agent Skill Exchange (agentskillexchange.com)

> **Resource name:** Agent Skill Exchange (ASE)
> **Canonical identity:** agentskillexchange.com; GitHub org agentskillexchange
> **Category:** Infrastructure — marketplace/registry + verification
> **Type:** Web marketplace + skill corpus repo + verification framework + resources repo
> **Official URL:** https://agentskillexchange.com
> **Description:** A skill marketplace/registry with web browse (`/browse-skills/` with search, filters, skill detail panels, install links), category taxonomy (WordPress & CMS 96 skills, Content Writing & SEO 84, etc.), TOP-STARS.md / TOP-DOWNLOADS.md leaderboards, full CATALOG.md, and a machine-readable `skills.json` index (name, slug, description, category, framework, verification tier, signals: tool, github_stars, npm_weekly_downloads, license). Verification tiers: Listed / Verified / Security Reviewed. Backed by repos: `agentskillexchange/skills` (the skill corpus; entries carry frontmatter with slug, description, github_stars, verification, source, category, framework, tool_ecosystem), `agentskillexchange/agent-skill-exchange` (verification framework: checklist, scan.sh, submission template), `agentskillexchange/agent-skills-resources` (framework guides, e.g., codex.md with ASE Codex-skill views). Mirrors observed: vood/agent-skill-exchange, hinvec/security-scanned-skills.
> **Contents inspected:** Search-result snippets of the corpus entries (e.g., stripe-agent-toolkit entry: 1,422 stars, security_reviewed, source stripe/ai; trail-of-bits entry: 4,663 stars), marketplace README structure, verification framework README. Site itself not fetched.
> **Actual capabilities:** Curated, verification-tiered skill discovery with install links and JSON index.
> **Usage domain:** Skill discovery across frameworks (Claude Code, Cursor, Codex, Copilot, Gemini, OpenClaw, MCP, LangChain).
> **Integration method:** Web browse; git clone of corpus; skills.json for programmatic access.
> **Compatibility (with evidence):** Framework tags per skill (Claude Code, Cursor, MCP, OpenClaw, Codex, Custom Agents). Verification tiers documented.
> **Dependencies:** None.
> **Availability:** Public, free.
> **Maintenance:** Active (corpus updated ~12 days before 2026-10-10). Operator identity not verified — treat as community-run.
> **License:** Not verified
> **Limitations:** Verification methodology is self-published; AIR incident research suggests scan-once models have TOCTOU gaps; site not primary-fetched.
> **Related resources:** skills.sh (alternative registry), VoltAgent/awesome-agent-skills (catalogued), royalpinto007/awesome-agent-skills.
> **Sources:** https://agentskillexchange.com; https://github.com/agentskillexchange/skills; https://github.com/agentskillexchange/agent-skill-exchange; https://github.com/agentskillexchange/agent-skills-resources
> **Verification date:** 2026-10-10
> **Confidence:** Medium. **Verification: Partially verified.**

### 6.2 Other directories and indexes

**(a) royalpinto007/awesome-agent-skills.** "A small, verified, security-aware directory of Agent Skills (SKILL.md format)" — curates the Claude Skills gallery, skill collections (obra/superpowers 292.4k★, trailofbits/skills 7.3k★, getsentry/skills, vostride/agent-qa, obra/superpowers-skills, Orkas-VideoStudio, etc.) with star counts. **Verification: Partially verified** (README via search snippet). Source: https://github.com/royalpinto007/awesome-agent-skills

**(b) jwv123/awesome-frontend-skills.** Curated frontend Agent Skills installable via `npx skills add` — React (wshobson/agents react-state-management, softaworks/agent-toolkit react-dev, millionco/react-doctor) and Angular (analogjs/angular-skills: angular-component/signals/forms/routing/http/di) tables with per-skill install commands. **Verification: Partially verified.** Source: https://github.com/jwv123/awesome-frontend-skills

**(c) cuoicungtui/agentskills-sdk.** Python SDK for discovering, retrieving, and serving Agent Skills to LLM agents: `SkillRegistry` + providers for filesystem and HTTP, integrations for LangChain, Microsoft Agent Framework, and MCP; progressive-disclosure tool API (get_skill_body, get_skill_reference, etc.); security features (path-traversal protection, file-size limits, error sanitization). Ships `docs/SKILLS-DIRECTORY.md` (curated directory of official + community skill repos). MIT. **Verification: Partially verified** (READMEs via search snippets). Source: https://github.com/cuoicungtui/agentskills-sdk

**(d) learn-skills.dev (neversight/learn-skills.dev).** Data-driven skills directory: `data/skills-md/<author>/<collection>/<skill>/SKILL.md` corpus with metadata (version, last_verified, production_tested, token_savings, errors_prevented, official_docs, keywords) — e.g., a better-auth skill entry. Appears to be a learning/discovery site backed by a skill corpus. **Verification: Partially verified** (single entry via search snippet). Source: https://github.com/neversight/learn-skills.dev

**(e) agent-skills-library (PyPI).** `pip install agent-skills-library` — SDK + CLI (`agent-skills stats/search/validate/quality/catalog`); claims 100 skills, 100% Russian translations, 16 domains, Grade-A quality bar, MIT; frontmatter strictly validated for cross-agent portability in CI (`scripts/check_agent_interop.py`). **Verification: Partially verified** (PyPI page via search snippet). Source: https://pypi.org/project/agent-skills-library/

**(f) EverMind-AI/SkillCorpus.** Large aggregate skill corpus for retrieval, scoring, and evaluation (embedding/reranker infrastructure) — referenced as the "bulk corpus" contrast to codex-skill-harvester's maintainer workflow. **Verification: Unverified** (referenced only). Source: https://github.com/EverMind-AI/SkillCorpus

**(g) dmgrok/agent_skills_directory.** Provider directory accepting "Add provider" issues (e.g., better-auth/skills registered as "Official (Better Auth)"). **Verification: Partially verified** (issue via search snippet). Source: https://github.com/dmgrok/agent_skills_directory

**(h) Catherine1401/agent-skills.** Portable skills + shared policies for Codex, Claude Code, Cursor on Linux; `./install.sh --agent all --mode symlink` installer; CI-tested; MIT. **Verification: Partially verified** (README via search snippet). Source: https://github.com/Catherine1401/agent-skills

---

## 7. Skill evaluators

**(a) expo-skill-eval (thenaubit/explora-app-example).** Skill evaluating Expo skills end-to-end: trigger accuracy, generated-code quality, runtime screenshots on iOS simulator and Android emulator via Expo Go (web optional); `allowed-tools` scoped to temp/cache paths. MIT. **Verification: Partially verified.** Source: https://github.com/thenaubit/explora-app-example/blob/HEAD/.agents/skills/expo-skill-eval/SKILL.md

**(b) Vally evaluations (microsoft/skills).** Repo documents "Vally Evaluations" plus Ralph Loop & Sensei patterns under "Testing Skills," with test-coverage summary and guidance for adding coverage. **Verification: Partially verified** (README outline). Source: https://github.com/microsoft/skills

**(c) skill-factory tuning loop (FrancoisChastel/skill-factory).** Covered in §5(f): evaluation-driven skill/judge improvement loop with separate validation sets. **Verification: Partially verified.**

**(d) hqhq1025/skill-optimizer** — already catalogued (cross-reference): skill optimization/personalization.

---

## 8. Community collections by domain (selected, non-duplicated)

> Only collections NOT in the already-catalogued list. Single-skill repos and mirrors are noted as leads, not full records.

- **podo/design-agent-skills** — Design-agent skill collection organized as catalogue stubs with decision trees and install commands: `vercel-skills`, `figma-official-skills` (7 official Figma skills), `figma-catalogue` (design tokens, Stitch, code-connect), `cloudflare-web-perf`, plus stubs for `openai-skills` (OpenAI's 9: Figma + frontend + slides + imagegen), `google-stitch-skills`, `anthropics-skills`, `microsoft-skills`, `software-mansion-skills`, `callstack-agent-skills`, `expo-skills`. Useful as a cross-vendor index of official suites. **Partially verified** (stub SKILL.md files via search). Source: https://github.com/podo/design-agent-skills
- **nanlabs/agent-toolkit** — Agent toolkit with a Figma skill family: entry-point `figma` skill routing to `figma-implement-design`, `figma-generate-design`, `figma-code-connect-components`, `figma-create-design-system-rules`, `figma-create-new-file`, `figma-use` (mirrors official Figma set) with MCP integration rules. **Partially verified.** Source: https://github.com/nanlabs/agent-toolkit
- **saschb2b/skills** — Engineering skills including `javascript-ecosystem` with a "prefer first-party agent skills" routing principle (Angular given as the example). **Partially verified.** Source: https://github.com/saschb2b/skills
- **georgeshani/skills** — Stack-specific skill collection (angular-ionic-capacitor) documenting the official-skills routing table + MCP server matrix. **Partially verified.** Source: https://github.com/georgeshani/skills
- **antfu/skills** — Anthony Fu's skills (e.g., `vite`, documentation-generated, MIT; vendored by consumers with license attribution). **Partially verified** (via samuelfarkas/nonstopvibin license docs). Source: https://github.com/antfu/skills
- **socialrobot-io/reflow docs/SKILLS.md**, **sprioleau/flock**, **miinhho/setup-project-skills** — consumer implementations showing real-world multi-vendor skill installs (better-auth, clerk, resend, temporal) with skills-lock.json pinning patterns. **Partially verified.**

---

## Coverage note

**Counts (this workstream, new resources only):**
- Distinct new resources recorded: **~48** (19 official-company collections, 4 installer/manager entries covering 7 distinct tools, 8 validators/scanners entries covering 11 distinct tools, 8 meta-skill/generator entries, 8 marketplace/directory entries, 4 evaluator entries, 6 community-collection entries).
- Full Part-21-style records: **27** (19 company + 1 standard cross-ref + vercel-labs/skills CLI + 4 validators + ASE + skillkit-variants grouped).
- **Verified** (primary source fetched): 11 — vercel-labs/agent-skills, vercel-labs/skills CLI, getsentry/skills, huggingface/skills, stripe/ai, trailofbits/skills, microsoft/skills, netlify/context-and-tools, supabase/agent-skills, figma/mcp-server-guide (README-level), Agent Skills standard (cross-ref).
- **Partially verified** (secondary/consumer sources, consistent across ≥1 independent source): ~30.
- **Unresolved**: 2 — `skills-ref` (Neon CI validator; existence inferred, no standalone source found), EverMind-AI/SkillCorpus (referenced only).
- **Inspected in depth** (README or skill bodies read): 11 primary READMEs + ~25 secondary SKILL.md/README snippets.

**Limitations:**
1. No live browser available to this subagent; several vendor READMEs (expo/skills, angular/skills, ClickHouse, HashiCorp, better-auth, LambdaTest, Capgo) were verified via search-result snippets and independent consumer mirrors rather than direct fetches — skill inventories for these should be re-confirmed from primary READMEs before being treated as canonical.
2. Individual SKILL.md bodies were inspected for only a subset (Stripe's stripe-best-practices via vendored copies, Figma skills via secondary descriptions, HashiCorp skills via vendored copies, TestMu AI docs skill); most records describe collections at the README level.
3. License and star/fork counts for snippet-verified repos are as-reported at fetch time and may be stale.
4. The skill landscape moves fast (repos created Dec 2025–Jan 2026 dominate); inventories dated 2026-10-10 will decay.

**More work warranted?** Yes, moderately:
- Primary-fetch verification for the 8 snippet-verified official collections (Expo, Angular, ClickHouse, HashiCorp, Better Auth, LambdaTest, Capgo, Neon).
- Resolve `skills-ref` and EverMind-AI/SkillCorpus.
- Follow the noted leads: getsentry/sentry-for-ai, auth0/agent-skills, clerk/skills, resend/resend-skills, temporalio/skill-temporal-developer, software-mansion/callstack RN skills, google-stitch-skills, openai Figma/frontend/slides/imagegen skills, `npx agentskillsforall`.
- A dedicated security pass: the AIR TOCTOU incident suggests scanner efficacy claims (Cisco, SkillSpector, francoischastel, husk) deserve independent benchmarking before the Atlas repeats them.
