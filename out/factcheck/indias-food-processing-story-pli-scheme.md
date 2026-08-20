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
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The article claims 3.39 lakh jobs were created against a 2.5 lakh target, but the table later states the target was for 2026 (implying a deadline), while the jobs figure is as of June 2026. However, the target is not explicitly dated in the claim, and the jobs figure (3.39 lakh) exceeds the target (2.5 lakh) by a significant margin, which may be correct. The primary issue is that the claim conflates "target" with a deadline (2026-27), which is not the same as the numerical target. The numerical target is 2.5 lakh jobs, and the jobs created (3.39 lakh) exceed it, so the claim is factually correct in terms of numbers but misleading in phrasing. [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but does not provide a primary source or methodology. Without a verifiable NABARD or MoFPI study, this cannot be confirmed as accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "Sales of PLI-supported products nearly doubled, from ₹58,758 crore in FY2019-20 to ₹1,08,854 crore in FY2025-26, and export sales from the scheme's beneficiaries have grown at a 13.23% compound annual rate since 2019-20." — The article implies that the PLI scheme directly caused the doubling of sales and the 13.23% CAGR in export sales. However, correlation does not equal causation. The growth in sales and exports could be due to other factors such as global demand, domestic policy changes, or general industry trends. The article does not provide evidence linking the PLI scheme's incentives to these outcomes. [confidence: high]

- "The structural shift is the more interesting number: processed food's share of India's total agricultural exports has risen from 13.7% to 20.4% over the last decade — the country is exporting less raw commodity and more value-added product than it did ten years ago." — While the share of processed food in agricultural exports has increased, this does not necessarily mean India is exporting "less raw commodity." The total volume of raw commodity exports could still be rising, just at a slower rate than processed food exports. The article conflates a rising share with an absolute decline in raw commodity exports, which is not supported by the data presented. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
