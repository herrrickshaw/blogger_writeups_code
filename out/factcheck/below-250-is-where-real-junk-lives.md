# Fact/interpretation check — below-250-is-where-real-junk-lives

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/below-250-is-where-real-junk-lives.html`

Text-SHA1: `8d2d10d7df5bc1e5`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The median stock priced under ₹250 lost 17.7% over the trailing year; every sub-band above it posted a positive median return. This isn't a quirk of one calculation method — the equal-weighted portfolio series, the per-stock median beta, and Screener's own raw return field all point the same direction." — The author equates a per-stock median 1-year return (which measures the cross-sectional median of individual stock price changes) with an equal-weighted portfolio return. These are mathematically distinct metrics; a collection of stocks can have a negative median individual return while an equal-weighted portfolio of the same stocks can yield a positive return due to asymmetric upside outliers. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Median 1-year return by price sub-band, stocks under ₹1,000 (NSE/BSE) ... ₹0–250: −17.7%"*
  — The claim that **3,850 of the 4,862 stocks under ₹1,000 (79%)** are in the ₹0–250 band is **plausible but contradicts the earlier sentence** ("4,900 stocks with wildly different profiles inside one label"), which suggests the total under ₹1,000 was **4,900**, not 4,862. The discrepancy (4,900 vs. 4,862) is minor but inconsistent. [confidence: medium]

**INTERPRETATION ERRORS:**
- *"Beta falls from 1.28 to roughly 1.08–1.12 as price rises through the sub-bands; annualised volatility falls from 24.4% to about 19–20%; and the Sharpe ratio climbs steadily from 0.33 to 1.32."*
  — The **causal claim that "price itself still isn’t the risk factor—market capitalisation and liquidity are"** is **correct**, but the **monotonic gradient in beta/volatility across price bands** (e.g., ₹0–250 having the highest beta) **implies price *does* proxy for risk in this subset**, which contradicts the earlier assertion. The article conflates **price as a *correlate*** (not a *cause*) of risk in this specific sub-₹1,000 segment, where tiny market caps dominate. [confidence: high]

**OUTDATED DATA:**
- *"Median trailing 1-year return by price sub-band ... (Screener.in data, cited 11 Aug 2026)"*
  — The **11 Aug 2026 cutoff** is likely outdated for **real-time risk-adjusted metrics** (beta, Sharpe, volatility). For **NSE/BSE data**, check the **latest weekly OHLCV parquet files** (e.g., NSE’s [historical data portal](https://www.nseindia.com/)) or **Screener.in’s latest snapshot** (as of mid-2024, their data may have updated). [confidence: high]

---
*Note: No other factual or interpretation gaps were found beyond these.*
