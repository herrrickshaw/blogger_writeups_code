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
- "PSU oil companies' domestic LPG sales in April-June 2026 actually fell 15.6% year-on-year" — The article claims this figure is from PPAC's Q1 FY2026-27 report, but the report's actual data (as cited in the article) shows sales of 6.48 million tonnes for April-June 2026, with no explicit year-on-year comparison provided in the quoted text. The 15.6% figure appears to be an unsupported assertion rather than a direct quote from PPAC. [confidence: high]

INTERPRETATION ERRORS:
- "Rising connection counts and falling sales volume in the same quarter aren't automatically a contradiction — a high year-ago base, price or subsidy timing, or a one-quarter demand dip could each explain it" — While the article acknowledges potential explanations for the disconnect between rising connections and falling sales, it does not critically assess whether these factors are sufficient to account for the 15.6% decline. The claim implies that the gap is merely unexplained rather than potentially indicative of deeper issues (e.g., underreporting, data discrepancies, or methodological changes in PPAC's reporting). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
