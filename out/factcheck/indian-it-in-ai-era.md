# Fact/interpretation check — indian-it-in-ai-era

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indian-it-in-ai-era.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "4 August 2026" — The article is dated in the future relative to the current date (2025), making it unverifiable and likely incorrect. [confidence: high]

- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year" — The RBI data in Exhibit 1 shows net services receipts rising from $188.8bn (FY2024-25) to $216.6bn (FY2025-26), which is an increase of $27.8bn. However, the article later states that the merchandise trade deficit widened by $50 billion in FY2026 alone, which contradicts the RBI data showing a $50.4bn increase ($337.3bn - $286.9bn). The $50bn figure is not supported by the RBI data. [confidence: high]

INTERPRETATION ERRORS:
- "The warning signs are elsewhere: net hiring has collapsed from ~450,000 (FY22) to 135,000 (FY26) against a growing revenue base, and chief executives now name 'AI deflation' worth 3–5% of revenue" — While the hiring decline and executive statements about "AI deflation" are factual, the article implies a causal link between AI and the hiring collapse without sufficient evidence. The hiring slowdown could be due to other factors (e.g., post-pandemic normalization, automation unrelated to AI, or strategic shifts in hiring practices), and the "AI deflation" figures are forward-looking estimates, not measured impacts. [confidence: medium]

- "It can produce a balance-of-payments event. If services receipts stall while the goods deficit keeps widening — and it widened by $50 billion in FY2026 alone — the adjustment happens in the exchange rate and the capital account, not in the unemployment rate." — The article conflates the goods deficit widening ($50bn) with services receipts stalling, but the data shows services receipts grew by $27.8bn in FY2025-26. The claim that the goods deficit widened by $50bn in FY2026 alone is not directly tied to services receipts stalling, and the causal link to exchange rate adjustments is speculative without evidence of an imminent stall. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
