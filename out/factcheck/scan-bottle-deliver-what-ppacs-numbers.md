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
- "PSU oil companies' domestic LPG sales in April-June 2026 actually fell 15.6% year-on-year" — The article cites PPAC's Q1 FY2026-27 report for this claim, but the report's date is 1 July 2026, which is before the end of the quarter (30 June 2026). Sales data for a quarter cannot be finalized until the quarter ends, making this claim unverifiable or premature. [confidence: high]

INTERPRETATION ERRORS:
- "Active domestic LPG connections have grown from 14.9 crore in 2015 to 33.14 crore this July, a genuine, government-verified expansion" — While the growth in connections is real, the article conflates "connections" (which may include inactive or duplicate accounts) with actual "consumption" or "usage." The PPAC report does not clarify whether these connections are actively used, leading to an overstatement of the expansion's impact on actual LPG consumption. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
