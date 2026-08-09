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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99299, Requested 7576. Please try again in 1h39m0s. Need more tokens? Upgrade to Dev Tier today at https:/]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Installed national capacity stood at roughly 2,000 crore litres/year for ethanol supply year 2025–26 (CareEdge, May 2026)" — The CareEdge report cited ("E85 Impact: Ethanol Overcapacity to Persist," May 14, 2026) states that India has **700 crore litres/year of structural ethanol overcapacity**, not 2,000 crore litres/year of installed capacity. The article later corrects this but initially misrepresents the figure. [confidence: high]

- "The Department of Food & Public Distribution’s sanction register is far larger — roughly 4,530 crore litres across 1,212 approved projects" — While the DFPD sanction register may list approved projects, the article does not provide a source or verification for the 4,530 crore litres figure, which appears to be an unsupported claim. [confidence: medium]

INTERPRETATION ERRORS:
- "A cane-surplus state that exports ethanol to a deficit state does not automatically keep that ethanol’s SGST — place-of-supply rules route it to the consuming state, subject to IGST settlement on the interstate movement." — While the claim about destination-based GST is correct, the article does not quantify the actual SGST revenue flows between states due to interstate ethanol movement. Without modeling the IGST settlement mechanics or actual state-wise ethanol transfers, the conclusion that "production capacity and SGST revenue are two separate maps" is speculative and lacks empirical support. [confidence: high]

- "Even a full 5% dedicated SGST recovers only 3–18% of the VAT states forgo, depending on rate and blend — it offsets part of the shortfall in Section 3.1, it does not close it." — The article correctly notes that a 5% dedicated SGST does not fully offset the VAT loss, but it does not address whether a higher SGST rate (e.g., 27%) would be politically or economically feasible. The conclusion that "full parity recovery would need a rate near 27%" is presented as a fait accompli without discussing the feasibility or unintended consequences of such a high rate, making this an apples-to-oranges comparison between a hypothetical tax rate and the current tax structure. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
