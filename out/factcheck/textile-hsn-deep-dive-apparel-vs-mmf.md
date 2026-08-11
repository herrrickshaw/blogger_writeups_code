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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99246, Requested 1808. Please try again in 15m10.656s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is the world's 6th-largest T&A exporter with ~3.9% global share." — The claim about India's global share is not verifiable from the provided sources or standard trade databases (e.g., UN Comtrade). The 6th-largest exporter claim may also be outdated or incorrect, as recent data often ranks India as the 2nd or 3rd largest T&A exporter globally. [confidence: medium]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026) , projected US$309 bn by 2047." — The projection of US$309 bn by 2047 is highly speculative and lacks credible sourcing or methodological justification. Such long-term projections are typically based on detailed econometric models, which are not referenced here. [confidence: high]

INTERPRETATION ERRORS:
- "The MMF gap is visible inside the 6-digit codes. Nearly every heading forks into "…of cotton" (61xx2), "…of man-made fibres" (61xx3), "…of other" . India's exports concentrate in the cotton lines ; the synthetic-fibre lines (610323, 610333, 610343, 610463, 610520, 610620, 611130, 611430…) are underweight against a world where MMF accounts for ~70% of fibre consumption (a fibre-level share, not a garment-purchase share — India's own basket skews the other way, see below)." — The claim implies that India's underweight in synthetic-fibre apparel exports is a problem or gap, but it does not logically follow that this is an issue. The global fibre consumption share (~70% MMF) is not directly comparable to garment export shares, as consumer preferences, production costs, and trade dynamics differ. The reasoning conflates fibre-level consumption with export competitiveness without justification. [confidence: high]

- "Exports ≈ US$3 bn (FY24), growing >15%/yr from near-zero a decade ago; imports ≈ US$2.5 bn — roughly trade-balanced overall but a net importer in the high-value segments." — While the trade balance may appear balanced in aggregate, the claim that India is a "net importer in the high-value segments" is not supported by the data provided. The article does not specify which segments are high-value or provide evidence of net import dependence in those segments beyond listing examples (e.g., Meditech, Protech). The conclusion extrapolates from partial data without clear segmentation or trade flow analysis. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
