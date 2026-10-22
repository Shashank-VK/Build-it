# Phase 3 — Multi-Agent Verification / Hallucination Reduction

> Research completed: 2026-08-09  
> Scope: llm-council fork comparison for OpenCode, n8n assessment, ensemble model research, practical council configuration

---

## SECTION A — llm-council Forks: OpenCode Compatibility Comparison

### karpathy/llm-council (original)
**Confirmed real.** Andrej Karpathy's original. A three-stage deliberation pipeline:
1. **Generate** — multiple models independently answer the same question
2. **Peer Review** — answers are anonymized and reviewed/ranked by the council members
3. **Chairman Synthesis** — a designated model integrates feedback into a final verdict noting agreements, disagreements, and blind spots

**OpenCode support:** The original is a Python script, not packaged as a SKILL.md or MCP server. It works via OpenRouter natively, so models are provider-agnostic. To use with OpenCode, you'd run it as a sidecar script or wrap it in a SKILL.md manually — not a turnkey install. **Usable but DIY.**

---

### okjpg/llm-council
**Status: NOT CONFIRMED TO EXIST AS THIS EXACT REPO.**

Searched specifically. No repository `okjpg/llm-council` was found as a distinct, independent GitHub repo. The search returned that "the project is widely distributed under various community-maintained repositories" — which typically means the specific fork does not exist under this name. Phase 0 flagged this as unverifiable; Phase 3 research confirms: **skip this entry, do not use.**

---

### ngmeyer/council-review — **Also active at `ngmeyer/skills` (monorepo)**
**Status correction (live URL verified 2026-08-09): `ngmeyer/council-review` is LIVE and active, not archived.**  
**Standalone page title confirmed:** *"Claude Code skill: Run decisions, code, and plans through a council of 5 AI advisors with anonymous peer review. Based on Karpathy's LLM Council."*  
**`ngmeyer/skills`** is a separate consolidated monorepo that also exists in parallel.

Both repos coexist:
- **`ngmeyer/council-review`** — standalone, focused skill for the council pattern specifically
- **`ngmeyer/skills`** — consolidated monorepo including council-review plus additional skills

The consolidated version in ngmeyer/skills adds significant upgrades over the original:
- **Devil's Advocate pass:** Mandatory adversarial pass against emerging consensus — designed to force genuine disagreement rather than polite concurrence
- **Theatrical consensus detector:** Catches when advisors superficially agree without independent reasoning
- **Sycophancy guardrail:** Built into advisor and peer prompts to block performative agreement
- **Mediating-Assessments step:** Added to chairman synthesis
- **Outside-view / base-rate check:** Forces the chairman to consider prior probability before accepting the council's conclusion

**OpenCode support:** Installable via `npx skills@latest add ngmeyer/skills` which writes standard SKILL.md files to `.agents/skills/`. **OpenCode-compatible via open standard.** Model-agnostic, composable.

**This is the best-maintained council-pattern implementation available.** Use ngmeyer/skills, not the archived council-review.

---

### deliberation (from awesome-opencode catalog)
**Confirmed and already in the catalog (Element 8 / Element 15).**

A native OpenCode plugin + MCP server that asks GPT, Gemini, Grok, or OpenRouter models for second opinions as expert subagents. Seven expert subagents (Architect, Plan Reviewer, Scope Analyst, Code Reviewer, Security Analyst, Researcher, Debugger). Two modes:
- `ask-all` — queries every configured model at once and returns all answers
- `consensus` — runs an arbiter loop until models converge

**OpenCode support:** Native plugin + MCP server. **This is the most turnkey option for a council pattern in OpenCode** — no sidecar scripts, no manual SKILL.md authoring, works out of the box.

---

### OpenCode Built-in Council Analog: Open Conclave
**Also already in the catalog (Element 8).**

Multi-agent debates moderated by a captain agent until consensus. Each agent runs a different system prompt (logical, creative, research-focused). Configurable provider/model per agent. Native OpenCode plugin.

**Use case:** More suited to structured debate on open-ended questions. Deliberation plugin is better for point-in-time verification of a specific code or architecture decision.

---

## SECTION B — n8n: Honest Assessment

### What exists (documented):
n8n added native MCP support (v2.18.4+). This means:
- n8n can expose any workflow as an MCP server via the "MCP Server Trigger Node"
- n8n can act as an MCP client and call external MCP servers via the "MCP Client Tool Node"
- An `n8n-nodes-opencode` community npm package exists that adds OpenCode as a chat model node inside n8n's AI Agent workflows

### What doesn't exist (the gap):
There is **no documented, official import path for n8n workflows into an OpenCode-driven pipeline**. The MCP bridge goes the other direction — Claude Desktop, Cursor, Windsurf connecting *to* n8n, not OpenCode orchestrating *via* n8n. The community `n8n-nodes-opencode` package puts OpenCode inside n8n (n8n becomes the orchestrator), which is the inverse of your setup.

### Honest verdict for a solo developer/student:
**Adding n8n would add more complexity than value in this specific setup.**

The honest reasons:
1. **Wrong direction of control.** Your setup has OpenCode as the primary agent. n8n is designed to be the orchestrator, which means using it here requires inverting the architecture — n8n calls OpenCode, rather than OpenCode using n8n as a tool. That's a fundamental mismatch.
2. **n8n has a learning curve and maintenance overhead.** For the use cases relevant here (multi-agent verification, workflow orchestration), OpenCode's native plugin ecosystem (FlowDeck, Open Dynamic Workflows, deliberation plugin) already covers the same ground without a separate running service.
3. **n8n's value is clearest for webhook-driven automation and data pipeline work** — connecting external services (Slack, email, CRM, databases) to LLM calls on a schedule or trigger. If you're not doing that kind of work, the overhead of setting up and maintaining a self-hosted n8n instance doesn't pay off.
4. **The MCP bridge is a workaround, not a native integration.** Connecting OpenCode to n8n via the MCP Client Tool Node is possible but requires manually wrapping n8n workflows as MCP endpoints — effectively building the integration by hand.

**Recommendation: Skip n8n for this setup.** If a future project needs webhook-triggered automation, event-driven pipelines, or CRM integrations, revisit it then. For now, it adds infrastructure complexity without enough benefit.

---

## SECTION C — Ensemble Research: Honest Current Verdict

### The question: does ensembling smaller/free models reliably approximate frontier-model quality?

**Short answer: Partially yes, with important caveats.**

**What the research confirms (2024–2026):**
- The original Mixture-of-Agents (MoA) paper (2024) demonstrated that layering multiple LLMs — where agents share outputs and refine responses — could outperform GPT-4 Omni on benchmarks like AlpacaEval 2.0. The "collaborativeness" phenomenon is real and well-documented.
- Practical ceiling: ~90% of frontier-model performance achievable at significant cost reduction (cited as up to 20x cheaper in some production routing setups)

**The 2025 "Self-MoA" correction (important, often omitted from the optimistic pitch):**
- Research published 2025 (*Rethinking Mixture-of-Agents*) found that aggregating multiple outputs from the **same top-performing model** often outperforms heterogeneous ensembles of different smaller models
- This means: **the diversity of models matters less than the quality of the aggregation step**
- Running the same good model 3 times and aggregating often beats running 3 different weaker models once each

**The latency problem:**
- MoA introduces significant latency — every council "turn" is a full LLM call, and multiple parallel or sequential calls compound. For interactive coding work (where you're waiting for a response), this is a real UX cost.
- The "cheap at scale" argument applies to batch tasks and synthetic data generation, not interactive single-session agent work.

**For benchmark saturation:**
- General benchmarks (MMLU, GSM8K) are largely saturated; ensemble advantages disappear when evaluating on newer "Failure-Focused" benchmarks (Humanity's Last Exam) where even frontier models show consistent failures. At that level, ensembling weaker models doesn't recover the gap.

**Honest overall verdict:**
> Ensembling works best when: (1) you're verifying a specific decision rather than generating new content, (2) you have a good aggregation/synthesis step, (3) latency is acceptable, and (4) the base models are at least competent. It is **not** a reliable substitute for a stronger single model on generation-heavy tasks. For this setup's specific goal — catching hallucinations and validating architectural decisions before they cause wasted work — the ensemble pattern is well-suited and worth using, because it's *checking* (verifying) rather than *creating*.

---

## SECTION D — Practical Council Configuration

### Available models in this setup:
- **Big Pickle** — Free, via OpenCode Zen gateway. Fast, optimized for coding tasks. Stealth-launched; no public model card. Privacy caveat: free tier models may be used for feedback/training; avoid proprietary code.
- **Claude Sonnet** (current session model) — Paid, via OpenRouter or direct Anthropic API. Current high-capability frontier model.

**Constraint:** Solo developer/student. Cost matters. Latency matters. The council should not run on every task — only on high-stakes decisions.

---

### Recommended Council Configuration

#### Name: "Two-Judge Verification Pass"

**When to trigger it:** Architectural decisions, algorithm choices, security-sensitive code, or any time the primary agent's answer "doesn't feel right" and you want a second opinion before proceeding.

**Not for:** Routine code generation, file edits, small bug fixes. The latency and cost overhead is not worth it for low-stakes tasks.

---

**Roles:**

| Role | Model | Provider | Cost |
|---|---|---|---|
| **Primary Agent** (working model) | Claude Sonnet | OpenRouter | ~$3/M input tokens |
| **Challenger** (devil's advocate) | Big Pickle | OpenCode Zen | Free |
| **Arbiter** (synthesis) | Claude Sonnet | OpenRouter | ~$3/M input tokens |

**Why this exact structure:**
1. **Two judges, not three or more.** The research (especially the "Self-MoA" finding) shows diminishing returns from adding more models. Two independent perspectives plus a synthesis step covers the core value of the council pattern without multiplying latency 3-4x.
2. **Big Pickle as the Challenger, not a second Sonnet.** You want diversity at the adversarial step. Big Pickle running against Sonnet is more likely to surface genuine disagreement than Sonnet-vs-Sonnet, even accounting for Self-MoA findings, because the *adversarial framing* of the Challenger role is what generates useful disagreement — not just model diversity alone.
3. **Sonnet as the Arbiter.** The synthesis step requires the highest reasoning quality (integrating two conflicting positions, detecting theatrical consensus, issuing a final verdict with explicit reasoning). This is where a frontier model pays for itself.

---

**Protocol (based on ngmeyer/skills council pattern):**

1. **Primary (Sonnet) produces initial answer** — the agent's normal response to the task
2. **Challenger (Big Pickle) receives the question and the primary answer anonymized** — instructed to: find the weakest assumption, identify what could go wrong, and state what the primary answer gets wrong or glosses over. Specifically prompted to disagree where possible.
3. **Arbiter (Sonnet) receives:** the original question, the primary answer, and the Challenger's critique — instructed to: identify where the primary answer is right despite the critique, where the critique is valid and changes the answer, and issue a final verdict with explicit reasoning. Must flag "theatrical consensus" if the primary and challenger actually agree on all substance.

---

**Implementation path:**

**Option A (recommended, lowest friction):** Use the **deliberation plugin** from the awesome-opencode catalog — it's a native OpenCode plugin that already implements this pattern. Configure Big Pickle for the Challenger role and Sonnet for the Arbiter. Invoke with `/deliberation:verify` before committing to an architectural decision.

**Option B (for skill-based workflow):** Install `ngmeyer/skills` via `npx skills@latest add ngmeyer/skills` into `.agents/skills/`. This gives you the council skill with devil's advocate and theatrical consensus detection. Manually configure model assignments in the skill config.

**Option C (for selective use without plugins):** Keep a council SKILL.md at `.opencode/skills/council/SKILL.md` with the three-role protocol above written out explicitly. Invoke with `/council` when needed. No additional tooling required — just the agent following written instructions.

---

**Cost estimate:**
- A full council pass on a medium-complexity decision: ~2,000 input tokens × 2 Sonnet calls + 1,000 output tokens × 2 calls ≈ **$0.012–0.018 per council invocation** at current OpenRouter Sonnet pricing
- At 5 council invocations per day: ~$0.06–0.09/day, ~$1.80–2.70/month
- Big Pickle calls are free, so no additional cost there

**This is budget-appropriate for a solo developer/student workflow.**

---

## Summary

| Finding | Verdict |
|---|---|
| karpathy/llm-council | Real, usable but DIY — Python script, not a turnkey OpenCode install |
| okjpg/llm-council | **Not confirmed to exist** — skip |
| ngmeyer/council-review | **LIVE and active** (prior "archived" finding was incorrect); standalone skill; `ngmeyer/skills` is a separate parallel monorepo — both usable |
| deliberation plugin | **Best turnkey option** — native OpenCode plugin, most ready to use |
| n8n | **Skip for this setup** — wrong direction of control, adds infrastructure overhead without proportional benefit |
| Ensemble model research | Works for *verification* tasks; not a reliable substitute for frontier models on *generation* tasks; latency is a real cost for interactive work |
| Recommended council | Two-Judge: Sonnet (Primary + Arbiter) + Big Pickle (Challenger) via deliberation plugin or ngmeyer/skills |
