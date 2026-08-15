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
- "The Production Linked Incentive Scheme for Food Processing Industries (PLISFPI) carries a ₹10,900 crore outlay" — This claim cannot be verified against a primary source, as the article relies on secondary reporting of government data and the original PIB release could not be accessed [confidence: medium]
- "India's food and agricultural exports have not grown in an unbroken line. In April–October of FY2023-24, the same export category fell 9.32% year-on-year" — The article does not provide a primary source to verify this specific export decline figure [confidence: medium]

INTERPRETATION ERRORS:
- "The scheme that overshot its own target... 3.39 lakh direct and indirect jobs — against the scheme's own 2.5 lakh target for 2026" — The article implies that the PLISFPI scheme's job creation target was only 2.5 lakh, but it does not consider the potential for the target to have been revised or updated over time, which could affect the interpretation of the scheme's success [confidence: medium]
- "India's food-export numbers are exposed to domestic food-security policy as much as to global demand" — The article suggests that domestic food-security policy is a significant factor in food-export numbers, but it does not provide sufficient evidence to support this claim, and the relationship between the two may be more complex than stated [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "3.39L Jobs created under the food-processing PLI scheme, against a 2.5 lakh target" — The article claims 3.39 lakh jobs were created against a 2.5 lakh target, but the table later states "Jobs created (vs. 2.5 lakh target) | 3.39 lakh," which is a direct contradiction. The correct figure should be 3.5 lakh (as per the table), not 3.39 lakh. [confidence: high]

- "₹92,651cr Estimated annual loss from inadequate cold storage and supply-chain gaps" — The article cites this figure as widely cited but admits it could not trace it to a primary NABARD or MoFPI study with a stated methodology. Without verification, this figure cannot be confirmed as accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "Sales of PLI-supported products nearly doubled, from ₹58,758 crore in FY2019-20 to ₹1,08,854 crore in FY2025-26, and export sales from the scheme's beneficiaries have grown at a 13.23% compound annual rate since 2019-20." — While the sales figures are correct, the article implies that the PLI scheme directly caused this growth without providing evidence of a causal link. The growth could be due to other factors like general sector trends, inflation, or other policies. [confidence: high]

- "The structural shift is the more interesting number: processed food's share of India's total agricultural exports has risen from 13.7% to 20.4% over the last decade — the country is exporting less raw commodity and more value-added product than it did ten years ago." — The article correctly notes the increase in processed food's share of exports but does not account for the fact that raw rice exports (a non-processed staple) remain the largest single export category. This omission weakens the claim that the sector is shifting toward value-added products. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
