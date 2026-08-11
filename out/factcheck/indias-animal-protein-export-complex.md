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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99664, Requested 2093. Please try again in 25m18.048s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year notation is inconsistent. FY2025-26 is the same as FY2026, but the article mixes both notations (e.g., "FY2024-25" for buffalo meat and "FY2025-26" for seafood). The correct notation should be consistent (either FY2025-26 or FY2026). [confidence: high]

- "₹47,973.13cr Frozen shrimp alone — over two-thirds of total seafood export earnings" — The claim states "over two-thirds," but the numbers provided (₹47,973.13cr out of ₹72,325.82cr) actually calculate to approximately 66.3%, which is just over two-thirds. However, the article rounds this to "over two-thirds," which is technically correct but could be misleading if interpreted as significantly more than two-thirds. [confidence: medium]

INTERPRETATION ERRORS:
- "The constraint isn't feedstock availability — it's structure. Tallow supply is almost entirely a derivative of the meat-processing and rendering industry, which means it inherits that industry's volatility. When COVID-era lockdowns cut meat exports and shut abattoirs, India's nascent tallow-biodiesel supply chain lost its raw material at the same time, a linkage flagged directly in contemporary trade reporting." — The article correctly notes the volatility of tallow supply due to its dependence on the meat industry, but it does not adequately explain why this structural constraint alone justifies the lack of scale in the tallow-to-biodiesel pipeline. The claim implies that the lack of scale is solely due to structural issues, but it does not address other potential factors such as economic viability, policy incentives, or market demand for biodiesel from tallow specifically. The reasoning gap is that the article does not rule out or explore other barriers beyond structural supply volatility. [confidence: medium]

- "The pattern across all three: India already has the raw production base — buffalo herds, rendering byproducts, brackish-water shrimp ponds. What separates the businesses that have scaled (buffalo meat, and now shrimp) from the one that hasn't (tallow biodiesel) is regulatory and logistics infrastructure..." — The article attributes the scaling of buffalo meat and shrimp exports to "regulatory and logistics infrastructure," but it does not provide evidence or analysis to support this causal claim. The comparison is an apples-to-oranges comparison because buffalo meat and shrimp exports are mature, globally traded commodities with established supply chains, while tallow biodiesel is a nascent, domestically focused energy product with different market dynamics. The reasoning gap is that the article assumes the lack of scaling in tallow biodiesel is solely due to infrastructure without considering differences in market demand, policy priorities, or economic incentives. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
