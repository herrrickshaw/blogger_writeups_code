# 03 — Cost, schedule and tariff benchmarks for LNG regas capacity (research notes, 23 Oct 2026)

Scope: global capex and schedule benchmarks (onshore greenfield, brownfield expansion, FSRU, GBS), LNG tank costs,
Indian regas tariffs and the economics of utilisation, and the regas capacity implied by India's demand projections.

## Method and source notes (read first)

- **Network limits.** WebFetch and curl could not reach any outside page from this environment: DNS failed and the
  proxy returned 403s, including for oxfordenergy.org, business-standard.com and petronetlng.in. So every web figure
  below comes from a **WebSearch result summary**, not from the page itself. Each line names the URL the summary cited.
  Treat these as "reported by" until someone checks the page. No *.gov.in page was opened.
- **Google Drive sources that were read in full:**
  - `World LNG report.pdf` (Drive id 18tUS9fclmyMC7ut-h-EFgT7B7DV88E6o) is **not the IGU World LNG Report**. Its text
    is the **GIIGNL Annual Report 2025 Edition** (2024 data). It is cited below as "GIIGNL 2025". [secondary]
  - `20250407_NG_Projections2030_40.md` (Drive id 1RLw1lXHpGDDeVqbOLGULnh9gISniEVvy) is the PNGRB paper
    "NG Demand projections for 2030 and 2040" (Apr 2025). Page numbers are taken from its page footers. [primary]
  - `20250609_CSR.pdf` (Drive id 10EQb_DygC47oeqHyHDNQ12pkFXKsT8VR) is the PNGRB slide version of the same projections
    (Jun 2025). [primary]
  - `LNG India Summit 2025 - Post event report.md` (Drive id 16TZ8BdjWTFc5ywlCm8ncoYXKdNEHGzCT) is by ICF for LNG India
    Summit 9 (2025). [secondary]
- **Exchange rates.** These are the author's assumptions, not sourced rates, and every conversion uses one of them:
  - ₹68/USD for spend in 2014–19
  - ₹74/USD for 2021
  - ₹75/USD as the average over 2017–23 construction periods
  - ₹78/USD as the average over 2021–24
  - ₹83/USD for 2024
  - ₹88/USD for 2025–26
  - USD 1.08/EUR
  - Argus used its own rate, ₹52.05 = USD 0.58 (about ₹89.7/USD), in Dec 2025.
- **Unit conversions** (assumptions):
  - 1 MTPA = 3.605 mmscmd. This is implied by PNGRB's "~190 MMSCMD (52.7 MMTPA)" (PNGRB Apr 2025, p.21).
  - 1 MTPA ≈ 1.36 bcm/yr, so 1 bcm ≈ 0.735 MTPA.
  - 1 t LNG ≈ 52 MMBtu. This is a rounded value; it varies by about ±2% with gas composition.
- **"My arithmetic"** marks a number I derived. It is not a published figure.

---

## 1. Capex benchmarks

### 1a. Headline table — capex per tonne per annum (USD/tpa) of regas capacity

| # | Project / benchmark | Type | Capacity added | Reported cost | USD/tpa (my arithmetic) | Date of cost | Tag & source |
|---|---|---|---|---|---|---|---|
| 1 | Generic 3 MTPA onshore terminal with one 180,000 m³ tank | Onshore greenfield | 3 MTPA | USD 700–800 m | 233–267 | 2017 | [secondary] OIES NG 123 "Outlook for FSRUs" (Jul 2017), via search summary of oxfordenergy.org PDF |
| 2 | Generic FSRU terminal of similar capacity | FSRU (vessel + infra) | ~3 MTPA | USD 400–500 m; "~50–60% of onshore" | 133–167 | 2017 | [secondary] same OIES NG 123, via search summary |
| 3 | Thi Vai (PV Gas, Vietnam), phase 1, one 180,000 m³ tank | Onshore greenfield | 1 MTPA (GIIGNL table: 1.1) | USD 285 m (GEM) / 286 m / ~300 m at inauguration | 260–300 | 2019–23 | [press] gem.wiki/Thi_Vai_LNG_Terminal; theinvestor.vn (Oct 2023) |
| 4 | Dhamra (Adani–TotalEnergies, Odisha) | Onshore greenfield | 5 MTPA | ₹6,450 cr (earlier ₹5,500 cr in 2016; ₹6,000 cr at groundbreaking) | ~172 at ₹75 | 2017–23 | [press] businesstoday.in / outlookbusiness.com (29 Oct 2023) |
| 5 | Chhara (HPCL, Gujarat) | Onshore greenfield (incl. jetty and breakwater scope; exact scope unverified) | 5 MTPA | ~₹4,300 cr | ~115 at ₹75 | c.2019–20 estimate | [press] search summary of shippingtribune / newsonprojects-type reports; final cost not found |
| 6 | Ennore (IOC, Tamil Nadu), original terminal | Onshore greenfield | 5 MTPA | "~₹5,000 cr" (a parliamentarian's comparison, quoted in press) | ~147 at ₹68 | 2014–19 | [press] outlookbusiness.com (Oct 2023). Could not verify the ₹5,151 cr figure |
| 7 | South Richards Bay (South Africa), proposed | FSRU-based / onshore mix | 2 MTPA | >ZAR 7 bn (USD 372 m) | ~186 | 2024–25 | [press] clubofmozambique.com, via search summary |
| 8 | South Korea: 11 projects, ~37 MTPA | Mostly onshore | ~37 MTPA | KRW 11.3 tn (USD 8.7 bn) | ~235 | 2023–24 | [secondary] IEEFA "South Korea's LNG overbuild", via search summary |
| 9 | Dunkerque LNG (France) | Onshore greenfield, 3 × 190,000 m³ | 13 bcm/yr (GIIGNL: 9.6 MTPA) | €1.0 bn terminal + €0.15 bn port works + €0.08 bn grid link = €1.23 bn | ~€128 ≈ USD 138 | FID 2011 | [primary] EDF "Dunkerque LNG presentation" (edf.fr PDF), via search summary; capacity from GIIGNL 2025 table |
| 10 | Brunsbüttel onshore (German LNG Terminal, KfW/Gasunie/RWE) | Onshore greenfield | 10 bcm/yr (~7.35 MTPA) | ~€1.5 bn initial estimate, now "nearly €1.9 bn" (OSW, 4 Nov 2024); CAP gives €1.3 bn | €204–258 ≈ USD 220–280 (CAP figure: €177) | 2024 | [secondary] osw.waw.pl (4 Nov 2024); [secondary] americanprogress.org. **Conflict**, see below |
| 11 | Stade (Hanseatic Energy Hub) | Onshore greenfield, 2 × 240,000 m³ | 13.3 bcm/yr (~9.8 MTPA) | ~€1 bn | ~€102 ≈ USD 110 | 2024 | [secondary] americanprogress.org (advocacy source); tank and capacity data from GIIGNL 2025, p.49. Cost unconfirmed elsewhere |
| 12 | Adriatic LNG (Italy) | GBS offshore, 2 steel tanks in a concrete caisson | 8 bcm/yr (~5.9 MTPA) | USD 900 m EPC (Aker Kvaerner, May 2004), incl. USD 200 m caisson subcontract; total capex not found | ≥153 (EPC only) | 2004 | [press] enr.com; lngindustry.com (2009), via search summary |
| 13 | Dahej 17.5 → 22.5 MTPA (Petronet) | **Brownfield**: send-out ₹560–600 cr + 2 tanks ₹1,250 cr | +5 MTPA | ≈ ₹1,810–1,850 cr in total | ~44 at ₹83 | 2021–26 | [press] Business Standard (via search summary): ₹560 cr, completed 2 months early; [press] indianchemicalnews.com: ₹570 cr; [press] search summary: tanks ₹1,250 cr and expansion ₹600 cr |
| 14 | Ennore 5 → 10 MTPA (IndianOil LNG), within the existing Kamarajar Port site | **Brownfield** | +5 MTPA | ₹3,400 cr (≈ USD 408 m per 2023 report) | ~77–82 | approved Jul 2026 | [press] propnewstime / shippingtribune / offshore-technology.com (2023: "USD 408 m"). Scope (number of tanks) not confirmed |
| 15 | Świnoujście stage 1+2 (Poland): 180,000 m³ tank, 2nd jetty, regas 3.7 → 6.1 MTPA | **Brownfield** (incl. jetty) | +2.4 MTPA | PLN 1.7–1.9 bn (≈ USD 483–512 m) | ~200–213 | 2020–24 | [press] search summary of Polish press and GEM (contract USD 483 m, Jun 2020); capacity from GIIGNL 2025, p.50 and table |
| 16 | Gate (Rotterdam): 4th tank 180,000 m³ + 1.5 bcm/yr extra send-out | **Brownfield** | +1.1 MTPA send-out (GIIGNL table) | ~€350 m in total; tank EPC (Vinci) €160 m | ~€318 ≈ USD 340, but mostly storage, not send-out | FID 2023 | [press] lngprime.com; gasunie.nl, via search summary |
| 17 | Revithoussa (Greece): 3rd tank 95,000 m³ + upgrade | **Brownfield** | +1.5 MTPA (GIIGNL table, 2018) | Tank €98 m; project €143 m (Greek News Agenda) or €195.6 m (EU Inforegio, phase 2) | €95–130 ≈ USD 103–141 | to 2018 | [press] stroumboulis.gr; [primary] ec.europa.eu Inforegio. **Conflict** on project total |
| 18 | Montoir "Ulysse" project (replacing gas-fired vaporisers with water-based ones) | Brownfield retrofit, no capacity added | 0 | €220 m, to 2031 | n/a | 2025 | [secondary] GIIGNL 2025, p.49 |
| 19 | Zeebrugge: 3 extra ORVs | Brownfield send-out only | +1 MTPA (to 12.3) | not disclosed | n/a | done 1 Jan 2025, a year early | [secondary] GIIGNL 2025, p.49 |

**Reading the table.** In practice, a brownfield send-out-plus-tank expansion at a site that already has jetties and
evacuation costs well under half of a greenfield terminal per tpa.

- Dahej came in at about USD 44/tpa (row 13) and Ennore at about USD 80/tpa (row 14).
- Indian greenfield onshore terminals came in at about USD 115–175/tpa (rows 4–6).
- European and other greenfield onshore terminals came in at about USD 140–300/tpa (rows 1, 3, 8–10). (My arithmetic.)
- European brownfield projects that also add a jetty (Świnoujście) or a large tank (Gate) cost about USD 200–340/tpa.
  That is because they add storage or berths, not only send-out.

### 1b. FSRU costs

| Item | Figure | Date | Tag & source |
|---|---|---|---|
| Newbuild FSRU, 170,000 m³ (HD Hyundai Heavy) | ~USD 364 m, delivery Jul 2027 ("highest to date") | 2024 order | [press] lngprime.com |
| Newbuild FSRU (Excelerate at HHI) | ~USD 332 m | 2022 order | [press] lngprime.com, via search summary |
| Newbuild FSRU market estimate (Energos) | USD 320–340 m | c.2024–25 | [press] rivieramm.com, via search summary |
| Converting a steam-turbine LNG carrier to an FSRU | USD 200–220 m; a large tri-fuel 165–170k m³ ship ≈ USD 250 m | c.2024–25 | [press] rivieramm.com (Energos), via search summary |
| Second-hand purchase: FSRU *Independence* (Klaipėda, 2.9 MTPA) | USD 153.5 m (KN Energies from Höegh Evi, at end of 10-yr lease) | Dec 2024 | [secondary] GIIGNL 2025, p.49 |
| Older benchmark for newbuild FSRUs | USD 250–300 m | 2017 | [secondary] OIES NG 123, via search summary |
| FSRU charter, Bangladesh Moheshkhali (Excelerate, 138,000 m³, 3.8 MTPA nameplate; 4.5 MTPA after 2024 upgrade per GEM) | USD 254,000/day | 2025–26 | [press] thedailystar.net; gem.wiki |
| FSRU charter, Bangladesh (Summit LNG) | USD 249,115/day | 2025–26 | [press] thedailystar.net |
| Proposed third Bangladesh FSRU (CNEE, China) | USD 342,000/day (15-yr) or 329,000/day (20-yr). Stalled or withdrawn: **sources conflict** | Oct 2026 | [press] dailywaadaa.com (18 Oct 2026); tob.news |
| Average charter cost of a German federal FSRU | ~€55 m net per FSRU per year (≈ €150,700/day) | 2023–24 | [secondary, advocacy] americanprogress.org |
| Older charter range | USD 110–160 k/day | 2017 | [secondary] OIES NG 123, via search summary |
| Industry charter range | USD 80–120 k/day, rising after 2022 | c.2025 | [press] shipfinex.com blog (low weight) |
| Assumed FSRU charter rate in a planning study | USD 150 k/day, against ~USD 300 m to buy | Jan 2025 | [secondary] FGE deck for Hawai'i State Energy Office (energy.hawaii.gov) |
| Implied vessel cost per MMBtu, Moheshkhali at USD 254k/day | USD 0.47/MMBtu at 3.8 MTPA, or 0.40 at 4.5 MTPA, at 100% use. **Doubles at 50% use.** Excludes jetty, O&M and fuel | 2025–26 | my arithmetic |
| Same, German FSRU at €55 m/yr, ~3.6 MTPA | ~€0.29/MMBtu at 100% use | 2023–24 | my arithmetic |
| Germany: all four state-chartered FSRUs (DET), net operating support 2023–33 | €4.06 bn (up to €4.96 bn) approved by the EC | Jan 2025 | [press] lngindustry.com (2 Jan 2025) reporting an EC state-aid approval; EC decision itself not opened |
| Germany: original budget line for 4 FSRU charters plus infrastructure | €2.04 bn (USD 3 bn) | May 2022 | [press] maritime-executive.com |
| Germany: public investment in FSRU sites | ~€6.9 bn; ≥€16.8 bn worst case incl. guarantees | 2024 | [secondary, advocacy] americanprogress.org |
| Wilhelmshaven 1: Uniper's own onshore and jetty works | ~€65 m | 2022 | [press] marinelink / lngprime, via search summary |
| Aqaba (Jordan): terminal modernisation incl. an onshore regas unit next to the FSU | USD 125 m | Aug 2024 | [secondary] GIIGNL 2025, p.50 |
| Bangladesh: existing offshore FSRU terminal vs a proposed onshore terminal | ~USD 500 m vs ~USD 1 bn | c.2021–23 | [secondary] IEEFA "Floating LNG import terminals pose cost and climate challenges", via search summary |
| IEEFA rule of thumb | onshore ">USD 1 bn", FSRUs "<USD 100 m" (excl. vessel; "highly site-specific") | 2021–23 | [secondary] IEEFA, as above |

**Quayside infrastructure.** No clean, comparable figure was found. The data points are:

- Uniper's ~€65 m at Wilhelmshaven.
- Jordan's USD 125 m.
- OIES says jetty and infrastructure costs "vary considerably on each project depending on the scope" (OIES NG 149,
  2019, via search summary). [secondary]
- Ravenna (Italy) shows how large the scope can get: platform, breakwater, an 8.5 km subsea line plus 2.5 km and
  31.5 km onshore lines (GIIGNL 2025, p.49). [secondary]

### 1c. LNG storage tanks: cost per m³ and storage per MTPA

| Item | Figure | USD/m³ (my arithmetic) | Tag & source |
|---|---|---|---|
| Dahej: 2 tanks, ₹1,250 cr. GIIGNL says 2 × 180,000 m³; L&T order reports say 2 × 170,000 m³ (**conflict**) | ₹34,700/m³ (on 360k m³) | ~USD 445 at ₹78 | [press] search summary; [secondary] GIIGNL 2025, p.47 (two 180,000 m³ tanks commissioned Oct 2024; Dahej now 8 tanks, 1,272,000 m³) |
| Dahej: L&T EPC order for the same 2 tanks | ">₹1,000 cr" → ≈ ₹29,400/m³ on 340k m³ | ~USD 397 at ₹74 | [press] businesstoday.in (20 Sep 2021) |
| Gate (Rotterdam): 4th tank, 180,000 m³, Vinci EPC | €160 m → €889/m³ | ~USD 960 | [press] lngprime.com |
| Revithoussa: 3rd tank, 95,000 m³ | €98 m → €1,032/m³ | ~USD 1,115 (small tank, so poor economies of scale) | [press] stroumboulis.gr, via search summary |
| Świnoujście: 180,000 m³ tank | not split out from the jetty package | n/a | [press] |

**Takeaway.** In Indian brownfield conditions, a 180k m³ full-containment tank cost roughly USD 400–450/m³ (2021–24
money). The European equivalent was about USD 900–1,100/m³. That puts a 180k m³ tank at roughly ₹600–650 cr in India
and €160 m in NW Europe. (My arithmetic, from two data points each; **thin evidence**.)

**Storage per MTPA** (my arithmetic, from GIIGNL 2025 terminal tables pp.55–56 and the Europe tables) [secondary]:

| Terminal | Storage | Capacity | Storage per MTPA |
|---|---|---|---|
| Dahej | 1,272k m³ | 22.5 MTPA | 57k m³ (73k m³ at 17.5 MTPA) |
| Kochi | 310k m³ | 5 MTPA | 62k m³ |
| Mundra | 320k m³ | 5 MTPA | 64k m³ |
| Hazira | 320k m³ | 5.2 MTPA | 62k m³ |
| Ennore | 360k m³ | 5 MTPA | 72k m³ |
| Dhamra | 360k m³ | 5 MTPA | 72k m³ |
| Chhara | 2 × 200k m³ | 5 MTPA | 80k m³ |
| Dabhol | 480k m³ | 5 MTPA | 96k m³ |
| Gate | 540k m³ | ~9.9 MTPA | 55k m³ |
| Dunkerque | 600k m³ | 9.6 MTPA | 63k m³ |
| Grain | 1,000k m³ | 14.3 MTPA | 70k m³ |
| Świnoujście | 500k m³ | 6.1 MTPA | 82k m³ |
| Thi Vai | 180k m³ | 1.1 MTPA | 164k m³ |

**Rule of thumb.** About 55–95k m³ per MTPA, i.e. two 160–200k m³ tanks per 5 MTPA. Small terminals carry far more
storage per MTPA. An FSRU holds 138–174k m³ for 3.6–6 MTPA, which is only about 30–40k m³ per MTPA.

---

## 2. Schedule benchmarks (months from FID or construction start to first gas or COD)

| Project | Type | Milestone A | Milestone B | Months (my arithmetic) | Tag & source |
|---|---|---|---|---|---|
| Wilhelmshaven 1 (Höegh Esperanza) | FSRU, new jetty | Preliminary works May 2022; official start 4 Jul 2022 | First gas 22 Dec 2022 | **~5.5–7** | [press] S&P Global (19 Dec 2022); maritime-executive; lngprime |
| Engro Elengy (Port Qasim, Pakistan) | FSRU, new jetty | Build start (date not found) | Ops 29 Mar 2015 | **~11** ("330" / "332 days" in Engro's own two statements) | [primary] engro.com; [secondary] PACRA rating report |
| Egypt (Ain Sokhna, 2015) | FSRU | Tender issued | Gas delivered | **~5** | [secondary] Oxford working paper (ora.ox.ac.uk), via search summary |
| Industry range (MOL, via Kpler) | FSRU vs onshore | — | — | FSRU 7–24; onshore ≥36–48 | [secondary] kpler.com blog (2 Jun 2023) |
| Jafrabad (Swan, Gujarat) | **FSRU, India** | Approved 2016, planned COD 2019 | Not operating as of 2023 reports; FSRU leased to BOTAS (Türkiye) instead | **>84 and counting** | [press] gem.wiki/Jafrabad_FSRU |
| Thi Vai (Vietnam) | Onshore greenfield, 1 tank | Construction Oct 2019 | Inaugurated Oct 2023 (was planned for 2022) | **~48** | [press] gem.wiki; theinvestor.vn |
| Chhara (HPCL) | Onshore greenfield | EPC to Toyo Jul 2019; construction Aug 2019 | Commissioning announced 13 Jan 2025 (delays: evacuation pipeline, fender failure, unfinished breakwater) | **~65** | [press] lngprime.com; argusmedia.com; Wikipedia citing Business Standard; [secondary] GIIGNL 2025, p.47 (commercial ops Feb 2025) |
| Dhamra (Adani–TotalEnergies) | Onshore greenfield | Groundbreaking 2017 (month not confirmed) | COD 21 May 2023 | **~70–76** | [press] enerdata; businesstoday.in |
| Dunkerque LNG | Onshore greenfield | FID 27 Jun 2011 | Industrial operation scheduled end-2016 (actual COD date not verified) | **~66 (planned)** | [primary] EDF presentation, via search summary |
| Brunsbüttel onshore | Onshore greenfield (replacing an FSRU at the same site) | FID Oct 2024 | Start expected 2027 | **~36 (planned)** | [secondary] GIIGNL 2025, p.50; osw.waw.pl |
| Stade (HEH) | Onshore greenfield | Construction start Jun 2024 | Start planned 2027 | **~36 (planned)**. GIIGNL notes the parallel Stade FSRU start "delayed due to technical issues" | [secondary] GIIGNL 2025, p.49 |
| Dahej: 2 new 180k m³ tanks | **Brownfield tanks** | L&T order Sep 2021 | Commissioned Oct 2024 | **~37** | [press] businesstoday.in; [secondary] GIIGNL 2025, p.47 |
| Dahej 17.5 → 22.5 MTPA send-out | **Brownfield send-out** | Under construction by May 2022 (GEM) | Commissioned 31 Mar 2026, "two months ahead of schedule" | **≥46 from the May 2022 status date** | [press] whalesbook.com; Business Standard, via search summary; gem.wiki |
| Ennore 5 → 10 MTPA | **Brownfield** | Board approval | "within 54 months of board approval" (planned) | **54 (planned)** | [press] tradebrains / newsonprojects (Jul 2026) |
| Gate 4th tank | **Brownfield tank** | Construction start Aug 2023 (FID 2023) | Operation H2 2026 | **~36** | [press] gasunie.nl; lngprime.com |
| Świnoujście stage 2 (tank + jetty) | **Brownfield tank + jetty** | Contract Jun 2020 | Completed Dec 2024 | **~54** | [press] gem.wiki; [secondary] GIIGNL 2025, p.50 |
| Zeebrugge: 3 ORVs | Brownfield send-out only | — | Done 1 Jan 2025, scheduled for early 2026 | about 12 months early | [secondary] GIIGNL 2025, p.49 |

**Pattern (my synthesis):**

- **FSRU:** 5–12 months where a government forces the pace (Germany, Pakistan, Egypt). But an Indian merchant FSRU
  (Jafrabad) has been stuck for more than 7 years. Speed comes from offtake and evacuation, not from the hull.
- **Onshore greenfield:** about 48 months at best (Thi Vai), and 65–76 months in India (Chhara, Dhamra), with delays
  driven by breakwaters, pipelines and jetties.
- **Brownfield tank or send-out:** 36–54 months. The tank is the critical path (about 36–37 months, both at Dahej and
  Gate). Send-out-only debottlenecking (ORVs, SCVs) is faster.

---

## 3. Indian regas tariffs and framework

### 3a. Tariffs

| Terminal | Tariff (₹/MMBtu) | Period | Escalation / notes | Tag & source |
|---|---|---|---|---|
| Dahej (Petronet) | 62.91 | 2024 | 5% a year | [press] argusmedia.com "India's higher LNG regas rates receive customer flak" |
| Dahej | 63.7 (FY25); 66.9 (FY26E) | FY25–26 | Brokerage model | [secondary] plindia.com PLNG note (29 Jan 2025) / dsij-hosted broker note (19 Nov 2025) |
| Dahej | 66.06 current; 69.36 projected for 2026 | c.Dec 2025 | "5pc annual rise" | [press] argusmedia.com "India's Petronet offers lower LNG regas rates" |
| Dahej escalation assumption | 5% a year to FY28, flat after | Jan 2025 | Analyst assumption, not a contract term | [secondary] JM Financial PLNG note (3 Jan 2025) |
| Dahej expansion capacity offered to GAIL | **52.05** (USD 0.58), >25% below 66.06. GAIL booked 1.5 of the new 5 MTPA | c.Dec 2025 | Marginal brownfield pricing | [press] argusmedia.com (same) |
| Dahej, analyst view | Motilal Oswal assumes a 5% tariff cut in FY28. Management said the new tariff for the 7.5 MTPA Qatar volumes "will not be lower than the current one" | 2026 | Conflicts with the GAIL discount | [secondary] Motilal Oswal via tradingview/moneycontrol |
| Kochi (Petronet) | **114.5** (to long-term customers; "may be the highest regasification tariffs globally") | c.Dec 2025 | — | [press] argusmedia.com |
| Kochi | 89.3 (FY25); 93.8 (FY26E) | FY25–26 | Brokerage model | [secondary] broker notes as above. **Conflict with Argus 114.5, unresolved** |
| HPCL (Chhara) and IOC (Ennore) | Need ₹83–87/MMBtu at 50% utilisation | Apr 2026 | Nomura, via Business Standard | [press] business-standard.com (4 Apr 2026) |
| Newer terminals vs Dahej | 19–26% above Dahej's current tariff | 2026 | — | [press] business-standard.com (2026), via search summary |
| Hazira, Dabhol, Mundra, Dhamra | **Not found** in usable form | — | — | Gap |
| Dahej tariff in USD | ≈ USD 0.75/MMBtu at ₹88 (Kochi at ₹114.5 ≈ USD 1.30) | 2025–26 | Compare: FSRU vessel-only cost ≈ USD 0.40–0.47/MMBtu at full use (Bangladesh) | my arithmetic |
| Share of delivered price | Regas is "merely around 5% to 6% of delivered gas price" | Jan 2025 | Petronet's reply to PNGRB | [primary] petronetlng.in (reply to PNGRB consultation, 2 Jan 2025), via search summary |

### 3b. Booking terms and framework (key facts only; T4S is already covered on the blog)

- **Not tariff-regulated.** Regas charges are set by bilateral agreements between the operator and capacity holders.
  PNGRB has said it "does not have the regulatory oversight over the regasification terminals and its charges".
  Regulating them would need statutory change. [primary] PNGRB consultation "Optimising LNG Supplies from Terminals in
  India" (Dec 2024), and Petronet's reply (Jan 2025), via search summaries.
- **PNGRB's complaint.** Terminals charge "almost the same" whether utilisation is 95% (Dahej) or below 25%. Mundra ran
  at 14.6% in its first full year. The Dec 2024 paper also counted 7 operational terminals with about 170 mmscmd
  (47.7 MTPA). [primary] PNGRB Dec 2024, via search summary.
- **2025 regulations.** The *Registration for Establishing and Operating LNG Terminals Regulations, 2025* require prior
  PNGRB registration or approval for new terminals and expansions. The criteria include "avoiding infructuous
  investment". The final rules **dropped** the draft requirement to reserve capacity for third-party access (the draft
  had 20% of short-term uncommitted capacity or 0.5 MTPA). [press] deccanherald.com; outlookbusiness.com;
  lawgratis.com (draft).
- **Booking platform.** On 16 Oct 2026 PNGRB approved IGX's voluntary platform for booking regas capacity. Contracts,
  payments and risk stay bilateral. [press] business-standard.com; zeebiz.com.
- **Use-or-pay.** No published use-or-pay percentage or contract term for any Indian terminal was found. GIIGNL notes
  that Chhara runs on a tolling model with "long-term capacity bookings and master regasification agreements for spot
  cargoes" (GIIGNL 2025, p.47). [secondary]
- **Gap between capacity and utilisation (context).**
  - PNGRB: 52.7 MTPA at about 50.5% utilisation in 2023-24. Dahej was at 95.1%; the others were at 14.6–42.7%
    (PNGRB Apr 2025, p.21 table, citing PPAC). [primary]
  - In Apr–Feb FY26 all terminals except Dahej ran at ≤35% (oil ministry data, via Business Standard, 4 Apr 2026).
    [press]
  - Dahej fell to 56% in Mar 2026 after the Strait of Hormuz closure (DAM Capital, via the same article). [press]

### 3c. Unit cost versus utilisation (fixed-cost recovery)

**Published reference points:**
- ICRA (Dec 2025): a 5 MTPA terminal needs regas charges above **₹81/MMBtu** at 30–55% utilisation just to meet debt
  service. Capacity is expected to rise from 52.7 MTPA (end-FY25) to about 77.5 MTPA. [secondary] icra.in "Indian Gas
  Utilities" (Dec 2025), via search summary.
- Nomura: HPCL and IOC terminals need ₹83–87/MMBtu at 50% utilisation. [press] Business Standard (4 Apr 2026).

**Illustrative model (my arithmetic, not sourced).** Assumptions: a 5 MTPA terminal, 260 m MMBtu/yr at 100%,
capital recovery over 25 years at 10–12%, and fixed O&M of 2.5% of capex a year. Variable costs (power, boil-off) are
ignored.

| Capex basis | Fixed cost ₹ cr/yr | 100% | 80% | 50% | 30% | 20% |
|---|---|---|---|---|---|---|
| Dhamra-like greenfield, ₹6,450 cr (12%) | 984 | 38 | 47 | 76 | 126 | 189 |
| Generic greenfield, ₹5,000 cr (12%) | 762 | 29 | 37 | 59 | 98 | 147 |
| Ennore-type brownfield, ₹3,400 cr (12%) | 518 | 20 | 25 | 40 | 67 | 100 |
| Dahej-type brownfield, ₹1,850 cr (12%) | 282 | 11 | 14 | 22 | 36 | 54 |

(Values under 100%–20% are ₹/MMBtu at that utilisation.)

**Cross-checks.** The Dhamra-like row at 50% (₹76) sits close to the ICRA (₹81) and Nomura (₹83–87) figures. The
Dahej-type row explains why Petronet can offer ₹52 for expansion capacity and still earn its cost of capital. Unit
cost scales with 1/utilisation, so a terminal at 20% needs about 4–5× the per-MMBtu charge of one at 90%.

---

## 4. Regas demand: what the projections imply for capacity

### 4a. Inputs

| Item | Figure | Tag & source |
|---|---|---|
| PNGRB gas demand 2030, Good-to-Go (GtG) / Good-to-Best (GtB) | 297 / 365 mmscmd (from 187 in 2024) | [primary] PNGRB Apr 2025, pp.5, 25 (sector table) |
| PNGRB gas demand 2040, GtG / GtB | 495 / 630 mmscmd | [primary] same |
| PNGRB on LNG | "LNG demand is projected to double to ~200 MMSCMD by 2030"; "doubling of LNG imports by 2030" | [primary] PNGRB Apr 2025, pp.20, 25 |
| PNGRB on domestic production | Meets "only ~50%" of demand; no numeric 2030/2040 production projection in the paper | [primary] PNGRB Apr 2025, p.19 |
| PNGRB on capacity | 52.7 MTPA (~190 mmscmd) across 8 onshore terminals at about 50% utilisation; Jafrabad 5 MTPA under construction; Dahej and Dabhol +5 MTPA each planned. "Large-scale investments … should align with industry needs to avoid excess capacity" | [primary] PNGRB Apr 2025, p.21 |
| PNGRB slides | "Adequate Regas capacity already existing in our terminals with expansion underway" | [primary] PNGRB Jun 2025 slides (20250609_CSR), slide 5 |
| Earlier PNGRB estimate | ~87 MTPA regas capacity by 2030 vs LNG import demand of 56 MTPA | [primary, reported] via argusmedia search summary (date not confirmed) |
| Government capacity target | 66.7 MTPA by 2030, from 52.7 (Minister Puri) | [press] argusmedia.com "India to increase LNG import capacity by 2030" (2025) |
| ICRA capacity outlook | to ~77.5 MTPA | [secondary] ICRA (Dec 2025) |
| IEA India Gas Market Report (Feb 2025) | Demand +60% (2023→2030) to ~103 bcm (accelerated case ~120 bcm). LNG imports roughly double from ~36 bcm (2024) to ~65 bcm (2030; Argus says 64). Domestic output just under 38 bcm. New terminals could add ~40 bcm/yr of capacity by 2030. Contracted supply falls short after 2028 | [secondary] iea.org news release and report PDF, via search summary |
| GAIL chairman | ~300 mmscmd by 2030; up to 365 with fiscal support | [press] energyconnects.com (Jan 2026) |
| MoPNG target | Gas at 15% of the primary energy mix by 2030, from ~6.5% | [secondary] ICF / LNG India Summit 2025 report, p.5. MoPNG source not opened (gov.in blocked) |
| India LNG imports 2024 | 27 MT (+23% y/y) | [secondary] GIIGNL 2025, p.11 |
| Global regas capacity | 1,188 MTPA at end-2024; India 47.7 MTPA in the GIIGNL table (before Chhara) | [secondary] GIIGNL 2025, pp.46, 55 |

### 4b. Implied regas capacity (my arithmetic)

Method: LNG need = demand − domestic supply, converted at 3.605 mmscmd per MTPA, then divided by a utilisation
ceiling. Domestic supply is taken as 104 mmscmd (the IEA's 38 bcm for 2030, held flat to 2040) or 130 mmscmd (a
growth case). Both are assumptions; PNGRB gives no production forecast.

| Scenario | Domestic (mmscmd) | LNG need (mmscmd) | LNG need (MTPA) | Capacity @90% | @85% | @80% |
|---|---|---|---|---|---|---|
| PNGRB GtG 2030 | 104 | 193 | 53.5 | 59.5 | **63.0** | 66.9 |
| PNGRB GtG 2030 | 130 | 167 | 46.3 | 51.5 | 54.5 | 57.9 |
| PNGRB GtB 2030 | 104 | 261 | 72.4 | 80.4 | **85.2** | 90.5 |
| PNGRB GtB 2030 | 130 | 235 | 65.2 | 72.4 | 76.7 | 81.5 |
| IEA base 2030 (65 bcm LNG) | — | — | 47.8 | 53.1 | **56.2** | 59.7 |
| IEA accelerated 2030 (120 bcm demand, same domestic) | 104 | — | 60.3 | 67.0 | 70.9 | 75.3 |
| PNGRB GtG 2040 | 104 | 391 | 108.5 | 120.5 | **127.6** | 135.6 |
| PNGRB GtG 2040 | 130 | 365 | 101.2 | 112.5 | 119.1 | 126.6 |
| PNGRB GtB 2040 | 104 | 526 | 145.9 | 162.1 | **171.7** | 182.4 |
| PNGRB GtB 2040 | 130 | 500 | 138.7 | 154.1 | 163.2 | 173.4 |

**Compare with capacity on hand:**
- 52.7 MTPA at end-FY25 (PNGRB); 57.7 MTPA after Dahej reached 22.5 MTPA on 31 Mar 2026 (my sum).
- Government target: 66.7 MTPA by 2030. ICRA pipeline: ~77.5 MTPA.

**Reading (my synthesis):**
- **For 2030:** the IEA base case and PNGRB GtG need about 56–63 MTPA at an 85% ceiling. That is roughly what exists
  now plus Dahej, or the 66.7 MTPA target at most. **Only GtB (about 77–90 MTPA) justifies the ICRA ~77.5 MTPA
  pipeline**, and the wrong *location* of capacity (east coast, Kochi) is the bigger problem.
- **For 2040:** GtG needs about 120–135 MTPA and GtB about 155–180 MTPA, so roughly 2–3× today's capacity. Each extra
  10 mmscmd of domestic gas cuts the requirement by about 2.8 MTPA of LNG, or about 3.3 MTPA of capacity at 85%.
- **Unit trap:** the summed nameplate ignores where the capacity is. PNGRB's own table shows Dahej at 95% while
  Kochi, Ennore and Mundra sit at 12–25% on 8-year averages.

---

## Conflicts noted (not resolved)

- **India's regas capacity.** PNGRB gives 52.7 MTPA, 8 terminals (Apr 2025). GIIGNL gives 47.7 MTPA at end-2024
  (before Chhara). PNGRB's Dec 2024 paper gives 47.7 MTPA / 7 terminals. ICF (LNG India Summit 2025) gives "~44.5 MTPA
  operational" and a "~59%" average utilisation, against PNGRB's 50.5% for 2023-24.
- **Kochi tariff.** ₹114.5 (Argus) vs ₹89–94 (broker models).
- **Dahej tank size.** 2 × 180,000 m³ (GIIGNL) vs 2 × 170,000 m³ (L&T order reports). Cost also differs: ₹1,250 cr
  (project) vs ">₹1,000 cr" (EPC order).
- **Dahej expansion cost.** ₹560 cr (Business Standard, final) vs ₹570–600 cr (earlier estimates). Unclear whether
  the tanks are excluded from these figures. I treated them as excluded.
- **Brunsbüttel onshore cost.** €1.3 bn (CAP) vs €1.5 bn rising to ~€1.9 bn (OSW).
- **Revithoussa project cost.** €143 m vs €195.6 m.
- **Bangladesh 3rd FSRU.** Reported as "withdrawn" (tob.news) vs "stalled" (dailywaadaa, 18 Oct 2026).
- **Engro build time.** 330 vs 332 days (two Engro statements).
- **Wilhelmshaven start date.** May 2022 preliminary works vs 4 Jul 2022 official construction start.
- **IEA 2030 LNG.** 65 bcm (IEA, LNG Prime) vs 64 bcm (Argus).
- **Petronet tariff direction.** The GAIL discount (Argus) vs management saying the Qatar-volume tariff will not be
  lower (Motilal Oswal).

## Gaps

1. **Pages were not opened.** No WebFetch succeeded (DNS/proxy). Every web figure is from a search summary. Before
   publishing, check at least: Argus (Dahej/Kochi tariffs), ICRA Dec 2025 (₹81 threshold), Business Standard 4 Apr
   2026, OIES NG 123 (onshore vs FSRU costs, charter rates) and the EDF Dunkerque presentation.
2. **Missing tariffs.** No public tariffs were found for Hazira, Dabhol, Mundra, Dhamra, Ennore or Chhara, only the
   Nomura ₹83–87 "required" range. Use-or-pay percentages, contract tenors and short-term or spot regas pricing
   (Petronet's spot-slot charges) were also not found.
3. **Missing primary cost data.** No final audited project cost for Chhara, Ennore (original), Dhamra (beyond press),
   Kochi or Mundra. The Ennore expansion scope (number of tanks, jetty) is unconfirmed. The Petronet annual report
   capex tables were not accessible (petronetlng.in blocked by proxy).
4. **IGU World LNG Report** was not available; the Drive file is GIIGNL 2025. The IGU's FSRU and regas statistics
   (e.g. average FSRU build times) were not obtained.
5. **Asia FSRU details not obtained:**
   - Pakistan: Engro or GasPort tariff or capacity charge.
   - Philippines: FGEN Batangas cost or schedule, beyond GIIGNL saying the BW Batangas FSRU started in 2023 on a
     5-year charter.
   - Sri Lanka: FSRU plans.
   - Bangladesh: Moheshkhali agreement-to-first-gas dates.
6. **Missing European details.** Grain's current expansion (new 200,000 m³ tank, 2 SCVs; GIIGNL 2025, p.50) has no
   cost or dates. The Eemshaven FSRU cost is not available. Dunkerque's actual COD date and final cost are unconfirmed.
7. **GBS.** Only the Adriatic LNG EPC contract value (USD 900 m, 2004) was found. There is no full capex and no
   second GBS data point.
8. **Generic tank benchmark.** No published USD/m³ benchmark for full-containment tanks was found. The ranges above
   rest on two Indian and two European data points.
9. **Domestic production forecasts.** PNGRB gives none for 2030/2040, so the implied-capacity table depends on my
   104 / 130 mmscmd assumptions.
10. **The 15% gas-share target.** No quantitative MoPNG translation into mmscmd was found, because mopng.gov.in is
    blocked.
