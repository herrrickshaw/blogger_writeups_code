# Fact/interpretation check — scan-bottle-deliver-what-ppacs-numbers

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/scan-bottle-deliver-what-ppacs-numbers.html`

Text-SHA1: `243033edd46e812c`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "That's a real, PPAC-reported quarter-on-quarter contraction in actual gas moved..." — The article describes a "year-on-year" drop of 15.6% comparing April–June 2026 to April–June 2025, but mislabels it in this sentence as a "quarter-on-quarter contraction." [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"PSU oil companies' domestic LPG sales in April–June 2026 actually fell 15.6% year-on-year"* — The claim conflates **domestic LPG sales** (likely retail deliveries) with **total LPG sales** (which may include industrial/non-domestic segments). PPAC’s Q1 FY2026-27 report does not explicitly break down the 15.6% decline by segment, but the article later notes that **domestic connections grew to 33.14 crore**—a contradiction if the drop were purely domestic. The source (PPAC’s report) does not clarify whether the 15.6% figure is for **domestic-only** sales or **total LPG sales** (which could include non-domestic users like auto-LPG or industrial). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The domestic LPG cylinder at the center of PPAC's connection and bottling-plant numbers... is not yet a rule PESO is enforcing against domestic LPG the way it now enforces against auto-LPG and CNG cylinders"* — While the article correctly notes that **Rule 6(2)(5) of the Gas Cylinders (Amendment) Rules, 2025** explicitly excludes domestic 14.2 kg LPG cylinders from mandatory scanning enforcement, it **overstates the clarity of the legal ambiguity**. The **2025 amendment’s Rule 6(2)(c)(i)** *does* require a "permanent, tamper-proof barcode" on *all* cylinders (including domestic LPG), but Rule 6(2)(5) later **narrows enforcement** to specific fuels (auto-LPG, CNG, etc.). The gap is that **PESO’s 2026 circulars** (cited in the article) only address industrial/automotive cylinders, leaving domestic LPG in a **regulatory grey zone**—not a definitive "not enforced" status. The article’s conclusion that QR-coding is "still a company-level initiative" may be true in practice, but the law *technically* applies to domestic cylinders unless PESO clarifies otherwise. [confidence: high]

---
**OUTDATED DATA:**
- *"Active domestic LPG connections have grown from 14.9 crore in 2015 to 33.14 crore this July [2026]"* — The **latest PPAC LPG Profile Report** (Q1 FY2026-27) is dated **1 July 2026**, but PPAC typically releases updated reports **quarterly** (e.g., Q2 FY2026-27 would cover 1 October 2026). For **real-time accuracy**, check the **PPAC LPG Profile Report (Q2 FY2026-27)** or the **latest monthly bulletin** (e.g., July 2026 data may have been superseded by August/September 2026 updates). [confidence: high]
- *"LPG coverage, estimated (%) moved from 56.2% in April 2015 to roughly 95.6% by July 2026"* — The **95.6% figure** uses a **revised methodology** (incorporating NFHS-5 data), while the **99.8% figure for 2021** uses the **older census-based method**. The article notes the inconsistency but does not provide a **direct reconciliation** of the two methods. For comparability, PPAC should publish **both old and new estimates for at least one common date** (e.g., 2021 or 2024). [confidence: high]
