# Fact/interpretation check — 7186-litre-why-maize-is-indias-priciest

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/7186-litre-why-maize-is-indias-priciest.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Maize is the only one of the four crops with a clear, double-digit percentage decline this season. The national drop of 9.7 per cent hides much sharper state-level falls..." — 9.7 per cent is a single-digit decline, not a double-digit decline. [confidence: high]

INTERPRETATION ERRORS:
- "Maize's price premium over every other feedstock is the direct policy lever behind the demand-side story: it pays millers and grain processors more per litre to convert maize into ethanol than to run any other feedstock through the same process, C-heavy molasses included by a wide margin." — This conflates the gross ex-mill purchase price paid by OMCs (revenue per litre) with net processing profitability. Different feedstocks (maize, sugarcane juice, B/C-heavy molasses, damaged rice) have fundamentally different input costs per tonne, conversion yields (litres of ethanol generated per quintal/tonne of feedstock), and processing/energy requirements. A higher headline procurement price per litre does not inherently mean converting maize is more remunerative or profitable for distillers than using cheaper, higher-yielding, or byproduct feedstocks. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Maize-based ethanol volumes went from zero to nearly 500 crore litres in three years" — This claim is incorrect. The article later states that maize-based ethanol supply reached 498.49 crore litres in ESY 2024-25, but the "three years" timeframe is misleading because the ethanol programme's maize-based ethanol production started before ESY 2021-22 (as implied by the zero figure for that year), making the actual timeframe closer to four years (ESY 2021-22 to ESY 2024-25). [confidence: high]

- "Wheat is a rabi (winter) crop and maize/rice/sugarcane figures above are kharif; the four aren't measured in the same sowing window" — While technically correct, the article incorrectly implies that the acreage figures for wheat (Rabi 2025-26) and the kharif crops (Kharif 2026) are directly comparable in terms of timeframes. The wheat figure is a final estimate, while the kharif figures are in-progress snapshots, which are not equivalent for comparison purposes. The article acknowledges this but does not correct the misleading implication that they are comparable. [confidence: medium]

INTERPRETATION ERRORS:
- "Maize's price premium over every other feedstock is the direct policy lever behind the demand-side story: it pays millers and grain processors more per litre to convert maize into ethanol than to run any other feedstock through the same process, C-heavy molasses included by a wide margin." — The article correctly states that maize has the highest government-set price, but it incorrectly implies that this price premium alone explains the "demand-side story" of maize-based ethanol volumes rising to 498.49 crore litres. The oversupply of tendered capacity (1,776.49 crore litres offered vs ~1,050 crore litres required) suggests that the ethanol programme's capacity was built out ahead of actual feedstock availability, meaning the price signal may not have been the sole or even primary driver of the volume surge. The article acknowledges other factors (e.g., weather, input costs) but does not address this oversupply context in its causal claim. [confidence: high]

- "The ethanol programme's grain-processing and distillation capacity has already been built out well ahead of what a single season's lower planting can meaningfully constrain, at least for this cycle." — The article correctly notes the oversupply of tendered capacity but incorrectly extrapolates that this means "a single season's lower planting" cannot meaningfully constrain ethanol production. The oversupply refers to tendered capacity (offers to supply ethanol), not actual production capacity or feedstock availability. A decline in maize acreage could still reduce maize-based ethanol production, even if total capacity is oversupplied, because other feedstocks (e.g., rice) may not be substitutable in the short term due to policy or logistical constraints. The article conflates capacity oversupply with feedstock availability. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
