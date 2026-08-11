# Fact/interpretation check — fci-storage-scenario-capacity-stock-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fci-storage-scenario-capacity-stock-and.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "FCI is 70% hired , only ~147 LMT owned of FCI's own ~482 LMT capacity" — The article does not provide a source for the 70% hired and 147 LMT owned figures, and the 482 LMT capacity figure is not directly supported by the provided sources [confidence: medium]
- None found for other specific factual errors, but the article's use of approximate figures (e.g., "~907 LMT", "~147 LMT") may indicate a lack of precision in the data [confidence: low]

INTERPRETATION ERRORS:
- "The cooperative plan fixes this at the village level (PACS godowns, 1,000 MT each; 2,000 MT hubs) — turning rented, centralised, over-stretched storage into owned, distributed capacity that doubles as procurement centres, Fair Price Shops and processing units — the feedstock node for the biorefinery" — The article assumes that adding cooperative storage capacity will automatically lead to more efficient and effective storage, procurement, and processing, without providing evidence for this causal link [confidence: high]
- "The scenario story: in mid-2021 stock hit a record ~907 LMT — brushing the covered-godown ceiling and spilling into open CAP/hired space" — The article implies that the record stock level in 2021 was a problem that needed to be solved, but it does not provide evidence that this level of stock was actually a problem, or that the new cooperative plan will prevent similar issues in the future [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India's grain-storage system has grown slowly (851→918 LMT, FCI+State, 2018→2025)" — The claim states the growth from 851 LMT to 918 LMT between 2018 and 2025, but the cited PIB PRID 2172351 (2025) reports 917.83 LMT, which is a growth from 851.54 LMT (2018) to 917.83 LMT (2025). The rounded figure of 918 LMT is correct, but the article incorrectly implies the growth is from 851 to 918 LMT over the period, whereas the actual growth is from 851.54 to 917.83 LMT. [confidence: high]

- "The World's Largest Grain Storage Plan (2023, ₹1 lakh cr) now adds +700 LMT of cooperative (PACS) capacity to lift total agri-storage from 1,450 to 2,150 LMT" — The claim states the plan lifts total agri-storage from 1,450 to 2,150 LMT, but the cited PIB PRID 2080612 (Plan) only mentions adding +700 LMT of cooperative capacity. The base total agri-storage (1,450 LMT) is not explicitly supported by the cited sources in the article. The article does not provide a clear breakdown of how the 1,450 LMT figure is derived or verified. [confidence: medium]

INTERPRETATION ERRORS:
- "The cooperative plan fixes this at the village level (PACS godowns, 1,000 MT each; 2,000 MT hubs) — turning rented, centralised, over-stretched storage into owned, distributed capacity that doubles as procurement centres, Fair Price Shops and processing units — the feedstock node for the biorefinery." — The claim suggests that the cooperative plan will "fix" the storage issue by converting rented, centralized storage into owned, distributed capacity with multiple functions. However, the article does not provide evidence or data to support the causal claim that this transformation will effectively address the storage problem or that the distributed capacity will function seamlessly as procurement centers, Fair Price Shops, and processing units. The reasoning assumes a direct link between storage type and efficiency without empirical or contextual evidence. [confidence: high]

- "Each figure is PIB-sourced (below)." — The claim implies that all figures in the article are sourced from PIB releases, but the article does not explicitly verify or cross-check every figure against the cited PIB PRIDs. For example, the "907 LMT record" is cited as a "chart figure" but is not directly linked to a PIB source in the claim. This creates an interpretation error where the reader assumes all figures are PIB-sourced without clear verification for each claim. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
