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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99822, Requested 1854. Please try again in 24m8.064s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is the world's 6th-largest T&A exporter with ~3.9% global share." — The source cited (PIB) likely refers to a specific year (e.g., FY2022-23), but the article presents this as a current claim for FY2024-25 without a time qualifier. The global ranking and share may have changed by FY2024-25, and the article does not provide updated verification. [confidence: medium]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026) , projected US$309 bn by 2047." — The projection to 2047 (US$309 bn) appears implausibly high compared to global technical-textiles market estimates (e.g., global market is projected at ~US$250–300 bn by 2030, making a 2047 projection of US$309 bn for India alone seem unrealistic). [confidence: high]

INTERPRETATION ERRORS:
- "The MMF gap is visible inside the 6-digit codes. Nearly every heading forks into '…of cotton' (61xx2), '…of man-made fibres' (61xx3), '…of other'... India's exports concentrate in the cotton lines; the synthetic-fibre lines (610323, 610333, 610343, 610463, 610520, 610620, 611130, 611430…) are underweight against a world where MMF accounts for ~70% of fibre consumption (a fibre-level share, not a garment-purchase share — India's own basket skews the other way, see below)." — The claim conflates fibre consumption share (global) with garment export composition (India-specific). While India's apparel exports are cotton-skewed, the statement implies India's underweight in synthetic-fibre garment exports is due to global MMF dominance, which is not a valid causal link. The "gap" is correctly noted (India's export basket skew), but the reasoning misattributes the cause to global fibre consumption rather than India's domestic production capabilities or policy factors. [confidence: high]

- "Exports ≈ US$3 bn (FY24), growing >15%/yr from near-zero a decade ago; imports ≈ US$2.5 bn — roughly trade-balanced overall but a net importer in the high-value segments." — The article presents exports and imports as "roughly trade-balanced" but then contradicts this by stating India is a net importer in high-value segments. The "roughly trade-balanced" claim is misleading because it averages across all segments, including low-value ones where India may have a surplus. The conclusion about net importer status in high-value segments is correct, but the initial framing of "trade-balanced overall" is an apples-to-oranges comparison that obscures the structural deficit in high-value technical textiles. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
