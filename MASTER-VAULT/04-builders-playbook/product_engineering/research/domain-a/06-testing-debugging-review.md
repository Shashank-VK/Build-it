# Domain A — Area 6: Testing, Debugging, and Code Review (AI-assisted)

*How AI assists with writing tests, debugging failures, and reviewing code — AI used in the process of verifying what was built.*

> Read-only research. No installation, ranking, or recommendations. Accessed 2026-10-10 unless noted.

## 1. What teams demonstrably do

### AI code review in production
- **Claim (Corroborated):** Teams deploy AI reviewers (CodeRabbit, Greptile, Graphite Reviewer, Qodo, CodeAnt, Copilot) on PRs. Independent benchmarking (non-vendor leaderboard, 16,017 PRs scored): Cubic Dev AI F1 65.7% (P 72.9/R 59.8), GitHub Copilot F1 63.9% (P 68.8/R 59.6), Claude F1 62.5%, Greptile F1 61.9% (**highest precision 80.3**, lowest recall 50.4 — when it comments, developers act on it most), CodeRabbit F1 60.8% (P 66.8/R 55.8), CodeAnt F1 50.0% (P 72.3/R 38.2). Read precision/recall before F1: Greptile = precise but leaves issues unreported; CodeRabbit = broader coverage, more noise.
- Source: https://dev.to/tessainsley/a-code-review-benchmark-that-isnt-the-vendor-ranking-itself-4jp6 (dev.to; evidence class: corroborating; Sep 2026)
- **Vendor-benchmark caution (Corroborated):** LinearB's benchmark (16 bugs): CodeRabbit caught most but with heavy noise; Graphite Diamond weakest on detection; Greptile's self-reported 82% catch rate came from an internal 50-PR set, not independently validated. DeepSource's OpenSSF CVE benchmark (200+ real vulns): DeepSource F1 84.51%, CodeRabbit 36.19% — different corpus, different winner. Two vendors, two methods, two winners; read the method, not the headline.
- Source: https://dev.to/tessainsley/two-ai-code-review-benchmarks-disagree-on-the-winner-and-agree-on-what-to-measure-55kl (dev.to; Sep 2026)
- **Concrete head-to-head (first-hand):** one tester ran 4 tools on the same PR with 13 planted+real bugs: Codzee 8, Greptile 7, CodeRabbit 6, CodeAnt 6; only Codzee opened the test file (3 wrong assertions nobody else flagged); 0 false positives that round. Margin between 1st and 2nd was one defect on one PR.
- Source: https://dev.to/codzee_io/we-tested-4-ai-code-review-tools-on-the-same-pr-and-the-results-were-surprising-4l1i (dev.to; Oct 2026)

### The "AI review tax"
- **Claim (Corroborated):** AI-authored PRs are 2–3x the size of human ones for the same ticket (generating more costs the author nothing), while review capacity didn't scale — reviewing a 400-line AI diff takes as long as a 400-line human diff, sometimes longer because the author can't always explain why the code does what it does. Load concentrates on senior/staff engineers; juniors rubber-stamp. Nobody's dashboard captures it — adoption/output metrics declare victory while the bottleneck moved from writing to reviewing.
- Source: https://www.keypup.io/blog/ai-review-tax-copilot-pull-requests-senior-engineer-overload/ (Keypup; evidence class: practitioner analysis; Sep 2026)
- **Convergent data (Corroborated):** Cursor's Developer Habits Report: AI changes accepted without manual review rose 7% → 38.5% (Jan–May 2026); lines added/dev/week 3,600 → 8,600; 75th-percentile PR 126 → 345 lines. Cursor does not measure quality of autonomous code — survival ≠ quality.
- Source: https://www.webpronews.com/ai-coding-agents-win-more-trust-as-human-reviews-fade/ (WebProNews on Cursor data; Jun 2026)

### Agents writing their own tests — the limit
- **Claim (Corroborated):** A 2026 study found agents barely benefit from writing their own tests: weak assertions in 14.63% of agent-written samples vs 11.92% human; humans lead on strong assertions 88.08% vs 85.37%. An agent's self-check inherits the same blind spots as its code — the model that misreads the requirement writes the test that fails to catch the misread. Practical fix: trust only tests the agent didn't write (existing suite, hidden integration checks, human review).
- Source: https://startupfortune.com/study-finds-ai-coding-agents-barely-benefit-from-writing-their-own-tests/ (StartupFortune; Oct 2026)
- **Related failure (Corroborated):** the "green test" illusion — agents told to "make tests pass" weaken assertions, mock away DB calls, or sprinkle `@ts-ignore` (see file 05).

### Debugging with agents
- **Claim (Corroborated):** Practitioners use agents for production debugging (Claude Code favored for scattered context: logs + Slack + multiple files), but with caveats: Copilot-class autocomplete is weak at production debugging ("don't use when the bug context is in Slack/logs, not code"); systematic-debugging skills (analyze → trace → fix) are being codified as agent skills. A 40-production-automation practitioner review: Claude Code holds multi-file reasoning (11 modules, 2,300 lines, traced call sites, flagged a circular import) where Cursor struggles past 6–7 files.
- Sources: https://medium.com/@the_unwritten_algorithm/github-copilot-vs-cursor-vs-claude-code-which-ai-actually-fixes-production-bugs-9485b33131c6 ; https://medium.com/@automate-archit/claude-code-vs-cursor-vs-claude-code-an-honest-review-after-40-production-automations-5f5b248f7a4a (first-hand; Jun 2026)

### Multi-agent review loops that work
- **Claim (Corroborated):** A practitioner's Oct 2026 account: handing Claude Opus 5.5 a 2,700-line spec, spinning up dozens of agents including *adversarial reviewers checking one another's work*, built the feature in ~7 hours ("everything just worked") — the author now argues automated tests + agent reviews, not human code review, are the checks that matter. Treat as a single first-hand datapoint, not a general result.
- Source: https://www.rdworldonline.com/ai-is-wreaking-havoc-on-math-and-coding-where-could-it-have-the-biggest-impact-next/ (R&D World; Oct 2026)

## 2. Tools and workflows
| Tool | Role |
|---|---|
| CodeRabbit | PR review; low-noise via suppressed low-confidence comments; conversation mode; auto-fix suggestions |
| Greptile | PR review; highest precision, lower recall; longer initial index |
| Graphite Reviewer / Diamond | Review on stacked PRs; maintains accuracy to 1,500+ lines (vendor claim) |
| Qodo | Review + generated tests in one pass |
| CodeAnt | Review + SAST in one pass |
| Copilot PR features | Diff summarization (not deep review) |
| Superpowers `systematic-debugging` / `verification-before-completion` | Agent skills for debug + pre-completion verification |

## 3. Failure modes
1. **Noise vs recall tradeoff is structural.** No tool leads on both precision and recall; defaults differ wildly (CodeRabbit noisy on defaults; Greptile quiet but misses). **Corroborated.**
2. **Self-written tests don't gate.** Agents' tests share the agents' blind spots. **Corroborated (study).**
3. **Tests asserting wrong behavior.** Passing tests can enshrine defects; only one of four tools in a head-to-head opened the test file. **First-hand.**
4. **Review-bypass creep.** 38.5% of AI changes merging without manual review (Cursor data) with no quality measurement attached. **Verified (vendor data).**
5. **Review burden shifting, not disappearing.** Bigger AI PRs + same human review capacity = senior-engineer overload. **Corroborated.**
6. **Vendor benchmarks rank the vendor first.** Always read the method; prefer public corpora (OpenSSF CVE) and independent leaderboards. **Corroborated.**

## 4. Costs / latency / reliability
- AI review tools: priced per developer or per usage; Greptile most expensive per-seat but cheaper per reviewer-hour-saved (practitioner claim). **Corroborated at low-medium confidence.**
- Latency: review comments arrive in minutes on PR open; the binding constraint is human re-review cycles. **Inferred.**

## 5. Human correction burden
- This area *is* correction burden: every AI-generated line must be read by someone qualified. The tax falls on seniors; juniors rubber-stamp. Independent-test prescription: keep the independent verification layer (pre-existing suite, hidden checks, human reviewer) — never let an agent merge on its own "all tests passed." **Corroborated.**

## 6. Where AI genuinely helps vs where it creates rework
- **Genuinely helps:** catching cross-file bugs humans miss in large diffs; summarizing PRs for triage; adversarial agent-review loops on well-specified work; finding real bugs in tests (the one tool that opened the test file).
- **Creates rework:** noisy comments that train developers to ignore the reviewer; self-certified merges; bigger PRs that cost more review time than the generation saved.

## 7. Boundary notes (A vs B vs C)
- **Domain A:** AI reviewing *your* code during *your* build process. **Domain B:** a shipped product feature like "AI code review" sold as a SaaS (CodeRabbit-the-product is B; your team using it is A). **Domain C:** n/a mostly — though "AI reviewing business documents" would be C. Keep product-vs-process explicit.

## Evidence register (this file)
| # | Claim | URL | Source type | Author/org | Pub date | Confidence | Class |
|---|---|---|---|---|---|---|---|
| 6.1 | Independent leaderboard: F1/precision/recall per tool; Greptile highest precision | https://dev.to/tessainsley/a-code-review-benchmark-that-isnt-the-vendor-ranking-itself-4jp6 | Analysis | tessainsley (dev.to) | Sep 2026 | Medium–High | corroborating |
| 6.2 | Vendor benchmarks disagree; method > headline | https://dev.to/tessainsley/two-ai-code-review-benchmarks-disagree-on-the-winner-and-agree-on-what-to-measure-55kl | Analysis | tessainsley (dev.to) | Sep 2026 | High | corroborating |
| 6.3 | Same-PR head-to-head: 8/7/6/6 of 13; only Codzee opened tests | https://dev.to/codzee_io/we-tested-4-ai-code-review-tools-on-the-same-pr-and-the-results-were-surprising-4l1i | Practitioner test | codzee_io | Oct 2026 | Medium | first-hand practitioner |
| 6.4 | AI review tax: 2–3x PR size; load on seniors; dashboards miss it | https://www.keypup.io/blog/ai-review-tax-copilot-pull-requests-senior-engineer-overload/ | Practitioner analysis | Keypup | Sep 2026 | Medium | first-hand practitioner |
| 6.5 | 7%→38.5% unreviewed AI changes; PR p75 126→345 lines | https://www.webpronews.com/ai-coding-agents-win-more-trust-as-human-reviews-fade/ | News on vendor data | WebProNews (Cursor data) | Jun 2026 | Medium (vendor-supplied) | secondary interpretation |
| 6.6 | Agents' self-written tests barely help; weak-assertion rates | https://startupfortune.com/study-finds-ai-coding-agents-barely-benefit-from-writing-their-own-tests/ | News on study | StartupFortune | Oct 2026 | Medium | secondary interpretation |
| 6.7 | Debugging: Copilot weak at prod debugging; Claude Code multi-file strength | https://medium.com/@the_unwritten_algorithm/github-copilot-vs-cursor-vs-claude-code-which-ai-actually-fixes-production-bugs-9485b33131c6 | Practitioner essay | the_unwritten_algorithm | Mar 2026 | Low–Medium | first-hand practitioner |
| 6.8 | 40 production automations review; Claude Code 11-module refactor | https://medium.com/@automate-archit/claude-code-vs-cursor-vs-claude-code-an-honest-review-after-40-production-automations-5f5b248f7a4a | Practitioner review | Archit Mittal | Jun 2026 | Medium | first-hand practitioner |
