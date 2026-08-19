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
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites the Reserve Bank of India (RBI) as the source, but the RBI's "Developments in India's Balance of Payments, Q4 2025-26" does not show net services receipts increasing by $27.8bn in a single year. The table shows an increase from $188.8bn (FY2024-25) to $216.6bn (FY2025-26), which is $27.8bn, but the article incorrectly implies this is the largest increase on record without verifying the historical data. [confidence: high]

- "The merchandise trade deficit was $337.3 billion." — The article cites the RBI as the source, but the RBI's table shows the merchandise trade deficit as $337.3bn for FY2025-26. However, the article does not clarify that this is a preliminary or estimated figure, as the RBI typically releases finalized data with a lag. The use of this figure without qualification could mislead readers into thinking it is final. [confidence: medium]

INTERPRETATION ERRORS:
- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — While the numbers are factually correct, the interpretation that this makes the current account deficit "survivable at 0.6% of GDP" is misleading. The current account deficit is primarily driven by the outflow of investment income ($48.2bn), not just the goods deficit. The article conflates the goods deficit with the current account deficit, ignoring the role of investment income outflows in determining the overall current account balance. [confidence: high]

- "A sector that is 1% of jobs but ~8% of GDP and covers two-thirds of the goods trade deficit cannot produce a mass-unemployment event. It can produce a balance-of-payments event." — While the sector's share of employment and GDP is correct, the causal claim that an AI shock would "show up in the rupee long before it showed up in the jobs data" is an over-extrapolation. The article assumes that the balance-of-payments impact would be immediate and dominant, but it does not provide evidence that the rupee would adjust before labor market effects become visible. The relationship between services receipts, the current account, and the exchange rate is complex and depends on multiple factors, including capital flows and monetary policy. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
