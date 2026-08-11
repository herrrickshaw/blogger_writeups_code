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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99394, Requested 1765. Please try again in 16m41.376s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year notation is inconsistent. FY2025-26 is not a standard way to denote a fiscal year in India (it should be FY2025 or FY2026). Additionally, the article mixes FY2024-25 for buffalo meat exports and FY2025-26 for seafood exports without clarifying the overlap or transition between these periods. [confidence: high]

- "₹47,973.13cr Frozen shrimp alone — over two-thirds of total seafood export earnings" — The claim that frozen shrimp accounts for "over two-thirds" of total seafood export earnings is not supported by the provided data. The article states frozen shrimp contributed ₹47,973.13cr to a total of ₹72,325.82cr, which is approximately 66.3%, not "over two-thirds" (which would imply >66.67%). [confidence: high]

INTERPRETATION ERRORS:
- "A rendering sector this concentrated in a few states, feeding a biodiesel programme with an explicit national blending target, is exactly the kind of byproduct-to-energy pipeline that gets built out once the economics and collection logistics catch up with the policy mandate — it just hasn't happened at scale yet." — The claim implies that the lack of scale in tallow-to-biodiesel is solely due to "economics and collection logistics" catching up with policy mandates. However, the article also notes that tallow supply is volatile due to its dependence on the meat-processing industry, which was disrupted during COVID-19. This suggests that structural and market risks (e.g., feedstock volatility) may also play a significant role in limiting scale, not just logistics or economics. The reasoning oversimplifies the barriers to scaling. [confidence: high]

- "The pattern across all three: India already has the raw production base — buffalo herds, rendering byproducts, brackish-water shrimp ponds. What separates the businesses that have scaled (buffalo meat, and now shrimp) from the one that hasn't (tallow biodiesel) is regulatory and logistics infrastructure..." — The claim attributes the scaling difference primarily to "regulatory and logistics infrastructure," but it ignores other critical factors such as market demand, price competitiveness of tallow biodiesel relative to alternatives (e.g., UCO), and the maturity of the biodiesel blending ecosystem. The comparison is an apples-to-oranges analysis, as the three sectors operate in fundamentally different markets with distinct demand drivers. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
