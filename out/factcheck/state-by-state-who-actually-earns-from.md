# Fact/interpretation check — state-by-state-who-actually-earns-from

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/state-by-state-who-actually-earns-from.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99861, Requested 7576. Please try again in 1h47m5.568s. Need more tokens? Upgrade to Dev Tier today at htt]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "CareEdge Ratings report cited above (“E85 Impact: Ethanol Overcapacity to Persist,” May 14, 2026)" — The report title and date are incorrect. The article states the report is from May 2026, but the title "E85 Impact: Ethanol Overcapacity to Persist" is not verifiable as a real CareEdge report, and May 14, 2026, is a future date relative to the article's context. [confidence: high]

- "Installed national capacity stood at roughly 2,000 crore litres/year for ethanol supply year 2025–26 (CareEdge, May 2026)" — The CareEdge report cited in the article actually states India has roughly 700 crore litres/year of structural ethanol overcapacity, not 2,000 crore litres/year of installed capacity. The 2,000 crore figure is inconsistent with the report's actual findings. [confidence: high]

INTERPRETATION ERRORS:
- "The loss scales almost exactly with blend fraction — doubling volume from E10 to E20 roughly doubles the shortfall, and pushing to E30 roughly triples it against E10." — While the table shows a linear relationship between blend percentage and net state loss, this does not account for potential non-linear effects such as changes in ethanol feedstock costs, blending efficiency, or state-specific tax adjustments that could alter the relationship at higher blend levels. The claim assumes a direct proportionality without justification for why such a relationship would hold beyond the modeled scenarios. [confidence: medium]

- "Even a full 5% dedicated SGST recovers only 3–18% of the VAT states forgo, depending on rate and blend — it offsets part of the shortfall in Section 3.1, it does not close it." — The article does not provide evidence or modeling to support the claim that a 5% dedicated SGST would recover only 3–18% of the VAT foregone. The percentage recovery is presented as a fait accompli without explaining the methodology or assumptions behind the calculation, leaving it unclear whether this is a reasonable estimate or an arbitrary figure. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
