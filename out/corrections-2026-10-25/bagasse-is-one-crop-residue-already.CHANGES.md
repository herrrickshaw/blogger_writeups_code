# CHANGES: bagasse-is-one-crop-residue-already (findings 08)
Draft only; nothing published. Original: posts/bagasse-is-one-crop-residue-already.html

## Applied
1. **Timung et al. 2016 row mislabelled.** Hydrolysis table: "282.85 (acid-only, in a comparison table: up to 487.5)" -> "282.85 for bagasse after acid then enzymes (acid-only maximum 452.27)". Sources note: the "487.5 mg/g acid-only figure from a comparison table" replaced with the abstract's actual numbers (452.27 mg/g bagasse acid-only; 282.85 mg/g bagasse after acid + T. reesei enzymes; 487.50 mg/g is spent citronella, 226.99 citronella after enzymes). Source: Journal of Energy 2016, doi:10.1155/2016/8506214, abstract. Note: raw/08/timung.pdf is a Cloudflare 403 stub; I re-verified the abstract text directly from the Crossref API record for this DOI.
2. **"No bagasse foam numbers" amended.** Xie et al., Materials 8 (2015), doi:10.3390/ma8125472, full text via Europe PMC PMC5458812 (raw/08/xie.txt): hydroxyl value 426-505 mg KOH/g; foam density 0.032-0.043 g/cm3 (150 C polyols), 0.031-0.037 (125 C); compressive strength 0.19-0.34 MPa at 125 C and 0.32-0.48 MPa at 150 C as BF/PA falls 1/2 to 1/4 (Table 2). Locations: liquefaction paragraph 1 (hydroxyl range added), foam paragraph ("only hard strength figure ... is for cassava" replaced), "Where the data stop" bullet retitled "Few bagasse foam numbers to rely on", intro sentence ("from abstracts and search summaries") and Sources note updated (Xie and lime study read in full, with PMC links). Wording stresses these are small-batch lab foams from a bagasse-only polyol in a bi-component alcohol.
3. Lime / hydrothermal (256, 320, 384 mg/g after 72 h), KOH 81.6%, FeCl3 42.2 g/100 g = 93.8%, Xie ~75% in 9 min at 150 C: CONFIRMED; no text change except citations.
4. **Visible correction note** (class warn, as a <p>) before "Sources and caveats". No dateModified element.

## Not applied
- **"No techno-economic study" (stat card "0 cost or life-cycle studies", standfirst, "Where the data stop" bullet):** findings report a 2023 techno-economic analysis of 2G ethanol via protic ionic liquid pretreatment of bagasse, and a 2026 review saying pretreatment is 40-50% of biorefinery cost, but journal/DOI were not captured and no raw document is in the folder. Evidence unclear, so not changed. Author decision: qualify the claim to "no study of a bagasse polyol/foam route" and keep the sugar-route statement narrower.
- **115 cane varieties, 27.3-55.2 g/100 g:** still unavailable; findings suggest the 115-variety count and attribution should be checked before keeping (paper is paywalled). Left in table.
- **HTL ~36 wt% (IIT Madras), composition 40.4/23.8/27.2/3.0/4.4, Indian figures (9,806 MW; 11,748 MW; 527 mills; 80 Mt):** unverified, unchanged.

## Title / headline
No change. Standfirst's "about 75% liquefied in nine minutes" is confirmed. The "No cost or life-cycle study was found" sentence stays (see above).

## Ripples checked
Stat cards (~75%, 0 studies) unaffected. No chart arrays depend on the corrected figures (SVG composition chart is a separate, unverified source).

## Checks
diff: 6 lines removed, 8 lines added (whole-line diff); tag counts (orig/new): <div:17/17, </div>:17/17, <table:2/2, </table>:2/2, <script:4/4, </script>:4/4; inline scripts parsed: 2, all OK: True; script bodies unchanged: True
