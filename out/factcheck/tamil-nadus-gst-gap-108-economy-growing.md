# Fact/interpretation check — tamil-nadus-gst-gap-108-economy-growing

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/tamil-nadus-gst-gap-108-economy-growing.html`

Text-SHA1: `9011607a54ef0d01`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Tamil Nadu's GSDP grew 10.83% in real (inflation-adjusted) terms in FY2025-26, on top of 11.19% the year before" — Real GSDP growth rates of over 10% for large Indian states are historically unprecedented and inconsistent with macroeconomic realities for this period. [confidence: high]
- "RFID-based e-way bill tracking, mandatory from 1 April 2026 for all registered transporters running more than 20 vehicles... Mandatory Ship-To GSTIN reporting, effective 15 June 2026" — The article cites specific future dates and mandates for policy changes beyond the model's knowledge cutoff that appear to be speculative or fabricated future policy timelines. [confidence: medium]

INTERPRETATION ERRORS:
- "GST is a tax on nominal transaction values, so the more directly comparable figure is nominal GSDP growth (13.1%), not real growth — and against that benchmark, the gap between economic growth and GST growth is wider, not narrower." — Comparing a macroeconomic output measure (GSDP) directly to an indirect tax revenue growth figure (GST) without accounting for changes in tax buoyancy, exemptions, rate revisions, or the shift from manufacturing value-added to consumption does not isolate an "administrative capture gap." [confidence: high]
- "Tamil Nadu's count of active GST-registered businesses (GSTINs) grew from 5,20,751 in April 2025 to 7,22,390 in April 2026, a genuine 38.7% expansion in one year... That's a normal lag pattern, not necessarily a failure: a large share of new registrants are likely smaller businesses just crossing the registration threshold, whose individual GST contribution starts small and takes time to scale with turnover." — A 38.7% surge in registered taxpayers alongside flat revenue is attributed entirely to a "timing lag" for small businesses, ignoring the alternative and more likely interpretation of administrative clean-ups, migration of existing unregistered entities due to tightening compliance, or bulk registrations that generate minimal or zero tax liability. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Tamil Nadu's GSDP grew 10.83% in real (inflation-adjusted) terms in FY2025-26"* — **No official GSDP data for FY2025-26 has been released by MoSPI or CAG as of mid-2024 (cutoff).** All figures cited are press estimates or state government sources, not finalized government statistics. [confidence: high]
- *"Mandatory Ship-To GSTIN reporting, effective 15 June 2026"* — **No official GSTN or TN Commercial Taxes Department announcement confirms this rule’s implementation date.** The article cites "industry reporting" but lacks a direct source. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"The more directly comparable figure is nominal GSDP growth (13.1%), not real growth — and against that benchmark, the gap between economic growth and GST growth is wider, not narrower."*
  **Gap:** The claim conflates *nominal vs. real GSDP* with *GST revenue growth* without adjusting GST for inflation. GST is a nominal tax (based on transaction values), so comparing it directly to real GSDP growth (inflation-adjusted) is misleading. A fairer comparison would either:
  1) Use nominal GSDP growth (13.1%) vs. nominal GST growth (≈0.7%), or
  2) Deflate GST collections by the same CPI used for real GSDP to isolate the *capture gap* (not just nominal vs. real).
  The article’s framing implies GST growth should align with *real* GSDP, which ignores GST’s nominal nature. [confidence: high]

- *"Tamil Nadu's effective take was ₹80,047 crore in FY2025-26 — SGST of ₹47,619 crore plus ₹32,428 crore in IGST settled to the state"*
  **Gap:** The claim treats IGST settlement as a *direct revenue source* for the state, but IGST is a *destination-based* tax share (not a "take" in the same sense as SGST). The "effective revenue" metric conflates two distinct flows:
  - SGST (state’s own tax on domestic sales, ~50% of effective take).
  - IGST settlement (a share of interstate GST, ~50%, but tied to consumption, not production).
  This double-counts the state’s role in the GST system, as IGST is already accounted for in the ₹1,30,248 crore *domestic GST* figure. [confidence: high]

---

**OUTDATED DATA:**
- *"Tamil Nadu's domestic GST collection, ₹ crore | FY2021-22: 85,492 | FY2022-23: 104,377 | FY2023-24: 121,329 | FY2024-25: 131,115 | FY2025-26: 130,248"*
  **Series to re-check:** GSTN’s *"Collections-Statewise"* workbook (updated monthly). As of **July 2024**, the latest official FY2025-26 data for Tamil Nadu (if released) would supersede this. The article’s FY2025-26 figure (₹130,248 crore) is likely a **preliminary estimate** (GSTN’s final FY2025-26 data is typically published by **March 2025** for FY2024-25 and **March 2026** for FY2025-26). [confidence: high]

- *"Tamil Nadu's count of active GST-registered businesses (GSTINs) grew from 5,20,751 in April 2025 to 7,22,390 in April 2026"*
  **Series to re-check:** GSTN’s **April 2026 monthly bulletin** (published ~June 2026). The article cites this as a **year-over-year jump**, but GSTN’s data is often revised quarterly. For example, the **April 2025 count** may have been adjusted upward in later releases. [confidence: medium]
