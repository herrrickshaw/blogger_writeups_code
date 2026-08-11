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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99748, Requested 1765. Please try again in 21m47.232s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year label is inconsistent. The article uses "FY2025-26" for the seafood export value but "FY2024-25" for the buffalo meat export value. This creates confusion about the correct fiscal year for the seafood data, as India's fiscal year runs from April to March (e.g., FY2025-26 would be April 2025–March 2026). The MPEDA source likely refers to FY2024-25, not FY2025-26. [confidence: high]

- "₹47,973.13cr Frozen shrimp alone — over two-thirds of total seafood export earnings" — The claim that frozen shrimp accounts for "over two-thirds" of total seafood export earnings is not supported by the quoted ₹47,973.13cr figure alone. The total seafood export value is ₹72,325.82cr, and ₹47,973.13cr divided by ₹72,325.82cr is approximately 66.3%, which is technically "over two-thirds." However, the article does not explicitly state the calculation or provide a clear breakdown to verify this proportion, making it difficult to confirm without cross-referencing the primary MPEDA data. [confidence: medium]

INTERPRETATION ERRORS:
- "A rendering sector this concentrated in a few states, feeding a biodiesel programme with an explicit national blending target, is exactly the kind of byproduct-to-energy pipeline that gets built out once the economics and collection logistics catch up with the policy mandate — it just hasn't happened at scale yet." — The claim implies that the concentration of the rendering sector in a few states and the national biodiesel blending target (B5 by 2030) should logically lead to the scaling of the tallow-to-biodiesel pipeline. However, the article itself notes that tallow contributed only about 3% of biodiesel feedstock in 2023, with volumes forecast around 9,000 tonnes as of 2022. The reasoning gap is that the article does not adequately explain why the policy mandate and sector concentration have not translated into scaled production, despite the apparent alignment. Factors such as feedstock volatility, lack of structured logistics, or economic disincentives are mentioned but not sufficiently analyzed to support the causal claim that the pipeline "gets built out once the economics and collection logistics catch up." [confidence: high]

- "The pattern across all three: India already has the raw production base — buffalo herds, rendering byproducts, brackish-water shrimp ponds. What separates the businesses that have scaled (buffalo meat, and now shrimp) from the one that hasn't (tallow biodiesel) is regulatory and logistics infrastructure..." — The claim suggests that the lack of scaling in the tallow-to-biodiesel sector is solely due to regulatory and logistics infrastructure, implying a direct causal relationship. However, the article also highlights that tallow supply is volatile and tied to the meat-processing industry, which is subject to disruptions (e.g., COVID-19 lockdowns). The reasoning gap is that the article does not sufficiently address whether the fundamental economics of tallow-to-biodiesel (e.g., cost-competitiveness with other feedstocks like UCO) or market demand dynamics also play a role in limiting scaling, beyond just infrastructure and regulation. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
