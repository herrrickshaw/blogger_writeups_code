# Fact/interpretation check — indias-food-processing-story-pli-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-food-processing-story-pli-scheme.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "one widely cited estimate puts the annual economic loss from inadequate cold-chain and supply-chain infrastructure at ₹92,651 crore" — The ₹92,651 crore figure comes from the 2015 ICAR-CIPHET national study on post-harvest agricultural losses across *all* commodity groups (including foodgrains, oilseeds, pulses, sugarcane, milk, and fisheries), not losses attributable solely to a lack of cold-chain infrastructure. [confidence: high]
- "Published 8 August 2026... PIB/MoFPI PLISFPI progress data through June 2026 · Union Budget 2026-27 allocations" — The article cites future dates (August 2026), future budget allocations (Union Budget 2026–27), and data reported through mid-2026 that do not exist in historical record. [confidence: high]

INTERPRETATION ERRORS:
- "processed food's share of India's total agricultural exports has risen from 13.7% to 20.4% over the last decade — the country is exporting less raw commodity and more value-added product than it did ten years ago." — A rising percentage share in a rapidly expanding total export basket (total agri-exports grew from ~$32 billion to over $50 billion over the past decade) does not mean the absolute volume or value of raw commodity exports decreased; raw commodity exports grew in absolute terms even as processed food grew at a faster rate. [confidence: high]
- "Against a stated annual loss of ₹92,651 crore and a 3.5-million-tonne capacity gap, a single year's PMKSY allocation of ₹915 crore is not sized to close it..." — This is an apples-to-oranges comparison. PMKSY operates as a capital subsidy/grant-in-aid scheme to catalyze private investment (leveraging several times the public outlay in private capital), rather than directly funding 100% of infrastructure creation from the Union budget. Comparing the annual budgetary grant directly against total national losses or total capital cost misrepresents how the scheme funds capacity. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The article claims 3.39 lakh jobs were created against a 2.5 lakh target, but the table later states the target was 2.5 lakh (250,000), while the jobs created are 3.39 lakh (339,000). This is a misrepresentation of the numbers, as 3.39 lakh is greater than 2.5 lakh, not against it. [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure without providing a primary source or methodology. While widely cited, the lack of verifiable origin (e.g., no direct NABARD or MoFPI study is linked) makes it unverifiable. [confidence: medium]

INTERPRETATION ERRORS:
- "Sales of PLI-supported products nearly doubled, from ₹58,758 crore in FY2019-20 to ₹1,08,854 crore in FY2025-26, and export sales from the scheme's beneficiaries have grown at a 13.23% compound annual rate since 2019-20." — While the sales figures are correct, the article implies that the PLI scheme directly caused this growth without establishing causality. The growth could be due to other factors (e.g., general sector trends, inflation, or other policies), and the article does not control for these confounding variables. [confidence: high]

- "The structural shift is the more interesting number: processed food's share of India's total agricultural exports has risen from 13.7% to 20.4% over the last decade — the country is exporting less raw commodity and more value-added product than it did ten years ago." — The article correctly notes the increase in processed food's share of exports but does not account for the fact that raw commodities (e.g., rice) still dominate the export basket in absolute terms. The conclusion that India is "exporting less raw commodity" is misleading because the total export value of raw commodities may still be higher, even if their share has declined. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
