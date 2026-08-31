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
- "Japan is in the first matcha shortage in its history." — The article itself cites the Global Japanese Tea Association describing the shortage as the first in history *beginning autumn 2024*, but the claim that it is the first in history is not verifiable as a factual statement about all of history (e.g., pre-2024 shortages may have existed but were not recorded or recognized). [confidence: medium]

- "Global matcha demand rose roughly eightfold in five years." — The article does not provide a source or specific timeframe for this claim, making it unverifiable. While the article mentions demand growth, the exact figure of "eightfold" is not attributed to a credible source or data set. [confidence: medium]

INTERPRETATION ERRORS:
- "India grows 342 times more tea than the world makes matcha." — This claim compares India's total tea production (1,370 million kg) to Japan's matcha output (4,000 tonnes or 4 million kg), creating a ratio of 342:1. However, this is an apples-to-oranges comparison because India's tea production includes all types of tea (black, green, etc.), while Japan's matcha output is a specific processed product. The ratio does not reflect actual production capacity for matcha, as it ignores India's lack of matcha-specific cultivars, processing methods, and market readiness. [confidence: high]

- "Matching Japan’s entire matcha output would take 0.29 per cent of India’s tea crop, or 0.58 per cent of Assam’s." — While the volume calculation is mathematically correct, this interpretation assumes that India could simply reallocate a small fraction of its tea crop to matcha production without addressing critical constraints like cultivar suitability (e.g., *Camellia sinensis* var. *sinensis* vs. *assamica*), shading requirements, or processing infrastructure (e.g., stone-grinding vs. industrial milling). The claim implies feasibility without accounting for these non-land constraints. [confidence: high]
