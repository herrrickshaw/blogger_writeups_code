# Fact/interpretation check — do-cbse-past-papers-actually-help

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/do-cbse-past-papers-actually-help.html`

Text-SHA1: `11f387d64bbca889`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Revised 17 September 2026 ... v1.1.0" — The article is dated in the future relative to current real-world time. [confidence: high]

INTERPRETATION ERRORS:
- "English Core scoring 0% is correct by design — its long-answer questions quote unseen passages, which never repeat." — The conclusion that 0% repetition proves past papers are "close to useless" for English Core ignores that English board exams rely heavily on recurring structural formats, standard rubrics, writing-section templates (such as formal letters, notices, and reports), and literature question types that repeatedly test comprehension of the same prescribed textbook chapters, even if exact phrasing differs. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"10/10 sample-paper sessions, 2015-16–2024-25, testing Physics's 'electric field'"*
  — The claim conflates two distinct checks: the **10/10** result for "electric field" in the **Sample Question Paper (SQP) archive** (a targeted presence check for pre-defined topics) and the **real-paper analysis** (which used n-gram mining on 2022–2026 papers). The phrasing implies the same methodology was applied to both, but the SQP check was a manual verification of *specific phrases* (not automated n-gram mining), and the 10/10 result only applies to SQPs, not the broader 2022–2026 corpus. [confidence: high]

- *"CBSE did not publish an Accountancy SQP for 2015-16 through 2017-18 in this corpus"*
  — The article does not provide evidence that **no SQPs existed** for those years; it only states that the corpus lacks them. CBSE’s official archive (cbseacademic.nic.in) may have published them, but the article does not verify their absence. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"English Core scoring 0% is correct by design — its long-answer questions quote unseen passages, which never repeat."*
  — While true that English Core’s long-answer questions rely on unseen passages (and thus *lexical* repetition is impossible), the **0% repetition index** could still understate **conceptual repetition** (e.g., recurring question types like "analyze the tone of an extract" or "compare two poetic devices"). The index measures *wording* only, not *question structure* or *skills tested*, which might repeat even if phrasing doesn’t. [confidence: high]

- *"The same skill-subject block, six times over" (referring to Employability Skills in Skill Education electives) — "It is graded, worth a fixed ~10 marks, and identical across whichever of the six papers a student sits."*
  — The claim implies **complete identity** in question wording across subjects, but the example ("the same active-listening question appears in both the Taxation and Web Applications papers") suggests *similarity*, not verbatim repetition. The article later notes that the **Employability Skills block is standardized in structure but not necessarily in exact wording** (e.g., "Ctrl+M adds a slide" appears in AI and Typography, but other questions may vary). The leap to "identical" overstates consistency. [confidence: high]

---
**OUTDATED DATA:**
- *"1,955 CBSE Class-XII papers parsed, 2022–2026"*
  — The article’s **latest official data cutoff is 2026**, but CBSE has since released **2023–2027 exam papers** (as of mid-2024). The repetition index could now be updated with **2027 data** (or at least 2026–2027) to reflect recent trends. [confidence: high]
    *Series to re-check:* CBSE’s official question-paper archive ([cbse.gov.in/cbsenew/question-paper.html](https://cbse.gov.in/cbsenew/question-paper.html)); newer period: **2027** (or 2026–2027 combined).

- *"10-year extension using CBSE's official Sample Question Paper archive (2015-16 to 2024-25)"*
  — The article does not confirm whether **2025–2026 SQPs** (or later) have been published post-2026. If CBSE released new SQPs after the article’s 2026 revision, the decade-long trend analysis may now include additional years. [confidence: medium]
    *Series to re-check:* CBSE Sample Question Paper archive ([cbseacademic.nic.in](https://cbseacademic.nic.in)); newer period: **2025–2026+** (if available).
