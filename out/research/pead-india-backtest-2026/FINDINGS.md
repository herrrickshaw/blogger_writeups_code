# India post-event drift, price-only proxy: findings (26 Nov 2026)

Backtest ideas 1 and 2 from `out/topics/pead-backtest-ideas-2026-11-26.md`, run as a **proxy**. Code: `run.py`; full tables: `RESULTS.md`, `results.json`. Data: `herrrickshaw/global-market-data`, `warehouse/ohlcv_adj/IN/`, daily NSE/BSE prices 2016-2025 (3,273 symbols, 2,468 days). Run with python3.13, pandas and numpy.

## What was and was not tested
- **Not the specified test.** The data holds no exchange result timestamps and no analyst surprises. Events are volume-spike days (volume above 2.5 times its prior 60-day mean on a market-adjusted move above 2 sigma, first event per stock in 40 days, eligible stocks only: 60-day median traded value at least Rs 50 lakh, price at least Rs 20). "Surprise" is the market-adjusted return over days -1 to +1. Drift is the market-adjusted return from day +2 to +61. Market return is the equal-weight mean of eligible stocks. Size terciles use the trailing 252-day median traded value, ranked among eligible stocks that day.
- **Signed drift** = sign of the first move times the drift: positive means continuation. Standard errors are clustered by event date. 477 one-day moves above 40% were dropped as splits or glitches.
- **Event purity is low.** 46.0% of events fall in the four results windows (15 Jul-20 Aug, 15 Oct-20 Nov, 15 Jan-20 Feb, 25 Apr-5 Jun) against 39.7% of the calendar. If non-earnings events are spread evenly over the year (an assumption), about 10% of all events and about 30% of in-season events are earnings days. The "results-season" subset is therefore the better read, not a clean one.
- **Placebo.** Large moves on ordinary volume (no spike) show no signed drift: mean -0.01% (t -0.03), n = 19,192. The continuation below is specific to volume-spike events.
- **Multiple testing.** 28 period-by-size cells per subset were reported. Only a few clear |t| of 3 and the cells overlap, so they are not independent tests.

## Idea 1: is there drift on the NSE, and by size?
Results-season events, 60-day signed drift, percent (n, t):

| Size | All years | 2016-18 | 2019-21 | 2022-25 |
|---|---|---|---|---|
| Small | +1.24 (3,961; t 3.65) | +2.25 (760; t 3.24) | +2.71 (1,117; t 3.61) | +0.08 (2,084; t 0.19) |
| Mid | +0.68 (3,840; t 2.08) | +0.83 (691; t 1.07) | +0.39 (981; t 0.56) | +0.76 (2,168; t 1.84) |
| Large | +0.18 (4,006; t 0.64) | +0.13 (858; t 0.22) | +0.57 (1,019; t 0.80) | +0.02 (2,129; t 0.06) |
| All | +0.70 (11,807; t 3.51) | +1.04 (2,309; t 2.34) | +1.28 (3,117; t 2.79) | +0.29 (6,381; t 1.20) |

- Pooled results-season top-minus-bottom surprise quintile gap in 60-day drift is +2.54% (monotonicity 0.90). The median signed drift is -0.30% with 49.3% positive, so the mean is carried by a minority of large moves.
- **Direction and size pattern held through 2021:** drift concentrated in small stocks (+2.25% and +2.71%, t above 3) and near zero in large ones. That fits Krishnan and Rangan (broad NSE sample, 2008-14) and Gupta and Dhusia (100 large stocks, no drift).
- **It did not hold in 2022-25:** the small-cap drift is +0.08% (t 0.19) and the small-cap quintile gap is -1.39%.
- Using all events (more non-earnings noise), 2022-25 small stocks show a reversal: -0.57% (t -2.00), slope -0.136 (t -3.91).

## Idea 2: has announcement-day absorption risen in India?
The specified test (R-squared of the day 0/1 return on analyst surprise) cannot be run. The proxy is the continuation slope: 60-day drift regressed on the day -1 to +1 move, results-season events, all sizes (n, slope, t):

| 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| 954, 0.296, 2.03 | 795, 0.287, 1.92 | 972, 0.241, 1.47 | 1,350, 0.227, 3.94 | 1,369, 0.045, 0.69 | 1,765, 0.121, 2.07 | 1,803, 0.012, 0.20 | 1,444, -0.088, -1.80 |

- The slope runs about 0.2 to 0.3 in 2018-21 and about 0 in 2022-25; in 2025 the mean signed drift is -1.11% (t -2.55). That is the direction the US took (Martineau: drift fading as more of the surprise is priced on the day), but it is a slope on a volume-spike proxy, not an absorption R-squared, and one reading of it is that continuation turned into reversal.

## What this supports and what it does not
- **Supported (proxy):** drift after volume-spike events in NSE-listed stocks was concentrated in small caps through 2021; the 2022-25 fade is visible in small caps and in the slope.
- **Not supported:** that these are earnings drift numbers. Only about 30% of in-season events are estimated earnings days. No claim here is about SUE or analyst surprises.
- **Alternative explanations for the 2022-25 fade:** the retail trading boom after 2020 (more attention on every volume spike), event contamination by non-earnings news, a changing mix of eligible stocks as traded-value filters bind, and a window that ends in 2025.
- **Costs and capacity not tested.** No spread or impact model was applied; small-cap drift of 1% to 3% over 60 days is before costs.

## Checks run
- Adjusted prices checked for continuity across HDFCBANK (2019 split), BAJFINANCE and TATAMOTORS.
- Placebo above. Date-clustered standard errors. Cells under 100 events not given a gap or slope.
- Not run: robustness to the thresholds (2.5x volume, 2 sigma, 40-day gap), a size-neutral market return, 2026 data (prices adjusted only to 2025), and out-of-sample splits other than the three periods.

## What would make this a real test
Exchange result timestamps (date and hour) for every NSE result since 2016, and a consensus or seasonal-random-walk surprise from filed quarterly profits; re-run `run.py` with events defined by those and the same cells.
