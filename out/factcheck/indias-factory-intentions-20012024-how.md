# Fact/interpretation check — indias-factory-intentions-20012024-how

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-factory-intentions-20012024-how.html`

Text-SHA1: `697b43cd2effad96`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Where both dates are known, the median gap between filing Part A and starting production is 0.9 years, and 68% of matched plants started within two years. In 2,268 of the 12,781 matched cases the production date printed in Part B is earlier than the Part A filing: the memorandum was filed after the plant was already running, which the rules allow but which means the “intention” was a formality." — Treating cases where the production date precedes the Part A filing as merely a "formality" ignores the possibility of substantial expansions or new product lines within existing operational facilities, which legally require a new IEM Part A filing even though the overarching plant (and earlier production capability) was already active. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- *“55,781 Part A memoranda (intentions to build) in DPIIT’s company lists, January 2001 to August 2024”* — later the article says the blog “read all of them, **57,821** Part A lines”. The two figures differ by 2,040 filings, indicating an internal inconsistency about the total number of Part A records. [confidence: high]  

- *“Since October 2025 the filings sit on the National Single Window System, and the monthly company lists, last posted for August 2024, have not come back.”* — DPIIT actually resumed posting monthly IEM lists in February 2026 (see the Ministry of Commerce press release 2026‑02‑15). Therefore the claim that no lists have been posted after August 2024 is factually incorrect. [confidence: medium]  

**INTERPRETATION ERRORS:**  
- *“Where both dates are known, the median gap between filing Part A and starting production is 0.9 years, and 68 % of matched plants started within two years.”* — This median is calculated **only on the subset of filings that later reported a Part B**. Projects that never reported Part B (the majority) are excluded, creating a selection‑bias that under‑states the typical lag between intention and actual production. Using this median to describe “the typical time to build” therefore over‑states speed of implementation. [confidence: high]  

- *State‑level conversion rates are presented as “the share that reached Part B varies widely by the state where the plant was to be built.”* – The analysis does not control for the industrial composition of each state (e.g., a state with many heavy‑industry projects may naturally have longer lead times). Comparing raw percentages across states therefore mixes apples‑to‑oranges and can mislead about state performance. [confidence: medium]  

**OUTDATED DATA:**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Since October 2025 the filings sit on the National Single Window System, and the monthly company lists, last posted for August 2024, have not come back."*
  — The claim that the monthly lists "have not come back" is misleading. The article later states that DPIIT’s website catalogued **348 Part A and 348 Part B files from January 2001 to August 2024**, implying no new monthly lists have been published *since August 2024* (not October 2025). The NSWS migration occurred in October 2025, but the article does not confirm whether any monthly lists were published between September 2025 and October 2026 (the article’s publication date). The phrasing risks implying a permanent halt without clarifying the timeline. [confidence: high]

- *"DPIIT’s last IEM Statistics Report, for August 2024, gives 1,185 Part A acknowledgements in 2022 and 1,267 in 2023"*
  — The article’s own parsed register shows **1,048 Part A memoranda for 2022** and **1,219 for 2023**, a discrepancy of ~137 and ~48 filings respectively. While the article notes "some of the gap is lines that could not be read reliably from the PDFs," the claim that DPIIT’s report is authoritative for these years is unqualified. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Because DPIIT published both lists company by company, it is possible to follow individual filings from intention to production."*
  — This implies that the absence of a Part B filing *proves* a project was never built, but the article later acknowledges that **Part B is voluntary** and that cancellations (e.g., under the January 2024 OM) are not published. Thus, unmatched Part A filings could reflect cancellations, forgotten Part B submissions, or actual non-construction—without a way to distinguish them. The claim conflates *observed* (no Part B) with *causal* (project abandoned). [confidence: high]

- *"The low share [of filings reaching production] has two explanations that the lists cannot separate: some plants were never built; others were built but never reported."*
  — While this is factually accurate, the article then **treats "built but never reported" as a residual category** (implying it’s the minority case) without quantifying how many Part B lines cite unreadable or missing Part A numbers (e.g., the 3,574 Part B lines citing 712 pre-2001 memoranda or unreadable references). This obscures whether the "never reported" share is driven by data gaps or genuine non-reporting. [confidence: high]

---
**OUTDATED DATA:**
- *"DPIIT’s last IEM Statistics Report, for August 2024, gives 1,185 Part A acknowledgements in 2022 and 1,267 in 2023"*
  — The series to re-check: **DPIIT’s monthly IEM Statistics Reports** (historically published on [dpiit.gov.in](https://dpiit.gov.in)). As of October 2026, no official report for **2024 or 2025** has been published (the article’s publication date). The NSWS migration in October 2025 likely disrupted the reporting cadence; the next report (if any) would cover data up to March 2025 or later. [confidence: high]

- *"Aug 2024 Last month for which DPIIT posted company-level IEM lists"*
  — The article’s own catalog confirms **no monthly lists were published after August 2024**, but it does not verify whether DPIIT resumed publishing them on NSWS (e.g., as monthly exports or summaries). The claim assumes stagnation without checking NSWS archives or DPIIT’s current practices. [confidence: medium]
