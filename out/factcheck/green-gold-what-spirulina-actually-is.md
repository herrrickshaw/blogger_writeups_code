# Fact/interpretation check — green-gold-what-spirulina-actually-is

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/green-gold-what-spirulina-actually-is.html`

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
- "China still grows most of the world’s supply; South Korea, it turns out, mostly buys it in." — This claim is partially incorrect. While China dominates global spirulina production, South Korea does have domestic microalgae cultivation (e.g., Phycoil Biotech Korea producing DHA oil), though not specifically spirulina. The article later acknowledges this but the initial claim oversimplifies South Korea's role. [confidence: high]

INTERPRETATION ERRORS:
- "A quarter-acre pond can out-earn an acre of crop" — The article cites commercial farming guides and trade press figures (₹60,000–₹1 lakh monthly revenue) to support this claim, but these are illustrative claims from industry sources, not verified averages from audited farm-income surveys. The comparison lacks rigorous economic analysis or peer-reviewed data to substantiate the "out-earn" assertion. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
