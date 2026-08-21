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
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year is incorrectly stated as FY2025-26, which would imply the year ending March 2026. However, the article later mentions "FY2025-26" for seafood exports but also cites MPEDA data, which typically reports fiscal years ending March 31. The correct fiscal year for such records is usually FY2023-24 or FY2024-25 (e.g., 2023-24). The claim is likely outdated or misstated. [confidence: high]

- "₹47,973.13cr Frozen shrimp alone (~$5.51bn) — roughly two-thirds (66.3%) of total seafood export earnings" — The percentage (66.3%) is inconsistent with the absolute values provided. If frozen shrimp earnings are ₹47,973.13cr and total seafood exports are ₹72,325.82cr, then frozen shrimp accounts for ~66.3% of total seafood exports (₹47,973.13 / ₹72,325.82 ≈ 0.663). However, the article presents this as a fact, but the calculation is correct based on the numbers given. No error here. [confidence: none found]

INTERPRETATION ERRORS:
- "India's buffalo-meat (carabeef) trade is the largest of the three businesses by export value." — While the article later states that buffalo meat exports were $4.06bn in FY2024-25, it does not provide a direct comparison with the other two businesses (rendering/tallow and shrimp) in the same fiscal year. The claim that buffalo meat is the "largest" is not explicitly supported by a side-by-side comparison of the three sectors' export values in the same timeframe. The shrimp export value is given for FY2025-26 (~$8.28bn), which is a different fiscal year, making a direct comparison invalid without adjustment. [confidence: high]

- "A rendering sector this concentrated in a few states, feeding a biodiesel programme with an explicit national blending target, is exactly the kind of byproduct-to-energy pipeline that gets built out once the economics and collection logistics catch up with the policy mandate — it just hasn't happened at scale yet." — The claim implies that the lack of scale in tallow-to-biodiesel is solely due to "economics and collection logistics," but it does not address other critical factors such as feedstock pricing, competing uses for tallow (e.g., soap manufacturing), policy enforcement gaps, or the maturity of the biodiesel market. The reasoning oversimplifies the barriers to scaling up the tallow-biodiesel supply chain. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
