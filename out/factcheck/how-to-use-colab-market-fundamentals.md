# Fact/interpretation check — how-to-use-colab-market-fundamentals

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-colab-market-fundamentals.html`

Text-SHA1: `aafcba5ee9adc5a0`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“SAP.DE 2025‑12‑31 … revenue 3.680e10 … filed 2026‑03‑31”** – The article presents financial figures for the fiscal year ending 31 Dec 2025 as if they are actual reported numbers. As of the article’s revision date (23 Oct 2026) the 2025‑year results have not been filed; Yahoo Finance (via yfinance) only provides estimates or placeholders for future periods. Presenting them as real, audited figures is factually incorrect. [confidence: high]  
- **“Three large companies, four fiscal years each, 13 columns.”** – The sample output shown later displays only **two** fiscal years per company (2024 and 2025). The statement that the test returned “four fiscal years each” contradicts the displayed data. [confidence: medium]

**INTERPRETATION ERRORS**
- **“It stores one row per company per fiscal year with the fields needed for a Piotroski‑style score, so the output slots straight into a screening notebook.”** – A Piotroski F‑Score requires nine specific signals (e.g., change in ROA, cash‑flow‑to‑assets ratio, change in leverage, change in share issuance). The columns listed (net_income, revenue, cfo, etc.) do **not** include all required variables (such as prior‑year ROA, change in gross margin, or share count changes). Assuming the dataset is sufficient for a Piotroski‑style screen is an over‑reach and misleads readers about the tool’s analytical completeness. [confidence: high]  
- **“The ‘filed’ column is fiscal year end plus 90 days … not the actual filing date, so do not use it for strict point‑in‑time work.”** – While the disclaimer is correct, the article later suggests the data can be used for “point‑in‑time backtests” elsewhere (e.g., in the “Limits and honest caveats” section). This mixed messaging creates a logical inconsistency: it first warns against point‑in‑time use, then implies it is acceptable for backtesting, which is contradictory. [confidence: medium]

**OUTDATED DATA**
- **“Latest two fiscal years, selected columns (EUR)” – figures for FY 2024 and FY 2025** – By the revision date (23 Oct 2026) FY 2026 results for many of the listed companies (e.g., SAP, Siemens) are already available or will be filed shortly. The dataset therefore omits the most recent completed fiscal year, making the “latest” claim outdated. The series to re‑check is the Yahoo Finance annual fundamentals for each ticker; the newer period would be FY 2026 (or FY 2025‑Q4 if quarterly data are used). [confidence: high]  

*No other categories contain additional issues.*

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"32,590 tickers in tickers.csv"** — The article states this as a fact, but the universe count shown in the sample output (cell 1) is **32,590 tickers total**, while the breakdown for **20 markets** sums to **32,590** (e.g., US: 7,441 + IN: 2,368 + others = 32,590). However, the article later claims **"32,590 tickers in tickers.csv"** as a standalone figure, which is technically correct but misleading because the US set is **skipped by default** in the collection loop. The actual usable universe for non-US markets is **25,150 tickers** (32,590 - 7,441). [confidence: high]

- **"The 'filed' date is an assumption (fiscal year end plus 90 days), not the real filing date."** — While the article correctly notes this is an **assumption**, the claim that it is **not the real filing date** is an overstatement. For many companies (especially in regulated markets like Germany or the US), the "filed" date in Yahoo Finance data **often aligns with the actual filing date** (e.g., SEC filings for US companies are typically within 60–90 days of fiscal year-end). The article’s phrasing risks implying the assumption is universally inaccurate, which is not the case. [confidence: high]

---
INTERPRETATION ERRORS:
- **"The notebook already handles Yahoo blocking, retries and checkpoints."** — The reasoning gap is that while the notebook **probes for blocked IPs** and **restarts the runtime** if blocked, it does **not guarantee success at scale**. The article states this as a feature, but the caveat later admits:
  > *"Yahoo blocks many datacentre IPs. ... total runtime and block rate at scale are not measured."*
  This implies the "handling" is **only partial** (IP probing + runtime restart) and **unvalidated for large runs**. The claim overstates the robustness of the solution. [confidence: high]

- **"The data come from Yahoo Finance through yfinance, so they are third-party and unaudited."** — The interpretation error is conflating **third-party sourcing** with **audit quality**. Yahoo Finance data are **not audited** (as the article correctly states), but this does not mean they are **inherently unreliable** for research. Many academic studies use Yahoo Finance for **relative comparisons** (e.g., Piotroski scores) where audit quality is less critical than consistency. The article’s framing risks discouraging legitimate use cases where unaudited data are sufficient. [confidence: medium]

---
OUTDATED DATA:
- **"32,590 tickers, 20 markets"** — The universe count and market breakdown are derived from the **tickers.csv** file in the GitHub repo, which may have been updated since **19 October 2026** (the article’s test date). To verify, check the latest **tickers.csv** on [GitHub](https://github.com/herrrickshaw/colab-market-fundamentals/blob/main/tickers.csv) and compare the market sums. [confidence: high]
  *Newer period if known*: N/A (repo may have been updated post-2026).

- **"Latest two fiscal years, selected columns (EUR) for SAP.DE, SIE.DE"** — The sample data (2024–2025) are **not "latest"** as of **23 October 2026** (article’s revision date). For example:
  - SAP’s **2026 fiscal year-end** (31 Dec 2026) would have been filed by **31 March 2027** (assuming 90-day lag). The article’s "latest" data stop at **2025**, which is outdated by at least **6 months**. Re-check the **yfinance** data for these tickers as of **2026–2027** (or later) to confirm. [confidence: high]
  *Series to re-check*: `yfinance` historical data for `SAP.DE`, `SIE.DE` (and other tickers) via [yfinance docs](https://pypi.org/project/yfinance/).
