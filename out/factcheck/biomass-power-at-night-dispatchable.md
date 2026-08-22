# Fact/interpretation check — biomass-power-at-night-dispatchable

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/biomass-power-at-night-dispatchable.html`

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
- "biomass power grew just 19% — the slowest of any renewable category, in the one slot on the grid where a dispatchable renewable should be winning" — The article later contradicts this claim by stating biomass grew "roughly a ninth" (11.1%) of the total non-hydro renewable growth rate (178%), not "just 19%." The 19% figure refers to absolute growth in MW (from 9,861 MW to 11,747.57 MW), while the "slowest" comparison is relative to the total non-hydro renewable growth rate. The phrasing conflates absolute and relative growth, making the claim misleading. [confidence: high]

- "the Ministry of New & Renewable Energy's state-wise installed renewable capacity table, dated 31 July 2026" — The article cites this table as the source for 2026 biomass capacity figures, but the date "31 July 2026" is in the future relative to the article's publication date (20 August 2026). This is likely a typographical error, as capacity tables are typically dated at the end of a month or quarter, not in the future. [confidence: high]

INTERPRETATION ERRORS:
- "Biomass power can run at night. It is one of the few renewable sources that actually can. And yet, while India's total renewable capacity (excluding large hydro) grew 178% between December 2019 and July 2026, biomass power grew just 19% — the slowest of any renewable category, in the one slot on the grid where a dispatchable renewable should be winning." — The article implies that biomass should have grown faster because it is dispatchable at night, but it does not account for the fact that biomass growth is constrained by feedstock availability, capital costs, and policy barriers (e.g., PPA structures) that are unrelated to its dispatchability. The claim assumes that dispatchability alone should drive growth, ignoring other economic and logistical factors. [confidence: high]

- "A 10–20% peak-hour premium is a percentage of the 'normal tariff' a state commission sets — for competitively bid solar and wind power in India, that normal tariff typically sits in the ₹2.5–3.5/kWh range, several times lower than biomass's own levellised cost before any ToD premium is even applied." — The article correctly notes that biomass's levellised cost (₹9.6–11.1/kWh) is higher than solar/wind tariffs, but it does not explain whether the ToD premium is applied to biomass generators or only to consumers. If the premium is not passed through to biomass generators (e.g., via PPAs), then the economic signal is ineffective, and the interpretation that the premium "isn't enough" is incomplete without evidence of pass-through. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
