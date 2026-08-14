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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99150, Requested 1854. Please try again in 14m27.456s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is the world's 6th-largest T&A exporter with ~3.9% global share." — This claim is unverifiable as the article does not provide a source for the global ranking or the 3.9% share. The cited sources (AEPC Annual Report 2024-25, CITI T&A export statistics, etc.) are not linked or quoted directly to confirm this specific statistic. [confidence: medium]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026), projected US$309 bn by 2047." — The projection of US$309 bn by 2047 is highly speculative and lacks a credible source or methodology. The intermediate figure (US$45 bn by 2026) is plausible but not verified in the article. [confidence: high]

INTERPRETATION ERRORS:
- "The MMF gap is visible inside the 6-digit codes. Nearly every heading forks into '…of cotton' (61xx2), '…of man-made fibres' (61xx3), '…of other'... India's exports concentrate in the cotton lines; the synthetic-fibre lines (610323, 610333, 610343, 610463, 610520, 610620, 611130, 611430…) are underweight against a world where MMF accounts for ~70% of fibre consumption (a fibre-level share, not a garment-purchase share — India's own basket skews the other way, see below)." — The article conflates fibre consumption share (~70% MMF globally) with garment export composition (where India's basket is cotton-skewed). The claim implies a causal link between global fibre consumption and India's export basket, but the two are not directly comparable. India's export structure is shaped by domestic industry strengths (e.g., cotton supply chains) and trade policies, not global fibre trends. [confidence: high]

- "Trade-data quality for this basket is reliable only post-2019." — While the 2019 HSN carve-out improved granularity, the article overstates the reliability of trade data. The carve-out enabled better tracking, but data quality depends on reporting accuracy, coverage gaps, and methodological consistency. The claim assumes perfect post-2019 data reliability without acknowledging potential limitations. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
