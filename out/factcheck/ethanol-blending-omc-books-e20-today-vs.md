# Fact/interpretation check — ethanol-blending-omc-books-e20-today-vs

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/ethanol-blending-omc-books-e20-today-vs.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99971, Requested 2695. Please try again in 38m23.424s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Domestic petrol 54.05 bn L (40 MMT, PPAC FY24-25)" — The conversion from billion litres to MMT (million metric tonnes) is incorrect. 1 litre of petrol weighs approximately 0.74 kg, so 54.05 billion litres ≈ 40.0 MMT (54.05 * 0.74 ≈ 39.997), which is correct. However, the article states "54.05 bn L (40 MMT)" without clarifying the conversion factor, which could mislead readers unfamiliar with the calculation. [confidence: high]

- "ethanol capacity ~2,000 cr L" — The article later states "Installed capacity is now ~2,000 cr L (CareEdge, ESY 2025-26), with a further ~400 cr L due by FY27." However, the "crore L" unit is ambiguous. In Indian numbering, "crore" = 10 million, so 2,000 crore L = 20 billion litres. This is a reasonable estimate for ethanol capacity, but the article does not explicitly define "cr L," which could confuse international readers. [confidence: medium]

INTERPRETATION ERRORS:
- "The petrol ethanol pushes out of the domestic tank doesn't vanish — India, a net product exporter, ships it." — While India is a net exporter of petroleum products, the claim that *all* displaced petrol is exported is an overgeneralization. The article later quantifies this as "~8 MMT at E20" and "~12 MMT at E30," but it does not account for potential domestic demand fluctuations, inventory changes, or logistical constraints that could prevent full export realization. The causal link between ethanol blending and guaranteed petrol export is not fully supported. [confidence: high]

- "A dedicated state SGST on ethanol recovers a slice for states — a partial, price-neutral recovery (full VAT-parity would need ~27%)." — The article correctly notes that the 5% SGST recovers only a fraction of the foregone VAT (₹5,513 cr vs. ₹23,716 cr foregone). However, it does not explain why "full VAT-parity" would require a 27% SGST. The 27% figure appears arbitrary without a clear derivation (e.g., is it based on the average state VAT rate of ~18% plus central taxes, or another calculation?). The causal claim lacks justification. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
