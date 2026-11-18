#!/usr/bin/env bash
# Insert the 11 Drishti/PRS-topic posts as Blogger DRAFTS (nothing goes live). Run on the Mac, from the repo root.
#   DRY=1 bash out/publish_drishti_prs_batch.sh     # dry run, writes nothing
#   bash out/publish_drishti_prs_batch.sh            # inserts drafts
#   SKIP="slug1 slug2" bash ...                      # skip posts already inserted (use the dir name in the table)
# The daily write ceiling may stop the run part-way; rerun with SKIP set to the ones already done.
set -u
ARGS="--draft"; [[ -n "${DRY:-}" ]] && ARGS="--draft --dry-run"
ins() { local key="$1" file="$2" title="$3"; [[ " ${SKIP:-} " == *" $key "* ]] && { echo "== skipped $key"; return; }
  echo "== $key"; python3 tools/blogger_api.py insert $ARGS --file "$file" --title "$title" || { echo "STOPPED at $key"; exit 1; }; }
ins pli-2026 "out/post-india-pli-schemes-scorecard-march-2026.html" "India's PLI schemes: Rs 35,354 crore paid, 18.5% of outlay, jobs at 28% of target"
ins dpiit-100-2026 "out/post-india-100-item-import-push-pvc-china-nov-2026.html" "India's 100-item import push: PVC capacity meets 39% of demand"
ins fom-2026 "out/post-india-biogas-biofertiliser-sales-subsidy-clearances-2026.html" "Biogas manure: 20.65 lakh tonnes sold, Rs 111.72 crore subsidy, 149 clearances"
ins discom-2026 "out/post-india-discom-losses-smart-meters-rdss-2026.html" "Discom losses: AT&C down to 15.04% in FY25, smart meters 28% installed"
ins ethanol-quality-2026 "out/post-india-ethanol-2026-27-tender-feedstock-blending.html" "Ethanol 2026-27: 11 billion litres tendered, cane juice and B-heavy molasses excluded"
ins corporate-laws-2026 "out/post-corporate-laws-amendment-bill-2026-jpc-changes.html" "Corporate Laws (Amendment) Bill 2026: what the joint committee changed in August"
ins special-session-2026 "out/post-delimitation-amendment-votes-needed-winter-session-2026.html" "Delimitation bill: 298 votes in April, 361 needed now, NDA holds 320 seats"
ins air-epi-2026 "out/post-india-epi-2026-air-quality-solar-output-nov-2026.html" "India's air: EPI rank 176 of 177, 9.6% of solar output lost, Delhi AQI 290"
ins agrivoltaics-2026 "out/post-india-pm-kusum-agrivoltaics-nov-2026.html" "PM-KUSUM: 24% of grid plants built; agrivoltaics estimates span 5 to 2,129 GW"
ins fcra-2026 "out/post-fcra-amendment-bill-2026-designated-authority.html" "FCRA Amendment Bill 2026: a new authority takes assets, jail cut to 1 year"
ins asean-2026 "out/post-india-asean-trade-deficit-aitiga-review-nov-2026.html" "India-ASEAN trade: $51.55 billion deficit in FY2026, goods pact review runs into 2027"
