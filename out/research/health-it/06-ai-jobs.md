# 06 - AI and health-BPM jobs: export jobs at risk vs. jobs in India's own health system (research notes)

Compiled 18 Oct 2026 for the conclusion of the "health-it vs tax-id" article (masaladeutsch.blogspot.com).
Method: 14 WebSearch calls (standard mode). I also tried WebFetch to check four primary pages (bls.gov, digitalhealthnews.com, nexdigm.com, kashmirlife.net), but all four failed with DNS errors. So **every figure below comes from a search-result summary (SR)** and was not read on the source page. Check before publishing. *.gov.in sites were not accessed. Where a gov figure appears, it is a press or secondary report of it, or a nic.in parliamentary PDF that surfaced in search results.
Confidence: H = official statistic and consistent across sources; M = one good source (official figure reported by press, or reputable trade outlet); L = vendor, aggregator, or single secondary source; "derived" = my own arithmetic.

## Key numbers

| Item | Figure | Period | Source URL | Confidence |
|---|---|---|---|---|
| US medical transcriptionists, employment | 43,900 (2024) to 41,800 (2034), -4.9% | 2024-34 projection | https://www.bls.gov/ooh/healthcare/medical-transcriptionists.htm (OOH says "decline 5 percent"); exact headcounts via secondary sites e.g. https://wagedex.com/jobs/medical-transcriptionists | M-H (BLS via SR; headcounts secondary) |
| US medical transcriptionists, openings and pay | ~7,400 openings/yr, mostly replacement; median wage US$37,550 | May 2024 wage; 2024-34 openings | https://www.bls.gov/ooh/healthcare/medical-transcriptionists.htm | M-H (SR) |
| Abridge scale (vendor claim) | >300 health systems live; >100 mn clinical conversations/yr | ~2025-26 | https://www.beri.net/tools/abridge (directory citing company) | L |
| Abridge revenue / price | ~US$100 mn ARR; ~US$2,500 per clinician per year | May 2025 | https://sacra.com/c/abridge/ | L (analyst estimate) |
| Epic native AI charting | Announced Aug 2025 (UGM); limited use from early 2026; uses Microsoft Dragon ambient tech for transcription/diarisation | Aug 2025 announcement | https://www.digitalhealth.net/2025/08/epic-announces-the-launch-of-native-ai-charting-tool/ | M |
| Dragon Copilot price (one customer's estimate) | "a couple hundred dollars per month per provider" (Mount Nittany Health CHIO) | Feb 2026 | https://distilinfo.com/2026/02/25/epic-ai-charting-reshapes-clinical-documentation/ | L (single quote) |
| AI scribe outcomes (AHA market scan) | +0.49 visits/clinician/week; Mass General Brigham burnout -21.2% after 84 days; Cooper: 4.15 min saved per patient (Dragon) | Apr 2026 | https://www.aha.org/aha-center-health-innovation-market-scan/2026-04-14-6-health-systems-enhancing-care-delivery-ambient-ai-scribes | M |
| Autonomous coding productivity (pilot) | "700% increase in productivity" in one unnamed pilot (AGS Health CIO) | ~2025 | https://www.hfma.org/revenue-cycle/coding/why-autonomous-coding-is-having-a-moment-in-healthcare/ | L-M (vendor quote, unnamed pilot) |
| Autonomous coding automation rates | 65-80% direct-to-bill at leading outpatient sites; 30-45% inpatient with no coder touch | 2026 roundup | https://stealthagents.com/research/ai-medical-coding-automation-statistics-2026 | L (weak sourcing; do not use without caveat) |
| Radiology autonomous coding pilot | 28% cut in coder workload (OHSU + CodaMetrix) | undated | same stealthagents page | L (aggregator) |
| Omega Healthcare AI productivity | +10-20% human productivity in RCM from AI; CEO expects at least +20% more over ~2 years | ~2025 | https://healthcareitnews.com/news/vast-majority-top-healthcare-execs-betting-ai-rev-cycle-efficiencies | M (CEO statement) |
| India healthcare BPM workforce | ~300,000 (3 lakh) professionals; healthcare services exports >US$10 bn; ~100,000 medical coders trained per year | ~2025 | https://www.nexdigm.com/market-research/insights/blog/india-healthcare-bpo-services-industry/ | L (consultancy blog; original source not seen) |
| India healthcare BPO market | US$11.35 bn (2025) to ~US$21.7 bn (2030), 13.8% CAGR | 2025-30 | https://www.marketsandmarkets.com/Market-Reports/geography/healthcare-outsourcing-bpo-market/India | L (vendor estimate) |
| US demand for offshore RCM | 70% of hospitals/health systems plan to expand offshore RCM (HFMA survey) | ~2025 | https://news.outsourceaccelerator.com/us-hospitals-rcm-india/ | L (secondary report of survey) |
| Indian jobs at risk from AI in health BPM | **No credible estimate found** | - | - | - |
| PM-JAY hospital admissions authorised | **2.74 crore** in FY2025-26; 3.75 crore Ayushman cards created; 5,074 hospitals empanelled in the year | FY2025-26 | https://kashmirlife.net/jammu-kashmir-gets-rs-96-58-crore-under-ab-pmjay-in-2025-26-over-4-08-lakh-cashless-hospital-admissions-recorded-446972/ (citing Lok Sabha reply) | M |
| PM-JAY cumulative | 12.69 crore admissions, >Rs 1.92 lakh crore (as of 30 Jun 2026); earlier 8.59 crore, Rs 1.19 lakh crore (as of 1 Jan 2025) | to 30 Jun 2026 | https://www.outlookmoney.com/retirement/ayushman-bharat-pm-jay-coverage-hospital-admissions-and-number-of-beneficiaries-explained ; https://morungexpress.com/ab-pmjay-enables-1269-crore-cashless-hospital-admissions-worth-rs-192-lakh-crore-govt ; https://rsdebate.nic.in/bitstream/123456789/757934/1/PQ_267_04022025_U290_p518_p522.pdf | M |
| PM-JAY admissions, Jan 2025 to Jun 2026 | ~4.1 crore in 18 months (12.69 - 8.59), about 2.7 crore/yr | derived | above | derived |
| Private health-insurance claims (IRDAI) | **3.26 crore** health claims processed; 87% settled, 8% repudiated, ~5% pending | FY2024-25 | https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/94048/Type/eDaily ; https://www.business-standard.com/finance/personal-finance/paying-claims-or-pushing-back-what-irdai-data-reveals-about-insurers-126010100580_1.html | M |
| Health insurance premium | Rs 1,27,417 crore (+9.19%) | FY2024-25 | https://www.outlookmoney.com/insurance/irdai-2024-25-annual-report-health-premiums-cross-rs-127-lakh-crore-mark | M |
| Domestic claims workload (rough) | ~6 crore claims/pre-auth events a year (2.74 cr PM-JAY + 3.26 cr IRDAI) | derived, mixed years | above | derived (L: years differ; some PM-JAY states run through insurers, so there may be overlap) |
| NHCX integration | "nearly 50 insurers, ~250 major private hospitals" engaged in integration; onboarding voluntary; FHIR-based e-claims | undated (likely 2024) | https://www.outlookbusiness.com/news/nhcx-gains-momentum-more-medical-insurers-joining-platform-for-efficient-claim-processing | L (date unclear; probably stale) |
| PM-JAY empanelled hospitals | >27,000, incl. 11,908 private | undated (2025-26) | https://www.newsonair.gov.in/over-27000-hospitals-including-11908-private-hospitals-are-empaneled-under-ayushman-bharat-pmjay-till-date | M |
| Bhashini-NHA MoU | Multilingual voice AI (ASR, translation, TTS) across Ayushman Bharat platforms; an official named "clinical documentation" as a use | ~Feb 2026 (page date) | https://indiamedtoday.com/digital-india-bhashini-division-signs-mou-with-national-health-authority/ ; https://www.digitalhealthnews.com/bhashini-partners-with-nha-to-deploy-multilingual-voice-enabled-ai-across-ayushman-bharat-platforms | M (announcement only) |
| Job-creation claim (PM-JAY, not ABDM) | "11 lakh new jobs in 5-7 years" (PM Modi) | Oct 2019 | https://theprint.in/india/governance/11-lakh-jobs-will-generate-due-to-ayushman-bharat-in-5-7-years-pm-modi/299799/ | M as a quote; L as an estimate (no methodology) |
| ABDM budget | Rs 1,600 crore over 5 years; "will generate employment", no figure given | Feb 2022 cabinet approval | https://www.theweek.in/news/india/2022/02/26/cabinet-approves-implementation-of-ayushman-bharat-digital-missi.amp.html | M |

## Notes per question

### (A) Jobs at risk

**1. Decline of medical transcription**
- BLS OOH (via SR): employment is projected to fall **5% in 2024-34**, with about **7,400 openings a year**, nearly all replacement. Median pay was **US$37,550 (May 2024)**. Secondary sites citing the BLS projections table give **43,900 to 41,800 (-4.9%)**. One secondary site gives a May 2025 median of US$40,410, which I have not verified. The BLS profile's own wording on *why* (speech recognition, outsourcing, productivity) was not read directly. A transcription-firm page quotes BLS as citing "increased productivity stemming from technological advances and outsourcing" (https://allegistranscription.com/medical-transcription-services/, secondary).
- Article angle: in the US the occupation is small and shrinking slowly, and openings are mostly replacements. The bigger shock to Indian transcription happened earlier (speech recognition with human editing, 2006-2014) and is happening now (ambient scribes that never produce a dictation file to transcribe).
- **India MT industry, then vs now: no credible figure found.** Search returned only older trade pieces: ValueNotes 2006, "threatened by voice recognition" (https://www.valuenotes.biz/medical-transcription-industry-threatened-by-voice-recognition-technology/); a ValueNotes "silent revival" note; M*Modal planning ~500 jobs at Mysore (https://cdn.auntminnie.com/imaging-informatics/enterprise-imaging/is/article/15604934/mmodal-expands-operations-in-india, undated, roughly early 2010s); and a 2011 For The Record piece on per-line rates falling from 9.5 to 3.5 US cents when transcription became editing speech-recognition drafts (https://www.fortherecordmag.com/archives/112111p10.shtml). An opinion essay on shashitharoor.in says AI/voice recognition "collapsed" the MT business, but it gives no numbers. No peak-workforce number and no count of closures. Do not state one.

**2. Ambient AI scribes (US)**
- No independent national count of clinicians using ambient scribes was found. Vendor scale: Abridge claims **>300 health systems** and **>100 mn conversations/yr** (directory listing citing the company, L). Sacra estimated **US$100 mn ARR (May 2025)** at **~US$2,500/clinician/yr**.
- **Epic** announced native AI charting at UGM in **Aug 2025**, for limited use from **early 2026**, built on Microsoft's Dragon ambient technology. Customers can keep third-party scribes (digitalhealth.net). One secondary source says Epic runs in ~42% of US hospitals (L). A Feb 2026 piece reports Mount Nittany Health moving to Epic AI Charting, with a Dragon Copilot cost of "a couple hundred dollars per month per provider". Epic pricing was not public.
- **Microsoft Dragon Copilot** (successor to Nuance DAX Copilot) added generally available ambient documentation for **nursing** in **Oct 2025** (https://hitconsultant.net/2025/10/16/microsoft-unveils-expanded-dragon-copilot/). No user counts were found.
- Outcomes (AHA market scan, 14 Apr 2026): +0.49 visits/week, MGB burnout -21.2% after 84 days, Cooper 4.15 min saved per patient.
- One search summary said VCs put "nearly US$1 bn" into Abridge, Suki, Ambience etc. in 2025. The page carrying it was not identified, so treat it as **unverified**.
- Why this matters for India: the documentation is produced at the point of care by software inside the EHR. There is no audio file to send offshore, so transcription demand is removed rather than offshored.

**3. Autonomous coding and AI in RCM**
- Vendors' claims vary widely. AGS Health (Indian RCM major) itself says broad ">80% chart coverage" claims are "often overhyped" and that fallout to human coders is common. It sells a hybrid model (100% of charts coded at ≥95% quality, with exceptions routed to its coders) (https://www.agshealth.com/ai-platform/autonomous-coding/). Its CIO cited a **700% productivity** jump in one unnamed pilot (HFMA).
- Aggregator figures (L): 65-80% direct-to-bill outpatient and 30-45% inpatient; OHSU/CodaMetrix radiology pilot **-28% coder workload**.
- GeBBS (Indian RCM) white paper, May 2025: autonomous coding lets volume grow "without adding headcount" (https://gebbs.com/wp-content/uploads/2025/05/Autonomous-Coding-White-Paper_GeBBS_May-2025.pdf). This is vendor framing, but it is the clearest statement of the mechanism: jobs are not cut, hiring is decoupled from volume.
- **Omega Healthcare** CEO Anurag Mehta: AI raised human productivity in RCM by **10-20%**, with at least another 20% expected. Omega widened its Microsoft generative/agentic AI tie-up in **Jul 2025** (https://hitconsultant.net/2025/07/14/omega-healthcare-expands-microsoft-collaboration/). It is growing its Philippines workforce toward ~5,000 (insiderph.com).
- **Access Healthcare**: plans to add 1,000 staff in coding/documentation/AR (DT Next via company blog, **undated**).
- **No layoffs or headcount cuts attributed to AI** were found for AGS, Omega, R1 RCM India, Access, GeBBS or Cognizant in 2025-26. R1 RCM India returned nothing. Honest framing: so far the evidence shows **productivity per worker rising and hiring decoupling from volume**, not visible mass layoffs.

**4. How many Indian jobs, and how many at risk**
- Stock: **~3 lakh (300,000)** in healthcare BPM, plus **~1 lakh coders trained per year** (Nexdigm blog, L). Related figure in 02-gccs.md: healthcare/life-sciences GCCs have ~3 lakh staff. These are different populations (third-party BPM vs captive centres) and should not be added together without care.
- Demand is still rising: the HFMA survey says 70% of US providers plan to expand offshore RCM. Market estimate US$11.35 bn (2025) to US$21.7 bn (2030), vendor estimate.
- Risk commentary: a Medical Buyer piece ("Inside India's medical coding army and Carlyle's USD 400m bet on AI", https://medicalbuyer.co.in/inside-indias-medical-coding-army-and-carlyles-usd-400m-bet-on-ai/) argues that if AI coding accuracy improves faster than expected, the economics of large offshore coding teams "could erode quickly". It also notes possible US political pushback against offshoring billing data. The Ken has a related piece ("How an army of Indian graduates keeps America's hospital bills error-free"), paywalled, contents not seen.
- **No NASSCOM, ISG or industry-body estimate of Indian health-BPM jobs at risk from AI was found. Do not invent one.**

### (B) Jobs from adapting to India

**5. Indian-language medical speech and documentation**
- **Eka Care's EkaScribe**: an ambient scribe for Indian clinics that produces structured notes and prescriptions, works in Hindi, Tamil, Kannada, Gujarati and other languages, is described as ABDM-compliant, and runs on Eka's own clinical speech/LLM model **Parrotlet**. It is available via platform/API (https://biovoicenews.com/eka-cares-ai-powered-ekascribe-aims-to-transform-clinical-documentation-for-doctors-across-india/ ; https://www.digitalhealthnews.com/eka-care-launches-india-s-first-ai-medical-scribe-powered-by-its-own-purpose-built-llm-parrotlet-). Eka is also working with **NVIDIA** on an **offline** multilingual scribe, still in development (https://www.digitalhealthnews.com/eka-care-nvidia-partner-to-develop-offline-multilingual-ai-medical-scribe-for-india). These are company press claims. No independent accuracy data or user count was found.
- **Bhashini x NHA MoU**: multilingual voice AI (ASR, translation, TTS) across Ayushman Bharat platforms. An official cited clinical documentation as a possible use. The page date reads around **9 Feb 2026**. This is an announcement only, with no rollout data. Separately, **Ayush ministry x Bhashini** aims at services in all 22 scheduled languages (https://www.outlookindia.com/amp/story/healthcare-spotlight/ayush-ministry-ties-up-with-bhashini-to-make-digital-healthcare-services-available-in-22-languages).
- **AI4Bharat** (IIT Madras): its open ASR/MT/TTS models underpin Bhashini. Nandan Nilekani's grants total INR 70 crore (https://india.entrepreneur.com/news-and-trends/nandan-nilekani-increases-support-to-ai4bharat-with-total/492931). The **DISPLACE-M** challenge (arXiv 2603.02813, ~Mar 2026) benchmarks speech systems on **frontline health conversations**, using AI4Bharat's IndicConformer (22 languages) as the baseline (https://arxiv.org/pdf/2603.02813). This is evidence that Indian-language clinical speech is still an open research problem.
- No ICMR or NHA programme specifically for AI clinical documentation was found beyond the Bhashini MoU.
- Jobs angle (my inference, not a sourced figure): Indian-language clinical ASR needs annotated medical speech in 22 languages, plus human review and QA of drafts. That is the same skill set Indian MT editors used on US dictation, applied to a domestic market where no labelled data yet exists.

**6. Coders and claims processors for India's own system**
- **PM-JAY: 2.74 crore hospital admissions authorised in FY2025-26** (Lok Sabha reply, via Kashmir Life). Cumulative **12.69 crore admissions / Rs 1.92 lakh crore by 30 Jun 2026**. Every one needs pre-authorisation and claim adjudication against package codes.
- **Private insurance: 3.26 crore health claims processed in FY2024-25** (IRDAI annual report via press). 8% were repudiated and ~5% pending, so disputes and documentation are a real workload. Premiums were Rs 1.27 lakh crore.
- Combined, India generates roughly **~6 crore health claims a year** (derived; years and definitions differ, and some overlap is possible where states run PM-JAY in insurance mode). By comparison, US claims number in the billions, so India's volume is smaller but large and growing.
- **NHCX**: FHIR-based e-claims exchange, built by NHA, with voluntary onboarding. The latest count found is "nearly 50 insurers, ~250 major hospitals" engaged in integration (Outlook Business, date unclear, probably 2024). **No current transaction volume found.**
- **ICD-coding requirement in India: no source found** stating that NHCX or IRDAI mandates ICD-10 coding of claims. Do not assert one. PM-JAY uses its own Health Benefit Package codes (general knowledge, not checked this round).

**7. Digitising records at facilities**
- **>27,000 PM-JAY-empanelled hospitals**, incl. 11,908 private (newsonair, undated).
- **Pradhan Mantri Arogya Mitras (PMAMs)**: every empanelled hospital must provide them. They are the first point of contact and handle beneficiary registration and e-card/"golden record" generation (Goa DIP release https://dip.goa.gov.in/governor-to-launch-pradhan-mantri-jan-arogya-yojana-on-sept-23/ ; https://compass.rauias.com/current-affairs/pradhan-mantri-jan-arogya-yojana-pmjay/). **No national headcount or wage for Arogya Mitras was found.**
- **Not found this round:** PHC/CHC/Ayushman Arogya Mandir counts (03-domestic.md may have them), the scale of paper records, data-entry operator or ASHA app-work programmes, Scan-and-Share token volumes, and wages.

**8. Estimates of jobs from ABDM / digital health**
- **No ABDM-specific job estimate found** (no NHA, NITI Aayog or consultancy figure). The 2022 cabinet approval (Rs 1,600 crore over 5 years) says only that ABDM "will generate employment".
- The often-quoted **"11 lakh jobs in 5-7 years"** (PM Modi, Oct 2019) is about **PM-JAY**, not ABDM, and comes with no published method. If used, it must be labelled as a political claim.

## Gaps
- Primary pages were not opened (WebFetch failed with DNS errors). All figures are from search summaries.
- India medical transcription: no peak-workforce number, no count of closures, no current size.
- No independent count of US clinicians/health systems using ambient scribes. Dragon Copilot and Epic AI Charting user numbers were not found.
- No credible estimate of Indian health-BPM jobs at risk from AI. No AI-attributed layoffs found at Indian RCM firms. Nothing on R1 RCM India or Cognizant health-BPM headcount for 2025-26.
- Autonomous-coding automation rates come only from vendors or aggregators. There is no peer-reviewed figure.
- NHCX: no current claim volume or integration count. No ICD-10 mandate found.
- Arogya Mitra numbers and wages, data-entry operator programmes, Scan-and-Share volumes, PHC/CHC counts and paper-record scale: not found.
- No ABDM job-creation estimate exists in the sources found.
- Eka Care and Bhashini evidence is announcements and press releases, with no deployment scale or accuracy data.
