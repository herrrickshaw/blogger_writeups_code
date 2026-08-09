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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99689, Requested 1981. Please try again in 24m2.88s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year 2025-26 is incorrect as it would end in March 2026, but the article cites data from MPEDA (Marine Products Export Development Authority) which typically reports data for completed fiscal years (e.g., FY2024-25). The correct year should likely be FY2024-25. [confidence: high]

- "₹47,973.13cr Frozen shrimp alone — over two-thirds of total seafood export earnings" — While the claim that frozen shrimp constitutes over two-thirds of seafood export earnings is plausible, the exact figure of ₹47,973.13cr is not verifiable against publicly available MPEDA data for any specific fiscal year. The article does not provide a source or link to confirm this precise number. [confidence: medium]

INTERPRETATION ERRORS:
- "India's National Biofuel Policy already permits tallow as a biodiesel feedstock, and the country carries a B20 blending target (20% biodiesel in diesel) for 2025-26." — While the policy may permit tallow as a feedstock and a B20 target may exist, the article implies a direct causal link between the policy and tallow's contribution to biodiesel (e.g., "tallow supplies only a small fraction..."). However, the small share of tallow in biodiesel feedstock (3% in 2023) is not necessarily due to policy constraints but rather structural, economic, or logistical factors (e.g., competition with UCO, collection challenges). The policy's permissiveness does not explain the low utilization rate. [confidence: high]

- "The forward projection is aggressive: India's shrimp market is expected to grow at a 9.60% CAGR from 2026-2035, reaching roughly 2.55 million tonnes of volume by the end of that window — a scale-up that dwarfs the tallow-biodiesel opportunity in absolute size, even though both start from the same underlying idea of turning an animal-protein production base into a structured export or energy business." — The comparison between shrimp market growth and tallow-biodiesel opportunity is flawed because they are fundamentally different markets with different demand drivers, regulatory frameworks, and scalability constraints. Shrimp is a high-value export commodity, while tallow-biodiesel is a niche energy feedstock with limited domestic demand and infrastructure. The "same underlying idea" does not justify a direct comparison in absolute size or growth potential. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
