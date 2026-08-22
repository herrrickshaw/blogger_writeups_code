# Fact/interpretation check — 574-gw-and-counting-indias-wind-fleet

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/574-gw-and-counting-indias-wind-fleet.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India's wind fleet crossed 57,443 MW in June 2026" — The article later contradicts this by stating "India's cumulative installed wind capacity reached 57,443.39 MW by the end of June 2026," which is a more precise figure. The initial claim lacks the decimal precision and is thus inconsistent with the later, more accurate data. [confidence: high]

- "GWEC's Global Wind Report 2025 credits India with adding 6.3 GW of new wind capacity in calendar year 2025" — The article later notes that MNRE's data shows ~6 GW added in FY2025-26 (April-March), which is not directly comparable to GWEC's calendar-year 2025 figure. The claim implies these figures are directly comparable, which they are not due to differing timeframes. [confidence: high]

INTERPRETATION ERRORS:
- "India's entire 57.4 GW fleet represents barely 8 per cent utilisation of the national onshore resource NIWE itself has mapped" — The claim suggests that the 8% utilization is a direct measure of how much of the resource is being used, but it is actually a ratio of installed capacity to NIWE's *technical potential* at 120m hub height. This does not account for practical constraints like land availability, transmission capacity, or economic viability, which may limit actual feasible utilization to a lower percentage. [confidence: high]

- "The resource was never the constraint — the build-out has been" — While the article correctly identifies build-out challenges (transmission, land, repowering), it extrapolates this to conclude that the resource itself was never a constraint, which is an overgeneralization. The claim implies that resource availability was never a limiting factor at any stage, but early wind development in India was indeed constrained by resource assessment limitations and turbine technology, which NIWE's atlases later addressed. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
