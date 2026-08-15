# Fact/interpretation check — if-india-paid-brics-in-rupees-scenario

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/if-india-paid-brics-in-rupees-scenario.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "The chronology settles it: the RBI only permitted surplus vostro balances to be invested in government securities in August 2025..." — This is factually incorrect. The Reserve Bank of India explicitly permitted foreign banks to invest surplus Special Rupee Vostro Account (SRVA) balances in Government Securities and Treasury Bills when it introduced the rupee trade settlement framework on July 11, 2022 (vide A.P. (DIR Series) Circular No. 10, paragraph 3(d)), not in August 2025. [confidence: high]

INTERPRETATION ERRORS:
- "India's merchandise imports of $775 billion spread over roughly 250 trading days is about $3.1 billion a day of dollar demand. Global USD/INR turnover was around $185 billion a day in the BIS Triennial Survey... So India's entire import-related dollar demand is about 1.7% of daily USD/INR turnover. Removing all BRICS imports from the dollar — the maximalist S3 — would remove roughly 0.70% of daily turnover." — This is an apples-to-oranges comparison. Gross foreign exchange turnover in the BIS survey includes interbank trades, swaps, forward rollovers, and speculative churn, where a single real transaction is multiplied across dealers. Comparing net real underlying trade demand directly against gross dealer turnover creates a misleading ratio that trivialises the macro impact of fundamental trade flows on currency pressure. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Saudi Arabia's BRICS membership status is formally ambiguous — invited in 2023, listed by BRICS chairs, never unambiguously confirmed by Riyadh" — The article does not provide a verifiable source for Saudi Arabia's BRICS membership status, and the claim of ambiguity may not be accurate [confidence: medium]
- "The RBI's own Inter-Departmental Group put dollar invoicing at about 86% of both India's exports and imports" — The article cites the RBI Inter-Departmental Group on Internationalisation of the INR, July 2023, but does not provide a direct quote or a verifiable source to confirm this specific figure [confidence: medium]

INTERPRETATION ERRORS:
- "The prize is real but the usable share is a quarter of it. BRICS supplies 41.5% of India's imports ($321.8bn), but only $93.4bn can be settled in local currency on a self-financing basis" — The article concludes that only $93.4bn can be settled in local currency, but this interpretation assumes that the self-financing portion is the only viable option, ignoring potential alternatives for settling the remaining $228.5bn [confidence: high]
- "The exchange-rate benefit is small. Even total success removes about 0.70% of daily USD/INR turnover, and it does not shrink the current account deficit at all" — The article interprets the removal of 0.70% of daily USD/INR turnover as a small benefit, but this conclusion may underestimate the potential impact of reducing dollar demand on the rupee's exchange rate and the overall economy [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "The Reserve Bank proposed, in January 2026, linking BRICS central bank digital currencies to make exactly this cheaper." — The RBI's proposal to link BRICS central bank digital currencies was made in **January 2026**, but the article later cites the RBI's proposal as being on the **2026 summit agenda**, which is inconsistent with the January timing. The claim implies the proposal was made in January, but the summit agenda reference suggests it was proposed earlier or is pending. [confidence: high]

- "Saudi Arabia's BRICS membership status is formally ambiguous — invited in 2023, listed by BRICS chairs, never unambiguously confirmed by Riyadh — but it is included here because the trade relationship is what matters to the model." — The article claims Saudi Arabia was invited to BRICS in **2023**, but BRICS officially announced the expansion including Saudi Arabia, Iran, Ethiopia, Egypt, and UAE in **August 2023**, with membership effective from January 2024. The 2023 invitation is correct, but the phrasing implies ambiguity persists, which is misleading as membership was confirmed by early 2024. [confidence: high]

---

INTERPRETATION ERRORS:
- "Local-currency settlement of a trade deficit is not de-dollarisation. It is vendor financing, and someone has to agree to extend it." — The article correctly identifies that settling a trade deficit in local currency does not reduce dollar demand but instead creates a capital inflow (rupee claims). However, it frames this as a failure of de-dollarization, implying that any local-currency settlement of deficits is inherently unsustainable or undesirable. This overlooks that **partial de-dollarization** (e.g., Scenario S2) can still reduce dollar exposure in balanced trade flows, even if deficits require financing. The interpretation conflates **full de-dollarization** (impossible without balanced trade) with **partial de-dollarization** (achievable and beneficial). [confidence: high]

- "The exchange-rate benefit is small. Even total success removes about 0.70% of daily USD/INR turnover, and it does not shrink the current account deficit at all." — The article correctly notes that local-currency settlement does not reduce the current account deficit, but it understates the **potential exchange-rate benefits** by focusing solely on turnover reduction. While the immediate impact on the rupee's level may be small, the **volatility reduction** from lower forced conversions and smaller RBI intervention could indirectly stabilize the exchange rate over time. The interpretation treats the absence of a direct level effect as proof of no benefit, ignoring secondary stabilization effects. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
