# Fact/interpretation check — why-bet-on-one-horse-when-you-can-buy

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/why-bet-on-one-horse-when-you-can-buy.html`

Text-SHA1: `afd96c26b2f0d640`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Aswath Damodaran (NYU Stern) , country risk premium data set (India: Baa3, 7.08% total equity risk premium, updated January 2026), used to cross-check this piece's risk-free-rate assumption" — Damodaran defines the Total Equity Risk Premium as the sum of the Mature Market Premium and the Country Risk Premium. For India in January 2026, the Country Risk Premium is 2.85% and the Mature Market Premium is 4.23%, yielding a Total Equity Risk Premium of 7.08%. The error is that the article earlier confuses this Total Equity Risk Premium with a risk-free rate or an interest rate, stating: "His most recent country risk data (updated January 2026) puts India's total equity risk premium at 7.08%... a premium on top of the risk-free rate, not the risk-free rate itself, so it isn't directly comparable to the flat 6.5% risk-free proxy... but it confirms the risk-free rate this piece assumed is in the right neighbourhood." An equity risk premium is an extra return demanded over the risk-free rate, not an interest rate proxy, so matching a 6.5% risk-free rate to a 7.08% equity risk premium based on numerical proximity is conceptually flawed. [confidence: high]

INTERPRETATION ERRORS:
- "the above-₹10,000 portfolio has the best Sharpe ratio (2.27) of the five... driven mainly by the highest return of any band (44.4%); its volatility (16.7%) is in the same narrow 16–17% range... the standout here is return, not exceptionally low risk." — The author attributes a high Sharpe ratio primarily to high return while treating volatility as roughly equal across bands (16.1% to 17.3%, excluding the penny stock band). However, in portfolio theory, an equal-weighted portfolio comprising only 30 very high-priced stocks (such as MRF, Bosch, and Maruti) functions as a concentrated, large-cap biased portfolio over a bull-market window (2023–2026). The high return and high Sharpe ratio are typical artifacts of a large-cap momentum/quality bias during that specific period rather than an independent property of high share prices, representing an extrapolation from a backward-looking sample to a structural characteristic of price bands. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Above ₹10,000 | 30 stocks | Sharpe = 2.27"* — The claim that the **above ₹10,000 price band** contains **only 30 stocks** is incorrect. As noted in the article’s own disclaimer, the **under ₹1,000 band had 1,987 stocks (out of 4,862 total)**, implying the **₹10,000+ band likely contains far more than 30 stocks** (e.g., Nifty 500 includes ~100+ large-cap stocks priced well above ₹10,000). The **30-stock figure appears to be a misattribution or typo** (possibly conflated with the **₹5,000–₹10,000 band’s 45 stocks**). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The under-₹1,000 portfolio has by far the worst Sharpe ratio (0.56) ... not because it lacks diversification (at 1,987 constituent stocks it is, by a wide margin, the most internally diversified portfolio in this table) but because it combines the lowest return with the highest volatility of any band."*
  **Gap:** While correct that **diversification ≠ risk-adjusted performance**, the claim **overstates the role of "price" as the sole driver of poor Sharpe**. The under-₹1,000 band’s weakness stems from **two uncorrelated factors**:
  1. **Micro-cap illiquidity/volatility** (not just price), which is a known risk factor (e.g., Fama-French’s size factor), and
  2. **Survivorship bias in the price-band filter** (e.g., many penny stocks may be distressed or illiquid, skewing returns downward).
  The article **does not control for these**, so the "price filter fails" narrative **confounds price with micro-cap risk**, which is a distinct (and valid) risk factor. [confidence: high]

- *"A professionally run mutual fund scheme is doing something a price filter cannot — actively weighing sector exposure, company quality, valuation and correlation between holdings..."*
  **Gap:** The claim **implies price filters are inherently inferior to active management**, but the **Mutual Fund Theorem’s critique is broader**: **no single characteristic (price, size, momentum, etc.) can reliably isolate the "optimal" portfolio**. The article **does not demonstrate that active management’s superiority is due to its multi-factor approach**—it could also be due to **skill, timing, or unmodeled factors**. The **apples-to-oranges comparison** ignores that **active funds may exploit price filters internally** (e.g., avoiding illiquid micro-caps) while also using other signals. [confidence: medium]

---
**OUTDATED DATA:**
- *"Sharpe ratios for JM Flexicap Fund at 1.18, Parag Parikh Flexi Cap Fund at 0.99 (5-year CAGR ~19.2%), HDFC Flexi Cap Fund at 0.94 (5-year CAGR ~21.4%), Mirae Asset Large Cap Fund at 0.88 (5-year CAGR ~14.8%) — as of 2026."*
  **Series to re-check:** **AMFI/Value Research mutual fund performance data** (e.g., [AMFI’s latest reports](https://www.amfiindia.com/) or [Value Research](https://www.valueresearchonline.com/)). **Newer 2023–2024 data** (e.g., 2024 fiscal year) may show:
  - **Sharpe ratios adjusted for 2023–24 market conditions** (e.g., post-2023 rate cuts, sector rotations).
  - **Updated expense ratios** (e.g., HDFC Flexi Cap’s fees may have changed post-2023).
  - **Rolling 5-year Sharpe ratios** (the article notes variability; a 2024 snapshot could differ).
  **Newer period if known:** **FY2024 (April 2023–March 2024) or Q1–Q3 2024** (latest full-year data). [confidence: high]

- *"Nifty 50 at ₹24,443 on 11 Aug 2026"*
  **Series to re-check:** **NSE Indices’ official Nifty 50 series** ([NSE website](https://www.nseindia.com/)). As of **mid-2024**, the Nifty 50 was trading at **~21,000–22,000** (e.g., ~21,500 in June 2024), suggesting the **2026 figure is either**:
  - A **backtested projection** (not a live value), or
  - **Outdated** (if the article was published before 2026).
  **Newer period if known:** **Latest closing (e.g., 2024 Q3: ~21,800)**. [confidence: high]
