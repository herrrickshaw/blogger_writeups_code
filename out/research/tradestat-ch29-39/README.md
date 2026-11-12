# TradeStat chapter-level trade: HS 29 + 39 (and 28, 32, 38, 54, 55)

Built 12 November 2026 to reconcile the Chapter 29 + 39 deficit quoted in
*From Fuel to Fibre* (`from-fuel-to-fibre-indias-textile`) and
*Re-spinning the Charkha* (`re-spinning-charkha`).

## Source

Ministry of Commerce & Industry, Department of Commerce, **TradeStat**
(DGCI&S data), <https://tradestat.commerce.gov.in/>. All reports: all commodities,
**2-digit HS level, values in US $ Million**. Fetched 12 November 2026 (UTC times
in `raw/fetch_log.json`) by a direct POST of each report's form; no login or
challenge page was encountered.

| Report | Page | Selections | Raw file | Site's stated data status |
|---|---|---|---|---|
| EIDB (annual) Commodity-wise **Export** | `/eidb/commodity_wise_export` | Year 2021…2025 (each returns that FY and the year before) | `raw/eidb_export_<Y>.html` | "Data available 2017-2018 to 2025-2026, last data updated on 07/08/2026" |
| EIDB (annual) Commodity-wise **Import** | `/eidb/commodity_wise_import` | same | `raw/eidb_import_<Y>.html` | same |
| MEIDB (monthly) Commodity-wise **Export** | `/meidb/commoditywise_export` | Month = August, Year = 2026, Financial Year basis | `raw/meidb_export_2026_08.html` | "Data available: Jan 2018 to Aug 2026 ((R) Revised Final upto Mar 2026, (F) Final upto Aug 2026). Data last updated on: 23/10/2026" |
| MEIDB (monthly) Commodity-wise **Import** | `/meidb/commoditywise_import` | same | `raw/meidb_import_2026_08.html` | same |

**Latest FY2026-27 month published: August 2026.** September, October and
November 2026 selections return 0.00 for every chapter (checked 12 Nov 2026).
The monthly report's April–August columns give the like-for-like comparison:
Apr–Aug 2025 (flagged R, revised final) vs Apr–Aug 2026 (flagged F).

## Files

- `fetch_tradestat.py` — downloads the raw HTML into `raw/` (≈1.5 s between
  requests; walks back from the current month to find the latest FY27 month).
- `build_tables.py` — offline; parses `raw/` and writes the outputs below.
  Run with `python3 -I build_tables.py`.
- `chapters_annual.csv` — FY2020-21 … FY2025-26, exports, imports, balance.
- `chapters_fy27ytd.csv` — Apr–Aug 2025 vs Apr–Aug 2026.
- `results.md` — tables for each chapter plus the consistency checks.

Balance = exports − imports; negative is a deficit.

## Consistency checks (all passed)

- Sum of all 2-digit chapters equals TradeStat's "India's Total" row in every
  annual table to within ±$0.05 million (rounding).
- Each FY appears in two annual selections (as "current" and as "previous"
  year); Chapters 28/29/32/38/39/54/55 are identical in both.
- Apr–Aug 2025 is 40–44% of the FY2025-26 annual value for HS 29 and 39 —
  plausible for five months.

## Headline result (US$ billion)

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 | Apr–Aug 25 | Apr–Aug 26 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HS 29 balance | −1.7 | −6.5 | −7.6 | −6.4 | −6.5 | −5.0 | −3.0 | −2.7 |
| HS 39 balance | −6.4 | −10.9 | −15.4 | −14.4 | −14.0 | −14.6 | −6.3 | −6.7 |
| **29+39 balance** | −8.2 | −17.4 | −23.0 | −20.9 | **−20.4** | **−19.6** | −9.3 | −9.5 |
| 29+39 imports | 33.0 | 48.5 | 52.1 | 48.6 | 48.7 | 47.6 | 20.8 | 22.9 |

- The posts' FY2024-25 numbers (Ch 39 imports 22.1, deficit −14.0; Ch 29
  imports 26.6, deficit −6.5; combined 48.7 / −20.4) and FY2020-21 imports
  (13.3 / 19.7 / 33.0) all reproduce exactly. **$20.4bn is correct for FY2024-25.**
- The "$19.6bn" in *Re-spinning the Charkha* is the **full-year FY2025-26**
  combined deficit (−5.0 + −14.6), the same figures the 3 Aug 2026 callout in
  *From Fuel to Fibre* already gave per chapter. It is not a part-year total.
