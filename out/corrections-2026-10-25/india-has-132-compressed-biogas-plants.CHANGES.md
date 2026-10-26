# CHANGES: india-has-132-compressed-biogas-plants (findings 18)

## PROMINENT: the headline argument was rewritten with newer figures
The post's thesis ("only 17 of 132 plants connected, ~13%") used stale snapshots. Primary documents give: 207 functional plants, 24 connected (11.6%), 15 in progress, 20 proposals, 148 not planned (PNGRB FY2025-26 connectivity report, Aug 2026; Statistical Booklet 30 Sep 2026: "only 24 (11.6%)"). The thesis survives (about 12% connected) but every number moved. **Please read the rewritten standfirst, "Functional does not mean connected" paragraph and the table.**

## Recommended title
Current: "India Has 132 Compressed Biogas Plants Running. The Pipeline to Actually Use That Gas Reaches 17 of Them."
Proposed (also applied to the body H1): **"India Has 207 Compressed Biogas Plants Running. The Pipeline to Actually Use That Gas Reaches 24 of Them."** (Blogger title must be changed manually; the URL slug contains "132".)

## Changes applied
Sources: PNGRB report https://www.pngrb.gov.in/pdf/CBG/20260806_CBG_pipeline.pdf (raw/18/cbg.pdf: Functional 207; Already connected 24; In progress 15; Proposals 20; Not planned 148; under-construction 328: 2/17/52/257); Booklet https://www.pngrb.gov.in/pdf/e-publication/20260930_PNGRB_Statistical_Booklet.pdf; PIB https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/aug/doc202686946301.pdf ("1,908 ... registered ... 217 plants have already been commissioned producing 0.4 MMSCMD, while 339 plants are under construction").
1. **H1 and standfirst**: 132/17 -> 207/24; standfirst now says "217 commissioned on the GOBARdhan portal by 6 August 2026".
2. **Stat cards**: "132 commissioned (Jan 2026)" -> 207 functional (with 132 Jan-2026 and 217 portal figures in the label); "17 of ~130 (Sept 2026)" -> "24 of 207 (11.6%), PNGRB Aug 2026"; "~20 more under construction" -> "15 in progress; 20 proposals; 148 no plan"; "174 / 425" -> "339 under construction (GOBARdhan portal)".
3. **Intro paragraph**: "India has commissioned 132 as of January 2026" -> "had commissioned 132 ... by 6 August 2026 the portal counted 217, 4.3% of the target"; "even the 132 plants" -> "even the plants that exist".
4. **"Functional does not mean connected"**: replaced the ATR quote paragraph with the PNGRB report/booklet numbers (24 of 207, ~12%, 15 in progress, 20 proposals, 148 no plan). The earlier ATR quote (17 of ~130) is retained as an "earlier count" with a note that the quote could not be re-located, so the following paragraph (which discusses mapping "proximity" and "feasibility") still reads coherently.
5. **CBO paragraph**: "roughly 13%" -> "roughly 12% (11.6%)".
6. **Table**: added rows Commissioned 6 Aug 2026 = 217 (4.3%), Functional Aug 2026 = 207 (4.1%); "pipeline-connected" 17 (0.3) -> 24 (0.5) "of which" functional; "Under construction 174 (3.5)" -> 339 (6.8); "Not yet started 425 (8.5)" -> "Registered on GOBARdhan portal (all stages) 1,908 (38.2)". Percentages are share of 5,000. **The old "Not yet started 425" has no current equivalent; I substituted the portal's registered total. The author may prefer to drop that row.**
7. **"Reading this table correctly"** note: "17-connected/~20-more ... smaller set of already-commissioned plants" -> "24-connected/15-in-progress ... within its 207 functional plants".
8. **Legislature comparison table and prose** (derived from 132 and 17): recomputed at 217 commissioned and 24 connected: districts 1 per 3.7 / 33; Lok Sabha 1 per 2.5 / 23; MLA constituencies 1 per 19 / 172; all seats 1 per 21.5 / 194; prose "six times ... forty-seven times the current count of 17" -> "four times the current count of 217 ... thirty-three times the current count of 24".
9. **"What would fix this"**: "the 20 under construction" -> "the 15 in progress"; "~90 unconnected" -> "148 functional plants with no connectivity plan".
10. **"What this piece does and doesn't cover"**: the "132/920 TPD ... most recent" claim now says it is a January 2026 snapshot superseded by PIB's 6 Aug figures and that 920 TPD was not re-verified.
11. **"Updated 13 October 2026" box**: "February 2026" -> "March 2026" (file dated 3 Mar 2026); "(not opened)" and "search summaries only" statements replaced by "since opened"; "original text below is unchanged" -> "has since been updated".
12. **Sources paragraph**: ATR is no longer "primary source"; added PNGRB report, Booklet, PIB backgrounder, Oct 2025 and Mar 2026 decks (links).
13. **Revised date**: `<time itemprop="dateModified">` -> 25 October 2026. Version label `v1.1.0` and the revision-history list were left; the author may add a v1.2.0 entry.
14. **Correction note** (`.warn` class, placed as a `<p>` before the closing Sources paragraph).

## Not applied / flagged for the author
- **"September 2026 Action Taken Report" quote** (17 plants / ~130 / ~20): could not be found anywhere; the quote is retained only as an "earlier count" with a caveat. Consider removing it and the sentence in the next paragraph that leans on it. Related claims "the ATR does not publish [blend achieved]" and "the ATR does not distinguish" are likewise unverified (left unchanged).
- **132 plants / ~920 tonnes/day (Jan 2026)**: unverified. Note PIB gives 0.4 MMSCMD for 217 plants, which does not obviously reconcile with 920 TPD for 132 plants. Needs checking against the Energetica article.
- "103 operational mid-2024", "40 by 2023-24": not rechecked.
- Gobardhan "about 210 as of June 2026" in the 13 Oct box: replaced in effect by the 217 (6 Aug 2026) in the body; box text left apart from the edits above.
- PNGRB Statistical Booklet 120.29 MMSCM / 0.998% blending vs the August report's 111.48 / 0.92%: not used in the post.
- Under-construction count differs by source (PIB portal 339 vs PNGRB 328); the post uses 339 and says datasets should not be added together.

## Verification
- diff vs original: 53 changed lines (`diff posts/india-has-132-compressed-biogas-plants.html out/corrections-2026-10-25/india-has-132-compressed-biogas-plants.html`); no CSS, script, Google Translate, AI-disclosure or gs-idx lines changed.
- tag counts (orig->new): <div 21->21; </div 21->21; <table 2->2; </table 2->2; <script 4->4; </script 4->4 (all unchanged).
- inline <script> blocks parsed with node: 2 blocks, ok, ok; script text identical to original.
