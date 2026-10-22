# Domain A — Area 12: Consolidated Evidence Register

*Every major claim in files 01–10, with per-finding metadata. Accessed 2026-10-10 unless noted.*

## How to read this register
- **Claim label:** Verified / Corroborated / Inferred / Proposed / Unknown
- **Evidence class:** primary technical / first-hand practitioner / corroborating / community observations / secondary interpretation / unverified
- Confidence is the researcher's judgment (High/Medium/Low), not the source's.

## Area 1 — Product research and planning
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 1.1 | Reusable research skill cards (citation rules, 8-round caps, coverage-score reflection) | Corroborated | https://github.com/vinod-donthi/hands-on-llm-engineering/blob/HEAD/week-04/theory/agent-skills-and-harness.md | GitHub curriculum | vinod-donthi | ~Aug 2026 | Medium | corroborating | Consistent with skill patterns in files 02/05/08 |
| 1.2 | Weekend roadmap pipeline (analytics+ticket+RSS → LLM → ranked table → Slack); self-reported 70% planning-time cut | Corroborated (pattern); Unverified (number) | https://medium.com/@ranajawadai/i-built-an-ai-powered-project-roadmap-generator-that-cuts-planning-time-by-70-86ccabbd25b9 | Blog | practitioner | Sep 2026 | Low–Medium | first-hand practitioner | Number is self-reported; no independent measurement found |
| 1.3 | 5-rung evidence ladder: LLM speculation = Rung 1, zero engineering capital | Corroborated | http://dev.to/tarikmostafa/how-enterprise-product-teams-enforce-operational-ai-governance-using-the-5-rung-evidence-ladder-1jm2 | Blog | tarikmostafa | Oct 2026 | Medium | community observations | Governance framing is a proposal; the underlying caution is corroborated |
| 1.4 | 140k-word, 11-track AI research program with decision gates (POC validation, ±20% cost confidence) | Corroborated | https://github.com/peermesh/knowledge-graph-lab/blob/HEAD/docs/research/ai-pipeline/POST-RESEARCH-ROADMAP.md | GitHub docs | peermesh | Nov 2025 | Medium | primary technical | Single-repo evidence |

## Area 2 — Requirements and technical specifications
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 2.1 | PRD Studio: Shape/Audit/Change/Recover; VERIFIED/DECLARED/INFERRED/OPEN/PLANNED evidence states | Corroborated | https://github.com/bboysky/prd-studio | GitHub repo | bboysky | 2026 | Medium | primary technical | No enterprise-adoption evidence found either way |
| 2.2 | 13-stage PRD pipeline; input quality dominates output | Corroborated | https://github.com/krosebrook/flashfusionwebsite/blob/HEAD/docs/PRD_GENERATOR_README.md | GitHub docs | krosebrook | ~Feb 2026 | Medium | primary technical | Consistent with 1.2 (input-quality theme) |
| 2.3 | Agent-enforced PRD rules: clarify-first, no implementation, ≤2000 words | Corroborated | https://github.com/orionth1/ai-orchestrator/blob/HEAD/docs/spec/create-prd.md | GitHub docs | orionth1 | 2026 | Medium | primary technical | Matches discipline pattern in 5.2 |
| 2.4 | 13-file framework (PRD + CLAUDE.md + AGENTS.md + plan + verify scripts), ~15 min for toy project | Corroborated | https://github.com/zc8163623/dualforge-workflow | GitHub repo | zc8163623 | ~Aug 2026 | Medium | primary technical | Example is a TodoApp; scaling to real projects Unknown |
| 2.5 | Role-simulating multi-agent spec chain (analyst→PM→PO→architect→SM→orchestrator) | Corroborated | https://github.com/mazoonfahmi/coacoa | GitHub repo | mazoonfahmi | ~Mar 2026 | Medium | primary technical | Pattern recurs in 8.4 (scrum-team-as-code) |
| 2.6 | "Prompt Requirements Document" living-PRD concept | Proposed | https://medium.com/@takafumi.endo/prompt-requirements-document-prd-a-new-concept-for-the-vibe-coding-era-0fb7bf339400 | Essay | takafumi.endo | ~Apr 2025 | Low | secondary interpretation | Concept piece; adoption Unknown |

## Area 3 — UX research and interface design
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 3.1 | Figma AI GA 24 Jul 2025; actions list; First Draft → agent entry point (May 2026 beta) | Verified | https://merge.rocks/blog/top-ai-design-tools-for-ux-ui-designers-in-2025 | Practitioner blog | Merge Rocks | ~Aug 2026 | High | corroborating | Dated product facts; cross-checkable |
| 3.2 | Paper-first/Figma-second workflow; 45-min exploration example | Corroborated | https://woahtech.com/paper-design-ai-paper-vs-figma-for-ai-assisted-product-design/ | Practitioner blog | Woahtech | Sep 2026 | Medium | first-hand practitioner | Single-team workflow |
| 3.3 | Per-tool limitation table (Uizard/Stitch/Locofy/Maze/Stark/etc.) | Corroborated | https://design-rise.com/top-ai-tools-for-ui-ux-designers-in-2026-from-prototyping-to-user-research/ | Roundup | DesignRise | ~Aug 2026 | Medium | corroborating | Limitations converge across roundups |
| 3.4 | Thesis: efficiency gains real; supervision essential; weak on expression/emotion | Corroborated | https://www.theseus.fi/bitstream/handle/10024/891768/Obanya_Chukwuemeka.pdf | Academic thesis | Obanya | 2025 | Medium–High | primary technical | Academic method; small tool sample |
| 3.5 | Same-prompt 5-tool test: inconsistent interpretation; AI as support | Corroborated | https://medium.com/@khushidoshi09/i-tested-the-5-best-ai-tools-for-ui-design-with-the-same-prompt-e5e1bb93a7a3 | Practitioner test | Khushi Doshi | Feb 2026 | Medium | first-hand practitioner | Single tester |
| 3.6 | Third-party design GPTs: personas are assumptions; a11y ≠ WCAG | Corroborated | https://www.therundown.ai/tools/ui-designer-gpt | Tool assessment | TheRundown.ai | 2026 | Medium | secondary interpretation | Vendor-adjacent assessor |

## Area 4 — Prototyping and frontend generation
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 4.1 | Same-app head-to-head metrics (time/LOC/design/cleanliness) | Corroborated | https://designrevision.com/blog/forge-vs-bolt-vs-lovable-vs-v0-comparison | Practitioner test | DesignRevision | ~Dec 2025 | Medium | first-hand practitioner | Includes "Forge," a less-documented entrant |
| 4.2 | Architecture differences (Bolt=real env; Lovable=Supabase project; v0=components) | Corroborated | https://anuragwagh.com/blog/lovable-vs-bolt-vs-v0-ai-app-builder-comparison | Roundup | Anurag Wagh | ~Jul 2026 | Medium | corroborating | Converges across roundups |
| 4.3 | 40–45% vulnerability rate in generated apps; per-tool insecure defaults; 20–30% security-review budget | Corroborated | https://publorai.com/lovable-vs-bolt-vs-v0/ | Practitioner test | PublorAI | ~Sep 2026 | Medium | first-hand practitioner | Converges with 7.5 (Symbiotic 98% ≥1 vuln) |
| 4.4 | Governed-backend split: generated UI over hand-written trust layer | Corroborated | https://dev.to/supero/ai-app-builders-and-multi-tenant-saas-the-30-you-still-write-yourself-2clg | Practitioner essay | supero | Oct 2026 | Medium | first-hand practitioner | Single-team pattern; plausible general |
| 4.5 | Enterprise limitations (integrations, backend automation, security) | Corroborated | https://blog.tooljet.com/lovable-vs-bolt-vs-v0/ | Vendor-adjacent blog | ToolJet | ~Mar 2026 | Low–Medium | secondary interpretation | Vendor-adjacent; direction converges |
| 4.6 | Export/sync terms per tool; Bolt two-way sync semantics | Verified (as reported) | https://dev.to/supero/ai-app-builders-and-multi-tenant-saas-the-30-you-still-write-yourself-2clg | Practitioner essay | supero | Oct 2026 | Medium | first-hand practitioner | Terms change; verify at source before relying |

## Area 5 — Codebase exploration and implementation
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 5.1 | AGENTS.md precedence table across 7 agents | Verified | https://github.com/hoangnb24/harness-engineering-blog/blob/HEAD/src/pages/blog/coding-agent-context-file-formats.md | Eng blog | hoangnb24 | ~Aug 2026 | High | primary technical | Convention is observable in repos |
| 5.2 | Instruction-file best practices (lean, commands, negatives, grow-from-scars) | Corroborated | https://github.com/theboringhumane/theboringfloor/blob/HEAD/website/content/blog/agents-md-best-practices.md | Eng blog | theboringhumane | ~Sep 2026 | Medium | first-hand practitioner | Converges with 10.1 (Microsoft) |
| 5.3 | Microsoft ISE docs-as-source-code practice | Verified | https://devblogs.microsoft.com/ise/documentation-is-the-new-source-code/ | Vendor eng blog | Microsoft ISE | Sep 2026 | High | primary technical | First-party; practices not outcomes |
| 5.4 | ETH: generic context files worse than none (+20% cost); TDAD: procedural test instructions +63% regressions | Corroborated | https://github.com/olivesz/custos-code/blob/HEAD/docs/research/workarounds_and_vendor_mitigations.md | Research compendium | olivesz | Sep 2026 | Medium | secondary interpretation | Cites studies; primary papers not separately verified |
| 5.5 | Anthropic internal usage (5 parallel sessions, plan mode, shared CLAUDE.md) | Corroborated | https://www.linkedin.com/posts/charlie-hills_this-is-how-anthropic-uses-claude-code-internally-activity-7449758375476834305-UsT5 | Social post | Charlie Hills | ~May 2026 | Low–Medium | community observations | Second-hand summary of creator tips |
| 5.6 | Anthropic case studies (Stripe/Ramp/Rakuten/Wiz metrics) | Corroborated (existence); Unverified (numbers) | https://github.com/tombedor/blog/blob/HEAD/research/coding-agents-have-no-moat/anthropic-stories.md | Compiled research | tombedor | ~Aug 2026 | Low–Medium | secondary interpretation | All vendor-supplied; no independent verification |
| 5.7 | Anthropic AI-native SDLC security (narrow agents; 16%→54% substantive comments) | Corroborated | https://github.com/uygnoey/skills-from-claude-blog/blob/HEAD/2026.07.21_how-anthropic-secures-its-ai-native-software-development-lifecycle/description.en.md | Blog notes | uygnoey | Jul 2026 | Medium | secondary interpretation | Notes on official Anthropic blog |
| 5.8 | SWE-bench Verified / Terminal-Bench snapshots; production metrics (PR acceptance 38–48%) | Corroborated | https://presenc.ai/research/coding-agent-benchmarks-2026 | Benchmark roundup | Presenc | May 2026 | Medium | corroborating | Provider-reported scores; saturating benchmarks |
| 5.9 | METR −19% RCT; Google +21% ns; DORA 2024/2025 flip | Verified (studies exist) | https://dev.to/freelance_inspector/ai-coding-assistants-558-faster-or-19-slower-both-are-right-paa | Analysis | freelance_inspector | Sep 2026 | Medium–High | secondary interpretation | Studies are real; synthesis is the author's |
| 5.10 | Developer failure reports (75% rework, false "done", 249-session audit) | Corroborated | https://github.com/olivesz/custos-code/blob/HEAD/docs/research/developer_voice.md | Issue compilation | olivesz | Sep 2026 | Medium | community observations | Self-selected complaints; direction converges with Transluce |
| 5.11 | Three classic failure modes (amnesia, hallucinated deps, green-test illusion) | Corroborated | https://medium.com/@neerajgrg93/why-90-of-ai-coding-agents-fail-in-real-repos-and-the-3-rules-that-actually-fix-them-4669799f2cc0 | Essay | Neeraj Garg | Sep 2026 | Medium | community observations | Essay; modes converge with issue reports |
| 5.12 | Claude Code Projects relaunch with parallel cloud agents (Sep 17, 2026) | Corroborated | https://www.itechpost.com/articles/237367/20260918/claude-code-projects-gets-major-relaunch-managing-parallel-ai-agents-cloud.htm | News | iTechPost | Sep 2026 | Medium | secondary interpretation | Launch announcement coverage |
| 5.13 | Copilot usage-based credits Jun 1 2026; $60–200/mo budgeting | Verified (trend) | https://spectrumailab.com/blog/ai-coding-tools-pricing-compared-2026 | Pricing analysis | Spectrum AI Labs | Oct 2026 | Medium | corroborating | Pricing changes fast; verify at source |
| 5.14 | Token-economics case study; Microsoft pilot budget anecdote | Proposed / Unverified | https://github.com/quantamixsol/graqle/blob/HEAD/docs/case-study-token-economics.md | Case study | quantamixsol (vendor-adjacent) | Sep 2026 | Low | unverified | "Industry reporting" cited without link |

## Area 6 — Testing, debugging, and code review
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 6.1 | Independent leaderboard F1/P/R per tool; Greptile highest precision (80.3) | Corroborated | https://dev.to/tessainsley/a-code-review-benchmark-that-isnt-the-vendor-ranking-itself-4jp6 | Analysis | tessainsley | Sep 2026 | Medium–High | corroborating | Method published; n=16,017 PRs |
| 6.2 | Vendor benchmarks disagree; method > headline | Verified (pattern) | https://dev.to/tessainsley/two-ai-code-review-benchmarks-disagree-on-the-winner-and-agree-on-what-to-measure-55kl | Analysis | tessainsley | Sep 2026 | High | corroborating | Demonstrated with two worked examples |
| 6.3 | Same-PR head-to-head 8/7/6/6 of 13; only Codzee opened tests | Corroborated | https://dev.to/codzee_io/we-tested-4-ai-code-review-tools-on-the-same-pr-and-the-results-were-surprising-4l1i | Practitioner test | codzee_io | Oct 2026 | Medium | first-hand practitioner | Single PR; author is a vendor (Codzee) — note bias |
| 6.4 | AI review tax: 2–3x PR size; senior-engineer overload; dashboards miss it | Corroborated | https://www.keypup.io/blog/ai-review-tax-copilot-pull-requests-senior-engineer-overload/ | Practitioner analysis | Keypup | Sep 2026 | Medium | first-hand practitioner | Converges with 5.10 and Cursor data |
| 6.5 | 7%→38.5% unreviewed AI changes; PR p75 126→345 lines | Verified (vendor data) | https://www.webpronews.com/ai-coding-agents-win-more-trust-as-human-reviews-fade/ | News | WebProNews (Cursor data) | Jun 2026 | Medium | secondary interpretation | Vendor-supplied; survival ≠ quality (noted by source) |
| 6.6 | Agents' self-written tests barely help; weak-assertion rates | Corroborated | https://startupfortune.com/study-finds-ai-coding-agents-barely-benefit-from-writing-their-own-tests/ | News on study | StartupFortune | Oct 2026 | Medium | secondary interpretation | Study not independently retrieved |
| 6.7 | Debugging tool fit: Copilot weak at prod debugging; Claude Code multi-file strength | Corroborated | https://medium.com/@the_unwritten_algorithm/github-copilot-vs-cursor-vs-claude-code-which-ai-actually-fixes-production-bugs-9485b33131c6 | Practitioner essay | the_unwritten_algorithm | Mar 2026 | Low–Medium | first-hand practitioner | Opinionated essay; single author |
| 6.8 | 40 production automations; 11-module refactor traced by Claude Code | Corroborated | https://medium.com/@automate-archit/claude-code-vs-cursor-vs-claude-code-an-honest-review-after-40-production-automations-5f5b248f7a4a | Practitioner review | Archit Mittal | Jun 2026 | Medium | first-hand practitioner | Script/automation context, not web-app |

## Area 7 — Security and quality assurance
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 7.1 | Veracode 2025: 45% insecure; 2026: 45% again across 150+ models; Java 71.5% | Verified | https://www.scworld.com/news/llms-make-insecure-coding-choices-for-45-of-tasks-study-finds | News on study | SC Media (Veracode) | ~Jul 2025 | High | secondary interpretation | Stable across two years |
| 7.2 | Veracode Spring 2026: 55% secure ceiling; XSS/log-injection weakest | Verified | https://www.secondtalent.com/resources/ai-generated-code-quality-metrics-and-statistics-for-2026/ | Stats roundup | SecondTalent (Veracode data) | Sep 2026 | Medium–High | secondary interpretation | Consistent with 7.1 |
| 7.3 | 6 LLMs vs OWASP: 25.7% vuln rate; Broken Access Control dominant | Corroborated | https://appsecsanta.com/research/ai-code-security-study-2026 | Study | AppSecSanta | ~May 2026 | Medium | primary technical | Lower rate than Veracode — different method/corpus |
| 7.4 | 3,500 artifacts, Z3-verified 55.8% vuln; tools miss 97.8%; gen–review asymmetry | Corroborated | https://arxiv.org/pdf/2604.05292v2 | Paper | Cobalt AI | Apr 2026 | Medium–High | primary technical | Formal method; vendor-authored (Cobalt sells this) |
| 7.5 | 1,967 repos: 4.4x vulns; 1,072 apps: 98% ≥1 vuln, 29% high/critical | Corroborated | https://lifestyle.thepointnews.com/story/825944/ai-assisted-code-introduces-4-4x-more-security-vulnerabilities-than-human-written-code-new-research-finds/ | Press release | Symbiotic Security | Aug 2026 | Medium | first-hand practitioner | Press release; method summarized not published |
| 7.6 | Anthropic in-session security review; narrow agents; risk tiering | Corroborated | https://github.com/uygnoey/skills-from-claude-blog/blob/HEAD/2026.07.21_how-anthropic-secures-its-ai-native-software-development-lifecycle/description.en.md | Blog notes | uygnoey | Jul 2026 | Medium | secondary interpretation | Notes on official blog |
| 7.7 | AI reviewers' blind spots (secrets, deps); 69% orgs / 1-in-5 incident stats | Corroborated (pattern); Unverified (stats) | https://huntaegis.com/article/8b56854efac9c26f729a381061af9c11 | Roundup | HuntAegis | Sep 2026 | Low–Medium | secondary interpretation | Stats unsourced in roundup |
| 7.8 | Verification as infrastructure; semantic-level failures | Corroborated | https://forgeworkflows.com/blog/why-ai-generated-code-fails-in-production | Practitioner essay | ForgeWorkflows | Oct 2026 | Medium | first-hand practitioner | Vendor-adjacent essay |

## Area 8 — CI/CD and deployment
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 8.1 | GitHub Actions agent skill (generate/harden/migrate) | Corroborated | https://github.com/mohammaddaoudfarooqi/agent-engineering-skills/blob/HEAD/skills/github-actions/SKILL.md | Skill repo | mohammaddaoudfarooqi | ~Jul 2026 | Medium | primary technical | Skill pattern converges with 1.1 |
| 8.2 | CI as enforcement layer; identical harness for agent/human code | Corroborated | https://github.com/deors/agent-skills | Skill pack | deors | ~Jul 2026 | Medium | primary technical | Matches Anthropic's test/CI hard gate (5.7) |
| 8.3 | Issue→branch→PR bot; bounded retries; focused-issue limitation | Verified (as documented) | https://github.com/tmseidel/ai-git-bot/blob/HEAD/doc/CODING_AGENT.md | Repo docs | tmseidel | Sep 2026 | Medium–High | primary technical | Limitations stated by the author |
| 8.4 | Scrum-team-as-code with traceability + quality gates | Proposed | https://github.com/flexnetos/ai-coding-factory | Repo | flexnetos | ~Apr 2026 | Low | primary technical | Working repo; no production-adoption evidence |
| 8.5 | AWS CI/CD guidance for serverless AI workloads | Verified | https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/cicd-and-automation.html | Official docs | AWS | 2026 | High | primary technical | Official; prescriptive not descriptive |
| 8.6 | 70–95% enterprise agent pilot failure (Fiddler AI 2026) | Unverified | https://coasty.ai/blog/ai-agent-workflow-automation-patterns-2026-20261003 | Vendor blog | Coasty | Oct 2026 | Low | unverified | Third-hand stat on a vendor blog |

## Area 9 — Monitoring and incident response
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 9.1 | Three layers: correlation vs postmortem vs agentic investigation | Corroborated | https://medium.com/@sms10221/ai-powered-incident-investigation-the-complete-guide-for-sre-teams-2026-d80d59afd2bc | Guide | sms10221 | ~May 2026 | Medium–High | corroborating | Taxonomy is the author's; useful and converging |
| 9.2 | AIOps' three durable jobs; LLM cost argument for plumbing | Corroborated | https://medium.com/@sms10221/ai-sre-vs-aiops-in-2026-definitions-differences-and-how-to-choose-90db1c6041a9 | Analysis | sms10221 | ~May 2026 | Medium | corroborating | Same author as 9.1 — not independent |
| 9.3 | Incident copilot POC: evidence bundle, heuristic baseline, eval harness | Corroborated | https://github.com/adeelarshad414/devops-interns-proj/commit/893b721806437e28d9c0c1171dc92426a54a3198 | GitHub commit | adeelarshad414 | ~Aug 2026 | Medium | primary technical | POC with honest limitations |
| 9.4 | Stateless-LLM failure (bad restart suggestion); memory-graph fix | Corroborated | https://dev.to/pavanamahima/stopping-ai-hallucinations-in-incident-response-with-hindsight-memory-2n30 | First-hand essay | pavanamahima | Sep 2026 | Medium | first-hand practitioner | Single-team incident |
| 9.5 | Least-privilege RBAC, cooldowns, evidentiary grounding | Corroborated | https://aiagentskit.com/blog/ai-agents-for-devops-sre/ | Guide | AIAgentsKit | Oct 2026 | Medium | corroborating | Guidance, not measured outcomes |
| 9.6 | AIOps blockers: data quality, black-box trust, integration, cost | Corroborated | https://devops.com/aiops-for-sre-using-ai-to-reduce-on-call-fatigue-and-improve-reliability/ | Article | DevOps.com | ~Nov 2025 | Medium | secondary interpretation | Converges with 9.7 |
| 9.7 | SRE skepticism: over-hyped but useful; won't replace SREs | Corroborated | https://rootly.com/blog/what-does-aiops-mean-for-sres-it-s-complicated | Vendor blog | Rootly | ~Mar 2026 | Medium | first-hand practitioner | Vendor (Rootly) but skeptical tone |

## Area 10 — Documentation and maintenance
| # | Claim | Label | URL | Source type | Author/org | Pub date | Confidence | Class | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|---|
| 10.1 | Docs-as-source-code; doc drift as CI bug; stale docs worse than none | Verified | https://devblogs.microsoft.com/ise/documentation-is-the-new-source-code/ | Vendor eng blog | Microsoft ISE | Sep 2026 | High | primary technical | First-party practice |
| 10.2 | DoGBench: 45.5% gaps, 36.6% inaccuracies, 6.1% fabrication (n=1,267) | Corroborated | https://www.webpronews.com/ai-agents-struggle-to-write-usable-software-docs/ | News on benchmark | WebProNews | Oct 2026 | Medium | secondary interpretation | Benchmark not independently retrieved |
| 10.3 | AI won't fix docs debt; "fast, plausible, and wrong" | Corroborated | https://sdtimes.com/softwaredev/great-documentation-takes-more-than-ai/ | Trade press | SD Times | ~Mar 2026 | Medium | corroborating | Converges with 10.2 |
| 10.4 | Four silent doc failures (chunking, visuals, examples, JS rendering) | Corroborated | https://medium.com/@buildwithcodeclarity/your-documentation-is-invisible-to-ai-and-its-killing-your-adoption-eb8256ffa73c | Practitioner essay | Code & Clarity | Nov 2025 | Medium | first-hand practitioner | Practical; widely echoed |
| 10.5 | Agents for bug backlogs, legacy tests, codebase explanation | Corroborated | https://www.eweek.com/news/anthropic-claude-code-launch/ | News | eWeek | ~Oct 2025 | Low–Medium | secondary interpretation | Vendor-adjacent claims |

## Cross-cutting negative-evidence summary
- Productivity: METR RCT −19% (experts, familiar repos) vs +21–56% (broader/greenfield) — task mix decides.
- Security: 45–56% insecure generation, stable 2024–2026; 4.4x vuln multiplier in AI-assisted repos.
- Review: agents' self-tests don't gate; 38.5% of AI changes merge unreviewed; review burden concentrates on seniors.
- Cost: $20–200/dev/mo; flat seats → metered tokens (Copilot credits Jun 2026); heavy users $200+/mo.
- Reliability: false "done" in ~1/3 of public agent sessions (Transluce); instruction files are injection not enforcement.
