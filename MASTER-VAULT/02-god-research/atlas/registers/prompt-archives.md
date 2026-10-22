# PROMPT ARCHIVES — Register (Atlas Part 18 + Deliverable E)

Workstream researcher #15. Verification date for all records: **2026-10-10**.

## Method

Live web research on primary sources only: repository pages, README files, directory listings, and official provider publications, fetched via text fetch (no live-browser sessions; nothing requiring sign-in, purchase, or form interaction was attempted). I inspected READMEs, root directory listings, file-naming conventions, license declarations, and provenance statements. I did **not** reproduce prompt bodies — records describe prompt types, counts, file names, and claimed provenance only.

Verification labels used (applied separately to an archive's **existence** and to its **authenticity claims**): Verified / Partially verified / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved — exactly as specified.

## Scope boundary

This register covers: (1) officially published system prompts; (2) public provider prompt examples and open-source prompt libraries; (3) public system-prompt archives, alleged-leak collections, unverified dumps, historical snapshots; (4) coding-agent instruction repositories, research-agent and tool-use prompt collections, prompt templates, system-message collections; (5) prompt evaluation datasets, prompt-testing tools, prompt registries and search tools.

**Dedup / cross-references (not duplicated here):** `asgeirtj/system_prompts_leaks` is the named research lead for this workstream and is recorded below (R5) — other workstreams should cross-reference this file rather than re-research it. `anthropics/claude-cookbooks` (contains prompt examples) is cross-referenced only, per instructions, and is not given a full record here. Boundary-adjacent items that are *user-facing prompt template libraries* rather than system-prompt archives (e.g. `f/awesome-chatgpt-prompts`, `danielmiessler/Fabric` pattern library) are noted in the coverage section, not fully recorded.

---

## 1. Official prompt publications

### R1 — Anthropic official system-prompt release notes

- **Resource name:** Anthropic — System prompts (Claude Platform Docs, release notes)
- **Canonical identity:** `platform.claude.com/docs/en/release-notes/system-prompts` (Anthropic, the model provider)
- **Category:** 1 (officially published system prompts)
- **Type:** Provider documentation page; dated system-prompt disclosures per model
- **Official URL:** https://platform.claude.com/docs/en/release-notes/system-prompts (older path `docs.anthropic.com/en/release-notes/system-prompts` 301-redirects here)
- **Description:** Anthropic's own release-notes page publishing the system prompts used by claude.ai web/mobile apps. Page text (fetched 2026-10-10, live) states the prompt provides up-to-date information such as the current date, encourages behaviors such as code snippets in Markdown, is periodically updated, and **does not apply to the Claude API**. Starting with the Claude 4.6 generation, each model ID is a single fixed snapshot with one entry.
- **Contents inspected:** Page header/intro text only (text fetch returned the page lead; per-entry tables require JS rendering and were not fully enumerated). Independent archiving projects (see R5, R16) confirm entries carry dates such as 2026-06-09 (Claude Fable 5), 2026-05-28 (Claude Opus 4.8), 2026-04-16 (Claude Opus 4.7), 2026-02-17 (Claude Sonnet 4.6).
- **What prompt types it contains:** The behavioral core (`claude_behavior`-style) of consumer Claude system prompts: product information, refusal handling, tone/formatting, user wellbeing, reminders, evenhandedness, knowledge cutoff. Does **not** include tool/function definitions, runtime-injected reminders, user preferences, or per-session context.
- **Claimed provenance + evidence:** Published by Anthropic itself on its own docs platform — official by construction. Corroborated by independent captures (R16 documents the Fable 5 entry verbatim with access date 2026-06-14; R5 mirrors dated versions).
- **Authenticity status:** Officially published (partial disclosure — behavior core only, not the full running context).
- **Where it can be used:** Reference for Claude consumer-app behavior; diffing behavior-core changes across model generations; citation in research.
- **Availability:** Public, no sign-in observed. **Maintenance:** Actively updated by Anthropic (page notes periodic updates; third-party trackers observed Fable 5.1-era updates).
- **Limitations:** Stale relative to deployed prompts (third-party analysis 2026-07-07 found the June 9 version still listed despite a July redeployment); covers claude.ai only, not API or Claude Code.
- **Related resources:** R5 (`Anthropic/Official/` subfolder archives these), R16 (verbatim official-disclosure captures).
- **Sources:** https://platform.claude.com/docs/en/release-notes/system-prompts (verified live 2026-10-10); https://github.com/eonedgeproject-code/the-brief/blob/HEAD/entries/anthropic/claude-fable-5/2026-06-09-official-disclosure.md; https://github.com/agricidaniel/fablesecondbrain/blob/HEAD/wiki/sources/Public%20System%20Prompt%20Copies.md
- **Verification date:** 2026-10-10. **Confidence:** High. **Existence:** Verified. **Authenticity:** Verified (officially published).

### R2 — xAI grok-prompts (official)

- **Resource name:** grok-prompts (xAI official)
- **Canonical identity:** `xai-org/grok-prompts` (xAI org account)
- **Category:** 1 (officially published system prompts)
- **Type:** GitHub repository of production system prompts
- **Official URL:** https://github.com/xai-org/grok-prompts
- **Description:** xAI's self-described official repository: "We are regularly updating this repository with the system prompts that we use for the Grok chat assistant and various product features across X and grok.com."
- **Contents inspected:** Full root listing + README (fetched 2026-10-10). 10 prompt files: `grok4_system_turn_prompt_v8.j2` (Grok 4 chat assistant, grok.com and X), `grok3_official0330_p1.j2` (Grok 3 chat assistant), `grok_analyze_button.j2` (Grok Explain feature on X), `ask_grok_system_prompt.j2` (@grok bot on X), `grok_4_code_rc1_safety_prompt.txt`, `grok_4_mini_system_prompt.txt`, `grok_4_safety_prompt.txt` (API-injected safety prefixes for grok-code-fast-1, grok-4-fast, grok-4-0709), `grok4p1_non_thinking_no_tool_system_turn_prompt.j2`, `grok4p1_non_thinking_system_turn_prompt.j2`, `grok4p1_thinking_system_turn_prompt_v2` (Grok 4.1 variants). README documents each file's purpose.
- **What prompt types it contains:** Actual chat-assistant system prompts (Jinja2 `.j2` templates with runtime directives) plus API-injected safety prompt prefixes. These are real served prompts, not policy summaries.
- **Claimed provenance + evidence:** Vendor-published on the vendor's own org account; README describes update cadence. Independent capture project R16 pinned a file to repo commit `a7c186f5ccac95875c0041aed60398f6ecb6d6c7` dated 2025-11-17. Note: repo page shows current HEAD commit as that same hash — repository appears not updated since Nov 2025.
- **Authenticity status:** Officially published.
- **Where it can be used:** Reference for Grok assistant behavior; template-structure study (Jinja2 system-turn construction).
- **Availability:** Public. **Maintenance:** Stated as regularly updated, but HEAD commit dates to 2025-11-17 (stale ~11 months as of 2026-10-10). License: AGPL-3.0 (copyleft — reuse implications).
- **Limitations:** Covers only listed products/features; not independently auditable against live grok.com behavior.
- **Related resources:** R5 (xAI/ folder holds extracted Grok prompts incl. versions not in this repo), R16 (official-disclosure capture).
- **Sources:** https://github.com/xai-org/grok-prompts (verified 2026-10-10); https://github.com/eonedgeproject-code/the-brief/blob/HEAD/entries/xai/grok-4-1/2025-11-17-official-disclosure.md
- **Verification date:** 2026-10-10. **Confidence:** High. **Existence:** Verified. **Authenticity:** Verified (officially published).

### R3 — OpenAI Model Spec

- **Resource name:** OpenAI Model Spec
- **Canonical identity:** OpenAI (provider publication, first draft May 2024)
- **Category:** 1 (officially published; behavior specification rather than literal system prompt)
- **Type:** Public behavior-specification document + announcement post
- **Official URL:** https://openai.com/index/introducing-the-model-spec/ (announcement); the spec document itself is hosted on OpenAI's site
- **Description:** OpenAI's published document specifying its approach to shaping desired model behavior: objectives (assist developer/user, benefit humanity, reflect well on OpenAI), rules (chain of command, legal compliance, no information hazards, IP respect, privacy, NSFW), and default behaviors (assume best intentions, ask clarifying questions, thorough but efficient, etc.). Positioned as guidance for RLHF researchers/trainers and as a public-conversation artifact.
- **Contents inspected:** Announcement page text via secondary sources (not the full spec PDF in this pass — page text fetch returned search-result excerpts).
- **What prompt types it contains:** High-level behavior policy, not a deployable system prompt. Distinct from ChatGPT's actual served system prompt (which remains unpublished by OpenAI).
- **Claimed provenance + evidence:** Published by OpenAI on openai.com; widely reported at publication (May 2024).
- **Authenticity status:** Officially published (policy-level, not a literal system prompt — preserve this distinction).
- **Where it can be used:** Reference for OpenAI's stated behavior priorities; comparison baseline against extracted ChatGPT prompts in archives.
- **Availability:** Public. **Maintenance:** Described as an evolving document; later revisions not enumerated here.
- **Limitations:** Does not disclose actual system-prompt text; cannot be used to verify extracted ChatGPT prompts.
- **Related resources:** R5/R6 (extracted ChatGPT system prompts — the unpublished counterpart).
- **Sources:** https://openai.com/index/introducing-the-model-spec/ (URL verified from search results 2026-10-10; full page not text-fetched in this pass)
- **Verification date:** 2026-10-10. **Confidence:** High (publication event well-documented). **Existence:** Verified. **Authenticity:** Verified (officially published). **Note:** full spec text not re-verified in this pass — Partially verified at document level.

### R4 — Meta Llama prompt formats / system-prompt guidance

- **Resource name:** Meta Llama prompt formats (meta-llama/llama-models) and Llama system-prompt update notes
- **Canonical identity:** `meta-llama/llama-models`, `meta-llama/llama` (Meta org accounts)
- **Category:** 1 (officially published prompt-format/system-prompt documentation)
- **Type:** Official model-card / prompt-format docs
- **Official URL:** https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/text_prompt_format.md; https://github.com/meta-llama/llama/blob/HEAD/UPDATES.md
- **Description:** Meta publishes chat-template formats including a `system` role slot with example system text (e.g. "You are a helpful assistant") — a format specification, not a fixed product system prompt. Separately, `meta-llama/llama` UPDATES.md (2023-08-07) documents Meta's decision to **remove the default system prompt** from chat-model examples after community feedback on false refusals, keeping only an example for experimentation.
- **Contents inspected:** Search-result excerpts of both files (not full text-fetched in this pass).
- **What prompt types it contains:** Chat-template skeletons with an (empty or example) system slot; historical notes on Meta's default system prompt.
- **Claimed provenance + evidence:** Vendor org repos; standard references in the ecosystem.
- **Authenticity status:** Officially published (format docs); the actual content of any deployed Meta AI system prompt is **not** published here.
- **Where it can be used:** Reference for Llama chat-template structure.
- **Availability:** Public. **Maintenance:** Versioned by model release.
- **Limitations:** Not a product system prompt; Meta AI's served prompt remains undisclosed by Meta (community archives hold extracted copies — see R5).
- **Related resources:** R5 (Meta/ folder: extracted Muse Spark / Meta AI prompts).
- **Sources:** URLs above (verified from search results 2026-10-10; full pages not text-fetched)
- **Verification date:** 2026-10-10. **Confidence:** Medium. **Existence:** Partially verified. **Authenticity:** Partially verified (official docs; limited to formats).

---

## 2. Public unofficial archives (community-extracted prompt collections)

### R5 — asgeirtj/system_prompts_leaks [NAMED RESEARCH LEAD]

- **Resource name:** system_prompts_leaks
- **Canonical identity:** `asgeirtj/system_prompts_leaks` (maintainer: asgeirtj)
- **Category:** 3 (public system-prompt archive; contents described as extracted, not hacked)
- **Type:** Multi-vendor system-prompt archive, Markdown files organized by provider
- **Official URL:** https://github.com/asgeirtj/system_prompts_leaks
- **Description:** The largest actively maintained community archive of extracted production system prompts, spanning Anthropic, OpenAI, Google, xAI (listed as "SpaceXAI" in the current README), Meta, Perplexity, Cursor, Mistral, Moonshot, DeepSeek, Z.ai, Microsoft Copilot, Notion, Qwen, plus an "Other products" section (Amp, Devin CLI, Warp, Zed, Docker Gordon, ElevenLabs, Reddit Answers, Brave Search, Character AI, Fellou, Gizmo, Hermes, Indus, Kagi, MiniMax, Pi, Proton Lumo, Raycast).
- **Contents inspected:** Full README (fetched 2026-10-10; 493+ lines) including the "Most recent additions/changes" table (latest entries: Claude Haiku 5.5 and Claude Code Haiku 5.5 — 2026-10-07; ChatGPT Dots — 2026-10-05; Meta Muse Code / Muse Spark 1.3 — 2026-10-04; Grok 4.7 — 2026-10-03; GPT-6.1-Sol Codex — 2026-09-29; Claude Sonnet 5.5 — 2026-09-29) and the per-provider catalog tables. Anthropic section verified to contain: claude.ai prompts per model (`claude-fable-5.1.md`, `claude-opus-5.md`, `claude-sonnet-5.5.md`, `claude-haiku-5.5.md`, older `claude-opus-4.8.md`, `claude-sonnet-5.md`, `claude-opus-4.7/4.6.md`, `claude-sonnet-4.6.md` incl. no-tools variants), Claude Code prompts per model + headless/desktop/web variants + subagents + advisor tool + skills/slash commands, integrations (Projects, Design, Cowork, Science, Microsoft 365, Chrome, iOS). The Anthropic folder README (verified via earlier inspection) documents the file taxonomy: bare `claude-<model>.md` = claude.ai app prompts (not API, not Code); `claude-code/` subfolder; `Official/` = Anthropic-published release-notes versions (shorter than served prompts); `raw/` = raw captures; `old/` = superseded versions. A GLM entry documents that GLM "serves no system prompt — verified & documented."
- **What prompt types it contains:** Chat-assistant system prompts; coding-agent system prompts (Claude Code, Codex variants, Gemini CLI, Copilot); subagent and slash-command prompts; injected reminder fragments; tool/skill bundles; API-injected prompt fragments; archived official publications (dated copies of Anthropic's own release-notes prompts, e.g. `Anthropic/Official/2026-06-09-claude-fable-5.md`).
- **Claimed provenance + evidence:** Described as extracted from production products ("prompts are extracted, not hacked" per prior finding 2026-08, consistent with current README framing). The `Anthropic/Official/` subfolder README (verified via fork mirror `diegosouzapw/system_prompts_leaks`) explicitly archives `https://platform.claude.com/docs/en/release-notes/system-prompts` with per-date files and an `all.md` rollup — that subfolder is provenance-clean. No per-file extraction methodology is stated for the rest.
- **Authenticity status:** Mixed — officially published (the `Official/` subfolder), otherwise independently reproduced at best / alleged extraction; individual files carry no vendor verification. A repo file labeled as a leaked system prompt does not establish authenticity.
- **Where it can be used:** Research into production prompt structure; cross-version diffs; agent-behavior analysis. Cited downstream by a Washington Post interactive piece (May 2026) and a CEPS AI World dashboard (July 2026) per community reporting — not independently verified.
- **Availability:** Public, CC0-1.0 license per community reports (license field not confirmed on the repo page in this pass — see Limitations). **Maintenance:** Highly active; README "recently updated" table shows additions within days of verification date.
- **Limitations:** (a) No stated per-file extraction method or capture dates on most files; (b) authenticity of any single file cannot be established from the repo alone; (c) scale: third-party trackers reported ~51,200 stars (2026-07-06) and ~66,743 stars (2026-09-15) — rapid growth, exact current count not independently counted; (d) proliferation of forks/mirrors reusing the same name (`sanjayshuklazoho`, `whoamimi`, `markoko007`, `ambalashov`, `aaroncarter112`, `loky160`, `yanyecao`, `diegosouzapw`, `stophobia`, `johnwilliambitlasoft` and others) creates confusion about which copy is canonical — the canonical copy is `asgeirtj/`; (e) license field (CC0-1.0) reported by secondary sources, not confirmed on the fetched repo page.
- **Related resources:** R1 (official prompts archived inside), R6 (upstream extractor for many entries), R7 (parallel archive), R16 (methodologically tagged subset).
- **Sources:** https://github.com/asgeirtj/system_prompts_leaks (README fetched 2026-10-10); https://github.com/asgeirtj/system_prompts_leaks/tree/main/Anthropic (folder taxonomy, crawled 2026-07); https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/README.md; https://github.com/diegosouzapw/system_prompts_leaks/blob/HEAD/Anthropic/Official/README.md (Official subfolder README, crawled 2026-07-22); https://github.com/hongsw/clawfit/blob/HEAD/docs/research-watch/2026-07-06-asgeirtj-system-prompts-leaks-multi-model-transparency.md
- **Verification date:** 2026-10-10. **Confidence:** High (existence, structure, activity). **Existence:** Verified. **Authenticity:** Partially verified — officially published for the `Official/` subfolder; otherwise alleged extraction / independently reproduced; authenticity of individual files: Unverified.

### R6 — elder-plinius/CL4R1T4S

- **Resource name:** CL4R1T4S ("clarities")
- **Canonical identity:** `elder-plinius/CL4R1T4S` (maintainer: elder_plinius / "Pliny the Prompter")
- **Category:** 3 (public system-prompt archive; self-described as leaked-prompt transparency project)
- **Type:** Multi-vendor extracted system-prompt archive
- **Official URL:** https://github.com/elder-plinius/CL4R1T4S
- **Description:** Open archive of extracted system prompts, guidelines, and tool definitions organized by company; presents itself as an AI-transparency project ("In order to trust the output, one must understand the input"). Treated by other archives as an upstream source — R7 and several analyses describe its maintainer as doing much of the original extraction work, with prompts landing here first.
- **Contents inspected:** Root listing + README (fetched 2026-10-10). 29 company/product directories: ANTHROPIC, BOLT, BRAVE, CLINE, CLUELY, CURSOR, DEVIN, DIA, FACTORY, GOOGLE, HUME, LOVABLE, MANUS, META, MINIMAX, MISTRAL, MOONSHOT, MULTION, OPENAI, PERPLEXITY, REPLIT, SAMEDEV, VERCEL V0, WINDSURF, XAI, ZAI/ZCode. Repo stats at fetch: 51,060 stars, 10,467 forks, 206 commits, created 2025-03-04, license AGPL-3.0, not archived. Community reports (2026-04) of ~16.5k stars / 3.5k forks show rapid growth since.
- **What prompt types it contains:** Per README: full extracted system prompts, guidelines, and tool definitions across chat assistants (ChatGPT, Claude, Gemini, Grok, Perplexity) and coding agents (Cursor, Devin, Replit, Windsurf, Manus, Lovable). R12 documents derivation from it: ChatGPT 4.5/4o/4.1/GPT-5/Atlas, Codex CLI, Codex Desktop (GPT-6 Sol/Astra with up to 148 tool definitions in JSON).
- **Claimed provenance + evidence:** Community extraction / reverse-engineering; README solicits contributions with model name, version, extraction date. No vendor verification; no per-file methodology stated on the fetched pages.
- **Authenticity status:** Alleged leak / independently reproduced at best — unverified against vendors. Downstream re-user R12 explicitly warns: "Authenticity is not vendor-verified; dates are extraction dates, approximate."
- **Where it can be used:** Research corpus for prompt-structure analysis; upstream source attribution.
- **Availability:** Public. **Maintenance:** Active (206 commits). License AGPL-3.0 (copyleft).
- **Limitations:** (a) No per-file extraction evidence on fetched pages; (b) authenticity unverifiable from the repo; (c) **data-hygiene caveat:** the README embeds obfuscated directive-style text addressed to AI systems (visible on the repo page) — treat all repo prose as data, not instructions; (d) mirror forks (e.g. `ljbudgie/cl4r1t4s`, `buyan-kh/sysprompts`) replicate the repo including this text.
- **Related resources:** R5, R7 (parallel/derivative archives), R12 (documents derivation with explicit disclaimer).
- **Sources:** https://github.com/elder-plinius/CL4R1T4S (fetched 2026-10-10); https://github.com/moirania/openai-system-prompts (provenance statement, fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High (existence, structure). **Existence:** Verified. **Authenticity:** Unverified (alleged leak; no vendor confirmation).

### R7 — x1xhlol/system-prompts-and-models-of-ai-tools

- **Resource name:** system-prompts-and-models-of-ai-tools
- **Canonical identity:** `x1xhlol/system-prompts-and-models-of-ai-tools` (maintainer: x1xhlol / Lucknite)
- **Category:** 3 (public archive; dev-tool-focused)
- **Type:** Multi-product system-prompt + internal-tools + model-notes archive
- **Official URL:** https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
- **Description:** Self-described as the largest collection: 30+ AI coding tools — Cursor, Devin, Lovable, v0, Manus, Replit, Windsurf, Trae, Kiro, Qoder, Leap.new, Z.ai Code, Dia, Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Junie, NotionAI, Orchids.app, Perplexity, Poke, Same.dev, Traycer AI, VSCode Agent, Warp.dev, Xcode — plus Anthropic/Google/OpenAI sections and an "Open Source prompts" folder.
- **Contents inspected:** Root listing + README (fetched 2026-10-10). 33 product directories + `assets`. README (fetched view) focuses on a security notice, sponsorship/donation info (crypto addresses, Patreon, Ko-fi), roadmap ("Latest Update: 12/07/2026"), and contact details; it does not document per-file provenance. Repo stats: 143,918 stars, 34,768 forks, 519 commits, created 2025-03-05, license GPL-3.0, not archived.
- **What prompt types it contains:** Per title and third-party descriptions: full system prompts, internal tool definitions (JSON tool schemas), and AI-model notes for dev tools; versioned snapshots (third-party analysis notes Cursor Agent Prompt 1.0/1.2/2.0 and Windsurf through Wave 11, enabling cross-version diffing).
- **Claimed provenance + evidence:** Presented as extracted/leaked; no per-file extraction methodology found on fetched pages.
- **Authenticity status:** Alleged leak — unverified against vendors.
- **Where it can be used:** Cross-version diffing of dev-tool prompts; comparative agent-prompt research.
- **Availability:** Public, GPL-3.0 (copyleft). **Maintenance:** Active ("Latest Update: 12/07/2026" on README).
- **Limitations:** (a) No per-file provenance or capture dates surfaced in fetched README; (b) README is dominated by sponsorship/security-notice content rather than documentation; (c) authenticity unverifiable from repo alone.
- **Related resources:** R5, R6 (overlapping scope), R14 (independent Claude Code extraction for cross-checking).
- **Sources:** https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools (fetched 2026-10-10); https://github.com/howdeploy/deploychan_mcp/blob/HEAD/content/knowledge/system-prompts-and-cards.md (third-party characterization, crawled 2026-10-02); https://github.com/4pixeltechbr/promptograph/blob/HEAD/ATTRIBUTIONS.md
- **Verification date:** 2026-10-10. **Confidence:** High (existence, scale, license). **Existence:** Verified. **Authenticity:** Unverified (alleged leak).

### R8 — jujumilk3/leaked-system-prompts

- **Resource name:** leaked-system-prompts
- **Canonical identity:** `jujumilk3/leaked-system-prompts`
- **Category:** 3 (public archive; historical — longest-lived of the set)
- **Type:** Flat-file chronological archive of leaked system prompts
- **Official URL:** https://github.com/jujumilk3/leaked-system-prompts
- **Description:** Collection of leaked system prompts from widely used LLM-based services, running continuously since 2023-05-16 — the earliest-founded major archive found, giving it unique historical depth (2022-12 through 2026-09 captures).
- **Contents inspected:** Full root file listing (fetched 2026-10-10; ~170 files). Flat naming convention `<service>-<product>_<extraction-date>.md`, e.g. `openai-chatgpt_20221201.md`, `microsoft-bing-chat_20230209.md`, `discord-clyde_20230420.md` (×5 dated variants), `anthropic-claude_2.0_20240306.md`, `perplexity.ai_20221208.md` through `perplexity.ai_claude_20251001.md`, `xAI-grok_20241003.md`, `openai-codex-cli_20250527.md` / `_20250915` / `_20260902`, `google-gemini-cli_20250626.md`, `anthropic-claude-code_20250304.md` / `_20260902`, `cursor-ide-2.0_20251029.md`, `aider_20260918.md`, `block-goose_20260918.md`. README contribution policy: PRs must match format and "include sources that I can verify or reproducible prompts"; links may be posted as issues for maintainer verification. Explicit DMCA-avoidance note: cited in many papers, so contributors must not include sensitive commercial source code.
- **What prompt types it contains:** Chat-assistant and coding-agent system prompts with extraction dates embedded in filenames — the filename dates make it the best archive for longitudinal study.
- **Claimed provenance + evidence:** Maintainer-verified sources or reproducible prompts required per contribution policy (policy claim only; per-file evidence not inspected).
- **Authenticity status:** Alleged leak / historical archive — individual files unverified against vendors; maintainer verification policy is a process claim, not per-file evidence.
- **Where it can be used:** Historical/longitudinal prompt research (2022–2026); dated corpus for diffing prompt evolution.
- **Availability:** Public, no license stated (defaults to all-rights-reserved — reuse caution). **Maintenance:** Active (281 commits; newest files dated 2026-09). Stats: 14,957 stars, 2,108 forks.
- **Limitations:** (a) No license; (b) verification policy is procedural, per-file provenance not shown on listing; (c) authenticity of individual files unverifiable from repo.
- **Related resources:** R5, R6, R7 (parallel archives); R17 (ingests this repo as a source).
- **Sources:** https://github.com/jujumilk3/leaked-system-prompts (fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High (existence, history, policy). **Existence:** Verified. **Authenticity:** Unverified (alleged leak; historical value independent of authenticity).

---

## 3. Alleged-leak / unverified collections

### R9 — LouisShark/chatgpt_system_prompt ("PromptCraft")

- **Resource name:** PromptCraft: The Ultimate GPT System Prompt Collection
- **Canonical identity:** `LouisShark/chatgpt_system_prompt`
- **Category:** 3 (collection of GPT system prompts + prompt-injection/leaking knowledge)
- **Type:** Crowd-sourced system-prompt collection with search tooling
- **Official URL:** https://github.com/LouisShark/chatgpt_system_prompt
- **Description:** "A collection of GPT system prompts and various prompt injection/leaking knowledge" — covers ChatGPT and other AI products plus custom GPT instructions; framed as educational for prompt writing and injection-security awareness. Third-party attribution tables describe it as "Collection of GPT system prompts and prompt injection knowledge (1.7k+ prompts)."
- **Contents inspected:** Root listing + README (fetched 2026-10-10). `prompts/` directory; `TOC.md` (searchable index); `GETTING_STARTED.md`, `SECURITY.md`, `CONTRIBUTING.md`, `RESOURCES.md`; `.scripts/` incl. an `idxtool` for local search; CI badge "Generate TOC on PR Merge" and a tokens badge. Stats: 10,803 stars, 1,459 forks, 1,863 commits, created 2023-11-01, license MIT.
- **What prompt types it contains:** GPT system prompts, custom-GPT instructions, prompt-injection/leak technique knowledge.
- **Claimed provenance + evidence:** Community-contributed; disclaimer states sharing is "purely for reference and knowledge sharing." No per-file extraction evidence inspected.
- **Authenticity status:** Alleged leak / unverified — community contributions without vendor confirmation.
- **Where it can be used:** Prompt-injection security education; custom-GPT instruction study.
- **Availability:** Public, MIT. **Maintenance:** Active (1,863 commits; CI-maintained TOC).
- **Limitations:** No per-file provenance surfaced; authenticity unverifiable from repo.
- **Related resources:** R5–R8 (parallel archives); R17 (lists related libraries).
- **Sources:** https://github.com/LouisShark/chatgpt_system_prompt (fetched 2026-10-10); https://github.com/4pixeltechbr/promptograph/blob/HEAD/ATTRIBUTIONS.md
- **Verification date:** 2026-10-10. **Confidence:** High (existence, tooling). **Existence:** Verified. **Authenticity:** Unverified.

### R10 — moirania/openai-system-prompts

- **Resource name:** openai-system-prompts (Agent Skill packaging of extracted OpenAI prompts)
- **Canonical identity:** `moirania/openai-system-prompts`
- **Category:** 4 (derived prompt collection packaged as an agent skill)
- **Type:** Secondary extraction archive + structural analysis
- **Official URL:** https://github.com/moirania/openai-system-prompts
- **Description:** Packages "18 extracted real OpenAI production system prompts & tool schemas" (ChatGPT 4.5/4o/4.1/GPT-5/Atlas, Codex CLI, Codex Desktop GPT-6 Sol/Astra with up to 148 tools) as an installable Agent Skill, with a prompt-anatomy analysis and an evolution timeline. A companion skill covers Claude prompts.
- **Contents inspected:** Full README + root listing (fetched 2026-10-10). Structure: `SKILL.md` + `references/prompt-anatomy.md`, `references/evolution-timeline.md`, `references/prompts/` (18 original extracted files, unmodified; Codex Desktop tool JSON ~2.7MB / 27,868 lines). Stats: 1 star, 1 commit, created 2026-09-27 — brand new, minimal adoption.
- **What prompt types it contains:** ChatGPT consumer-line prompts, Codex CLI minimal contracts, Codex Desktop maximal agentic prompts + namespaced tool JSONs.
- **Claimed provenance + evidence:** README "Provenance & disclaimer" section states: all files sourced from `elder-plinius/CL4R1T4S` (sourced 2026-09-28); **"Authenticity is not vendor-verified; dates are extraction dates, approximate"**; "Sol"/"Astra"/"Atlas" are extractor codenames, not official OpenAI product names; "don't present quotes as verbatim current production text." This is the clearest provenance disclaimer found in any archive in this pass.
- **Authenticity status:** Unverified (explicitly disclaimed by the maintainer; secondary of R6).
- **Where it can be used:** Study of prompt anatomy/evolution narratives; example of responsible provenance labeling.
- **Availability:** Public. **Maintenance:** Single commit; effectively a snapshot.
- **Limitations:** Secondary source; no independent extraction; tiny adoption.
- **Related resources:** R6 (upstream source), R14/R7 (alternative Codex prompt sources).
- **Sources:** https://github.com/moirania/openai-system-prompts (fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High. **Existence:** Verified. **Authenticity:** Unverified (maintainer-disclaimed).

### R11 — thekishandev/ai-system-prompt

- **Resource name:** AI System Prompts & Models Collection
- **Canonical identity:** `thekishandev/ai-system-prompt`
- **Category:** 4 (coding-agent instruction repository)
- **Type:** Small dev-tool prompt collection
- **Official URL:** https://github.com/thekishandev/ai-system-prompt
- **Description:** Claims "FULL v0, Cursor, Manus, Same.dev & Lovable System Prompts & AI Models"; README markets it as "official system prompts" from "leading AI development platforms."
- **Contents inspected:** Root listing + README (fetched 2026-10-10). Directories: `Cursor Prompts`, `Lovable`, `Manus Agent Tools & Prompt`, `Same.dev`, `Tools`, `v0 Prompts and Tools`. README is largely generic marketing copy (integrations, FAQs) with some structural inaccuracies (e.g. clone URL placeholder `yourusername/ai-system-prompts`, some Cursor files marked "coming soon"). Stats: 41 stars, 10 forks, **1 commit**, created 2025-04-04, license MIT. The directory naming mirrors `x1xhlol/system-prompts-and-models-of-ai-tools` ("Manus Agent Tools & Prompt", "v0 Prompts and Tools").
- **What prompt types it contains:** Purported v0, Cursor, Manus, Same.dev, Lovable system prompts and tool definitions.
- **Claimed provenance + evidence:** README claims "official system prompts" — no evidence offered; single-commit repo with placeholder text undermines the claim.
- **Authenticity status:** Unverified. The word "official" in its README is a marketing claim, not provenance — do not treat as officially published.
- **Where it can be used:** Not recommended as a primary source; at most a pointer to better-documented archives.
- **Availability:** Public, MIT. **Maintenance:** Single commit (2025-04-04); stale.
- **Limitations:** Unsubstantiated "official" claims; stale; appears derivative of R7's folder structure.
- **Related resources:** R7 (likely upstream of its folder structure).
- **Sources:** https://github.com/thekishandev/ai-system-prompt (fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** Medium-High (existence verified; claims unverified). **Existence:** Verified. **Authenticity:** Unverified.

### R12 — labac-dev/cursor-system-prompts

- **Resource name:** Cursor IDE System Prompts
- **Canonical identity:** `labac-dev/cursor-system-prompts`
- **Category:** 4 (coding-agent instruction repository)
- **Type:** Two-file prompt archive with comparative notes
- **Official URL:** https://github.com/labac-dev/cursor-system-prompts
- **Description:** "This repository contains the system prompts used by Cursor IDE for its AI coding assistants: Claude 3.7 Sonnet and Gemini 2.5 Pro."
- **Contents inspected:** README text (fetched 2026-10-10). Two files: `Claude_3.7_Sonnet.txt`, `Gemini_2.5_Pro.txt`. README includes a feature-comparison table (response style, tool usage, code editing, proactiveness) and a disclaimer: prompts "were obtained and are being shared for educational purposes."
- **What prompt types it contains:** Cursor IDE per-model system prompts (instruction sets for codebase interaction, formatting, tool use).
- **Claimed provenance + evidence:** Stated as the prompts "used by Cursor IDE" — no extraction method given.
- **Authenticity status:** Alleged extraction — unverified against Cursor.
- **Where it can be used:** Comparison of per-model prompt tuning inside one product.
- **Availability:** Public (license not captured in fetched text). **Maintenance:** Not assessed (repo stats not returned in fetch — Unresolved).
- **Limitations:** Tiny scope; no provenance detail; repo metadata (stars, license, activity) not captured — Unresolved.
- **Related resources:** R7, R14-adjacent (Cursor prompts appear in larger archives with version history).
- **Sources:** https://github.com/labac-dev/cursor-system-prompts (fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** Medium. **Existence:** Verified. **Authenticity:** Unverified.

---

## 4. Coding-agent instruction repositories, prompt templates, registries & search tools

### R13 — Piebald-AI/claude-code-system-prompts

- **Resource name:** Claude Code System Prompts (Piebald-AI)
- **Canonical identity:** `Piebald-AI/claude-code-system-prompts` (from the team behind Piebald)
- **Category:** 4 (coding-agent instruction repository; single-product deep archive)
- **Type:** Script-extracted, version-tracked prompt corpus
- **Official URL:** https://github.com/Piebald-AI/claude-code-system-prompts
- **Description:** "All parts of Claude Code's system prompt, 27 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline…)." The strongest provenance methodology found in this pass: prompts are extracted by script **directly from the published npm package of Claude Code**, so (per README) "they're guaranteed to be exactly what Claude Code uses." Updated within minutes of each Claude Code release; a GitHub Release is cut per Claude Code version (260 releases, 310 tags); CHANGELOG.md tracks prompt changes across 311 versions since v2.0.14.
- **Contents inspected:** Root listing + README (fetched 2026-10-10; README is long — 2,773 lines rendered, inspected through the agent-prompt sections). As of Claude Code v2.1.295 (2026-10-08): 515 prompt strings (up from 350 on 2026-06-12). Catalogued: sub-agent prompts (Explore 862 tokens, Plan mode 1,066 tokens), creation assistants (CLAUDE.md creation, statusline setup), ~20 slash-command prompts (/batch, /code-review multi-phase, /rename, /schedule, /security-review, /simplify, artifact flows), utilities (agent hooks, background-agent state classifier, conversation summarization variants, session-title generator), system reminders, builtin tool descriptions, skills. Token counts published per string.
- **What prompt types it contains:** Coding-agent system prompt *components* — the main system prompt plus its conditionally-loaded fragments, sub-agent prompts, slash-command prompts, utility prompts, tool descriptions, system reminders.
- **Claimed provenance + evidence:** Extraction-from-npm methodology stated in README and reproducible by anyone (the npm package is public). This is the closest any community archive gets to independently reproduced authenticity.
- **Authenticity status:** Independently reproduced (strong) — extraction is deterministic from a public artifact; not vendor-*endorsed*, but vendor-*published* source material.
- **Where it can be used:** Version-to-version diffing of Claude Code's prompt engineering; study of conditional prompt assembly; sub-agent/utility prompt design.
- **Availability:** Public, MIT. **Maintenance:** Very active (660 commits; same-day updates with releases). Stats: 12,860 stars, 2,038 forks, created 2025-11-18.
- **Limitations:** Single-product scope (Claude Code only); interpolated variables noted (±20 tokens); assembly logic (which fragments load when) documented only partially.
- **Related resources:** R5 (Anthropic/claude-code/ folder — overlapping content, weaker provenance), R7 (Anthropic section).
- **Sources:** https://github.com/Piebald-AI/claude-code-system-prompts (fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High. **Existence:** Verified. **Authenticity:** Partially verified — independently reproduced via public npm artifact (methodology sound; not vendor-confirmed file-by-file).

### R14 — dontriskit/awesome-ai-system-prompts

- **Resource name:** awesome-ai-system-prompts
- **Canonical identity:** `dontriskit/awesome-ai-system-prompts`
- **Category:** 4 (curated prompt collection + analytical guide)
- **Type:** Curated multi-tool collection with a patterns-and-practices guide
- **Official URL:** https://github.com/dontriskit/awesome-ai-system-prompts
- **Description:** "Curated collection of system prompts for top AI tools. Perfect for AI agent builders and prompt engineers." The README has been rewritten as a long-form analytical guide, "Crafting Effective Prompts for Agentic AI Systems: Patterns and Practices," which extracts 8 design principles (role definition, structured instructions, tool integration, step-by-step reasoning, environment awareness, domain expertise, safety/refusal protocols, tone) with case studies on v0, same.new, Manus, ChatGPT (GPT-4.5/4o), Cline, Bolt, Augment, Claude Code, Clawdbot — quoting short prompt excerpts with file-level sources.
- **Contents inspected:** Root listing + README (fetched 2026-10-10; 1,350 lines rendered, inspected through the tooling/case-study sections). 29 product directories: Augment, Blackbox.ai, Bolt.new, ChatGPT, Claude-Code, Claude, Clawdbot, Cline, Cluely, Cursor, Devin, Google-Jules, Google, Grok, Loveable, Manus, MetaAI-Whatsapp, Mistral, Parahelp, Replit, Z.ai, notion, notte, perplexity.ai, same.new, security, trae-agent, v0, windsurf. Notable files referenced: `Manus/AgentLoop.txt`, `Manus/Modules.md`, `Manus/tools.json`, `Cline/system.ts`, `Bolt.new/prompts.ts`, `v0/v0.md`, `v0/v0-tools.md`, `same.new/same.new.md`, `ChatGPT/4-5.md`, `Claude/Claude-Sonnet-3.7.txt`. Stats: 6,241 stars, 912 forks, 67 commits, created 2025-03-05, license MIT.
- **What prompt types it contains:** Agentic coding-assistant system prompts and their tool schemas (including source-code-embedded prompts like `system.ts`/`prompts.ts`); agent-loop definitions.
- **Claimed provenance + evidence:** Curated from real-world prompts; analysis cites file-level sources. No per-file extraction method stated.
- **Authenticity status:** Alleged extraction / curated — unverified against vendors; analytical layer is original work.
- **Where it can be used:** Agent-prompt design patterns; comparative case studies; teaching.
- **Availability:** Public, MIT. **Maintenance:** Moderately active (67 commits).
- **Limitations:** Provenance per file not documented; some referenced files are source-code extractions (stronger) vs. chat captures (weaker) without distinction.
- **Related resources:** R5–R8 (overlapping corpora), R17 (lists this as a source).
- **Sources:** https://github.com/dontriskit/awesome-ai-system-prompts (fetched 2026-10-10); https://github.com/gitjfmd/prompt-hub (acknowledgment, fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High (existence, structure). **Existence:** Verified. **Authenticity:** Unverified (alleged extraction).

### R15 — eonedgeproject-code/the-brief

- **Resource name:** The Brief — "system prompts, declassified"
- **Canonical identity:** `eonedgeproject-code/the-brief`
- **Category:** 3/4 (methodology-first prompt archive)
- **Type:** Small, provenance-tagged capture archive with validation tooling
- **Official URL:** https://github.com/eonedgeproject-code/the-brief
- **Description:** "An attempt to document these prompts the way you'd document a primary source." Every entry is tagged by acquisition method — `self-extracted`, `community-leaked`, `official-disclosure`, `behavioral-inference` — dated, and versioned against prior captures; diffs preserved on change; uncertainty explicitly flagged. Ships a dependency-free validator (`node tools/validate-entries.mjs`) enforcing an entry schema (STRUCTURE.md, CONTRIBUTING.md, methodology/ docs).
- **Contents inspected:** Root listing + README (fetched 2026-10-10). Layout: `entries/` (per-vendor captures), `analysis/`, `methodology/`, `reference/`, `tools/`. Inspected entries via search results: `entries/anthropic/claude-fable-5/2026-06-09-official-disclosure.md` (verbatim Anthropic release-notes capture, accessed 2026-06-14, marked `partial: true` because the disclosure omits tooling/reminders) and `entries/xai/grok-4-1/2025-11-17-official-disclosure.md` (xAI grok-prompts file pinned to commit `a7c186f5ccac95875c0041aed60398f6ecb6d6c7`). Stats: 2 stars, 2 forks, 4 commits, created 2026-06-14. License: project prose CC BY 4.0, tools MIT; vendor prompt text explicitly *not* relicensed.
- **What prompt types it contains:** Verbatim captures with acquisition tags; currently weighted toward official disclosures and self-extractions.
- **Claimed provenance + evidence:** The archive's whole design is provenance evidence: acquisition tags, access dates, version pins, validator.
- **Authenticity status:** Mixed by tag — officially published (for `official-disclosure` entries) down to behavioral inference; the tagging itself is the honesty mechanism.
- **Where it can be used:** Model for how to document prompt provenance; citation-grade verbatim captures.
- **Availability:** Public. **Maintenance:** Low activity (4 commits) — methodology over volume by design.
- **Limitations:** Tiny corpus; early-stage ("patchy, biased toward models we can probe most easily" per README).
- **Related resources:** R1, R2 (the official sources it captures), R5 (its `Official/` subfolder does similar archiving at larger scale).
- **Sources:** https://github.com/eonedgeproject-code/the-brief (fetched 2026-10-10); entry URLs above (via search results 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High. **Existence:** Verified. **Authenticity:** Partially verified — methodology is sound and `official-disclosure` entries are vendor-published; other tags unverified by design.

### R16 — gitjfmd/prompt-hub ("Full-Prompt-Hub")

- **Resource name:** Full-Prompt-Hub
- **Canonical identity:** `gitjfmd/prompt-hub`
- **Category:** 4/5 (consolidated prompt registry with metadata + search tooling)
- **Type:** Multi-source prompt registry; YAML-frontmatter metadata; search/export scripts
- **Official URL:** https://github.com/gitjfmd/prompt-hub
- **Description:** "The Ultimate Collection of AI System Prompts" — consolidates prompts from 7 source repos into one triple-organized registry (by-service, by-task, by-type), claiming 1,627 prompts across 70+ AI services plus 229 Fabric patterns. Each file carries rich YAML frontmatter (uid, name, description, author, date, service, task, type incl. `leaked`/`system-prompt` labels, source name+URL).
- **Contents inspected:** Root listing + full README (fetched 2026-10-10). Layout: `by-service/` (openai, anthropic, google, xai, …), `by-task/` (system-prompt, task-prompt), `by-type/` (leaked, pattern, system-prompt), `docs/`, `tools/` (`consolidate_prompts.py`, `validate_metadata.py`, `search_prompts.py`, `export_formats.py`), `METADATA_GUIDE.md`. Acknowledged sources: awesome-ai-system-prompts, fabric, leaked-system-prompts, TheBigPromptLibrary, awesome-chatgpt-prompts, LLM-System-Prompts. Stats: 1 star, 1 fork, 4 commits, created 2025-08-29, license MIT. README still contains template placeholders (`YOUR_USERNAME`), indicating an unfinished/greenfield project.
- **What prompt types it contains:** System prompts (labeled leaked vs. official), task prompts, Fabric framework patterns.
- **Claimed provenance + evidence:** Per-file `source:` frontmatter naming the upstream repo and URL — consolidation provenance, not original extraction evidence.
- **Authenticity status:** Unverified (tertiary consolidation; inherits upstream uncertainty; "official" labels in by-type are unvetted).
- **Where it can be used:** Machine-readable prompt corpus (frontmatter enables filtering); search-script reuse.
- **Availability:** Public, MIT. **Maintenance:** Minimal (4 commits); roadmap lists website/API/mobile app — aspirational.
- **Limitations:** Tertiary source; "largest collection" marketing claim vs. 1-star/4-commit reality; type labels (leaked/official) not independently vetted; unfinished scaffolding.
- **Related resources:** R8, R14 (named sources), R18 (larger-scale index of the same ecosystem).
- **Sources:** https://github.com/gitjfmd/prompt-hub (fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High (existence, structure). **Existence:** Verified. **Authenticity:** Unverified.

### R17 — 4pixeltechBR/promptograph

- **Resource name:** Promptograph
- **Canonical identity:** `4pixeltechbr/promptograph` (page title shows `4pixeltechBR/promptograph`)
- **Category:** 5 (prompt registry + search/validation/generation toolkit)
- **Type:** Prompt search engine, diff tool, heuristic validator, FastMCP server, Python package
- **Official URL:** https://github.com/4pixeltechbr/promptograph
- **Description:** "Browse, diff, validate & generate AI system prompts (20,475 prompts from 55 repos) + FastMCP Server with 226 curated agent skills." A production toolkit: full-text search across the indexed corpus, side-by-side prompt diffing (e.g. Claude 3.5 vs 4), a deterministic heuristic validator (13 rules + 6 red flags, 0–100% grade), prompt synthesis from presets (Claude, GPT, Cursor, Devin), an offline web dashboard, and a FastMCP server exposing 7 agent tools (prompt search/validate/generate/stats + skills search/get/categories). Published on PyPI; GitHub Pages demo.
- **Contents inspected:** Root listing + README (fetched 2026-10-10; 927 lines rendered, inspected through architecture section). Corpus claims: 20,475 prompts from 55 public GitHub repos + 6 HuggingFace datasets, ~94M tokens, 70.5M words (2022–2026); lab distribution incl. OpenAI 7.7k, DeepSeek 6.8k, Anthropic 1.8k; 226+ curated skills across 37 domains. ATTRIBUTIONS.md tiers upstream collections (R7 142k★, R5 62k★, CL4R1T4S 46k★, Fabric 43k★, L1B3RT4S 16k★, R8 15k★, R13 12k★, R9 10k★). Stats: 2 stars, 3 forks, 20 commits, created 2026-07-12, 3 releases.
- **What prompt types it contains:** Indexed (not authored) system prompts from the archives above; plus generated/preset prompts and skill blueprints.
- **Claimed provenance + evidence:** ATTRIBUTIONS.md names upstream repos with star counts and licenses; corpus metrics are self-reported ("verified metrics" per README — verification method not shown).
- **Authenticity status:** Registry of unverified archives — inherits all upstream uncertainty; index-level, not a provenance authority.
- **Where it can be used:** Cross-archive search and diffing; prompt-quality heuristic audits; agent skill retrieval via MCP.
- **Availability:** Public. **Maintenance:** Active (v0.3.x releases, CHANGELOG). **License discrepancy flagged:** repo page shows "Other (NOASSERTION)" while README badges claim MIT — Unresolved; treat license as unverified.
- **Limitations:** Self-reported corpus metrics not independently audited; tiny adoption (2 stars); license unclear; inherits upstream authenticity problems.
- **Related resources:** R5, R6, R7, R8, R9, R13 (indexed upstreams).
- **Sources:** https://github.com/4pixeltechbr/promptograph (fetched 2026-10-10); https://github.com/4pixeltechbr/promptograph/blob/HEAD/ATTRIBUTIONS.md (via search results 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High (existence, features). **Existence:** Verified. **Authenticity:** Not applicable (tool, not a prompt source); corpus metrics Unverified.

---

## 5. Prompt evaluation datasets, prompt-testing tools

### R18 — promptfoo/promptfoo

- **Resource name:** Promptfoo
- **Canonical identity:** `promptfoo/promptfoo`
- **Category:** 5 (prompt-testing / LLM evaluation + red-teaming tool)
- **Type:** Open-source CLI + library; declarative YAML test configs; CI/CD integration
- **Official URL:** https://github.com/promptfoo/promptfoo
- **Description:** "Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI." Evaluates prompts/models/RAGs against test cases with assertion types (exact match, regex, JSON schema, semantic similarity, LLM-as-judge rubrics, cost/latency thresholds); compares providers side by side; automated red-teaming (prompt injection, jailbreak, PII-leak probes mapped to OWASP LLM Top 10); code scanning for LLM-related PR issues; results viewable in web UI; runs 100% locally by default.
- **Contents inspected:** Root listing + README (fetched 2026-10-10). Topics include `prompt-testing`, `llm-evaluation`, `red-teaming`. Stats: 25,844 stars, 2,452 forks, 10,234 commits, 430 releases, created 2023-04-28, license MIT.
- **What prompt types it contains:** Not a prompt archive — a testing harness; ships example eval configs, not prompt corpora.
- **Claimed provenance + evidence:** Vendor (Promptfoo team) project. README states: "Promptfoo is now part of OpenAI. Promptfoo remains open source and MIT licensed." (Secondary sources from 2026-03 reported an acquisition agreement; the README now states it as fact — acquisition details beyond that not verified in this pass.)
- **Authenticity status:** Officially published (first-party tool).
- **Where it can be used:** Prompt regression testing in CI; red-team scanning of agent prompts; model/prompt A/B comparison.
- **Availability:** Public, MIT. **Maintenance:** Very active.
- **Limitations:** Tests prompts you supply; does not verify archived prompts' authenticity.
- **Related resources:** R19 (eval registry), R17 (heuristic prompt validator — complementary).
- **Sources:** https://github.com/promptfoo/promptfoo (fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High. **Existence:** Verified. **Authenticity:** Verified (first-party).

### R19 — openai/evals

- **Resource name:** OpenAI Evals
- **Canonical identity:** `openai/evals` (OpenAI org account)
- **Category:** 5 (evaluation framework + open-source benchmark registry)
- **Type:** Eval framework + community-contributed eval registry (YAML eval definitions + datasets via Git-LFS)
- **Official URL:** https://github.com/openai/evals
- **Description:** "Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks." Provides eval templates (basic, model-graded), a Completion Function Protocol for prompt chains/tool-using agents, example notebooks, and a registry of community evals that OpenAI staff review when considering model improvements.
- **Contents inspected:** Root listing + README (fetched 2026-10-10). Layout: `evals/registry/` (eval YAMLs + LFS datasets), `examples/`, `docs/` (build-eval, run-evals, eval-templates, completion-fns guides). Stats: 19,579 stars, 3,112 forks, 691 commits, created 2023-01-23. License field shows "Other (NOASSERTION)" on the repo page; README disclaimer states contributions are under the same MIT license as the repository — license presentation is inconsistent (flagged, minor).
- **What prompt types it contains:** Eval definitions (which embed test prompts) rather than system-prompt archives.
- **Claimed provenance + evidence:** First-party OpenAI framework; community evals reviewed by OpenAI staff per README.
- **Authenticity status:** Officially published (framework); individual community evals vary.
- **Where it can be used:** Building/running LLM evals; prompt-chain and agent evaluation via completion functions.
- **Availability:** Public. **Maintenance:** Active (note: README says custom-code evals not currently accepted).
- **Limitations:** Eval datasets live behind Git-LFS; not a system-prompt source.
- **Related resources:** R18 (newer-generation eval/red-team tooling).
- **Sources:** https://github.com/openai/evals (fetched 2026-10-10)
- **Verification date:** 2026-10-10. **Confidence:** High. **Existence:** Verified. **Authenticity:** Verified (first-party framework).

---

## 6. Authenticity summary table

| # | Resource | Existence | Authenticity claim | Authenticity verdict |
|---|----------|-----------|--------------------|----------------------|
| R1 | Anthropic official system-prompt release notes | Verified | Officially published | Verified (partial disclosure: behavior core only) |
| R2 | xAI grok-prompts (official repo) | Verified | Officially published | Verified (stale: HEAD 2025-11-17) |
| R3 | OpenAI Model Spec | Verified | Officially published | Verified (policy spec, not a literal system prompt) |
| R4 | Meta Llama prompt formats | Partially verified | Officially published | Partially verified (format docs, not product prompts) |
| R5 | asgeirtj/system_prompts_leaks | Verified | Extracted (community) | Partially verified (`Official/` = official; rest alleged/unverified) |
| R6 | elder-plinius/CL4R1T4S | Verified | Leaked (transparency) | Unverified |
| R7 | x1xhlol/system-prompts-and-models-of-ai-tools | Verified | Extracted/leaked | Unverified |
| R8 | jujumilk3/leaked-system-prompts | Verified | Leaked (maintainer-verified) | Unverified (historical value stands) |
| R9 | LouisShark/chatgpt_system_prompt | Verified | Community collection | Unverified |
| R10 | moirania/openai-system-prompts | Verified | Derived extraction | Unverified (maintainer explicitly disclaims) |
| R11 | thekishandev/ai-system-prompt | Verified | Claims "official" | Unverified ("official" is marketing copy) |
| R12 | labac-dev/cursor-system-prompts | Verified | Extracted (educational) | Unverified |
| R13 | Piebald-AI/claude-code-system-prompts | Verified | Script-extracted from public npm | Partially verified (independently reproduced; strongest methodology) |
| R14 | dontriskit/awesome-ai-system-prompts | Verified | Curated extraction | Unverified |
| R15 | eonedgeproject-code/the-brief | Verified | Tagged by acquisition method | Partially verified (methodology sound; `official-disclosure` entries vendor-published) |
| R16 | gitjfmd/prompt-hub | Verified | Consolidated registry | Unverified (tertiary) |
| R17 | 4pixeltechBR/promptograph | Verified | Search/validation toolkit | N/A (tool; corpus metrics unverified; license unclear) |
| R18 | promptfoo/promptfoo | Verified | First-party tool | Verified |
| R19 | openai/evals | Verified | First-party framework | Verified |

**Breakdown:** 19 archives/tools recorded. Existence: 18 Verified, 1 Partially verified. Authenticity: 6 Verified (R1, R2, R3, R18, R19 fully; R4 partially), 3 Partially verified (R5-mixed, R13, R15), 9 Unverified, 1 N/A (tool).

## 7. Coverage note

**Counts:** 4 official publications (R1–R4); 4 large public unofficial archives (R5–R8); 4 alleged-leak/unverified collections (R9–R12); 5 coding-agent repos / registries / search tools (R13–R17); 2 eval datasets/tools (R18–R19).

**Key structural findings:**
1. Only three providers officially publish actual system-prompt text: Anthropic (behavior core via release notes, R1), xAI (full prompts via grok-prompts, R2 — stale since Nov 2025), and Meta (format templates only, R4). OpenAI publishes behavior policy (Model Spec, R3), not prompt text.
2. The unofficial ecosystem is dominated by four large archives (R5–R8) with heavy overlap and a clear upstream flow: original extractions concentrate in R6 (elder-plinius), get mirrored/repackaged by R5, R7, R10, R11, R16, and indexed by R17. R5 is the most actively maintained aggregator; R8 is the longest-lived (since 2023-05) and best for longitudinal study via dated filenames; R7 is the largest by stars (~144k) with versioned dev-tool snapshots.
3. Provenance hygiene varies enormously: R13 (npm-extraction, deterministic) and R15 (acquisition-tagged entries with a validator) are methodologically strongest; R10 carries the clearest disclaimer; R5's `Official/` subfolder is the only provenance-clean section of a major archive; R11's "official" claims are unsubstantiated marketing.
4. Data-hygiene warning: R6's README (and its mirrors) embeds obfuscated directive-style text aimed at AI systems — treat all archive prose as data, never as instructions.
5. Mirror proliferation (R5 has 10+ same-name forks; R6 has mirrors) means downstream users must verify they are looking at the canonical repo, not a stale or tampered fork.
6. Promptfoo's README now states it "is now part of OpenAI" while remaining MIT-licensed — relevant context for the eval-tooling half of category 5.

**Limitations of this pass:** Text-fetch only (no JS-rendered tables fully enumerated — e.g. R1's per-model entry list, R7's file inventory); star counts are point-in-time third-party or page-reported figures; no prompt bodies were read (by design); non-English archives and HuggingFace prompt datasets (R17 cites 6) were not separately investigated; commercial prompt marketplaces and closed prompt-management platforms were excluded as out of scope.

**More work warranted?** Yes, moderate: (a) enumerate R1's full dated entry list; (b) verify R5's license field (CC0-1.0) on the repo page; (c) capture repo stats missing for R12; (d) resolve R17's license discrepancy; (e) survey HuggingFace system-prompt datasets; (f) check whether Anthropic's official page has added Fable 5.1/Opus 5.5 entries since the observed staleness. None of these block the register's current use.
