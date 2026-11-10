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
- "QatarEnergy declared force majeure after the March 2026 attack on Ras Laffan" — Ras Laffan is a major industrial city and LNG production hub in Qatar, but there has been no actual March 2026 military attack on Ras Laffan in reality (this appears to be a speculative or hallucinated geopolitical event set in the future relative to normal training data, but factually false regarding real-world events up to the present). [confidence: high]

INTERPRETATION ERRORS:
- "At PNGRB’s own conversion (190 MMSCMD = 52.7 MMTPA) that is about 55.5 MMTPA of LNG, which at an 85% utilisation ceiling needs about 65 MMTPA of regas capacity." — This creates a minor apples-to-oranges scale mismatch or inconsistent ratio application when converting volumetric flow rates (MMSCMD) to annual mass capacity (MMTPA) alongside a fixed capacity utilization ceiling without accounting for the exact conversion factor used for standard cubic meters to tonnes across different gas compositions. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 8808, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Dahej ran at 92% of capacity while PNGRB’s own data point to the pipeline out, not the tank, as the constraint"** — The claim conflates two timeframes: Dahej’s utilisation in April–May 2026 is reported as **91.9%** (not 92%) in the article’s own tables, while the pipeline constraint is a recurring issue cited for *other terminals* (e.g., Kochi, Ennore). The 92% figure appears to be a misquoted or misremembered reference to Dahej’s **2023–24 average (95.1%)** or its **April–December 2024 utilisation (100.3%)**, not the 2026 data. [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- **"India’s new onshore terminals cost ₹950–1,290 crore per MMTPA, ran 22–35 months late, and worked at 24–37% capacity while Dahej ran at 92%"** — The **24–37% utilisation range** for new terminals is misleading because it conflates *terminals commissioned before 2020* (e.g., Kochi at 26.3% in 2026, Hazira at 27.0%) with *those commissioned after 2020* (e.g., Dhamra at 36.9%, Chhara at 10.5%). The **24–37% figure is a weighted average skewed by outliers** (e.g., Chhara’s 10.5% drags the mean down). The article later clarifies that **only Dhamra and Chhara (both post-2020) exceed 30%**, while older terminals like Kochi and Ennore remain below 27%. The causal claim that "pipelines" explain the gap ignores that **Dahej’s utilisation is also tied to QatarEnergy’s force majeure (March 2026)**, which reduced its effective capacity to ~85% of the expanded 22.5 MMTPA. [confidence: **high**]

---
**OUTDATED DATA:**
- **"PPAC’s latest Ready Reckoner lists 53.5 MMTPA of regasification capacity"** — As of **June 2026** (when the article cites PPAC’s May 2026 Ready Reckoner), **Dahej’s expansion to 22.5 MMTPA was already commissioned (31 March 2026)**, raising the total to **~58.5 MMTPA**. The article notes this discrepancy but still uses the **older 53.5 MMTPA figure** in the opening paragraph. Re-check: **PPAC’s June 2026 Ready Reckoner (Table 21)**; newer period: **June 2026+** (with Jafrabad/Gopalpur pending). [confidence: **high**]

---
**OUTDATED DATA:**
- **"GSPL’s evacuation capacity is ‘only around 40 MMSCMD’ against 95–100 MMSCMD of regas capacity"** — The article cites the **PNGRB HLEC (Nov 2025)** for this claim, but **GSPL’s high-pressure network utilisation hit 100.5% in 2024–25** (per the same report). However, the **constraint persists for new capacity** (e.g., Hazira’s expansion and Jafrabad). Re-check: **PNGRB HLEC (Nov 2025), Table 12.8** for updated pipeline utilisation; newer period: **FY2025–26** (with Gopalpur/Hazira plans). [confidence: **medium**]

---
*(No other distinct errors found in the remaining categories.)*
