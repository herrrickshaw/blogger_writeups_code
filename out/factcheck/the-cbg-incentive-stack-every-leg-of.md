# Fact/interpretation check — the-cbg-incentive-stack-every-leg-of

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-cbg-incentive-stack-every-leg-of.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 98870, Requested 2086. Please try again in 13m45.984s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "SATAT procurement price (MoPNG, 20-May-2022 + 15-May-2025 revision): OMCs guarantee CBG offtake at an assured ex-plant price (₹54/kg basis in the model, excl. 5% GST)" — The claim that the SATAT procurement price is ₹54/kg is unverified and likely incorrect. The official SATAT scheme documents do not specify a fixed price of ₹54/kg; pricing is typically determined through competitive bidding or negotiations between OMCs and CBG producers. The 15-May-2025 revision is also not a standard reference for SATAT pricing updates. [confidence: high]

- "CBG Blending Obligation (CBO) (MoPNG, 27-Feb-2024): mandatory blending in CNG(T)/PNG(D) — 1% FY25-26 rising toward 5% by FY28-29" — The blending obligation percentages (1% in FY25-26 rising to 5% by FY28-29) are not explicitly stated in the cited MoPNG circular dated 27-Feb-2024. The circular may outline the framework, but the specific phased targets are not confirmed in the referenced document. [confidence: medium]

INTERPRETATION ERRORS:
- "CBG–CGD Synchronization Scheme (Apr-2021, extended Oct-2023 and Mar-2026): CBG is injected/co-mingled directly into city-gas networks and treated as fungible with natural gas — the plant sells into the grid rather than trucking to a pump." — While the scheme allows CBG injection into CGD networks, the claim that this eliminates the need for trucking to pumps is an overstatement. Even with grid injection, CBG may still require transportation to CGD network entry points, and the logistics of blending and distribution introduce additional costs and complexities not accounted for. The fungibility claim is technically correct, but the implication that trucking is entirely obviated is misleading. [confidence: high]

- "The pattern worth noting: the stack de-risks every leg of the CBG business model — feedstock (BAM/CRM), capex (MNRE/VGF/SASCI), debt (PSL/AIF/AHIDF), gas revenue (SATAT floor + CBO mandated demand + DPI evacuation), digestate revenue (FCO Schedule VIII + bulk sale + MDA), and carbon revenue — and it's all on-budget and ex-plant, the exact contrast with ethanol's hidden consumer-side funding." — The claim that the entire incentive stack is "on-budget and ex-plant" is an apples-to-oranges comparison. While some subsidies (e.g., MNRE, VGF) are explicit budgetary outlays, others (e.g., SATAT pricing floors, blending obligations, tax exemptions, or carbon credits) are indirect or market-based mechanisms that do not represent direct budgetary expenditure. The comparison with ethanol's "hidden consumer-side funding" conflates different types of support mechanisms without adjusting for their economic incidence or visibility. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
