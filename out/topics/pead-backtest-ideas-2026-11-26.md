# Literature-backed backtest ideas: earnings drift, dividends and attention, 26 Nov 2026

These are designs, not results. Nothing here was run. Each idea names the paper that motivates it, how that paper was read in this project (opened, abstract only, or search excerpt only), the test, what would count as failure, and the data it needs. Read status comes from `out/research/pead-behavioural-2026/notes.md`, `out/research/pead-geography-2026/NOTES.md` and `out/topics/pead-dividend-hunters-2026-11-26.md`.

## Protocol every idea must follow (lessons from the project's own failed metrics)

From `piotroski-liquidity-research` (eleven derived metrics that looked right and were wrong) and the scanners research paper:

1. **Real event dates, not volume spikes.** The blog's own US result moved from +0.010 to +0.102 (illiquidity-drift rank correlation) when SEC filing dates replaced the volume-spike stand-in. For India use exchange-filed result timestamps (date and hour; after-market results belong to the next session).
2. **Point in time.** Use only data public at the event; keep delisted names and exit at the last traded close; no current-universe selection.
3. **Corporate actions.** Adjust splits and bonuses before computing any return; the repo's raw-close panels created a fake +12.2% mean from unadjusted splits. Drop one-day moves outside a stated band only after checking they are splits.
4. **Plausibility checks on every derived field** (revenue, EBIT, ROCE ranges) and no `x or 0` on values that can be NaN. EBIT built as profit before tax plus interest is wrong for banks and NBFCs; exclude financials from any ROCE or margin screen until fixed.
5. **Report medians and the share of positive periods**, not only means; show event counts beside every number; mark any cell under 100 events as too few to read.
6. **Costs and capacity.** Net every spread of an estimated round-trip cost (Corwin-Schultz spread plus Amihud impact, as in `cost_vs_edge.py`) and state the capital at which the position exceeds 15% to 20% of median daily volume (the repo's illiquid-stock limit was about $250,000).
7. **Multiple testing.** State the hypothesis and its sign before looking; with eight ideas, a single test should clear a higher bar (Harvey, Liu and Zhu 2016 suggest t above 3; cited in the scanners paper, not opened here). Cluster standard errors by announcement date, not by stock (the October 2026 reaction data showed daily shares from 6.2% to 50%).
8. **Pre-register the sample split** (for example 2008-14 against 2019-26) and do not change it after seeing results.

## Ideas

### 1. Does NSE drift survive 2019-2026, by size tercile?
- **Motivation:** Krishnan and Rangan (NSE-IGIDR working paper, opened): top minus bottom surprise quartile +7.3% mean over days +2 to +64, 18,269 announcements, 2008-14. Gupta and Dhusia (2021, opened): no drift among 100 large NSE stocks, 2014-18. Martineau (opened): US drift gone from large stocks since 2006. The Indian studies end in 2018 or earlier.
- **Test:** For every NSE result announcement 2019-2026, compute standardised unexpected earnings (seasonal random walk, as Krishnan and Rangan) and also an analyst-forecast surprise where available. Sort into quartiles within size terciles (Nifty 100, Nifty Midcap 150, rest). Measure market-adjusted CAR from day +2 to day +64, and also from day +2 to +20.
- **Prediction (sign fixed in advance):** top-minus-bottom gap positive and largest in the smallest tercile, near zero in the largest.
- **Fails if:** the small-cap gap is under its clustered 2-sigma band, or does not shrink with size.
- **Data:** NSE and BSE results-filing timestamps (XBRL or the corporate-announcements feed), bhavcopy prices, a consensus source for analyst surprise.

### 2. Is announcement-day absorption rising in India, as it did in the US?
- **Motivation:** Martineau (opened): US announcement-day R-squared on analyst surprise rose from 1.7% (1984-90) to 11.7% (2016-19), the mechanism he gives for drift fading.
- **Test:** Regress day 0/1 abnormal return on surprise rank by year for NSE stocks, 2008-2026, separately for large, mid and small caps; plot R-squared and the under-reaction slope (drift divided by day-0/1 move) by year.
- **Prediction:** R-squared rises and the slope falls first in large caps.
- **Fails if:** neither series trends, which would say India's large caps have not followed the US path.
- **Data:** as idea 1.

### 3. Attention: Friday and crowded-day results on the NSE
- **Motivation:** DellaVigna and Pollet (opened): Friday announcements had 15% lower immediate response and 60% larger delayed response (121,381 announcements, 1995-2004). Peress (opened): drift 6.7% with low media coverage against 3.1% with high coverage for the top decile. Hirshleifer, Lim and Teoh (2009) on crowded days: seen only as Fink's summary.
- **Test:** Split NSE announcements by weekday, by after-hours release, and by the number of firms reporting the same day (top tercile against bottom). Compare day 0/1 response and day +2 to +60 drift. Use news-count or analyst-coverage as a coverage proxy where media data is unavailable.
- **Prediction:** weaker immediate response and stronger delayed drift on Fridays, after hours and on crowded days; Indian results season is dense, so crowding should matter more than in the US.
- **Fails if:** the interaction terms are insignificant after clustering by date.

### 4. Illiquidity and capacity: is NSE drift net of cost tradable?
- **Motivation:** Chordia et al. (2009, as cited in the existing PEAD post, not opened here) argue costs explain persistence; this blog's own result is a +0.102 link with true dates in the US and +0.242 in Brazil (109 events). The repo's cost-versus-edge module gave a $250,000 capacity for a thinly traded premium.
- **Test:** Rank NSE stocks by pre-event Amihud illiquidity; compute the drift gap per illiquidity quintile; subtract estimated round-trip cost (Corwin-Schultz plus impact) and report net gap by capital level (Rs 10 lakh, 1 crore, 10 crore).
- **Prediction:** gross drift concentrates in the illiquid quintiles and net drift vanishes above a modest capital level.
- **Fails if:** the net gap stays positive at Rs 10 crore, which would be a surprising capacity.

### 5. Dividend omissions and cuts as a payout-risk screen (the dividend-hunter test)
- **Motivation:** Michaely, Thaler and Womack (1995): 12-month market-adjusted +7.5% after initiations, -11.0% after omissions (search excerpt only). Benartzi, Michaely and Thaler (1997): dividend changes follow earnings changes (excerpt only). Grullon et al. (2005) and Stacescu (2006) disagree on whether dividends carry information about future earnings (excerpts only).
- **Test:** For NSE dividend payers 2010-2026, define a negative-surprise run (two or three consecutive quarters in the bottom surprise quartile). Test whether it predicts a dividend cut or omission in the next four quarters, and measure the 12-month return after cuts and omissions. Compare payers with high and low payout cover.
- **Prediction:** the negative-surprise run raises the probability of a cut, and the post-cut drift is negative.
- **Fails if:** negative runs do not predict cuts better than payout cover alone; then drift adds nothing for an income investor.
- **Open question the literature does not answer:** no study found tests drift separately for dividend growers and flat payers, or covers Indian payers. Dividend declarations are filed with the exchanges and give a clean date.

### 6. Add-after-good-news rule for an income portfolio
- **Motivation:** the timing case in the dividend section of the behavioural post (reasoning, not a tested rule).
- **Test:** Build a payer universe (Nifty Dividend Opportunities or a yield-and-cover screen). Compare buying equal amounts on a fixed monthly schedule against buying only after a positive-surprise result (waiting a fixed number of days after a negative one), over 2012-2026. Report total return, income received, turnover and drawdown, net of costs.
- **Prediction:** a small improvement in return and drawdown at low turnover; large gains would be suspicious.
- **Fails if:** the improvement is within the clustered noise band, which is the likely outcome in liquid large caps.

### 7. Piotroski and quality combined with drift
- **Motivation:** the blog's own result: strong F-scores beat weak ones by 31.4 percentage points in large illiquid US stocks, mostly because weak names fall (-24.6%). Quality (QMJ) alpha in India of 0.92% a month is the IIMA paper's finding, summarised in the scanners repo.
- **Test:** Intersect a positive earnings surprise with a high F-score (and separately a high quality score) on the NSE; compare drift against positive surprises with low scores. Exclude financials until the EBIT definition is fixed.
- **Prediction:** drift after a good surprise is stronger when quality is high (the news is more persistent) and the downside drift is stronger after a bad surprise at a low-quality firm.
- **Fails if:** the interaction is not significant; the repo's earlier ROCE addition did not beat the market in US tests.
- **Note:** the repo's Piotroski figures are provisional (eight defects found, one unfixed); rerun on a corrected panel before using them as an input.

### 8. Calibration of options-implied earnings moves on NSE stock options
- **Motivation:** the October 2026 US sample: 38 of 137 names closed beyond the implied move (27.7%; day-clustered interval 17.7% to 37.8%) against 42.5% for a normal curve and 36.8% for a Laplace curve.
- **Test:** For NSE stocks with listed options, compute the pre-result straddle price and the next-session absolute move, 2019-2026; report the share beyond the implied move, the mean ratio of realised to implied, and the same by size and by result day.
- **Prediction:** the share beyond sits below the normal benchmark (a premium in implied moves or fat tails); the ratio is stable across years.
- **Fails if:** the share is near or above 42.5%, which would say implied moves are too small.
- **Data:** NSE option chains before results; liquid only (a thin chain gives a meaningless straddle).

### 9. FII behaviour around results
- **Motivation:** Krishnan and Rangan (FII working paper, opened): FII net buying at the announcement is unrelated to the surprise and negatively related to later returns, so FIIs do not exploit the drift.
- **Test:** Using daily FII flows, test whether the result still holds for 2015-2026, and whether domestic institutions (mutual funds, from monthly holdings) lean with or against the surprise.
- **Prediction:** FIIs remain unrelated to the surprise; domestic funds show some positive relation as their share rises.
- **Data:** NSDL or exchange FII data; AMFI monthly holdings, which lag, so use the longer window.

## What not to backtest on the current evidence
- A country ranking of drift from the blog's 19-market data: the per-market quintile gap was never saved and the event dates are volume-spike proxies, so a ranking is unsupported (see the geography post).
- Any strategy built on the October 2026 reaction counts: eight days, a vendor-selected list, no surprise labels.
- Any dividend-growth rule that relies on the 1995 initiation and omission figures without opening the paper and checking its sample period and calendar (the figures here come from an abstract excerpt).

## Suggested order
1. Idea 1 and idea 2 together (same data, answers whether Indian drift exists today and why the US lost it).
2. Idea 5 (dividend payout risk), because it answers the income-investor question the posts left open.
3. Idea 4 (capacity) as the reality check on any positive result.
4. Ideas 3, 7, 8 and 9 as extensions.
Build one reusable event table (symbol, result timestamp, standalone or consolidated, surprise, size tercile, illiquidity, prior-quarter dividend, payout cover) and run ideas 1 to 5 off it.
