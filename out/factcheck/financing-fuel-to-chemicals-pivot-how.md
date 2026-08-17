# Fact/interpretation check — financing-fuel-to-chemicals-pivot-how

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/financing-fuel-to-chemicals-pivot-how.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "India's own petrochemical intensity — the share of crude actually converted into chemicals rather than fuel — has room to grow from roughly 13% today toward a 15% national target by 2030" — India's national petrochemical intensity is currently around 4–5%, not 13% (global averages are ~10–15%). This claim also directly contradicts data presented later in the same article stating that PSU refiners' intensity is ~4.1% and IOCL's is ~6.5%. [confidence: high]
- "₹15,000 crore of debt, roughly 30% of it — $500 million to $1 billion — sourced from foreign currency loans and bonds" — 30% of ₹15,000 crore is ₹4,500 crore (equivalent to roughly $530–540 million at current exchange rates). Stating an upper range of $1 billion (approx. ₹8,300+ crore) would represent over 55% of the total raise, making the stated math and proportions contradictory. [confidence: high]

INTERPRETATION ERRORS:
- "...several of the world's largest, most liquid lending currencies (yen, Swiss franc, euro) still sit meaningfully below India's own policy rate, so a dollar or yen-denominated loan, even after hedging costs eat into the naked rate gap, can land cheaper than an equivalent domestic-currency raise..." — This assumes that low foreign nominal interest rates inherently provide a net borrowing cost advantage over domestic debt. Under covered interest parity, standard currency hedging costs (forward premia/cross-currency swap spreads) generally offset the interest rate differential between the foreign currency and INR, leaving no structural cost advantage unless the borrower takes on unhedged foreign exchange risk. [confidence: high]
- "Financing the Fuel-to-Chemicals Pivot: How Indian Oil's ₹15,000 Crore Debt Raise Fits a Much Bigger Pattern" — The article attributes a general corporate borrowing program (₹15,000 crore debt raised to support a broader ₹35,000 crore annual capex budget spanning routine maintenance, refinery expansions, and operations) directly to the "fuel-to-chemicals pivot," treating general balance-sheet funding as if it were earmarked petrochemical project finance. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India's stated national target is to lift refining capacity from roughly 258 MMTPA today to 450 MMTPA by 2030" — This claim cannot be verified against publicly available information, and the article does not provide a direct source for this specific target [confidence: medium]
- None found for other factual errors

INTERPRETATION ERRORS:
- "IndianOil's finance director explicitly linked the 30% foreign-currency share to 'interest rate trends' — and the rate backdrop already mapped in this site's green-debt piece explains why" — The article assumes that the interest rate trends are the primary reason for the foreign-currency share, but it does not consider other potential factors that might influence this decision, such as currency risk, hedging costs, or lender preferences [confidence: medium]
- None found for other interpretation errors

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "14 August 2026" — The article is dated in the future (2026), which is impossible as the current date is 2023. This is likely a typographical error or misconfiguration. [confidence: high]

- "₹35,000 crore annual capex programme" (mentioned in the first paragraph) — While Indian Oil Corporation (IOCL) has disclosed large capex plans, there is no verifiable public source confirming a specific ₹35,000 crore *annual* capex figure for IOCL in recent disclosures. The article cites IOCL's finance director but does not provide a direct quote or official document linking this exact number to an annual program. [confidence: medium]

INTERPRETATION ERRORS:
- "IndianOil's finance director described the raise as split roughly 70/30 between domestic bonds and foreign currency loans or bonds, with the foreign leg sized at $500 million to $1 billion depending on prevailing interest rates..." — The article implies that the ₹15,000 crore debt raise is directly tied to funding the petrochemical pivot, but IOCL has not explicitly earmarked this tranche for petrochemicals. The financing is framed as part of a broader ₹35,000 crore capex program, which includes refinery expansions and other projects. There is no project-level breakdown confirming that the ₹15,000 crore is allocated specifically to petrochemicals. This conflates general capex with targeted petrochemical funding. [confidence: high]

- "The RBI's February 2026 liberalisation of the External Commercial Borrowings framework raised the automatic-route ceiling to the higher of $1 billion outstanding or 300% of net worth..." — The article uses a future date ("February 2026") for an RBI policy change, which is factually incorrect (as noted above). Even if the date were corrected, the claim that the ECB liberalization "explains why" the foreign-currency leg of IOCL’s debt makes sense is an overreach. While the policy change may have expanded access to foreign borrowing, the article does not provide evidence that IOCL’s specific 30% foreign-currency borrowing decision was influenced by this policy or that the timing of the raise was driven by it. The causal link is speculative. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
