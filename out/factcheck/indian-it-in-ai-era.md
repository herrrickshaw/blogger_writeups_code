# Fact/interpretation check — indian-it-in-ai-era

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indian-it-in-ai-era.html`

## Gemini gemini-flash-latest

[Gemini API error 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites the RBI's *Developments in India's Balance of Payments, Q4 2025-26* for this figure, but the table in the same source shows net services receipts rising from $188.8bn (FY2024-25) to $216.6bn (FY2025-26), a $27.8bn increase. However, the RBI's published current account balance for FY2025-26 is -$25.2bn, while the table's sum is -$25.3bn (a $0.1bn rounding gap). The claim itself is consistent with the RBI data, but the phrasing implies a single-year jump that aligns with the RBI's figures. No error found. [confidence: high]
- "The Economic Survey's own uncomfortable framing" — The article references the *Economic Survey 2025-26* but does not provide a direct quote or citation for the specific claims about services exports not substituting for goods-based export ecosystems. Without a verifiable source, this cannot be confirmed. [confidence: medium]

INTERPRETATION ERRORS:
- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — The article correctly cites the RBI data showing net services receipts covering 64% of the goods deficit and 107% when combined with remittances. However, the interpretation that this makes the current account deficit "survivable at 0.6% of GDP" is misleading. The current account deficit is driven by *primary income* (investment income paid out), not just the goods deficit. The services surplus offsets the goods deficit, but the primary income outflow is the actual cause of the CAD. The conclusion conflates the goods deficit with the CAD, ignoring the role of investment income. [confidence: high]
- "A sector that is 1% of jobs but ~8% of GDP and covers two-thirds of the goods trade deficit cannot produce a mass-unemployment event. It can produce a balance-of-payments event." — While the sector's share of employment (1%) and GDP (~8%) is correct, the claim that it "covers two-thirds of the goods trade deficit" is an oversimplification. The article earlier states that net services cover 64% of the goods deficit, not two-thirds (which would be ~66.7%). More importantly, the interpretation that the sector's size alone determines the nature of the shock (jobs vs. balance-of-payments) ignores other structural factors like wage rigidity, skill mismatches, and the sector's role in the broader economy. The causal link between sector size and the type of shock is not directly supported by the data. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
