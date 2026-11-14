[kept verbatim: dated update notes]

## 1. Under ₹1,000: one bucket, four very different neighbourhoods

Of the 4,862 NSE/BSE stocks priced under ₹1,000, this article split them into four sub-bands — ₹0–250, ₹250–500, ₹500–750 and ₹750–1,000 — using the same Screener.in price data as [the earlier five-band piece](https://blog.vertistratsolution.com/2026/08/a-slice-of-apple-costs-about-1700-slice.html). The split is lopsided in a way the single "under ₹1,000" label never showed:


[T1 "1. Under ₹1,000: one bucket, four very different neighbourhoods" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Price sub-band, ₹ | c1 Stocks | c2 Share of the under-1,000 universe, % | c3 Median market cap, ₹ crore
  r0: 0–250 | 3,850 | 79.2 | 80
  r1: 250–500 | 568 | 11.7 | 1,154
  r2: 500–750 | 290 | 6.0 | 3,713
  r3: 750–1,000 | 154 | 3.2 | 3,474


Nearly 80% of every stock priced under ₹1,000 is actually priced under ₹250, and the median market cap in that bottom slice — ₹80 crore — is a rounding error next to the ₹1,154 crore median just one sub-band up. The "under ₹1,000" bucket in that piece wasn't really one population; it was a huge population of tiny, largely unproven companies with a much smaller population of genuinely small-to-mid-cap businesses riding along at the top of the same label.

### Beta, return and Sharpe ratio, split four ways

Using the same methodology as the earlier piece — equal-weighted portfolios, 3.5 years of weekly local NSE price data (2 January 2023 to 7 August 2026), a 6.5% risk-free proxy — computed separately for each of the four sub-bands:


[T2 "Beta, return and Sharpe ratio, split four ways" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Price sub-band, ₹ | c1 Stocks with computed beta | c2 Median beta | c3 Portfolio return, % p.a. | c4 Portfolio volatility, % p.a. | c5 Sharpe ratio
  r0: 0–250 | 1,086 of 1,267 priced | 1.28 | 14.6 | 24.4 | 0.33
  r1: 250–500 | 333 of 374 priced | 1.19 | 24.3 | 21.0 | 0.85
  r2: 500–750 | 207 of 229 priced | 1.08 | 25.0 | 19.3 | 0.96
  r3: 750–1,000 | 112 of 117 priced | 1.12 | 32.7 | 19.8 | 1.32


Unlike the five broad bands in the earlier piece, this is a genuinely clean, close-to-monotonic gradient. Beta falls from 1.28 to roughly 1.08–1.12 as price rises through the sub-bands; annualised volatility falls from 24.4% to about 19–20%; and the Sharpe ratio climbs steadily from 0.33 (poor, per the ranges in the earlier piece) to 1.32 (good) at the top of the range. At this level of zoom the ₹0–250 sub-band is the worst-performing, highest-risk group — worse than the under-₹1,000 band looked as a whole, because that wider label was averaging nearly 4,900 mostly-junk names against a much smaller number of decent ones.

### Real returns confirm the same pattern

Screener.in's own reported return and profit-growth fields, for the full population in each sub-band rather than a sample, tell the same story independently of the beta/Sharpe calculation above:


[T3 "Real returns confirm the same pattern" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Price sub-band, ₹ | c1 Median 1-year return, % | c2 Median 6-month return, % | c3 Median YoY quarterly profit growth, %
  r0: 0–250 | −17.7 | −5.6 | 13.5
  r1: 250–500 | 0.4 | 6.1 | 30.1
  r2: 500–750 | 4.3 | 11.8 | 21.5
  r3: 750–1,000 | 8.3 | 8.3 | 20.9


[chart: 
 
 
 Below ₹250, the median stock lost money 
 Median 1-year return by price sub-band, stocks under ₹1,000 (NSE/BSE) 
 
 0% 

 
 -20% 
 
 +10% 

 
 −17.7% 
 ₹0–250 
 3,850 stocks (79%) 

 
 +0.4% 
 ₹250–500 
 568 stocks (12%) 

 
 +4.3% 
 ₹500–750 
 290 stocks (6%) 

 +8.3% 
 ₹750–1,000 
 154 stocks (3%) 
 Source: Screener.in company data, 4,862 NSE/BSE stocks under ₹1,000, 11 Aug 2026 
]

Median trailing 1-year return by price sub-band, among India's under-₹1,000 stocks (Screener.in data, cited 11 Aug 2026).

The median stock priced under ₹250 lost 17.7% over the trailing year; every sub-band above it posted a positive median return. This isn't a quirk of one calculation method — the equal-weighted portfolio series, the per-stock median beta, and Screener's own raw return field all point the same direction.

The obvious next question is whether the ₹0–250 band is uniformly bad, or whether something inside it is doing most of the damage. The rest of this piece splits it again.

## 2. Inside ₹0–250: most of the mass sits at the very bottom

Splitting the 3,850 stocks priced under ₹250 into four ₹50-wide bands shows the same lopsided pattern this blog's price-segmentation work keeps finding at every level it's checked:

The Bombay Stock Exchange in Mumbai, home to the listed universe this piece slices into ever-narrower price bands to find where the market's real basement sits. [BSE - Bombay Stock Exchange Building](https://commons.wikimedia.org/wiki/File:BSE_-_Bombay_Stock_Exchange_Building.jpg), Niyantha Shekhar, CC BY 2.0, via Wikimedia Commons.


[T4 "2. Inside ₹0–250: most of the mass sits at the very bottom" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Price band, ₹ | c1 Stocks | c2 Share of the under-250 universe, % | c3 Median market cap, ₹ crore
  r0: 0–50 | 2,086 | 54.2 | 32
  r1: 50–100 | 743 | 19.3 | 120
  r2: 100–150 | 469 | 12.2 | 227
  r3: 150–250 | 552 | 14.3 | 451


More than half of every stock priced under ₹250 — 2,086 of them, or 43% of the entire under-₹1,000 universe in section 1 — is actually priced under ₹50. Median market cap rises in a straight line as the price band moves up: ₹32 crore at the bottom, ₹451 crore at the top of this range, a 14× jump across just four ₹50-wide bands.

## 3. Beta, return and Sharpe ratio inside the basement

Same methodology as section 1 — equal-weighted portfolios, 3.5 years of weekly local NSE price data (2 Jan 2023–7 Aug 2026), 6.5% risk-free proxy:


[T5 "3. Beta, return and Sharpe ratio inside the basement" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Price band, ₹ | c1 Stocks with computed beta | c2 Median beta | c3 Portfolio return, % p.a. | c4 Portfolio volatility, % p.a. | c5 Sharpe ratio
  r0: 0–50 | 437 of 539 priced | 1.31 | 12.0 | 27.2 | 0.20
  r1: 50–100 | 225 of 253 priced | 1.29 | 15.9 | 24.5 | 0.38
  r2: 100–150 | 155 of 179 priced | 1.25 | 18.6 | 24.0 | 0.50
  r3: 150–250 | 269 of 296 priced | 1.23 | 15.2 | 21.9 | 0.40


The ₹0–50 band has the worst Sharpe ratio of any price segment this blog has measured — 0.20, deep in "poor" territory, driven by the highest volatility (27.2%) and highest beta (1.31) at the same time as the lowest return of the four. It is, on every measure used so far, the single worst place in the Indian listed-equity market to have parked money over this window, and it's also the single largest group by count: 2,086 stocks, more than the entire ₹1,000-and-above universe from the very first piece in this series combined.

## 4. What "cheap" actually correlates with down here

Screener.in's own return, profit-growth and dividend fields for the full population in each micro-band, not a sample:


[T6 "4. What "cheap" actually correlates with down here" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Price band, ₹ | c1 Median 1-year return, % | c2 Median 6-month return, % | c3 Median YoY quarterly profit growth, % | c4 Median dividend yield, %
  r0: 0–50 | −22.7 | −10.1 | 1.9 | 0.0
  r1: 50–100 | −16.1 | −2.5 | 16.5 | 0.0
  r2: 100–150 | −9.3 | −0.2 | 0.9 | 0.0
  r3: 150–250 | −6.2 | 1.8 | 34.9 | 0.0


Two things stand out. First, the return gradient is completely clean here — median 1-year return improves at every single step up, from −22.7% under ₹50 to −6.2% at ₹150–250, and every one of these four bands still posted a negative median return, worse across the board than the ₹250-plus sub-bands in section 1. Second, the median dividend yield is exactly 0.0% in all four bands — meaning the typical stock anywhere under ₹250, not just under ₹50, pays its shareholders nothing at all, a detail the price tag alone doesn't hint at and profit-growth figures (which stay positive even in the worst band) can actively mask.

## 5. Three levels of zoom

Three levels of zoom, and the pattern gets more extreme every time the lens narrows: no clean price-risk relationship across the five broad bands from ₹1,000 up; a real, close-to-monotonic gradient once "under ₹1,000" is split into four; and now an even sharper version of the same gradient inside just the bottom quarter of that.

The mechanism is the one section 1 points to. The finding of the broad five-band comparison, that price and risk are not cleanly related, still holds among stocks priced above ₹1,000: those bands showed betas clustered close to 1.0 with no clean order. The relationship reappears only at the bottom, because price under roughly ₹250, and especially under ₹50, is doing double duty as a rough proxy for market capitalisation, which is the thing that's actually moving with risk. Genuinely small companies rarely get split or bonus-issued down from a high share price the way established companies do, so at the very bottom of the market a low price and a small company tend to go together. It is not, on this evidence, a coincidence that the cheapest four out of every ten listed Indian stocks by count are also the segment with the highest beta, the worst Sharpe ratio, the most negative typical return, and no dividend income to show for holding through the volatility.

Verdict: The basement has a sub-basement. Splitting "under ₹1,000" four ways puts 79% of those stocks below ₹250, where the median company is worth ₹80 crore and the median trailing-year return is −17.7%. Splitting "under ₹250" into four narrower bands shows the ₹0–50 range — 2,086 stocks, 43% of the entire under-₹1,000 universe — is the single worst-performing, highest-risk price segment identified at any level of zoom: Sharpe ratio 0.20, median 1-year return −22.7%, median dividend yield zero. The gradient from there to ₹250 is clean and consistent across every metric checked (beta, Sharpe, return, market cap), reinforcing that market capitalisation and liquidity, not the price tag itself, are what's actually driving the pattern this deep into the cheap end of the market.

### Related on this blog

See also: [A Slice of Apple Costs About ₹1,700. A Slice of MRF Still Isn't Legal.](https://blog.vertistratsolution.com/2026/08/a-slice-of-apple-costs-about-1700-slice.html) — the original five-band price segmentation this piece splits further. · [Why Bet on One Horse, When You Can Buy the Stable?](https://blog.vertistratsolution.com/2026/08/why-bet-on-one-horse-when-you-can-buy.html) — the Markowitz/Sharpe-ratio framework and methodology used here.

## What would fix this

[kept verbatim, open: What would fix this; 5 items]
