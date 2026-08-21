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
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites the Reserve Bank of India (RBI) data showing net services receipts at $216.6bn for FY2025-26, but the RBI's "Developments in India's Balance of Payments, Q4 2025-26" report (the cited source) lists net services receipts as $216.6bn for FY2025-26 and $188.8bn for FY2024-25, implying an increase of $27.8bn. However, the RBI report's table shows the increase as $27.8bn ($216.6bn - $188.8bn), which is correct. No factual error found here. [confidence: high]
- "The Economic Survey's own uncomfortable framing" — The article quotes the 2025-26 Economic Survey as saying services exports are "not a substitute for the goods-based export ecosystems that ultimately underpin durable external and currency stability." However, the Economic Survey 2025-26 does not contain this exact phrasing. The quoted lines appear to be paraphrased or misattributed. [confidence: high]

INTERPRETATION ERRORS:
- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — While the numbers are factually correct (64% and 107%), the interpretation that this means the current account deficit is solely due to investment income outflows ($48.2bn) is incomplete. The article implies that the services surplus and remittances fully cover the goods deficit, leaving only investment income outflows as the cause of the CAD. However, the CAD is also influenced by other factors like secondary income (remittances) and primary income (investment income), and the article does not adequately explain how these interact to produce the CAD. The reasoning oversimplifies the balance-of-payments dynamics. [confidence: high]
- "A sector that is 1% of jobs but ~8% of GDP and covers two-thirds of the goods trade deficit cannot produce a mass-unemployment event. It can produce a balance-of-payments event." — While the sector's share of employment (1%) and GDP (~8%) is correct, the interpretation that it "cannot produce a mass-unemployment event" is an overstatement. The article correctly notes that the sector's employment share is small, but it does not rule out sector-specific unemployment (e.g., layoffs in IT firms) or broader economic impacts (e.g., reduced hiring of graduates). The claim conflates macroeconomic unemployment (national level) with sectoral unemployment (industry level), which is a reasoning gap. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
