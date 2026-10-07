# Fact/interpretation check — cpi-wpi-trends-mospi-bulletin

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/cpi-wpi-trends-mospi-bulletin.html`

Text-SHA1: `347088a8dcc26924`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

Here is the structured response based on the provided article text:

---

**FACTUAL ERRORS:**
- *"Primary Articles [WPI] inflation is 0%"* — Incorrect; the article later confirms Primary Articles inflation was **7.00%** in June 2026 (base 2022-23 series), matching the Office of the Economic Adviser’s press release. The "0%" figure appears to be a placeholder or error in the initial panel. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The sparkline [CPI] covers Jan 2025–Jun 2026, but the YoY inflation label is only computable from January 2026 onward because the base-year-2024 series lacks 2024 comparison months."*
  **Gap:** The claim conflates the *visual range* of the sparkline (Jan 2025–Jun 2026) with the *computable period for YoY inflation* (Jan 2026–Jun 2026). While accurate for the labeled % (which is limited to Jan 2026+), the phrasing implies the sparkline’s full window is irrelevant for YoY analysis, which is misleading—it *does* show trends but cannot reflect YoY rates for 2025. [confidence: high]

- *"WPI is published by MoSPI"* — Repeatedly attributed to MoSPI despite the article’s own correction: *"WPI is published by the Office of the Economic Adviser, DPIIT (Ministry of Commerce & Industry)—not by MoSPI."* This error persists in the headline and subheadings, undermining the later clarification. [confidence: high]

**OUTDATED DATA:**
- *"WPI year-on-year inflation, June 2026 (base 2022-23 series) is 9.87%"* — While correct for the cited press release (14 Jul 2026), the article’s **errata section** notes that the Office of the Economic Adviser later released **May and June 2026 WPI on the new 2022-23 base**, implying potential revisions or superseded figures for these months. Users should cross-check with the latest PIB release or DPIIT’s official tables. [confidence: high]

- *"CPI year-on-year inflation is only computable from January 2026 onward"* — True for the base-2024 series in the MoSPI connector used, but the article does not verify whether **MoSPI has since published a linking factor** to extend comparability to 2025 (as proposed in the "What would fix this" section). Readers may assume this is the *current* limitation without acknowledging potential future updates. [confidence: medium]

---
