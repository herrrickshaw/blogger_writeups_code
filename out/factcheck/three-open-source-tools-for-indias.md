# Fact/interpretation check — three-open-source-tools-for-indias

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/three-open-source-tools-for-indias.html`

Text-SHA1: `257009533dfbc4a7`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The FCI repo’s msp_series.csv files the Rs 2,425 rabi wheat MSP under 2024-25 and Rs 2,585 under 2025-26, by sowing year. Its mandi table, like india-mandi-arrivals, uses the marketing year: wheat Rs 2,425 for 2025-26, and Rs 2,585 in india-mandi-arrivals for 2026-27." — The text introduces a temporal mismatch/contradiction regarding the MSP of wheat: earlier in the text (under Step 4), the Rs 2,585 MSP for Madhya Pradesh wheat is explicitly mapped to the 2026-27 marketing year, but here it states it corresponds to the 2025-26 marketing year. [confidence: high]

INTERPRETATION ERRORS:
- "In the harvest month of May, the mandi price sat 6.4% under the Rs 2,585 MSP. By October it was 2.9% above. The script matches the MSP year to the marketing year." — Comparing the modal mandi price of a specific month directly against the annual Minimum Support Price (MSP) and drawing conclusions about whether the price "holds up to MSP" can be misleading, as MSP is typically an announced baseline guarantee for procurement throughout the season rather than a rigid monthly moving target that accounts for intra-season storage and carrying costs. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- **Claim:** “Millets, groundnut and pulses traded below MSP most of the time; wheat and mustard rarely did.”  
  **Reasoning gap:** The metric used is the *share of state‑months* where the weighted mandi price was below MSP. This treats each state‑month equally, ignoring the huge differences in trade volume across states and crops. A volume‑weighted measure could show a very different picture, so the conclusion about “most of the time” is not supported by the data as presented. [confidence: high]  

- **Claim:** “The holding‑economics model found storage and financing costs exceeded price appreciation for all 16 commodities tested, over 12, 24 and 36 months.”  
  **Reasoning gap:** The model relies on stylised assumptions about storage costs, financing rates, and price trajectories, and is not calibrated against observed market outcomes. Presenting the result as a definitive finding overstates what the model can legitimately conclude; it should be framed as “under the model’s assumptions” rather than a factual statement about the real economy. [confidence: high]  

**OUTDATED DATA:**  
- **Claim:** “The MSP series for 14 crops from 2010‑11 … includes the Rs 2,425 rabi wheat MSP under 2024‑25 and Rs 2,585 under 2025‑26.”  
  **Series to re‑check:** Government of India “Minimum Support Price (MSP) – Rabi/Winter Crops” tables. A newer MSP for the 2026‑27 marketing year (announced in September 2026) is not reflected, so the series is missing the latest MSP figure. [confidence: medium]  

- **Claim:** “The guide’s table … shows the share of state‑months … over the last 24 months, up to October 2026.”  
  **Series to re‑check:** Monthly mandi price and arrival data from Agmarknet/UPAG for November 2026. Since the article was published on 12 Nov 2026, at least one additional month of data is now available, making the “latest month October 2026” statement outdated. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The Agmarknet side holds state-by-commodity monthly prices and arrivals from **January 2019 to October 2026**"*
  — Agmarknet’s official data portal (agmarknet.gov.in) does not publish historical arrivals data beyond **2022–23** (the latest full fiscal year available). The article’s claim of arrivals through October 2026 is likely based on an unofficial extract or misinterpretation of the portal’s current-day-only API. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The holding-economics model found **storage and financing costs exceeded price appreciation for all 16 commodities tested** over 12, 24, and 36 months."*
  — This conclusion conflates **historical cost data** (assumed rates) with **future price trends**, which are not guaranteed. The model’s stylized unit economics (e.g., fixed storage rates) do not account for:
  1. **Volatility in mandi prices** (e.g., wheat’s 2026–27 MSP vs. actual market swings).
  2. **Policy changes** (e.g., FCI procurement thresholds, MSP revisions).
  3. **External shocks** (e.g., supply chain disruptions, climate impacts).
  The claim thus **overgeneralizes** from a deterministic model to a broad policy recommendation. [confidence: high]

**OUTDATED DATA:**
- *"The Agmarknet side holds **market-level daily sample (23 field crops, every sixth day since November 2025)**."*
  — Agmarknet’s **official daily mandi price data** (via data.gov.in) is updated in real-time, but the portal’s **historical API** (used here) only provides **current-day snapshots** and lacks a true "daily sample" archive. The article’s claim of a "daily sample" since November 2025 is likely based on an **unofficial extract** or **reconstructed dataset**—not the portal’s live data. To verify, check:
  - Agmarknet’s **API documentation** (data.gov.in) for available historical periods.
  - The **latest fiscal year (2025–26) data dump** from Agmarknet’s portal (if available). [confidence: high]

---
*Note: No other factual, interpretation, or outdated-data issues were found in the provided text.*
