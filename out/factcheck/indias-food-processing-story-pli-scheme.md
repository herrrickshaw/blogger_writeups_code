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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99682, Requested 2650. Please try again in 33m34.848s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The article references data through June 2026 and cites sources dated between September 2025 and June 2026, but the publication date of 8 August 2026 is impossible to verify as accurate given the timeline of cited data and the fact that the article itself notes it could not retrieve primary PIB releases (suggesting the article may not have been published yet or the date is incorrect). [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely reported but admits it could not trace it to a primary NABARD or MoFPI study with a stated methodology, meaning the figure's accuracy or source cannot be verified. [confidence: high]

INTERPRETATION ERRORS:
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — While the PLISFPI scheme did create 3.39 lakh jobs against a 2.5 lakh target, the article does not clarify whether these jobs are *direct* or *indirect* (as it later mentions both terms separately) or whether the target itself was for direct jobs only. This ambiguity risks double-counting or misrepresenting the achievement. [confidence: medium]

- "Sales of PLI-supported products nearly doubled, from ₹58,758 crore in FY2019-20 to ₹1,08,854 crore in FY2025-26" — The article attributes this growth solely to the PLISFPI scheme, but the sales figures include products from FY2019-20 (pre-PLISFPI implementation) and do not isolate the scheme's incremental impact. The growth could reflect broader sector trends unrelated to PLISFPI. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
