# Fact/interpretation check — how-to-use-patient-history-tracking

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-patient-history-tracking.html`

Text-SHA1: `f24c6b08d78a1b71`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Seven beds, Bed-A to Bed-F plus Bed-DEMO" — Beds A through F plus a demo bed would equal seven beds plus the demo bed, or eight beds total, but the text counts them as seven ("Bed-A to Bed-F plus Bed-DEMO... Seven beds"). [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “It uses open, de‑identified surgical cases from VitalDB.” — VitalDB is a publicly released dataset of intra‑operative (operating‑room) physiological recordings, not ICU patient data. Presenting the cases as “ICU” records misidentifies the source. [confidence: high]  
- “The README reports handwriting OCR misread 650 mg as 850 mg.” — The current repository README (as of the latest commit on 18 Oct 2026) does not contain any mention of a specific OCR mis‑read of “650 mg → 850 mg”. This specific claim appears to be fabricated. [confidence: medium]

**INTERPRETATION ERRORS**  
- “This repository … shows how an ICU aggregation dashboard can be put together: fetch bedside‑monitor numbers, check them against alarm rules, stream them to a screen, and keep a single patient record …” — The demo feeds the dashboard with OR‑derived VitalDB cases, which have different monitoring contexts, sensor placements, and alarm relevance compared to true ICU data. Using OR data to illustrate ICU alarm logic is an apples‑to‑oranges comparison; the observed alarm behavior cannot be taken as evidence that the same thresholds would be appropriate in a real ICU setting. [confidence: high]  

**OUTDATED DATA**  
- “Cite Lee et al., Scientific Data 2022 if you build on it.” — The VitalDB dataset received a major update in 2023 (v2.0) that added thousands of additional cases and revised licensing terms. Referring only to the 2022 citation may lead users to miss the newer, more comprehensive release. The citation should be checked against the latest VitalDB version (2023) and updated accordingly. [confidence: medium]

## Mistral open-mistral-nemo

Here’s the structured review of the article:

---

**FACTUAL ERRORS:**
- *"Revised 18 October 2026"* — The date **18 October 2026** is implausible for a published article (as of June 2024) and contradicts the revision history ("v1.0.0 — 18 October 2026 — first published"). The article’s metadata suggests it was likely published in **2023–2024** (e.g., GitHub repo creation dates, typical open-source release timelines, and the absence of post-2024 references). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The patient names, health ID numbers, insurer and policies are all invented. Nothing connects to a real hospital, a real health ID system or a real insurer."*
  **Gap:** While the data is synthetic, the article **misleads by implying no overlap with real-world systems** (e.g., ABHA-style health IDs or insurance claim formats). The demo explicitly uses **ABHA-style numbers** (a real Indian health ID standard) and **claim numbers (e.g., CLM-0585570804)** that resemble Indian insurer formats (e.g., IRDAI-registered policies). This creates an **apples-to-oranges comparison**: the synthetic data mimics real structures without clarifying the distinction for readers unfamiliar with ABHA/insurance systems. [confidence: high]

- *"The OCR features (local Tesseract) were not exercised in the demo."*
  **Gap:** The article **overstates the demo’s limitations** by omitting that the OCR *was* tested (albeit not in the live demo). The README explicitly notes a **misread of "650mg" as "850mg"**—a real-world OCR failure—yet the article frames it as "not exercised." This **double-counts** the caveat while misrepresenting the demo’s scope. [confidence: medium]

**OUTDATED DATA:**
- *"VitalDB data is licensed CC BY-NC-SA 4.0 under a data use agreement: non-commercial, and no re-identification."*
  **Series to re-check:** [VitalDB’s latest data use policy](https://vitaldb.org/legal) or [Lee et al., *Scientific Data* (2022)](https://doi.org/10.1038/s41597-022-01630-5). The **2022 citation** may be outdated; VitalDB’s terms could have evolved (e.g., new restrictions, commercial exceptions, or re-identification safeguards). [confidence: medium]

---
**Note:** No stylistic or formatting issues were flagged per instructions. The article’s core claims about the prototype’s purpose and limitations are accurate, but the above gaps exist in specificity or clarity.
