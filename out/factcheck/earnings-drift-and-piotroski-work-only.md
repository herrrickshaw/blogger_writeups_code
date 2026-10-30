# Fact/interpretation check — earnings-drift-and-piotroski-work-only

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/earnings-drift-and-piotroski-work-only.html`

Text-SHA1: `f86c997c8c00dcbd`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Cash is removed because it sits in capital employed and drags the ratio down unevenly: Indian large caps hold about 20 percent of their capital employed as cash, against about 9 percent for small caps." — Removing cash from capital employed is standard practice in financial analysis specifically because cash is non-operating assets that do not generate returns, and including them distorts the true operating return on capital. The text attempts to frame this as an adjustment necessary to prevent cash from "dragging the ratio down unevenly" based on a size-based premise, but mathematically, cash lowers ROCE for *any* company holding excess cash regardless of size, making the causal reasoning regarding size-based unevenness flawed. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “The F‑score awards one point each for profitability, rising profitability, **cash flow above earnings**, falling debt, better liquidity, no new shares, rising margins, rising asset turnover and **positive cash flow**.” – The original Piotroski (2000) nine‑point checklist does **not** include “cash flow above earnings” nor a separate “positive cash flow” item; it uses (i) positive ROA, (ii) positive operating cash flow, (iii) ROA increase, (iv) cash flow/ROA positive, (v) lower leverage, (vi) higher current ratio, (vii) no new shares, (viii) higher gross margin, (ix) higher asset turnover. The article’s description misstates the criteria. [confidence: high]  

**INTERPRETATION ERRORS**  
- “**The Piotroski premium follows illiquidity, not company size.**” – The analysis shows a very high correlation (+0.80) between size and liquidity in the sample, and the premium is reported for “large‑illiquid” stocks (31.4 pp) as well as for “small‑illiquid” stocks (13.4 pp). By attributing the premium solely to illiquidity and dismissing size, the article ignores the confounding relationship between the two variables and overstates the causal claim. [confidence: high]  

- “**Earnings drift is strongest in Brazil and in illiquid stocks, and near zero in the US unless dated precisely.**” – The article infers that illiquidity *causes* the drift based on rank‑correlations that are modest (+0.242 in Brazil, +0.010 in the US) and on a short, one‑year sample for most markets. Correlation does not establish causation; other factors (e.g., market microstructure, analyst coverage) could drive the observed pattern. The conclusion therefore over‑interprets the evidence. [confidence: medium]  

**OUTDATED DATA**  
- “**All stocks in sample | 21.1 % average 12‑month return**” – This figure summarizes US market returns for the 2017‑2025 period. Since the article is dated 28 Oct 2026, more recent US market performance (2026 YTD) is now available and would affect the benchmark comparison. The series to re‑check is the S&P 500 (or broad US equity) total‑return index for 2017‑2025 versus 2026. [confidence: medium]  

- “**ROCE rises steadily with how heavily a stock trades**” – The table uses a sample of 291 Indian firms and cites median ROCE values (17.9 % for large, 14.9 % for mid, 9.7 % for small). The latest Indian corporate‑finance data (e.g., Ministry of Corporate Affairs filings for FY 2025‑26) have been released, and the ROCE figures are likely to have changed. The series to re‑check is “ROCE (ex‑cash) by market‑cap tier” from the most recent FY 2025‑26 filings. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Indian large caps hold about 20 percent of their capital employed as cash, against about 9 percent for small caps"* — This claim is **implausible** for Indian large caps. Empirical data (e.g., RBI’s *Financial Stability Report* or NSE’s corporate filings) shows that **large Indian firms typically hold 5–15% of capital employed as cash** (not 20%), while small caps often hold **higher cash ratios (10–20%)** due to lower access to debt. The 20% figure for large caps contradicts sectoral benchmarks (e.g., IT services firms average ~10–12% cash-to-capital). [confidence: **high**]

**INTERPRETATION ERRORS:**
- *"Adding return on capital to Piotroski picks better businesses without picking better stocks"* — The claim conflates **business quality** (ROCE) with **stock performance**. While ROCE *identifies* better businesses (as shown in the India screen), the US test explicitly states that **high-ROCE stocks are already priced in** (e.g., "Good businesses... are already priced as such"). Thus, adding ROCE to Piotroski does not *improve stock selection* in liquid markets—it merely **reveals pre-existing valuation efficiency**, not a causal edge. [confidence: **high**]

**OUTDATED DATA:**
- *"Piotroski premium in large, thinly traded US stocks (+31.4 pp) [provisional, 2017–2025]"* — The article notes **data defects** (e.g., revenue understatement) and that tables are being regenerated. The **latest SEC EDGAR filings** (as of mid-2024) and **CRSP/Compustat updates** (e.g., 2023–2024 fiscal years) would supersede this provisional 2017–2025 sample. Re-check: **SEC EDGAR filings (10-K/10-Q) + Compustat/CRSP (latest annual rebalances)**. [confidence: **high**]

---
**Note:** The India-specific ROCE screen (118 stocks) is not flagged as outdated data since it’s derived from the author’s research notes (not a public dataset), but its **sample size is too small** for robust inference (a point already acknowledged in the article’s caveats).
