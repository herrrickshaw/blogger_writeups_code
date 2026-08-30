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

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "China still grows most of the world’s supply; South Korea, it turns out, mostly buys it in." — This claim is incorrect. While China dominates global spirulina production (45–65% of world output), South Korea does have domestic cultivation trials (e.g., Spirulina maxima in Ansan) and at least one commercial microalgae producer (Phycoil Biotech Korea, though focused on DHA, not spirulina). The article later acknowledges this but the initial claim oversimplifies South Korea's role. [confidence: high]

- "The Union Cabinet approved the BioE3 Policy on 24 August 2024" — This date is incorrect. The BioE3 Policy was approved on **17 August 2023**, not 2024. The article cites correct details about the policy's scope but the date is factually wrong. [confidence: high]

INTERPRETATION ERRORS:
- "A quarter-acre pond can out-earn an acre of crop" — The article cites commercial farming guides and trade press figures (e.g., ₹1,000/kg selling price, ₹60,000–₹1 lakh monthly revenue) to support this claim, but these are **not audited farm-income surveys** and are presented as illustrative claims. The conclusion that a quarter-acre pond can out-earn an acre of row crops is an **extrapolation beyond verified data**, as the cited figures are not representative of typical outcomes or peer-reviewed economic analyses. [confidence: high]

- "Spirulina cultivation doesn't need farmland in the conventional sense — it needs shallow, agitated ponds or tanks... so a single pond turns over multiple harvests a season." — While the technical description of spirulina cultivation is correct, the implication that this **automatically translates to higher profitability per unit land** is an **apples-to-oranges comparison**. The article conflates **land efficiency** (less land needed) with **economic out-earning**, ignoring factors like capital costs, labor, energy inputs, and market volatility in spirulina prices. The claim assumes revenue scales linearly with harvest frequency without accounting for operational constraints or real-world farm economics. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
