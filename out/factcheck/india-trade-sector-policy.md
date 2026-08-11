# Fact/interpretation check — india-trade-sector-policy

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-trade-sector-policy.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99484, Requested 1670. Please try again in 16m37.056s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "the $333bn deficit (current TradeStat running total is closer to $334.3bn)" — The claim conflates a specific figure ($333bn) with a "running total" ($334.3bn) without clarifying whether the latter is an official or updated figure. TradeStat (likely referring to India's official trade statistics) does not typically report "running totals" in this manner, and the discrepancy suggests a lack of precision in sourcing. [confidence: high]

- "₹1.97 lakh cr forex saved" — The claim attributes forex savings to PIB-verified ethanol blending but does not provide a verifiable source or methodology for this calculation. The Reserve Bank of India (RBI) or Ministry of Petroleum and Natural Gas (which oversees ethanol blending) do not publish such a specific figure in public reports. [confidence: high]

INTERPRETATION ERRORS:
- "DPIIT attributes inflow to the recipient company's registered office, not the project site — with no published caveat" — The claim suggests a causal link between DPIIT's methodology and potential misattribution of FDI inflows, but it does not provide evidence that this methodological choice leads to systematic over- or underestimation of FDI. The absence of a caveat does not inherently invalidate the data; the interpretation assumes a problem without demonstrating its impact. [confidence: medium]

- "₹28,748cr = ~15% of outlay; Pharma A to ACC Battery F" — The claim grades PLI disbursals but does not clarify whether the 15% figure refers to disbursed funds relative to total allocated outlays or actual utilization. Without a clear definition of "outlay" (e.g., committed vs. disbursed), the grading system lacks a transparent benchmark, making the comparison between sectors (e.g., Pharma vs. ACC Battery) potentially misleading. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
