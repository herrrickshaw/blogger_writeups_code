# Fact/interpretation check — indias-8-digit-trade-book-searchable

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-8-digit-trade-book-searchable.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Trade value on codes absent nine years earlier" — The article claims that 31.8% of FY2025-26 export value and ~39% of import value sits on codes that did not exist in FY2017-18. However, the article later states these figures are from an "independent audit of this dataset carried out for this blog," not directly from DGCI&S TradeStat EIDB. Without a primary source citation, these percentages cannot be verified as factual. [confidence: medium]

- "The export series has no FY2021-22" — The article states the export series lacks data for FY2021-22, but this is not confirmed by the DGCI&S TradeStat EIDB portal or any cited primary source. The claim appears to be an assumption made by the authors. [confidence: medium]

INTERPRETATION ERRORS:
- "Renumbering, not trade collapse: HS8 codes churn by a third; HS4 headings barely move." — The article uses the high percentage of trade value on new HS8 codes (31.8% exports, ~39% imports) to argue that "renumbering" (not trade collapse) explains the churn. However, this interpretation conflates *nomenclature changes* with *actual trade dynamics*. The presence of new codes does not inherently disprove a trade collapse in older codes; it merely indicates reclassification. The article does not provide evidence that the "missing" trade value in older codes is offset by equivalent growth in new codes (e.g., via product splitting or merging). [confidence: high]

- "Aggregating 8-digit codes up to the 4-digit HS heading removes almost all the churn" — The article claims that churn falls to "under one per cent" at the 4-digit HS level, implying that HS4 headings are stable over time. However, this interpretation assumes that aggregation inherently resolves classification issues, which may not be true. HS4 headings can also undergo revisions (e.g., splits, merges, or redefinitions), and the article does not verify whether the "under one per cent" churn accounts for such changes. The claim risks overgeneralizing the stability of HS4 headings without addressing potential limitations in the aggregation method. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
