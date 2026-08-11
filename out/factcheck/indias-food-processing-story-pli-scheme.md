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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99320, Requested 2650. Please try again in 28m22.08s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The article claims a publication date of 8 August 2026, but this is impossible as the current date is before that (as of the knowledge cutoff in April 2024). The date is likely a placeholder or error. [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but admits it could not trace it to a single primary NABARD or MoFPI study with a stated methodology. Without verifiable sourcing, this claim cannot be confirmed as accurate. [confidence: high]

INTERPRETATION ERRORS:
- "India's food processing PLI scheme has created more jobs than it promised, ahead of its 2026-27 deadline." — The article claims the PLISFPI scheme created 3.39 lakh jobs against a 2.5 lakh target by 2026, but it does not establish whether the 2.5 lakh target was for 2026-27 or an earlier year. The comparison may be apples-to-oranges if the target was set for a different timeframe. [confidence: medium]

- "The Union Budget 2026-27 allocated ₹4,064 crore to the Ministry of Food Processing Industries in total — ₹1,200 crore to PLISFPI, ₹1,700 crore to PMFME, and ₹915 crore to PMKSY, the scheme that funds cold-chain and processing infrastructure directly." — The article implies that the ₹915 crore allocation to PMKSY is insufficient to address the ₹92,651 crore annual loss from cold-chain gaps. However, it does not account for the fact that PMKSY funds infrastructure projects (e.g., cold-chain projects) that may address the capacity gap over multiple years, not just a single year. The comparison conflates annual loss with one-time or multi-year infrastructure investments. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
