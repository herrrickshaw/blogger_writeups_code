# Fact/interpretation check — indias-reported-central-project-overrun

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-reported-central-project-overrun.html`

Text-SHA1: `2a5b8efc0714db14`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "After MoSPI moved to its PAIMANA monitoring portal in September 2025, the reports present projects as “ongoing” with their physical and financial progress. The Wire and ThePrint both observed that the word “delay” stopped appearing in the monthly reports after May 2025." — The article contradicts itself on the date of the PAIMANA transition (the Sources section cites "PAIMANA portal release (25 March 2026, PIB 2244898)"). Furthermore, moving to the portal in September 2025 is chronologically impossible as a cause for a reporting change that allegedly occurred months earlier, after May 2025. [confidence: high]

INTERPRETATION ERRORS:
- "43 of 44 Projects that left the set between July and August were Railways projects" — This confuses net change with gross exits. While the net count of all monitored projects fell by 44 (from 1,775 to 1,731), other sectors added projects over the same month (Power increased by 4 from 98 to 102, and Petroleum increased by 14 from 103 to 117). Because at least 18 new projects entered the dataset, the gross number of exiting projects was at least 62, not 44. Railways' net reduction of 43 projects cannot be claimed as 43 out of 44 exits. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- “Read quickly, the central government’s infrastructure overrun halved in four months.” — The article treats the drop from ₹5.65 lakh cr to ₹2.88 lakh cr as evidence of progress, but the underlying project set changed (1,981 → 1,731 projects). Comparing totals from two different samples is an apples‑to‑oranges comparison, so the conclusion that the overrun “halved” is misleading. [confidence: high]  

**OUTDATED DATA:**  
- “The latest, for August 2026, put the cumulative cost overrun at ₹2.88 lakh cr across 1,731 ongoing projects.” — A September 2026 flash report (released 26 September 2026, PIB 2314852) exists, but the article does not incorporate its figures, presenting August as the most recent data. The series to re‑check is MoSPI’s monthly flash report on central sector infrastructure projects (cost ≥ ₹150 cr); the newer September 2026 release should be used. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"43 of 44 Projects that left the set between July and August were Railways projects"* — The article does not provide a definitive source or methodology for this claim (e.g., whether it’s derived from MoSPI’s PAIMANA portal or press summaries). The data is presented as a fact without cross-verification, and the discrepancy between the 43 projects (July–Aug) and the broader trend (Railways dropping from 260 to 147 over the period) lacks transparency. [confidence: medium]

**INTERPRETATION ERRORS:**
- *"The Ministry of Statistics and Programme Implementation publishes a monthly flash report on central government projects costing ₹150 crore or more. ... The latest, for August 2026, put the cumulative cost overrun at ₹2.88 lakh crore across 1,731 ongoing projects. ... It did not [halve]. The monitored set changed."* — While the article correctly identifies that the reduction in overrun is partly due to projects leaving the monitored set, it conflates this with a *misleading headline implication* that the overrun "halved" as a standalone metric. The overrun *as a share of original cost* (15.2% → 9.4%) is a valid adjustment, but the raw ₹5.65 lakh crore → ₹2.88 lakh crore comparison ignores the fact that the *base set of projects* (and their original costs) has shrunk significantly. This creates an apples-to-oranges comparison where the numerator and denominator are not directly comparable without reconciliation. [confidence: high]

- *"The count that used to be there ... Projects delayed | 780 | 779 | Not stated"* — The article notes that the "delay" metric disappeared from reports post-May 2025 but then later states *"MoSPI has itself noted in earlier reports that agencies do not always report revised costs and dates, so the overrun figures can understate the problem."* This implies that the absence of delay data *might* hide a worsening problem, but the reasoning is circular: the article assumes the data *would* show delays if reported, yet provides no empirical basis (e.g., pre-2025 trends or alternative delay proxies like progress bands) to support this claim. [confidence: medium]

**OUTDATED DATA:**
- *"Cost overrun, ₹ lakh crore (projects monitored) | Jan 2026 · 5.52 | Feb 2026 · 5.66 | Apr 2026 · 5.65 | Jun 2026 · 4.93 (unconfirmed) | Jul 2026 · 3.41 | Aug 2026 · 2.88"* — The June 2026 figure is labeled *"unconfirmed"* due to conflicting press summaries. The article should explicitly note that **no official MoSPI release for June 2026** (or its exact data) has been verified, as the PIB reference (2277758) may not align with the cited ₹4.93 lakh crore figure. [confidence: high]

- *"Original cost, ₹ lakh crore | April 2026 | 37.12 | July 2026 | 33.70 | August 2026 | 30.72"* — While these figures are plausible, the article does not check whether MoSPI’s **PAIMANA portal (launched March 2026)** or the **latest PIB releases (e.g., September 2026’s PIB 2314852)** have superseded these mid-year estimates. The portal’s data could provide a more granular breakdown of project exits/entrants. [confidence: medium]
