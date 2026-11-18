#!/usr/bin/env bash
# Insert all 21 November 2026 draft posts as Blogger DRAFTS (nothing goes live). Run on the Mac from the repo root, after "git pull".
#   DRY=1 bash out/publish_all_nov2026_drafts.sh   # dry run
#   bash out/publish_all_nov2026_drafts.sh          # insert drafts
#   SKIP="mcl-ipo-2026 pli-2026" bash ...           # skip ones already inserted (use the names below)
# The daily write ceiling may stop the run part-way ("STOPPED at ..."); rerun with SKIP set to those done.
set -u
ARGS="--draft"; [[ -n "${DRY:-}" ]] && ARGS="--draft --dry-run"
ins() { local key="$1" file="$2" title="$3"; [[ " ${SKIP:-} " == *" $key "* ]] && { echo "== skipped $key"; return; }
  [[ -f "$file" ]] || { echo "MISSING $file (git pull?)"; return; }
  echo "== $key"; python3 tools/blogger_api.py insert $ARGS --file "$file" --title "$title" || { echo "STOPPED at $key"; exit 1; }; }
ins mcl-ipo-2026 "out/post-mahanadi-coalfields-ipo-offer-for-sale-valuation-nov-2026.html" "Mahanadi Coalfields IPO: Rs 8,981 crore offer, all proceeds to Coal India"
ins coal-gasification-2026 "out/post-india-coal-gasification-incentive-scheme-applications-nov-2026.html" "Coal gasification: 9 applications in two rounds for a Rs 37,500 crore scheme"
ins cpi-october-2026 "out/post-india-retail-inflation-october-2026.html" "India's retail inflation: 6.09% in October 2026, above the RBI's 6% upper limit"
ins wpi-october-2026 "out/post-india-wholesale-inflation-october-2026.html" "India's wholesale inflation: 12.29% in October 2026, fuel and power up 32.84%"
ins power-squeeze-2026 "out/post-india-power-demand-coal-stocks-october-2026.html" "India's power demand in October 2026: 160 billion units, coal stocks at six days"
ins renewables-vs-coal-2026 "out/post-india-renewables-coal-capacity-generation-q2-2026-27.html" "India's power mix, Q2 2026-27: coal 42% of capacity but 66% of generation"
ins us-trade-deal-2026 "out/post-india-us-trade-deal-tariffs-open-items-nov-2026.html" "India-US trade deal, November 2026: 10% duty in force, agreement text unsigned"
ins el-nino-2026 "out/post-india-monsoon-2026-el-nino-reservoirs-rabi.html" "India's 2026 monsoon: 87% of normal rain, reservoirs low, a very strong El Niño"
ins crude-fall-2026 "out/post-india-crude-basket-fall-november-2026.html" "India's crude basket: \$120 in October, \$89 on 10 November; pump prices frozen"
ins rupee-2026 "out/post-india-rupee-rebound-reserves-forward-book-november-2026.html" "India's rupee: Rs 93.69 a dollar on 11 November, 3% above its early-October low"
ins special-session-2026 "out/post-delimitation-amendment-votes-needed-winter-session-2026.html" "Delimitation bill: 298 votes in April, 361 needed now, NDA holds 320 seats"
ins pli-2026 "out/post-india-pli-schemes-scorecard-march-2026.html" "India's PLI schemes: Rs 35,354 crore paid, 18.5% of outlay, jobs at 28% of target"
ins dpiit-100-2026 "out/post-india-100-item-import-push-pvc-china-nov-2026.html" "India's 100-item import push: PVC capacity meets 39% of demand"
ins fom-2026 "out/post-india-biogas-biofertiliser-sales-subsidy-clearances-2026.html" "Biogas manure: 20.65 lakh tonnes sold, Rs 111.72 crore subsidy, 149 clearances"
ins discom-2026 "out/post-india-discom-losses-smart-meters-rdss-2026.html" "Discom losses: AT&C down to 15.04% in FY25, smart meters 28% installed"
ins ethanol-quality-2026 "out/post-india-ethanol-2026-27-tender-feedstock-blending.html" "Ethanol 2026-27: 11 billion litres tendered, cane juice and B-heavy molasses excluded"
ins corporate-laws-2026 "out/post-corporate-laws-amendment-bill-2026-jpc-changes.html" "Corporate Laws (Amendment) Bill 2026: what the joint committee changed in August"
ins air-epi-2026 "out/post-india-epi-2026-air-quality-solar-output-nov-2026.html" "India's air: EPI rank 176 of 177, 9.6% of solar output lost, Delhi AQI 290"
ins agrivoltaics-2026 "out/post-india-pm-kusum-agrivoltaics-nov-2026.html" "PM-KUSUM: 24% of grid plants built; agrivoltaics estimates span 5 to 2,129 GW"
ins fcra-2026 "out/post-fcra-amendment-bill-2026-designated-authority.html" "FCRA Amendment Bill 2026: a new authority takes assets, jail cut to 1 year"
ins asean-2026 "out/post-india-asean-trade-deficit-aitiga-review-nov-2026.html" "India-ASEAN trade: \$51.55 billion deficit in FY2026, goods pact review runs into 2027"
