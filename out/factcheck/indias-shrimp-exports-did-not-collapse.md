# Fact/interpretation check — indias-shrimp-exports-did-not-collapse

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-shrimp-exports-did-not-collapse.html`

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
- "Smartphones are now India’s single largest export line at $29.4 billion" — The article later states the correct figure as $29,363 million ($29.36 billion), not $29.4 billion. [confidence: high]

- "Total exports rise from $303,526 million to $441,452 million, a gain of 45.4 per cent" — The correct calculation is ($441,452 - $303,526) / $303,526 ≈ 45.44%, which rounds to 45.4%, so this is technically correct but misleadingly precise given the context. [confidence: high]

INTERPRETATION ERRORS:
- "Five of the six largest apparent export collapses are not collapses at all" — The article implies that the "apparent collapses" are due to recoding, but it does not provide evidence that all five cases are solely recoding-related. For example, the shrimp case shows a 95% drop in the old code but a near-flat total when the new code is included, which is a valid interpretation. However, the phrasing suggests a blanket conclusion without acknowledging that some declines might be partially real even if recoding plays a role. [confidence: medium]

- "Of lines that genuinely grew, 84 per cent grew on volume, not price" — This claim is based on a subset of 4,958 comparable lines, excluding large new lines like smartphones and refined petroleum products. The article does not clarify that this 84% figure does not represent the entire export book, which could lead readers to overgeneralize the finding. [confidence: high]
