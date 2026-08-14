# Fact/interpretation check — indias-food-processing-story-pli-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-food-processing-story-pli-scheme.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The claim is presented as a fact, but the article itself notes that the figures are compiled from secondary reporting of government data and the primary document could not be accessed, which may raise questions about the accuracy of the figure [confidence: medium].
- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article could not trace this figure to a single primary NABARD or MoFPI study with a stated methodology, which may indicate that the figure is not verifiable [confidence: medium].

INTERPRETATION ERRORS:
- "The scheme that overshot its own target ... generated 3.39 lakh direct and indirect jobs — against the scheme's own 2.5 lakh target for 2026" — The article implies that the scheme's success in creating jobs is a direct result of its implementation, but it does not provide a clear causal link between the scheme and the job creation, nor does it account for other factors that may have contributed to the job growth [confidence: high].
- "India's food-export numbers are exposed to domestic food-security policy as much as to global demand" — The article suggests that domestic food-security policy is a significant factor in India's food-export numbers, but it does not provide sufficient evidence to support this claim, and the example provided (the wheat export ban) may not be representative of the broader trend [confidence: medium].

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The article claims 3.39 lakh jobs were created, but the exhibit table lists "Jobs created (vs. 2.5 lakh target)" as 3.39 lakh. The "L" notation is inconsistent with the rest of the article's use of "lakh" (e.g., "2.5 lakh target"). This is likely a typographical inconsistency rather than a factual error, but it could cause confusion. [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but does not provide a primary source or methodology. Without verification from a NABARD or MoFPI study, this claim cannot be confirmed as accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "Sales of PLI-supported products nearly doubled, from ₹58,758 crore in FY2019-20 to ₹1,08,854 crore in FY2025-26, and export sales from the scheme's beneficiaries have grown at a 13.23% compound annual rate since 2019-20." — While the sales figures are correct, the article implies that the PLI scheme directly caused this growth without providing evidence of a causal link. The growth could be due to other factors such as general industry trends, inflation, or other policies. [confidence: high]

- "Under PMKSY, 399 cold-chain projects have been approved to date. Against a stated annual loss of ₹92,651 crore and a 3.5-million-tonne capacity gap, a single year's PMKSY allocation of ₹915 crore is not sized to close it — it is sized to keep adding to it more slowly than the sector is growing around it." — The article correctly notes the scale of the cold-chain gap but incorrectly implies that the ₹915 crore allocation is insufficient to make progress. The allocation may be part of a multi-year plan, and the article does not provide evidence that the gap is growing faster than the allocation can address. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
