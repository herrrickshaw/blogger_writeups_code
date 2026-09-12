# Data validation — the-50-tariff-and-234-one-untangling

> **Tests 2 and 3 are model output, not verified fact.** A flagged claim is a
> prompt to check the cited primary source, never a reason to edit the post
> on its own. Test 1 is deterministic.

Source: `posts/the-50-tariff-and-234-one-untangling.html` · title: From 50% to 10%: How Three Tariff Regimes and a Supreme Court Ruling Reshaped What Hits India's Exports · printed date: 12 September 2026
Run: 2026-09-12T23:32:25+00:00 · endpoint: http://localhost:20128 · model: gemini/gemini-3.6-flash

## 1. House rules (static, deterministic)

| rule | severity | result | detail |
|---|---|---|---|
| js-parses | BLOCKER | PASS |  |
| no-disclaimer-in-script | BLOCKER | PASS |  |
| no-inverted-media-query | BLOCKER | PASS |  |
| dark-vars-locked | BLOCKER | PASS | n/a (no dark palette) |
| wpi-attribution | MAJOR | PASS | n/a |
| disclaimer-present | MAJOR | PASS |  |
| translate-widget | MINOR | PASS |  |
| index-link | MINOR | PASS |  |
| bw-override | MINOR | PASS | n/a (no dark palette) |
| table-units-in-header | MINOR | **FAIL** | 40% of 55 cells carry units |

9/10 passed.

## 2. Internal consistency (LLM)

No mismatches or arithmetic problems reported.
_The audit found no internal inconsistencies or arithmetic errors. All tariff rates, date intervals, percentage point changes, multiplier claims, and product-level duty figures across the prose, tables, and chart labels are fully consistent._

## 3. Claims ledger (LLM)

Status counts: cannot_verify_offline=1, consistent=14 · unsourced (model count): 0

| status | claim | source as cited | tier | note |
|---|---|---|---|---|
| cannot_verify_offline | Walmart received a $2.9 billion tariff refund following the February 2026 Supreme Court ruling. | Trade press / corporate disclosures | secondary | Factual claim cited from trade press/reporting; requires external verification of filing/refund details. |
| consistent | In August 2025, the US blanket tariff on Indian goods rose to 50% overnight following executive orders issued under emergency powers and a Russian-oil penalty. | US Executive Orders (2 April & 6 August 2025) / KPMG report | primary | Matches the post's detailed breakdown of the 25% reciprocal tariff plus the 25% Russian oil penalty taking effect 27 August 2025. |
| consistent | The US Supreme Court ruled in February 2026 that the International Emergency Economic Powers Act (IEEPA) did not authorize blanket tariffs. | US Supreme Court ruling | primary | Accurately reflects the post's narrative on the legal invalidation of IEEPA blanket tariffs. |
| consistent | As of July/September 2026, India faces a 10% Section 301 tariff, tying it with Bangladesh for the lowest rate among its peer group. | US Section 301 executive action / Federal Register | primary | Matches Section 301 duty details in text and Chart 1. |
| consistent | US AD/CVD duties on Indian solar cells and modules exceed 230% combined (~123% preliminary AD margin). | International Trade Administration / Federal Register / PV Tech | primary | Directly matches Table 1 details regarding solar module investigations initiated on 7 August 2025. |
| consistent | Indian frozen warmwater shrimp carries an AD duty of 2.71%–5.08% for named exporters (3.76% all others) and a CVD duty of ~5.6%–5.9%. | US Department of Commerce / Federal Register / Southern Shrimp Alliance | primary | Matches Table 1 figures derived from 2023-24 and 2024-25 administrative reviews. |
| consistent | Walmart sourced approximately 25% of its US-bound imports from India by 2023 against a target of $10 billion per year by 2027. | Walmart corporate announcements | primary | Cites company figures provided in prose. |
| consistent | CBP's Enforce and Protect Act (EAPA) recovered over $1 billion in evaded duties in 2026, approximately 300% above its historical annual average. | US Customs and Border Protection (CBP) EAPA program reporting | primary | Matches stats provided in Section 2 on AD/CVD evasion enforcement. |
| consistent | A 2026 EAPA evasion case on transshipped solar modules resulted in cash-deposit rates of 271% for Vietnam and 239% for China-wide exporters. | US Customs and Border Protection / Federal Register | primary | Accurately reflects Section 2 data on circumvention penalty rates. |
| consistent | The reciprocal-tariff executive order of 2025 included a 40% tariff specifically targeting transshipped goods. | KPMG India, 'U.S. Tariff Shifts' (September 2025) | secondary | Matches KPMG report summary detailed in Section 3. |
| consistent | India imposed a 12% safeguard duty on Chinese steel in April 2025 and notified the WTO in July 2025 of intent to suspend equivalent concessions against the US. | Government of India / WTO notifications / KPMG India | primary | Accurately represents India's trade policy counter-measures described in Section 3. |
| consistent | India exported $10.9 billion in smartphones to the US in FY25, accounting for 42% of India's total smartphone exports and 7.8% of US smartphone imports. | Ministry of Commerce and Industry & ITC Trade Map via KPMG India | primary | Matches Table 2 sector exposure metrics. |
| consistent | India exported $10.7 billion in textiles and apparel to the US in FY25, representing 29% of India's textile exports and 9.1% of US imports in the category. | Ministry of Commerce and Industry & ITC Trade Map via KPMG India | primary | Matches Table 2 sector exposure metrics. |
| consistent | India exported $9.8 billion in pharmaceuticals to the US in FY25, making up 40% of India's pharma exports and 6.0% of US pharma imports. | Ministry of Commerce and Industry & ITC Trade Map via KPMG India | primary | Matches Table 2 sector exposure metrics. |
| consistent | In August 2025, peak blanket tariffs for peer sourcing countries were 20% for Vietnam, 19% for Thailand, and 15% for Turkey, all falling to 12.5% under Section 301 by September 2026. | KPMG snapshot & Section 301 schedules cited in Chart 1 | primary | Directly matches comparative figures listed in Chart 1. |

_The post provides a well-documented narrative on US-India tariff changes and AD/CVD duties between August 2025 and September 2026. Quantitative claims and regulatory statuses are consistently supported by primary government filings, trade agency reports, and KPMG analysis._
