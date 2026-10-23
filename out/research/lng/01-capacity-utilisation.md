# 01 — LNG regas terminals: capacity and utilisation (terminal by terminal)

Compiled 23 Oct 2026. Scope: nameplate capacity, capacity steps, utilisation by period, pipeline connectivity,
national totals, and terminals under construction or planned. Tags: [primary] = PPAC/PNGRB/MoPNG/company filing;
[secondary] = rating agency, broker, consultant, IGU; [press] = news/trade press. "[derived]" = my arithmetic
on tagged inputs (method stated). Search-summary items come from web-search result summaries; the pages themselves
could not be opened, because every non-Google host was refused by this environment's proxy.

## Sources used (short names used below)

- **HLEC-2025**: PNGRB High Level Expert Committee, "Vision 2040 – Natural Gas Infrastructure in India" (report dated 10 Nov 2025), Drive markdown copies `20251110_HLEC_compressed-1-200.md` and `-201-352.md`. Page numbers below are the **printed** page numbers in the report. Table 6.4 is on p.176-177. Section 6.2 (LNG terminals) is on pp.175-182. [primary]
- **PNGRB-Proj-2025**: PNGRB, "NG Demand projections for 2030 and 2040" (7 Apr 2025), Drive `20250407_NG_Projections2030_40.md`. The terminal table is on p.21 (section 4.2) and cites "Source: PPAC". [primary] The same table appears in the slide deck `20250609_CSR.pdf` ("Natural Gas Projections – 2030 Base Case", PNGRB Monitoring Division), slide 22. [primary]
- **PNGRB-Initiative**: `20250424_PNGRB_Initiative_copy.pdf` ("PNGRB: An Enabler, Facilitator and Regulator", Mar 2025). It has **no terminal capacity or utilisation data**. It only mentions a PNGRB case study, "Optimizing LNG Supplies from Terminals in India" (Dec 2024, pngrb.gov.in, which is blocked here).
- **ppac_2526.json / build_ppac_2526_data.py**: these hold petroleum-product trade, consumption, production and ethanol data. **There are no LNG terminal or utilisation fields.** Not used.
- **PPAC MRR Feb-2026** (Drive id 1VtUVwQJ…, 28 MB) and **MRR Nov-2025** (Drive, 16 MB): **not extractable.** Drive text extraction returns only page numbers and logos, so the PDFs are image-based. Binary download is refused because the files exceed the connector's 10 MB limit, and the direct Drive download host is blocked by the proxy. **The PPAC "LNG terminals capacity and utilisation" table was therefore NOT read.** See Gaps.
- **Elara-Mar-2026**: Elara Securities, "LNG: Steering through the Hormuz bottleneck" (6 Mar 2026), Drive PDF, Exhibit 1 (terminal-wise CY25 LNG imports, citing PPAC and DGCI&S). [secondary]
- **ICF-LNGIS-2025**: ICF, LNG India Summit 2025 post-event report, Drive markdown. [secondary]
- **ICRA-Dec-2025**: ICRA, "Indian Gas Utilities – LNG terminal capacities to remain underutilised…" (Dec 2025), via search summary. [secondary]
- **LNG Prime**: monthly articles quoting PPAC, via search summaries: https://lngprime.com/asia/indias-lng-imports-drop-in-june/192519/ , https://lngprime.com/asia/indias-lng-imports-down-in-may/189591/ , https://lngprime.com/asia/indias-lng-imports-dip-in-april/187360/ . [press, quoting PPAC]

---

## 1. Terminal table

### 1a. Snapshot: capacity, operator, location, commissioning year

| # | Terminal | State | Operator (as named by source) | Type | Commissioned | Nameplate MMTPA (date) |
|---|---|---|---|---|---|---|
| 1 | Dahej | Gujarat | Petronet LNG Ltd (PLL) | Onshore | 2004 | 17.5 (1 Feb 2025) → **22.5 from 31 Mar 2026** |
| 2 | Hazira | Gujarat | Shell Energy India Pvt Ltd / "Hazira LNG Pvt Ltd" | Onshore | 2005 | 5.2 |
| 3 | Kochi | Kerala | Petronet LNG Ltd | Onshore | 2013 | 5.0 |
| 4 | Dabhol | Maharashtra | Konkan LNG Ltd (KLL; GAIL group) | Onshore + breakwater | 2013 | 5.0 |
| 5 | Ennore | Tamil Nadu | Indian Oil LNG Pvt Ltd (IOLPL) | Onshore | 2019 | 5.0 |
| 6 | Mundra | Gujarat | GSPC LNG Ltd | Onshore | 2020 | 5.0 |
| 7 | Dhamra | Odisha | Adani Total Pvt Ltd | Onshore | 2023 | 5.0 |
| 8 | Chhara | Gujarat | HPCL LNG Ltd | Onshore | 2025 | 5.0 |
| | **Total operational** | | | | | **52.7 (1 Feb 2025) → 57.7 [derived] after Dahej expansion** |

Line-by-line sourcing:
- Names, states, entities, capacities and the 52.7 total come from HLEC-2025 Table 6.4(A), p.176. Capacities are "as on February 1, 2025". [primary]
- Commissioning years come from HLEC-2025 truck-loading table (§6.2.3.2, pp.179-180): Dahej 2004, Kochi 2013, Dabhol 2013, Ennore 2019, Mundra 2020, Hazira 2005, Dhamra 2023. [primary] PNGRB-Proj-2025 p.21 gives the same years and adds Chhara as 2025. [primary]
- Type: "eight operational onshore LNG terminals … combined regasification capacity of ~190 MMSCMD (52.7 MMTPA)" (PNGRB-Proj-2025 p.21). [primary] There are no FSRUs or GBS terminals in operation. The only FSRU in the pipeline is Jafrabad (see §3).
- Chhara capex: "approximately Rs. 4,750 Crore (around US$550 million)" for 5 MTPA, with marine unloading, storage, truck loading and grid supply (HLEC-2025 p.176). [primary]
- Dahej 22.5 MMTPA: Petronet's stock-exchange filing says the expansion facilities "commissioned at 23:30 hrs on March 31 [2026]". This was reported by LNG Prime (https://lngprime.com/lng-terminals/indias-petronet-launches-dahej-lng-expansion/182021/) and Construction World. [press, quoting company filing; filing itself not read]
- Operator names differ across sources. Elara-Mar-2026 labels Mundra "Adani", Ennore "IOCL" and Dabhol "GAIL". HLEC labels them "GSPC LNG Ltd", "Indian Oil LNG Pvt Ltd" and "Konkan LNG Ltd". The two are consistent (they reflect parent or JV partner versus SPV) but are listed here unresolved. A press item calls Chhara an "ONGC unit"; HPCL is an ONGC subsidiary, so this is not a contradiction.
- **Conflict on national capacity:** ICF-LNGIS-2025 §2.1 and Appendix B say "approximately 44.5 MTPA operational" (2025). [secondary] PNGRB says 52.7 MMTPA (Feb 2025) [primary]. ICF's figure has no stated basis and matches no combination of PNGRB nameplates. Use PNGRB.

### 1b. Capacity history (steps)

- **Dahej**: 5 MMTPA at start (2004) → 10 MMTPA (2009) → 15 MMTPA (expansion due Nov 2016; one source says commissioned Oct 2016) → 17.5 MMTPA (date **not verified**; a CRISIL rationale of 26 Feb 2021 already cites 17.5) → 22.5 MMTPA (31 Mar 2026). Sources: search summaries of ADB, Petronet and CRISIL pages. [press/secondary] The last step comes from the company filing as reported. [press]
  - The expansion date slipped several times: Petronet guided Mar 2025, then Jun 2025, then end-2025, then Mar 2026 (LNG Prime search summary). [press]
- **Hazira**: commissioned 2005 at 5 MMTPA (PNGRB-Proj-2025 p.21) [primary]. It is 5.2 MMTPA by Feb 2025 (HLEC Table 6.4) [primary]. Date of the 5 → 5.2 step not found.
- **Dabhol**: 5 MMTPA nameplate since 2013 [primary]. Before 2025 the terminal "used to be shut for four months during the rainy season", because it had no breakwater. A 2.3 km breakwater was completed and all-weather status was granted, and the first monsoon cargo (GAIL Bhuwan) berthed on 2 Jun 2025 (Baird Maritime, Outlook Business, GAC; search summary). [press] GAIL plans 5 → 6.3 MMTPA "in the next three years" (statement Jun 2025). [press]
- **Kochi, Ennore, Mundra, Dhamra, Chhara**: no capacity change since commissioning in these sources. All are 5.0 MMTPA. [primary]

### 1c. Utilisation by terminal and period

All figures are capacity utilisation %. "PNGRB-Proj" is the PPAC-sourced table in PNGRB-Proj-2025 p.21.

| Terminal | Avg FY16–FY23 | FY2023-24 | Apr–Dec 2024 (FY25 9M) | FY2024-25 | CY2025 implied [derived] | FY2025-26 | Apr–Jun 2026 (FY27 Q1) |
|---|---|---|---|---|---|---|---|
| Dahej | 98.23% | 95.10% | 100.3% | 98.1% | 93% | 91.9% (Apr–Feb: 94.3%) | 91.9% ⚠ |
| Hazira | 67.17% | 30.30% | 38.5% | 34.9% | 73% | 27.2% | 29.5% |
| Kochi | 13.14% | 20.60% | 22.0% | 22.3% | 10% | 26.3% ⚠ | 26.3% ⚠ |
| Dabhol | 57.50% | 42.7% | 41.5% | 46.6% | 16% (incl. swap) | n/f | 39.2% |
| Ennore | 12.00% | 18.30% | 24.8% | 25.2% | 20% | 25.1% | 26% |
| Mundra | 24.93% | 14.60% | 23.6% | 17.6%? | 40% | 17.4% | 29.7% |
| Dhamra | – | 27.40% | 49.5% | 40.8% | 22% | 34.1% | 41.7% |
| Chhara | – | – | NA (just commissioned) | 4%? | 2% | n/f | 9% |
| **All terminals** | **54.64%** | **50.50%** | 57.9% [derived] | 55.8% [derived] | 48.6% [derived] | n/f | see note |

Sources and notes, one per column:
- **Avg FY2015-16 to FY2022-23** and **FY2023-24**: PNGRB-Proj-2025 p.21 table, "Source: PPAC". Totals are printed in the table: 54.64% and 50.50%. [primary, PNGRB citing PPAC]
- **Apr–Dec 2024**: HLEC-2025 Table 6.4(A), p.176, footnote "** Percentage capacity utilisation is during April-Dec'24". Chhara is printed as "NA*** Recently commissioned". [primary] The all-terminal 57.9% is [derived]: capacity-weighted sum of 27.6 MMTPA-equivalent throughput ÷ 47.7 MMTPA (ex-Chhara). ICF-LNGIS-2025 gives "national average utilization rate hovers around 59%" (2025) [secondary], which is consistent.
- **FY2024-25**: table "as on 1 June 2025" in the NGS India "GSR July 2025" report (search summary; ngsindia.org unreachable). The table does not name its source, so it is **not confirmed as PPAC**. Values: Dahej 98.1, Hazira 34.9, Dabhol 46.6, Kochi 22.3, Ennore 25.2, Dhamra 40.8. [secondary]
  - Mundra 17.6% and Chhara 4% come from Indian Infrastructure, 4 Aug 2025. That article gives Dahej at 89.9%, so it covers a **different, unstated period**. [press]
  - The all-terminal 55.8% is [derived]: ≈26.6 MMT ÷ 47.7 MMTPA, excluding Chhara.
- **CY2025 implied**: [derived] from Elara-Mar-2026 Exhibit 1 (CY25 LNG imports by terminal, mn t, citing PPAC/DGCI&S) [secondary], divided by nameplate.
  - Elara volumes: Dahej 14.8 + 1.5 GAIL US-swap = 16.3; Hazira 3.8; Mundra 2.0; Dhamra 1.1; Ennore 1.0; Dabhol 0.6 + 0.2 swap = 0.8; Kochi 0.5; Chhara 0.1. Total 25.6 mn t including swap (23.9 excluding).
  - Dahej is computed on 17.5 MMTPA. Total = 25.6 ÷ 52.7.
  - **Conflict:** Elara's Hazira (3.8 mn t, about 73%) and Mundra (2.0 mn t, 40%) are far above the PPAC-sourced FY25 and FY26 utilisation figures (Hazira 27–35%, Mundra 17–18%). Elara's Kochi (0.5 mn t, 10%) is far below them (22–26%). Possible causes: Elara assigns cargoes by DGCI&S port of import, so Hazira may absorb cargoes that were regasified elsewhere, or the gap is a CY vs FY effect. Unresolved; do not mix the two series.
- **FY2025-26**: LNG Prime (May/June 2026 articles, quoting PPAC, "April 2025–March 2026"): Dahej 91.9, Hazira 27.2, Kochi 26.3, Ennore 25.1, Mundra 17.4, Dhamra 34.1. Dabhol and Chhara were not in the summary. [press quoting PPAC]
  - Business Standard (4 Apr 2026, citing "oil ministry data") gives Apr–Feb FY26: Dahej 94.3%, and "all Indian LNG import terminals, excluding Dahej, operated at 35 per cent or lower". [press quoting MoPNG/PPAC]
  - The same article, citing DAM Capital, says Dahej's monthly utilisation fell to 56% in Mar 2026, from 94% in Feb 2026 and 75% a year earlier, after the Hormuz-related force majeure. [press]
- **Apr–Jun 2026** (latest FY2026-27 data found): LNG Prime, "India's LNG imports drop in June" (quoting PPAC). Dahej (17.5 mtpa basis) 91.9, Hazira 29.5, Dhamra 41.7, Dabhol 39.2, Kochi 26.3, Ennore 26, Mundra 29.7, Chhara 9. [press quoting PPAC]
  - Apr–May 2026: Dahej 91.9, Hazira 27 (LNG Prime May article). [press]
  - ⚠ **Reliability flag.** Dahej "91.9%" appears for three different periods across LNG Prime articles (FY26 full year, Apr–May 2026, Apr–Jun 2026), and Kochi "26.3%" appears for two. This suggests stale or mislabelled figures in the articles or in the search summaries.
  - It is also inconsistent with volumes. Apr 2026 imports were ~1.5 Mt (−29.6% y/y) and Jun 2026 2,604 mmscm ≈ 1.9 Mt (−5.4% y/y), which annualises to roughly 20–23 Mt (38–44% of 52.7 MMTPA). The terminal-wise Apr–Jun figures instead imply ~26 Mt annualised (~50%) [derived].
  - The figures still use the old 17.5 MMTPA Dahej base, although 22.5 MMTPA was commissioned on 31 Mar 2026.
  - **Treat the FY27 Q1 terminal row as unverified until the PPAC table itself is read.**
- **Outlook**:
  - ICRA-Dec-2025: utilisation of terminals ex-Dahej is "25–30%" now and is projected "to remain below 40% on an overall basis over the next three to five years". [secondary]
  - ICRA rating note on Petronet (later than Dec 2025): Dahej "upwards of 90% on an ongoing basis", expected to moderate in FY2027 because of the new 5 MMTPA and the QatarEnergy force majeure. [secondary]
  - A MoPNG report cited by Argus has Dahej at 92% "as of June" (year not shown in summary), with the rest at 20–30%. [press quoting MoPNG]

### 1d. Pipeline connectivity and evacuation constraints (by terminal)

- **System-wide**: "Most LNG regasification terminals in India, except for PLL Dahej, operate at less than 50% capacity utilisation." HLEC-2025 §6.2.3.3, p.180 gives three reasons [primary]:
  - (A) inadequate evacuation infrastructure. "Past experiences, such as Kochi and Ennore terminals (where connectivity faced prolonged delays despite their readiness)."
  - (B) destination clauses in long-term SPAs that tie cargoes to a specific terminal.
  - (C) price-sensitive demand switching to alternate fuels when LNG prices are high.
- **Dahej / Mundra / Hazira cluster**: "Existing LNG terminals (Dahej, Mundra and Hazira) have a capacity of around 27.7 MMTPA, i.e., almost 95-100 MMSCMD. An extra ~10 MMTPA (~37 MMSCMD) is planned (Jafrabad 5 MTPA and upgradation of Dahej to 22.5 MMTPA)." Yet "the HP and LP evacuation pipelines operated by GSPL [have] a cumulative capacity of only around 40 MMSCMD" (HLEC-2025 annexure on pipeline augmentation, p.276). [primary]
  - GSPL High Pressure network utilisation was 100.5% in FY25 (to Dec 2024) (HLEC Table 6.3, p.167, and Annexure Table 12.7, p.271). [primary]
  - The Hazira–Ankleshwar (GGL) line was 12.06% utilised (Table 12.7). [primary]
- **Dahej / Dabhol on the GAIL system**: "DUPL (Dahej-Uran-Panvel-Dabhol) pipeline (20 MMSCMD) facilitates evacuation of gas through Dahej and Dabhol LNG terminals, having capacity of ~80 MMSCMD, expandable until 90-100 MMSCMD" (HLEC p.276). [primary]
  - The Dabhol–Bangalore pipeline (1,414 km authorised; 1,148 km operational) is "partially commissioned" (Table 12.7, p.271). [primary]
- **Dabhol**: before Jun 2025 it shut for ~4 monsoon months because it had no breakwater; it has been all-weather since Jun 2025 (§1b). [press]
  - GAC: expected to achieve 41% of 5 MMTPA, and "100% capacity after completion of AAHS … expected by December 2026" (AAHS undefined in the summary). [press]
- **Kochi**: the Kochi–Koottanad–Bangalore–Mangalore pipeline (GAIL, 1,104 km authorised; 644 km operational) is "partially commissioned" and ran at 24.5% utilisation in FY25 to Dec 2024 (HLEC Table 12.7, p.272). [primary]
  - "KKBMPL is yet to be connected to the national grid, restricting gas expansion and leading to underutilisation of the infrastructure created in Kochi" (HLEC §3.4 refineries, p.94). [primary]
  - "~58% of pipeline work has been completed" (PNGRB 20250609_CSR slide 9). [primary]
  - HLEC proposes a Kochi–Thoothukkudi line of ~399-450 km. [primary]
- **Ennore**: the Ennore–Tuticorin pipeline (IOCL, 1,431 km authorised; 1,080 km operational) is "partially commissioned" at 5.91% utilisation (HLEC Table 12.8, p.273). [primary]
  - "~75% of pipeline work has been completed" (PNGRB CSR slide 9). [primary]
  - The ETBPNMTPL and Dabhol–Bengaluru lines "have not been interconnected due to a missing pipeline segment of fewer than 17 km outside Bengaluru" (HLEC CGD chapter, p.42). [primary]
  - Ennore–Nellore (GTIL, 220 km) is under construction (Table 12.8). [primary]
- **Dhamra**: the Jagdishpur–Haldia–Bokaro–Dhamra pipeline (GAIL, 3,546 km authorised; 3,270 km operational) is "partially commissioned" (Table 12.7). [primary] It is "~92% of pipeline work … completed" (PNGRB CSR slide 9). [primary]
  - HLEC also notes that "LNG Terminals available on the east coast are not connected with many power plants situated in eastern parts of the country" (power chapter, p.81). [primary]
- **Chhara**: the GSPL 36-inch, 18 MMSCMD pipeline to Gundala, connecting the terminal to the grid, was commissioned 20 Mar 2025 (Pipeline Journal, World Pipelines, Indian Infrastructure 26 Mar 2025). [press]
- **Mundra**: no terminal-specific connectivity statement was found. HLEC groups it within the GSPL-evacuated Gujarat cluster (above).

### 1e. Tariffs, capacity booking, other operating economics (HLEC-2025 §6.2.3–6.2.4, pp.179-182 unless noted)

- Regas charges: "RLNG terminals located in Dahej, Hazira, and Mundra have regasification charge of ~Rs. 66.05 per MMBtu, RLNG terminals located in Kochi and Ennore charge … ~Rs. 79.80/MMBtu for CY 2025". "These regasification charges keep on escalating by 5% every calendar year." [primary]
- Table titled "Truck Loading Charges (Rs/MMBtu)": Dahej 97.26, Kochi 97.26, Dabhol 66.05, Ennore 63.04, Mundra 79.54, Hazira 64.17, Dhamra 66.35. [primary]
  - ⚠ Possible labelling inconsistency: the table's Dabhol value (66.05) equals the text's regas charge for Dahej/Hazira/Mundra, and the Dahej/Kochi values differ from the text. Quote as printed and flag.
  - Comparators: POL truck loading is ~Rs 2.1/MMBtu. Netherlands regas is ~US$0.35/MMBtu (~Rs 29.75). Japan regas is ~US$0.50/MMBtu (~Rs 42.5). [primary]
- The Committee recommends **no** regulatory tariff fixation for regas. Tariffs should be published and non-discriminatory. Truck-loading charges should be reviewed "with PNGRB oversight", and the 5% annual escalation reviewed because "a very large portion of the regasification expenses is on account of capital cost" (§6.2.4.2, p.181). [primary]
- Capacity booking:
  - No secondary trading market exists, and existing holders "lock in terminal capacity under long-term agreements" (§6.2.3.1, p.179). [primary]
  - Recommendations: an online bulletin board, transparent booking, PNGRB-enforced SOPs, a rule-based short-term (≤1 yr) booking process, UIOLI, and secondary capacity trading via a gas exchange (§10.4.2.2, pp.233-234). [primary]
  - The TPA recommendation (#10) "shall be re-looked into by PNGRB in phased and holistic manner" (HLEC final note, p.299). [primary]
- Pipeline synchronisation proposal: for spur lines under 50 km, the nearest trunk operator would build them and recover cost under the Unified Tariff. For lines over 50 km, PNGRB would bid them out; failing that, the terminal operator builds the line (cost recovered via regas tariff) or books long-term pipeline capacity. "Construction of an LNG terminal typically takes three years" (§6.2.4.3 D, pp.181-182). [primary]
- Registration regulations notified 8 May 2025 (§6.2.2.3–6.2.2.4, pp.177-179). [primary]
  - Pre-FID intimation to PNGRB is required.
  - A performance bank guarantee of 1% of project cost (or Rs 25 crore, whichever is lower) applies.
  - Registration is valid 30 years.
  - Any expansion needs an amendment application ≥90 days before work starts.
  - **Operational and performance data must be filed bi-annually (1 Apr, 1 Oct) and published on the operator's website.** This is a future primary source for terminal-wise utilisation.
- Tax: GST on LNG terminal regasification and storage is 18% (HLEC Table 7.1, p.194). [primary]
- Debt-service break-even: "a 5 MMTPA LNG terminal will need regas charges above Rs. 81/mmbtu with capacity utilisation levels between 30% to 55% to meet its debt servicing requirements" (ICRA-Dec-2025). [secondary]

---

## 2. National totals by year

### 2a. Installed regas capacity (MMTPA, nameplate, year-end)

Step-sum [derived] from §1a/1b. Dates are commissioning years. Dahej 17.5 is assumed in place from FY2019-20, which is **unverified**.

| Year (approx.) | Capacity | Composition | Basis |
|---|---|---|---|
| 2013–Oct 2016 | ~25 | Dahej 10 + Hazira 5 + Kochi 5 + Dabhol 5 | [derived]. Dabhol was effectively unusable in monsoon (no breakwater) |
| late 2016–2018 | ~30 | Dahej 15 | [derived] |
| 2019 (Ennore) | ~35–37.7 | + Ennore 5; Dahej 15 or 17.5 (date unverified) | [derived] |
| 2020 (Mundra) | 42.7 | + Mundra 5; Hazira at 5.2 by this point (date unverified) | [derived] |
| 2023 (Dhamra) | 47.7 | + Dhamra 5 | [derived]. Cross-check: "47.7 MMTPA" national figure in search summary [press] |
| Feb 2025 (Chhara) | **52.7** | + Chhara 5 | **[primary]** HLEC Table 6.4; PNGRB-Proj p.21; ICRA "52.7 MMTPA as of end FY2025" [secondary] |
| 31 Mar 2026 | **57.7** | Dahej 17.5 → 22.5 | [derived] from company filing [press]. Note: LNG Prime's Jun-2026 article still says "eight facilities with a combined capacity of about 52.7" |
| end-FY2029 (plan) | ~77.5 | | ICRA-Dec-2025 [secondary] |

The brief's guess of "2015 ~26 MMTPA" fits the 25 MMTPA step-sum if Hazira is taken at 5.2 or rounding is used. No source found states a 2015 national figure.

### 2b. LNG imports and implied average utilisation

| Period | LNG imports | Source / tag | Implied avg utilisation [derived] |
|---|---|---|---|
| FY2015-16 to FY2022-23 (avg) | — | — | **54.64%** printed (PNGRB-Proj p.21, citing PPAC) [primary] |
| FY2018-19 | ~29 bcm | Statista citing PPAC, rounded chart value [secondary] | n/c |
| FY2019-20 | ~34 bcm (Statista) vs 32.35 bcm (HLEC Fig 7.1) | conflict, see note | n/c |
| FY2020-21 | 33.20 bcm; US$7.88 bn | HLEC Fig 7.1, p.189 [primary; OCR-garbled, mapping inferred] | ~56% (≈24.5 MMT ÷ 42.7) |
| FY2021-22 | 31.03 bcm; US$13.47 bn | HLEC Fig 7.1 [primary; mapping inferred] | ~54% |
| FY2022-23 | 26.30 bcm; US$17.11 bn | HLEC Fig 7.1 [primary; mapping inferred] | ~46% |
| FY2023-24 | 31.80 bcm; US$13.40 bn | HLEC Fig 7.1 [primary; mapping inferred] | **50.50%** printed (PNGRB-Proj) [primary] |
| Apr–Dec 2024 | 28.30 bcm; US$11.62 bn | HLEC Fig 7.1 [primary; mapping inferred] | 57.9% (terminal-weighted, ex-Chhara) |
| FY2024-25 | 36.99 bcm ≈ 27.7 Mt (+15.4% y/y) | LNG Prime quoting PPAC [press] | ~58% on 47.7 (Chhara only ~2 months); ~53% on 52.7 |
| CY2024 | ~27 Mt (record, +20% y/y) | Shell LNG Outlook via chemindigest [secondary] | — |
| CY2025 | 25.6 Mt incl. GAIL swap (23.9 excl.); ≈91.8 mmscmd | Elara-Mar-2026 Ex.1, citing PPAC/DGCI&S [secondary] | 48.6% (÷52.7) |
| CY2025 (forecast) | 25 Mt (−6%) | Kpler via Argus [press] | — |
| FY2025-26 | **not found** | — | Terminal-weighted, ex-Dabhol/Chhara: Dahej 16.1 + Hazira 1.4 + Kochi 1.3 + Ennore 1.3 + Mundra 0.9 + Dhamra 1.7 = 22.7 Mt over 42.7 MMTPA ≈ 53% |
| Apr 2026 | 1.95 bcm ≈ 1.5 Mt (−29.6% y/y) | LNG Prime quoting PPAC [press] | ≈34% annualised on 52.7; ≈31% on 57.7 |
| Jun 2026 | 2,604 mmscm ≈ 1.9 Mt (−5.4% y/y) | LNG Prime quoting PPAC [press] | ≈43% on 52.7; ≈40% on 57.7 |

Method and conflict notes:
- **Conversion**: 1 Mt LNG ≈ 1,314–1,316 scm. Basis: PNGRB's "1 MT of LNG = 1314 scm" (CSR slide 14) and its "190 MMSCMD (52.7 MMTPA)" (PNGRB-Proj p.21), which implies 1,316. bcm → Mt is therefore ÷ ~1.33. This is a rough conversion; PPAC's own MMSCM figures are on a gross calorific basis.
- **HLEC Fig 7.1** is image text garbled by OCR (`32.35 33.20 31.03 31.80 … 28.30 26.30 17.11 … 13.47 13.40 … 11.62 9.66 7.88`). I mapped BCM and US$ to years by ordering and by matching known price-shock patterns (FY23 highest US$, lowest volume). The mapping is **inferred**. FY2019-20 under this mapping would be 32.35 bcm / US$9.66 bn.
- **Conflict**: Statista (citing PPAC) gives ~34 bcm for FY2019-20, against 32.35 bcm in the inferred HLEC mapping. Unresolved; it may reflect a different calorific basis or a mapping error.
- **Years not found**: annual import totals for FY2015-16 to FY2017-18 and FY2025-26 were not found in any accessible source.

---

## 3. Under construction / planned

| Project | Owner | Capacity | Status / COD as stated | Statement source & date |
|---|---|---|---|---|
| Dahej expansion | Petronet LNG | +5 → 22.5 MMTPA | Listed as "under construction" in Feb 2025 [primary, HLEC Table 6.4(B)]. **Commissioned 31 Mar 2026** [press, quoting PLL filing]. Guidance slipped Mar-25 → Jun-25 → end-25 → Mar-26 [press] | HLEC-2025; LNG Prime Apr 2026 |
| Jafrabad (Gujarat) FSRU | Swan LNG (Swan Energy) | 5 MMTPA | "Under construction" (HLEC Table 6.4(B), capacity as on 1 Feb 2025) [primary] | HLEC-2025 |
| ″ (continued) | | | Original COD 2019, phase 1 targeted 2022. FSRU *Vasant-1* chartered to BOTAŞ, then sale to BOTAŞ announced Aug 2024 (~US$399 m). Dec 2024 HOA with AG&P for a replacement FSRU/FSU JV. **No COD found**; Swan's site describes it as "developing" [press] | GEM wiki, Hellenic Shipping News, Swan site (search summaries) |
| Dabhol expansion | Konkan LNG / GAIL | 5 → 6.3 MMTPA | "in the next three years" [press] | GAIL statements, Jun 2025 |
| ″ conflict | | +5 MMTPA | PNGRB-Proj p.21: "expansion plans for the Dahej and Dabhol terminals, each adding 5 MMTPA" [primary] | PNGRB, Apr 2025 |
| Gopalpur (Odisha) | Petronet LNG | 4.0 MMTPA | "Proposed/Announced" — no date [primary] | HLEC Table 6.4(C), p.177 |
| Kakinada (AP) | Crown LNG | 7.2 MMTPA | Proposed/announced — no date [primary] | HLEC Table 6.4(C) |
| Haldia (WB) | H-Energy | 5.0 MMTPA | Proposed/announced — no date [primary] | HLEC Table 6.4(C) |
| Karaikal (TN) | AG&P | 4.0 MMTPA | Proposed/announced — no date [primary] | HLEC Table 6.4(C) |
| Gangavaram (AP) | Petronet LNG | 5.0 MMTPA | Proposed/announced — no date [primary] | HLEC Table 6.4(C) |
| **Totals** | | **B = 10.0; C = 25.2; A+B+C = 87.9 MMTPA** | "Their development depends on the growth of the natural gas market in their respective areas" (p.175) [primary] | HLEC-2025 |

Other mentions:
- HLEC's pipeline annex (pp.275-276) refers to "Dhamra and Digha LNG terminals", "Kukrahati or Haldia LNG terminals" and a "proposed Jaigarh FSRU" when sizing evacuation pipelines. Digha, Kukrahati and Jaigarh are **not** in Table 6.4. [primary]
- ICRA projects ~77.5 MMTPA by end-FY2029 (from 52.7). It does not list projects in the summary, and it warns the new terminals face "muted capacity utilisation". [secondary]

### Demand and regas requirement projections (PNGRB)

- Total gas demand (PNGRB-Proj-2025 p.25; CSR slide 7) [primary]:
  - FY2024 base: 187 MMSCMD.
  - 2030: 297 MMSCMD (Good-to-Go) / 365 (Good-to-Best).
  - 2040: 495 / 630.
- LNG demand: "projected to double to ~200 MMSCMD by 2030" (PNGRB-Proj p.20). [primary] HLEC restates the 2030 GtG split as "~200 MMSCMD of LNG imports and ~100 MMSCMD of domestically produced gas" (HLEC gas storage chapter, p.203). [primary]
- Implied regas need [derived]:
  - GtG 2030: 200 MMSCMD ≈ 55.5 MMTPA of LNG (at 190 MMSCMD = 52.7 MMTPA). That is about 96% of 2025 capacity (52.7), or about 72% of ICRA's 77.5 MMTPA for FY2029.
  - GtB 2030, if domestic stays ~100 MMSCMD (my assumption, not PNGRB's): ~265 MMSCMD ≈ 73.5 MMTPA.
- **No explicit regas-capacity requirement** is stated in either PNGRB document. HLEC says only that "timely investments in long-term LNG contracts, regasification capacity, and infrastructure connectivity will be key" (executive summary, unnumbered front matter). PNGRB's CSR deck says "Adequate Regas capacity already existing in our terminals with expansion underway" (slide 5). [primary]

---

## 4. Gaps

1. **The PPAC Ready Reckoner terminal table (Feb 2026 edition, and Nov 2025) was not read.** The PDFs are image-only, too large for the Drive connector (>10 MB), and the direct download is blocked. Workaround for the user: export the relevant MRR page (the "LNG terminals capacity and utilisation" table) as a separate PDF under 10 MB or as PNG, put it in Drive, and re-run. Drive's image reader or the PDF text should then work.
2. **The FY2026-27 Q1 terminal-wise figures (LNG Prime) are suspect.** Dahej 91.9% is repeated across three periods and conflicts with the volume drop after Hormuz. They need checking against the PPAC monthly "LNG import" note or the MRR.
3. **The terminal-wise FY2024-25 series is not confirmed as PPAC.** The NGS table has no stated source, Mundra is from a different-period press figure, and Chhara FY25 is unknown. Dabhol and Chhara for FY2025-26 were not found.
4. **The year-by-year terminal series FY2015-16 to FY2022-23 is missing.** Only the 8-year average per terminal (PNGRB, citing PPAC) was found. Year-wise values would need the PPAC annual "Snapshot"/Ready Reckoner back-editions, or PLL annual reports for Dahej and Kochi.
5. **National LNG import totals** are missing for FY2015-16 to FY2017-18 and FY2025-26. The FY2019-23 values rest on an OCR-garbled HLEC chart with an inferred year mapping.
6. **Capacity step dates are unverified** for Dahej 15 → 17.5 and Hazira 5 → 5.2. Exact first-cargo / COD dates for Ennore, Mundra, Dhamra and Chhara are from general sources, not checked. Chhara was "Jan–Feb 2025" per a PNGRB-linked summary.
7. **Owners/equity splits** (PLL promoters; GSPC–Adani split at Mundra; Adani–TotalEnergies at Dhamra; GAIL share in Konkan LNG; IOCL share in IOLPL; Shell at Hazira) were not verified this session; only operator names as printed are given.
8. **The PNGRB "data bank" / LNG terminal register** (registrations under the 8 May 2025 regulations, and the bi-annual operational filings due 1 Apr / 1 Oct) was not accessible; pngrb.gov.in is blocked. These would be the cleanest primary source for terminal-wise utilisation, booked capacity and regas tariffs once published.
9. **Regas tariff table ambiguity in HLEC** (truck-loading vs regas columns) is unresolved. Current published tariffs per terminal were not collected; Argus reports "Petronet offers lower LNG regas rates", not opened.
10. **Sansad (Lok/Rajya Sabha) answers with terminal-wise utilisation were not found** for 2024–26. The only hit was LS USQ 2005 of 9 Dec 2021 ("LNG Terminal"), with no text available.
11. **Terminal types**: all eight operating terminals are described by PNGRB as onshore. GBS and FSRU status of proposed projects (e.g., Kakinada, Haldia, Karaikal) is not stated in the sources read.
