# Fact/interpretation check — japan-ran-out-of-matcha-assam-just-sold

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/japan-ran-out-of-matcha-assam-just-sold.html`

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
- "Japan is in the first matcha shortage in its history." — The article cites the Global Japanese Tea Association describing the shortage as the "first in history" beginning autumn 2024, but this claim is not verifiable as a factual historical record. Matcha has been produced for centuries, and shortages (even severe ones) have likely occurred before, though not necessarily documented in this manner. [confidence: medium]

- "Global matcha demand rose roughly eightfold in five years." — The article does not provide a verifiable source for this specific figure. While demand has clearly surged, an "eightfold" increase over five years is an extraordinary claim that requires robust data (e.g., market reports or official statistics) to substantiate. [confidence: medium]

INTERPRETATION ERRORS:
- "India grows 342 times more tea than the world makes matcha." — This claim is based on comparing India’s total tea production (1,370 million kg) to Japan’s matcha output (4,000 tonnes). However, this is an apples-to-oranges comparison because India’s tea production includes all types of tea (black, green, etc.), while Japan’s matcha output is a specific processed product. The ratio does not reflect actual production capacity for matcha-specific tea (tencha), which is the relevant input. [confidence: high]

- "Matching Japan’s entire matcha output would take 0.29 per cent of India’s tea crop, or 0.58 per cent of Assam’s." — While the volume calculation is mathematically correct, this interpretation assumes that India’s existing tea crop (primarily assamica variety) can be directly converted into tencha suitable for matcha production without accounting for the specific cultivar requirements (e.g., sinensis varieties) or processing constraints (e.g., shading, de-veining, stone-grinding). The claim implies feasibility where none is guaranteed. [confidence: high]
