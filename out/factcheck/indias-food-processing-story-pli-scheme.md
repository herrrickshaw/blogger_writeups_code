# Fact/interpretation check — indias-food-processing-story-pli-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-food-processing-story-pli-scheme.html`

## Gemini gemini-flash-latest

[Gemini API error 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The article states "3.39 lakh" (339,000) jobs created, but the table later clarifies this as "3.39 lakh" (339,000) vs. a 2.5 lakh (250,000) target. The phrasing "3.39L" is inconsistent with the rest of the text (which uses "lakh" spelled out) and could be misinterpreted as 339,000 vs. 250,000, which is correct, but the inconsistency in notation is a minor factual inconsistency in presentation. [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but does not provide a primary source or methodology. Without verification from NABARD or MoFPI, this cannot be confirmed as accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "India's food processing PLI scheme has created more jobs than it promised, ahead of its 2026-27 deadline." — The article claims the PLI scheme "overshot its own target" by creating 3.39 lakh jobs against a 2.5 lakh target. However, the target is for 2026 (the deadline year), and the data is as of June 2026. The claim implies the target was for the entire scheme duration, but the target may have been set for the cumulative period up to 2026-27, not a specific year. The overshooting could be due to early acceleration rather than exceeding the final cumulative target. The reasoning gap is whether the 2.5 lakh target was for the entire period or an annual target. [confidence: medium]

- "The structural shift is the more interesting number: processed food's share of India's total agricultural exports has risen from 13.7% to 20.4% over the last decade — the country is exporting less raw commodity and more value-added product than it did ten years ago." — While the percentage increase is correct, the conclusion that India is exporting "less raw commodity" is an overinterpretation. The rise in processed food's share does not necessarily mean absolute declines in raw commodity exports; raw commodity exports could still be growing in absolute terms but at a slower rate than processed food exports. The reasoning gap is conflating a rising share with an absolute decline in raw commodity exports. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
