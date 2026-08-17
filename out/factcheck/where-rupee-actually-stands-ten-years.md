# Fact/interpretation check — where-rupee-actually-stands-ten-years

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-rupee-actually-stands-ten-years.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99495, Requested 6304. Please try again in 1h23m30.336s. Need more tokens? Upgrade to Dev Tier today at ht]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "14 August 2026" (date in the article title and multiple places) — The article is dated in the future (2026), which is impossible for a published piece. The correct date should be 2024 or 2025. [confidence: high]

- "CNY, RUB and SAR have no direct, officially published INR reference rate (see Section 4)" — While the article correctly notes that FBIL does not publish direct INR reference rates for CNY, RUB, or SAR, it incorrectly states that SAR has no direct reference rate. The UAE dirham (AED) is listed as having a direct FBIL reference rate, but the Saudi riyal (SAR) does not. However, the article later contradicts itself by stating that SAR/INR is derived as a USD cross-rate, which is correct. The claim about SAR is misleading because it implies SAR is in the same category as CNY and RUB, but SAR's peg to USD makes its derived rate more stable and predictable. [confidence: high]

INTERPRETATION ERRORS:
- "The rouble is the outlier, and not in the direction the other four suggest: it sits at just 112, the shallowest ten-year rise of the five, but it got there by way of the sharpest single move on the chart — the vertical plunge and rebound around 2022, when the rouble first crashed against every currency in the wake of the Ukraine invasion sanctions, then recovered hard as Russia's central bank imposed capital controls and its energy-export earnings kept flowing in roubles." — The article correctly describes the rouble's volatility but misinterprets the ten-year trend. The shallow rise (+4.1%) is not a meaningful indicator of the rouble's actual performance because it is dominated by the extreme 2022 crash and rebound. The ten-year change is a mechanical artifact of measuring from a post-crash low, not a genuine reflection of long-term weakness or strength. The article acknowledges this later but frames the initial observation as if the ten-year trend were a valid standalone conclusion. [confidence: high]

- "Rupee-invoicing India's exports (the USA relationship, Section 7's one surplus) creates genuine foreign demand for rupees — a buyer abroad has to acquire INR to pay an Indian exporter, which is currency-supportive in the same direction a stronger current account already is." — While the claim about foreign demand for rupees is correct, the interpretation that this necessarily strengthens the rupee is an oversimplification. The article does not account for the fact that the impact on the rupee's value depends on the RBI's intervention, capital flows, and broader macroeconomic conditions. The claim assumes a direct and unconditional link between rupee invoicing and currency strength, which is not supported by the data or economic theory. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
