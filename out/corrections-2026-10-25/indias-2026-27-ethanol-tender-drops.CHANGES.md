# CHANGES: indias-2026-27-ethanol-tender-drops (findings 16)

**Recommended title change: none.** The headline (drops cane juice, cuts maize Rs 3, cheapest-first) is not affected.

## Important note on the finding
The findings file says the post states Rs 2,320/quintal as the FCI rice price for the 2026-27 tender. It does not. The post's table gives Rs 2,320 only in the 2025-26 column (correct) and "no rice price stated" for 2026-27, and the prose already says Rs 2,390 for Nov 2026-Jun 2027. The real defect is attribution and caveats, so only those were fixed.

## Changes applied (5 text edits + 1 note)
1. **"One cost moves against distillers..." paragraph** (section "Prices: maize loses its premium"/FCI rice paragraph)
   - Old: "...according to a Rajya Sabha reply reported by Business Standard, while the tender keeps rice ethanol at Rs 60.32 a litre."
   - New: "...according to the Department of Food and Public Distribution's OMSS(D) 2026-27 policy order of 2 July 2026 (Rural Voice; also Outlook India), while the tender..."
   - Source: https://eng.ruralvoice.in/government-to-sell-fci-rice-for-ethanol-at-rs-2320-per-qtl-below-paddy-msp-omss-policy-2026-27-announced (raw/16/rv.html: "Rs 2,320 per quintal until October 31, 2026. From November 1 ... Rs 2,390"; order "issued by the Department of Food and Public Distribution on July 2") and https://www.outlookindia.com/national/fci-sold-rice-to-ethanol-distilleries-at-nearly-40-below-acquisition-cost (raw/16/ol.html: "For November 2026 to June 2027, ... Rs 2,390").
   - Why: neither Business Standard page in raw/16 (bs.html) contains 2,390; the figure comes from the policy order.
2. **"How much to trust it" paragraph**: "the FCI rice price for this year from a parliamentary reply as reported" -> "...from the DFPD OMSS(D) 2026-27 policy order as reported by Rural Voice and Outlook India". Same source and reason.
3. **Sources and caveats**: replaced "ChiniMandi pages were read through search summaries." with a statement that the ChiniMandi pages, Deccan Chronicle and Onmanorama were opened in full (findings fetch log: HTTP 200), plus a cited sentence for the Rs 2,320 -> Rs 2,390 rice price and the 7.2 million tonnes allocated for 2026-27 (Outlook India).
4. **Correction note** (existing `.gb-warn` class) added before "Sources and caveats".
5. No dateModified element exists in this post; nothing to update.

## Not applied
- BPCL tender 26985 terms (quarter split 300/300/250/250, 72 LMT FCI rice, 108 crore litre quarterly cap, 29 Oct due date, cheapest-first order, "no rice price stated"): the PDF returns 404 and no source reproduces them. **Not applied, left as is; the "read in full from a copy" wording in Sources is unchanged and the author should confirm they hold that copy.** Partial support found: Outlook India's 7.2 Mt (= 72 LMT) for 2026-27 matches the post's "72 LMT"; ChiniMandi/Deccan Chronicle confirm ~1,100 crore litres, maize Rs 68.86 from 71.86, bid validity 31 Oct 2027.
- "The portal itself could not be opened from here" caveat: still true (404), kept.
- Last-year figures, court cases, 26.4% / 276 / 479 / Rs 1,440 crore: findings mark CONFIRMED, no change.

## Ripples
None. No other figure derives from the FCI rice price. No script/chart data in this post depends on it.

## Verification
- diff vs original: 8 changed lines (`diff posts/indias-2026-27-ethanol-tender-drops.html out/corrections-2026-10-25/indias-2026-27-ethanol-tender-drops.html`); no CSS, script, Google Translate, AI-disclosure or gs-idx lines changed.
- tag counts (orig->new): <div 16->16; </div 16->16; <table 2->2; </table 2->2; <script 4->4; </script 4->4 (all unchanged).
- inline <script> blocks parsed with node: 2 blocks, ok, ok; script text identical to original.
