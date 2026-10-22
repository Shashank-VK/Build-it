# E — Prompt Directory (Metadata Only — No Bodies)
Date: 2026-10-09
Rule: METADATA ONLY. Do NOT reproduce prompt text. No bypass, no credentials, no jailbreak content. For each entry: exact URL, claimed source, types, structure, filenames, date, provenance (+evidence), accessibility, authenticity limits.
Method: read-only WebSearch + WebFetch. Star/commit counts are point-in-time excerpts.

## Record schema
- `URL:` exact link inspected or cataloged
- `Claimed source:`
- `Types / structure / filenames:`
- `Date:`
- `Provenance:` official | reproduced | archived | alleged-leak | unverified (+evidence)
- `Accessibility:`
- `Authenticity limits:`

---

### P-01. asgeirtj/system_prompts_leaks (alleged-leak collection — metadata only)
- URL: https://github.com/asgeirtj/system_prompts_leaks
- Claimed source: community curation by `asgeirtj`; claims "full verbatim system prompts behind the most popular chatbots", PRs welcome, contact if different result observed.
- Types / structure / filenames: top-level vendor folders observed on `main`: `Anthropic/`, `Cursor/`, `DeepSeek/`, `GLM/`, `Google/`, `Kimi/`, `Meta/`, `Microsoft/`, `Misc/`, `Mistral/`, `Notion/`, `OpenAI/`, `Perplexity/`, `Pi/`, `Qwen/`, `xAI/` + `.github/`, `LICENSE`, `README.md`. README sub-indexes (filenames observed, bodies NOT accessed): `Anthropic/claude-haiku-5.5.md`, `claude-sonnet-5.5.md`, `claude-opus-5.5.md`, `claude-fable-5.1.md`, `claude-code/claude-code-opus-5.5.md`, `claude-code-sonnet-5.5.md`, `claude-code-haiku-5.5.md`, `claude-code-cloud-fable-5.1.md`, `claude-design/claude-design.md`, `claude-cowork/claude-cowork.md`, `OpenAI/dots/dreamer.md`, `dots/voice.md`, `dots/tools.md`, `dots/available-skills.md`, `dots/skills`, `Codex/gpt-6.1-sol.md`, `Codex/gpt-6-astra.md`, `Meta/muse-code/muse-spark-1.3-muse-code.md`, `Meta/muse-agent/workspace/system/system_prompt.md`, `xAI/grok-4.7.md`. Recent-additions table in README lists dated entries (see Dates).
- Date: repo 851 commits on `main` (as fetched); README recent table: Claude Haiku 5.5 + Haiku 5.5 Claude Code 2026-10-07; ChatGPT Dots + Muse Spark 1.3 Muse Code 2026-10-05/04; Muse agent VM files + Grok 4.7 2026-10-03; Fable 5.1 web/headless + GPT-6.1-Sol Codex + Sonnet 5.5 2026-09-29/30. Cited press: Washington Post interactive 2026-05-11, CEPS AI World 2026-07-10, Simon Willison 2026-08-20 (per README claims, not independently verified).
- Provenance: ALLEGED-LEAK / UNVERIFIED (community-reproduced). Evidence: About text "Documented system prompts from Anthropic - Claude Fable 5.1, Opus 5.5... OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash... xAI - Grok... Updated regularly."; topics include `system-prompts`, `prompt-engineering`; license `CC0-1.0`; 69.2k stars / 11.3k forks / 777 watchers (point-in-time). No vendor signature, no checksum, no official mirror statement observed.
- Accessibility: public GitHub repo (Code/Issues 21/Pull requests 35/Actions/Security/Insights tabs observed); no auth required for listing.
- Authenticity limits: HIGH — third-party claims of verbatim prompts; model names include unconfirmed/future-sounding versions (e.g., Fable 5.1, GPT-6-Astra, Gemini 3.8); contents may be reconstructed, outdated, partial, or injected; do not treat as vendor ground truth; do not use to bypass controls; verify against official docs only.

### P-02. anthropics/claude-cookbooks — skills/ (official examples)
- URL: https://github.com/anthropics/claude-cookbooks ; subpath https://github.com/anthropics/claude-cookbooks/tree/main/skills
- Claimed source: Anthropic (org `anthropics`), official cookbook.
- Types / structure / filenames: top-level cookbook (notebooks/recipes: classification, RAG, summarization, tool use, vision, sub-agents, evals, prompt caching). Subfolder `skills/` = "Claude Skills Cookbook": built-in skill reference table (IDs `xlsx`, `pptx`, `pdf`, `docx`), custom-skill structure, paths observed: `skills/notebooks/03_skills_custom_development.ipynb`, `skills/custom_skills`, `skills/README.md`.
- Date: repo created 2023-08-15 (per search excerpt).
- Provenance: OFFICIAL (example/reproduced pedagogy, not leak). Evidence: org `anthropics`, cookbook framing, built-in skill IDs matching Skills API docs.
- Accessibility: public.
- Authenticity limits: LOW for provenance (official), but examples are illustrative, version-sensitive; check model/skill IDs against current docs.

### P-03. anthropics/skills (official implementation + templates)
- URL: https://github.com/anthropics/skills ; spec https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md ; template https://github.com/anthropics/skills/blob/main/template/SKILL.md
- Claimed source: Anthropic (`anthropics`), "Public repository for Agent Skills" (note: implementation; standard at agentskills.io).
- Types / structure / filenames: `./skills` (19 example folders observed: academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx); `./spec`; `./template` (`template-skill`, frontmatter `name`+`description`). Example files observed (names only): `skills/claude-api/SKILL.md`, `skills/docx/SKILL.md`, `skills/template/SKILL.md`.
- Date: created 2025-09-22 (per search excerpt).
- Provenance: OFFICIAL. Evidence: org `anthropics`, docs cross-links (Skills API, Claude Code plugin `document-skills@anthropic-agent-skills`), license split (many Apache-2.0; docx/pdf/pptx/xlsx source-available/proprietary per README).
- Accessibility: public; install via Skills API `/v1/skills`, claude.ai settings, Claude Code plugin marketplace.
- Authenticity limits: LOW for provenance; HIGH version sensitivity (skill IDs, frontmatter triggers evolve); respect proprietary license on document skills.

### P-04. Agent Skills standard (agentskills/agentskills + spec site)
- URL: https://github.com/agentskills/agentskills ; https://agentskills.io/specification ; https://anthropics-skills.mintlify.app/spec/overview
- Claimed source: open standard, originally Anthropic, community-contributed.
- Types / structure / filenames: spec defines folder + `SKILL.md` (YAML `name`, `description`) + `scripts/` + `references/` + `assets/`; progressive disclosure (metadata → body → resources); engineering post `https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills` (2025-10-16, open-standard update Dec 18 2025).
- Date: engineering post 2025-10-16; standard opened Dec 2025 (per post update note).
- Provenance: OFFICIAL (standard). Evidence: `agentskills/agentskills` README + Mintlify overview + Anthropic docs `docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview`.
- Accessibility: public docs/repo.
- Authenticity limits: LOW; implementations vary by host (Claude Code vs API vs third-party); confirm host support matrix.

### P-05. travisvn/awesome-claude-skills (community registry — metadata)
- URL: https://github.com/travisvn/awesome-claude-skills
- Claimed source: community curator `travisvn`; "curated list of awesome Claude Skills... particularly Claude Code".
- Types / structure / filenames: awesome-list (links to Official Skills: `anthropics/skills`, Cookbooks skills notebooks). Exact file list not enumerated this session.
- Date: created 2025-10-16; ~15294 stars / 2017 forks (point-in-time).
- Provenance: REPRODUCED/ARCHIVED (third-party directory). Evidence: README excerpt + repo header.
- Accessibility: public.
- Authenticity limits: MEDIUM — curation quality varies; links rot; verify each skill's own repo/license; not a leak source.

### P-06. ComposioHQ/awesome-claude-skills (community registry — metadata)
- URL: https://github.com/ComposioHQ/awesome-claude-skills/
- Claimed source: community org `ComposioHQ`; claims 1000+ production-ready skills/plugins across Claude/Codex/Cursor/Gemini/Antigravity.
- Types / structure / filenames: large categorized directory (automation entries e.g., Bitbucket/CircleCI/Datadog/GitHub observed in excerpt). Exact tree not enumerated this session.
- Date: created 2025-10-17; 64110–74137 stars across snapshots / 7067–8493 forks; default `master`.
- Provenance: REPRODUCED/ARCHIVED (third-party). Evidence: README excerpt.
- Accessibility: public.
- Authenticity limits: MEDIUM-HIGH — commercial curator ("Connect" actions), possible duplication/staleness; verify per-skill provenance.

### P-07. BehiSecc/awesome-claude-skills (community registry — metadata)
- URL: https://github.com/BehiSecc/awesome-claude-skills
- Claimed source: community curator `BehiSecc`.
- Types / structure / filenames: categorized TOC (Document, Dev/Code, Data, Science, Writing, Learning, Media, Health, Collab, Security/Web-testing, Utility, Articles, Collections). Exact files not enumerated.
- Date: created 2025-10-17; ~10090 stars / 1495 forks.
- Provenance: REPRODUCED/ARCHIVED. Evidence: README TOC excerpt.
- Accessibility: public.
- Authenticity limits: MEDIUM — same as P-05/P-06.

### P-08. karanb192/awesome-claude-skills (community registry — metadata)
- URL: https://github.com/karanb192/awesome-claude-skills
- Claimed source: community curator `karanb192`; claims 50+ verified skills; MIT.
- Types / structure / filenames: directory + install FAQ (skills vs MCP vs project instructions; `claude plugin marketplace add anthropics/skills`). Exact files not enumerated.
- Date: created 2025-10-21; 541 stars / 339 forks.
- Provenance: REPRODUCED/ARCHIVED. Evidence: README excerpt.
- Accessibility: public.
- Authenticity limits: MEDIUM — "verified" is curator-claimed, not audited; check per-skill tests.

### P-09. Official prompt-engineering docs (official examples — metadata)
- URL catalog (not body-fetched this session, listed for follow-up): https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview ; https://platform.openai.com/docs/guides/prompt-engineering ; https://ai.google.dev/gemini-api/docs/prompting-strategies
- Claimed source: vendors (Anthropic, OpenAI, Google).
- Types / structure / filenames: web docs (guides, API references, cookbook snippets). No filenames to list (not a repo).
- Date: living docs (version by access date 2026-10-09).
- Provenance: OFFICIAL. Evidence: well-known vendor doc hosts (not fetched this session — mark pending verification).
- Accessibility: public web.
- Authenticity limits: LOW for provenance; content updates frequently; pin access date.

### P-10. Historical / eval datasets (metadata placeholders — verification pending)
- URL catalog (pending verification): HumanEval, MMLU, GSM8K, SWE-bench, AgentBench (exact URLs not fetched this session — DO NOT treat as verified).
- Claimed source: academic/industry benchmarks commonly reused as prompt/eval corpora.
- Types / structure / filenames: task JSON/JSONL, prompts + hidden tests, model-graded rubrics (exact schemas pending per-dataset fetch).
- Date: various (2019–2025 originals; living forks).
- Provenance: UNVERIFIED this session (official paper + community mirrors exist; specific mirror not yet inspected).
- Accessibility: varies (public repos/HF datasets; some gated).
- Authenticity limits: HIGH until pinned — contamination risk, version forks, license variance; record dataset version/hash before use.

### P-11. Agent-instruction / template dirs in inspected repos (official, metadata)
- URLs: https://github.com/facebook/astryx (paths `AGENTS.md`, `CLAUDE.md`, `packages/cli` docs/templates); https://github.com/vercel/eve (`agent/instructions.md`, `agent/tools/`, `agent/skills/`, `agent/channels/`); https://github.com/affaan-m/ECC (`AGENTS.md`, `CLAUDE.md`, `rules/`, `skills/`, `workflows/`); https://github.com/ruvnet/ruflo (`USERGUIDE.md`, `docs/STATUS.md`)
- Claimed source: respective repo owners (official in-repo instructions, not leaks).
- Types: agent instructions, skill dirs, channel/tool/schedule scaffolds, rule packs, workflow playbooks. Bodies NOT reproduced.
- Date: as-fetched 2026-10-09 (commit counts: Astryx 4537, ECC 3043; others per repo).
- Provenance: OFFICIAL (in-repo). Evidence: file trees observed via WebFetch excerpts this session.
- Accessibility: public repos.
- Authenticity limits: LOW for provenance; instructions are project-scoped, not universal prompts; version with repo commit.

### P-12. Unverified dumps / misc prompt libs (explicitly UNVERIFIED — do not use)
- Scope: any `system-prompts`, `awesome-prompts`, `prompt-library`, paste-site mirrors, or social-media screenshots NOT listed in P-01–P-11.
- Provenance: UNVERIFIED. Evidence: none captured this session.
- Accessibility: unknown.
- Authenticity limits: HIGHEST — treat as untrusted; record URL + claimant + date + hash if ever cataloged; never reproduce bodies; never use for bypass.

---

## Counts
- Total prompt-archive records: 12 (P-01–P-12)
- Fully inspected this session (tree/README excerpt via WebFetch/WebSearch): 8 (P-01, P-02, P-03, P-04, P-05, P-06, P-07, P-08)
- Official examples/standards/in-repo instructions: P-02, P-03, P-04, P-09, P-11
- Alleged-leak: P-01 only (asgeirtj/system_prompts_leaks) — falshood-prone, metadata-only
- Community registries (reproduced/archived): P-05, P-06, P-07, P-08
- Placeholders pending verification: P-09 (docs not fetched), P-10 (datasets), P-12 (unverified dumps bucket)
- Prompt bodies reproduced: 0 (compliant)

## Unresolved / follow-up list
1. asgeirtj subfolder file-level inventory (dates/hashes per `Anthropic/`, `OpenAI/`, `Meta/`, `xAI/`, etc.) — README table captured, per-file commit dates not yet pulled.
2. P-09: fetch each official prompt-engineering doc (URL → title → version → access date) without copying examples.
3. P-10: pin exact dataset URLs + versions + licenses + hashes.
4. P-05–P-08: enumerate top-level filenames + last-commit dates (registry freshness check).
5. Any additional alleged-leak repos beyond asgeirtj: catalog URL + claimant + provenance only; no bodies.
6. Re-verify `vercel/deepsec` non-existence before citing it as prompt/security source (currently 404).

## Method notes / limits
- No prompt text, system-prompt verbatim, or bypass-relevant content included by design.
- asgeirtj folder/filename lists come from README excerpts + root tree; per-file bodies/descriptions were NOT opened.
- Star/fork/commit counts are excerpts, not API guarantees.
- Press citations (WaPo, CEPS, Willison) are README claims, not independently verified.
- All unresolved items preserved verbatim for retry.
