# 01 — India NGPL bids, authorisations, cancellations and approvals (2023 to Oct 2026)

Compiled 2026-10-23. Scope: PNGRB bid rounds and authorisations, stalled or cancelled pipelines, approvals outside PNGRB bidding, tariff and grid policy, and the latest official length totals.

## Method and caveats

- 30 WebSearch calls used. **No page could be opened.** WebFetch failed on DNS for every host tried (indianinfrastructure.com, eparlib.sansad.in, nsearchives.nseindia.com), and curl through the agent proxy was refused (403 connect_rejected). Every figure below therefore comes from **WebSearch result summaries**, plus the two local files already in hand (`00-ppac-mrr-may2026-table20.txt`, `_hlec_part2.md` = PNGRB Vision 2040 expert committee report, 2025).
- Did not access *.gov.in. Where a PNGRB, PPAC or MoPNG document appeared only as a search-result summary, the tag is **[primary-via-summary]**.
- Tags: [primary] = regulator, ministry or company filing read directly (here, only the local PPAC and HLEC files); [primary-via-summary]; [secondary] = rating agency, consultancy or tracker (Global Energy Monitor wiki = GEM); [press].
- Search summaries sometimes mis-read table columns or dates. Treat single-source numbers as provisional.
- Format: fact — tag — source URL — date of source (date of the fact, if different).

---

## A. Quick table for the map (best current reading; details and sources in section B)

| # | Pipeline (endpoints / main towns) | Entity | Length km | Cap. MMSCMD | Key dates | Status at latest source |
|---|---|---|---|---|---|---|
| 1 | Kochi–Kanyakumari–Thoothukudi (KTPL), Kerala–TN | IOCL | 424.65 | 6.84 | Bid 17 Oct 2024; authorised Apr 2026; IOCL board capex 21 Sep 2026 (Rs 2,448.70 cr) | Newly authorised; no construction yet reported |
| 2 | Ennore–Barshi (Chennai to Solapur dist., Maharashtra) | — | ~875 | ≥8.0 | Bid Dec 2023; due date extended to 16 May 2024 | No award found |
| 3 | Jammu–Srinagar | — | ~325 | ≥2.0 | Bid Jan 2024; due 13 May 2024 | No award found |
| 4 | Gurdaspur–Jammu (via Pathankot, Kathua, Samba) | GAIL | 160 (175 in press) | 3.10 (+0.78) | Bid Jan 2023; authorised Jul 2023; target Jul 2026 | ~90% complete; commissioning not confirmed |
| 5 | Hazaribagh–Ranchi, Jharkhand | IOCL | 65 / 68 / 71 | 1.03 | Bid Mar 2022; authorised 9 Feb 2023; target Feb 2026 | Under construction (Jan 2026) |
| 6 | Jamnagar–Dwarka, Gujarat | GSPL | 100 | 3 | Authorised 19 Aug 2021; target Oct 2026 | Under construction (Jan 2026) |
| 7 | Mehsana–Bhatinda (GJ, RJ, HR, PB) | GIGL | 1,943 | 83.1 | Authorised 7 Jul 2011; target Jun 2026 | 1,318 km operational, 624 km remaining (Jan 2026) |
| 8 | Bhatinda–Gurdaspur, Punjab | GIGL | 261 | 42.42 | target Dec 2024 (lapsed) | 102 km operational (Dec 2024) |
| 9 | Mallavaram–Bhopal–Bhilwara–Vijaipur | GITL | 1,881 | 78.25 | target Mar 2020 (lapsed) | 365 km operational, 1,517 km under construction (Jan 2026) |
| 10 | Ennore–Thiruvallur–Bengaluru–Puducherry–Nagapattinam–Madurai–Tuticorin | IOCL | 1,431 | 84.67 | phased 2019–2023 | 1,054–1,080 km operational, ~351 km left (Mar 2024) |
| 11 | Mumbai–Nagpur–Jharsuguda (+ Nagpur–Jabalpur spur 317 km) | GAIL | 1,755 (1,702 in a GAIL filing) | 16.5 | Earlier target 31 Dec 2025; revised 30 Jun 2026 | Mumbai–Nagpur and CG/Odisha sections operating; Maharashtra part of Nagpur–Jharsuguda pending (Mar 2026) |
| 12 | Srikakulam–Angul (AP 124 km + Odisha 298 km mainline) | GAIL | 690 authorised incl. spurs; 422 mainline | 6.65 | Inaugurated 16 Oct 2025; spurs by Jun 2026 | Mainline operating |
| 13 | Kakinada–Vijayawada–Nellore, AP | IMC | 667 (522 in HLEC text) | 18 | Authorised 19 Feb 2018; target Mar 2024 | Stalled; still listed (Jan 2026); HLEC proposes alternate route |
| 14 | Kanai Chhata–Panitar (ex-Shrirampur), WB | H-Energy consortium | 317 | 19.2 | Authorised 8 Jul 2019; endpoint changed Aug 2022 | Stalled; HLEC proposes alternate route |
| 15 | Jaigarh–Mangalore | H-Energy | 635 | 17 | Authorised 28 Jun 2016; surrender refused 2022; GEM says cancelled 4 Jul 2022 | Cancelled per GEM; HLEC still lists it as authorised but not executed |
| 16 | Kakinada–Vizag–Srikakulam, AP | APGDC (per GEM) | — | — | Cancelled Dec 2023 (GEM) | Cancelled |
| 17 | Ennore–Nellore | GTIL | 220 | 36 | Authorisation cancelled Oct 2019 (GEM/APTEL) | Conflict: HLEC Table 12.8 lists it as under construction |
| 18 | Anjar–Palanpur spur, Gujarat | GSPL | 274 | 12 | PNGRB approval Mar 2025; capex Rs 2,051.18 cr | Approved spur |
| 19 | North East Gas Grid (Guwahati–Numaligarh–Dimapur–Kohima–Imphal etc.) | IGGL | 1,656 (1,688 authorised) | — | CCEA Jan 2020: 60% capital grant (Rs 5,559 cr) on Rs 9,265 cr | 396 km Guwahati–Numaligarh commissioned Jul 2025; Phase I (~553 km) inaugurated 13 Mar 2026 |
| 20 | Jagdishpur–Haldia–Bokaro–Dhamra + Barauni–Guwahati (Urja Ganga) | GAIL | 3,266–3,306 | — | Remaining sections targeted Dec 2025, then Sep 2026 | 3,119 km in operation; Durgapur–Haldia and Dhamra–Haldia tails pending |

---

## B. Fact lines by pipeline

### B1. Pipelines bid out or authorised by PNGRB, 2023–2026

**Kochi–Kanyakumari–Thoothukudi (KTPL), IOCL**
- PNGRB opened suo motu bidding on 17 Oct 2024, with bids due 18 Feb 2025. [press] — https://www.worldpipelines.com/project-news/25102024/india-pngrb-invites-bids-on-suo-motu-basis-for-kochi-kanyakumari-thoothukudi-natural-gas-pipeline/ — 25 Oct 2024
- Route: Petronet's Kochi LNG terminal to IOCL's ETBPNMTPL at Thoothukudi, via Kanyakumari. Bid length about 425 km. [press] — same URL — 25 Oct 2024
- PNGRB granted the authorisation to IOCL after competitive bidding; reported 17 Apr 2026. [press] — https://english.punjabkesari.com/business/petroleum-and-natural-gas-regulatory-board-grants-authorization-to-iocl-kochi-kanyakumari-thoothukudi-pipeline/ — Apr 2026
- Authorisation also reported by Indian Infrastructure. [press] — https://indianinfrastructure.com/2026/05/08/pngrb-grants-authorisation-to-iocl-for-kochi-kanyakumari-thoothukudi-natural-gas-pipeline/ — 8 May 2026
- Length 424.65 km; system capacity 6.84 MMSCMD; common-carrier capacity at least 1.71 MMSCMD. [press] — https://www.indianchemicalnews.com/gas/indian-oil-board-clears-rs-244870-crore-kochi-kanyakumari-thoothukudi-gas-pipeline-31985 — Sep 2026
- IOCL board approved Rs 2,448.70 crore capex at its 21 Sep 2026 meeting. [primary-via-summary] (stock-exchange disclosure as reported) — https://chemindigest.com/iocl-board-clears-%e2%82%b92449-crore-kochi-thoothukudi-pipeline/ — Sep 2026
- No completion schedule, winning tariff or competing bidders found.

**Ennore–Barshi (EBPL)**
- PNGRB issued the bid notice in Dec 2023 under Reg. 5 of the 2008 authorisation regulations (public notice dated 19 Dec 2023; the summary gives the issue date as 15 Dec 2023). [primary-via-summary] — https://pngrb.gov.in/pdf/ngp/bid/bid19/PN19122023.pdf — Dec 2023
- Length about 875 km, from the Ennore LNG terminal (Chennai) to Barshi (Solapur district, Maharashtra). Minimum initial capacity 8.0 MMSCMD. [primary-via-summary] — same — Dec 2023
- Pre-bid conference held 19 Jan 2024; clarifications issued 13 Mar 2024 on the Barshi termination point and injection pressure. [primary-via-summary] — https://pngrb.gov.in/pdf/ngp/bid/bid19/Clarifications_13032024.pdf — 13 Mar 2024
- Bid deadline extended to 16 May 2024 after bidders asked for more time. [primary-via-summary] — https://pngrb.gov.in/pdf/ngp/bid/bid19/Corrigendum15042024.pdf — 15 Apr 2024
- GEM lists the project as "Proposed". [secondary] — https://www.gem.wiki/Ennore_Barshi_Gas_Pipeline — n.d.
- No award, annulment or re-bid found after 2 searches.

**Jammu–Srinagar**
- PNGRB invited bids for about 325 km with initial capacity of at least 2 MMSCMD. The line starts where GAIL's Gurdaspur–Jammu line ends. [press] — https://www.deccanherald.com/india/bidding-process-starts-for-325-km-gas-pipeline-in-kashmir-2858175 — Jan 2024
- Bids were due 13 May 2024. [press] — https://ogj.com/pipelines-transportation/pipelines/article/14303907/india-starts-bidding-for-jammu-srinagar-natural-gas-pipeline — Jan 2024
- No award found. GEM says the earlier "Jammu and Kashmir" project appears cancelled. [secondary] — https://www.gem.wiki/Jammu_and_Kashmir_Gas_Pipeline — n.d.
- Background: PNGRB cancelled the earlier Bhatinda–Jammu–Srinagar authorisation of a GSPL-led consortium for failing to lay the line on time, then bid out Gurdaspur–Jammu. [press] — https://kashmirdespatch.com/gas-pipeline-to-jammu/ — n.d.

**Gurdaspur–Jammu, GAIL**
- PNGRB public notice for the bid dated 6 Jan 2023. [primary-via-summary] — https://pngrb.gov.in/pdf/ngp/bid/bid18/PublicNotice06012023.pdf — 6 Jan 2023
- GAIL and IOCL both qualified technically. Financial bids were opened 21 June (2023) and GAIL won. [press] — https://indiainfrahub.com/featured/gail-emerges-as-successful-bidder-for-175-km-natural-gas-pipeline-to-jk/ — Jun 2023
- PNGRB granted the authorisation to GAIL: 160 km, 12-inch, 3.10 MMSCMD plus 0.78 MMSCMD extra capacity. [press] — https://indianinfrastructure.com/2023/07/29/pngrb-grants-authorisation-to-gail-for-development-of-gurdaspur-jammu-natural-gas-pipeline/ — 29 Jul 2023
- Route through Pathankot, Kathua and Samba. [press] — https://www.ogj.com/pipelines-transportation/pipelines/article/14295531/gail-wins-gurdaspur-jammu-gas-pipeline-project — 2023
- Work began on the "175-km" Gurdaspur–Jammu Tawi line, with household gas targeted for 2026. [press] — https://m.greaterkashmir.com/article/work-on-175-km-gurdaspur-jammu-pipeline-begins-project-to-supply-domestic-gas-by-2026/354580 — Dec 2024
- PNGRB MIS (Dec 2025) gives a target of Jul-26. [primary-via-summary] — https://pngrb.gov.in/data-bank/20251231-NGPL-MIS-Report.pdf — Dec 2025
- Reported nearly 90% complete. No confirmation of commissioning. [press] — https://www.dailyexcelsior.com/gas-grid-uncertainty/ — 2026 (exact date not shown)

**Hazaribagh–Ranchi, IOCL**
- PNGRB bid notice dated 15 Mar 2022. [primary-via-summary] — https://pngrb.gov.in/pdf/ngp/bid/bid17/PN15032022.pdf — 15 Mar 2022
- Authorised 09.02.2023; 71 km in the later MIS reports (68 km in an earlier one); target Feb-26; not yet operational as of early 2026. [primary-via-summary] — https://www.pngrb.gov.in/data-bank/20260131-NGPL-MIS-Report.pdf — Jan 2026
- HLEC Table 12.8 gives 65 km and 1.03 MMSCMD, under construction (as of Dec 2024). [primary] — local `_hlec_part2.md`, Table 12.8 — 2025

**Jamnagar–Dwarka, GSPL**
- Authorised 19.08.2021; 100 km; 3 MMSCMD; Gujarat; expected completion Oct-26; not operational as of Jan 2026. [primary-via-summary] — https://www.pngrb.gov.in/data-bank/20260131-NGPL-MIS-Report.pdf — Jan 2026

**Anjar–Palanpur spur, GSPL (approval, not a bid)**
- PNGRB approved GSPL's Anjar–Palanpur spur in Mar 2025: 274 km, 30-inch, 12 MMSCMD, capex Rs 2,051.18 crore. The capex is excluded from tariff until the actual spend is verified. [press] — https://www.alchempro.com/news/energy-news/pngrb-clears-gspl-s-237-8-mn-anjar-palanpur-pipeline-plan-301469-newsdetails.htm — Mar 2025

**PNGRB activity in 2026**
- No new natural-gas pipeline bid notice from 2025–26 was found. PNGRB's 2026 bidding activity reported in the press is for LPG pipelines (four close to finalisation, nine in all), which are out of scope. [press] — https://www.pressreader.com/india/businessline-kolkata-9wvy/20260418/281560887372926 — 18 Apr 2026
- A PNGRB web page lists an "NGPL Bid for Kanai Chhata – Shrirampur" with no date. It is most likely the 2018 bid page, not a re-bid. [primary-via-summary] — https://pngrb.gov.in/eng-web/ng-bid-12.html — n.d.

### B2. Earlier bid-out pipelines still under construction (status 2025–26)

**Mehsana–Bhatinda and Bhatinda–Gurdaspur, GIGL**
- Mehsana–Bhatinda: authorised 07.07.2011; 1,943 km; 83.1 MMSCMD; 1,318 km done and 624 km remaining (column labels inferred by the summary); target Jun-26; states GJ, RJ, HR, PB. [primary-via-summary] — https://www.pngrb.gov.in/data-bank/20260131-NGPL-MIS-Report.pdf — Jan 2026
- Bhatinda–Gurdaspur: 261 km; target Dec-24 (lapsed). [primary-via-summary] — same — Jan 2026
- HLEC Table 12.8 (as of Dec 2024): Mehsana–Bhatinda 1,940 km, 80.11 MMSCMD, 1,200 km operational, 4.77% utilisation; Bhatinda–Gurdaspur 261 km, 42.42 MMSCMD, 102 km operational. [primary] — local `_hlec_part2.md` — 2025
- A GIGL filing says 1,418 km completed (filing date not shown). [primary-via-summary] — https://bseindia.com/xml-data/corpfiling/AttachHis/\64b0cda8-f5b3-4d98-babd-09a68390213b.pdf — n.d.

**Mallavaram–Bhopal–Bhilwara–Vijaipur, GITL**
- 365 km operating and 1,517 km under construction; 2.2 MMSCMD flowing (~3% utilisation); target still shown as Mar 2020. [primary-via-summary] — https://www.pngrb.gov.in/data-bank/20260131-NGPL-MIS-Report.pdf — Jan 2026
- Phase I (Kunchanapalli–Ramagundam) is operating and supplies the Ramagundam fertiliser plant. Phase II spurs and tap-offs on the Mancherial–Bellampally–Nagpur stretch are pending. [primary-via-summary] (Lok Sabha answer, undated) — https://eparlib.sansad.in/bitstream/123456789/3017823/1/4695.pdf — n.d.

**Ennore–Thiruvallur–Bengaluru–Puducherry–Nagapattinam–Madurai–Tuticorin (ETBPNMTPL), IOCL**
- IOCL: commissioned in phases 2019–2023, now about 1,054 km. [primary-via-summary] — https://iocl.com/gas-pipelines — n.d.
- GEM, citing PNGRB: 1,080 km operating and 351 km under construction as of Mar 2024. [secondary] — https://www.gem.wiki/Ennore-Tuticorin_Gas_Pipeline — n.d. (as of Mar 2024)
- HLEC Table 12.8: authorised 1,431 km, 84.67 MMSCMD, 1,080 km operational, 5.91% utilisation. [primary] — local `_hlec_part2.md` — 2025
- IOCL capacity schedules for Aug and Sep 2026 list five sections and 27 exit points (Sep). [primary-via-summary] — https://iocl.com/Uploads/Schedule1ETBPNMTPLOCTsept26.pdf — Sep 2026

**Mumbai–Nagpur–Jharsuguda (MNJPL), GAIL**
- HLEC Table 12.8: 1,755 km, 16.50 MMSCMD, under construction. [primary] — local `_hlec_part2.md` — 2025
- GAIL completed final testing of the Mumbai–Nagpur section. [press] — https://indianinfrastructure.com/2025/11/19/gail-completes-final-testing-of-mumbai-nagpur-section-of-mumbai-nagpur-jharsuguda-natural-gas-pipeline-project/ — 19 Nov 2025
- Earlier target was full launch by 31 Dec 2025. [press] — https://themachinemaker.com/news/gails-mumbai-nagpur-jharsuguda-pipeline-set-for-full-launch-by-december-31-2025/ — 2025
- GAIL Reg. 30 filing: the Mumbai–Nagpur section and the Chhattisgarh and Odisha sections of Nagpur–Jharsuguda are operational; length given as 1,702 km. [primary-via-summary] — https://nsearchives.nseindia.com/corporate/Himanshugail_31012026172038_Reg30.pdf — 31 Jan 2026
- GAIL board (25 Mar 2026) revised the schedule: the Maharashtra section of Nagpur–Jharsuguda is to be commissioned progressively by 30 Jun 2026, with an extension sought from PNGRB. [primary-via-summary] — https://insights.dsij.in/dsijarticledetail/this-gas-transmission-and-marketing-company-updates-project-pipeline-and-approves-usd-64-million-us-investment-know-the-details — Mar 2026
- Nagpur–Jabalpur spur (317 km) is complete and commissioning is expected soon. [press] — https://www.thehitavada.com/Encyc/2026/3/25/major-energy-boost-gail-finishes-nagpurjabalpur-gas-pipeline-work.html — 25 Mar 2026

**Srikakulam–Angul (SAPL), GAIL**
- HLEC Table 12.8: 690 km authorised (incl. spurs), 6.65 MMSCMD. [primary] — local `_hlec_part2.md` — 2025
- PM inaugurated it on 16 Oct 2025. [press] — https://indianinfrastructure.com/2025/10/17/gails-srikakulam-angul-natural-gas-pipeline-and-iocls-lpg-bottling-plant-inaugurated/ — 17 Oct 2025
- Mainline 422 km (124 km in Andhra Pradesh, 298 km in Odisha); spur lines expected by Jun 2026. [press] — https://chemindigest.com/gails-srikakulam-angul-pipeline-connects-east-india/ — Oct 2025
- Cost reported as about Rs 2,800 crore in one source and Rs 17.3 billion in another (see Conflicts). [press] — https://infrastructuretoday.co.in/steeling-energy-security-sapl-redefines-indias-gas-economy/ — 2025

### B3. Stalled, cancelled or re-routed pipelines (Vision 2040 context)

**PNGRB Vision 2040 expert committee (HLEC) findings, 2025**
- As of Dec 2024, 12 pipelines had been authorised through bidding. Only Shahdol–Phulpur is fully operational; the other 11 are under construction or partly commissioned. The committee blames unrealistically low bid tariffs. [primary] — local `_hlec_part2.md` (line ~259) — 2025
- Recommends PNGRB guidelines on: terminating non-starter projects; tariffs for partly built assets; voluntary surrender; and re-bidding or reallocation. [primary] — same (line ~523) — 2025
- Lists as authorised but not executed or delayed: Kakinada–Vijayawada–Nellore, Ennore–Nellore, Kakinada–Srikakulam, Kanai Chhata–Panitar, Jaigarh–Mangalore. [primary] — same (Annexure 6.1.3) — 2025
- Proposes alternate routes (Table 12.9): KVN → Kakinada–Vijayawada–Kadapa–Chittoor (~705 km); Kanai Chhata–Panitar → Digha–Kolkata–Paschim Medinipur (~300 km); Jaigarh–Mangalore → Mangalore–Shimoga–Dharwad (~400 km). [primary] — same — 2025
- Proposes new lines: Barmer–Jaisalmer–Jodhpur–Bikaner–Churu (~650 km, Barmer–Jaisalmer gas into Mehsana–Bhatinda); Kochi–Kanyakumari–Thoothukkudi (~400–450 km; since authorised, see B1); Jabalpur–Shahdol (~200–250 km). These are 3 of 21 projects in the conceptual 2040 study. [primary] — same — 2025
- No search result showed PNGRB formally cancelling or re-bidding KVN, Kanai Chhata–Panitar or Jaigarh–Mangalore after the report.

**Kakinada–Vijayawada–Nellore, IMC Ltd**
- Authorised 19.02.2018 with completion due Mar 2021; IMC sought an extension to Mar 2024. [primary-via-summary] (Rajya Sabha answer) — https://rsdebate.nic.in/bitstream/123456789/734537/1/PQ_258_19122022_U1421_p417_p417.pdf — 19 Dec 2022
- PNGRB extension letter dated 19.12.2022. [primary-via-summary] — https://www.pngrb.gov.in/eng-web/ngpl-auth.html — n.d.
- PNGRB MIS still lists it: 667 km, IMC, target Mar-24. [primary-via-summary] — https://www.pngrb.gov.in/data-bank/20260131-NGPL-MIS-Report.pdf — Jan 2026
- HLEC: 667 km and 18 MMSCMD in Table 12.8, but the text calls it the "authorised 522-km" project with pipeline-siting issues. [primary] — local `_hlec_part2.md` — 2025

**Kanai Chhata–Panitar (formerly Kanai Chhata–Shrirampur), H-Energy consortium**
- Bid document dated 28 Sep 2018. Authorisation granted 08.07.2019 and accepted 19.07.2019. [primary-via-summary] (H-Energy project sheet) — https://www.henergy.com/uploads/1717924470_KANAI-CHATTA-SHRIRAMPUR-NATURAL-GAS-PIPELINE.pdf — n.d.
- 317 km of trunk and spurs; 19.2 MMSCMD; 4.80 MMSCMD common-carrier capacity. Route: Kanai Chhata/Kukrahati–Narikeldaha–Sargaria–Shrirampur (Nadia). Intended to carry regasified LNG to the Bangladesh border. [primary-via-summary] — same — n.d.
- PNGRB listing shows an extension letter (12 May 2022) and an amendment letter (1 Aug 2022). [primary-via-summary] — https://www.pngrb.gov.in/eng-web/ngpl-auth.html — n.d.
- The 2022 amendment moved the endpoint to Panitar. GEM lists the line as under construction. [secondary] — https://www.gem.wiki/Kanai_Chhata-Shrirampur_Gas_Pipeline — n.d.
- H-Energy and Petrobangla signed an MoU in Jun 2021 for cross-border RLNG supply. [press] — https://www.hydrocarbonengineering.com/refining/24062021/h-energy-signs-lng-mou-with-petrobangla — 24 Jun 2021

**Jaigarh–Mangalore (JMPL), H-Energy**
- Authorised 28 Jun 2016: 635 km, 17 MMSCMD, commissioning due 27 Jun 2019. H-Energy sought to surrender the authorisation on 17 May 2022. PNGRB said there is no provision for surrender, rejected the request and imposed a penalty for delay. [press] — https://psuwatch.com/amp/story/latestnews/pngrb-fines-h-energy-for-delays-in-pipeline-construction — 2022
- GEM says PNGRB cancelled the authorisation by order dated 4 Jul 2022. [secondary] — https://www.gem.wiki/Jaigarh-Mangalore_Gas_Pipeline — n.d.

**Kakinada–Vizag–Srikakulam**
- Cancelled in Dec 2023. PNGRB later proposed a Kakinada–Srikakulam line connecting to IMC's KVN. [secondary] — https://www.gem.wiki/Kakinada-Srikakulam_Gas_Pipeline — n.d.

**Ennore–Nellore, GTIL**
- PNGRB cancelled GTIL's authorisation in Oct 2019; the cancellation was upheld on appeal. [secondary] — https://www.gem.wiki/Ennore-Nellore_Gas_Pipeline — n.d.
- APTEL reviewed the termination; PNGRB had encashed 100% of the Rs 7.30 crore performance bank guarantee. [primary-via-summary] — https://aptel.gov.in/sites/default/files/Jud2023/APL156of23.pdf (one of several APTEL links in the result) — 2023–24
- Earlier precedent (before scope): PNGRB cancelled GAIL's 1,724 km Surat–Paradip authorisation and encashed its PBG by order of 13 Mar 2018. [press] — https://indianinfrastructure.com/2018/04/09/pngrb-cancels-gails-licence-for-the-surat-paradip-natural-gas-pipeline/ — 9 Apr 2018
- No PNGRB cancellation order dated 2024–2026 was found.

### B4. Approvals outside PNGRB bidding

**North East Gas Grid (Indradhanush Gas Grid Ltd)**
- CCEA approved viability gap funding (capital grant) of Rs 5,559 crore, i.e. 60% of the estimated cost. [press] — https://www.tribuneindia.com/news/business/rs-5-559-cr-for-northeast-gas-grid-23662/amp — Jan 2020
- Network of 1,656 km at an estimated Rs 9,265 crore (incl. IDC). The rest (about Rs 3,706 crore) comes from IOCL, ONGC, GAIL, OIL and NRL. Route from Guwahati to Numaligarh, Dimapur, Kohima and Imphal. [press] — https://www.pressreader.com/india/the-free-press-journal/20200113/282441351031987 — 13 Jan 2020
- IGGL had spent Rs 5,361.41 crore by 31 Mar 2024. [press] — https://www.outlookbusiness.com/corporate/iggl-achieves-8535-cumulative-progress — 2024
- PNGRB press note: 396 km Guwahati–Numaligarh section commissioned Jul 2025 and connected to NRL; authorised length 1,688 km; full commissioning planned by 31 Mar 2026. [primary-via-summary] — https://pngrb.gov.in/pdf/press-note/20251203_PR.pdf — 3 Dec 2025
- Phase I (~553 km across Assam, Arunachal Pradesh and Nagaland) inaugurated 13 Mar 2026. [press] — https://indianinfrastructure.com/2026/03/16/capacity-augmentation-of-numaligarh-siliguri-product-pipeline-and-phase-i-of-north-east-gas-grid-witnesses-inauguration/ — 16 Mar 2026
- Nagaland joined the grid on 18 Aug 2026 via a 128 km Dergaon–Dimapur line. A 175 km Duliajan feeder line received PNGRB authorisation on 20 Feb 2026. [press] (single low-reliability aggregator; unverified) — https://discoveryalert.com/news/nagaland-north-east-gas-grid-september-2026/ — Sep 2026
- No revised project cost or grant amount was found.

**Pradhan Mantri Urja Ganga (JHBDPL + Barauni–Guwahati), GAIL**
- GAIL press release: 97.6% laid; commercial operation on 3,119 km (96.6%); 12.26 MMSCMD transported. [primary-via-summary] — https://gailonline.com/PressRelease_09042025.html — 9 Apr 2025
- Durgapur–Haldia (294 km): 132 km to Kolkata operating; 103 of the remaining 162 km to Haldia laid. Dhamra–Haldia: 198 of 240 km laid. Both pushed from Mar 2025 to Dec 2025 because of right-of-use constraints. [primary-via-summary] — same — 9 Apr 2025
- Total length cited as 3,306 km. [press] — https://www.procurementresource.com/news-and-articles/gail-urja-ganga-pipeline-progress-2025 — 2025
- Later report: 3,119 of 3,266 km commissioned; remaining Kolkata–Haldia section now expected by Sep 2026. [press] (source not identified in the summary; appeared with GAIL 2026 items) — https://chemindigest.com/gail-to-invest-rs-12000-crore-in-pipeline-and-lng-infrastructure/ — 2026
- No confirmation of full completion found.

**Cross-border**
- India–Nepal: only the 69 km Motihari–Amlekhgunj petroleum products pipeline exists (inaugurated Sep 2019). It is not a gas line. [press] — https://www.gatewayhouse.in/events/inauguration-of-cross-border-petroleum-products-pipeline/ — Sep 2019
- India gave preliminary consent (2018) to a gas pipeline to Nepal. A Gorakhpur–Bhairahawa (Rupandehi) gas or LNG line was agreed for a feasibility study. No DPR, approval or cost found for 2023–26. [press] — https://kathmandupost.com/money/2018/09/01/india-agrees-to-build-gas-pipeline-to-nepal — 1 Sep 2018; https://thehimalayantimes.com/business/nepal-india-to-study-feasibility-of-liquefied-natural-gas-pipeline-project/ — n.d.
- India–Bangladesh: the only gas-pipeline link found is H-Energy's Kanai Chhata line to the border (MoU Jun 2021, see B3). It is stalled.

**State-level grids**
- Gujarat: GSPL Anjar–Palanpur spur (see B1); Jamnagar–Dwarka (see B1).
- Andhra Pradesh (APGDC), Telangana and Rajasthan: no 2023–26 approvals found. See Gaps.

### B5. Policy context

**Unified tariff**
- PNGRB's Second Amendment to the NG Pipeline Tariff Regulations (dated 07.07.2025) cut the unified tariff zones from three to two. [primary-via-summary] (Parliament answer) — https://eparlib.sansad.in/bitstream/123456789/3022360/1/AU2102_QKF7yV.pdf — 2025
- Same amendment reported on 4–5 Jul 2025. [press] — https://www.tribuneindia.com/news/business/pngrb-approves-pivotal-reforms-in-natural-gas-pipeline-tariff-regulations — Jul 2025
- From 1 Jan 2026: Zone 1 (up to 300 km from source) Rs 54.00/MMBtu; Zone 2 (beyond 300 km) Rs 102.86/MMBtu. CNG and domestic PNG pay Zone 1 everywhere, roughly halving transport charges for consumers beyond 300 km. [press] — https://indianinfrastructure.com/2025/12/16/pngrb-rationalises-unified-tariff-structure-for-natural-gas-transportation/ — 16 Dec 2025
- Business Today report on the same cut. [press] — https://www.businesstoday.in/amp/india/story/consumers-likely-to-get-relief-from-cng-png-bills-as-pngrb-cuts-gas-transportation-tariffs-507090-2025-12-17 — 17 Dec 2025

**National Gas Grid target**
- MoPNG's investible-projects page says about 17,000 km is operating and about 15,500 km more is envisaged to complete the National Gas Grid. No year is given and the figures are clearly dated. [primary-via-summary] — https://mopng.gov.in/en/pdc/investible-projects/oil-amp-gas-infrastructure/natural-gas-pipelines — n.d.
- About 2023, the government said all states were likely to be connected to the grid by 2026. [press] — https://swarajyamag.com/infrastructure/national-gas-grid-68-per-cent-work-complete-all-states-likely-to-get-connected-by-2026 — c. 2023
- No official km-by-year target found.

---

## C. Official totals (newest first)

- PPAC MRR May 2026, Table 20 (as on 31.12.2025): 34,273 km authorised incl. tie-in, dedicated and STPL; 27,427 km operational; 8,489 km under construction. Common-carrier/contract lines: 25,925 km operational, 7,301 km under construction, 33,226 km total. [primary] — local `00-ppac-mrr-may2026-table20.txt` — Jun 2026
- PNGRB CGD MIS Mar 2026 repeats 34,273 / 27,427 / 8,489 under the NGPL heading. [primary-via-summary] — https://pngrb.gov.in/data-bank/20260331-CGD-MIS-Report.pdf — Mar 2026
- PNGRB NGPL MIS Dec 2025 and Jan 2026: 34,273 km authorised, 27,427 km operational. [primary-via-summary] — https://www.pngrb.gov.in/data-bank/20260131-NGPL-MIS-Report.pdf — Jan 2026
- Rajya Sabha reply: PNGRB has authorised about 34,233 km of NGPL network (common carrier, spur, tie-in and dedicated). [primary-via-summary] — via search summary; URL not given — Dec 2025
- PNGRB NGPL MIS Oct and Nov 2025: 34,238 km authorised, 25,923 km operational (as of Sep 2025). [primary-via-summary] — https://pngrb.gov.in/data-bank/20251031-NGPL-MIS-Report.pdf — Oct 2025
- PNGRB NGPL MIS Jul 2025: 34,233 km authorised, 25,429 km operational (as of Jun 2025). [primary-via-summary] — https://pngrb.gov.in/data-bank/20250731-NGPL-MIS-Report.pdf — Jul 2025
- Indian Infrastructure, citing PNGRB as of Mar 2025: 34,233 km authorised, ~25,429 km operational, ~10,459 km under construction. [press] — https://indianinfrastructure.com/2025/08/04/growing-coverage-expansion-of-oil-and-gas-pipeline-infrastructure/ — 4 Aug 2025
- PNGRB press note: about 33,500 km authorised, about 25,000 km operational; nameplate capacity 722 MMSCMD against an assumed ~400 MMSCMD effective carrying capacity of operating pipelines. [primary-via-summary] — https://www.pngrb.gov.in/pdf/press-note/20250407_NG_Projections2030_40.pdf — 7 Apr 2025
- MoPNG year-end review: operational length up from 15,340 km (2014) to 24,945 km (10 Sep 2024), +62.6%; about 10,805 km under execution. [primary-via-summary] (via press) — https://www.tribuneindia.com/news/business/indias-operational-natural-gas-pipeline-expands-by-62-6-development-of-10805-km-under-execution-ministry/amp — 7 Jan 2025
- Indian Infrastructure, as of Sep 2024: 33,475 km authorised, 24,945 km operational. [press] — https://indianinfrastructure.com/2025/01/06/promising-prospects-expanding-pipeline-network-across-the-country/ — 6 Jan 2025
- Older Parliament replies (c. 2023): 33,592 km authorised, 23,173 km operational, 12,206 km under construction; earlier 33,500 / 21,715 / 13,605. [primary-via-summary] (via press) — https://swarajyamag.com/business/21715-km-natural-gas-pipelines-operational-13605-km-length-under-various-stages-of-construction-govt — c. 2022–23
- The MoPNG year-end review for 2025 (Dec 2025 or Jan 2026) and any 2026 Parliament answer with totals were not found.

---

## D. Conflicts

1. **Under-construction total.** PPAC and PNGRB give 8,489 km under construction (Dec 2025), but authorised minus operational is only 6,846 km. The likely reason is that part-operational lines count both sections, or that capacity augmentation is included; this is not verified. Separately, Indian Infrastructure gives 10,459 km (Mar 2025) and the MoPNG review 10,805 km (Sep 2024).
2. **Date label for 34,233 / 25,429.** PNGRB MIS Jul 2025 says "as of Jun 2025"; Indian Infrastructure says "as of Mar 2025".
3. **Jump in operational length.** 25,923 km (Sep 2025) to 27,427 km (Dec 2025) is +1,504 km in one quarter. This could reflect a definitional change (tie-ins and dedicated lines included) rather than new build. PPAC's common-carrier-only figure for the same date is 25,925 km.
4. **Kochi–Thoothukudi length.** 425 km (bid notice) vs 424.65 km (authorisation). Minor.
5. **Gurdaspur–Jammu length.** 160 km (PNGRB authorisation) vs 175 km (press, GAIL). 2022 GAIL statements cite 425 km for Gurdaspur–Srinagar.
6. **Hazaribagh–Ranchi length.** 65 km (HLEC Table 12.8) vs 68 km (earlier MIS) vs 71 km (2025–26 MIS).
7. **Mehsana–Bhatinda.** HLEC gives 1,940 km, 80.11 MMSCMD and 1,200 km operational (Dec 2024); MIS Jan 2026 gives 1,943 km, 83.1 MMSCMD and 1,318 km. The GIGL figure of "1,418 km completed" fits the total of Mehsana–Bhatinda 1,318 + Bhatinda–Gurdaspur 102 = 1,420 km, which also matches PPAC's GIGL operational figure of 1,419 km. So it is probably not a real conflict.
8. **MNJPL length.** 1,755 km (HLEC/PNGRB) vs 1,702 km (GAIL filing Jan 2026) vs 1,707 and 1,780 km (press). The Mumbai–Nagpur section is given as 693 or 694 km.
9. **Srikakulam–Angul.** 690 km authorised (incl. spurs) vs 422 km mainline. Cost ~Rs 2,800 crore vs Rs 17.3 billion (Rs 1,730 crore).
10. **Kakinada–Vijayawada–Nellore length.** 667 km (HLEC Table 12.8 and MIS) vs "authorised 522-km" (HLEC text).
11. **Kanai Chhata line.** 317 km (H-Energy sheet, GEM) vs "about 250 km" (H-Energy web page). GEM places the endpoint in Maharashtra, which is wrong: Shrirampur is in Nadia, West Bengal.
12. **Ennore–Nellore (GTIL).** GEM and APTEL show the authorisation cancelled (Oct 2019, PBG encashed), but HLEC Table 12.8 (2025) lists it as under construction (220 km, 36 MMSCMD).
13. **Jaigarh–Mangalore.** GEM says it was cancelled on 4 Jul 2022, but HLEC (2025) still lists it among "authorised under-construction" pipelines.
14. **Ennore–Barshi deadline.** 16 Apr 2024 (Swarajya, original) vs 16 May 2024 (PNGRB corrigendum, extended). The later date is the operative one.
15. **North East Gas Grid.** Length 1,656 km (CCEA 2020) vs 1,688 km authorised (PNGRB 2025). Cost Rs 9,265 crore vs 9,000 or 9,500 crore in other reports. Grant Rs 5,559 crore approved (pre-approval reports said ~Rs 5,400 crore). The 396 km (Guwahati–Numaligarh) and ~553 km (Phase I) figures describe different scopes.
16. **Urja Ganga total length.** 3,266 km vs 3,306 km. The Dec 2025 completion target was later reported as Sep 2026.
17. **Jammu–Srinagar bid date.** Kashmir Life says 12 Jan 2023; Deccan Herald and OGJ say Jan 2024. Probably 2024 (the Jan 2023 notice was Gurdaspur–Jammu).

---

## E. Gaps

- **No primary document opened.** Every PNGRB, MoPNG, PPAC and NSE/BSE figure is via search summary. Before publication, confirm from the PNGRB NGPL MIS (latest available is probably Aug or Sep 2026, not found) and the PNGRB authorisation page.
- **Ennore–Barshi and Jammu–Srinagar bid outcomes (2024):** no award, annulment or re-bid found.
- **KTPL:** completion schedule, winning tariff and losing bidders not found.
- **Commissioning confirmations missing** for Gurdaspur–Jammu (target Jul 2026), Hazaribagh–Ranchi (Feb 2026), Jamnagar–Dwarka (Oct 2026), the Maharashtra part of MNJPL (Jun 2026), Mehsana–Bhatinda (Jun 2026), full NE Gas Grid (Mar 2026) and the Urja Ganga Haldia tails.
- **No formal 2024–26 PNGRB order** found cancelling or re-bidding KVN, Kanai Chhata–Panitar or Jaigarh–Mangalore after the Vision 2040 recommendations, and no 2025–26 "expression of interest" route pipeline found.
- **National Gas Grid km-by-year target:** not found. The MoPNG year-end review for 2025 and 2026 Parliament answers with totals were not found.
- **State grids:** nothing found for APGDC (Andhra), Telangana or Rajasthan approvals in 2023–26. Gujarat has only GSPL Anjar–Palanpur and Jamnagar–Dwarka.
- **Cross-border:** no 2023–26 approval, DPR or cost found for any India–Nepal gas line or India–Bangladesh gas pipeline.
- **North East Gas Grid:** revised cost, revised grant amount, Duliajan feeder cost, and confirmation of the Aug 2026 Nagaland link (single weak source) are all missing.
- **Costs** are missing for most under-construction bid-out lines (GIGL, GITL, IMC, HPPL, Hazaribagh–Ranchi, Jamnagar–Dwarka).
- **Geometry for the map:** endpoints and towns are listed above, but no GIS or route shapefiles were sought. Route detail beyond main towns would need company route maps.
