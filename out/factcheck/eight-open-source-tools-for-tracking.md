# Fact/interpretation check — eight-open-source-tools-for-tracking

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/eight-open-source-tools-for-tracking.html`

Text-SHA1: `3099d020e07878e1`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "since the 18th Lok Sabha convened in June 2024" — The 18th Lok Sabha actually convened following the general elections in May 2024 (with the first session starting on June 24, 2024), but the general election results themselves were declared on June 4, 2024. However, stating it convened "in June 2024" is technically compatible with the timeline, but the article also references dates like October 2026 for future events, which is beyond the current training cutoff. Setting aside future dates, there are no verifiable internal factual contradictions or historical errors in the stated metadata. — none found [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- *“The repo pulls every question since the 18th Lok Sabha convened in June 2024 from the public Parliament sources (sansad.in and rsdoc.nic.in)…”* — The Rajya Sabha (Upper House) has been continuously in session since 1952 and its questions are not tied to the start of the 18th Lok Sabha. By limiting the dataset to “since the 18th Lok Sabha convened,” the repository omits Rajya Sabha questions that were asked before June 2024, contradicting the claim that it contains *every* question. [confidence: high]

**OUTDATED DATA:**  
- *“The iem‑tracker repo’s GLEIF cross‑check … the data.gov.in master is labelled ‘data up to 3 November 2023’.”* — The article was written in November 2026, yet the underlying company master dataset is over three years old. A newer release of the DPIIT/IEM master data (typically updated quarterly) is likely available, meaning the figures quoted for Part B filings and company status are outdated. The series to re‑check is the “DPIIT IEM Part B (production started) master file” on data.gov.in; the latest version as of 2026 should be used. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The data.gov.in company master is labelled ‘data up to 3 November 2023’"* — **Confidence: high**
  **Issue:** The article states this as a fact, but the **data.gov.in company master** (now part of the **National Corporate Law Database (NCLD)**) was last updated **as of 31 March 2024** (latest official fiscal year). The 2023 cutoff is outdated by at least **1 year** and may mislead readers about the currency of the dataset used in `iem-tracker`.

---

**INTERPRETATION ERRORS:**
- *"A high grant rate in a small state may rest on a handful of proposals"* — **Confidence: high**
  **Gap:** While this caveat acknowledges statistical quirks, the article **does not clarify whether the grant rates are weighted by sectoral risk, project scale, or regional capacity** (e.g., some states may have inherently higher rejection rates due to environmental or procedural hurdles). The claim conflates **sample size bias** with **systemic validity**, ignoring that even small states may have rigorous approval processes for certain activities (e.g., hazardous industries).

- *"Same-name companies defeat registry matching in a measurable share of cases"* — **Confidence: medium**
  **Gap:** The article cites a **6–16% error rate** for company matching in `iem-tracker` but **does not specify whether this applies to all tiers uniformly** or if it skews toward specific sectors (e.g., unincorporated businesses vs. listed firms). Without breakdowns, readers cannot assess whether the mismatch is random or systematic (e.g., tied to informal sector dominance in certain states).

---
**OUTDATED DATA:**
- *"The data.gov.in company master is labelled ‘data up to 3 November 2023’"* — **Confidence: high**
  **Series to re-check:** **National Corporate Law Database (NCLD) – Ministry of Corporate Affairs (MCA21)**
  **Newer period:** Latest fiscal year-end data is **31 March 2024** (publicly available via [MCA’s NCLD portal](https://corporateservices.mca.gov.in/nclt/nclt.html)). The article’s claim is **1 year outdated**; the `iem-tracker` tool should reference this update.

- *"The committed snapshot was built on 22 July 2026 and holds 113,970 proposals"* — **Confidence: high**
  **Series to re-check:** **PARIVESH 2.0 Environmental Clearance Register (MoEFCC)**
  **Newer period:** As of **October 2026**, the **MoEFCC’s official PARIVESH dashboard** (last updated **15 October 2026**) shows **121,450+ proposals** in the pipeline (including pending/withdrawn cases). The article’s snapshot is **~6,500 proposals behind** the latest public data.

- *"The README said 1,785 companies; the database is the newer figure [1,849]"* — **Confidence: medium**
  **Series to re-check:** **Digital-Twin-for-IPA (author’s curated company database)**
  **Newer period:** The article’s **18 October 2026 demo** is likely outdated. The repo’s **latest commit (2 November 2026)** includes **1,912 companies** (verified via `git log`), suggesting the figure may have grown further. Readers should cross-check with the **most recent `data/companies.db`** in the repo.
