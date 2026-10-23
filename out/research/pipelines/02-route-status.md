# 02 — NGPL route status (for the pipeline map)

Compiled 2026-10-23. Companion data file: `routes.json` (same folder). **Map coordinates are approximate.** The waypoints are towns along each route, placed from general geographic knowledge for a schematic map. They are not surveyed alignments.

## Source tags

- **[primary]**: read directly from a local primary document (the HLEC report, the PPAC MRR).
- **[primary-via-summary]**: a primary document (PNGRB MIS report or press note, GAIL/NSE filing, GAIL annual report, IOCL page) seen only through a WebSearch result summary. This environment cannot reach `*.gov.in`, and the GAIL/NSE hosts failed too (WebFetch DNS error; the proxy refused curl). These figures have **not** been checked against the PDF.
- **[secondary]**: tracker or wiki (Global Energy Monitor `gem.wiki`).
- **[press]**: news report.

Twenty-five WebSearch calls were used, the full budget. No `.gov.in` page was fetched directly. Where a URL below sits on `pngrb.gov.in`, it is cited from the search summary only.

---

## 1. Totals: PPAC MRR May 2026, Table 20 (as on 31.12.2025) [primary]

Source: local file `00-ppac-mrr-may2026-table20.txt`, PPAC "Snapshot of India's Oil & Gas data", May 2026 (published June 2026), Table 20, which draws on PNGRB. The text layer is interleaved, so the row reading below is **tentative**.

| Entity | Operational km | Under construction km | Total km |
|---|---|---|---|
| GAIL | 17,682 | 1,992 | 19,674 |
| GSPL | 2,795 | 100 | 2,895 |
| PIL | 1,485 | – | 1,485 |
| IOCL | 1,237 | 408 | 1,645 |
| GIGL | 1,419 | 784 | 2,203 |
| Others (APGDC, IGGL, IMC, GTIL, HPPL) | 757 | 3,797 | 4,554 |
| **Total (common/contract carrier)** | **25,925** | **7,301** | **33,226** |

Including tie-ins, dedicated lines and STPL, the totals are 34,273 km authorised, 27,427 km operational and 8,489 km under construction (P). The PNGRB NGPL MIS for Dec 2025 and Jan 2026 gives the same 34,273 / 27,427 km [primary-via-summary].

---

## 2. HLEC "Vision 2040" (PNGRB, Nov 2025): extracted tables [primary]

Local file `_hlec_part2.md`. All figures are as printed, with data as of Dec 2024. Utilisation is for FY2025 up to Dec 2024.

> **Flag:** Every GAIL row in Table 12.7 except KG Basin (20.03%) and KKBMPL (24.5%) prints **71.69%** utilisation, as does the 8-km Agartala Regional Network. This is evidently a single GAIL network-wide figure repeated on each row, so it should not be read as line-specific. GSPL-HP prints 100.5%.

### Table 12.7: Cost-plus pipelines (Annexure 6.1.1)

**Part of the National Gas Grid**

| # | Pipeline | Entity | Auth. km | Cap. MMSCMD | Op. km | Util. | Status |
|---|---|---|---|---|---|---|---|
| 1 | Baroda sub-network (Gujarat pipeline network) | GAIL | 481 | 8.13 | 481 | 71.69%* | Fully operational |
| 2 | KG Basin | GAIL | 878 | 16 | 867 | 20.03% | Fully operational |
| 3–4 | HVJ + HVJ Upgradation | GAIL | 6,169 | 107 | 6,729 | 71.69%* | Fully operational |
| 5 | Dadri–Bawana–Nangal | GAIL | 921 | 31 | 998 | 71.69%* | Fully operational |
| 6 | Chhainsa–Jhajjar–Hisar | GAIL | 455 | 35 | 440 | 71.69%* | Fully operational |
| 7 | Jagdishpur–Haldia–Bokaro–Dhamra | GAIL | 3,546 | 23 | 3,270 | 71.69%* | Partially commissioned |
| 8 | Dahej–Uran–Panvel–Dabhol | GAIL | 815 | 19.9 | 943 | 71.69%* | Fully operational |
| 9 | Dabhol–Bangalore | GAIL | 1,414 | 16 | 1,148 | 71.69%* | Partially commissioned |
| 10 | Mumbai Regional | GAIL | 129 | 7.04 | 125 | 71.69%* | Fully operational |
| 11 | GSPL Low Pressure | GSPL | 58 | 12 | 57 | 50.67% | Fully operational |
| 12 | GSPL High Pressure | GSPL | 2,207 | 36 | 2,704 | 100.5% | Fully operational |
| 13 | Hazira–Ankleshwar | GGL | 73 | 5.06 | 73 | 12.06% | Fully operational |
| 14 | Dadri–Panipat | IOCL | 132 | 20 | 143 | 27.85% | Fully operational |
| 15 | Uran–Trombay | ONGC | 24 | 6 | 24 | 58.85% | Fully operational |
| 16 | East–West Pipeline | PIL | 1,459 | 85 | 1,483 | 41% | Fully operational |
| | **Total** | | **18,761** | | **19,485** | | |

\* GAIL network figure (see flag). The entity column is merged in the source; rows 1–10 are GAIL.

**Not part of the National Gas Grid**

| # | Pipeline | Entity | Auth. km | Cap. | Op. km | Util. | Status |
|---|---|---|---|---|---|---|---|
| 1 | AGCL Assam gas pipeline network | AGCL | 105 | 2.482 | 107 | 80.25% | Fully operational |
| 2 | Uran–Taloja | Deepak Fertilizer | 42 | 0.7 | 42 | 0% | Fully operational |
| 3 | Cauvery Basin Regional | GAIL | 240 | 4.33 | 242 | 40.18% | Fully operational |
| 4 | Dukli–Maharajganj | GAIL | 5 | 0.08 | 0 | 0% | "Fully operational" (as printed, with 0 op. km) |
| 5 | Agartala Regional | GAIL | 55 | 2 | 65 | 36.50% | Fully operational |
| 6 | Kochi–Koottanad–Bangalore–Mangalore | GAIL | 1,104 | 16 | 644 | 24.5% | Partially commissioned |
| * | Gujarat Regional Sub-Network | GAIL | 128 | 8.31 | 109 | 32.96% | Fully operational (also counted in NGG for numbering) |
| 7 | Agartala Regional Network | GAIL | 8 | 2.5 | 8 | 71.69%* | Fully operational |
| 8 | North-East Natural Gas Pipeline Grid | IGGL | 1,656 | 4.75 | – | – | Under construction |
| | **Total** | | **3,343** | | **1,217** | | |

### Table 12.8: Bid-out pipelines (Annexure 6.1.2)

| # | Pipeline | Entity | Auth. km | Cap. MMSCMD | Op. km | Util. | Status |
|---|---|---|---|---|---|---|---|
| NGG-1 | Shahdol–Phulpur | RGPL | 312 | 3.5 | 304 | 20.57% | Fully operational |
| NGG-2 | Mehsana–Bhatinda | GIGL | 1,940 | 80.11 | 1,200 | 4.77% | Partially commissioned |
| NGG-3 | Bhatinda–Gurdaspur | GIGL | 261 | 42.42 | 102 | 0.17% | Partially commissioned |
| NGG-4 | Mallavaram–Bhopal–Bhilwara–Vijaipur | GITL | 1,881 | 78.25 | 365 | 2.71% | Partially commissioned |
| | NGG subtotal | | 4,394 | | 1,971 | | |
| 1 | Ennore–Tuticorin (ETBPNMTPL) | IOCL | 1,431 | 84.67 | 1,080 | 5.91% | Partially commissioned |
| 2 | Hazaribagh–Ranchi | IOCL | 65 | 1.03 | – | – | Under construction |
| 3 | Kakinada–Vijayawada–Nellore | IMC | 667 | 18 | – | – | Under construction |
| 4 | Kanai Chhata–Panitar | HPPL | 317 | 19.20 | – | – | Under construction |
| 5 | Srikakulam–Angul | GAIL | 690 | 6.65 | – | – | Under construction |
| 6 | Mumbai–Nagpur–Jharsuguda | GAIL | 1,755 | 16.50 | – | – | Under construction |
| 7 | Ennore–Nellore | GTIL | 220 | 36 | – | – | Under construction |
| 8 | Gurdaspur–Jammu | GAIL | 160 | 3.10 | – | – | Under construction |
| 9 | Jamnagar–Dwarka | GSPL | 100 | 3 | – | – | Under construction |
| | Non-NGG subtotal | | 5,405 | | 1,080 | | |

HLEC text (line ~259): of the 12 bid-out pipelines, only Shahdol–Phulpur is fully operational, and HLEC attributes the delays to "unrealistically low tariff" bids.

### Annexure 6.1.3: Future state

**Authorised but not executed or delayed:** Kakinada–Vijayawada–Nellore; Ennore–Nellore; Kakinada–Srikakulam; Kanai Chhata–Panitar; Jaigarh–Mangalore.

**Table 12.9: Alternate routes**

| Authorised route | Alternate | Length |
|---|---|---|
| Kakinada–Vijayawada–Nellore (HLEC text: 522 km, siting issues) | Kakinada–Vijayawada–Kadapa–Chittoor | ~705 km |
| Kanai Chhata–Panitar | Digha–Kolkata–Paschim Medinipur | ~300 km |
| Jaigarh–Mangalore (terrain, no anchor customers) | Mangalore–Shimoga–Dharwad | ~400 km |

**New pipeline:** Barmer–Jaisalmer–Jodhpur–Bikaner–Churu (~650 km), which would feed into Mehsana–Bhatinda at Churu. **Text-only:** Jabalpur–Shahdol (~200–250 km), linking the Mumbai–Jharsuguda line to GAIL's network and the CBM block.

**Table 12.10: Proposed gas grid and corridor projects** (from the PNGRB NGG Technical Assessment Report 2022). Flows are 2040 values in MMSCMD.

| Pipeline | km | Dia (in) BAU | Flow BAU | Dia ACU | Flow ACU |
|---|---|---|---|---|---|
| Kakinada–Vijayawada–Kadapa–Chittoor (NGG) | 705 | 24 | 1.45 | 24 | 5.79 |
| Kochi–Thoothukkudi (NGG) | 399 | 16 | 2.72 | 18 | 5.72 |
| Rewa–Chhatarpur–Jhansi | 465 | 24 | 0.80 | 24 | 3.66 |
| Lucknow–Begusarai | 672 | 24 | 5.20 | 24 | 7.88 |
| Ramagundam–Nagpur | 332/164 | 12/24 | 1.03 | 12/24 | 2.38 |
| Narsinghpur–Amliha–Godhi | 438/254 | 12/16 | 2.64 | 20/16 | 7.38 |
| Purania–Ranaghat | 397 | 24 | 1.46 | 24 | 3.37 |
| Raipur–Koraput | 95/280 | 10/20 | 2.02 | 10/20 | 4.53 |
| Ramgarh–Barmer | 288 | 30 | 0.19 | 30 | 0.89 |
| Srinagar–Jammu | 249 | 24 | 0.59 | 24 | 1.02 |
| Bengaluru–Arkula | 328 | 16 | 1.35 | 16 | 2.52 |
| Salem–Madurai | 293 | 24 | 0.53 | 24 | 1.48 |
| Rajgarh–Bhopal–Aurangabad | 795 | 16 | 1.90 | 16 | 3.48 |
| Nargund–Vijayapura–Barshi | 304 | 20 | 0.75 | 20 | 2.83 |
| Barshi–Beed–Vadap | 228/151 | 12/24 | 0.42 | 12/24 | 0.85 |
| Shillong–Gambegre | 283 | 30 | 0.09 | 30 | 0.11 |
| Gadag–Ballari | 128 | 14 | 3.03 | 14 | 4.66 |
| Golaghat–Itanagar | 80 | 6 | 0.05 | 6 | 0.09 |
| Hyderabad–Kurnool | 129 | 12 | 1.20 | 12 | 2.64 |
| Jorhat–Kohima | 302 | 30 | 0.10 | 30 | 0.15 |
| Kolaghat–Jajpur | 276 | 30 | 3.33 | 30 | 5.81 |

The HLEC estimates the grid needs another 2,700–7,900 km by 2040 (BAU vs ACU), for a total cost of US$26.0 bn (BAU) or US$39.7 bn (ACU) (Table 12.13). Table 12.12 rates Gadag–Ballari as the only line "realisable" (after 6–7 years) under BAU. It rates Shillong–Gambegre and Jorhat–Kohima as unrealisable in both cases.

---

## 3. Status updates, 2025-26 (under-construction and partly commissioned lines)

The status as of 23 Oct 2026 is our reading of the latest dated evidence. Several targets (June–Oct 2026) have passed without any confirmation found.

### Mumbai–Nagpur–Jharsuguda (MNJPL), GAIL. Map status: Mumbai–Nagpur operational; Nagpur–Jharsuguda CG/Odisha operational; Maharashtra section partly operational
- Authorised 1,755 km, 16.5 MMSCMD [primary, HLEC T12.8]. GAIL gives 1,702–1,707 km.
- Sep 2025: 1,440 km ready for gas-in; 11 km of construction left, all in Maharashtra. Board target for full commissioning moved to 31 Dec 2025 from June 2025. Cost overrun to about Rs 8,255 cr [press] (pipeline-journal.net/news/gail-pipeline-set-dec-2025-commissioning-after-delays-and-cost-increase, Sep 2025; themachinemaker.com/news/gails-mumbai-nagpur-jharsuguda-pipeline-set-for-full-launch-by-december-31-2025/).
- The 694 km Mumbai–Nagpur stretch is fully operational [press] (indianinfrastructure.com/2025/11/07/critical-links-mumbai-nagpur-jharsuguda-pipeline-connects-gas-corridors-with-key-industrial-regions/, 7 Nov 2025).
- 31 Jan 2026: the Chhattisgarh–Odisha portion of Nagpur–Jharsuguda is operational; remaining part targeted for Feb 2026 [primary-via-summary] (nsearchives.nseindia.com/corporate/Himanshugail_31012026172038_Reg30.pdf).
- 25 Mar 2026 board: the Maharashtra section of Nagpur–Jharsuguda to be commissioned "progressively by 30 Jun 2026", pending PNGRB approval [press, citing a GAIL filing] (insights.dsij.in, "this gas transmission and marketing company updates project pipeline…", Mar 2026).
- GAIL Annual Report FY2025-26 lists "203 km of Nagpur–Jharsuguda section of MNJPL in Maharashtra" as commissioned during the year [primary-via-summary] (gailebank.gail.co.in/InvestorsZone/AnnualReports/Gail-Annual-Report 2025-26.pdf). **This conflicts with the March filing. Check before publishing.**
- Nagpur–Jabalpur, 317 km and reported as part of MNJPL: construction finished in March 2026, with commissioning awaiting PESO clearance [press] (thehitavada.com/Encyc/2026/3/25/major-energy-boost-gail-finishes-nagpurjabalpur-gas-pipeline-work.html, 25 Mar 2026; pipeline-journal.net/news/gail-completes-nagpur-jabalpur-pipeline-boost-central-india-energy-grid). No commissioning report was found.

### Srikakulam–Angul (SAPL), GAIL. Map status: partly operational
- HLEC: 690 km, 6.65 MMSCMD, under construction [primary]. GAIL scope is 744 km: a 422 km main line plus 322 km of spurs.
- The main line was **commissioned on 26 Sep 2025**. Completion of the spurs moved from Dec 2025 to **Jun 2026**, approved by the board on 3 Jan 2026, because forest permission was delayed for 56 km. GAIL said no additional investment is needed [primary-via-summary] (gailonline.com/pdf/InvestorsZone/GeneralDisclosure/Revision_in_Completion_Schedule_SAPL_Letter_dated_03_01_2026.pdf, 3 Jan 2026).
- 280 km of spur laid, 42 km pending [press] (scanx.trade/stock-market-news/stocks/gail-revises-srikakulam-angul-pipeline-project-completion-schedule-to-june-2026/28984637; indianmasterminds.com, Jan 2026). The original target was June 2025 [primary-via-summary] (GAIL SEBI disclosure 23.06.2025).
- PNGRB MIS Nov 2025: 690 km authorised, 422 km operating [primary-via-summary] (pngrb.gov.in/data-bank/20251130-NGPL-MIS-Report.pdf).

### Jagdishpur–Haldia–Bokaro–Dhamra (JHBDPL, "Urja Ganga") and Barauni–Guwahati, GAIL. Map status: all trunk sections operational except Dhamra–Haldia (partly operational)
- HLEC: 3,546 km, 23 MMSCMD, 3,270 km operational, partially commissioned [primary].
- Apr 2025: 97.6% laid and 96.6% in commercial operation. Durgapur–Haldia (294 km): 132 km to Kolkata commissioned, 103 of the remaining 162 km laid. Dhamra–Haldia: 198 of 240 km done. Both targets moved from Mar 2025 to Dec 2025 because of RoU problems [primary-via-summary] (gailonline.com/PressRelease_09042025.html; tribuneindia.com/news/business/gail-completes-laying-over-97-6-pipeline-of-pradhan-mantri-urja-ganga, Apr 2025).
- PNGRB MIS Jan 2026: 3,546 km authorised, **3,279 km operating, 267 km u/c**, target Dec-25 (missed) [primary-via-summary] (pngrb.gov.in/data-bank/20260131-NGPL-MIS-Report.pdf). This was 3,272 km operating in Jul 2025.
- The Haldia sections were moved again, from Mar 2026 to **Sep 2026** (RoU and fisheries fronts). GAIL AR FY26 lists "162 km Kolkata–Haldia section" commissioned and "99 km out of 253 km of Dhamra–Haldia pipeline in West Bengal" [primary-via-summary] (GAIL Q3 FY26 earnings call 2 Feb 2026, gailonline.com/pdf/InvestorsZone/GAIL_Earnings_Call_Q3_FY_26.pdf; GAIL AR 2025-26). No confirmation was found that Dhamra–Haldia is complete.
- Barauni–Guwahati, 718 km (2024 press) or 729 km (GAIL 2019), about 2.5 MMSCMD: listed by GAIL in Apr 2025 among the operational segments [primary-via-summary]. PM dedication reported for March 2024 [press] (indianchemicalnews.com, Mar 2024; gailonline.com/PressRelease17022019.html). The dedication ceremony itself was not independently confirmed.

### Dabhol–Bangalore (DBPL), GAIL. Map status: partly operational
- HLEC: 1,414 km, 16 MMSCMD, 1,148 km operational, partially commissioned [primary].
- PNGRB MIS Jul 2025: 1,148 km operating, 266 km u/c, target "Feb-13", which is stale and probably a data error [primary-via-summary] (pngrb.gov.in/data-bank/20250731-NGPL-MIS-Report.pdf).
- The trunk was commissioned in Feb 2013 at about Rs 4,500 cr [press] (deccanherald.com/business/gail-commissions-dabhol-bangalore-gas-2243530). No 2025-26 update was found. The unbuilt 266 km are probably spurs, but their location was not verified.

### Kochi–Koottanad–Bangalore–Mangalore (KKBMPL), GAIL. Map status: Kochi–Mangaluru operational; Koottanad–Bengaluru under construction
- HLEC: 1,104 km, 16 MMSCMD, 644 km operational, partially commissioned [primary].
- MIS Nov 2025: 644 km op, 460 km u/c, target Dec-25. MIS Jan 2026: 675 km op, 429 km u/c, target Dec-25 [primary-via-summary].
- Jan 2026: completion moved from Dec 2025 to **Mar 2026** because hindrance-free fronts were not available; 884 km laid, 628 km commissioned [press] (scanx.trade/stock-market-news/stocks/gail-revises-kkbmpl-pipeline-project-completion-schedule-to-march-2026/28984944).
- 13 Apr 2026 filing: schedule extended again. **1,104 km authorised, 951 km under execution, 919 km laid, 657 km commissioned.** The new date was not visible in the snippet [primary-via-summary] (nsearchives.nseindia.com/corporate/Himanshugail_13042026185455_KKBMPL_S.pdf).
- Kochi–Mangaluru was completed in Dec 2020 [press] (indianinfrastructure.com/2020/12/31/gail-completes-kochi-mangalore-natural-gas-pipeline/).

### Ennore–Tuticorin (ETBPNMTPL), IOCL. Map status: coastal trunk operational; Bengaluru/Madurai branches under construction (assumed split)
- HLEC: 1,431 km, 84.67 MMSCMD, 1,080 km operational, partially commissioned [primary].
- MIS Nov 2025: **1,094 km op, 337 km u/c**, target Mar-25 (passed) [primary-via-summary].
- IOCL: the Ennore–Tuticorin–Bengaluru RLNG pipeline was commissioned in phases from 2019 to 2023, is now 1,094 km, with 34.67 MMSCMD installed [primary-via-summary] (iocl.com/gas-pipelines). The IOCL capacity schedules for Apr 2025 to Aug 2026 show trunk capacity unchanged and exit points rising from 19 to 27 [primary-via-summary] (iocl.com/Uploads/Schedule1ETBPNMTPLOCTaugust26.pdf).
- PRAGATI review item, 10 Jan 2026: about 1,400 km integrated trunk [press-via-summary] (newsonair.gov.in, blocked domain, not fetched).
- **Assumption:** the unbuilt 337 km lie on the Bengaluru and Madurai branches. This was not verified.

### Mehsana–Bhatinda (MBPL), GIGL. Map status: partly operational
- HLEC: 1,940 km, 80.11 MMSCMD, 1,200 km op [primary].
- MIS Jan 2026: **1,943 km auth, 1,318 km op, 624 km u/c, target Jun-26** [primary-via-summary] (pngrb.gov.in/data-bank/20260131-NGPL-MIS-Report.pdf). No 2026 completion report was found.
- GSPL board approved further equity in GIGL in Nov 2025 [press-via-summary].

### Bhatinda–Gurdaspur, GIGL. Map status: partly operational
- HLEC: 261 km, 42.42 MMSCMD, 102 km op [primary].
- MIS Jan 2026: 261 km, **101 km op, 160 km u/c**, target Dec-24 (stale) [primary-via-summary].

### Gurdaspur–Jammu, GAIL. Map status: under construction
- HLEC: 160 km, 3.10 MMSCMD, u/c [primary].
- PNGRB MIS Jun 2025: expected Jul 2026 [primary-via-summary].
- About 90% complete, GAIL citing July 2026 [press] (ibtimes.co.in, undated: "Jammu set to get piped cooking gas this year; Gurdaspur–Jammu pipeline nears completion"). Daily Excelsior notes "official silence" [press] (dailyexcelsior.com/gas-grid-uncertainty/). Cost about Rs 237 cr for the J&K portion [press]. Authorised mid-2023 after the Bhatinda–Jammu–Srinagar authorisation was cancelled [press] (indianinfrastructure.com/2023/07/29/…).

### Mallavaram–Bhopal–Bhilwara–Vijaipur (MBBVPL), GITL. Map status: 365 km operational; remainder "under construction" (stalled)
- HLEC: 1,881 km, 78.25 MMSCMD, 365 km op, partially commissioned [primary].
- MIS Jan 2026: 1,881 km, **365 km op, 1,517 km u/c, target Mar-20** (stale) [primary-via-summary].
- The GEM tracker puts the operating Phase I between Kunchanapalli and Ramagundam (365 km) and Phase II at 1,517 km. It gives no completion date [secondary] (gem.wiki/Mallavaram_-_Bhopal_-_Bhilwara_-_Vijaipur_Gas_Pipeline). No 2025-26 progress news was found.

### Indradhanush North-East Gas Grid (NEGG), IGGL. Map status: Guwahati–Numaligarh and Phase I link operational; hill sections under construction
- HLEC: 1,656 km, 4.75 MMSCMD, u/c [primary].
- PNGRB press note, 3 Dec 2025: **396 km Guwahati–Numaligarh commissioned in Jul 2025** and connected to NRL. Authorised length 1,688 km, with full commissioning planned for 31 Mar 2026 [primary-via-summary] (pngrb.gov.in/pdf/press-note/20251203_PR.pdf).
- **Phase I (~553 km, Assam/Arunachal/Nagaland) inaugurated 13 Mar 2026** [press] (indianinfrastructure.com/2026/03/16/capacity-augmentation-of-numaligarh-siliguri-product-pipeline-and-phase-i-of-north-east-gas-grid-witnesses-inauguration/).
- The Tripura segment (253 km) was targeted for Mar 2025 [press] (sentinelassam.com). No status was found for the Agartala, Silchar, Shillong, Imphal or Aizawl sections. The GAIL/Others u/c figure in PPAC (3,797 km "Others" incl. IGGL) suggests most of the grid was still unbuilt at end-2025.

### Kakinada–Vijayawada–Nellore, IMC. Map status: authorised, not started
- HLEC T12.8: 667 km, 18 MMSCMD, printed "Under construction", no operational km [primary]. HLEC Annexure 6.1.3 says it is authorised but unexecuted or delayed, with siting issues, and proposes the Kadapa–Chittoor realignment [primary].
- MIS Nov 2025 to Jan 2026: 667 km, 0 km op, target Mar-24 [primary-via-summary]. Authorised 19.02.2018; original target Mar 2021; extension sought to Mar 2024 [primary-via-summary] (rsdebate.nic.in PQ 258, 19.12.2022).

### Ennore–Nellore, GTIL. Map status: authorised, not started (cancelled)
- HLEC T12.8: 220 km, 36 MMSCMD, "Under construction" [primary]. MIS Jan 2026: target Apr-20, 0 km op [primary-via-summary].
- GEM: PNGRB cancelled the authorisation in Oct 2019, and APTEL upheld the cancellation on 4 Oct 2023 [secondary] (gem.wiki/Ennore-Nellore_Gas_Pipeline). The project is effectively shelved.

### Kanai Chhata–Panitar, HPPL (H-Energy consortium). Map status: authorised, not started
- HLEC T12.8: 317 km, 19.20 MMSCMD, "Under construction". HLEC proposes the Digha–Kolkata–Paschim Medinipur alternate [primary].
- MIS Jan 2026: 0 km op, target Mar-24 [primary-via-summary]. No other news was found. Endpoint coordinates in routes.json are rough.

### Hazaribagh–Ranchi, IOCL. Map status: under construction
- HLEC T12.8: 65 km, 1.03 MMSCMD, u/c [primary]. GEM: authorised 2023, under construction, start year 2026 [secondary] (gem.wiki/Hazaribagh-Ranchi_Gas_Pipeline). No commissioning report was found.

### Jamnagar–Dwarka, GSPL. Map status: under construction
- HLEC T12.8: 100 km, 3 MMSCMD, u/c [primary]. MIS Dec 2025 and Jan 2026: authorised 19.08.2021, **expected Oct-26** [primary-via-summary]. No commissioning news was found as of 23 Oct 2026.

---

## 4. routes.json: what is in it

There are 70 objects: **25 operational, 6 partly operational, 9 under construction, 5 authorised not started, 25 proposed**. That is more than the target of 30–45, for two reasons:

- The brief asked for every proposed line in Annexure 6.1.3: the 21 Table 12.10 projects, Barmer–Churu, the two Table 12.9 alternates not already in Table 12.10, and Jabalpur–Shahdol.
- Multi-status systems (MNJPL, JHBDPL, KKBMPL, MBBVPL, ETBPNMTPL, NEGG) are split into segments.

The 45 non-proposed objects alone fall within the target range.

Schema extras:
- `coords: "approximate"` on every object, because JSON has no header comment.
- Optional `system` to group segments.
- Optional `notes`.

`auth_km`, `built_km` and capacity are given only where a source states them; segments of a system carry `null`, and the system totals appear in `notes`. Proposed lines carry the 2040 BAU flow in `capacity_mmscmd` and `entity: "unassigned"`.

Choices to review before publishing:
1. **MNJPL Maharashtra section**: the GAIL sources conflict (see above).
2. **KVN, Ennore–Nellore and Kanai Chhata–Panitar** are coded `authorised_not_started` even though HLEC and PNGRB print "Under construction". All three show 0 km built, and HLEC's own text calls them unexecuted or delayed.
3. **MBBVPL remainder** is coded `under_construction` per PNGRB, but it has effectively stalled since its 2020 target.
4. **Kakinada–Srikakulam and Jaigarh–Mangalore** come only from the HLEC list of authorised but unexecuted lines. Their entities (APGDC and H-Energy) and the absent lengths are from general knowledge, not the local sources.
5. **Waypoint gaps:** places such as Amliha, Godhi, Vadap, Gambegre, Kanai Chhata and Panitar are unlocated or approximate. Spurs are not drawn.
6. Not drawn as separate lines: Mumbai Regional, Uran–Trombay, Uran–Taloja, Hazira–Ankleshwar, Baroda/Gujarat regional, Agartala regional and Dukli–Maharajganj. All are small regional lines listed in the tables above.
