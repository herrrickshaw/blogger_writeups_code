# Fact/interpretation check — blending-on-budget-energy-density-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/blending-on-budget-energy-density-and.html`

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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India now has one live nationwide fuel-blending mandate (E20 petrol)" — The article incorrectly states that E20 petrol is a live nationwide mandate. As of the article's publication date (19 August 2026), E20 petrol is only a voluntary standard in India, not a nationwide mandate. The government has not yet mandated E20 nationwide, despite pilot programs and discussions. [confidence: high]

- "SAF in ATF ... from 2027" — The article claims India's SAF mandate starts in 2027, but this is incorrect. India's SAF policy, aligned with ICAO's CORSIA Phase II, actually begins with 1% blending from 2025, not 2027. The timeline is misstated. [confidence: high]

INTERPRETATION ERRORS:
- "Ethanol in petrol ... E20 sells at the same price as the petrol it replaced" — The article assumes that E20 petrol is sold at the same price as E0 petrol, implying no price premium for the blend. However, ethanol typically trades at a discount to petrol, and blending costs (denaturing, logistics) may not fully offset this. The claim ignores potential price differentials that could affect consumer costs beyond mileage loss. [confidence: medium]

- "Isobutanol in diesel ... the government is working toward blending isobutanol into diesel at up to 15%, targeted from 2027" — The article treats the 15% isobutanol-diesel blend as a fait accompli based on a ministerial announcement, but this is a proposed mandate, not a finalized policy. The interpretation extrapolates from an unnotified proposal to a near-certain outcome, ignoring regulatory and industry uncertainties. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
