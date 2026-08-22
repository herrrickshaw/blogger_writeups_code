# Fact/interpretation check — top-15-chemicals-for-import

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/top-15-chemicals-for-import.html`

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
- "Annual Imports (FY25-26) : $2,800 million" (Ethylene) — The corrected figure is $44 million, as explicitly stated in the article's correction notice. [confidence: high]
- "Annual Imports (FY25-26) : $1,650 million" (Sulfuric Acid) — The corrected figure is $250 million, as explicitly stated in the article's correction notice. [confidence: high]

INTERPRETATION ERRORS:
- "FY30 Substitution Target : -80% (down to $275mn imports)" (Polypropylene) — The article later retracts the FY30 savings targets due to corrected import values, making the substitution target meaningless as it was derived from the retracted figures. The corrected Summary Table does not provide meaningful substitution targets, so the claim lacks valid support. [confidence: high]
- "YoY Growth : +81%" (Acetic Acid) — The corrected YoY growth is +2.6%, but the article still uses the retracted +81% figure to justify the chemical's priority status as a "red flag." This misrepresents the actual growth trend and undermines the reasoning for its inclusion as a high-priority import-substitution target. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
