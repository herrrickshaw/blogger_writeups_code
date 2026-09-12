# Data validation — a-million-wine-market-behind-150-wall

> **Tests 2 and 3 are model output, not verified fact.** A flagged claim is a
> prompt to check the cited primary source, never a reason to edit the post
> on its own. Test 1 is deterministic.

Source: `posts/a-million-wine-market-behind-150-wall.html` · title: A $195 Million Wine Market Behind a 150% Wall, and the Deal That Cracks It · printed date: 30 August 2026
Run: 2026-09-12T23:21:22+00:00 · endpoint: http://localhost:20128 · model: gemini/gemini-3.6-flash

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
| table-units-in-header | MINOR | PASS | 25% |

10/10 passed.

## 2. Internal consistency (LLM)

No mismatches or arithmetic problems reported.
_The post was audited for internal consistency across text, tables, chart labels, and captions. All reported figures, calculations (including the 17.01% CAGR and percentage shares), and date references are internally consistent and fully supported by the provided text._

## 3. Claims ledger (LLM)

Status counts: consistent=18, stale_risk=3 · unsourced (model count): 0

| status | claim | source as cited | tier | note |
|---|---|---|---|---|
| **stale_risk** | Maharashtra had 35+ wineries across roughly 1,500 acres of wine grapes in 2022. | Ministry of Commerce & Industry / APEDA PIB release PRID 1832846 (10 June 2022) | primary | Cited from a 2022 government release in a post dated August 2026. |
| **stale_risk** | Sula Vineyards held 52.6% of the domestic 100%-grape-wine category in FY2021. | Sula Vineyards regulatory filings / IPO disclosures | primary | Historical data from FY2021 disclosures cited in an August 2026 post. |
| **stale_risk** | Sula Vineyards held roughly 61% of the Elite and Premium wine segments in FY2022. | Sula Vineyards regulatory filings / IPO disclosures | primary | Data from FY2022 disclosures cited in an August 2026 post. |
| consistent | India's wine market was worth US$195.3 million in 2023. | IMARC Group | analyst-estimate | Matches text, Table 1, and Chart 1. |
| consistent | India's wine market is projected to reach US$802.9 million by 2032 at a 17.01% CAGR. | IMARC Group | analyst-estimate | Matches text, Table 1, and Chart 1. |
| consistent | Per-capita wine consumption in India is approximately 9 millilitres per year. | Triangulated across trade and industry sources | secondary | Matches text and Table 1. |
| consistent | Wine represents approximately 0.5% to 2% of India's total alcoholic-beverage volume. | Trade and industry sources | secondary | Matches text and Table 1. |
| consistent | Only 1–2% of India's ~123,000 acres of vineyards are grown for wine grapes. | Industry estimates | analyst-estimate | Matches text details. |
| consistent | Tamil Nadu has roughly 2,800 hectares of total grape area. | Tamil Nadu State Horticulture data | primary | Matches Table 3 and text. |
| consistent | Theni district accounts for 78% of Tamil Nadu's grape area (2,184 ha) and 76% of state grape production (29,338 tonnes). | Tamil Nadu State Horticulture data | primary | Matches Table 3 and text. |
| consistent | Tamil Nadu was exploring wine production from grapes and cashew apples in July 2025. | Sommelier India (July 2025) | secondary | Matches text. |
| consistent | A winery built at Anamalayanpatti in Tamil Nadu has a stated capacity of ~75,000 litres per year. | Sommelier India (July 2025 reporting) | secondary | Matches Table 3 and text. |
| consistent | Sula listed on the BSE and NSE in December 2022 via a ₹960 crore offer-for-sale at ₹340–357 per share. | Sula Vineyards regulatory filings / IPO disclosures | primary | Accurately recounts historical IPO details. |
| consistent | Sula Vineyards drew over 3.3 lakh (330,000+) visitors in FY2025. | Sula Vineyards regulatory/company filings | primary | Matches text and Table 4 notes. |
| consistent | Fratelli Wines holds an estimated 25–30% market share. | Trade estimates | analyst-estimate | Matches Table 4 and text. |
| consistent | Grover Zampa Vineyards holds an estimated 7% market share. | Trade estimates | analyst-estimate | Matches Table 4 and text. |
| consistent | India's WTO-bound tariff ceiling on wine imports is 150%. | India's WTO commitments / trade reporting | primary | Matches Table 5 and text. |
| consistent | India and the EU reached a political trade agreement on 27 January 2026. | India–EU FTA trade reporting | secondary | Matches text and post context. |
| consistent | Under the India–EU FTA, wine tariffs will initially cut to 75% upon entry into force, phasing down to 20% (premium) and 30% (mid-range). | India–EU FTA trade reporting | secondary | Matches Table 5 and text. |
| consistent | Under the India–EU FTA, spirits tariffs will fall to 40% and beer tariffs from 110% to 50%. | India–EU FTA trade reporting | secondary | Matches Table 5 and text. |
| consistent | Millennials aged 25–34 make up roughly 45% of India's wine-drinking base. | Industry/trade estimates | analyst-estimate | Matches text assertion. |

_All extracted factual and quantitative claims are accurately attributed to government statistics, company disclosures, analyst forecasts, or trade reporting. Data regarding state winery counts and company market shares relies on FY2021–FY2022 figures, presenting minor stale-data risk in an August 2026 post._
