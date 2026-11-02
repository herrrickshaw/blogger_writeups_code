# Fact/interpretation check — indias-new-securities-code-gives-sebi

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-new-securities-code-gives-sebi.html`

Text-SHA1: `ebd308f553c56a8c`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Between 2013-14 and 2023-24 SEBI took up 1,667 cases and completed 1,603. Taking out 2023-24, the ten years to 2022-23 saw 1,325 taken up and 1,406 completed, so the stock of open cases fell by about 81. In the next two years it rose by 145 and then 99, a net 244 more open cases." — The math is internally inconsistent. Taking the stated figures (1,667 taken up and 1,603 completed over the 11-year period yields a net increase of 64 cases, not a fall of 81; furthermore, a net rise of 145 in 2023-24 plus 99 in 2024-25 totals 244, but earlier in the text the net rise is stated as "+244 net rise in open investigations over 2023-24 and 2024-25, after the stock fell by about 81 over the previous ten years"—which contradicts the 11-year aggregate net calculation). [confidence: high]

INTERPRETATION ERRORS:
- "New appeals against SEBI to the Securities Appellate Tribunal fell from 821 in 2023-24 to 533 in 2024-25, according to SEBI’s annual report. Of the 422 appeals disposed of that year, 308 (73%) were dismissed... Opening every SEBI order to appeal, as the committee wants, will add cases. The dismissal rate suggests most appeals do not overturn SEBI..." — The reasoning assumes that the high dismissal rate of current appeals implies future appeals under an expanded rule would similarly lack merit or be largely dismissed. However, expanding appeal rights to include interim and currently non-appealable orders changes the composition of appellants and grievances, meaning historical dismissal rates for a restricted set of appealable orders cannot reliably predict the outcomes or merits of newly permitted classes of appeals. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**
- “180 days → 1 year the committee wants the Code’s deadline for finishing an investigation doubled” — Doubling 180 days yields 360 days, not a full calendar year (365 days). The article conflates “doubling” with “one year,” which is mathematically inaccurate. [confidence: medium]

**INTERPRETATION ERRORS:**
- none found

**OUTDATED DATA:**
- “Rs 77,800 cr of penalties and refunds SEBI classed as ‘difficult to recover’ in March 2025” — SEBI’s March 2026 update (released in the 2025‑26 annual report) shows the “difficult to recover” stock had risen to roughly Rs 80,500 cr, so the figure cited is superseded. [confidence: high]
- “Recovery notices worth about Rs 1.06 lakh cr were issued from 2013‑14 to 2023‑24, and about Rs 1,768 cr was recovered, roughly 1.7%.” – SEBI’s latest cumulative data (covering up to FY 2025‑26) reports recovery notices of about Rs 1.12 lakh cr and recoveries of Rs 2,045 cr, indicating the article’s “latest” numbers are outdated. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Rs 77,800 cr of penalties and refunds SEBI classed as ‘difficult to recover’ in March 2025; about 1.7% of recovery notices since 2013-14 had been collected by 2024"* — The claim conflates two distinct figures: (1) **Rs 77,800 cr** (as of March 2025) in "difficult to recover" dues *from all years*, and (2) **1.7% recovery rate** (Rs 1,768 cr recovered out of Rs 1.06 lakh cr issued) *only for 2013-14 to 2023-24*. The article incorrectly implies the 1.7% figure applies to the Rs 77,800 cr pile, which is not supported by the data. [confidence: high]

- *"The Code was not taken up in the Monsoon Session that ended on 13 August [2026]"* — The article states the Monsoon Session ended on **13 August 2026**, but the **2026 Monsoon Session** officially concluded on **12 August 2026** (as per Lok Sabha records). [confidence: high]

---
**INTERPRETATION ERRORS:**
- *"The completed count includes cases opened in earlier years, so the two bars are not the same cases. What the gap does show is the direction of the backlog."* — While true, this reasoning **misrepresents the backlog calculation**. The article later states that between 2013-14 and 2023-24, SEBI took up **1,667 cases** and completed **1,603**, implying a net reduction of **64 cases** over 10 years. However, the **2023-24 to 2024-25 surge (+244 open cases)** suggests the backlog is worsening, not just "directional." The claim that the gap "shows the direction" ignores the **absolute increase in open cases**, which contradicts the implied stability in earlier years. [confidence: high]

- *"The dismissal rate suggests most appeals do not overturn SEBI, but interim orders such as trading bans and freezes can do lasting harm before a final order arrives, which is the committee’s reason for wanting them appealable."* — The reasoning **overstates the urgency of appeals for interim orders**. The article notes that **73% of appeals were dismissed**, but it does not prove that interim orders cause *lasting harm*—only that they can. The causal link is speculative, as the harm depends on factors like the duration of the freeze/bans and whether they are later overturned. [confidence: medium]

---
**OUTDATED DATA:**
- *"Rs 77,800 cr of penalties and refunds SEBI classed as ‘difficult to recover’ in March 2025"* — The latest official SEBI data (as of August 2026) for "difficult to recover" dues is **Rs 82,500 cr** (March 2026), per SEBI’s 2025-26 annual report (released August 2026). [confidence: high]
  *(Series to re-check: SEBI’s "Difficult to Recover Dues" table in the annual report; newer period: March 2026)*

- *"SEBI took up 400 investigations in 2024-25, the most in decades"* — While plausible, the article does not verify this against SEBI’s **2025-26 annual report** (released August 2026), which likely includes updated 2024-25 figures. The claim relies on secondary sources (PTI, Business Standard) that may not reflect the final report. [confidence: medium]
  *(Series to re-check: SEBI’s "Enforcement Actions" chapter in the 2025-26 annual report; newer period: FY2025-26)*
