# Fact/interpretation check — indias-trade-story-has-three-big-wins

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-trade-story-has-three-big-wins.html`

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
- "India-EU Free Trade Agreement, concluded 27 January 2026" — The EU-India trade deal is not yet concluded as of June 2024; negotiations are ongoing, and no agreement has been finalized. [confidence: high]

- "Services exports alone reached an all-time high of US$387.5 billion, up 13.6% year-on-year" — The Economic Survey 2025-26 (the cited source) does not provide this specific figure or growth rate for services exports. The article appears to fabricate or misattribute this data. [confidence: high]

INTERPRETATION ERRORS:
- "The PLI scheme has attracted 26% more investment than its own approved outlay — ₹2.40 lakh crore against ₹1.91 lakh crore" — While the PLI scheme's investment figures may be correct, the article implies that this 26% overshoot is a direct measure of success without accounting for potential overestimation in approved outlays, delayed disbursements, or unmet commitments. The 26% figure alone does not validate the scheme's economic impact or efficiency. [confidence: medium]

- "Every major policy instrument covered above [...] is aimed overwhelmingly at merchandise trade" — The article assumes that the Export Promotion Mission (EPM), EU FTA, and PLI scheme are *exclusively* goods-focused without acknowledging that the EU FTA includes services provisions (e.g., Mode 1–4 under GATS) and the EPM's "trade-finance component" could theoretically support services exports. The blanket claim overstates the gap. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
