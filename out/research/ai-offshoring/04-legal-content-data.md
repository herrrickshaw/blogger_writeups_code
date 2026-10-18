# 04 - Legal process outsourcing, content moderation, translation/publishing services, data annotation (research notes)

Method: 14 WebSearch calls (standard mode). Every WebFetch attempt failed with DNS errors (theprint.in, imerit.ai, imerit.net, heise.de, cxodigitalpulse.com, cmr.berkeley.edu, emarketer.com), so **no page was fetched in full**. Everything below comes from search-result summaries only and should be checked against the original pages before publication. Dates are those given in the search snippets. "Primary" means a company statement, filing or official statistic. "Press" means a press report of a primary source. "Est." means a consultancy, vendor or job-board estimate.

## Key numbers

| Item | Figure | Period | Source URL | Confidence H/M/L |
|---|---|---|---|---|
| India data-annotation workforce (full- and part-time) | ~70,000 | Nasscom report, 2025 (press, via Straits Times/Mint reprinted on iMerit site) | https://imerit.ai/press/ai-data-jobs-attract-highly-skilled-indians/ | M (one Nasscom figure; LiveLaw 2026 attributes ~70,000 to 2021) |
| Nasscom projection of India annotation workers | ~1 million by 2030 | older forecast | https://gulfnews.com/amp/story/world%2Fasia%2Findia%2Fgoogle-microsoft-bet-on-27-year-old-stanford-alum-to-make-ai-work-in-india-1.1699015151586 | L (an analyst quoted by Straits Times says it "could be inflated") |
| India annotation market | US$250mn, 60% from US clients | 2023 | https://imerit.ai/press/ai-data-jobs-attract-highly-skilled-indians/ | M |
| India annotation market (alternative) | US$419mn, rising to US$603mn by 2032 | 2025 est. (6Wresearch, cited by ThePrint) | https://theprint.in/ground-reports/ai-is-creating-lakhs-of-low-paying-jobs-in-gurugram-noida-it-is-indias-new-bpo/3030288/ | L (est.) |
| iMerit employees | ~5,000, most in 12 India centres, mostly graduates | 2025 | https://imerit.ai/press/ai-data-jobs-attract-highly-skilled-indians/ | M (company, via press) |
| Karya workers / tasks / pay | 50,000 workers; 42mn paid tasks; claims US$5/hr (~20x minimum wage) | to 2025 | https://cmr.berkeley.edu/2025/10/karya/ | L-M (self-reported, no independent check) |
| Entry-level annotator pay (job listing) | Rs 20,000-30,000/month | 2025-26 | https://in.indeed.com/Data-Annotator-jobs-in-India | L (single listing) |
| Expert AI-training pay (global remote listings open to India) | legal US$70-90/hr; clinical up to US$65/hr | mid-2026 | https://www.opentrain.ai/jobs/country/india/?page=7 | L (advertised, not earned) |
| India LPO market value | US$2.7bn (IMARC) vs US$8.7bn (Mobility Foresights) | 2025 est. | https://www.imarcgroup.com/india-legal-process-outsourcing-market ; https://mobilityforesights.com/product/india-legal-process-outsourcing-market | L (vendor estimates disagree 3x) |
| India LPO headcount (latest found) | 4,900 professionals | Dec 2009 (Evalueserve) | https://www.legallyindia.com/20100506778/Legal-Process-Outsourcing-LPO/india-lpo-inc-headcounts-to-triple-as-15-of-work-usuk-associate-level | L (17 years old) |
| Meta: human moderation requests moved to LLMs | ~50% now; target >90% for some content types | FT-based reports; snippets date this to 2025 or 25 Jun 2026 (conflicting) | https://www.freevacy.com/news/financial-times/meta-accelerates-shift-to-ai-content-moderation/7497 | M (press of company plan; date unclear) |
| Meta claim for AI vs human moderators | 13% fewer errors, 10% more violations found | same report | https://the-decoder.com/meta-employees-warn-ai-moderation-rollout-is-too-fast/ | M (company claim, disputed by staff) |
| TikTok moderation cuts | ~500 Malaysia (late 2024); ~150 Berlin (Jul 2024); "hundreds" of ~2,500 UK (2025) | 2024-25 | https://www.techspot.com/news/109194-tiktok-lays-off-hundres-content-moderators-replaces-them.html | M (press) |
| TikTok: share of violating content removed by AI | >85% | 2025 company claim | https://getcoai.com/news/tiktok-cuts-hundreds-of-jobs-as-ai-integration-expands | M (company claim) |
| Duolingo contractor cut | ~10% of contractors | end 2023 / Jan 2024 | https://www.computing.co.uk/news/2025/ai/duolingo-goes-ai-first-as-it-phases-out-human-contractors | H (company-confirmed, widely reported) |
| Lumina Datamatics headcount | ~5,196 (Revelio) vs ">6,500 globally" after TNQTech deal (company) | 2025 | https://www.reveliolabs.com/companies/lumina-datamatics/employees ; https://www.globenewswire.com/de/news-release/2025/01/28/3016376/0/en/Lumina-Datamatics-Acquires-TNQTech-Pioneering-AI-Driven-Publishing-Solutions-and-Charting-a-New-Era-of-Excellence-in-2025.html | L-M |
| Integra Software Services headcount | ~3,234 (+4.6% y/y) | 2025 | https://www.reveliolabs.com/companies/integra-software-services/employees | L (data aggregator) |
| Moderator workload in India | ~1,500 items per 8-hour shift | study pub. Aug 2025 | https://news.uq.edu.au/2025-08-judgement-call-unseen-pressures-people-who-police-internet | M (academic) |

## Sector notes

### (a) Legal process outsourcing (document review, e-discovery, contract review, IP)
- **Size in India:** No credible current headcount found. The last measured figure found is 4,900 professionals (Evalueserve, Dec 2009). Market-value estimates for 2025 range from US$2.7bn (IMARC) to US$8.7bn (Mobility Foresights), which shows they are not reliable. One stats site's "India ~59% of global LPO delivery" is unsourced.
- **AI impact evidence:** The evidence is about how the work is done, not about job losses. Integreon called itself the "first generative AI-led ALSP" in December 2023, using ContractPodAi's Leah (press release, primary). QuisLex built Leah into its CLM, M&A and compliance work in April 2024 (primary). ContractPodAi renamed itself Leah in January 2026. Job postings show the work changing. DISCO's 2026 Gurugram "Review Associate" role does first-level review and QC inside the AI platform. Deccan AI's Mumbai freelance listing has lawyers grading AI-generated legal analysis. Client-side tools are priced per seat. CoCounsel is roughly US$100-640/user/month and bundled with Westlaw in 2026. Harvey is unpublished but reportedly US$50k-300k+ per year per firm (aggregator estimates, L). Those prices are what offshore per-hour review now competes against.
- **Offsetting job creation / counter-evidence:** No 2025-26 reports of layoffs were found at UnitedLex, Integreon, QuisLex, Mindcrest or Clutch Group. Lawyers are finding new work grading legal AI output for AI labs (see d). At Clarivate, which owns the former CPA Global IP-services business (large Noida operations), the 2025 messaging focused on AI and subscriptions. It explored strategic alternatives and divestitures (Feb 2025) and its IP segment is under "structural pressure". No India-specific headcount data was found.
- **What is not known:** LPO headcount in India, any change in first-level review volumes, and how much offshore review has moved into AI tools.

### (b) Content moderation
- **Size in India:** No credible current figure found. The only firm numbers are old. In 2019 Reuters reported a 1,600-person Genpact team in Hyderabad reviewing Facebook content, with entry pay of about Rs 1 lakh/year. Accenture Hyderabad staff reviewed Arabic YouTube content for Google at Rs 3.5 lakh/year or more. A 2025 academic study (New Media & Society, via UQ) gives Indian moderators about 1,500 items per shift.
- **AI impact evidence:** Meta has moved about half of human review requests to LLMs and aims for over 90% for some content types (FT, via press). The snippets disagree on whether this was reported in 2025 or June 2026. Meta says the change is about quality, not cost. Its claims are 13% fewer errors and 10% more violations found. Reports say vendors whose contracts are not renewed will bear the impact. A separate item from 1 June 2025 says Meta aims to have AI do up to 90% of its product risk and privacy assessments. That is not moderation, and the two are easy to confuse. In January 2025 Meta also moved towards community-based moderation, which an aggregator calls "cutting professional moderators en masse" (press, M-L). TikTok cut about 500 moderators in Malaysia (late 2024), about 150 in Berlin (July 2024) and hundreds in the UK (2025). It says AI removes over 85% of violating content. The WSJ reported that South and Southeast Asia staff would also be affected. TikTok is banned in India, so its moderation vendors there are a minor factor.
- **Offsetting job creation / counter-evidence:** Moderation and annotation are merging. LiveLaw (2026) calls moderators and annotators the "human backbone" of the AI supply chain, and much of the remaining work is labelling harmful content for model training (see d). Meta says human oversight continues through sample testing.
- **What is not known:** How many moderation jobs the Meta/Google vendors (Genpact, Accenture, TaskUs, Teleperformance and others) have in India today, and whether India lost any of them in 2025-26. No India-specific cut was found.

### (c) Translation/localisation and publishing services
- **Size in India:** No sector-wide figure found. Firm-level figures: Lumina Datamatics has about 5,200 employees (Revelio) or more than 6,500 globally after buying TNQTech (company, Jan 2025). Integra has about 3,234 (+4.6% y/y, Revelio 2025). The searches returned no Straive or Newgen headcount.
- **AI impact evidence:** So far the clearest sign is a change in strategy, not job cuts. Lumina Datamatics bought a controlling stake in TNQTech, a Chennai firm, in January 2025 for "AI-driven publishing". Straive, formerly SPi and owned by EQT, bought SG Analytics in June 2025 and now presents itself as a data, analytics and AI operations firm, not a content/pre-press firm. The demand-side signal is Duolingo. It cut about 10% of its contractors (end 2023 / January 2024). CEO Luis von Ahn's April 2025 "AI-first" memo said contractors would be phased out for work AI can do, including translation and content creation, and that new hires need proof the work cannot be automated. After the backlash he softened his tone but did not reverse the policy.
- **Offsetting job creation / counter-evidence:** Revelio shows modest headcount growth at Lumina and Integra in 2025. That suggests no collapse so far, but the data comes from an aggregator.
- **What is not known:** Any survey of Indian translators or pre-press workers, page-volume prices, and the India headcount of Straive and Newgen.

### (d) Data annotation and labelling: AI as a source of offshore jobs
- **Size in India:** About 70,000 full- and part-time workers (Nasscom 2025, via press). This is the best figure available, but LiveLaw (2026) gives about 70,000 for 2021, so the number may be stale. Nasscom's forecast of about 1 million by 2030 is widely seen as inflated. The market was about US$250mn in 2023 (60% from US clients), with an estimate of US$419mn in 2025.
- **Job creation evidence:** iMerit has about 5,000 staff, mostly in 12 Indian centres. Karya says it has 50,000 workers in all 28 states, 42mn paid tasks and US$5/hr (self-reported). ThePrint (2025-26) describes "lakhs" of low-paid annotation jobs in Gurugram and Noida as "India's new BPO", with long hours, strict targets and low pay. The "lakhs" figure is ThePrint's characterisation and is not sourced. A typical listing pays Rs 20-30k/month.
- **Shift to expert work:** Mint (via iMerit) describes firms such as iMerit, NextWealth and Indika AI moving "from volume-based labelling to expert-led AI training" and hiring doctors, lawyers, engineers and PhDs. Remote listings advertise legal work at US$70-90/hr and clinical work up to US$65/hr (mid-2026). A careers source (Dheya, 2026) claims basic annotation has "compressed by more than half" as models do the simpler labelling, while basic pay has stagnated. That claim comes from a single, non-primary source.
- **What is not known:** India headcount at Scale/Remotasks/Outlier, Sama, Turing or Deccan AI. Whether volume work grew or shrank in 2025-26. Any primary wage survey.

## Best chart data
1. India annotation market: US$250mn (2023) to US$419mn (2025 est.) to US$603mn (2032 proj.). Sources: Straits Times via iMerit; 6Wresearch via ThePrint (L-M).
2. India annotation workforce: ~70,000 (Nasscom 2025) vs ~1mn projection for 2030. Use with an "inflated?" caveat.
3. Pay ladder: entry annotator Rs 20-30k/month (about US$240-360) vs expert legal RLHF US$70-90/hr (listings).
4. Meta human moderation requests handled by LLMs: ~50% now to >90% target (FT via press).
5. TikTok moderator cuts: Berlin ~150 (Jul 2024), Malaysia ~500 (late 2024), UK "hundreds" of ~2,500 (2025).
6. Duolingo contractor cut: ~10% (Jan 2024), then the AI-first memo (Apr 2025).

## Claims seen but not usable
- **"India ~59% of global LPO delivery"** (stealthagents.com): no methodology or source.
- **India LPO market US$8.7bn (2025), US$23.4bn by 2031**: a vendor forecast that is 3x IMARC's US$2.7bn. Neither is usable as a headline figure.
- **"Lakhs" of annotation jobs** (ThePrint headline): a descriptive word, not a count.
- **"Basic annotation compressed by more than half"** (Dheya careers blog): based on the firm's own mentors' estimates.
- **Karya "US$5/hr, 20x minimum wage"**: self-reported, not independently checked.
- **Harvey per-seat prices** (US$1,000-2,000/month mid-market): pricing-aggregator estimates; Harvey does not publish prices.
- **Meta "replace 90% of moderation with AI"** headlines: these mix up the June 2025 risk-assessment story with the later FT moderation story, and the dates conflict. Cite carefully.
- **Genpact 1,600 / Accenture Hyderabad moderation figures**: real (Reuters 2019) but 6-7 years old. Do not present them as current.
