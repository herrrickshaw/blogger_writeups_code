# Fact/interpretation check — india-grain-cultivation-fci-storage

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-grain-cultivation-fci-storage.html`

## Gemini gemini-flash-latest

[Gemini API error 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Punjab has 569 FCI depots but only 78 FPOs" — The article later states that Punjab has 174.5 LMT storage, 78 FPOs, and 569 FCI depots, which seems to be consistent, but without external verification, it's unclear if these numbers are accurate [confidence: medium]
- "Uttar Pradesh has 758 FPOs (the most of any state)" — According to the article, the India-wide FPO count is ~45,000 across all promoting agencies, and the SFAC channel only has 3,649 FPOs, but it's unclear if 758 is the correct number for Uttar Pradesh without external verification [confidence: medium]

INTERPRETATION ERRORS:
- "the storage belt and the FPO belt are different states" — This conclusion is based on the observation that some states have high storage capacity but low FPO counts, and vice versa, but it doesn't necessarily follow that the two are distinct, as there could be other factors at play [confidence: medium]
- "Madhya Pradesh has both (200 LMT storage, 348 FPOs); Punjab has 174 LMT of storage but only 78 FPOs" — The article uses these examples to illustrate the difference between the storage belt and the FPO belt, but it's unclear if these specific examples are representative of the broader trend, or if they are cherry-picked to support the conclusion [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Punjab has 569 FCI depots but only 78 FPOs" — The article later contradicts this by stating Punjab has 569 FCI depots, 78 FPOs, and 174.5 LMT storage. The initial claim is inconsistent with the later detailed breakdown. [confidence: high]

INTERPRETATION ERRORS:
- "the storage belt and the FPO belt are different states" — While the data shows a divergence between states with high storage capacity (e.g., Madhya Pradesh, Punjab) and those with high FPO counts (e.g., Uttar Pradesh), the article does not provide evidence or analysis to support the causal or conceptual claim that these are distinct "belts." The term implies a geographic or functional separation that is not substantiated by the data presented. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
