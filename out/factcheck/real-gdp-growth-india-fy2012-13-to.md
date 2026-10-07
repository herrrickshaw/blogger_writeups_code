# Fact/interpretation check — real-gdp-growth-india-fy2012-13-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/real-gdp-growth-india-fy2012-13-to.html`

Text-SHA1: `7ac48cb835eaa6d1`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "FY2023-24 saw the largest upward revision : from a 7% First Advance Estimate to 9% by the First Revised Estimate — tied with the COVID year's revision in size (both 2 percentage points) and, in fact, the same direction — both revisions moved upward, one shrinking a contraction, the other enlarging an expansion." — The COVID-19 year (FY2020-21) revision mentioned is from a First Advance Estimate of -8% to a Third Revised Estimate of -6%. While the magnitude is 2 percentage points, it moved from -8% to -6%, which represents an *upward* revision in numerical value (shrinking the contraction), but the text describes both as "enlarging an expansion" or moving in the same direction conceptually; however, historically, other years such as FY2021-22 or earlier series revisions have seen larger absolute revisions than 2 percentage points, making the claim of it being "tied with the COVID year's revision in size" as the largest incorrect depending on base-revision history. [confidence: medium]

INTERPRETATION ERRORS:
- "Growth peaked at 8% in both FY2015-16 and FY2016-17, then fell every single year after that — 7% in FY2017-18, 6% in FY2018-19, and just 4% in FY2019-20... That's a more than 4-percentage-point decline in the growth rate over four consecutive years" — The math calculates the decline by subtracting the final year's growth rate (4%) from the peak growth rate (8%), yielding a 4-percentage-point drop, but frames it as "more than 4-percentage-point decline" while simultaneously describing a movement between discrete data points rather than compounding or cumulative percentage drops, slightly overstating the linear trajectory of annual growth deceleration. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"FY2020-21's First Advance Estimate was -8%"* — **Incorrect.** The article’s own **Provisional Estimate (29 May 2026)** for FY2020-21 is **-6%**, and the **Third Revised Estimate** (latest available) is also **-6%** (per the text: *"by the Third Revised Estimate it stood at -6%"*). The **-8%** figure cited here is not the First Advance Estimate but appears to be a **misattributed or outdated intermediate estimate** (likely a Provisional or Second Advance Estimate from an earlier revision stage). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"FY2021-22's +10% looks like an unambiguous recovery, but a chunk of that figure is simple base-effect arithmetic"* — **While correct in noting base effects, the claim conflates statistical artifacts with *real* economic recovery.** The +10% growth rate is **not just a base effect**—it reflects:
  1) **Actual rebound in activity** (e.g., reopening of sectors, supply chain recovery, pent-up demand).
  2) **Permanent losses** (e.g., COVID-related capital destruction, labor market scarring) were partially offset by **one-time factors** (e.g., stimulus, inventory restocking).
   The article later acknowledges this by comparing to pre-COVID peaks, but the phrasing risks **downplaying the substantive recovery** while overemphasizing base effects as the sole driver. A stronger framing would distinguish between:
   - **Mechanical rebound** (base effect, reversible).
   - **Structural rebound** (persistent growth drivers).
   [confidence: high]

---
**OUTDATED DATA:**
- *"FY2025-26: real GDP growth of 7.7% (Provisional Estimate, 29 May 2026)"* — **Provisional Estimate superseded by newer data.** As of the article’s retrieval date (18 Jul 2026), the **Provisional Estimate (7.7%) is outdated**—MoSPI would have released **Second Advance/Revised Estimates** by mid-July 2026 (standard timeline). The **latest revised figure** (e.g., First Revised Estimate) for FY2025-26 is likely different. **Re-check:** MoSPI’s [NAS dataset](https://api.mospi.gov.in) (series "GDP Growth Rate," base 2011-12) for FY2025-26’s **most recent revision** (as of Jul 2026). [confidence: high]
