# 07 - NASSCOM and national/institutional jobs reports: occupations most hit by AI (research notes)

Method: 18 WebSearch calls (standard mode, as the caller allowed). All WebFetch attempts failed with DNS errors (bls.gov, newyorkfed.org, weforum.org, jobsandskills.gov.au, statcan.gc.ca), so **every item below comes from search-result summaries, not from fetched primary pages**. URLs point to the primary page where the search surfaced one. Excluded by scope (covered by another agent): the IMF Jan 2024 note, the ILO 2025 index, the World Bank South Asia update, NITI Aayog Oct 2025, and Stanford "Canaries". Not found within budget: OECD Employment Outlook 2025 occupation ranking, Japan (METI/MHLW), Singapore MOM, a 2025-26 DTI/DOST statement, ONS/IPPR 2025-26.

## Key numbers

| Item | Figure | Period | Source URL | Confidence |
|---|---|---|---|---|
| BLS: customer service reps, projected change | -5.5% (about -153,700 jobs) | 2024-34 | https://www.bls.gov/opub/ted/2026/artificial-intelligence-information-technology-and-employment-2024-34.htm | M (search summary of primary) |
| BLS: claims adjusters, examiners, investigators | -5.1% (about -18,200) | 2024-34 | same | M |
| BLS: medical transcriptionists | -4.9% (about -2,200) | 2024-34 | same | M |
| BLS: software developers | +15.8% (about +267,700) | 2024-34 | same | M |
| BLS: all occupations | +3.1% | 2024-34 | https://fraser.stlouisfed.org/files/docs/publications/bls_mlr/bls_mlr_20260108.pdf | M |
| NY Fed: service firms using AI that hired fewer because of it | about 12% (concentrated in degree jobs); layoffs blamed on AI about 1% | Aug 2025 survey | https://libertystreeteconomics.newyorkfed.org/?p=36928 (press: https://fortune.com/2025/09/05/ai-job-market-layoffs-retraining-hiring-entry-level-college-graduates) | M |
| NY Fed: service-firm AI adoption | 25% (2024), 40% (2025), 61% (2026); layoffs still "uncommon" | Sep 2026 | https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/ | M |
| St Louis Fed: computer and mathematical occupations | about 80% exposure; unemployment +1.2 pp 2022-25 | 26 Aug 2025 | https://www.stlouisfed.org/on-the-economy/2025/aug/is-ai-contributing-unemployment-evidence-occupational-variation | M (correlation 0.47 or 0.57, depending on the source) |
| Bank of Korea: jobs lost by people aged 15-29 | -285,000, of which 268,000 (94%) in high-AI-exposure sectors | Jun 2022 to Jun 2026 | https://www.koreatimes.co.kr/southkorea/society/20260818/ai-exposed-sectors-see-sharp-drop-in-youth-employment-bok-report | M (press reports of a BOK report) |
| BOK: youth jobs by sector | info services -31.4%, publishing -27.4%, computer programming -16.6%, professional services -11.6% | same | https://mbiz.heraldcorp.com/article/10844024 | M |
| StatCan: workers in high-exposure, low-complementarity jobs | 31% (29% high exposure/high complementarity; 40% low exposure) | May 2021 data, publ. Sep 2024 | https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm | H |
| IBPAP: Philippine IT-BPM | about 1.9mn workers, about US$40bn, +80,000 jobs in 2025 | 2025 | https://www.philstar.com/business/2026/01/01/2498004/it-bpm-sector-track-hit-40-billion-revenue-goal | M |
| IBPAP: 2028 target cut | from 2.5mn workers/US$59bn to 1.85-2.14mn/US$43.3-50.5bn | revised 2026 | https://wealthinsights.metrobank.com.ph/news/ai-global-competition-force-philippines-it-bpm-industry-to-cut-targets | M |
| WEF FoJ 2025: global jobs | 170mn created, 92mn displaced, net +78mn | 2025-30 (employer survey) | https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/ | H |
| NASSCOM-Indeed: employers who say AI is changing roles | 86%; 14% of Indian job postings mention AI (up from 8.9%) | May 2026 (postings to Jan 2026) | https://race.reva.edu.in/wp-content/uploads/Retina_Issue_Issue_15_Week_10_-16_August_2026_RACE_REVA_University.pdf (secondary) | L-M |
| NASSCOM-Deloitte: AI talent demand | about 600-650k rising to >1.25mn by 2027 | 2024 report | https://indiaai.gov.in/article/india-s-ai-talent-pool-to-grow-to-1-25-million-by-2027-nasscom-deloitte-india-report | M |
| NASSCOM-BCG: AI job-function base | 420,000 people; AI-talent demand +15% CAGR to 2027 | Feb 2024 | https://www.theweek.in/news/biz-tech/2024/02/20/india-ai-market-to-touch-dollar17-billion-by-2027-nasscom-bcg-report.html | M |

## Sector notes

### A. NASSCOM
- **Method:** Employer surveys and job-posting analysis with partners: Deloitte (2024), BCG (Feb 2024) and Indeed (19 May 2026, "India's AI Talent Inflection Point: From Skill Gaps to Competitive Advantage").
- **Roles growing:** AI/ML engineers. NASSCOM-BCG says AI engineers grew 67% YoY within AI/ML postings (2024). An older NASSCOM AI and big-data report found 73% of AI jobs in five roles, including data engineers, ML engineers and data scientists. Demand estimates: Deloitte puts it above 1.25mn by 2027; a 2022 report gave 629k demand against 416k supply, a 51% gap.
- **Roles declining:** **No NASSCOM document naming declining roles (testing, L1 support, entry coding) was found.** Claims of a "20-25% cut in entry-level IT roles per NASSCOM FY26 data" appear only on secondary blogs and are unverified (see below). The 2026 NASSCOM-Indeed report frames the issue as reshaped roles and a skills mismatch (50% of employers name it the main hiring problem), not as job losses.
- **Related, not NASSCOM:** Cognizant-Pearson survey of 750 HR leaders (18 Jun 2026) found 37% of entry-level tasks in India already done by AI, against a 33% global average. https://news.cognizant.com/2026-06-18-37-of-Entry-Level-Tasks-in-India-Already-Done-by-AI,-Finds-Cognizant-and-Pearson-Study (vendor survey).
- **Not known:** NASSCOM's role-by-role taxonomy and the methodology of the 2026 report.

### B1. United States
- **BLS Employment Projections 2024-34 (released 28 Aug 2025; TED article 2026)**
  - Method: projections built with occupational AI-exposure scores (Felten et al.; Eloundou et al.) plus BLS staff judgement on productivity against substitution.
  - Declines named in the AI/IT table: customer service reps (-5.5%), claims adjusters/examiners (-5.1%) and medical transcriptionists (-4.9%).
  - Growth: software developers (+15.8%); data scientists and information security analysts also grow.
  - Paralegals: no 2024-34 figure found. A BLS presentation (Jun 2025, on the 2023-33 round) called paralegals/legal assistants the legal occupation with the "strongest AI employment impact": +1.2%, below average.
  - These are projections, not measurements. https://www.nationalacademies.org/cdn/materials/a1edef65-19af-4f2f-9120-7abf42518f0c
- **NY Fed regional business surveys (Aug 2025; Sep 2026)**
  - Measured self-reports: layoffs attributed to AI are rare (about 1% of service firms in 2025), and firms mostly retrain.
  - The real effect is reduced hiring: 12% of AI-using service firms hired fewer, mostly in degree-requiring jobs.
- **St Louis Fed (Ozkan & Sullivan, 26 Aug 2025)**
  - A measured correlation: occupations with higher AI exposure saw larger rises in unemployment, 2022-25.
  - Computer/math occupations: about 80% exposure, 45% adoption, +1.2 pp unemployment. The authors call it correlation, not cause.

### B2. United Kingdom
- **DfE Unit for Future Skills, "The impact of AI on UK jobs and training" (Nov 2023)**
  - Method: AI Occupational Exposure (Felten-type) mapped onto UK SOC codes.
  - Most exposed to all AI: management consultants and business analysts, then financial managers/directors and chartered accountants.
  - Most exposed to LLMs: telephone salespersons, then solicitors and psychologists.
  - Most exposed sector: finance and insurance.
  - The report itself warns that "exposure" does not mean replacement. https://www.edge.co.uk/research/skills-shortages/skills-shortages-publication-library/the-impact-of-ai-on-uk-jobs-and-training-report/ and https://lawgazette.co.uk/practice/solicitors-on-governments-list-of-ai-impacted-jobs/5118062.article
- **Possible 2026 update:** FE Week (30 May 2026) cites newer DfE/UFS work with the same top three. It is unclear whether this is a new edition (single source).
- **2026 measured signals:**
  - These come from private and academic sources, not ONS.
  - Indeed (Aug 2026): vacancies about -10% since Jan 2025; software postings +14%; accounting and marketing down by double digits. https://fortune.com/2026/08/02/ai-two-speed-job-market-uk-software-manufacturing-experience-entry-level/
  - Lancaster Work Foundation: 36% of firms cut entry-level roles, partly because of AI. https://allwork.space/2026/08/one-in-three-u-k-employers-cut-entry-level-jobs-as-ai-expands-survey-finds/
  - Graduate vacancies -45.6% YoY (Jul 2026, one platform). Rises in National Insurance and the minimum wage are confounders.

### B3. Philippines (India's main offshore competitor)
- **IBPAP (Jan and Jul 2026)**
  - About 1.9mn workers and about US$40bn in 2025; still growing (+80k jobs).
  - 2026 outlook: US$42bn and about 1.96-1.97mn jobs. https://www.sunstar.com.ph/cebu/it-bpm-eyes-42b-exports-near-2-million-jobs-in-2026
  - The 2028 roadmap was cut from 2.5mn workers to 1.85-2.14mn, explicitly citing AI and competing hubs.
  - IBPAP says AI will weaken the link between revenue growth and job growth for entry-level functions. It is moving its success metric from headcount to value per worker. https://news.outsourceaccelerator.com/philippine-it-bpm-roadmap-rewrite/ ; https://tribune.net.ph/2026/07/14/it-bpm-eyes-50b-in-revenues-with-ai-enabled-workforce
- **Government statements:** The only DTI/DOST statements found are from 2017: DTI said AI could reduce 45-50% of about 1.2mn BPO jobs, and DOST warned about 700k workers. Neither came true; the headcount grew to 1.9mn. No 2025-26 official statement was found.

### B4. Other countries
- **Australia, JSA "Our Gen AI Transition" (2025)**
  - Method: task-level exposure modelling plus labour-market data.
  - Finding: Gen AI is more likely to augment than automate.
  - Most exposed to automation: clerical and administrative roles, entry-level workers, and female-dominated occupations.
  - JSA found **no sign yet** of entry-level effects in the data. https://www.jobsandskills.gov.au/publications/generative-ai-capacity-study-report ; https://ia.acs.org.au/article/2025/aussie-jobs-most-vulnerable-to-ai-outlined-in-govt-study.html
  - The ACS claim that office clerks, receptionists and bookkeepers lose most by 2050 was not verified in the JSA text.
- **Canada, StatCan (Sep 2024; Daily 30 Jul 2026)**
  - 31% of workers are in high-exposure, low-complementarity jobs.
  - The 2026 Daily reports 53.8% Gen AI use at work in high-exposure, high-complementarity occupations, against 14.2% in low-exposure ones. https://www150.statcan.gc.ca/n1/daily-quotidien/260730/dq260730b-eng.htm
  - Named occupations were not retrieved.
- **Germany, IAB**
  - Kurzbericht 5/2024 (substitution potential recomputed for Gen AI): the potential is highest in helper and skilled-worker jobs and in manufacturing. The **fastest rise** is in expert, IT and science-related services.
  - IAB-Regional 2/2026 (Thuringia) confirms the shift toward non-routine expert tasks. https://doku.iab.de/regional/SAT/2026/regional_sat_0226.pdf
  - No 2025 national IAB update was found.
- **South Korea, BOK (Oct 2025 issue note; 18 Aug 2026 report)**
  - The strongest measured evidence in this file: youth job losses concentrated in high-AI-exposure sectors (IT services, publishing, programming, professional services).
  - Meanwhile, jobs for people in their 50s rose by 230k, 75% of it in the same sectors. This pattern fits the "juniors lose, seniors keep" story.
  - BOK says demographics explain part of the decline. https://www.koreajoongangdaily.com/korea/aiexposed-sectors-see-sharp-decline-in-youth-employment-bok-report/12829686
- **Singapore:** No MOM report found. The ILO ASEAN study (Jul 2026) puts 42.2% of Singapore employment in Gen-AI-exposed occupations, the highest in ASEAN. Top exposed: financial analysts, multimedia developers, financial brokers. It found no large-scale job losses. https://www.thestar.com.my/aseanplus/aseanplus-news/2026/07/10/ai-could-affect-millions-in-south-east-asia-as-ilo-sees-no-big-job-cuts
- **Japan / OECD EO 2025:** No credible occupation ranking found within the search budget.
- **WEF Future of Jobs 2025 (Jan 2025; survey of 1,000+ employers covering 14mn workers in 55 economies)**
  - Fastest declining: postal clerks, bank tellers, **data entry clerks**, cashiers/ticket clerks, **administrative assistants and executive secretaries**, plus other clerical roles.
  - Fastest growing: big data specialists, fintech engineers, AI/ML specialists, software developers, security management specialists.
  - India: secondary outlets say Indian employers are more bullish than the global average (35% against 20% expect semiconductors/computing to transform operations); skills-based hiring. The "96% of Indian firms implementing AI" figure is unverified.

## Mapping to India's offshored work

| India export line | Matching "most exposed/declining" occupation (report) | Evidence type | Read-across |
|---|---|---|---|
| Contact centres / CX | Customer service reps -5.5% (BLS); telephone salespersons top LLM exposure (DfE) | Projection / exposure | Strongest official signal. The Philippines, the closest comparator, still added jobs in 2025 but cut its 2028 target. |
| Data entry, back-office admin | Data entry clerks, admin assistants among fastest declining (WEF); clerical most exposed (JSA) | Employer survey / exposure | Directly matches low-end BPM. No measured India figure found. |
| Insurance claims processing | Claims adjusters/examiners -5.1% (BLS); finance and insurance the most exposed sector (DfE) | Projection / exposure | Matches insurance BPM and GCC work. |
| Medical transcription | Medical transcriptionists -4.9% (BLS) | Projection | Already in archive; consistent. |
| Paralegal / document review (LPO) | Paralegals: strongest AI impact among legal jobs (BLS 2023-33 round); solicitors #2 in LLM exposure (DfE) | Projection / exposure | Moderate signal; no 2024-34 figure found. |
| Bookkeeping / F&A | Chartered accountants, financial managers in DfE top 3; UK accounting postings down by double digits (Indeed 2026) | Exposure / postings | F&A BPM is highly exposed under every UK measure. |
| Junior coding / testing | Computer/math unemployment +1.2 pp (St Louis Fed); Korean youth programming jobs -16.6% (BOK); IAB fastest rise in IT; yet BLS software devs +15.8% | **Measured** (Fed, BOK) and projection | The only line with measured effects: losses at junior level, while senior and overall demand still grow. |

## Best chart data
1. BLS 2024-34 projected change: customer service reps -5.5%, claims adjusters -5.1%, medical transcriptionists -4.9%, software developers +15.8%, all jobs +3.1% (BLS TED 2026; MLR Jan 2026).
2. BOK youth job change by sector, Jun 2022 to Jun 2026: info services -31.4%, publishing -27.4%, programming -16.6%, professional services -11.6% (Herald/Korea Times, 18 Aug 2026).
3. Philippine IT-BPM 2028 headcount target: 2.5mn (2022 roadmap) against 1.85-2.14mn (2026 revision); 2025 actual 1.9mn (IBPAP via Philstar/Metrobank).
4. NY Fed service-firm AI adoption 25% to 40% to 61% (2024-26), while AI layoffs stay about 1%.
5. StatCan exposure split: 31% high-exposure/low-complementarity, 29% high/high, 40% low.

## Claims seen but not usable
- **"NASSCOM FY26 data shows a 20-25% cut in entry-level IT roles":** appears only on secondary blogs (startupfeed.in, a university newsletter); no NASSCOM source was found.
- **"WEF: 96% of Indian companies implementing AI" and "India Skills Fit score 59.1":** cited by Indian exam-prep sites, not verified in WEF text.
- **"Paralegals -4% to 2034 (BLS)":** from a consumer site, not traceable to BLS.
- **DTI 2017 "45-50% of BPO jobs lost to AI" and the Banatao "most of 1.3mn displaced in two years":** old or undated forecasts that did not happen (headcount 1.9mn in 2025).
- **ACS "office clerks, receptionists, bookkeepers lose most by 2050" attributed to JSA:** not confirmed in the JSA report.
- **St Louis Fed correlation "0.57":** the Fed's own text gives 0.47 per search summary; use neither without checking.
- **AgentLocker / ChatGPT-generated "jobs AI will replace" lists:** not authoritative.
