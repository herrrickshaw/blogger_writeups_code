# CHANGES: the-recycling-lottery-playbook-norways (findings 13)

## AUTHOR DECISIONS (flag)
- The headline claims "97% return rate" and "zero addiction cases" are both weakened: 97% is not Norway's deposit return rate (93.1% cans / 92.4% bottles in 2025; total collection 97.9% / 98.2%), and "zero addiction" is only an assertion by the UBC authors. I attributed rather than deleted. The "gold standard" framing otherwise stands.
- Revenue and payout ripples: the old "~NOK 300M (~EUR 25M)" revenue and "~EUR 4M/yr payout (16-yr average of EUR 62M)" are replaced by the legal turnover cap (NOK 410M, Dec 2025) and the Red Cross's current ~NOK 150M/yr. I did NOT convert to euro (no stated rate in the sources). Note the two new figures sit oddly together (150M is ~37% of a 410M cap, vs the 53% share after prizes), because the cap is turnover and the Red Cross share is after prizes; reconcile if you want a payout ratio. Actual 2025 turnover is not published in what I read.
- "Red Cross funding growing 5%/yr" (financial-model box) is unverified in any document; left untouched. Consider deleting.

## Changes applied
Sources: Infinitum Annual Report 2025 https://infinitum.no/media/hg5dea4x/infinitum_a-rsrapport_2025_web-en.pdf (raw/13/inf25.txt: 93.1% cans, 92.4% bottles deposit return; 97.9% / 98.2% total recycled; 2024 report 93%/more than 98%); Red Cross Norway https://www.rodekors.no/pantelotteriet (raw/13/rkp.html: "ca. 150 millioner kroner" per year; "over 1 milliard kroner" since 2008; owners Thon 60% / Red Cross 40%); Red Cross poster (raw/13/rk_poster.txt: lottery "midlertidig stengt ut 2025" after reaching the statutory turnover limit); Lotteritilsynet permit 14 Jan 2026 https://lottstift.no/app/uploads/2026/01/25_05228-7-Tillatelse-til-a-tilby-stort-pengespill-jf.-pengespillforskriften-kapittel-10-P-1341790_11_1.pdf (raw/13/lottstift.txt: max NOK 410 million per calendar year as of Dec 2025; NOK 0.50 per ticket; 1/468); Thon Group Sustainability Report 2018 (raw/13/thon2018.txt: share to the cause raised "from 50%, after deduction of prizes, to 53%"; deposit rates raised to NOK 2 and 3); UBC article https://beyond.ubc.ca/how-a-lottery-style-refund-system-could-boost-recycling/ (raw/13/ubc.html: 47 per cent more containers; $1,000 at 0.01% vs 10 cents; food courts in Vancouver and RibFest in Spruce Grove; "not a single case linking the recycling lottery to gambling addiction"; links doi 10.1016/j.wasman.2025.114954).
1. Display subtitle paragraph (hero): "97% return rates, zero addiction cases, EUR 62M+ to charity over 16 years" -> "about 93% of containers returned through the deposit system (98% total collection), no addiction case reported by the UBC researchers, and more than NOK 1 billion to the Red Cross since 2008".
2. 13 Oct update box: "All of this comes from search summaries" -> points have since been checked against primary documents (see correction note).
3. Intro line: "zero addiction issues" -> "no addiction case reported by the UBC authors who studied it".
4. Key metrics table: return rate 97% -> 93% deposit return (cans 93.1 / bottles 92.4, 2025), ~98% total collection, "whole deposit system rather than the lottery's effect"; charitable funding NOK 737.4M (EUR 62M+) by 2023 -> over NOK 1bn since 2008, ~NOK 150M/yr, 737.4M kept as the Nov 2023 figure; annual revenue ~NOK 300M -> legal cap NOK 410M turnover (Dec 2025), reached, paused rest of 2025; addiction row -> "None reported, according to the UBC authors (an assertion, not an audited statistic)".
5. Behavioural-economics section: "University of British Columbia study (2024) ... 47% more bottles ... Randomized controlled trial, peer-reviewed, replicated, and validated ... by Norway's 97% return rate" -> 2025 field experiment in BC and Alberta, 47% more containers brought to the researchers' tables for a 0.01% chance of $1,000 vs a guaranteed 10 cents; peer-reviewed (Waste Management, 2025); no replication described; Norway's return rate is system-wide so not evidence for the lottery effect; 47% is containers brought to an experiment. (Expected value: 0.01% x $1,000 = $0.10, so "identical expected value" stays correct. I dropped "randomized controlled trial" because the UBC text calls it an experiment and does not describe randomisation.)
6. Financial model block: "NOK 2-3 (2026 rate)" -> "the rate since 2018; no 2026 change found" (Infinitum/Thon 2018); "50%+ of proceeds -> Red Cross" -> "53% of turnover after prizes (Thon Group, 2018 report)"; "~NOK 300M revenue" -> "turnover up to the NOK 410M legal cap; Red Cross receives about NOK 150M/yr". 4-6 tickets (NOK 2 or 3 / 0.50) stays correct.
7. International expansion: "Canada (UBC trial 2023-24): 47% recycling increase confirmed; provincial rollout under consideration" -> published 2025 field experiment, 47% more containers brought; "the UBC article reports no provincial rollout". No support was found for a rollout.
8. Norway vs Jal Jeevan table: Norway annual revenue "~EUR 25M" -> "Up to NOK 410M (legal cap, reached in 2025)"; payout "~EUR 4M/yr (16-yr avg of the EUR 62M cumulative)" -> "About NOK 150M/yr now (Red Cross Norway); over NOK 1bn since 2008". Jal Jeevan design-target columns untouched.
9. Pahle paragraph source note: added that the paper reaches the US$12bn by extrapolating Kerala lottery earnings nationally and words it "cumulatively" (so the per-year reading is the blog's), and that it only sets the figure beside budgets and does not say Jal Jeevan would receive lottery money. All Pahle figures themselves CONFIRMED (33.2bn, 26bn, 12bn/11.9bn, 44.3bn by 2030, JJM 8.4bn, MGNREGA 7.2bn etc.). NOTE: I did not adopt the findings' phrase "potential market not measured"; the white paper text says the market "currently stands at roughly USD 33.2 billion annually".
10. Sources list: added Infinitum 2025, Red Cross Norway, Lotteritilsynet permit, Thon 2018 report; UBC entry now carries the full study citation and DOI.
11. Visible correction note (class warn, as a <p> with the post's existing warn styling) inserted directly before the "Sources" h2. No dateModified element.

## Title
No change needed (h1/title do not carry the corrected figures). The hero subtitle paragraph was edited.

## Not applied / open
- Finland Palkinto Lotteri (2011), UK/Sweden/Germany/Australia "licensing/launches expected", "~5 billion tickets (target)": not checked.
- Germany Pfand figures (97.7%, Destatis): not checked in this pass; the comparison table still says "97.7-98%+ return" for Germany (separate figure, left).
- "Win: NOK 50 - 1,000,000" matches the permit (50, 100, 1,000, 10,000, 1 million); unchanged.
- The "34.5% of gross" on Thon's page was not found in any fetched document; the 13 Oct box that mentions it was left as is.
- "Added: 39% choose the lottery" (UBC/Thon) not re-verified.
- TOMRA, theweek.in blocked; not used.

## Ripples checked
- 97%: hero, key metrics table, behavioural section - all fixed. EUR 62M: key metrics (kept as dated Nov 2023), Norway-vs-JJ payout row (replaced). EUR 25M: JJ table (replaced). NOK 300M: key metrics and financial model (replaced). No chart data arrays depend on these; the two SVG charts use Pahle figures only (unchanged).

## Verification
    ## diff stat
    38
     the-recycling-lottery-playbook-norways.html |   38 +++++++++++++++-------------
     1 file changed, 21 insertions(+), 17 deletions(-)
    <div orig=      11 new=      11
    </div orig=      11 new=      11
    <table orig=       6 new=       6
    </table orig=       6 new=       6
    <script orig=       4 new=       4
    </script orig=       4 new=       4
    scripts parsed: 2, failures: 0
