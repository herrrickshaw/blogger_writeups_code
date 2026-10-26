# MoSPI-sourced statistics in the blog archive: inventory of 26 October 2026

**Scope.** All 425 `posts/*.html`, with HTML tags stripped. Script-rendered stat cards and chart captions were scanned separately. The search terms were MoSPI/NSO, CPI, WPI, IIP, PLFS, GDP/GVA/GSDP, NAS, ASI, ASUSE, HCES, NSS, EnviStats, Energy Statistics, NFHS, CPI-AL/RL and inflation. 107 posts matched at least one term, and each was read. Most matches were navigation lists, other countries' data, ratios to GDP, or RBI/DGCI&S data. Nothing under `posts/` or `meta/` was changed.

**Output.** `inventory-2026-10-26.csv` has one row per figure, or per closely grouped set of figures. Its columns are: slug, series, metric, period, value, base_year, is_latest_claim, updated_note, source_as_stated, quote (verbatim, at most 200 characters), and notes.

## Counts

**Totals:** 93 figures in 35 posts. 83 of those figures are presented as the latest reading.

| Series | Posts | Figures | Presented as latest |
|---|---|---|---|
| CPI (all-India, state, item; 14 rows are the June 2026 state heatmap) | 10 | 28 | 23 |
| National Accounts (GDP growth, deflator, GVA shares, GSDP, NAS) | 11 | 18 | 16 |
| WPI (OEA/DPIIT) | 6 | 16 | 15 |
| NSS rounds (70th SAS, 77th SAS, 80th tourism survey) | 3 | 10 | 10 |
| IIP | 1 | 6 | 5 |
| PLFS | 2 | 6 | 6 |
| CPI-AL/RL (Labour Bureau) | 2 | 3 | 2 |
| MoSPI project-monitoring flash report | 1 | 2 | 2 |
| EnviStats | 1 | 2 | 2 |
| Energy (MNRE capacity via MoSPI data service) | 1 | 1 | 1 |
| HCES (World Bank Gini) | 1 | 1 | 1 |

**Excluded, with the reason:**
- **RBI series served through the MoSPI connector** (forex reserves, exchange rate, BoP services) are RBI data, not MoSPI data.
- **Correlations** in the diesel-CPI posts are derived statistics, not readings.
- **Generic ranges** ("CPI in the 4–6% band") and illustrative figures (rule-of-72) are not figures from a release.
- **Long-run spans**, such as diesel WPI +79% from April 2012 to April 2026, are long-run context.
- **The Minor Irrigation and Livestock censuses** are published by the Ministry of Jal Shakti and by DAHD, not MoSPI.
- **ASI, ASUSE and Women & Men** appear only inside "What would fix this" proposals, with no figures.

**Latest MoSPI prints, for reference:**
- **CPI (2024 base):** September 2026, all-India combined 5.54% (index 109.49). I checked this through the MoSPI API on 26 October.
- **WPI (2022-23 base):** September 2026, 11.39%.
- **IIP:** August 2026.
- **GDP:** Q1 FY2026-27 is the latest quarter. FY2025-26 has a provisional estimate on the 2022-23 base: real 7.8%, nominal 8.6%.

## Refresh candidates: "latest" readings for a period before August 2026

### A. Superseded, and no update note in the post yet (highest priority)

| Series | Slug | Period | Value as stated |
|---|---|---|---|
| CPI | cpi-inflation-heatmap-india-june-2026 | June 2026 | All-India 4.38%, plus 13 states (Telangana 6.36% … Delhi 2.96%) |
| CPI | cpi-wpi-trends-mospi-bulletin | June 2026 | All-India 4.38% (stat card), Telangana 6.36% vs Delhi 2.96%. The 22 Oct note refreshed WPI only. |
| CPI | the-lpg-distributors-commission-rose-16 | Dec 2025 | Uses the 2012-base CPI to December 2025 as "today's rupees" |
| WPI (item) | imported-fertiliser-fuel-prices-diesel | June 2026 | Diesel +32.57%, urea +1.09%, DAP +12.63% |
| WPI | reinvesting-capital-gains-in-higher | Apr 2026 | 167.6 on the 2011-12 base, used as the current deflator |
| National Accounts | five-years-and-25000-crore-later-china | FY2022-23 | NAS 2024 pharma output ₹4,56,246 cr, GVA ₹1,75,583 cr (old base) |
| National Accounts | fy2025-26-sample-report-india-trade | FY2025-26 | FAE +7% stat tile (its sub-label says it is superseded, but the 7.8% PE is not given) |
| National Accounts | up-has-indias-biggest-herd-punjab-has | FY2023-24 | Livestock is 31% of agri GVA and 5.5% of GVA |
| PLFS | indian-it-in-ai-era | Q2 FY2025-26 | 56.2 crore employed |
| HCES | one-nation-one-gst-rate-what-true-flat | 2022-23 | Gini 25.5 (HCES 2023-24 is out) |
| NSS | the-price-of-grain-msp-msv-and | 2012-13 (70th round) | 13% of paddy sellers and 16% of wheat sellers sold to a procurement agency (77th-round SAS exists) |
| EnviStats | nature-versus-nurture-indias-fertiliser | 2015–2019 | EnviStats 2019 soil-card counts; nitrogen "Low" |
| CPI-AL/RL | a-17-rural-pay-rise-that-nobody-received | May 2026 | ~2.9% vs 3.9% (preliminary) |

### B. Superseded in the body, but an update note already gives newer figures
- **WPI June 2026 (9.87%):**
  - cpi-wpi-trends-mospi-bulletin
  - fourteen-years-of-indian-wholesale

  Both carry an "Updated 22 October 2026" note with the September figure, 11.39%.
- **WPI April 2026 (+8.3%, 2011-12 base):**
  - indias-wholesale-prices-next-to: "Updated 22 October 2026"
  - inflation-trends-globally-what-five: "Updated 18 October 2026"
- **GDP:**
  - real-gdp-growth-india-fy2012-13-to (FY2025-26 +8%/+7%, FY2024-25 +6%): "Updated 22 October 2026"
  - what-india-is-actually-paying-for (7.6%): "Updated 22 October 2026"
  - effective-buying-power-china-comparison (deflator ~0.9%): "Updated 22 October 2026"
  - five-year-synthesis-trade-currency (10→8→9→6→7): "Updated 12 October 2026", corrected by "Updated 26 October 2026"

### C. Period before August 2026, but still the latest release (no action needed)

| Series | Slug | Period |
|---|---|---|
| PLFS | rural-indias-farm-employment-share | Apr–Jun 2026; the Jul–Sep quarterly bulletin is pending |
| NSS (80th round, tourism) | indias-first-tourism-survey-since-2014 | Jul 2025–Jun 2026 |
| NSS (77th round, SAS) | the-wage-beats-crop-in-survey-that | 2018-19 |
| IIP | indias-old-factory-index-said | FY2025-26 annual (its monthly figure is August 2026) |
| GSDP | tamil-nadus-gst-gap-108-economy-growing | FY2025-26 (10.83%, press-sourced) |
| GSDP | uttar-pradeshs-gst-puzzle-growing | FY2025-26 (~11%, press-sourced) |
| CPI | indias-wholesale-prices-next-to, inflation-trends-globally-what-five | Calendar-year 2025 (2.4%, World Bank) |

Two posts were left out of the candidate lists:
- **indias-food-processing-story-pli-scheme:** the GVA share has no period stated.
- **fci-grain-flow-procurement-storage:** the CPI-AL real-income figure for 2024-25 is a projection, not a reading.

## Old base presented as "latest" after the 2026 rebasings

**CPI (2012 base, replaced by 2024):**
- the-lpg-distributors-commission-rose-16 uses the 2012 series to December 2025 as the current price level, and says the 2024 series "was not linked".
- petrol-pump-margins-and-e20-one-dealer and imported-fertiliser-fuel-prices-diesel also use the 2012 base, but only for historical spans.
- epfos-pay-ceiling-rose-to-25000-after links the two bases correctly.

**WPI (2011-12 base, replaced by 2022-23):**
- **reinvesting-capital-gains-in-higher:** uses April 2026 = 167.6 as today's price level. It has no note. The MoSPI API gives 167.0 for the same month.
- **cpi-wpi-trends-mospi-bulletin:** the stat card "WPI, Apr 2026 · 167.0" is still on the old base.
- **indias-wholesale-prices-next-to and inflation-trends-globally-what-five:** use +8.3% for April 2026 as India's latest print. Their notes flag the new base.

**GDP / NAS (2011-12 base, replaced by 2022-23):**
- **real-gdp-growth-india-fy2012-13-to:** the chart and stat cards are sourced "base year 2011-12", and a card still says "the only estimate released so far". The notes correct this, but the chart has not been redrawn.
- **fy2025-26-sample-report-india-trade:** the FAE tile.
- **five-year-synthesis-trade-currency and effective-buying-power-china-comparison:** these are old-series runs, corrected only in their notes.
- **five-years-and-25000-crore-later-china:** cites NAS 2024 (old base) with no note.

**IIP:** no post presents the 2011-12 base as the latest. The IIP post compares the two bases explicitly.
