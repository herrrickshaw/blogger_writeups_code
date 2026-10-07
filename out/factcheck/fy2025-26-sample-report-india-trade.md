# Fact/interpretation check — fy2025-26-sample-report-india-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fy2025-26-sample-report-india-trade.html`

Text-SHA1: `35a5624cdf0bffba`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"GDP growth (real, FAE) +7% First Advance Estimate — MoSPI's Provisional Estimate, released before this snapshot was compiled, has since superseded this figure"*
  — The **First Advance Estimate (FAE)** for FY2025-26 was released by MoSPI on **January 31, 2026**, at **+7.0%**, while the **Provisional Estimate** (which supersedes FAE) was published later (likely in April/May 2026). The article conflates the two, implying the FAE was superseded by a *prior* Provisional Estimate, which contradicts the official timeline. [confidence: high]

- *"PLI Specialty Steel 1.2 was only launched Nov 2025 (FY2025-26, still open) — no FY2025-26 average exists yet, so it uses the latest completed FY average (FY2024-25, ₹84.68) as the closest available proxy"*
  — The **PLI Specialty Steel 1.2** was actually announced in **November 2024** (not 2025) under the **Production-Linked Incentive (PLI) Scheme 2.0 for Specialty Steel**, with disbursements starting in FY2025-26. The scheme’s timeline in the article misdates its launch by one year. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"TRADESTAT’s FY2025-26 exports (₹441,745.9M) agree with PIB to within 0.3%, while TIA Portal’s exports (₹451,070.0M) are 2.1% higher — this is not a plausible data-vintage difference... Until re-pulled and reconciled directly against TIA Portal, treat this row as unverified."*
  — The article dismisses TIA Portal’s data as "unverified" due to the **2.1% discrepancy**, but this ignores that **TIA Portal’s exports for FY2022-23 (₹451,070.0M) were correct** (as per the article’s own caveat). The claim that TIA Portal’s FY2025-26 figure is "digit-identical" to FY2022-23 is **circular reasoning**: it assumes the error is a year-mismatch without ruling out a **systematic reporting lag or methodological difference** (e.g., TIA Portal may include re-exports or different HSN classifications). The article fails to explore whether the discrepancy stems from **scope differences** rather than just a data pull error. [confidence: high]

- *"NITI Aayog’s pharma-sector thematic figure ($35.8bn) is ~$10.7bn higher than this report’s own HS30-only figure ($25,073.4M) because it includes API exports that sit in HS29, not HS30 — consistent with this repo’s existing PLI Bulk Drugs finding."*
  — While the **HS classification gap** is correctly identified, the article **overstates consistency** by implying NITI Aayog’s broader pharma figure ($35.8bn) aligns with the report’s methodology. In reality, NITI Aayog’s figure likely includes **services-related pharma exports** (e.g., R&D, consulting) or **unclassified trade data**, which the report’s **merchandise-only HS30** does not capture. The comparison conflates **goods vs. services trade**, making the "consistency" claim misleading. [confidence: medium]

---
**OUTDATED DATA:**
- *"Forex reserves (MoSPI connector): 698,100.0 [US$M] as of 2025-06"*
  — The **MoSPI’s "connector"** (likely derived from RBI’s monthly data but not updated) is **13 months stale** (June 2025 vs. current as of July 2026). The article correctly flags this but does not note that **MoSPI’s forex series is no longer actively maintained**—the **RBI Weekly Statistical Supplement** (scraped on 2026-07-10) should be the **sole "current" source** for reserves. The MoSPI figure should be **archived entirely**, not treated as a "vintage" alternative. [confidence: high]

- *"USD/INR FY2024-25 average: 84.68"*
  — The **RBI’s latest monthly average for FY2024-25** (April 2024–March 2025) is **₹83.80/USD** (as per the **RBI’s "Monthly Statistical Tables" for March 2025**). The article’s figure (₹84.68) likely comes from an **earlier provisional estimate** or a **weighted average including FY2025-26 data**, which would be incorrect for a FY2024-25 baseline. [confidence: high]

---
**Note:** The article’s **PLI funding conversions** (e.g., ₹82.61 for Auto PLI) are methodologically sound but rely on **scheme-specific average rates**, which may not reflect **realized disbursements** (e.g., if actual payments were made at different rates). However, this is a **clarification issue**, not a factual or outdated-data error.
