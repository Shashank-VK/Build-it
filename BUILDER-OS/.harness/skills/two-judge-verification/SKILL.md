---
name: bos-two-judge-verification
description: >
  Auto-triggers before finalizing an architectural decision, choosing
  between competing algorithms/approaches, writing security-sensitive
  code (auth, secrets handling, input validation), or when the primary
  agent's own confidence in an answer is genuinely low. Does NOT
  trigger for routine code edits, small bug fixes, formatting, or
  any change where the correct approach is not actually in question.
  If uncertain whether this qualifies, err toward NOT triggering --
  the cost/latency of a false trigger is not worth it for low-stakes work.
---

# Two-Judge Verification

When this skill loads, convene a Two-Judge verification panel. 
You MUST explicitly route the models for this process as follows:

1. **Judge 1 (Devil's Advocate):** Use the free 'Big Pickle' model. This judge takes the strongest possible case AGAINST the proposed approach. Identifies failure modes, edge cases, and hidden assumptions.

2. **Judge 2 (Steelman):** Use your standard reasoning model (e.g., Claude 3.5 Sonnet). This judge takes the strongest possible case FOR the approach, responding specifically to Judge 1's objections.

3. **Verdict:** Use your standard reasoning model. After both judges have argued their case, summarize:
   - The core tradeoff
   - Which judge's argument was stronger and why
   - The recommended decision with explicit reasoning
   - Any conditions under which the opposite decision would be correct

Do NOT produce a wishy-washy "both sides have merit" verdict. Make a specific
recommendation. If the evidence genuinely does not favor either side, say that
explicitly and explain what additional information would break the tie.

Ref: files/01-opencode-research/BUILD-PROMPT-UNIVERSAL.md (PART 3A); contract ../how-to-use/01-skills.md.
