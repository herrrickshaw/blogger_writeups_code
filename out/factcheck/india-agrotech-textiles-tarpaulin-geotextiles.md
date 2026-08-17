# Fact/interpretation check — india-agrotech-textiles-tarpaulin-geotextiles

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-agrotech-textiles-tarpaulin-geotextiles.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "and the government has additionally granted full duty relief on commodity PE/PP imports to keep supply flush for downstream weavers." — India does not provide full duty relief (zero duty) on commodity polyethylene (PE) and polypropylene (PP) imports. Standard Basic Customs Duty (typically 7.5%) applies, and the government has actively enforced mandatory Bureau of Indian Standards (BIS) Quality Control Orders (QCOs) that restrict commodity polymer imports rather than liberalizing them. [confidence: high]

INTERPRETATION ERRORS:
- "By shipment count, India is the world's largest exporter of HDPE tarpaulin — 6,763 shipments, against Vietnam's 991 and China's 166 — moving mainly to the UAE, UK and Bhutan. This isn't a category India is trying to build; it's one it already leads." — Using shipment count (from shipment-tracking aggregators like Volza) as proof of global export leadership is an invalid metric. Shipment counts measure the number of individual consignment records rather than actual export volume (tonnage) or export value. Large exporters like China ship in massive consolidated container volumes, making shipment count an apples-to-oranges metric that does not substantiate the claim of global leadership. [confidence: high]
- "less than 30% of geotextile demand for National Highway Authority of India projects — a mandatory requirement under Ministry of Road Transport and Highways rules — is met by Indian MSMEs. The gap is filled by imports" — The author infers that because Indian MSMEs fulfill less than 30% of NHAI demand, the remainder is imported. This is a false dichotomy that overlooks large domestic (non-MSME) technical textile and geosynthetics manufacturers in India who supply major national infrastructure projects. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India is the world's largest exporter of HDPE tarpaulin by shipment count, with 6,763 shipments, against Vietnam's 991 and China's 166" — The article does not provide a source for the shipment counts of Vietnam and China, and the numbers seem unusually low for major exporting countries, but the claim about India being the largest exporter is supported by the provided Volza trade-data compilations [confidence: medium].
- "The ₹487 crore domestic shade-net/mulch-film consumption estimate" — The exact base year for this estimate is not stated in the article, which could affect the accuracy of the figure [confidence: medium].

INTERPRETATION ERRORS:
- "The 'less than 30% MSME-fulfilled' figure is specific to National Highway projects, not to agriculture-sector geotextile demand (canal lining, farm-pond liners) specifically" — The article uses the National Highway projects figure as a proxy for India's geotextile-manufacturing capacity gap, but this might not accurately represent the entire agriculture sector's geotextile demand [confidence: high].
- "Tarpaulin is the segment India built its own supply chain for, feedstock included. Geotextiles are the segment still being filled in from Germany, the Netherlands, China and South Korea — two products woven from similar-sounding fibres, opposite trade positions" — The article implies a direct comparison between tarpaulin and geotextiles, but they serve different purposes and have different manufacturing requirements, which might not make them directly comparable [confidence: medium].

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is the world's largest exporter of HDPE tarpaulin by shipment count, and its shade-net and mulch-film makers largely serve the domestic market without importing." — The claim conflates tarpaulin (HDPE) with shade-net and mulch-film (Agrotech), which are separate segments under the National Technical Textiles Mission (NTTM). While tarpaulin is a major export, shade-net and mulch-film are domestically focused, but the phrasing incorrectly implies all three are export-oriented or import-independent. [confidence: high]

- "This site's own TradeStat-based segment mapping (see the companion piece on India's technical-textiles feedstock loop) puts Agrotech at a stable net export surplus: FY2025-26 exports of $193M against imports of $100M, a net +$93M — down from FY25's $231M/$92M as exports softened 16.4% year-on-year." — The article cites "FY2025-26" and "FY25," which are not standard fiscal year notations for India (where FY25 would typically refer to 2024-25). The correct notation should be "FY25" for 2024-25 and "FY26" for 2025-26. [confidence: high]

INTERPRETATION ERRORS:
- "The 'less than 30% MSME-fulfilled' figure is specific to National Highway projects, not to agriculture-sector geotextile demand (canal lining, farm-pond liners) specifically — this piece could not find a canal-lining-specific import share, and the highway figure is used here as the best available proxy for India's geotextile-manufacturing capacity gap generally." — The article acknowledges the limitation but still uses the highway figure as a proxy for agriculture-adjacent geotextile demand (e.g., canal lining). This is an extrapolation beyond the data, as the import dependency in highways may not reflect the import dependency in agriculture-specific applications. [confidence: high]

- "Tarpaulin is the segment India built its own supply chain for, feedstock included. Geotextiles are the segment still being filled in from Germany, the Netherlands, China and South Korea — two products woven from similar-sounding fibres, opposite trade positions." — While the trade positions are contrasted, the claim implies a direct causal link between the products' "similar-sounding fibres" and their trade outcomes. However, the difference in trade positions is more likely due to regulatory requirements (e.g., mandatory use of high-spec geotextiles in highways) and technological sophistication rather than the fibres themselves. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
