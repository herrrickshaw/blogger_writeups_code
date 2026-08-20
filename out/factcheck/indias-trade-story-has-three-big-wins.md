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
- "India's exports hit a record US$825.3 billion in FY25 across goods and services combined, per the Economic Survey 2025-26" — The article cites the Economic Survey 2025-26, but the date in the article header is "Published 8 August 2026 · v1.0.0 · Economic Survey 2025-26," which implies the survey covers FY2025-26 (April 2025–March 2026), not FY25 (April 2024–March 2025). The figure likely belongs to FY2025-26, not FY25. [confidence: high]

- "Services exports alone reached an all-time high of US$387.5 billion, up 13.6% year-on-year" — The article does not provide a source for this specific figure or the year-on-year growth rate, and it is not clearly attributed to the Economic Survey 2025-26 or any other verifiable source within the text. [confidence: medium]

INTERPRETATION ERRORS:
- "The PLI scheme has attracted 26% more investment than its own approved outlay — ₹2.40 lakh crore against ₹1.91 lakh crore" — While the PLI scheme's investment figures are factually correct, the article implies that this overshooting is a direct measure of success without addressing potential inefficiencies or overestimation in the approved outlay. The 26% overshoot could reflect conservative initial estimates rather than exceptional performance, and the article does not explore whether the actual economic impact (e.g., net exports, job sustainability) justifies the higher investment. [confidence: high]

- "Whether that is a genuine policy gap or simply a reflection of services already being globally competitive without needing the same subsidy architecture is a judgement this article does not make — it only surfaces that the asymmetry exists" — The article highlights the mismatch between policy focus (goods) and export growth (services) but does not critically assess whether the lack of services-specific policies is justified by market dynamics or if it reflects an oversight. The claim that services may already be globally competitive is speculative and not supported by data in the article. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
