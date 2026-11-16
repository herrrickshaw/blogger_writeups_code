# Flag review ledger, 16 Nov 2026

Subagents reviewed the 73 unverified flags in `out/viz/leaf-flags.md` (chunks 01-10; chunk 08 report was still pending when this was written). Full text of reports 01, 07, 09, 10 is in this folder; the others were returned as text only.

Rule used: `posts/` is never edited. Every flagged slug has a verified edition, and publishing the edition replaces the post, so an error that exists only in the old post text is fixed by publishing the edition. Do not also publish `out/update-*` files for these slugs over the edition.

## Applied to the edition (viz_verify PASS)
| slug | change |
|---|---|
| the-rupee-fell-10-and-exports-grew-09 | "rupee fell 10.4%" -> 9.4% (spec top line and chart title; derived `(94.4-85.5)/94.4*10*10`). 10.4% is the dollar's rise in rupees |
| the-price-of-grain-msp-msv-and | photo caption "reaches most of the harvest" -> "a sizeable share of the harvest (36.3% of rice and 22.6% of wheat)". Edited in `edition.html` (frame text), so re-rendering from `posts/` would undo it |
| india-hit-e20-on-maize-and-rice-not | "setting a fifth of the blend" -> "setting a fifth of the ethanol" (22.25% is a share of ethanol, not petrol). `edition.html` edit, same re-render caveat |
| the-rbis-fcnrb-window-drew-133-billion | "What it means": $133bn is the 18 Sep RBI swap figure; $127.2bn was the 31 Aug close |
| the-price-and-tap-two-levers-behind | "roughly 6 lakh crore" of CRR + OMO + swaps -> 7.3 (2.5 + 3.5 + 1.3; derived.json). Edited in `edition.html` |
| iem-conversion-historical-performance | "largest year in the table" -> "largest full year in the table" (the partial 2025 row is higher at Rs 5.83L cr) |
| nano-urea-works-as-supplement-and-fails | caption: only the IFFCO-funded trial tested a quarter substitution; the Punjab trial tested only half. `edition.html` edit |
| europes-export-credit-agencies-are | chart title "far below the 2.15bn KfW loan" -> "below" (950m is 44% of 2.15bn) |

## Real errors that exist only in the old post text (edition already clean; fixed when the edition is published)
thirty-one-years-of-asking-parliament (2004 had 34 questions, not 39; "nearly three a month"); fbil-rates-vs-tradestat-volumes-does-fx (Russia is 3rd of the five by import value, not 5th); sugar-at-5570-kilo-why-cane-acreage (UP's gain is not "nearly" the other states' losses: 0.36 vs 0.60); india-exports-naphtha-and-benzene-its ("four straight years" is three rises); indias-12385-project-investment-grid ("less than a third" is 43%; "nearly a quarter" heading is 41%); new-zealand-opens-every-tariff-line-to ("eighteen months" is about nineteen); indias-lock-imports-hit-19784-million ("two orders of magnitude" is about 33-fold); abha-what-indias-14-digit-health-id (yearly additions fell from 21.6 to 12.3 crore in 2025); if-india-paid-brics-in-rupees-scenario ("a quarter" is 29%; UAE is not balanced: -26.5bn); indian-it-in-ai-era ("revenue per head rose everywhere" is four of five; "other four added staff" is three); engineering-and-auto-component-makers (26 companies/7.4% should be 28/7.2%; "14% of the filings" is of filer companies); india-ended-63-years-of-state-nuclear (three "took effect"/"law for nine months" leftovers; SHANTI is not yet in force); india-has-auctioned-141-commercial-coal ("doubled" is 1.85x); the-rupee (post wording, same as above); the-price-of-grain, india-hit-e20 (post wording, same as above).

also: the-price-and-tap (3 places say ~6, sum is 7.3); iem-conversion ("best year on record" ignores the partial-2025 row at 109.9%); nano-urea ("both trials agree it works at a quarter", and "level both say works" in the body).

## Not applied: needs an outside source or a decision
- indias-ev-localisation-deadline-just: amendment counts (table says 3 bus / 4 truck; heading says 4 / 5) depend on how the notification recitals count; China pause extension is already in the 16 Nov update note.
- india-rewrote-its-entire-maritime-legal: header "Revised 21 Sep v1.1.0" but body has a 7 Nov update; version bump is the maintainer's call.
- indias-epr-regime-just-got-teeth-and: "deadline just twelve days later" has no date or source (likely 31 Jan 2026).
- indias-trade-story-has-three-big-wins: "5.9%" combined H1 growth does not follow from 2.4% goods and 6.5% services at FY25 weights (about 4.3%); already superseded by the dated updates.
- new-zealand (2025-26 exports 566 vs about 480), lemon (Andhra 7.31 vs 9.06), the-sme-growth-fund (Rs 2,000 vs 4,000 crore), ahidf (29,610.25 vs 29,110.25), the-world-bank (unusually large vs unprecedented), indias-medical-device (IVD 9-31%), do-cbse-past-papers (14 of 20 papers), the-cluster-automotive (Rs 1,653 crore as about $200m), south-africa-lost-its-gulf-fuel-supply (6,000 nautical miles), indias-biofuel-rules (23 Sep hearing outcome).
- pli-medical-devices-coverage-and-gaps: 28 vs 27 projects is disclosed; two-open-source-health-prototypes-icu (582 - 131 = 451 vs 455 'to review': quoted tool output, check how frames_to_review is defined); indias-fertiliser-import-bill ($7.86 is below the raw 10% of basket; 'currently' is an August snapshot); india-built-offshore-insurance-hub (stale 'Vintage' paragraph only).
- Stale but already disclosed in dated notes: rooftop-solar, 574-gw wind, diesel-truck eggs, the-cbg-incentive-stack, indias-oil-fields (88.2 vs 88.7).

## Not errors (rounding or disclosed in the post)
Tourism 45.4 vs 45.5, charkha 20.4, wage 12.7, e100 Rs 109, quantum range, CSR 3.1%, matcha 342, diesel/CPI, jai-kisan, from-cane-to-code, epfos 14,500/14,520, samudra-manthan, FDI table, mercosur -4,860, ethanol tender 26.4, bankruptcy 9,528/9,531, cough syrup, idbi 3,392, spirulina range, gobardhan 19%, constitution-set date stamp, annexure-314 label, city-gas pool.
