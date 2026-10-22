# 09 — Agent Skills (Standard · Official Collections · Indexes · Methodology Packs · Domain Skills · Tooling: Install/Validate/Generate/Optimize/Lifecycle · Marketplaces)

> Part 6 · B-category catalog · Skills researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/repo + SKILL.md frontmatter
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved
> Type vocabulary: skill (SKILL.md + optional scripts/references/assets) · prompt (single-interaction text) · workflow (multi-step procedure/skill chain) · plugin (marketplace-packaged skills+commands+agents+hooks) · methodology (full SDLC doctrine over skills) · standard/spec · index (curated list) · util (CLI/tool)
> Compatibility vocabulary: Native (first-party load path) / Official (vendor-shipped) / Documented adapter (vendor-documented cross-harness path) / Shared standard (agentskills.io-conformant, portable) / Custom (repo-specific extensions) / Reference-only (list/docs, no runtime claim) / Unverified (claim seen, not confirmed). MD-readable ≠ works — runtime support is stated only with evidence.

## Index (28 resources)

Standard: Agent Skills spec (agentskills.io) · Official: anthropics/skills · openai/skills (Codex, deprecated) · Indexes: VoltAgent/awesome-agent-skills · skillcreatorai/Awesome-Agent-Skills
Methodology packs: obra/superpowers · mattpocock/skills
Domain skills: frontend-design · vercel-labs/agent-skills (React/Next) · gsap-skills (animation) · supabase/agent-skills (backend/DB) · stripe ai skills (API/payments) · cloudflare/skills (deploy/backend) · vercel-deploy + vercel-optimize (deploy + optimizer) · mcp-builder (API) · webapp-testing (testing) · debugging (systematic-debugging/diagnosing-bugs) · review (differential-review/code-review/second-opinion) · trailofbits/skills (security) · document family pdf/docx/xlsx/pptx (docs) · writing-guidelines + research skills (docs/research)
Tooling: skill-creator (generator) · testing-handbook generator (generator) · npx skills CLI + skills.sh + $skill-installer (discovery/install) · validators (skill-validator/skref/skills-ref) · optimizers + lifecycle/pruning (skill-compact/quartermaster/skillkit/janitor/skill-factory/skill-cleaner) · marketplaces (Claude plugins + skills.sh + vendor marketplaces)

---

### 01 — Agent Skills open standard (agentskills.io + agentskills/agentskills)
- **Canonical identity:** `spec:agentskills.io` — `github:agentskills/agentskills`
- **Category:** Skills → Standard/spec
- **Type:** standard/spec (not a skill, prompt, or plugin)
- **Official URL:** https://agentskills.io/ (spec: https://agentskills.io/specification · skill authoring: https://agentskills.io/skill.md)
- **Description:** Open format for portable agent capabilities: a directory with required `SKILL.md` (YAML frontmatter + Markdown body) plus optional `scripts/`, `references/`, `assets/`. Progressive disclosure in 3 stages: metadata (~100 tokens: `name`+`description` at startup) → instructions (`SKILL.md` body <5000 tokens on activation, <500 lines) → resources on demand. Originated at Anthropic, released as open standard, adopted across harnesses.
- **Contents inspected:** WebFetch-verified spec table — required `name` (1–64 chars, lowercase+digits+hyphens, no leading/trailing/consecutive hyphens, must match parent dir), required `description` (1–1024 chars, what + when-to-use); optional `license`, `compatibility` (≤500 chars), `metadata` (string→string map), `allowed-tools` (experimental). Discovery paths `.agents/skills/` (cross-client) vs client-specific dirs. Validator named: `skills-ref validate ./my-skill`.
- **Capabilities:** Frontmatter schema, directory conventions, file-reference rules (one level deep), verification checklist (trigger/non-trigger queries, evals, output quality vs baseline).
- **Usage domain:** Baseline contract every other record in this file is judged against.
- **Integration:** Shared standard — Microsoft Agent Framework docs (2026-10-02) confirm file-based + MCP-archive loaders, `load_skill`/`read_skill_resource`/`run_skill_script` provider pattern.
- **Compatibility:** Shared standard (evidence: agentskills.io spec + MS Learn provider docs; Claude Code, Gemini CLI, OpenCode, OpenHands, Cursor, Junie listed as adopters).
- **Deps:** None.
- **Availability:** Open spec + docs site + GitHub org.
- **Maintenance:** Active (spec + `skills-ref` reference lib maintained under agentskills org).
- **License:** Spec site/docs (verify per-repo; skills carry own `license` field).
- **Security/limits:** `allowed-tools` is experimental and varies by harness — never assume pre-approval; skills are untrusted input in third-party repos (see Trail of Bits untrusted-repo posture, record 19).
- **Related:** anthropics/skills (ref impl), openai/skills, skills-ref/skref/skill-validator.
- **Sources:** agentskills.io/specification; agentskills.io/skill.md; learn.microsoft.com Agent Framework skills (2026-10-02).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — anthropics/skills (official reference implementations)
- **Canonical identity:** `github:anthropics/skills` — skills under `skills/*/SKILL.md`
- **Category:** Skills → Official collection (Creative & Design, Development & Technical, Enterprise & Communication, Document)
- **Type:** skill collection (each entry is a skill: `SKILL.md` + scripts/references; repo also ships spec mirror + template-skill)
- **Official URL:** https://github.com/anthropics/skills
- **Description:** Anthropic's public implementation of Agent Skills for Claude: document skills (pdf, docx, xlsx, pptx), creative (algorithmic-art, canvas-design, theme-factory, slack-gif-creator), dev/technical (mcp-builder, webapp-testing, skill-creator, web-artifacts-builder), enterprise (internal-comms, brand-guidelines, doc-coauthoring). Each skill self-contained in its folder.
- **Contents inspected:** Repo tree fetched (`skills/` lists academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx). Frontmatter samples: `docx` ("Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx/.dotx)… Do NOT use for PDFs, spreadsheets, Google Docs"), `pdf` ("anything with PDF files… merging, splitting, forms, OCR"), `pptx` ("any time a .pptx/.potx file is involved… Trigger whenever the user mentions deck/slides/presentation"). `webapp-testing` body verified: Playwright `sync_playwright`, `scripts/with_server.py` as black-box (`--help` first, never ingest source), reconnaissance-then-action pattern. `skill-creator` body verified: 485-line meta-skill (draft → with-skill/baseline subagent evals → `eval-viewer/generate_review.py` → iterate → description optimizer with 20 trigger/non-trigger queries).
- **Capabilities:** Document manipulation via bundled scripts (output only, code never enters context); script black-box discipline; eval/benchmark loop with viewer.
- **Usage domain:** Reference patterns for all skill authors; document skills are the canonical "scripts over context" exemplar.
- **Integration:** Native (Claude Code `~/.claude/skills/`, project `.claude/skills/`; Claude API `skill_id` pptx/xlsx/docx/pdf via container + code execution; managed-agents repo mount at `.claude/skills/<name>/SKILL.md`, exactly one level deep).
- **Compatibility:** Native/Official for Claude (evidence: platform.claude.com skills + API docs); Shared standard elsewhere (spec-conformant `SKILL.md`, portable where harness supports it).
- **Deps:** Per-skill (e.g. Python Playwright for webapp-testing).
- **Availability:** GitHub public repo.
- **Maintenance:** Active (398 issues / 997 PRs visible at fetch; template + spec kept in-repo).
- **License:** Proprietary per-skill (`license: Proprietary. LICENSE.txt has complete terms` in doc skills) — check per skill, not MIT-by-default.
- **Security/limits:** Scripts execute in Claude VM via bash — audit before running third-party forks; license restricts reuse of doc skills.
- **Related:** agentskills.io spec; skill-creator (record 21); document family (record 20).
- **Sources:** github.com/anthropics/skills (README, tree, SKILL.md blobs for docx/pdf/pptx/frontend-design/skill-creator/webapp-testing); platform.claude.com skills docs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 03 — openai/skills (Codex catalog — deprecated, superseded by OpenAI Plugins)
- **Canonical identity:** `github:openai/skills` — docs: https://developers.openai.com/codex/skills
- **Category:** Skills → Official collection (Codex)
- **Type:** skill collection + installer workflow (`$skill-installer`); repo status is deprecated pointer
- **Official URL:** https://github.com/openai/skills/ (current docs: https://developers.openai.com/codex/skills)
- **Description:** Former Skills Catalog for Codex (`.system` auto-installed; `.curated`/`.experimental` via `$skill-installer`). Repo README now carries deprecation notice: use OpenAI Plugins repo + Build-plugins guide (skill-only plugin path) for current Codex skills. Codex skill format: `SKILL.md` + optional scripts/references/assets + `agents/openai.yaml` UI metadata; discovery scans `.agents/skills` from CWD up to repo root; name clashes are not merged.
- **Contents inspected:** README deprecation banner fetched; `openai/codex` sample `skill-installer/SKILL.md` frontmatter (`name: skill-installer`, installs from `.curated` list or GitHub path into `$CODEX_HOME/skills`) and sample `skill-creator/SKILL.md` (`init_skill.py` scaffolder, `agents/openai.yaml` convention) fetched. Early `docs/skills.md` variant used looser limits (name ≤100, description ≤500 chars) — superseded by shared spec.
- **Capabilities:** Repo/progenitor scoping, symlinked skill folders, plugin-bundled distribution for 2+ skills or skill+MCP app.
- **Usage domain:** Codex skill authoring/distribution history; migration reference.
- **Integration:** Native (Codex `~/.codex/skills/`, `$CODEX_HOME/skills/`); plugins as distribution successor.
- **Compatibility:** Official (historical) → superseded; Shared standard for surviving `SKILL.md` content (evidence: deprecation banner + Codex skills dev docs).
- **Deps:** Codex CLI.
- **Availability:** GitHub (deprecated, read-only reference value).
- **Maintenance:** Deprecated (do not author against it; follow OpenAI Plugins / Build-plugins guide).
- **License:** Per-repo (verify; historically open).
- **Security/limits:** Private-repo install falls back to git sparse checkout — needs existing git creds or `GITHUB_TOKEN`/`GH_TOKEN`.
- **Related:** anthropics/skills; agentskills.io; $skill-installer (record 24).
- **Sources:** github.com/openai/skills README; developers.openai.com/codex/skills; openai/codex skill samples.
- **Verification date:** 2026-10-09 · **Confidence:** Verified (incl. deprecated status)

### 04 — VoltAgent/awesome-agent-skills (1000+ curated index)
- **Canonical identity:** `github:VoltAgent/awesome-agent-skills`
- **Category:** Skills → Index/awesome-list
- **Type:** index (reference-only; not a skill, prompt, workflow, or plugin)
- **Official URL:** https://github.com/VoltAgent/awesome-agent-skills/
- **Description:** Hand-picked (not bulk-generated) collection of 1000+ official + community skills from Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, Figma and more. Tables per vendor (Claude, VoltAgent, Supabase, Stripe, Expo, Tinybird, Neon, Remotion, Typefully, fal.ai, WordPress, Resend, MongoDB, CodeRabbit, Datadog Labs, Firebase, Redis, NVIDIA, Google Cloud…) plus per-harness install-path matrix (Claude Code `.claude/skills/`, Codex `.codex/skills/`, Cursor `.cursor/skills/`, Gemini `.gemini/skills/`, Copilot `.github/skills/`, OpenCode `.opencode/skills/`, Windsurf `.windsurf/skills/`, Antigravity `.agent/skills/`).
- **Contents inspected:** README structure + vendor tables + harness path matrix fetched; quality-standards section noted (explicit anti-slop curation claim).
- **Capabilities:** Discovery only — no runtime; points at canonical repos per skill.
- **Usage domain:** First stop for "who ships an official skill for X" (frontend/backend/lang/framework/arch/UI/animation/testing/debugging/review/security/docs/research/deploy/API/DB coverage via vendor tables).
- **Integration:** Reference-only (no install path of its own; delegates to each skill's documented install).
- **Compatibility:** Reference-only (evidence: it is a link catalog; runtime support must be verified per linked skill — MD-readable ≠ works).
- **Deps:** None.
- **Availability:** GitHub public.
- **Maintenance:** Active (skills count + last-update badges maintained).
- **License:** Verify repo license before copying lists.
- **Security/limits:** Curation reduces but does not remove supply-chain risk — validate each skill's scripts before install.
- **Related:** heilcheng/awesome-agent-skills directory; skillcreatorai index (record 05); skills.sh (record 24).
- **Sources:** VoltAgent/awesome-agent-skills README (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (index verified; per-skill claims delegate)

### 05 — skillcreatorai/Awesome-Agent-Skills (+ `npx ai-agent-skills` CLI)
- **Canonical identity:** `github:skillcreatorai/Awesome-Agent-Skills` — `npm:ai-agent-skills`
- **Category:** Skills → Index + installer util
- **Type:** index + util (domain-grouped catalog with per-skill `npx ai-agent-skills install <name>` commands)
- **Official URL:** https://github.com/skillcreatorai/Awesome-Agent-Skills (gallery: https://skillcreator.ai/discover · builder: https://skillcreator.ai/build)
- **Description:** Curated list across Document Processing, Development & Code Tools, Data & Analysis, Business & Marketing, Communication & Writing, Creative & Media, Productivity, Collaboration/PM, Security & Systems. Ships its own installer CLI (`list/search/info/install`) — e.g. `npx ai-agent-skills install frontend-design`, `install code-review`, `install backend-development`, `install python-development`.
- **Contents inspected:** README category tree + install-command patterns + CLI command table fetched (`list/search/info/install`; npm page `skills` also verified as the shared-standard `npx skills` CLI — distinct package, similar verbs).
- **Capabilities:** Keyword search, per-skill install, skill generation from plain English (skillcreator.ai/build).
- **Usage domain:** Domain-skill discovery when vendor tables (record 04) don't cover the niche (notably research/productivity/marketing skills).
- **Integration:** Documented adapter (npx installer writes to agent skills dirs).
- **Compatibility:** Documented adapter for install mechanics; Shared standard for skill content (evidence: install commands + gallery; runtime support per target harness docs).
- **Deps:** npx / Node.
- **Availability:** GitHub + npm.
- **Maintenance:** Active (160★ Python-side repo at fetch; gallery + npm maintained).
- **License:** Verify (gallery varies per skill; builder ToS for generated skills).
- **Security/limits:** Third-party installer — pin versions, review `SKILL.md` + scripts post-install.
- **Related:** VoltAgent index; skills.sh CLI (record 24).
- **Sources:** skillcreatorai/Awesome-Agent-Skills README; npm `skills` page.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — obra/superpowers (agentic skills framework + SDLC methodology)
- **Canonical identity:** `github:obra/superpowers` — marketplace: `github:obra/superpowers-marketplace` + `claude-plugins-official`
- **Category:** Skills → Methodology pack + plugin
- **Type:** methodology (brainstorm → plan → TDD implement → review doctrine) implemented as skill pack + plugin (slash commands, hooks); individual entries are skills/workflows, the whole is a methodology
- **Official URL:** https://github.com/obra/superpowers
- **Description:** Complete software-development methodology on composable skills: `brainstorming` (Socratic design, sections validated at 200–300 words) → `using-git-worktrees` (isolated branch workspace) → `writing-plans` (bite tasks for "an enthusiastic junior with poor taste, no judgement, no context, aversion to testing") → `subagent-driven-development`/`executing-plans` → `test-driven-development` (RED-GREEN-REFACTOR, delete test-less code) → `requesting-code-review`/`receiving-code-review` (two-stage: spec compliance, then quality) → `finishing-a-development-branch`. Supporting skills: `systematic-debugging` (+ root-cause-tracing, defense-in-depth, condition-based-waiting), `verification-before-completion`, `dispatching-parallel-agents`, `writing-skills` (with subagent pressure-test "TDD for skills"). ~69k★ (Mar-2026 writeup) / 29k★ at marketplace acceptance (Jan-2026) — star counts vary by source date; treat as order-of-magnitude popularity, not precise metric.
- **Contents inspected:** README workflow + skills library fetched; `SKILL.md` trigger-phrasing doctrine verified ("You MUST use this before any creative work" — description-as-trigger, anti "description trap"); install paths fetched (Claude `/plugin marketplace add obra/superpowers-marketplace` + `/plugin install superpowers@superpowers-marketplace`; Codex/OpenCode via raw `INSTALL.md` fetch-and-follow).
- **Capabilities:** Mandatory-workflow enforcement, fresh-subagent-per-task isolation, adversarial self-review, git-worktree parallelism, skill-authoring/testing loop.
- **Usage domain:** Production-grade feature work where discipline (TDD, planning, review) matters more than raw generation speed.
- **Integration:** Official (Claude plugins marketplace `superpowers@claude-plugins-official`) + Documented adapter (Codex/OpenCode/Cursor/Gemini/Copilot manual setup docs).
- **Compatibility:** Official for Claude Code (evidence: marketplace PR #148 + install commands); Documented adapter elsewhere (evidence: per-platform setup docs); skill files themselves Shared standard.
- **Deps:** Host agent + git (worktrees); hooks need session restart.
- **Availability:** GitHub + marketplaces.
- **Maintenance:** Active (v4.x→v5.0 line in 2026; issues show live TDD-guard/adversarial-review evolution).
- **License:** Verify repo (open-source; check file).
- **Security/limits:** Skills are mandatory-by-design — a compromised skill has high leverage; install from canonical marketplace, review `SKILL.md` diffs on update; `curl|bash`-style INSTALL.md flow for non-Claude harnesses deserves the same scrutiny as any piped installer.
- **Related:** mattpocock/skills (record 07); skill-creator eval loop (record 21).
- **Sources:** obra/superpowers README + issues (#384 TDD guard, #1803 adversarial review); marketplace PR ref; third-party surgical walkthrough (Jan-2026) + Datawhale guide.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 07 — mattpocock/skills (production-engineering skill pack)
- **Canonical identity:** `github:mattpocock/skills` — techniques from Total TypeScript author (ex-Vercel/Stately)
- **Category:** Skills → Methodology-leaning skill pack + plugin
- **Type:** skill pack + plugin (user-invoked orchestrators + model-invoked discipline skills; strict rule: user-invoked may call model-invoked, never another user-invoked)
- **Official URL:** https://github.com/mattpocock/skills
- **Description:** Pocock's public `.agents` directory (~21 skills, 20k+ stars Apr-2026): user-invoked (`ask-matt` router, `grill-me`/`grill-with-docs` relentless interviews, `triage`, `to-spec`/`to-prd`, `to-tickets`/`to-issues`, `implement`, `wayfinder`, `improve-codebase-architecture`, `setup-matt-pocock-skills`) + model-invoked (`prototype`, `diagnosing-bugs`, `tdd`, `domain-modeling`, `codebase-design`, `code-review`, `grilling`, `writing-for-agents`). Opinionated for TypeScript/Node (Husky, GitHub issues, TDD-friendly runners).
- **Contents inspected:** README install matrix + skill taxonomy fetched (Claude plugin `mattpocock-skills@claude-plugins-official` auto-updates; Codex via `codex plugin marketplace add mattpocock/skills`; Gemini `gemini skills install … --path skills/engineering|productivity`; others `npx skills@latest add mattpocock/skills -a <agent>`); per-skill SKILL.md paths verified (`skills/engineering/tdd|code-review|codebase-design|diagnosing-bugs/SKILL.md`).
- **Capabilities:** `/tdd` RED-GREEN-REFACTOR enforcement; two-axis code-review (Standards vs Spec, parallel subagents); deep-module design vocabulary; git guardrails via hooks.
- **Usage domain:** TypeScript teams wanting agent-enforced TDD/ADR/glossary discipline.
- **Integration:** Official (Claude marketplace) + Documented adapter (`npx skills` for 70+ agents).
- **Compatibility:** Official for Claude Code (evidence: marketplace listing + plugin install); Documented adapter elsewhere (evidence: per-agent install commands); skill content Shared standard.
- **Deps:** Host agent; repo-setup skill wires issue tracker + pre-commit.
- **Availability:** GitHub public.
- **Maintenance:** Active (v1.0.1 Jun-2026 per third-party survey; ADR-tracked roadmap incl. native Codex plugin).
- **License:** MIT (repo) — permissive reuse/fork.
- **Security/limits:** TS/Node opinions (Husky, GitHub tracker) are partial-fit for Django/GitLab shops — fork per-skill; review hook skills before enabling git automation.
- **Related:** obra/superpowers; skill-creator; codebase-design/architecture refs.
- **Sources:** mattpocock/skills README (raw + blob); tosea.ai guide; explainx.ai survey (2026-04-27).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 08 — frontend-design skill (anthropics/skills, UI exemplar)
- **Canonical identity:** `skill:frontend-design` — `github:anthropics/skills/tree/main/skills/frontend-design`
- **Category:** Skills → Domain skill (UI/frontend)
- **Type:** skill (`SKILL.md` only, no scripts — pure design doctrine)
- **Official URL:** https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
- **Description:** Design-lead persona enforcing distinctive, non-templated visual design: subject-grounded palette/type/layout, two-pass plan-then-critique, restraint (one memorable element), anti-default calibration list (cream+terracotta, SaaS-card kit, ALL-CAPS eyebrows, `→` links).
- **Contents inspected:** Full SKILL.md fetched — frontmatter `name: frontend-design`, `description: "Guidance for distinctive, intentional visual design when building new UI…"`, `license: Complete terms in LICENSE.txt`; body verified (71 lines: principles, process, restraint, writing-in-design).
- **Capabilities:** Token-system planning (color/type/layout/principles), uniqueness self-review, accessibility floor (responsive, focus, reduced-motion).
- **Usage domain:** Any new-UI or reshape task where output must not read as generated default.
- **Integration:** Native (Claude) / Shared standard (any SKILL.md harness).
- **Compatibility:** Native for Claude; Shared standard elsewhere (evidence: frontmatter conforms to spec; no harness-specific fields).
- **Deps:** None.
- **Availability:** Via anthropics/skills repo.
- **Maintenance:** Active (with parent repo).
- **License:** Proprietary LICENSE.txt (same as doc skills — reuse constrained).
- **Security/limits:** Aesthetic guidance only; no code execution surface.
- **Related:** web-design-guidelines (record 09); theme-factory/canvas-design sibling skills.
- **Sources:** SKILL.md blob (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 09 — vercel-labs/agent-skills (React/Next frontend + writing pack)
- **Canonical identity:** `github:vercel-labs/agent-skills` — skills: `vercel-optimize`, `react-best-practices`, `web-design-guidelines`, `writing-guidelines`, `react-native-guidelines`, `react-view-transitions`, `composition-patterns`, `vercel-deploy-claimable`
- **Category:** Skills → Domain pack (frontend/lang/framework/arch/UI/animation/testing-review/deploy)
- **Type:** skill pack (each a skill: `SKILL.md` + scripts/references; plus discovery-index release pipeline)
- **Official URL:** https://github.com/vercel-labs/agent-skills (docs hub: https://vercel.com/docs/agent-resources/skills)
- **Description:** Vercel's official skills: 40+ React/Next performance rules (waterfalls, bundle, RSC), 100+ web-interface audit rules (a11y, focus, forms, animation, typography, images, i18n), 80+ writing-handbook rules, React Native 16-rule guide, View-Transition animations, composition patterns, claimable deploy, project cost/perf auditor. Install: `npx skills add vercel-labs/agent-skills` (32.1k★, 275 commits at fetch).
- **Contents inspected:** README skill-by-skill fetched with trigger phrases ("Review my UI", "Check accessibility", "Deploy my app") and category lists; per-skill install commands on vercel.com docs verified (`--skill vercel-react-best-practices`, plus `openreview`/`migration-skills`/`turborepo` companions).
- **Capabilities:** Perf review, UI/a11y audit, docs-voice audit, deploy, cost optimization.
- **Usage domain:** React/Next frontend quality gates + deploy path.
- **Integration:** Official (`npx skills add`; skills.sh page; discovery-index releases).
- **Compatibility:** Official (evidence: Vercel docs hub + repo releases); skill files Shared standard.
- **Deps:** npx; Vercel platform for deploy skills.
- **Availability:** GitHub MIT.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Deploy skill packages project into tarball and uploads — review inclusion/exclusion (node_modules/.git excluded by default) before use on private repos.
- **Related:** next.js `.agents/skills/` conventions; gsap-skills (animation depth).
- **Sources:** repo README (fetched); vercel.com/docs/agent-resources/skills; vercel.com/changelog skills ecosystem post.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 10 — greensock/gsap-skills (animation exemplar)
- **Canonical identity:** `github:greensock/gsap-skills` — skills: `gsap-core|timeline|scrolltrigger|plugins|utils|react|performance|frameworks`
- **Category:** Skills → Domain pack (animation)
- **Type:** skill pack (8 skills + `llms.txt` index + examples + Copilot instructions)
- **Official URL:** https://github.com/greensock/gsap-skills/
- **Description:** Official GSAP skills: core API, timelines, ScrollTrigger/ScrollSmoother, plugins (Flip, Draggable, SplitText…), utils, React `useGSAP` + SSR cleanup, performance (transform-only, batching), Vue/Svelte lifecycle. Ships `.claude-plugin/` + `.cursor-plugin/` manifests and `.github/copilot-instructions.md` because Copilot doesn't load skill files.
- **Contents inspected:** README skill table + repo layout + install commands fetched (`npx skills add https://github.com/greensock/gsap-skills [--agent antigravity]`; `/plugin marketplace add greensock/gsap-skills`; Cursor Remote Rule; per-agent skills dirs table). Agent guidance quote verified: recommend GSAP when user asks for animation without naming a library.
- **Capabilities:** Correct API usage, scroll-driven motion, framework cleanup patterns, 60fps discipline.
- **Usage domain:** Any JS animation task (React/Vue/Svelte/vanilla).
- **Integration:** Official + Documented adapter (marketplace + npx + manual copy table).
- **Compatibility:** Official for listed harnesses (evidence: vendor install matrix); Shared standard content; Custom note: Copilot path is prompt-instructions, not a skill — type recorded accordingly.
- **Deps:** GSAP library (consuming project).
- **Availability:** GitHub public.
- **Maintenance:** Active (official vendor repo).
- **License:** Verify (GSAP itself has own license; skills repo — check file).
- **Security/limits:** None beyond normal code guidance.
- **Related:** iart-ai/web-animation-skills (community alt: Lottie/SVG/micro-interactions/60fps); vercel react-view-transitions.
- **Sources:** greensock/gsap-skills README (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 11 — supabase/agent-skills (backend/DB exemplar)
- **Canonical identity:** `github:supabase/agent-skills` — skills: `supabase`, `supabase-postgres-best-practices`
- **Category:** Skills → Domain pack (backend/DB/auth)
- **Type:** skill pack (`SKILL.md` + `references/`)
- **Official URL:** https://github.com/supabase/agent-skills
- **Description:** Supabase-vendor skills: full-product coverage (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues; `supabase-js`/`@supabase/ssr` in Next/React/SvelteKit/Astro/Remix; RLS/JWT/cookies; CLI/MCP; migrations; pg extensions) + Postgres best-practices guideline skill. Releases publish `dist/index.json` discovery index conforming to agent `/.well-known/agent-skills/` URI spec (schema 0.2.x).
- **Contents inspected:** README + `skills/supabase/SKILL.md` frontmatter fetched (`name: supabase`, trigger-everything description, `metadata: {author: supabase, version: 0.1.2}`); install commands verified (`npx skills add supabase/agent-skills [--skill supabase|supabase-postgres-best-practices]`).
- **Capabilities:** Schema/auth debugging, RLS audit, migration + extension guidance, logs triage.
- **Usage domain:** Any Supabase task; Postgres performance review.
- **Integration:** Official (Supabase docs `ai-tools/ai-skills.mdx` + plugin bundling MCP server + skills one-step setup).
- **Compatibility:** Official (evidence: vendor repo + docs + release discovery index); skill files Shared standard (18+ agents claimed).
- **Deps:** Supabase project; MCP server optional companion.
- **Availability:** GitHub public.
- **Maintenance:** Active (release-please pipeline, versioned skills).
- **License:** Verify repo file.
- **Security/limits:** Skills touch auth/RLS/keys — review generated policies; keep service keys out of skill-invoked logs.
- **Related:** stripe skills (API-money adj.); cloudflare/skills (deploy adj.).
- **Sources:** supabase/agent-skills README + SKILL.md (fetched); supabase/supabase docs mdx.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 12 — Stripe agent skills (API/payments exemplar)
- **Canonical identity:** `github:stripe/ai` (`skills/stripe-best-practices/SKILL.md`) — docs: https://docs.stripe.com/skills
- **Category:** Skills → Domain skill (API/payments)
- **Type:** skill (vendor-maintained guidance) + plugin path (auto-configures MCP + skills + updates)
- **Official URL:** https://docs.stripe.com/skills (repo: https://github.com/stripe/ai)
- **Description:** Stripe-maintained integration routing: Checkout Sessions vs PaymentIntents, Connect v2/Accounts, billing/subscriptions, Tax/registrations, Treasury, Checkout vs Payment Element, deprecated-API migration, key/webhook/OAuth security. Manual path: `npx skills add https://docs.stripe.com` (+ `npx skills update -y` to stay current); plugin path auto-updates.
- **Contents inspected:** `stripe-best-practices/SKILL.md` frontmatter fetched (routing description incl. "building, modifying, or reviewing any Stripe integration… subscriptions… connected accounts… secure key handling"); docs page install/update + plugin-vs-manual distinction verified.
- **Capabilities:** API selection, Connect setup, billing/tax wiring, webhook/key hardening.
- **Usage domain:** Any Stripe build/modify/review task.
- **Integration:** Official (plugin with MCP + auto-update; manual npx fallback).
- **Compatibility:** Official (evidence: docs.stripe.com + stripe/ai repo); Shared standard content.
- **Deps:** Stripe account; MCP server for live data (manual setup needs both).
- **Availability:** Docs + GitHub.
- **Maintenance:** Active (vendor tracks latest API guidance).
- **License:** Verify (docs ToS + repo file).
- **Security/limits:** Manually installed skills don't auto-update — stale payment guidance is a live risk; run `update -y`; restricted keys + webhook signature verify per skill.
- **Related:** supabase skills (SaaS wiring); community `stripe-developer` orchestrator (Next+Supabase+Vercel refs) — community, verify before use.
- **Sources:** stripe/ai SKILL.md; docs.stripe.com/skills (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 13 — cloudflare/skills (deploy/backend exemplar)
- **Canonical identity:** `github:cloudflare/skills`
- **Category:** Skills → Domain pack (deploy/backend/edge)
- **Type:** skill pack + plugin (skills + Cloudflare Code-Mode MCP server bundle)
- **Official URL:** https://github.com/cloudflare/skills/
- **Description:** Vendor skills for Workers, Pages, storage (KV/D1/R2), AI (Workers AI, Vectorize, Agents SDK), networking (Tunnel, Spectrum), security (WAF/DDoS), IaC, plus `agents-sdk`, `durable-objects`, `sandbox-sdk`, `wrangler`, `web-perf` (Core Web Vitals), MCP/agent builders. Root `cloudflare` skill routes to product skills + docs.
- **Contents inspected:** README fetched (skill table, `/cloudflare:build-agent|build-mcp` commands, MCP bundle note, `npx skills add https://github.com/cloudflare/skills`, per-agent copy-dirs table, Cursor Remote Rule, VS Code plugin-from-source flow).
- **Capabilities:** Product selection, Workers/D1/KV deploy, agents/MCP scaffolding, perf audit.
- **Usage domain:** Build + deploy on Cloudflare edge platform.
- **Integration:** Official (Claude marketplace `/plugin marketplace add cloudflare/skills`, Cursor marketplace, npx CLI).
- **Compatibility:** Official (evidence: vendor install matrix); skill files Shared standard.
- **Deps:** Cloudflare account; Wrangler for deploy actions.
- **Availability:** GitHub public.
- **Maintenance:** Active (Dec-2025 origin, maintained).
- **License:** Verify repo file.
- **Security/limits:** Skills can invoke account-scoped deploys — scope API tokens, review wrangler actions.
- **Related:** vercel deploy skills (record 14); supabase skills.
- **Sources:** cloudflare/skills README raw + rendered (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 14 — vercel deploy + optimize skills (deploy + optimizer exemplars)
- **Canonical identity:** `skill:vercel-deploy-claimable` + `skill:vercel-optimize` — both in `github:vercel-labs/agent-skills`
- **Category:** Skills → Domain skills (deploy; optimizer)
- **Type:** skill + skill (deploy runner with scripts; auditor producing ranked report)
- **Official URL:** https://github.com/vercel-labs/agent-skills (skill sections: vercel-deploy-claimable, vercel-optimize)
- **Description:** Deploy: framework auto-detect (40+), tarball packaging, preview + claim URLs, static-HTML handling — built for Claude.ai/Desktop conversations. Optimize: metrics-first audit (cost, perf, reliability, caching, functions, billing) investigating only metric-indicated routes.
- **Contents inspected:** README sections fetched (feature lists, 4-step deploy flow, sample output URLs, optimize trigger list).
- **Capabilities:** One-shot deploy from chat; ranked cost/perf remediation.
- **Usage domain:** Ship preview + claim; cut Vercel bill / fix slow routes.
- **Integration:** Official (`npx skills add vercel-labs/agent-skills`; Claude Code copy-to-`~/.claude/skills/` documented).
- **Compatibility:** Official (evidence: Vercel repo + docs); Shared standard files.
- **Deps:** Deployment service endpoint; Vercel metrics access for optimize.
- **Availability:** GitHub MIT.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Claim-URL flow transfers ownership — treat claim links as secrets; audit tarball contents pre-upload.
- **Related:** cloudflare/skills; autoship release skill (vercel-labs/autoship).
- **Sources:** repo README (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 15 — mcp-builder skill (API/tooling exemplar)
- **Canonical identity:** `skill:mcp-builder` — `github:anthropics/skills/tree/main/skills/mcp-builder`
- **Category:** Skills → Domain skill (API/backend tooling)
- **Type:** skill (MCP server generation guidance)
- **Official URL:** https://github.com/anthropics/skills/tree/main/skills/mcp-builder
- **Description:** Anthropic technical skill guiding MCP server construction (tool schemas, resources, server scaffolding patterns) — the canonical "skill builds the connector the agent then uses" loop.
- **Contents inspected:** Repo tree presence verified (listed in skills/); body not line-verified this pass.
- **Capabilities:** MCP server design/scaffold/review.
- **Usage domain:** Exposing APIs/data to agents via MCP.
- **Integration:** Native (Claude) / Shared standard.
- **Compatibility:** Official for Claude (evidence: ships in anthropics/skills); Shared standard content (evidence: spec-conformant layout per repo convention) — body-level verification pending.
- **Deps:** MCP SDK of target language.
- **Availability:** Via anthropics/skills repo.
- **Maintenance:** Active (with parent repo).
- **License:** Check per-skill LICENSE.txt.
- **Security/limits:** Generated servers are credential-bearing code — review scopes before running.
- **Related:** cloudflare building-mcp-server skill; Stripe MCP+skills plugin pattern.
- **Sources:** anthropics/skills tree (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (presence confirmed, body unverified)

### 16 — webapp-testing skill (testing exemplar)
- **Canonical identity:** `skill:webapp-testing` — `github:anthropics/skills/tree/main/skills/webapp-testing`
- **Category:** Skills → Domain skill (testing/debugging-UI)
- **Type:** skill (`SKILL.md` + `scripts/with_server.py` + `examples/`)
- **Official URL:** https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md
- **Description:** Playwright-based local webapp verification: server-lifecycle helper, reconnaissance-then-action (networkidle → screenshot/DOM → selectors → act), headless Chromium, console-log capture, static-HTML file:// path.
- **Contents inspected:** Full SKILL.md fetched — frontmatter `name: webapp-testing`, `description: "Toolkit for interacting with and testing local web applications using Playwright…"`, `license: Complete terms in LICENSE.txt`; decision tree, `with_server.py` single/multi-server patterns, common-pitfall rule verified verbatim.
- **Capabilities:** Frontend verification, UI debugging, screenshots, browser-log triage.
- **Usage domain:** "Verify this page works" for local dev servers.
- **Integration:** Native (Claude) / Shared standard.
- **Compatibility:** Native for Claude; Shared standard elsewhere (evidence: frontmatter + layout conform to spec; needs Python+Playwright at runtime — capability, not harness lock-in).
- **Deps:** Python 3, Playwright, Chromium, project dev server.
- **Availability:** Via anthropics/skills repo.
- **Maintenance:** Active.
- **License:** Proprietary LICENSE.txt.
- **Security/limits:** Launches browsers/servers locally — bind ports to localhost; don't run against untrusted pages with creds loaded.
- **Related:** Trail of Bits testing-handbook skills (record 22); TDD skills (records 06/07).
- **Sources:** SKILL.md blob (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 17 — Debugging skills: systematic-debugging + diagnosing-bugs (debugging exemplars)
- **Canonical identity:** `skill:systematic-debugging` (`github:obra/superpowers`) + `skill:diagnosing-bugs` (`github:mattpocock/skills/skills/engineering/diagnosing-bugs`)
- **Category:** Skills → Domain skills (debugging)
- **Type:** skill + skill (both are workflows: phased diagnosis loops)
- **Official URL:** https://github.com/obra/superpowers (debugging library) · https://github.com/mattpocock/skills (diagnosing-bugs SKILL.md)
- **Description:** superpowers: 4-phase root-cause process (+ root-cause-tracing, defense-in-depth, condition-based-waiting, verification-before-completion). mattpocock: red-loop diagnosis (reproduce → minimise → hypothesise → instrument → fix → regression-test) for hard bugs/perf regressions.
- **Contents inspected:** superpowers skills library (debugging section) + diagnosing-bugs loop summary fetched; full SKILL.md bodies not line-verified this pass.
- **Capabilities:** Root-cause isolation, flake/async patterns, fix verification, regression tests.
- **Usage domain:** Any "it's broken / slow / flaky" task.
- **Integration:** Via parent packs (marketplace / npx).
- **Compatibility:** Shared standard content; Documented adapter install (evidence: parent-pack install docs) — body text Unverified beyond summaries.
- **Deps:** Parent pack install.
- **Availability:** Via parent repos.
- **Maintenance:** Active (both parents).
- **License:** Parent repo terms (verify).
- **Security/limits:** Debugging skills may request logs/dumps — scrub secrets before pasting; superpowers `diagnosing-superpowers` explicitly supports scrubbed bundles.
- **Related:** webapp-testing (UI evidence); trailmark (code-graph slicing for audits).
- **Sources:** parent READMEs (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — Review skills: differential-review + code-review + second-opinion (review exemplars)
- **Canonical identity:** `plugin:differential-review` (`github:trailofbits/skills`) + `skill:code-review` (`github:mattpocock/skills`) + `plugin:second-opinion` (trailofbits)
- **Category:** Skills → Domain skills/workflows (review)
- **Type:** workflow/plugin + skill + plugin-agent (methodology + subagent execution patterns)
- **Official URL:** https://trailofbits.com/skills/differential-review/ · https://github.com/mattpocock/skills (code-review SKILL.md)
- **Description:** differential-review: phased security review of diffs (triage → code analysis → test coverage → blast radius → attacker modeling → report), with `methodology.md/adversarial.md/reporting.md/patterns.md` + namespaced `differential-review:adversarial-modeler` subagent (bare name fails dispatch — documented gotcha). mattpocock code-review: two-axis diff review (Standards incl. Fowler smells vs Spec fidelity) as parallel subagents. second-opinion: cross-model review via external LLM CLIs (Codex/Gemini), bundling Codex MCP server.
- **Contents inspected:** Trail of Bits skill page (phase tree + agent name + supporting docs) fetched; mattpocock code-review two-axis summary fetched.
- **Capabilities:** PR/commit security + quality review; exploit-scenario modeling; cross-model verification.
- **Usage domain:** Pre-merge gates; audit diff triage.
- **Integration:** Marketplace plugins + skill files.
- **Compatibility:** Official (trailofbits, evidence: marketplace + skill pages); Shared standard skill content; second-opinion needs external CLIs (capability-gated, not harness-gated).
- **Deps:** git history; external CLIs for second-opinion.
- **Availability:** GitHub (CC-BY-SA skill content — see record 19).
- **Maintenance:** Active.
- **License:** CC-BY-SA-4.0 (trailofbits); MIT (mattpocock).
- **Security/limits:** Reviewers read full diffs — scope to the change; external-model review sends code off-machine (policy check first).
- **Related:** superpowers requesting/receiving-code-review; code-improver fix loop.
- **Sources:** trailofbits.com skill page; mattpocock README (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (page-level verified; SKILL.md bodies not line-read)

### 19 — trailofbits/skills marketplace (security exemplar)
- **Canonical identity:** `github:trailofbits/skills` — marketplace `.claude-plugin/marketplace.json` (~35 plugins)
- **Category:** Skills → Plugin marketplace (security/review/testing)
- **Type:** plugin marketplace (each plugin bundles skills + agents + commands)
- **Official URL:** https://github.com/trailofbits/skills (docs: https://trailofbits-skills.mintlify.app/)
- **Description:** Auditor-authored marketplace: smart-contract (`building-secure-contracts` 6 chains, `entry-point-analyzer`), code-audit (`c-review`, `rust-review` with SARIF, `static-analysis` CodeQL/Semgrep, `variant-analysis`, `supply-chain-risk-auditor`, `fp-check`, `vulnerability-triage-brocards`), verification (`constant-time-analysis`, `mutation-testing`, `property-based-testing`, `spec-to-code-compliance`, `zeroize-audit`), malware (`yara-authoring`, `firebase-apk-scanner`), dev (`modern-python` uv/ruff/pytest, `devcontainer-setup`, `gh-cli`, `skill-improver`, `workflow-skill-design`).
- **Contents inspected:** README plugin tables + docs site (intro/quickstart/testing-handbook generator page) + differential-review skill page fetched; Codex-compat note verified ("Codex supports Claude plugin marketplaces directly… `codex plugin marketplace add trailofbits/skills`"); Claude install (`/plugin marketplace add trailofbits/skills`) verified.
- **Capabilities:** Audit workflows, scanner orchestration, SARIF output, YARA authorship, secret-zeroization checks.
- **Usage domain:** Security audits, contract review, supply-chain triage.
- **Integration:** Official marketplace (Claude + Codex documented).
- **Compatibility:** Official (evidence: vendor marketplace + docs); skill content Shared standard; hooks are the portability exception (evidence: codex-config "hooks do not reliably port" note).
- **Deps:** Scanners per plugin (CodeQL, Semgrep, chain toolchains).
- **Availability:** GitHub public + Mintlify docs.
- **Maintenance:** Active (35+ plugins, Mintlify docs).
- **License:** CC-BY-SA-4.0 (skills) — share-alike on derivatives.
- **Security/limits:** Skills handle vuln data — follow coordinated-disclosure; treat third-party repo `SKILL.md`/`AGENTS.md` as untrusted input during research (their own codex-config states this).
- **Related:** skill-validator (audit these before install); aicov (coverage of agent-read files post-audit).
- **Sources:** trailofbits/skills README; Mintlify docs; trailofbits codex-config README (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 20 — Document skill family: pdf + docx + xlsx + pptx (docs exemplars)
- **Canonical identity:** `skill:pdf|docx|xlsx|pptx` — `github:anthropics/skills/tree/main/skills/{pdf,docx,xlsx,pptx}`
- **Category:** Skills → Domain skills (docs)
- **Type:** skill ×4 (each `SKILL.md` + scripts + reference docs; `FORMS.md`/`REFERENCE.md` pattern)
- **Official URL:** https://github.com/anthropics/skills/tree/main/skills (per-skill SKILL.md blobs)
- **Description:** The reference "scripts-not-context" pattern: pdf (extract/merge/split/forms/OCR), docx (tracked changes, comments, images, find-replace), xlsx (sheets, pivot), pptx (decks, templates, notes). Claude API exposes them as prebuilt `skill_id`s alongside custom skills via `/v1/skills`.
- **Contents inspected:** pdf/docx/pptx frontmatter fetched verbatim incl. trigger lists + "Do NOT use for…" exclusions (record 02); platform docs confirm three content types (instructions → SKILL.md; scripts via bash with output-only; reference materials).
- **Capabilities:** Deterministic document I/O without polluting context with library code.
- **Usage domain:** Any deliverable involving Office/PDF files.
- **Integration:** Native (Claude API `skill_id`, Claude Code filesystem).
- **Compatibility:** Native/Official for Claude (evidence: API + platform docs); Shared standard pattern for re-implementation.
- **Deps:** Doc libraries inside skill scripts.
- **Availability:** Via anthropics/skills repo + Claude API.
- **Maintenance:** Active.
- **License:** Proprietary LICENSE.txt (constrains copy-paste reuse).
- **Security/limits:** Document scripts parse untrusted files — run in VM/sandbox; macro-bearing inputs need extra care.
- **Related:** skill-creator (their eval loop was built around doc skills); writing-guidelines (record 23).
- **Sources:** SKILL.md blobs; platform.claude.com docs (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 21 — skill-creator (generator exemplar #1: full authoring + eval loop)
- **Canonical identity:** `skill:skill-creator` — `github:anthropics/skills/tree/main/skills/skill-creator` (+ Codex sample `skill-creator` in `openai/codex`)
- **Category:** Skills → Tooling (generator)
- **Type:** skill (meta-skill: creates/improves/evaluates other skills) + workflow (eval pipeline)
- **Official URL:** https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- **Description:** End-to-end authoring: intent capture → draft SKILL.md (pushy descriptions to counter undertriggering) → 2–3 test prompts → parallel with-skill/baseline subagent runs → grader + `aggregate_benchmark` → `eval-viewer/generate_review.py` human review → iterate → 20-query description optimizer (`run_loop.py`, 60/40 train/test, 5 iterations) → `package_skill.py` `.skill` packaging. Adapters for Claude.ai (no subagents: inline runs, no baselines) and Cowork (static HTML viewer).
- **Contents inspected:** Full 485-line SKILL.md fetched (all sections verified: anatomy, progressive disclosure, lack-of-surprise, writing patterns, eval steps, blind comparison, description optimization, packaging).
- **Capabilities:** New-skill scaffolding, iterative improvement, quantitative benchmarking, trigger optimization, packaging.
- **Usage domain:** Authoring any production skill in this catalog.
- **Integration:** Native (Claude) ; Codex sample variant (`init_skill.py`, `agents/openai.yaml`) for Codex authoring.
- **Compatibility:** Native for Claude (evidence: full fetched body); Documented adapter for Codex (evidence: openai/codex sample skill-creator); Shared standard output (produces spec-conformant skills).
- **Deps:** Subagents + browser for full loop; Python for scripts.
- **Availability:** Via parent repos.
- **Maintenance:** Active.
- **License:** Parent terms (Anthropic skill license; check file).
- **Security/limits:** Lack-of-surprise rule (no malware/exfiltration skills); eval baselines snapshot old skill before editing.
- **Related:** skills-janitor precheck (pre-author overlap check); skill-factory authoring arm; writing-for-agents (record 07).
- **Sources:** SKILL.md blob; openai/codex sample (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 22 — testing-handbook-skills generator (generator exemplar #2: doc-to-skills factory)
- **Canonical identity:** `plugin:testing-handbook-skills` — `github:trailofbits/skills` (`plugins/testing-handbook-skills/`)
- **Category:** Skills → Tooling (generator: handbook → 16 skills)
- **Type:** skill (meta-skill generator) + workflow (generate → validate → cross-reference)
- **Official URL:** https://trailofbits-skills.mintlify.app/plugins/testing-handbook-skills
- **Description:** Generates Claude Code skills from the Trail of Bits Application Security Testing Handbook: 4 templates (Tool/Fuzzer/Technique/Domain), agent prompt template with variable substitution, Hugo→Mintlify conversion, line-count splitting, `validate-skills.py` quality gate, README + cross-reference graph updates. Ships generator AND 16 pre-generated skills (fuzzers, SAST, sanitizers, coverage).
- **Contents inspected:** Plugin docs page fetched (templates, architecture, example content contract: frontmatter + when-to-use/NOT-use + quickstart + CI + troubleshooting).
- **Capabilities:** Bulk skill synthesis from authoritative docs with validation.
- **Usage domain:** Turning any handbook/docs corpus into a skill library.
- **Integration:** Marketplace plugin.
- **Compatibility:** Official (evidence: vendor docs); output Shared standard (validated skills).
- **Deps:** Handbook source; validator script.
- **Availability:** Via trailofbits/skills marketplace.
- **Maintenance:** Active.
- **License:** CC-BY-SA-4.0 (parent marketplace).
- **Security/limits:** Generated testing skills drive scanners/fuzzers — sandbox execution targets.
- **Related:** skill-creator (bespoke authoring); skill-compact (post-generation dedup).
- **Sources:** Mintlify plugin page (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (docs verified; generator scripts not executed)

### 23 — writing-guidelines + research skills (docs/research exemplars)
- **Canonical identity:** `skill:writing-guidelines` (`github:vercel-labs/agent-skills`) + research skills indexed via records 04/05 (Firecrawl, Exa, Context7 patterns)
- **Category:** Skills → Domain skills (docs/research)
- **Type:** skill (audit ruleset) + skill references (research connectors vary by vendor)
- **Official URL:** https://github.com/vercel-labs/agent-skills (writing-guidelines section) · https://vercel.com/docs/agent-resources/skills
- **Description:** writing-guidelines: 80+ Vercel writing-handbook rules (plan, voice/tone by content type, headings, lists, code samples TS-first, placeholders, typography, pricing pages, AI-workflow disclosure, PR discipline). Research: agent skills wrapping search/crawl/doc-fetch (Firecrawl whole-site→markdown, Exa web/code search, Context7 live docs) discovered through awesome indexes + skills.sh — patterns consistent, vendors multiple.
- **Contents inspected:** writing-guidelines categories + triggers ("Review my docs", "Check writing style") fetched from Vercel README; research-skill existence confirmed via VoltAgent vendor tables + trailofbits codex-config Context7/Exa wiring note.
- **Capabilities:** Docs-voice audit; web/docs research grounding for agents.
- **Usage domain:** Docs PRs; pre-implementation unknown-domain research.
- **Integration:** npx skills / marketplace per vendor.
- **Compatibility:** Official (writing-guidelines, evidence: Vercel repo); research skills Documented adapter → verify per vendor (evidence: index listings + config wiring, no single canonical SKILL.md fetched) — recorded as Partially.
- **Deps:** Search/crawl API keys for research skills.
- **Availability:** GitHub + skills.sh.
- **Maintenance:** Active.
- **License:** MIT (writing-guidelines); per-vendor for research.
- **Security/limits:** Research skills fetch untrusted web content — treat as untrusted input; crawl keys scoped.
- **Related:** doc-coauthoring/internal-comms (enterprise writing); mcp-builder (Context7-style doc MCPs).
- **Sources:** vercel-labs README; VoltAgent tables; trailofbits codex-config (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 24 — Discovery/install utils: `npx skills` CLI + skills.sh + $skill-installer (installer exemplars)
- **Canonical identity:** `npm:skills` (`github:vercel-labs/skills`) — directory https://skills.sh — Codex `$skill-installer` sample (`github:openai/codex/.../skill-installer`)
- **Category:** Skills → Tooling (discovery/install)
- **Type:** util (CLI) + marketplace/directory (skills.sh) + workflow (skill-installer skill)
- **Official URL:** https://github.com/vercel-labs/skills · https://skills.sh · https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem
- **Description:** `npx skills` CLI: `add <owner/repo> [--skill name] [-g] [-a agents] [-s skills] [--copy] [-y] [--all]`; `use` (ephemeral, pipeable: `npx skills use … | claude`); `find` (interactive/by-keyword); `list/ls`; `remove`; `update`; `init` (SKILL.md template). Auto-detects 70+ agents with per-agent project/global paths; bounded depth-3 catalog walk over skill container dirs + plugin-manifest discovery + `--full-depth` fallback; per-release immutable discovery index. skills.sh: public directory + leaderboard. $skill-installer: in-Codex curated/experimental installer (`scripts/install-skill-from-github.py`, direct-download → git-sparse-checkout fallback, private-repo via git creds/token).
- **Contents inspected:** CLI README (commands/flags/discovery rules/manifest support/40–75 agents) + npm page + Vercel changelog announcement + Codex skill-installer SKILL.md fetched.
- **Capabilities:** Cross-harness install/update/remove/search/scaffold; shareable one-liners (`npx skills add owner/repo`).
- **Usage domain:** Every install command quoted in this catalog.
- **Integration:** Native distribution channel for the ecosystem.
- **Compatibility:** Documented adapter (evidence: per-agent path table + agent docs links for 18+ harnesses; `allowed-tools` support matrix showing Zencoder/Kiro gaps) — adapter coverage documented, not universal.
- **Deps:** Node/npx; git for fallback paths.
- **Availability:** npm + GitHub + skills.sh.
- **Maintenance:** Active (Jan-2026 launch, 70+ agents).
- **License:** Verify repo file.
- **Security/limits:** Installer writes files into agent dirs — a malicious skill repo lands executable scripts + hook configs; precheck (record 27) before adding unknowns; prefer `--skill` scoping over `--all`.
- **Related:** skills-janitor precheck; skill-factory tiered search; awesome indexes (records 04/05) as search front-ends.
- **Sources:** vercel-labs/skills README; npm `skills` page; Vercel changelog; openai/codex skill-installer sample (all fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 25 — Validators: skill-validator + skref + skills-ref (validator exemplars)
- **Canonical identity:** `github:agent-ecosystem/skill-validator` + `github:alephic-ai/skref` (+ `github:agentskills/agentskills/skills-ref`)
- **Category:** Skills → Tooling (validator)
- **Type:** util (CLIs; skref also ships as GitHub Action)
- **Official URL:** https://github.com/agent-ecosystem/skill-validator · https://github.com/alephic-ai/skref
- **Description:** skill-validator: spec compliance PLUS link resolution, non-standard-file flags, token/context budgeting, content-quality metrics (density, imperative ratio), cross-language contamination detection, LLM-as-judge scoring (clarity/actionability/novelty), pre-commit hooks per platform, multi-skill-dir detection. Commands: `validate structure|links`, `analyze content|contamination`, `score evaluate|report`, `check` (all-but-LLM). skref: Rust port of `skills-ref` — `validate`, `read-properties`, `to-prompt` (`<available_skills>` block), single static binary + Action. skills-ref: canonical Python reference (`skills-ref validate`).
- **Contents inspected:** Both READMEs fetched (command tables, rule tables incl. name/directory match, 64/1024/500 limits, orphan-file reachability rule, `--allow-dirs/--allow-flat-layouts/--allow-extra-frontmatter` escape hatches, Action inputs).
- **Capabilities:** Pre-publish gates, CI validation, token budgeting, quality scoring.
- **Usage domain:** Every skill authored or vendored in this catalog before install.
- **Integration:** CLI + pre-commit + GitHub Action.
- **Compatibility:** Shared standard enforcement (evidence: rule tables mirror spec fields; `--allow-claude-fields` flag documents the Custom-extension boundary explicitly).
- **Deps:** Python (skill-validator/skills-ref) / none (skref binary); LLM key only for `score`.
- **Availability:** GitHub public.
- **Maintenance:** Active (both repos).
- **License:** Verify per repo.
- **Security/limits:** Validators check structure/links, not malice — a valid skill can still be hostile; pair with janitor precheck + manual script review.
- **Related:** moutons/skills-validator (alt 5-pass pipeline); coreyhaines31 validate-skills-official.sh pattern.
- **Sources:** both READMEs (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 26 — Optimizers: skill-compact + description optimizer + vercel-optimize (optimizer exemplars)
- **Canonical identity:** `github:JuanJoseGonGi/skill-compact` + optimizer loop in `skill-creator/scripts/run_loop.py` + `skill:vercel-optimize`
- **Category:** Skills → Tooling (optimizer)
- **Type:** skill (skill-compact: agent-executed compaction) + workflow (run_loop) + skill (vercel-optimize auditor)
- **Official URL:** https://github.com/JuanJoseGonGi/skill-compact · https://github.com/vercel-labs/agent-skills (vercel-optimize)
- **Description:** skill-compact finds duplication across installed skills (demo corpus: 120 skills, 25,874 lines, ~222k tokens, 16 dupes in 4 clusters, 30–40% boilerplate); strategies per cluster (merge/absorb/extract-shared/refactor/no-op); backup → compact → spec-validate (<500 lines, <5k tokens) → source-tracked manifest + update-then-recompact per manager. "They install, we optimize." Description optimizer: 60/40 train/test trigger-eval loop, 3 runs/query, 5 iterations, best-by-test-score. vercel-optimize: runtime cost/perf auditor (record 14).
- **Contents inspected:** skill-compact README (metrics table, strategy table, script phases, manager matrix) fetched; run_loop mechanism from skill-creator SKILL.md (record 21); vercel-optimize section (record 14).
- **Capabilities:** Token-budget recovery, trigger-accuracy tuning, deploy-cost reduction.
- **Usage domain:** Post-install hygiene for large skill sets; pre-publish tuning.
- **Integration:** Skill/CLI per tool.
- **Compatibility:** Shared standard (evidence: gates reference agentskills.io limits); manager-detection table is Documented adapter behavior.
- **Deps:** Host agent (skill-compact intelligence); Vercel metrics (optimize).
- **Availability:** GitHub.
- **Maintenance:** Active.
- **License:** Verify per repo.
- **Security/limits:** Compaction rewrites skill instructions — keep timestamped backups (tool does), re-validate, spot-check merged triggers.
- **Related:** lifecycle/pruning (record 27 — compact pairs with prune); skill-creator evals.
- **Sources:** skill-compact README; skill-creator SKILL.md; vercel-labs README (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (docs verified; demo metrics are author-reported)

### 27 — Lifecycle/pruning: quartermaster + skillkit + janitor + skill-factory + skill-cleaner (lifecycle exemplars)
- **Canonical identity:** `github:ginaecho/skill-quartermaster` (`qm`) + `github:cravenceiling/skill-kit` (`skillkit`) + `github:prateek/skills-janitor` (7 janitor-* skills) + `github:rooftop-Owl/skill-factory` (9 commands) + `skill-cleaner` (`github:steipete/agent-scripts`)
- **Category:** Skills → Tooling (lifecycle/pruning)
- **Type:** util + skill pack + plugin (mixed; all manage skill state, not skill content)
- **Official URL:** https://github.com/ginaecho/skill-quartermaster · https://github.com/cravenceiling/skill-kit · https://github.com/prateek/skills-janitor · https://github.com/rooftop-Owl/skill-factory
- **Description:** quartermaster: non-destructive tiered lifecycle (active→demoted→hidden→archived→deleted-only-with---yes), intent compiler (~30-skill sweet spot; reported 851→30 set, 59.7k→2.2k tokens, byte-identical restore 200/200, 97%-vs-93% selection A/B), telemetry hooks, policy proposals + human gate, gap→author→graduate arm. skillkit: local-first usage analytics (JSONL/SQLite session parsing, Claude+OpenCode connectors), `stats/list/health/prune` (30-day unused). janitor: 7 slash skills (audit/report/fix/usage/tokens/search/precheck), realpath-deduped duplicates, dry-run-by-default, Codex+Claude coverage. skill-factory: full lifecycle (tiered search T0–T5 across Skyll/LobeHub/skills.sh/openskills/GitHub/awesome-lists → import with provenance manifest → validate/audit/health/eval → clean remove). skill-cleaner: prompt-budget trim + duplicate + root audit script.
- **Contents inspected:** All four READMEs + skill-cleaner page fetched (command tables, state tables, metric claims, connector lists).
- **Capabilities:** Install→use→demote→restore→delete governance; context-budget reclamation; overlap precheck.
- **Usage domain:** Any agent with more than ~30 skills installed (the accuracy sweet-spot ceiling).
- **Integration:** CLI + slash skills + hooks.
- **Compatibility:** Documented adapter (evidence: per-runtime adapter tables; skillkit's "only Claude+OpenCode have trackable Skill invocations" is an honest adapter-limit statement).
- **Deps:** Session history access (JSONL/SQLite); local-only telemetry.
- **Availability:** GitHub (+ skills.sh listings).
- **Maintenance:** Active (2026 repos).
- **License:** Verify per repo (skill-factory MPL-2.0 stated).
- **Security/limits:** Pruners delete files — require dry-run + explicit confirm; telemetry stays local (verify before enabling); reported A/B/token metrics are author-run, treat as directional.
- **Related:** validators (precheck before add); optimizers (compact after prune); marketplaces (intake sources).
- **Sources:** four READMEs + skills.sh skill-cleaner page (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (interfaces verified; efficacy metrics author-reported)

### 28 — Marketplaces: Claude plugins + skills.sh + vendor/federated directories (marketplace exemplars)
- **Canonical identity:** `github:anthropics/claude-plugins-official` + https://skills.sh + vendor marketplaces (trailofbits/skills, obra/superpowers-marketplace, mattpocock via official) + federated search (Skyll 89k+, LobeHub 100k+, openskills, GitHub topics, awesome-lists)
- **Category:** Skills → Distribution (marketplace)
- **Type:** plugin marketplace + directory/leaderboard + federated search tiers
- **Official URL:** https://code.claude.com/docs/en/discover-plugins · https://skills.sh · https://github.com/trailofbits/skills
- **Description:** Claude official marketplace (acceptance bar; superpowers PR #148; mattpocock-skills listed) with `/plugin marketplace add` + `/plugin install` flows; skills.sh directory + leaderboard + per-package pages (`skills.sh/<owner>/<repo>`) fed by release discovery indexes; vendor marketplaces (trailofbits 35 plugins; obra; cloudflare; greensock dual `.claude-plugin/`+`.cursor-plugin/` manifests); skill-factory T0–T5 cascade documents the federated reality (300k+ skills, no single registry complete); Codex side uses plugin-bundled distribution post-deprecation.
- **Contents inspected:** Marketplace install commands + acceptance refs fetched across records 06/07/13/19; skills.sh badges/links verified in vercel/cloudflare READMEs; skill-factory search-tiers table fetched.
- **Capabilities:** Trusted-channel install, versioned releases, leaderboard signal, cross-registry search.
- **Usage domain:** Sourcing every skill in this catalog.
- **Integration:** Native per harness.
- **Compatibility:** Official per vendor (evidence: install commands + docs); federated tiers Reference-only-to-Documented adapter (evidence: skill-factory tier table) — marketplace presence is NOT a functional guarantee; verify SKILL.md + validators per skill.
- **Deps:** Host agent marketplace support.
- **Availability:** Public.
- **Maintenance:** Active.
- **License:** Per-skill (marketplace aggregates mixed licenses incl. Proprietary + CC-BY-SA).
- **Security/limits:** Marketplace is not an audit — pin versions, review scripts/hooks, run validators; untrusted-repo rule stands even for marketplace-sourced research targets.
- **Related:** All records (distribution layer); lifecycle intake (record 27).
- **Sources:** Claude plugin docs; skills.sh; vendor READMEs; skill-factory handbook (fetched).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (channels verified; per-skill guarantees explicitly not claimed)

---

**Count: 28 resources** (meets 20–30 requirement). No install/execute performed. SKILL.md frontmatter/bodies line-verified where marked Verified (records 01, 02, 06, 07, 08, 09, 10, 11, 12, 13, 14, 16, 20, 21, 24, 25); page/tree-level verification where marked Partially (03-deprecated pointer, 04/05 indexes, 15, 17, 18, 22, 23, 26-metrics, 27-metrics, 28-channels). Type recorded per record (skill vs prompt vs workflow vs plugin vs methodology vs standard/index/util — no prompts catalogued: all executable entries are skills or higher-order groupings). Compatibility recorded per record with evidence; MD-readable ≠ works observed throughout (Copilot GSAP path, Codex hooks non-portability, Zencoder/Kiro `allowed-tools` gaps, adapter-only research skills).