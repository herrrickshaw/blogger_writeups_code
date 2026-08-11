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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99338, Requested 2650. Please try again in 28m37.631999999s. Need more tokens? Upgrade to Dev Tier today a]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The article references data and allocations from the Union Budget 2026-27, which would not have been finalized or published by August 2026 (India's budget is typically presented in late February/early March). This date is likely incorrect or premature. [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely reported but acknowledges it could not trace it to a primary NABARD or MoFPI study with a stated methodology. Without verifiable sourcing, this claim cannot be confirmed as accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "Sales of PLI-supported products nearly doubled, from ₹58,758 crore in FY2019-20 to ₹1,08,854 crore in FY2025-26, and export sales from the scheme's beneficiaries have grown at a 13.23% compound annual rate since 2019-20." — While the sales figures may be correct, the article implies a direct causal link between the PLI scheme and this growth without controlling for other factors (e.g., general sector trends, inflation, or external demand shifts). The growth could be driven by broader industry dynamics rather than the PLI scheme alone. [confidence: high]

- "The structural shift is the more interesting number: processed food's share of India's total agricultural exports has risen from 13.7% to 20.4% over the last decade — the country is exporting less raw commodity and more value-added product than it did ten years ago." — The article correctly notes the shift in export composition but does not address whether this is *solely* due to increased processing capacity or if other factors (e.g., global demand trends, trade policies, or currency fluctuations) played a role. The conclusion oversimplifies the drivers of this structural change. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
