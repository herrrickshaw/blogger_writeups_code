# Fact/interpretation check — iem-conversion-historical-performance

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/iem-conversion-historical-performance.html`

Text-SHA1: `ea0950e9112bd35f`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Conversion (Part B implemented ÷ same-year Part A filed) is a same-period flow ratio, not a cohort match: this year's Part B often implements filings from 2-3 years earlier, so a high ratio can mean either "government executing faster" or "an old backlog finally landing." ... Conversion % | Note | ... 2024 | 602,082 | 986 | 493,765 | 1,165 | 82.0 |" — The article computes a conversion rate by dividing Part B implemented in year $t$ by Part A filed in year $t$. Because factory construction and implementation take multiple years, the numerator (Part B in year $t$) does not correspond to the denominator (Part A in year $t$). Dividing contemporaneous flows produces mathematically volatile and misleading ratios that can exceed 100% simply due to denominator drops or backlog clearing, making a "conversion rate" calculated this way structurally flawed for measuring actual project conversion. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Rs 4.94L cr CY2024 implemented — the best year on record"* — The claim conflates **calendar-year (CY) 2024 IEM Part B (Rs 493,765 cr)** with the earlier **2017 Part B value (Rs 71,396 cr)** for comparison. The highest *recorded* Part B value is actually **Rs 583,096 cr (up to Dec 2025, partial-year)**, not CY2024. [confidence: high]

**INTERPRETATION ERRORS:**
- *"2024 first year IEM implementation > FDI equity inflow"* — The comparison mixes **calendar-year (CY) IEM Part B (Rs 493,765 cr, 2024)** with **fiscal-year (FY) FDI equity inflow (Rs 421,929 cr, 2024-25)**. The periods overlap but are not identical (CY2024 IEM vs. FY2024-25 FDI), and the FDI figure is for a *fiscal year* (April–March), not a calendar year. [confidence: high]

**OUTDATED DATA:**
- *"Source: DPIIT Annual Reports 2018-19 through 2025-26 (reconciled across vintages)"* — The **2025 data is provisional ("Up to Dec 2025")** and likely to revise further in the **2026-27 Annual Report** (released post-publication). The **2019 exclusion** is noted but lacks a formal erratum; the **2025 partial-year figure (109.9%)** is explicitly flagged as upward-revising. [confidence: high]
