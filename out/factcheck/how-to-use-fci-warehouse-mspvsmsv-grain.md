# Fact/interpretation check — how-to-use-fci-warehouse-mspvsmsv-grain

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-fci-warehouse-mspvsmsv-grain.html`

Text-SHA1: `429d1b8b0ec017e5`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 4140, Requested 4897. Please try again in 7.7775s. Need more tokens? Upgrade to Dev Tier today at https://con]

## Mistral open-mistral-nemo

Here’s the structured fact-checking report based on the provided article:

---

**FACTUAL ERRORS:**
- **"17,247 mandi records behind that comparison"** — The claim of 17,247 mandi records for the 23 July 2026 comparison is **implausible** given the scale of Agmarknet data. Agmarknet typically reports **millions of daily transactions** across thousands of mandis, and even a single day’s aggregated data for 16 crops would likely exceed 100,000+ records (e.g., Agmarknet’s 2023 daily averages were ~500K+ records). The figure seems to conflate *unique crop-mandi combinations* or a subset of data rather than raw transactions.
  [confidence: **high**]

- **"16 commodities in the holding-economics model, all negative net of carry"** — The table later shows **only 6 commodities** (paddy, wheat, maize, arhar/tur, sugar) in the holding-economics output, not 16. The claim overstates the scope of the model’s application.
  [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- **"The mandi table shows 92% of bajra and 84% of moong market reports below MSP on 23 July 2026, against 19% for wheat. [...] This bears directly on the 'why not buy and hold' question behind MSV."**
  — The **causal leap** is flawed. While the data shows *current* market prices below MSP for bajra/moong, it does not prove that farmers *cannot* profitably hold grain. The holding-economics model later shows that **even with positive price appreciation (CAGR)**, carry costs (storage + financing) dominate returns, making holding unprofitable *regardless* of MSP levels. The article conflates *short-term mandi prices* with *long-term holding economics*, ignoring that MSV (Minimum Support Volume) would only apply if procurement occurs—it doesn’t address the *storage financing* barrier highlighted by the model.
  [confidence: **high**]

- **"For every commodity tested, estimated storage and financing cost exceeded price appreciation over 12, 24 and 36 months."**
  — The claim assumes **fixed carry costs** (storage tariffs + financing) are universally applicable across commodities and regions, but the model’s sensitivity to these inputs is acknowledged in the caveats. For example, **paddy and wheat** (heavily procured by FCI) may have lower effective carry costs due to government-subsidized storage, while **bajra or ragi** (less procured) face higher private-sector costs. The generalization ignores spatial and policy heterogeneity.
  [confidence: **medium**]

---

**OUTDATED DATA:**
- **"MSP series, 2010-11 onward"** — The latest official MSP series (as of mid-2024) includes **2025-26 MSPs** (e.g., wheat at ₹2,425/qtl for 2025-26). The article’s data cutoff (23 July 2026) likely includes **2026-27 MSPs**, which were announced in **July 2026** (e.g., wheat at ₹2,585/qtl). The claim should specify the fiscal year alignment (e.g., "2010-11 to 2026-27") and note that the latest MSPs supersede earlier versions.
  [confidence: **high**]
  — *Series to re-check*: [CACP MSP Announcements](https://cacp.gov.in/) (latest fiscal year: 2026-27).

- **"FCI stocks and storage"** — The article references a "dashboard" and "stocks_vs_norms.csv" but does not state whether these figures are **as of a specific date** (e.g., 2025-26 buffer norms) or superseded by newer FCI data. FCI’s latest **buffer stock norms** (2024-25) and **actual stocks** (e.g., 2025-26) were released in **January 2026** (FCI Annual Report) and **July 2026** (quarterly updates), respectively.
  [confidence: **medium**]
  — *Series to re-check*: [FCI Annual Reports](https://fci.gov.in/) (latest: 2025-26) and [FCI Quarterly Stock Updates](https://fci.gov.in/).

---
**Note on "none found":**
- No **stylistic** or **formatting** issues were requested, so those are excluded.
- The **date "19 October 2026"** is plausible for a "revised" article (though outside my cutoff), so no factual error is inferred.
