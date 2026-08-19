# Fact/interpretation check — indias-coking-coal-dependency-and-biomass

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-coking-coal-dependency-and-biomass.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "...explaining why the 2021 Ministry of Steel–Russia MoU and SAIL's Russian-supplier trial (Section 1) were framed as deliberate diversification, not business as usual." — Section 1 contains no mention of a 2021 Ministry of Steel–Russia MoU or SAIL's Russian-supplier trial; the cross-reference cites text that does not exist in the article. [confidence: high]

INTERPRETATION ERRORS:
- "Domestic raw coking coal production stood at 59.6 MT in FY2024-25. The Ministry's target for FY2025-26 is 83 MT, rising to 140 MT by FY2029-30 — roughly a 2.4× increase from current output inside five years." — Apples-to-oranges comparison / extrapolation gap: The article uses raw coking coal production targets (140 MT) to imply closing the ~90% coking coal import gap, but imported coking coal is washed/clean metallurgical coal. Indian raw coking coal has high ash content and must be washed (typically yielding only ~35–50% clean coal). Furthermore, the article notes planned washery capacity will reach only 58 MT by FY2030, meaning the 140 MT raw production target cannot translate 1:1 into usable domestic coking coal to replace imports. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "54.17% year-on-year, from 12 MT to just 5.5 MT by December 2025 (down from 35 MT in 2022-23)" — The claim incorrectly states "December 2025" as the timeframe for the 5.5 MT figure, which is not a valid fiscal or calendar year reference. The correct timeframe should be December 2024 (FY2024-25), as the article itself later refers to FY2024-25 data. [confidence: high]

- "140 MT Mission Coking Coal's domestic production target for FY2029-30" — The article cites this figure without clarifying whether it refers to raw coking coal or washed coking coal. Mission Coking Coal's targets are typically for raw coal, but the context implies processed coal, creating ambiguity. [confidence: medium]

INTERPRETATION ERRORS:
- "The SAMARTH mandate isn't the only biomass-co-firing rule in force, and the sourcing for this section turned up something worth flagging rather than smoothing over: there appear to be two related but not fully reconciled compliance tracks, run by different bodies, with different phase-in percentages for the same period." — While the article correctly notes the discrepancy between CAQM's 3% and SAMARTH's 5% mandate for FY2024-25, it does not explain why this discrepancy exists or whether it reflects overlapping but distinct regulatory scopes. The lack of reconciliation is presented as a curiosity rather than an inconsistency requiring resolution, which could mislead readers about the nature of the policy conflict. [confidence: high]

- "The reason this pass-through mechanism exists at all is that biomass pellets cost meaningfully more than the coal they're displacing. Reported landed-cost figures put biomass pellets in the roughly ₹9,000–13,000 per tonne range against coal at around ₹5,000 per tonne — a gap wide enough that, in at least one regulatory cost estimate this piece found, co-firing at mandated levels added on the order of ₹0.13 per unit to the generation cost." — The article conflates the cost of biomass pellets in power plants (thermal coal co-firing) with their potential cost in steel-making (coking coal substitution). Since coking coal and thermal coal are not interchangeable, the cost comparison is an apples-to-oranges comparison that does not support the conclusion about biomass substitution in steel-making. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
