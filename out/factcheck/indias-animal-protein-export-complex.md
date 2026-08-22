# Fact/interpretation check — indias-animal-protein-export-complex

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-animal-protein-export-complex.html`

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
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year notation is incorrect. India's fiscal year runs from April to March, so FY2025-26 would refer to April 2025–March 2026, but the article likely means FY2023-24 or FY2024-25, as MPEDA's latest published data for seafood exports is typically for the previous fiscal year (e.g., FY2023-24). [confidence: high]

- "₹47,973.13cr Frozen shrimp alone (~$5.51bn) — roughly two-thirds (66.3%) of total seafood export earnings" — The percentage (66.3%) does not match the implied calculation. If frozen shrimp earnings are ₹47,973.13cr and total seafood exports are ₹72,325.82cr, then frozen shrimp would account for ~66.3% of total earnings (₹47,973.13 / ₹72,325.82 ≈ 0.663). However, the article presents this as a fact without verifying the source's accuracy, and the numbers may be outdated or misstated (see prior error). [confidence: medium]

INTERPRETATION ERRORS:
- "India's National Biofuel Policy already permits tallow as a biodiesel feedstock, and the country carries a 5% biodiesel blending (B5) target for 2030 (separate from the unrelated 20% ethanol/E20 target set for 2025-26)." — While the policy may permit tallow as a feedstock and a B5 target exists, the article implies a direct link between the two without evidence. The B5 target is a blending mandate, but the actual adoption of tallow in biodiesel depends on economic viability, infrastructure, and feedstock availability, which the article acknowledges are lacking. The claim conflates policy permission with actual implementation. [confidence: high]

- "A rendering sector this concentrated in a few states, feeding a biodiesel programme with an explicit national blending target, is exactly the kind of byproduct-to-energy pipeline that gets built out once the economics and collection logistics catch up with the policy mandate — it just hasn't happened at scale yet." — The article assumes that the concentration of the rendering sector and the existence of a blending target are sufficient conditions for the tallow-biodiesel pipeline to scale. However, it does not address other critical factors like feedstock pricing, collection efficiency, or competing uses for tallow (e.g., in soap or animal feed industries), which may limit scalability regardless of policy or infrastructure. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
