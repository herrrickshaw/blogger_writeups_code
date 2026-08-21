# Fact/interpretation check — indias-two-tracks-of-health-cover-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-two-tracks-of-health-cover-and.html`

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
- "West Bengal became the last holdout to join [PM-JAY] as of June 2026" — The article later contradicts this by stating West Bengal signed its implementation MoU on **8 June 2026**, implying it joined in mid-2026, not as of June 2026. The phrasing suggests it joined *by* June 2026, which is technically correct but misleadingly implies it was the last holdout *as of* that date (when the MoU was signed). The claim is factually imprecise in its phrasing. [confidence: high]

- "PM-JAY's 43.52 crore cards have been created nationally, with 12.69 crore cumulative hospital admissions authorised as of 30 June 2026" — While the card count and admissions are cited, the **₹1.92 lakh crore in approved claims** is not sourced or verified in the provided text. The article does not cite a primary or secondary source for this figure, making it unverifiable. [confidence: high]

INTERPRETATION ERRORS:
- "PM-JAY's expansion should crowd out private insurance demand — why buy a policy if the government already covers ₹5 lakh of hospitalisation? The research evidence points the other way." — The article cites studies showing PM-JAY enrollment increases private facility visits by 4.6 percentage points, but this **does not prove complementarity with private insurance uptake**. The evidence only shows increased private *facility utilization*, not whether beneficiaries also purchase private insurance policies. The conclusion conflates *healthcare utilization* with *insurance demand*, which are distinct phenomena. [confidence: high]

- "They're not competing for the same household's decision so much as operating on different segments of the same underlying gap — the roughly 43% of India's total health expenditure that NHA 2022-23 still records as out-of-pocket is the space both tracks are separately trying to shrink, from opposite ends of the income distribution." — The article assumes that PM-JAY and private insurance target *different income segments* based on out-of-pocket expenditure data, but **no direct evidence links PM-JAY enrollment or private insurance uptake to income distribution**. The NHA 2022-23 figure describes *aggregate* out-of-pocket spending, not the income-specific distribution of PM-JAY beneficiaries or private policyholders. The reasoning extrapolates beyond the data. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
