# Government-data posts refresh, 9 Nov 2026

Scope:
- The 22 analysis posts built mainly on PIB, gazette, Parliament and ministry data that were last updated on 28 Oct and so
  fell outside the 7 Nov refresh.
- Pipeline-built trackers were assessed but not hand-edited (see below).

15 update files: out/update-2026-11-09-<slug>.html. 7 no change. Per-group logs: log_g1..g4.md.

## Updated
- india-has-27400-km-of-gas-pipeline / right-of-user-what-indias-pipeline: gazette ROU notices from 28 Sep to 5 Nov added
  (Kandla-Gorakhpur LPG, Siliguri-Gangtok, Duliajan feeder, BPCL Malkapur-Shamshabad, JSW Raigarh and Hindalco Rayagada
  last-mile lines, JHBDPL Durgapur-Haldia, Barmer-Bhogat, two ONGC Gujarat lines). Projects ~19 -> ~28.
- india-ended-63-years-of-state-nuclear: CORRECTED. The law has no commencement notification and the rules are in draft;
  "can now apply" / "took effect" fixed.
- india-will-spend-rs-33660-crore-on: CORRECTED. BHAVYA round two closed 31 Oct (extended), not 30 Sep.
- india-imported-295-more-steel-this-year: Apr-Oct 2026 imports 4.90 Mt (+28.9%) (PIB 2333256); South Korea is the top
  source FY27 YTD; 7th open house; a safeguard extension is under consideration.
- india-capped-margins-on-137-cancer: the revised prices took effect; saving Rs 2,500 -> 3,502 cr (NPPA 7 Nov); SC remark of 27 Oct.
- india-raised-cooking-oil-duties-to-help: Sept veg-oil index 135.8 (+16% since the May 2025 cut); SEA import data.
- EV posts (localisation, fleet conversion, market): H1 FY27 EV share 12%; Oct sales; magnet scheme bids; China
  rare-earth pause lapses 10 Nov.
- india-has-legalised-e100-for-flex-fuel: G.S.R. 911(E) dated 23 Oct, gazetted 26 Oct.
- rice-and-maize-became-ethanol: WDRA June 2026 commodity additions; ESY 2026-27 tender closed 5 Nov.
- india-let-oil-companies-put-solar-on (Ayana 3,362 MW), indias-first-seabed-mineral-auction (13 Oct PIB),
  states-won-right-to-tax-mines-in-2024 (curative petition; 4 Nov judgment; Jharkhand session 25-26 Nov).

No change: phone PLI successor, display fab, data-centre tax holiday, oil-PSU MSME quota, rural wages, EPFO ceiling,
plastic heat.

## Needs a human decision
- indias-ev-market-single-digit: the title's "Single-Digit Penetration" no longer holds for the whole market (12% in H1 FY27); it still holds for cars.
- india-ended-63-years-of-state-nuclear: the title and kicker overstate a law that is not in force.
- india-imported-295-more-steel: the title and tiles use Apr-Aug +29.5% (Apr-Oct is +28.9%); "China largest" is Apr-Aug only.
- the-easiest-ev-conversion: the chart's 6.5% bar is 2024 data; it needs a redraw. The cooking-oil chart ends in August.
- Unconfirmed in gazette text: 31/2026-Customs (edible oil), S.O. 5109(E) (EPFO), the 24 Sep offshore-auction rule change.

## Pipeline trackers (rebuild on the Mac; not hand-edited)
- quarterly-reportage-4034-scheme and ipa-digital-twin-reportage-latest: PIB register, data to 26 Aug and 14 Sep.
  They need refresh_twin.py pib, then build_reportage.py and collect_state_news.py in digital-twin-for-ipa.
- Lok/Rajya Sabha registries and the most-discussed-schemes post: complete to the Monsoon Session (19 Aug). The Winter
  Session 2026 is not yet announced, so rebuild after it.
- interpreting-gazette-notification (Gazette Trail DB) and india-environmental-clearances-state (PARIVESH snapshot of
  22 Jul): rebuild via gazette-translated-indexed (ingest.freshness_check) and india-ec-subsector-analysis.

## Rechecks
China rare-earth pause (after 10 Nov); CPI 12 Nov (edible-oil index); CPI-AL ~20 Nov; Jharkhand Assembly 25-26 Nov;
offshore mineral bids 28 Dec.

## PIB data refresh (later on 9 Nov)
- PIB register (india-trade-sector-policy-recommendations/data/pib_index.sqlite) refreshed to 9 Nov 2026: 127,735 releases.
  This was done by a session on the "masaladeutsch blog (PIB access)" environment (commit 16217d3), which also corrected
  409 September dates. The reportage was rebuilt in digital-twin-for-ipa (commit 07a1205), central releases only.
- quarterly-reportage-4034-scheme: 4,146 -> 4,220 rows. +57 rows for 2 Oct-6 Nov; +17 September rows from days the register
  had missed; nine September rows re-dated by one day. Ten collisions were vetoed (the four from October plus Aditi Ashok,
  the TBZ merger, a precision-medicine speech, an AFMS eye camp and two Rahat Mitra exercises). NIDHI was untagged from the
  Digital Bharat Nidhi rows. Retitle to "4,220 ... 2017 to November 2026".
- ipa-digital-twin-reportage-latest: window 15 Sep-9 Nov (101 central, 35 schemes, 13 Cabinet). The stale state wire
  (to 26 Aug) was removed with a note. Retitle to "(15 Sep – 9 Nov 2026)".
- Still open: the state wire needs collect_state_news.py run on the Mac, since the state portals are not allowed in the cloud environment.
- ipa-digital-twin-reportage-latest: state wire restored (89 items, 12 states, 15 Sep-9 Nov) from
  digital-twin-for-ipa docs/state_wire_2026-09-15_2026-11-09.csv (commit 46f96f5), using build_reportage's signal filter.
  Punjab, Kerala, Assam and West Bengal failed on the Mac (scrapling module missing), and the MP Hindi titles were not
  translated. To widen it: pip install scrapling, enable translation, re-run collect_state_news.py --days 56.
