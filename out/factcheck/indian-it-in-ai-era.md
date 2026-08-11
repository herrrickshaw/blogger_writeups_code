# Fact/interpretation check — indian-it-in-ai-era

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indian-it-in-ai-era.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99406, Requested 4951. Please try again in 1h2m44.448s. Need more tokens? Upgrade to Dev Tier today at htt]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites the Reserve Bank of India (RBI) data showing net services receipts at $216.6bn in FY2025-26, but the RBI's "Developments in India's Balance of Payments, Q4 2025-26" report (the cited source) does not show this figure. The table in the article shows net services receipts as $188.8bn in FY2024-25 and $216.6bn in FY2025-26, but the $27.8bn increase is not explicitly stated in the RBI report. The increase is implied by the difference between the two years, but the article presents it as a direct claim without clear RBI confirmation. [confidence: medium]

- "The Economic Survey's own uncomfortable framing" section quotes the 2025-26 Survey as saying services exports are “not a substitute for the goods-based export ecosystems that ultimately underpin durable external and currency stability.” — The Economic Survey 2025-26 does not contain this exact phrasing. The article appears to paraphrase or misattribute a claim from the Survey, which does discuss the role of services exports but not in these specific terms. [confidence: high]

INTERPRETATION ERRORS:
- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — While the numbers are factually correct (64% and 107% based on the RBI data), the interpretation that this means services exports are "covering" the goods deficit in a sustainable way is misleading. The article implies that this coverage is a positive sign for India's external account, but it does not address the structural risks: the goods deficit is widening ($50 billion increase in FY2026 alone), and the coverage by services and remittances is dependent on volatile factors like remittances (which are tied to global migration patterns) and services exports (which are increasingly subject to AI-driven price deflation). The conclusion that this is a "macro-stabilising" factor is an overreach given these risks. [confidence: high]

- "A sector that is 1% of jobs but ~8% of GDP and covers two-thirds of the goods trade deficit cannot produce a mass-unemployment event. It can produce a balance-of-payments event." — While the sector's share of jobs (~1.1%) and GDP (~8%) is correct, the causal claim that an AI shock to services exports would "show up in the rupee long before it showed up in the jobs data" is an overinterpretation. The article conflates the sector's macroeconomic importance with the timing of impacts. A balance-of-payments event (e.g., currency depreciation) could occur due to multiple factors, not solely AI-driven services export shocks. The claim assumes a direct and immediate link between services export performance and currency movements, which is not necessarily supported by the data. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
