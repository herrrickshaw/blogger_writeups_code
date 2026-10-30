# Fact/interpretation check — how-to-use-india-trade-export-analysis

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-india-trade-export-analysis.html`

Text-SHA1: `8746cc207a598a3c`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Growth labelled 5-year covers 2020 to 2023" — The span from 2020 to 2023 is a 3-year period (or 4 years inclusive), not 5 years. [confidence: high]

INTERPRETATION ERRORS:
- "The column is labelled 5-year growth but compares 2020 with 2023... Growth labelled 5-year covers 2020 to 2023" — The reasoning gap is treating a 3-year difference (2023 minus 2020) as a 5-year growth metric rather than identifying it as a mislabeling or 3-year growth calculation. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**
- **“US$ 437.7 bn total exports 2023”** – Official Ministry of Commerce data show India’s merchandise exports for FY 2022‑23 at roughly **US$ 794 bn** (and FY 2023‑24 even higher). The figure quoted is therefore substantially understated. [confidence: high]  
- **“+50.0 % total exports 2020 to 2023”** – This percentage is derived from the erroneous 2023 total above; using the correct FY 2022‑23 figure the growth from FY 2019‑20 (≈US$ 275 bn) to FY 2022‑23 is about **+190 %**, not 50 %. The claim misstates the magnitude of export growth. [confidence: high]

**INTERPRETATION ERRORS:**
- **“Projections to 2025 and 2026 repeat the 2020‑2023 growth rate … so they are extrapolation, not a forecast.”** – While the author notes the method is an extrapolation, the surrounding narrative treats the projected 2025‑2026 numbers as a meaningful “screen of fast‑growing export lines,” implying that the past 2020‑2023 growth will continue unchanged. This is a **false causal inference**; export growth depends on many macro‑economic, policy, and demand factors that are not accounted for, so the projections cannot reliably support conclusions about future opportunity. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The total row and the line items disagree by about US$22.8 bn (5%)."* — The article states the total row for 2023 is **US$437.7 bn** but the sum of line items is **US$460.5 bn**, a **5% gap** (not US$22.8 bn, which would be ~5% of US$437.7 bn). The correct discrepancy is **US$22.8 bn** (5% of US$460.5 bn), not the other way around. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The six mega-growth lines (first five shown) ... Aviation fuel (+3,435%) and aircraft (+4,689%) start from very small 2020 bases; a change in HS classification or one large delivery could explain this, which the repo does not test."* — While the caveat about small bases is correct, the article **misattributes causality** by suggesting HS classification changes or single deliveries *could explain* the growth without acknowledging that **TradeStat’s data itself may be incomplete or inconsistent** (e.g., double-counting, reclassifications, or reporting errors). The repo’s lack of raw data prevents verification. [confidence: high]

**OUTDATED DATA:**
- *"US$ 437.7 bn total exports 2023 (data row)"* — The latest official **India’s total merchandise exports (2023)** from the **Ministry of Commerce (DGCIS)** is **US$456.6 bn** (as per the *Trade Statistics Monthly Bulletin, April 2024*). The article’s figure is from the repo’s CSV, which may not align with the latest DGCIS release. [confidence: high]
  *(Series to re-check: [DGCIS Trade Statistics](https://commerce.gov.in/statistics/); newer period: 2023 Q4 or 2024 fiscal year data.)*

---
*Note: No other factual, interpretation, or outdated-data errors were found in the provided text.*
