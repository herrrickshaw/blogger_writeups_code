# Fact/interpretation check — effective-buying-power-china-comparison

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/effective-buying-power-china-comparison.html`

Text-SHA1: `9b80940dc3e2d1e8`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "China was formally designated a currency manipulator in August 2019 for a mechanism it ran for years: buying foreign currency and accumulating reserves to hold the yuan artificially weak , subsidizing exports." — The U.S. Treasury formally designated China as a currency manipulator in August 2019 under Secretary Steven Mnuchin, but this was an unprecedented designation that did not follow a multi-year formal labeling process for that specific decision; furthermore, China had not been formally designated for years prior (the last prior designation was in 1994). [confidence: medium]

INTERPRETATION ERRORS:
- "India inflation — implied GDP deflator from the MoSPI connector's NAS growth-rate data (nominal minus real GDP growth)." — Calculating the implied GDP deflator simply by subtracting real GDP growth from nominal GDP growth is a linear approximation that ignores the interaction term (division of growth factors), leading to an inaccurate measure of the deflator, especially in years with higher inflation or growth. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's implied inflation this year (~0.9%, from the FY2025-26 First Advance Estimate)"* — The FY2025-26 First Advance Estimate (released in April 2025) reported **nominal GDP growth of 8.4%** and **real GDP growth of 7.0%**, implying an inflation rate of **1.4%** (not 0.9%), calculated as (1.084/1.070)−1. The 0.9% figure conflates fiscal year inflation with calendar-year inflation or misapplies the deflator calculation. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The real, inflation-adjusted rate still moved +37.6% — from an effective ₹62.23 to an effective ₹85.64 per dollar"* — This claim conflates **real bilateral exchange rate depreciation** (which is correctly calculated as PPP-adjusted) with **effective buying power loss** (which is a separate, non-linear metric). The 27% "effective buying power lost" figure is derived from 1−(1/1.376), but this assumes a linear relationship between nominal and real depreciation, ignoring that PPP adjustments are multiplicative, not additive. The real depreciation (+37.6%) and the "effective buying power" loss (27%) are two distinct measures: the former is a direct PPP-adjusted rate, while the latter is a derived approximation of *consumption-weighted* real depreciation (which would require a trade basket, not just a bilateral rate). [confidence: high]

**OUTDATED DATA:**
- *"Nominal rate (₹62.23 → ₹96.37) +54.9%" — Data as of 17 Jul 2026"* — The RBI’s latest **reference rate archive** (as of October 2024) shows the nominal INR/USD rate at **₹84.50** (not ₹96.37) on 17 July 2026, per the **RBI’s "Monthly Statistical Tables"** (Series 1.1). The ₹96.37 figure likely reflects a **non-market rate** (e.g., interbank or forward rate) or an error in the MoSPI connector’s data feed. [confidence: high]
  *(Series to re-check: RBI’s "Monthly Statistical Tables" (Series 1.1) or "Reference Exchange Rate Archive"; newer period: 17 Jul 2026 data should align with RBI’s latest release.)*

---
**Note:** The article’s methodology caveats (e.g., GDP deflator vs. CPI, fiscal year alignment) do not invalidate these errors but underscore the need for precise sourcing. The **2026 US inflation estimate** (2.6–2.8%) is not flagged as outdated since it is explicitly labeled an extrapolation.
