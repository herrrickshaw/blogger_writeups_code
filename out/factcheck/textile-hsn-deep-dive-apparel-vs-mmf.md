# Fact/interpretation check — textile-hsn-deep-dive-apparel-vs-mmf

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/textile-hsn-deep-dive-apparel-vs-mmf.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99841, Requested 1808. Please try again in 23m44.736s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is the world's 6th-largest T&A exporter with ~3.9% global share." — This claim is unverifiable as the article does not provide a source or context for the global ranking and share. The cited sources (AEPC Annual Report 2024-25, CITI T&A export statistics) do not appear to include this specific ranking or global comparison. [confidence: medium]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026) , projected US$309 bn by 2047." — The projection of US$309 bn by 2047 is highly speculative and lacks a credible source or methodology. The article cites "Technical-textile market $29bn FY24 → $309bn 2047" without attribution to a reputable forecasting body or study. [confidence: high]

INTERPRETATION ERRORS:
- "Cotton textiles were ~33% of the Apr–Oct FY25 export basket vs man-made textiles ~15%." — This claim is presented as a direct comparison between cotton and man-made textiles in the apparel basket, but the article does not clarify whether these percentages are based on volume, value, or another metric. Additionally, the "fibre-level share" vs "garment-purchase share" distinction is not consistently applied, making it unclear if the comparison is apples-to-apples. [confidence: high]

- "The binding constraint is specialty fibre + technology. India imports high-performance fibres and the machinery for depolymerization-grade and high-tenacity output." — While the claim about import dependence on specialty fibres is likely correct, the article conflates the need for fibres with the need for machinery, implying that importing machinery alone would solve the constraint. This is an overgeneralization, as technology adoption also depends on skills, infrastructure, and policy support, which are not addressed. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
