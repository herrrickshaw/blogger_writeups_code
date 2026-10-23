# Data freshness worklist, as of 2026-10-23

> **Model extraction, script judgement, not verified fact.** Gemini/Mistral listed each post's data
> points; this script counted how many newer releases have *probably* come out, from the period end,
> release frequency and a typical lag. Fetch the newer release from the primary source before changing
> anything (house rule: PIB / MoSPI / RBI / DGCI&S / PPAC / ministry originals).

9895 data points from 270 posts; 529 probably superseded (170 headline) across 169 posts, counted once per publisher and release frequency at the post's newest period (610 older figures not listed because the post already has a newer one from that source). 0 posts have no clean model answer yet; 2 skipped as too large. Full list: `out/freshness/worklist.csv`.

## Series behind in the most posts

| Publisher / series | Posts |
|---|---|
| DPIIT: List of IEM Filed | 2 |
| PPAC: Industry Consumption Report POL & NG | 2 |
| RBI: Foreign Exchange Reserves | 2 |
| DGCI&S: HS 710510 imports | 2 |
| RBI: Weekly Statistical Supplement | 2 |
| Ember: Inter-state grid renewable curtailment | 2 |
| HPCL: pipeline throughput | 2 |
| CPCB: Continuous Ambient Air Quality Monitoring Station data | 1 |
| Business Standard: Share price | 1 |
| Agmarknet: mandi modal prices against MSP | 1 |
| OilPriceAPI & Rigzone: Brent Crude | 1 |
| PPAC: Implied Indian basket | 1 |
| CNBC: Berkshire Hathaway share price | 1 |
| MoHUA: India daily waste stream volume | 1 |
| USGC: Ethanol Market and Pricing Data | 1 |
| PMBI: PMBI Product List | 1 |
| data.gov.in: Agmarknet mandi prices | 1 |
| Tradingeconomics, ConvexTrade, OneValor: Brent Crude | 1 |
| DFPD: Foodgrain Bulletin | 1 |
| DFPD: Central-pool stock levels | 1 |
| PPAC: ATF consumption | 1 |
| DGCI&S: HS 8301 import value | 1 |
| PPAC: Snapshot of India's Oil & Gas Data | 1 |
| Department of Fertilizers: Market Development Assistance (MDA) scheme | 1 |
| RBI: Services trade balance | 1 |
| NPCI: NPCI merchant-category classification data | 1 |
| ANP: Gasolina C mandatory blend | 1 |
| Coir Board: Coir and coir-product exports | 1 |
| PNGRB: CNG stations built out | 1 |
| USDA / industry data (via secondary coverage): India cotton lint yield national peak | 1 |

## Posts ranked by stale data (headline figures weighted x3)

### fuel-pricing-to-crude-cost  (score 67)
- **H** $78.87/bbl — 5 Aug 2026 (OilPriceAPI & Rigzone: Brent Crude; daily) — ~72 newer release(s), 2 figure(s) from this source [gemini+mistral]
- **H** $78.30/bbl — 5 Aug 2026 (PPAC: Implied Indian basket; daily) — ~72 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** $104–105/bbl — 25 Sep 2026 (Tradingeconomics, ConvexTrade, OneValor: Brent Crude; daily) — ~21 newer release(s), 2 figure(s) from this source [gemini+mistral]
- **H** ₹94.77/l — as on 01.10.2025 (PPAC: Ready Reckoner; half-yearly) — ~1 newer release(s), 17 figure(s) from this source [gemini+mistral]
- $78.04 — 5 Aug 2026 (OilPriceAPI: Dubai benchmark; daily) — ~72 newer release(s), 2 figure(s) from this source [gemini]
- $69.89/bbl — Jul–Sep 2025 (PPAC: Table 8.1; quarterly) — ~3 newer release(s), 2 figure(s) from this source [gemini+mistral]
- ₹66.61/litre — FY2025-26 (Government disclosures (reported early August 2026): Ethanol procurement cost; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### india-approved-15-lakh-crore-in  (score 66)
- **H** ₹35,354 crore — March 2026 (PIB / ministry: PLI programme disbursement; monthly) — ~5 newer release(s), 6 figure(s) from this source [gemini+mistral]
- **H** ₹18,500 crore — March 2026 (MNRE / Ministry: PLI Solar scheme outlay; monthly) — ~5 newer release(s), 2 figure(s) from this source [gemini]
- **H** ₹17,490 crore — March 2026 (Ministry: NGHM/SIGHT scheme outlay; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini]
- **H** ₹15,000 crore — March 2026 (DoP: PLI Pharmaceuticals outlay; monthly) — ~5 newer release(s), 6 figure(s) from this source [gemini]
- ₹953 cr — March 2026 (MeitY: PLI-LSEM disbursements; monthly) — ~5 newer release(s), 2 figure(s) from this source [gemini]
- ₹209.8 crore — FY2024-25 (DoP: Medical-device-park infrastructure release; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]

### cocoa-quintupled-then-gave-most-of-it  (score 63)
- **H** $394 to $38 per kg — 2019 to Q4 2025 (UN Comtrade / Central Bank of Madagascar: Madagascar vanilla export price; quarterly) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** 3x — 2023 to 2024 (UN Comtrade: India cocoa-bean import bill; annual) — ~1 newer release(s), 16 figure(s) from this source [gemini+mistral]
- US$12,931 per tonne — 18 Dec 2024 (CNBC / Barchart: New York futures intraday record; daily) — ~667 newer release(s), 1 figure(s) from this source [gemini]
- US$11,545 per tonne — 31 Dec 2024 (ICCO: New York nearby futures; daily) — ~654 newer release(s), 2 figure(s) from this source [gemini]
- US$4,000 per tonne — 30 Jan 2026 (Bloomberg: New York futures; daily) — ~259 newer release(s), 1 figure(s) from this source [gemini]
- US$4,000/tonne (Jan 2026) / US$2,850/tonne (spring 2026) — Jan 2026–Mar–Apr 2026 (Bloomberg / market data aggregators: New York futures; daily) — ~169 newer release(s), 1 figure(s) from this source [mistral]
- ₹830/kg (Apr 2024) / ₹1,000/kg (May 2024) / ₹550/kg (Sep 2024) — Apr–Sep 2024 (Onmanorama / Mongabay India: Farmgate price reports; monthly) — ~23 newer release(s), 1 figure(s) from this source [mistral]
- US$5,590 per tonne — 24 Sep 2026 (market data: New York futures; daily) — ~22 newer release(s), 1 figure(s) from this source [gemini]
- 265 ha (2000–01) → 2,000+ ha (2004–05) / 5,815 ha (2005–06) — 2000–06 (Spices Board: Area statistics; annual) — ~20 newer release(s), 1 figure(s) from this source [mistral]
- US$2,850 per tonne — Mar-Apr 2026 (market data aggregators: New York futures cycle low; monthly) — ~4 newer release(s), 1 figure(s) from this source [gemini]
- 4,733 thousand tonnes — 2024/25 (ICCO: Quarterly Bulletin of Cocoa Statistics - Output; quarterly) — ~3 newer release(s), 8 figure(s) from this source [gemini]
- US$38 per kg — Q4 2025 (Central Bank of Madagascar: Average export price; quarterly) — ~2 newer release(s), 2 figure(s) from this source [gemini]
- 432,000 tonnes (actual) / 800,000 tonnes (target) — 2023/24 (COCOBOD (Ghana): Annual production report; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- 44 tonnes — 2024-25 (Ministry of Agriculture: Horticulture statistics - Vanilla production; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]

### india-will-finance-waste-to-energy  (score 61)
- **H** 1.66 lakh tonnes a day — 2026 (MoHUA: India daily waste stream volume; daily) — ~51 newer release(s), 1 figure(s) from this source [gemini]
- **H** 132 plants — January 2026 (PNGRB: Compressed Biogas Plants Running; monthly) — ~7 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** 1,129 plants — end-2024 (Chinese government data: China waste-to-energy plant count; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 1.15 million tonnes daily — end-2024 (Chinese government data: China waste-to-energy daily throughput capacity; daily) — ~654 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 7,250–8,000 tonnes daily — 2026 (Delhi municipal authorities / media reports: Delhi WtE daily waste burning volume; daily) — ~51 newer release(s), 1 figure(s) from this source [gemini]
- 250–300 MW — 2020 (MNRE / Government of India: Installed waste-to-energy capacity; annual) — ~5 newer release(s), 2 figure(s) from this source [gemini]
- 800 MW (target) vs 250–300 MW (installed by 2020) — 2018–2019 (target) / 2020 (actual) (Bharatnama (via CSE/Down To Earth): Waste-to-energy capacity; annual) — ~5 newer release(s), 1 figure(s) from this source [mistral]

### indias-wholesale-prices-next-to  (score 50)
- **H** +9.4% — April 2026 (national statistical offices/central banks: Producer Price Index / WPI; monthly) — ~4 newer release(s), 5 figure(s) from this source [gemini+mistral]
- **H** +8.3% — April 2026 (MoSPI API: India WPI; monthly) — ~4 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 167.0 (MoSPI), 167.6 (Office of the Economic Adviser) — April 2026 (MoSPI / Office of the Economic Adviser: Wholesale Price Index (WPI); monthly) — ~4 newer release(s), 1 figure(s) from this source [mistral]
- 9.68% — May 2026 (Moneylife: WPI; monthly) — ~3 newer release(s), 1 figure(s) from this source [gemini+mistral]
- +2.4% (Jan 2026) to +12.3% (May 2026) — January–May 2026 (US Bureau of Labor Statistics: Producer Price Index by Commodity: All Commodities (PPIACO); monthly) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- +1.9% (Jan 2026) to +8.6% (May 2026) — January–May 2026 (Bank of Korea: Producer Price Index total index (404Y014); monthly) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- −2.7% (Feb 2026) to +4.9% (May 2026) — February–May 2026 (Eurostat: Industrial Producer Prices (EA20); monthly) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- +10.1 — June 2026 (BLS: PPI; monthly) — ~2 newer release(s), 5 figure(s) from this source [gemini]
- +15.4% (2022), −0.8% (2023) — 2022–2023 (MoSPI: Wholesale Price Index (WPI); annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- +2.9% (Mar 2026) to +7.1% (Jun 2026) — March–June 2026 (Bank of Japan: Corporate Goods Price Index (CGPI); monthly) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- −4.4% (Jan 2026) to +2.5% (Jun 2026) — January–June 2026 (IBGE: Índice de Preços ao Produtor (IPP); monthly) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- 6.8 — 2020 to 2024 (National Bureau of Statistics of China: Statistical Communiqué on National Economic and Social Development; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 194.4 (1940s baseline) to 260.3 (2024) — 2020–2024 (US Bureau of Labor Statistics: Producer Price Index by Commodity: All Commodities (PPIACO); annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### fy2025-26-sample-report-india-trade  (score 47)
- **H** 441,745.9 US$ Million — FY2025-26 (TRADESTAT: Merchandise trade; monthly) — ~5 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 96.3665 — 2026-07-17 (RBI: USD/INR spot rate; daily) — ~91 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 698,100.0 US$M — June 2025 (MoSPI: Forex reserves; monthly) — ~14 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 675,157.0 US$M — 2026-07-10 (RBI: Forex reserves; weekly) — ~13 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 451,070.0 US$ Million — FY2025-26 (Dept. of Commerce: TIA Portal Merchandise Exports; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 441,780.0 US$ Million — FY2025-26 (PIB: PIB Merchandise Exports; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini+mistral]
- $25.2 billion — FY2025-26 (RBI: Current-account deficit; quarterly) — ~1 newer release(s), 5 figure(s) from this source [gemini+mistral]
- 84.68 — FY2024-25 (RBI: USD/INR FY average; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- $1.84 trillion — FY2025-26 (NITI Aayog: Blended goods+services trade; quarterly) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 1,403.8 US$ million (PLI Specialty Steel 1.2) — FY24-25 (DPIIT: PLI scheme funding; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### nine-ministries-one-list-every-company  (score 44)
- **H** ₹11,198 crore — 23 Jan 2026 (DPIIT: PLI 8 of 14: White Goods; monthly) — ~7 newer release(s), 3 figure(s) from this source [gemini+mistral]
- **H** ₹44,326 crore — as of 31 Mar 2026 (Ministry of Heavy Industries: PLI 4 of 14: Automobiles and Auto Components; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** ₹26,320 crore — as of 30 Jun 2026 (Ministry of Steel: PLI 6 of 14: Specialty Steel; monthly) — ~2 newer release(s), 2 figure(s) from this source [gemini+mistral]
- ₹319 crore — FY22 (Ministry of Civil Aviation: PLI 13 of 14: Drones and Drone Components; annual) — ~4 newer release(s), 2 figure(s) from this source [gemini]
- 49 MTPA cumulative capacity — 13th Round (15 Jan 2026) (Ministry of Coal: Coal Mine Auction Capacity; quarterly) — ~1 newer release(s), 5 figure(s) from this source [mistral]

### five-year-synthesis-trade-currency  (score 42)
- **H** $188.9bn — FY2024-25 (RBI: Services trade balance; monthly) — ~17 newer release(s), 5 figure(s) from this source [gemini]
- **H** nearly six times — FY2021-22 to FY2025-26 (DGCI&S: Merchandise trade; monthly) — ~5 newer release(s), 11 figure(s) from this source [gemini]
- 96.3 — early October 2026 (RBI / market data: USD-INR spot rate; daily) — ~9 newer release(s), 3 figure(s) from this source [gemini]
- $734.61bn — week ended 2 October 2026 (RBI: Weekly Statistical Supplement; weekly) — ~1 newer release(s), 6 figure(s) from this source [gemini+mistral]
- $216.6 billion — 2025-26 (RBI: Balance of payments; quarterly) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 74.50 INR/USD (FY2021-22), 84.68 INR/USD (FY2024-25) — FY2021-22 to FY2024-25 (RBI (via repo's rbi_usd_inr_exchange_rate): Average INR/USD exchange rate; annual) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### indias-semaglutide-patent-cliff-26  (score 42)
- **H** 33% — March 2026 (CNBC, Bloomberg, Seeking Alpha and eMarketer: India GLP-1 category share; monthly) — ~5 newer release(s), 6 figure(s) from this source [gemini+mistral]
- **H** ₹1,300–4,200 — March 2026 (malaymail.com (Reuters wire): Monthly generic price range; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini]
- Eli Lilly: 61% (Feb 2026) → 56% (Mar 2026); tirzepatide: 71% → 64% — February 2026 vs. March 2026 (CNBC, Bloomberg, Seeking Alpha, eMarketer: India GLP-1 market share by brand; monthly) — ~5 newer release(s), 1 figure(s) from this source [mistral]
- 25% (Novo Nordisk branded share, March 2026) — March 2026 (Article text (CNBC, Bloomberg, Seeking Alpha, eMarketer): India GLP-1 market share by brand; monthly) — ~5 newer release(s), 2 figure(s) from this source [mistral]
- 89.8 million adults — 2024 (MoSPI: Adults living with diabetes; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 10.5% adult diabetes prevalence (2024) — 2024 (Article text (malaymail.com/Reuters): Diabetes prevalence rate (India); annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### kpler-and-vortexa-track-every-barrel  (score 41)
- **H** 0.07% — 2022 (Invest India / USDA: Biodiesel blend rate; annual) — ~3 newer release(s), 14 figure(s) from this source [gemini+mistral]
- **H** ~$451,000/day — mid-September 2026 (Affinity Shipbrokers / Hellenic Shipping News: VLCC tanker earnings; weekly) — ~3 newer release(s), 3 figure(s) from this source [gemini+mistral]
- **H** 2.58–2.70M bpd — June 2026 (Kpler / Reuters / LSEG: India's Russian crude imports; monthly) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** 63 — mid-2026 (FSSAI: RUCO scheme enrolment; monthly) — ~2 newer release(s), 1 figure(s) from this source [gemini]
- 1.37 million tonnes — January–May 2026 (China customs: China UCO exports; monthly) — ~3 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 600 million litres — 2022 (Invest India: Biodiesel plant capacity; annual) — ~3 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 1,648 shipments — March 2023–February 2024 (Volza / Seair: India UCO exports (HSN 15180039); annual) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 1.09 million bpd (Jan), 1.04 million bpd (Feb), 2.13 million bpd (May), 2.58–2.70 million bpd (Jun) — January–June 2026 (Kpler / LSEG (via Reuters, Business Standard, Yahoo Finance): India's Russian crude imports by month; monthly) — ~2 newer release(s), 6 figure(s) from this source [mistral]
- 4–5% above prior year — early 2026 (Vortexa: Seaborne clean product exports growth; quarterly) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indian-it-in-ai-era  (score 40)
- **H** 27% — 2025 (WTO: quarterly and monthly commercial services statistics; monthly) — ~8 newer release(s), 2 figure(s) from this source [gemini]
- **H** $216.6bn — FY2025-26 (Reserve Bank of India: Developments in India's Balance of Payments; quarterly) — ~5 newer release(s), 15 figure(s) from this source [gemini]
- 21% — January 2026 (Naukri JobSpeak: BPO/ITES hiring index; monthly) — ~7 newer release(s), 1 figure(s) from this source [mistral]
- 2,117 — FY2025-26 (Zinnov–NASSCOM: India GCC Landscape; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini]

### india-exports-worlds-coco-peat-its-own  (score 39)
- **H** 62.9% — first four months of FY26 (Coir Board: Coir and coir-product exports; monthly) — ~13 newer release(s), 4 figure(s) from this source [gemini+mistral]
- **H** 2.6 tonnes — FY2023-24 (PIB / ministry: Kashmir saffron production; annual) — ~2 newer release(s), 2 figure(s) from this source [gemini]
- **H** 8.0 MT (FY2010-11) → 2.6 MT (FY2023-24) — FY2010-11 to FY2023-24 (Jammu & Kashmir Agriculture Production Department (via National Geographic, Dialogue Earth, Greater Kashmir): Saffron production (annual); annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- **H** $455 million — FY25 (Coir Board: Coir and coir-manufactured-product exports; annual) — ~1 newer release(s), 6 figure(s) from this source [gemini+mistral]
- 16 tonnes — 1996 (Frontline (The Hindu) / official-data series: saffron production; annual) — ~29 newer release(s), 1 figure(s) from this source [gemini]

### indias-cotton-yield-fell-from-566-kg-to  (score 39)
- **H** 566 kilograms of lint a hectare — 2013-14 (USDA / industry data (via secondary coverage): India cotton lint yield national peak; annual) — ~12 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** 436 to under 450 kg/ha — 2024-25 (secondary coverage / USDA: India cotton lint yield estimate; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 89.5 kg N/ha — 2003-04 (FAO country study) (FAO country study (via blog's earlier reporting): India cotton nitrogen fertilizer use; annual) — ~21 newer release(s), 1 figure(s) from this source [mistral]
- 348 lakh bales — 2025-26 (Confederation of Indian Textile Industry (CITI): Cotton consumption estimate; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini+mistral]
- $800 million — 2020 (Review paper: Raw cotton export earnings; annual) — ~5 newer release(s), 2 figure(s) from this source [gemini]
- 285 kg/ha — 2001-2025 (CEIC Data: Maharashtra average lint yield; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 337 lakh bales — July 2026 (Cotton Association of India (CAI): Crop estimate; monthly) — ~1 newer release(s), 8 figure(s) from this source [gemini]

### one-refinery-flipped-nigeria-from  (score 37)
- **H** 62% — January-February 2026 (OilPrice.com: Nigeria's fuel-import reversal, as Dangote ramped; monthly) — ~6 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 445,000 bpd — 2018 (Nigerian National Petroleum Corporation: State refineries installed capacity; annual) — ~7 newer release(s), 3 figure(s) from this source [gemini]
- 37% (2017) and 14% (2018) — 2017 and 2018 (Ricardo Alves Silva and Rosário Paixão (Miranda Law Firm): Nigeria's state refineries utilisation rate; annual) — ~7 newer release(s), 1 figure(s) from this source [mistral]
- -54% — Q1 2025 (OilPrice.com: Nigeria's fuel-import reversal, as Dangote ramped; quarterly) — ~5 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 466,000 metric tonnes — June 2026 (Economic Confidential: Dangote jet-fuel exports; monthly) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]

### a-slice-of-apple-costs-about-1700-slice  (score 34)
- **H** ~$780,000 — early Aug 2026 (CNBC: Berkshire Hathaway share price; daily) — ~67 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** 23.15 crore demat accounts — June 2026 (PIB / ministry: Total Number of Demat Accounts in India; monthly) — ~2 newer release(s), 2 figure(s) from this source [gemini+mistral]
- **H** ₹29,87,880 crore — July 2026 (NPCI: UPI Product Statistics; monthly) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- ₹11,00,000 — 11 Aug 2026 (Screener.in: Company stock price; daily) — ~66 newer release(s), 33 figure(s) from this source [gemini+mistral]
- ₹589 — 1H 2025 (Worldline: India Digital Payments Report; half-yearly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### indias-food-processing-story-pli-scheme  (score 33)
- **H** 3.39 lakh — June 2026 (MoFPI: Production Linked Incentive Scheme for Food Processing Industries (PLISFPI) Progress; monthly) — ~2 newer release(s), 6 figure(s) from this source [gemini+mistral]
- 9.32% — April–October FY2023-24 (DGCI&S: Agricultural and Processed Food Exports Growth; monthly) — ~34 newer release(s), 2 figure(s) from this source [gemini+mistral]
- ₹1,15,596 crore — April 2000 to June 2025 (DPIIT / IBEF: FDI into Food Processing Sector; monthly) — ~14 newer release(s), 2 figure(s) from this source [gemini+mistral]
- US$15,423 million (FY2022-23) to US$13,985 million (FY2023-24) — April–October FY2023-24 (The Tribune: Export earnings decline; quarterly) — ~10 newer release(s), 2 figure(s) from this source [mistral]
- 1.18 US$ billion — Q1 FY26 (DGCI&S: Buffalo Meat, Dairy & Poultry Exports; quarterly) — ~4 newer release(s), 1 figure(s) from this source [gemini]
- US$1.18 billion (Q1 FY26), +17% YoY — Q1 FY2026 (Eastern Mirror Nagaland / Rural Voice: Top agricultural export category (Buffalo meat, dairy & poultry); quarterly) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- US$12.5 billion — FY25 (IBEF: Processed Food Exports; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 12.95 US$ billion — FY25 (DGCI&S: Rice Exports; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]

### nature-versus-nurture-indias-fertiliser  (score 32)
- **H** 120% — Apr-Nov FY25-26 (DGCI&S: urea imports growth y/y; monthly) — ~9 newer release(s), 3 figure(s) from this source [gemini+mistral]
- **H** ~$20/MMBtu — Mar-Apr 2026 (PPAC: crisis-level spot LNG; monthly) — ~4 newer release(s), 4 figure(s) from this source [gemini]
- $7.7 billion — 2024 (Department of Fertilizers / UN COMTRADE: Fertiliser Trade Deficit; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 25.89 crore — as of July 2026 (Ministry of Agriculture & Farmers Welfare: Cumulative Soil Health Cards; live) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### indias-ethanol-surplus-isnt-going-to  (score 31)
- **H** $0.449/L — 7 Jan 2026 (USGC: Ethanol Market and Pricing Data; weekly) — ~39 newer release(s), 5 figure(s) from this source [gemini+mistral]
- ₹95/$1 — August 2026 (Federal Reserve H.10 / market data: USD/INR reference rate; daily) — ~46 newer release(s), 1 figure(s) from this source [gemini+mistral]
- $0.616/gallon ($0.81/L) spread; >2x prior year — 2025–2026 (US Grains & Bioproducts Council (USGC): Weekly Ethanol and Co-Product Pricing Report; weekly) — ~39 newer release(s), 1 figure(s) from this source [mistral]
- $815 per tonne — Q1 2026 (IMARC: regional bio-ethanol price index; quarterly) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]

### five-years-and-25000-crore-later-china  (score 30)
- **H** 0 of 3 — March 2026 (PIB / ministry: Bulk Drug Parks status; monthly) — ~5 newer release(s), 12 figure(s) from this source [gemini+mistral]
- **H** 73.71% — FY2024-25 (PIB / ministry: API/bulk-drug/intermediate imports by origin; annual) — ~1 newer release(s), 5 figure(s) from this source [gemini+mistral]
- **H** US$3,204.70mn — FY2024-25 (PIB (DGCIS data): API/bulk-drug/intermediate imports by origin; annual) — ~1 newer release(s), 5 figure(s) from this source [gemini]
- **H** US$4,350,000,000 — FY2024-25 (PIB / DGCIS: API/bulk-drug/intermediate imports; annual) — ~1 newer release(s), 9 figure(s) from this source [mistral]
- ₹4,56,246 crore — FY2022-23 (MoSPI: National Accounts Statistics; annual) — ~3 newer release(s), 3 figure(s) from this source [gemini+mistral]
- US$23,500,000,000 — FY2023-24 (National Accounts Statistics 2024: Domestic consumption of finished drugs; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- 1.8% (value) / 9.3% (volume) — FY2024-25 (pharmabiz.com (secondary): Bulk-drug import growth; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### one-nation-one-ration-card-doesnt-move  (score 30)
- **H** 604.02 lakh tonnes — 1 April 2026 (PIB / ministry: FCI central-pool stock (rice and wheat combined); monthly) — ~5 newer release(s), 4 figure(s) from this source [gemini+mistral]
- under 0.5 million transactions a month — 2024 (IIM Ahmedabad: PDS portability monthly transactions; monthly) — ~20 newer release(s), 2 figure(s) from this source [gemini]
- 19.97% — one month in ESY 2024-25 (Ministry of Petroleum & Natural Gas: Ethanol blending monthly peak; monthly) — ~10 newer release(s), 1 figure(s) from this source [gemini]
- 81.35 crore — Census 2011 (Census: Census 2011 population shares; multi-year) — ~2 newer release(s), 1 figure(s) from this source [gemini]
- 8.8% CAGR — FY2022–FY2025 (Economic Survey 2025-26 (Ministry of Finance): Maize production growth rate; annual) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### bio-fertiliser-and-green-credits  (score 28)
- **H** ₹1,500/MT — FY2024-25 (Department of Fertilizers: Market Development Assistance (MDA) scheme; monthly) — ~17 newer release(s), 1 figure(s) from this source [gemini]
- **H** 42,800 tonnes — FY2024-25 (PPAC / MoPNG / PNGRB: India's CBG Sector — Situation Report; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 7 notifications — Nov 2023–Feb 2026 (Department of Agriculture & Farmers Welfare (DA&FW): GOBARdhan Gazette notifications (S.O. 4918(E) to S.O. 1018(E)); monthly) — ~6 newer release(s), 1 figure(s) from this source [mistral]
- 1,620 tonnes/day — July 2026 (PPAC / MoPNG / PNGRB: CBG Customer Willingness-to-Pay; monthly) — ~1 newer release(s), 5 figure(s) from this source [gemini+mistral]

### a-17-rural-pay-rise-that-nobody-received  (score 27)
- **H** 4.3% — March 2026 (AlphaEcon analysis: Break-adjusted rural wage growth estimate; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 134 points — June 2025 (Ministry of Labour and Employment: CPI-AL index level; monthly) — ~14 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 2.9 per cent — May 2026 (Labour Bureau: State-level inflation in newly added regions; monthly) — ~3 newer release(s), 15 figure(s) from this source [gemini+mistral]
- 30 crore (Apr 2026), 43 crore (May 2026) — Apr-May 2026 (VB-G RAM G scheme data: Person-days approved; monthly) — ~3 newer release(s), 1 figure(s) from this source [mistral]

### from-fuel-to-fibre-indias-textile  (score 25)
- **H** $1.45bn exports (FY17), $2.84bn exports (FY22), $277M deficit (FY17), $384–532M surplus (FY22–24) — FY17, FY22, FY22–24 (Ministry of Textiles (eBooklet), separate Fuel-to-Fibre analysis: 207-HSN-code technical textiles trade balance and exports; annual) — ~4 newer release(s), 1 figure(s) from this source [mistral]
- **H** $2.85 billion — FY2024-25 (Ministry of Textiles: 207-HSN-code technical textiles trade table; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini]
- 1,150 acres — Feb 2026 (PIB / ministry: PM MITRA progress release; monthly) — ~6 newer release(s), 10 figure(s) from this source [gemini+mistral]
- $261M exports, $806M imports, −$545M trade balance (FY22) — FY22 (Ministry of Commerce and Industry: Mobiltech segment trade data (207-HSN codes); annual) — ~4 newer release(s), 1 figure(s) from this source [mistral]

### diesel-doesnt-move-cpi-it-moves-40  (score 25)
- **H** >₹40 per litre — May 2026 (PPAC: Industry Consumption Report POL & NG; monthly) — ~3 newer release(s), 20 figure(s) from this source [gemini+mistral]
- **H** 7.09 ₹/km — July 2026 (ARAI / SIAM / OMC: Modelled running cost per kilometre, Delhi; monthly) — ~1 newer release(s), 1 figure(s) from this source [gemini]
- +11.0% — May 2026 (GSTN: Industry Consumption Report / e-way bills; monthly) — ~3 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 270.82 GW — April-May 2026 (PIB / ministry: Power supply position; monthly) — ~3 newer release(s), 1 figure(s) from this source [gemini+mistral]
- +5.3% — May 2026 (FADA: Industry Consumption Report / vehicle sales; monthly) — ~3 newer release(s), 2 figure(s) from this source [gemini]
- +4.5% — May 2026 (ipa.nic.in: Industry Consumption Report / port cargo; monthly) — ~3 newer release(s), 2 figure(s) from this source [gemini]
- 88.2% — FY2024-25 (PPAC: Snapshot of India’s Oil & Gas Data; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]

### dr-reddys-cut-its-semaglutide-guidance  (score 24)
- **H** 3.7% — 10 July 2026 (Business Standard: Share price; daily) — ~98 newer release(s), 1 figure(s) from this source [gemini+mistral]
- ₹1,275 — July 2026 (Investing.com: Share price; daily) — ~98 newer release(s), 1 figure(s) from this source [gemini]

### how-to-use-agri-commodity-tracker-india  (score 24)
- **H** 463,023 rows — 21 Jul to 24 Sep 2026 (data.gov.in: Agmarknet mandi prices; daily) — ~22 newer release(s), 15 figure(s) from this source [gemini+mistral]
- 605 ₹/quintal — 2026-09-24 (Agmarknet (via data.gov.in): APMC mandi price dataset (modal price); daily) — ~22 newer release(s), 19 figure(s) from this source [mistral]

### indias-coking-coal-import-problem-and  (score 24)
- **H** 5.5 MT — December 2025 (MoSPI: Thermal power plant coal blending imports; monthly) — ~8 newer release(s), 1 figure(s) from this source [gemini]
- **H** 1,047.5 million tonnes — FY2024-25 (PIB / ministry: Ministry of Coal's Year End Review; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 5% (FY2024-25), 7% (FY2025-26) — FY2024-25, FY2025-26 (Ministry of Power: SAMARTH Mission biomass co-firing mandate; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 3% (FY2024-25), 7% (FY2025-26) — FY2024-25, FY2025-26 (Commission for Air Quality Management (CAQM): Delhi-NCR biomass co-firing mandate; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 43–46% — FY2024-25, FY2025-26 (DGCI&S TradeStat: Country-wise coking coal import share; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-renewable-energy-certificates  (score 24)
- **H** ₹2,300, ₹115, ₹380 — mid-2026 (IEX session reports and trade-press coverage: REC session data; monthly) — ~2 newer release(s), 2 figure(s) from this source [gemini]
- **H** ₹2,300 (Feb 2022), ₹115 (Aug 2024), ~₹380 (mid-2026) — Feb 2022, Aug 2024, mid-2026 (IEX session data (via Mercom India/SolarQuarter): IEX REC trading session prices (Non-Solar/Solar pre-2022, unified post-2022); live) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- **H** ₹115 (Aug 2024) — 14/28 Aug 2024 (IEX session reports: REC trading session prices (unified); live) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 1.22 crore certificates — 2015 (REC Registry: REC Registry data; annual) — ~10 newer release(s), 3 figure(s) from this source [gemini+mistral]
- FY2023-24 — FY2023-24 (CPCB: Tyre/Rubber Waste EPR Certificate launch; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- ₹380 / ₹376 — Jul 2026 (IEX: IEX session data; monthly) — ~1 newer release(s), 11 figure(s) from this source [gemini+mistral]
- ~1.8 lakh certificates — 2024 (BEE / CERC: PAT scheme; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- ₹316 (Dec 2024) — 11/26 Dec 2024 (Mercom India/SolarQuarter: REC trading session prices (unified); live) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- Jun 2025 (voluntary) — Jun 2025 (CERC/BEE: CCTS voluntary trading; live) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### ai-is-not-taking-indias-offshore-work  (score 23)
- 50,000 calls a day — February 2024 (I4C: Cyber-fraud helpline volume; daily) — ~960 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 1.4-1.6 lakh a month — October 2025 (CPGRAMS: Public grievances workload; monthly) — ~10 newer release(s), 1 figure(s) from this source [gemini]
- 24.6 lakh — February 2026 (Income Tax Department: Unprocessed income-tax returns; monthly) — ~6 newer release(s), 1 figure(s) from this source [gemini]
- 0.10m — 2022 (AIBEST: Offshore services workforce; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini]
- 27.0% — Q1 2026 (Genpact: Advanced Technology Solutions revenue share; quarterly) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 0.50m — Q1 2026 (ABSL: Offshore services workforce; quarterly) — ~1 newer release(s), 1 figure(s) from this source [gemini]

### announced-vs-delivered-three-indian  (score 23)
- ₹16,358 crore (collected), ₹16,290 crore (target) — April–August 2025 (Deccan Chronicle, Tamil Nadu government white paper: Karnataka Excise Revenue Collection (Partial Year); monthly) — ~12 newer release(s), 1 figure(s) from this source [mistral]
- ₹36,492 crore — Apr 2025 - Feb 2026 (Commercial Taxes/Excise Department, Government of Karnataka: Karnataka Excise Collection; monthly) — ~6 newer release(s), 1 figure(s) from this source [gemini+mistral]
- $3.04 bn — 2022-23 (MPEDA / Government of Andhra Pradesh: Aqua and shrimp export share; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini]
- ~80% (shrimp), 37.7% (marine), ~$3.04bn (2022-23) — 2022-23 (GFST, article estimate: Aqua/Shrimp Export Share; annual) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- 86,489 — mid-2026 (UP EV Subsidy Portal: EV subsidy applications approved; monthly) — ~2 newer release(s), 7 figure(s) from this source [gemini+mistral]
- ~18% — mid-2026 (Transport Department, Government of Uttar Pradesh: UP's share of national EV sales; monthly) — ~2 newer release(s), 2 figure(s) from this source [gemini]
- ₹38,525 crore — FY2024-25 (PRS Legislative Research: Karnataka Budget Excise Target; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini]

### fci-grain-flow-procurement-storage  (score 22)
- **H** 476.85 LMT — 1 January 2025 (DFPD: Central-pool stock levels; monthly) — ~20 newer release(s), 10 figure(s) from this source [gemini+mistral]
- **H** ₹1.99 lakh crore — FY25 (MoF / DFPD: Food subsidy released; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 544.8 LMT — 2024-25 (MoSPI / Economic Survey: Rice-terms procurement; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### indias-oil-fields-are-running-down-3696  (score 22)
- **H** 11.8% — FY2024-25 (PPAC: Snapshot of India's Oil & Gas Data; monthly) — ~17 newer release(s), 7 figure(s) from this source [gemini+mistral]
- **H** 36.96 to 28.70 MMT — FY2024-25 (DGH: India's Hydrocarbon Outlook; annual) — ~1 newer release(s), 42 figure(s) from this source [gemini+mistral]
- 267.5 MMT — FY2024-25 (PPAC: Snapshot of India's Oil & Gas Data; annual) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### india-hit-e20-on-maize-and-rice-not  (score 22)
- **H** 20% — ESY 2025-26 (ChiniMandi / BioEnergy Times (trade reporting): Ethanol blending rate (monthly supply figures); monthly) — ~5 newer release(s), 1 figure(s) from this source [mistral]
- **H** 6.2% — ESY 2022-23 (ChiniMandi / BioEnergy Times: Maize Share of Ethanol Allocation; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini]
- 515 crore litres supplied (vs. 1,059 crore litres contracted) — Apr-Sep 2025 (half-year) (All India Distillers’ Association (via Business Today): Ethanol supply vs. contracted volume; half-yearly) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### not-drop-out-ethanols-zero-liquid  (score 22)
- 6,561 MLD — October 2025 (National Mission for Clean Ganga (NMCG): Namami Gange Project Portfolio; monthly) — ~10 newer release(s), 5 figure(s) from this source [gemini+mistral]
- 392 distilleries — 2019-20 (All India Distillers Association (AIDA): Distillery Count and Capacity; annual) — ~6 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 26 projects — calendar 2022 (National Mission for Clean Ganga (NMCG): Namami Gange Annual Additions; annual) — ~3 newer release(s), 2 figure(s) from this source [gemini]
- 70.1% collection rate; 216,000 MLD treatment capacity — 2022 (China National Bureau of Statistics (implied): China wastewater treatment capacity; annual) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- 80.7% population connected (EU) — 2023 (Eurostat: EU wastewater treatment coverage; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- ₹35,970 crore — August 2026 (Ministry of Jal Shakti: Namami Gange Mission-II Status; monthly) — ~1 newer release(s), 5 figure(s) from this source [gemini+mistral]
- 56% global wastewater treatment — 2024 (UN-Water/WHO/UN-Habitat (SDG 6 progress report): Global wastewater treatment progress; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### jan-aushadhi-sells-2439-products-heres  (score 21)
- **H** 2,439 products — as on 16 September 2026 (PMBI: PMBI Product List; daily) — ~30 newer release(s), 27 figure(s) from this source [gemini]
- 43.45% — FY2023-24 (DGCI&S: Pharma import statistics; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini]
- 98.02% — FY2024-25 (PIB (Press Information Bureau): China-dependency for Ciprofloxacin API imports; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-factory-intentions-20012024-how  (score 21)
- **H** 55,781 Part A memoranda — January 2001 to August 2024 (DPIIT: List of IEM Filed; monthly) — ~24 newer release(s), 35 figure(s) from this source [gemini+mistral]
- 1,219 — 2023 (DPIIT: IEM Register (parsed from monthly lists); annual) — ~2 newer release(s), 3 figure(s) from this source [mistral]
- ₹1,000 — as on 1 October 2025 (DPIIT: National Single Window System IEM service fee; live) — ~1 newer release(s), 2 figure(s) from this source [gemini]

### india-grain-cultivation-fci-storage  (score 21)
- **H** 200 LMT — Nov 2024 (DFPD: Foodgrain Bulletin; monthly) — ~21 newer release(s), 11 figure(s) from this source [gemini+mistral]
- **H** 348 FPOs — 24-02-2025 (SFAC: 10,000-FPO registry; live) — ~1 newer release(s), 13 figure(s) from this source [gemini+mistral]

### beyond-pump-what-upi-fee-would-cost  (score 21)
- **H** 43.7% — July 2025 (NPCI: NPCI merchant-category classification data; monthly) — ~13 newer release(s), 40 figure(s) from this source [gemini+mistral]
- **H** 25.8% — FY2025-26 H1 (PPAC: PPAC Ready Reckoner; half-yearly) — ~1 newer release(s), 2 figure(s) from this source [gemini]

### can-rupee-trade-actually-offset  (score 21)
- **H** 156 accounts — Feb 2026 (RBI: Special Rupee Vostro Account programme status; monthly) — ~6 newer release(s), 3 figure(s) from this source [gemini+mistral]
- ~5.4% — 2026 YTD (exchange-rates.org: SAR/INR spot-rate range; daily) — ~3 newer release(s), 5 figure(s) from this source [gemini+mistral]

### indias-gas-pipelines-run-at-half  (score 21)
- **H** 91.46% — FY2024-25 (Oil India: Numaligarh–Siliguri crude line utilisation; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- **H** 41% — FY2025 (IEEFA: capacity-weighted gas-pipeline utilisation estimate; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 5.67% — 2016-17 (Industry commentary / Stanford / Oil & Gas Journal: Kochi LNG terminal utilisation; annual) — ~9 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 14,800 km — late 2025 (PNGRB: multi-product common-carrier pipelines authorised length; monthly) — ~8 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 96.924 million tonnes — FY2024-25 (Indian Oil: pipeline throughput liquids; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 26.90 million tonnes — FY2024-25 (HPCL: pipeline throughput; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 4.478 million tonnes — FY2024-25 (GAIL: LPG pipelines throughput; annual) — ~1 newer release(s), 5 figure(s) from this source [gemini+mistral]

### indian-railways-98-to-earn-100-business  (score 21)
- **H** 98.90 — FY2024-25 (PRS Legislative Research / Railways' Demand for Grants; CAG: Indian Railways' Operating Ratio; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini]
- **H** 98.43% (FY2025-26), 98.9% (FY2024-25 RE) — FY2024-25 (RE), FY2025-26 (BE) (PRS Legislative Research: Railways' Demand for Grants; annual) — ~1 newer release(s), 2 figure(s) from this source [mistral]
- ₹26,388 crore — 2019-20 (Comptroller and Auditor General: CAG Audit Report; annual) — ~6 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 100%+ (hypothetical) — 2018-19, 2019-20, 2020-21 (CAG: Audit Reports; annual) — ~5 newer release(s), 1 figure(s) from this source [mistral]
- 102 trains, 2 crore passengers, 92%+ utilisation — FY2023-24 (Railway Ministry (RTI response): Vande Bharat Operations; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- 91% — 2009 to 2019 (NITI Aayog / PRS: Freight Rates and Passenger Fares Growth; multi-year) — ~1 newer release(s), 2 figure(s) from this source [gemini]
- 3x (freight vs. passenger charges), 91% (freight growth), 28% (passenger growth) — 2009-2019, 2018-19 (NITI Aayog: 2023 Analysis; multi-year) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-factory-intentions-20012024-how_0101046393  (score 20)
- **H** 55,781 — January 2001 to August 2024 (DPIIT: List of IEM Filed; monthly) — ~24 newer release(s), 21 figure(s) from this source [gemini+mistral]
- 7,488 — 2017 to 2024 (Ministry of Corporate Affairs / LEI register: Company master data and LEI register; live) — ~1 newer release(s), 2 figure(s) from this source [gemini]
- 4,604 — 2017 to 2024 (Ministry of Corporate Affairs: Company master data; live) — ~1 newer release(s), 2 figure(s) from this source [gemini]

### how-india-actually-plans-to-hit-net  (score 20)
- **H** 52.57% — February 2026 (PIB / ministry: Nationally Determined Contribution tracking; monthly) — ~6 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 46.8% — November 2024 (Economic Survey 2024-25: Energy Statistics; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 31 January 2025 — 31 January 2025 (MoSPI: Economic Survey 2024-25; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-445-billion-spice-export-book-is  (score 20)
- **H** $945.7mn — FY26 (DGCI&S: DGCI&S 8-digit trade-data analysis; monthly) — ~5 newer release(s), 8 figure(s) from this source [gemini+mistral]
- **H** $4.45 billion — FY2024-25 (PIB / ministry: Trading Aromas: The Rise of the Spice Economy; annual) — ~1 newer release(s), 6 figure(s) from this source [gemini+mistral]
- $1,508.94 million — FY2023-24 (PIB: Trading Aromas: The Rise of the Spice Economy (chilli exports); annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]

### foreign-capital-found-indias-hospitals  (score 20)
- **H** 1.59 hospital beds per 1,000 population — 2021 (World Bank / WHO: SH.MED.BEDS.ZS; annual) — ~4 newer release(s), 3 figure(s) from this source [gemini+mistral]
- **H** 4.3% — CY2023 (DPIIT: FDI Equity Inflows; annual) — ~2 newer release(s), 11 figure(s) from this source [gemini+mistral]
- $13.23 billion — April 2000 to June 2026 (DPIIT: FDI Equity Inflows fact sheet; monthly) — ~2 newer release(s), 4 figure(s) from this source [gemini+mistral]

### india-sells-world-about-third-of-its  (score 20)
- **H** US$535.9 million — 2024–25 (Spices Board / DGCI&S: Item-wise export of spices from India; annual) — ~1 newer release(s), 21 figure(s) from this source [gemini+mistral]
- ₹886 crore — FY22 (CARE Ratings: Annual revenue; annual) — ~5 newer release(s), 1 figure(s) from this source [mistral]
- ₹533 crore — FY24 (CRISIL: Annual revenue; annual) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- ₹1,940 cr — FY24 (Acuité: Company revenue; annual) — ~2 newer release(s), 2 figure(s) from this source [gemini]
- ₹2,672 crore — FY25 (Company filings aggregator: Annual revenue; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- ₹2,672 cr — FY25 (CRISIL / Company filings: Company revenue; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini]
- ₹713 crore — FY26 (Business Standard: Annual revenue; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 52,000 tonnes — 2024 (UN Comtrade (compiled by trade-data provider): Pepper import data; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 55% (Sri Lanka share), 20,830 tonnes (exported pepper) — 2024 (imports), 2024–25 (exports) (UN Comtrade / Spices Board: Pepper trade data; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- US$56 million — 2024 (US Commerce Department: Petition initiation data; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-irrigation-system-recovered-96  (score 20)
- **H** ~22M ha — 2024-25 (PIB / ministry: Irrigation potential created and utilised; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- **H** 57.72% — as on 8 May 2026 (PIB / ministry: Accelerated Irrigation Benefits Programme (AIBP); live) — ~1 newer release(s), 5 figure(s) from this source [gemini+mistral]
- 20% — 2013-14 (Central Water Commission: Financial Performance of India's Irrigation Sector; annual) — ~12 newer release(s), 3 figure(s) from this source [gemini+mistral]
- ₹64,407 crore — as on August 2025 (PIB / ministry: PMKSY fund release; monthly) — ~12 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 2017-18 — 2017-18 (Central Water Commission (CWC): Financial recovery rate of public irrigation (last published data); multi-year) — ~1 newer release(s), 6 figure(s) from this source [mistral]
- 20 states — 1983-84 to 2019-20 (Bathla, Kannan & Das (2024): Public capital formation in irrigation; multi-year) — ~1 newer release(s), 3 figure(s) from this source [mistral]

### india-grows-soybean-exports-meal-leads  (score 20)
- ₹3,800–4,000/quintal — Kharif 2025 (Department of Agriculture / Mandi data: Soybean mandi prices; daily) — ~350 newer release(s), 1 figure(s) from this source [gemini]
- 19.5 lakh tonnes — October 2023-June 2024 (SOPA / DGCI&S: Soybean meal exports; monthly) — ~26 newer release(s), 1 figure(s) from this source [gemini]
- 1.62 lakh tonnes — November 2025 (SEA / DGCI&S: Oilmeal exports; monthly) — ~9 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 21 lakh tonnes — 2023-24 (SOPA / DGCI&S: Soybean meal exports; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini]

### india-has-132-compressed-biogas-plants  (score 19)
- **H** 132 CBG plants — as of January 2026 (MoPNG: Commissioned CBG plants under SATAT; monthly) — ~7 newer release(s), 4 figure(s) from this source [gemini+mistral]
- about 210 CBG plants — as of June 2026 (Unified GOBARdhan Portal: Commissioned CBG plants; live) — ~1 newer release(s), 1 figure(s) from this source [gemini]

### india-imports-283000-tonnes-of-almonds  (score 19)
- **H** 283,000 tonnes — calendar 2024 (UN Comtrade / World Bank WITS: HS 080211 + 080212 import volume; annual) — ~1 newer release(s), 10 figure(s) from this source [gemini+mistral]
- **H** 4,100 tonnes — Calendar year 2024 (USDA FAS: India domestic almond production; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini]
- ₹99.82/USD — March 2026 (Business Standard (unspecified source): INR/USD exchange rate; daily) — ~199 newer release(s), 1 figure(s) from this source [mistral]
- ₹96/USD — early October 2026 (RBI (reference-rate data): INR/USD exchange rate; daily) — ~11 newer release(s), 4 figure(s) from this source [mistral]
- 248,000–260,000 tonnes (fiscal year) — Apr–Mar (fiscal year) (DGCI&S (DGCIS-derived): Fiscal-year import volume (product weight); annual) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### delhis-smog-towers-failed-test-44-year  (score 18)
- **H** 87 days — 1 Oct 2025 to 28 Feb 2026 (CPCB: Continuous Ambient Air Quality Monitoring Station data; daily) — ~230 newer release(s), 6 figure(s) from this source [gemini+mistral]

### how-to-use-fci-warehouse-mspvsmsv-grain  (score 18)
- **H** 92% — 23 July 2026 (Agmarknet: mandi modal prices against MSP; daily) — ~85 newer release(s), 12 figure(s) from this source [gemini+mistral]

### india-is-piping-jet-fuel-to-five-new  (score 18)
- **H** 8.85 MT — calendar year 2024 (PPAC: ATF consumption; monthly) — ~20 newer release(s), 4 figure(s) from this source [gemini+mistral]

### indias-lock-imports-hit-19784-million  (score 18)
- **H** $197.84 Million — FY2024-25 (DGCI&S: HS 8301 import value; monthly) — ~17 newer release(s), 22 figure(s) from this source [gemini+mistral]

### brazil-pumps-e30-at-every-station  (score 18)
- **H** 30% — 1 August 2025 (ANP: Gasolina C mandatory blend; monthly) — ~13 newer release(s), 3 figure(s) from this source [gemini+mistral]

### india-fuel-retail-outlets-82k-geocoded  (score 18)
- **H** 5,665+ — March 2023 (PNGRB: CNG stations built out; quarterly) — ~13 newer release(s), 3 figure(s) from this source [gemini+mistral]

### green-energy-corridor-iii-is-15-times_01338283908  (score 17)
- **H** 26 of 44 GW — March 2026 (PIB / ministry: Green Energy Corridor Phases I and II; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 9,161 ckm — March 2025 (Ministry of Power: Green Energy Corridor Phase I; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 470 GWh — January to March 2026 (Ember: Inter-state grid renewable curtailment; quarterly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### indias-trade-balance-hsn-wise  (score 17)
- **H** -$147.5bn — FY2025-26 (DGCI&S: TRADESTAT Commodity-wise Export and Commodity-wise Import reports; monthly) — ~5 newer release(s), 11 figure(s) from this source [gemini+mistral]
- $734.6bn — week ended 2 October 2026 (RBI: RBI weekly data; weekly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- ₹233,829 crore — 2024 (DPIIT: Industrial Entrepreneur Memorandum (IEM) Part-A investment-intention data; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini]

### hsn-wise-historical-importexport-trends  (score 17)
- **H** +118.9% — FY2018-19 to FY2025-26 (DGCI&S: TRADESTAT Commodity-wise Import reports; monthly) — ~5 newer release(s), 40 figure(s) from this source [gemini]
- ₹65,979 crore (2021) to ₹233,829 crore (2024) — 2021 to 2024 (DPIIT: Industrial Entrepreneur Memorandum (Investment-intention data); annual) — ~2 newer release(s), 2 figure(s) from this source [mistral]

### india-leads-world-in-jute-and-ranks  (score 17)
- **H** 92.2 million kilograms — 2023-24 (IBEF: raw wool imports; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]
- ₹5,335 (2014-15), ₹5,650 (2025-26), ₹5,925 (2026-27) — 2014-15, 2025-26, 2026-27 (Tribune India, agrijob.in: Jute Minimum Support Price (MSP) historical and future; annual) — ~11 newer release(s), 1 figure(s) from this source [mistral]
- 97.6 lakh bales — 2021-22 (MoSPI: national raw jute output; annual) — ~4 newer release(s), 1 figure(s) from this source [gemini+mistral]
- $272.51 million — 2024 (Industry market-sizing report: Sustainable-fashion market value; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-tyre-waste-problem-and-crumb  (score 17)
- **H** ₹25,000–30,000 crore — FY24 (DGCI&S / Ministry of Commerce: petroleum bitumen annual import cost; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** 10 million tonnes — FY2024-25 (PPAC / industry sources: national petroleum bitumen consumption projection; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- ₹23.9 crore (9 months) — FY2026 (Jan-Sep) (Tinna Rubber & Infrastructure Ltd (company disclosure): EPR-credit revenue; quarterly) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- 35% (2022-23), 70% (2023-24), 100% (2024-25 onward) — 2022-23, 2023-24, 2024-25 onward (CPCB (Hazardous and Other Wastes Rules, 2022): EPR recycling obligations for waste tyres; annual) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- ₹23.9 crore — first nine months of FY2026 (Tinna Rubber & Infrastructure Limited: EPR-credit revenue; quarterly) — ~2 newer release(s), 1 figure(s) from this source [gemini]

### mrs-watanabe-traded-from-kitchen-table  (score 17)
- **H** 28.4% — FY2024-25 (NSE: Women as a share of registered investors by state / region; annual) — ~1 newer release(s), 11 figure(s) from this source [gemini+mistral]
- $9.1 billion — 2007 (Bloomberg Opinion: Yen Retail Trading data; annual) — ~18 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 150 million — March 2025 (SEBI / Depositories: Demat accounts count; monthly) — ~17 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 45% — FY2024-25 (Mutual fund industry data: Average lump-sum investments by gender; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 22% — FY2024-25 (Business Standard: SIP ticket size by gender; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### everyone-worries-about-who-pays-for  (score 17)
- 10,445 km — 1 Apr 2025 (PPAC: PPAC Data; monthly) — ~17 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 9,301 km — Jun–Sep 2025 (PPAC / ministry: Petroleum Product Pipelines; monthly) — ~11 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 34,803 km — as on 31 Mar 2026 (PNGRB: PNGRB Data Bank; monthly) — ~5 newer release(s), 7 figure(s) from this source [gemini]

### india-built-offshore-insurance-hub-it  (score 16)
- **H** 94% — FY2024-25 (IFSCA: Quarterly Statistical Bulletin; quarterly) — ~5 newer release(s), 16 figure(s) from this source [gemini+mistral]
- 4% — FY2024-25 (IRDAI / GIC Re: Compulsory Cession; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini]

### biomass-power-at-night-dispatchable  (score 16)
- **H** 178% — between December 2019 and July 2026 (MNRE / CEA: state-wise installed renewable capacity table / Executive Summary on Power Sector; monthly) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- **H** 11,747.57 MW — as on 31 July 2026 (MNRE: state-wise installed renewable capacity table; monthly) — ~1 newer release(s), 9 figure(s) from this source [gemini+mistral]
- **H** +384% — Dec 2019 to Jul 2026 (CSEP / CEA / MNRE: state-wise installed renewable capacity table / Executive Summary on Power Sector; monthly) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 9,861 MW — Dec 2019 (Centre for Social and Economic Progress (CSEP) / CEA: Executive Summary on Power Sector (2019/2020); annual) — ~6 newer release(s), 1 figure(s) from this source [mistral]
- 58 million smart meters — 15 February 2026 (Business Standard / The Secretariat: Revamped Distribution Sector Scheme smart meter tracker; live) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### indias-coal-to-chemicals-menu-ranked-by  (score 16)
- **H** ₹2.77 lakh crore — FY2025 (PIB / ministry: Cabinet press release on Surface Coal/Lignite Gasification Projects; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- $1,420–1,450/t — early 2026 (global commodity reference: PE global reference price; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini+mistral]
- ₹1,800–1,900 a tonne — early-to-mid 2026 (CEIC: e-auction non-coking coal representative-price series; monthly) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]
- ₹9,000–11,600 a tonne — early-to-mid 2026 (trade-press reporting: imported sub-bituminous or thermal coal landed cost; monthly) — ~2 newer release(s), 1 figure(s) from this source [gemini]
- $428/t — early-to-mid 2026 (Intratec / ChemAnalyst / Argus Media: global commodity pricing aggregators; monthly) — ~2 newer release(s), 1 figure(s) from this source [gemini]
- >90% — early-to-mid 2026 (Intratec / ChemAnalyst / IMARC: import-dependence series; monthly) — ~2 newer release(s), 1 figure(s) from this source [gemini]

### chemical-import-substitution-analysis  (score 15)
- **H** $74.37 billion — FY2025-26 (DGCI&S: TradeStat EIDB; monthly) — ~5 newer release(s), 11 figure(s) from this source [gemini+mistral]

### endoscopes-never-made-indias-pli-list  (score 15)
- **H** $112mn — FY2025-26 (DGCI&S: TradeStat fetch; monthly) — ~5 newer release(s), 9 figure(s) from this source [gemini+mistral]

### 050-is-its-own-category-diving-into  (score 15)
- **H** 2,086 stocks — Jan 2023–Aug 2026 (NSE: weekly NSE data; weekly) — ~5 newer release(s), 12 figure(s) from this source [gemini]

### india-imports-60-of-its-cooking-gas  (score 15)
- **H** 20–24 litres/day — 2020 (CSIR-NCL: CSIR success-story page; annual) — ~5 newer release(s), 1 figure(s) from this source [gemini]

### city-gas-just-became-indias-largest-gas  (score 15)
- **H** 8,980 — as on 31 May 2026 (PNGRB: Snapshot of India’s Oil & Gas Data; monthly) — ~3 newer release(s), 3 figure(s) from this source [gemini+mistral]
- **H** 4,964 MMSCM — Q1 FY2026-27 (PPAC: Current-Year Sectoral Consumption workbook (NG-C); monthly) — ~2 newer release(s), 15 figure(s) from this source [gemini+mistral]

### lpgs-missing-number-7308-commission-and  (score 15)
- **H** 7.8% — 7 August 2026 (PPAC: Dealers/Distributors Commission page; monthly) — ~1 newer release(s), 8 figure(s) from this source [gemini+mistral]
- **H** 3.87% — FY2025-26 H1 (PPAC: Ready Reckoner FY2025-26 H1; half-yearly) — ~1 newer release(s), 4 figure(s) from this source [gemini]
- ₹942 — 7 August 2026 (PIB / ministry: Goodreturns LPG price tracker; daily) — ~70 newer release(s), 1 figure(s) from this source [gemini]
- 10.58 crore — July 2026 (PIB / ministry: Pradhan Mantri Ujjwala Yojana beneficiary count; monthly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 4.71 cylinders per beneficiary per year — FY2025-26 (NITI Aayog (April 2026 evaluation): PMUY per-consumer consumption; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- ₹12,000 crore per year — 2025-26 (Cabinet approval (reported by Business Standard and PIB, August 2025): PMUY subsidy budget; annual) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### mapping-indias-other-pipelines-every  (score 15)
- **H** 20,000 km — FY2024-25 (Indian Oil: annual report; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 258.1 MMTPA — April 2025 (PPAC: India refinery capacity; monthly) — ~16 newer release(s), 1 figure(s) from this source [gemini]
- 102.9% — first half of FY2024-25 (PPAC: crude processed vs nameplate refining capacity; half-yearly) — ~3 newer release(s), 1 figure(s) from this source [gemini]
- 26.90 million tonnes — FY2024-25 (HPCL: pipeline throughput; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 91.46% — FY2024-25 (Oil India: Numaligarh–Siliguri product line utilisation; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 4.478 million tonnes (throughput), 4.58 million tonnes (capacity) — FY2024-25 (GAIL: Annual Report (LPG Throughput and Capacity); annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-new-car-rules-count-every-ev-as  (score 15)
- 121.3 g CO₂/km — FY2021 (International Council on Clean Transportation (ICCT): India new passenger cars CO₂ emission average; annual) — ~5 newer release(s), 1 figure(s) from this source [mistral]
- ₹7,300 crore — FY2023 (BEE: CAFE-II penalties; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 113 g CO₂/km (MIDC) — FY2023 (Bureau of Energy Efficiency (BEE): CAFE-II fleet CO₂ emission target; annual) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- 2.0 (2020) → 1.67 (2021) → 1.33 (2022), capped at 7.5 g/km — 2020–2022 (European Commission: EU super-credits for ultra-low-emission vehicles; annual) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- 1.5 multiplier, capped at 10 g/mile — MY2023–2024 (US EPA: EV multiplier for greenhouse-gas standards; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-textile-import-export-strategy  (score 14)
- **H** Rs 15.76L Cr — FY2022-23 (MoSPI: Chemical & Petrochemical Sector Size Output; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini]
- **H** $22.1B — FY25 (DGCI&S: Chapter 39 Polymer Imports; annual) — ~1 newer release(s), 14 figure(s) from this source [gemini+mistral]
- 69,308 MT ('000) — 2024-25 (MoC&F: Installed Capacity & Utilization; annual) — ~1 newer release(s), 6 figure(s) from this source [gemini+mistral]
- 249.2 MMTPA — FY2025 (PPAC: Refining Capacity Ecosystem; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### effective-buying-power-china-comparison  (score 14)
- **H** +54.9% — January 2015 to 17 Jul 2026 (MoSPI / RBI: Nominal rate; monthly) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- **H** $734bn — 2 October 2026 (RBI: Foreign Exchange Reserves; weekly) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- **H** 11.9% — last twelve months (RBI: Nominal rate; monthly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- ~0.9% implied inflation (FY2025-26) — FY2025-26 (Apr 2025 – Jun 2025) (MoSPI (implied from NAS data): GDP deflator (implied inflation); quarterly) — ~4 newer release(s), 1 figure(s) from this source [mistral]
- 25% renminbi depreciation against the dollar since 2005 — 2005 – 2019 (approximate) (Brookings Institution: Renminbi exchange rate analysis; multi-year) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### india-polishes-worlds-diamonds-with_01635124664  (score 14)
- **H** ₹239.5 crore — 2024–25 (DGCI&S: HS 710510 imports; annual) — ~1 newer release(s), 10 figure(s) from this source [gemini+mistral]
- 1,238 million carats — 2021–22 (MoSPI: Indian Minerals Yearbook; annual) — ~4 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 97% — 2021–22 (Indian Bureau of Mines: Indian Minerals Yearbook 2022, Diamond chapter; annual) — ~4 newer release(s), 3 figure(s) from this source [mistral]
- US$35 per carat (average) — 2023 (GTRI / Business Standard: Lab-grown diamond import unit value; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- 15.5 billion carats — 2024 (US Geological Survey: Mineral Commodity Summaries; annual) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### cotton-stalk-is-one-of-hardest-crop  (score 14)
- 4%→8% maize residue burning share; 0.30 Mt→1.60 Mt (2011→2020) — 2011 and 2020 (Unspecified study (Science of the Total Environment): Residue burning share trends; annual) — ~14 newer release(s), 1 figure(s) from this source [mistral]
- 6 — 2025 (Punjab Energy Development Agency: operating CBG projects; monthly) — ~8 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 43.4 million tonnes — 2024–25 (PIB / ministry: maize production; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 29% — 2024–25 (industry and press reporting: maize to ethanol allocation; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]

### india-polishes-worlds-diamonds-with  (score 13)
- **H** ₹239.5 crore — 2024–25 (DGCI&S: HS 710510 imports; annual) — ~1 newer release(s), 7 figure(s) from this source [gemini+mistral]
- 1,238 million carats — 2021–22 (Indian Bureau of Mines: Indian Minerals Yearbook, Diamond chapter; annual) — ~4 newer release(s), 5 figure(s) from this source [gemini+mistral]
- ₹242.96 crore — 2023–24 Budget (PIB / Ministry: Union Budget allocations; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini]
- US$35 per carat — 2023 (GTRI (Business Standard): Import unit value estimates; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- ₹239.49 crore — 2024–25 (Ministry of Commerce / DGCI&S: HS 710510 diamond dust and powder imports; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 15.5 billion carats — 2024 (US Geological Survey: Mineral Commodity Summaries (2025); annual) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### nobody-blockaded-hormuz-to-slow-india  (score 12)
- **H** >95% — April 2026 peak (Wikipedia / USNI News / NPR: Timeline of the 2026 Iran war, 2026 Strait of Hormuz campaign/crisis; monthly) — ~4 newer release(s), 1 figure(s) from this source [gemini+mistral]

### guar-gum-indias-35-billion-export-peak  (score 12)
- **H** $541.65 million — 2023-24 (APEDA / DGCIS: Export value; annual) — ~2 newer release(s), 8 figure(s) from this source [gemini+mistral]
- **H** 80% — 2025-26 (APEDA: GuarGum commodity page; live) — ~1 newer release(s), 6 figure(s) from this source [gemini]
- 417,674 MT — 2023-24 (APEDA: Official Guar Gum profile; annual) — ~2 newer release(s), 2 figure(s) from this source [gemini+mistral]
- ₹8,440-11,671/quintal — 2024-25 (NCDEX: Jodhpur spot market price; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]

### if-india-paid-brics-in-rupees-scenario  (score 12)
- **H** $93.4 billion — FY2025-26 (Ministry of Commerce TradeStat: BRICS trade imports self-financing portion; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini]
- **H** $775 billion — FY2025-26 (PIB: PIB trade release; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini]
- $682.235bn — week ended 24 July 2026 (RBI: Weekly Statistical Supplement; weekly) — ~11 newer release(s), 2 figure(s) from this source [gemini+mistral]

### india-tracks-every-taxpayer-in-minutes  (score 11)
- **H** 80 crore PANs — March 2025 (Income Tax Department: PAN allotment statistics; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 14.5% — Q1 FY26 (HCLTech: Healthcare and life sciences, % of revenue; quarterly) — ~4 newer release(s), 1 figure(s) from this source [gemini]
- 3.26 crore health claims — 2024-25 (Business Standard on IRDAI data: Private health insurance claims; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 10.4% — FY2025-26 (TCS: Results release; quarterly) — ~1 newer release(s), 1 figure(s) from this source [gemini]
- 14.4% — Q4 FY26 (Wipro: Healthcare and life sciences, % of revenue; quarterly) — ~1 newer release(s), 1 figure(s) from this source [gemini]
- 7.4% — Q4 FY26 (Tech Mahindra: Healthcare and life sciences, % of revenue; quarterly) — ~1 newer release(s), 1 figure(s) from this source [gemini]

### indias-trade-story-has-three-big-wins  (score 11)
- **H** $825.3 billion — FY25 (MoSPI: Economic Survey 2025-26; annual) — ~1 newer release(s), 6 figure(s) from this source [gemini+mistral]
- **H** 2.4% — H1 FY26 (MoSPI: Economic Survey 2025-26; half-yearly) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- **H** $825 billion — FY2025 (Economic Survey 2025-26: Total goods and services exports; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 5.9% — H1 FY26 (2025-26) (Economic Survey 2025-26: Combined exports growth (weighted blend); half-yearly) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 4 years — as of 31 March 2026 (Government of India (PLI scheme reporting): PLI scheme reporting duration; live) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-oil-psus-say-they-clear-their_01269248608  (score 11)
- **H** 43.58% — FY2024-25 (Ministry of MSME: CPSE-wide MSE compliance; annual) — ~1 newer release(s), 6 figure(s) from this source [gemini]
- ₹262 crore — 2013-14 (ONGC: MSE procurement value; annual) — ~12 newer release(s), 1 figure(s) from this source [gemini]
- ₹773.39 crore — FY2023-24 (Business Standard: CPSE procurement from MSEs; annual) — ~2 newer release(s), 3 figure(s) from this source [gemini]

### discom-debt-relief-token-charge  (score 11)
- ₹71,750 cr — Apr 2025 (Ministry of Power: PRAAPTI portal; monthly) — ~16 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 33.38 crore — 2022-23 (CAG: India Electricity Trends; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 45 paise/unit — FY2023-24 (PFC: PFC Reports; annual) — ~2 newer release(s), 3 figure(s) from this source [gemini+mistral]

### 7186-litre-why-maize-is-indias-priciest  (score 11)
- 37 per cent — Kharif 2026 (DA&FW: State-wise kharif maize area change; weekly) — ~7 newer release(s), 9 figure(s) from this source [gemini]
- 57.40 lakh hectares — 2023-24 (Directorate of Sugarcane Development: State wise Area/Production/Productivity of Sugarcane; annual) — ~2 newer release(s), 6 figure(s) from this source [gemini+mistral]
- 86.15 lakh hectares — kharif 2025 (prior year) (MoA / UPAg (via ChiniMandi): maize acreage (all-India); live) — ~1 newer release(s), 2 figure(s) from this source [mistral]
- 58.62 lakh hectares — kharif 2025 (prior year) (MoA / Directorate of Sugarcane Development (via ChiniMandi): sugarcane acreage (all-India); live) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 1,776.49 crore litres (offered) — ESY 2025-26 Cycle 1 (OMCs (via iamrenew.com): ethanol tender offer volume; quarterly) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### indias-animal-protein-export-complex  (score 10)
- **H** $4.06 billion — FY2024-25 (APEDA: Animal Products exports; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** 513 plants — July 2026 (APEDA / EIC: Export-registered abattoirs and meat processing plants; monthly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 35% — 2023 (TERI / Statista: Biodiesel feedstock share; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 3% — 2023 (Statista: Biodiesel feedstock composition; annual) — ~2 newer release(s), 2 figure(s) from this source [mistral]

### abha-covers-93-crore-patients-its  (score 10)
- ~100% of residents with a digital health record (Estonia) — 2008 (Invest in Estonia: Estonia National Health Information System (X-Road) population coverage; annual) — ~17 newer release(s), 1 figure(s) from this source [mistral]
- 1,421,853 — April 2026 (MoSPI: Indian Medical Register; monthly) — ~4 newer release(s), 1 figure(s) from this source [gemini+mistral]

### methionine-not-lysine-is-indias-biggest  (score 10)
- 10 yuan a kilogram — April 2025 (trade press: Chinese threonine price; monthly) — ~16 newer release(s), 2 figure(s) from this source [gemini+mistral]
- 76% — 2023 (CCM: China lysine world capacity share; annual) — ~2 newer release(s), 2 figure(s) from this source [gemini+mistral]
- $2.68 a kilogram — first quarter of 2026 (market-research: Indian methionine import price; quarterly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- $870 a tonne — July 2026 (aggregator: China FOB lysine price; monthly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### annadata-to-urjadata-farmer-income-case  (score 8)
- **H** ~1.5% (2013-14), 20% (2025) — 2013-14 to 2025 (Ministry of Petroleum & Natural Gas / PIB: Ethanol blending rate; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 99.92% (2023-24), 99.5% (2024-25) — Sugar Season 2023-24, 2024-25 (PIB / DFPD: Sugar mills cane dues clearance rate; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- ₹1,97,000 crore — ESY 2014-15 to 2025-26 (PIB / ministry: Ethanol Programme Cumulative Scoreboard; monthly) — ~1 newer release(s), 14 figure(s) from this source [gemini]
- ~125.75 lakh MT (2024-25), ~125.78 lakh MT (2025-26) — ESY 2024-25, ESY 2025-26 (Lok Sabha reply (Dec 2025): Maize demand for ethanol; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 0.9 million tonnes — 2024 (DA&FW / USDA / FAO: Maize imports; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### cpi-wpi-trends-mospi-bulletin  (score 8)
- June 2025 — June 2025 (RBI: Foreign Exchange Reserves; monthly) — ~14 newer release(s), 1 figure(s) from this source [mistral]
- ≥ 5% — January 2026 – June 2026 (MoSPI: Consumer Price Index (CPI) - YoY Inflation (base 2024); monthly) — ~2 newer release(s), 2 figure(s) from this source [mistral]

### imported-fertiliser-fuel-prices-diesel  (score 8)
- +21.24% — August 2025 (MoSPI: CPI oils & fats; monthly) — ~12 newer release(s), 2 figure(s) from this source [gemini+mistral]
- +32.57% — June 2026 (DPIIT: WPI (2022-23 base series); monthly) — ~2 newer release(s), 7 figure(s) from this source [gemini+mistral]

### icra-rates-most-of-indias-economy  (score 8)
- ₹12,357 crore — first nine months of FY2026 (NHAI / ICRA: Toll-Operate-Transfer monetisation; monthly) — ~8 newer release(s), 1 figure(s) from this source [gemini]
- 150 GW — 30 June 2026 (ICRA: Renewable capacity under construction; monthly) — ~2 newer release(s), 3 figure(s) from this source [gemini+mistral]

### india-let-oil-companies-put-solar-on  (score 8)
- 283.46 GW — March 2026 (Ministry of New and Renewable Energy: physical-progress data; monthly) — ~5 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 162,701 sq km — 31 March 2023 (Business Standard: exploration activity disclosures; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini+mistral]

### a-million-wine-market-behind-150-wall  (score 7)
- **H** US$195.3 million — 2023 (IMARC Group: India Wine Market report; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 3.3 lakh+ visitors — FY2025 (Sula Vineyards: IPO disclosures and trade reporting; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### indias-ethanol-surplus-buys-about-five  (score 7)
- **H** ~2,000 crore litres — Jul 2026 (PIB: Installed ethanol capacity; monthly) — ~1 newer release(s), 1 figure(s) from this source [gemini]
- 718 crore litres (received), 83% — Q1–Q3 2025-26 (ChiniMandi: Ethanol procurement progress; quarterly) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- 139.0 million hectares (net sown), 217.9 million hectares (gross sown) — 2023-24 (Directorate of Economics and Statistics: Land use statistics; annual) — ~2 newer release(s), 2 figure(s) from this source [mistral]

### 5071-items-you-cannot-import-and-rs  (score 7)
- over 36,000 — June 2024 (PIB / ministry: SRIJAN portal items offered; monthly) — ~26 newer release(s), 1 figure(s) from this source [gemini+mistral]
- over 33,000 items — June 2026 (PIB / ministry: SRIJAN portal items offered; live) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]

### indias-coffee-crop-hasnt-grown-in  (score 7)
- $735.87 mn — FY26 (DGCI&S: 8-digit trade dataset; monthly) — ~5 newer release(s), 7 figure(s) from this source [gemini+mistral]
- US$1.8 billion — FY2024-25 (Department of Commerce: Coffee export earnings; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- $1.07 billion — April–September 2025 (Department of Commerce: Coffee export earnings; half-yearly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### basf-and-mitsubishi-are-running  (score 7)
- 6,137 sites and 1,361.6 hectares — FY2023 (pv magazine: Japan’s national agrivoltaic site approvals; annual) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- 44,000 kWh a year, 961.4 kWh per installed kW — 2025 (Journal of Photonics for Energy: Miyada-mura agrivoltaic pilot generation; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini]
- 6,137 sites, 1,361.6 hectares — FY2023 (Government of Japan: Agrivoltaic site approvals; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini]

### cpi-inflation-heatmap-india-june-2026  (score 6)
- **H** 4.38% — June 2026 (MoSPI: Combined-sector CPI, year-on-year inflation; monthly) — ~2 newer release(s), 17 figure(s) from this source [gemini+mistral]

### europes-export-credit-agencies-are  (score 6)
- **H** 20 — 2023 (European Commission: Annual review of member states' export credit agencies; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]

### oilfield-costs-rose-68-while-global  (score 6)
- **H** 206 rigs — June 2026 (Baker Hughes: Baker Hughes international rig count; monthly) — ~2 newer release(s), 2 figure(s) from this source [gemini+mistral]

### bagasse-is-one-crop-residue-already  (score 6)
- **H** 9,806 MW — end of 2024 (MNRE: bagasse cogeneration capacity; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** 11,748 MW — July 2026 (MNRE: combined bagasse and other biomass cogeneration capacity; monthly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### green-gold-what-spirulina-actually-is  (score 6)
- **H** $6.69 million — 2024 (trade-data aggregators: National spirulina export value; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- **H** >20,000 tonnes — 2024 (market-research firms: Global market production volume; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]

### how-indias-automotive-clusters-rewired  (score 6)
- **H** ₹6.73 lakh crore — FY2024-25 (ACMA: Auto-component industry turnover; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- USD21.2 billion — FY24 (ACMA / KPMG India: Auto-component export base; annual) — ~2 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 155 products and variants — July 2026 (Ministry of Heavy Industries: PLI-Auto DVA certificates; monthly) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]

### indias-60000-crore-api-push-traced-to  (score 6)
- **H** 33 drugs — March 2026 (PIB / ministry: Bulk Drugs PLI approved projects and drugs; quarterly) — ~1 newer release(s), 14 figure(s) from this source [gemini+mistral]
- 45% — 2022 (industry estimates: China share of global API supply; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini]

### indias-lng-trucks-grew-75-in-2025-about  (score 6)
- **H** ~30% — 2024 (Wood Mackenzie / IEEFA: China's heavy-duty truck sales; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- **H** 1,309 units (end-2025) / 747 units (2024) — 2024 / end-2025 (Vahan registration estimates (via Business Standard/Essar): Vahan registrations of goods vehicles by fuel type (unofficial estimate); annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-used-oil-epr-wants-half-of-all  (score 6)
- **H** 5% — 2024-25 (MoEFCC: Hazardous and Other Wastes (Management and Transboundary Movement) Second Amendment Rules, 2023; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- **H** 119 — as on 10 August 2026 (CPCB: CPCB Used Oil EPR Portal; live) — ~1 newer release(s), 5 figure(s) from this source [gemini+mistral]

### how-to-use-data-source-mining-pull  (score 6)
- 1840.0 Rs per quintal — 21/07/2026 (Agmarknet: mandi_prices; daily) — ~87 newer release(s), 4 figure(s) from this source [gemini+mistral]

### fci-storage-scenario-capacity-stock-and  (score 6)
- ~907 LMT — mid-2021 (DFPD Foodgrain Bulletin: Central-pool stock (record); monthly) — ~62 newer release(s), 1 figure(s) from this source [mistral]

### indias-6000-crore-fisheries-scheme  (score 6)
- 3,183 new registrations — 24 hours before 30 August 2026 (National Fisheries Digital Platform (NFDP): NFDP daily registration growth; daily) — ~48 newer release(s), 1 figure(s) from this source [mistral]

### alimco-jaipur-foot-and-bionic-gap-in  (score 6)
- 21 approved projects — March 2025 (DPIIT: PLI Scheme for Medical Devices Progress; monthly) — ~17 newer release(s), 2 figure(s) from this source [gemini+mistral]

### a-supreme-court-ruling-on-intoxicating  (score 6)
- 50% — June 2025 (Maharashtra state excise department: IMFL retail prices and duty; monthly) — ~14 newer release(s), 1 figure(s) from this source [gemini+mistral]

### india-imports-whey-protein-its-cheese  (score 6)
- US$12.50 to 13.00 a pound — mid-July 2026 (USDA Agricultural Marketing Service: Dairy Market News WPC80 price; weekly) — ~12 newer release(s), 1 figure(s) from this source [gemini+mistral]

### india-rewrote-its-entire-maritime-legal  (score 6)
- 1,592 vessels — Dec 2025 (DG Shipping: Indian Shipping Statistics; monthly) — ~8 newer release(s), 3 figure(s) from this source [gemini+mistral]

### a-2013-vision-saw-india-needing-746  (score 6)
- 68,542 MMSCM — FY2025-26 (PPAC: Gas balance; monthly) — ~5 newer release(s), 6 figure(s) from this source [gemini]
- 68,542 MMSCM (≈188 MMSCMD) — FY2025-26 (NSE-hosted industry review (using PPAC's gas balance): Gas consumption (NSE review); annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### every-india-europe-tech-agreement-pib  (score 6)
- Feb 2025 — Feb 2025 (PIB: TTC Working Group 2 (WG2) activities; quarterly) — ~5 newer release(s), 1 figure(s) from this source [mistral]
- 28 Feb 2025 — 28 Feb 2025 (PIB: TTC Ministerial Meetings; annual) — ~1 newer release(s), 3 figure(s) from this source [mistral]

### a-tax-play-grow-ethanol-sgst-revenue  (score 6)
- ₹76.08–₹122.00/kg (CNG price range, April 2025) — April 2025 (PNGRB: State/UT-wise CNG retail price (Case Study Report); quarterly) — ~4 newer release(s), 2 figure(s) from this source [mistral]
- 1 TMT — H1 FY26 (PPAC: Ready Reckoner Table 3.7 CNG Sales in India; half-yearly) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 23.9% (Gujarat), 22.1% (Haryana), 16.4% (Uttar Pradesh), 15.4% (Maharashtra), 14.2% (Kerala), 12.2% (Punjab), 12.0% (Madhya Pradesh), 12.5% (Bihar), 13.1% (Uttarakhand), 4.9% (Himachal Pradesh), 1.4% (Delhi) — as on 2026-07-22 (cng-cgd-retail-outlet-mapping repo (PNGRB GA × SSRI): State-wise CNG-equipped fuel retail outlets; live) — ~1 newer release(s), 3 figure(s) from this source [mistral]

### cow-dung-already-flew-rocket-engine  (score 5)
- **H** 200+ — as on 6 Aug 2026 (PIB / ministry: SATAT and related schemes commissioned plants; monthly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 90% — 2013 (Bureau of Indian Standards: IS 16087 CBG specification; multi-year) — ~2 newer release(s), 5 figure(s) from this source [gemini]

### ethanol-freed-up-refinery-capacity-for  (score 5)
- **H** 20% — since 2025-26 (this blog's own reporting: E20 petrol ethanol blending share; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 258.1 MMTPA — FY2024-25 (MoPNG: Installed refining capacity; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 99.34% (FY2023-24) → 80.73% (FY2024-25) — FY2023-24 → FY2024-25 (this blog's own reporting, drawn from PIB Annexure PRID 2237414: China dependency of India's ibuprofen imports; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### annexure-314-hsn-codes-mapped-to  (score 5)
- 42 codes — FY2024-25 or FY2025-26 (DGCI&S: TradeStat Eidb Commodity-wise export/import reports; monthly) — ~5 newer release(s), 2 figure(s) from this source [gemini+mistral]

### indias-subsidised-imports-fertilisers  (score 5)
- ~₹35,354 crore — March 2026 (PIB / ministry: PLI disbursement; monthly) — ~5 newer release(s), 1 figure(s) from this source [gemini+mistral]

### from-barrel-to-bottle-petrochemical  (score 5)
- 3,450 thousand tonnes — FY2023 (ChemAnalyst: India HDPE market report; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 8% — January–June 2026 (PPAC: Industry Consumption Report POL & NG; monthly) — ~2 newer release(s), 8 figure(s) from this source [gemini+mistral]

### cough-syrup-in-lollipop-for-babies  (score 5)
- 4,097 hospitalisations + 2 deaths — 2012–2022 (US CDC: CDC poison control data; annual) — ~3 newer release(s), 1 figure(s) from this source [mistral]
- 324 million strips a year — FY2024 (ZIM Labs: Annual Report; annual) — ~2 newer release(s), 2 figure(s) from this source [gemini+mistral]

### inflation-trends-globally-what-five  (score 5)
- 3.7% — Q4 2025 (OECD: OECD Wage Bulletin; quarterly) — ~2 newer release(s), 7 figure(s) from this source [gemini+mistral]
- 12.3% (US, May 2026), 8.6% (Korea, May 2026), 8.3% (India, April 2026), 7.1% (Japan, June 2026), 4.9% (Euro area, May 2026) — Jan-Jun 2026 (Various (BLS, Bank of Japan, Bank of Korea, Eurostat, Office of the Economic Adviser): Producer Price Index (PPI) / Wholesale Price Index (WPI); monthly) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- Steepest rise (qualitative, no exact figure) — July 2026 (S&P Global Market Intelligence: Purchasing Managers’ Index (PMI) commentary; monthly) — ~1 newer release(s), 2 figure(s) from this source [mistral]

### 379-kilos-hectare-in-punjab-44-in  (score 5)
- 172 of 223 — 2026-07 up to June (PIB / ministry: Central Fertiliser Quality Control and Training Institute sample testing data; monthly) — ~2 newer release(s), 1 figure(s) from this source [gemini]
- 93.5% (Punjab), 90% (Haryana), 60% (national) — 2023-24 (Directorate of Economics and Statistics: Irrigation shares of gross cropped area; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- ₹111.72 crore (total), ₹28 crore (2024-25), ₹83.72 crore (2025-26) — 2024-25, 2025-26 (up to 28 Feb) (Department of Fertilizers: Market Development Assistance disbursement; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### india-cannot-sell-china-free-medicine  (score 5)
- ₹58,440 crore — FY2023-24 (Department of Pharmaceuticals and DGCI&S: Total pharma imports; annual) — ~2 newer release(s), 2 figure(s) from this source [gemini]
- ₹63,573 crore — FY2024-25 (Department of Pharmaceuticals / DGCI&S: Total pharmaceutical imports; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]
- 97 distinct active ingredients — FY2024 and FY2025 (PIB: APIs with ≥70% China supply; annual) — ~1 newer release(s), 2 figure(s) from this source [mistral]
- 30% (bulk drug exports), 26.5% (formulation exports) — FY2024-25 (Department of Pharmaceuticals: PLI Bulk Drugs export contribution; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-state-incentive-war-gujarats  (score 5)
- ₹83 cr (disbursed), ₹28,400 cr (outlay) — FY2024 (Jammu & Kashmir: Industrial Policy; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- ₹7,864 cr (total), ~1.3 lakh MSMEs — FY2020-21 to FY2024-25 (Gujarat: MSME Track Disbursal; annual) — ~2 newer release(s), 1 figure(s) from this source [mistral]
- ₹765.78 cr (FY2025), +293% YoY — FY2025 (Rajasthan: RIPS Disbursal; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### india-has-tested-its-soil-twice-second  (score 4)
- **H** 25.89 cr — as of July 2026 (PIB / Ministry of Agriculture & Farmers Welfare: Soil Health Cards issued; live) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- over 25 crore — January 2026 (Ministry of Agriculture & Farmers Welfare: Soil Health Cards issued; live) — ~1 newer release(s), 1 figure(s) from this source [gemini]

### india-mineral-oil-hsn-ch27-trade  (score 4)
- **H** 121.1 MMT — FY2025-26 H1 (PPAC: Crude imported; half-yearly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- Export refined MS/HSD/ATF/naphtha; import crude, LPG, base oil, petcoke, bitumen — FY2024-25 (PPAC / DGCI&S: TRADESTAT orientation + PPAC FY2024-25 values; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### indias-ev-market-single-digit  (score 4)
- **H** 2.5 million — FY2025-26 (Vahan / CEEW-GFC: EV registrations; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini]
- ₹0.35/km — July 2026 (~/vehicle_fuel_mileage repo: Running cost/km; monthly) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]

### interest-subvention-built-499-ethanol  (score 4)
- **H** 1,822 crore litres/year (capacity) + 38 distilleries + 169 crore litres (pipeline) — ESY 2024-25 (NABARD / MoPNG (via Lok Sabha, Business Today, ChiniMandi, BioEnergy Times, USDA FAS): Ethanol Distillery Capacity & Pipeline (1G Interest Subvention Scheme); annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]
- 684 crore litres (few years ago) → 1,822 crore litres (ESY 2024-25) — ESY 2024-25 (MoPNG / BioEnergy Times / IANS: Ethanol Capacity Growth; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### epfos-pay-ceiling-rose-to-25000-after  (score 4)
- ₹18,456 — April 2026 (PIB / ministry: minimum wage; monthly) — ~4 newer release(s), 1 figure(s) from this source [gemini+mistral]

### indias-fdi-moved-to-software-and  (score 4)
- $12.1 billion — April 2026 (DPIIT: Quarterly Fact Sheet on FDI Inflow; monthly) — ~4 newer release(s), 1 figure(s) from this source [gemini+mistral]

### indias-first-seabed-mineral-auction  (score 4)
- 75,000 square kilometres — 2002 (PIB / ministry: International Seabed Authority contract area; multi-year) — ~4 newer release(s), 1 figure(s) from this source [gemini+mistral]

### ahidf-has-sanctioned-19751-crore-in  (score 3)
- **H** ₹36,344.3 crore — 10 August 2026 (SIDBI / Udyami Mitra: AHIDF live dashboard Volume & Value Tracker; live) — ~1 newer release(s), 25 figure(s) from this source [gemini+mistral]

### do-cbse-past-papers-actually-help  (score 3)
- **H** 10/10 sessions — 2015-16–2024-25 (CBSE: Sample Question Paper archive; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### greenhouse-emissions-reduction-and-cbam  (score 3)
- **H** ₹11.5 lakh crore — 2024-25 (PIB / ministry: India-EU bilateral trade in goods; annual) — ~1 newer release(s), 4 figure(s) from this source [gemini+mistral]

### iem-conversion-historical-performance  (score 3)
- **H** Rs 4,21,929cr — FY2024-25 (PIB / ministry: FDI equity inflow; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### india-has-tax-treaties-with-97  (score 3)
- **H** 97 — 30 July 2026 (Income Tax Department: Income Tax Department DTAA database; live) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]

### india-irrigates-itself-966-of-its  (score 3)
- **H** 23.14 million — 2017-18 (Ministry of Jal Shakti: 6th Minor Irrigation Census; multi-year) — ~1 newer release(s), 15 figure(s) from this source [gemini+mistral]

### indias-live-ipo-queue-has-232-companies  (score 3)
- **H** 232 companies — Dec 2024-Jun 2026 (SEBI: Live mainboard DRHP pipeline; live) — ~1 newer release(s), 13 figure(s) from this source [gemini+mistral]

### lemon-cultivation-in-india-steady-trees  (score 3)
- **H** ₹80.7/kg — 18 Aug 2026 (PIB / ministry: Agmarknet national average and state prices; live) — ~1 newer release(s), 16 figure(s) from this source [gemini+mistral]

### lok-sabha-question-registry-1843-scheme  (score 3)
- **H** 273 questions — 17th–18th Lok Sabha (Lok Sabha Secretariat: Lok Sabha Question Registry; live) — ~1 newer release(s), 5 figure(s) from this source [gemini+mistral]

### import-dependent-sectors-vs-government  (score 3)
- **H** $203.4 billion — FY2025-26 (repo's own data (TRADESTAT/DGCI&S): HS27 import value; annual) — ~1 newer release(s), 12 figure(s) from this source [mistral]

### india-forest-wildlife-crz-clearances  (score 3)
- **H** 42.0% — as on 22 Jul 2026 (MoEFCC: PARIVESH 2.0 Forest Clearance register; live) — ~1 newer release(s), 29 figure(s) from this source [gemini]

### indias-two-tracks-of-health-cover-and  (score 3)
- 43% — FY2022-23 (MoSPI: National Health Accounts Estimates; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini+mistral]

### pet-recycling-already-cuts-emissions-60  (score 3)
- 95% — 2022 (CPCB: PET recovery rate; annual) — ~3 newer release(s), 2 figure(s) from this source [gemini+mistral]

### 028-unit-diesel-math-behind-indias-data  (score 3)
- 5,665 CNG stations — March 2023 (PNGRB: network-expansion statements; annual) — ~3 newer release(s), 1 figure(s) from this source [gemini]

### ethanols-coal-boilers-briquette-gap-and  (score 3)
- 428,580–525,002 tonnes/year — 2017–2022 (EPA-reported figures (via EESI, MIT Sequestration project database): ADM Decatur ICCS project CO₂ storage; annual) — ~3 newer release(s), 1 figure(s) from this source [mistral]

### abu-dhabi-paid-2-billion-for-binance  (score 3)
- US$26.45 billion — April 2000 to June 2026 (DPIIT: Fact sheet on foreign direct investment; monthly) — ~2 newer release(s), 4 figure(s) from this source [gemini+mistral]
- 3rd place — 2024 (Henley Passport Index: Crypto-friendly countries ranking; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### oisd-writes-indias-oil-safety-rules-api  (score 3)
- ~95 members — 2023-24 (FIPI: Annual Report; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]
- statutory licensing authority — 1934, 2002 (Government of India: Petroleum Act and Rules; live) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### india-imported-28-million-of-sucralose  (score 3)
- 89.8 million — 2024 (International Diabetes Federation: IDF Diabetes Atlas; annual) — ~1 newer release(s), 2 figure(s) from this source [gemini+mistral]
- ₹161.79 crore — FY25 (Customs: Customs data aggregation; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- 85–90% — 2024 (Market reports: World sucralose capacity share; annual) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]

### airbags-and-seat-belts-are-import-heavy  (score 2)
- 40 lakh units — FY2023-24 (PIB / ministry: Passenger and commercial vehicle sales; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]

### cough-syrup-in-lollipop-for-babies_0399087402  (score 2)
- 324 million strips a year — FY2024 (ZIM Laboratories: annual report; annual) — ~2 newer release(s), 2 figure(s) from this source [gemini+mistral]

### indias-mobile-phone-pli-beat-every  (score 2)
- 23% — FY2023-24 (Lok Sabha: PLI-LSEM Domestic Value Addition; annual) — ~2 newer release(s), 1 figure(s) from this source [gemini+mistral]

### engineering-and-auto-component-makers  (score 2)
- June 2026 — June 2026 (SEBI (via DRHP filings): SEBI Updated DRHP filing month; monthly) — ~2 newer release(s), 1 figure(s) from this source [mistral]

### indias-display-fab-scheme-got-two  (score 2)
- ₹1.64 lakh crore — July 2026 (PIB: India Semiconductor Mission Tally; monthly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]
- FY25 — FY2024-25 (Angel One: Crystal Matrix Ltd – FY25 balance sheet; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### 577-of-indias-plant-variety  (score 2)
- 43 certificates — as on 31 Jul 2026 (PPV&FR Authority: certificate count by crop category; monthly) — ~1 newer release(s), 4 figure(s) from this source [gemini]
- 239 certificates (sum of sub-categories) — as on 31 July 2026 (Protection of Plant Varieties and Farmers' Rights (PPV&FR) Authority: Certificates by sub-category (sum); live) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### green-energy-corridor-iii-is-15-times  (score 1)
- 470 GWh — January to March 2026 (Ember: Inter-state grid renewable curtailment; quarterly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### indias-biofuel-rules-are-being-written  (score 1)
- 149 crore litres — Q4 (OMCs: Q4 allocation; quarterly) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### indias-lysine-deficit-is-102-million  (score 1)
- $870 a tonne — July 2026 (procurement-data aggregator: China FOB lysine price; monthly) — ~1 newer release(s), 3 figure(s) from this source [gemini+mistral]

### indias-military-quantum-plan-has-four  (score 1)
- 43.07 / 32.77 — 2024-25 (Policy Circle: National Quantum Mission released / used; annual) — ~1 newer release(s), 1 figure(s) from this source [gemini+mistral]

### ethanol-blending-omc-books-e20-today-vs  (score 1)
- ₹46/L (~$86/bbl) — FY2024-25 (RR Table 4.11 (cited): Petrol export price; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### fipis-biggest-ask-is-getting-natural  (score 1)
- Gurmeet Singh — 2024-25 (FIPI Annual Report 2024-25: FIPI Director General; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### india-and-mercosur-are-expanding-450  (score 1)
- $8.12 billion (2024-25 exports), $9.36 billion (2024-25 imports) — 2024-25 (Press reports of official data: India-MERCOSUR two-way trade; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### mopsws-25000-crore-maritime-development  (score 1)
- ~0.05–0.06% (India), ~95%+ (China-South Korea-Japan), ~54%+ (China alone) — 2024 (Author's prior reporting: Global shipbuilding market share; annual) — ~1 newer release(s), 1 figure(s) from this source [mistral]

### one-nation-one-gst-rate-what-true-flat  (score 1)
- ~2018 (Gini estimate) — circa 2018 (UAE National Bureau of Statistics (estimated): UAE Gini coefficient; multi-year) — ~1 newer release(s), 1 figure(s) from this source [mistral]

## Skipped (too large)

- chemical-import-substitution-full-hsn-8_01082878313: too large: 203,677 chars > 100,000
- ipa-digital-twin-reportage-latest: too large: 120,086 chars > 100,000
