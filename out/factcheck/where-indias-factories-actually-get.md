# Fact/interpretation check — where-indias-factories-actually-get

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-indias-factories-actually-get.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99138, Requested 5907. Please try again in 1h12m38.88s. Need more tokens? Upgrade to Dev Tier today at htt]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 1,869,333 Rs cr implemented" — The correct figure for implemented industrial projects (Part B) from 2021–Dec 2025 is Rs 19,51,828 cr (as stated later in the article), not Rs 1,869,333 Rs cr. The "Rs cr" unit is redundant and incorrect. [confidence: high]

- "Rs 4.55 lakh cr in 2024-2025 alone" (Gujarat) — The article states Gujarat's 2024-2025 implementation is Rs 4.55 lakh cr, but the table shows Rs 208,025 cr (2024) + Rs 246,595 cr (2025 to Dec) = Rs 454,620 cr (Rs 4.55 lakh cr). However, the 2024-2025 fiscal year total is not directly comparable to the calendar-year data in the table. The claim conflates fiscal and calendar years without clarification. [confidence: high]

INTERPRETATION ERRORS:
- "Rs 70,117cr of the [Fuels sector's] total is one year (2025) -- likely a single refinery/energy mega-filing." — While the data shows a spike in Fuels sector implementation in 2025, attributing it to a single project ("likely a single refinery/energy mega-filing") is speculative. The article provides no evidence or external verification for this claim, and the DPIIT data does not specify project-level details. This is an overinterpretation of the aggregate data. [confidence: high]

- "Punjab's 356% [A→B conversion] is a small-base artifact (2023's Rs 32,182cr spike vs tiny same-period intent) -- old filings landing, not a boom in new intent." — While the article correctly notes the small-base effect, it does not adequately address the broader issue: the A→B conversion rate is a flow ratio (same-period intent vs. same-period implementation) and does not account for pre-2023 filings being implemented in 2023. The claim implies the spike is solely due to old filings, but the data does not isolate the source of the implementation surge. This is a misinterpretation of the conversion metric's limitations. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
