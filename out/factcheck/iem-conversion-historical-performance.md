# Fact/interpretation check — iem-conversion-historical-performance

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/iem-conversion-historical-performance.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "The eligibility threshold changed (Rs 50cr → Rs 125cr from Apr 2025) mid-series" — There is no official DPIIT or MSME policy change altering the IEM threshold from Rs 50 crore to Rs 125 crore in April 2025. The MSME investment ceiling for medium enterprises was set at Rs 50 crore in the July 2020 notification, above which undertakings file an IEM. [confidence: high]
- "the partial-year 'Up to Dec 2025' row runs higher" / "2025's own Part A count is undercounted mid-year" — In a calendar-year dataset (January–December), data reported "Up to Dec" covers the entire 12-month period, making it a full calendar year rather than a "partial-year" or "mid-year" count. [confidence: high]

INTERPRETATION ERRORS:
- "the raw implemented value (Rs 4.94L cr) is the highest single year on record, and it happened while the Part A base (Rs 6.02L cr) sat well below 2021's outlier peak (Rs 7.71L cr), meaning most of 2024's Part A filings weren't just filed but built." — This is a false cohort inference that contradicts the author's own caveat. Because IEM Part B implementation is a flow measure with a multi-year gestation lag (typically 2–3 years), Part B implemented in 2024 reflects projects filed in prior years (such as 2021–2023), not the cohort realization of proposals filed in 2024 itself. [confidence: high]
- "This is the year IEM implementation (Rs 4,93,765cr, CY2024 as reconciled in the Dec-2025 Annual Report vintage) overtook FY2024-25 FDI equity inflow (Rs 4,21,929cr) for the first time — domestic industrial capex outpacing foreign investment as a growth engine" — This is an apples-to-oranges comparison. IEM implementation tracks total investment in large-scale manufacturing/industrial units (which can be financed by domestic or foreign capital, leading to double-counting with FDI), whereas FDI equity inflows cover foreign cross-border capital across all sectors (including services, IT, and financial services). Thus, comparing the two figures cannot show that "domestic capex" outpaced foreign investment. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Rs 4,21,929cr" (FDI equity inflow for FY2024-25) — This figure cannot be verified against publicly available data and may require cross-checking with official sources [confidence: medium]
- "Rs 15,18,861cr" (Gujarat 2019 investment) — This figure seems unusually high and may be an error in the source data, but without further information, it's difficult to confirm [confidence: medium]

INTERPRETATION ERRORS:
- "2024 first year IEM implementation > FDI equity inflow" — This comparison may not be entirely accurate since IEM implementation and FDI equity inflow are reported on different calendars (calendar-year vs. fiscal-year), which could lead to an apples-to-oranges comparison [confidence: high]
- "The national conversion-rate story is thus not evenly distributed — it is disproportionately a story about a handful of large industrial states executing faster" — This conclusion may be based on incomplete data, as the article mentions that the eligibility threshold changed in April 2025, which could affect the comparability of year-over-year IEM counts [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 4.94L cr CY2024 implemented — the best year on record" — The article later contradicts this by stating that the "Up to Dec 2025" figure (Rs 5.83L cr) is provisional and likely to be revised upward, implying CY2024 may not be the final "best year on record." Additionally, the Rs 4.94L cr figure is cited as CY2024, but the source material (DPIIT Annual Reports) typically reports fiscal years (e.g., FY2024-25), not calendar years. [confidence: high]

- "2019 Part B EXCLUDED — source defect: AR2022-23 prints Gujarat 2019 at Rs 15,18,861cr (~6x all-India)" — The claim that Gujarat's 2019 Part B investment was printed at Rs 15,18,861 crore (15.19 lakh crore) is implausibly high (e.g., India's total GDP in 2019 was ~Rs 147 lakh crore). This suggests a typographical error in the article (likely a misplaced comma or incorrect unit), as the DPIIT Annual Reports do not report such extreme values. [confidence: high]

INTERPRETATION ERRORS:
- "2024 first year IEM implementation > FDI equity inflow" — The article claims that CY2024 IEM implementation (Rs 4.94L cr) overtook FY2024-25 FDI equity inflow (Rs 4.22L cr), implying domestic industrial capex outpaced foreign investment. However, this compares a **calendar-year** figure (IEM) to a **fiscal-year** figure (FDI), which are not directly comparable due to differing timeframes and reporting conventions. The overlap is not identical, and the comparison conflates two different accounting periods. [confidence: high]

- "The national conversion-rate story is thus not evenly distributed — it is disproportionately a story about a handful of large industrial states executing faster, not a uniform national acceleration." — While the state-level data shows concentration in Gujarat, Odisha, and Maharashtra, the article does not provide evidence that this disproportionality is *not* reflective of a broader national trend. The claim assumes that the remaining states' performance is irrelevant or stagnant without supporting data or analysis. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
