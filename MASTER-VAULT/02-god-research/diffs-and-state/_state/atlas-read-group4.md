# Atlas Read Group 4 — Full Line-by-Line Read (8 files, paginated to EOF)

**Base:** `/mnt/c/Users/Shashank Karamudi/Desktop/God research/atlas/`
**Date read:** 2026-10-10 verification dates inside files; read 2026-10-09 UTC
**Mode:** Read-only, no execution. Every line paginated to EOF via Read offset/limit.
**Output:** `/mnt/c/Users/Shashank Karamudi/Desktop/God research/_state/atlas-read-group4.md`

---

## 1. catalogs/05b-context.md — 1380 lines total

**Read ranges:** 1–564, 565–1308, 1309–1380 (EOF confirmed: "End of file - total 1380 lines").

**Counts (per file Coverage note lines 1370–1380):**
- 58 full records — A: 29 (A1–A29), B: 18 (B1–B18), C: 11 (C1–C11)
- A = Context/Memory (memory frameworks, vector DBs, embeddings, RAG, benchmarks, compression)
- B = Repository Intelligence (indexing, AST, code graphs, search, repo-map/packaging)
- C = Documentation Grounding (live docs, versioned/API docs, llms.txt, MCP docs, generation)

**Verification / discrepancy entries (record-by-record as read):**
- Verified High (primary README read 2026-10-10, 3 records only):
  - A1 Mem0 `mem0ai/mem0` — 66,891★, 2,671 commits, 416 releases, Apache-2.0
  - A2 Zep/Graphiti `getzep/graphiti` — 31,590★, 1,011 commits, 200 releases, Apache-2.0; Zep Community Edition deprecated Apr 2025
  - B1 Serena `oraios/serena` — 30,125★, **GPL-3.0-or-later (Corrected vs secondary MIT claims)**
- Archived (2): B16 Bloop `BloopAI/bloop` (archived Jan 2025, Apache-2.0 readable); B17 Sourcetrail `CoatiSoftware/Sourcetrail` (archived 2021, was GPL)
- Historical (1): B3 Sourcegraph Cody (embeddings dropped Feb 2024 for BM25+code-graph; Cody Free/Pro closed Jun–Jul 2025; repos archived)
- Partially verified remainder (Medium unless noted):
  - A3 Letta (Medium), A4 LangMem (Medium, 1.4–1.6k★), A5 Cognee (Medium, 16–17k★), A6 Hindsight (Low), A7 A-Mem (Low, 2.6k★), A8 Qdrant, A9 Weaviate (BSD-3), A10 Chroma, A11 LanceDB, A12 pgvector, A13 Milvus, A14 Pinecone (proprietary), A15 FAISS (MIT, library not DB), A16 OpenAI Embeddings, A17 Voyage (Low), A18 Cohere Embed (Low), A19 Jina (Low, license varies), A20 open families sbert/BGE/E5/Nomic/mxbai/GTE/Qwen3/NV-Embed, A21 LlamaIndex (MIT, ~44k★), A22 LangChain/LangGraph (MIT), A23 Haystack (Apache-2.0, ~25k★), A24 LoCoMo (locomo10: 10 convos ~600 turns/9k tokens, 1,986 Qs), A25 LongMemEval (500 Qs, ICLR 2025), A26 BEAM (Low, 64.1 @1M / 48.6 @10M vendor-reported), A27 LLMLingua (MIT), A28 RULER (Low), A29 InfiniteBench (Low)
  - B2 ast-grep, B4 Aider repo-map (Apache-2.0), B5 repomix (MIT), B6 gitingest `cyclotruc/gitingest` (Low — **stale canonical in this file; corrected to `coderamp-labs/gitingest` in 06a**), B7 ctags, B8 tree-sitter (MIT), B9 SCIP (Low), B10 Kythe (Low), B11 CodeQL, B12 Joern, B13 Semgrep (LGPL-2.1 Dec 2024 relicense per secondary), B14 OpenGrep (Low, LGPL-2.1), B15 comby (Low), B18 ripgrep (MIT/UNLICENSE, v15.2.0)
  - C1 Mintlify, C2 llms.txt (proposal 2024-09-03, not RFC), C3 DeepWiki (Low, dedup cross-ref), C4 Kapa.ai (Low), C5 Inkeep (Low), C6 DocSearch (Low), C7 Fern (Low), C8 ReadMe (Low), C9 Redocly/Redoc (Low), C10 GitBook (Low), C11 readme-ai `eli64s/readme-ai` (Low)
- Dedup cross-ref only (lines 1362–1364): Graphify-Labs/graphify, Opencode-DCP/opencode-dynamic-context-pruning, tickernelz/opencode-mem, 0xranx/OpenContext, thedotmack/claude-mem, upstash/context7 (+ arabold/docs-mcp-server, DeepWiki-alts, Docfork, Ref Tools), oc-mnemoria, supamem, Hipocampo, opencode-short-term-memory, MrDoe/OpenCodeRAG, opencode-skillful, cortexkit/magic-context, g1331/opencode-magic-context, aerovato/magic-compact, kdcokenny/opencode-background-agents, code-yeongyu/oh-my-openagent, [REDACTED-caveman]

**Coverage limits (lines 1374–1380):**
1. Star/maintenance for Partially records from secondary with varying crawl dates — only 3 primary numbers current as of 2026-10-10.
2. Licenses not independently re-verified: universal-ctags, ast-grep, Joern, SCIP, CodeQL terms, Redoc OSS, readme-ai, most embedding weights.
3. Thin: arch-extraction beyond Joern/CodeQL; standalone graph DBs (Neo4j/FalkorDB/Kuzu/Memgraph/Neptune only as backends); stale-doc detection (only via llms.txt/Kapa/Inkeep); embedding benchmarks (MTEB passing mention).
4. 2026 single-source flagged Unresolved/low-confidence.

**Unresolved items in this file:**
- BEAM details — single-source 2026, thin coverage — Unresolved depth (A26)
- RULER v2 — single-source, not independently verified — Unresolved (A28)
- Chroma "Context Rot" discussion — single-source 2026 — Unresolved (A10)
- SCIP maintenance — Sourcegraph archival wave 2025 — Unresolved (B9)
- gitingest canonical outdated here (`cyclotruc` vs `coderamp-labs` correction in 06a)

---

## 2. catalogs/06a-data-acquisition.md — 2322 lines total

**Read ranges:** 1–760, 761–1483, 1484–2243, 2244–2322 (EOF: "End of Part 12 … total 2322 lines").
**Size note:** 160–217KB class; paginated in 4 chunks to EOF as requested.

**Counts (per Coverage note lines 2295–2310):**
- Total 111 (90 full + 21 compact, no duplicates)
- A Web Data Acquisition: 68 full (frameworks 6, parsers 4, browser automation 4, extraction APIs/services 15, LLM readers 6, PDF/document 8, media 2, monitoring 2, metasearch 3, web archives 7, anti-bot 2)
- B Public API Directories: 25 (catalogs/marketplaces 7, curated lists 2, mock APIs 4 full + 10 compact, data portals 4 full + 11 compact)
- C Research/Ingestion: 18 full (codebase ingest 1, fetch MCP 4, deep-research 2, paper sources 4, discussion 2, + A5 cross-refs)

**Verification distribution (90 full records):**
- Verified 13: MarkItDown (`microsoft/markitdown`, MIT), Docling (`docling-project/docling`, MIT, 40k+★ 1.5M/mo), Unstructured (`Unstructured-IO/unstructured`, Apache-2.0, 15,525★), Crawl4AI (`unclecode/crawl4ai`, Apache-2.0, ~63k★), pdfplumber (PyPI 0.11.8), yt-dlp (`yt-dlp/yt-dlp`, Unlicense, 2026.08.19; Historical predecessor youtube-dl superseded), Jina Reader (`jina-ai/reader`, Apache-2.0, ~10.5k★, r.jina.ai/s.jina.ai), Common Crawl (10+PB, CC-MAIN-2026-34, WARC/WAT/WET, CDX+Parquet), changedetection.io (`dgtlmoon/changedetection.io`, Apache-2.0), Gitingest (`coderamp-labs/gitingest`, gitingest.com), GPT Researcher (`assafelovic/gpt-researcher`, MIT), Open Deep Research (`langchain-ai/open_deep_research`, MIT, #6 0.4344 Aug 2025), ai_agents_api_library (`eater2/ai_agents_api_library`, 300+ APIs, JSON/llms.txt/MCP)
- Corrected 4 (inline with Verified): Docling org DS4SD→docling-project/LF AI & Data; changedetection.io upstream dgtlmoon (not 5 forks); Gitingest coderamp-labs ex-cyclotruc + AnEntrypoint/macxwhale fork disambiguation; Zyte formerly Scrapinghub
- Partially verified 66 (majority: Scrapy BSD-3 53k+★, Crawlee Apache-2.0, Botasaurus, MechanicalSoup MIT, BeautifulSoup MIT, Cheerio MIT, Parsel BSD-3, Selectolax MIT, Playwright Apache-2.0, Puppeteer, Selenium, Splash GPL-3.0, Apify, ScrapingBee→Oxylabs Jan 2026, ScraperAPI, Zyte, Bright Data, Oxylabs, Browserbase, ZenRows, Diffbot, SerpApi, Octoparse, Browse AI, Tavily, Exa, Perplexity, Brave Search, MarkItDown already counted, PyMuPDF AGPL-3.0, kreuzberg, Tesseract Apache-2.0, youtube-transcript-api MIT, Huginn MIT, SearXNG AGPL-3.0, Webz.io, Wayback 900B+, ArchiveBox MIT, SingleFile, Heritrix Apache-2.0, Browsertrix (+Historical Conifer), Archive.today, Perma.cc, curl_cffi MIT, Patchright Apache-2.0, RapidAPI, Postman Network, APIs.guru, awesome-free-apis, api_explorer, JSONPlaceholder, ReqRes, DummyJSON, httpbin, Kaggle, HF Datasets, Data.gov CKAN, data.europa.eu, arXiv, Semantic Scholar, Unpaywall, CORE, HN API)
- Unverified 8: Browserless, Crawlbase, Context.dev, DataForSEO, APILayer, publicapis.dev/io, LlamaParse, Reddit API
- Historical 1 standalone + 3 inline: youtube-dl→yt-dlp; Conifer→Browsertrix; Mocky.io gone 2026 (do not depend); ProgrammableWeb retired (details Unresolved)
- Unresolved 2 standalone: Spider-Rust (`spider-rs/spider` unconfirmed — do not cite); Parallel (parallel.ai unconfirmed)

**Discrepancy entries contributed to registers/discrepancies.md:**
- Gitingest canonical coderamp-labs; Docling docling-project; Zyte ex-Scrapinghub; ScrapingBee→Oxylabs Jan 2026; changedetection.io dgtlmoon; ReqRes keyless rejection 2026

**Coverage limits (lines 2311–2316):**
1. Primary depth: ~55 items primary not opened; honestly marked Partially/Unverified.
2. Pricing all 2026 secondary snapshots, not verified vs billing — do not quote as current.
3. Anti-bot lawful documented only; CAPTCHA/credential bypass out of scope.
4. No execution; claims from docs not testing.
5. Copyright: summarized+linked, not quoted at length.

**Unresolved / gaps (B5 lines 1950–1959, C7 lines 2284–2291, + Coverage note):**
- B5: public GraphQL API directory gap; API status/uptime directory gap (Mockbird covers mocks only); APILayer needs primary; publicapis.dev/io needs primary; ProgrammableWeb retirement Unresolved; SDK directories gap; API doc indexes beyond APIs.guru partial gap; sample/mock GraphQL gap
- C7: GitHub REST/GraphQL code-search Unresolved; news APIs (NewsAPI/GDELT) gap — GDELT candidate; video beyond YouTube partial (yt-dlp covers); managed OCR (Azure Doc Intelligence/Content Understanding) Unresolved; readability (mozilla/readability, kepano/defuddle) minor gap; Common Crawl columnar tooling (cc-index-table/Athena) minor gap
- Licenses to verify from files: PyMuPDF AGPL implications, SearXNG, Gitingest
- Pricing re-check if Atlas needs prices

---

## 3. catalogs/06b-quality.md — 2779 lines total

**Read ranges:** 1–565, 566–1219, 1220–1966, 1967–2689, 2690–2779 (EOF: "total 2779 lines").

**Counts (per Coverage Note lines 2733–2760):**
- Total 119 across 34 subcategories
- Part 13 Testing/QA (A1–A20): 75 records R-01–R-75 (incl 6 group, 4 archive/correction-flagged)
- Part 14 Security/Sandboxing/Safety (B1–B14): 44 records S-01–S-44 (incl 12 group, 1 incident compilation, 2 historical/archived)
- Table: A1 7 (R01-07), A2 8 (R08-15), A3 7 (R16-22), A4 5 (R23-27), A5 3 (R28-30), A6 3 (R31-33), A7 6 (R34-39), A8 2 (R40-41), A9 2 (R42-43), A10 6 (R44-49), A11 4 (R50-53), A12 3 (R54-56), A13 2 (R57-58), A14 2 (R59-60), A15 3 (R61-63), A16 2 (R64-65), A17 3 (R66-68), A18 2 (R69-70), A19 3 (R71-73), A20 2 (R74-75); B1 6 (S01-06), B2 3 (S07-09), B3 3 (S10-12), B4 2 (S13-14), B5 4 (S15-18), B6 2 (S19-20), B7 5 (S21-25), B8 4 (S26-29), B9 3 (S30-32), B10 4 (S33-36), B11 3 (S37-39), B12 1 (S40), B13 2 (S41-42), B14 2 (S43-44)

**Verification / discrepancy entries:**
- Verified High: R-03 pytest (9.1.1 2026-06-19 MIT), R-08 Playwright (v1.62.1 Sep 2026, Test Agents v1.56.0), R-15 Playwright Test Agents (planner/generator/healer, JS/TS), R-23 axe-core (MPL-2.0, 4.12.1), R-25 Lighthouse (Apache-2.0, 13.4.1), R-50 tsc (Apache-2.0), R-71 SWE-bench (2,294 issues, swebench.com live), R-75 QA skills (contents read), S-07 Trivy (Apache-2.0 + incident), S-25 (Trivy + CVE-2026-80521 part)
- Corrected: R-24 pa11y **LGPL-3.0-only not MIT**; S-30 mcp-scan → **Snyk Agent Scan** (`snyk/agent-scan`, `uvx snyk-agent-scan`)
- Archived: R-22 Lost Pixel (sunsetting into Figma, 3.22.0 Nov 2024, successor Argos); R-39 Dredd (archived May 2024); R-41 Optic (archived Jan 2026); Locust Cloud closed 2025-12; BackstopJS dormant (6.3.25 Sep 2024)
- Historical: git-secrets stale 2021
- Partially verified bulk (Medium/Low-Medium/Low as labeled): Jest, Vitest (v4.1.6 Mar 2026), unittest, Mocha, JUnit5, RSpec/PHPUnit/xUnit, WebdriverIO, Puppeteer, TestCafe, Cypress (14.x–15.x), Selenium (4.47), Percy (5k shots free, ~$149–199/mo), Applitools (~$399/mo entry), Chromatic (5k snaps free), Argos ($100/mo flat), reg-suit/Loki/Happo, WAVE, Accessibility Insights, BrowserStack (trial only, ~$29/$399), Sauce Labs, LambdaTest/TestMu AI, Appium (3.4.2 May 2026), Maestro (2.5.x Apr 2026), Detox (20.51+), Postman/Newman, Bruno, REST-assured, Karate/Supertest, Schemathesis (4.27.3 Sep 2026), WireMock (v3.13.2)/Prism, Pact (20.4.0), Specmatic/SCC, Testcontainers, Hypothesis (MPL-2.0), k6 (AGPL-3.0, 1.6.1 Feb 2026), Locust (MIT), JMeter, Gatling, Artillery/Vegeta, WebPageTest, mypy, Pyright, ty (pre-1.0), SonarQube (LGPL Community), Semgrep (LGPL-2.1)+Opengrep, ESLint/Ruff/Biome/Oxlint/PMD/Checkov, Codecov/Coveralls, Istanbul/JaCoCo/coverage.py, Diffblue, Mabl, QA Wolf, Testim/Functionize/Qodex, TestRail/Qase/Xray/Zephyr, Allure, CodeRabbit, Greptile/Qodo/Bito, Sourcery/Reviewdog, Checkly, Datadog Synthetics, Multi-SWE-bench, Inspect AI, testland/qa, OSV/osv-scanner, Dependabot, Renovate (AGPL-3.0), Snyk, Socket, npm/pip/cargo-audit, Grype/Syft, Clair/Scout, gitleaks (MIT), trufflehog (AGPL-3.0), detect-secrets, dotenvx, Doppler/Infisical/Vault BUSL/OpenBao/SOPS, ZAP, Burp, Nuclei, sqlmap/Nmap/Metasploit/ffuf/Nikto, AFL++/libFuzzer/Jazzer/Honggfuzz, OSS-Fuzz, Sigstore, SLSA v1.2, Scorecard v5.5.0/in-toto v1.0/TUF, GUAC/CycloneDX/SPDX/deps.dev, Garak, PyRIT (MIT), promptfoo (MIT), Rebuff/Vigil/LLM Guard/Lakera/LlamaGuard/NeMo/Prompt Shields/picklescan, mcpscan, Inspector, gVisor, Firecracker, bwrap/nsjail/Firejail/Kata/Landlock/seccomp, Deno/Wasmtime, E2B, Modal/Vercel Sandbox/Cloudflare Sandbox/Fly Machines/Riza/Val Town, Codespaces/Ona/DevPod/CodeSandbox, devcontainers spec, OPA/Gatekeeper/Conftest, Kyverno/policy-controller/Ratify, restic/kopia, Velero
- Unverified: R-60 Cover-Agent (`Codium-ai/cover-agent` — no search hit captured); R-14 Playwright MCP dedup (see prior catalog)
- Incidents S-25 (lines 2273–2293): (1) Trivy-action hijack 2026-03-19 TeamPCP CVE-2026-33634/GHSA-69fq-xp46-6x23 exfil `scan.aquasecurtiy.org` — safe iff tag 0.35.0 or SHA post-2025-04-09; (2) axios Mar 2026 hijack; (3) LiteLLM PyPI 1.82.7/1.82.8 Mar 2026; (4) Bitwarden CLI Apr 2026; (5) KICS action Mar 2026; (6) CVE-2026-80521 kernel AF_UNIX GC UAF 2026-09-22 container-escape (undermines user-namespace sandboxes). (1)+(6) Verified High/Medium; (2)–(5) Partially (secondary only).

**Coverage limits (lines 2762–2767):**
1. Uneven depth — ~16 batches strong for high-traffic (Playwright, axe-core, tsc, SWE-bench, Trivy); long-tail R-59–R-70, S-23–S-24, S-38–S-39 secondary only, Low confidence.
2. Many official URLs "Not verified" (no guessing; needs README fetch pass).
3. Dedup ~35 cross-ref not re-researched.
4. Fast-moving 2026 events (Gitpod→Ona sunset 2026-10-15; CVE-2026-80521; Trivy) will date quickly.
5. Copyright ≤50 words honored.

**Unresolved (lines 2769–2774):**
- R-60 Cover-Agent needs primary pass
- S-25 incidents 2–5 exact versions/blast radius unconfirmed
- ~30 license fields "widely reported" not inspected — LICENSE sweep warranted
- Dredd/Optic/git-secrets/BackstopJS/Lost Pixel/Locust Cloud correctly flagged; successors noted
- Single-source: BackstopJS dormancy date, LambdaTest/TestMu pricing, pa11y LGPL (credible secondhand via skill LICENSE check)

---

## 4. catalogs/06c-operations.md — 2436 lines total

**Read ranges:** 1–513, 514–1088, 1089–1667, 1668–2285, 2286–2436 (EOF: "total 2436 lines").
**Size note:** Largest file in group; 5 chunks to EOF.

**Counts (per Coverage note lines 2410–2419):**
- Total ~337 (297 full + ~40 rapid-fire compact)
- Part A Build/CI/Cloud/Infra: 190 full across A1–A26 + ~40 rapid-fire
- Part B SEO/Analytics/CMS/Commerce/Ops: 107 full across B1–B18
- A breakdown: A1 VCS 6, A2 pre-commit 7, A3 CI 14, A4 CD/GitOps 7, A5 build 7, A6 containers 8, A7 dev containers 6, A8 IaC 9, A9 cloud CLIs 7, A10 frontend hosting 6, A11 PaaS 10, A12 serverless/edge 10, A13 CDN 5, A14 DBs 12, A15 secrets 9, A16 env 4, A17 deploy/preview 3, A18 release 6, A19 flags 8, A20 observability 8, A21 errors 3, A22 perf 4, A23 AI telemetry 10, A24 cost 6, A25 jobs 9, A26 headless agents 6, rapid-fire 40
- B breakdown: B1 SEO 6, B2 suites 3, B3 analytics 9, B4 product 5, B5 consent 5, B6 experiments 3, B7 headless CMS 11, B8 CMS/blog 4, B9 docs 7, B10 e-commerce 6, B11 payments 5, B12 email 8, B13 comms 6, B14 localization 7, B15 search 5, B16 feedback 4, B17 forms 5, B18 uptime 8

**Verification / discrepancy entries:**
- Verified (primary fetched): pre-commit.com (v4.6.2 MIT), lefthook README (8,890★ 1,272 commits MIT v2.2.1), opentofu.org (MPL-2.0, 3,900+ providers 23,600+ modules, 1.7–1.12.x), workers.cloudflare.com (330+ cities, 100k req/day free), GitHub/GitHub Actions (docs corroboration), Docker, Kubernetes (CNCF de-facto), Git (GPL-2.0), Deno Deploy sunset (RuntimeWire/Appwrite primary-adjacent)
- Partially verified bulk (Medium/Low-Medium/Low): GitLab, Bitbucket, Gitea/Forgejo MIT, Azure DevOps, husky, lint-staged, Husky.Net, pre-commit.ci, commitlint/commitizen, GitLab CI, Jenkins MIT, CircleCI, Buildkite, Azure Pipelines, Bitbucket Pipelines, TeamCity, Drone/Woodpecker, GoCD Apache-2.0, Dagger Apache-2.0, Harness, Semaphore, Travis (Historical), Argo CD/Flux/Rollouts/Helm/Kustomize Apache-2.0, Spinnaker (Historical), Octopus, Bazel/Buck2/Pants/Turborepo MIT/Nx MIT/Gradle-Maven/Moon, Podman/containerd/Buildah-Kaniko/k3s-kind-minikube/OrbStack-Colima-Rancher-Finch/DevPod, Dev Containers, Devbox/devenv/Nix/Coder, Terraform BSL-1.1, Pulumi Apache-2.0, CloudFormation/CDK, SST MIT, Ansible GPL-3.0, Crossplane, Terramate MPL-2.0/Terragrunt MIT, Checkov/Trivy, AWS/gcloud/Azure CLIs, Wrangler, flyctl, Supabase CLI, Vercel CLI, Vercel/Netlify/Pages/GH Pages/Firebase/Amplify, Fly.io/Render/Railway/Heroku/DO App/Coolify Apache-2.0/Dokku MIT/Caprover-Dokploy/Northflank-Qovery-Upsun/Koyeb, Lambda, workerd Apache-2.0, Vercel/Netlify Functions, Deno MIT, Bun MIT, Fastly/Akamai, WinterCG, Cloudflare/Fastly/Akamai/CloudFront/Bunny, Supabase Apache-2.0, Neon AGPLv3 platform, PlanetScale, Turso/libSQL MIT, D1, Convex, Firebase, Atlas SSPL, Upstash, Prisma/Drizzle Apache-2.0, Crunchy Bridge, Vault BSL-1.1, OpenBao MPL-2.0, Doppler, Infisical MIT 25k+★, SOPS MPL-2.0 17k+★, 1Password, cloud secret stores, Pulumi ESC, GH Secrets OIDC, direnv/mise/asdf/Flox, Kamal MIT, Vercel/Netlify previews, Tugboat, semantic-release MIT, release-please Apache-2.0, Changesets MIT, GoReleaser MIT, git-cliff, knope/release-it/cargo-dist, LaunchDarkly, Unleash Apache-2.0, Flagsmith BSD-3, GrowthBook MIT, Statsig (Corrected), OpenFeature/flagd Apache-2.0, ConfigCat, Vercel Flags/Flagship, Datadog, Grafana AGPL-3.0, Prometheus, OTel, New Relic, Honeycomb, Elastic SSPL/Elastic, SigNoz/HyperDX/Better Stack, Sentry BSL, Rollbar/Bugsnag, GlitchTip MIT, Lighthouse, web-vitals, SpeedCurve/Calibre/DebugBear, Vercel Speed Insights, Langfuse MIT core, LangSmith, Helicone Apache-2.0 (maintenance), Braintrust, Phoenix Elastic-2.0, Opik Apache-2.0 20.9k★, Traceloop, Portkey/LiteLLM MIT, promptfoo/DeepEval/Ragas, Lunary, Infracost, Vantage, CloudZero, OpenCost/Kubecost, Komiser MPL-2.0/Custodian, Finout/nOps/CloudFix, Inngest/Trigger.dev Apache-2.0/Temporal MIT/BullMQ MIT/QStash/Restate-DBOS-Hatchet/Airflow-Prefect-Dagster/pg-boss-Graphile/Sidekiq-Celery, Copilot agent, Claude Code CI, Codex cloud, Jules, Devin, Aider Apache-2.0, rapid-fire 40 (act MIT, Earthly MPL-2.0 cloud shut Jul 2025, BuildJet closed Mar 2026 Archived, Renovate, Dependabot, Trunk, just CC0, Tailscale, ngrok/Tunnel, Caddy/Traefik/nginx, Let's Encrypt Verified, ESO, cert-manager, Vagrant/Packer/Consul-Nomad BSL, OpenTofu Registry Verified, Spacelift/env0/Scalr, HCP Terraform, PagerDuty/Opsgenie, incident.io/Rootly, Healthchecks, Cronitor, EventBridge/GCP Scheduler, GH schedule/dispatch, Vercel/Netlify cron, Cloudflare Cron, QStash schedules, Railway/Render cron), B1 GSC/Bing/schema.org/sitemaps-robots-llms.txt/next-sitemap/Screaming Frog, B2 Ahrefs/Semrush/Yoast-RankMath GPL, B3 GA4/Plausible AGPL-3.0/Fathom/Umami MIT/Matomo GPL-3.0/Simple-Pirsch-Rybbit/Cloudflare/MClarity/Vercel, B4 PostHog MIT/Mixpanel/Amplitude/Heap/Pendo, B5 CookieYes (2M+ sites, MCP 2026, SDK OSS)/OneTrust/Cookiebot/Klaro BSD-3/Osano-Complianz GPL, B6 GrowthBook/PostHog/Optimizely-VWO, B7 Sanity/Contentful/Strapi MIT/Payload MIT/Storyblok/Hygraph/Directus BSL-1.1 nuance/Prismic-Dato/Contentstack-Kontent/Keystatic-Tina/BCMS, B8 WordPress GPL-2.0/Ghost MIT/Drupal/Hashnode-DEV-Substack-Medium, B9 Docusaurus MIT/Mintlify/GitBook/Starlight MIT/Nextra-Fumadocs/VitePress-MkDocs-Sphinx/Fern-ReadMe-Scalar MIT core, B10 Shopify-Hydrogen/Medusa MIT/Saleor BSD-3/Woo GPL/BigCommerce/Vendure GPLv3-Spree-Solidus BSD-3, B11 Stripe/Paddle/Lemon Squeezy/PayPal-Braintree-Adyen-Razorpay/Polar, B12 Resend (8M npm)/SendGrid/Mailgun/Postmark/SES/Loops/Brevo-Mailchimp-Kit-Customer.io/Buttondown-Mailtrap-Postal MIT, B13 Intercom→Fin/Salesforce pending/Crisp/Plain/Zendesk-Freshdesk-HelpScout/Discourse GPL-2.0-Discord/1mind, B14 i18next/next-intl/FormatJS/Lingui-Paraglide-Intlayer/Crowdin/Lokalise-Phrase/Tolgee Apache-2.0-Weblate GPL-3.0-Locize, B15 Algolia/Typesense GPL-3.0/Meilisearch MIT/Elastic-OpenSearch/Orama-Pagefind, B16 Canny/Featurebase/Nolt/Frill-Upvoty-Sleekplan-UserVoice, B17 Typeform/Tally/Formspree/Jotform-GForms-Netlify/RHF-Formik MIT, B18 UptimeRobot/Better Stack/Checkly/Pingdom/Kuma MIT/openstatus AGPL-3.0/Statuspage-Instatus/OhDear-StatusCake-Datadog
- Corrected: Statsig (OpenAI Sep 2025 $1.1B → Amplitude May 2026 brand takeover); Intercom rebrand Fin May 2026 + Salesforce Jun 2026 pending
- Archived: Deno Deploy sunsetting ~Apr 2027 (team joined Cloudflare 2026-10-09, runtime 1yr maintenance); BuildJet closed Mar 2026; Travis Historical
- Notable 2026 changes (lines 54–67): Deno→Cloudflare; Langfuse→ClickHouse Jan 2026; Statsig→OpenAI→Amplitude; MkDocs Material maintenance Nov 2025–Nov 2026; Piwik PRO Core sunset Feb 2026; Intercom→Fin/Salesforce; Mixpanel breach Nov 2025 ShinyHunters 28M; Neon→Databricks May 2025; IBM/HashiCorp $6.4B Feb 2025 BSL unchanged Sep 2026; Helicone maintenance; Railway/Koyeb free removed; GH Actions Linux −39% Jan 2026; Earthly cloud Jul 2025; Agentic Workflows preview, Buildkite LLM proxy, TeamCity AI+MCP

**Coverage limits (lines 2429–2433):**
1. Uneven depth — high-signal primary fetched; long-tail secondary Partially.
2. Pricing snapshots per 2026 comparisons, not live-verified.
3. Licenses re-check before legal reliance (Directus, Sentry self-host, Restate/DBOS).
4. No live-browser; account/pricing/features not live-verified.

**Unresolved:**
- Xata (shutdown rumors vs 2026 listings active — conflict)
- Gitpod 2026 direction unclear (see also 06b Gitpod→Ona sunset 2026-10-15 — reconcile at assembly)
- Directus BSL 1.1 reported — verify
- Restate/DBOS license nuances (BSL historically — Unresolved)
- Top-20 pricing live-verify; rapid-fire READMEs; AI skills directories adjacent sweep needed

---

## 5. registers/coverage.md — 37 lines total

**Read:** 1–37 single read (EOF: "total 37 lines"). Complete.

**Counts:**
- Grand totals: 1,210 canonical (1,281 raw, 71 duplicates folded) + Phase 0 base (~200 names)
- Index-wide verification mix: 914 Verified / 141 Partially / 29 Unverified / 8 Historical / 8 Unresolved / 3 Corrected / 3 Archived / 104 Not labeled (no explicit label; see source catalog)
- Workstreams table (#0–15):
  - 0 Phase0 ~200+ names (16 corrections, 10 gaps, 8 open Qs)
  - 1 01a 155 (9V/107P/39U; ES2026 2026-06-30, TS7.0 GA 2026-07-08, WASI 0.3 2026-06-11, Vite8 Mar 2026, tsup→tsdown, Rye→uv, Volta→mise, pnpm10/11, npm11.19)
  - 2 01b 195 (190+5 cross-refs; 10V/175P/4Hist/1Unres +10 sub-items)
  - 3 01c ~240 (3V/~225P/4U/2Unres/1Hist; 5 Corrected: Cal.com+cal.diy, Stytch→Twilio, Lemon Squeezy→Stripe, Payload→Figma, Auth.js→Better Auth; 3 Archived: Atlas App Services EOL 2025-09-30, Optic, Dredd; Astryx gap Unresolved)
  - 4 02a 97+~95 compact (72V/23P/1Corr Polaris/1Unres Supernova/1Arch BackstopJS/1Hist Lost Pixel)
  - 5 02b 29 styles ~60 res (Surrealism 0, Victorian .btn-victorian only; classic-css, NES.css mirror, snes.css, tattoo-studio need re-open)
  - 6 03a ~48 new (11V/~30P/2Unres; 19 official collections)
  - 7 03b 34 (15 named; 8V/9P/2Hist/17U mentions/4Unres; Gemini CLI→agy, Windsurf→Devin Desktop, Kimi CLI alias)
  - 8 04-mcp 82+~30 sub (~14V/~50P/~18 entry; CVE-2025-49596 Inspector v2)
  - 9 05a 57 (26V/24P/2Hist/1Arch/2Unres; AutoGen→AG2/MAF)
  - 10 05b 58 (29+18+11; 3V Mem0/Graphiti/Serena /52P/2Arch Bloop+Sourcetrail/1Hist Cody; Serena GPL correction)
  - 11 06a 111 (90+21 compact; 68/25/18; Docling→docling-project, Gitingest→coderamp-labs, ScrapingBee→Oxylabs Jan2026, ReqRes keyless 2026; 8 Unverified need primary)
  - 12 06b 119 (75+44; pa11y LGPL, mcp-scan→Snyk Agent Scan, Gitpod→Ona Classic sunset 2026-10-15; CVE-2026-33634 2026-03-19; CVE-2026-80521 2026-09-22; R-60 Unverified; S-25 2–5 secondary-only)
  - 13 06c ~337 (297+~40 compact; Deno→Cloudflare Deploy sunset Apr2027; Langfuse→ClickHouse; Statsig→OpenAI→Amplitude; Intercom→Fin Salesforce pending; Railway/Koyeb free removed; Mixpanel Nov2025 breach; Xata, Gitpod, Directus BSL unresolved)
  - 14 watchlist 23 (18V/1Corr/2P/2Unres)
  - 15 prompt-archives 19 (existence 18V/1P; authenticity 6V/3P/9U/1N-A)

**Coverage limits / cross-workstream reconcile (lines 26–37):**
- OpenCode sandbox contradiction (C5) → workstream 12 evidence
- Output-styles gap (C6) → workstream 7
- SDK identity (C7) → workstream 13 (@opencode-ai/sdk vs anomalyco)
- gstack (C8) → workstream 7 vs workstream 6
- vercel/deepsec→vercel-labs/deepsec (C14) → workstream 12 recorded
- Astryx backend equivalent gap → workstream 3
- Designs + backend design skill unresolved → workstreams 6/14
- NotebookLM skill (stefandsl) → workstream 10 cross-ref
- Munder Difflin dedupe (05a harness vs watchlist Part-19 → one canonical at assembly)
- Serena GPL-3.0-or-later override secondary MIT at assembly

**Unresolved in this register:** 8 Unresolved index-wide; 104 Not labeled (see source catalog); per-workstream gaps listed above.

---

## 6. registers/discrepancies.md — 83 lines total

**Read:** 1–83 single read (EOF: "total 83 lines"). Complete.

**Counts:**
- A. Identity corrections 20 rows (lines 9–28): ruvnet/ruflo ex-Claude Flow; emilkowalski/skills; Karim Shoair D4Vinci; AWS Pizza Bot (no PizzaBox); affaan-m/ECC retired name (`ecc@ecc`, `ecc-universal`); vercel-labs/deepsec; stefandsl/notebooklm-skill beyond teng-lin/notebooklm-py; Astryx NO MCP (CLI `--dense` only); Anthropic/claude-fable-5.md subfolder; Gitingest coderamp-labs; Docling docling-project LF AI & Data; Zyte ex-Scrapinghub; ScrapingBee→Oxylabs Jan2026; mcp-scan→Snyk Agent Scan; changedetection.io dgtlmoon; Gemini CLI→agy (2026-06-18); Windsurf→Devin Desktop `.devin/rules/`; Kimi CLI alias MoonshotAI/kimi-code MIT; Gitpod→Ona (OpenAI Jun2026, Classic sunset 2026-10-15); IBM ACP→A2A Aug2025 archived
- B. License discrepancies 8 rows (lines 34–41): Serena MIT→GPL-3.0-or-later (use GPL); pa11y MIT→LGPL-3.0-only; promptograph NOASSERTION vs MIT badge Unresolved; nightwire NOASSERTION vs MIT Unresolved; Astro NOASSERTION vs MIT badge Unresolved; Slate archive single-source Unresolved; Directus BSL 1.1 verify before legal; Xata shutdown vs active conflict Unresolved
- C. 2026 acquisition/status 11 bullets (lines 46–55): Auth.js→Better Auth; Cal.com closed 2026-04-14 MIT fork cal.diy; Stytch→Twilio $104.1M 2025-11-14; Lemon Squeezy→Stripe Managed Payments; Payload→Figma Jun2025; Langfuse→ClickHouse Jan2026; Statsig→OpenAI→Amplitude May2026; Intercom→Fin Salesforce pending Jun2026; Deno→Cloudflare Deploy sunset Apr2027 1yr maintenance; MkDocs maintenance Nov2025 Piwik Core sunset Feb2026 Railway/Koyeb removed; Atlas App Services EOL 2025-09-30 Dredd May2024 Optic Jan2026 BackstopJS dormant Lost Pixel→Figma git-secrets 2021 Locust Cloud 2025 Mocky.io 2026
- D. Security incidents 6 bullets (lines 59–64): CVE-2026-33634/GHSA-69fq-xp46-6x23 2026-03-19 TeamPCP trivy-action 75/76 + v0.69.4 exfil `scan.aquasecurtiy.org` (safe iff 0.35.0 or SHA post-2025-04-09); CVE-2026-80521 2026-09-22 kernel escape; CVE-2025-49596 Inspector v2; axios Mar2026 hijack; Mixpanel Nov2025 28M LiteLLM PyPI Bitwarden CLI KICS (secondary-only); gsd-build/get-shit-done archived Jun2026 DO NOT USE (fork open-gsd/gsd-core)
- E. Contradictions 9 items (lines 68–76): (1) OpenCode sandbox none vs Bubblewrap/gVisor/Firecracker/Seatbelt; (2) Output styles 8 themes vs gap issue #5199; (3) SDK anomalyco vs @opencode-ai/sdk; (4) gstack OpenCode vs Claude-only; (5) Issue #30295 open vs Closed-by-process; (6) Smithery monetization conflict; (7) Astryx backend gap (Convex/Encore/Hasura/Atlas candidates 01c §3.6.11); (8) Surrealism/Victorian 0 resources; (9) Designs + backend design skill unresolved
- F. Dedup 4 bullets (lines 80–83): Munder Difflin 05a vs watchlist (one canonical Part-19); DeepWiki 05b+04-mcp folded; anthropics/skills, cookbooks, public-apis, context7 Phase0+cross-refs folded; 71 duplicates folded (1,281→1,210 preferring highest verification)

**Coverage limits:** Primary-check advised for legal reliance (C); do not re-verify blindly (D); do not silently resolve (E).

**Unresolved:** E 1–9 preserved; B 6 rows (promptograph, nightwire, Astro, Slate, Directus, Xata); C/D secondary-only incidents.

---

## 7. registers/named-watchlist.md — 435 lines total

**Read ranges:** 1–349, 350–435 (EOF: "total 435 lines"). Complete.

**Counts:** 23 items Part 19 / Deliverable C. Totals line 415: **18 Verified · 1 Corrected · 2 Partially · 2 Unresolved · 0 Not found**

**Per-item verification:**
- 1 OpenViking `volcengine/OpenViking` (openviking.ai, AGPL-3.0, viking:// L0/L1/L2, ov CLI Rust+Python, MCP, Web Studio) — Verified
- 2 PizzaBox by AWS → **Pizza Bot** `pizza-bot-app/pizza-bot` (AWS Blog 2026-09-10, Hono+SQLite+Electron, DeepAgents/LangGraph, MCP) — Corrected (no PizzaBox project)
- 3 Scrapling `D4Vinci/Scrapling` by **Karim Shoair** (Krim→Karim, BSD-3, Fetchers+Spider+Playwright+MCP+skill) — Verified
- 4 ChatDev 2.0/devAll `OpenBMB/ChatDev` (v2.0.0 2026-01-07 DevAll zero-code, 1.0 on `chatdev1.0` branch) — Verified
- 5 Munder Difflin `jeffreycayao/munder-difflin` (Electron+React+TS+Pixi+xterm+node-pty, wraps Claude/Codex/OpenCode etc, Trending #1) — Verified
- 6 Taste skill `Leonxlnx/taste-skill` (~94k★ MIT, 10 install names incl `design-taste-frontend`, dials, GSAP, TasteCode companion) + variants sprungundlandung/lamwon + helldeck — Verified
- 7 Frontend design skill → `anthropics/skills` `frontend-design` candidate (mirrors idwong/evolve/test-harness/dotfiles/turbo/yukiteruamano) — Partially verified (canonical file not inspected on canonical tree)
- 8 Backend design skill — 5 candidates (ainnaziha, kv-skills, techneuma Apache-2.0, majiayu000, xsefirosus) — Unresolved (no canonical; anthropics/skills has none)
- 9 public-apis/public-apis (1,400+ 51 cats, Auth/HTTPS/CORS, APILayer sponsor, MIT) — Verified
- 10 Agent Skills agentskills.io + `agentskills/agentskills` (Apache-2.0/CC-BY-4.0, Discovery/Activation/Execution, `npx skills add`, `.well-known/agent-skills/`) — Verified
- 11 Astryx `facebook/astryx` (150+ React19+StyleX, 7 themes, `@astryxdesign/*`, CLI bash `astryx.mjs`, **NO MCP re-confirmed**, MIT beta Jan2026) — Verified
- 12 DeepSec `vercel-labs/deepsec` (org corrected vercel→vercel-labs, TS CLI `deepsec`, scan→matchers→agents→revalidate, Opus4.7/GPT5.5, $1k–$10k warning, Apache-2.0) — Verified
- 13 ECC `affaan-m/ECC` (retired Everything Claude Code, #3330 Oct2026, ~182 skills ~68 commands, plugin `ecc@ecc` npm `ecc-universal`) — Verified
- 14 Ruflo `ruvnet/ruflo` (ex-Claude Flow, Cognitum.One, 100+ agents, MCP 314 tools, `npx ruflo init`, v3.50.0/3.51.0) — Verified
- 15 Claude Cookbooks `anthropics/claude-cookbooks` (org anthropics with s, notebooks/recipes, MIT) — Verified
- 16 Designs — bare name generic, no match — Unresolved
- 17 Firecrawl `firecrawl/firecrawl` (Search/Scrape/Interact/Agent/Crawl/Map/Batch, SDKs 9 langs, MCP, AGPL-3.0) — Verified
- 18 Eve `vercel/eve` (lowercase, filesystem-first durable agent, Workflow/Sandbox/Gateway, `npx eve init/deploy`, Apache-2.0 beta 2026-06-17) — Verified
- 19 Strix → `usestrix/strix` primary (67k★ Apache-2.0, pentest Graph of Agents, Docker, `strix-agent`, skills) + alts strixgov/strix (MIT+Elastic), strixproject/Strix, mythicalsign/strix — Partially verified
- 20 DESIGN.md `google-labs-code/design.md` (YAML frontmatter+Markdown, `lint/diff/export/spec`, Tailwind/DTCG export, alpha) + VoltAgent 73+ + getdesign.md 300+ — Verified
- 21 awesome-claude-skills `ComposioHQ/awesome-claude-skills` (~76k★, skill folders not just links) + similars jculberson/arturayupov/travisvn 5.7k/BehiSecc 4.2k/mingrath + zh-TW/cn mirrors — Verified
- 22 anthropics/skills official (spec/, template/, skill-creator, docx/pdf/pptx/xlsx source-available, plugin marketplace) + knowledge-work-plugins 11 + claude-plugins-official — Verified
- 23 NotebookLM skill `stefandsl/notebooklm-skill` (RoboNuggets, SKILL.md+nlm.py+refresh_auth+INSTALL_PROMPT, on `teng-lin/notebooklm-py` unofficial RPCs) — Verified (distinct beyond library)

**Key corrections (lines 417–424):** PizzaBox→Pizza Bot; Krim→Karim; vercel→vercel-labs; Ruflo successor; ECC retired; Astryx no MCP; notebooklm distinct skill.
**New leads (426–434):** TasteCode, getdesign.md, knowledge-work-plugins, vercel-labs/add-skill, agentskills/agentskills, Microsoft skills repos, Firecrawl onboarding skill, alt taste-skills, alt Strix.

**Coverage limits:** Exact-string search + variants + org/package-registry + README inspection; no guessed repo presented as intended; read-only no install.

**Unresolved:** #8 backend-design (5 distinct, not forks); #16 Designs (candidates canvas-design, taste variants, design-agent-skills, awesome-design-skills, awesome-design-md, hermes-design-md — none tied); Strix alt identification if security-tool wrong.

---

## 8. registers/prompt-archives.md — 440 lines total

**Read ranges:** 1–357, 358–440 (EOF: "total 440 lines"). Complete.

**Counts (per §6–7 lines 400–428):**
- 19 archives/tools: 4 official (R1–R4), 4 large unofficial (R5–R8), 4 alleged-leak (R9–R12), 5 coding-agent repos/registries/tools (R13–R17), 2 eval datasets/tools (R18–R19)
- Existence: 18 Verified, 1 Partially (R4)
- Authenticity: 6 Verified (R1,R2,R3,R18,R19 fully; R4 partially — see line 424 nuance), 3 Partially (R5-mixed Official subfolder official rest alleged, R13 npm-reproduced strongest, R15 tagged methodology), 9 Unverified, 1 N/A (R17 tool; corpus Unverified, license unclear)
- Table lines 402–422 itemized.

**Per-record verification:**
- R1 Anthropic release notes `platform.claude.com/docs/en/release-notes/system-prompts` — Existence Verified, Authenticity Verified (official, partial: behavior core only, no tools/reminders; stale Jul redeploy; Fable5 2026-06-09 Opus4.8 2026-05-28 Opus4.7 2026-04-16 Sonnet4.6 2026-02-17) High
- R2 xAI `xai-org/grok-prompts` — V/V High (10 .j2 files incl grok4 v8, grok3 0330, grok4.1 variants, safety prefixes; HEAD a7c186f 2025-11-17 stale 11mo; AGPL-3.0)
- R3 OpenAI Model Spec (May2024) — V/V High (policy not literal; full spec not re-fetched — Partially doc-level)
- R4 Meta `meta-llama/llama-models` formats + UPDATES.md 2023-08-07 (system slot example only, default removed) — Partially/Partially Medium
- R5 `asgeirtj/system_prompts_leaks` [LEAD] — V/Partially High (493+ line README, recent Haiku5.5/Code Haiku5.5 2026-10-07 ChatGPT Dots 2026-10-05 Muse Spark 1.3 2026-10-04 Grok4.7 2026-10-03 GPT-6.1-Sol 2026-09-29 Sonnet5.5 2026-09-29; taxonomy bare=claude.ai Official=published raw=captures old=superseded; GLM no-prompt documented; Official provenance-clean rest alleged; downstream WaPo May2026 CEPS Jul2026 unverified; CC0-1.0 not confirmed; 51.2k★ Jul 66.7k★ Sep; 10+ forks confusion)
- R6 `elder-plinius/CL4R1T4S` — V/Unverified High (29 dirs, 51,060★ 10,467 forks 206 commits 2025-03-04 AGPL-3.0; upstream source; README directive-style text hygiene warning; mirrors ljbudgie/buyan-kh)
- R7 `x1xhlol/system-prompts-and-models-of-ai-tools` — V/Unverified High (33 dirs+assets, 143,918★ 34,768 forks 519 commits GPL-3.0, Latest Update 12/07/2026, no provenance)
- R8 `jujumilk3/leaked-system-prompts` — V/Unverified High (170 files `<service>_<date>.md` 2022-12–2026-09 incl chatgpt 20221201 bing 20230209 clyde 20230420 claude2.0 20240306 codex-cli 20250527/20250915/20260902 gemini-cli 20250626 cursor2.0 20251029 aider/goose 20260918; policy PR must match format+verifiable source DMCA note; 14,957★ no license; best longitudinal)
- R9 `LouisShark/chatgpt_system_prompt` PromptCraft — V/Unverified High (prompts/ TOC.md idxtool CI, 10,803★ 1,459 forks 1,863 commits MIT, 1.7k+ prompts)
- R10 `moirania/openai-system-prompts` — V/Unverified High (18 files from R6 2026-09-28, SKILL.md+anatomy+evolution, Codex JSON 2.7MB 27,868 lines, 1★ 1 commit 2026-09-27, clearest disclaimer: extractor codenames Sol/Astra/Atlas not official, dates approx)
- R11 `thekishandev/ai-system-prompt` — V/Unverified Medium-High (41★ 10 forks 1 commit 2025-04-04 MIT, "official" marketing unsubstantiated, R7 folder mirror, placeholders)
- R12 `labac-dev/cursor-system-prompts` — V/Unverified Medium (2 files Claude3.7/Gemini2.5Pro + comparison, educational disclaimer, stats/license Unresolved)
- R13 `Piebald-AI/claude-code-system-prompts` — V/Partially High (npm-extraction deterministic, 515 strings v2.1.295 2026-10-08 up from 350 Jun12, Explore862 Plan1066 tokens, 27 tools subagents slash utils reminders, 12,860★ 2,038 forks 660 commits 260 releases 310 tags MIT, ±20 tokens interpolation)
- R14 `dontriskit/awesome-ai-system-prompts` — V/Unverified High (29 dirs incl Manus/AgentLoop Cline/system.ts Bolt/prompts.ts v0 ChatGPT4.5/4o, 6,241★ 912 forks 67 commits MIT, 8 principles guide)
- R15 `eonedgeproject-code/the-brief` — V/Partially High (tags self-extracted/community-leaked/official-disclosure/behavioral-inference + dates + diffs + validator `validate-entries.mjs`, entries fable5 2026-06-09 partial:true grok4.1 2025-11-17 a7c186f, 2★ 2 forks 4 commits CC BY4.0/MIT tools vendor text not relicensed, tiny methodology-over-volume)
- R16 `gitjfmd/prompt-hub` Full-Prompt-Hub — V/Unverified High (1,627 prompts 70+ services +229 Fabric, triple by-service/by-task/by-type, YAML uid/name/source, tools consolidate/validate/search/export, 1★ 1 fork 4 commits MIT, placeholders YOUR_USERNAME unfinished, tertiary)
- R17 `4pixeltechbr/promptograph` — V/N-A High (20,475 prompts 55 repos +6 HF 94M tokens, lab OpenAI7.7k DeepSeek6.8k Anthropic1.8k, 226 skills 37 domains, search/diff/validator 13+6 rules/FastMCP 7 tools/PyPI/Pages, ATTRIBUTIONS tiers R7 142k R5 62k CL4R1T4S 46k Fabric43k L1B3RT4S16k R8 15k R13 12k R9 10k, 2★ 3 forks 20 commits v0.3.x, **license NOASSERTION vs MIT badge Unresolved**)
- R18 `promptfoo/promptfoo` — V/V High (evals+red-team OWASP LLM Top10, 25,844★ 2,452 forks 10,234 commits 430 releases MIT, now part of OpenAI per README Mar2026 agreement)
- R19 `openai/evals` — V/V High (registry YAML+LFS, templates Completion Protocol, 19,579★ 3,112 forks 691 commits, Other NOASSERTION vs MIT disclaimer flagged minor)

**Coverage limits (line 438):** Text-fetch only (R1 tables, R7 inventory not fully enumerated); stars point-in-time; no prompt bodies by design; non-English + HF datasets (R17 cites 6) not investigated; commercial closed excluded.
**More work (line 440):** (a) R1 full dated list; (b) R5 CC0-1.0 confirm; (c) R12 stats; (d) R17 license; (e) HF datasets; (f) Fable5.1/Opus5.5 staleness. Non-blocking.

**Unresolved in this file:** R12 repo stats/license; R17 license; R5 license field; HF datasets gap; R1 staleness check.

---

## Group totals (returned counts)

| File | Lines (EOF) | Key counts |
|---|---|---|
| catalogs/05b-context.md | 1380 | 58 (29+18+11); 3V / 52P / 2Arch / 1Hist |
| catalogs/06a-data-acquisition.md | 2322 | 111 (90 full+21 compact; 68/25/18); 13V +4Corr / 66P / 8U / 1Hist+3 inline / 2 Unres |
| catalogs/06b-quality.md | 2779 | 119 (75R+44S, 34 subcats); ~8V High +2Corr +3Arch/Hist / bulk P / 1U (R-60) |
| catalogs/06c-operations.md | 2436 | ~337 (297 full+~40 rapid-fire; 190+107); V primary 8 groups / bulk P / 2Corr / 2Arch+1Hist / 4 Unres |
| registers/coverage.md | 37 | 1210 canonical (1281 raw 71 folded) +~200 base; 914V/141P/29U/8Hist/8Unres/3Corr/3Arch/104 Not labeled |
| registers/discrepancies.md | 83 | 20 identity Corr +8 license (2 resolved 6 unres) +11 status +6 incidents +9 contradictions +4 dedup |
| registers/named-watchlist.md | 435 | 23 items: 18V / 1Corr / 2P / 2U |
| registers/prompt-archives.md | 440 | 19 items: existence 18V/1P; authenticity 6V/3P/9U/1N-A |
| **Group total** | **8912 lines** | **~8 files, all paginated to EOF, no execution** |

**Cross-file unresolved roll-up (do not silently resolve):**
- 05b: BEAM depth, RULER v2, Chroma Context Rot, SCIP maintenance, gitingest canonical drift
- 06a: Spider-Rust, Parallel, APILayer, publicapis.dev/io, LlamaParse, Reddit terms, ProgrammableWeb details, GraphQL dir / API status / SDK dir / mock-GraphQL / news APIs / managed OCR / readability / CC columnar gaps; licenses PyMuPDF/SearXNG/Gitingest
- 06b: R-60 Cover-Agent, S-25 incidents 2–5, ~30 licenses, BackstopJS single-source, pricing indicative, pa11y secondhand
- 06c: Xata, Gitpod direction (vs 06b Ona sunset — reconcile), Directus BSL, Restate/DBOS, top-20 pricing, rapid-fire READMEs, skills sweep
- coverage: 8 Unresolved + 104 Not labeled + per-workstream gaps
- discrepancies: E1–9 contradictions + B license 6 + C/D secondary-only
- watchlist: backend-design (5 cands), Designs (generic), Strix alts
- prompt-archives: R12 stats, R17 license, R5 license, HF datasets, R1 staleness

*End of group 4 read. All 8 files read every line to EOF.*
