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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99171, Requested 7620. Please try again in 1h37m47.424s. Need more tokens? Upgrade to Dev Tier today at ht]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Installed national capacity stood at roughly 2,000 crore litres/year for ethanol supply year 2025–26 (CareEdge, May 2026)" — The CareEdge report cited ("E85 Impact: Ethanol Overcapacity to Persist," May 14, 2026) states that India has **700 crore litres/year of structural ethanol overcapacity**, not 2,000 crore litres/year of installed capacity. The 2,000 crore litres/year figure likely refers to total capacity including approved but unbuilt projects, but the article misrepresents it as actual installed capacity. [confidence: high]

- "The Department of Food & Public Distribution’s sanction register is far larger — roughly 4,530 crore litres across 1,212 approved projects" — While the DFPD sanction register may list 4,530 crore litres of approved capacity, the CareEdge report explicitly states that **distilleries are running at only 60–65% utilization**, meaning the actual installed capacity is lower than the sanctioned figure. The article conflates sanctioned capacity with actual capacity without clarifying this discrepancy. [confidence: high]

INTERPRETATION ERRORS:
- "The capacity source says the opposite of 'clean buildout.' The CareEdge Ratings report cited above (“E85 Impact: Ethanol Overcapacity to Persist,” May 14, 2026) is not describing healthy capacity growth — its actual thesis, stated as its own headline finding, is that India has roughly 700 crore litres/year of structural ethanol overcapacity, with distilleries running at only 60–65% utilization" — While the CareEdge report does highlight overcapacity, the article incorrectly implies that this overcapacity is a direct contradiction to "clean buildout." The report's thesis is about **persistent overcapacity**, not the absence of capacity growth. The article frames it as a binary (clean buildout vs. overcapacity) when the reality is a nuanced situation where capacity has grown but utilization remains low due to structural issues. [confidence: high]

- "Even a full 5% dedicated SGST recovers only 3–18% of the VAT states forgo, depending on rate and blend — it offsets part of the shortfall in Section 3.1, it does not close it." — The article presents the 5% dedicated SGST as a potential policy solution but does not adequately explain why a higher rate (e.g., 27%) would be politically or economically infeasible. The claim that a 27% rate would "stop being a modest, price-neutral levy" is an assertion without supporting evidence or analysis of the actual policy trade-offs involved. The interpretation gap is that the article does not explore the feasibility or implications of higher SGST rates beyond the illustrative 1–5% range. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
