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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Used 8210, Requested 5286. Please try again in 7.48s. Need more tokens? Upgrade to Dev Tier today at https://]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Services · Balance of payments · 4 August 2026" — The article is dated 4 August 2026, but the referenced data (e.g., FY2025-26 figures) and sources (e.g., RBI's Q4 2025-26 report) are for FY2025-26, which ends on 31 March 2026. The article incorrectly labels the fiscal year as 2026-27 or later. [confidence: high]

- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The RBI data in Exhibit 1 shows net services receipts rising from $188.8bn (FY2024-25) to $216.6bn (FY2025-26), a $27.8bn increase. However, the article later cites NASSCOM's Strategic Review 2026, which restated FY2024-25 services receipts from $188.8bn to $268.8bn, implying the $27.8bn increase is based on the restated figure. The original RBI figure ($188.8bn) is correct, but the article does not clarify this restatement, making the claim misleading. [confidence: high]

INTERPRETATION ERRORS:
- "The warning signs are elsewhere: net hiring has collapsed from ~450,000 (FY22) to 135,000 (FY26) against a growing revenue base, and chief executives now name 'AI deflation' worth 3–5% of revenue." — While the hiring and revenue data are correct, the article conflates correlation with causation. The collapse in net hiring could be due to factors other than AI (e.g., automation, outsourcing, or structural shifts in the industry), and the "AI deflation" claim is based on executive testimony rather than measured displacement. The article assumes AI is the primary driver without sufficient evidence. [confidence: medium]

- "So when people ask whether AI threatens Indian IT, the question that matters for the country is narrower and sharper: does it threaten the dollar receipts that make a $337 billion goods deficit survivable at 0.6% of GDP?" — The article correctly notes that services receipts offset the goods deficit, but it overstates the causal link between AI and potential threats to dollar receipts. The data shows AI has increased productivity and volumes, but the "AI deflation" (price erosion) is a separate issue. The conclusion that AI threatens dollar receipts is an extrapolation beyond the evidence, as the article itself acknowledges that the displacement has not been measured. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
