# Fact/interpretation check — how-to-use-market-correlation-matrices

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-market-correlation-matrices.html`

Text-SHA1: `c638e9807a2d0d81`

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
- none found  

**INTERPRETATION ERRORS:**  
- **Claim:** “Korea and India are still the most tightly co‑moving markets, Europe the lowest.”  
  **Reasoning gap:** The article ranks markets solely on the reported *mean* pairwise correlation, but the six markets have different numbers of symbols (e.g., 1,828 for India vs. 2,883 for the US) and non‑aligned 252‑day windows (India ends 22 Oct 2026, US ends 21 Oct 2026, China ends 1 Jul 2026). Mean correlation is sensitive to sample size, symbol selection (thinly‑traded stocks, ETFs, dual‑listed securities), and the distribution of correlations (a few very high pairs can inflate the mean). Therefore, using the mean alone to assert that Korea and India are “most tightly co‑moving” is an apples‑to‑oranges comparison that does not robustly support the conclusion. [confidence: high]  

**OUTDATED DATA:**  
- **Claim:** “China … window ending 1 Jul 2026 (stale, so its row is unchanged in substance from the committed one).”  
  **Series to re‑check:** The underlying OHLCV warehouse for the China market (price series used to compute the correlation matrix). By the article’s own revision date (23 Oct 2026) and today’s date (29 Oct 2026), newer daily price data for China (e.g., trading days in August‑October 2026) should be available, meaning the “latest” snapshot is likely outdated. [confidence: high]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **“0.211 India mean pairwise r, window ending 22 Oct 2026 (was 0.225)”** — The prior value of **0.225** for India’s mean pairwise correlation is inconsistent with the earlier table, which shows the old mean as **0.2253** (not 0.225). The rounding discrepancy may mislead readers about the magnitude of change. [confidence: high]

INTERPRETATION ERRORS:
- **“Korea and India are still the most tightly co-moving markets, Europe the lowest.”** — While the mean pairwise correlations (India: 0.211, Korea: 0.253) are numerically higher than Europe’s (0.098), this claim conflates pairwise correlation with *market-level co-movement*. Higher pairwise r does not necessarily imply stronger *diversification benefits* or tighter *market-wide synchronization*—it only reflects individual stock correlations. A better phrasing would acknowledge that these metrics measure stock-level linkage, not systemic risk or portfolio-level diversification. [confidence: high]

OUTDATED DATA:
none found
