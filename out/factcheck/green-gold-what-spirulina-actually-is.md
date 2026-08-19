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
- "China still grows most of the world’s supply; South Korea, it turns out, mostly buys it in." — This claim is incorrect. While China dominates global spirulina production (~45-65% of global production), South Korea does not primarily import spirulina; it has no major spirulina cultivation at scale but does cultivate other microalgae (e.g., DHA-focused Phycoil Biotech Korea). The article later contradicts this by stating South Korea imports spirulina for cosmetic/pharma-grade processing, but the initial claim oversimplifies and misrepresents South Korea's role. [confidence: high]

- "India's small and marginal farmers are eligible for up to 50% subsidy (capped around ₹5 lakh) on pond construction" — The article cites this as a commercial claim from industry guides but does not verify it against an official government source. The subsidy cap and eligibility details may be outdated or misrepresented, as no primary government document is cited. [confidence: medium]

INTERPRETATION ERRORS:
- "A quarter-acre pond can out-earn an acre of crop" — The article presents revenue estimates (₹60,000–₹1 lakh/month) from commercial farming guides as a generalizable claim, but these figures are not based on audited farm-income surveys or peer-reviewed economic analyses. The comparison to row crops (e.g., paddy or sugarcane) is not standardized (e.g., no adjustment for labor, input costs, or market volatility), making the "out-earn" claim an extrapolation beyond verifiable data. [confidence: high]

- "Spirulina cultivation doesn't need farmland in the conventional sense — it needs shallow, agitated ponds or tanks... A batch reaches harvestable density in roughly 15–18 days" — While the cultivation cycle is factually correct, the implication that this inherently makes spirulina more land-efficient than row crops is an apples-to-oranges comparison. The article does not account for the fact that row crops (e.g., cereals) are typically grown in multi-crop rotations per year, whereas spirulina ponds may face seasonal limitations (e.g., temperature, sunlight) or require continuous energy inputs for agitation, which are not factored into the land-use comparison. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
