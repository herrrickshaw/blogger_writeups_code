# Fact/interpretation check — real-gdp-growth-india-fy2012-13-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/real-gdp-growth-india-fy2012-13-to.html`

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
- "FY2025-26 now has a Provisional Estimate (released 29 May 2026: real GDP growth of 7.7%, up from the First Advance Estimate)" — The date "29 May 2026" is in the future relative to the article's retrieval date of 18 Jul 2026, which is impossible. The claim is unverifiable as written. [confidence: high]

- "FY2020-21's First Advance Estimate was -8%" — The First Advance Estimate for FY2020-21 was actually -7.3%, not -8%. The claim is incorrect. [confidence: high]

INTERPRETATION ERRORS:
- "FY2023-24 saw the largest upward revision: from a 7% First Advance Estimate to 9% by the First Revised Estimate — tied with the COVID year's revision in size (both 2 percentage points)" — While the revision size is correctly noted (2 percentage points), the claim that it is "tied with the COVID year's revision" is misleading. The COVID year (FY2020-21) had a revision from -8% to -6% (2 percentage points), but this was a *reduction in contraction*, not an expansion. The FY2023-24 revision was an *increase in growth*. The comparison conflates different types of revisions (shrinking contraction vs. enlarging expansion), making the tie claim invalid. [confidence: high]

- "The distance between tick and bar is that year's revision so far, not a forecast error against some final truth: even 'Final Estimates' can predate a later methodology change." — While the first part is correct, the second part ("even 'Final Estimates' can predate a later methodology change") is an overgeneralization. MoSPI's "Final Estimates" are typically the most comprehensive and are not subject to further revisions unless a methodology change occurs *after* their release. The phrasing suggests that "Final Estimates" are inherently unreliable, which is not supported by standard statistical practices. This misrepresents the reliability of final data. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
