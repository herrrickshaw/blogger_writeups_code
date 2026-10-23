# Data freshness worklist, as of 2026-10-23

> **Model extraction, script judgement, not verified fact.** Gemini/Mistral listed each post's data
> points; this script counted how many newer releases have *probably* come out, from the period end,
> release frequency and a typical lag. Fetch the newer release from the primary source before changing
> anything (house rule: PIB / MoSPI / RBI / DGCI&S / PPAC / ministry originals).

135 data points from 3 posts; 3 probably superseded (1 headline) across 3 posts, counted once per publisher and release frequency at the post's newest period (28 older figures not listed because the post already has a newer one from that source). 0 posts have no clean model answer yet; 0 skipped as too large. Full list: `out/freshness/worklist.csv`.

## Series behind in the most posts

| Publisher / series | Posts |
|---|---|
| NSE: weekly NSE data | 1 |
| DPIIT: Quarterly Fact Sheet on FDI Inflow | 1 |
| PNGRB: network-expansion statements | 1 |

## Posts ranked by stale data (headline figures weighted x3)

### 050-is-its-own-category-diving-into  (score 15)
- **H** 2,086 stocks — Jan 2023–Aug 2026 (NSE: weekly NSE data; weekly) — ~5 newer release(s), 12 figure(s) from this source [gemini]

### indias-fdi-moved-to-software-and  (score 4)
- $12.1 billion — April 2026 (DPIIT: Quarterly Fact Sheet on FDI Inflow; monthly) — ~4 newer release(s), 1 figure(s) from this source [gemini+mistral]

### 028-unit-diesel-math-behind-indias-data  (score 3)
- 5,665 CNG stations — March 2023 (PNGRB: network-expansion statements; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini]
