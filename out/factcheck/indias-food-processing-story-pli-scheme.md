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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 97835, Requested 3208. Please try again in 15m1.152s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The article claims 3.39 lakh jobs were created, but the table below shows "Jobs created (vs. 2.5 lakh target) | 3.39 lakh." The discrepancy in units (3.39L vs. 3.39 lakh) is inconsistent, as "L" typically denotes 100,000, while "lakh" is 100,000. This suggests a potential typographical or numerical error in the claim. [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but notes it could not trace it to a primary NABARD or MoFPI study with a stated methodology. Without a verifiable source, this claim lacks credibility. [confidence: high]

INTERPRETATION ERRORS:
- "Sales of PLI-supported products nearly doubled, from ₹58,758 crore in FY2019-20 to ₹1,08,854 crore in FY2025-26, and export sales from the scheme's beneficiaries have grown at a 13.23% compound annual rate since 2019-20." — While the sales figures are correct, the article implies a causal link between the PLI scheme and this growth without providing evidence that the scheme directly caused the increase. The growth could be due to other factors like general industry trends, global demand, or other policies. [confidence: high]

- "Under PMKSY, 399 cold-chain projects have been approved to date. Against a stated annual loss of ₹92,651 crore and a 3.5-million-tonne capacity gap, a single year's PMKSY allocation of ₹915 crore is not sized to close it — it is sized to keep adding to it more slowly than the sector is growing around it." — The article correctly notes the scale of the cold-chain gap but incorrectly implies that the ₹915 crore allocation is insufficient to make any meaningful progress. The allocation may be part of a multi-year plan, and its impact should be evaluated over time rather than as a one-time fix. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
