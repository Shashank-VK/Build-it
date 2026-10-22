# Domain B — 06: Multimodal Capabilities in Products

> Scope: products that take or produce non-text modalities — vision (image/document understanding), voice (STT/TTS, voice agents), video, and image generation — as customer-facing features. Research date: 2026-10-10.

## 1. What "multimodal product" means (plain English → mechanics)

**Plain English:** A multimodal feature lets users interact beyond typed text: talk to the product by voice, show it a photo of a broken appliance, get a spoken answer back, or generate an image. Each modality adds a model (or model capability), a latency budget, a cost line, and a failure mode.

**Concrete example:** A voice support agent. The naive version chains three models: speech-to-text (Whisper-class) → LLM reasoning → text-to-speech. Each hop adds latency and a failure point. The modern version uses a native speech-to-speech model (one model, no hops) — fewer failure points, lower latency, better prosody.

**Deeper mechanics:** Modalities arrive at different rates with different latencies (audio streams continuously; vision arrives in frames; text arrives in bursts). Fusing them requires *temporal synchronization* — e.g., aligning "this one" in speech with the image frame the user was pointing at. Without explicit sync logic, cross-modal references break silently. Each modality also needs independent health checks, circuit breakers, and fallback paths (if STT fails, fall back to text input; if vision times out, acknowledge and process async).

## 2. Vision in products

### 2.1 Document/vision understanding

- **General VLMs** (GPT-4o, Gemini 2.5, Claude) handle charts, screenshots, multi-panel diagrams with improving spatial reasoning and text-in-image extraction.
- **Specialized pipelines beat general VLMs for high-volume structured extraction** (invoices, forms, receipts): dedicated OCR + layout models are cheaper and more accurate per page at volume. The practical split: VLMs for understanding/classification, specialized pipelines for high-throughput extraction (see 05).
- **Production practices:** downscale images, use low-detail modes when possible, crop to regions of interest, sample fewer video frames, cache results by file hash, validate MIME types/sizes, scan uploads for malware, handle HEIC/TIFF/multi-page PDFs.
- **Privacy:** faces, license plates, IDs, voices are sensitive — blur/redact, get consent, respect data residency.
- **Security:** images can carry *visual prompt injection* — hidden text in an image instructing the model. Treat image-derived text as untrusted input (see 10).

### 2.2 Multimodal search and RAG

- **Multimodal embeddings** (CLIP/SigLIP-class): text-image search, zero-shot classification.
- **Multimodal RAG:** index figures as captioned chunks, but at answer time send the *original* image to the VLM with text context — captions lose what the model could have seen.
- **Video:** frame sampling + transcripts, segment indexing. Cost scales with frames processed.

### 2.3 Image generation as a feature

- Diffusion models with structured prompting; legal/provenance cautions (training-data copyright, likeness rights — see Meta's Muse Image removal below).

## 3. Voice in products

### 3.1 Architectures

- **Cascaded:** STT → LLM → TTS. Mature, debuggable per stage, but latency stacks (each stage adds hundreds of ms) and errors compound (mis-transcription poisons reasoning).
- **Native speech-to-speech:** one model handles audio in/out (OpenAI Realtime API, Gemini Realtime). Lower latency (~320ms reported for realtime conversational turn-taking with interruption support), better prosody, fewer hops — but 10–20× the cost of a regular API call and less debuggable.
- **Latency budget:** voice is the most latency-sensitive modality — sub-second (ideally <800ms) response feels conversational; multi-second feels broken. Streaming output is mandatory, not optional.

### 3.2 Cost picture (practitioner-reported ranges)

- Text-only agent: ~$0.01–0.05 per conversation.
- Voice adds ~$0.02–0.10 per audio minute (STT + TTS).
- Vision adds ~$0.01–0.05 per image analyzed.
- A fully multimodal 5-minute call with 3 image analyses: ~$0.30–0.80 — viable for high-value interactions (insurance claims, technical support), prohibitive for casual chat at scale.
- **Evidence:** practitioner (channel.tel production guide). Accessed 2026-10-10. Confidence: **Inferred** (ranges, provider/model-dependent; directionally consistent with API pricing).

### 3.3 Evaluation

- **WER** (word error rate) for STT; field-level accuracy for extraction; human ratings for generation quality; latency percentiles per stage.
- Voice agents need *interruption* handling and turn-taking evals — metrics text chat never needs.

## 4. Negative evidence: multimodal AI hardware

### 4.1 Humane AI Pin (discontinued Feb 2025)

- $699 + subscription; projected 100,000 year-one sales, achieved ~10%. Killed Feb 28, 2025 — devices bricked when servers shut off (only battery-level display remained).
- Failure modes: overheating, poor battery, unreliable interactions, and a fundamental product error — trying to replace the phone screen rather than complement it. Non-transferable subscription locked buyers in.
- **Lesson:** committing to manufacturing before validating the experience with retention data is uniquely dangerous in hardware — you can't patch physical products.

### 4.2 Rabbit R1 ($199)

- Sold ~100,000 pre-orders on a CES demo showing capabilities the shipped product lacked; reviews panned sluggishness. Survived longer than Humane via post-launch updates, but reviewer consensus: "barely reviewable" at launch, a "Large Action Model" without enough training data — a cold-start problem (see 04) in hardware form: they needed user data to improve, but users wouldn't buy an unfinished product to provide it.
- **Tony Fadell's verdict (MIT Future Fest, Oct 2026):** the Gen-1 AI gadgets failed because they solved no genuine problem — "interesting technology for geeks" projecting executives' assistant-using lives onto consumers who've never had one.

### 4.3 Meta Muse Image (removed July 2026, days after launch)

- AI image feature that auto-opted-in public Instagram content for AI-generated imagery; pulled within days after backlash from SAG-AFTRA, CAA, and privacy advocates over non-consensual digital replicas. Meta had claimed "strong controls and safety guardrails from day one" — the controls didn't cover the consent model.
- **Lesson:** for generative visual features, the *consent architecture* is the safety architecture. Opt-out is not consent.
- **Evidence:** secondary (iHeart/WRKO, Campaign Asia via mmm-online, July 2026). Accessed 2026-10-10. Confidence: **Verified** on the removal and stated reasons.

## 5. Cross-cutting engineering lessons

1. **One modality, one budget, one fallback.** Each modality needs its own latency budget, cost accounting, health checks, and degradation path.
2. **Synchronization is the hidden hard problem** in voice+vision fusion — timestamps, not vibes.
3. **Specialized beats general at volume** (OCR pipelines for extraction; cascaded voice for debuggability), while **native beats chained for latency** (speech-to-speech for conversation).
4. **Demo-driven development is the failure pattern** across Humane, Rabbit, and Sora: optimizing for stage impact instead of consistent daily experience.
5. **Consent and privacy are product architecture** for anything that sees faces or hears voices — not legal afterthoughts.

## 6. Per-finding metadata (selected)

| Claim | URL | Source type / author | Pub date | Accessed | Confidence | Evidence class |
|---|---|---|---|---|---|---|
| Multimodal production: sync, graceful degradation, cost ranges $0.30–0.80/multimodal call | https://www.channel.tel/blog/multimodal-ai-agents-voice-vision-text-production | practitioner / channel.tel | ~2026-03 | 2026-10-10 | Corroborated (ranges) | first-hand practitioner |
| Multimodal production practices: cost/latency/privacy/security table | https://github.com/rajsekharalluri/devthread.in/blob/HEAD/content/genai-engineer/multimodal.md | practitioner handbook | 2026-09 | 2026-10-10 | Corroborated | corroborating |
| Realtime API ~320ms, 10–20× cost of regular API | https://github.com/forhow134/ai-coding-guide/blob/HEAD/docs/08-multimodal/video-realtime.md | practitioner guide | 2026-02 | 2026-10-10 | Corroborated | community observations |
| Humane: 100k projected, ~10k sold, bricked Feb 28 2025 | https://www.digitaltrends.com/phones/i-knew-the-humane-ai-pin-would-fail/ | secondary / Digital Trends | ~2025 | 2026-10-10 | Verified | corroborating |
| Rabbit R1: 100k pre-orders, demo exceeded shipped product, "barely reviewable" | https://www.Dexerto.com/tech/marques-brownlee-slams-another-ai-product-as-barely-reviewable-after-humane-ai-pin-controversy-2669843/ | secondary / Dexerto (MKBHD review) | 2024 | 2026-10-10 | Corroborated | community observations |
| Fadell: Gen-1 AI gadgets failed; solved no genuine problem | https://www.webpronews.com/why-tony-fadell-says-the-ai-gadget-experiment-already-failed/ | secondary / WebProNews | 2026-10-08 | 2026-10-10 | Verified (on-record quote) | corroborating |
| Meta Muse Image removed days after launch over consent/backlash | https://wrko.iheart.com/content/2026-07-13-new-meta-ai-app-disabled-after-pushback/ | secondary / iHeart | 2026-07-13 | 2026-10-10 | Verified | corroborating |

**Gaps / Unknowns:** per-modality production cost/latency for any named product (no vendor publishes); measured WER/accuracy for production voice agents; independent safety audits of visual prompt-injection defenses.
