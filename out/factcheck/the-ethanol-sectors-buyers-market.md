# Fact/interpretation check — the-ethanol-sectors-buyers-market

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-ethanol-sectors-buyers-market.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99809, Requested 1907. Please try again in 24m42.624s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India built roughly 2,000 crore litres of ethanol distillation capacity to chase the EBP blending mandate — and demand has not caught up." — The claim implies that the 2,000 crore litres of capacity was *built specifically* to meet the EBP mandate, but the article later states that ~400 crore litres of *additional* capacity is due by FY27. This suggests the 2,000 crore litres figure includes pre-existing capacity, not just new builds tied to the mandate. [confidence: high]

- "The funding structure is unusually capital-light for whoever partners with a CSM: NCDC provides 90% of project cost, so a private JV partner or the mill itself needs only 10% equity to fund a conversion." — The claim states that the NCDC loan pool covers 90% of the project cost, but the preceding sentence mentions that the ₹10,000 crore loan pool is funded by ₹1,000 crore in grant-in-aid (₹500 crore across two financial years). This implies the loan pool is not entirely subsidized but partially funded by grants, which may not fully cover 90% of the project cost. The exact proportion of grant vs. loan is unclear, making the "90% of project cost" claim unverifiable. [confidence: medium]

INTERPRETATION ERRORS:
- "EV displacement of two-wheeler petrol demand. A medium-term threat to blending-volume growth as two-wheeler electrification accelerates — ethanol’s non-fuel uses (industrial, pharma, potable) are the partial offset." — The claim suggests that the growth of electric two-wheelers will reduce petrol demand, thereby threatening ethanol blending volumes. However, ethanol blending is tied to *petrol* consumption, not total fuel demand. If EV adoption reduces petrol consumption, ethanol blending volumes could decline *proportionally*, but this does not necessarily mean ethanol demand will fall—it may simply scale with petrol demand. The claim conflates absolute ethanol demand with blending *rates*, which are policy-driven. [confidence: high]

- "Capacity overhang / utilisation risk. The core structural risk: ~700 crore litres of excess supply relative to absorption, concentrated in surplus states." — The claim states that there is a ~700 crore litre excess supply, but earlier in the article, the excess is calculated as ~2,000 crore litres (capacity) minus ~1,100 crore litres (demand) = ~900 crore litres. The ~700 crore litres figure appears to be an underestimate or miscalculation, as it does not align with the previously stated numbers. This inconsistency suggests a double-counting or misinterpretation of the data. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
