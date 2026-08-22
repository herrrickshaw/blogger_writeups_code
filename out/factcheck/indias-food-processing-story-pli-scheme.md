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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The article claims 3.39 lakh jobs were created against a 2.5 lakh target, but the table later states the target was for 2026 (implying a deadline), while the jobs figure is as of June 2026. However, the target is not explicitly dated in the claim, and the jobs figure (3.39 lakh) exceeds the target (2.5 lakh), which is correct. No factual error found here. [confidence: high]
- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but does not provide a primary source or methodology. Without verification from NABARD or MoFPI, this cannot be confirmed as accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "India's food processing PLI scheme has created more jobs than it promised, ahead of its 2026-27 deadline." — The claim implies causation between the PLI scheme and job creation, but the article does not establish a direct link. The jobs figure could include indirect effects or pre-existing trends. [confidence: high]
- "The structural shift is the more interesting number: processed food's share of India's total agricultural exports has risen from 13.7% to 20.4% over the last decade — the country is exporting less raw commodity and more value-added product than it did ten years ago." — While the share increase is correct, the conclusion that this represents a structural shift toward value-added exports is an overgeneralization. Rice (a raw commodity) remains the largest agricultural export by value, as noted later in the article. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
