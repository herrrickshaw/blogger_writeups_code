# Fact/interpretation check — indias-coffee-crop-hasnt-grown-in

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-coffee-crop-hasnt-grown-in.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India grows roughly 4% of the world's coffee and ranks 7th globally by volume" — This claim is outdated. The article later cites USDA FAS GAIN reports and other sources confirming India's global rank as 6th (not 7th), with Brazil (35%), Vietnam (18%), Colombia, Indonesia, and Ethiopia ahead of India. [confidence: high]

- "the Coffee Board's 2025-26 post-blossom estimate shows an 11% single-season jump to roughly 403,000 tonnes" — While the 403,000-tonne figure is correct, the article incorrectly states this is a "single-season jump" from the 2024-25 final tally of 363,500 tonnes. The actual jump is from the 2024-25 final tally of 363,500 tonnes to the 2025-26 post-blossom estimate of 403,000 tonnes, which is an 11% increase. The phrasing implies a comparison to the 2025-26 second-advance estimate (373,000 tonnes), which would make the jump ~8%, not 11%. [confidence: high]

INTERPRETATION ERRORS:
- "record export earnings say more about that shift [to instant coffee and extracts] than about any growth in the crop itself, which has been essentially flat for a decade" — While the crop has been flat for a decade, the article later cites a significant 11% single-season jump in production (403,000 tonnes in 2025-26). The claim that export earnings are driven *only* by the shift to processed coffee ignores the potential contribution of this production increase to export volumes and earnings. The reasoning gap is that the article does not reconcile the decade-long stagnation with the recent production spike when attributing export earnings growth solely to processing shifts. [confidence: high]

- "Labour is roughly 65–70% of India's coffee production cost, against about 25% in Brazil — the single structural gap most repeatedly cited for why Indian coffee struggles on cost competitiveness" — While the labour cost disparity is a valid structural issue, the article does not provide evidence that this *alone* explains India's cost competitiveness struggles. Other factors, such as scale (98% smallholders vs. Brazil's plantation model), ageing bushes, climate volatility, and export dependence (95% of crop exported), are also cited in the article but not weighed against the labour cost claim. The reasoning gap is that the article presents labour costs as the *primary* structural gap without addressing these other contributing factors in the same context. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
