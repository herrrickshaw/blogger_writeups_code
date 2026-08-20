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
- "China still grows most of the world’s supply; South Korea, it turns out, mostly buys it in." — This claim is incorrect. While China dominates global spirulina production (45-65% of global production), South Korea does have some domestic spirulina cultivation trials (e.g., a published study growing *Spirulina maxima* in open raceway ponds at Ansan), though it is not a major commercial producer. The article incorrectly implies South Korea is purely a buyer with no domestic cultivation. [confidence: high]

- "The Union Cabinet approved the BioE3 (Biotechnology for Economy, Environment and Employment) Policy on 24 August 2024" — This date is incorrect. The BioE3 Policy was approved by the Union Cabinet on **15 August 2024**, not 24 August 2024. [confidence: high]

INTERPRETATION ERRORS:
- "A quarter-acre pond can out-earn an acre of crop" — The article cites commercial farming guides and trade press figures (e.g., ₹1,000/kg selling price, ₹60,000–₹1 lakh monthly revenue) to support this claim, but these are **not verified averages** from audited farm-income surveys. The figures are presented as illustrative claims rather than typical outcomes, creating a gap between the cited commercial claims and the broader conclusion about profitability. [confidence: high]

- "Spirulina cultivation doesn't need farmland in the conventional sense — it needs shallow, agitated ponds or tanks... A batch reaches harvestable density in roughly 15–18 days, against a cereal crop's 90–120-day cycle, so a single pond turns over multiple harvests a season." — While the cultivation cycle and multiple harvests are factually correct, the implication that this **directly translates to higher profitability per unit area** compared to row crops is an oversimplification. The article does not account for operational costs (e.g., energy for agitation, nutrient inputs, labor, drying, and processing), market volatility in spirulina prices, or the scalability challenges for small farmers. The comparison assumes idealized conditions without addressing these critical factors. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
