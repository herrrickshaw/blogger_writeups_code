# Merge notes: where-rupee-actually-stands-ten-years

- TARGET: where-rupee-actually-stands-ten-years (current file: out/update-2026-11-07-where-rupee-actually-stands-ten-years.html, published 2026-08-14 10:47 IST)
- Folded: the-currency-rupee-trends-piece-left (current file: posts/the-currency-rupee-trends-piece-left.html; no out/update-* exists; published 2026-08-14 18:48 IST, so it is the newer post)
- Output: out/update-2026-11-14-where-rupee-actually-stands-ten-years.html
- New title: "The rupee over 10 years: against the dollar, yuan, rouble, riyal, dirham and yen" (80 characters)

## Where each section came from

| Merged section | Source |
|---|---|
| Standfirst | Target standfirst, plus the yen rationale from the yen post's standfirst |
| 14 Nov update note | New (required by brief) |
| "Why these six" card | Target "Why these five" card, plus the yen rationale |
| Ten-year indexed chart (#chart) | Target section 1 text; chart is the yen post's six-line SVG (same five polylines plus JPY); 7 Nov update note kept from target; yen "below 100" text from yen post section 1; banknote image from yen post |
| Each currency (#pairs) | Table: yen post's six-row table with volatility column (supersedes the target's five-row table). Five-year bar chart: yen post's lead figure (caption retargeted to "this piece"). Currency paragraphs: target section 2; yen paragraph from the yen post's section 2 card |
| Volatility (#volatility) | Target section 3 + yen post section 3 (12.1%) + yen post section 4 (the "fourth category" reading). Bar chart: target's, with RUB updated to 52.3% and a JPY bar (12.1%, same px-per-% scale) added |
| EM ranking (#em-ranking) | Target section 3a |
| Reference rates (#reference-rates) | Target section 4 (added the plain observation that JPY and AED are on FBIL's list, which is the target's own list) |
| Benchmark (#benchmark) | Target section 5, incl. regime table |
| NEER/REER (#neer-reer) | Target section 6 |
| Trade table (#trade) | Target section 7; note added that Japan is not in the table because the yen is here as a borrowing currency |
| Carry trade (#carry-trade) | Yen post section 5, plus the yen post's 22 Oct 2026 update box (BoJ to 1.25% on 18 Sep 2026) folded into the text with its three links |
| Rupee-settled trade (#rupee-trade) | Target section 8, lightly trimmed |
| What would fix this | Target's 4 + yen post's 3 proposals merged to 5 (FBIL items merged; the two NEER/REER items merged) |
| What this piece could not establish | New merged section from: yen post's "What this piece does not establish" card, target's REER caveat (section 6 card), SAR upper-bound and pre-1993 caveats (target sources note), 7 Nov "not rechecked" note, and the chart/table conflict below |
| Related | Union of both lists, minus the cluster link (yen post linked to the target) |
| Documents & sources | Both source notes merged, deduplicated; all links from both posts listed (MSEI, Nippon.com, InvestingLive, Babypips, Wikimedia Commons) |

Head (lines 1-29, style), the accessibility bar, translate widget, and everything after the sources card (closing div, disclaimer, accordion script, RBI image) are byte-identical to the target's current file.

## Number conflicts and how they were resolved

1. **RUB/INR volatility: 52.2% (target, chart and text) vs 52.3% (yen post table and text).** Used 52.3% (newer post) everywhere, including the bar chart.
2. **Indexed chart line-end labels: target labels USD/AED/SAR 148, CNY 145, RUB 104; yen post labels USD/AED/SAR 142, CNY 141, RUB 112, JPY 92.** The polylines are identical in both posts. Their end points sit at 142 / 141 / 112 / 92 on the axis (y = 52.5, 57.2, 161.8, 233.0 at 3.6 px per index point), so the yen post's labels match the plotted data; the target's labels match the table's 10-year column instead. Used the yen post's chart and labels (newer and geometrically consistent).
3. **Chart vs table, unresolved:** the chart ends (142, 141, 112, 92) do not match the table's 10-year changes (+48.0%, +44.8%, +4.1%, +3.5%). For the yen they point in opposite directions (chart below 100, table +3.5%). Both posts published both figures with no reconciliation, and I cannot recompute without the data. The text now quotes both and says so; the conflict is listed under "What this piece could not establish". Not resolved; needs the raw series. (Possible cause, not stated in the post: the polyline is down-sampled and its last point may not be the 14 Aug 2026 close.)
4. **Target text "rouble sits at just 104"** replaced by the chart's 112 plus the table's +4.1% (per conflicts 2 and 3).
5. **Target text said CNY had the fastest 1-year AND 3-year depreciation "of the five"**, but the same table shows RUB 3-year +32.0% (which the target itself calls "the largest of the five"). Reworded: fastest 1-year (+15.5%), second-fastest 3-year (+24.0%) after the rouble.
6. **Yen post said every other currency weakened the rupee "by double digits" over five years**; RUB 5-year is +9.4%. Reworded to "by 9.4% to 26.7%".
7. **Target text "the rupee buying about 45-48% more of the dollar..."** had the direction backwards (the rupee buys less). Reworded to "it takes about 45-48% more rupees", using the table's +44.8% to +48.0%.
8. **Target said USD is the pair "every other pair ... is measured against, since none of the other four trade INR directly".** With the yen added (JPYINR=X is a direct series), reworded to: the dollar is the pivot through which the yuan, rouble, riyal and dirham series are derived (matches the sources note: AED=X combined with USDINR).
9. **BoJ path:** yen post body "1.00% by June 2026, the highest since 1995"; its 22 Oct 2026 update "1.25% on 18 Sep 2026, highest since 1995". Kept both in sequence, as the change itself (risk has grown) matters, with the update's links.

## Dropped, and why

- Target's five-line indexed chart: superseded by the six-line chart (same five polylines plus JPY).
- Target's five-row table: superseded by the six-row table with volatility column.
- Yen post's section 2 table rows for the five currencies: duplicated the target's table (merged into one).
- Yen post's pull quote ("...and that wasn't a coincidence"): editorial, repeats the yen paragraph.
- Yen post's 22 Oct "Updated" box as a separate box: its content is now in the carry-trade section with the same three links.
- Internal "Section N" cross-references: replaced with #anchor links or plain words. Text references to the folded/target post by title ("Where the Rupee Actually Stands", "The Currency the Rupee-Trends Piece Left Out", also in the bar chart caption) removed.
- Related-link to where-rupee-actually-stands-ten-years from the yen post: removed (cluster link).
- Section numbering in headings dropped; headings rewritten as plain statements.

## Checks

- `_local_check.py` FAIL count: 0 (target current file: 0).
- html.parser tag balance: no errors, nothing unclosed.
- No "masaladeutsch.blogspot.com" or "Masala Deutsch" (the accordion.js script URL on herrrickshaw.github.io/masaladeutsch is in the preserved tail, unchanged).
- Size: 68,852 bytes vs inputs 51,626 + 38,704 = 90,330. Words (text outside script/style/svg): 5,571 vs inputs 4,100 and 1,680 (limit about 6,150).
