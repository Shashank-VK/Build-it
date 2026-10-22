# 15 — Scraping (Crawling / HTML Parse / Dynamic Extraction / Sitemap / Structured Data / PDF / YouTube / Monitoring)

> Part 3 · B-category catalog · Infra-Ops researcher · Read-only (no install/execute — scrapers NOT executed)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved
> Note: Docs inspected via search excerpts only. No target site was fetched, no scraper was run.

Scope: crawling/scraping frameworks, HTML parsing, dynamic (browser) extraction, sitemap discovery, structured-data (JSON-LD/schema), PDF extraction, YouTube metadata, proxy/unblock infra, monitoring/scheduling.

## Index (20 resources)

01 Scrapy · 02 Crawlee · 03 Apify Platform · 04 Firecrawl · 05 Crawl4AI · 06 ScrapeGraphAI · 07 BeautifulSoup4 · 08 lxml · 09 selectolax · 10 Cheerio · 11 Playwright (extraction) · 12 Puppeteer · 13 Selenium · 14 httpx/requests/curl_cffi (fetch layer) · 15 Bright Data / Oxylabs / IPRoyal (proxy exemplar) · 16 Common Crawl · 17 schema.org + JSON-LD · 18 PyMuPDF / pdfplumber (PDF) · 19 yt-dlp / youtube-transcript-api (YouTube) · 20 Uptime-Kuma / Apify Schedules / n8n (monitoring)

---

### 01 — Scrapy (Python crawling framework)
- **Canonical identity:** `pypi:scrapy` — `github:scrapy/scrapy`
- **Category:** Scraping → Crawling framework (static-first)
- **Type:** OSS framework
- **Official URL:** https://scrapy.org/
- **Description:** Mature Python framework (since 2008): spiders, scheduler, dupefilter, auto-throttle, item pipelines, feed exports (JSON/CSV/XML/S3).
- **Contents inspected:** scrapy.org landing excerpts; 2026 Scrapy-vs-Crawlee comparisons.
- **Capabilities:** CSS/XPath selectors, async engine (Twisted+asyncio), middleware/signals, scrapy-redis distribution, scrapy-playwright/splash for JS.
- **Usage domain:** Large-scale static-HTML crawls.
- **Integration:** library (`scrapy startproject` / `scrapy crawl`).
- **Compatibility:** Python 3.9+ (3.14 per 2026 notes); Twisted 26.x.
- **Deps:** lxml, parsel, Twisted; browser via optional plugin.
- **Availability:** PyPI free OSS.
- **Maintenance:** Active (62k stars 2026, 500+ contributors).
- **License:** BSD-3.
- **Security/limits:** No built-in anti-bot; respect robots/ToS/rate limits; do NOT run without permission check.
- **Related:** Crawlee, Zyte, BeautifulSoup.
- **Sources:** scrapy.org; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — Crawlee (Apify; Node.js + Python)
- **Canonical identity:** `npm:crawlee` / `pypi:crawlee` — `github:apify/crawlee`
- **Category:** Scraping → Crawling framework (HTTP + browser unified)
- **Type:** OSS framework (Apache-2.0)
- **Official URL:** https://crawlee.dev/
- **Description:** Successor to Apify SDK; CheerioCrawler / PlaywrightCrawler / PuppeteerCrawler, queues, session pools, proxy rotation, fingerprinting.
- **Contents inspected:** Search-verified matrix (queues, sessions, storage); 23.7k stars 2026.
- **Capabilities:** Persistent queues, session rotation on 403, Dataset/KV store, deploys to Apify Cloud.
- **Usage domain:** Mixed static+dynamic sites, auth flows.
- **Integration:** library; deploys to Apify Actors.
- **Compatibility:** Node 18+; Python 3.9+.
- **Deps:** cheerio/jsdom or playwright/puppeteer per crawler.
- **Availability:** npm/PyPI free; hosting extra.
- **Maintenance:** Active (Apify team).
- **License:** Apache-2.0.
- **Security/limits:** Fingerprinting ≠ authorization; respect robots/ToS.
- **Related:** Apify, Playwright, Cheerio, Scrapy.
- **Sources:** crawlee.dev; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 03 — Apify Platform (Actors, Store, Proxy, Schedules)
- **Canonical identity:** `service:apify` — https://apify.com/
- **Category:** Scraping → Hosted platform + marketplace
- **Type:** Service (managed) + OSS components
- **Official URL:** https://apify.com/
- **Description:** Serverless Actor runs, 1500+ ready-made Actors, proxy network, Datasets, Schedules, webhooks, Zapier/Make/n8n.
- **Contents inspected:** Search excerpts (pricing $49–999/mo variants, $5 free credit).
- **Capabilities:** Prebuilt scrapers, scheduling, teams, residential/datacenter proxy.
- **Usage domain:** Results without operating infra.
- **Integration:** service (UI/API/MCP); Crawlee code graduates to Actors.
- **Compatibility:** JS/Python Actors; REST + MCP.
- **Deps:** None (managed).
- **Availability:** SaaS, compute-unit billing.
- **Maintenance:** Active.
- **License:** Proprietary platform; Crawlee OSS.
- **Security/limits:** Verify target ToS, PII handling, retention.
- **Related:** Crawlee, Firecrawl, Bright Data.
- **Sources:** apify.com; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 04 — Firecrawl (URL → Markdown/JSON API)
- **Canonical identity:** `service:firecrawl` — `github:firecrawl/firecrawl`
- **Category:** Scraping → Hosted extraction API (LLM-ready)
- **Type:** Service + OSS core (AGPL-3.0)
- **Official URL:** https://www.firecrawl.dev/
- **Description:** /scrape, /crawl, /map, /search, /extract; JS rendering, banners, anti-bot; MCP server; clean Markdown for RAG.
- **Contents inspected:** Search excerpts (Hobby $16/mo, Scale $333/mo variants).
- **Capabilities:** Markdown for agents, paginated crawl, schema-grounded JSON via managed LLM.
- **Usage domain:** RAG ingestion, agent read-jobs.
- **Integration:** service (REST + MCP); self-host OSS possible (loses Fire-engine/proxy).
- **Compatibility:** HTTP; LangChain/MCP.
- **Deps:** None client-side.
- **Availability:** SaaS + OSS core.
- **Maintenance:** Active.
- **License:** AGPL-3.0 core; commercial Cloud terms.
- **Security/limits:** Stateless (weak for auth flows); /extract can hallucinate — verify deterministic fields; costly at 10M+ pages.
- **Related:** Crawl4AI, ScrapeGraphAI.
- **Sources:** firecrawl.dev; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 05 — Crawl4AI (OSS LLM-ready crawler)
- **Canonical identity:** `pypi:crawl4ai` — `github:unclecode/crawl4ai`
- **Category:** Scraping → AI-pipeline crawler
- **Type:** OSS library (self-hosted)
- **Official URL:** https://docs.crawl4ai.com/
- **Description:** Async crawler returning fit_markdown (boilerplate stripped); adaptive crawling, BFS/DFS/BestFirst, proxy rotation, Playwright JS.
- **Contents inspected:** Search excerpts (150–300 pages/min claim).
- **Capabilities:** Markdown-first output, deep-crawl strategies.
- **Usage domain:** Self-hosted RAG pipelines.
- **Integration:** library (Python asyncio); BYO proxies/LLM.
- **Compatibility:** Python 3.9+; Playwright.
- **Deps:** playwright + user LLM provider.
- **Availability:** PyPI/GitHub free.
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security/limits:** Operator owns politeness, PII redaction.
- **Related:** Firecrawl, ScrapeGraphAI.
- **Sources:** GitHub/docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — ScrapeGraphAI (NL-to-extraction)
- **Canonical identity:** `pypi:scrapegraphai` — `github:ScrapeGraphAI/Scrapegraph-ai`
- **Category:** Scraping → LLM-driven extraction
- **Type:** OSS library
- **Official URL:** https://github.com/ScrapeGraphAI/Scrapegraph-ai
- **Description:** Describe fields in NL; Playwright fetch + BYO LLM (OpenAI/Anthropic/Groq/Gemini/Ollama) maps DOM to JSON.
- **Contents inspected:** Search excerpts (BYO-key model).
- **Capabilities:** Exploration of unfamiliar layouts without selectors.
- **Usage domain:** Long-tail sites.
- **Integration:** library (Python).
- **Compatibility:** Python; Playwright.
- **Deps:** LLM API key (token cost/page).
- **Availability:** Free OSS (+LLM spend).
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Non-deterministic; validate vs schema; fallback for prices/IDs.
- **Related:** Firecrawl /extract, Crawl4AI.
- **Sources:** GitHub via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 07 — BeautifulSoup4 (HTML/XML parser)
- **Canonical identity:** `pypi:beautifulsoup4`
- **Category:** Scraping → HTML parse
- **Type:** OSS library
- **Official URL:** https://pypi.org/project/beautifulsoup4/
- **Description:** Pythonic parse-tree search/traversal atop html.parser/lxml/html5lib; most readable API for messy markup.
- **Contents inspected:** PyPI v4.15.0 excerpt; guides (default lxml backend).
- **Capabilities:** find/select, attribute/regex search, tree modification.
- **Usage domain:** Static pages; rendered-HTML post-processing.
- **Integration:** library (paired with requests/httpx/Playwright HTML); does NOT fetch/render.
- **Compatibility:** Python 3.x.
- **Deps:** Parser backend (lxml recommended).
- **Availability:** PyPI free.
- **Maintenance:** Active (4.15).
- **License:** MIT.
- **Security/limits:** Parser only; harden XML parsing on untrusted docs.
- **Related:** lxml, selectolax, Cheerio.
- **Sources:** PyPI; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 08 — lxml (fast HTML/XML + XPath)
- **Canonical identity:** `pypi:lxml`
- **Category:** Scraping → Parse (speed + XPath)
- **Type:** OSS library
- **Official URL:** https://lxml.de/
- **Description:** C-speed parsing; full XPath for structural queries CSS cannot express.
- **Contents inspected:** Search excerpts (recommended BS4 backend).
- **Capabilities:** HTML/XML parse, XPath 1.0, XSLT.
- **Usage domain:** High-throughput parse.
- **Integration:** library (direct or BS4 backend).
- **Compatibility:** Python; wheels provided.
- **Deps:** libxml2/libxslt (wheeled).
- **Availability:** PyPI free.
- **Maintenance:** Active.
- **License:** BSD.
- **Security/limits:** Disable network/DTD expansion on untrusted XML.
- **Related:** selectolax, BeautifulSoup.
- **Sources:** lxml.de via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — selectolax (throughput parser)
- **Canonical identity:** `pypi:selectolax`
- **Category:** Scraping → Parse (throughput specialist)
- **Type:** OSS library
- **Official URL:** https://github.com/rushter/selectolax
- **Description:** Fast C parser; CSS-only, no XPath; wins when parse is profiled bottleneck (millions of docs).
- **Contents inspected:** Search excerpts (CSS-only trade-off).
- **Capabilities:** Fast traversal on large corpora.
- **Usage domain:** Bulk re-parse of snapshots/WARC.
- **Integration:** library.
- **Compatibility:** Python.
- **Deps:** Bundled C parser.
- **Availability:** PyPI free.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Use only after profiling.
- **Related:** lxml, BeautifulSoup.
- **Sources:** GitHub via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — Cheerio (Node HTML parsing)
- **Canonical identity:** `npm:cheerio`
- **Category:** Scraping → HTML parse (JS)
- **Type:** OSS library
- **Official URL:** https://cheerio.js.org/
- **Description:** Fast jQuery-subset for server HTML/XML; load markup, query, traverse without browser cost.
- **Contents inspected:** cheerio.js.org landing excerpts.
- **Capabilities:** Selector extraction, manipulation, rendering.
- **Usage domain:** Node parsing of fetched HTML, sitemaps, SEO fields.
- **Integration:** library (HTML in → data out); does NOT fetch/render.
- **Compatibility:** Node 16+; ESM/CJS.
- **Deps:** htmlparser2/parse5 family.
- **Availability:** npm free.
- **Maintenance:** Active (v1.x).
- **License:** MIT.
- **Security/limits:** Finds nothing if data needs JS — escalate hard pages only.
- **Related:** BeautifulSoup, Crawlee CheerioCrawler.
- **Sources:** cheerio.js.org; WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 11 — Playwright (dynamic extraction)
- **Canonical identity:** `npm:playwright` / `pypi:playwright` — `github:microsoft/playwright`
- **Category:** Scraping → Dynamic extraction (browser)
- **Type:** OSS framework (Microsoft)
- **Official URL:** https://playwright.dev/
- **Description:** Chromium/Firefox/WebKit (TS/Python/.NET/Java); auto-wait, contexts, interception, emulation; ~90k stars 2026.
- **Contents inspected:** Search excerpts (2–10s/page, 10–50x cost vs HTTP).
- **Capabilities:** Login/scroll/click, cookies, network capture, page.content() bridge.
- **Usage domain:** SPA content existing only after JS; auth flows.
- **Integration:** library; Crawlee/Crawl4AI backend.
- **Compatibility:** Multi-language; `playwright install` browsers.
- **Deps:** Browser binaries; user proxies.
- **Availability:** Free OSS (+infra).
- **Maintenance:** Active (v1.5x).
- **License:** Apache-2.0.
- **Security/limits:** Check Network/API first; manage concurrency/timeouts.
- **Related:** Puppeteer, Selenium, Crawlee.
- **Sources:** playwright.dev via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 12 — Puppeteer (Chrome-first automation)
- **Canonical identity:** `npm:puppeteer` — `github:puppeteer/puppeteer`
- **Category:** Scraping → Dynamic extraction (Chromium-first)
- **Type:** OSS library
- **Official URL:** https://pptr.dev/
- **Description:** High-level Chrome/Firefox control via DevTools/WebDriver BiDi; headless default; screenshots/PDFs.
- **Contents inspected:** GitHub README (puppeteer vs puppeteer-core).
- **Capabilities:** Navigation, evaluation, PDFs/screenshots.
- **Usage domain:** Chromium-centric jobs, visual checks.
- **Integration:** library (Node-first).
- **Compatibility:** Node 18+; Chrome download (or -core BYO).
- **Deps:** Chrome binary.
- **Availability:** npm free.
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security/limits:** Heavier than Cheerio; operator owns infra/anti-bot.
- **Related:** Playwright, Cheerio.
- **Sources:** GitHub; WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 13 — Selenium (legacy browser automation)
- **Canonical identity:** `pypi:selenium` / `npm:selenium-webdriver`
- **Category:** Scraping → Dynamic extraction (legacy/compat)
- **Type:** OSS framework (W3C WebDriver)
- **Official URL:** https://www.selenium.dev/
- **Description:** Multi-language WebDriver; Grid for scale; 34k stars; for existing suites or exotic driver needs.
- **Contents inspected:** Search excerpts (slower than Playwright).
- **Capabilities:** Cross-browser sessions, Grid parallelism.
- **Usage domain:** Legacy suites.
- **Integration:** library + Grid.
- **Compatibility:** All major languages.
- **Deps:** Drivers + Grid.
- **Availability:** Free OSS.
- **Maintenance:** Active but Hold for new scraping.
- **License:** Apache-2.0.
- **Security/limits:** Flaky waits; audit Grid exposure.
- **Related:** Playwright, Puppeteer.
- **Sources:** selenium.dev via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — httpx / requests / curl_cffi (fetch layer)
- **Canonical identity:** `pypi:httpx` + `pypi:requests` + `pypi:curl_cffi`
- **Category:** Scraping → Fetch (HTTP clients)
- **Type:** OSS utilities
- **Official URL:** https://www.python-httpx.org/
- **Description:** requests for throwaway scripts; httpx adds async+HTTP/2; curl_cffi impersonates browser TLS/JA3 past 403-before-headers blocks.
- **Contents inspected:** 2026 failure-matched guide.
- **Capabilities:** Async fan-out, HTTP/2, TLS impersonation, direct JSON-API calls.
- **Usage domain:** Front-end for BS4/lxml; API fast path.
- **Integration:** library (fetch string → parser).
- **Compatibility:** Python 3.8+.
- **Deps:** httpcore/certifi; curl-impersonate.
- **Availability:** PyPI free.
- **Maintenance:** Active.
- **License:** BSD/MIT variants.
- **Security/limits:** Spoofing ≠ authorization; verify API ToS.
- **Related:** Scrapy, Playwright.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — Proxy / unblock exemplar (Bright Data · Oxylabs · IPRoyal · Zyte)
- **Canonical identity:** `service:proxy-exemplar`
- **Category:** Scraping → Network / anti-block infra
- **Type:** Service
- **Official URL:** https://brightdata.com/
- **Description:** Residential/datacenter rotation, Web Unlocker; APIs (ScraperAPI/ScrapingBee/ZenRows/Scrape.do) wrap render+proxy.
- **Contents inspected:** Search excerpts ($300–1k/mo Bright Data; $29/mo Scrape.do hobby).
- **Capabilities:** Rotation, health checks, geo targeting, render APIs.
- **Usage domain:** Bot-protected targets.
- **Integration:** service (proxy URL/API; Crawlee ProxyConfiguration).
- **Compatibility:** HTTP(S) proxy.
- **Deps:** Paid quota.
- **Availability:** Commercial SaaS.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** WARNING — proxies do not legalize ToS-violating collection; legal review required.
- **Related:** Apify Proxy, Firecrawl Cloud.
- **Sources:** Vendor sites via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — Common Crawl (no-crawl corpus)
- **Canonical identity:** `dataset:common-crawl` — https://commoncrawl.org/
- **Category:** Scraping → Bulk corpus alternative
- **Type:** OSS dataset / utility
- **Official URL:** https://commoncrawl.org/
- **Description:** Monthly petabyte WARC/WAT/WET on AWS Open Data; index API/Athena; avoids re-crawling for research/LLM.
- **Contents inspected:** Search-verified identity.
- **Capabilities:** Bulk HTML/metadata/text without hitting origins.
- **Usage domain:** Research, seed URLs, backfill.
- **Integration:** utility (S3 + cdx API + warcio).
- **Compatibility:** Any S3/Athena client.
- **Deps:** Egress/compute.
- **Availability:** Free dataset (+compute).
- **Maintenance:** Active (monthly).
- **License:** Origin-dependent; metadata CC.
- **Security/limits:** Stale vs live; filter PII downstream.
- **Related:** Sitemaps, Heritrix/Nutch.
- **Sources:** commoncrawl.org via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 17 — schema.org + JSON-LD (structured data)
- **Canonical identity:** `spec:schema-org` — https://schema.org/
- **Category:** Scraping → Structured-data extraction
- **Type:** Open standard + extraction target
- **Official URL:** https://schema.org/
- **Description:** Product/Article/BreadcrumbList vocabularies in ld+json script tags; richest deterministic signal before fragile CSS.
- **Contents inspected:** SEO-scraping guides (extract schema first).
- **Capabilities:** Typed entities; Rich Results/Schema validators.
- **Usage domain:** Prefer-first extraction (prices, ratings, canonicals).
- **Integration:** open-standard (parse script tags; validate).
- **Compatibility:** All opt-in origins.
- **Deps:** None.
- **Availability:** Free spec.
- **Maintenance:** Active.
- **License:** CC-BY-SA / W3C doc license.
- **Security/limits:** Markup may be stale/spammy — cross-check DOM.
- **Related:** Sitemap/robots, Open Graph.
- **Sources:** schema.org; WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 18 — PDF extraction exemplar (PyMuPDF / pdfplumber)
- **Canonical identity:** `pypi:PyMuPDF` + `pypi:pdfplumber`
- **Category:** Scraping → Document extraction (PDF)
- **Type:** OSS utilities
- **Official URL:** https://pymupdf.readthedocs.io/
- **Description:** PyMuPDF for fast text/layout/images; pdfplumber for table-aware extraction; OCR handoff for scans.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Page text, bbox words, tables.
- **Usage domain:** Crawled PDFs → Markdown/RAG.
- **Integration:** utility (file in → text/tables out).
- **Compatibility:** Python 3.9+.
- **Deps:** MuPDF wheels; pdfminer/Pillow.
- **Availability:** PyPI free.
- **Maintenance:** Active.
- **License:** AGPL-3.0 (PyMuPDF) / MIT (pdfplumber) — note copyleft.
- **Security/limits:** Parse in sandbox; disable JS/launch actions.
- **Related:** Common Crawl PDFs, Crawl4AI.
- **Sources:** ReadTheDocs/GitHub via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — YouTube metadata exemplar (yt-dlp / youtube-transcript-api)
- **Canonical identity:** `tool:yt-dlp` + `pypi:youtube-transcript-api`
- **Category:** Scraping → Video metadata / transcripts
- **Type:** OSS utilities (metadata-only)
- **Official URL:** https://github.com/yt-dlp/yt-dlp
- **Description:** yt-dlp --skip-download --print for titles/descriptions/chapters; transcript-api for caption tracks where permitted; prefer YouTube Data API v3.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Metadata JSON, subtitle fetch, chapter parse.
- **Usage domain:** Cataloging public video metadata (no re-upload).
- **Integration:** utility (CLI/library; prefer official API quota path).
- **Compatibility:** Python/CLI.
- **Deps:** ffmpeg only for media (unneeded for metadata).
- **Availability:** GitHub/PyPI free.
- **Maintenance:** Active.
- **License:** Unlicense / MIT; YouTube ToS + copyright still apply.
- **Security/limits:** WARNING — circumventing DRM / ignoring owner rights violates ToS/law; rights check required.
- **Related:** YouTube Data API v3 (authorized path).
- **Sources:** GitHub via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — Crawl monitoring / scheduling exemplar (Uptime-Kuma · Apify Schedules · n8n)
- **Canonical identity:** `tool:monitoring-exemplar`
- **Category:** Scraping → Monitoring / orchestration
- **Type:** OSS + service mix
- **Official URL:** https://github.com/louislam/uptime-kuma
- **Description:** Uptime-Kuma self-hosted status; Apify Schedules + webhooks for cadence; n8n/Zapier/Make chaining scrape→store→notify.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Cron/schedules, failure alerts, dataset diffing, snapshot persistence for selector-drift debug.
- **Usage domain:** Selector-drift + rendering-failure monitoring.
- **Integration:** utility/service (webhooks, cron).
- **Compatibility:** Docker/self-host or SaaS.
- **Deps:** None / managed.
- **Availability:** OSS + SaaS.
- **Maintenance:** Active.
- **License:** MIT (Kuma) / proprietary (schedulers).
- **Security/limits:** Persist HTML snapshots without PII; alert on 403-rate spikes.
- **Related:** Apify, Firecrawl.
- **Sources:** GitHub/docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

## Cross-cutting warnings
- Do NOT execute scrapers in this research environment (read-only). All capability claims are docs-based.
- Hybrid stack rule (2026 consensus): try direct HTTP + Cheerio/BS4 first → check JSON API in Network tab → escalate only hard pages to Playwright/Crawlee-browser → persist snapshots → monitor selector drift separately.
- Cost rule: browser pages cost 10–50x HTTP pages; Firecrawl/Apify credits beat self-host only under ~100k pages/mo or without DevOps capacity.
- Count: 20 resources.
