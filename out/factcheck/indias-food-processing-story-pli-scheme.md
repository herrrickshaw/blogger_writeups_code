# Fact/interpretation check — indias-food-processing-story-pli-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-food-processing-story-pli-scheme.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99599, Requested 2978. Please try again in 37m6.528s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The date is impossible as the article references data through June 2026 and mentions FY2026-27 allocations, which would not be available in August 2026. [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but acknowledges it could not trace it to a primary NABARD or MoFPI study with a stated methodology. Without a verifiable source, this claim cannot be confirmed as factual. [confidence: medium]

INTERPRETATION ERRORS:
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The article claims the PLISFPI scheme "created more jobs than it promised" but does not clarify whether the 3.39 lakh jobs are net new jobs or include existing jobs reclassified under the scheme. Without this distinction, the claim that the scheme "created" more jobs than targeted is unsupported. [confidence: high]

- "Sales of PLI-supported products nearly doubled, from ₹58,758 crore in FY2019-20 to ₹1,08,854 crore in FY2025-26" — The article implies this growth is attributable to the PLISFPI scheme, but the sales figures include pre-PLISFPI data (FY2019-20) and do not isolate the impact of the scheme. The causal link between PLISFPI and the sales growth is not established. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
