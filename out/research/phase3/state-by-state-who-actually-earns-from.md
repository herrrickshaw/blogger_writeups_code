# Merge notes: state-by-state-who-actually-earns-from

Output: `out/update-2026-11-14-state-by-state-who-actually-earns-from.html`

New title (83 chars): State tax from ethanol blending in India: Rs 17,863 crore net loss at E20, by state

Folded in (all August 2026):
- a-tax-play-grow-ethanol-sgst-revenue (current file: out/update-2026-11-07-...)
- would-more-sgst-fix-donor-state-problem (posts/...)
- push-ethanol-sgst-rate-from-25-to-5-and (out/update-2026-11-07-...)
- the-case-for-biofuels-over-imports (out/update-2026-11-07-...)

Not folded: ethanol-blending-omc-books-e20-today-vs. All links to it kept.

## Sizes

| | bytes | words (text, scripts/styles stripped) |
|---|---|---|
| target (11-07 update) | 60,038 | 4,982 |
| a-tax-play | 45,920 | 4,501 |
| would-more-sgst | 32,029 | 2,232 |
| push-ethanol | 35,412 | 2,616 |
| case-for-biofuels | 32,978 | 2,467 |
| sum of inputs | 206,377 | 16,798 |
| merged | 89,702 | 7,239 (cap: 4,982 x 1.5 = 7,473) |

FAIL count (`_local_check.py`): target 0, merged 0. Tag balance clean. No old domain or old blog name.

## Where each section came from

- Header, chips, read-first callout, image: target. Lede rewritten for the merged scope.
- 1 Mechanism + production map: target s.1-2. Its 13 Oct (excise) and 7 Nov (tender) update boxes turned into dated notes inside the section.
- 2 State losses: target s.3.1-3.3 and s.4 (cards). Top-15 table gains push-ethanol's net-at-10% and net-at-15% columns (s.4 of that post) for the 10 states it covered; the separate push state-net table was dropped as a duplicate.
- 3 SGST rates: national table merges push s.2 + s.4 and biofuels s.1 (adds 18% row). One new chart combines the push chart (2.5-15%) and biofuels chart (2.5-18%). Dedicated-levy-by-blend table and top-5 E27 figures from target s.3.4-3.5 (top-5 table turned into a sentence). State SGST-by-volume table from push s.3. TN/Gujarat at 15% from push, at 18% from biofuels. Karnataka 2024 precedent from push s.5.
- 4 CNG VAT: a-tax-play Part 1 and 1.5. PNGRB VAT table and PNGRB price table merged into one table; PPAC CNG-sales table and outlet-density table merged into one table. Its 7 Nov update (Chandigarh, Ladakh, IGL price) became a table note. Segment cost/payback/sales mix/energy-content material from target s.5 condensed into one table plus two paragraphs; the six-metro city table was reduced to one sentence.
- 5 Donor states: would-more-sgst s.1-3, with its 13 Oct 16th Finance Commission update as a dated note. The donor chart was dropped (exact duplicate of the table); the table gains a net-ethanol-loss column from target s.3.2.
- 6 Proposal: lever table is a new arrangement of figures already in the posts. Option A/B and the ethanol-CNG package from a-tax-play Parts 2-3; crude-for-petrochemicals and "what states must agree to" from biofuels s.3-4; "does not solve" list merges a-tax-play's list, target's consumer callout and target s.5.5 (E20 extra-spend figures, now in prose).
- What would fix this: 21 proposals across five posts merged into five (see below).
- What this piece could not establish: target s.6 plus the caveats and disclaimers of all four folded posts.
- Sources: footer list merging every source line and link from all five posts, deduplicated.

In-cluster links (a-tax-play, would-more-sgst, push-ethanol, case-for-biofuels, and the target's own URL) were removed or replaced with in-page anchors (#state-losses, #limits). Links to other posts kept.

## Number conflicts and how they were resolved

1. National E20 net loss: ₹17,863 crore (target, push, biofuels table) vs ₹17,865 crore (would-more-sgst text, biofuels text and chart). Used ₹17,863: it equals 19,485 - 1,622, and the biofuels post's own table shows -17,863.
2. National E30 net loss: ₹26,795 crore (target table and chart) vs ₹26,792 crore (a-tax-play, would-more-sgst). Used ₹26,795 from the source model table. Option B's E30 ratio stays "about 41%" either way.
3. State net loss today: target Karnataka 1,798 / Rajasthan 1,164 / Gujarat 671; push 1,797 / 1,163 / 670 (push recomputes from rounded volumes). Kept the target's model figures in the table and flagged push's figures in a note under the table. This is rounding of one model, not a changed figure.
4. CNG VAT range: biofuels said "from 3.3% to over 14%"; the PNGRB table it cites shows 0% (Delhi) to 15% (Odisha), and 3.3% is Punjab's DPNG rate. Used the PNGRB range.
5. Delhi CNG price: ₹76.08 (PNGRB Apr 2025), ₹80.90 (outlet snapshot 22 Jul 2026), ₹83.09 (cost-model city board, Jul 2026), ₹86.98 (IGL after 29 Aug 2026, newest). Kept the April 2025 figures for the tax arithmetic, as the posts did, and listed all four in a note with ₹86.98 as the latest.
6. Crude substitution and forex: 244 lakh tonnes / ₹1.84 lakh crore (original biofuels) vs 316 lakh tonnes / ₹1.97 lakh crore to June 2026 (biofuels 7 Nov update). Used the newer; older and the Outlook Business ₹1.90 lakh crore / 310 lakh tonnes (to May 2026) are mentioned/cited.
7. PPAC data year: the target labels its state volumes PPAC Ready Reckoner FY2025-26 H1; push and biofuels say FY2024-25 full year and state that they reproduce the target's volumes. Could not reconcile; both stated in the caveats.
8. Push s.3 said "even at 15%, no state gets more than about half its loss back", but its own s.4 shows Tamil Nadu at 86.9% closure at 15%. Dropped the s.3 sentence.
9. a-tax-play said the SGST piece "did not publish petrol VAT figures for Odisha, Chhattisgarh or Madhya Pradesh"; the target's current top-15 table does (28%, 24%, 29%). The merged text gives those rates and net losses, says Jharkhand and Puducherry are not in the petrol model, and says the ethanol-CNG balance for those states was not modelled (no new claim).
10. would-more-sgst said Telangana, Karnataka and Maharashtra are "the three most exposed" to the ethanol shortfall; by the target table Uttar Pradesh (₹1,776 crore) loses more than Telangana (₹1,264 crore). Rephrased to "among donor states, the loss is largest in Maharashtra, Karnataka and Telangana".
11. Target chart caption said states lose "roughly three times more" in VAT than they gain in SGST; the figures are ₹19,485 vs ₹1,622 crore at E20. Caption rewritten to give the two figures without a ratio.
12. Central excise: target's ₹19.90/litre is superseded (13 Oct update: cut by about ₹10/litre in March 2026). Mechanism text no longer quotes ₹19.90 as current; the Union excise-loss range is kept with the "overstated" caveat.
13. Petrol volumes +6.5% in 2025-26 (push/biofuels/a-tax-play 7 Nov updates): stated once in Section 3 as applying to all rupee figures.

## Dropped, and why

- a-tax-play opening chart (VAT foregone / SGST / net E20 / net E30): every figure is in the Section 2 table and chart.
- would-more-sgst donor chart: same data as the donor table.
- push-ethanol and biofuels rate charts: replaced by one combined chart.
- push state net table (separate): merged into the top-15 table.
- Target six-metro city cost table: reduced to the Delhi-Hyderabad range and the ₹101.5-115.7 pump-price spread.
- Target separate payback table and E20 extra-spend table: merged into the segment table and prose respectively.
- Images: kept the target's sugarcane photo and a-tax-play's CNG station photo (moved to Section 4); dropped the sugarcane-field, HP pump and sugar-factory photos (decorative).
- Repeated restatements of the VAT/GST mechanism (in all five posts), repeated "27% for parity", "3-18%" and the energy-content callout (target and a-tax-play).
- Verdict boxes and "Related on this blog" blocks of the folded posts: their claims are in Sections 3, 5 and 6; the out-of-cluster related links moved to the Sources list.
- "What would fix this" proposals not carried (21 merged to 5, per the 3-5 rule): DFPD state-wise built capacity; Finance Ministry effective-devolution share; GSTN effective-GST-share table; Finance Commission ratio under alternative formula; PPAC refinery product slates; MoPNG method for cumulative savings. The IGST study and density/blend-volume points were folded into the kept items.
- Old dated update boxes (13 Oct excise; 7 Nov tender; 7 Nov CNG VAT/IGL; 7 Nov petrol volumes; 7 Nov forex; 13 Oct 16th FC): their facts and source links are kept as dated notes in the relevant sections.
