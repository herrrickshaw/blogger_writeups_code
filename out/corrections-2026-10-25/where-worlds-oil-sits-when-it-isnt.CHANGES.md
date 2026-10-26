# CHANGES: where-worlds-oil-sits-when-it-isnt (findings 11)

## AUTHOR DECISIONS (flag)
- **Prices basis.** The post's 14 Aug figures (Brent 87.23 / WTI 81.27 / 5.96) come from an OilPriceAPI live quote at 01:33 UTC; EIA's daily spot series (physical spot assessment) gives 92.02 / 83.99 / 8.03 for 14 Aug. I did NOT overwrite the 14 Aug OilPriceAPI figures (they are correctly attributed to that source and time); I added the EIA figure as a cross-check. For 25 Sep I REPLACED the secondary-reporting numbers (Brent ~104-105, WTI ~93, spread 11-12) with the EIA primary series (Brent 116.01, WTI 85.23, spread 30.78), because they differ by ~$11 on Brent and the post's own note says they were second-hand. The WTI print on 25 Sep (85.23) looks like an outlier (24 Sep 95.88; 28 Sep 99.37), so I also gave the neighbouring-day spread range ($18-25, 21-29 Sep excl. 25th; computed from raw/11 RBRTEd/RWTCd.xls). If you prefer to keep the futures-style numbers, revert items 2, 6 and 9 below. The post's conclusion (spread widened, shore-vs-ship pressure intensified) is unchanged in direction but the magnitude is much larger: "roughly doubled" is no longer true on EIA data (8.03 -> 18-31).
- **Cushing narrative.** The old reading ("little changed ... market holding inland storage down rather than rebuilding it") is contradicted by later EIA data (24.3M w/e 25 Sep; 27.6M w/e 16 Oct). I rewrote the sentence to say the reading held at the time of the 26 Sep update but no longer does.
- **"US officials cited roughly 60 ships"**: not in any fetched document; left in the 26 Sep update box and flagged as unverified in the sources list. Author may wish to delete it.

## Changes applied (location -> old -> new; source; why)
Sources: EIA series W_EPC0_SAX_YCUOK_MBBL (https://www.eia.gov/dnav/pet/hist_xls/W_EPC0_SAX_YCUOK_MBBLw.xls), RBRTE (https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls), RWTC (https://www.eia.gov/dnav/pet/hist_xls/RWTCd.xls), WCSSTUS1 (https://www.eia.gov/dnav/pet/hist_xls/WCSSTUS1w.xls); all re-parsed from raw/11 xls. Al Jazeera 25 Sep 2026 https://www.aljazeera.com/news/2026/9/25/whats-in-irans-seven-day-plan-to-reopen-the-strait-of-hormuz (raw/11/aj.html). The Diplomat 3 Aug 2026 https://thediplomat.com/2026/08/myanmars-depleted-oil-pipeline/ (raw/11/dip.html).
1. Stat card (SPR): "298.7M bbl reported 10 Aug 2026" -> "298.7M bbl of the week ending 7 Aug 2026 (EIA)". EIA: w/e 7 Aug = 298,694 kb. (284.6M, 39.9% confirmed; unchanged.)
2. Stat card (spread): "~$11-12/bbl ... nearly double the $5.96/bbl gap" -> "~$18-31/bbl on EIA daily spot, 21-29 Sep ($30.78 on 25 Sep, WTI print an outlier) against $8.03 on 14 Aug (originally $5.96 from a live quote)". EIA RBRTE/RWTC.
3. 26 Sep update box (Section 1): "Iran presented the US with a written road map ... proposing a up-to-60-day regional ceasefire and a phased reopening of the Strait within seven days" -> Iran put forward a plan "through intermediaries and Qatari mediation": fighting stops on all fronts, US lifts naval blockade and oil sanctions and releases frozen assets, Strait reopens after seven days; the 60-day period belongs to the June MoU. Al Jazeera (quotes in raw/11/aj.html). Dropped "written" (article says "through intermediaries"; nothing about writing).
4. Section 6, 14 Aug sentence: appended EIA cross-check (92.02 / 83.99 / 8.03) after the $5.96 figure.
5. Section 6, 25 Sep sentence: "roughly doubled: Brent ~$104-105 vs WTI ~$93, spread ~$11-12" -> EIA 116.01 / 85.23 / 30.78 with outlier caveat and $18-25 neighbouring range; "over the six weeks" clause kept, now notes EIA 14 Aug spread 8.03 is the comparison.
6. Section 6, Cushing: "little changed ... ~23.8 million barrels for the week ending 22 September 2026 ... not rebuilding" -> 23.7M for w/e 18 Sep (EIA: 23,748 kb; up from 21,482 on 11 Sep; no 22 Sep week), then later rebuild to 24.3M (25 Sep) and 27.6M (16 Oct). 22.566M for 7 Aug confirmed, unchanged.
7. Section 6 "Data sources checked" note: Tradingeconomics/ConvexTrade/OneValor attribution replaced by EIA daily spot series, with the spot-vs-futures basis caveat.
8. Section 7 pipeline table (China-Myanmar): "reporting as recent as Aug 2026 describes the line as running well under its designed throughput" -> The Diplomat (3 Aug 2026) says the Gulf tanker slowdown "further dented the pipeline's capacity to supply" China's western provinces; no throughput or utilisation figure, so none quantified. Priority-project claim (June 2026) confirmed and kept.
9. Sources list: Diplomat entry (now read in full, 3 Aug 2026, no throughput figure); EIA Cushing entry (23.748M w/e 18 Sep, later values, series link); Tradingeconomics entry replaced by EIA RBRTE/RWTC entry; Al Jazeera/PortWatch entry (read in full; PortWatch 1 transit 20 Sep and 2025 mean 85.5 confirmed from the public data service; 60 ships/day flagged as not found in primary source).
10. Visible correction note (class warn, as a <p>) inserted directly before the "Sources" h3. No dateModified element in the post.

## Not applied
- **Myanmar pipeline "Operational since 2017"**: The Diplomat says "completed in 2014"; crude flows beginning 2017 comes from other reports not verified here. Evidence unclear, so left. Author could write "built 2014, crude flows from 2017" if confirmed.
- **~1,820 nautical miles Malacca saving**: unverified in any fetched document; left as "reported".
- **OilPriceAPI futures curve / backwardation**: STILL UNAVAILABLE; existing caveat box stays.
- 714M bbl SPR capacity (BPC) not re-fetched; left. IEA OMR, ISPRL 39M bbl, Vortexa ~135M bbl floating storage: not checked.

## Title
No title change needed.

## Ripples checked
- Spread occurrences: stat card, Section 6 body, update box mentions "Brent-WTI figures" generically (fine), sources list. "doubled" removed everywhere (grep clean). Disclaimer paragraph lists SPR and other figures as confident; unchanged.
- No chart/JS data arrays in this post (only accessibility and translate script blocks, untouched).
- The 26 Sep update box still says Sections 1, 2, 6 were updated "with current SPR, Cushing and Brent-WTI figures"; still accurate as a statement of that update.

## Verification
    ## diff stat
    21
     where-worlds-oil-sits-when-it-isnt.html |   21 +++++++++++----------
     1 file changed, 11 insertions(+), 10 deletions(-)
    <div orig=      20 new=      20
    </div orig=      20 new=      20
    <table orig=       2 new=       2
    </table orig=       2 new=       2
    <script orig=       4 new=       4
    </script orig=       4 new=       4
    scripts parsed: 2, failures: 0
