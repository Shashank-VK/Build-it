# Domain A — Area 7: Security and Quality Assurance (AI-assisted)

*How AI assists with securing the product during the build — SAST/secret scanning on AI-generated code, AI security review agents, and the measured insecurity of AI-generated code.*

> Read-only research. No installation, ranking, or recommendations. Accessed 2026-10-10 unless noted.

## 1. What teams demonstrably do

### The measured insecurity of AI-generated code — multiple independent studies converge
- **Claim (Verified — multiple independent studies, same direction):**
  - Veracode GenAI Code Security Report (Jul 2025; Spring 2026 update): 80 coding tasks, 4 languages, 4 CWE types, no security hints in prompts → models generated insecure code **45%** of the time (2025, 100+ models) and **45%** again in Spring 2026 (150+ models incl. GPT-5.1/5.2, Gemini 3, Claude 4.5/4.6) — "the security ceiling holds firm." Java worst (71.5% insecure). XSS/log-injection weakest (86–88% fail); SQLi/crypto patterns better (models get them right 83–87%).
  - AppSecSanta (2026): 6 LLMs vs OWASP Top 10, 522 samples → **25.7%** overall vulnerability rate; GPT-5.2 best 19.5%, Claude Opus 4.6/DeepSeek V3/Llama 4 Maverick worst 29.9%; dominant category Broken Access Control (path traversal, SSRF).
  - Cobalt AI / arXiv 2604.05292 (Apr 2026): 3,500 artifacts, 7 LLMs, Z3 SMT formal verification → **55.8%** contain a vulnerability; explicit security instructions reduce the rate by only 4 points; six industry tools combined flag 7.6% and miss 97.8% of Z3-proven findings; models identify their own vulnerable outputs 78.7% of the time in review mode yet generate them at 55.8% — a generation–review asymmetry.
  - Symbiotic Security "State of Cyber" (Aug 2026): 1,967 repos + 1,072 vibe-coded apps + 10 scanners → AI-assisted repos averaged **42.3 vulns vs 9.6** human-only (**4.4x**); 98% of vibe-coded apps had ≥1 vuln, 29% high/critical, 16% let strangers modify data with no login.
  - Headline aggregates (secondary): 69% of orgs found vulns from AI-generated code; 1 in 5 suffered a serious incident tied to AI-generated code.
- Sources: https://www.scworld.com/news/llms-make-insecure-coding-choices-for-45-of-tasks-study-finds ; https://www.secondtalent.com/resources/ai-generated-code-quality-metrics-and-statistics-for-2026/ ; https://appsecsanta.com/research/ai-code-security-study-2026 ; https://arxiv.org/pdf/2604.05292v2 ; https://lifestyle.thepointnews.com/story/825944/ai-assisted-code-introduces-4-4x-more-security-vulnerabilities-than-human-written-code-new-research-finds/ ; https://codeqa.aivyuh.com/blog/ai-generated-code-vulnerabilities-2026/
- **Engineering implication:** treat every AI-generated code path as untrusted-by-default; the numbers are stable across two years and don't improve with newer models ("model release date and size did not have a significant impact on security performance" — Veracode).

### AI security review in the dev loop
- **Claim (Corroborated):** Teams wire security review into the agent loop rather than as a pre-PR gate: Anthropic moved `/security-review` from pre-PR to in-session with a security-guidance plugin (some customers enforce it as a hard gate via PreToolUse hook; Anthropic's own hard gate sits at test/CI). Separate *narrow* review agents beat one mega-prompt — requiring agents to write proof a finding is valid raised substantive review comments from 16% to 54% of PRs.
- Source: https://github.com/uygnoey/skills-from-claude-blog/blob/HEAD/2026.07.21_how-anthropic-secures-its-ai-native-software-development-lifecycle/description.en.md
- **Claim (Corroborated):** AI review tools pair review with SAST in one pass (CodeAnt), or back PR review with security across code/deps/cloud/runtime (Aikido). Greptile does not reliably catch hardcoded secrets or vulnerable dependencies per a 2026 alternatives roundup — i.e., AI review ≠ secret/dependency scanning; keep dedicated scanners.
- Source: https://huntaegis.com/article/8b56854efac9c26f729a381061af9c11

### Encoding secure-coding guidance in agent context
- **Claim (Corroborated):** Anthropic's posture: "secure coding guidance is encoded, not published" — guidelines live in `CLAUDE.md` files and org-wide skills so generated code follows them at generation time; the loop closes when an agent discovers a bug class and the relevant file is updated so it cannot recur. Agents code on remote VMs with egress allowlists; risk tiering decides what may be automated, with strict human approval retained on sensitive codebases and invariant testing ("user A can never read user B's data") triggering manual review.
- Source: https://github.com/uygnoey/skills-from-claude-blog/blob/HEAD/2026.07.21_how-anthropic-secures-its-ai-native-software-development-lifecycle/description.en.md

## 2. Tools and workflows
| Tool/pattern | Role |
|---|---|
| Veracode/SAST + SCA + secret scanners | Baseline gates on AI-generated code (still required — AI review doesn't replace) |
| In-session `/security-review` agents | Continuous review during generation; proof-of-validity requirement |
| Narrow scoped review agents | One concern per agent; catches others' blind spots |
| Egress-allowlists + remote VMs + sandboxes | Contain agent blast radius (Anthropic: sandboxing cut permission prompts 84%) |
| Risk tiering + invariant tests | Decide what may be automated; trigger manual review |

## 3. Failure modes
1. **Insecure-by-default generation.** 45–56% insecure across studies; stable over two years. **Verified.**
2. **Generation–review asymmetry.** Models catch their own vulns 78.7% in review mode but emit them 55.8% of the time — generating safely is a different skill from reviewing. **Verified (Cobalt).**
3. **Prompt instructions barely help.** Explicit security instructions: −4 points only. **Verified (Cobalt).**
4. **Tooling gap.** Six industry tools combined miss 97.8% of formally-proven findings — pattern-based scanners structurally miss what models emit. **Verified (Cobalt).**
5. **Secrets/dependency blind spots.** AI reviewers don't reliably catch hardcoded secrets or vulnerable deps. **Corroborated.**
6. **Access-control dominance.** The top flaw class is Broken Access Control (path traversal, SSRF) — the kind that needs app-context, not pattern matching. **Corroborated (AppSecSanta).**

## 4. Costs / latency / reliability
- Security scanning adds pipeline latency; agent-based stress testing needs compute + config + expertise. For auth/payments/data pipelines the cost is justified; for low-stakes output it may not be. **Corroborated (forgeworkflows analysis).**
- SAST-on-every-PR is the enforcement layer in agent-heavy pipelines (see file 08). **Corroborated.**

## 5. Human correction burden
- High and non-delegable on trust boundaries: invariant testing and manual review trigger on data-access invariants; a third of past claude.ai incident bugs would have been caught by current automation — meaning two-thirds needed humans or better automation. **Corroborated (Anthropic-derived).**

## 6. Where AI genuinely helps vs where it creates rework
- **Genuinely helps:** in-session review with proof-of-validity (16%→54% substantive comments); narrow agents catching one another's mistakes; encoding learned bug classes into CLAUDE.md so they don't recur; invariant tests as executable security specs.
- **Creates rework:** insecure defaults that must be re-audited (4.4x vuln multiplier); false confidence from "AI-reviewed" labels when scanners structurally miss the flaw classes models emit.

## 7. Boundary notes (A vs B vs C)
- **Domain A:** securing the software you're building (SAST on AI-generated code, review agents in your pipeline). **Domain B:** a shipped *security product* with AI inside (e.g., an AI firewall or AI vuln-scanner SaaS — the product is B; using it in your pipeline is A). **Domain C:** AI doing security-operations business work (SOC triage as an org function). Keep product / process / operations distinct.

## Evidence register (this file)
| # | Claim | URL | Source type | Author/org | Pub date | Confidence | Class |
|---|---|---|---|---|---|---|---|
| 7.1 | Veracode 2025: 45% insecure; 2026: 45% again, 150+ models; Java 71.5% | https://www.scworld.com/news/llms-make-insecure-coding-choices-for-45-of-tasks-study-finds | News on study | SC Media (Veracode report) | ~Jul 2025 | High | secondary interpretation |
| 7.2 | Veracode Spring 2026: 55% secure ceiling; XSS/log-injection weakest | https://www.secondtalent.com/resources/ai-generated-code-quality-metrics-and-statistics-for-2026/ | Stats roundup | SecondTalent (Veracode data) | Sep 2026 | Medium–High | secondary interpretation |
| 7.3 | 6 LLMs vs OWASP: 25.7% vuln rate; access control dominant | https://appsecsanta.com/research/ai-code-security-study-2026 | Study | AppSecSanta | ~May 2026 | Medium | primary technical |
| 7.4 | 3,500 artifacts, Z3-verified 55.8% vuln; tools miss 97.8%; gen-review asymmetry | https://arxiv.org/pdf/2604.05292v2 | Paper (arXiv) | Cobalt AI (Blain, Noiseux) | Apr 2026 | Medium–High | primary technical |
| 7.5 | 1,967 repos: 4.4x vulns; 1,072 apps: 98% ≥1 vuln | https://lifestyle.thepointnews.com/story/825944/ai-assisted-code-introduces-4-4x-more-security-vulnerabilities-than-human-written-code-new-research-finds/ | Press release | Symbiotic Security via EINPresswire | Aug 2026 | Medium | first-hand practitioner |
| 7.6 | Anthropic in-session security review; narrow agents; risk tiering | https://github.com/uygnoey/skills-from-claude-blog/blob/HEAD/2026.07.21_how-anthropic-secures-its-ai-native-software-development-lifecycle/description.en.md | Blog notes | uygnoey (on Anthropic blog) | Jul 2026 | Medium | secondary interpretation |
| 7.7 | AI reviewers' blind spots (secrets, deps); 69% orgs stat | https://huntaegis.com/article/8b56854efac9c26f729a381061af9c11 | Roundup | HuntAegis | Sep 2026 | Low–Medium | secondary interpretation |
| 7.8 | Verification as infrastructure; semantic-level failures | https://forgeworkflows.com/blog/why-ai-generated-code-fails-in-production | Practitioner essay | ForgeWorkflows | Oct 2026 | Medium | first-hand practitioner |
