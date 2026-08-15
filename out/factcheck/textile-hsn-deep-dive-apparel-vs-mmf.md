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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 98891, Requested 1854. Please try again in 10m43.68s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Total textiles & apparel exports ≈ US$37 bn (FY2024-25, +6% YoY); India is the world's 6th-largest T&A exporter with ~3.9% global share." — The FY2024-25 export figure is likely incorrect or unverifiable. The article cites sources like AEPC Annual Report 2024-25 and CITI T&A export statistics, but the US$37 bn figure does not align with known data (e.g., AEPC's reported exports for FY2023-24 were ~US$44 bn, and FY2024-25 growth would not plausibly reduce this to US$37 bn). [confidence: high]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026) , projected US$309 bn by 2047." — The US$309 bn projection for 2047 is an extreme extrapolation with no cited methodology or source. The 2026 figure (US$45 bn) is plausible, but the 2047 projection lacks credible backing and appears speculative. [confidence: high]

INTERPRETATION ERRORS:
- "India imports very little finished apparel (high duties + domestic supply) — a large structural surplus in Ch 61/62." — While India may have a trade surplus in apparel (HS 61–62), the claim that this is due to "high duties + domestic supply" conflates correlation with causation. The article does not provide evidence that duties are the primary driver of the surplus (e.g., by comparing pre- and post-duty periods or analyzing duty-free competitors like Bangladesh). The surplus could also stem from India's cost advantages, global demand, or other factors. [confidence: medium]

- "The binding constraint is specialty fibre + technology. India imports high-performance fibres and the machinery for depolymerization-grade and high-tenacity output." — The article correctly identifies India's import dependence on specialty fibres but incorrectly implies that the *only* binding constraint is fibre/technology imports. It ignores other critical factors like domestic demand growth, policy bottlenecks (e.g., PLI scheme uptake), infrastructure gaps, or skill shortages that may also limit technical-textile expansion. The claim oversimplifies the problem by attributing it solely to imports. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
