# Fact/interpretation check — how-to-use-global-ticker-universe-look

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-global-ticker-universe-look.html`

Text-SHA1: `18eb86b18f95b0c3`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- “US United States NYSE/NASDAQ/AMEX 7,726” — The United States exchange universe contains far more than 7,726 active ticker symbols (NASDAQ alone lists >3,300 tickers, NYSE >2,800, and AMEX adds several hundred; combined, the count exceeds 10,000). The figure cited is therefore understated and does not match publicly available exchange listings. [confidence: high]  

- “DE Germany Xetra + Frankfurt 17,121” — The total number of securities listed on Germany’s Xetra and Frankfurt exchanges is roughly 13,000–14,000, not 17,121. The count in the article appears inflated relative to official exchange statistics. [confidence: high]  

**INTERPRETATION ERRORS:**  
- “Exchange‑qualified symbols resolve to exactly one market.” — This statement is contradicted elsewhere in the article, which notes that Indian companies appear twice (once on NSE and once on BSE) and that cross‑listed securities exist in other jurisdictions. Therefore the claim that each Yahoo‑style symbol maps uniquely to a single market is inaccurate; the data actually contain duplicate symbols across markets, so the conclusion of one‑to‑one mapping is unsupported. [confidence: medium]  

**OUTDATED DATA:**  
- none found

## Mistral open-mistral-nemo

Here is the structured feedback based on the provided article text:

---

**FACTUAL ERRORS:**
- **"74,239 tickers in the committed universe file"** — The article states this as the current count (October 2026), but the README explicitly notes the *validated flat file* (July 2026) contains **60,971 symbols**, while the *JSON universe* (the actual committed file) has **74,239 symbols**. The article conflates these two inconsistent snapshots, making the claim misleading. [confidence: high]

**INTERPRETATION ERRORS:**
- **"The helper loaded 74,239 symbols across 34 markets in well under a second, all unique"** — While the JSON file *claims* 74,239 unique symbols, the article does not verify whether this count excludes duplicates *across markets* (e.g., companies listed on multiple exchanges, like Reliance appearing as `RELIANCE.NS` and `RELIANCE.BO`). The "0 duplicate symbols" claim only checks for *symbol string* duplicates (e.g., `7203.T` appearing twice), not *company-level* duplicates. [confidence: high]

- **"India comes as RELIANCE.NS or .BO, so some companies appear twice"** — This is factually correct, but the article *later* warns that the dataset is a "snapshot" and "some markets are only partly covered," implying incompleteness. However, it then uses this partiality (e.g., "China is flagged as a coverage gap") to *support* the tool’s utility for research—ignoring that the same logic applies to India’s double-listed stocks, which could skew analyses (e.g., overcounting Reliance’s market cap). [confidence: medium]

**OUTDATED DATA:**
- **"The validated flat file is as of July 2026"** — The article cites this as current, but the *README* (also dated October 2026) mentions a later update (widening to 75,815 symbols with Taiwan/Singapore merges). The JSON file in the repo (committed Oct 2026) reflects this update (74,239 symbols), so the article’s July 2026 claim is outdated. Re-check: [GitHub repo’s `data/global_universe.json` metadata; newer period: October 2026]. [confidence: high]

- **"US symbols are bare (e.g., 'A', 'AA'); the exchange (NYSE, NASDAQ, AMEX) is not in the symbol"** — While true for the *current* dataset, the article does not note that this format change (removing exchange suffixes) was introduced in the *July 2026* flat file. The JSON file (Oct 2026) may have reverted or adjusted this, but the article treats it as a static fact without clarifying the temporal context. [confidence: medium]

---
**Note:** The article’s disclaimers (e.g., "snapshot," "partly covered") are correct but *underutilized* to contextualize claims about completeness or uniqueness. The core issue is *transparency* about evolving data states.
