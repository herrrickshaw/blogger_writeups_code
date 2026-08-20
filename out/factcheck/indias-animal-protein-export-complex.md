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
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year is incorrectly stated as FY2025-26, which would imply the year ending March 2026. However, the article later mentions "FY2025-26" for seafood exports but also cites "FY2024-25" for buffalo meat exports, creating inconsistency. The correct fiscal year for the seafood export record is likely FY2023-24 (as per MPEDA's actual data), not FY2025-26. [confidence: high]

- "₹47,973.13cr Frozen shrimp alone (~$5.51bn) — roughly two-thirds (66.3%) of total seafood export earnings" — The percentage (66.3%) is inconsistent with the provided figures. ₹47,973.13cr divided by ₹72,325.82cr equals ~66.3%, but the article later states frozen shrimp contributes "roughly two-thirds (66.3%) of total earnings," which is correct numerically. However, the claim is misleading because the ₹72,325.82cr figure itself is likely incorrect (as noted above), making the derived percentage unreliable. [confidence: high]

INTERPRETATION ERRORS:
- "India's National Biofuel Policy already permits tallow as a biodiesel feedstock, and the country carries a 5% biodiesel blending (B5) target for 2030 (separate from the unrelated 20% ethanol/E20 target set for 2025-26)." — While the policy and targets are correctly stated, the article implies that the tallow-to-biodiesel pipeline is constrained solely by "structure" (logistics/infrastructure) and not by policy gaps. However, the National Biofuel Policy's permissibility of tallow does not guarantee its prioritization or incentivization in blending mandates, which may still favor other feedstocks (e.g., UCO). The claim overlooks potential policy biases or economic disincentives that could hinder tallow's adoption despite its availability. [confidence: medium]

- "A rendering sector this concentrated in a few states, feeding a biodiesel programme with an explicit national blending target, is exactly the kind of byproduct-to-energy pipeline that gets built out once the economics and collection logistics catch up with the policy mandate — it just hasn't happened at scale yet." — The article assumes that the mere existence of a blending target (B5 by 2030) and a concentrated rendering sector will inevitably lead to scaled-up tallow biodiesel production. However, this ignores potential market failures, such as lack of demand from biodiesel producers, price volatility of tallow, or competing uses (e.g., animal feed, soap manufacturing). The causal link between policy targets and actual industry scaling is overstated. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
