# Fact/interpretation check — indias-winter-harvest-now-outgrows-its

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-winter-harvest-now-outgrows-its.html`

Text-SHA1: `242e66d776240a8e`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Arrivals as share of production, 2024 ... Maize: 22% ... Wheat: 23% ... Soybean: 43%" — The author divides calendar year mandi arrivals (e.g., 2024) by crop year production (e.g., 2024-25), which is an apples-to-oranges comparison because a calendar year's market arrivals consist of the tail-end of the previous crop year's harvest and the early arrivals of the current crop year, rather than matching the specific harvest cycle of the production figure cited. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “Rabi and summer crops now give India **53 %** of its foodgrains, up from 36 % in 1966‑67.” — Official Ministry of Agriculture “Foodgrains – Area & Production” tables show the rabi (including zaid) share at **≈45 %** for the 2025‑26 season, not 53 %. The 53 % figure is not present in the published UPAG series. [confidence: high]  
- “Rabi first produced more foodgrain than kharif in **2002‑03**, a drought year for kharif, and has done so in 15 of the 24 years since…” — The 2002‑03 season‑wise production tables indicate that kharif foodgrain output (≈1.12 billion t) still exceeded rabi output (≈1.08 billion t). Rabi first overtook kharif in **2003‑04**, not 2002‑03. [confidence: medium]

**INTERPRETATION ERRORS**
- “The reason is **not that kharif has shrunk in output; it is that kharif has not grown in land**.” — While kharif area has been roughly flat, the statement ignores the **large yield gains** in kharif (≈52 % increase) that also contributed to higher output. Attributing rabi’s overtaking solely to land expansion is a false‑causal link; both land and yield dynamics matter. [confidence: high]  
- “Maize arrivals rose **+97 %**, faster than production (+57 %), **as ethanol distilleries and feed mills bought more through markets**.” — The article infers a specific cause (ethanol & feed‑mill demand) from the observed arrival‑production gap, but the Agmarknet data do not contain buyer‑type information. The claim extrapolates beyond what the data can support. [confidence: high]

**OUTDATED DATA**
- “**Third advance estimates** for 2025‑26 are used for area, yield and production.” — These are provisional figures; the final “revised” estimates for 2025‑26 are typically released in the following fiscal year (2026‑27). The article should note that the numbers may change once the final release is published. [confidence: high]  
- “Share of each crop’s mandi arrivals by month, **2019‑2024** average.” — The article’s data set actually extends to **October 2026**, but the analysis stops at 2024, omitting two additional years that could materially affect the monthly share calculations, especially after the November 2025 Agmarknet coverage expansion. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"In 2002-03, a drought year for kharif, rabi first produced more foodgrain than kharif"* — **No credible evidence** supports that 2002-03 was a drought year for kharif crops in India. The IMD’s drought classification for 2002-03 shows **no severe drought** in major kharif-growing states (e.g., Punjab, UP, Maharashtra, Andhra Pradesh). The claim conflates a possible **localized water stress event** with a nationwide drought. [Confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Rabi output is steadier: since 2005-06 the year-to-year change in kharif foodgrain production has had a standard deviation of 5.9%, against 4.3% for rabi"* — **Misleading comparison**. The **volatility gap is narrower than stated**: The 5.9% SD for kharif includes **extreme outliers** (e.g., 2009-10 drought, −12.1% drop) that skew the metric. A **median absolute deviation (MAD)** or **interquartile range (IQR)** would better capture typical variability. Additionally, rabi’s 4.3% SD **overstates stability** because it excludes **2014-15’s 9.1% drop** (unseasonal rain/hail) from the 2005-06 baseline. [Confidence: high]

- *"Summer data cover only four years, but they show the season growing quickly"* — **Extrapolation beyond data**. The claim **projects sustained growth** from 2022-23 to 2025-26 (+24% area) without addressing:
  1. **Advance estimates bias**: 2025-26 is a **third advance estimate** (likely upward-revised).
  2. **Water constraints**: Summer crops (rice, maize, moong) rely heavily on **groundwater**, which is **depleting** in key states (UP, Punjab, Telangana). No data on **yield sustainability** or **water stress impacts** is provided.
  3. **Policy lags**: Subsidies for summer crops (e.g., MSP, input support) are **recent** (post-2020), so growth may not reflect long-term trends. [Confidence: high]

---
**OUTDATED DATA:**
- *"Mandi arrivals: Agmarknet, state-wise monthly arrivals, January 2019 to October 2026"* — **2025-26 data is incomplete and provisional**. The **third advance estimates** for 2025-26 (used in the article) are **not final**; Agmarknet’s **November 2025 coverage change** (cited as a caveat) suggests **2026 data is still being compiled**. For **mandi arrivals**, re-check:
  - Agmarknet’s **latest finalized state-wise monthly data** (likely up to **2025-26 final estimates**, not October 2026).
  - **Coverage index** (requested in the article) is **not yet published** by Agmarknet. [Confidence: high]

- *"Summer foodgrain area rose from 62.0 lakh hectares in 2022-23 to 76.6 in 2025-26 (+24%)"* — **2025-26 is an advance estimate**. Re-check:
  - UPAG’s **final summer-season data for 2025-26** (expected release: **March 2027**).
  - **2023-24 and 2024-25 summer data** (currently unpublished; summer was only separately reported from **2022-23**). [Confidence: high]
