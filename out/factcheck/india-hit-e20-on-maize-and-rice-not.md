# Fact/interpretation check — india-hit-e20-on-maize-and-rice-not

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-hit-e20-on-maize-and-rice-not.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Blending is at 20 per cent through ESY 2025-26, held month after month." — The article claims blending has held at 20% "month after month" through ESY 2025-26, but the cited sources (ChiniMandi, BioEnergy Times) do not provide monthly breakdowns to verify this claim. The only monthly data referenced is a half-year supply figure (515 crore litres in 6 months), which does not confirm consistent 20% blending across all months. [confidence: medium]

- "Maize alone is 45.7 per cent, up from 6.2 per cent in ESY 2022-23 — a sevenfold shift in three years." — The article states maize's share rose from 6.2% to 45.7%, implying a sevenfold increase. However, the exact figures cited in the table for ESY 2025-26 are 45.68% (not 45.7%) and 6.2% (ESY 2022-23). While mathematically close, the phrasing "sevenfold shift" is imprecise (45.68 / 6.2 ≈ 7.37, not exactly seven). [confidence: high]

INTERPRETATION ERRORS:
- "The target has been met. Blending has held at 20 per cent through the current Ethanol Supply Year. And the assumption behind the question turned out to be wrong." — The article concludes that the original feedstock assumption (that sugarcane would dominate ethanol production) was wrong because blending reached 20%. However, this conflates *achieving the blending target* with *validating the feedstock assumption*. The feedstock mix (grain-dominated) is unrelated to whether the 20% blending target was met; the target could have been achieved with any feedstock. The interpretation incorrectly implies that the feedstock outcome explains the target's achievement. [confidence: high]

- "The water argument changed address. Much of the case against cane-based ethanol was about irrigation intensity in Maharashtra and Karnataka. Maize is a far less thirsty crop, so on that specific metric the switch is an improvement." — While maize is less water-intensive than sugarcane, the article does not provide data to support this claim (e.g., water footprint comparisons). The conclusion that the switch "is an improvement" assumes maize's lower water use without quantifying or sourcing the comparison, making it an unsupported interpretation. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
