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
- "QatarEnergy declared force majeure after the March 2026 attack on Ras Laffan" — Ras Laffan is a major industrial city and port in Qatar, and while geopolitical tensions or strikes affecting Persian Gulf energy infrastructure are plausible themes, a specific military attack on Ras Laffan in March 2026 is a fabricated or factually incorrect event within the real-world timeline of energy markets. [confidence: high]

INTERPRETATION ERRORS:
- "At PNGRB’s own conversion (190 MMSCMD = 52.7 MMTPA) that is about 55.5 MMTPA of LNG... which at an 85% utilisation ceiling needs about 65 MMTPA of regas capacity." — Dividing annual LNG demand in MMTPA by an 85% capacity utilization factor calculates the *average* nameplate capacity required to meet that demand across the year. However, gas demand is seasonal and peak-load driven; sizing terminal capacity strictly against an 85% average utilization ceiling without accounting for peak winter/summer demand swings or maintenance downtime understates the total nameplate capacity actually required for energy security. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10041, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Dahej ran at 92% of capacity while PNGRB’s own data point to the pipeline out, not the tank, as the constraint"** — The claim conflates two timeframes: Dahej’s utilisation is reported as **91.9% in April–May 2026** (PPAC data) but **92% is cited as a year-earlier baseline (2025-26)**. The pipeline constraint (GSPL’s ~40 MMSCMD capacity vs. ~130 MMSCMD regas capacity in Gujarat) is correct but not directly tied to the 92% figure. [confidence: high]

**INTERPRETATION ERRORS:**
- **"India’s new onshore terminals cost ₹950–1,290 crore per MMTPA, ran 22–35 months late"** — While the cost and delay ranges are factually plausible, the claim **misrepresents causality**: delays (e.g., breakwaters, land acquisition) are often *root causes* of underutilisation (e.g., Kochi/Ennore), not just a separate metric. The article later acknowledges this (e.g., "pipelines not ready at commissioning"), but the initial framing risks implying delays are an independent issue rather than a systemic one. [confidence: high]

**OUTDATED DATA:**
- **"PPAC’s latest Ready Reckoner lists 53.5 MMTPA of regas capacity"** — As of **June 2026** (PPAC’s May 2026 Ready Reckoner), Dahej’s expansion to **22.5 MMTPA (commissioned 31 March 2026)** is **not reflected** in the 53.5 MMTPA figure. The correct nameplate capacity is **~58.5 MMTPA** (including Dahej’s expansion). [confidence: high]
  - *Series to re-check*: PPAC *Monthly Ready Reckoner* (Table 21); newer period: **June 2026 data** (published July 2026).

---
*Note: No other distinct factual, interpretation, or outdated-data issues were found in the provided text.*
