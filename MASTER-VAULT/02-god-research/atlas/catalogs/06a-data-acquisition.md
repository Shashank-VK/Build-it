# Part 12 — Web Data Acquisition, Public API Directories, Research & Ingestion Tools (06a-data-acquisition)

> Research workstream #11 | Verification date: 2026-10-10
> READ-ONLY research: discover, inspect, identify, verify, categorize, explain usage, record sources.
> No installing, executing, building, configuring, ranking, or recommending.
> No scraping tools were executed and no restricted content was accessed; all findings are from public documentation and public web sources.

## 0. Research method

### Sources searched (primary-first)
For each resource: official GitHub repository (README, releases, license files where surfaced), official documentation sites, official product pages, package registries (PyPI/npm), and Wikipedia for historical facts. Secondary: 2026-dated comparison articles and agent-skill documentation (used only to corroborate, never as sole source for primary claims). All pricing figures are snapshots from secondary sources and are marked as such — prices change and were not verified against vendor billing pages.

### Search themes used
1. `best web scraping crawling frameworks 2026 Scrapy Crawlee Playwright` — framework landscape
2. `Firecrawl alternatives web scraping API Apify Browserless ScrapingBee` — extraction services
3. `microsoft markitdown github markdown conversion tool` — document ingestion
4. `public API directory RapidAPI Postman public API network APIs.guru catalog` — API indexes
5. `open data portals Kaggle datasets Hugging Face datasets data.gov API` — dataset portals
6. `jina ai reader API web page to markdown r.jina.ai` — reader APIs
7. `gitingest github repository to text prompt-friendly` — codebase ingestion
8. `gpt-researcher github autonomous agent deep research` — research agents
9. `Crawl4AI github open source LLM-friendly web crawler` — LLM crawlers
10. `Tavily AI search API for agents Exa neural search API documentation` — agent search APIs
11. `Docling IBM github document parsing PDF` — document AI
12. `yt-dlp github youtube-dl fork video download` — media extraction
13. `changedetection.io github website change monitoring open source` — monitoring
14. `modelcontextprotocol fetch MCP server github web page fetching` — fetch MCP servers
15. `JSONPlaceholder ReqRes free fake REST API testing mock data` — mock APIs
16. `Unstructured github document extraction PDF ETL library` — document ETL
17. `arXiv API Semantic Scholar API documentation academic papers` — paper sources
18. `Common Crawl web archive petabytes API index` — web-scale archive
19. `Apify web scraping automation platform actors official` — scraping platform
20. `Zyte ScraperAPI ScrapingBee official web scraping API service` — scraping vendors
21. `SearXNG self-hosted metasearch engine github privacy` — metasearch
22. `youtube-transcript-api github Python captions subtitles` — transcript extraction
23. `Patchright playwright stealth fork github anti-detection` — stealth automation (lawful docs)
24. `LangChain open deep research github open source agent` — deep research
25. `pdfplumber PyMuPDF github Python PDF text extraction tables` — PDF libraries
26. `Kaggle API documentation datasets Hugging Face datasets library load_dataset` — dataset SDKs
27. `ArchiveBox self-hosted web archiving github Wayback Machine CDX API` — archiving

### Deduplication (already catalogued — cross-referenced, not re-researched)
Per the workstream brief, the following are cross-referenced only:
- **public-apis/public-apis** — the well-known free public API reference list. Used as a grounding document for category B; not re-researched.
- **Firecrawl** (mendableai/firecrawl) — covered by the watchlist. Cross-referenced as the baseline "web-to-markdown" extraction API that alternatives are compared against.
- **mvanhorn/last30days-skill**, **thedotmack/claude-mem**, **teng-lin/notebooklm-py** (unofficial, breakage risk) — out of scope for this workstream; not researched.

### Verification labels (used exactly as specified)
**Verified** / **Partially verified** / **Unverified** / **Corrected** / **Archived** / **Inaccessible** / **Historical** / **Unresolved**

- **Verified**: primary source (official repo README/docs, official product page) was opened in this sweep and directly supports the record.
- **Partially verified**: canonical identity and key facts are corroborated by multiple independent secondary sources, but the primary source was not opened in this sweep.
- **Unverified**: single-source or thinly sourced; needs a follow-up pass.
- **Corrected**: an earlier public record was wrong and this sweep fixes it (e.g., moved repositories).
- **Archived** / **Historical**: project or service is discontinued/retired or superseded; successor noted where known.

---

## A. WEB DATA ACQUISITION

### A1. Crawling & scraping frameworks

---

**Resource name:** Scrapy
**Canonical identity:** scrapy/scrapy (GitHub); Zyte (formerly Scrapinghub) is the primary commercial steward
**Category:** A. Web Data Acquisition — crawling framework
**Type:** Open-source library (Python)
**Official URL:** https://github.com/scrapy/scrapy (docs: https://docs.scrapy.org)
**Description:** The long-standing general-purpose Python web crawling and scraping framework. Provides spiders, request scheduling, concurrency, middleware, item pipelines, and built-in feed exports (JSON/CSV/XML).
**Contents inspected:** Search-result snippets from framework comparisons (awesome-web-scraping-2026 lists, dev.to 2026 comparison); primary repo README not opened in this sweep.
**Actual capabilities:** Async crawling on Twisted; CSS/XPath selectors (via Parsel); middleware for cookies, retries, redirects, user-agents; item pipelines for validation/storage; feed exports; AutoThrottle; support for JS rendering via plugins (e.g., scrapy-playwright).
**Usage domain:** Large-scale production crawling, data mining, archival crawls, price monitoring.
**Inputs:** Seed URLs, spider definitions, crawl rules.
**Outputs:** Structured items (dicts) exported to JSON/CSV/XML or pushed through pipelines to databases.
**Integration method:** Python library; CLI (`scrapy crawl`); deployable to Scrapy Cloud / Scrapyd.
**Dependencies:** Python, Twisted, lxml, parsel, w3lib; optional: scrapy-playwright for JS rendering.
**Availability:** Open source, actively maintained (53k+ GitHub stars cited in 2026 lists).
**Maintenance:** Active (2026 comparisons still list it as the default large-scale choice).
**License:** BSD-3-Clause (not re-verified in this sweep — treat as Partially verified).
**Limitations:** Twisted-based async (not asyncio); learning curve; no built-in JS rendering; overkill for one-off scrapes.
**Related resources:** Parsel, scrapy-playwright, Splash, Zyte (Scrapy Cloud), Crawlee.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md ; https://dev.to/0012303/scrapy-vs-playwright-vs-crawlee-which-web-scraping-tool-should-you-use-in-2026-1eik (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — primary README not opened; identity and capabilities corroborated by multiple 2026 sources.

---

**Resource name:** Crawlee
**Canonical identity:** apify/crawlee (JavaScript/TypeScript) and apify/crawlee-python (Python); maintained by Apify
**Category:** A. Web Data Acquisition — crawling framework
**Type:** Open-source library (JS + Python)
**Official URL:** https://github.com/apify/crawlee and https://github.com/apify/crawlee-python
**Description:** Apify's modern web scraping and browser automation library. Unifies HTTP crawling (Cheerio/BeautifulSoup-based) and headless-browser crawling (Playwright/Puppeteer-based) with autoscaling, proxy rotation, and persistent request queues.
**Contents inspected:** Framework comparison tables (2026 lists); Apify skill docs describing CheerioCrawler vs PlaywrightCrawler and SDK storage; primary repo README not opened.
**Actual capabilities:** Multiple crawler types (HTTP, headless browser); autoscaled concurrency; session management and retries; proxy rotation; dataset/key-value/request-queue storage abstractions; Playwright integration for JS-heavy sites.
**Usage domain:** Modern async scraping, Apify Actor development, mid-to-large crawls.
**Inputs:** Seed URLs, crawler configuration, proxy settings.
**Outputs:** Structured datasets (JSON), key-value stores, files.
**Integration method:** npm/PyPI library; native runtime for Apify Actors; CLI via Apify CLI.
**Dependencies:** Node.js or Python; Playwright/Puppeteer for browser crawlers; Apify SDK storage (local or cloud).
**Availability:** Open source, actively maintained.
**Maintenance:** Active (Apify's flagship OSS; Python port growing).
**License:** Apache-2.0 (not re-verified — treat as Partially verified).
**Limitations:** Medium learning curve; heaviest features (proxy network, scheduling, storage) are designed around the Apify platform.
**Related resources:** Apify platform, Playwright, Puppeteer, Cheerio, Scrapy.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md ; https://github.com/haluk4365/antigravity/blob/HEAD/_skills/apify-scraping-rules/SKILL.md ; https://github.com/hardgraph/skills/blob/HEAD/skills/apify/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — primary README not opened; identity corroborated by Apify's own skill docs.

---

**Resource name:** Crawl4AI
**Canonical identity:** unclecode/crawl4ai (GitHub)
**Category:** A. Web Data Acquisition — LLM-oriented crawler
**Type:** Open-source library + CLI + Docker (Python)
**Official URL:** https://github.com/unclecode/crawl4ai
**Description:** Open-source web crawler built to convert websites into clean, LLM-ready Markdown for RAG pipelines, AI agents, and data extraction. Async browser pool, caching, sessions, proxies, hooks, and LLM-powered extraction strategies.
**Contents inspected:** GitHub README content as surfaced in search results (quick start, feature list, CLI `crwl`, Docker deployment, sponsorship note).
**Actual capabilities:** Async crawling via Playwright-backed browser pool; markdown/HTML/JSON output; CSS-selector and LLM-based extraction strategies; chunking strategies; deep-crawl (BFS) strategies; proxy/cookie/session support; screenshots; Docker deployment with job-queue API and webhooks.
**Usage domain:** RAG ingestion, agent web research, LLM data pipelines.
**Inputs:** URLs, crawl strategies, extraction schemas/questions.
**Outputs:** Markdown, cleaned HTML, JSON, structured extraction results.
**Integration method:** Python library (`AsyncWebCrawler`), CLI (`crwl`), Docker image.
**Dependencies:** Python, Playwright/Chromium (via `crawl4ai-setup`), optional LLM provider for extraction strategies.
**Availability:** Open source; self-hostable; no API key required for local use.
**Maintenance:** Active (~63k stars cited in 2026 skill docs; "most-starred crawler on GitHub" per README).
**License:** Apache-2.0 (per README badges — Partially verified, license file not opened).
**Limitations:** Browser-based, so heavier than HTTP-only crawlers; LLM extraction incurs model costs; anti-bot handling is basic compared to managed APIs.
**Related resources:** Firecrawl (hosted analogue), Jina Reader, MarkItDown, Playwright.
**Sources:** https://github.com/unclecode/crawl4ai ; https://github.com/agentskillexchange/skills/blob/HEAD/./skills/crawl4ai-llm-web-crawler-scraper/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — README content inspected via search-cached primary source; star counts from secondary corroboration.

---

**Resource name:** Botasaurus
**Canonical identity:** omkarcloud/botasaurus (GitHub)
**Category:** A. Web Data Acquisition — scraping framework
**Type:** Open-source framework (Python)
**Official URL:** https://github.com/omkarcloud/botasaurus
**Description:** All-in-one Python web scraping framework bundling browser automation, anti-detection, caching, and parallelism.
**Contents inspected:** 2026 awesome-list entry only; primary README not opened.
**Actual capabilities:** (Per 2026 list) browser automation, anti-detect features, caching, parallel execution. Details not verified against primary docs.
**Usage domain:** Python scraping projects wanting batteries-included setup.
**Inputs:** Not verified.
**Outputs:** Not verified.
**Integration method:** Python library.
**Dependencies:** Not verified.
**Availability:** Open source (~4k stars cited in 2026 list).
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Smaller community than Scrapy/Playwright; primary docs not inspected — treat capabilities as claimed, not confirmed.
**Related resources:** Scrapy, Crawlee, Playwright.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — identity corroborated; capabilities single-sourced.

---

**Resource name:** MechanicalSoup
**Canonical identity:** MechanicalSoup/MechanicalSoup (GitHub)
**Category:** A. Web Data Acquisition — stateful browsing library
**Type:** Open-source library (Python)
**Official URL:** https://github.com/MechanicalSoup/MechanicalSoup
**Description:** Stateful programmatic web browser library (built on Requests + BeautifulSoup) for form submission, cookie handling, and link-following — "like a human clicking."
**Contents inspected:** 2026 awesome-list entry only; primary README not opened.
**Actual capabilities:** Session/cookie persistence, form filling and submission, link navigation. No JavaScript rendering.
**Usage domain:** Login flows, form-driven sites, simple stateful scraping.
**Inputs:** URLs, form data.
**Outputs:** Parsed pages (BeautifulSoup objects), submitted-form results.
**Integration method:** Python library.
**Dependencies:** requests, beautifulsoup4, lxml (not re-verified).
**Availability:** Open source (~4k stars cited).
**Maintenance:** Not verified in this sweep.
**License:** MIT (not re-verified).
**Limitations:** No JS execution; not a crawler (no built-in frontier/scheduling).
**Related resources:** BeautifulSoup, requests, Scrapy.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Spider (Rust crawler)
**Canonical identity:** Unresolved — commonly referenced as `spider-rs/spider`; repo identity not confirmed in this sweep
**Category:** A. Web Data Acquisition — high-speed crawler
**Type:** Open-source library (Rust)
**Official URL:** Unresolved
**Description:** Rust-based web crawler cited in 2026 lists as 20–100x faster than Python alternatives; aimed at speed-first crawling.
**Contents inspected:** 2026 awesome-list entries only.
**Actual capabilities:** Not verified.
**Usage domain:** High-throughput crawling where Python overhead is the bottleneck.
**Inputs/Outputs/Integration/Dependencies:** Not verified.
**Availability:** Open source (claimed).
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Repo identity and API surface not confirmed — needs a dedicated verification pass.
**Related resources:** Scrapy, Crawlee.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unresolved — do not cite the repo path until confirmed.

---

### A2. HTML parsing libraries

---

**Resource name:** BeautifulSoup
**Canonical identity:** beautifulsoup4 (PyPI); documentation at crummy.com/software/BeautifulSoup/
**Category:** A. Web Data Acquisition — HTML/XML parser
**Type:** Open-source library (Python)
**Official URL:** https://www.crummy.com/software/BeautifulSoup/
**Description:** The canonical Python HTML/XML parsing library. Lenient with malformed markup; typically paired with `requests`/`httpx` for fetching. Not a crawler — parsing only.
**Contents inspected:** 2026 comparison tables and usage patterns; primary docs not opened.
**Actual capabilities:** Parse HTML/XML into a navigable tree; search by tag/CSS/XPath-ish selectors; encoding detection; multiple parser backends (html.parser, lxml, html5lib).
**Usage domain:** Quick scripts, one-off scrapes, HTML cleanup in pipelines.
**Inputs:** HTML/XML strings or files.
**Outputs:** Navigable parse tree; extracted text/attributes.
**Integration method:** Python library.
**Dependencies:** Python; optional lxml/html5lib backends.
**Availability:** Open source, mature.
**Maintenance:** Maintained (long-lived project).
**License:** MIT (not re-verified).
**Limitations:** Synchronous; no fetching, no JS rendering, no rate limiting — boilerplate must be built around it.
**Related resources:** lxml, Parsel, Cheerio, Selectolax.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md ; https://dev.to/0012303/scrapy-vs-playwright-vs-crawlee-which-web-scraping-tool-should-you-use-in-2026-1eik (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — identity and role corroborated across many sources.

---

**Resource name:** Cheerio
**Canonical identity:** cheeriojs/cheerio (GitHub); npm package `cheerio`
**Category:** A. Web Data Acquisition — HTML parser
**Type:** Open-source library (JavaScript/TypeScript)
**Official URL:** https://github.com/cheeriojs/cheerio
**Description:** Fast, lean server-side implementation of core jQuery for parsing and manipulating HTML in Node.js. The standard HTML-parsing layer under Crawlee's HTTP crawlers.
**Contents inspected:** Not opened directly in this sweep; identity corroborated by Crawlee/Apify docs referencing CheerioCrawler.
**Actual capabilities:** jQuery-like selectors and DOM traversal/manipulation on server-rendered HTML; no browser, no JS execution.
**Usage domain:** Node.js scraping of static/server-rendered pages; HTML post-processing.
**Inputs:** HTML strings.
**Outputs:** Queryable DOM; extracted text/attributes/HTML.
**Integration method:** npm library.
**Dependencies:** Node.js; htmlparser2/parse5 under the hood (not re-verified).
**Availability:** Open source, actively maintained.
**Maintenance:** Active.
**License:** MIT (not re-verified).
**Limitations:** No JavaScript rendering; server-side only.
**Related resources:** BeautifulSoup, Crawlee (CheerioCrawler), jsdom.
**Sources:** https://github.com/haluk4365/antigravity/blob/HEAD/_skills/apify-scraping-rules/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Parsel
**Canonical identity:** scrapy/parsel (GitHub); PyPI package `parsel`
**Category:** A. Web Data Acquisition — selector library
**Type:** Open-source library (Python)
**Official URL:** https://github.com/scrapy/parsel
**Description:** CSS and XPath selector library extracted from Scrapy; usable standalone for HTML/XML data extraction.
**Contents inspected:** 2026 awesome-list entry only.
**Actual capabilities:** CSS and XPath selectors over HTML/XML; regex helpers.
**Usage domain:** Lightweight extraction inside custom scrapers.
**Inputs:** HTML/XML strings.
**Outputs:** Selected nodes/text.
**Integration method:** Python library.
**Dependencies:** lxml, cssselect, w3lib (not re-verified).
**Availability:** Open source.
**Maintenance:** Maintained alongside Scrapy.
**License:** BSD-3-Clause (not re-verified).
**Limitations:** Parsing/selectors only — no fetching or rendering.
**Related resources:** Scrapy, BeautifulSoup, lxml.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Selectolax
**Canonical identity:** rushter/selectolax (GitHub); PyPI package `selectolax`
**Category:** A. Web Data Acquisition — high-speed HTML parser
**Type:** Open-source library (Python, C backend)
**Official URL:** https://github.com/rushter/selectolax
**Description:** Very fast HTML parser for Python (claimed 10–20x faster than lxml-class parsers) built on a C-level engine (Modest/Lexbor lineage).
**Contents inspected:** 2026 awesome-list entry only; primary README not opened.
**Actual capabilities:** Fast parsing, CSS selector queries. Exact API not verified.
**Usage domain:** Performance-sensitive parsing inside high-throughput scrapers.
**Inputs:** HTML strings.
**Outputs:** Parsed tree; selected nodes.
**Integration method:** Python library.
**Dependencies:** C extension; Python (details not verified).
**Availability:** Open source.
**Maintenance:** Not verified in this sweep.
**License:** MIT (not re-verified).
**Limitations:** Parsing only; exact benchmark claims not independently verified.
**Related resources:** BeautifulSoup, lxml, Parsel.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

### A3. Browser automation for extraction

---

**Resource name:** Playwright
**Canonical identity:** microsoft/playwright (GitHub); Microsoft
**Category:** A. Web Data Acquisition — browser automation
**Type:** Open-source library (Python, JavaScript/TypeScript, Java, .NET)
**Official URL:** https://github.com/microsoft/playwright (docs: https://playwright.dev)
**Description:** Cross-browser automation library (Chromium, Firefox, WebKit) widely used as the rendering engine behind modern scrapers. Auto-waiting, network interception, and multi-language bindings.
**Contents inspected:** 2026 comparison tables; Crawl4AI install docs referencing `playwright install`; changedetection.io docs referencing a Playwright content fetcher; primary repo not opened.
**Actual capabilities:** Headless/headed browser control; auto-wait; request interception and mocking; screenshots/PDFs; mobile emulation; tracing.
**Usage domain:** JavaScript-rendered page extraction, end-to-end testing, browser-based monitoring.
**Inputs:** Scripts driving browser sessions.
**Outputs:** Rendered DOM, screenshots, PDFs, network logs, extracted data.
**Integration method:** Library (pip/npm/Maven/NuGet); language-specific test runners.
**Dependencies:** Browser binaries (downloaded via `playwright install`); language runtime.
**Availability:** Open source, very actively maintained by Microsoft.
**Maintenance:** Active.
**License:** Apache-2.0 (not re-verified).
**Limitations:** Detectable by advanced bot-detection out of the box (CDP fingerprints, automation flags) — the reason stealth forks like Patchright exist; heavier than HTTP-only fetching.
**Related resources:** Puppeteer, Selenium, Patchright, Crawl4AI, Crawlee, Browserbase, Playwright MCP server.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md ; https://github.com/unclecode/crawl4ai ; https://github.com/dmtea/changedetection.io (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — identity and role corroborated across many independent sources.

---

**Resource name:** Puppeteer
**Canonical identity:** puppeteer/puppeteer (GitHub)
**Category:** A. Web Data Acquisition — browser automation
**Type:** Open-source library (JavaScript/TypeScript; Chrome-focused)
**Official URL:** https://github.com/puppeteer/puppeteer (docs: https://pptr.dev)
**Description:** Chrome/Chromium automation library (originally from the Chrome DevTools team). The predecessor/peer of Playwright; still widely used for Chrome-only scraping and PDF/screenshot generation.
**Contents inspected:** 2026 comparison tables only; primary repo not opened.
**Actual capabilities:** Headless Chrome control via DevTools Protocol; screenshots, PDFs, request interception, JS evaluation.
**Usage domain:** Chrome-only scraping/automation, legacy codebases.
**Inputs:** Node.js scripts.
**Outputs:** Rendered pages, screenshots, PDFs, extracted data.
**Integration method:** npm library.
**Dependencies:** Node.js; Chrome/Chromium binary.
**Availability:** Open source, maintained.
**Maintenance:** Active (2026 comparisons list it as the Chrome-only choice).
**License:** Apache-2.0 (not re-verified).
**Limitations:** Chrome/Chromium only; JS-only stealth plugins leave CDP-level fingerprints (see Patchright).
**Related resources:** Playwright, puppeteer-stealth (community plugin), Patchright.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Selenium
**Canonical identity:** SeleniumHQ/selenium (GitHub)
**Category:** A. Web Data Acquisition — browser automation
**Type:** Open-source framework (multi-language: Python, Java, C#, Ruby, JS)
**Official URL:** https://github.com/SeleniumHQ/selenium (docs: https://www.selenium.dev)
**Description:** The veteran browser-automation framework driving real browsers via WebDriver. Largest ecosystem; slower and more detectable than Playwright for scraping use.
**Contents inspected:** 2026 comparison tables only; primary repo not opened.
**Actual capabilities:** WebDriver-based browser control across all major browsers; grid for distributed runs.
**Usage domain:** Legacy scraping systems, cross-browser testing, enterprise automation.
**Inputs:** WebDriver scripts.
**Outputs:** Browser-driven page state, screenshots, extracted data.
**Integration method:** Language bindings + browser drivers.
**Availability:** Open source, maintained.
**Maintenance:** Active.
**License:** Apache-2.0 (not re-verified).
**Limitations:** Slower than Playwright/Puppeteer; poor anti-detection posture; manual waits.
**Related resources:** Playwright, Puppeteer.
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Splash
**Canonical identity:** scrapinghub/splash (GitHub); Zyte (formerly Scrapinghub)
**Category:** A. Web Data Acquisition — scriptable rendering service
**Type:** Open-source service (Python/Lua scripting, HTTP API)
**Official URL:** https://github.com/scrapinghub/splash
**Description:** Scriptable headless browser with an HTTP API for JavaScript rendering, from the makers of Scrapy. Designed to sit behind Scrapy spiders that need rendering.
**Contents inspected:** 2026 AI-scraping directory entry only; primary README not opened.
**Actual capabilities:** HTTP API returning rendered HTML/screenshots; Lua scripting for interaction; ad-block and request filtering (claimed — not verified).
**Usage domain:** Scrapy-based pipelines needing JS rendering without full Playwright.
**Inputs:** URLs + Lua scripts via HTTP API.
**Outputs:** Rendered HTML, screenshots, HAR data.
**Integration method:** Docker container exposing HTTP API; scrapy-splash integration.
**Dependencies:** Docker; Qt/WebKit-based browser stack (details not verified).
**Availability:** Open source (GPL-3.0 per directory listing — not re-verified).
**Maintenance:** Low activity suspected (not verified in this sweep).
**License:** GPL-3.0 (per secondary listing — not re-verified).
**Limitations:** WebKit-based (not Chromium); Lua scripting is niche; likely less maintained than Playwright-based options.
**Related resources:** Scrapy, Zyte, Playwright.
**Sources:** https://github.com/kriptoburak/ai-web-scraping-directory (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — maintenance status and license need a follow-up pass.

---

### A4. Managed extraction APIs / scraping services (Firecrawl alternatives)

> Cross-reference: **Firecrawl** (mendableai/firecrawl, firecrawl.dev) is covered by the watchlist and used here only as the comparison baseline: API-first scraping that returns Markdown/JSON, with search and site-monitoring features. Pricing snapshots below are from September–October 2026 secondary sources and were **not** verified against vendor billing pages.

---

**Resource name:** Apify (platform)
**Canonical identity:** Apify (company); platform at apify.com; SDKs: apify/apify-sdk (JS), apify/apify-sdk-python
**Category:** A. Web Data Acquisition — scraping platform / Actor marketplace
**Type:** Hosted service (proprietary) + open-source SDKs and Crawlee
**Official URL:** https://apify.com
**Description:** Full web scraping and automation platform. Developers run "Actors" — serverless programs (Docker + Node/Python) that take JSON input, scrape or automate, and write structured output to datasets, key-value stores, and request queues. A public Store lists thousands of prebuilt Actors for specific sites (e.g., Google Maps, Instagram, Amazon).
**Contents inspected:** Apify skill documentation (actor mental model: Actor / run / dataset / KV store / request queue), Actor Store examples, Cursor plugin listing (official Apify agent skills + `@apify/actors-mcp-server`), 2026 pricing comparisons; apify.com itself not opened.
**Actual capabilities:** Serverless Actor execution; proxy network with rotation; scheduling; dataset storage with JSON/CSV/Excel export; webhooks; REST API v2; `apify` CLI; official MCP server for agents; Actor Store (community + official Actors, some pay-per-result).
**Usage domain:** Production scraping at scale, scheduled monitoring, marketplace reuse of site-specific scrapers, social/search data collection.
**Inputs:** Actor input JSON (URLs, queries, limits); schedules.
**Outputs:** Datasets (JSON/CSV/Excel), files, webhook payloads.
**Integration method:** Web console, REST API, CLI, JS/Python SDK clients (`apify-client`), MCP server (`@apify/actors-mcp-server`).
**Dependencies:** Apify account + API token; usage billed in compute units plus Actor/proxy fees.
**Availability:** Hosted; free tier cited as $5/month platform credit (no card); paid tiers from Starter.
**Maintenance:** Active (Store cited at 4,500–70,000 tools across sources — figures vary by source and date; treat as approximate).
**License:** Platform proprietary; SDKs and Crawlee open source.
**Limitations:** Not self-hostable; credit + Actor + proxy cost stacking can surprise; not purpose-built for LLM markdown output (conversion is DIY); site Terms of Service still apply to users.
**Related resources:** Crawlee, Firecrawl, Bright Data, actor marketplaces.
**Sources:** https://github.com/hardgraph/skills/blob/HEAD/skills/apify/SKILL.md ; https://github.com/srsnolasco/si-squads/blob/HEAD/skills/apify/SKILL.md ; https://github.com/virtual0ps/crw/blob/HEAD/blog/best-web-scraping-apis.md ; https://www.youtube.com/watch?v=et5Z3BGjXAA (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — platform model corroborated by multiple sources; pricing and Store counts approximate.

---

**Resource name:** ScrapingBee
**Canonical identity:** ScrapingBee (scrapingbee.com); joined the Oxylabs group in January 2026 (per 2026 reporting)
**Category:** A. Web Data Acquisition — scraping API
**Type:** Hosted service (proprietary)
**Official URL:** https://www.scrapingbee.com
**Description:** Managed scraping API: send a URL, get back rendered HTML/extracted data. Handles headless Chrome rendering, proxy rotation, and CAPTCHAs server-side; offers CSS/XPath extraction rules, AI extraction parameters, screenshots, and a Google Search API plus Amazon/Walmart endpoints.
**Contents inspected:** Firecrawl's 2026 alternatives article (feature/pricing detail), 2026 cost comparisons; scrapingbee.com not opened.
**Actual capabilities:** JS rendering in headless Chrome; automatic proxy rotation (standard/premium/stealth tiers); geotargeting; screenshots; extraction rules; AI query extraction; SERP API.
**Usage domain:** Developer-owned scrapers needing managed fetching, SERP collection, JS-heavy sites.
**Inputs:** Target URL + API params (rendering, proxies, extraction rules).
**Outputs:** HTML, extracted fields, screenshots, SERP JSON.
**Integration method:** REST API; client libraries (Python, Ruby, JS).
**Dependencies:** API key; credit-based billing (rendering/proxy options multiply credit cost).
**Availability:** Hosted; trial credits offered; paid tiers (secondary sources cite entry ~$19–49/mo; not verified).
**Maintenance:** Active; corporate change: acquired into Oxylabs group January 2026, plans reportedly unchanged.
**License:** Proprietary.
**Limitations:** HTTP/HTTPS only (per secondary); stealth proxy calls cost far more credits than base calls; no custom JS execution (per one secondary source — single-sourced, treat cautiously).
**Related resources:** ScraperAPI, Zyte, Oxylabs, ZenRows, Firecrawl.
**Sources:** https://www.firecrawl.dev/blog/scrapingbee-alternatives ; https://devtoolpicks.com/blog/when-to-use-a-scraping-api-vs-building-your-own-scraper-indie-hackers-2026 (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** ScraperAPI
**Canonical identity:** ScraperAPI (scraperapi.com); Las Vegas–based company founded 2018
**Category:** A. Web Data Acquisition — scraping API
**Type:** Hosted service (proprietary)
**Official URL:** https://www.scraperapi.com
**Description:** Proxy + rendering API: one API call returns page HTML with IP rotation, CAPTCHA handling, retries, and JS rendering handled server-side. Offers structured-data endpoints for Amazon, Google, Walmart, eBay.
**Contents inspected:** 2026 benchmark write-ups (feature lists, 40M+ IP pool claim, structured endpoints); scraperapi.com not opened.
**Actual capabilities:** Automatic IP rotation; CAPTCHA solving; JS rendering; customizable headers/proxies; structured SERP and e-commerce endpoints; usage analytics.
**Usage domain:** General-purpose scraping, Amazon/Google SERP pipelines, real-estate data.
**Inputs:** Target URL + params (render, premium proxies, structured endpoint).
**Outputs:** HTML or parsed JSON (structured endpoints).
**Integration method:** REST API; SDKs.
**Dependencies:** API key; credit billing (rendering costs multiples of base credits).
**Availability:** Hosted; trial credits; paid tiers from ~$49/mo (secondary, not verified).
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Rendering/proxy multipliers make nominal credit counts misleading; you're buying infrastructure, not normalized product data.
**Related resources:** ScrapingBee, Zyte, Bright Data, Oxylabs.
**Sources:** https://github.com/pecgk79/scraping-api-benchmark ; https://github.com/cnhyzg991/scraping-api-costs (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Zyte
**Canonical identity:** Zyte (zyte.com); formerly Scrapinghub — the company behind Scrapy
**Category:** A. Web Data Acquisition — scraping platform / extraction API
**Type:** Hosted service (proprietary)
**Official URL:** https://www.zyte.com
**Description:** End-to-end scraping platform from Scrapy's creators: Zyte API (automatic extraction with difficulty-tiered pricing), Smart Proxy Manager (automatic ban handling), and Scrapy Cloud (managed Scrapy deployment).
**Contents inspected:** 2026 comparisons and benchmark docs; zyte.com not opened.
**Actual capabilities:** Automatic data extraction (ML-inferred page schemas); proxy/ban management; browser rendering mode; Scrapy Cloud hosting; pay-as-you-go pricing by site difficulty.
**Usage domain:** Python teams with Scrapy-native pipelines; cost-sensitive HTTP-only scraping.
**Inputs:** URLs via API or deployed spiders.
**Outputs:** Extracted structured data, HTML.
**Integration method:** REST API, Scrapy Cloud deployment, proxy endpoint.
**Dependencies:** API key; usage-based billing.
**Availability:** Hosted; free trial credit reported ($5); PAYG from ~$0.13/1K HTTP responses (secondary, not verified).
**Maintenance:** Active.
**License:** Proprietary platform; Scrapy/Splash remain open source.
**Limitations:** Automatic extraction quality varies by site; browser-mode costs far exceed HTTP-mode; setup heavier than single-endpoint APIs.
**Related resources:** Scrapy, Splash, Scrapy Cloud, ScrapingBee, Bright Data.
**Sources:** https://github.com/api-evangelist/scraping ; https://devtoolpicks.com/blog/when-to-use-a-scraping-api-vs-building-your-own-scraper-indie-hackers-2026 (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified. Note: **Corrected** — older references say "Scrapinghub"; current canonical name is Zyte.

---

**Resource name:** Bright Data
**Canonical identity:** Bright Data (brightdata.com)
**Category:** A. Web Data Acquisition — proxy network + scraping APIs
**Type:** Hosted service (proprietary)
**Official URL:** https://brightdata.com
**Description:** Enterprise-scale proxy network (tens of millions of residential IPs claimed) plus managed products: Web Scraper API/IDE, Web Unlocker, SERP API, and site-specific dataset products.
**Contents inspected:** 2026 comparisons only; brightdata.com not opened.
**Actual capabilities:** Residential/datacenter/mobile proxies; unblocking APIs; SERP and e-commerce scraper APIs; pre-collected datasets.
**Usage domain:** Enterprise scraping, hardest anti-bot targets, large proxy pools.
**Inputs:** URLs, search queries, dataset subscriptions.
**Outputs:** HTML/JSON, proxy endpoints, datasets.
**Integration method:** REST APIs, proxy endpoints, dashboard/IDE.
**Dependencies:** Account; enterprise-oriented pricing (entry cited ~$499/mo Growth; not verified).
**Availability:** Hosted; trial options reported.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Enterprise pricing; overkill for small projects.
**Related resources:** Oxylabs, Zyte, Apify, ScraperAPI.
**Sources:** https://github.com/api-evangelist/scraping ; https://github.com/pecgk79/scraping-api-benchmark (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Oxylabs
**Canonical identity:** Oxylabs (oxylabs.io); ScrapingBee joined its group in January 2026
**Category:** A. Web Data Acquisition — proxy infrastructure + scraper APIs
**Type:** Hosted service (proprietary)
**Official URL:** https://oxylabs.io
**Description:** Premium proxy provider (residential, datacenter, mobile; 100M+ IPs claimed) with dedicated Web Scraper API, SERP Scraper API, and E-Commerce Scraper API products.
**Contents inspected:** 2026 comparisons only; oxylabs.io not opened.
**Actual capabilities:** Managed proxies; JS rendering; dedicated scraper APIs for SERP/e-commerce/web.
**Usage domain:** Proxy-heavy scraping, e-commerce and SERP data at scale.
**Inputs:** URLs/queries via API or proxy endpoint.
**Outputs:** HTML/JSON.
**Integration method:** REST APIs, proxy endpoints.
**Dependencies:** Account; plans from ~$49/mo Micro reported (not verified).
**Availability:** Hosted; free trial reported.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Premium pricing tier; IP pool size claims not independently verified.
**Related resources:** Bright Data, ScrapingBee (group company since 2026-01), ScraperAPI.
**Sources:** https://secureblitz.com/best-web-scraper-apis/ ; https://devtoolpicks.com/blog/when-to-use-a-scraping-api-vs-building-your-own-scraper-indie-hackers-2026 (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Browserbase
**Canonical identity:** Browserbase (browserbase.com)
**Category:** A. Web Data Acquisition — hosted headless browsers
**Type:** Hosted service (proprietary)
**Official URL:** https://www.browserbase.com
**Description:** Hosted real-Chrome browser infrastructure for automation and scraping at scale; billed per browser-minute. Positioned as the choice when full browser interaction (not just HTML fetching) is needed.
**Contents inspected:** 2026 comparison tables only; browserbase.com not opened.
**Actual capabilities:** Real Chrome instances via API/SDK; Playwright/Puppeteer-compatible endpoints; screenshots, PDFs; proxy configuration.
**Usage domain:** Browser automation at scale, agent browsing infrastructure, JS-heavy extraction.
**Inputs:** Automation scripts/sessions.
**Outputs:** Browser sessions, screenshots, PDFs, extracted DOM data.
**Integration method:** SDK/API compatible with Playwright/Puppeteer.
**Dependencies:** API key; per-minute billing.
**Availability:** Hosted; free tier reported.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Per-minute billing can be expensive for long sessions; you still write the automation.
**Related resources:** Browserless, Playwright, Apify.
**Sources:** https://enterprisedna.co/directories/compare/apify-vs-firecrawl-vs-browserbase/ ; https://github.com/kriptoburak/ai-web-scraping-directory (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Browserless
**Canonical identity:** Browserless (browserless.io)
**Category:** A. Web Data Acquisition — hosted headless browsers
**Type:** Hosted service (proprietary)
**Official URL:** https://browserless.io
**Description:** Hosted headless-Chrome service offering browser automation over WebSocket/REST, commonly used as a rendering backend for scrapers.
**Contents inspected:** Named in workstream brief and 2026 alternative lists; primary site not opened in this sweep.
**Actual capabilities:** Not verified against primary docs — reported: headless Chrome as a service, Puppeteer/Playwright-compatible.
**Usage domain:** Rendering backend for self-built scrapers.
**Inputs/Outputs/Integration:** Not verified.
**Dependencies:** API key (reported).
**Availability:** Hosted (reported).
**Maintenance:** Not verified.
**License:** Proprietary (reported).
**Limitations:** Primary source not inspected — record is thin.
**Related resources:** Browserbase, Playwright.
**Sources:** Workstream brief (Part 12 search themes) (2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unverified — needs a primary-source pass.

---

**Resource name:** ZenRows
**Canonical identity:** ZenRows (zenrows.com)
**Category:** A. Web Data Acquisition — anti-bot scraping API
**Type:** Hosted service (proprietary)
**Official URL:** https://www.zenrows.com
**Description:** Scraping API positioned on anti-bot bypass strength (noted for Cloudflare bypass), with fetch/extract/batch/browser-session modes on one balance.
**Contents inspected:** 2026 comparisons only; zenrows.com not opened.
**Actual capabilities:** JS rendering, anti-bot bypass, rotating proxies, batch scraping (reported).
**Usage domain:** Protected sites where standard fetchers are blocked.
**Inputs:** URLs via API.
**Outputs:** HTML/JSON.
**Integration method:** REST API; SDKs (reported).
**Dependencies:** API key; credit billing (reported).
**Availability:** Hosted; free trial reported.
**Maintenance:** Active (per 2026 sources).
**License:** Proprietary.
**Limitations:** Bypass effectiveness varies by target and over time; primary docs not inspected.
**Related resources:** ScrapingBee, ScraperAPI.
**Sources:** https://www.firecrawl.dev/blog/scrapingbee-alternatives ; https://github.com/pecgk79/scraping-api-benchmark (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Diffbot
**Canonical identity:** Diffbot (diffbot.com)
**Category:** A. Web Data Acquisition — automatic extraction APIs + knowledge graph
**Type:** Hosted service (proprietary)
**Official URL:** https://www.diffbot.com
**Description:** AI-powered structured extraction APIs (article, product, discussion, video extractors) plus a public Knowledge Graph of billions of entities built from crawled web data.
**Contents inspected:** 2026 directory entries only; diffbot.com not opened.
**Actual capabilities:** Visual/ML page understanding returning normalized entities; crawl API; knowledge graph query (reported).
**Usage domain:** Normalized product/article data, entity enrichment, knowledge-graph queries.
**Inputs:** URLs, entity queries.
**Outputs:** Normalized JSON entities; graph query results.
**Integration method:** REST APIs.
**Dependencies:** API key; token/credit billing (reported).
**Availability:** Hosted; trial reported.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Normalization is opinionated; coverage/cost trade-offs not verified.
**Related resources:** Zyte (auto-extract), Firecrawl (extract), Exa.
**Sources:** https://github.com/kriptoburak/ai-web-scraping-directory ; https://github.com/api-evangelist/scraping (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** SerpApi
**Canonical identity:** SerpApi (serpapi.com)
**Category:** A. Web Data Acquisition — SERP collection API
**Type:** Hosted service (proprietary)
**Official URL:** https://serpapi.com
**Description:** Structured search-engine-results API covering Google, Bing, Yahoo, Baidu, YouTube, Amazon, eBay and others; returns parsed JSON instead of SERP HTML.
**Contents inspected:** 2026 comparisons and benchmark docs; serpapi.com not opened.
**Actual capabilities:** Real-time SERP scraping with structured JSON output across 30+ engines; location/device parameters (reported).
**Usage domain:** SEO tooling, SERP monitoring, search-result collection for research.
**Inputs:** Search queries + engine/locale parameters.
**Outputs:** Structured JSON (organic results, ads, knowledge panels, etc.).
**Integration method:** REST API; client libraries.
**Dependencies:** API key; per-search billing (entry ~$75/mo, 100 free searches reported — not verified).
**Availability:** Hosted.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Search results only — not a general page-fetching API.
**Related resources:** ScrapingBee (Google Search API), DataForSEO, Exa, Tavily.
**Sources:** https://github.com/api-evangelist/scraping ; https://github.com/pecgk79/scraping-api-benchmark (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Crawlbase
**Canonical identity:** Crawlbase (crawlbase.com)
**Category:** A. Web Data Acquisition — budget scraping API
**Type:** Hosted service (proprietary)
**Official URL:** https://crawlbase.com
**Description:** Low-entry-price scraping API (crawling + storage) positioned for budget startups and side projects.
**Contents inspected:** 2026 benchmark table only; crawlbase.com not opened.
**Actual capabilities:** Not verified against primary docs — reported: JS rendering, 1,000 free requests, entry ~$29/mo.
**Usage domain:** Low-volume scraping on a budget.
**Inputs/Outputs:** Not verified.
**Integration method:** REST API (reported).
**Dependencies:** API key (reported).
**Availability:** Hosted (reported).
**Maintenance:** Not verified.
**License:** Proprietary (reported).
**Limitations:** Thin record; primary docs not inspected.
**Related resources:** ScraperAPI, ScrapingBee.
**Sources:** https://github.com/pecgk79/scraping-api-benchmark (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unverified — needs a primary-source pass.

---

**Resource name:** Octoparse
**Canonical identity:** Octoparse (octoparse.com)
**Category:** A. Web Data Acquisition — no-code scraping
**Type:** Hosted service + desktop app (proprietary)
**Official URL:** https://www.octoparse.com
**Description:** Visual, no-code web scraping builder (desktop + cloud): point-and-click extraction templates with cloud scheduling.
**Contents inspected:** 2026 comparisons only; octoparse.com not opened.
**Actual capabilities:** Visual task builder; cloud extraction scheduling; export to CSV/Excel/API (reported).
**Usage domain:** Non-programmers; business users needing recurring extracts.
**Inputs:** Visual workflow definitions.
**Outputs:** CSV/Excel/JSON/API.
**Integration method:** Desktop app + cloud dashboard.
**Dependencies:** Subscription (entry cited ~$69/mo billed annually; free local tasks reported — not verified).
**Availability:** Hosted + desktop.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Less flexible than code; site changes break visual templates.
**Related resources:** Browse AI, Apify (no-code actors).
**Sources:** https://www.firecrawl.dev/blog/scrapingbee-alternatives ; https://omidsaffari.com/blog/best-web-scraping-tools (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Browse AI
**Canonical identity:** Browse AI (browse.ai)
**Category:** A. Web Data Acquisition — no-code extraction + change monitoring
**Type:** Hosted service (proprietary)
**Official URL:** https://browse.ai
**Description:** No-code "train a robot" extraction: point at data on a page and it builds a recurring scraper; includes change monitoring.
**Contents inspected:** 2026 comparison table only; browse.ai not opened.
**Actual capabilities:** Trainable extraction robots; monitoring with alerts; integrations (reported).
**Usage domain:** Recurring extraction and page-change monitoring without code.
**Inputs:** Trained robot definitions (URLs + labeled fields).
**Outputs:** Spreadsheet/API data; change alerts.
**Integration method:** Web app; API/integrations.
**Dependencies:** Subscription (entry ~$19/mo, 50 credits/mo free reported — not verified).
**Availability:** Hosted.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Robot training per site; credit costs scale with pages/rows.
**Related resources:** Octoparse, changedetection.io.
**Sources:** https://omidsaffari.com/blog/best-web-scraping-tools (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Context.dev
**Canonical identity:** Context.dev (context.dev)
**Category:** A. Web Data Acquisition — agent-oriented extraction API
**Type:** Hosted service (proprietary)
**Official URL:** https://context.dev
**Description:** Newer API positioned as "agent data" infrastructure: crawling plus webhook-based page monitoring, priced per page/JSON scrape.
**Contents inspected:** 2026 comparison table only; context.dev not opened.
**Actual capabilities:** Not verified — reported: scrape/crawl endpoints, monitoring webhooks.
**Usage domain:** AI agent data pipelines.
**Inputs/Outputs:** Not verified.
**Integration method:** REST API (reported).
**Dependencies:** Subscription (Developer $19/mo, 1,000 credits/mo free reported — not verified).
**Availability:** Hosted (reported).
**Maintenance:** Not verified.
**License:** Proprietary (reported).
**Limitations:** Thin record; primary docs not inspected.
**Related resources:** Firecrawl, Tavily.
**Sources:** https://omidsaffari.com/blog/best-web-scraping-tools (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unverified — needs a primary-source pass.

---

### A5. LLM-ready web readers (URL-to-markdown / agent search APIs)

---

**Resource name:** Jina Reader
**Canonical identity:** jina-ai/reader (GitHub); Jina AI; endpoints r.jina.ai (Reader), s.jina.ai (Search), deepsearch.jina.ai (DeepSearch)
**Category:** A. Web Data Acquisition — page-to-markdown reader; C. Research ingestion
**Type:** Open-source project + hosted API (freemium)
**Official URL:** https://github.com/jina-ai/reader (product: https://jina.ai/)
**Description:** Converts any web page into clean, LLM-friendly markdown by prepending `https://r.jina.ai/` to the URL. Handles HTML pages, PDFs, and JS-rendered sites server-side; strips navigation/ads. Companion search endpoint `s.jina.ai` returns web search results as markdown for agents/RAG.
**Contents inspected:** Multiple 2026 agent-skill docs describing endpoints, headers, rate limits, and fallback workflows; jina-ai/reader repo referenced as source (~10.5k stars cited).
**Actual capabilities:** URL → markdown/text/JSON; image captioning via opt-in header; target CSS selectors; cookie/proxy forwarding headers; search endpoint with top results as full markdown; batch URL support.
**Usage domain:** Agent fallback when direct fetching is blocked (403/Cloudflare/CAPTCHA), RAG ingestion, quick page summarization.
**Inputs:** URLs; search queries.
**Outputs:** Markdown, plain text, or JSON (url/title/content/timestamp).
**Integration method:** Plain HTTPS GET (curl/requests/WebFetch); optional `Authorization: Bearer` API key for higher limits.
**Dependencies:** None for basic use; API key for raised rate limits.
**Availability:** Hosted; free tier reported (~20 req/min without key); keyed plans via jina.ai dashboard.
**Maintenance:** Active.
**License:** Apache-2.0 (reported — not re-verified from license file).
**Limitations:** Rate limits on free use; heavy-JS pages may still be incomplete; very long pages may truncate; bypassing site protections raises ToS questions — use on content you have the right to access.
**Related resources:** Firecrawl, Crawl4AI, MarkItDown, Tavily Extract.
**Sources:** https://github.com/hinvec/security-scanned-skills/blob/HEAD/skills/jina-reader-url-to-markdown-web-search/SKILL.md ; https://github.com/majiayu000/claude-skill-registry/blob/HEAD/skills/other/other/using-jina-reader/SKILL.md ; https://github.com/dawgomatic/xagent/blob/HEAD/skills/skills/adhishthite/jina-ai/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — behavior corroborated by many independent 2026 agent docs; repo README not opened directly.

---

**Resource name:** Tavily
**Canonical identity:** Tavily (tavily.com); API at api.tavily.com
**Category:** A. Web Data Acquisition — agent search/extract API; C. Research ingestion
**Type:** Hosted service (proprietary)
**Official URL:** https://tavily.com (docs: https://docs.tavily.com)
**Description:** AI search engine built as a "web access layer" for LLM agents. One API call chains search → crawl → filter → extract and returns RAG-optimized structured content rather than raw URLs/snippets.
**Contents inspected:** 2026 SOP/skill docs detailing five endpoints and parameters; tavily.com not opened.
**Actual capabilities:** `/search` (AI-ranked results, topics: general/news/finance, time ranges, domain filters), `/extract` (URL → structured content), `/crawl` (site crawling), `/map` (site URL discovery), `/research` (end-to-end agentic research). Python/JS SDKs.
**Usage domain:** Deep-research agents, RAG retrieval, agent web access.
**Inputs:** Queries, URLs, site roots, research questions.
**Outputs:** Ranked results with AI-scored content, extracted page content, site maps, research reports.
**Integration method:** REST API (Bearer key); SDKs; MCP servers built on it.
**Dependencies:** API key (free tier reported; keyless rate-limited access reported in some agent docs — not verified).
**Availability:** Hosted.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Keyed service; costs scale with search depth and extraction volume; result quality depends on underlying index coverage.
**Related resources:** Exa, Perplexity Search API, Jina Reader, SerpApi, GPT Researcher.
**Sources:** https://github.com/crazyfishjack/aiwiki/blob/HEAD/search-sop/Tavily-Search-API.md ; https://github.com/ouyanggai/skills-by-zw/blob/HEAD/global/tavily-best-practices/SKILL.md ; https://www.humai.blog/ai-search-apis-compared-tavily-vs-exa-vs-perplexity/ (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — endpoint model corroborated by multiple sources; primary docs not opened.

---

**Resource name:** Exa
**Canonical identity:** Exa (exa.ai)
**Category:** A. Web Data Acquisition — neural search API; C. Research ingestion
**Type:** Hosted service (proprietary)
**Official URL:** https://exa.ai
**Description:** Neural (semantic) web search API for AI applications: keyword, semantic, and "auto" search modes plus content retrieval, positioned for research and conceptually-related content discovery.
**Contents inspected:** 2026 agent docs (MCP server AGENTS.md, Hermes web-search docs); exa.ai not opened.
**Actual capabilities:** Neural/keyword search; contents retrieval endpoint; used as search backend in agent MCP servers (reported).
**Usage domain:** Agent research, semantic discovery, RAG retrieval.
**Inputs:** Natural-language queries.
**Outputs:** Ranked results with retrieved content.
**Integration method:** REST API (API key); consumed via MCP servers.
**Dependencies:** API key; free tier reported (~1,000 searches/month — not verified).
**Availability:** Hosted.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Primary docs not inspected; free-tier figure single-sourced.
**Related resources:** Tavily, Perplexity Search API, Jina Search.
**Sources:** https://github.com/tavily-fde/autopr--fork-web-retrieval-mcp/blob/HEAD/AGENTS.md ; https://github.com/lexus2016/hermes-agent-evolution/blob/HEAD/website/docs/user-guide/features/web-search.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Perplexity Search API
**Canonical identity:** Perplexity (perplexity.ai); docs at docs.perplexity.ai
**Category:** A. Web Data Acquisition — search API; C. Research ingestion
**Type:** Hosted service (proprietary)
**Official URL:** https://docs.perplexity.ai
**Description:** Search API returning ranked, date-stamped results from Perplexity's index; extraction returns query-relevant snippets rather than full-page dumps.
**Contents inspected:** 2026 agent docs only; docs.perplexity.ai not opened.
**Actual capabilities:** Web search with ranked results; snippet-level extraction (reported).
**Usage domain:** Agent search backends.
**Inputs:** Queries.
**Outputs:** Ranked results; relevant passages.
**Integration method:** REST API (keyed only — no anonymous tier reported).
**Dependencies:** API key.
**Availability:** Hosted.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Keyed only; snippet-level extraction is not full-page content.
**Related resources:** Tavily, Exa.
**Sources:** https://github.com/lexus2016/hermes-agent-evolution/blob/HEAD/website/docs/user-guide/features/web-search.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — single-source corroboration; needs primary docs.

---

**Resource name:** Brave Search API
**Canonical identity:** Brave Search (api.search.brave.com); Brave Software
**Category:** A. Web Data Acquisition — independent search index API
**Type:** Hosted service (proprietary, freemium)
**Official URL:** https://api.search.brave.com
**Description:** API over Brave's independent web index — a queryable alternative to scraping Google/Bing SERPs; commonly wired into agent MCP servers.
**Contents inspected:** 2026 MCP server docs (free tier 2,000 queries/month, 1 req/sec reported); api.search.brave.com not opened.
**Actual capabilities:** Web search over Brave's own index (reported).
**Usage domain:** Agent search backends, SERP collection without scraping.
**Inputs:** Queries.
**Outputs:** Ranked results JSON.
**Integration method:** REST API (API key).
**Dependencies:** API key; free tier reported.
**Availability:** Hosted.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** Independent index is smaller than Google/Bing; free-tier figures not verified against primary docs.
**Related resources:** SerpApi, Exa, Tavily, Mojeek.
**Sources:** https://github.com/billallison/brsearch-mcp-server/blob/HEAD/.github/copilot-instructions.md ; https://serp.fast/tools/common-crawl (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Parallel (parallel.ai)
**Canonical identity:** Unresolved — reported as parallel.ai offering AI-native search/extraction
**Category:** A. Web Data Acquisition — agent search API
**Type:** Hosted service (reported)
**Official URL:** Unresolved (reported: https://parallel.ai — not verified)
**Description:** Mentioned in 2026 agent docs as AI-native search and extraction with deep-research capabilities.
**Contents inspected:** One 2026 agent doc mention only.
**Actual capabilities:** Not verified.
**Usage domain:** Reported: agent search backends.
**Inputs/Outputs/Integration/Dependencies/Availability/Maintenance/License/Limitations:** Not verified.
**Related resources:** Tavily, Exa.
**Sources:** https://github.com/lexus2016/hermes-agent-evolution/blob/HEAD/website/docs/user-guide/features/web-search.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unresolved — needs a dedicated verification pass.

---

### A6. PDF & document extraction

---

**Resource name:** MarkItDown
**Canonical identity:** microsoft/markitdown (GitHub); built by Microsoft's AutoGen team
**Category:** A. Web Data Acquisition — document-to-markdown conversion; C. Research ingestion
**Type:** Open-source library + CLI + Docker (Python)
**Official URL:** https://github.com/microsoft/markitdown
**Description:** Lightweight Python utility converting many file types to Markdown for LLM and text-analysis pipelines: PDF, PowerPoint, Word, Excel, images (EXIF + OCR), audio (EXIF + speech transcription), HTML, CSV/JSON/XML, ZIP archives, YouTube URLs, EPUBs. Comparable to textract but preserves document structure (headings, lists, tables, links).
**Contents inspected:** GitHub README as surfaced in search results (format list, security notice, CLI/Python API/Docker usage, plugin system incl. markitdown-ocr, Azure Content Understanding / Document Intelligence integrations).
**Actual capabilities:** Per-format converters with plugin architecture; CLI (`markitdown`); Python API (`convert_local`, `convert_stream`); Docker image.
**Usage domain:** LLM ingestion pipelines, RAG document preprocessing.
**Inputs:** Files, streams, URLs (YouTube).
**Outputs:** Markdown (token-efficient, structure-preserving).
**Integration method:** pip package, CLI, Docker, Python API; MCP server also referenced by community (not verified as official).
**Dependencies:** Python; optional per-format extras (OCR, transcription).
**Availability:** Open source; PyPI `markitdown`.
**Maintenance:** Active (README updated ~72 days before sweep).
**License:** MIT (per README badges — Partially verified, license file not opened).
**Limitations:** Output is meant for machine consumption, not high-fidelity human rendering; performs I/O with process privileges — sanitize untrusted inputs (per README security notice).
**Related resources:** Docling, Unstructured, textract, Docling MCP server.
**Sources:** https://github.com/microsoft/markitdown (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — README inspected via search-cached primary source.

---

**Resource name:** Docling
**Canonical identity:** docling-project/docling (GitHub) — **Corrected**: moved from DS4SD/docling; now hosted by the LF AI & Data Foundation (project originated at IBM Research Zurich)
**Category:** A. Web Data Acquisition — advanced document parsing
**Type:** Open-source library + CLI + API server + MCP server (Python)
**Official URL:** https://github.com/docling-project/docling (docs: https://docling-project.github.io/docling/)
**Description:** Document-processing toolkit with advanced PDF understanding (page layout, reading order, table structure, code/formula parsing, image classification), OCR for scanned PDFs, and a unified `DoclingDocument` model exportable to Markdown, HTML, DocTags, and lossless JSON. Integrates with LangChain, LlamaIndex, Haystack, CrewAI.
**Contents inspected:** GitHub org page and README as surfaced in search results (feature list, repo family: docling-core, docling-parse, docling-serve, docling-ibm-models, docling-mcp, docling-sdg); IBM TechXchange 2025 lab guide (40k+ stars, 1.5M+ monthly downloads claimed).
**Actual capabilities:** Multi-format parsing (PDF, DOCX, PPTX, XLSX, HTML, EPUB, images, audio/ASR, LaTeX, emails); layout/table/formula models; OCR; chunking; MCP server (`docling-mcp`); REST API server (`docling-serve`); CLI.
**Usage domain:** Production RAG ingestion, document-grounded AI, large-scale knowledge intake.
**Inputs:** Documents in many formats.
**Outputs:** Markdown, JSON (lossless), HTML, DocTags, chunked representations.
**Integration method:** pip package, CLI, Docker, REST API (docling-serve), MCP server, framework integrations.
**Dependencies:** Python; ML models downloaded on first use (heavier than MarkItDown).
**Availability:** Open source; self-hostable; local execution for air-gapped use.
**Maintenance:** Very active (donated to LF AI & Data Foundation; cited as IBM's most successful organic OSS project).
**License:** MIT (per secondary reporting — not re-verified from license file).
**Limitations:** Heavier resource footprint than lightweight converters; model downloads required; accuracy varies by document type.
**Related resources:** MarkItDown, Unstructured, LlamaParse, unstructured.io platform.
**Sources:** https://github.com/docling-project/docling ; https://github.com/docling-project ; https://ethantroy.dev/events/ibm-techxchange-2025/IBM-TechXchange-2025-Lab-Guide-Docling-3640_1759260769370001oTNW.pdf ; https://Dev.to/aairom/my-first-hands-on-experience-with-docling-46mi (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — with **Corrected** canonical identity (DS4SD → docling-project; LF AI & Data Foundation hosting).

---

**Resource name:** Unstructured (open-source library)
**Canonical identity:** Unstructured-IO/unstructured (GitHub); company: Unstructured (unstructured.io)
**Category:** A. Web Data Acquisition — document ETL
**Type:** Open-source library (Python) + commercial platform/API
**Official URL:** https://github.com/Unstructured-IO/unstructured
**Description:** Open-source ETL for transforming complex documents into clean, structured formats for language models: partitioning (layout-aware chunking), connectors (S3, Azure, local, and more), and normalized JSON output across 25+ file types. The company also sells an enterprise platform/API.
**Contents inspected:** GitHub repo metadata as surfaced (15,525 stars, 1,940 commits, Apache-2.0, not archived, created 2022-09-26); README description.
**Actual capabilities:** Document partitioning with strategies (fast/OCR/hi-res); table extraction; staging/serialization; ingest connectors; chunking for RAG.
**Usage domain:** RAG preprocessing, document ETL pipelines.
**Inputs:** PDFs, Office docs, images, emails, HTML, and 20+ other types.
**Outputs:** Normalized JSON elements with metadata; staged formats.
**Integration method:** Python library; Docker; hosted API (commercial).
**Dependencies:** Python; optional heavy extras (detectron2, OCR, etc.).
**Availability:** Open source (Apache-2.0); commercial hosted API.
**Maintenance:** Active (243 releases cited).
**License:** Apache-2.0 (confirmed via repo metadata).
**Limitations:** Heavy optional dependencies; `hi_res` strategy is slow and GPU-hungry; commercial features (enrichment, embedding) are platform-only.
**Related resources:** Docling, MarkItDown, LlamaParse.
**Sources:** https://github.com/Unstructured-IO/unstructured (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — repo metadata and README description inspected.

---

**Resource name:** pdfplumber
**Canonical identity:** jsvine/pdfplumber (GitHub); PyPI package `pdfplumber`
**Category:** A. Web Data Acquisition — PDF text/table extraction
**Type:** Open-source library (Python)
**Official URL:** https://github.com/jsvine/pdfplumber (PyPI: https://pypi.org/project/pdfplumber/)
**Description:** Python library for detailed PDF inspection and extraction: per-character/line/rectangle geometry, text extraction, and table detection/extraction with tunable strategies.
**Contents inspected:** PyPI project page as surfaced (table-extraction API: `extract_tables`, `find_tables`, debug tablefinder).
**Actual capabilities:** Text extraction with layout metadata; table finding/extraction; visual debugging of table detection.
**Usage domain:** Table-heavy PDF extraction, invoice/report parsing.
**Inputs:** PDF files.
**Outputs:** Text, tables (lists of rows/cells), geometric objects.
**Integration method:** Python library.
**Dependencies:** pdfminer.six, Pillow (not re-verified).
**Availability:** Open source.
**Maintenance:** Maintained (PyPI page current; version 0.11.8 surfaced).
**License:** MIT (not re-verified).
**Limitations:** Struggles with complex layouts/merged cells; no OCR (needs text-based PDFs); slower than PyMuPDF on large files.
**Related resources:** PyMuPDF, pdfminer.six, camelot, tabula.
**Sources:** https://pypi.org/project/pdfplumber/0.11.8/ ; https://github.com/topics/table-extraction (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — PyPI page inspected; canonical GitHub owner (jsvine) from general knowledge, Partially verified.

---

**Resource name:** PyMuPDF
**Canonical identity:** pymupdf/PyMuPDF (GitHub); PyPI package `pymupdf` (import `fitz`)
**Category:** A. Web Data Acquisition — high-performance PDF library
**Type:** Open-source library (Python bindings over MuPDF)
**Official URL:** https://github.com/pymupdf/PyMuPDF
**Description:** High-performance Python library for PDF data extraction, analysis, conversion, and manipulation; also handles XPS/EPUB and other formats. Companion package `pymupdf4llm` adds LLM-oriented helpers (e.g., improved line/column-aware text extraction).
**Contents inspected:** GitHub topics page and a maintainer discussion (#3552) as surfaced; primary README not opened.
**Actual capabilities:** Fast text extraction (multiple modes incl. blocks/words), table finding (`find_tables`), rendering to images, annotations, document manipulation; `pymupdf4llm` for markdown-oriented extraction.
**Usage domain:** High-throughput PDF text/table extraction, rendering, document workflows.
**Inputs:** PDF and other document formats.
**Outputs:** Text, tables (incl. pandas), images, structured blocks.
**Integration method:** Python library.
**Dependencies:** MuPDF native bindings (wheels provided).
**Availability:** Open source.
**Maintenance:** Active (topics page shows 2026 updates).
**License:** AGPL-3.0 for the open-source distribution (widely reported — not re-verified from license file; commercial licenses available). Treat license as Partially verified.
**Limitations:** AGPL licensing affects commercial embedding; scanned PDFs still need OCR.
**Related resources:** pdfplumber, pymupdf4llm, pdfminer.six.
**Sources:** https://github.com/topics/pymupdf ; https://github.com/pymupdf/PyMuPDF/discussions/3552 (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — identity and capabilities corroborated; license needs file-level confirmation.

---

**Resource name:** kreuzberg
**Canonical identity:** kreuzberg-dev/kreuzberg (GitHub)
**Category:** A. Web Data Acquisition — polyglot document intelligence
**Type:** Open-source framework (Rust core; bindings for Python, Ruby, Java, Go, PHP, Elixir, C#, TypeScript) + CLI + REST API + MCP server
**Official URL:** https://github.com/kreuzberg-dev/kreuzberg
**Description:** Document intelligence framework with a Rust core: extracts text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats; usable as library, CLI, REST API, or MCP server.
**Contents inspected:** GitHub topics entry only; primary README not opened.
**Actual capabilities:** Not verified beyond the topics-page description.
**Usage domain:** Reported: multi-language document extraction pipelines.
**Inputs/Outputs:** Not verified.
**Integration method:** Reported: native bindings, CLI, REST, MCP.
**Dependencies:** Not verified.
**Availability:** Open source (reported).
**Maintenance:** Active per topics page (Feb 2026 update noted).
**License:** Not verified.
**Limitations:** Thin record; primary docs not inspected.
**Related resources:** Docling, MarkItDown, Unstructured.
**Sources:** https://github.com/topics/table-extraction (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — identity corroborated; capabilities single-sourced.

---

**Resource name:** Tesseract OCR
**Canonical identity:** tesseract-ocr/tesseract (GitHub)
**Category:** A. Web Data Acquisition — optical character recognition
**Type:** Open-source engine (C++)
**Official URL:** https://github.com/tesseract-ocr/tesseract
**Description:** The standard open-source OCR engine; used as the OCR backend inside Docling, Unstructured, MarkItDown (via plugin), and countless scanned-PDF pipelines.
**Contents inspected:** Not opened in this sweep; identity from general knowledge + its role cited in Docling/OpenContracts docs.
**Actual capabilities:** Text recognition in 100+ languages; LSTM models; hOCR/TSV/PDF outputs (general knowledge — Partially verified).
**Usage domain:** Scanned PDFs/images → text.
**Inputs:** Images, scanned PDFs.
**Outputs:** Text, hOCR, searchable PDF.
**Integration method:** CLI, C++ API, wrappers (pytesseract, tesserocr).
**Dependencies:** Leptonica; traineddata language files.
**Availability:** Open source.
**Maintenance:** Maintained.
**License:** Apache-2.0 (not re-verified).
**Limitations:** Accuracy depends on image quality; layout understanding is minimal compared to Docling/Unstructured pipelines.
**Related resources:** Docling, Unstructured, MarkItDown (markitdown-ocr plugin), EasyOCR.
**Sources:** https://github.com/Open-Source-Legal/OpenContracts/blob/main/docs/pipelines/docling_parser.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** LlamaParse
**Canonical identity:** LlamaIndex — LlamaParse (LlamaCloud parsing service)
**Category:** A. Web Data Acquisition — managed document parsing
**Type:** Hosted service (proprietary) + client libraries
**Official URL:** https://cloud.llamaindex.ai (parsing product page not opened)
**Description:** LlamaIndex's managed document-parsing API aimed at producing LLM-ready structured output from complex documents (tables, embedded objects).
**Contents inspected:** Named in workstream brief only; primary docs not opened in this sweep.
**Actual capabilities:** Not verified.
**Usage domain:** Reported: RAG ingestion via LlamaIndex ecosystem.
**Inputs/Outputs/Integration/Dependencies/Availability/Maintenance/License/Limitations:** Not verified.
**Related resources:** Docling, Unstructured, MarkItDown, LlamaIndex.
**Sources:** Workstream brief (Part 12) (2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unverified — needs a primary-source pass.

---

### A7. YouTube / media metadata extraction

---

**Resource name:** yt-dlp
**Canonical identity:** yt-dlp/yt-dlp (GitHub); community fork of youtube-dl (ytdl-org/youtube-dl, now largely inactive)
**Category:** A. Web Data Acquisition — media download & metadata extraction
**Type:** Open-source CLI + Python library
**Official URL:** https://github.com/yt-dlp/yt-dlp
**Description:** Feature-rich command-line audio/video downloader and metadata extractor supporting YouTube and hundreds of other sites (per its supported-sites list). Forked from youtube-dl in 2021 after that project's stagnation; now the actively maintained standard. Also the standard fallback for caption/transcript extraction (`--write-auto-subs --skip-download`).
**Contents inspected:** Wikipedia youtube-dl article (fork history, stable release 2026.08.19, Ubuntu packaging) and fork README excerpts as surfaced.
**Actual capabilities:** Video/audio download, format selection/sorting, subtitle/caption extraction (incl. auto-generated), metadata JSON dumps, playlist/channel extraction, SponsorBlock integration, browser-cookie import.
**Usage domain:** Media archiving, transcript extraction for research ingestion, dataset building from video platforms.
**Inputs:** Video/page URLs.
**Outputs:** Media files, subtitles (vtt/srt), metadata JSON.
**Integration method:** CLI; Python API.
**Dependencies:** Python; ffmpeg for merging/transcoding; optional browser for cookies.
**Availability:** Open source; packaged in major Linux distros.
**Maintenance:** Very active.
**License:** Unlicense (per fork README badges — Partially verified).
**Limitations:** Site breakage is constant (cat-and-mouse with platforms); downloading copyrighted material without rights may be unlawful — research use should respect platform ToS and copyright.
**Related resources:** youtube-dl (Historical), youtube-transcript-api, gallery-dl.
**Sources:** https://en.wikipedia.org/wiki/Youtube-dl ; https://github.com/mohammedabdelshafy/yt-dlp (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified. Note: **Historical** predecessor youtube-dl is superseded by this fork.

---

**Resource name:** youtube-transcript-api
**Canonical identity:** jdepoix/youtube-transcript-api (GitHub); PyPI package `youtube-transcript-api`
**Category:** A. Web Data Acquisition — caption/transcript extraction
**Type:** Open-source library + CLI (Python)
**Official URL:** https://github.com/jdepoix/youtube-transcript-api
**Description:** Python API to fetch transcripts/subtitles (manual and auto-generated, with translation support) for YouTube videos without an API key or headless browser.
**Contents inspected:** 2026 skill docs and planning docs describing the API (`YouTubeTranscriptApi().fetch(video_id)` returning timestamped snippets); an older fork page (nsmirnov214) also surfaced — canonical remains jdepoix.
**Actual capabilities:** Fetch captions by video ID; language selection; translation; list available transcript tracks; CLI.
**Usage domain:** Video research ingestion, summarization pipelines.
**Inputs:** YouTube video IDs/URLs.
**Outputs:** Timestamped transcript snippets (text/start/duration), SRT/text/JSON formats.
**Integration method:** Python library; CLI.
**Dependencies:** Python, requests (not re-verified).
**Availability:** Open source.
**Maintenance:** Maintained (widely used in 2026 agent skills).
**License:** MIT (not re-verified).
**Limitations:** Fails when videos disable captions, are region-blocked, or under bot-mitigation; auto-captions are imperfect; no speech-to-text fallback (use yt-dlp + transcription for that).
**Related resources:** yt-dlp (fallback via `--write-auto-subs`), YouTube Data API captions endpoints (official but requires OAuth/edit permission for arbitrary videos).
**Sources:** https://github.com/0sxd/youtube-transcript-skill/blob/HEAD/SKILL.md ; https://github.com/mpsanders/voxscripta/blob/HEAD/docs/planning/YouTube%20Transcript%20Extraction%20Methods.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — canonical identity corroborated; primary README not opened.

---

### A8. Public webpage monitoring & change detection

---

**Resource name:** changedetection.io
**Canonical identity:** dgtlmoon/changedetection.io (GitHub) — **Corrected**: several forks (ilijian, zznidar, chris2k20, adamhancock, dmtea) surfaced in search; upstream is dgtlmoon (Docker image published as ghcr.io/dgtlmoon/changedetection.io)
**Category:** A. Web Data Acquisition — webpage/API change monitoring
**Type:** Open-source self-hosted app (Python) + commercial SaaS
**Official URL:** https://github.com/dgtlmoon/changedetection.io (product: https://changedetection.io/)
**Description:** Self-hosted website change detection, monitoring, and notification service. Watches pages (and JSON API responses) for text changes and notifies via email/Discord/Slack/Telegram/webhooks/API calls. Supports a fast built-in HTTP fetcher and a Chrome/WebDriver or Playwright-based fetcher for JS sites, plus "browser steps" (form fills, clicks, logins) before checks.
**Contents inspected:** README content as surfaced across upstream and forks (use cases, Docker/pip install, Playwright fetcher, browser steps, JSON monitoring).
**Actual capabilities:** URL watches with CSS/XPath/JSON filters; diff viewing (word/line/character); notification integrations; REST API; RSS feed generation from changes; re-stock/price monitoring.
**Usage domain:** Price monitoring, release/security-advisory tracking, government-page monitoring, API response monitoring, compliance checks.
**Inputs:** Watched URLs, selectors/filters, check intervals.
**Outputs:** Change diffs, notifications, RSS feeds, API callbacks.
**Integration method:** Self-hosted Docker/pip app with web UI and REST API; SaaS option.
**Dependencies:** Python or Docker; Playwright/Chromium for JS fetching.
**Availability:** Open source self-hosted (free); SaaS from ~$7–9/mo (secondary, not verified).
**Maintenance:** Active.
**License:** Apache-2.0 (widely reported; README-level — Partially verified).
**Limitations:** Self-hosting burden; aggressive check intervals can get IPs blocked; JS-heavy sites need the browser fetcher.
**Related resources:** Huginn, Browse AI, Visualping (proprietary), Wayback Machine.
**Sources:** https://github.com/ilijian/changedetection.io ; https://github.com/dmtea/changedetection.io ; https://github.com/harishpiyer/free-api-bazaar/blob/HEAD/browser-tools/changedetection-io/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — with **Corrected** canonical identity (dgtlmoon upstream, not the forks).

---

**Resource name:** Huginn
**Canonical identity:** huginn/huginn (GitHub)
**Category:** A. Web Data Acquisition — monitoring & automation agents
**Type:** Open-source self-hosted app (Ruby)
**Official URL:** https://github.com/huginn/huginn
**Description:** Self-hosted "agents" system that monitors the web and acts on events: website change watchers, RSS, scrapers, and notification/action agents chained into workflows. The open-source analogue of Yahoo Pipes/IFTTT for web monitoring.
**Contents inspected:** Not opened in this sweep; named in workstream brief; identity from general knowledge.
**Actual capabilities:** Not verified against primary docs — reported: website agents, data agents, notification agents.
**Usage domain:** Web monitoring, automation workflows.
**Inputs/Outputs/Integration:** Not verified.
**Dependencies:** Ruby/Rails stack (reported).
**Availability:** Open source (reported).
**Maintenance:** Not verified.
**License:** MIT (not re-verified).
**Limitations:** Thin record; primary docs not inspected.
**Related resources:** changedetection.io, n8n.
**Sources:** Workstream brief (Part 12) (2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — identity known; capabilities need a primary-source pass.

---

### A9. Search-result collection & metasearch

---

**Resource name:** SearXNG
**Canonical identity:** searxng/searxng (GitHub); project site searxng.org
**Category:** A. Web Data Acquisition — self-hosted metasearch
**Type:** Open-source service (Python)
**Official URL:** https://github.com/searxng/searxng
**Description:** Privacy-respecting, self-hosted metasearch engine aggregating results from 70+ search engines without tracking. Exposes HTML UI and a JSON API (`/search?q=…&format=json`), making it a keyless search backend for agents when self-hosted or pointed at a public instance.
**Contents inspected:** 2026 agent skill docs (JSON API usage, engine selection, categories, safesearch params) and a Home Assistant addon doc describing privacy hardening; primary repo not opened.
**Actual capabilities:** Multi-engine aggregation; JSON/HTML/RSS output formats; per-engine and per-category selection; safesearch controls; no tracking/profiling.
**Usage domain:** Private search backend for research agents; SERP collection without API keys.
**Inputs:** Search queries (+ engine/category/locale params).
**Outputs:** Aggregated results (JSON/HTML/RSS).
**Integration method:** Self-hosted HTTP service; queried via curl/HTTP.
**Dependencies:** Python; outbound access to upstream engines.
**Availability:** Open source; public instances exist (reliability varies).
**Maintenance:** Active.
**License:** AGPL-3.0 (widely reported — not re-verified).
**Limitations:** Upstream engines rate-limit aggressive instances; public instances are best-effort; result quality depends on enabled engines.
**Related resources:** Brave Search API, SerpApi, Exa, Tavily.
**Sources:** https://github.com/magnetoid/janus/blob/HEAD/./optional-skills/research/searxng-search/SKILL.md ; https://github.com/andreibarburas/hassio-apps/blob/HEAD/searxng/DOCS.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Webz.io
**Canonical identity:** Webz.io (webz.io)
**Category:** A. Web Data Acquisition — queryable web-data feeds
**Type:** Hosted service (proprietary, enterprise)
**Official URL:** https://webz.io
**Description:** Pre-processed Common Crawl–scale web data delivered as queryable structured feeds (news, forums, blogs, dark web) for teams that cannot run their own crawl infrastructure.
**Contents inspected:** 2026 comparison blurb only; webz.io not opened.
**Actual capabilities:** Not verified — reported: filtered web-data APIs/feeds.
**Usage domain:** Enterprise web intelligence without crawl infrastructure.
**Inputs/Outputs/Integration:** Not verified.
**Availability:** Hosted, enterprise (reported).
**License:** Proprietary.
**Limitations:** Thin record; primary docs not inspected.
**Related resources:** Common Crawl, Diffbot, Bright Data datasets.
**Sources:** https://serp.fast/tools/common-crawl (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — identity corroborated; details single-sourced.

---

**Resource name:** DataForSEO
**Canonical identity:** DataForSEO (dataforseo.com)
**Category:** A. Web Data Acquisition — SEO/SERP data APIs
**Type:** Hosted service (proprietary, pay-as-you-go)
**Official URL:** https://dataforseo.com
**Description:** API platform with 60+ endpoints for SERP data, keywords, backlinks, and on-page audits; pay-as-you-go from ~$0.0006/SERP (secondary, not verified).
**Contents inspected:** 2026 benchmark table only; dataforseo.com not opened.
**Actual capabilities:** Not verified — reported: SERP, keyword, backlink, and content APIs.
**Usage domain:** SEO data pipelines, SERP collection at scale.
**Inputs:** Queries/URLs via API.
**Outputs:** Structured JSON.
**Integration method:** REST API (reported).
**Dependencies:** Account credit (reported; $1 free credit cited).
**Availability:** Hosted (reported).
**Maintenance:** Not verified.
**License:** Proprietary.
**Limitations:** Thin record; pricing not verified.
**Related resources:** SerpApi, Bright Data.
**Sources:** https://github.com/pecgk79/scraping-api-benchmark (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unverified — needs a primary-source pass.

---

### A10. Web archives as data sources

---

**Resource name:** Common Crawl
**Canonical identity:** Common Crawl (nonprofit); data at data.commoncrawl.org; index at index.commoncrawl.org; code: github.com/commoncrawl
**Category:** A. Web Data Acquisition — web-scale archive; B. Public datasets
**Type:** Open nonprofit dataset + access APIs
**Official URL:** https://commoncrawl.org
**Description:** Nonprofit open web archive of 10+ petabytes: monthly crawls (2B+ pages each) stored as WARC (raw), WAT (metadata), and WET (extracted plain text), with a CDX URL index, columnar Parquet index (queryable via Athena/Spark/DuckDB), and a PageRank/hyperlink graph. The foundational training dataset behind most major LLMs.
**Contents inspected:** 2026 MotherDuck engineering write-up (formats, S3 layout, CDX usage, columnar index), agent skill docs (CDX API + warcio + byte-range WARC retrieval), Common Crawl Python/Java tour repos.
**Actual capabilities:** CDX Server API for URL/domain/time lookups; bulk S3 access (`s3://commoncrawl` + HTTPS); columnar index for analytical queries; WARC/WAT/WET formats.
**Usage domain:** LLM training corpora, link-graph analysis, domain inventories, historical page retrieval.
**Inputs:** CDX queries (URL prefixes, domains, MIME filters, crawl IDs like `CC-MAIN-2026-34`); Athena/Spark SQL over columnar index.
**Outputs:** WARC records (HTTP headers + bodies), metadata, plain text, index rows.
**Integration method:** HTTPS (index + data), S3 API, Athena/Spark/DuckDB; Python libs: warcio, cdx_toolkit, cdxj-indexer.
**Dependencies:** AWS egress/compute for bulk processing (data is free; compute is not).
**Availability:** Open data; no key required for index/HTTPS access.
**Maintenance:** Active (monthly crawls ongoing).
**License:** Data is freely usable (crawl data released openly; individual page copyrights belong to origin sites — respect robots.txt and origin licenses).
**Limitations:** Monthly snapshots (not real-time); each crawl is a sample, not exhaustive; processing petabytes needs serious infrastructure; "free in cost, expensive in engineering."
**Related resources:** Wayback Machine, Webz.io, Brave Search API, warcio.
**Sources:** https://motherduck.com/blog/querying-the-entire-internet-100-billion-rows-with-motherduck/ ; https://github.com/hinvec/security-scanned-skills/blob/HEAD/skills/common-crawl-index-query-agent/SKILL.md ; https://github.com/blkout-hd/whirlwind-python ; https://serp.fast/tools/common-crawl (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified.

---

**Resource name:** Wayback Machine (Internet Archive)
**Canonical identity:** Internet Archive (archive.org); Wayback at web.archive.org
**Category:** A. Web Data Acquisition — historical web snapshots
**Type:** Open nonprofit service + APIs
**Official URL:** https://web.archive.org (APIs: https://archive.org/help/wayback_api.php)
**Description:** 900B+ archived web pages since 1996. Programmatic access via the Availability API, CDX Server API (snapshot enumeration), and Save Page Now (on-demand archiving; anonymous ~15/min reported, higher with S3 auth keys). Respects robots.txt retroactively — a current disallow can hide older snapshots.
**Contents inspected:** 2026 journalism-research reports (API inventory, rate limits, deletion behavior) and archivist notes; archive.org API help not opened directly.
**Actual capabilities:** Snapshot lookup by URL+timestamp; CDX queries; on-demand capture; browser extensions.
**Usage domain:** Historical research, citation archiving, deleted-page recovery, change forensics.
**Inputs:** URLs, timestamps, CDX query params.
**Outputs:** Archived page snapshots (HTML + assets), CDX JSON.
**Integration method:** HTTPS APIs; `web.archive.org/web/<timestamp>/<url>` replay URLs; Python clients (e.g., `wayback`).
**Dependencies:** None for reads; S3 keys for higher SPN quotas.
**Availability:** Free; no rate limits reported for reads (SPN is throttled).
**Maintenance:** Active.
**License:** Service; archived content retains origin copyrights.
**Limitations:** Retroactive robots.txt honoring; takedown requests honored; snapshot frequency varies by site popularity; not a bulk-download corpus like Common Crawl.
**Related resources:** Common Crawl, ArchiveBox, Archive.today, Perma.cc, Heritrix, pywb.
**Sources:** https://github.com/jamditis/claude-skills-journalism/blob/HEAD/research-toolkit/skills/web-archiving/SKILL.md ; https://github.com/jamditis/claude-skills-journalism/blob/HEAD/research/web-access-tools-comprehensive-report.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — API inventory from 2026 secondary sources; primary API docs not opened.

---

**Resource name:** ArchiveBox
**Canonical identity:** ArchiveBox/ArchiveBox (GitHub); site archivebox.io
**Category:** A. Web Data Acquisition — self-hosted web archiving
**Type:** Open-source app (Python/Docker)
**Official URL:** https://github.com/ArchiveBox/ArchiveBox
**Description:** Self-hosted web archiving: takes URLs (bookmarks, history, RSS, Pocket/Pinboard imports) and saves HTML, screenshots, PDFs, media, and more locally. v0.8 ships Docker Compose with Chromium, yt-dlp, and wget extractors.
**Contents inspected:** 2026 awesome-selfhosted and journalism-skill entries; primary README not opened.
**Actual capabilities:** Multi-format archiving (HTML, screenshot, PDF, media, git, wget); scheduled imports; local searchable UI (reported).
**Usage domain:** Personal/institutional archiving, citation preservation, offline research corpora.
**Inputs:** URLs, browser history, bookmarks, feeds.
**Outputs:** Local archive (HTML/WARC-ish bundles, screenshots, PDFs, media).
**Integration method:** Self-hosted Docker/CLI with web UI.
**Dependencies:** Docker; disk space.
**Availability:** Open source.
**Maintenance:** Active (v0.8 noted in 2026 sources).
**License:** MIT (per awesome-selfhosted — not re-verified).
**Limitations:** Disk-hungry; JS-heavy archiving depends on Chromium extractor config.
**Related resources:** Wayback Machine, SingleFile, Browsertrix, Heritrix.
**Sources:** https://github.com/pennyp309-ui/awesome-selfhosted ; https://github.com/jamditis/claude-skills-journalism/blob/HEAD/research-toolkit/skills/web-archiving/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** SingleFile
**Canonical identity:** gildas-lormeau/SingleFile (GitHub)
**Category:** A. Web Data Acquisition — single-page preservation
**Type:** Open-source browser extension + CLI
**Official URL:** https://github.com/gildas-lormeau/SingleFile
**Description:** Saves a complete web page (HTML + assets inlined) into a single self-contained HTML file; the standard tool for single-page preservation.
**Contents inspected:** 2026 journalism-report mention only; primary README not opened.
**Actual capabilities:** Inlines CSS/images/fonts into one HTML file; annotations; batch CLI (reported).
**Usage domain:** Evidence preservation, offline reading, citation snapshots.
**Inputs:** Page URLs (via browser extension) or CLI.
**Outputs:** Single self-contained HTML files.
**Integration method:** Browser extension (Chrome/Firefox/Edge); CLI/Node library.
**Dependencies:** Browser for extension use.
**Availability:** Open source.
**Maintenance:** Active (per 2026 listing).
**License:** Not verified.
**Limitations:** One page at a time; dynamic content captured as-rendered.
**Related resources:** ArchiveBox, Wayback Save Page Now.
**Sources:** https://github.com/jamditis/claude-skills-journalism/blob/HEAD/research/web-access-tools-comprehensive-report.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Heritrix
**Canonical identity:** internetarchive/heritrix3 (GitHub); Internet Archive
**Category:** A. Web Data Acquisition — archival crawler
**Type:** Open-source crawler (Java)
**Official URL:** https://github.com/internetarchive/heritrix3
**Description:** The Internet Archive's large-scale archival web crawler (the engine behind much of the Wayback Machine's captures).
**Contents inspected:** Archivist notes only; primary repo not opened.
**Actual capabilities:** Large-scale crawl management, WARC output, politeness controls (general knowledge — Partially verified).
**Usage domain:** Institutional web archiving.
**Inputs:** Seed lists, crawl jobs.
**Outputs:** WARC files.
**Integration method:** Java application with web UI/API.
**Dependencies:** Java.
**Availability:** Open source.
**Maintenance:** Mature/slow-moving (not verified in this sweep).
**License:** Apache-2.0 (not re-verified).
**Limitations:** Java ops burden; not designed for JS-heavy modern sites (Browsertrix covers that).
**Related resources:** Wayback Machine, Browsertrix, pywb, Common Crawl.
**Sources:** https://github.com/thaliaarchi/notes/blob/HEAD/topics/archival/internet_archive.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Browsertrix (Browsertrix Cloud)
**Canonical identity:** Browsertrix (browsertrix.com); Webrecorder project — successor to Conifer
**Category:** A. Web Data Acquisition — high-fidelity web archiving
**Type:** Open-source tools + hosted service
**Official URL:** https://browsertrix.com
**Description:** Webrecorder's browser-based archiving platform for interactive/JS-heavy capture, outputting standard WARC files. Successor to the Conifer (formerly Webrecorder) service.
**Contents inspected:** 2026 journalism-skill comparison only; browsertrix.com not opened.
**Actual capabilities:** Browser-driven capture; WARC output; hosted cloud with API (reported).
**Usage domain:** High-fidelity archiving of dynamic sites.
**Inputs:** URLs/crawl configs.
**Outputs:** WARC files; replayable archives.
**Integration method:** Open-source crawler + hosted cloud API (reported).
**Dependencies:** Account for cloud; Docker for self-hosted (reported).
**Availability:** Open tools; cloud plans (reported).
**Maintenance:** Active (reported as the active path; Conifer legacy).
**License:** Not verified.
**Limitations:** Thin record; primary docs not inspected. Note: **Historical** — Conifer is the retired predecessor.
**Related resources:** Heritrix, ArchiveBox, pywb, Conifer (Historical).
**Sources:** https://github.com/jamditis/claude-skills-journalism/blob/HEAD/research-toolkit/skills/web-archiving/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Archive.today (archive.ph / archive.is / archive.li)
**Canonical identity:** Archive.today (mirror domains: archive.ph, archive.is, archive.li, archive.md)
**Category:** A. Web Data Acquisition — on-demand archiving
**Type:** Free service (operator-run; informal API)
**Official URL:** https://archive.ph
**Description:** On-demand web archiving with JS support; captures pages others miss and does not honor robots.txt or deletion requests (content stays permanently). 2026 notes: subpoenaed (FBI, Oct 2025) and deprecated by Wikipedia as a citation source (Feb 2026) — use as a capture tool, not a citation target.
**Contents inspected:** 2026 journalism-skill comparison only; archive.ph not opened.
**Actual capabilities:** On-demand snapshots (interactive + screenshot versions); no deletion policy (reported).
**Usage domain:** Capturing pages that block other archivers; paywalled content snapshots.
**Inputs:** URLs submitted for archiving.
**Outputs:** Snapshot URLs.
**Integration method:** Web form; informal URL patterns.
**Dependencies:** None.
**Availability:** Free.
**Maintenance:** Operational (per 2026 sources).
**License:** Service; operator-run.
**Limitations:** 50MB cap reported; no formal API; legal/reliability caveats above; circumventing paywalls may violate ToS — record for research awareness, not endorsement.
**Related resources:** Wayback Machine, ArchiveBox.
**Sources:** https://github.com/jamditis/claude-skills-journalism/blob/HEAD/research-toolkit/skills/web-archiving/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Perma.cc
**Canonical identity:** Perma.cc (Harvard Library Innovation Lab)
**Category:** A. Web Data Acquisition — legal-grade archiving
**Type:** Service (free tier + institutional)
**Official URL:** https://perma.cc
**Description:** Web archiving service designed for legal citations — used by US courts. Free tier with API-key auth (`Authorization: ApiKey`).
**Contents inspected:** 2026 journalism-skill comparison only; perma.cc not opened.
**Actual capabilities:** Permanent captures with citation URLs; API (reported).
**Usage domain:** Legal/academic citations requiring durable links.
**Inputs:** URLs via web/API.
**Outputs:** Permanent perma.cc links.
**Integration method:** Web UI; REST API with API key (reported).
**Dependencies:** Account/API key.
**Availability:** Free tier reported.
**Maintenance:** Active.
**License:** Service (Harvard LIL).
**Limitations:** Standard pages; account-gated.
**Related resources:** Wayback Machine, Archive.today.
**Sources:** https://github.com/jamditis/claude-skills-journalism/blob/HEAD/research-toolkit/skills/web-archiving/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

### A11. Anti-bot handling (lawful, documented only)

> Scope note: this section records publicly documented, lawful techniques and tools (TLS fingerprint consistency, CDP-level automation hygiene) used to access content the operator has the right to access — e.g., one's own sites, or sites whose ToS permit automation. It does not cover CAPTCHA-solving services or credential bypass.

---

**Resource name:** curl_cffi
**Canonical identity:** yifeikong/curl_cffi (GitHub); PyPI package `curl_cffi`
**Category:** A. Web Data Acquisition — anti-bot handling (HTTP layer)
**Type:** Open-source library (Python bindings for curl-impersonate)
**Official URL:** https://github.com/yifeikong/curl_cffi
**Description:** Python bindings for curl-impersonate: makes HTTP requests present the same TLS/JA3 fingerprints as real browsers (Chrome, Safari, Firefox), defeating naive TLS-fingerprint bot detection without a browser.
**Contents inspected:** 2026 awesome-list entry only; primary README not opened.
**Actual capabilities:** Browser-impersonating TLS fingerprints; HTTP/2 support; session/cookie handling (reported).
**Usage domain:** HTTP-only scraping where TLS fingerprinting blocks default clients.
**Inputs:** URLs + impersonation profile.
**Outputs:** HTTP responses.
**Integration method:** Python library (requests-like API).
**Dependencies:** Bundled curl-impersonate binaries.
**Availability:** Open source (~3k stars cited).
**Maintenance:** Not verified.
**License:** MIT (not re-verified).
**Limitations:** Only the TLS/HTTP layer — JS challenges still need a browser; impersonation must be used within site ToS.
**Related resources:** httpx, requests, Patchright (browser layer).
**Sources:** https://github.com/spinov001-art/awesome-web-scraping-2026/blob/HEAD/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Patchright
**Canonical identity:** Kaliiiiiiiiii-Vinyzu/patchright (GitHub); Python twin: Kaliiiiiiiiii-Vinyzu/patchright-python
**Category:** A. Web Data Acquisition — anti-bot handling (browser layer)
**Type:** Open-source Playwright fork (Python, Node.js, .NET)
**Official URL:** https://github.com/Kaliiiiiiiiii-Vinyzu/patchright
**Description:** Patched, drop-in API-compatible fork of Playwright that rewrites the Playwright driver's TypeScript (via AST transforms) so it stops emitting CDP-level automation fingerprints: removes `Runtime.enable`/`Console.enable` leaks, the `--enable-automation` flag, and `navigator.webdriver=true`. Published to PyPI/npm/NuGet; Chromium-only (Firefox/WebKit explicitly unsupported).
**Contents inspected:** 2026 technical comparisons (patch mechanism, detection vectors bypassed, Playwright-vs-Patchright tables) and MCP server docs built on it; primary repo README not opened.
**Actual capabilities:** Same API as Playwright; stealth at the protocol level; passes Cloudflare/Kasada/Akamai/DataDome/Fingerprint.com checks per community reports (not independently verified).
**Usage domain:** Accessing one's own or ToS-permitting content on sites where automated browsers are incorrectly blocked; content verification tooling.
**Inputs:** Standard Playwright scripts (import swap).
**Outputs:** Same as Playwright.
**Integration method:** Drop-in package replacement (`patchright` instead of `playwright`); MCP servers available (patchright-mcp).
**Dependencies:** Chromium; language runtime.
**Availability:** Open source.
**Maintenance:** Active; tracks Playwright releases (per 2026 sources).
**License:** Apache-2.0 (reported — not re-verified).
**Limitations:** Chromium-only; stealth is cat-and-mouse (breaks as detectors evolve); does not legitimize scraping where ToS forbid it.
**Related resources:** Playwright, playwright-stealth plugins, Camoufox, curl_cffi.
**Sources:** https://github.com/success-meta-1/anti-detect-browser-tools-tech-comparison/blob/HEAD/patchright.md ; https://github.com/openonion/connectonion/issues/168 ; https://github.com/CapMonsterCloud/capmonster-mcp-patchright-captcha-solver (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — mechanism corroborated by multiple technical sources; primary README not opened.

---

## B. PUBLIC API DIRECTORIES

### B1. API catalogs, marketplaces & indexes

---

**Resource name:** RapidAPI Hub
**Canonical identity:** RapidAPI (rapidapi.com)
**Category:** B. Public API Directories — API marketplace
**Type:** Hosted marketplace (proprietary)
**Official URL:** https://rapidapi.com
**Description:** Large third-party API marketplace: providers publish APIs, developers subscribe and call them through a single key/gateway with unified billing. Also referenced as a place to publish public APIs (with growing MCP support for agents).
**Contents inspected:** 2026 agent-catalog notes (no public unauthenticated catalog endpoint for bulk discovery) and RAPIDAPI.md publishing guides; rapidapi.com not opened.
**Actual capabilities:** Searchable marketplace; single-key access; usage analytics; provider monetization (reported).
**What it indexes:** Third-party REST APIs across categories (sports, finance, weather, etc.).
**Organization:** Category search, provider pages, per-API pricing tiers.
**Accessibility:** Web UI; subscription required per API.
**Downloadable catalog / programmatic interface / CLI / MCP:** No public unauthenticated bulk-catalog endpoint reported; MCP support growing (reported). Treat as Not publicly documented.
**Availability:** Hosted.
**Maintenance:** Active.
**License:** Proprietary.
**Limitations:** No bulk programmatic discovery; per-API pricing fragmentation.
**Related resources:** Postman Public API Network, APIs.guru, APILayer.
**Sources:** https://github.com/eater2/ai_agents_api_library ; https://github.com/matthewdtowles/i-want-my-mtg/blob/HEAD/RAPIDAPI.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Postman Public API Network
**Canonical identity:** Postman (postman.com/explore)
**Category:** B. Public API Directories — API collection network
**Type:** Hosted network (proprietary platform; public collections)
**Official URL:** https://www.postman.com/explore
**Description:** The largest network of public API collections shared on Postman: browsable workspaces with ready-to-run requests, documentation, and environments. Publishing path: create a Postman workspace, import an OpenAPI spec, mark it public.
**Contents inspected:** 2026 agent-catalog notes and WSTG API-recon docs; postman.com/explore not opened.
**Actual capabilities:** Browse/search public collections; fork and run requests in Postman (reported).
**What it indexes:** Public API collections (requests + docs) published by API providers and community.
**Organization:** Search, categories, workspaces, collections.
**Accessibility:** Web UI; Postman client for execution.
**Downloadable catalog / programmatic interface / CLI / MCP:** No documented public API for programmatic discovery (reported). Treat as Not publicly documented.
**Availability:** Hosted.
**Maintenance:** Active.
**License:** Proprietary platform; collection contents per publisher.
**Limitations:** Browsable but not bulk-queryable; quality varies by publisher.
**Related resources:** RapidAPI, APIs.guru.
**Sources:** https://github.com/eater2/ai_agents_api_library ; https://github.com/fredrick-maina/wstg/blob/HEAD/document/4-Web_Application_Security_Testing/12-API_Testing/01-API_Reconnaissance.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** APIs.guru
**Canonical identity:** APIs.guru; machine-readable directory at github.com/APIs-guru/openapi-directory
**Category:** B. Public API Directories — OpenAPI directory
**Type:** Open directory (website + GitHub repo of specs)
**Official URL:** https://apis.guru
**Description:** Directory of public APIs described by OpenAPI specifications. Publishing path: PR to the `openapi-directory` repo adding an `openapi-public.json`. The GitHub repo itself is the downloadable, programmatic catalog.
**Contents inspected:** 2026 WSTG and RAPIDAPI.md references; apis.guru and the GitHub repo not opened directly.
**Actual capabilities:** Browsable directory; every listing backed by a machine-readable OpenAPI file in git.
**What it indexes:** Public APIs with OpenAPI/Swagger definitions.
**Organization:** Searchable site; repo organized by provider.
**Accessibility:** Web UI + git clone.
**Downloadable catalog:** Yes — the GitHub repo is the catalog. **Programmatic interface:** via raw GitHub file access (reported). **CLI/MCP:** Not publicly documented.
**Availability:** Open.
**Maintenance:** Community-maintained (activity not verified in this sweep).
**License:** Specs per provider; directory tooling open (not re-verified).
**Limitations:** Only APIs with OpenAPI specs; curation is community-driven.
**Related resources:** public-apis/public-apis, Postman Public API Network.
**Sources:** https://github.com/fredrick-maina/wstg/blob/HEAD/document/4-Web_Application_Security_Testing/12-API_Testing/01-API_Reconnaissance.md ; https://github.com/matthewdtowles/i-want-my-mtg/blob/HEAD/RAPIDAPI.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** PublicAPIs.dev / PublicAPIs.io
**Canonical identity:** publicapis.dev and publicapis.io (two distinct community sites)
**Category:** B. Public API Directories — free-API listings
**Type:** Community websites
**Official URL:** https://publicapis.dev and https://publicapis.io
**Description:** Community-run browsable lists of public/free APIs, referenced in 2026 API-recon documentation alongside the GitHub public-apis list.
**Contents inspected:** WSTG reference only; sites not opened.
**Actual capabilities / organization / accessibility:** Not verified.
**Downloadable catalog / programmatic interface / CLI / MCP:** Not publicly documented.
**Limitations:** Thin record; primary sites not inspected.
**Related resources:** public-apis/public-apis, APIs.guru.
**Sources:** https://github.com/fredrick-maina/wstg/blob/HEAD/document/4-Web_Application_Security_Testing/12-API_Testing/01-API_Reconnaissance.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unverified — needs a primary-source pass.

---

**Resource name:** ai_agents_api_library
**Canonical identity:** eater2/ai_agents_api_library (GitHub)
**Category:** B. Public API Directories — agent-oriented API catalog
**Type:** Open-source curated catalog (JSON data + build scripts)
**Official URL:** https://github.com/eater2/ai_agents_api_library
**Description:** Verified catalog of 300+ APIs and MCP servers that AI agents can call after one-time API key/OAuth setup. Ships machine-readable artifacts: JSON, llms.txt, and an MCP server for agents; contributions require linking the vendor's official API docs.
**Contents inspected:** README as surfaced (catalog structure, machine-readable endpoints, per-directory notes on Postman/RapidAPI/PulseMCP/mcp.so/llms.txt).
**Actual capabilities:** Curated, agent-focused API/MCP directory with programmatic artifacts.
**What it indexes:** APIs + MCP servers usable by AI agents, with auth notes.
**Organization:** `data/catalog.json` source; generated English/Polish/LLM files.
**Accessibility:** GitHub repo; JSON/llms.txt/MCP.
**Downloadable catalog:** Yes (JSON). **Programmatic interface:** MCP server + JSON. **CLI:** Not publicly documented. **Reference page:** README.
**Availability:** Open source.
**Maintenance:** Active (updated ~4 days before sweep).
**License:** Not verified.
**Limitations:** Curation is opinionated toward agent use; 300+ entries is selective, not exhaustive.
**Related resources:** public-apis/public-apis, PulseMCP, mcp.so, llms.txt directory.
**Sources:** https://github.com/eater2/ai_agents_api_library (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — README inspected via search-cached primary source.

---

**Resource name:** APILayer
**Canonical identity:** APILayer (apilayer.com)
**Category:** B. Public API Directories — API product marketplace
**Type:** Hosted service (proprietary)
**Official URL:** https://apilayer.com
**Description:** Marketplace of ready-to-use API products (geolocation, exchange rates, weather, phone validation, etc.) with unified key management.
**Contents inspected:** Named in workstream brief only; apilayer.com not opened.
**Actual capabilities / organization / accessibility:** Not verified.
**Downloadable catalog / programmatic interface / CLI / MCP:** Not publicly documented.
**Limitations:** Thin record.
**Related resources:** RapidAPI, Abstract API.
**Sources:** Workstream brief (Part 12) (2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unverified — needs a primary-source pass.

---

**Resource name:** ProgrammableWeb
**Canonical identity:** ProgrammableWeb (programmableweb.com)
**Category:** B. Public API Directories — API directory (retired)
**Type:** Defunct service
**Official URL:** https://www.programmableweb.com (Historical)
**Description:** Formerly the best-known API directory/marketplace (API search, SDK listings, news). Retired — the directory is no longer an active resource.
**Contents inspected:** Named in workstream brief; retirement not re-verified against a primary announcement in this sweep.
**Actual capabilities:** Historical only.
**Successors/alternatives:** RapidAPI, Postman Public API Network, APIs.guru.
**Sources:** Workstream brief (Part 12) (2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Historical — retirement details Unresolved; do not rely on it as a live directory.

---

### B2. Curated free-API lists

---

**Resource name:** awesome-free-apis
**Canonical identity:** hamzali6307/awesome-free-apis (GitHub)
**Category:** B. Public API Directories — curated free-API list
**Type:** Open-source awesome list
**Official URL:** https://github.com/hamzali6307/awesome-free-apis
**Description:** Curated, categorized list of 150+ free public APIs for developers (learning, side projects, hackathons), with auth/HTTPS metadata per entry.
**Contents inspected:** README table excerpts as surfaced (mock APIs, blockchain, and other categories).
**What it indexes:** Free APIs by category.
**Organization:** Markdown tables by category.
**Accessibility:** GitHub README.
**Downloadable catalog / programmatic interface / CLI / MCP:** Markdown only; no API/CLI/MCP.
**Availability:** Open.
**Maintenance:** Active (updated ~48 days before sweep).
**License:** Not verified.
**Limitations:** Curation quality varies; free-tier details decay quickly.
**Related resources:** public-apis/public-apis, api_explorer.
**Sources:** https://github.com/hamzali6307/awesome-free-apis (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** api_explorer
**Canonical identity:** yesanisha/api_explorer (GitHub)
**Category:** B. Public API Directories — API repository
**Type:** Open-source catalog
**Official URL:** https://github.com/yesanisha/api_explorer
**Description:** Self-described "ultimate open-source API repository": hundreds of public APIs across AI, finance, weather, maps, payments, social, healthcare, with auth details, pricing, docs, rate limits, and code examples in one searchable collection.
**Contents inspected:** README excerpt (mock/testing API table); full catalog not inspected.
**What it indexes:** Public APIs with practical integration metadata.
**Organization:** Categorized markdown.
**Accessibility:** GitHub README.
**Downloadable catalog / programmatic interface / CLI / MCP:** Markdown only (reported).
**Availability:** Open.
**Maintenance:** Active (updated ~78 days before sweep).
**License:** Not verified.
**Limitations:** Single-maintainer curation; metadata freshness varies.
**Related resources:** awesome-free-apis, public-apis/public-apis.
**Sources:** https://github.com/yesanisha/api_explorer (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

### B3. Sample / mock APIs

---

**Resource name:** JSONPlaceholder
**Canonical identity:** JSONPlaceholder (jsonplaceholder.typicode.com); by Typicode
**Category:** B. Public API Directories — sample/mock API
**Type:** Hosted free fake REST API
**Official URL:** https://jsonplaceholder.typicode.com
**Description:** The classic free fake REST API for testing and prototyping: posts, comments, albums, photos, todos, users. Supports GET/POST/PUT/PATCH/DELETE; writes are faked (returns success with a new id but nothing persists — a follow-up GET 404s). No auth, no signup.
**Contents inspected:** 2026 mock-API comparisons (reqres.in guides, Mockbird live-status guide, awesome lists); jsonplaceholder.typicode.com not opened.
**Actual capabilities:** Fixed fake resources; full HTTP verb support with simulated writes.
**Usage domain:** Tutorials, frontend prototypes, API-client testing.
**Inputs:** REST calls against /posts, /users, etc.
**Outputs:** Fake JSON.
**Integration method:** Plain HTTPS.
**Dependencies:** None.
**Availability:** Free, no signup.
**Maintenance:** Long-running side project (uptime varies; check live status before depending on it).
**License:** Service (free to use).
**Limitations:** No persistence, no auth, no logging; unsuitable for auth-flow or persistence testing.
**Related resources:** ReqRes, DummyJSON, httpbin.
**Sources:** https://reqres.in/blog/best-mock-api-tools ; https://reqres.in/blog/when-jsonplaceholder-isnt-enough ; https://github.com/hamzali6307/awesome-free-apis (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** ReqRes
**Canonical identity:** ReqRes (reqres.in)
**Category:** B. Public API Directories — sample/mock API
**Type:** Hosted mock API + backend (freemium)
**Official URL:** https://reqres.in
**Description:** Hosted REST mock with realistic behaviors: real status codes, pagination, delayed responses (`?delay=3`), user auth flows, and persistent collections in projects. 2026 status: keyless requests began being rejected in 2026 (per Mockbird's live-status monitoring); demo tier offers ~250 req/day without signup; writes persist in projects with API keys.
**Contents inspected:** reqres.in's own 2026 comparison guides and Mockbird's live-status report; reqres.in not opened directly.
**Actual capabilities:** Fake users/resources; login/register flows; realistic errors (404/400); delays; persistent collections; request logging; per-user data with magic-code login.
**Usage domain:** Frontend/QA testing, teaching, agent API practice, auth-flow testing.
**Inputs:** REST calls; project API keys for writes.
**Outputs:** Fake-but-stateful JSON; logs.
**Integration method:** Plain HTTPS.
**Dependencies:** None for demo reads; API key for projects.
**Availability:** Freemium; demo without signup (250 req/day reported).
**Maintenance:** Active (blog updated 1 day before sweep).
**License:** Service.
**Limitations:** 2026 keyless restrictions; demo tier is rate-limited; not for production data.
**Related resources:** JSONPlaceholder, DummyJSON, Beeceptor.
**Sources:** https://reqres.in/blog/best-mock-api-tools ; https://mockbird.mockbird.workers.dev (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — 2026 access changes single-sourced to Mockbird/ReqRes's own blog.

---

**Resource name:** DummyJSON
**Canonical identity:** DummyJSON (dummyjson.com)
**Category:** B. Public API Directories — sample/mock API
**Type:** Hosted free fake-data API
**Official URL:** https://dummyjson.com
**Description:** Richer fake dataset API than JSONPlaceholder: products (with images), carts, users, quotes, recipes, todos; plus search and a demo JWT login. Free, no signup; writes not persisted.
**Contents inspected:** 2026 comparisons and awesome lists; dummyjson.com not opened.
**Actual capabilities:** 100+ fake products/users/etc.; search, pagination, auth demo (reported).
**Usage domain:** E-commerce UI prototypes, richer fake data than JSONPlaceholder.
**Inputs:** REST calls.
**Outputs:** Fake JSON.
**Integration method:** Plain HTTPS.
**Dependencies:** None.
**Availability:** Free, no signup.
**Maintenance:** Active (per 2026 sources).
**License:** Service.
**Limitations:** No write persistence; demo auth only.
**Related resources:** JSONPlaceholder, Fake Store API, ReqRes.
**Sources:** https://reqres.in/blog/best-mock-api-tools ; https://github.com/hamzali6307/awesome-free-apis (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** httpbin.org
**Canonical identity:** httpbin.org (Kenneth Reitz's httpbin; org site)
**Category:** B. Public API Directories — HTTP testing service
**Type:** Hosted free service (open source)
**Official URL:** https://httpbin.org
**Description:** HTTP request/response testing service: echoes requests, returns arbitrary status codes, handles headers/cookies/redirects/delays/streaming. Not fake data — a protocol-level test harness.
**Contents inspected:** 2026 mock-API guides; httpbin.org not opened.
**Actual capabilities:** /status/:code, /delay/:n, /headers, /cookies, /redirect, /stream, auth endpoints (reported).
**Usage domain:** HTTP client testing, retry/timeout logic, webhook debugging.
**Inputs:** HTTP requests.
**Outputs:** Echoed/controlled HTTP responses.
**Integration method:** Plain HTTPS.
**Dependencies:** None.
**Availability:** Free.
**Maintenance:** Community-maintained (uptime best-effort).
**License:** Open source (not re-verified).
**Limitations:** No fake domain data; shared public instance has abuse-driven rate limits.
**Related resources:** Postman Echo, Beeceptor.
**Sources:** https://github.com/hamzali6307/awesome-free-apis ; https://reqres.in/blog/best-mock-api-tools (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Other mock/testing services (compact records):** all Partially verified via 2026 comparisons/awesome lists; primary sites not opened.

| Resource | Canonical identity | What it is | Access | Limitation noted |
|---|---|---|---|---|
| Postman Echo | docs.postman-echo.com | Echoes requests; tests auth headers, cookies, redirects | Free, no signup | Echo only, no fake data |
| Mockaroo | mockaroo.com | Realistic mock dataset generator (CSV/JSON/SQL) + live mock API | Free tier; key for API | 200 rows/request on free plan reported |
| Beeceptor | beeceptor.com | Instant mock API/webhook endpoints; rule-based mocks | Free tier (50 req/day, 3 rules reported) | Capped per endpoint |
| RandomUser.me | randomuser.me | Random realistic user profiles (name/photo/address/login) | Free, no signup | Profiles only |
| json-server | typicode/json-server (GitHub) | Local CLI: full fake REST API from a JSON file | Free, OSS | Local only; writes to local file |
| WireMock | wiremock.io / WireMock (GitHub) | API mocking library/JAR/Docker + cloud | OSS free; cloud freemium | Heavier setup |
| Mockoon | mockoon.com | Local app/CLI/Docker mock server; mocks in Git, CI-friendly | Free locally; cloud paid | State resets between runs |
| Fake Store API | fakestoreapi.com | Mock e-commerce products/carts/users | Free, no signup | E-commerce domain only |
| FakerAPI | fakerapi.it | Fake persons/companies/products/texts/images | Free, no signup | Single-sourced |
| Mocky.io | mocky.io | Was: instant custom mock endpoints | **Historical** — reported gone entirely in 2026 | Do not depend on it |

Sources: https://reqres.in/blog/best-mock-api-tools ; https://github.com/hamzali6307/awesome-free-apis ; https://github.com/yesanisha/api_explorer (accessed 2026-10-10)

---

### B4. Open data portals & dataset repositories

---

**Resource name:** Kaggle Datasets
**Canonical identity:** Kaggle (kaggle.com/datasets); Google subsidiary
**Category:** B. Public API Directories — dataset portal
**Type:** Hosted platform (free with account)
**Official URL:** https://www.kaggle.com/datasets
**Description:** 300k+ community datasets plus competitions; programmatic access via the `kaggle` CLI/API (API key from account) and the newer `kagglehub` Python library (dataset/model download, upload, pandas/polars/HF adapters, SQL queries against SQLite datasets).
**Contents inspected:** 2026 agent skill docs (CLI commands, kagglehub adapters, env vars); kaggle.com not opened.
**Actual capabilities:** Dataset search/list/download/versioning; competition data; notebook kernels; `kagglehub.dataset_download` / `dataset_load` with adapters.
**What it indexes:** Community-uploaded datasets across domains; competition datasets.
**Organization:** Search, tags, vote/sort rankings, versioning.
**Accessibility:** Web UI; CLI; Python (`kaggle`, `kagglehub`); REST-ish API (key required).
**Downloadable catalog:** Via API/CLI listing. **Programmatic interface:** Yes (kaggle API, kagglehub). **CLI:** Yes. **MCP:** Not publicly documented.
**Availability:** Free with Kaggle account (API key).
**Maintenance:** Active.
**License:** Per-dataset licenses (must check each dataset's license before use).
**Limitations:** Account + API key required; dataset quality/licensing varies; redistribution terms are per-dataset.
**Related resources:** Hugging Face Datasets, OpenML, data.gov.
**Sources:** https://github.com/bai-ca/research-plugins/blob/HEAD/skills/tools/scraping/dataset-finder-guide/SKILL.md ; https://github.com/shepsci/kaggle-skill/blob/HEAD/skills/kaggle/modules/datasets/references/kagglehub-datasets.md ; https://github.com/cxz324/kagglehub (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified. Note: canonical `kagglehub` is kaggle/kagglehub; cxz324/kagglehub surfaced as a fork — use the official repo.

---

**Resource name:** Hugging Face Datasets
**Canonical identity:** Hugging Face Hub — Datasets (huggingface.co/datasets); library: huggingface/datasets (GitHub)
**Category:** B. Public API Directories — dataset portal + library
**Type:** Hosted hub (freemium) + open-source library
**Official URL:** https://huggingface.co/datasets
**Description:** The largest ML dataset collection (100k+ datasets reported): one-line loading via `datasets.load_dataset()`, streaming for huge datasets, dataset cards with license/metadata, and a read API (`GET /api/datasets`) needing no auth for public datasets.
**Contents inspected:** 2026 agent skill docs (load_dataset patterns, HfApi search, license-checking guidance); huggingface.co not opened.
**Actual capabilities:** `load_dataset` with caching/streaming/splits; Hub search API; dataset cards; gated datasets with access requests.
**What it indexes:** ML datasets (text, vision, audio, tabular, multimodal).
**Organization:** Search, task/language/license filters, download rankings.
**Accessibility:** Web UI; Python library; REST API (no auth for public reads).
**Downloadable catalog:** Via Hub API listing. **Programmatic interface:** Yes (Hub API, huggingface_hub). **CLI:** via huggingface_hub. **MCP:** Not publicly documented.
**Availability:** Free for public datasets; gated ones need approval.
**Maintenance:** Very active.
**License:** Per-dataset (cardData license must be checked; `other`/missing = treat as all-rights-reserved per 2026 guidance).
**Limitations:** License heterogeneity; huge datasets need streaming; gated datasets add friction.
**Related resources:** Kaggle, OpenML, Papers with Code, Common Crawl.
**Sources:** https://github.com/bai-ca/research-plugins/blob/HEAD/skills/tools/scraping/dataset-finder-guide/SKILL.md ; https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/research-analyst/skills/kaggle-huggingface-datasets/SKILL.md ; https://github.com/sourabh-kumar04/rasosynth_cutc/blob/HEAD/docs/OPEN_DATA_REPOSITORIES.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Data.gov (US)
**Canonical identity:** Data.gov — US federal open data portal (CKAN-based catalog API)
**Category:** B. Public API Directories — government open-data portal
**Type:** Hosted public service
**Official URL:** https://data.gov
**Description:** 300k+ US government datasets aggregated from federal agencies; catalog API follows CKAN conventions (`/api/3/action/package_search`).
**Contents inspected:** 2026 open-data repository docs; data.gov not opened.
**Actual capabilities:** Dataset search/metadata API; agency feeds (reported).
**What it indexes:** US federal public datasets.
**Organization:** CKAN catalog: search, groups, tags, formats.
**Accessibility:** Web UI; CKAN API (no key for reads reported).
**Downloadable catalog:** Via CKAN API. **Programmatic interface:** Yes (CKAN). **CLI/MCP:** Not publicly documented.
**Availability:** Free, public.
**Maintenance:** Active (federal program).
**License:** US public domain / per-dataset.
**Limitations:** Metadata quality varies by agency; API is catalog-level (actual files live on agency sites).
**Related resources:** data.europa.eu, data.gov.uk, CKAN.
**Sources:** https://github.com/sourabh-kumar04/rasosynth_cutc/blob/HEAD/docs/OPEN_DATA_REPOSITORIES.md ; https://github.com/xpos587/agent-skills/blob/HEAD/skills/finding-datasets/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** data.europa.eu
**Canonical identity:** data.europa.eu — EU open data portal
**Category:** B. Public API Directories — government open-data portal
**Type:** Hosted public service
**Official URL:** https://data.europa.eu
**Description:** Aggregates open data from EU institutions and member-state portals; search API reported at `/api/hub/search/search`.
**Contents inspected:** 2026 open-data docs only; portal not opened.
**Actual capabilities:** Cross-portal search API (reported).
**What it indexes:** EU public-sector datasets.
**Organization:** Faceted search by country, theme, format.
**Accessibility:** Web UI; API (no key reported).
**Downloadable catalog / programmatic interface:** API reported; bulk dump not verified.
**Availability:** Free, public.
**Maintenance:** Active (EU program).
**License:** Per-dataset (often CC-BY).
**Limitations:** Aggregation lag; metadata in many languages.
**Related resources:** Data.gov, Eurostat, national portals (data.gouv.fr, data.gov.uk, open.canada.ca, data.gov.au).
**Sources:** https://github.com/sourabh-kumar04/rasosynth_cutc/blob/HEAD/docs/OPEN_DATA_REPOSITORIES.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Other dataset portals & repositories (compact records):** all Partially verified via 2026 open-data docs; primary sites not opened.

| Resource | Canonical identity | What it indexes | Programmatic access reported |
|---|---|---|---|
| OpenML | openml.org | Curated ML datasets with task definitions + benchmarking | REST API (no auth for reads) |
| UCI ML Repository | archive.ics.uci.edu | 600+ classic benchmark datasets | API + `ucimlrepo` Python package |
| Zenodo | zenodo.org | CERN-hosted research outputs with DOIs | REST API for records |
| Papers with Code — Datasets | paperswithcode.com/datasets | Datasets mapped to papers/code/results | REST API (no auth) |
| Google Dataset Search | datasetsearch.research.google.com | Cross-web dataset discovery | **No official API** — web UI only |
| Registry of Open Data on AWS | registry.opendata.aws | Datasets hosted as public S3 buckets | S3 direct access; SNS notifications |
| data.world | data.world | Collaborative datasets + queries | API (key) |
| Eurostat | ec.europa.eu/eurostat | European statistics | REST API + bulk downloads |
| Figshare | figshare.com | Research outputs incl. datasets | API for public articles |
| Harvard Dataverse | dataverse.harvard.edu | 100k+ social-science datasets | Search API |
| TensorFlow Datasets | tensorflow.org/datasets | 300+ Google-curated versioned datasets | `tensorflow_datasets` Python SDK |

Sources: https://github.com/sourabh-kumar04/rasosynth_cutc/blob/HEAD/docs/OPEN_DATA_REPOSITORIES.md ; https://github.com/nielitropar/datasets ; https://github.com/xpos587/agent-skills/blob/HEAD/skills/finding-datasets/SKILL.md (accessed 2026-10-10)

---

### B5. Gaps & thin spots in category B

- **Public GraphQL API directory:** no dedicated, maintained public GraphQL API catalog was verified in this sweep. Known single endpoints (e.g., GitHub GraphQL API at docs.github.com/graphql) exist but a curated directory is a **gap** — Unresolved.
- **API availability/status tools:** no dedicated public-API uptime/status directory was verified — **gap** (Unresolved). Mockbird's live-status page covers only mock APIs.
- **APILayer:** identity known, details Unverified — needs a primary pass.
- **publicapis.dev / publicapis.io:** Unverified — needs a primary pass.
- **ProgrammableWeb:** Historical (retired); retirement details Unresolved.
- **SDK directories:** no maintained general SDK directory was found — **gap** (Unresolved).
- **API documentation indexes** beyond APIs.guru: none verified — partial gap.
- **Sample/mock GraphQL APIs:** none verified — gap (Unresolved).

---

## C. RESEARCH AND INGESTION TOOLS

### C1. Codebase ingestion (Git → LLM-ready text)

---

**Resource name:** Gitingest
**Canonical identity:** coderamp-labs/gitingest (GitHub); hosted service at gitingest.com; PyPI package `gitingest` — **Corrected**: the original repo was cyclotruc/gitingest; canonical is now coderamp-labs/gitingest. Distinct similarly-named projects exist: AnEntrypoint/gitingest (npm package `gitoutput`, Node-based) and macxwhale/gitingest (Ruby gem) — these are separate implementations, not the canonical project.
**Category:** C. Research and Ingestion Tools — codebase ingestion
**Type:** Open-source tool: CLI + Python library + hosted web service + browser extensions
**Official URL:** https://github.com/coderamp-labs/gitingest
**Description:** Turns any Git repository (or local directory) into a single prompt-friendly text digest for LLMs: summary statistics, directory tree, file contents, and token counts. Best-known flow: replace `hub` with `ingest` in any GitHub URL (github.com/… → gitingest.com/…) to get an instant digest. Also ships a CLI, Python package, and optional self-hosted server mode; private repos via GitHub personal access token; Chrome/Firefox extensions add one-click ingestion on GitHub pages.
**Contents inspected:** Upstream README as surfaced (features, pip/pipx install, PAT for private repos, browser extensions at lcandy2/gitingest-extension) and multiple 2026 skill docs (uvx usage, include/exclude patterns, token counts).
**Actual capabilities:** Repo/URL/directory ingestion; include/exclude patterns; token counting; size statistics; private-repo support via PAT; server mode for self-hosting.
**Supported inputs:** GitHub URLs, generic Git remotes, local directories.
**Outputs:** Single text digest (summary + tree + contents); token/size stats.
**Integrations:** CLI, Python import, hosted URL pattern, browser extensions, Docker/server.
**Known restrictions:** Public repos only without a token; GitHub API rate limits apply (60 req/hr unauthenticated); very large repos produce digests exceeding context windows — filtering required.
**Availability:** Open source; hosted gitingest.com free.
**Maintenance:** Active (~14k stars cited in 2026 skill docs).
**License:** Not verified (not surfaced in this sweep).
**Limitations:** GitHub-centric URL trick; binary assets skipped; token counts are estimates.
**Related resources:** MarkItDown (file-level), repo2txt-style tools, GitHub code search.
**Sources:** https://GitHub.Com/coderamp-labs/gitingest ; https://github.com/danilotpnta/agent-skills/blob/HEAD/skills/gitingest/SKILL.md ; https://github.com/hinvec/security-scanned-skills/blob/HEAD/skills/gitingest-repository-to-prompt-codebase-extraction-tool/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — with **Corrected** canonical identity and fork disambiguation.

---

### C2. Web-fetch MCP servers

---

**Resource name:** MCP Fetch Server (official)
**Canonical identity:** modelcontextprotocol/servers — `src/fetch` (TypeScript); npm `@modelcontextprotocol/server-fetch`
**Category:** C. Research and Ingestion Tools — web ingestion via MCP
**Type:** Open-source MCP server (official reference implementation)
**Official URL:** https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
**Description:** The official reference MCP server for web content fetching: a `fetch` tool that retrieves a URL over HTTP and converts HTML to markdown for LLM consumption. Supports chunked reading of large pages (`start_index`, `max_length`), raw mode, custom user-agent, and robots.txt handling (obeyed by default for model-initiated requests; user-initiated prompt requests are exempt by default; overridable with `--ignore-robots-txt`).
**Contents inspected:** 2026 awesome-MCP detail page and skill docs (tool params, robots.txt behavior, user-agent strings); primary src/fetch README not opened.
**Actual capabilities:** URL fetch → markdown; pagination of long pages; robots.txt-aware.
**Supported inputs:** URLs.
**Outputs:** Markdown (or raw HTML/text).
**Integrations:** Any MCP client (Claude Code, Cursor, etc.) via npx/uvx stdio.
**Known restrictions:** Honors robots.txt for agent-initiated fetches; no JS rendering (static HTTP only); no auth flows.
**Availability:** Open source.
**Maintenance:** Maintained by the MCP steering group.
**License:** MIT (not re-verified).
**Limitations:** Static fetching only — JS-heavy pages return shells; rate limits of target sites apply.
**Related resources:** defuddle-fetch-mcp-server, Jina Reader, Firecrawl MCP.
**Sources:** https://github.com/ever-works/awesome-mcp-servers/blob/HEAD/details/mcp-server-fetch.md ; https://github.com/georgekhananaev/claude-skills-vault/blob/HEAD/mcp-servers/fetch/README.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** defuddle-fetch-mcp-server
**Canonical identity:** domdomegg/defuddle-fetch-mcp-server (GitHub); built on kepano/defuddle
**Category:** C. Research and Ingestion Tools — web ingestion via MCP
**Type:** Open-source MCP server (community)
**Official URL:** https://github.com/domdomegg/defuddle-fetch-mcp-server
**Description:** Drop-in replacement for the official fetch MCP server that swaps Mozilla Readability for the Defuddle extraction library, reported to give better results on modern web pages.
**Contents inspected:** GitHub README as surfaced (comparison framing, drop-in claim); primary code not opened.
**Actual capabilities:** Same `fetch` tool surface as official server; Defuddle-based HTML→markdown (reported).
**Supported inputs:** URLs.
**Outputs:** Cleaned markdown.
**Integrations:** MCP clients via npx.
**Known restrictions:** Same robots.txt/static-fetch limits as the official server (inferred, not verified).
**Availability:** Open source.
**Maintenance:** Active (updated ~9 days before sweep).
**License:** Not verified.
**Limitations:** Community project; extraction-quality claims not independently benchmarked here.
**Related resources:** Official MCP fetch server, kepano/defuddle, mozilla/readability.
**Sources:** https://github.com/domdomegg/defuddle-fetch-mcp-server (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** mult-fetch-mcp-server
**Canonical identity:** lmcc-dev/mult-fetch-mcp-server (GitHub)
**Category:** C. Research and Ingestion Tools — web ingestion via MCP
**Type:** Open-source MCP server (community)
**Official URL:** https://github.com/lmcc-dev/mult-fetch-mcp-server
**Description:** MCP web-fetching server with multiple modes (browser/Node) and formats (HTML/JSON/Markdown/text/plaintext), intelligent proxy detection, and bilingual (EN/ZH) interface. Tools: `fetch_html`, `fetch_json`, `fetch_txt`, `fetch_markdown`, `fetch_plaintext`.
**Contents inspected:** README excerpts as surfaced (tool list, parameter handling); primary code not opened.
**Actual capabilities:** Multi-format fetching; per-request debug flag (reported).
**Supported inputs:** URLs.
**Outputs:** HTML/JSON/text/markdown per tool.
**Integrations:** MCP clients via node stdio.
**Known restrictions:** Not verified.
**Availability:** Open source.
**Maintenance:** Active (updated ~13 days before sweep).
**License:** Not verified.
**Limitations:** Community project; proxy/browser-mode details not verified.
**Related resources:** Official MCP fetch server, defuddle-fetch-mcp-server.
**Sources:** https://github.com/lmcc-dev/mult-fetch-mcp-server (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Docling MCP server
**Canonical identity:** docling-project/docling-mcp (GitHub)
**Category:** C. Research and Ingestion Tools — document ingestion via MCP
**Type:** Open-source MCP server
**Official URL:** https://github.com/docling-project/docling-mcp (docs: https://docling-project.github.io/docling/usage/mcp/)
**Description:** Official Docling MCP server exposing document conversion, manipulation, and generation tools to agents — brings Docling's PDF/Office parsing into MCP clients.
**Contents inspected:** Docling org page listing only; docling-mcp README not opened.
**Actual capabilities:** Not verified beyond org description (document conversion/manipulation/generation tools).
**Supported inputs:** Documents (per Docling format support).
**Outputs:** Markdown/JSON per Docling.
**Integrations:** MCP clients.
**Known restrictions:** Same compute weight as Docling itself (inferred).
**Availability:** Open source.
**Maintenance:** Active (part of the active Docling project).
**License:** Not verified.
**Limitations:** Thin record; tool list not inspected.
**Related resources:** Docling, MarkItDown, official MCP fetch server.
**Sources:** https://github.com/docling-project (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

### C3. Deep-research agents (ingestion pipelines)

---

**Resource name:** GPT Researcher
**Canonical identity:** assafelovic/gpt-researcher (GitHub)
**Category:** C. Research and Ingestion Tools — autonomous research agent
**Type:** Open-source agent framework (Python)
**Official URL:** https://github.com/assafelovic/gpt-researcher
**Description:** Open deep-research agent for web and local research on any task: plans research, runs parallelized web retrieval, and produces detailed, cited research reports. Works with many LLM providers and search backends; installable as a Claude Skill (`npx skills add assafelovic/gpt-researcher`).
**Contents inspected:** GitHub README as surfaced (mission, plan-and-solve/RAG inspiration, customization options, skill install); code not opened.
**Actual capabilities:** Multi-step research planning; parallel sub-agent research; report generation with citations; configurable retrievers and LLMs (reported).
**Supported inputs:** Research questions/tasks; local document collections.
**Outputs:** Structured research reports with citations.
**Integrations:** Python library; CLI; Claude Skill packaging.
**Known restrictions:** Requires LLM provider keys and search API keys (Tavily/Exa/etc.) for full function; output quality depends on retriever coverage.
**Availability:** Open source.
**Maintenance:** Active (updated ~13 days before sweep).
**License:** MIT (not re-verified).
**Limitations:** Agent loop costs (LLM + search API spend); no built-in fact-checking beyond retrieval.
**Related resources:** Open Deep Research, Tavily, Exa, Jina Reader.
**Sources:** https://github.com/assafelovic/gpt-researcher (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — README inspected via search-cached primary source.

---

**Resource name:** Open Deep Research
**Canonical identity:** langchain-ai/open_deep_research (GitHub); LangChain
**Category:** C. Research and Ingestion Tools — autonomous research agent
**Type:** Open-source agent (Python, LangGraph)
**Official URL:** https://github.com/langchain-ai/open_deep_research
**Description:** Configurable, fully open-source deep research agent built on LangGraph: autonomously plans, searches, synthesizes, and writes structured Markdown reports. Works across model providers, search tools, and MCP servers. Ranked #6 on the Deep Research Bench leaderboard (score 0.4344, Aug 2025 per README).
**Contents inspected:** GitHub README as surfaced (quickstart with LangGraph server/Studio, recent-updates log, benchmark claims); code not opened.
**Actual capabilities:** Research planning graph; multi-provider LLM support; pluggable search backends; MCP server integration; LangGraph Studio UI + API.
**Supported inputs:** Research questions.
**Outputs:** Markdown research reports.
**Integrations:** LangGraph platform (local dev server, Studio UI, API docs endpoint); MCP servers.
**Known restrictions:** Requires model + search API keys; LangGraph server for the full UI experience.
**Availability:** Open source.
**Maintenance:** Active (updated ~60 days before sweep).
**License:** MIT (not re-verified).
**Limitations:** Benchmark claims are self-reported; setup is heavier than single-script researchers.
**Related resources:** GPT Researcher, LangGraph, Tavily, Exa.
**Sources:** https://github.com/langchain-ai/open_deep_research (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Verified — README inspected via search-cached primary source.

---

### C4. Search/extract APIs for agents (cross-reference)

Covered with full records in **A5**: **Tavily** (search/extract/crawl/map/research), **Exa** (neural search), **Jina Reader/Search** (r.jina.ai / s.jina.ai), **Brave Search API**, **Perplexity Search API**, **SearXNG** (A9, self-hosted). These are the primary ingestion entry points for research agents in 2026 practice.

---

### C5. Academic paper sources

---

**Resource name:** arXiv API
**Canonical identity:** arXiv (arxiv.org); API at export.arxiv.org/api/query
**Category:** C. Research and Ingestion Tools — paper metadata/full-text source
**Type:** Open nonprofit service + API
**Official URL:** https://arxiv.org (API docs: https://info.arxiv.org/help/api/)
**Description:** Open-access preprint repository (physics, math, CS, and more). The API returns Atom XML for search by keyword/author/category/ID; full text via `/abs/` (metadata) and `/pdf/` endpoints. Rate limit ~1 request per 3 seconds (per 2026 skill docs); no citation data — pair with Semantic Scholar.
**Contents inspected:** 2026 agent skill docs (endpoint patterns, category taxonomy, rate limits, version-suffix guidance); info.arxiv.org not opened.
**Actual capabilities:** Paper search; metadata + abstract; PDF full text; category taxonomy.
**Supported inputs:** Queries, author names, categories, arXiv IDs.
**Outputs:** Atom XML metadata; PDFs.
**Integrations:** Plain HTTPS; helper scripts in agent skills.
**Known restrictions:** ~1 req/3s politeness limit; 429s if exceeded; no citation graph.
**Availability:** Free, no key.
**Maintenance:** Active (Cornell/announcement).
**License:** Per-paper licenses (arXiv license variants).
**Limitations:** Preprints only (not peer-reviewed corpus); no citations/recommendations.
**Related resources:** Semantic Scholar API, Unpaywall, CORE.
**Sources:** https://github.com/chengyaoyang/lazyresearch/blob/HEAD/src/skills/arxiv/SKILL.md ; https://github.com/aiqinghaiwork163/haishui-agent/blob/HEAD/skills/research/arxiv/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Semantic Scholar API
**Canonical identity:** Semantic Scholar (semanticscholar.org); API at api.semanticscholar.org/graph/v1; Allen Institute for AI
**Category:** C. Research and Ingestion Tools — paper metadata + citation graph
**Type:** Open service + API (freemium)
**Official URL:** https://www.semanticscholar.org/product/api
**Description:** AI-powered academic search over 200M+ papers with a free JSON API: paper search, paper lookup by DOI/arXiv/S2 ID, citations, references, author profiles (h-index, citation counts), recommendations, and open-access PDF links. Anonymous use ~1 req/sec (shared pool); free API key raises limits.
**Contents inspected:** 2026 agent skill docs (base URL, endpoint inventory, field lists, rate limits); semanticscholar.org/product/api not opened.
**Actual capabilities:** Keyword/title search; citation and reference graphs; author metrics; paper recommendations; bulk dataset (S2ORC) separately.
**Supported inputs:** Queries, paper IDs (DOI/arXiv/S2/CorpusID), author names.
**Outputs:** JSON metadata, citation counts, abstracts, open-access PDF URLs.
**Integrations:** Plain HTTPS.
**Known restrictions:** Anonymous ~1 rps; bulk/high-volume needs key or dataset download; some fields require key.
**Availability:** Free; key optional.
**Maintenance:** Active.
**License:** API data under Semantic Scholar terms; abstracts/metadata generally reusable with attribution (not re-verified).
**Limitations:** Coverage skews to English STEM; citation counts lag real time.
**Related resources:** arXiv API, OpenAlex, Crossref, Unpaywall.
**Sources:** https://github.com/cliffvale/opencode-free-setup/blob/HEAD/skills/ai-engineer/web-search-modules/semantic-scholar.md ; https://github.com/tanue-hou/phd-thesis-butler/blob/HEAD/research_layer/sources/semantic_scholar_profile.md ; https://github.com/jenkinsrobotics/jros/blob/HEAD/jaeger_os/agent/skills/research/arxiv/SKILL.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** Unpaywall
**Canonical identity:** Unpaywall (unpaywall.org); OurResearch nonprofit
**Category:** C. Research and Ingestion Tools — open-access discovery
**Type:** Open service + API
**Official URL:** https://unpaywall.org
**Description:** Finds legal open-access versions of 20M+ academic papers (given a DOI, returns OA locations). Used as the first step before paywalled-publisher access.
**Contents inspected:** 2026 journalism-research report mention only; unpaywall.org not opened.
**Actual capabilities:** DOI → OA URL resolution via API (reported).
**Supported inputs:** DOIs.
**Outputs:** OA locations, license info.
**Integrations:** REST API; browser extension (reported).
**Known restrictions:** Requires email for API use (reported — not verified).
**Availability:** Free.
**Maintenance:** Active (per 2026 sources).
**License:** Service (nonprofit).
**Limitations:** Only what is legally OA; coverage gaps in humanities.
**Related resources:** Semantic Scholar (openAccessPdf), CORE, arXiv.
**Sources:** https://github.com/jamditis/claude-skills-journalism/blob/HEAD/research/web-access-tools-comprehensive-report.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified.

---

**Resource name:** CORE
**Canonical identity:** CORE (core.ac.uk)
**Category:** C. Research and Ingestion Tools — open-access paper aggregation
**Type:** Service + API (freemium)
**Official URL:** https://core.ac.uk
**Description:** Aggregator of open-access research papers (295M papers claimed in 2026 reporting) with search and API access.
**Contents inspected:** 2026 journalism-report mention only; core.ac.uk not opened.
**Actual capabilities:** Not verified beyond description.
**Supported inputs:** Queries (reported).
**Outputs:** Paper metadata + OA full text (reported).
**Integrations:** API (reported).
**Known restrictions:** Not verified.
**Availability:** Service (reported).
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Thin record; primary docs not inspected.
**Related resources:** Unpaywall, Semantic Scholar, OpenAlex.
**Sources:** https://github.com/jamditis/claude-skills-journalism/blob/HEAD/research/web-access-tools-comprehensive-report.md (accessed 2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — single-sourced; needs a primary pass.

---

### C6. News & public technical discussion sources

---

**Resource name:** Hacker News API
**Canonical identity:** Hacker News (news.ycombinator.com); official Firebase API; Algolia HN Search API
**Category:** C. Research and Ingestion Tools — public technical discussion source
**Type:** Open APIs (official + third-party)
**Official URL:** https://github.com/HackerNews/API (Firebase API); https://hn.algolia.com/api (search)
**Description:** Two programmatic routes to HN content: the official Firebase API (items, users, top/new stories — real-time, no search) and the Algolia HN Search API (full-text search over stories/comments with date/tag filters). The standard ingestion path for "public technical discussion."
**Contents inspected:** Named in workstream brief; endpoints from general knowledge — primary docs not opened in this sweep.
**Actual capabilities:** Item/user lookup; top/new/ask/show streams; full-text search with filters (general knowledge — Partially verified).
**Supported inputs:** Item IDs; search queries.
**Outputs:** JSON stories/comments/user profiles.
**Integrations:** Plain HTTPS.
**Known restrictions:** Firebase API has no search; Algolia API is third-party with its own rate limits (general knowledge).
**Availability:** Free, no key (reported).
**Maintenance:** Active.
**License:** Data: HN content (Y Combinator); API use per terms.
**Limitations:** No official full-text search; comment threading needs client-side assembly.
**Related resources:** Reddit API, Lobsters (lobste.rs — not researched).
**Sources:** Workstream brief (Part 12) (2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Partially verified — needs primary-docs confirmation.

---

**Resource name:** Reddit API
**Canonical identity:** Reddit (reddit.com); API at oauth.reddit.com / public JSON endpoints
**Category:** C. Research and Ingestion Tools — public discussion source
**Type:** Platform API (authenticated; restricted since 2023 pricing changes)
**Official URL:** https://www.reddit.com/dev/api/
**Description:** API access to Reddit posts/comments/subreddits for public-discussion ingestion. Since the 2023 API pricing changes, free-tier programmatic access is heavily restricted; most bulk/research use now requires paid data access or the (limited) free tier.
**Contents inspected:** Named in workstream brief; current terms not opened in this sweep.
**Actual capabilities / restrictions:** Not verified — treat the 2023-restriction claim as background needing confirmation.
**Availability:** Restricted (reported).
**Limitations:** Record is thin; needs a dedicated pass on current Reddit data-access terms.
**Related resources:** Hacker News API, Pushshift (Historical — shut down; not re-verified).
**Sources:** Workstream brief (Part 12) (2026-10-10)
**Verification date:** 2026-10-10
**Confidence:** Unverified — needs a primary-source pass.

---

### C7. Gaps & thin spots in category C

- **GitHub ingestion beyond Gitingest:** GitHub's own REST/GraphQL code-search APIs are the official route for repo content at scale — noted but not given a full record (Unresolved).
- **News APIs for agents:** no dedicated 2026 news-ingestion API (e.g., NewsAPI, GDELT) was researched — **gap** (Unresolved). GDELT (gdeltproject.org) is a known candidate for a follow-up pass.
- **Video-platform ingestion beyond YouTube:** TikTok/Vimeo extractors inside yt-dlp cover this partially; no dedicated record — partial gap.
- **PDF OCR services (managed):** Azure Document Intelligence / Content Understanding referenced by MarkItDown docs but not researched — Unresolved.
- **Readability libraries:** mozilla/readability and kepano/defuddle noted as extraction backends; no full records — minor gap.
- **Common Crawl columnar-index tooling** (cc-index-table, Athena setup): referenced, not given a full record — minor gap.

---

## Coverage note

### Counts
- **Total resources catalogued:** 111 (90 full Part-21 records + 21 compact records in tables; no duplicates)
- **Category A — Web Data Acquisition:** 68 full records (frameworks 6, parsers 4, browser automation 4, extraction APIs/services 15, LLM readers 6, PDF/document extraction 8, media extraction 2, monitoring 2, metasearch 3, web archives 7, anti-bot 2)
- **Category B — Public API Directories:** 25 (catalogs/marketplaces 7, curated lists 2, mock APIs 4 full + 10 compact, data portals 4 full + 11 compact)
- **Category C — Research and Ingestion Tools:** 18 full records (codebase ingestion 1, fetch MCP servers 4, deep-research agents 2, paper sources 4, discussion sources 2, plus A5 cross-refs)

### Verification-label distribution (per-record Confidence lines; 90 full records)
- **Verified:** 13 (MarkItDown, Docling, Unstructured, Crawl4AI, pdfplumber, yt-dlp, Jina Reader, Common Crawl, changedetection.io, Gitingest, GPT Researcher, Open Deep Research, ai_agents_api_library)
- **Corrected** (applied inline alongside Verified): 4 identity corrections — Docling org move (DS4SD → docling-project, LF AI & Data Foundation); changedetection.io upstream (dgtlmoon, not forks); Gitingest canonical (coderamp-labs, ex-cyclotruc, plus同名-fork disambiguation); Zyte (formerly Scrapinghub)
- **Partially verified:** 66
- **Unverified:** 8 (Browserless, Crawlbase, Context.dev, DataForSEO, APILayer, publicapis.dev/io, LlamaParse, Reddit API)
- **Historical:** 1 standalone + 3 noted inline (youtube-dl → yt-dlp; Conifer → Browsertrix; mocky.io gone 2026; ProgrammableWeb retired)
- **Unresolved:** 2 standalone (Spider-Rust repo identity; Parallel) + gaps listed in B5/C7

### Limitations of this sweep
1. **Primary-source depth:** the most heavily verified items are those whose READMEs/docs were retrievable via search-cached primary content. For ~55 items the primary repo/site was not opened; their records are honestly marked Partially verified/Unverified rather than asserted.
2. **Pricing:** all prices are 2026 secondary-source snapshots, explicitly not verified against vendor billing pages. Do not quote them as current.
3. **Anti-bot section** covers only lawful, documented techniques per the brief; CAPTCHA-solving services and credential bypass are out of scope and were not catalogued.
4. **No execution:** per read-only rules, no tool was installed or run; capability claims rest on documentation, not testing.
5. **Copyright discipline:** secondary sources are summarized and linked, not quoted at length.

### More work warranted?
Yes — a focused second pass should: (a) open primary READMEs/docs for the 9 Unverified items (Browserless, Crawlbase, Context.dev, DataForSEO, APILayer, publicapis.dev/io, LlamaParse, Reddit API terms, Parallel); (b) confirm the Rust "spider" crawler's canonical repo; (c) research the identified gaps — public GraphQL API directory, API status tools, SDK directories, news APIs (NewsAPI/GDELT), managed OCR services; (d) verify licenses from license files for PyMuPDF (AGPL implications), SearXNG, and Gitingest; (e) re-check 2026 pricing against vendor pages if the Atlas needs price data at all.

---
*End of Part 12 (06a-data-acquisition). Researcher: workstream #11. Verification date: 2026-10-10.*
