# Fact/interpretation check — indias-cheapest-lng-capacity-is-extra

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-cheapest-lng-capacity-is-extra.html`

Text-SHA1: `572ea7ebf157b3a7`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 9829, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Dahej ran at 92% in April–May 2026 while newer ones at 24–37%"** — The claim conflates two different bases: Dahej’s utilisation is reported at **91.9%** on its *old 17.5 MMTPA base* (PPAC data), while the newer terminals’ 24–37% figures are on their *full 5 MMTPA capacity*. The comparison is misleading because Dahej’s expansion to 22.5 MMTPA (commissioned March 2026) was not yet reflected in PPAC’s April–May 2026 data (as noted in the article itself). [confidence: high]

- **"PNGRB’s own data point to the pipeline out, not the tank, as the constraint"** — While pipeline constraints are cited as a key reason for low utilisation (e.g., Kochi/Ennore), the article later acknowledges that **Dahej’s utilisation is near-full because its pipelines (GSPL’s Gujarat network) are fully utilised at ~100%**, while newer terminals lack adequate evacuation capacity. The claim oversimplifies the constraint as *only* pipeline-related, ignoring that Dahej’s long-term contracts (e.g., QatarEnergy) and existing infrastructure also play a role. [confidence: medium]

---
**INTERPRETATION ERRORS:**
- **"Expanding Dahej cost about ₹370 crore per MMTPA, while new terminals cost ₹950–1,290 crore"** — The cost comparison is **apples-to-oranges** because:
  1. The ₹370 crore figure for Dahej’s 2021–26 expansion **excludes the second jetty** (costing ~₹1,000 crore), which was part of the 2012–16 expansion (₹600 crore/MMTPA). The article later clarifies that the **send-out equipment alone** (reusing existing infrastructure) drove the lower cost, but the headline comparison omits this nuance.
  2. New terminals like Chhara/Dhamra include **new marine works (breakwaters, dredging)**, while Dahej’s expansion reused existing jetties/pipelines. The cost gap is structural, not just "expansion vs. new build." [confidence: high]

- **"India’s LNG demand doubled to ~200 MMSCMD by 2030"** — The claim is **extrapolated from PNGRB’s "Good-to-Go" scenario**, which assumes **LNG demand doubling to ~200 MMSCMD** (from ~100 MMSCMD in 2023–24). However:
  - The article later notes that **PNGRB’s base case only projects 187 MMSCMD total gas demand (including domestic production) by 2030**, with LNG demand unspecified in the "Good-to-Best" case. The "doubling" figure is **not directly supported by the demand projections table** (p.25 of the April 2025 PNGRB report), which lacks a clear LNG split. [confidence: high]

---
**OUTDATED DATA:**
- **"PPAC lists Dahej at 17.5 MMTPA as of 1 June 2026, two months after its expansion to 22.5 MMTPA"** — The article cites this as a **data lag in PPAC’s May 2026 Ready Reckoner**, but the newer **June 2026 PPAC data** (released in July 2026) should reflect the updated capacity. Re-check: [PPAC Monthly Ready Reckoner (June 2026+)] for terminal capacity updates. [confidence: high]

- **"LNG imports for 2025-26 at 34,216 MMSCM (PPAC, May 2026 data)"** — While accurate for the period, **PPAC’s June 2026 data** (released in July 2026) likely includes revised provisional figures for 2025-26 and updated monthly breakdowns (e.g., June–September 2026). Re-check: [PPAC Table 18 (LNG imports, latest edition)]. [confidence: high]
