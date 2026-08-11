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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99676, Requested 5418. Please try again in 1h13m21.216s. Need more tokens? Upgrade to Dev Tier today at ht]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites the Reserve Bank of India (RBI) data showing net services receipts at $216.6bn in FY2025-26, but the RBI's "Developments in India's Balance of Payments, Q4 2025-26" report (the cited source) does not show this figure. The table in the article shows net services receipts as $216.6bn for FY2025-26, but the RBI data in the table lists $216.6bn for FY2025-26 and $188.8bn for FY2024-25, implying a $27.8bn increase. However, the RBI table's figures are rounded, and the actual increase is closer to $27.8bn only if the unrounded figures are used. The article does not clarify this rounding, making the claim potentially misleading. [confidence: high]

- "The Economic Survey's own uncomfortable framing" section quotes the 2025-26 Survey as saying services exports are “not a substitute for the goods-based export ecosystems that ultimately underpin durable external and currency stability.” — The article does not provide a direct quote or citation from the Economic Survey 2025-26 to support this claim. While the Economic Survey may contain such language, the article does not reference a specific page, paragraph, or section, making the claim unverifiable as presented. [confidence: medium]

---

INTERPRETATION ERRORS:
- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — The article correctly states the ratios but implies that the services surplus and remittances are the primary reasons India's current account deficit is small (0.6% of GDP). However, the current account deficit is primarily driven by the primary income deficit (investment income paid out, $48.2bn), which is not offset by services or remittances. The article does not explicitly state this, creating a misleading impression that services and remittances are the sole or main reasons for the small CAD. The reasoning gap is that the article does not clarify that the CAD is small *despite* the primary income deficit, not because of the services surplus. [confidence: high]

- "A sector that is 1% of jobs but ~8% of GDP and covers two-thirds of the goods trade deficit cannot produce a mass-unemployment event. It can produce a balance-of-payments event." — The article correctly notes the asymmetry between employment share and economic contribution but incorrectly implies that a balance-of-payments event (currency adjustment) is the *only* possible outcome of an AI shock to IT services. The reasoning gap is that the article does not consider other potential outcomes, such as sectoral restructuring, skill mismatches, or broader economic disruptions, which could still lead to job losses or other economic challenges even if the balance of payments remains stable. The claim oversimplifies the causal chain by assuming a direct and exclusive link between balance-of-payments effects and employment outcomes. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
