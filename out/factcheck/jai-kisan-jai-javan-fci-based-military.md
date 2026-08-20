# Fact/interpretation check — jai-kisan-jai-javan-fci-based-military

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/jai-kisan-jai-javan-fci-based-military.html`

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
- "₹300 Cr is roughly 27× (about one order of magnitude) larger than this plan's own annual output (~₹11 Cr)" — The ₹300 Cr figure is likely a multi-year cumulative figure, not an annual output, as the article itself notes ("likely a multi-year cumulative figure the deck does not label as such"). The comparison to annual output is incorrect because it treats a cumulative figure as an annual one. [confidence: high]

- "targeting operational status by July 2027 (an 18-month plan starting Aug 2026 lands ~Feb 2028, not July 2027)" — The timeline calculation is incorrect. An 18-month plan starting in August 2026 would end in February 2028, not July 2027. [confidence: high]

INTERPRETATION ERRORS:
- "5-year net savings vs private (the visible line items in this table sum to ~₹10–14 Cr, not ₹8.51 Cr — the deck does not show a full reconciling derivation)" — The claim of ₹8.51 Cr in 5-year savings is not supported by the visible line items, which sum to a higher amount. The discrepancy suggests either missing items or an error in the deck's calculations, but the article does not reconcile this gap. [confidence: high]

- "Perpetual annual savings (Yr 2+, gross — before the ₹1.2-1.4 Cr/yr operating cost and Year-1 setup are netted; the ₹8.51 Cr row above is the 5-year net of both)" — The presentation of "perpetual annual savings" as ₹4.5 Cr/yr is misleading because it does not account for the ongoing operating costs (₹1.2–1.4 Cr/yr) or the initial setup cost (₹2.85 Cr). The net savings would be lower after accounting for these costs, but the article does not clarify this. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
