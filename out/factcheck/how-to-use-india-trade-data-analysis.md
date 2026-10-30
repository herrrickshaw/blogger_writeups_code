# Fact/interpretation check — how-to-use-india-trade-data-analysis

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-india-trade-data-analysis.html`

Text-SHA1: `b43308216ba47145`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The file states the services surplus covers about 87.9% of the extra goods gap." — The goods deficit (goods_balance) changes from year to year rather than representing a static "extra goods gap" being covered by services in a cumulative sense, making a direct percentage comparison of net services to the year-over-year change or absolute deficit conceptually imprecise without clearer baseline definitions. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“The file states the services surplus covers about 87.9 % of the extra goods gap.”** – The numbers shown in the article’s own table give a services surplus of 188.9 billion USD (FY 2024‑25) against a goods deficit of 283.5 billion USD, which is only ≈ 66.7 % (188.9 ÷ 283.5 × 100). Even using the FY 2023‑24 figures (services 162.8 bn vs goods ‑241.1 bn) the coverage is ≈ 67.5 %. The 87.9 % figure does not match the underlying data. [confidence: high]

**INTERPRETATION ERRORS**  
- **“The services surplus covers about 87.9 % of the extra goods gap.”** – Even if the percentage were correct, presenting the services surplus as “covering” the goods deficit implies that the surplus largely offsets the deficit, suggesting the overall external balance is close to neutral. In reality, the services surplus offsets only roughly two‑thirds of the goods deficit, leaving a sizable net trade deficit (≈ ‑94.6 bn USD in FY 2024‑25). The claim therefore overstates the offsetting effect and draws a conclusion (that the deficit is largely mitigated) that the data do not support. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"US$ 776.0 bn merchandise imports, FY2025-26"* — The article’s own JSON data (`five_year_trade_currency_synthesis_2026-07-18.json`) shows **US$ 776,013.7 million** (≈ **US$ 776.01 bn**), not US$ 776.0 bn. The discrepancy is likely rounding in the text vs. the precise JSON figure. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The five-year synthesis file shows imports up 26.58% against exports up 4.68% over FY2021-22 to FY2025-26"* — While the claim is factually correct, it conflates **nominal growth** (which includes inflation) with **real growth** (inflation-adjusted). Without deflating for inflation (e.g., using WPI/CPI), the import growth overstates true volume growth, and the export growth understates it. The article does not adjust for inflation, so the "26.6% vs 4.7%" comparison is misleading for policy analysis. [confidence: high]

**OUTDATED DATA:**
- *"FY2025-26 is provisional"* — The article explicitly states this, but **no newer official data** (e.g., MoSPI’s finalized FY2025-26 trade figures or RBI’s updated balance of payments) is referenced. Readers should cross-check with:
  - **MoSPI’s *Trade Statistics* (latest provisional/advance estimates)** [series: *Monthly Trade Statistics*; check for FY2026-27 or revised FY2025-26].
  - **RBI’s *Balance of Payments* (BoP) handbook** [series: *BoP Statistics*; latest quarterly update].
  [confidence: high]

---
*Note: The article’s caveats (e.g., "provisional," "services trade lags by a year") are correctly noted, but the above gaps remain.*
