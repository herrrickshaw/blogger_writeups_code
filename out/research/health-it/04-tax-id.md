# 04 - Tax-identity side: how India built taxpayer tracking (timeline + numbers)

Research date: 18 Oct 2026. Method: 14 standard WebSearch calls. *.gov.in pages were not fetched; where a gov.in URL is cited it was surfaced (with snippet text) by the search engine, and is labelled "gov URL via search snippet". Everything else is press or secondary. Confidence: **High** = 2+ independent sources or official doc snippet; **Medium** = one decent source; **Low** = blog/single weak source or my background knowledge, not confirmed in this run.

## Headline verdict on the thesis (tax side only)

- **The "decades earlier" framing holds, but "PAN launched in 2003" is wrong.** PAN as a concept dates to 1972, became mandatory in 1976 (Section 139A), and got its modern 10-character computerised format around 1995. The 2003 changes were about **outsourcing issuance** to UTIITSL and NSDL and a **new photo card**, not the creation of PAN.
- **Scale is near-universal for adults:** 80.08 crore PANs as of 31 Mar 2025, of which 66.38 crore were linked to Aadhaar. There were also 1.67 crore active GST taxpayers (June 2026), and 7.8 crore+ ITRs filed for AY 2026-27 by 31 Aug 2026.
- **Vendor figures need correcting.** Infosys's CPC deal (2009) was approved at **Rs 255 crore**, not about Rs 400 crore. The 2019 project was **Rs 4,241.97 crore** for 8.5 years, and it covered **CPC 2.0 and the new e-filing portal together**. These are not two separate deals of Rs 8,500 crore and Rs 4,242 crore. GSTN (2015, Infosys) was **Rs 1,380 crore**, which is confirmed.

## Timeline

| Year | Milestone | Source URL | Confidence |
|---|---|---|---|
| 1972 | PAN concept introduced. It replaced the manual GIR number, which was unique only within a ward or assessing officer. | https://en.wikipedia.org/wiki/Permanent_account_number ; https://bigbasket.bankbazaar.com/pan-card.html | Medium (secondary) |
| 1976 | PAN made mandatory for tax-paying individuals under Sec 139A, Income-tax Act 1961. The section was inserted by the Taxation Laws (Amendment) Act 1975; that Act's name comes from background knowledge and was not verified here. | https://en.wikipedia.org/wiki/Permanent_account_number | Medium |
| 1995 | Manual allotment series abandoned. The 10-character alphanumeric computerised PAN became the standard. | https://en.wikipedia.org/wiki/Permanent_account_number ; https://www.incometaxindia.gov.in/documents/d/guest/1-permanent-account-number-pan-pdf (gov URL via search snippet) | Medium |
| 2003 (by Jul) | PAN card issuance entrusted to UTI (UTIITSL) for a nominal fee, per a Lok Sabha answer of 25 Jul 2003. NSDL (now Protean) is also a PAN service provider. | https://eparlib.nic.in/bitstream/123456789/458875/1/71354.pdf ; https://www.icai.org/post/outsourcing-of-pan-related-services-by-the-income-tax-department | Medium-High (UTI date); NSDL's start year not pinned |
| 2003 | New "superior" PAN card with a colour photo for individuals. From 1 Oct 2003 the IT PAN Service Centres also handle grievances and change requests. | https://www.icai.org/post/outsourcing-of-pan-related-services-by-the-income-tax-department | Medium (exact launch date not stated) |
| 2003-04 | TIN (Tax Information Network) set up by NSDL as the CBDT's data repository. It later hosted Form 26AS viewing via tin-nsdl.com. | https://www.business-standard.com/article/pf/primer-how-to-view-your-tax-credit-form-26as-113052900146_1.html (confirms TIN/NSDL role only) | Low for the year (not confirmed in this run) |
| 2006-07 | E-filing of ITRs mandatory for companies (corporate assessees) from AY 2006-07. The sources disagree: one says e-filing was merely optional for all taxpayers that year. | https://blog.ipleaders.in/e-filing-income-tax-returns/ ; https://taxguru.in/?p=51039 | Low-Medium |
| 2009 | Union Cabinet approves the Centralised Processing Centre (CPC), Bengaluru, at Rs 255 crore over 5 years. An Infosys-led consortium built and ran it. | https://www.pmindia.gov.in/en/news_updates/approval-for-revised-project-cost-and-extension-of-contract-for-the-centralized-processing-center-of-the-income-tax-department-at-bengaluru/ ; https://www.indianemployees.com/cabinet-decision/details/approval-for-revised-project-cost-and-extension-of-contract-for-the-centralized-processing-center-of-the | High (cost); year of approval Medium |
| 2012 | E-filing made compulsory for income above Rs 10 lakh from AY 2012-13 (S.O. 626(E), 28 Mar 2012). One report says the threshold was then cut to Rs 5 lakh for AY 2013-14. | https://www.business-standard.com/article/news-ians/e-filing-of-income-tax-returns-to-surge-on-new-norms-113071400086_1.html ; https://taxguru.in/?p=51039 | Medium |
| c. 2012 | TRACES (TDS Reconciliation Analysis and Correction Enabling System) becomes the portal for TDS and Form 26AS. | https://www.business-standard.com/article/pf/primer-how-to-view-your-tax-credit-form-26as-113052900146_1.html (role only) | Low for the year |
| 2013 (28 Mar) | GSTN incorporated as a not-for-profit SPV. | https://www.thenewsminute.com/news/infosys-expand-team-fix-bugs-create-new-functionalities-gst-network-70722 | Medium |
| 2014 (10 Dec) | Cabinet revises the CPC Bengaluru cost to Rs 1,078.59 crore and extends the Infosys contract to Sep 2017. | https://www.pmindia.gov.in/en/news_updates/approval-for-revised-project-cost-and-extension-of-contract-for-the-centralized-processing-center-of-the-income-tax-department-at-bengaluru/ ; https://www.businesstoday.in/story/infosys-tax-centre-contract-extension-gets-cabinet-aprroval/1/213364.html | High |
| 2015 | Infosys wins the Rs 1,380 crore GSTN contract to build and run the GST back-end for 5 years (about Rs 550 crore capex). | https://www.thenewsminute.com/news/infosys-expand-team-fix-bugs-create-new-functionalities-gst-network-70722 ; https://www.businessinsider.in/infosys-is-working-on-technicalities-of-gst/amp_articleshow/50279678.cms | High |
| 2016 (Jul) | Income Tax Department signs the Project Insight contract with L&T Infotech for data analytics. | https://www.asianage.com/business/taxmen-lt-tie-data-mining-632 ; https://personalfn.com/fns/evading-income-tax-may-soon-become-impossible | Medium |
| 2017 (1 Jul) | GST goes live on GSTN with 66.5 lakh registered taxpayers. Portal glitches follow; CAIT sought a CBI probe of Infosys. | https://a2ztaxcorp.net/?p=36857 ; https://www.thequint.com/news/business/government-blames-infosys-for-gstn-glitches | High |
| 2017 | CBDT allots PAN and TAN within a day to newly incorporated companies via the MCA form; 19,704 companies were covered by 31 Mar 2017. | https://www.moneylife.in/article/cbdt-allots-pan-and-tan-in-a-day-for-ease-of-doing-business/50238.html | Medium |
| 2018 (1 Apr) | Nationwide e-way bill for inter-state movement of goods. | not confirmed in this run | Low (background knowledge) |
| 2019 (16 Jan) | Cabinet approves "Integrated E-filing and CPC 2.0" at Rs 4,241.97 crore over 8.5 years, with Infosys as Managed Service Provider. | https://www.businesstoday.in/latest/economy/story/centre-paid-rs-1645-cr-to-infosys-to-develop-new-i-t-portal-says-mos-finance-302456-2021-07-26 ; https://www.dailypioneer.com/2021/business/govt-paid-rs-164-5-cr-to-infosys-for-new-i-t-portal--chaudhary.html | High |
| 2019 (1 Apr) | Project Insight reported "fully functional". It combines INTRAC (analytics) and CMCPC (compliance notices) and reportedly draws on social-media data. | https://personalfn.com/fns/evading-income-tax-may-soon-become-impossible ; https://www.imf.org/-/media/files/conferences/2025/tokyo/session-4-ms-maya-maheshwari-india-digital-tax-administration-the-role-of-ai.pdf | Medium |
| 2020 (28 May) | Instant e-PAN via Aadhaar e-KYC formally launched: paperless, free, within about 10 minutes, for individuals only. At that point 50.52 crore PANs had been allotted, about 32.17 crore of them Aadhaar-linked. | https://etvbharat.com/english/business/economy/now-one-can-get-instant-pan-via-aadhaar/na20200528170815764 ; https://cleartax.in/s/instant-pan-through-aadhaar | Medium-High |
| 2020 (1 Oct) | GST B2B e-invoicing (IRN) mandatory for turnover above Rs 500 crore. | https://mybillbook.in/s/gst-e-invoice/e-invoice-limit ; https://taxninja.in/blog/gst-e-invoicing-threshold-limit-reduced-to-rs-5-crores | High |
| 2021 (1 Jan / 1 Apr) | E-invoicing threshold cut to Rs 100 crore, then Rs 50 crore. | same as above | High |
| 2021 (Jun) | New Infosys-built e-filing portal (incometax.gov.in) launches with glitches. Rs 164.5 crore had been paid to Infosys by June 2021 (Lok Sabha reply, Jul 2021). Infosys's CEO was summoned to the Finance Ministry in Aug 2021, which comes from background knowledge and was not re-confirmed here. | https://www.businesstoday.in/latest/economy/story/centre-paid-rs-1645-cr-to-infosys-to-develop-new-i-t-portal-says-mos-finance-302456-2021-07-26 ; https://www.outlookbusiness.com/news/income-tax-e-filing-gstn-portals-working-pretty-well-infosys-ceo-news-216512 | Medium-High (glitches + payment); summons Low |
| 2021 (Nov) | Annual Information Statement (AIS) and Taxpayer Information Summary (TIS) introduced. The IMF deck lists AIS under Project Insight but gives no date. | https://www.imf.org/-/media/files/conferences/2025/tokyo/session-4-ms-maya-maheshwari-india-digital-tax-administration-the-role-of-ai.pdf | Low for the exact month (background knowledge: 1 Nov 2021) |
| 2022 (1 Apr / 1 Oct) | E-invoicing threshold cut to Rs 20 crore, then Rs 10 crore. | https://mybillbook.in/s/gst-e-invoice/e-invoice-limit | High |
| 2023 (1 Aug) | E-invoicing threshold cut to Rs 5 crore (CBIC Notification 10/2023, 10 May 2023). Still Rs 5 crore as of mid-2026. | https://www.outlookbusiness.com/news/businesses-with-turnover-of-over-rs-5-crore-to-generate-e-invoice-from-august-1-news-285364 ; https://www.accountune.com/e-invoicing-compulsory-india-small-business-2026 | High |
| 2024 (25 Nov) | CCEA approves PAN 2.0 at Rs 1,435 crore. It aims to make PAN a "common business identifier" and to unify the PAN/TAN services spread across the e-filing portal, UTIITSL and Protean. Existing PANs stay valid and the upgrade is free. | https://www.business-standard.com/india-news/govt-announces-rs-1-435-cr-project-to-make-pan-a-common-business-identifier-124112501229_1.html ; https://www.taxscan.in/?p=459914 | High |
| 2025 | PAN 2.0 build awarded to LTIMindtree with a reported bid above Rs 792 crore and an 18-month go-live target. | https://www.outlookbusiness.com/corporate/pan-20-project-awarded-to-ltimindtree-by-income-tax-department | Medium (single source; award date not pinned) |
| 2026 (mid) | PAN 2.0 unified portal reported in "advanced testing", with the old portals still running. No confirmed go-live date found. | https://www.thecurrentindia.com/govt/pan-2-0-features-explained/ | Low-Medium |

## Key numbers

| Metric | Value | As of | Source | Confidence |
|---|---|---|---|---|
| Total PANs allotted | 80,07,78,637 (about 80.1 crore) | 31 Mar 2025 | https://incometaxindia.gov.in/Documents/Direct%20Tax%20Data/Income-Tax-Department-PAN-Allotment-Statistics-Up-to-31-03-2025.pdf (gov URL via search snippet) | High |
| PANs held by individuals | 78,44,49,739 (97.97%) | 31 Mar 2025 | same | High |
| PANs held by firms | 65,58,224 (0.82%) | 31 Mar 2025 | same | High |
| PANs held by companies | 27,38,868 (0.35%) | 31 Mar 2025 | same | High |
| PANs held by AOPs / HUFs / trusts / government | 27,35,561 / 25,15,371 / 13,18,782 / 88,293 | 31 Mar 2025 | same | High |
| PANs linked with Aadhaar | 66,37,93,569 (about 66.4 crore, about 83% of all PANs) | 31 Mar 2025 | same | High (the percentage is my arithmetic) |
| PANs not linked (excluding exempt categories) | 11.48 crore; Rs 601.97 crore in late-link fees collected 1 Jul 2023 to 31 Jan 2024 | 29 Jan 2024 | https://thewire.in/government/union-govt-pockets-rs-601-97-crore-in-penalties-for-not-linking-pan-to-aadhaar-finance-ministry | Medium-High |
| Total PANs (earlier benchmarks) | 50.52 crore (May 2020); 74.67 crore (Mar 2024) | - | ETV Bharat 2020; https://www.republicworld.com/money/personal-finance/pan-ownership-gap-shrinks-with-4210-crore-males-and-3105-crore-females-holding-cards | Medium |
| Growth in PANs | about 5.4 crore new PANs in FY 2024-25 (80.08 minus 74.67) | - | my arithmetic | Medium |
| ITRs filed, AY 2026-27 | 7.8 crore+ (record), of which 5.9 crore+ ITR-1/ITR-2 were filed by 31 Jul | 31 Aug 2026 | https://telanganatoday.com/record-7-8-crore-itrs-filed-for-ay-2026-27 ; https://www.ibef.org/news/over-7-8-crore-itrs-filed-for-ay-2026-27-by-august-31-income-tax-department | High |
| ITRs filed, AY 2025-26 | 7.3 crore+ | by 16 Sep 2025 (extended due date) | same reports | Medium-High |
| Active GST taxpayers | 1,67,14,646, of which about 1.49 crore are normal and 13.55 lakh are composition taxpayers | 30 Jun 2026 | https://a2ztaxcorp.net/nine-years-of-gst-taxpayer-base-crosses-1-67-crore-as-indias-digital-indirect-tax-ecosystem-scales-new-milestones-report-highlights-expansion-of-taxpayer-base-192-27-crore-returns-filed-an/ (citing a GSTN report) | High |
| GST registrations at launch | 66.5 lakh | Jul 2017 | Finance Ministry statement via a2ztaxcorp / studyiq | High |
| GST returns filed (cumulative) | 192.27 crore | 9 years to mid-2026 | a2ztaxcorp headline, same link | Medium |
| TAN count | not found | - | - | Gap |
| Infosys CPC (original) | Rs 255 crore over 5 years | approved 2009 | pmindia.gov.in / indianemployees.com | High |
| Infosys CPC (revised) | Rs 1,078.59 crore, extended to Sep 2017 | 10 Dec 2014 | pmindia.gov.in; Business Today | High |
| Integrated e-filing and CPC 2.0 (Infosys) | Rs 4,241.97 crore over 8.5 years; Rs 164.5 crore paid to Infosys from Jan 2019 to Jun 2021 | approved 16 Jan 2019 | Business Today / Daily Pioneer (Lok Sabha reply) | High |
| GSTN (Infosys) | Rs 1,380 crore for 5 years, of which about Rs 550 crore capex | 2015 | The News Minute; Business Insider | High |
| PAN 2.0 | Rs 1,435 crore outlay; LTIMindtree bid above Rs 792 crore | Nov 2024 approval | Business Standard; Outlook Business | High / Medium |
| Time to get a PAN today | Individual: e-PAN within about 10 minutes via Aadhaar OTP. New company: PAN and TAN on incorporation, within a day, since 2017. | - | cleartax / vikaspedia; Moneylife | Medium-High |

## Notes per question

### Q1. PAN history: what happened in 2003 and what came earlier
- **Pre-1972:** Taxpayers had a GIR (General Index Register) number. It was manual and unique only within a ward or assessing officer, so it could not trace a person across the country.
- **1972 / 1976:** The PAN concept was introduced in 1972 and made mandatory/statutory under Section 139A around 1976. The sources blur the two: Wikipedia says "1972... made statutory under 139A", while BankBazaar says mandatory from 1976. Write "introduced in 1972, made mandatory in 1976" and avoid "Section 139A, 1972" as a single claim.
- **1995:** The old manual series was abandoned and the computerised 10-character alphanumeric PAN became the format. It is unique nationwide and still used today.
- **2003:** This is when PAN *issuance* was outsourced. A Lok Sabha answer of 25 Jul 2003 confirms PAN card issuance was entrusted to UTI (UTIITSL) for a nominal fee. NSDL e-Gov (now Protean) is the other service provider. The exact NSDL start month was not confirmed, though it was likely the same period. A new card with a colour photo ("superior card") arrived with the outsourcing, and from 1 Oct 2003 the PAN service centres also handled change requests. **Correct the user's belief:** PAN was not launched in 2003. 2003 brought the modern card and the outsourced, mass-scale issuance pipeline.
- **PAN 2.0:** Approved 25 Nov 2024 at Rs 1,435 crore. It is a single unified portal for PAN/TAN, with a QR code on the card and a free upgrade with no new numbers. The build reportedly went to LTIMindtree (bid above Rs 792 crore, 18-month target). As of mid-2026 it is reported in advanced testing with no confirmed full go-live. One Hindi source dates the approval to Nov 2025, which conflicts with Business Standard; treat that source as wrong.

### Q2. Scale now
- The latest official PAN statistics found are for 31 Mar 2025: 80.08 crore PANs. Companies (27.4 lakh) and firms (65.6 lakh) are tiny shares; individuals are 97.97%. No 31 Mar 2026 edition was surfaced.
- PAN-Aadhaar: 66.38 crore linked as of 31 Mar 2025. The unlinked figure was 11.48 crore (non-exempt) in Jan 2024. A CBDT circular of 3 Apr 2025 set a 31 Dec 2025 deadline for PANs allotted on an Aadhaar enrolment ID (single source: outlookmoney).
- ITRs: AY 2026-27 is a record at 7.8 crore+ by 31 Aug 2026, against 7.3 crore+ for AY 2025-26 by 16 Sep 2025. **Article angle:** 80 crore PANs against about 7.8 crore returns means fewer than 1 in 10 PAN holders files.
- GST: 1.67 crore active taxpayers (30 Jun 2026), up from 66.5 lakh in 2017. Net additions were 7.9 lakh in H1 2026, led by UP (22 lakh+).
- TAN: no count found.

### Q3. Tracking machinery
- TIN (NSDL), about 2003-04: the role is confirmed, the year is not.
- Form 26AS: the annual tax-credit statement, first viewable via TIN-NSDL. No launch year was confirmed in this run.
- TRACES: TDS reconciliation portal, about 2012. The year was not confirmed here.
- CPC Bengaluru: approved 2009 at Rs 255 crore with an Infosys-led consortium. Background knowledge puts it in operation from about 2010; not confirmed here.
- E-filing: mandatory for corporates from AY 2006-07 (blog sources conflict), and compulsory above Rs 10 lakh income from AY 2012-13.
- AIS: Nov 2021 per background knowledge. The IMF deck links it to Project Insight but gives no date.
- GSTN: SPV incorporated 28 Mar 2013, Infosys contract 2015, live 1 Jul 2017.
- E-way bill: 1 Apr 2018. Not confirmed in this run.
- E-invoicing: Rs 500 cr (Oct 2020), then Rs 100 cr (Jan 2021), Rs 50 cr (Apr 2021), Rs 20 cr (Apr 2022), Rs 10 cr (Oct 2022), and Rs 5 cr (1 Aug 2023, still current). A rumoured Rs 2 crore proposal is unverified.
- Project Insight: L&T Infotech contract in Jul 2016, fully functional 1 Apr 2019. It has INTRAC (analytics) and CMCPC (compliance) units and reportedly uses social-media data.

### Q4. Vendors and money (corrections to the user's figures)
- **CPC 2009:** Rs 255 crore approved, **not about Rs 400 crore**. It was revised to Rs 1,078.59 crore in Dec 2014.
- **CPC 2.0 2019:** Rs 4,241.97 crore over 8.5 years, **not Rs 8,500 crore**. No source supports Rs 8,500 crore.
- **E-filing portal 2021:** It was **not a separate Rs 4,242 crore contract**. The Rs 4,241.97 crore approval of 16 Jan 2019 covered integrated e-filing and CPC 2.0 together, and the 2021 portal was built under it. Rs 164.5 crore had been paid to Infosys by Jun 2021.
- **2021 glitches:** The portal launched in Jun 2021 with widespread problems. The government stated the Rs 164.5 crore payment figure in Parliament amid the criticism. Infosys's CEO later said the portals were "working pretty well".
- **GSTN 2015:** Rs 1,380 crore confirmed (5-year build-and-run, about Rs 550 crore capex). In 2017 there were glitches and CAIT demanded a CBI probe; CAIT's "Rs 1,400 crore+" is a rounded or inflated figure.
- **Non-Infosys players:** NSDL/Protean (TIN, PAN), UTIITSL (PAN), L&T Infotech (Project Insight), LTIMindtree (PAN 2.0).

### Q5. Speed of identification today
- **Individual:** Instant e-PAN via Aadhaar OTP takes about 10 minutes, is free and paperless, and has been formally available since 28 May 2020. The launch date is inferred from the dated ETV Bharat URL plus the CBDT figure of the same week.
- **Company:** Since 2017, PAN and TAN are allotted within a day of incorporation through the MCA form; 19,704 companies had been covered by 31 Mar 2017. **Contrast for the article:** a new company is known to the tax system from day 1 of its legal existence, and an adult can get a nationally unique tax ID in 10 minutes.

## Gaps
- **TAN count:** not found.
- **PAN statistics as of 31 Mar 2026:** not found. The 2025 figures are the latest.
- **Exact start dates not confirmed in this run:** TIN (2003-04), TRACES (about 2012), Form 26AS, the CPC going operational (about 2010), the e-way bill (1 Apr 2018), AIS (1 Nov 2021), and NSDL's PAN start month in 2003. These are background knowledge and marked Low.
- **Sec 139A:** whether it was inserted in 1975 or 1976 (Taxation Laws (Amendment) Act) is not verified. The "1972 Sec 139A" phrasing in secondary sources is loose.
- **E-filing:** whether it was optional for all or mandatory for corporates in 2004-07 is unresolved; the sources conflict.
- **PAN 2.0:** the LTIMindtree award date and the go-live status are single-sourced, and no official go-live was found as of Oct 2026.
- **Infosys CEO summons (Aug 2021):** not re-sourced in this run.
- **gov.in documents:** the PAN statistics PDF, pmindia and eparlib were seen only through search snippets. Before publishing, verify the exact figures by opening the PDFs directly.
