# Research-gap crosscheck: 2026-10-26

**Scope:** 114 recently published or edited posts from `recent_posts.txt`. Each was run through `tools/research_crosscheck.py --auto --numbers` and the output read. The tool's raw output was almost all noise: site boilerplate, related-links lists, and substring number collisions, for example "8.5%" matching "98.5%". So candidates were generated in three other ways:

1. Pairing number-bearing sentences across posts that share rare terms.
2. Following every "this blog's earlier piece" cross-reference made by a recent post.
3. Taking every "Updated / Correction" note in the 114 posts and searching all of `posts/` for the claim it superseded.

Every item below was confirmed in the HTML of both posts. Nothing under `posts/` or `meta/` was edited.

**Result:** 9 genuine gaps. Eight are factual. The ninth (#9) is a low-severity terminology mismatch.

---

## 1. CAQM ₹61.85 crore co-firing penalty: called an imposed "order" in Dec 2025

- **Stale:** `indias-coking-coal-import-problem-and` (not in the recent list)
  > "In a compensation order published 26 December 2025, CAQM found six major thermal plants in Punjab, Haryana and Uttar Pradesh had missed their FY2024-25 co-firing targets and demanded a combined ₹61.85 crore in environmental compensation, with each plant given 15 days to respond:"
- **Right:** `ethanols-coal-boilers-briquette-gap-and`, update note of 22 Oct 2026
  > "Coverage of CAQM's own releases indicates that the December 2025 action was a set of show-cause notices that only proposed the amount. The compensation was formally imposed in a CAQM press release dated 8 April 2026. That release covered non-compliance in 2024-25 and set the 15 April 2026 deposit deadline."
- **Evidence:** the note links CAQM's own release (`CAQM PR 08042026 (Notice to 06 TPPs)`) and All India Radio's "CAQM issues show-cause notices" report. The coking-coal post relies on a single trade site (PelletRates). The ethanols post's own body text still says "imposed". That is covered by its update note, so it is not counted as a separate gap.
- **Proposed sentence (coking-coal post):** "In show-cause notices issued in late December 2025, CAQM found six major thermal plants in Punjab, Haryana and Uttar Pradesh had missed their FY2024-25 co-firing targets and proposed a combined ₹61.85 crore in environmental compensation, with each plant given 15 days to respond; it formally imposed the compensation in a press release of 8 April 2026, with a 15 April 2026 deposit deadline:"

## 2. Gas-grid length and utilisation: a newer regulator source exists but is not used

- **Stale (a):** `indias-gas-pipelines-run-at-half`, update note of 22 Oct 2026
  > "PNGRB's data sheet for 31 March 2026, as seen in search summaries, puts the operational gas trunk network at about 27,900 km against about 34,800 km authorised, with about 8,550 km under construction or partly commissioned. We found no newer national utilisation figure, so the 50% and 41% estimates below remain the latest."
- **Stale (b):** `a-2013-vision-saw-india-needing-746`
  > "This blog's earlier research (again via PIB year-end reviews, not a document read directly) put India's operational gas trunk pipeline network at roughly 25,400 km by June 2025, with an authorised length of roughly 34,200 km …"

  It also says: "… so that figures such as 25,400 km operational and 34,200 km authorised do not have to be reconstructed from year-end press reviews."
- **Right:** `india-has-27400-km-of-gas-pipeline` (23 Oct 2026)
  > "PNGRB's own monthly pipeline report for August 2026 puts 28,157 km in operation out of 34,978 km authorised, as of June 2026."

  Its table ("PNGRB MIS report, NGPL, August 2026, page 4") gives: "All common-carrier pipelines 28 | 26,646 km | 762 MMSCMD capacity | 247 carried | 32%".
- **Evidence:** the regulator's own MIS PDFs were read in full, and the post is dated one day after the other note. The 32% figure is a capacity-weighted, network-wide utilisation for a named month. That is exactly what the gas-pipelines note says does not exist.

  The figures do not contradict the chairman's "~50%" remark outright. That remark was made against a ~400 MMSCMD base, while the MIS table uses 762 MMSCMD of nameplate capacity. So the two should be shown side by side with their bases, not one replacing the other.
- **Proposed sentence (gas-pipelines note):** "PNGRB's own MIS report for August 2026 puts the operational network at 28,157 km against 34,978 km authorised (June 2026), and shows the 28 common-carrier pipelines carrying 247 MMSCMD against 762 MMSCMD of capacity in August 2026, about 32%; the 50% (chairman, against ~400 MMSCMD) and 41% (IEEFA, FY2025) estimates below use different bases and vintages."
- **Proposed sentence (a-2013-vision):** "PNGRB's own MIS report puts India's operational gas pipeline network at 28,157 km against 34,978 km authorised as of June 2026, already within the report's 28,000–32,727 km five-to-six-year target, albeit reached on a much longer timeline." The "reconstructed from year-end press reviews" recommendation should be reworded, because PNGRB does publish a dated monthly table.

## 3. FY2025-26 real GDP growth: 7.7% / 7.1% versus 7.8% / 7.2%

- **Stale:** `five-year-synthesis-trade-currency`, update note of 12 Oct 2026
  > "(2) GDP: the provisional estimate of 29 May 2026 puts FY2025-26 growth at 7.7% with FY2024-25 revised to 7.1%, so the first-advance series and the "softest of the five" reading below no longer hold."
- **Right:** `real-gdp-growth-india-fy2012-13-to`, correction of 22 Oct 2026
  > "MoSPI's own national accounts data on the new 2022-23 base give real GDP growth of 7.3% in FY2023-24 (final estimate), 7.2% in FY2024-25 (first revised estimate) and 7.8% in FY2025-26 (provisional estimate), not the 7.2%, 7.1% and 7.7% that note gave from press summaries."

  `effective-buying-power-china-comparison` (22 Oct 2026) agrees: "7.8% … (some early press reports gave 7.7% and 8.9%)".
- **Evidence:** the correcting post states it read the figures through MoSPI's data service on 22 Oct 2026. The 7.7% / 7.1% pair came from press summaries and is the same pair that post explicitly withdrew.
- **Proposed sentence:** "(2) GDP: MoSPI's provisional estimate (29 May 2026, new 2022-23 base) puts FY2025-26 growth at 7.8%, with FY2024-25 at 7.2% (first revised estimate), so the first-advance series and the "softest of the five" reading below no longer hold."

## 4. Green-hydrogen tender prices: ₹387–397/kg cited as the settled cost curve

- **Stale:** `the-hydrogen-bill-hiding-inside-indias`
  > "This blog has already tracked India's actual green-hydrogen cost curve in detail: recent SIGHT-scheme tenders cleared at $4.11–4.21 per kilogram (₹387–397), against the National Green Hydrogen Mission's own $1.50/kg by 2030 target …"

  It also says: "… are drawn from this blog's own prior, separately sourced reporting (see the levelised-cost-of-hydrogen piece linked above) — graded strong …"
- **Right:** `the-levelised-cost-of-hydrogen`, the very source it cites, update note of 22 Oct 2026
  > "Those rupee figures appear to include 18% GST. Excluding tax, the IOCL Panipat award was reported at ₹336/kg and the HPCL Visakhapatnam award at ₹328/kg. A later refinery tender, for Numaligarh, closed in February 2026, before this post, at a reported record low of ₹279/kg (about $3.08/kg) excluding taxes."

  `europe-wants-green-steel-it-cant-afford` already uses "India, Rs 279/kg (Numaligarh tender, Feb 2026)".
- **Evidence:** the source post has corrected itself. The citing post contains no Numaligarh mention or tax caveat. `inside-refinery-how-hydrogen-cleans` (not recent) still uses "$4.16/kg" as "today's SIGHT bid price". It does label ₹397 "including GST", so it should get the same Numaligarh line.
- **Proposed sentence:** "This blog has already tracked India's actual green-hydrogen cost curve in detail: the first SIGHT refinery awards were reported at $4.11–4.21 per kilogram (₹387–397 including 18% GST; ₹328–336 before tax), and the Numaligarh tender of February 2026 cleared at a reported ₹279/kg (about $3.08) before tax, against the National Green Hydrogen Mission's own $1.50/kg by 2030 target …"

## 5. Wind: "Gujarat overtaking Tamil Nadu … for the first time" in June 2026

- **Wrong:** `574-gw-and-counting-indias-wind-fleet`, in its standfirst and again in §2
  > "India's wind fleet crossed 57,443 MW in June 2026, with Gujarat overtaking Tamil Nadu as the single biggest contributor for the first time."

  §2 adds: "… Gujarat's newer, larger-scale build-out has now overtaken it as the single biggest contributor to the national total."
- **Right:** `tamil-nadus-wind-potential-according-to`
  > "Tamil Nadu's installed wind capacity stood at roughly 11,938 MW as of 31 October 2025 — India's second-largest wind fleet, after Gujarat's 14,493 MW. Tamil Nadu held the #1 spot nationally until 2023, when Gujarat overtook it."
- **Evidence:** MNRE figures in the Tamil Nadu post show Gujarat already about 2.5 GW ahead eight months before June 2026. The 574-GW post's own data shows something new, but a different thing: Gujarat taking 49% of FY2025-26 additions.
- **Proposed sentence:** "India's wind fleet crossed 57,443 MW in June 2026, with Gujarat, which overtook Tamil Nadu as the largest state fleet in 2023, now adding almost half of all new capacity (49% in FY2025-26)."

## 6. IOCL Petrochemical Intensity target: 16% where the corrected figure is 15%

- **Stale:** `financing-fuel-to-chemicals-pivot-how` (not in the recent list). The figure appears three times: in the body, in the table row "Petrochemical intensity target 6.5%→16%", and in "What would fix this".
  > "… aimed at lifting IndianOil's own petrochemical intensity from about 6.5% to 16% and its petrochemical capacity from 4.3 MMTPA to 13 MMTPA by 2030."
- **Right:** `the-barrel-really-is-shifting-indias`
  > "… to raise its own PII from roughly 6.5% to 15% — corrected here from an earlier version of this piece that had stated 16% … IOCL's own transcript of that call and independent S&P Global reporting on it both instead put the target at 15% …"

  `the-detergent-chemical-india-exports` was corrected the same way.
- **Evidence:** an IOCL primary transcript plus S&P Global stand against a single Business Standard report. The financing post's own source list cites the "IOCL Q1 FY27 earnings call transcript", which gives 15%.
- **Proposed sentence:** "… aimed at lifting IndianOil's own petrochemical intensity from about 6.5% to 15% (per IOCL's Q1 FY27 call transcript and S&P Global; one press report gave 16%) and its petrochemical capacity from 4.3 MMTPA to 13 MMTPA by 2030." Change the table row and the "fix this" line to 15% as well.

## 7. Rupee's 2026 record low: three different figures for the same event

- **Wrong:** `india-imports-283000-tonnes-of-almonds`, update note of 12 Oct 2026 (not in the recent list)
  > "Reported record lows in 2026 were about 95.86 on 14 May and about 96.2–96.4 in late September and early October …"
- **Contradicted by:**
  - `rbi-foreign-exchange-reserves-20152026`: "The weakest single session in this window was ₹96.84 around 19–20 May 2026, when the rupee briefly touched a fresh record low …"
  - `the-rbis-fcnrb-window-drew-133-billion` (9 Oct 2026): "… against a record low of 96.96 in May …"
  - `can-rupee-trade-actually-offset`: "USD/INR 2026 YTD range … (₹89.87–96.88/USD)"
- **Also flawed:** `what-india-is-actually-paying-for` (recent)
  > "The rupee depreciated roughly 9% over FY2025-26 (April 2025 to end-March 2026), ending the year at approximately ₹93.88 to the dollar after touching a then-record intraday low of ₹95.63 on 13 May 2026 …"

  A 13 May 2026 low cannot precede the end-March 2026 close.
- **Evidence:** three independent sibling posts put the May 2026 trough at about 96.8–97.0. If that is right, late-September levels of 96.2–96.4 were not record lows. The 95.63 (13 May) and 95.86 (14 May) figures fit as earlier steps in the same mid-May slide. The exact May trough (96.84, 96.88 or 96.96) differs by source and basis; it should be checked once against RBI reference-rate data, as the almonds note itself advises.
- **Proposed sentence (almonds note):** "Reported lows in 2026 include about 95.86 on 14 May and a record near 96.8–97.0 later in May (this blog's reserves and FCNR(B) pieces give 96.84 and 96.96); the rupee was about 96 to the dollar in early October …"
- **Proposed sentence (what-india):** "The rupee depreciated roughly 9% over FY2025-26 (April 2025 to end-March 2026), ending the year at approximately ₹93.88 to the dollar; it then hit a record intraday low of ₹95.63 on 13 May 2026, a low surpassed within days as the Hormuz crisis intensified."

## 8. Dahej LNG expansion described as under construction after it was commissioned

- **Stale:** `europe-bought-record-amount-of-lng-and` (not in the recent list; revised 8 Aug 2026, v3.0.0, and updated 27 Sep 2026)
  > "A further expansion of Dahej — at 17.5 Mtpa the country's only ultra-large terminal and the sixth largest in the world — is under construction."

  It also says: "India added 7.1 Mtpa in 2025, has a further 5 Mtpa under construction at Jafrabad, and 5 Mtpa expansions planned at both Dahej and Dabhol." The recommendation refers to "the planned Dahej and Dabhol expansions".
- **Right:** `indias-cheapest-lng-capacity-is-extra` (23 Oct 2026)
  > "… counting Petronet LNG's expansion of Dahej from 17.5 to 22.5 MMTPA, commissioned on 31 March 2026, the nameplate is about 58.5 MMTPA."

  It adds: "Petronet's own results put Dahej at 65.6% of the enlarged capacity in April–June 2026 …"
- **Evidence:** Petronet's Q1 FY2026-27 results report Dahej on the 22.5 MMTPA base. The commissioning date is four months before the Europe post's v3.0.0 revision.
- **Proposed sentence:** "Dahej — the country's only ultra-large terminal and the sixth largest in the world — was expanded from 17.5 to 22.5 Mtpa on 31 March 2026." The later sentence should read "… has a further 5 Mtpa under construction at Jafrabad, a 5 Mtpa Dabhol expansion planned, and Dahej's 5 Mtpa expansion commissioned in March 2026."

## 9. (Minor, terminology) Number of CCTS sectors: "eight covered + two more" versus "7 of 9"

- **Posts A:** `greenhouse-emissions-reduction-and-cbam`
  > "… brought 490 entities across eight sectors under compliance obligations — Aluminium, Cement, Chlor-Alkali and Pulp & Paper …; Petroleum Refineries, Petrochemicals, Textiles and Secondary Aluminium … Two more sectors sit on CCTS's designated list …: Fertiliser and Iron & Steel."

  `indias-carbon-credit-market-domestic` uses the same count: "Total (as of Jan 2026) — Eight sectors covered 490".
- **Post B:** `indias-renewable-energy-certificates`
  > "~490 entities across 7 of 9 planned sectors (aluminium, cement, chlor-alkali, pulp & paper, petroleum refining, petrochemicals, textiles; iron&steel and fertiliser not yet notified)"
- **Assessment:** the entities, batches and dates agree; only the counting differs. Posts A count Secondary Aluminium as its own sector, which implies 10 designated sectors. CCTS's designated list has nine, with secondary aluminium a sub-sector of aluminium notified separately in January 2026. A reader comparing the posts sees 10 against 9.
- **Proposed sentence (Posts A):** "… brought 490 entities in seven of CCTS's nine sectors under compliance obligations (secondary aluminium was notified separately in the January 2026 batch) … Two more sectors, Fertiliser and Iron & Steel, remain without notified targets."

---

## Considered and dismissed

- **Tool `--numbers` hits (e.g. "11%", "23%", "28%", "8.5%"):** unrelated claims or substring collisions ("8.5%" inside "98.5%").
- **`ethanols-coal-boilers` body says CAQM "imposed" the penalty in Dec 2025:** corrected by its own 22 Oct update note.
- **`the-easiest-ev-conversion` body still says "PM E-DRIVE (… October 2024–March 2026)":** its 12 Oct and 27 Sep notes record the extension to 31 Mar 2028. `indias-ev-market-single-digit`'s "₹10,900 cr/2 yrs" describes the scheme as launched, and its 12 Oct note covers the 2028 extensions.
- **PM-eBus Sewa 7,293 sanctioned buses:** explicitly dated as a Feb 2025 snapshot and superseded in its update note.
- **`who-collects-indias-gst` "17.93–17.96% under the 15th FC" next to 17.62%:** the post's own 16th Finance Commission note explains that 17.62% is the new award share.
- **Ethanol capacity 1,822 vs ~1,990–2,000 crore litres:** different dates, reconciled in the update note of `interest-subvention-built-499-ethanol`.
- **Wind 57.4 vs 59.2 GW; Tamil Nadu 11,938 vs 12,274 MW:** different dates, each with an update note.
- **Kawas hydrogen blend 5% (`india-imports-60-of-its-cooking-gas`) vs 8% (PNGRB list):** the sibling says "5% initial", which is still accurate.
- **Gas consumption 188 / 195 / 197.1 / 201 / 212 MMSCMD:** different periods and sources, reconciled in the 22 Oct note of `a-2013-vision`.
- **Gas share of the energy mix 6% / 6.2% / 6.3%:** rounding and different years.
- **Active LPG connections 33.31 crore (May 2026, national) vs 33.14 crore (1 Jul 2026, three PSU OMCs):** different scope.
- **Hot-rolled coil €558 / €578 / €595 / €731; EU blast-furnace average ~1.9 t vs CBAM benchmark 1.370 t:** different dates, different benchmarks, and an average versus a benchmark.
- **Rupee depreciation "~9%" vs "~10%":** different windows, and the text says so.
- **Medical transcriptionists "about 5%" vs "4.9%":** rounding of the same BLS projection.
- **Co-firing mandate 3% vs 5% for FY2024-25:** the coking-coal post already flags this as an unreconciled CAQM versus SAMARTH difference.
- **Talcher "2.6 MTPA" vs "1.27 mtpa":** coal-gasification input versus urea output.
- **PM MITRA Warangal "already grounded" (`from-fuel-to-fibre`, Feb 2026 table) vs inaugurated 10 May 2026:** the table is an explicitly dated snapshot.
- **UAE FDI $25.6bn (to Mar 2026) vs $26.45bn (to Jun 2026):** different cut-offs, both in the same post.
- **CBSE subject shares, PLI-Auto tenure, BoJ 1.00% → 1.25%, repo 5.25% → 5.50%, Russia's crude share, APM ceiling, semaglutide expiry abroad, PLI textiles and bulk-drug counts, foodgrain record, FCI rice price:** all either consistent across posts or already corrected by update notes in every post that carries them.
