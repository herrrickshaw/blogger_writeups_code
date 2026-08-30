# Fact/interpretation check — where-rupee-actually-stands-ten-years

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-rupee-actually-stands-ten-years.html`

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
- "14 August 2026" (appears multiple times, including in the article title and data retrieval date) — The article is dated 14 August 2026, but this date is in the future relative to the current date (2023). The claim is unverifiable and likely incorrect. [confidence: high]

- "CNY, RUB and SAR have no direct, officially published INR reference rate" — While the article correctly notes that FBIL does not publish direct INR reference rates for CNY, RUB, or SAR, it incorrectly states that SAR has no direct reference rate. The UAE dirham (AED) is mentioned as having a direct FBIL reference rate, and the Saudi riyal (SAR) is pegged to the USD, but the article conflates the absence of a direct INR reference rate with the absence of any official rate mechanism. SAR is pegged to USD, and its rate is effectively published via the USD/INR rate. [confidence: high]

INTERPRETATION ERRORS:
- "the rouble is the outlier, and not in the direction the other four suggest: it sits at just 104, the shallowest ten-year rise of the five, but it got there by way of the sharpest single move on the chart — the vertical plunge and rebound around 2022" — While the rouble's volatility and the 2022 crash/recovery are correctly noted, the claim that the rouble's ten-year trend is an "outlier" in the *direction* of its movement is misleading. The rouble's ten-year indexed value (104) is indeed the smallest increase among the five currencies, but this is not because it moved in the "opposite direction" of the others—it still appreciated (from 100 to 104), just far less than the others. The phrasing suggests the rouble depreciated or moved counter to the trend, which is incorrect. The correct interpretation is that the rouble's *volatility* and *non-linear path* are outliers, not its direction of movement. [confidence: high]

- "Rupee settlement moves who bears conversion risk and when; it does not touch the underlying trade imbalance" — While this claim is generally correct, the article later contradicts it by acknowledging that rupee invoicing could affect the trade balance indirectly through invoicing shifts (e.g., rupee invoicing of exports creating foreign demand for INR). The claim oversimplifies by stating that rupee settlement *does not touch* the trade imbalance at all, ignoring potential feedback effects where invoicing choices could influence trade flows over time. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
