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

- "Total exports rise from $303,526 million to $441,452 million, a gain of 45.4 per cent" — The actual increase is (441,452 - 303,526)/303,526 ≈ 45.44%, which rounds to 45.4%, but the article does not specify the rounding method. While not strictly incorrect, the precision is misleading as the exact figure is 45.44%. [confidence: medium]

INTERPRETATION ERRORS:
- "Five of the six largest apparent export collapses are not collapses at all" — The article claims that five of the six largest apparent declines are due to recoding, but it does not provide evidence that these are the *largest* declines in absolute terms. The table lists declines in descending order of absolute value, but the claim implies these are the largest *relative* declines, which is not supported by the data presented. The article does not clarify whether "largest" refers to absolute or relative magnitude. [confidence: high]

- "Eighty-four per cent of growing export lines grew on volume, not price" — The article restricts this finding to codes that exist in both years with quantity data and at least $1 million of base value (4,958 lines), excluding new codes like smartphones and petroleum products. This subset is not representative of the entire export book, so the 84% figure does not apply to all growing lines. The claim implies broader applicability than the data supports. [confidence: high]
