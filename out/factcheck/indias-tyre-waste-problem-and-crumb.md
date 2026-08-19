# Fact/interpretation check — indias-tyre-waste-problem-and-crumb

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-tyre-waste-problem-and-crumb.html`

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
- "Lab testing at India’s SSPACE Wardha civil engineering department, reported in a 2025 study" — The article cites a 2025 study, but 2025 is in the future as of the current date (2023). This is likely a typographical error or misattribution. [confidence: high]

- "Revenue was around ₹572 crore in the most recent reported year. In FY2026 the company won a two-year, ₹75.79 crore contract" — The article mixes FY2026 revenue and contract figures, but FY2026 is in the future. This is inconsistent with standard fiscal year reporting. [confidence: high]

INTERPRETATION ERRORS:
- "CRMB doesn't eliminate this dependency — the lab data in the previous section shows crumb rubber typically substitutes at 5-14% of binder content, not a wholesale bitumen replacement. But at India's road-construction volumes, even a single-digit percentage substitution across the CRMB-eligible network share represents a real, quantifiable dent in a multi-billion-dollar import bill concentrated in three countries." — While the substitution percentage is correct, the claim that this "represents a real, quantifiable dent" in the import bill lacks quantification or evidence. The article does not provide data on how much CRMB is actually used in road construction or the resulting reduction in bitumen imports. [confidence: high]

- "The 100%-of-production EPR target now in force from 2024-25 is the clearest signal yet that this shifts from a niche technical option to a mainstream compliance-driven material stream." — While the EPR target is a strong policy signal, the article does not provide evidence that CRMB use has actually shifted from niche to mainstream. The claim assumes compliance with EPR will directly translate to increased CRMB adoption, but this is not necessarily supported by the data presented. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
