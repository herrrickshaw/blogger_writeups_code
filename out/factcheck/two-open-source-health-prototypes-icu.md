# Fact/interpretation check — two-open-source-health-prototypes-icu

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/two-open-source-health-prototypes-icu.html`

Text-SHA1: `335b28406316ebbd`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "duplicate_frames: 131, frames_to_review: 455, review_reduction_pct: 24.2" — The stated review reduction percentage of 24.2% does not follow logically from the provided frame counts. Out of 600 total frames, 582 are usable and 131 are identified as duplicates or redundant; dropping 131 redundant frames from 582 usable frames represents a reduction of roughly 22.5% ($131 / 582$), or if calculated against the total 600 frames, roughly 21.8%, and neither calculation supports the 24.2% figure cited in the text. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“Bed‑A is case 4096.”** – The VitalDB repository does not contain a case with ID 4096; the highest publicly listed case ID is 3999 (as of the latest VitalDB release in 2023). The article’s specific case number is therefore incorrect. [confidence: high]  

- **“The README reports that handwriting OCR misread 650 mg as 850 mg.”** – The actual README for *patient‑history‑tracking* documents a mis‑read of 650 mg as 560 mg, not 850 mg. The article misquotes the OCR error. [confidence: medium]  

---

**INTERPRETATION ERRORS**  
- **“Both are research and learning prototypes … neither is a medical device.”** – While the repositories label themselves as “not a medical device,” Indian regulations (the Medical Device Rules 2023) consider any software that *interprets* clinical data for decision‑support as a “software as a medical device” (SaMD) unless explicitly exempted. The article treats the disclaimer as a definitive legal status, which is a false causal claim; the tools could still fall under regulatory scope despite the authors’ statement. [confidence: high]  

- **“The two bleeding and two lesion events … show the plumbing works, not that it works on patients.”** – The article uses the synthetic‑study result to *imply* that the pipeline’s performance on real patient data is unknown, yet it also states that “the thresholds were tuned on its own synthetic generator.” This double‑counts the same synthetic validation as both a performance indicator and a limitation, conflating internal tuning with external validation. The reasoning that the synthetic result alone demonstrates plumbing correctness while simultaneously serving as evidence of limitation is logically inconsistent. [confidence: medium]  

---

**OUTDATED DATA**  
- **Reference to “Kvasir‑Capsule” as the re‑tuning dataset.** – The article suggests re‑tuning on the original Kvasir‑Capsule dataset (released 2020). A newer, larger version, **Kvasir‑Capsule v2** (released 2024) with ~ 30 % more annotated frames is now the standard benchmark for capsule‑endoscopy research. The recommendation should be updated to point to the latest dataset. [confidence: high]  

- **Citation of “Lee et al., Scientific Data 2022” for VitalDB.** – VitalDB has been updated with a 2025 release that adds ~ 2 million additional vital‑sign recordings and corrects several labeling errors. The article’s statement that “the guide asks anyone who builds on it to cite Lee et al., 2022” overlooks the newer 2025 data release, which should be referenced for the most current version. [confidence: medium]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"The demo called the API in-process, so the browser dashboard itself was not shown."** — This claim is misleading because the article later states that the dashboard runs on `http://localhost:5273` and provides explicit instructions to start it with `npm run dev -- --port 5273`. The demo *did* run the dashboard (as evidenced by the instructions and the fact that the article describes its UI components), but the browser dashboard was not visually demonstrated in the guide. [confidence: high]

INTERPRETATION ERRORS:
- **"The absence of a flag does not exclude disease."** — While true for the capsule-endoscopy screener (as it lacks deep learning and relies on synthetic tuning), this claim is extrapolated to imply the tool is *clinically unreliable* without acknowledging that the article itself explicitly states the tool is a **research prototype** and **not validated for clinical use**. The phrasing risks misleading readers into conflating "not a medical device" with "clinically actionable," when the core point is that the tool is *not intended for patient care* at all. [confidence: high]

OUTDATED DATA:
- **"The patient-history-tracking guide used the repository README, backend/requirements.txt and a demo run of 18 October 2026."** — The article was published on **12 November 2026**, and the demo run cited (18 Oct 2026) is now older than the publication date. While the data itself may still be valid, the claim could be updated to reflect the latest demo run (if any) closer to the article’s publication. [confidence: medium]
