# INR FX pairs dataset

Daily and monthly INR exchange rates against USD, CNY (yuan), RUB (rouble),
SAR (Saudi riyal) and AED (dirham), 2016-08-15 to present.

## Files
- `inr_fx_pairs_daily_derived.csv` — daily close, INR per unit of foreign currency
- `inr_fx_pairs_monthly.csv` — month-end close, same units
- `inr_fx_pairs_summary.csv` — 1y/3y/5y/10y/YTD % change and annualised volatility per pair
- `usd_cross_legs_daily.csv` — raw USD-leg quotes used to derive the cross rates (source data)

## Method
- USDINR and AEDINR: direct Yahoo Finance tickers (`USDINR=X`, `AED=X` combined with `USDINR=X`).
- CNYINR, RUBINR, SARINR: no reliable direct INR cross exists on Yahoo, so each is
  derived as USDINR / USD<CCY> (e.g. RUBINR = USDINR / (RUB=X)). This mirrors how these
  pairs actually trade in practice — as USD cross-rates, not direct interbank quotes
  (see the FBIL data point noted in the "Can Rupee Trade Actually Offset..." post:
  FBIL only publishes official INR reference rates for USD/GBP/EUR/JPY/AED/IDR).

## Known data-quality issues
- A single-day bad tick in the Yahoo RUB=X series on 2023-03-16 (implied ~1400% one-day
  move) was identified and interpolated out. The real March 2022 rouble crash (RUB
  weakening to INR 0.55, i.e. RUB briefly worth ~120+/USD) and the June-July 2022 rebound
  (RUB strengthening to INR ~1.5, i.e. ~50-55/USD under capital controls) are both genuine
  and left in the series.
- SAR=X carries some noisy ticks around the 3.75 hard peg (min 3.30, ~97% of days within
  0.5% of peg) — treat SAR's derived annualised volatility (~9.6%) as an upper bound; a
  cleaner series would likely show closer to AED's ~6.0% (AED=X is essentially glitch-free,
  std of 0.0004 around its 3.6725 peg).

## Provenance
Pulled via yfinance (`period="10y", interval="1d"`), 14 Aug 2026. Not an official RBI/FBIL
series for CNY/RUB/SAR since none exists — see the caveat above.
