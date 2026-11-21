# Source Register — VertiStrat

Running log of papers, datasets and official releases assessed as **commissioning
material for the blog**. One entry per source. Extended by track B of the
`literature-review-daily` scheduled task.

This is deliberately *not* the market-pipeline literature register. That one grades
papers on whether a technique is worth implementing in a screener. This one grades
sources on whether they can carry an article: primary data the blog can pull itself,
a finding worth reporting, and a subject the blog has not already covered.

**Grading convention**

- **COMMISSIONABLE** — names a primary dataset the blog can obtain (government portal,
  journal appendix, official return), and carries at least one quantified finding that
  is either counterintuitive or not already common knowledge in Indian coverage.
- **BACKGROUND** — sound and relevant, but no independently obtainable data. Useful for
  context or a citation inside a piece built on something else. Not a piece on its own.
- **WEAK** — modelled or vendor-sourced numbers with undisclosed method, a scope too
  narrow to generalise, or a finding the blog already published. One line, no write-up.

Vendor market-sizing reports are **WEAK by default**. A standing correction applies:
one such report overstated an India figure by 6.5×. If a vendor number is the only
source for a claim, the claim does not go in an article.

**Dedup rule** — before logging a candidate, check it against:
1. this file,
2. `docs/LITERATURE_SURVEY.md` (the 2026-08-22 corpus survey and its commissioning list),
3. `meta/manifest.json` (every published post title).

---

## Commissionable

### PPV&FR Authority registration data (Protection of Plant Varieties and Farmers' Rights Authority, MoA&FW)
India's plant-variety-rights registry. The homepage carries a live certificate counter
with a crop-category breakdown, **verified by direct fetch on 2026-08-27**: **10,802
certificates issued as of 31.07.2026** — Cereals 6,246, Vegetables 1,367, Fibre Crops 989,
Legumes 866, Oilseeds 577, Fruits 425, Spices 151, Sugar Crops 93, Trees/Forest 43,
Flowers 36, Cash crops 5, Medicinal & Aromatic plants 4.
- **Data**: Annual Report 2024-25 — free PDF, **no login, no payment**, 22.77 MB, at
  `plantauthority.gov.in/sites/default/files/annual-report-2024-25-english.pdf` (link
  verified on the report's landing page). Also free and public: the *Plant Variety
  Journal* (monthly, latest Vol. 20 No. 07, July 2026), the *Compendium of Varieties
  Registered under PPV&FR Act, 2001*, Gazette Notifications, and Public Notices
  2007-2025. Login is required only for PARV, the online **application** system — not
  for any of the published data. Gazette Notification G.S.R. 483(E) of 4 July 2025
  (PPVFR Amendment Regulations 2025) is the most recent rule change.
- **Finding**: the distribution is extraordinarily lopsided. Cereals alone hold **6,246
  of 10,802 certificates — 57.8% of every plant-variety right India has ever granted**.
  Against that, spices have 151 and medicinal & aromatic plants have 4. The blog has
  already published that spices are a **$4.45 billion export book across eight crops in
  eight states** (`indias-445-billion-spice-export-book-is`); that entire export book
  rests on 151 registered varieties. The juxtaposition is the piece, and both halves are
  primary-sourced — one from this registry, one from the blog's own prior work.
- **Blog fit**: opens the **confirmed zero-coverage seeds / plant-variety-rights /
  agricultural-IP area**. Dedup was run against `meta/manifest.json` (217 posts,
  snapshot 2026-08-27T04:20): a regex for seed/variety/germplasm/breed/PPVFR/patent/
  ICAR/hybrid/cotton/plant returned **2 hits, both false positives** —
  `the-cbg-incentive-stack-every-leg-of` and `india-will-finance-waste-to-energy`, where
  "plant" means an industrial facility. Coverage of this subject is genuinely zero.
  It extends the existing crop-economics beat, whose nearest published neighbours are
  `379-kilos-hectare-in-punjab-44-in` (input use mapped by crop and state) and
  `indias-445-billion-spice-export-book-is`.
- **Caveat**: four things need checking before publication. (1) The homepage counter is
  a **live figure with no vintage archive** — it must be screenshotted or cross-read
  against the Annual Report PDF, and dated in the piece, or it becomes unverifiable
  later. (2) A widely-repeated split — 19,888 applications filed, 9,210 certificates, of
  which **4,847 (52.6%) registered by farmers** rather than companies — appeared only in
  a search-result snippet and **was NOT verified against any page fetched today**. It is
  the more striking claim of the two and must be confirmed from the Annual Report PDF
  before it is used at all. (3) "Certificates issued" is not "varieties commercially
  sold" — registration is a legal act, not a market outcome, and the piece must not
  elide them. (4) The crop-category counts sum to 10,802 exactly, so the breakdown is
  complete, but the categories are the Authority's own and their boundaries are
  undefined on the homepage.
- **Grade: COMMISSIONABLE.**


### Defence Positive Indigenisation Lists (DDP, Ministry of Defence)
Four PILs notified for DPSUs covering Line Replacement Units, sub-systems, spares and
components: 1st 2,851 items, 2nd 107, 3rd 780, 4th 928 — **4,666 items** total (arithmetic
checked against the release, sums exactly). A 6th PIL of 405 items was notified around
18 August 2026 per PIB listings; not yet verified against its own release.
- **Data**: DPSU-wise item lists are published as PDFs on the Srijan portal
  (`srijandefence.gov.in`). Verified downloadable — the 12 May 2023 notification returns
  HTTP 200, 1.9 MB, `application/pdf`. No login, no payment.
- **Finding**: 2,736 of the 4,666 items are recorded as indigenised (58.6%), but the
  claimed import-substitution value totals only **₹2,570 crore** (₹1,756 cr + ₹814 cr) —
  roughly $295 mn, averaging **₹94 lakh per item**. A very large item count against a very
  small rupee value.
- **Blog fit**: defence indigenisation is effectively zero-coverage. The only defence post
  is `jai-kisan-jai-javan-fci-based-military` (military rations, FCI-based), and "Positive Indigenisation List"
  appears in the corpus only inside `quarterly-reportage-4034-scheme` as a logged scheme
  announcement, never analysed. The method is the one the blog already uses on chemicals in
  `top-15-chemicals-for-import` and `chemical-import-substitution-hsn-8-registry` — a code-by-code
  substitution list checked against trade data.
- **Caveat**: "import substitution value" is the ministry's own definition and is not
  reconciled here against actual defence import lines. The count-versus-value gap is the
  story, but the denominator (total defence imports over the same period) must be sourced
  before any share is stated. The 6th PIL needs its own release verified.
- Grade: **COMMISSIONABLE**. Logged 2026-08-22 (Saturday rotation).

### The 1,272-product, $189 billion import-substitution list (centre-state / DPIIT)
A centre-state exercise reported to have identified 1,272 products worth nearly $189 bn of
annual imports, each above a $50 mn annual import threshold and either not made in India or
made in inadequate quantity; sectors named are chemicals, electronics, machinery and
speciality steel.
- **Data**: the list itself is **not published**. Traced through Business Standard (16 July
  2026, HTTP 403 to automated fetch) and Policy Circle; no PIB release found for it — a PIB
  search returned only defence PILs and the DPIIT year-end review. The obtainable data is
  the *substitute* for it: DGCI&S TradeStat, which the blog already uses, can be filtered to
  every HSN line above $50 mn independently.
- **Finding**: the reproducible question is whether a public-data reconstruction of the
  ">$50 mn, inadequately made in India" filter lands anywhere near 1,272 products and
  $189 bn. Policy Circle also reports mobile-phone assembly at 18–20% domestic value
  addition, which is the standing critique of counting import substitution by output value.
- **Blog fit**: extends `chemical-import-substitution-hsn-8-registry` and
  `chemical-import-substitution-full-hsn-8_01082878313` from chemicals to all sectors,
  and `half-of-indias-import-bill-is`. The blog has 40 trade-adjacent posts, so
  this only earns a piece as a *check on an official claim*, not as a report of it.
- **Caveat**: no primary document located. Do not state 1,272 or $189 bn as established —
  attribute to press reporting, or derive the blog's own figure and compare.
- Grade: **COMMISSIONABLE** (as a reconstruction, not a write-up of the list).

### PLFS Quarterly Bulletin, January–March 2026 and April–June 2026 (NSO, MoSPI)
Official quarterly labour-force releases — Jan-Mar 2026 published 11 May 2026 (fourth in
the series), Apr-Jun 2026 published 10 August 2026 (fifth). The survey was revamped from
Jan 2025 to cover rural areas quarterly, not just urban. Both fetched and read directly
(not via secondary reporting).
- **Data**: `mospi.gov.in/uploads/PressRelease/Press_note%20_Jan_March_2026%20PLFS_QB.pdf`
  and `mospi.gov.in/uploads/latestReleases/latest_release_1786356517178_3a125c52-4680-4258-9dc5-aebea9b8f3f0_Press_note_Apr-Jun_2026_PLFS_QB.pdf`
  — both free PDFs, no login. Apr-Jun 2026 sample: 5,59,673 persons surveyed nationally
  (3,18,792 rural). A new quarterly bulletin is released roughly 5-6 weeks after each
  quarter ends, so this is a recurring, obtainable series, not a one-off.
- **Finding**: rural agriculture's share of employment fell for two straight quarters —
  58.5% (Oct–Dec 2025) → 55.8% (Jan–Mar 2026) → **52.9%** (Apr–Jun 2026, confirmed against
  the primary bulletin, p.8) — a 5.6-point drop in six months, while the rural secondary
  sector rose 20.9%→22.6%→24.4% and tertiary 20.6%→21.7%→22.7% over the same two
  quarters. Rural regular wage/salaried employment rose for a third straight quarter
  (14.8%→15.5%→16.1%) as self-employment fell (63.2%→62.5%→61.4%, p.7). The shift is
  sharper for rural women: agriculture's share of rural female employment fell
  75.5%→73.5%→70.7% across the same three quarters (p.8 chart). Readers who think of
  "rural India moving off farms" as a decades-long trend would not expect a two-quarter
  move this size.
- **Blog fit**: zero coverage — `PLFS`, `labour force`, `non-farm` return no manifest
  hits. Extends `A 17% Rural Pay Rise That Nobody Received` (farm wages, published
  2026-08-22): that piece covered what farm labour earns, this covers how many rural
  workers are still doing farm labour at all, and the two would read as a pair.
- **Caveat**: the rural quarterly series only has 5 data points (Apr–Jun 2025 through
  Apr–Jun 2026, methodology revamped Jan 2025) — real, but too short to call an
  established multi-year "trend" without hedging as early data from a young series.
- Grade: **COMMISSIONABLE**. Logged 2026-08-24 (Monday rotation); Apr-Jun 2026 figure
  verified against the primary bulletin same day, superseding the press-sourced estimate.

---

### Minor Irrigation Census, 6th round (Ministry of Jal Shakti, DoWR-RD&GR) + AERR irrigation-recovery paper
Paired source: one census that counts who actually owns India's irrigation, one
peer-reviewed paper that measures what the public money bought. Neither is on the blog.
- **Data**: **free, no login, no payment — all verified by direct download 2026-08-28.**
  The census document portal `mowr.nic.in/irrigationcensus/` returns HTTP 200 and links
  direct PDFs under `Documents/MI-Census/Reports/`: `6-MI-Report-All-India-Vol-I.pdf`
  and `6-MI-Report-State-Wise-Vol-II.pdf` both fetch as real PDFs (ranged GET returned
  HTTP 206, `application/pdf`, valid PDF 1.6). Every earlier round is there too —
  `Files/5th-MICensusReport.pdf`, `4thmicensusreport.pdf`, `Third-MI-report.pdf`, the
  2nd in six parts — so a **six-census series from reference year 1986-87 to 2017-18**
  is obtainable, which is what makes a trend argument possible rather than a snapshot.
  The primary release is PIB PRID **1952480**, Ministry of Jal Shakti, **26 Aug 2023**,
  fetched in full 2026-08-28 (needs a browser user-agent; plain fetchers get 403 —
  consistent with this register's standing PIB note).
  The AERR paper is **Seema Bathla, Elumalai Kannan & Gautam Kumar Das, "Public
  investment in irrigation across the Indian states: Financial recovery and governance",
  *Agricultural Economics Research Review* 37(1), pp. 93-112, 2024**
  (`epubs.icar.org.in/index.php/AERR/article/view/154839`). ⚠️ Abstract is public but
  **the full-text PDF is NOT freely downloadable** — the article page exposes only
  BibTeX/RIS citation exports, no PDF galley link, and the issue page redirects to a
  login screen. Treat it as a **concept citation**, not a data source.
- **Finding**: the census numbers, verbatim from the release. India has **23.14 million
  minor irrigation schemes; 21.93 million (94.8%) are groundwater** and only 1.21 million
  (5.2%) surface water. **96.6% of all MI schemes are under private ownership** — 98.3%
  of groundwater schemes, 64.2% of surface water. Of schemes with a single source of
  finance (60.2% of the total), **79.5% are financed by the individual farmer's own
  savings**. 97.0% are 'in use'. 18.1% of individually-owned schemes are owned by women
  (collected for the first time in this round). Growth over the 5th census: +1.42 million
  schemes, groundwater +6.9%, surface water +1.2%.
  Set against that, AERR's abstract reports that across **20 states, 1981-82 to 2019-20**,
  "increasing public capital formation in irrigation has **barely corresponded** with the
  outcomes in terms of net irrigated area, potential utilised, and rate of financial
  recovery" — while agriculturally advanced states spend *more*, not less. The census
  explains why the two can both be true: the state is capitalising the 5% of schemes it
  owns, and the country irrigates itself off the other 95%, out of pocket.
- **Blog fit**: opens the **confirmed zero-coverage "irrigation investment and
  governance" area** (LITERATURE_SURVEY §3), and puts a second post in the "water"
  band, which the survey scored at 2 hits in 192 titles. Dedup run against
  `meta/manifest.json` (**219 posts, snapshot 2026-08-28T07:27**): a regex for
  water/irrigat/soil/groundwater/aquifer/canal/drip/watershed/borewell/tubewell/
  reservoir/rain returned **8 title hits, none about irrigation**. Nearest published post
  is `tamil-nadus-water-infrastructure-runs` (25 Aug 2026) — checked by reading the post
  body, not by title: it is **urban municipal** water finance (KfW SMIF-TN tranches, tank
  desilting) and contains **zero** occurrences of irrigation, groundwater, tubewell or
  dugwell. It is a strong cross-link rather than an overlap, because it makes the same
  shape of argument — the headline water number not matching the money underneath.
  Others in the 8: `the-water-bill-nobody-mentions-what` (Taiwan fabs),
  `price-is-wire-how-gcam-actually-links` (GCAM modelling),
  `guar-gum-indias-35-billion-export-peak` ("poor soil" in the title only).
- **Caveat**: 🔴 **vintage — a 7th census exists and is partly published.** The 6th
  census reference year is **2017-18** (released Aug 2023), so the headline figures are
  eight years stale on the ground. `7-MI-Report-State-Wise-Vol-II-Part-1.pdf` fetches
  (HTTP 206, valid PDF) but `7-MI-Report-All-India-Vol-I.pdf` returns **404**, and the
  7th MI Census is running jointly with the 2nd Census of Water Bodies, 1st Census of
  Major & Medium Irrigation Projects and 1st Census of Springs at
  `wrcensus.mowr.gov.in` — i.e. still in progress. Any piece must date the 6th-census
  figures explicitly and check the 7th before publication; the all-India 7th totals
  were **not** obtainable today and must not be guessed at.
  Second caveat: the **village-level microdata is not confirmed obtainable**. The
  data.gov.in catalog page is JS-rendered with no resource hrefs in the HTML, and the
  catalog-level API id (`35a18274-b04c-4db6-b732-b23ff68a359b`) returned
  `{"message":"Meta not found"}` against the public sample key — per-resource ids are
  needed and were not found today. Do not promise village or district granularity.
  Third: "schemes" are not "farmers" and not "hectares" — one owner can hold several,
  and the census counts structures, not irrigated area. State that rather than sliding
  between units.

## Background only

### DPIIT Year End Review — PLI aggregate outcomes (PIB, Ministry of Commerce & Industry)
Official aggregates: ₹1.46 lakh crore investment, ₹12.5 lakh crore production, ₹4 lakh crore
exports, 9.5 lakh jobs, 1,300+ manufacturing units across 14 sectors and 27 states/UTs.
- **Data**: PIB release, fetched and readable (PRID 2086347, HTTP 200).
- **Blog fit**: the blog already has five PLI posts including
  `pli-medical-devices-coverage-and-gaps` and two priority-sector PLI-coverage pieces. These are headline
  aggregates without sector splits, so they are citation material inside a future piece
  rather than a piece themselves.
- Grade: **BACKGROUND**. Logged 2026-08-22.

### PMFBY premium-sharing structure and cumulative claims (PIB Explainer 155010, Ministry of Agriculture & Farmers Welfare)
"Empowering Annadatas: Pradhan Mantri Fasal Bima Yojana", PIB Explainer ID 155010,
posted **11 August 2025** (a year old — see Caveat). Fetched directly 2026-08-25 (the
`PressNoteDetails.aspx` URL 403s to plain fetchers; it returns HTTP 200 with a normal
browser user-agent).
- **Data**: the release itself carries the hard numbers, free and no login — **78.41 crore
  applications insured** and **₹1.83 lakh crore claims paid** since the 2016 launch;
  enrolment **3.17 crore (2022–23) → 4.19 crore (2024–25)**, +32%; non-loanee applications
  **20 lakh (2014–15) → 522 lakh (2024–25)**. It also states the full premium-sharing
  *rule*: the farmer pays a capped **2% (kharif food/oilseed), 1.5% (rabi food/oilseed),
  5% (annual commercial/horticultural)** of actuarial premium, and **"the remaining part
  (95% to 98.5%)... is borne jointly by the Central and State Governments on 50:50 basis"**,
  except North-Eastern (from Kharif 2020) and Himalayan states (from Kharif 2023) at 90:10.
  The release links a compendium PDF on `pmfby.gov.in/compendium/` for scheme rules.
- **Obtainability caveat (verified, not assumed)**: the state-wise/season-wise *gross
  premium* series is **not** confirmed pullable. `pmfby.gov.in` is a single-page app —
  `/adminStatistics/dashboard`, `/reportsummary` and `/statistics` all return the identical
  6,842-byte shell, `/api/v1/dashboard/statistics` 404s, and a `data.gov.in` catalog query
  for "fasal bima" failed to return. The argument below is buildable from the rule plus the
  cumulative totals *without* that series; anything state-level needs the portal cracked first.
- **Finding**: the release headlines ₹1.83 lakh crore paid *to* farmers but never states what
  farmers paid *in*. By the scheme's own capped rates, farmers fund only 1.5–5% of actuarial
  premium — so the overwhelming majority of every rupee disbursed is taxpayer-funded, split
  50:50 between Centre and states (90:10 in the hill states). The scheme is reported as
  insurance; structurally it is closer to a subsidy routed through insurers.
- **Blog fit**: opens the **crop-insurance** intersection of the blog's heaviest beat
  (agriculture) and its newest, near-empty one. Manifest grep confirms **zero** posts matching
  `pmfby|crop insur|fasal|reinsur|gic re` across all 210 posts, and only one insurance post at
  all — `premium-now-claim-later-float-indias` ("Premium Now, Claim Later: The Float India's
  Car Boom Is Building", 2026-08-22, labels incl. *Insurance & Reinsurance*), which is motor,
  not crop. The natural structural sibling is `who-collects-indias-gst-and-who` — same
  who-pays-vs-who-receives framing.
- **Caveat**: the release is **11 Aug 2025**, so "since inception" totals are ~15 months
  stale and must be re-based before publication. It is also an explainer with a promotional
  register (it opens with a single named farmer's testimonial) — use it for the *rule* and the
  *totals*, not for interpretation. The 90:10 hill-state split materially changes any national
  average and must not be flattened. Finally, "applications insured" is not "farmers insured" —
  one farmer files across seasons and plots, so 78.41 crore applications ≠ 78.41 crore people.


---

## Weak — logged, not actioned

- **data.gov.in "6th Minor Irrigation Census — Village Schedule, Ground Water / Surface
  Water Schemes"** — the obvious route to village-level microdata, but not obtainable as
  fetched 2026-08-28: the catalog page is JS-rendered with zero `/resource/` hrefs in the
  served HTML, and the catalog-level API id `35a18274-b04c-4db6-b732-b23ff68a359b`
  returned `{"message":"Meta not found"}` against the public sample key. Not a permanent
  dead end — per-resource ids would need harvesting from the rendered page first. Re-probe
  before promising any sub-state granularity. Logged 2026-08-28.
- **jalshakti-dowr.gov.in `/document/...` report pages** — the route PIB itself links for
  the 6th MI Census reports, but it is a Next.js SPA: HTTP 200, 7,256 bytes, and the only
  hrefs served are CSS/JS bundles and the favicon. Use `mowr.nic.in/irrigationcensus/`
  instead, which serves direct PDF paths. Logged 2026-08-28.
- **7th Minor Irrigation Census all-India totals** — not published yet.
  `7-MI-Report-State-Wise-Vol-II-Part-1.pdf` fetches, `7-MI-Report-All-India-Vol-I.pdf`
  returns 404, and the round is still running jointly with the 2nd Census of Water Bodies
  at `wrcensus.mowr.gov.in`. Do not cite a 7th-census national figure from any secondary
  source until the all-India volume appears. Logged 2026-08-28.

- India's simple average tariff rising 12% (FY2011) to 14.3% (FY2021) — sourced only to a
  commercial tariff-aggregator site, and the blog already runs heavy tariff coverage across
  40 trade-adjacent posts. Needs a WTO Tariff Profiles primary before it is usable. WEAK,
  logged 2026-08-22.
- PMFBY figures via **Indiastat** — real state/season-wise gross premium, paid claims and
  claim-ratio tables exist there, but it is a paid subscription aggregator, not a primary
  source. Use only to locate a series, never to cite one. WEAK, logged 2026-08-25.
- PMFBY claims summaries on **agrijob.in** ("₹1.92 lakh crore claims paid", state-wise premium
  lists) — SEO content farm restating PIB without attribution, and its total already disagrees
  with the primary release's ₹1.83 lakh crore. Do not cite. WEAK, logged 2026-08-25.
- **IBEF** PMFBY scheme page — IBEF is a Department of Commerce promotional body; useful only
  as a pointer to primaries it cites. BACKGROUND at best, not a source. Logged 2026-08-25.
- **pmfby.gov.in dashboard** — the obvious primary, but unusable as fetched today: SPA shell on
  every route, no working JSON endpoint found. Not a dead end permanently, just not obtainable
  without cracking the app's XHR calls. Re-probe before commissioning anything state-level.
  Logged 2026-08-25.

---

## Seeded from the 2026-08-22 corpus survey

The survey in `docs/LITERATURE_SURVEY.md` established the corpus profile and a 14-item
commissioning list. Its Tier-1 items are the standing backlog and do **not** need
re-deriving each day:

1. Farm labour wages against food inflation — **published 2026-08-22**, so this one is
   closed; the AERR wages paper is now cited in a live piece.
2. Ethanol feedstock balance against the E20 target (AERR).
3. Nano-urea against the trial literature (IJAgS).
4. Mandi market integration and e-NAM (AERR, Agmarknet).

Items 5–14 of that list remain open. A daily run should prefer a genuinely new source
over restating one of these.

---

## Added 2026-08-26 (Wednesday theme: energy and gas)

The energy beat is the blog's second-heaviest: a manifest grep for
`gas|energy|ethanol|lpg|petrol|diesel|crude|electric|power|solar|coal|refin|pngrb|cgd|blend|pipeline|fuel`
matches **60 of 211 posts**, with ethanol alone accounting for roughly fifteen. Every
candidate today failed the third grading question — the blog has covered it — and the
day's one real result is a dedup finding, not a new source.

### 🔴 Corpus-survey Tier-1 item 2 ("ethanol feedstock balance against the E20 target") is CLOSED
Not a new source — a correction to this register's own standing backlog. The item, and
the matching COMMISSION_QUEUE entry "Does India have the feedstock for E20?", were both
logged 2026-08-22 against an AERR paper whose latest listed issue is Vol. 37 No. 1 (2024).
The blog then **answered the question itself the following day**:
`india-hit-e20-on-maize-and-rice-not`, published **2026-08-23**, 23,234 bytes, labels
Ethanol & Biofuels · Agriculture & Fertilisers · Energy & Fuels · India.
- The post names the AERR paper by its title ("does India have enough feedstock to meet
  its E20 targets by 2025?") and treats it as the question being answered, which is
  precisely the framing the queue item proposed.
- It runs on ESY 2025-26 allocation data, not the 2024 AERR vintage: ~1,048 crore litres
  allocated against 1,776 crore litres offered (a 59% allocation rate); grain 72.5% of
  allocation vs cane 27.5%; maize alone 45.7%, up from 6.2% in ESY 2022-23; surplus FCI
  rice 22.3%, i.e. more than direct sugarcane juice.
- **Consequence:** do not commission that item. Anything further on E20 feedstock must
  be a genuinely new angle, not the balance question. The only obvious remaining one is
  the *food-security* side the post states but does not develop — a fifth of the petrol
  blend coming out of the public foodgrain stock, against FCI's own stocking norms — and
  that would need the FCI stock series, not an ethanol series. Related published posts
  to dedup against first: `fci-grain-flow-procurement-storage`,
  `fci-storage-scenario-capacity-stock-and`, `7186-litre-why-maize-is-indias-priciest`,
  `sugar-at-5570-kilo-why-cane-acreage`.

### Weak — logged, not actioned (2026-08-26)
- **ESY 2025-26 ethanol allocation figures** (via press aggregation of DFPD/MoPNG; PIB
  factsheet "Ethanol Blending in India", `static.pib.gov.in/.../doc202675912001.pdf`,
  July 2026) — the underlying primary is real and free, but every headline figure is
  already in a post three days old (see above). WEAK on dedup, not on quality. The PDF
  itself did not text-extract on fetch (415 KB, compressed streams); the PIB HTML
  factsheet route `FactsheetDetails.aspx?id=150699` returned **403** to a plain fetcher —
  consistent with this register's standing note that PIB needs a browser user-agent.
- **ORF Middle East, "A $6 LNG Window: Mapping India's Short-Term Gas Demand Potential"**
  (Parul Bakshi, 9 Dec 2025) — fetched and read. Fails grading question 1: no downloadable
  dataset, table or appendix; the numbers are the author's own contribution to an OIES
  report, not a released official series. Fails question 3 as well — the gas-competitiveness
  thesis is already the published `thermal-parity-is-dead-what-85-oil-and`. Its one
  usable figure is a hedge, not a finding: demand "roughly 5–10 percent above the PNGRB
  Good-to-Go baseline", explicitly called "incremental rather than transformative".
  BACKGROUND at best.
- **OIES, "The Global Outlook for Gas Demand in a $6 World"** — could not be assessed:
  `oxfordenergy.org` returned **403** to the fetcher, so nothing about it was verified
  first-hand and nothing is claimed here. Modelled projections with no released dataset
  would be BACKGROUND even if fetched. Re-probe with a browser user-agent if the gas beat
  is revisited.
- **ORF, "A $6 LNG Window: Mapping India's Long-Term Gas Demand Potential"** — companion
  piece to the above, same author and same data profile. Not separately fetched; assumed
  nothing about it beyond that. Not registered.

### Weak / background — logged, not actioned (2026-08-27)
- **Lakshmi Prasanna, Subba Rao, Hari Prasad, Waris & Arun Kumar (2023), "Essentially
  derived variety concept in plant variety rights protection system: underlying economic
  theories, and issues in implementation", *Agricultural Economics Research Review*
  36(1): 77-86, `epubs.icar.org.in/index.php/AERR/article/view/143786`** — fetched and
  read. Open access, free PDF, and squarely in the Thursday beat, but it fails grading
  question 1: the abstract describes a review that "trace[s] theories underlying, and
  rationale behind [the] EDV concept by reviewing economic models of innovation" and
  "documented some challenges in implementation". No released dataset, no appendix, and
  the article page carries no quantified finding of any kind. **BACKGROUND** — the right
  citation to sit *inside* a piece built on the PPV&FR registry data above, explaining
  what an essentially derived variety is and why the boundary is contested, but not a
  piece on its own.


---

## Added 2026-08-29 (Saturday theme: trade, tariffs and industrial policy)

🔴 **File-loss note.** This file and `COMMISSION_QUEUE.md` were both missing from
`masaladeutsch-archive/docs/` at the start of today's run. Neither was ever committed to
git (`git log --all --diff-filter=AD` returns nothing for either path), so when something
reset the repo's working tree on 2026-08-28 (docs/ mtime 14:14) they were wiped as
untracked files, taking six days of Track B output with them. Both were restored from the
Track C mirror at `/Users/Shared/lit_review/masaladeutsch/` (synced 2026-08-28 07:48).
The restore is trustworthy: `LITERATURE_SURVEY.md`, which *is* tracked, is byte-identical
between the repo and the mirror, and the restored queue has 9 open items, matching the
count the 2026-08-28 log recorded. Content after 2026-08-28 07:48 — if any — is not
recoverable. **These two files need committing to git; the mirror is the only copy.**

### Defence Positive Indigenisation Lists — 5th and 6th PIL primaries (DDP, Ministry of Defence)

Follow-up to the 2026-08-22 entry above, which closed with "The 6th PIL needs its own
release verified." It is now verified, from its own release, and the trip turned up a
second primary that contradicts the figure the blog has already published.

- **Data**: two PIB releases, both fetched in full today. **PRID 2300723** (18 Aug 2026,
  11:15AM, Ministry of Defence) and **PRID 2033571** (16 Jul 2024, 12:29PM). Free, no
  login. 🔴 PIB 403s plain fetchers — a browser User-Agent is required, and
  `PressReleaseDetail.aspx` returns a shell with no body; use
  `PressReleasePage.aspx?PRID=<id>`, which returns the full text.

- **Finding 1 — the published post's declared floor can now be closed.** The post
  `5071-items-you-cannot-import-and-rs` (23 Aug 2026) states plainly that "a fifth list
  exists in the sequence but its item count is not established in the sources used here,
  so it is excluded rather than estimated — the 5,071 total is therefore a floor, not the
  full count." PRID 2033571 establishes it: the **5th PIL is 346 items, import-substitution
  value ₹1,048 crore**. The full six-list DPSU total is therefore **5,417**, not 5,071.
  This reconciles exactly against the other primary: PRID 2300723 states "5,012 items
  notified under the first five Positive Indigenisation Lists", and 4,666 + 346 = 5,012.
  Two independent PIB releases agree to the item.

- **Finding 2 🔴 — the ₹2,570 crore figure the blog published is contradicted by an
  *earlier* ministry release.** PRID 2033571 (July 2024) says of the same PIL 1–4 scope:
  "four PILs comprising 4,666 items were notified by the DDP for DPSUs, of which **2,972**,
  having import substitution value worth **Rs 3,400 crore**, have already been
  indigenised." The register entry above, and the published post, carry **2,736 items /
  ₹2,570 crore** for that same scope. A cumulative indigenisation count cannot fall from
  2,972 to 2,736, nor its value from ₹3,400 cr to ₹2,570 cr, between 2024 and 2026 — so
  the two are different vintages or different scopes, and the post's headline arithmetic
  (**₹94 lakh per item**) rests on the smaller pair. On the 2024 primary the same
  calculation gives **₹114 lakh per item** across a *larger* base. The direction of the
  post's argument survives; the specific number does not.

- **Finding 3 — the series the post explicitly set aside is quantified.** The post notes
  the Department of Military Affairs runs "a different series and are not counted above."
  PRID 2033571 gives it: "five positive indigenisation lists of **509 items** notified by
  the Department of Military Affairs (DMA)." Both series together = 5,417 + 509 = **5,926**.

- **Finding 4 — the PIL lists are a small slice of the actual programme.** PRID 2300723:
  more than **33,000** items offered on SRIJAN by DPSUs and SHQs up to June 2026, of which
  the 5,012 PIL items are a subset; more than **15,700** indigenised for an estimated
  import-substitution value of about **₹9,000 crore over the last five years**; and DPSU
  procurement orders on domestic vendors of about **₹10,000 crore** up to March 2026.
  ₹9,000 cr ÷ 15,700 ≈ **₹57 lakh an item** — the same shape as the post's finding (long
  list, small money) at four times the scale, but on a *different denominator*.

- **Blog fit**: this does not open a beat — it **materially updates a published post**,
  `5071-items-you-cannot-import-and-rs` (23 Aug 2026, labels Industrial Policy · Import
  Substitution · Manufacturing · India). Manifest dedup: snapshot 2026-08-29T06:04, 224
  posts, 15 title hits on the defence/indigenisation/import-substitution regex; that slug
  is the only one on the PILs, and it was read in full rather than judged by title.

- **Caveat**: 🔴 the SRIJAN "items offered" total went **down** — over 36,000 by June 2024
  (PRID 2033571) against more than 33,000 by June 2026 (PRID 2300723). A cumulative offer
  count cannot shrink, so the series has been re-based or de-duplicated at some point and
  neither release says so. Do not build a trend on it, and do not present the two as
  comparable. Same caution applies to "indigenised": 12,300 in three years (2024) vs
  15,700 in five years (2026) are different windows, not a delta. And "import substitution
  value" remains the ministry's own undefined term throughout.

- Grade: **COMMISSIONABLE** — as a correction-and-update piece, not a new subject.

### Weak / background — logged, not actioned (2026-08-29)

- **DGCI&S publication activity** (dgciskol.gov.in) — surfaced by the second Saturday
  query: Laspeyres trade indices for Apr–May 2026 on both 2012-13 and 2022-23 bases, a
  committee report on base-year revision for merchandise trade indices, and a quarterly
  merchandise-trade review for Oct–Dec 2025. Not fetched, so nothing is asserted about
  contents. Noted only because a **base-year revision** is the kind of thing that silently
  breaks a published index series, and the blog runs trade-data pieces off this portal;
  worth a proper look on a future Saturday. BACKGROUND, pending verification.

---

## Added 2026-08-31 (Monday theme: agricultural labour and rural incomes)

**Dedup finding that reframes the theme, recorded first because it changes the brief.**
`LITERATURE_SURVEY.md` §3 lists agricultural labour and rural incomes as a zero-coverage
area. That is now **stale**. The published post `a-17-rural-pay-rise-that-nobody-received`
(22 Aug 2026) was read in full today, and it does not merely touch the beat — it covers
the Labour Bureau's CPI-AL/CPI-RL base revision from 1986-87 to 2019=100 and the
undisclosed village-sample swap underneath the headline 17-18% wage jump; the
break-adjusted 4.3% versus the old-sample 6.23%; the fact that CPI-AL sets wages under
the central rural employment guarantee and anchors state minimum wages for agricultural
and rural labour; **MGNREGA's repeal** by the VB-G RAM G Act 2025 (assent 21 Dec 2025, in
force 1 Jul 2026), with a side-by-side of the two schemes' guaranteed days (100 -> 125)
and work-availability windows; early VB-G RAM G person-days (30 crore approved April 2026
-> 43 crore May); and PM-KISAN's landholding targeting as the reason it exerts no pressure
on the agricultural wage. **MGNREGA and rural wage indexation should be treated as a
covered subject from now on, not a gap.** Manifest dedup: snapshot 2026-08-31T07:39,
237 posts; regex `wage|labour|labor|employ|mgnrega|rural|migrant|income|job|worker` over
titles returns 4 hits, of which this is the only one on the beat.

Two sub-angles the post explicitly declines and leaves open: (a) VB-G RAM G's own
performance, which the post refuses on the ground that the scheme was "nine weeks old at
the time of writing" — still true, it is nine days older today, so hold it; (b) the
occupation-level anomalies in the Labour Bureau's own tables, for which the post notes
"no occupation-level explanation has been offered".

**Open-item check (step 1, which outranks new candidates).** The E20 feedstock item and
the Minor Irrigation item both carry AERR citations pinned to "latest listed issue is
Vol. 37 No. 1 (2024)". Re-checked today at `epubs.icar.org.in/index.php/AERR/issue/archive`:
the archive still ends at **Vol. 37 No. 1 (2024)**, twelve issues back to Vol. 31 No. 2
(2018). No newer issue, so neither item is unblocked and both caveats stand unchanged.

### NSS 77th Round — Situation Assessment of Agricultural Households (NSSO / MoSPI)

**Data**: PIB PRID 1753856, MoSPI, "NSS REPORT NO. 587: Situation Assessment of
Agricultural Households and Land and Livestock Holdings of Households in Rural India,
2019", posted 10 Sep 2021 — fetched in full 2026-08-31. 🔴 PIB 302-redirects plain
requests to `?PRID=<id>&reg=48&lang=2`; follow redirects (`curl -L`) **and** send a
browser user-agent, or you get a 174-byte "Object moved" stub. Reference year is the
agricultural year **July 2018 – June 2019**; fieldwork Jan–Dec 2019 in two visits.
Sample stated in the release: 5,950 FSUs allotted, 5,940 surveyed in visit 1, 58,035
households, of which 45,714 agricultural households (44,770 in visit 2). Free, no login.
Companion release for the comparison year: PIB PRID 2003180 (MoA&FW, 6 Feb 2024).

**Finding**: for the household India's farm-income policy is actually measured on,
**wages are the largest single source of income, not crops**. Table 6, paid-out-expenses
basis, average monthly income per agricultural household: wages **₹4,063**, net receipt
from crop production **₹3,798**, farming of animals ₹1,582, non-farm business ₹641,
leasing out land ₹134 — total **₹10,218**. On the fuller basis that also charges imputed
expenses, the gap roughly doubles: wages ₹4,063 (unchanged, since imputation hits farm
costs) against crop production **₹3,058** and animals **₹441**, total **₹8,337** — wages
are then **49%** of household income and crop production **37%**.

And the survey reaches that result on a population **defined to exclude the rural workers
most dependent on wages**. The release states in terms: "households which were entirely
agricultural labour households and households receiving income entirely from coastal
fishing, activity of rural artisans and agricultural services were not considered as
agricultural households and they were kept outside the scope of the survey." Qualifying
required more than ₹4,000 of agricultural produce value plus a member self-employed in
agriculture. Landless share within the surveyed population: 8.2%; average area owned
0.512 ha. Indebtedness: 50.2% of agricultural households, ₹74,121 average outstanding.

**Blog fit**: extends the beat `a-17-rural-pay-rise-that-nobody-received` opened, from
the opposite side. That post is about the index that sets what agricultural labourers are
paid; this is the official survey that measures farm household income and leaves pure
agricultural-labour households out of the frame entirely — while still finding that the
wage beats the crop inside the households it does count. Nearest published post by slug:
`a-17-rural-pay-rise-that-nobody-received`. Also adjacent to
`annadata-to-urjadata-farmer-income-case` (4 Aug 2026), which argues a farmer-income case
without this income decomposition. Dedup on bodies, not just titles: `grep -rliE
'situation assessment|77th round|NSS 587|agricultural household' posts/` returns two files
(`the-price-of-grain-msp-msv-and`, `tamil-nadus-water-infrastructure-runs`) and the phrase
"agricultural households" appears exactly **once** across the whole corpus — incidental,
not a treatment. The income composition is uncovered.

**Caveat**: 🔴 **vintage is the whole risk here.** Reference year 2018-19, published 2021,
and it is *still* the current official figure — PIB PRID 2003180 (MoA&FW, 6 Feb 2024) is a
Lok Sabha reply that gives the government's own latest answer as the 77th round, tabulating
only 2012-13 (70th round, NSS Report 576) at ₹6,426 and 2018-19 (77th round) at ₹10,218.
So the number is seven years stale by reference year and there is no newer round to cite —
that is a fact about the data, not a defect in the source, but every figure must be dated
in the piece and no "farmers today earn" phrasing is defensible. Second caveat: the two
expense bases are not interchangeable, and the ₹6,426 comparison figure's basis was not
established today — do not compute a 2012-13 → 2018-19 growth rate until both are
confirmed to be on the same basis. Third: "agricultural household" is a survey construct
with a ₹4,000 threshold, not a synonym for "farmer" — the piece must define it early.

### Weak / background — logged, not actioned (2026-08-31)

- **ICAR e-publications, *Agricultural Economics Research Review* archive
  (`epubs.icar.org.in/index.php/AERR/issue/archive`)** — re-fetched today only as the
  open-item vintage check described above. Still ends at Vol. 37 No. 1 (2024). Not a
  candidate in itself; logged so the next Monday/Friday run does not re-fetch it hoping
  for a new issue. Re-check no sooner than a month out.

---

## Added 2026-09-01 (Tuesday theme: insurance, reinsurance and financial plumbing)

Dedup baseline for this whole section, run 2026-09-01 against `meta/manifest.json`
(snapshot 2026-08-31, **238 posts**): a regex for `insur|reinsur|irdai|ifsca|gift.?city|
solvency|actuar` over the full manifest returns **exactly one post** —
`premium-now-claim-later-float-indias` ("Premium Now, Claim Later: The Float India's Car
Boom Is Building", 2026-08-22, labels incl. *Insurance & Reinsurance*), which is motor
float. `irdai`, `ifsca`, `gift city`, `solvency` and `actuar` return **zero**. The beat is
as empty as the survey said.

### IRDAI obligatory cession to GIC Re, held at 4% for FY 2025-26 (third consecutive year)

IRDAI's annual cession notification for the financial year 1 April 2025 – 31 March 2026,
as reported and quoted by Reinsurance News (fetched 2026-09-01, HTTP 200).

- **Data**: the notification text itself is quoted verbatim — "The percentage cession of
  the sum insured on each General Insurance Policy to be reinsured with the Indian
  Re-insurer(s) shall be 4% (four percent) in respect of insurance attaching during the
  financial year beginning from 1st April, 2025 to 31st March, 2026." The backing
  dataset is the **IRDAI Annual Report 2024-25** (free PDF, no login — a copy is served
  at `lifeinscouncil.org/component/IRDAI%20Annual%20Report%202024-25.pdf`; source it from
  `irdai.gov.in` before publication), which carries 74 registered insurers and reinsurers
  as at 31 March 2025 and industry AUM of ₹74.43 lakh crore. Minimum commission floors by
  line are also stated: 5% motor TP and oil & energy, 10% group health, 7.5% crop, 15% all
  other classes.
- **Finding**: every general insurance policy written in India carries a **compulsory 4%
  cession to a single state-owned reinsurer**, GIC Re — held at 4% for the third year
  running, down from 5% earlier. The interesting number is on the receiving side: GIC Re's
  obligatory business fell from **43% of total revenue to 39%** (April–October FY25), and
  was 30% in FY21. So the mandate is being *held constant* while the recipient's
  dependence on it moves — up sharply from FY21, then down again. A compulsory transfer
  whose share of the beneficiary's book is not stable is not the settled arrangement it is
  usually described as.
- **Blog fit**: opens the near-empty **Insurance & Reinsurance** beat from the
  wholesale/plumbing end rather than the retail end. Nearest published post is
  `premium-now-claim-later-float-indias` (motor float — the retail side of the same
  balance sheet). The structural sibling is `who-collects-indias-gst-and-who`: identical
  who-pays-vs-who-receives framing, applied to a mandated transfer instead of a tax.
- **Caveat**: the 4% and the quoted sentence reached this register **through a trade
  publication quoting the notification**, not from `irdai.gov.in` directly — pull the
  notification itself before publishing, and do not repeat the 5%-to-4% history until the
  year of that change is sourced (the article does not give it). The 43%→39% figure is a
  **part-year** number (April–October FY25) and must not be presented as a full-year
  share. Finally, "4% cession" is 4% of *sum insured on each policy*, not 4% of industry
  premium — do not convert one into the other without the Annual Report's own tables.
- Grade: **COMMISSIONABLE**. Logged 2026-09-01.

### General Insurance Council industry statistics (Flash Figures, Segmentwise Report, GIC Year Book 2024-25)

`gicouncil.in/statistics/industry-statistics/`, fetched 2026-09-01.

- **Data**: four published series — **Flash Figures**, **Segmentwise Report**, **Financial
  Highlights**, and **Yearbook Archives**, latest edition **GIC Year Book 2024-25**, served
  as a PDF at `/Year-Book/GIC_Yearbook_2024-25.pdf`. Free, no login, no paywall on the
  statistics pages. Segments covered: fire, marine, motor, health, aviation, liability,
  personal accident, crop, engineering, property, miscellaneous. This is the segment-level
  premium data the blog would need for any general-insurance piece, and it is the natural
  primary behind the existing motor-float post.
- **Finding (NOT yet primary-verified)**: the statistics page surfaces **₹94,247.6 crore in
  total health claims settled in 2024-25, with cashless-only admissions at 66.4% of
  volume**. Both fetches placed this figure inside a **news item on the page**, not in a
  data table — so it is trade-press-on-a-trade-body-site, which is not the same thing as
  the Council's own statistics.
- **Blog fit**: the dataset, not the figure, is what earns the entry — it is the missing
  primary under the whole *Insurance & Reinsurance* label, and it would let a future piece
  put the motor float of `premium-now-claim-later-float-indias` next to the other ten
  segments instead of standing alone.
- **Caveat**: periodicity and year-coverage of Flash Figures and the Segmentwise Report
  were **not** resolvable from the fetched pages — confirm both before building anything
  time-series on them. The health-claims figure above must be re-sourced from the Year Book
  PDF or dropped; do not publish it on the page-snippet's authority. Note also that the GI
  Council is an **industry body**, not the regulator — cross-read anything load-bearing
  against IRDAI.
- Grade: **BACKGROUND** (obtainable primary data confirmed; no verified finding yet).
  Logged 2026-09-01.

### Weak / not deep-read, one line each

- **GIFT City IIO premiums "quadruple to $648.7 million in FY26"** (Business Standard,
  4 June 2026) — the most striking number of the day and a confirmed zero-coverage area,
  but the **primary could not be located**: the Business Standard article 403s,
  `ifsca.gov.in/Publication` 404s, and the IFSCA Bulletin listing
  (`ReportPublication/index/wF6kttc1JR8=`) renders an **empty table**. IFSCA's own homepage
  publishes a differently-scoped counter — **"USD 334 Mn+ premium transacted by insurance
  entities (IIOs & IIIOs)" for Q4 2025-26** — which includes intermediary offices and so
  cannot be reconciled with the press figure without the underlying release. A quadrupling
  off a $162.10 mn base is also a small-base artefact as much as a finding. Re-try when the
  **IFSCA Annual Report 2025-26** appears; do not commission on press attribution alone.
- **NCAER, "Making the IFSC a Re-insurance Hub"** (hosted on ifsca.gov.in,
  `ncaer-report20042022032732.pdf`, dated 2022) — a commissioned advocacy report, four years
  stale, and its numbers are projections rather than released data. Background at best.

### seednet.gov.in — DA&FW Seed Net portal (candidate, NOT assessed)

- **Data**: unknown. Surfaced 2026-09-03 as a possible government primary for the
  Thursday seeds / plant-variety-rights / agricultural-IP beat — the three-generation
  breeder → foundation → certified seed production series, seed availability and indent,
  and state-wise figures are the sort of thing the portal is supposed to carry.
- **Status**: `https://seednet.gov.in/Material/Seed_Production.htm` returned **HTTP 503**
  on direct fetch, so **nothing on the page has been read and nothing is claimed about
  it**. Not graded. Retry on a future Thursday before deciding whether it is
  COMMISSIONABLE, BACKGROUND or WEAK.
- **Blog fit (provisional)**: would extend the same confirmed zero-coverage area the open
  PPV&FR queue item opens. Manifest dedup re-run 2026-09-03 for
  seed/variet/ppvfr/patent/breeder/germplasm/intellectual/hybrid across titles and slugs:
  **zero hits**, so the area is still genuinely uncovered.
- **Caveat**: Seed Replacement Rate is the figure most likely to be reachable and also
  the one most likely to be quoted loosely — search-result prose today gave "less than
  25%-30%" for open-pollinated food grains and oilseeds with no year and no source
  attached. Treat any SRR number as unusable until it is read off a dated departmental
  table. WEAK on evidence until fetched, logged 2026-09-03.

---

## Added 2026-09-04 (Friday theme: irrigation, water and soil)

**Dedup first.** The Friday theme's headline source is already here: the AERR paper
Bathla, Kannan & Das, "Public investment in irrigation across the Indian states",
AERR 37(1) 2024, was registered on the irrigation entry at line 158 and already carries
an open queue item (COMMISSION_QUEUE, the 6th Minor Irrigation Census piece). Today's
search returned it again; it is **not re-logged**. The soil half of the Friday theme was
untouched, so the search went there.

Manifest dedup re-run 2026-09-04 across all **255** post titles for
`irrigat|water|soil|groundwater|canal|drip|organic carbon|aquifer|monsoon|rainfall|watershed`:
**6 hits, none about soil or agricultural water**. All six are water *infrastructure
spending* pieces — `amruts-197-lakh-crore-urban-portfolio`,
`tamil-nadus-water-infrastructure-runs`, `indias-79-lakh-crore-rural-water`,
`the-water-bill-nobody-mentions-what` (semiconductor fabs),
`price-is-wire-how-gcam-actually-links` (a model, not a measurement), and
`guar-gum-indias-35-billion-export-peak`, where "poor soil" is agronomic colour in a
trade piece. Soil health as a measured quantity has **zero coverage**.

### Soil Health Card scheme — the national soil-test panel, and its April-2023 break — COMMISSIONABLE
- **Data**: the Soil Health Card portal, `soilhealth.dac.gov.in`, run by DA&FW with NIC.
  Verified live by direct fetch 2026-09-04: home and `/nutrient-dashboard` both return
  **HTTP 200**. It is a JavaScript single-page app, so the dashboard content is not
  visible to a plain fetch; the app's own bundle
  (`/assets/index-Ed_k0WPH.js`) names its data endpoint as an Apollo GraphQL client
  pointed at **`https://soilhealth4.dac.gov.in`**, which answers a bare GET with
  **HTTP 400** — i.e. the server is up and rejecting a malformed query, not refusing
  access. No login wall was encountered at the transport level. The card itself carries
  **12 parameters: N, P, K, S; Zn, Fe, Cu, Mn, Bo; pH, EC and OC (Organic Carbon)** —
  organic carbon is a scheme-standard field on every card, not an add-on.
- **Finding**: not the SOC level — the **regime break in how it is measured**. PIB
  release PRID 2104403, Ministry of Agriculture & Farmers Welfare, "Celebrating a Decade
  of Soil Health Cards", posted 18 Feb 2025 (fetched in full 2026-09-04), states that the
  portal was revamped and rolled out in **April 2023** with GIS integration, and that
  from then on the mobile app **restricts the sample-collection region** for the village
  operator, **auto-selects the latitude and longitude** of the sample, and generates a
  **QR code linking sample to result directly from geo-mapped labs, "without any manual
  intervention"**. It renders layers down to **cadastral boundary**. The plain reading is
  that samples before April 2023 were sited and keyed by hand and samples after it are
  machine-geolocated and machine-keyed — so any district organic-carbon series that
  straddles April 2023 is comparing two different collection regimes, and a "decline" or
  "improvement" across that seam may be an artefact of the seam. The same release gives
  the delivery scaffolding: **665 Village-Level Soil Testing Labs across 17 States** as of
  February 2025, and, as of 2024, **1,020 schools running the School Soil Health
  Programme with 1,000 school labs and 125,972 students enrolled**. The scheme was folded
  into RKVY as the "Soil Health & Fertility" component from **2022-23**.
- **Blog fit**: opens the **soil** half of the Friday zero-coverage area (irrigation is
  already opened by the Minor Irrigation Census queue item) and puts a fourth post in the
  water/land cluster. Nearest published post is `indias-79-lakh-crore-rural-water` — that
  is Jal Jeevan Mission *drinking-water* capital expenditure, a different ministry and a
  different quantity; the connection is thematic only and should be cross-linked as the
  blog cites its own reporting, never as confirmation.
- **Caveat**: 🔴 **The export path is the one thing not yet verified.** The endpoint is
  live and the dashboard is described by the government as being in the public domain,
  but no query has been run and no district-level organic-carbon table has been pulled.
  Nothing about SOC levels, trends, or district rankings may be written until a real
  query returns a real table. Second, the widely circulated "ICAR six-year study, 254,236
  soil samples, 620 districts, 29 states" figure surfaced today **only from coaching-site
  secondaries** (vajiramandravi, carpediemias, dhruvstarindustryinsights) and is **not
  verified**; do not repeat it on that authority — trace it to the IISS Bhopal source or
  drop it. Third, PIB PRID 2104403 gives no national count of cards issued or samples
  tested, so those numbers must come from the portal or a dated Lok Sabha answer, not
  from this release. Fourth, `pib.gov.in` returns **403 to a plain fetcher and 302 to a
  UA-less curl** — it needs a browser user-agent and `-L` to follow to the
  `&reg=&lang=` form of the URL.

### Weak / background — one line each (triaged, not deep-read)
- **Rattan Lal, "Soil Carbon in Agro-Ecosystems of India", Journal of the Indian Society
  of Soil Science 74(1), 2026** (`epubs.icar.org.in/index.php/JISSS/article/view/180202`,
  fetched 2026-09-04) — **BACKGROUND**. It is a review and a policy argument, not a
  measurement: the abstract carries exactly one number, a proposed payment-for-ecosystem-
  services rate of **US $50 per credit (~INR 4,600)**, and no SOC stock in Mg/ha or Pg,
  no sample, no district. It also names the **Bharat Soil Protection Policy (BSPP) being
  developed by ICAR** and calls for a Soil Health Act at district, state and national
  level — both useful as the policy frame around a piece built on portal data, neither
  able to carry one. Cite inside, do not commission.
- **AERR 37(1) 2024, Bathla, Kannan & Das, public irrigation investment and financial
  recovery** — already registered (line 158) with an open queue item. Re-surfaced by
  today's first search; not re-logged.
- **Frontiers in Sustainable Food Systems 2025, SOC fractions across land uses in
  temperate India** — single-region field study outside the Indian-journal estate, no
  national panel, nothing the blog could pull. **WEAK**.
- **Coaching-site summaries of the ICAR/IISS SOC study** (vajiramandravi, carpediemias,
  dhruvstarindustryinsights) — **WEAK by construction**: secondary prose with no
  citation to a dated ICAR document. Logged only so a future run does not mistake their
  agreement with each other for corroboration.

---

## Added 2026-09-07 (Monday theme: agricultural labour and rural incomes)

**Step 1 outranked the search today, and produced the day's whole result.** The Monday
theme is now well covered — the 2026-08-31 entry established that
`a-17-rural-pay-rise-that-nobody-received` (22 Aug 2026) treats CPI-AL/CPI-RL rebasing,
the village-sample swap, MGNREGA's repeal by the VB-G RAM G Act 2025 and PM-KISAN's
targeting, and that the beat should be treated as covered rather than as a gap. Manifest
dedup re-run today (snapshot 2026-09-05T22:16, **257 posts**, regex
`wage|labour|labor|mgnrega|nrega|rural|farm|employ|migrant|income|agricultur|harvest|crop`
over titles and slugs): 11 hits, of which exactly one — that post — is on the beat, and
one more, `annadata-to-urjadata-farmer-income-case`, is adjacent. Unchanged picture. So
the open-queue check took priority, and it paid.

### PPV&FR Authority registry — the blocked check is resolved, and it changes a number

**Status of the host.** `https://plantauthority.gov.in/` returned **HTTP 200, 171,508
bytes** on direct fetch today with a browser user-agent. On 2026-09-03 it returned 503 and
the Thursday run recorded the item as un-advanceable. It is up now, so the two outstanding
checks on the queued item "57.8% of India's plant-variety rights are cereals" were run.
(The deep link `/plant-varieties-registry-related-information` still fails outright —
curl exit 000, connection never completes — so the homepage is the working surface.)

**Data**: two ECharts series hardcoded in the homepage source, both headed with an
explicit vintage the site states itself: "**10885 Certificates issued as on 31.08.2026**"
and "10885 Certificates issued crop group-wise as on 31.08.2026". Free, no login, no
browser needed beyond a UA string. This is materially better than what the item was
resting on: the 2026-08-27 capture was described in the queue as a *live counter with no
vintage archive*, which is why check (1) told the writer to date-stamp it by hand. The
page now carries its own as-on date.

**Finding 1 — the crop split holds, on a newer vintage.** Crop-group series as on
31.08.2026, total 10,885: **Cereals 6,280**, Vegetables 1,386, Fibre 1,006, Legumes 872,
Oilseeds 577, Fruits 429, Sugar 93, Other 242. Cereals are **57.7%**, against the 57.8%
(6,246 of 10,802, as on 31.07.2026) captured on 2026-08-27. The queued headline survives.

The two captures also **cross-validate**, which is the reason to trust either. Month on
month: cereals +34, vegetables +19, fibre +17, legumes +6, fruits +4, oilseeds 0, sugar 0,
other +3 — summing to +83, exactly 10,885 − 10,802. And today's single "Other" bucket
(242) reconciles with the five small categories the 31.07 capture broke out separately
(Spices 151 + Trees 43 + Flowers 36 + Cash 5 + Medicinal & Aromatic 4 = 239, +3 in a
month). ⚠️ Note the consequence for the piece: **today's homepage no longer breaks out
spices**, so the "Spices get 151" half of the working title is only available from the
2026-08-27 capture or the Annual Report — do not expect to re-fetch it.

**Finding 2 — check (2) is resolved, and the unverified figure was wrong in the direction
that matters.** The registration-type series as on 31.08.2026, total 10,885: **Farmer
5,368**, Extant Notified 2,025, New 1,921, Extant VCK (varieties of common knowledge)
1,557, **EDV 14**. Farmers' varieties are therefore **49.3%** of all certificates ever
issued — **just under half, not over it**. The circulating snippet claim the queue item
flagged as unverified ("4,847 of 9,210 certificates (52.6%) went to farmers") is now
superseded by a dated primary, and a piece written on it would have asserted that most
Indian plant-variety certificates go to farmers when the Authority's own figure says they
do not. Both series sum independently to the same 10,885, which is the check that makes
them usable.

**Finding 3 — incidental, and the sharpest number on the page.** Essentially derived
varieties: **14 certificates, 0.13% of 10,885**, in a register that has been issuing since
2007 — while the homepage simultaneously carries a live notice, "General Guidelines
Regarding the Registration of EDV". EDV is the doctrine that decides whether a variety
bred from a protected variety needs the original breeder's authorisation, so it is the
mechanism that determines who captures the value of incremental breeding. Fourteen.

**Blog fit**: does not open a new area — it resolves checks on an item already queued
against the confirmed zero-coverage seeds / plant-variety-rights / agricultural-IP area.
Nearest published posts remain `indias-445-billion-spice-export-book-is` and
`379-kilos-hectare-in-punjab-44-in`, both to be cross-linked as earlier reporting in house
style, never as confirmation.

**Caveat**: 🔴 these are **chart literals embedded in homepage JavaScript**, not a
published table — genuinely primary, and internally consistent across two independent
series and two dates, but the Authority publishes no schema for them. The category names
come from hidden inputs on the same page (`Extant Notified`, `Extant VCK`, `Farmer`,
`New`, `EDV`) and are undefined there, so check (4) of the original item — state that the
categories are the Authority's own and undefined — now applies to the *registration-type*
split as well as the crop split. The Annual Report cross-read (check 1) is still worth
doing and is still the citable artefact; nothing here replaces it. Check (3) stands
unchanged: certificates issued ≠ varieties commercially sold. The host is intermittent —
up today, 503 four days ago — so anyone writing this should pull and keep a local copy
rather than plan to fetch at publication time.

### Weak/off-scope, one line each (triaged, not deep-read)

- **AERR, "Agricultural wages in India: trends and determinants"**
  (`epubs.icar.org.in/index.php/AERR/article/view/140527`) — WEAK by dedup, not by
  quality: farm-wage trends are the exact subject of `a-17-rural-pay-rise-that-nobody-received`,
  which runs on the Labour Bureau's own CPI-AL series and a base-revision break. A
  determinants paper does not contradict or materially update it.
- **Venkatesh P., "Recent Trends in Rural Employment and Wages in India: Has the Growth
  Benefitted the Agricultural Labours?", AERR Vol. 26 (2013)** — WEAK on vintage: a
  thirteen-year-old series on a beat where the live question is a 2026 base revision and a
  scheme repealed in December 2025.
- **Pattayat & Parida, "Drivers of Rural Non-farm Sector Employment in India, 1983–2019"
  (Sage, 2024)** and **NCAER, "Rural Non-farm Employment in India: Access, Incomes and
  Poverty Impact"** — WEAK by dedup: rural non-farm employment is **already queued** as
  "Rural India's fastest quarter off the farm" (COMMISSION_QUEUE, logged 2026-08-24) on
  the PLFS Quarterly Bulletin, which is a quarterly official series running to Apr–Jun
  2026. Neither an academic panel ending in 2019 nor an undated NCAER volume improves on
  that source, and the queue item is the piece.
- **IJAgS, "Trends in agriculture, non-farm sector and rural employment in India: An
  insight from state level analysis"** (`epubs.icar.org.in/index.php/IJAgS/article/view/48502`)
  — same dedup as above; not fetched beyond the search listing, and not counted as assessed.
- **AERR issue archive** — not re-checked today. It was confirmed on 2026-08-31 as still
  ending at Vol. 37 No. 1 (2024), and one week is not a plausible interval for a new issue
  of a journal whose archive has been static since 2024.

## Added 2026-09-08 (Tuesday theme: insurance, reinsurance and financial plumbing)

Second Tuesday pass on this theme (2026-09-01 took the domestic wholesale end — the IRDAI
obligatory cession and the GI Council statistics), so it was re-aimed at the leg 09-01
explicitly left untouched: **IFSCA / GIFT City**, which that entry's own dedup run
recorded as returning zero manifest hits. Dedup re-run today against
`meta/manifest.json` (snapshot 2026-09-07T19:53+05:30, **257 posts**): a regex for
`ifsca|gift.?city|reinsur|insur|bullion|fintech|offshore|banking.?unit` over the full
manifest returns **exactly one post**, `premium-now-claim-later-float-indias` ("Premium
Now, Claim Later: The Float India's Car Boom Is Building", 2026-08-22), matching only on
`insur`. `ifsca`, `gift city`, `bullion`, `offshore` and `banking unit` return **zero**,
unchanged from a week ago and now against 19 more posts.

### IFSCA Bulletin, Jan–Mar 2025 — GIFT IFSC's insurance leg is 94% reinsurance

`ifsca.gov.in/Document/ReportandPublication/ifsca-bulletin-jan-mar-202509052025055132.pdf`,
fetched 2026-09-08 (HTTP 200, 4.6 MB, text extracted with `pdftotext -layout`). Issued by
the Division of Economic Policy and Analysis, IFSCA; the front matter states the source is
"the periodic reports submitted by the regulated entities to IFSCA" and grants explicit
reproduction permission subject to acknowledgement.

- **Data**: a quarterly statistical bulletin with **26 numbered tables**, free, no login,
  no paywall, published on the regulator's own domain, and issued each quarter (Apr–Jun,
  Jul–Sep, Oct–Dec, Jan–Mar editions for 2024 and 2025 all resolve on `ifsca.gov.in`), so
  it is a genuine time series rather than a one-off report. The tables the blog would
  actually use: **Table 3** number of IBUs, **Table 4/5** assets and liabilities of IBUs,
  **Table 10** industry-wise credit exposure of IBUs, **Table 11** *country-wise* exposure
  of IBUs, **Table 12** IFSC exchange turnover, **Table 24** premium written by IFSC
  Insurance Offices (IIOs) and Intermediary Offices (IIIOs), **Table 25** line-of-business
  direct insurance, **Table 26** line-of-business reinsurance. Headline dashboard figures
  (as on/during Mar 2025): 865 total IFSCA registrations (including in-principle/
  provisional), banking assets USD 88.51 Bn, average monthly IFSC-exchange turnover USD
  92.15 Bn, 162 fund management entities with USD 15.74 Bn of commitments raised, 33
  aircraft lessors and 24 ship lessors, 31.99 tonnes of gold traded on IIBX worth USD 2.9
  Bn in the quarter, and 18 insurance offices plus 27 intermediary offices.
- **Finding**: GIFT IFSC is described everywhere as an offshore insurance hub. Its own
  quarterly tables say the direct-insurance business barely exists. Summing Table 25 across
  the four quarters of FY 2024-25 gives **USD 12.42 Mn of gross direct written premium**
  (2.43 + 2.42 + 3.96 + 3.61); summing Table 26 over the same four quarters gives **USD
  195.45 Mn of reinsurance premium** (44.54 + 48.00 + 44.76 + 58.15). Reinsurance is
  therefore **94.0% of the centre's insurance book**. The direct **life** line is USD
  **2.54 Mn for the entire year** (0.46 + 0.82 + 0.90 + 0.36) — under ₹25 crore, from a
  jurisdiction hosting 18 registered insurance offices. Set against USD 88.51 Bn of banking
  assets on the same dashboard page, the whole insurance leg is roughly a five-hundredth of
  the banking leg. The centre did not fail to attract insurance; it attracted one *kind* of
  insurance, the wholesale cession end, and almost none of the retail end it is marketed on.
- **Blog fit**: opens the **IFSCA / GIFT City** zero-coverage area and gives the near-empty
  *Insurance & Reinsurance* label its offshore half. Nearest published post is
  `premium-now-claim-later-float-indias` (motor float — domestic, retail, the opposite end
  of the same balance sheet). It also completes the pipe the 2026-09-01 entry opened: India
  *compels* 4% of every general policy into a domestic state reinsurer (GIC Re) while the
  offshore centre built to attract international reinsurance capacity writes USD 195 Mn a
  year. Structural sibling on the blog is `who-collects-indias-gst-and-who` — the same
  who-writes-vs-who-receives framing.
- **Caveat**: four things must be checked before publication. (1) Table 24's Jan–Mar 2025
  IIO figure of USD 61.70 Mn carries a printed footnote — "Reinsurance data of one IIO is
  under examination and hence not included" — so that one quarter is understated by an
  unknown amount; the 94% share should be recomputed once the audited figure lands, and
  quoted as *approximately* 94% until then. (2) All FY 2024-25 figures are marked
  **unaudited** on both tables. (3) Table 26 shows "Health + PA" collapsing from 26.48 to
  2.21 between Oct–Dec and Jan–Mar while a separate "Health Insurance" line appears at
  5.77 in the same quarter — that looks like a reclassification, not a collapse in
  business, and must be resolved against the following bulletin before either number is
  narrated. (4) Table 24 (offices) and Tables 25/26 (lines of business) are differently
  scoped — do not add or divide across them.
- Grade: **COMMISSIONABLE**. Logged 2026-09-08.

### Weak/off-scope, one line each (triaged, not deep-read)

- **IFSCA Annual Report 2024-25** (issued 2025-08-18; TeamLease RegTech and Cyril Amarchand
  Mangaldas both carry summaries) — almost certainly the right *annual* primary, but three
  searches failed to surface a direct PDF URL on `ifsca.gov.in`, and every accessible
  account of its contents was a law-firm or compliance-vendor summary rather than the
  document. Not registered on secondhand summaries. Worth one attempt at
  `ifsca.gov.in/ReportPublication/index/zcGvy-Iqfcg=` (the Annual Reports index, which does
  resolve) on a future Tuesday; the quarterly bulletins already carry the tables, so this is
  a completeness errand, not a blocker.
- **PwC India, "Banking in GIFT IFSC" (April 2024)** — a consultancy explainer, not a data
  source; its figures are restatements of IFSCA's own. Standing rule on vendor material
  applies. WEAK, and unnecessary now that the primary is in hand.
- **`giftcityadvisor.com` mirror of the Jul–Sep 2025 IFSCA bulletin** — a third-party copy of
  a document the regulator publishes itself. Never cite the mirror; note only that a
  **Jul–Sep 2025** edition exists, which means the series runs at least two quarters past
  the edition read today and a piece built on it can be brought to a current vintage.
- **`gicouncil.in` industry statistics** — surfaced again alongside today's query; **already
  registered 2026-09-01** with its own caveats. Listed only so the day's candidate count is
  honest, not re-triaged.

## Added 2026-09-09 (daily task, Wednesday: energy and gas)

The weekday brief warns that energy is heavily covered and to bias hard toward something
unrun. Dedup measured how heavily: a broad energy regex over the **257-post manifest**
(snapshot 2026-09-07) returns **93 hits** — more than a third of the blog. But the same
sweep found the coverage is almost entirely on the **molecule** side. Narrow regexes
returned: nuclear **0**, energy-efficiency/PAT/appliance-labelling **0**, domestic coal
supply (Coal India / e-auction / washery / linkage) **0**, transmission-and-grid **0** real
hits (one false positive on "SIP"), power-market/exchange **0** real (all forex false
positives). A precise electricity-distribution regex
(`discom|at&c|electricity|power utilit|rdss|distribution util|smart meter|kwh`) returns
exactly **one** post. So the blog has 93 energy pieces and essentially nothing on the
**electron** side: the grid, the discoms, the power market, nuclear. That asymmetry is the
day's real finding and it should shape future Wednesdays.

The one electricity post is `discom-debt-relief-token-charge` — an interactive *calculator*
(read directly, 4,673 chars), not a reported piece. It models a per-connection token charge
against discom debt, with defaults sourced to ICRA May 2025 (debt ₹7.4 lakh crore), IISD
2025 (subsidies ₹2.1 lakh crore), CEA/Manorama (8.7% CAGR) and PFC (~70% rural billing
efficiency), and its standing premise is **"₹64,000 cr added to debt every year"**. Today's
source bears directly on that premise, which makes this a materially-updating candidate
against a named slug rather than a new-beat land grab.

### PIB / Ministry of Power — two releases, six weeks apart, two different FY25 AT&C loss figures

Both fetched directly (`pib.gov.in` returns HTTP 403 to a plain fetch; a browser
User-Agent over curl returns HTTP 200 — the standing PIB access note holds).

- **Data**: two Press Information Bureau releases from the **same ministry**, free, no login.
  (1) **PRID 2200450**, *"Key Initiatives to Bring Down AT&C Losses of Power Distribution
  Utilities"*, **08 DEC 2025 5:02PM by PIB Delhi** — a written reply by the Minister of
  State for Power, Shri Shripad Yesso Naik, in the **Rajya Sabha**. (2) **PRID 2215761**,
  *"Power Distribution Utilities Record Positive PAT After Years of Losses; This Marks a New
  Chapter, Says Power Minister"*, **18 JAN 2026 10:34AM by PIB Delhi** — a press release
  quoting the Union Minister of Power, Shri Manohar Lal. The underlying annual series is
  PFC's *Report on Performance of Power Utilities*; neither release names its source.
- **Finding**: the two releases give **different AT&C loss figures for the same financial
  year**. The December parliamentary answer: AT&C losses "reduced from 21.91% in FY 21 to
  **16.16% in FY25**". The January press release: AT&C losses "reduced from 22.62% in FY
  2013-14 to **15.04% in FY 2024-25**". FY25 and FY 2024-25 are the same year, and the gap
  is **1.12 percentage points**. This is not cosmetic. RDSS — the flagship distribution
  scheme, ₹2.83 lakh crore sanctioned per the December release — targets a pan-India AT&C
  band of **12–15%**. At 15.04% the scheme lands just outside its own target; at 16.16% it
  misses by more than a point. The lower number appears in the celebratory press release;
  the higher one was given under parliamentary answer six weeks earlier. Alongside it, the
  January release reports the sector's first positive bottom line in years: **PAT of
  +₹2,701 crore in FY 2024-25**, against **−₹25,553 crore in FY 2023-24** and **−₹67,962
  crore in FY 2013-14** — a ₹28,254 crore swing in a single year — and an ACS–ARR gap
  narrowing from ₹0.78/kWh (FY 2013-14) to **₹0.06/kWh (FY 2024-25)**.
- **Blog fit**: opens the confirmed zero-coverage **electricity distribution** area, and
  materially updates `discom-debt-relief-token-charge`, whose entire model rests on discoms
  *adding* ₹64,000 crore of debt a year — a premise a sector-wide positive PAT puts in
  question, or at least dates. Nearest published neighbours are
  `thermal-parity-is-dead-what-85-oil-and` (power economics reached through fuel prices) and
  `rooftop-solar-is-working-household` (the consumer end of distribution). Structurally it
  is the same move as `fourteen-years-of-indian-wholesale` and the WPI-rebasing work: take
  an official number everyone repeats and ask which official number.
- **Caveat**: five, and the first is the one that could kill the piece. (1) **The two
  releases may not have the same denominator.** Neither states which utilities it counts —
  all distribution utilities, only RDSS participants, discoms-plus-power-departments, or
  state-only. The January PAT sentence says "DISCOMs and power departments" explicitly; the
  December AT&C sentence says only "distribution utilities at the national level". If the
  coverage differs, the 1.12-point gap is a scope difference, not a contradiction, and the
  piece must say so — resolve this against the PFC report's utility count before writing
  anything. (2) **FY25 figures are almost certainly provisional.** PFC's own FY 2023-24
  edition covered 63 of 72 distribution utilities with 52 of 59 submitting audited accounts
  (trade-press figure, see WEAK below); an FY25 number published in Dec 2025 / Jan 2026
  cannot be more audited than that, and provisional numbers get revised. (3) **AT&C loss is
  a ratio, and ratios move for accounting reasons.** The same January release lists the
  *Electricity Distribution (Accounts and Additional Disclosure) Rules, 2025* and new
  subsidy-accounting rules among its achievements — changes to how subsidy is booked move
  ACS–ARR and AT&C without a single unit of stolen power being recovered. (4) **₹0.06/kWh
  is suspiciously round and is a national average** that hides state dispersion; do not
  narrate it as "cost recovery achieved". (5) The FY21 and FY 2013-14 baselines are
  different in the two releases, so the *trends* are not directly comparable either — only
  the FY25 endpoint is a like-for-like clash.
- Grade: **COMMISSIONABLE**. Logged 2026-09-09.

### Weak/off-scope, one line each (triaged, not deep-read)

- **PFC, *Report on Performance of Power Utilities* (2023-24 and 2024-25 editions)** — the
  underlying annual series for every figure above, and the primary this piece really wants.
  **Currently unreachable.** `pfcindia.com` now fails TLS (its certificate covers only
  `*.pfcindia.co.in`), and `pfcindia.co.in` has migrated to a React SPA that returns the
  same 2,322-byte JavaScript shell — HTTP 200, `text/html` — for *every* legacy
  `ensite/DocumentRepository/...` PDF path indexed by search engines, including the
  2024-25 edition, with a browser User-Agent and Referer set. The Wagtail CMS at
  `cms.pfcindia.co.in` serves documents from `/media/documents/`, but the site's own API
  routes (`/api/v2/data_listing/`, `/api/v2/search-page/`) 404 from outside the app. Not
  registered on trade-press figures alone. **Next attempt should drive the SPA in a browser
  to capture the real `cms.pfcindia.co.in/media/documents/` URL**, which is the one durable
  path — this is a retrieval problem, not a source problem, and the document is free.
- **Power Line Magazine, "PFC releases latest report... for 2023-24" (02 June 2025)** —
  fetched, and the only accessible account of the FY24 edition: AT&C **rose** 15.11% →
  16.12% between FY23 and FY24, billing efficiency 86.98% → 86.91%, collection efficiency
  97.6% → 96.51%, 63 of 72 utilities covered. Useful as corroboration that the series was
  *worsening* the year before both PIB releases claim improvement — but it is trade press
  summarising a document, so **cite the PFC report or nothing**. WEAK as a citation,
  valuable as a pointer.
- **PFC/MoP, *13th Annual Integrated Rating & Ranking of Power Distribution Utilities***
  (indexed at two `pfcindia.co.in` paths, one dated 18 06 2025) — the per-discom grading
  companion to the report above and the natural source for a state-by-state map in the
  blog's usual style. Same broken repository, so unverified; note it for the same browser
  attempt.
- **Dataful / FACTLY structured discom tables** — a third-party re-publication of PFC's
  numbers in clean form. Convenient, but it is a mirror of a government series; the standing
  rule applies. Never cite in place of PFC.

## Added 2026-10-01 (daily task, Thursday: seeds, plant variety rights and agricultural IP)

An empty day: nothing commissionable.
- **seednet.gov.in, retried.** It returned HTTP 503 again on `/`,
  `/Material/Seed_Production.htm` and `/PDFFILES/SRR.pdf` (curl with a browser UA). It
  stays NOT assessed; see the 2026-09-03 entry. Retry on a future Thursday.
- **PPV&FR homepage, re-fetched** (HTTP 200, 171,505 bytes). It still reads "10885
  Certificates issued as on 31.08.2026". No newer vintage, so nothing updates the
  published `577-of-indias-plant-variety` (2026-09-17).
- WEAK, one line each:
  - **IBEF blog, "India's Seed Reforms and Agricultural Productivity Growth in 2025-26".**
    Promotional summary; the SRR claims carry no dated table.
  - **IMPRI, "National Mission on High-Yielding Seeds (2025)".** Policy explainer with no
    primary dataset.
  - **Draft Seeds Bill 2025 explainers** (universalinstitutions.com, countercurrents.org,
    Deccan Herald). Already covered by `indias-draft-seeds-bill-cuts-states`
    (2026-09-10), and none is primary.
  - **EDV search.** It returned only FAQs and coaching pages restating the Act. The
    "General Guidelines Regarding the Registration of EDV" notice (2026-09-07 entry) is
    still the only primary EDV source.

## Added 2026-10-03 (daily task, Saturday: trade, tariffs and industrial policy)

An empty day: nothing commissionable. Dedup was run against the fuller mirror copy of this
register, because the source copy is truncated (see the Track C note in the 10-03 log).
- **DGCI&S, *Report of the committee on Base year Revision for Merchandise Trade Indices*
  (Feb 2026; `dgciskol.gov.in/writereaddata/Downloads/20260217171604Final Base Year Report
  2026.pdf`, HTTP 200, 3.6 MB, free).** This follows up the 2026-08-29 pending lead. The
  committee recommends **2022-23** as the new base for the Laspeyres unit-value indices,
  matching the NAD/MoSPI national-accounts base. 2020-21 and 2021-22 were excluded as COVID
  years. The common commodity basket used for base selection was 7,676 of 11,695 export
  HS-8 lines and 6,506 of 10,978 import lines. About 2% of unit values were imputed. The new
  series starts in April 2023 and is published alongside the 2012-13 series (both now run to
  Apr–Jun 2026), and it includes a separate Terms of Trade table
  (`TermsofTrade_202223.aspx`). **BACKGROUND.** This is a methodology report with no finding
  for readers in it. The one possible story, terms of trade re-stated on the new base, sits
  behind an ASP.NET postback link (a 15 KB "Apr26_Jun26" file) that curl could not reach. A
  title grep of the manifest (342 posts) finds no post on terms of trade or unit-value indices,
  so a browser pull of the two-base ToT files could open a small new angle. Retry on a future
  Saturday with a browser.
- **August 2026 merchandise trade headline** (exports +26.12% YoY to USD 43.81 bn, imports
  USD 70.76 bn, merchandise deficit USD 26.86 bn). All of these came from press only
  (ThePrint, UNI, Asianet) and the PIB primary was not fetched. It is a routine monthly
  print, so WEAK.

## Added 2026-10-05 (daily task, Monday: agricultural labour and rural incomes)

An empty day. Nothing commissionable and nothing queued.
- **PLFS Monthly Bulletin, August 2026** (NSO/MoSPI, released 15 Sep 2026). BACKGROUND.
  Rural LFPR was 58.2% (+1.2pp YoY), rural WPR 55.8% (+1.3pp YoY) and rural UR 4.1%, down
  from 4.5% in July and the lowest since Jan 2026. These figures come from the PolicyEdge
  summary; the MoSPI press-note PDF returned 502 to WebFetch and HTML to curl. Checked as
  a possible update to the open queue item "Rural India's fastest quarter off the farm":
  it does **not** update it. The monthly bulletin gives no industry or employment-status
  split, so agriculture's share stays a quarterly-only number. The Jul–Sep 2026 Quarterly
  Bulletin (due about mid-Nov) is the update to watch for.
- **AERR, "Agricultural wages in India: trends and determinants"**
  (`epubs.icar.org.in/index.php/AERR/article/view/140527`). WEAK by dedup: already logged
  at SOURCE_REGISTER.md:877.

## Added 2026-10-07 (daily task, Tuesday: insurance, reinsurance and financial plumbing)

### IFSCA Bulletin, Q1 FY 2026–27 (Apr–Jun 2026) — materially updates a published post

- **Source:** *IFSCA Bulletin, Q1 FY 2026–27 (Apr–Jun 2026)*, International Financial
  Services Centres Authority, Division of Economic Policy and Analysis.
  `ifsca.gov.in/Document/IFSCA_Bulletin.pdf` (a rolling URL that serves the latest edition).
  Fetched 2026-10-07: HTTP 200, 14.6 MB, 72 pp; `pdftotext -layout` extracts cleanly. Free,
  no login.
- **Data:** the insurance tables have been renumbered since the Jan–Mar 2025 edition.
  - **Table 43:** IIO/IIIO counts.
  - **Table 44:** written/transacted premium by IIOs and IIIOs.
  - **Table 45:** direct insurance by class.
  - **Table 46:** reinsurance by class.
  - **Table 47:** claims.
  - All are quarterly for Q1–Q4 FY 2025–26 plus Q1 FY 2026–27, with an FY 2025–26 total.
    Footnoted "Unaudited data".
- **Finding (my sums tie to the printed FY totals):**
  - **FY 2025–26:** direct GWP **USD 40.72 Mn** against reinsurance **USD 607.96 Mn**, so
    reinsurance is **93.7%** of the IIO book (FY 2024–25: 94.0%). The *share* thesis holds.
  - The *levels* do not:
    - Direct cover is 3.3× the USD 12.42 Mn the post headlines.
    - Direct **life** went from USD 2.54 Mn to **19.43 Mn** in FY26, and **13.25 Mn in Q1
      FY27 alone**.
    - Reinsurance went from 195.45 to 607.96 (3.1×).
    - Q1 FY27 reinsurance was **USD 400.30 Mn**, two-thirds of all of FY26 in one quarter.
      The jump comes mostly from reinsurance Life (0.8 → 96.66) and Trade Credit
      (0.2 → 42.55), which look like single large treaties.
  - IIOs: 36 → 37 (23 of them reinsurers). Outstanding claims rose from USD 173.94 Mn to
    195.67 Mn.
- **Blog fit:** a correction/update to `india-built-offshore-insurance-hub-it` (published
  2026-09-18). That post uses FY 2024–25 figures only (grep: "12.42" ×5, "195.45" ×4,
  "2024-25" ×8, no FY26 figure). Its headline "$12 Million of Direct Cover a Year" is now a
  year stale. Labels: Insurance & Reinsurance; Markets & Finance.
- **Caveats:**
  1. Unaudited, and the disclaimer warns that figures may be revised for reclassification.
  2. Q1 FY27 lumpiness. Do not annualise 400.30.
  3. Crop reinsurance prints −11.5 in Q4 FY26 and Marine Cargo direct −0.01 in Q3:
     reversals, not business written.
  4. The old "Health + PA vs separate Health line" puzzle (the post's check 3) does not
     appear here. FY26 has one Health + PA row in both tables, so it was a reclassification.
  5. 🔴 The trade-press figure "USD 102 Mn (2020) → >USD 1.2 Bn (2025)" (Reinsurance News,
     via search snippet; the page returned 403) is probably IIO written premium plus IIIO
     *transacted* premium (FY26: 648.68 + 481.36 = 1,130.04). Intermediated premium is not
     underwritten in the IFSC. Never add the two.

### Weak/off-scope, one line each (triaged, not deep-read)

- **Reinsurance News, "GIFT IFSC continues rapid growth as registrations and (re)insurance
  activity rise"** (Q4 FY26 bulletin write-up). Returned 403 to WebFetch and a Cloudflare
  stub to curl, so it was not read. Secondary anyway; the primary bulletin above supersedes
  it.

## Added 2026-10-09 (daily task, Thursday: seeds, plant variety rights and agricultural IP)

**Step 1 paid off again, the same way it did on 2026-10-07.** The open queue item "57.8% of
India's plant-variety rights are cereals. Spices get 151." was **published on 2026-09-17** as
`577-of-indias-plant-variety` (manifest, 346 posts, snapshot 2026-10-07; labels Agriculture &
Fertilisers · Seeds & Plant Genetics), but its `- [ ]` box was never ticked. The manifest now
carries four posts under `Seeds & Plant Genetics` (`indias-draft-seeds-bill-cuts-states`
2026-09-10, `577-of-indias-plant-variety` 2026-09-17, `indias-cotton-yield-fell-from-566-kg-to`
2026-09-27), so "zero coverage" no longer describes the area; the dedup bar is now ordinary.
Manifest grep for replacement rate / SRR / certified seed / quality seed / pulses: **zero hits**.

### PPV&FR Authority homepage, as on 30.09.2026 — a new vintage, and the homepage's three series no longer agree with each other

`https://plantauthority.gov.in/` returned HTTP 200, 173,092 bytes, browser UA, direct curl.

- **Data (crop groups).** This month the crop counts are plain `<h3>` literals in the HTML
  boxes, headed "**10981 Certificates issued as on 30.09.2026**": Cereals **6,324** · Fibre
  1,014 · Vegetables 1,394 · Legumes 882 · Oilseeds 581 · Fruits 440 · **Spices 151** · Sugar
  94 · Trees 50 · Flowers 39 · and two boxes both captioned "Plantation crop" showing 7 and 5
  (the link targets are Cash and Medicinal & Aromatic plants; the alt text is identical, so
  which is which cannot be read off the page). The twelve boxes sum to exactly 10,981.
- **Finding 1 — the published headline survives on the newer vintage, with one digit moving.**
  Cereals are **57.6%** (6,324 of 10,981); the post says 57.7% (6,280 of 10,885 as on
  31.08.2026). Month on month: +96 certificates = cereals +44, fruits +11, legumes +10,
  vegetables +8, fibre +8, oilseeds +4, sugar +1, other +10 (the 31.08 "Other" was 242; the
  five small boxes now sum to 252). It reconciles exactly against the 31.08 capture.
  **Spices are still 151** — zero new spice certificates since 31.07.2026 while the register
  added 179. The homepage breaks spices out again, so the 2026-09-07 caveat ("do not expect to
  re-fetch it") is lifted for now.
- **Finding 2 — 🔴 the registration-type pie and the year-wise line were NOT updated.** The
  pie literal in the page JavaScript is unchanged from 31.08: Extant Notified 2,025 · Extant
  VCK 1,557 · **Farmer 5,368** · New 1,921 · **EDV 14**, summing to 10,885. The year-wise
  series also sums to 10,885. So the homepage currently mixes a 30.09 crop count with 31.08
  type and year series. **Do not recompute the farmer share against 10,981** — it would print
  48.9% for no reason. The post's 49.3% as on 31.08.2026 stands, and must keep its date.
- **Finding 3 — new, quantified, and not in the published post.** The year-wise series
  (certificates issued, as on 31.08.2026) reads: 2009 168 · 2010 49 · 2011 116 · 2012 212 ·
  2013 304 · 2014 833 · 2015 385 · 2016 606 · 2017 371 · 2018 477 · 2019 395 · 2020 424 ·
  2021 508 · 2022 265 · **2023 1,259 · 2024 2,017 · 2025 2,073** · 2026 (to Aug) 423.
  **2023–2025 = 5,349 = 49.1% of every certificate issued since 2009.** 2024 and 2025 each
  issued more than the first five years (2009–13: 849) combined. A grep of the published post
  for 1,259 / 2,017 / 2,073 / 2009 returns nothing, so the surge is unreported. It is
  consistent with the search-result snippet seen on 2026-10-01 ("registration got a boost in
  2023–25, about half of total registrations", on a 9,210 base) — now from the primary.
- **Blog fit.** (a) An update box on `577-of-indias-plant-variety` (new vintage; spices still
  151; the stale-chart caveat). (b) A **COMMISSIONABLE** follow-on: "half of India's
  plant-variety certificates were issued in the last three years". Nearest posts:
  `577-of-indias-plant-variety`, `indias-draft-seeds-bill-cuts-states`.
- **Caveat.** HTML and chart literals with no schema; the three series are now at two
  vintages; the "Plantation crop" alt-text collision; host intermittent (200 today, 503 on
  2026-09-03). 🔴 For the surge piece: certificates issued ≠ applications filed. A 2023–25
  jump can be a backlog clearance as easily as a filing boom. The Annual Report's application
  series (and, if possible, which registration type drove it — farmer vs new) has to be read
  before anyone writes "breeding activity doubled". The 2022 trough (265) is the other thing
  to explain.

### data.gov.in — State/UT-wise Seed Replacement Rate (SRR) of important crops, 2019 to 2021 — BACKGROUND, data not read

- **Source.** Resource `11af01f5-6f54-4f7d-ab1c-d279aff4bdc0` in catalog "Answers Data of Rajya
  Sabha Questions Session 259", published 30/10/2023. Page note: "Source - RAJYA SABHA
  SESSION - 259 UNSTARRED QUESTION No 2742. ANSWERED ON, 24th March 2023. Data Figures are in
  Percentage. NA - Not Available." Sector: Agriculture. Reference URL:
  sansad.in/rs/questions/questions-and-answers.
- **Data.** CSV, 5,255 bytes; fields: State/UT, Year, Wheat, Paddy (Variety / Hybrid), Maize
  (V/H), Jowar (V/H), Bajra (V/H), Gram, Peas, Lentil, Urd, Moong, Arhar, Groundnut, R/M
  (rapeseed-mustard), Soyabean, Sunflower (V/H), Cotton … Years 2019–2021. API available.
- **Access today: failed on every path, so no number is claimed.** The resource page itself
  came back with curl (1.0 MB, metadata read from the Nuxt state). The CSV returned 403 on
  `files/ogdpv2dms/s3fs-public/…`, redirected to `page_not_found` on `system/files/2023-10/…`,
  the API host refused the TLS handshake from this Mac, WebFetch got 403 / socket closed, and
  the built-in browser was denied the API host. Obtainable from a registered data.gov.in
  account, or from the RS answer annexure on sansad.in (the memory file holds the LS question
  endpoint, not the RS one).
- **Blog fit.** Would open the seed-*quality* half of the Thursday area, which the three
  published seed posts (IP, bill, cotton yield) do not touch: SRR by state × crop, with
  hybrid vs variety split for paddy/maize/jowar/bajra/sunflower. Zero manifest hits.
- **Caveat.** State-reported percentages in a PQ answer; 2019–2021 vintage; the SRR concept
  itself is contested (IIMA working paper, "Seed Replacement Rate: Some Methodological Issues",
  seen in search results only, not fetched). Re-grade once the table is read.

### Weak / background — one line each (triaged, not deep-read)

- **seednet.gov.in** — HTTP 503 on `/`, `/Material/Seed_Production.htm` and `/PDFFILES/SRR.pdf`
  for the third Thursday running (2026-09-03, 10-01, 10-09). Still NOT assessed. Stop
  spending a retry on it every week; try once a month.
- **ICAR-NAARM, "Enhancing the Availability of Quality Seed and Planting Material"**
  (naarm.org.in, Nov 2025, 3-page PDF, fetched). Policy essay: Seeds Act 1966 → PPV&FR Act
  2001 → draft Seeds Bill; "SRR for wheat, rice and maize has risen steadily" with no table,
  no year, no state. BACKGROUND.
- **Chauhan, Singh & Gupta, "Enhancing pulses production in India through improving seed and
  variety replacement rates", Indian J. Genetics & Plant Breeding 76(4), 2016** (epubs ICAR,
  abstract fetched; PDF open at `article/view/67292/28784`). Seed chain of six pulses kept
  with 236 varieties, 44 of them doing the work; 39.38 and 46.87 lakh q quality seed needed in
  2020 and 2025. Useful as the method reference distinguishing seed-replacement from
  variety-replacement rate, but 2016 vintage with projections now in the past. BACKGROUND.
- **PPV&FR Annual Report search** returned only the 2023-24 PDF and older; no 2024-25 PDF
  surfaced in search today (the published post cites one — not re-verified). Not fetched.

## Added 2026-10-12 (daily task, Monday: agricultural labour and rural incomes)

An empty day. Nothing commissionable and nothing queued.

### Lok Sabha reply on MGNREGS average workdays, FY26 — BACKGROUND (primary not read)

- **Source seen:** PTI via Deccan Chronicle (updated 28 Jul 2026) reporting a starred-question reply by the Rural Development Minister: average workdays per household fell from **50 (2024-25) to 43 (2025-26)**, a decade low; **24** till June 2026; series range 38 (2008-09) to 52 (2020-21 and 2023-24). Central allocation for 1 Jul 2026–31 Mar 2027 is Rs 95,692.31 crore (outlay with state share above Rs 1.51 lakh crore).
- **Data:** the underlying Lok Sabha reply (sansad.in) is the primary, free. I did not fetch it; the question number and sitting date are not in the article.
- **Blog fit:** extends `a-17-rural-pay-rise-that-nobody-received`, which covers the repeal and early VB-G RAM G person-days but explicitly held back on the scheme's performance. The FY26 workdays series is a legacy-scheme figure, not a VB-G RAM G one.
- **Caveat:** secondary source only; the "households completing 100 days fell 40.5%" figure comes from a campaign group (NREGA Sangharsh Morcha) via Down To Earth, not read. Fetch the reply before any queue entry.

### Weak, one line each
- **Dataful MGNREGA dataset pages (20047/20048/24237/24239)** surfaced in search: paywalled aggregator listings, not read. WEAK.

## Added 2026-10-13 (daily task, Tuesday: insurance, reinsurance and financial plumbing)

### IRDAI Annual Report 2024-25 — grievances and claims chapter — BACKGROUND (primary PDF not read)

- **Source seen:** IRDAI document page irdai.gov.in/document-detail?documentId=8375620 (12.2 MB PDF, free; listing shows updated 30-12-2025). Figures below come only from Outlook Money's write-up (updated 2 Jan 2026), not the PDF.
- **Data:** Bima Bharosa grievances 2,57,790 (life 1,20,429; general+health 1,37,361); claim-related 33,280 life (vs 26.68 lakh claims) and 88,841 general+health (vs 11.26 crore claims); life mis-selling complaints 23,335 -> 26,667 (19.33% -> 22.14%).
- **Blog fit:** extends the insurance beat; nearest posts `premium-now-claim-later-float-indias`, `india-built-offshore-insurance-hub-it`. Manifest grep for repudiat/ombudsman/bima bharosa found no insurance post covering claims or grievances.
- **Caveat:** secondary article contradicts itself on the life claims count (2.66 million vs 26.68 lakh); search snippets conflict on whether 1,37,361 is health-only. Ombudsman 53,184 vs 53,102 also disputed. Read the PDF chapter before any use. Could be promoted to COMMISSIONABLE once the primary is read.

## Added 2026-10-24 (daily task, Saturday: trade, tariffs and industrial policy; reduced budget)

Reduced budget today (triage 1, deep-read 0) because Track A ran long. **The manifest dedup could not be run.** This session has no Grep tool, and the 406-post manifest is too large to read whole. So nothing below can be graded COMMISSIONABLE, by rule.

### Weak, one line each
- **Commerce Ministry monthly trade release, Sep 2026 (15 Oct 2026)**, seen only via press (Business Today, Deccan Chronicle, devdiscourse). Exports $44.40 bn (+23% y/y), imports $74.61 bn, deficit $30.21 bn; Apr–Sep exports $259.89 bn; gold imports down to $1.8 bn. One outlet (indiaseatradenews) prints conflicting figures ($34.58 bn exports, $20.78 bn deficit), possibly an older month. The PIB primary was not fetched. This is a routine monthly headline on the blog's heaviest beat. WEAK unless a later run finds it contradicts a published post.

## Added 2026-10-29 (daily task, Thursday even week: fertiliser, coal-to-urea and chemicals import substitution)

Dedup run with `repo_read.sh localgrep` over `meta/manifest.json` and `posts/`. Fertiliser is a thin but real beat: the manifest carries `indias-fertiliser-import-bill-hits-18`, `indias-subsidised-imports-fertilisers`, `nature-versus-nurture-indias-fertiliser`, `thirty-one-years-of-asking-parliament`, `nano-urea-works-as-supplement-and-fails`, `how-to-use-coal-to-urea-design`, `indias-fertiliser-sales-fell-where`, `379-kilos-hectare-in-punjab-44-in` and `bio-fertiliser-and-green-credits`. Three WebSearches; two PRS Legislative Research summaries fetched in full; the eparlib primary PDF returned no content to fetch_source.sh today. Open COMMISSION_QUEUE items were re-read: none gained a newer source today, and the coal-gasification Round III item stays on hold.

### Commissionable

**Standing Committee on Chemicals and Fertilisers (chair Azad Kirti Jha), report "Alignment of Logistics for Efficient Fertiliser Movement and Availability at Affordable Prices during Peak Season and Steps Taken to Curb Forced Bundling of Unnecessary Boosters with Essential Fertilisers", presented 6 Aug 2026** — read via the PRS summary (prsindia.org, fetched 2026-10-29). Report number not on the page. Primary PDF on eparlib.sansad.in not fetched: the host returned no content today.
- **Data:** the committee report (free PDF on eparlib or sansad.in once reachable); RFCL's filed annual accounts for the loss; Department of Fertilizers plant-wise production for utilisation.
- **Finding:** Ramagundam Fertilizers and Chemicals Ltd, the first of the five revived FCIL/HFCL plants to run, has an estimated revenue loss of **Rs 7,954 crore between 2021-22 and November 2025**, attributed to recurring technology failure. DAP plant capacity utilisation fell from **87.5% in 2022-23 to 67.8%** in the first ten months of 2025-26. "Several" new-generation urea plants run significantly below capacity (no figure on the page). Fertiliser moves between distant states when nearer sources exist, inflating the freight subsidy, and the Department had not costed it. Recommendations: amend the Fertiliser (Control) Order 1985 to prohibit forced bundling with penalties; separate digital billing of non-subsidised products in the iFMS; a permanent joint command cell of DoF, DA&FW, Railways and states; performance guarantees and warranty obligations in future technology transfers.
- **Blog fit:** this is the first official answer to a proposal the blog has made twice. `thirty-one-years-of-asking-parliament` asks DoF to "publish plant-wise production and capacity utilisation each year for the revived Talcher, Ramagundam, Gorakhpur, Sindri and Barauni units", and `textbooks-say-project-returns-converge` asks for "plant-wise urea capacity utilisation every year". It also qualifies `nature-versus-nurture-indias-fertiliser`, whose plant table lists Ramagundam 12.7 LTPA as "Operational (RFCL)" with no caveat, and extends `the-reactor-nobody-names-how-coal` (technology dependence) from Talcher's gasifier to the gas-based revival. The forced-bundling half is the weaker angle: `nano-urea-works-as-supplement-and-fails` already covers the 13 Mar 2026 FCO amendment on tagged sales. Posts dedup: `Ramagundam` appears in 3 posts (two tables, one pipeline map); no post carries the Rs 7,954 crore figure or DAP utilisation, and every `[Cc]apacity utili` hit is ethanol, LNG, pipelines, steel, CBG or a proposal asking for the fertiliser number.
- **Caveat:** (1) "revenue loss" is the committee's phrase as relayed by PRS; whether it is foregone revenue at nameplate or an accounting loss, and against which capacity, must come from the report and RFCL's accounts before the figure is printed; (2) 67.8% is ten months of 2025-26, not a year; (3) the primary was not fetched today, so fetch it and cite paragraph numbers, do not write from PRS alone; (4) "several new-generation plants below capacity" has no number on the page, so get the plant-wise table from the report or a Lok Sabha answer.
→ queued in COMMISSION_QUEUE.

### Background only

- **Standing Committee on Chemicals and Fertilisers, 15th Report (18th Lok Sabha), "Self-Sufficiency in Production of Fertilisers with a View to Curb Import of Fertilisers – Review of Constraints Thereof"**, presented 1 Dec 2025 per PRS (a search snippet of the eparlib cover says laid in the Rajya Sabha 21 Aug 2025 and presented to the Speaker 4 Oct 2025, a date discrepancy to settle from the primary). PRS summary fetched; the eparlib PDF `18_Chemicals_And_Fertilizers_15.pdf` returned no content today. Figures: natural gas is 90% of urea cost and only 26% of it is domestic; India imports 95% of phosphate and 100% of potash; **of 33 operational urea plants, 27 are older than 25 years and 7 older than 50**; recommends two task forces (urea under the New Investment Policy; ageing plants), a drone PLI for nano-fertiliser spraying, and assessing an extension of the urea subsidy scheme beyond 31 Mar 2025. The blog's `indias-fertiliser-import-bill-hits-18` already rests on this committee's 90%-gas finding (manifest note), so the report as such is covered. The plant-age finding is not: `50 years` in posts matches only a constitution piece and SASCI loans. "Seven of India's 33 urea plants are older than 50 years" is a possible piece once the PDF's plant list is in hand. BACKGROUND until the primary is fetched.
- **Action-taken report on the above, presented in the Lok Sabha on Monday 27 Jul 2026** — seen only through The Pioneer (28 Jul 2026, fetched) and a Vision IAS digest; not located on eparlib. Department replies as quoted: urea production 307 lakh t against consumption 388 lakh t in 2024-25; imports **above 100 lakh t in FY 2025-26**; demand projected at 444 lakh t by 2035-36; Talcher "under execution", with 63.5 lakh tpa to be added across the five revivals; a new 12.7 lakh tpa Namrup plant approved and its JV signed; the committee urges reviving Durgapur, Haldia and Korba and the Department defers until the gap is clearer. None of the volume figures appear in posts (`307 lakh` → 0 hits). Press-only today, so BACKGROUND; it is the natural dated update box for `thirty-one-years-of-asking-parliament`, which ends on exactly this question.

### Weak, one line each

- **ICRA special comment on the fertiliser sector (icra.in download, 2026)** — rating-agency note, not fetched, seen only as a search hit. WEAK under the vendor-research rule; cite the committee instead.
- **Vision IAS, Vajiram and Chanakya Mandal digests on coal gasification and the fertiliser sector** — tertiary coaching material, not sources. Not logged further.

## Added 2026-10-30 (daily task, Friday even week: city gas, CGD and refinery economics)

Dedup run with `repo_read.sh localgrep` over `meta/manifest.json`. PNGRB is a heavy beat: `pngrb-hydrogen-blending-pilots-real`, `pngrbs-own-committee-found-pipelines`, `pngrb-wants-prepaid-smart-meters-on`, `pngrb-graded-its-own-homework-on-2025`, `pngrbs-own-2025-committee-now-expects`, the Aug-2026 pipeline-map post and "City Gas Just Became India's Largest Gas Consumer". So the bar today was "a figure in the regulator's own statistical report that no post carries". `[Cc]omplaint` returns 0 hits in the manifest; `[Uu]nified` returns only the RBI UMI and ABHA posts; `MMBTU` returns only the GOBARdhan CBG price. Two WebSearches (PNGRB/CGD; PPAC refinery margins). One fetch_source.sh call, OK. The refinery-margin search returned company results and rating-agency notes citing PPAC, never a PPAC table, so that half of the beat was not pursued. Open COMMISSION_QUEUE items re-read: the coal-gasification Round III item stays on hold; nothing else gained a newer source today.

### Commissionable

**PNGRB, Annual Statistical Report 2025-26 (Statistics Division, Petroleum and Natural Gas Regulatory Board; foreword dated 28 September 2026; described in its introduction as the "Maiden" edition)** — free PDF, no login, `pngrb.gov.in/pdf/e-publication/20260930_PNGRB_Statistical_Booklet.pdf`, fetched in full via fetch_source.sh (376,762 chars of text; Chapters I, VII, IX and X read; the rest skimmed from the contents page).
- **Data:** ten chapters of entity- and GA-level tables as on 31.03.2026, "as submitted by entities" with PPAC as the other named source. Chapter X (pp. 70–76): Tables 10.1–10.6, complaints and resolutions by segment (PNG, CNG), by month, and for the top ten entities, with a four-band entity classification. Chapter IX (pp. 67–69): Tables 9.1–9.6, unified tariff zones and rates. Chapter VII (pp. 54–59): Table 7.4 CBG plant connectivity, 7.5 offtake mode, 7.6 monthly CBG sales, 7.7 top ten entities by CBG sales and blending %. Chapter II: CGD performance grading of every GA against pro-rata minimum-work-programme targets. Monthly backing data is the CGD MIS report series on the same site.
- **Finding (lead, Chapter X):** 19,36,409 complaints were recorded across the 307 GAs in FY 2025–26 and 11,43,489 were resolved, **59.05%**. PNG is 98.5% of the volume and resolves **58.6%** (19,07,757 received, 11,17,767 resolved); CNG resolves 89.8% (28,652 / 25,722). The monthly PNG resolution rate fell from a peak of 68.5% in July 2025 to **48.9% in February 2026** and 51.9% in March, while monthly PNG complaints received rose from 93,422 in April 2025 to 2,20,985 in March 2026 (+136.5%). The entity spread on PNG runs from **Green Gas 20.5%**, Indian Oil Adani Gas 24.7%, Mahanagar Gas 32.9% and GAIL India 34.3% up to Megha City Gas 97.5%; Indraprastha Gas carries 5,92,014 complaints, 31% of the national total, at 62.9%. The chapter's own bands put three of the ten largest PNG entities in "Critical" (below 50%). **The reading that matters:** Table 10.2's column is "Complaints Received (including carry forward)", so the monthly series is a stock, not a flow, and the 19.36 lakh annual total appears to be the sum of twelve monthly stocks. An unresolved complaint is then counted again in every month it stays open, a falling resolution rate alongside a rising count is what an accumulating backlog looks like, and the true number of distinct complaints is smaller than the headline. The booklet does not say this; it is a plain reading of the column header.
- **Finding (second, Chapter IX):** the Unified Tariff went from three zones to two with effect from July 2025 (Zone 1 up to 300 km, Zone 2 beyond; the old Zone 3 beyond 1,200 km discontinued). For January–March 2026: Zone 1 ₹54.00/MMBTU, Zone 2 ₹102.86, levelised ₹83.94. CNG and PNG-Domestic are charged Zone 1 wherever they sit, which the report prices at ₹48.86/MMBTU less than Zone 2 beyond 300 km, and PNGRB estimates the reform cuts CGD transportation cost by about ₹1,000 crore a year, ₹1.25–2.50/kg on CNG and ₹0.90–1.80/SCM on PNG-D.
- **Finding (third, Chapter VII, an update):** 207 functional CBG plants, **24 connected to a pipeline (11.6%)**, 15 in progress, 20 proposed, 148 (71.5%) with no connectivity planned; of 328 plants under construction, 2 are connected and 257 (78.4%) have none planned. Reported offtake (74 plants) is 65.7% cascade, 25.4% standalone, 8.9% pipeline. CBG sales 120.29 MMSCM, blending 0.998% against the 1% obligation; monthly sales 0.211 → 0.620 MMSCMD April to March; top five entities 52.66% of CBG sales. The obligation rises to 3%, 4%, 5% over FY27–FY29.
- **Blog fit:** Chapter X opens consumer grievance redressal, which has zero coverage, and is the natural sibling of `pngrb-graded-its-own-homework-on-2025` (Ombudsman unstaffed five months after the Consumer Protection Regulations; billing compliance 49%): that post is about the regulator's machinery, this is about the complaints the machinery is for. Chapter IX has no post at all and pairs with `pngrbs-own-committee-found-pipelines` as the price side of under-used pipelines. Chapter VII materially updates `india-has-132-compressed-biogas-plants` (2026-09-23, from the September ATR: 132 plants commissioned, 17 pipeline-connected): the regulator's own year-end count is 207 functional and 24 connected, and it adds the offtake-mode split and the "no connectivity planned" share the ATR did not have.
- **Caveat:** (1) 🔴 the carry-forward reading above must be confirmed, from PNGRB's definition or by reconciling Table 10.2 against the monthly CGD MIS reports, before "19.36 lakh complaints" is printed; if the total is distinct complaints after all, the piece is about resolution rates, not volume; (2) "resolved" is undefined in the chapter and the data are entity-submitted, so an entity's rate can reflect its closure practice as much as its service; (3) complaints per connection is the fair comparator across entities (IGL's 5.92 lakh sits on the largest base) and the booklet does not compute it, so the piece has to, from Chapter II's state/entity connection tables; (4) the ₹1,000 crore tariff saving is PNGRB's own estimate, not a measured outcome; (5) the PDF's text layer duplicates and interleaves lines on several pages (the Chapter X introduction appears three times), so take every figure from the rendered table, not the extracted text; (6) Chapter I's "DPNG achievement 41% of pro-rata target" and "billed/connected ~63%" are different denominators from the ATR post's "billing compliance 49%" and must not be run together.
→ queued in COMMISSION_QUEUE (the grievance piece), with update notes for the CBG post and a tariff follow-on.

### Background only

- **PNGRB CGD MIS Report, March 2026** (`pngrb.gov.in/data-bank/20260331-CGD-MIS-Report.pdf`) — the monthly GA-level series behind the booklet; the blog already used the August 2026 edition for the pipeline-map post. Not fetched today. It is the source for check (1) above.

### Weak, one line each

- **CareEdge note on OMC gross refining margins, ICRA refinery research summary, Baroda BNP Paribas and other broker result reviews (IOCL Q3 FY26 GRM $12.2/bbl, utilisation 110%)** — rating-agency and broker material that cites PPAC; WEAK under the vendor rule, and the PPAC refinery table itself did not surface in search. Fetch PPAC's monthly refinery pages directly if the refinery half of this beat is ever picked up.
- **Fortune Business Insights and vestai.io "city gas distribution market" reports** — vendor market sizing, WEAK by rule.
- **LatestLY / AngelOne items on PNGRB asking CGD entities for 30,000 PNG connections a day (April 2026)** — press of a regulator statement; the booklet's own figure is 19.08 lakh domestic connections added in FY26, about 5,200 a day, which is the primary number to cite against that target.

## Added 2026-10-31 (daily task, Saturday even week: Gulf/DACH/India trade corridors)

Dedup run with `repo_read.sh localgrep` over `meta/manifest.json`, one term per call: `UAE` matches one post note (the crypto-settled FDI and UAE stablecoin-pilot post); `Emirates` and `Dubai` return 0; `CEPA` matches only the stale-fact-sweep notes ("UK CETA + Oman CEPA now in force"), no title; `TEPA` matches the title "What TEPA Actually Opens: EFTA Goods, India's Real Numbers, and Where Domestic Manufacturing Needs to Catch Up"; `German` matches only an instrument note on the global inflation post; `[Ss]wi[st][sz]` returns 0; `Gulf` matches the Hormuz/IMEC post note and the title "South Africa Lost Its Gulf Fuel Supply. It Turned to America, Not India." So the Gulf corridor is covered from the energy and payments side, Switzerland from the TEPA side, and Germany–India goods trade not at all. Three WebSearches (UAE CEPA; Destatis/Germany; Swiss customs/TEPA year one). Two pages fetched in full (GTAI, Deccan Chronicle); the WAM article returned only its masthead. Open COMMISSION_QUEUE items re-read: none gained a newer source today; the coal-gasification Round III item stays on hold.

### Commissionable

**Germany Trade & Invest (GTAI, the federal foreign-trade agency), "Deutsch-indischer Handel" country page, Florian Wenke, Mumbai, dated 05.06.2026, citing Destatis 2026 provisional data for calendar 2025** — fetched in full.
- **Data:** the page tabulates Destatis's bilateral goods trade by SITC product group in US$, marked provisional with rounding differences. The underlying primary is Destatis GENESIS-Online (foreign trade by country and product, table family 51000, free, EUR), which the blog can pull directly; the GTAI page is the secondary that already did the product cut.
- **Finding:** Germany–India goods trade was US$35.4 bn in 2025, +6%. German exports to India US$18.4 bn, **+0.6%**; German imports from India US$16.95 bn, **+12.5%**. Germany's surplus with India was "about US$1.5 billion, less than half the prior year's figure". Inside that: German machinery exports to India +5.2% to US$5.24 bn, but Indian machinery exports to Germany **+23.9% to US$2.26 bn**; Indian clothing +19.7% (US$2.0 bn), food +21.3% (US$1.03 bn), chemicals +9.5% (US$3.38 bn, the largest import line); Indian refined-fuel sales to Germany from about US$283 mn to just over US$498 mn. On the German export side aircraft fell 17.1% and road vehicles 22.3%. India ranked 21st as a German export market and 22nd as a supplier. The counter-intuitive line is that the corridor is usually written as German machinery flowing to India; in 2025 the growth was Indian machinery, clothing and chemicals flowing to Germany, and the German surplus more than halved.
- **Blog fit:** opens Germany–India goods trade, which has no post (manifest above), on a blog named for the corridor. Nearest published posts: the TEPA piece (Switzerland/EFTA goods) and `half-of-indias-import-bill-is`. Pairs with the India–EU FTA framing in the Hormuz/IMEC post.
- **Caveat:** (1) provisional Destatis figures; final 2025 data and the 2024 surplus comparison must come from GENESIS, not this page; (2) GTAI converts to US$, Destatis publishes EUR, so the growth rates carry an exchange-rate effect and the piece should quote EUR from the primary; (3) the "+44.5%" line for vegetables, fruit, seafood, rice and coffee is ambiguous on the page (whole food group or those items); (4) DGCI&S will show a different bilateral total (CIF/FOB, fiscal year, re-exports via Rotterdam/Antwerp), so do not splice the two sources in one table; (5) the VDMA +8.5% Q1 2026 figure is an industry body, not statistics.
→ queued in COMMISSION_QUEUE.

### Background only

- **India–UAE bilateral trade FY 2025-26: US$101.25 bn (FY25: 100.03), exports US$37.36 bn (+~2%), imports US$63.89 bn (+0.77%), deficit US$26.53 bn; UAE FDI US$2.45 bn Apr–Dec FY26 vs 4.34 bn FY25** — Deccan Chronicle, 1 May 2026, fetched in full; source is a social-media post by the Commerce Minister, not a PIB release or a DGCI&S table. The article has no non-oil or non-precious-metals figure, no oil or gold share and no target. Search snippets (not fetched) put the CEPA goal at US$100 bn of non-oil, non-precious-metals trade by 2030 and H1-2025 non-oil trade at US$37.6 bn (UAE minister via WAM; the WAM page could not be read today). The piece that would exist here is a reconstruction: how much of the "US$100 bn milestone" is crude, LNG, gold and diamonds, from TradeStat HS2 lines, against the target's own definition. BACKGROUND until the DGCI&S split is pulled; nothing queued.
- **TEPA year one, press only:** India's exports to Switzerland above US$1.2 bn in FY 2025-26 and exports to EFTA down about 10.8% in FY26 (search snippets from IANS/Drishti coverage of the 8 May 2026 review and the 7 Oct 2026 Prosperity Summit; not fetched). If confirmed from DGCI&S, that is a dated update box for the published TEPA post, which argued from pre-agreement numbers. BACKGROUND, unverified.

### Weak, one line each

- **IMC Switzerland–Liechtenstein Monthly Economic & Commercial Report, May 2026 (imcnet.org PDF)** — chamber document citing Swiss customs for one provisional month (exports 370, imports 222, US$ mn). Not a series; pull Swiss-Impex directly instead. WEAK.
- **PwC Switzerland TEPA explainer pages, Statista Germany–India charts, trade.gov.tr relay of the Destatis June 2026 release** — vendor or tertiary; the Destatis monthly release itself has no India breakdown. WEAK.
- **GulfNews / Khaleej Times / Arabian Business items on UIBC-UC CEPA studies and "US$37.6 bn H1 2025 non-oil trade"** — press of ministerial statements and a business-council study; the FCSC release behind them did not surface. WEAK until the FCSC table is fetched.

## Added 2026-11-10 (daily task, Tuesday even week: carbon markets and compliance)

Dedup with `repo_read.sh localgrep` over `meta/manifest.json`: `CBAM` matches several titles, including the Indian steel post ("To Comply or Not to Comply: CBAM Costs Indian Steel €93 a Tonne…"), the green-steel post and the eu-ets-compliance-platform how-to; one post note mentions "CBAM Article 9 carbon-price recognition gap". `CCTS` over SOURCE_REGISTER.md returned 0. One WebSearch; one document fetched in full via fetch_source.sh (direct route). Open COMMISSION_QUEUE items not re-read today (reduced budget).

### Background only

- **Khaitan & Co ERGO note, "UK recognition to CCTS", 18 September 2026 (law-firm commentary, PDF, Vanita Bhargava and Vishal Shrivastava)** — fetched in full. Claims HM Treasury added India's CCTS to the UK's indicative list of qualifying overseas carbon pricing schemes under the Carbon Border Adjustment Mechanism (Calculation of CBAM Rate and Determination of Carbon Price Relief) Regulations 2026; UK CBAM starts 1 Jan 2027 (aluminium, cement, fertiliser, hydrogen, iron and steel; GBP 50,000 importer threshold); relief is proportionate to the carbon price actually paid under CCTS and not embedded in the CETA (in force 15 July 2026); EU CBAM definitive phase from 1 Jan 2026 with Q1 certificate price EUR 75.36/t, and no EU recognition yet. **Blog fit:** materially updates the published Article 9 recognition-gap and CBAM-steel posts (UK has recognised CCTS, the EU has not, per this source), so worth a dated update box. **Caveat:** secondary; the primary (HM Treasury list and the 2026 Regulations) was not fetched, the EU-status line comes from the same note, and CCTS prices are not yet set so the relief is unquantified. No dataset, so not COMMISSIONABLE; nothing queued. Verify against gov.uk before any update box.

## Added 2026-11-17 (daily task, Tuesday odd week: insurance, reinsurance and financial plumbing)

Dedup with `repo_read.sh localgrep` over `meta/manifest.json`: `[Bb]ima [Bb]harosa`, `[Rr]epudiat` and a title-line `[Gg]rievance` search all returned 0 hits; insurance posts are `premium-now-claim-later-float-indias`, `india-built-offshore-insurance-hub-it`, the PM-JAY health-cover post, the PMFBY post and the agentic-insurance-agent how-to. Two WebSearches (IRDAI; secondary sites only, not used). The primary was read today: the irdai.gov.in document page (12.2 MB PDF, listing only, no text) and then the same report via the Life Insurance Council mirror, fetch_source.sh direct route, chapter II.6 to II.8 read in full.

### Commissionable

**IRDAI, Annual Report 2024-25, Part II.6 "Grievances" (pp. 81-84, Tables II.15 to II.19)** — upgrades the 2026-10-13 entry from BACKGROUND (secondary only) now that the primary is read.
- **Data:** the report PDF, free, no login: irdai.gov.in/document-detail?documentId=8375620 (listing page; the PDF itself was read from the lifeinscouncil.org mirror, `/component/IRDAI%20Annual%20Report%202024-25.pdf`). Source of the counts is the Bima Bharosa portal (Table II.15 note).
- **Finding (all from the PDF):** grievances on Bima Bharosa 2,57,790 in 2024-25 against 2,15,569 in 2023-24 (+19.6%). Life flat (1,20,726 to 1,20,429) but General & Health up from 94,843 to 1,37,361 (+44.8%). Pending at year end for General & Health rose from 5,056 to 9,606; public-sector General & Health pending rose from 4,055 to 8,201 on 24,955 to 38,924 received (Table II.17). Grievances per lakh policies and lives: life 15.72, General & Health 5.29 (Table II.15). Claims-related grievances: life 33,280 on 26.68 lakh claims; General & Health 88,841 on 11.26 crore claims (para II.6.9). Life unfair-business-practice grievances 23,335 to 26,667, share 19.33% to 22.14% (Table II.16). Ombudsman compensation cap raised from Rs 30 lakh to Rs 50 lakh (II.8.5).
- **Blog fit:** extends the insurance beat from the money side (float, cession, GIFT City) to the policyholder side; nearest posts `premium-now-claim-later-float-indias`, `india-built-offshore-insurance-hub-it`. Opens zero-coverage ground: claims, grievances, Ombudsman.
- **Caveat:** (1) para II.6.7 and the text after Table II.17 say "the majority" of General & Health grievances were claims related (69%), but 88,841 / 1,37,361 is 64.7%; reconcile before printing either; (2) Table II.17 "attended" is not "resolved", so do not call pending a backlog measure without the report's own definition; (3) public-sector pending figures are by sector, not by insurer, so do not rank named insurers from this table; (4) grievance counts are portal-registered only, not insurer-internal complaints; (5) the claims denominators are not like for like (11.26 crore general claims are dominated by health); (6) the earlier secondary-source doubts on the Ombudsman count (53,184 vs 53,102) are not settled by chapter II.8, which carries no count; (7) FY 2025-26 report may supersede this by publication time, check irdai.gov.in annual reports first.
→ queued in COMMISSION_QUEUE.

## Added 2026-11-18 (daily task, Wednesday odd week: energy and gas; one source found off-beat)

Dedup with `repo_read.sh localgrep` over `meta/manifest.json`: `[Uu]nified [Tt]ariff` returned 0 hits. A WebSearch on the PNGRB unified tariff (zones cut from three to two, effective 1 Jan 2026, GAIL integrated tariff Rs 65.69 per mmBtu, 12 unconnected pipelines proposed, comments closed 23 Oct 2026) returned news and PNGRB press-note links only; none was fetched, so it is logged below as unread. The same run's Track D search surfaced the NITI PLI report, which is the day's real source; the manifest already carries many PLI posts, so it is graded on whether it updates them.

### Commissionable

**NITI Aayog with IIM Ahmedabad, "Impact Assessment of PLI Schemes", November 2026 (free PDF, 160+ pages, no login)** — fetched in full by `fetch_source.sh` (direct route; text read: front matter, Executive Summary, Introduction, Tables 1 and 2, the 50% benchmark discussion; sector chapters 1-14 and appendices NOT read).
- **Data:** niti.gov.in/sites/default/files/2026-11/Impact-Assessment-of-PLI-Schemes.pdf. Table 1 (outlay by scheme), Table 3 (disbursement by scheme to March 2026), Table 4 (sector indicators), per-sector graphs on beneficiary-level data supplied by ministries. Free download.
- **Finding (Introduction, text):** across 14 schemes with Rs 1,91,049 crore outlay, cumulative investment Rs 2,40,138 crore (76% of the Rs 3,15,092 crore full-tenure target), production/sales Rs 22,66,412 crore (64% of Rs 35,37,863 crore), employment 8,49,069 (28% of 30,18,750), disbursement Rs 35,354 crore (18.51% of outlay), against 58% of aggregate scheme duration elapsed (578 of 996 months). Yearly employment achievement: 86%, 85%, 156%, then 31% in FY2025-26. Yearly disbursement against plan: 63%, 71%, 100%.
- **Blog fit:** extends the PLI cluster; nearest published posts `indias-food-processing-story-pli-scheme`, `indias-mobile-phone-pli-beat-every`, `pli-medical-devices-coverage-and-gaps`, and the "14 PLI schemes ... every named winner" post (slug not looked up). It is a primary, official portfolio-level scorecard the blog's per-scheme posts have not had; it also gives the first stated employment shortfall (28%) next to investment (76%).
- **Caveat:** (1) NITI's own disclaimer says NITI does not confirm data authenticity or the methodology; all data are "interpreted solely by" IIM Ahmedabad. (2) Method is comparison with an "underlying/natural trend" and a self-chosen 50% mid-course threshold; I saw no counterfactual or firm-level matching in the parts read, so "additionality" is asserted, not estimated. (3) Targets are scheme-reported, not independent. (4) Nominal values; the report itself warns about this. (5) The red/amber/green colour grades in Table 2 do not survive the text extraction, so per-sector verdicts must be read from the PDF page. (6) Whether this report contradicts the food-processing post's job claim was not checked (sector chapter 13 not read).
→ queued in COMMISSION_QUEUE.

### Weak — logged, not actioned

- **PNGRB unified tariff, press coverage (search snippets only, 2026-11-18)** — zones three to two, effective 1 Jan 2026, claimed Rs 2-3 per unit consumer saving and about Rs 1,000 crore a year saved in CGD transport cost. Not fetched; a Lok Sabha reply in the same results dates the zone amendment 7 Jul 2025 against December 2025 orders in the press, an unreconciled conflict. Primary to fetch next: pngrb.gov.in press note 20251216_PR.pdf. BACKGROUND until read.
