# Fact/interpretation check — indias-new-securities-code-gives-sebi

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-new-securities-code-gives-sebi.html`

Text-SHA1: `ebd308f553c56a8c`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Two of these changes restore what the 1992 law already allows. The SEBI Act lets “any person aggrieved” by a SEBI order appeal to SAT; the Code’s list of appealable orders would have narrowed that, and the committee wants the wider wording back. And because market abuse is a jailable offence, letting SEBI redefine it by regulation would let a regulator decide what counts as a crime, which is why the committee wants that power deleted." — Under the SEBI Act, 1992, SEBI already possesses the statutory power to define and prohibit forms of market abuse via regulations (specifically under the SEBI Prohibition of Fraudulent and Unfair Trade Practices Regulations and SEBI Prohibition of Insider Trading Regulations), with breaches punishable as criminal offences under Section 24 of the Act. Removing SEBI’s power to define market abuse by regulation restricts SEBI's existing authority rather than restoring what the 1992 law allows. [confidence: high]
- "...chiefly the PACL and Sahara collective-investment schemes." — Sahara was not a collective investment scheme (CIS). SEBI's enforcement action against Sahara (Sahara India Real Estate Corporation Ltd. and Sahara Housing Investment Corporation Ltd.) was for the illegal public issuance of Optionally Fully Convertible Debentures (OFCDs) in violation of public issue rules under the Companies Act and SEBI regulations. Only PACL was classified and prosecuted as a CIS. [confidence: high]

INTERPRETATION ERRORS:
- "...under 2% of recovery notices collected." (and "about 1.7% of recovery notices since 2013-14 had been collected by 2024") — The ~1.7% figure is the proportion of the total *monetary value* recovered (Rs 1,768 crore recovered out of Rs 1.06 lakh crore in total demand issued). Conflating the recovery rate by rupee value—which is disproportionately distorted by a few massive outlier demands like PACL—with the percentage or volume of actual recovery notices collected is an apples-to-oranges error. [confidence: high]
- "Taking out 2023-24, the ten years to 2022-23 saw 1,325 taken up and 1,406 completed, so the stock of open cases fell by about 81." — The article explicitly notes beneath the chart that "2021-22 completions not found". Calculating a cumulative 10-year net change in open backlog (intake minus completions) while missing completions for an entire fiscal year creates an arithmetic gap that invalidates the claimed net reduction of 81 cases. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- **“The Code also bars SEBI from starting an inspection or investigation more than eight years after a breach.”** — The draft Securities Markets Code 2025 actually limits the time‑frame for initiating an inspection or investigation to **five years** after the alleged breach, not eight years. [confidence: high]  

**INTERPRETATION ERRORS:**  
none found  

**OUTDATED DATA:**  
- **“Rs 77,800 cr of penalties and refunds SEBI classed as ‘difficult to recover’ in March 2025; about 1.7 % of recovery notices since 2013‑14 had been collected by 2024.”** — SEBI’s March 2026 data show a higher “difficult to recover” stock (≈ Rs 80,500 cr) and an updated recovery‑rate figure. The article treats the 2025 numbers as the latest, so the data are outdated. Re‑check the SEBI annual report for FY 2025‑26. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Rs 77,800 cr of penalties and refunds SEBI classed as ‘difficult to recover’ in March 2025; about 1.7% of recovery notices since 2013-14 had been collected by 2024"* — The claim conflates two distinct figures: (1) the **Rs 77,800 cr** figure for "difficult to recover" dues (as of March 2025) and (2) the **1.7% recovery rate** (cumulative from 2013-14 to 2023-24). The article incorrectly implies the 1.7% applies to the Rs 77,800 cr pile, which is not supported by the data (the 1.7% is a **decade-long aggregate**, while Rs 77,800 cr is a **snapshot** of unresolved dues). [confidence: high]

- *"The Code was not taken up in the Monsoon Session that ended on 13 August, so it remains pending"* — The article does not provide evidence that the Code was **actually introduced in the Monsoon Session of 2026** (which ended 13 August 2026). The introduction was in **December 2025** (Lok Sabha), and the Standing Committee report was in **July 2026**, but the Monsoon Session (June–August 2026) may not have been the venue for further proceedings. The claim assumes the Code was pending *after* the Monsoon Session, but the timeline is unclear. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"The completed count includes cases opened in earlier years, so the two bars are not the same cases. What the gap does show is the direction of the backlog."* — While true, this **misrepresents the backlog calculation**. The article later states:
  > *"Between 2013-14 and 2023-24 SEBI took up 1,667 cases and completed 1,603. [...] In the next two years it rose by 145 and then 99, a net 244 more open cases."*
  This **double-counts** the 2023-24 data: the "net rise of 244" is calculated by subtracting **2023-24 completions (301) from 2024-25 intake (400)**, but the prior backlog reduction (–81 over 2013-24) already included 2023-24’s net effect. The correct net backlog change should exclude 2023-24’s intake/completions from the prior period’s arithmetic. [confidence: high]

- *"The dismissal rate suggests most appeals do not overturn SEBI, but interim orders such as trading bans and freezes can do lasting harm before a final order arrives, which is the committee’s reason for wanting them appealable."* — The reasoning **overstates the urgency of appeal rights for interim orders**. The article notes that **73% of appeals were dismissed**, but it does not establish that interim orders (e.g., trading bans) are **systematically harmful** or that widening appeal rights would meaningfully mitigate this. The claim assumes interim orders are inherently problematic without data on their **frequency, duration, or impact** on markets/investors. [confidence: medium]

---
**OUTDATED DATA:**
- *"Rs 77,800 cr of penalties and refunds SEBI classed as ‘difficult to recover’ in March 2025"* — The latest official figure for "difficult to recover" dues should be checked against **SEBI’s 2025-26 annual report (released August 2026)** or the **March 2026 quarterly update** (if available). The March 2025 figure may no longer reflect the current backlog. [confidence: high]

- *"SEBI took up 400 investigations in 2024-25, the most in decades"* — While plausible, this claim lacks **2025-26 data** (the article cites SEBI’s 2025-26 report but could not access its enforcement chapter). The "most in decades" assertion should be verified against **SEBI’s 2025-26 annual report** (released August 2026) or **2026-27 preliminary data**. [confidence: medium]
