# What We Couldn't Find — Phase 0 Gaps

These are items from the original research brief that either **could not be verified at all**, were **found but are broken/retired**, or **need your help to resolve**. Nothing here was silently substituted — each gap is reported plainly.

---

## ❌ Completely Unverifiable — Need Your Help

| Name As Given | What Was Searched | What Was Found | What's Needed |
|---|---|---|---|
| `okjpg/llm-council` | Searched GitHub for `okjpg` username + `llm-council` fork | No public repo under this handle in any search. The `karpathy/llm-council` fork ecosystem is large but this specific username never appeared. | **Provide the exact GitHub URL.** This may be a voice-to-text distortion of a different username entirely. |

---

## ⚠️ Found But Broken / Retired / Security-Flagged

| Name As Given | Status | Detail |
|---|---|---|
| `ngmeyer/council-review` | **Archived — no longer maintained as standalone** | Migrated into `ngmeyer/skills` monorepo. The standalone install path (`npx skills@latest add ngmeyer/council-review`) no longer works. Use `npx skills@latest add ngmeyer/skills` instead. |
| `gsd-build/get-shit-done` (GSD) | **Original repo archived June 2026 with security warning** | Creator reportedly abandoned project after trust issues. Original npm package flagged as potentially compromised due to deep shell/bash permissions. Community has forked to `open-gsd` and `get-shit-done-redux`. Do not use original package. |

---

## ⚠️ Found But Unofficial / Fragile

| Name As Given | Status | Risk |
|---|---|---|
| `teng-lin/notebooklm-py` | **Real but unofficial** | Reverse-engineers undocumented Google internal RPCs. Will break silently if Google updates its backend. No official Google API exists for NotebookLM/Gemini Notebook as of this research. |

---

## ⚠️ URL Exists But Content Doesn't Match

| Claim | Reality |
|---|---|
| The walkinglabs "five layers" framework (task not clearly defined / insufficient context / misconfigured environment / missing verification / loss of state between sessions) lives at `https://github.com/walkinglabs/learn-harness-engineering/blob/main/docs/en/resources/templates/index.md` | **URL resolves and file is real**, but it contains a Template Guide (AGENTS.md, init.sh, claude-progress.md templates) — NOT the five-layer framework. The five-layer framework exists elsewhere in the repo with different layer names: **Instructions / State / Verification / Scope Boundaries / Lifecycle Handoff**. The phrasing you were given is a paraphrase, not a direct quote from that file. |

---

## ⚠️ Repo Name Was Wrong (Corrected, But You Should Know)

| What You Said | What Actually Exists | Difference |
|---|---|---|
| `KanakMalpani/Loop-Engineering` | `KanakMalpani/LoopBench` | Completely different purpose — LoopBench is a benchmark/evaluation tool (like MLPerf), not a loop framework or pattern library. If you wanted a loop framework from this person, it doesn't appear to exist. |

---

## ⚠️ Ecosystem Gap Found (Not a Missing Repo — An Actual Gap)

| Gap | Detail |
|---|---|
| **n8n ↔ OpenCode native integration** | No official integration path between n8n and OpenCode exists. Community nodes (`n8n-nodes-opencode`) are unofficial and unmaintained. No pre-built OpenCode workflow templates exist in n8n's template library. These are two separate ecosystems that would require custom wiring to connect. |
| **Backend equivalent of Astryx** | No tool was found that does for backend architecture what Astryx does for frontend — i.e., structured, agent-readable API/schema specs that prevent an agent from hallucinating endpoints or schema fields. This appears to be a genuine gap in the ecosystem as of August 2026. (Phase 2 will search more thoroughly.) |

---

## Items Deliberately Skipped in Future Phases

Per the research brief rules: **Phase 5 will NOT research any item Phase 0 could not confirm.** The following will be skipped in Phase 5 unless you provide a corrected URL:

- ~~`okjpg/llm-council`~~ — unverifiable handle, no repo found

---

## How to Help

If you have better information on any of the above, paste it in and I'll update the relevant files before the next phase that needs it.
