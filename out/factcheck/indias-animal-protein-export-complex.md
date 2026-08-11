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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99383, Requested 1765. Please try again in 16m31.872s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The article incorrectly states the fiscal year as FY2025-26 for the seafood export value, which should be FY2024-25 (as the data is from MPEDA's official report for that period). The value itself is correct, but the fiscal year is mislabeled. [confidence: high]

- "₹47,973.13cr Frozen shrimp alone — over two-thirds of total seafood export earnings" — While the value is correct, the claim that frozen shrimp accounts for "over two-thirds" of total seafood export earnings is misleading. The actual share is closer to 66.3% (₹47,973.13cr / ₹72,325.82cr), which is technically over two-thirds, but the phrasing could imply a much larger margin (e.g., 70%+), which is not accurate. [confidence: high]

INTERPRETATION ERRORS:
- "A rendering sector this concentrated in a few states, feeding a biodiesel programme with an explicit national blending target, is exactly the kind of byproduct-to-energy pipeline that gets built out once the economics and collection logistics catch up with the policy mandate — it just hasn't happened at scale yet." — The claim implies that the lack of scale in tallow-to-biodiesel is solely due to "economics and collection logistics," ignoring other critical factors like feedstock price volatility, competition with cheaper alternatives (e.g., UCO), and the absence of a dedicated supply chain infrastructure for tallow. The reasoning oversimplifies the barriers to scaling. [confidence: high]

- "The pattern across all three: India already has the raw production base — buffalo herds, rendering byproducts, brackish-water shrimp ponds. What separates the businesses that have scaled (buffalo meat, and now shrimp) from the one that hasn't (tallow biodiesel) is regulatory and logistics infrastructure..." — While regulatory and logistics infrastructure are important, the claim ignores market demand dynamics (e.g., shrimp has high global demand, while biodiesel faces competition and policy inconsistencies) and economic viability (e.g., tallow biodiesel may not be cost-competitive without subsidies). The reasoning conflates infrastructure with other critical factors. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
