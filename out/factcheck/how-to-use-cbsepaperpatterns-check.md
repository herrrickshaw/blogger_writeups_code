# Fact/interpretation check — how-to-use-cbsepaperpatterns-check

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-cbsepaperpatterns-check.html`

Text-SHA1: `48e52da03d7cf227`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
- "Teachers, students and tutors get an evidence-based answer to 'do the papers repeat?' by subject, instead of coaching-industry folklore. It replaces gut feeling with one number per subject: the share of marks in 4-mark-or-higher questions sitting on a phrase that recurs in at least 3 of 5 exam years." — The methodology tracks recurring 2-to-4 word lexical n-grams (such as "electric field" or "balance sheet"), which are standard, unavoidable curricular terminology in high-mark questions rather than duplicated questions. Equating the presence of recurring subject vocabulary with "papers repeating" is an extrapolation that conflates lexical recurrence with actual question reuse. [confidence: high]
- "The result is uneven: Accountancy 49%, Physics 44%, Economics 38% versus Chemistry and Biology at 5%." — This is an apples-to-oranges comparison across subjects. Accountancy and Physics high-mark questions rely heavily on standardized phrasing ("balance sheet", "electric field"), whereas Chemistry and Biology rely extensively on chemical formulas, reaction equations, diagrams, and diverse biological nomenclature that vary textually even when testing identical concepts. Concluding that repetition is intrinsically lower in Chemistry and Biology overlooks the fact that this is an artifact of the text-only n-gram parsing method. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“An analysis of 1,955 CBSE Class XII question papers (2022 to 2026)”** – The total number of CBSE Class XII papers released each year is far lower (≈ 2 papers per subject, ~30 subjects ⇒ ~60 papers per year, ≈ 300 papers over five years). 1,955 papers would require roughly 390 papers per year, which does not match CBSE’s published exam schedule. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“Teachers, students and tutors get an evidence‑based answer to ‘do the papers repeat?’ … It replaces gut feeling with one number per subject: the share of marks in 4‑mark‑or‑higher questions sitting on a phrase that recurs in at least 3 of 5 exam years.”** – The repetition index measures only lexical overlap of short phrases, not whether the underlying concepts, problem types, or syllabus coverage repeat. Concluding that a high index proves “papers repeat” conflates surface‑level wording similarity with substantive exam repeatability, which the article itself later admits is a limitation. [confidence: high]  

**OUTDATED DATA**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"1,955 Class XII papers analysed (2022-2026)"* — The article states the analysis covers **2022–2026**, but CBSE’s official exam schedule for **Class XII in 2026** was not yet conducted at the time of publication (28 October 2026). While the repo may include *projected* or *mock* papers, the claim conflates real exam years with hypothetical data. [confidence: high]

**INTERPRETATION ERRORS:**
- *"2 content topics recurring at high marks in 4 of 5 years"* — This claim is misleading because the **5-year window (2022–2026)** includes **2026**, which is not a completed exam year. Even if 2026 data is included, the phrasing implies a *stable 5-year trend* (e.g., 2022–2026), but the repetition index is likely skewed by incomplete or hypothetical 2026 data. [confidence: high]

**OUTDATED DATA:**
- *"Repetition index by subject (data/subject_repetition.csv, read 19 October 2026)"* — The CSV was last read on **19 October 2026**, but the article was published on **28 October 2026**. While the data may not be outdated, the claim of "latest" or "current" figures is ambiguous. For absolute accuracy, the source should specify whether the CSV reflects **finalized 2025 data** or includes provisional 2026 results. [confidence: medium]

---
*Note: No other factual, interpretive, or data-specific errors were identified based on the provided text.*
