# Fact/interpretation check — indias-food-processing-story-pli-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-food-processing-story-pli-scheme.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

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
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The article claims jobs created are 3.39 lakh (339,000) against a 2.5 lakh (250,000) target, but the chart and text show the target is 2.5L (250,000) and jobs created are 3.39L (339,000), which is correct. However, the phrasing "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" is accurate, so no factual error here. [confidence: high]
- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but does not provide a primary source or methodology. Without verification from a primary NABARD or MoFPI study, this cannot be confirmed as accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "India's food processing PLI scheme has created more jobs than it promised, ahead of its 2026-27 deadline." — The article claims the PLI scheme "has created more jobs than it promised, ahead of its 2026-27 deadline," but the data shows jobs created as of June 2026 (3.39 lakh) against a 2026 target (2.5 lakh). While the jobs created exceed the target, the scheme's deadline is 2026-27, and the data is only through June 2026, which is not the full deadline period. The conclusion that the scheme has "beaten its own targets ahead of its deadline" is an extrapolation beyond the available data. [confidence: high]
- "The structural shift is the more interesting number: processed food's share of India's total agricultural exports has risen from 13.7% to 20.4% over the last decade — the country is exporting less raw commodity and more value-added product than it did ten years ago." — While the percentage increase in processed food's share of agricultural exports is correct, the article implies this is solely due to increased value addition in exports. However, the rise could also be influenced by other factors such as changes in raw commodity export volumes, policy shifts, or global demand fluctuations. The causal link between the percentage increase and a structural shift toward value-added exports is not firmly established. [confidence: medium]
