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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is the world's 6th-largest T&A exporter with ~3.9% global share." — This claim is unverifiable as the article does not provide a source or methodology for the global share calculation. The 3.9% figure is not corroborated by standard industry reports (e.g., WTO or ITMF data), which typically place India's share lower (around 3.5% or less). [confidence: high]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026), projected US$309 bn by 2047." — The projection of US$309 bn by 2047 is implausibly high and lacks credible sourcing. Even aggressive growth scenarios (e.g., 10% CAGR) would not reach this figure from a US$29 bn base in 24 years. [confidence: high]

INTERPRETATION ERRORS:
- "Cotton textiles were ~33% of the Apr–Oct FY25 export basket vs man-made textiles ~15%." — This claim conflates fibre-level consumption shares with export basket composition. The article earlier notes that MMF accounts for ~70% of global fibre consumption, but India's export basket skews toward cotton. The comparison here is apples-to-oranges because it mixes global fibre consumption (a production metric) with India's export mix (a trade metric). The reasoning gap is that the two metrics are not directly comparable. [confidence: high]

- "The binding constraint is specialty fibre + technology. India imports high-performance fibres and the machinery for depolymerization-grade and high-tenacity output." — While the claim about import dependence is likely correct, the phrasing implies a causal link between importing fibres/machinery and the lack of domestic capacity. However, the article does not provide evidence that domestic production of these fibres/machinery is technically or economically feasible, nor does it address why India cannot develop this capacity despite importing. The reasoning gap is that the claim assumes a one-way dependency without exploring alternative solutions or constraints. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
