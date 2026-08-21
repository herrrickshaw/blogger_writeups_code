# Fact/interpretation check — 574-gw-and-counting-indias-wind-fleet

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/574-gw-and-counting-indias-wind-fleet.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "India's wind fleet crossed 57,443 MW in June 2026, with Gujarat overtaking Tamil Nadu as the single biggest contributor for the first time." — Gujarat first overtook Tamil Nadu as India's leading state in cumulative installed wind capacity in mid-2023 (May/June 2023, reaching ~10,415 MW vs. Tamil Nadu's ~10,125 MW), not in 2026. [confidence: high]

INTERPRETATION ERRORS:
- "Part of why the FY2025-26 growth rate jumped is a 7 December 2023 MNRE circular, the National Repowering & Life Extension Policy for Wind Power Projects..." — False causal claim. The article attributes the surge in new wind additions to the repowering policy without establishing that repowered projects contributed significantly to the newly commissioned MW. In practice, utility-scale wind additions in India are overwhelmingly greenfield projects won via central/state SECI auctions; repowering remains constrained by fragmented micro-ownership, existing long-term PPAs, and grid-connectivity legacy issues. [confidence: high]
- "India's entire 57.4 GW fleet represents barely 8 per cent utilisation of the national onshore resource NIWE itself has mapped. That gap isn't a wind-resource problem... it's a build-out problem..." — Extrapolation / false equivalence. NIWE's 695.5 GW figure represents gross theoretical and technical potential assuming a uniform 2% land availability across entire resource areas. Equating unbuilt theoretical potential directly to an execution/build-out shortfall ignores economic viability, local land use zoning, environmental/forest clearances, and grid demand absorption limits. [confidence: medium]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India's wind fleet crossed 57,443 MW in June 2026" — The article later contradicts this by stating "India's cumulative installed wind capacity reached 57,443.39 MW by the end of June 2026," implying the figure is precise to two decimal places, which is unlikely for installed capacity data. [confidence: high]

- "GWEC's Global Wind Report 2025 credits India with adding 6.3 GW of new wind capacity in calendar year 2025" — The article later notes that MNRE's figure for FY2025-26 is ~6 GW, and explicitly states that these figures describe "overlapping but not identical periods" and should not be read as confirming each other. The claim implies direct confirmation, which is misleading. [confidence: high]

INTERPRETATION ERRORS:
- "India's entire 57.4 GW fleet represents barely 8 per cent utilisation of the national onshore resource NIWE itself has mapped" — The claim conflates "utilisation" with "installed capacity as a share of technical potential." NIWE's figures represent *technical potential* (theoretical maximum under ideal conditions), not *economic or feasible potential*. Using installed capacity as a share of technical potential does not measure actual utilisation or deployment efficiency. [confidence: high]

- "The resource was never the constraint — the build-out has been" — While the article correctly identifies build-out challenges (transmission, land, repowering), it extrapolates from state-level constraints to a national conclusion without demonstrating that these same constraints uniformly limit deployment across all states or that resource availability is not a binding constraint in any context. The causal claim is overgeneralized. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
