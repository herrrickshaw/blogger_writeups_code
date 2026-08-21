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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Installed national capacity stood at roughly 2,000 crore litres/year for ethanol supply year 2025–26 (CareEdge, May 2026)" — This claim is incorrect because the CareEdge report cited ("E85 Impact: Ethanol Overcapacity to Persist," May 14, 2026) explicitly states that India has **700 crore litres/year of structural ethanol overcapacity**, not 2,000 crore litres/year. The article misrepresents the report's findings by conflating installed capacity with overcapacity. [confidence: high]

- "The Department of Food & Public Distribution’s sanction register is far larger — roughly 4,530 crore litres across 1,212 approved projects" — While the article correctly cites the DFPD sanction register, it does not clarify that these are **approved capacities**, not actual installed capacities. The article implies a direct relationship between sanctioned and installed capacity without acknowledging the significant gap (as noted in the CareEdge report). [confidence: high]

INTERPRETATION ERRORS:
- "A cane-surplus state that exports ethanol to a deficit state does not automatically keep that ethanol’s SGST — place-of-supply rules route it to the consuming state, subject to IGST settlement on the interstate movement." — While this claim is factually correct, the article **overgeneralizes the SGST revenue impact** by implying that all ethanol exports result in SGST revenue loss for the producing state. The actual SGST revenue depends on the **IGST settlement mechanism**, which may partially compensate the producing state. The article does not account for this nuance, leading to an oversimplified interpretation of the fiscal impact. [confidence: medium]

- "Even a full 5% dedicated SGST recovers only 3–18% of the VAT states forgo, depending on rate and blend — it offsets part of the shortfall in Section 3.1, it does not close it." — The article correctly states the limited recovery from a 5% dedicated SGST, but it **misinterprets the policy objective**. The purpose of such a levy is not to fully offset the VAT loss but to **partially compensate states for foregone revenue** while maintaining price neutrality. The article frames the 5% levy as a failure to "close" the shortfall, which is an apples-to-oranges comparison (policy goal vs. full revenue replacement). [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
