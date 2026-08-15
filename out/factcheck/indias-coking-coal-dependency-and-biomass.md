# Fact/interpretation check — indias-coking-coal-dependency-and-biomass

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-coking-coal-dependency-and-biomass.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Used 7090, Requested 7836. Please try again in 14.63s. Need more tokens? Upgrade to Dev Tier today at https:/]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "54.17% year-on-year, from 12 MT to just 5.5 MT by December 2025 (down from 35 MT in 2022-23)" — The claim incorrectly states "December 2025" when the article text itself refers to "December 2024" in the context of FY2024-25 data. The year is wrong. [confidence: high]

- "140 MT Mission Coking Coal's domestic production target for FY2029-30" — The article text does not provide a source or context for this specific figure. While the Ministry of Coal's Year End Review 2025 mentions a target of 140 MT by FY2029-30, the article does not explicitly cite this as a claim, but the figure is presented as a standalone fact without attribution in the context of the article's structure. [confidence: medium]

INTERPRETATION ERRORS:
- "Stamp-charging is a coke-making technique that compacts the coal blend before it goes into the oven, which allows a higher proportion of India's own (lower-quality) coking coal to be blended in without compromising coke strength. The Ministry states this raises the domestic-coal share of the blend from roughly 10% to 30% — a real substitution of imported coking coal, achieved through process technology on India's own coal, not through a different material altogether." — The claim implies that stamp-charging directly substitutes imported coking coal by increasing the domestic share in the blend. However, the article does not provide evidence that this substitution reduces the *absolute volume* of imported coking coal, only that it increases the domestic share in the blend. The interpretation conflates a relative increase with an absolute reduction in imports. [confidence: high]

- "The SAMARTH mandate isn't the only biomass-co-firing rule in force, and the sourcing for this section turned up something worth flagging rather than smoothing over: there appear to be two related but not fully reconciled compliance tracks, run by different bodies, with different phase-in percentages for the same period." — The article highlights a discrepancy between the national SAMARTH mandate (5% for FY2024-25) and the CAQM Delhi-NCR rule (3% for FY2024-25) but does not reconcile or explain the gap. While the discrepancy is noted, the article does not clarify whether this is a policy inconsistency, a phased rollout, or an error, leaving the reader to infer a problem without providing analysis or context to interpret the discrepancy's significance. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
