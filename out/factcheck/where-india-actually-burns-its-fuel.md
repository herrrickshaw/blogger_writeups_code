# Fact/interpretation check — where-india-actually-burns-its-fuel

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-india-actually-burns-its-fuel.html`

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
- "Delhi is the finding hiding in the slow column. The capital’s fuel sales grew 22% in sixteen years — a period in which its vehicle stock multiplied." — The claim that Delhi's vehicle stock multiplied is not supported by any cited data in the article. While fuel sales growth is stated as +22%, there is no verifiable evidence provided for the assertion about vehicle stock growth. [confidence: medium]

- "Delhi runs India’s densest gas transport network — 458 CNG station clusters and 19.6 lakh piped-gas connections on PNGRB’s May 2026 count" — The figure "19.6 lakh piped-gas connections" is not sourced or explained in the article. The PNGRB count is mentioned, but the specific number is not referenced in the cited sources (PPAC workbook or PNGRB snapshot). [confidence: high]

INTERPRETATION ERRORS:
- "The composition flipped: India’s fuel demand is passenger-ising. Diesel still dominates, but every increment leans petrol." — The article conflates growth rates (+255% petrol vs +77% diesel) with the *composition* of demand. While petrol grew faster, diesel still accounts for a larger absolute volume of sales (91,408 TMT vs 40,004 TMT in FY2024-25). The claim that "every increment leans petrol" implies a structural shift in the *share* of demand, but the data only shows relative growth rates, not absolute shares or incremental contributions. [confidence: high]

- "Delhi is what the CGD takeover of India’s gas demand looks like from the petrol pump’s side of the ledger." — The article attributes Delhi's slow fuel growth *solely* to CNG/metro expansion without quantifying the contribution of each factor (e.g., CNG adoption rate, metro ridership impact, vehicle-age rules). The causal claim is presented as definitive without decomposition or statistical evidence. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
