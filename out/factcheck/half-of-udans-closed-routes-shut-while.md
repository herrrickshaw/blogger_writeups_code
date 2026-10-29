# Fact/interpretation check — half-of-udans-closed-routes-shut-while

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/half-of-udans-closed-routes-shut-while.html`

Text-SHA1: `1cffbc56f7cf5362`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Over a route’s life that is 3.5 years of full support against 3 before, about 17% more." — The calculation of "3.5 years of full support" adds the partial percentages incorrectly (100% + 100% + 75% + 50% + 25% = 350%, or 3.5 equivalent years), but comparing this sum of tapered percentages directly against 3 full years of 100% support (300%) is an apples-to-oranges comparison of nominal duration versus aggregate subsidy value. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “Helipads | 3,661 cr | 200 helipads at Rs 15 cr each” — 200 × 15 = 3,000 cr, not 3,661 cr. The total amount and the per‑helipad cost are inconsistent, indicating a factual mistake. **[confidence: high]**  
- “Operation and maintenance support | 2,577 cr | About 441 aerodromes for 3 years; capped at Rs 3.06 cr a year an airport” — 441 × 3.06 cr × 3 years ≈ 4,048 cr, far above the stated 2,577 cr, showing a mismatch between the cap description and the aggregate figure. **[confidence: medium]**

**INTERPRETATION ERRORS**
- “A longer taper addresses only part of why routes fail.” — The article infers that extending the subsidy to five years will help the 166 routes that closed after the three‑year period, but it ignores that many closures (165 routes) occurred while the subsidy was still fully in force, driven by low demand rather than subsidy length. Thus the claim that the longer taper will meaningfully reduce route failures overstates what the data actually support. **[confidence: medium]**  
- “The new scheme roughly doubles the yearly rate so far.” — The comparison uses the historical average subsidy (≈ Rs 536 cr / yr over 9.5 years) versus the projected annual outlay (Rs 1,004 cr / yr). The historical average is skewed by pandemic‑affected years with unusually low spending, so stating the increase is “about twice” extrapolates a simple ratio without adjusting for those anomalies, leading to a misleading interpretation of the magnitude of change. **[confidence: medium]**

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"UDAN turned ten on 21 October"* — UDAN was launched on **31 March 2017** (not 21 October), making its 10th anniversary **31 March 2027** (not October 2026). [confidence: high]

**INTERPRETATION ERRORS:**
- *"Rs 2,960 of airline subsidy per UDAN passenger over ten years"* — This figure conflates **total subsidy paid (Rs 5,091 crore) across all routes (including closed ones) with passenger numbers (1.72 crore)**, ignoring that:
  1) Many closed routes received full subsidies but no passengers.
  2) The cost per passenger **varies wildly** by route (e.g., high-cost heliports vs. low-cost regional flights).
  The claim **misrepresents efficiency** by averaging across all routes, masking the fact that **failed routes may have incurred disproportionate per-passenger costs**. [confidence: high]

**OUTDATED DATA:**
- *"Rs 5,091 crore for 1.72 crore passengers"* — The **latest PIB note (October 2026)** is cited, but the **Rajya Sabha reply (July 2026)** and **CAG audit (March 2023)** are older. For **real-time passenger/route data**, re-check:
  - **PIB’s latest UDAN dashboard** (if available post-October 2026) for FY2026-27 figures.
  - **Civil Aviation Ministry’s annual report (2026-27)** for updated VGF disbursements. [confidence: high]
