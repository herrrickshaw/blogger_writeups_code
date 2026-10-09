# Fact/interpretation check — indias-factory-intentions-20012024-how_0101046393

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-factory-intentions-20012024-how_0101046393.html`

Text-SHA1: `697b43cd2effad96`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Of the 48,485 memoranda filed from 2001 to 2018, 7,078 (15%) are cited by number in a later Part B list. Another 4,097 have no Part B citing them, but the same company filed a Part B after the filing date; counting those as well gives 23%, an upper estimate, because a company with several projects can report one and not another." — Matching a Part B filing to a different Part A filing simply because they belong to the same company assumes that a company's subsequent production report corresponds to the specific earlier intent memorandum in question. A multi-project firm filing a new Part B could be reporting on an entirely different unlisted or newer facility rather than the specific 2001–2018 filing being evaluated, making the name-only match an unreliable indicator of completion for that specific intent. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“55,781 Part A memoranda (intentions to build) in DPIIT’s company lists, January 2001 to August 2024”** – later the article says the blog “read all of them, **57,821** Part A lines”. The two totals for the same period are inconsistent, indicating a factual mistake in the reported count. [confidence: high]

**INTERPRETATION ERRORS**
- **“The low share has two explanations… Some plants were never built… Others were built but never reported… The share of Part A filings that reach a Part B list therefore shows how many intended plants actually become operational.”**  
  The article treats the 15 % (or 23 % with name‑only matches) conversion rate as evidence of the proportion of intended factories that are built, even though Part B filing is voluntary and many companies may have started production without submitting the required Part B. This creates a false causal link: a low Part B match rate does **not** reliably measure the true build‑out rate. [confidence: high]

**OUTDATED DATA**
- **“the monthly company lists, last posted for August 2024, have not come back.”** – The article was published on 7 Oct 2026. DPIIT’s portal may have released lists after August 2024 (e.g., for 2025‑2026) that the author has not incorporated. The relevant series to re‑check is the **DPIIT monthly IEM “List of IEM Filed” and “List of IEM Implemented”** on the DPIIT website for the period **Sept 2024 – Oct 2026**. [confidence: medium]  

- **“DPIIT’s last IEM Statistics Report, for August 2024, gives 1,185 Part A acknowledgements in 2022 and 1,267 in 2023…”** – As of the article date, newer DPIIT IEM Statistics Reports (e.g., for 2024, 2025) are likely available. The series to verify is **DPIIT IEM Statistics Report** for **2024‑2025**. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Since October 2025 the filings sit on the National Single Window System, and the monthly company lists, last posted for August 2024, have not come back."*
  — The claim that the monthly lists "have not come back" is misleading. The article later states that DPIIT’s website catalogued **348 Part A and 348 Part B files from January 2001 to August 2024**, with **nothing newer** in the library as of 7 October 2026. This implies no new monthly lists have been published post-August 2024, but the phrasing "have not come back" could imply a temporary hiatus rather than permanent cessation. The article’s own data confirms the absence of post-August 2024 lists, but the wording risks overstating the certainty of non-publication. [confidence: high]

- *"DPIIT raised them [IEM thresholds] to match the Ministry of MSME’s notification S.O. 1364(E) of 21 March 2025"*
  — The article cites **Press Note 1 (2025 Series), 1 April 2025**, as the source for the threshold hike, but the MSME notification (S.O. 1364(E)) was issued **21 March 2025**. While the timing aligns, the phrasing suggests the DPIIT change was *directly* tied to the MSME notification’s wording or timing, which may not be explicitly stated in the DPIIT’s Press Note. The article does not clarify whether DPIIT’s thresholds were *identical* to MSME’s or merely aligned in spirit. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"Because DPIIT published both lists company by company, it is possible to follow individual filings from intention to production."*
  — This claim conflates **public availability** with **completeness**. The article later notes that **3,574 Part B lines cite Part A memoranda not in the register** (due to unreadable numbers, missing PDFs, or pre-2001 filings), and that **712 Part B lines reference memoranda filed before 2001**—a period not covered in the 2001–2018 analysis. Thus, while the methodology *could* track filings, it **fails to account for a significant portion of Part B data** due to data gaps, rendering the "complete follow-up" claim overstated. [confidence: high]

- *"The low share [of filings reaching production] has two explanations that the lists cannot separate: some plants were never built; others were built but never reported."*
  — The reasoning gap lies in **ignoring a third possibility**: some plants *were built but never filed a Part B* due to **voluntary non-compliance** (e.g., companies skipping the reporting step) or **systemic failures** (e.g., DPIIT not enforcing Part B filings). The article treats "never reported" as synonymous with "built but not reported," but it does not explore whether the *lack of reporting* reflects **intentional non-compliance** (e.g., companies avoiding regulatory scrutiny) or **administrative inertia** (e.g., DPIIT not tracking or publishing Part B filings reliably). The causal attribution is thus **underdetermined**. [confidence: high]

---
**OUTDATED DATA:**
- *"DPIIT’s last IEM Statistics Report, for August 2024, gives 1,185 Part A acknowledgements in 2022 and 1,267 in 2023, and 916 and 968 Part B acknowledgements."*
  — The article’s own **parsed register** (from monthly PDFs) shows **1,048 Part A and 755 Part B for 2022** and **1,219 Part A and 846 Part B for 2023**, with the note that *"some of the gap is lines that could not be read reliably from the PDFs."* Given the **October 2025 migration to NSWS**, a **new official report for 2024–2026** (if published) would likely supersede these figures. The claim is correct for August 2024 but risks being outdated by the time of publication (7 October 2026). [confidence: high]
  — **Series to re-check**: DPIIT’s *IEM Statistics Report* (quarterly/annual); newer period: **2024–2026** (if available).

- *"The register built from the monthly lists has 57,821 Part A lines and 14,091 Part B lines."*
  — The article’s **total for 2001–August 2024** (55,781 Part A) is later refined to **57,821** in the table breakdown (2001–2024). However, the **NSWS system (post-October 2025)** likely contains **additional filings** not captured in the PDF-based register. The claim is accurate for the parsed data but does not account for post-2024 filings. [confidence: medium]
  — **Series to re-check**: NSWS IEM database (no direct public API, but DPIIT’s *IEM Statistics Report* or NSWS export may include totals).
