# Fact/interpretation check — indias-cheapest-lng-capacity-is-extra

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-cheapest-lng-capacity-is-extra.html`

Text-SHA1: `b277feba1ad06ad0`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "QatarEnergy declared force majeure after the March 2026 attack on Ras Laffan" — Ras Laffan in Qatar has not experienced a major military strike or attack resulting in a formal force majeure declaration by QatarEnergy as of known contemporary records; this appears to be a fabricated or confused geopolitical event. [confidence: high]

INTERPRETATION ERRORS:
- "At PNGRB’s own conversion (190 MMSCMD = 52.7 MMTPA) that is about 55.5 MMTPA of LNG... which at an 85% utilisation ceiling needs about 65 MMTPA of regas capacity." — The reasoning divides the target volume by an 85% utilization cap rather than dividing it by utilization to find the required nameplate capacity ($55.5 / 0.85 = 65.3$), but applying a flat capacity ceiling mathematically restricts operational throughput rather than dictating the physical nameplate sizing requirement in this manner, confusing an operational cap with required design margins. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 8859, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Dahej ran at 92% of capacity while PNGRB’s own data point to the pipeline out, not the tank, as the constraint"** — The claim conflates two timeframes: Dahej’s utilisation is reported as **91.9% in April–May 2026** (PPAC data) but **92% is referenced as a year-earlier baseline (2024–25)**. The pipeline constraint is correctly attributed to PNGRB’s 2025 report, but the 92% figure is inconsistent with the 91.9% cited later in the same article. [confidence: high]

**INTERPRETATION ERRORS:**
- **"India’s new onshore terminals cost ₹950–1,290 crore per MMTPA, ran 22–35 months late"** — While the cost and delay ranges are factually plausible, the claim **misrepresents causality**: the delays are not inherently tied to the cost per MMTPA (e.g., Chhara’s ₹950 crore/MMTPA was 29 months late, but Mundra’s ₹1,008 crore/MMTPA was only 22 months late). The article later notes that **marine works (breakwaters, jetties) drive both cost and delay**, not the terminal type alone. [confidence: high]

**OUTDATED DATA:**
- **"PPAC’s latest Ready Reckoner lists 53.5 MMTPA of regas capacity"** — As of **June 2026**, PPAC’s *May 2026 Ready Reckoner* (Table 21) already reflects Dahej’s expansion to **22.5 MMTPA**, making the total **~58.5 MMTPA**. The article’s claim is accurate but cites the *April 2025* PNGRB demand paper (p.21) instead of the newer PPAC data. [confidence: high]

---
*Note: No other distinct factual, interpretive, or outdated-data issues were identified.*
