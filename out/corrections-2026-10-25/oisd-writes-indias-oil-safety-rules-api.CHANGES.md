# CHANGES: oisd-writes-indias-oil-safety-rules-api (findings 17)

**Recommended title change: optional.** Current: "OISD Writes India's Oil-Safety Rules. API Just Signed FIPI Up to Help Its Own Standards Reach Further." Body H1 left unchanged. The title's "Just Signed" is soft: the FIPI MOU dates from early 2024 (World Oil, 10 Apr 2024: "earlier this year", no day given). Suggested: "OISD Writes India's Oil-Safety Rules. API Has Spent a Decade Signing MOUs to Help Its Own Standards Reach Further." Author's call.

## Changes applied
1. **Standfirst + Section 3 framing**: "has spent the past two years signing memoranda of understanding with three of them - FIPI, OISD, and PNGRB" -> "has signed memoranda of understanding with three of them - OISD (2014), FIPI (2024) and PNGRB (February 2025)". Source: API International Usage Report 2025 ("API signed an MOU with OISD in March 2014"), https://api.org/-/media/APIWebsite/products-and-services/2025_Intnl-Usage_Report_web-final.pdf (India chapter, ~p.52); PNGRB press release https://pngrb.gov.in/pdf/press-note/20250225_PR.pdf ("signed ... on 10th of February 2025"). Why: OISD MOU is 12 years old, so "past two years" was wrong.
2. **Key-points list, "four bodies" bullet** and **Section 1 body paragraph**: "roughly a dozen OISD standards" -> six in the Petroleum Rules 2002 (21 distinct across four instruments). Source: https://www.oisd.gov.in/list-of-oisd-standards-in-various-statutory-regulations (6 Petroleum Rules 2002; 2 Gas Cylinder Rules 2016; 1 SMPV(U) Rules 2016; 16 Oil Mines Regulations 2017; I de-duplicated the lists in raw/17 and get 21 distinct, matching API's report "21 standards issued by OISD are cited directly"). The key-points bullet also had "PESO ... has adopted"; reworded to what OISD's list shows.
3. **Section 1 source note (gb-note)**: removed the "roughly a dozen" attribution to ifluids.com and the statement that oisd.gov.in could not be reached; now cites OISD's list and says OISD pages were read on 25 Oct 2026 (PESO/PNGRB Act text still not).
4. **"90 API standards ... in its technical regulations"** (key points, Section 2 body): -> "in its national standards and technical regulations" (API report category: "References to API standards the national standards and technical regulations of: Indonesia (149), Canada (106), Brazil (99), India (90)"). Ranking and numbers unchanged (confirmed). Section 5 caveat sentence updated the same way.
5. **API-FIPI date** (key points): "in April 2024, API signed" -> "by April 2024, API had signed" (World Oil, https://www.worldoil.com/news/2024/4/10/api-finding-common-ground-global-collaboration-fuels-progress-in-oil-and-gas/ says "Earlier this year"; the exact signing day is unknown).
6. **OISD/PNGRB MOUs** (key points, Section 3 paragraph, Section 3 source note): "comparable MOUs with OISD and ... an older MOU with PNGRB reported to be under renewal" -> OISD MOU March 2014, new PNGRB MOU 10 Feb 2025. Sources as in 1. Removed the unverified green-hydrogen-document / PNGRB-ASME claims.
7. **API RP 583 "$170"** (Section 2): "a paywalled $170 standard" -> "a paywalled standard (the first edition of May 2014 was priced at $170; later editions cost more)". Source: https://www.api.org/~/media/files/publications/whats%20new/583%20e1%20pa.pdf ("FIRST EDITION | MAY 2014 | 88 PAGES | $170.00"). "Later editions cost more" rests on search snippets only (2021 and 2026 listings); the author may prefer to drop that clause.
8. **Section 5 ("What doesn't follow")**: "a stated aspiration in an early-stage partnership" -> "...a programme that dates from 2014 with OISD and only from 2024-25 with FIPI and PNGRB". Depends on correction 1.
9. **"What would fix this"**: "so the 'roughly a dozen' figure carried by secondary sources is replaced by an official count" -> "so the six-standard list OISD itself publishes for the Petroleum Rules 2002 can be checked against PESO's own record".
10. **Sources and caveats**: replaced the "researched through web search ... could not reach" opener with the list of primary documents now read (API report, OISD list, PNGRB press release, World Oil, API RP 583 flyer) with links; updated the API-report and MOU caveat sentences.
11. **Correction note** (`.gb-note`, the only note class in this post's CSS) added before "Sources and caveats". No dateModified element in this post.

## Not applied / flagged
- **"121 standards and RPs"**: OISD's current list shows 105 entries; API says OISD "has issued over 120". Not a clear error (current vs all-issued). Left at 121; a clarifying sentence was added to Sources only.
- Section 4 comparisons (Aramco, EU PED, UK HSE), FIPI ~95 members, FIPI-IOCL meeting: not covered by the findings; unchanged.
- "Reports to the Safety Council", 1986 founding, offshore competent authority: confirmed on oisd.gov.in/about-us; no change.
- PESO text itself still unavailable (302).

## Ripples
- Bar chart (inline SVG, API usage report) values 149/106/99/90 unchanged and correct. Its caption "figures as stated in this article" left as is.
- Text claim "OISD, 121 standards" appears in several places (key points, Section 1, table row, fix list); all left.

## Verification
- diff vs original: 28 changed lines (`diff posts/oisd-writes-indias-oil-safety-rules-api.html out/corrections-2026-10-25/oisd-writes-indias-oil-safety-rules-api.html`); no CSS, script, Google Translate, AI-disclosure or gs-idx lines changed.
- tag counts (orig->new): <div 11->11; </div 11->11; <table 1->1; </table 1->1; <script 4->4; </script 4->4 (all unchanged).
- inline <script> blocks parsed with node: 2 blocks, ok, ok; script text identical to original.
