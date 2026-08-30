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

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹72,325.82cr (~$8.28bn) FY2025-26 seafood export earnings" — The article cites MPEDA data for FY2025-26 seafood exports, but the same figure is later repeated as "₹72,325.82cr (~$8.28bn) Record India seafood export value, FY2025-26". The claim is inconsistent because the article also states that "seafood exports hit an all-time high of ₹72,325.82 crore (~$8.28 billion) in FY2025-26", implying this is a record, which contradicts the earlier phrasing that treats it as a projection (FY2025-26 is not yet complete as of the current date). [confidence: high]

- "tallow volumes were forecast at around 9,000 tonnes as of 2022" — The article cites a forecast from 2022 without specifying the source or methodology. This figure appears unverifiable against publicly available data, and no primary source is directly linked in the text to confirm this claim. [confidence: medium]

INTERPRETATION ERRORS:
- "India's National Biofuel Policy already permits tallow as a biodiesel feedstock, and the country carries a 5% biodiesel blending (B5) target for 2030... In practice, tallow supplies only a small fraction of what actually gets used: used cooking oil (UCO) accounted for roughly 35% of India's biodiesel feedstock in 2023, while animal fat and tallow contributed only about 3%." — The article correctly notes the low contribution of tallow to biodiesel feedstock, but then implies that the constraint on scaling tallow-to-biodiesel is purely structural (volatility and logistics), ignoring potential economic and policy barriers such as the lack of price incentives, competing uses for tallow, or the absence of a dedicated procurement mechanism. The reasoning gap is that the article assumes the policy mandate (B5 by 2030) will drive demand for tallow without addressing whether market conditions or policy support exist to make tallow competitive as a feedstock. [confidence: high]

- "The forward projection is aggressive: India's shrimp market is expected to grow at a 9.60% CAGR from 2026-2035, reaching roughly 2.55 million tonnes of volume by the end of that window — a scale-up that dwarfs the tallow-biodiesel opportunity in absolute size, even though both start from the same underlying idea of turning an animal-protein production base into a structured export or energy business." — The article compares the projected shrimp export volume (2.55 million tonnes by 2035) with the tallow-biodiesel "opportunity" without clarifying the units or context of the latter. Tallow volumes are discussed in tonnes (e.g., 9,000 tonnes forecast), while shrimp is measured in metric tonnes (1,000 kg units). The comparison is apples-to-oranges because shrimp export volume is not directly comparable to tallow production volume in terms of energy output or economic value. The reasoning gap is that the article conflates different metrics without normalization or explanation. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
