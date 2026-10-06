# Fact/interpretation check — 050-is-its-own-category-diving-into

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/050-is-its-own-category-diving-into.html`

Text-SHA1: `3422533a889f189e`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "weekly NSE data, 2 Jan 2023–7 Aug 2026" — August 7, 2026, is a future date relative to the real-world knowledge cutoff, making claims based on completed weekly data up to that exact future date impossible to verify and likely fabricated or prematurely published. [confidence: high]

INTERPRETATION ERRORS:
- "More than half of every stock priced under ₹250 — 2,086 of them, or 43% of the entire under-₹1,000 universe from the previous piece — is actually priced under ₹50." — The text calculates 2,086 out of 3,850 as 54.2% (correctly stated in the table), but the inline text swaps in "43%" by comparing it to a different denominator (the "entire under-₹1,000 universe"), mixing denominators while describing the same subset. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The ₹0–50 band — 2,086 stocks, 54.2% of the under-₹250 universe"* — The claim that **54.2% of the under-₹250 universe** is in the ₹0–50 band contradicts the earlier statement that this band represents **43% of the entire under-₹1,000 universe** (from the first piece). If the under-₹250 universe is **~43% of the under-₹1,000 universe**, then 54.2% of it would be **~23.3% of the full under-₹1,000 universe**, not 43%. This suggests a miscalculation or inconsistent framing. [confidence: high]

- *"Median dividend yield is exactly 0.0% in all four bands"* — While plausible for microcaps, **no dividend yield is not the same as 0.0%**. Many stocks in this range may have **no dividend history recorded**, not necessarily a yield of zero. The phrasing risks implying all stocks *explicitly* yield 0%, which could mislead readers. [confidence: medium]

---
**INTERPRETATION ERRORS:**
- *"Price under roughly ₹250 [...] is doing double duty as a rough proxy for market capitalisation"* — While the data shows a **correlation** between low price and small market cap, this does **not prove causation**. The relationship could be confounded by other factors (e.g., illiquidity, regulatory hurdles, or investor aversion to microcaps), which the article does not explore. The claim risks oversimplifying the mechanism. [confidence: high]

- *"The ₹0–50 band has the worst Sharpe ratio [...] because of the highest volatility (27.2%) and highest beta (1.31) at the same time as the lowest return"* — While volatility and beta contribute to the Sharpe ratio, **this ignores liquidity effects**. Thinly traded stocks may exhibit high volatility *not due to risk but due to lack of trading volume*, which distorts Sharpe ratios. The article does not adjust for liquidity, making the causal link tenuous. [confidence: high]

---
**OUTDATED DATA:**
- *"Beta, portfolio return, volatility and Sharpe ratio for each sub-band — computed from a local historical NSE OHLCV warehouse (adjusted close, year-partitioned parquet, **2 Jan 2023–7 Aug 2026**)"* — The data window ends in **August 2026**, which is likely outdated by the time of publication (assuming this is 2024/2025). For a current analysis, the period should reflect **recent market conditions** (e.g., 2024–2027 or latest available). [confidence: high]
  - *Series to re-check:* NSE/BSE historical price data (OHLCV) for microcap segments; latest fiscal year-end (e.g., March 2027).

- *"Median market cap rises in a straight line as the price band moves up: ₹32 crore at the bottom, ₹451 crore at the top"* — While the trend is plausible, **median market caps for microcaps can fluctuate sharply** due to delistings, new issuances, or accounting changes. The claim assumes stability over 3.5 years; a **2026–2027 recalculation** (e.g., via Screener.in or NSE’s latest filings) could show divergence. [confidence: medium]
  - *Series to re-check:* Screener.in’s latest company data (as of 2027); NSE/BSE’s annual market cap statistics.
