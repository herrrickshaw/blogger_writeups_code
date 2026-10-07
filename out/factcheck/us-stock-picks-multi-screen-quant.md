# Fact/interpretation check — us-stock-picks-multi-screen-quant

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/us-stock-picks-multi-screen-quant.html`

Text-SHA1: `9d5cc983cd14f18f`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **Leonardo DRS (DRS) listed under "Industrials" with a sector mismatch** — The article states "Industrials" in the sector column but later clarifies in the thesis row that it is "Leonardo DRS (Industrials)" with a backfilled note. However, the sector mix table lists it under "Industrials (Leonardo DRS, backfilled)" but does not explicitly reconcile the inconsistency in the main table. The ticker **Leonardo DRS** is actually a **defense/aerospace** company (Leonardo S.p.A.'s subsidiary), not strictly "Industrials" as traditionally defined in US stock classifications. [confidence: high]

- **Medpace Holdings (MEDP) Avg ROE of 65.3%** — While the claim may be correct for the specific period, a 65.3% ROE is unusually high for a healthcare services company (e.g., clinical trial services) and would require verification against recent SEC filings (e.g., 10-K/10-Q) for 2025–2026. [confidence: medium]

INTERPRETATION ERRORS:
- **Piotroski F-score as a standalone "strong" indicator without context** — The article repeatedly describes stocks with a Piotroski F-score of 7 or 8 as "Piotroski strong" without clarifying that the F-score is a **relative** metric (out of 9) and that a score of 7–8 is **not universally strong** (e.g., it depends on the stock's baseline fundamentals, sector norms, and historical performance). This misleads readers into assuming all F=7–8 stocks are equally robust. [confidence: high]

- **Liquidity tiers (T1, T2, T3) as binary "tradeable" vs. "illiquid" labels** — The article gates out illiquid names but then includes **T2_LIQUID and T3_MID** stocks (e.g., TIGO, ATAT, NBIS) in the "CORE" sleeve without distinguishing their liquidity risk. While the liquidity filter is noted, the **equal-weight portfolio** treats all T1–T3 stocks identically, ignoring that T3 stocks (e.g., TIGO with ~$2M/day turnover) may have higher slippage or bid-ask spreads than T1 stocks. [confidence: high]

OUTDATED DATA:
- **None found** — All figures (prices, liquidity, conviction scores) are dated **2026-07-24**, and while newer data may exist, the article explicitly states it is a "scan as of" that date with no claim of "latest" or "current" data. No official series (e.g., SEC filings, Bloomberg terminals) are cited for verification.
