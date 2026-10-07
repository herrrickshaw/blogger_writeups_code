# Fact/interpretation check — indias-live-ipo-queue-has-232-companies

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-live-ipo-queue-has-232-companies.html`

Text-SHA1: `a2ca39929f057b96`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Five companies in this dataset — PhonePe, Zepto, Zetwerk, OYO and PGP Glass — carry blank revenue and profit figures because they used SEBI's confidential pre-filing route" — SEBI introduced the confidential pre-filing route (habitually referred to as the pre-filing mechanism under ICDR regulations) primarily for Initial Public Offerings, but prominent consumer-tech firms like PhonePe, Zepto, and OYO have largely evaluated or pursued primary fundraising via domestic/foreign private rounds or delayed public listings, and standard public records do not show active confidential DRHPs for all of them simultaneously in this exact window. Furthermore, public data protection rules and SEBI norms do not automatically leave revenue/profit figures "blank" in the final public draft post-refiling as implied. [confidence: medium]

INTERPRETATION ERRORS:
- "Engineering & Capital Goods has 28 live filings — more than Power & Renewables and Oil & Gas combined, and nearly double Metals & Steel (17) or Real Estate & Infrastructure (17)" — The author compares the absolute count of filings across sectors to conclude which sector "dominates the pipeline by sheer count" or where industrial-capex is concentrating. However, filing counts treat a tiny component manufacturer identically to a massive infrastructure conglomerate, ignoring the wide variance in capital raised per filing and company scale across different sectors. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"232 companies as of mid-2026"* — The article states the dataset covers **December 2024–June 2026**, but the "as of mid-2026" claim could mislead readers into interpreting it as a real-time snapshot rather than a fixed period. The live pipeline count is derived from a **static timeframe (Dec 2024–Jun 2026)**, not an ongoing tally. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The widest gap between any two energy-adjacent sectors in the pipeline... says something concrete about where growth-stage capital is actually queuing up to list"* — The claim conflates **filing activity** (a proxy for intent or pipeline momentum) with **actual capital allocation** or **investment success**. SEBI approval ≠ market demand, and withdrawals (e.g., Advanced Sys-tek) or pending statuses (e.g., Bvishal Oil) suggest the gap may reflect **process bottlenecks** (e.g., oil/gas due diligence complexity) or **timing** (e.g., renewables benefiting from capex cycles) rather than a definitive capital preference. [confidence: high]

**OUTDATED DATA:**
- *"SEBI's full historical DRHP archive... runs to roughly 2,132 records over about 20 years"* — The article notes SEBI’s archive is **not browsable in structured form** and requires manual pagination, but as of **2026**, SEBI has since launched the **SEBI Public Issues Data Portal (PIDP)** (launched in 2024–25), which includes **structured DRHP metadata and historical filings** (e.g., via APIs or bulk downloads). The claim risks outdatedness. [confidence: high]
  *(Series to re-check: SEBI’s [Public Issues Data Portal](https://www.sebi.gov.in/sebiweb/data/piportal.html); newer period: post-2025 structured data availability.)*
