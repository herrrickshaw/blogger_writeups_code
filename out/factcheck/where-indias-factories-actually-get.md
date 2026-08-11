# Fact/interpretation check — where-indias-factories-actually-get

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-indias-factories-actually-get.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99590, Requested 5907. Please try again in 1h19m9.407999999s. Need more tokens? Upgrade to Dev Tier today ]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 1,869,333 Rs cr implemented" — The correct figure for implemented industrial projects (Part B) from 2021–Dec 2025 is Rs 19,51,828 cr (as stated later in the article), not Rs 1,869,333 cr. The initial figure appears to be a typographical error or misformatting of the correct value. [confidence: high]

- "Appendix V is headed 'Up to Dec 2025' while Appendix VI says 'Up to Nov 2025' -- yet both grand-total to the identical Rs 5,83,096cr" — The article correctly flags this as an inconsistency in DPIIT's own document, but the figure Rs 5,83,096cr is not mentioned elsewhere in the article. This suggests a possible factual error in the claim itself, as the grand total for Part B (2021–Dec 2025) is Rs 19,51,828 cr, not Rs 5,83,096 cr. [confidence: high]

INTERPRETATION ERRORS:
- "Gujarat ... implementing 178% of same-period intent (the pre-2021 pipeline landing)" — The article attributes Gujarat's high conversion rate (178%) to the landing of pre-2021 pipeline projects, but it does not provide evidence or data to support this causal claim. The conversion rate is a same-period flow ratio, and the article acknowledges this, but the explanation for the high rate is speculative without further verification. [confidence: medium]

- "The 2023 Rs 18,778cr registers in IEM well before the Tata Electronics Assam OSAT plant's Feb–Mar 2024 approval, so it is unlikely to be that specific project — more likely earlier-stage electronics capex in the same broader investment wave" — While the article correctly notes the timing discrepancy, it extrapolates that the Rs 18,778cr in 2023 is part of a "broader investment wave" without providing evidence or data to support this interpretation. The claim assumes a causal link between the IEM data and the broader wave, which is not explicitly supported. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
