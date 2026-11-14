# Merge notes: lpgs-missing-number-7308-commission-and

- Target: lpgs-missing-number-7308-commission-and (base file out/update-2026-11-10-...)
- Folded in: the-lpg-distributors-commission-rose-16 (base file posts/the-lpg-distributors-commission-rose-16.html; no out/update file existed)
- Output: out/update-2026-11-14-lpgs-missing-number-7308-commission-and.html
- New h1 (87 chars): LPG distributor commission: ₹73.08, its 2012 real value, half petrol's UPI fee exposure

## Kept unchanged from the target
Style block, head-order block (index link, eyebrow; only h1 and standfirst rewritten), the margin-share SVG figure,
skip link, a11y bar and script, translate widget, revision line, Wikimedia image, disclaimer, accordion script.

## Where each section came from
| Merged section | Source |
|---|---|
| Stat tiles | T: 73.08, 7.76% (was 7.8%), 3,642cr; F: 16.71→73.08, 83→73, Rs 150. Dropped F's "Rs 70–73" and T's "2.0×" tiles (2.0× folded into the 7.76% tile) |
| Intro: "named and not numbered" | T "The gap this article closes" |
| Intro: current vs real rupees | F opening paragraph |
| How much to trust it | F, plus T's 17 Oct note (73.03 vs 73.08, 7.75% vs 7.76%) |
| #record: Exhibit 1 table, notes, line chart | F "The record" table and chart (replaces T Exhibit 1, a 4-row subset); T's "no entry after Oct 2023" note |
| #inflation | F "Three phases" (sub-heading "a jump, then a treadmill" made literal) |
| #delivery | F "What the commission pays for" |
| #price-share | F "Against the cylinder price" + bar chart |
| #upi-fee: margin, Exhibit 2, structure-vs-exposure para | T "What that number is worth as a margin" and its note box |
| #upi-fee: fee notified in 2026 | T's 7 November 2026 update box, moved into the body |
| #pool: Exhibit 3 | T "The pool this commission adds up to" |
| #pool: Exhibit 4 distributor month | F "A distributor's month, roughly" |
| #associations | F "What the distributors' associations say" |
| #compare | F "Compared with the pump and the kerosene dealer" |
| What would fix this | T (5) + F (4) merged to 5 items |
| What this piece could not establish | F "What is not known" + T "What this article does not establish" |
| Related | T fertiliser/gas list + F related list, minus the two in-cluster links |
| Sources | All links from both posts, deduplicated (Deccan Herald MDR, Moneylife, Goodreturns, PPAC page, upi-fees post kept once) |

## Number conflicts and resolutions
1. Commission rate ₹73.08 (PPAC page, CEEW 2024) vs ₹73.03 (Goa notice, March 2024): both posts already flagged it. Kept ₹73.08, stated ₹73.03 and its effect (7.75% vs 7.76%) once in "How much to trust it" and in the caveats list.
2. "Additional commission for sale at market-determined price": T's original Exhibit 1 note said January 2016 to August 2019 (₹0.06–₹0.63). T's own 17 Oct correction and F (PPAC table posted 4 July 2022) say it started 7 October 2012 at ₹0.75–₹0.82, then monthly ₹0.06–₹0.63 from December 2015, ending 1 August 2019. Used the corrected PPAC-table version; the January 2016 claim is gone.
3. Commission as share of price: T 7.76% (₹942, 7 August 2026) vs F 7.8% (₹942, 7 June 2026). Same figure at different rounding; used 7.76% in text and tiles, F's chart keeps its 7.8% label for June 2026.
4. Ujjwala refill rate: T uses 4.71 a year (FY2025-26) for its computation; F says "4.4 to 4.7 for Ujjwala homes". Not a conflict; both kept in their own contexts.
5. Commission pools: T's ₹3,642 crore (Ujjwala, from beneficiaries x refills) and F's ₹13,649 crore (all distributors, from sales volume) are different scopes and methods. Both kept in one section with T's caveat that non-PMUY refill rates were not established.

## Dropped, and why
- T's 17 October 2026 update box: its two corrections are now in the body; its link to the folded post is removed.
- T's 7 November 2026 update box: content moved into the #upi-fee section with its dates and links.
- F's "Updated 17 October 2026" box: it only listed additions that are now part of the body.
- F's Timeline table: every row repeats a date already in the record table or the text.
- T's Exhibit 1 (4-row subset of F's full table) and T's "2.0×" and F's "Rs 70–73" stat tiles: duplicates.
- T's h2sub teaser lines ("It wasn't missing from PPAC's own page", "Two things this article does not know"): headings now state findings.
- T sentence "larger in aggregate ... than the entire incentive scheme built to keep UPI free": repeats the 8x ₹437 crore comparison in the sentence before it.
- Links between the two posts (T's link to F in the 17 Oct box and F's links to T in Sources and Related): removed, words kept where needed.
- What would fix this: 9 proposals merged to 5 (CLAUDE.md rule asks for 3 to 5). The Ministry of Finance proposal (list categories in the fee notification) became an NPCI proposal to state LPG's fee category, because a fee has now been notified.
- Currency: F's "Rs" changed to ₹ in body text to match the target; F's two SVG charts keep "Rs" in their labels.

## Checks
- _local_check.py FAIL count: target before 0, merged 0.
- html.parser tag balance: no errors, nothing unclosed.
- No masaladeutsch.blogspot.com, no "Masala Deutsch".
- Size: inputs 32,861 + 39,003 = 71,864 bytes; merged 55,690 bytes. Words: inputs 2,116 and 2,986; merged 4,207 (limit about 4,479).
