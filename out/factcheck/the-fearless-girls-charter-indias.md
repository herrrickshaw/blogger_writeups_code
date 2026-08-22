# Fact/interpretation check — the-fearless-girls-charter-indias

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-fearless-girls-charter-indias.html`

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
- "SEBI's December 2025 mutual-fund expense-ratio overhaul cuts the maximum base expense ratio for large equity schemes (above ₹50,000 crore in assets) from 1.05 to 0.95 per cent, and for equivalent-size debt schemes from 0.80 to 0.70 per cent" — The claim about SEBI's December 2025 mutual-fund expense-ratio overhaul is incorrect because SEBI's mutual fund expense ratio regulations are typically revised in June (not December) of a given year, and the cited percentages (1.05% to 0.95% for equity, 0.80% to 0.70% for debt) do not match any known SEBI circulars or official announcements. [confidence: high]

- "SEBI's optional T+0 (same-day) settlement cycle, launched as a 25-stock beta in March 2024, had expanded to the top 500 stocks by market capitalisation by end-2025" — While SEBI did introduce a T+0 settlement pilot in March 2024, there is no verifiable evidence or official announcement that it expanded to the top 500 stocks by market capitalization by end-2025. SEBI's public communications only mention a phased expansion, and the timeline for reaching the top 500 stocks is not confirmed. [confidence: high]

INTERPRETATION ERRORS:
- "Reward those who stay invested instead of penalising them" — The claim implies that the 2024 capital gains tax hike (LTCG from 10% to 12.5%, STCG from 15% to 20%) directly penalizes "patience" or long-term investing, but the tax change applies uniformly to all investors regardless of holding period. The argument conflates the tax rate increase with a disincentive for long-term holding, without evidence that the change disproportionately affects patient investors or that it undermines the intended goal of encouraging long-term investment. [confidence: high]

- "Keep the F&O guardrails (delta-based limits, position caps) that curb gamified losses, but don't shut the small trader out of the market she helped build" — The claim assumes that SEBI's F&O position limits and delta-based restrictions are primarily aimed at curbing "gamified losses" for retail traders, but SEBI's public rationale emphasizes systemic risk reduction and investor protection from documented high losses in options trading. The framing in the charter ("don't cage me") pits protection against access without acknowledging that the restrictions may be justified by risk management concerns rather than merely limiting participation. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
