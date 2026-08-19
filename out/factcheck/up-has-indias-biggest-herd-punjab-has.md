# Fact/interpretation check — up-has-indias-biggest-herd-punjab-has

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/up-has-indias-biggest-herd-punjab-has.html`

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
- "53.68cr India's total livestock population, 20th Livestock Census (2019)" — The correct figure is 536.76 million (53.676 crore), not 53.68 crore. The article rounds incorrectly. [confidence: high]

- "247.87 MT Milk production, 2024-25 — up 3.58% year-on-year, per BAHS 2025" — The article does not specify whether "MT" refers to metric tons or million tonnes. In the context of milk production, "MT" typically stands for million tonnes, but the article should clarify this to avoid ambiguity. [confidence: medium]

INTERPRETATION ERRORS:
- "Uttar Pradesh's position holds on raw output: it produces 15.66% of India's milk, more than any other state, consistent with its lead in cattle-plus-buffalo population." — While Uttar Pradesh's milk production share aligns with its herd size, the article implies a direct causal link between herd size and milk production without accounting for other factors like yield per animal, which vary significantly across states (e.g., Punjab's higher yield). The reasoning gap is assuming that herd size alone explains production share without considering efficiency. [confidence: high]

- "The headcount Parliament was given is a 2019 snapshot... Until the 21st Census numbers are released, every state-wise livestock-population figure the government cites — including the one placed on the record in December 2025 — is a 2019 measurement of a sector that has since grown at nearly 13% a year." — The article claims the livestock sector has grown at "nearly 13% a year" based on the 12.77% CAGR from FY2014-15 to FY2023-24, but this CAGR refers to milk production, not livestock population. The reasoning gap is conflating growth in milk production with growth in livestock numbers, which are distinct metrics. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
