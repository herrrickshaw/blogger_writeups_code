# Fact/interpretation check — india-mineral-oil-hsn-ch27-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-mineral-oil-hsn-ch27-trade.html`

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
- "121.1 MMT Crude imported (FY25-26 H1)" — The claim refers to the first half of FY2025-26 (H1), but the article later states "$203.4B Ch.27 imports FY25-26 (26.2% of all imports)" and "$55.9B Ch.27 exports FY25-26," implying full-year figures. The H1 crude import figure cannot be directly compared to full-year trade values without adjustment, and the article does not clarify this. [confidence: high]

- "Gas (Kirit Parikh 2023): APM gas sloped to the same Indian crude basket, floor $4 / ceiling $6.5 per MMBtu (+$0.5/yr), difficult fields cap $12.46" — The Kirit Parikh Committee report (2023) does not set a "floor" or "ceiling" price for APM gas tied to the Indian crude basket in this manner. The committee recommended a market-linked pricing mechanism, not a fixed floor/ceiling tied to crude prices. [confidence: high]

INTERPRETATION ERRORS:
- "Implied $/bbl from trade value÷quantity tracks the Indian basket within ±6% every year — the core consistency check." — While the implied $/bbl may track the Indian basket closely, this does not necessarily validate the pricing formula or the trade parity price (TPP) mechanism. The ±6% deviation could be due to timing differences, grade variations, or other factors unrelated to the accuracy of the pricing formula. The article conflates consistency in unit-value tracking with validation of the pricing mechanism itself. [confidence: high]

- "80 : 20 Trade Parity Price = IPP : EPP weight" — The article states that the Trade Parity Price (TPP) is calculated as 80% Import Parity Price (IPP) and 20% Export Parity Price (EPP), but it does not explain why this specific weight is used or whether it is empirically justified. The 80:20 split appears arbitrary without evidence that it reflects actual trade patterns or economic rationale. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
