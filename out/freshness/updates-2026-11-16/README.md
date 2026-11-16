# Stale-post checks, 16 Nov 2026

| Post | Result | File |
|---|---|---|
| top-15-chemicals-for-import | BPCL clearance already in the 10 Nov draft. Added: project-company board approval (23 Oct), 10 MTPA plan, approvals by Feb 2027 per management, no FID yet. TPA/dye anti-dumping: no final findings found on DGTR (absence of evidence, wording kept cautious). | out/update-2026-11-16-top-15-chemicals-for-import.html |
| india-solved-carbon-credit-banking-with | Trading still not started. Added: BEE draft Detailed Procedure (19 Oct), needs CERC approval; CERC next hearing 12 Jan 2027. Not used: a 12 Nov secondary page saying BEE's director put most-sector trading at end-2027 (one secondary source). | out/update-2026-11-16-india-solved-carbon-credit-banking-with.html |

Neither post has a viz edition, so these are update files. Publish with `python3 tools/blogger_api.py update --slug <slug> --file <file>` on the Mac. Nothing was published from the cloud.

## "As of" posts checked (27 flagged; the rest are correctly dated snapshots)

Applied as `update_notes` on editions (re-rendered, `viz_verify` PASS): rooftop-solar-is-working-household (65.26 lakh households, 19.1 GW at 2 Nov), city-gas-just-became-indias-largest-gas (PNGRB Aug 2026: 9,158 CNG stations, 1.77 crore PNG), tamil-nadus-wind-potential-according-to (12,273 MW at 30 Jun 2026, PIB), the-solar-panel-recycling-opportunity (171 GW solar at 30 Sep, MNRE via Spirit of Chennai).

New update file: fuel-pricing-to-crude-cost (Brent back near $93-96; secondary sources, wording says so).

Applied by hand: one-nation-one-ration-card-doesnt-move (hand-built edition). The 1 Oct 2026 stock line (840.8 lakh tonnes, 2.7x the 307.7 norm) is an `xv-upd` block in `edition.html` and in `build.py`. Do not re-run `build.py` to regenerate `edition.html`: its raw output corrupts two PIB links (`&reg=` becomes a registered-mark character) and lacks later CSS, so edit `edition.html` directly.

Already updated earlier: india-trade-sector-policy, indias-state-incentive-war-gujarats (PLI 30 Jun 2026), indias-trade-story-has-three-big-wins.

Left as is: the remaining "as of" dates are labelled historical snapshots (GST 2025, ICRA March 2026 capital intensity, TNPL March 2025 capacity, wage and PLI statistics tied to a stated date). Delhi sapling drive: the post already reports the late-September review; The Hindu (26 Sep) says the 70 lakh target was met.
