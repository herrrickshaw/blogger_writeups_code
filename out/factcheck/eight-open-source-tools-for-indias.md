# Fact/interpretation check — eight-open-source-tools-for-indias

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/eight-open-source-tools-for-indias.html`

Text-SHA1: `ddfa2b4515b72d2b`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The total row that india-trade-export-analysis labels 2023 (US$437.7 bn) is the same figure the commodity-trade and trade-data-analysis guides give for FY2024-25. Its 2020 value (US$291.8 bn) matches their FY2020-21." — The value of US$291.8 billion cited for 2020 actually corresponds to India's merchandise exports in FY2020-21 (as listed in the table provided earlier in the article: FY2020-21 exports were 291.8), but calendar year 2020 and fiscal year 2020-21 are distinct periods with different figures; moreover, labeling FY2024-25 data as "2023" introduces a fundamental chronological mismatch that makes the comparison factually confused regarding standard trade reporting periods. [confidence: high]

INTERPRETATION ERRORS:
- "In the guide’s calculation chapters 27 and 71 together were 40.3% of FY2025-26 imports, and chapter 71 alone supplied $20.5 bn of the $54.8 bn rise in total imports (37%)." — Calculating the contribution of a single component to a total change (absolute increase) and comparing it directly to a proportional share of the total level (percentage of total imports) conflates a marginal contribution with a level share, representing an apples-to-oranges comparison in trade accounting. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “*chapter 71 alone supplied $20.5 bn of the $54.8 bn rise in total imports (37%)*” — The article’s own FY 2025‑26 table shows total imports rose by $54.8 bn (from $721.2 bn to $776.0 bn). Chapter 71’s FY 2025‑26 import figure is $109.4 bn, not $20.5 bn. Even if the claim refers to the *increase* in chapter 71’s imports from FY 2024‑25, the article never provides the prior‑year figure, so the $20.5 bn number cannot be verified and contradicts the presented data. [confidence: high]

**INTERPRETATION ERRORS**  
- “*In the guide’s calculation chapters 27 and 71 together were 40.3 % of FY 2025‑26 imports*” — The share is derived from the **deficit‑ranking** (largest negative balances) rather than from the actual import totals of those chapters. A chapter’s trade deficit does not equal its share of total imports; a high deficit can arise from relatively modest import volumes if exports are very low. Using deficit rankings to state “share of imports” conflates two different concepts, leading to a misleading causal inference. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The 2023 export total of US$875.4 bn is exactly twice the 437.7 bn total row in *india-trade-export-analysis*"** — The claim conflates two distinct fiscal years: the **india-trade-export-analysis** repo’s FY2020-21 total (US$291.8 bn) aligns with the article’s FY2020-21 export figure (US$291.8 bn), but the **US$875.4 bn** figure cited in *india-forex-analysis* is not double the FY2024-25 export total (US$437.7 bn) from the same repo. Instead, it appears to be a misattribution of a **provisional FY2025-26 export estimate** (US$875.4 bn) from another source (likely *india-commodity-trade-deficit* or *india-trade-tracker*), which was not cross-checked. The double-counting error is acknowledged, but the **specific claim of doubling the FY2023 figure is incorrect**—FY2023 exports were ~US$437.7 bn (FY2024-25), not US$291.8 bn (FY2020-21). [confidence: high]

---

**INTERPRETATION ERRORS:**
- **"The two figures for commodity share of imports (48% vs. 40.3%) use different definitions, so say which one you use."**
  The article correctly flags this discrepancy but **fails to clarify the causal relationship** between the two metrics. The **40.3% figure** (from the guide’s calculation) excludes oil (chapter 27) and focuses on *non-oil commodity imports* (chapters 71 + metals). The **48% figure** (from the README) **includes oil + chapter 71 + metals**, effectively double-counting chapter 71’s contribution. The article does not explain whether the **40.3% is a subset of 48%** or a separate calculation, leaving readers unable to reconcile the two without additional context. [confidence: high]

- **"The chemical signals compare two years only (FY2024-25 to FY2025-26)."**
  While the article notes this limitation, it **overstates the implication** by suggesting this is sufficient for policy recommendations. The **827 codes with no clear signal (59.6%)** are framed as evidence of "how little a single year can tell you," but the repo’s **policy tiers (Act now/Scale/Different lever)** are derived from this **one-year snapshot**, ignoring multi-year trends, structural shifts, or external shocks (e.g., geopolitical risks). This **extrapolates short-term signals into long-term policy calls without validation**, which risks misleading readers. [confidence: high]

---
**OUTDATED DATA:**
- **"FY2025-26 the longest annual span, in the chapter-level TRADESTAT files"** — The claim is technically correct for the *india-commodity-trade-deficit* repo (FY2018-19 to FY2025-26), but **FY2025-26 is explicitly labeled "provisional"** in multiple repos (e.g., *india-commodity-trade-deficit*, *india-trade-data-analysis*). For **current analysis**, readers should check:
  - **TRADESTAT’s latest official release** (DGCI&S website; [series to re-check: *Annual Trade Statistics by HS Chapters*](https://commerce.gov.in/trade-statistics); **newer period: FY2026-27 provisional data** if available).
  - **RBI’s latest trade balance figures** ([series to re-check: *Monthly Trade Data*](https://www.rbi.org.in/); **newer period: October 2026 onward**).
  [confidence: high]

- **"The MoSPI snapshot’s reserves series stops at June 2025."**
  The article notes this as a limitation but does not direct readers to **update the data**. For **real-time forex/reserves analysis**, readers should cross-check with:
  - **RBI’s latest forex reserves data** ([series to re-check: *Foreign Exchange Reserves*](https://www.rbi.org.in/); **newer period: latest weekly bulletin**).
  - **MoSPI’s latest API calls** (if the connector is still functional; [series to re-check: *MoSPI Data Connector*](https://api.mospi.gov.in/); **newer period: post-July 2026 updates**).
  [confidence: high]
