# Fact/interpretation check — indias-coffee-crop-hasnt-grown-in

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-coffee-crop-hasnt-grown-in.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

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
- "India grows roughly 4% of the world's coffee and ranks 7th globally by volume" — This claim is outdated. The article later cites USDA FAS GAIN reports and other sources confirming India's global rank is now 6th (not 7th), with Ethiopia and Uganda surpassing it. [confidence: high]

- "the Coffee Board's 2025-26 post-blossom estimate shows an 11% single-season jump to roughly 403,000 tonnes" — The article later clarifies that the 403,000-tonne figure is a post-blossom estimate, not a final production figure. However, the initial claim implies it is a finalized production number, which is misleading. [confidence: high]

INTERPRETATION ERRORS:
- "record export earnings say more about that shift [to instant coffee and extracts] than about any growth in the crop itself, which has been essentially flat for a decade" — While the crop has been flat for a decade, the article later introduces a significant 11% single-season production jump (403,000 tonnes in 2025-26). The claim that export earnings are solely due to processing shifts ignores the potential contribution of this production increase to export volumes and earnings. [confidence: high]

- "Labour is roughly 65–70% of India's coffee production cost, against about 25% in Brazil — the single structural gap most repeatedly cited for why Indian coffee struggles on cost competitiveness" — While the labour cost disparity is real, the article does not provide evidence that this alone explains India's cost competitiveness struggles. Other factors like smallholder fragmentation, ageing bushes, climate volatility, and export dependence are also cited but not weighed against the labour cost claim to support the conclusion. [confidence: medium]
