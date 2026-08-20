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
- "India is the world's 6th-largest T&A exporter with ~3.9% global share." — The claim is unverifiable as stated; the sources (AEPC Annual Report 2024-25, PIB) are cited but not directly quoted or linked, and the 3.9% figure lacks a clear basis (e.g., no reference year or methodology for global rankings). [confidence: medium]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026), projected US$309 bn by 2047." — The 2047 projection of US$309 bn appears implausibly high without context or a cited source; it is not supported by the listed references (IBEF, Ministry of Textiles) and lacks a credible growth trajectory or external validation. [confidence: high]

INTERPRETATION ERRORS:
- "Cotton textiles were ~33% of the Apr–Oct FY25 export basket vs man-made textiles ~15%." — This claim conflates fibre-level consumption (global ~70% MMF) with export basket composition, but the article does not clarify whether the 33% and 15% figures refer to fibre share in exports or garment categories. The comparison is apples-to-oranges because the global fibre share (~70% MMF) is not directly comparable to India's export basket share (which may include cotton garments made from MMF blends). [confidence: high]

- "The binding constraint is specialty fibre + technology. India imports high-performance fibres and the machinery for depolymerization-grade and high-tenacity output." — While the claim about import dependence is likely correct, the article does not provide evidence that the *machinery* for depolymerization-grade output is a binding constraint. The cited HS codes (e.g., 54021910, 5911) refer to fibres/fabrics, not machinery, and no data or expert source is cited to support the claim about machinery imports. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
