# Fact/interpretation check — scan-bottle-deliver-what-ppacs-numbers

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/scan-bottle-deliver-what-ppacs-numbers.html`

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
- "PSU oil companies' domestic LPG sales in April-June 2026 actually fell 15.6% year-on-year" — The article cites PPAC's Q1 FY2026-27 report for this claim, but the report's date is "as on 1 July 2026," which is before the end of Q1 FY2026-27 (ending 30 June 2026). This is a temporal inconsistency, as the quarterly data cannot be finalized before the quarter ends. [confidence: high]

INTERPRETATION ERRORS:
- "Active domestic LPG connections have grown from 14.9 crore in 2015 to 33.14 crore this July, a genuine, government-verified expansion" — While the growth in connections is real, the article implies this directly reflects increased LPG consumption or usage. However, the same article later notes a 15.6% year-on-year *decline* in PSU OMCs' domestic LPG sales in Q1 FY2026-27, suggesting that connection growth does not necessarily correlate with consumption growth in that period. The article acknowledges this discrepancy but does not adequately explain why the two metrics diverge, leaving the causal link between connection growth and consumption growth unsupported. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
