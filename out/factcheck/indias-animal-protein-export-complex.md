# Fact/interpretation check — indias-animal-protein-export-complex

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-animal-protein-export-complex.html`

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
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year is incorrectly stated as FY2025-26, which would imply the year ending March 2026. However, the article later references FY2024-25 for buffalo meat exports, and the MPEDA data for seafood exports is typically reported for FY2023-24 (ending March 2024). The correct fiscal year for the seafood export record is likely FY2023-24, not FY2025-26. [confidence: high]

- "₹47,973.13cr Frozen shrimp alone — roughly two-thirds (66.3%) of total seafood export earnings" — The article does not provide the total seafood export earnings figure that would allow this calculation. The ₹72,325.82cr figure is cited as the total seafood export value, but 66.3% of this would be ₹47,973.13cr, which matches the frozen shrimp value. However, the article does not explicitly state that the total seafood export earnings are ₹72,325.82cr, making the claim unverifiable without cross-referencing the source. [confidence: medium]

INTERPRETATION ERRORS:
- "India's National Biofuel Policy already permits tallow as a biodiesel feedstock, and the country carries a 5% biodiesel blending (B5) target for 2030 (separate from the unrelated 20% ethanol/E20 target set for 2025-26)." — While the policy and targets are correctly stated, the article implies that the tallow-to-biodiesel pipeline is a natural extension of the biofuel policy without addressing the structural challenges (e.g., feedstock volatility, collection logistics, or economic viability) that prevent scaling. The claim does not acknowledge that the policy mandate (B5 by 2030) is not aligned with current feedstock realities (tallow contributes only ~3% of biodiesel feedstock). This creates a false expectation that the policy alone will drive the industry forward. [confidence: high]

- "A rendering sector this concentrated in a few states, feeding a biodiesel programme with an explicit national blending target, is exactly the kind of byproduct-to-energy pipeline that gets built out once the economics and collection logistics catch up with the policy mandate — it just hasn't happened at scale yet." — The article assumes that the concentration of the rendering sector and the national blending target are sufficient conditions for the tallow-to-biodiesel pipeline to scale. However, it does not address other critical factors such as feedstock pricing, competition with other biodiesel feedstocks (e.g., UCO), or the lack of dedicated infrastructure for tallow collection and processing. The claim overgeneralizes the conditions required for scaling without evidence. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
