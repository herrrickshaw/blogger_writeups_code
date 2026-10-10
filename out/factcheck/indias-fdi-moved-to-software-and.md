# Fact/interpretation check — indias-fdi-moved-to-software-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-fdi-moved-to-software-and.html`

Text-SHA1: `cce93f75a9511901`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
- "No sector has a negative implied inflow, which is the first sign the two tables are on the same footing." — A non-negative result when subtracting two cumulative tables spanning a 6.25-year gap does not demonstrate that the tables share the same vintage, methodology, or sector definitions. Because gross inflows across all sectors were large over that period (~$313 billion total), net positive residuals would easily overwhelm and conceal retrospective data revisions or inter-sector reclassifications between the 2017 and 2023 releases. [confidence: high]

OUTDATED DATA:
- "$645.4 bn FDI equity inflow into India from April 2000 to June 2023, in the last sector table DPIIT put on the open data portal" — DPIIT Quarterly Fact Sheet on Foreign Direct Investment (FDI); newer official releases exist covering the full 2023-24 fiscal year (through March 2024) and subsequent periods. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- **Claim:** “The yearly average rose from $19.5 billion to about $50.1 billion. The inflow was also more concentrated: the five biggest sectors took 58.1 % of it against 44.9 % before.”  
  **Reasoning gap:** The comparison treats the two periods (2000‑01 to 2016‑17 vs. April 2017 to June 2023) as directly comparable, even though the “after” figures are derived by subtracting a cumulative table that may incorporate restatements of earlier years and changes in sector classification. Those adjustments can shift amounts between periods without any real change in investor behaviour, so the conclusion that average inflows have risen and that FDI has become more sector‑concentrated is not fully supported by the data. [confidence: high]  

- **Claim:** “Software and hardware went from $24.7 billion before April 2017 to about $71.2 billion after, 2.9 times as much, and from 7.4 % of the inflow to 22.7 %.”  
  **Reasoning gap:** The “after” amount is obtained by subtracting the cumulative 2000‑2023 total from the earlier 2000‑2017 total. Because DPIIT periodically revises historic figures and may re‑classify activities between sectors, part of the increase could be a statistical artefact rather than a genuine surge in software‑related FDI. Using this derived number to imply a dramatic shift in investor preference overstates what the data can reliably show. [confidence: high]  

**OUTDATED DATA:**  
- **Claim:** “$645.4 bn FDI equity inflow into India from April 2000 to June 2023.”  
  **Series to re‑check:** DPIIT “Foreign Direct Investment (FDI) Equity Inflows – cumulative by sector” (data.gov.in). A newer release covering up to at least June 2024 (and possibly June 2025) is likely available as of October 2026, which would change the cumulative total. [confidence: high]  

- **Claim:** “The portal lists the resource as updated on 15 June 2022, but the data run to 30 June 2023.”  
  **Series to re‑check:** Same DPIIT cumulative file metadata. The portal’s “last updated” timestamp should reflect the most recent revision (likely after June 2023); the cited date is probably outdated. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"$20 bn → $50 bn Average yearly inflow before and after April 2017"* — The article’s own subtraction shows **$19.5 bn** (not $20 bn) for the pre-2017 period and **$50.1 bn** (not $50 bn) for the post-2017 period. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Software and hardware took 22.7% of the second amount [post-2017], against 7.4% of the first [pre-2017]"* — The claim conflates **share of inflow** (22.7% vs. 7.4%) with **absolute dollar growth** ($71.2 bn vs. $24.7 bn), which is a 2.9x increase. The article later notes the rise began *before* 2017 (11.4% in 2015–16/17), so the "after 2017" share is misleadingly framed as a sudden shift. [confidence: high]

**OUTDATED DATA:**
- *"$645.4 bn FDI equity inflow into India from April 2000 to June 2023"* — The cumulative file’s metadata claims a **15 June 2022 update**, but the data runs to **30 June 2023**. DPIIT’s latest official cumulative FDI equity inflow (as of mid-2024) likely exceeds this figure. Re-check: DPIIT’s open data portal (data.gov.in); newer period: FY2023–24+ cumulative. [confidence: high]
