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
- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but does not provide a primary source or methodology. Without verification, this cannot be confirmed as accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "India's food processing PLI scheme has created more jobs than it promised, ahead of its 2026-27 deadline." — The scheme's target is for 2026-27, and the article claims jobs were created ahead of the deadline (June 2026). However, the data is through June 2026, which is before the end of the fiscal year 2026-27 (March 2027). The claim implies the scheme has already met its target before the deadline, but the data only shows progress up to June 2026, not completion. The interpretation that the scheme has "beaten its own targets" ahead of the deadline is not fully supported by the data presented. [confidence: high]
- "The structural shift is the more interesting number: processed food's share of India's total agricultural exports has risen from 13.7% to 20.4% over the last decade — the country is exporting less raw commodity and more value-added product than it did ten years ago." — While the percentage share increase is correct, the conclusion that India is exporting "less raw commodity" is an overinterpretation. The total agricultural export value may have grown, meaning raw commodity exports could still be increasing in absolute terms even as processed food's share rises. The article does not provide absolute export values for raw vs. processed commodities to support this causal claim. [confidence: high]
