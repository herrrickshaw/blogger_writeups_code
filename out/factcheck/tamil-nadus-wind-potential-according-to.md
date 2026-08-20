# Fact/interpretation check — tamil-nadus-wind-potential-according-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/tamil-nadus-wind-potential-according-to.html`

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
- "Tamil Nadu's installed wind capacity stood at roughly 11,938 MW as of 31 October 2025" — The date is in the future (2025) relative to the article's publication date of 14 August 2026, making it unverifiable and likely incorrect. [confidence: high]

- "NIWE's separate offshore assessment puts wind potential off the Tamil Nadu coast at roughly 35 GW" — The article acknowledges that offshore assessments vary across studies and years, and the 35 GW figure is sourced from "recent coverage" rather than a primary NIWE document. This introduces uncertainty about the exact figure. [confidence: medium]

INTERPRETATION ERRORS:
- "The utilisation math. ~11,938 MW installed against NIWE's 33,799 MW 100m-hub-height potential works out to roughly 35% utilisation — meaning nearly two-thirds of NIWE's own assessed onshore potential in India's most mature wind state remains unbuilt." — The calculation compares installed capacity (11,938 MW) to NIWE's 100m-hub-height potential (33,799 MW), but modern turbines operate at 120–150m hub heights, where the potential is significantly higher. The 35% utilisation figure is misleading because it understates the true potential at modern hub heights. [confidence: high]

- "Wind alone won't close that gap, but at 35% utilisation of NIWE's own onshore estimate and near-zero offshore development, it's the renewable resource with the most obvious unused headroom in the state's own numbers." — The article uses the 35% utilisation figure (based on 100m hub height) to argue that wind has "unused headroom," but this ignores the much larger potential at 120–150m hub heights. The conclusion overstates the actual unused potential. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
