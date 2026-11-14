# Phase 3 merge: indias-trade-balance-hsn-wise

- TARGET: `indias-trade-balance-hsn-wise`, from `out/update-2026-11-07-indias-trade-balance-hsn-wise.html` (66,326 bytes, 1,956 words)
- Folded in: `hsn-wise-historical-importexport-trends`, from `posts/hsn-wise-historical-importexport-trends.html` (36,226 bytes, 1,570 words; it has no out/update file)
- Output: `out/update-2026-11-14-indias-trade-balance-hsn-wise.html` (84,793 bytes, 2,866 words)
- New h1 (78 chars): India's trade balance and growth by HSN chapter: $334.3bn deficit in FY2025-26
- `_local_check.py` FAIL count: 0 on the target, 0 on the merged file. Tags balance. No old domain or blog name.

## Kept exactly as they were
- File lines 1-166 (style blocks, `.bulletin`/`.sheet`/`.masthead` openers), the JNPT photo figure, the skip link, the accessibility bar and its script, the translate widget, the source line, and the last four lines (disclaimer, gs-idx plus accordion.js, light-lock and dark-panel-guard styles).

## Where each section came from
| Merged section (id) | Source |
|---|---|
| Masthead dek and h1 | Rewritten from both deks |
| Main finding (verdict box) | Target verdict, reworded as a plain statement, plus the electrical machinery growth figures from the folded post |
| Stat strip (6 tiles, built by script) | 3 from the target (deficit, cover ratio, HS27), 3 from the folded post (81.5% concentration, HS85 exports +324.1%, HS71 exports -29.9%). The target's "+$150.3bn widened" tile went into the first tile's subtitle |
| 14 Nov update note | New, as the brief requires |
| `#totals`: deficit widened from $184.0bn to $334.3bn | Target trade chart and totals table. The 7 Nov update note (H1 2026-27) became a dated paragraph here. The 22 Oct "FY2025-26 has now closed, provisional" point went into the legend note |
| `#chapters`: deficit and surplus chapters | Target diverging chart and the 98-chapter table |
| `#import-growth`: top 12 imports hold 81.5% | Folded post sparkline grid and import table; the 81.5% and "Top 12 by value" caveats moved here from its errata |
| `#import-cagr`: import growth ranking | Folded post CAGR chart and legend note, plus its fertiliser photo |
| `#shape`: growth rates hide reversals | Folded post shape-check table and notes, condensed into one paragraph |
| `#export-growth` | Folded post export grid, table and note |
| `#momentum`: largest deficit chapters are not the fastest-growing | Folded post "Reading this against the deficit", plus the DPIIT corroboration (it appeared in BOTH posts, so it is now given once, here) |
| `#services` | Target services chart and table. The 22 Oct note's FY2025-26 BoP points (CAD about $25.2bn, combined deficit about $119bn) became a dated paragraph here |
| `#rupee` | Target "How this connects to the rupee's slide". The 22 Oct note's reserves update ($734.6bn, week ended 2 Oct 2026) is now in the text |
| `#validation` | Target cross-validation section. Its DPIIT paragraph points to `#momentum` |
| Errata | Both errata lists merged and shortened. The folded post's cross-validation bullet duplicated `#validation` and was dropped. Its scraping-method bullet duplicated the target's "How this was pulled" |
| What would fix this | 4 target bullets plus 4 folded bullets, which made 7. Target bullet 3 (open TRADESTAT interface with no session) and folded bullet 1 (bulk download of the full series) are now one bullet |
| What this piece could not establish | New. Neither post had this section. Built only from limits the posts state themselves (provisional FY2025-26, no quantity data, services not cross-checked with SERF, services stop at FY2024-25, DPIIT data are intentions, 2-digit level). One point comes from comparing the posts' own numbers (see the conflicts below) |
| Sources | New merged list: every external link from both posts (6 news links, 2 Wikimedia file pages, CC licence), plus the named primary sources (TRADESTAT, TIA, DPIIT linked by the domains the posts give; DGFT, PIB and RBI unlinked, as in the posts) |
| Related box | Kept the 8-digit trade book link. Removed the link to the folded post (it is in the cluster). Added the folded post's China priority-partners link |

## Scripts
- One inline chart script. It is the target's IIFE with the stat array replaced, followed in the same `<script>` by the folded post's IIFE with its own stat-strip block removed, so `#statStrip` is filled once. The folded code keeps its own closure, so `rowH` and `scale` do not clash with the target's.
- All IDs either script needs are present and unique: statStrip, tradeChart/Tooltip, totalsTable, divergingChart/divTooltip, chapterTable, servicesChart/Tooltip, servicesTable, importGrid, importTable, cagrChart/Tooltip, exportGrid, exportTable. I ran the script against a DOM stub and every target was filled.
- The live folded post had lost its `.panel-*` CSS and the `#cagrChart` height in an earlier normalisation, so its sparkline panels rendered unstyled. I added a small scoped `<style>` at the start of the article body for these, using the target's existing CSS variables. No media queries.
- accordion.js and the translate script each load once.

## Number conflicts and how they were resolved
- None between the two posts. Shared figures agree: HS27 imports 203,415.4 and exports 55,871.2; HS85 imports 104,852.7 and exports 53,976.3; the DPIIT IEM figures are identical in both.
- Inside the target there is rounding drift between the diverging-chart array and the 98-chapter table (HS31 -14,423.8 vs -14,423.9, HS88 -12,108.8 vs -12,108.9, HS87 16,612.1 vs 16,612.2, HS30 21,441.3 vs 21,441.4). It is left as is, because it is 0.1 of $1 million and lives in script data.
- Reserves: the target text said a "$728.5bn peak". Its own 22 Oct note says reserves later reached about $734.6bn (week ended 2 Oct 2026). Resolution: the text keeps the $728.5bn peak and $666.9bn trough as the history and adds the newer dated figure.
- FY2025-26 status: the original text said "not necessarily a complete fiscal year". The 22 Oct note says it has closed but is provisional. The newer wording is used.
- Fertilisers: the folded post's stat tile called fertilisers the "fastest-growing big import", but its own shape check calls the chapter volatile, not fast-growing. Resolution: the tile was dropped, and the text keeps the +118.9% figure with the volatility caveat.
- Flagged, not resolved: the TIA Portal FY2025-26 export total of $451.07bn equals, to the same digits, the target's own TRADESTAT FY2022-23 export total (451,070.0 US$ million). The post blames a data-vintage difference. A mix-up of fiscal years is equally possible. I did not check this against the source. It is stated in "What this piece could not establish". Worth a primary-source check before publishing.

## Dropped, and why
- Target static SVG "What's Driving India's Trade Gap, FY2025-26" (top 5 deficit and top 5 surplus chapters): all 10 values are in the scripted diverging chart, which shows 8 + 8.
- Folded static SVG "India's fastest-growing big imports" (5 chapters, total growth %): the same chapters and ranking are in the scripted CAGR chart, and the tooltips and import table give total growth.
- Folded masthead photo caption text was kept with the photo. The folded post's dek, eyebrow and colophon duplicated the target's.
- Stand-alone 22 Oct and 7 Nov "Updated" boxes: their facts and dates moved into the sections they update. Their "original text below is unchanged" lines are no longer true and were dropped.
- Some wording was cut to keep the length within the brief's limit (rhetorical lines such as "worsening, not improving" and "by design"). No figures were removed.
