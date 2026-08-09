# Fact/interpretation check — from-cane-to-code-digital-layer

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/from-cane-to-code-digital-layer.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99896, Requested 3049. Please try again in 42m24.48s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The article references a document ("KPMG–ChiniMandi, 'Beyond E20' (June 2026)") and a Rajya Sabha question ("9 March 2026"), but the publication date of the article itself is stated as "8 August 2026," which is in the future relative to the cited sources. This is likely a typographical error, as publishing dates are typically not set in the future. [confidence: high]

- "20% Nationwide ethanol blending achieved in ESY2025-26 — five years ahead of the 2030 target" — The table shows ESY2025-26 as a partial year (November 2025–March 2026) with a blending rate of 20.0%, but the claim implies this is a full-year achievement. The partial-year data does not confirm a full-year 20% blending rate. [confidence: high]

INTERPRETATION ERRORS:
- "4–8% Additional ethanol yield claimed from AI-tuned fermentation, same molasses input" — The article presents this as a verified efficiency gain, but it is sourced from vendor-reported figures (Findability Sciences) that are not independently audited. The claim implies a causal relationship between AI tuning and yield improvement, but without primary operational data or third-party verification, the magnitude and generalizability of this effect remain uncertain. [confidence: high]

- "10–20% Farm yield improvement claimed for growers on an AI advisory pilot in Maharashtra" — The article treats this as a concrete outcome, but it is based on a small, unaudited pilot (the "Super 50 AI Farmers" in Jalna district). The claim extrapolates localized results to broader farm yield improvements without evidence of scalability or statistical significance. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
