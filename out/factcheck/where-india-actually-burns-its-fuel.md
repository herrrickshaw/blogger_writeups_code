# Fact/interpretation check — where-india-actually-burns-its-fuel

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-india-actually-burns-its-fuel.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99542, Requested 2324. Please try again in 26m52.224s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026 · v1.0.0" — The article claims a publication date of 8 August 2026, but this is likely incorrect as the article references data from PPAC's workbook dated 8 August 2026, suggesting the publication date is likely the same as the data retrieval date, which is implausible for a published article. [confidence: high]

- "Delhi’s gas-infrastructure counts (CNG stations and domestic PNG connections, as on 31.05.2026, source PNGRB)" — The article cites PNGRB data as of 31 May 2026, but this date is in the future relative to the article's publication date (8 August 2026), which is impossible. [confidence: high]

INTERPRETATION ERRORS:
- "Delhi is the finding hiding in the slow column. The capital’s fuel sales grew 22% in sixteen years — a period in which its vehicle stock multiplied. The explanation is substitution, not stagnation: Delhi runs India’s densest gas transport network — 458 CNG station clusters and 19.6 lakh piped-gas connections on PNGRB’s May 2026 count — a metro carrying millions of trips, and the country’s most aggressive vehicle-age rules." — While the claim about Delhi's fuel sales growth is correct, the article assumes that the substitution effect (CNG, metro, vehicle rules) is the sole or primary reason for the slow growth in fuel sales without providing quantitative evidence or decomposition of contributions. The causal link is asserted but not substantiated. [confidence: high]

- "Sixteen years ago India sold 4.6 tonnes of diesel for every tonne of petrol; it now sells 2.3. The increment is two-wheelers and cars, not trucks and tractors — which is why the ethanol-blending programme (petrol-side) keeps gaining policy leverage while diesel-side interventions fade..." — The article implies a direct causal relationship between the shift in the diesel-to-petrol ratio and the composition of vehicle growth (two-wheelers and cars vs. trucks and tractors). However, it does not provide data or analysis to support this causal claim, nor does it rule out other contributing factors (e.g., fuel efficiency improvements, changes in industrial activity, or policy interventions like the ethanol-blending program). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
