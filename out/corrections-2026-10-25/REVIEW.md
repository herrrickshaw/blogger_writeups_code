# Correction drafts — review index (2026-10-25)

15 corrected post bodies, drafted from the source-gap pass in
`~/Downloads/masaladeutsch_source_gaps_2026-10-25/` (findings + downloaded primaries in `raw/`).
**Nothing published, nothing committed.** Each post has `<slug>.html` (full body, paste-ready)
and `<slug>.CHANGES.md` (old → new, source, not-applied items, checks).

Independent check (all 15): div/table/tr/td/script/style counts balanced, CSS byte-identical,
script bodies unchanged and parse in node, Translate widget / AI-disclosure / gs-idx stub
present, visible "Corrected 25 October 2026" note present. Only biogas adds table rows
(2 new rows, balanced; per-district ratios re-computed and checked).

| Post | Applied / not | Title change? | Decide before publishing |
|---|---|---|---|
| **Coffee** `indias-coffee-crop-hasnt-grown-in` | 5 / 3 | no | "Trend break" argument rewritten: 373k t is the *final* estimate (+2.6%); 403k was a forecast cut by ~30k t |
| **Biogas** `india-has-132-compressed-biogas-plants` | headline rewrite | **yes** → "India Has 207 Compressed Biogas Plants Running. The Pipeline to Actually Use That Gas Reaches 24 of Them." | 920 TPD figure unverified; "Not yet started 425" row replaced with 1,908 registered; Action Taken Report quote not found |
| **TN sewage** `what-sewage-disposal-in-key-parts-of` | 5 / 3 | no | Bengaluru ₹120 cr now "over ~20 years"; unsourced Ghaziabad 1.8 t/day removed; Chennai Metrowater feasibility not applied |
| **Oil storage** `where-worlds-oil-sits-when-it-isnt` | 13 / 3 | no | Ceasefire timeline re-attributed; 25 Sep prices replaced with EIA spot series — keep or revert |
| **Project returns** `textbooks-say-project-returns-converge` | 16 / 0 | **yes** → "...About 79% of a Company's Edge Over Average Returns Survives Each Year" | −0.8 pt is traditional ROIC only; intangibles-adjusted +1.9 pt |
| **OISD/API** `oisd-writes-indias-oil-safety-rules-api` | 14 / 1 | optional ("Just Signed" is soft) | "121 standards" left as is |
| **Auto textiles** `airbags-and-seat-belts-are-import-heavy` | applied | no | Tyre-cord duty dates from 2005 and post-2020 status unclear — weakens "actively protected" angle |
| **Ethanol tender** `indias-2026-27-ethanol-tender-drops` | 3 / 1 | no | Earlier finding was partly wrong (post already had ₹2,390); only the attribution changed. BPCL tender PDF 404 |
| **Patient ID** `india-tracks-every-taxpayer-in-minutes` | 9 / 5 | no | Cognizant 85%+ → 73%; "1.3 lakh facilities connected" still unsourced |
| **Cheese** `the-milk-india-doesnt-drink-cheese-and` | 11 / 3 | no | Swiss side of the EFTA treaty: limited dairy cuts (0402/0403), not a blanket exclusion |
| **Recycling lottery** `the-recycling-lottery-playbook-norways` | 18 / 4 | no | Figures switched from € to NOK; "5%/yr growth" unverified |
| **FIPI** `fipis-biggest-ask-is-getting-natural` | 6 / 5 | no | Merge the 22 Oct box with the new note? keep "7 December" and "dmg events"? |
| **ONORC** `one-nation-one-ration-card-doesnt-move` | 3 / 4 | no | Storage-plan cost and "on track" wording |
| **Bagasse** `bagasse-is-one-crop-residue-already` | 4 / 3 | no | Qualify "no techno-economic study"? (no primary found) |
| **Thermocol** `thermocol-dissolves-in-orange-peel-oil` | note + sourcing | no | Settled: the 2010 paper's Table 1 confirms 182–197 g (the 127 g figure is an earlier study with a different polystyrene); "reused 10 times" not in the cited chapter |

## When publishing (later, after review)
`snapshot.py` first; PUT each body via `tools/blogger_api.py` sending `published` **and**
`labels` back; set the new title for biogas/project-returns in the same PUT; re-fetch with a
cache-buster; `snapshot.py --push`; rebuild the article index (titles changed). Mind the
~50–100 writes/day ceiling — 15 posts is fine.
