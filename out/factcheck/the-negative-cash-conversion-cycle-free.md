# Fact/interpretation check — the-negative-cash-conversion-cycle-free

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-negative-cash-conversion-cycle-free.html`

Text-SHA1: `d8692fbe0668e811`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Financial years end between September 2025 and August 2026." and "financial years ending Sep 2025 to Aug 2026" — The publication date of the article is October 28, 2026, meaning corporate financial statements for full annual periods ending in mid-to-late 2026 (such as June, July, or August 2026) would not yet be publicly filed or available for companies like Apple, Amazon, or Hindustan Unilever. [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 2044, Requested 5984. Please try again in 210ms. Need more tokens? Upgrade to Dev Tier today at https://conso]

## Mistral open-mistral-nemo

Here is the structured feedback based on the provided article:

---

**FACTUAL ERRORS:**
- **"Carillion’s standard supplier terms before it collapsed in 2018 [were] 120 days"** — The article states this as a fact, but the **House of Commons report (May 2018)** explicitly describes Carillion’s *standard* payment terms as **"an extraordinary 120 days"** *after* its collapse (January 2018). The phrasing here conflates the *cause* (supplier terms used to finance operations) with the *timing* of the terms’ existence. While the 120-day figure itself may be accurate for Carillion’s pre-collapse practices, the article’s wording risks implying the terms were standard *before* the collapse (when they were likely already in place but exploited more aggressively). [confidence: high]

- **"The rules [on supplier finance disclosures] apply to annual periods beginning on or after 1 January 2024"** — The **IASB amendments to IAS 7/IFRS 7** were issued in **May 2023**, but the effective date for mandatory adoption is **annual periods beginning on or after 1 January 2024**. The article correctly states the effective date but could clarify that the *issuance* occurred earlier (May 2023), which might mislead readers into thinking the rules were retroactive. [confidence: medium]

---
**INTERPRETATION ERRORS:**
- **"A negative cash conversion cycle is good only if it comes from something the company can sustain"** — While this is a sound *conclusion*, the article later **overgeneralizes the "sustainability" test** by conflating two distinct mechanisms:
  1. **Healthy negative cycles** (e.g., Apple’s 115-day payables due to bargaining power).
  2. **Unsustainable negative cycles** (e.g., Carillion’s 120-day terms used to mask cash shortages).
  The article does not consistently apply the **supplier health check** (e.g., tracking payables growth vs. sales growth or supplier finance disclosures) as a *necessary* part of the "sustainability" analysis. For example, Hindustan Unilever’s −65 days are framed as "scale-based," but the article does not flag that **India’s supplier finance regulations (e.g., reverse factoring) might apply**, which could reveal whether the 137-day payables are truly "bargaining power" or a financing tool. [confidence: high]

- **"The negative cycles come from different places"** (e.g., Apple’s low inventory vs. Amazon’s receivable days) — The article **double-counts the role of deferred revenue/contract liabilities** in cases like Larsen & Toubro and Amazon. For Amazon, the article notes that **"a large share of its revenue comes from business customers... who are billed on account"**, but it does not adjust the CCC calculation to account for **deferred revenue** (which could make Amazon’s true cycle even more negative). This omits a key **hidden float** that the article later warns readers to look for. [confidence: high]

---
**OUTDATED DATA:**
- **"Financial years ending Sep 2025 to Aug 2026"** — The article was **revised on 28 October 2026** and explicitly states it uses data from Yahoo Finance for FYs ending in this range. However:
  - For **Indian companies**, the latest available FY2026–27 annual reports (as of October 2026) would likely have been filed by **June–July 2027** (with some delays). The article’s data is **not yet final** for the period it claims to cover.
  - **Hindustan Unilever’s 137-day payables** and **Apple’s 115-day payables** may have changed in **FY2026–27** (e.g., due to new supplier finance disclosures or IFRS 16 lease adjustments). The article does not cross-check with the companies’ **latest filings** (e.g., via [BSE/NSE](https://www.bseindia.com/) for Indian firms or [SEC Edgar](https://www.sec.gov/edgar/searchedgar/companysearch.html) for Apple).
  - **Screener.in filters** (e.g., "Sales growth 5Years > 10") assume **5-year trailing data ending in FY2026–27**, but the article’s own data cutoff (Aug 2026) may not yet include the full 5-year window for all companies. [confidence: high]

- **"The US supplier finance rule (FASB Accounting Standards Update 2022-04)"** — The article cites this rule but does not specify whether it applies to **FY2026 data** (ending Aug 2026). FASB’s **ASU 2022-04** (issued in **March 2022**) became effective for **annual periods beginning after December 15, 2022**, meaning **FY2023+** for most US companies. The article’s reference to "current" rules may mislead readers into thinking the 2024 IFRS changes are the only relevant standard, when US companies would also need to comply with ASU 2022-04 for their latest filings. [confidence: medium]

---
