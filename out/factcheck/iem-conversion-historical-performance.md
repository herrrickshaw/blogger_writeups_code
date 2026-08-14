# Fact/interpretation check — iem-conversion-historical-performance

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/iem-conversion-historical-performance.html`

## Gemini gemini-flash-latest

[Gemini network error: The read operation timed out]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "2024 first year IEM implementation > FDI equity inflow" — The article compares calendar-year IEM implementation with fiscal-year FDI equity inflow, which may not be directly comparable due to the difference in reporting periods [confidence: medium]
- "Gujarat alone implemented Rs 4.55L cr across just 2024-2025" — This claim is based on state-level Part B data, but the article does not provide a source for this specific figure, making it difficult to verify [confidence: low]

INTERPRETATION ERRORS:
- "45.1% → 82.0% conversion rate, 2021 low to 2024 high" — The article interprets the increase in conversion rate as a sign of improving government performance, but it also acknowledges that the conversion rate is a same-period flow ratio, not a cohort match, which means that the increase could be due to other factors, such as a pipeline effect [confidence: high]
- "The headline number: is conversion improving? Yes, and sharply" — The article concludes that conversion is improving based on the increase in conversion rate, but it does not account for the fact that the eligibility threshold changed mid-series, which could affect the comparability of the data [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 4.94L cr CY2024 implemented — the best year on record" — The article later contradicts this by stating "Rs 4,93,765cr, CY2024 as reconciled in the Dec-2025 Annual Report vintage," which is Rs 4.93765 lakh crore, not Rs 4.94 lakh crore. The rounding is inconsistent and incorrect. [confidence: high]

- "2019 Part B EXCLUDED — source defect: AR2022-23 prints Gujarat 2019 at Rs 15,18,861cr (~6x all-India)" — The figure Rs 15,18,861 crore is implausibly high for Gujarat's 2019 Part B implementation (likely a typographical error where "15,18,861" should be "15,188.61" or similar). This is a clear data entry error in the source material. [confidence: high]

INTERPRETATION ERRORS:
- "2024 first year IEM implementation > FDI equity inflow" — The article claims that "IEM implementation (Rs 4,93,765cr, CY2024) overtook FY2024-25 FDI equity inflow (Rs 4,21,929cr) for the first time," but compares a calendar-year IEM figure to a fiscal-year FDI figure (FY2024-25). This is an apples-to-oranges comparison because the periods do not align (calendar vs. fiscal year), and the FDI figure may not correspond to the same economic activity. [confidence: high]

- "The national conversion-rate story is thus not evenly distributed — it is disproportionately a story about a handful of large industrial states executing faster, not a uniform national acceleration." — While the state-level data shows concentration in Gujarat, Odisha, and Maharashtra, the article does not provide evidence that this disproportionality is due to "executing faster" rather than other factors like larger project sizes or state-specific incentives. The conclusion assumes causation without addressing potential confounding variables. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
