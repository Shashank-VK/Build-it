---
name: bos-context-compaction-pruner
domain: Context & Memory
version: 1.0.0
tier: Essential
cap: CAP-09
triggers:
  - "context full"
  - "token limit"
  - "compact context"
  - "context window"
---

# Context Compaction Pruner

## Objective
Proactively compress, distill, and prune agent working memory during long execution trajectories to prevent context saturation, reduce hallucination risks, and maintain razor-sharp alignment with core task objectives while achieving a compression ratio of $C < 0.40$.

## When to Activate
- Total conversation token count exceeds 28,000 tokens (or ~70% of available attention budget).
- Immediately prior to loading or ingesting large source files, dependency trees, or database dumps (>500 lines or >10k tokens).
- Transitioning between major workflow phases (e.g. from codebase survey to implementation, or from implementation to testing/debugging).
- Detecting degraded attention, repetitive tool loops, or sluggish prompt evaluations.

## Step-by-Step Runbook

### Step 1: Trigger Check & Threshold Monitoring
Continuously audit estimated prompt size and token consumption. Trigger the pruning procedure immediately if either condition is met:
1. **Token Threshold**: Conversation context reaches or exceeds **28k tokens**.
2. **Pre-Ingestion Buffer**: Preparing to read a file, diff, or log trace whose size exceeds **10k tokens**, to prevent unrecoverable context truncation.

---

### Step 2: Pinned Set Identification
Before discarding any context history, explicitly catalog the **Immutable Pinned Set** that MUST survive compaction:

1. **System Invariants & Operating Rules**: All safety bounds, permission classes, and coding style constraints.
2. **Active Task Objective**: The primary user request, specific acceptance criteria, and explicit non-goals.
3. **Open Work Tracking (TODOs)**: Complete backlog of pending items with exact current completion state.
4. **Active Code Anchors**: File paths of actively edited modules, critical type definitions, and core interface signatures.

---

### Step 3: Structured Compaction Procedure
Apply deterministic pruning and distillation across existing conversational context:

1. **Synthesize Completed Trajectory**: Replace sprawling conversational steps and reasoning logs with a concise, high-density 3-bullet block:
   ```markdown
   ### Completed so far:
   - [Architectural Decision / Setup]: Initialized module boundaries and configured test harness.
   - [Implementation State]: Created core service handlers in `src/service.py` and validated schemas.
   - [Verification Outcome]: Unit test suite passing 14/14 tests; identified edge-case in retry handler.
   ```
2. **Drop Intermediate Reasoning**: Discard all speculative thoughts, exploratory dead-ends, scratchpad brainstorming, and intermediate conversational pleasantries.
3. **Prune Tool Call History**: Purge older tool execution payloads (e.g. large file contents, directory trees, raw build logs), retaining strictly the **last 2 tool call results** for active working memory.

---

### Step 4: Verification & Compression Ratio Target
Validate the compaction against quantitative and qualitative exit criteria:

1. **Mathematical Compression Target**:
   $$\text{Compression Ratio } C = \frac{\text{tokens\_after}}{\text{tokens\_before}} < 0.40$$
   *(The pruned context must consume less than 40% of pre-compaction tokens, achieving $\ge 60\%$ reduction).*
2. **Semantic Integrity Check**:
   - Confirm active goal and acceptance criteria are unambiguous.
   - Verify that all 4 elements from the Pinned Set are fully preserved.
   - Ensure the next actionable step is explicitly stated with target filenames and expected inputs.

## Completion Gate
- Context token consumption is verified below the 40% threshold ($C < 0.40$).
- All pinned items (system rules, task objectives, open TODOs, active file paths) remain fully intact.
- Agent seamlessly proceeds with the subsequent step without requesting re-explanation of prior work.

## Common Pitfalls
- **Premature or Delayed Compaction**: Waiting until the model hits a hard context cut-off window rather than executing proactive compaction at 28k tokens.
- **Accidental TODO Erasure**: Dropping pending edge cases or unverified assertions during trajectory summarization.
- **Retaining Heavy Tool Outputs**: Keeping large multi-megabyte tool responses (such as full coverage reports or raw dependency trees) in context instead of extracting single-line summary metrics.
Ref: verbatim runbook from solo the-harness; skill card in `../how-to-use/01-skills.md`.
