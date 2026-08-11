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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99460, Requested 1765. Please try again in 17m38.4s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year notation is inconsistent. FY2025-26 is the same as FY2026, but the article uses both formats in the same sentence. Additionally, the export value is listed as ₹72,325.82cr (~$8.28bn), but the source (MPEDA) typically reports in USD terms first, with INR conversions being approximate. The exact INR figure may not match MPEDA's published data. [confidence: high]

- "₹47,973.13cr Frozen shrimp alone — over two-thirds of total seafood export earnings" — The claim that frozen shrimp accounts for "over two-thirds" of total seafood export earnings is not supported by the provided data. The article states frozen shrimp contributed ₹47,973.13cr (~$5.51bn) to a total seafood export value of ₹72,325.82cr (~$8.28bn), which is approximately 66.3% (not "over two-thirds" as a rounded figure). While mathematically close, the phrasing implies a higher proportion than the data supports. [confidence: high]

INTERPRETATION ERRORS:
- "The constraint isn't feedstock availability — it's structure. Tallow supply is almost entirely a derivative of the meat-processing and rendering industry, which means it inherits that industry's volatility." — While the claim about structural constraints (e.g., logistics, collection) may be correct, the article conflates *volatility in supply* with *structural constraints* as the sole reason for limited tallow-to-biodiesel scaling. It does not address other potential factors, such as policy incentives, pricing, or competing uses for tallow (e.g., soap manufacturing), which could also limit biodiesel adoption. The reasoning gap is that the article assumes structural issues are the *only* constraint without ruling out or discussing other economic or market barriers. [confidence: medium]

- "The forward projection is aggressive: India's shrimp market is expected to grow at a 9.60% CAGR from 2026-2035, reaching roughly 2.55 million tonnes of volume by the end of that window — a scale-up that dwarfs the tallow-biodiesel opportunity in absolute size, even though both start from the same underlying idea of turning an animal-protein production base into a structured export or energy business." — The comparison between shrimp market growth and tallow-biodiesel "opportunity" is flawed because the two are not directly comparable. Shrimp export volume (2.55 million tonnes) is a *production/output* metric, while the tallow-biodiesel "opportunity" is framed as a *feedstock potential* (9,000 tonnes in 2022). The article does not clarify whether the tallow volume is expected to scale proportionally or if the comparison is apples-to-oranges. The reasoning gap is that the two metrics are not equivalent, making the claim about one "dwarfing" the other misleading. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
