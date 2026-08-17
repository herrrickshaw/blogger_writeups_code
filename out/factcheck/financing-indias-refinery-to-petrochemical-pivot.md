# Fact/interpretation check — financing-indias-refinery-to-petrochemical-pivot

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/financing-indias-refinery-to-petrochemical-pivot.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "roughly 30% of it — $500 million to $1 billion — sourced from foreign currency loans and bonds" — 30% of ₹15,000 crore is ₹4,500 crore. At current USD/INR exchange rates (~₹83–85/USD), ₹4,500 crore equals approximately $530–540 million; $1 billion would represent over ₹8,300 crore (more than 55% of the total raise), making the "$500 million to $1 billion" range mathematically inconsistent with the stated 30% share. [confidence: high]
- "lift refining capacity from roughly 258 MMTPA today to 450 MMTPA by 2030 — more than 75% growth" — An increase from 258 MMTPA to 450 MMTPA represents an increase of 192 MMTPA, which is 74.42% growth, not "more than 75%". [confidence: high]
- "The RBI's February 2026 liberalisation of the External Commercial Borrowings framework raised the automatic-route ceiling to the higher of $1 billion outstanding or 300% of net worth, and removed the all-in-cost ceiling entirely, leaving only a market-conforming-cost requirement" — Under the RBI's Master Direction on External Commercial Borrowings (ECB), the automatic route limit is $750 million (or equivalent) per financial year, and all-in-cost ceilings (benchmark rate plus a prescribed spread) remain mandatory regulatory parameters rather than entirely eliminated. [confidence: high]

INTERPRETATION ERRORS:
- "several of the world's largest, most liquid lending currencies (yen, Swiss franc, euro) still sit meaningfully below India's own policy rate, so a dollar or yen-denominated loan, even after hedging costs eat into the naked rate gap, can land cheaper than an equivalent domestic-currency raise" — The text conflates US dollar interest rates with low-yielding currencies like the Japanese Yen and Swiss Franc, treating dollar borrowing as having a wide naked policy rate discount relative to India. Furthermore, under standard Covered Interest Parity (CIP), fully hedging currency and interest rate risk eliminates the naked interest rate differential between foreign and domestic borrowing costs; foreign currency borrowing does not automatically generate cheaper landed borrowing costs once fully hedged. [confidence: medium]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India's stated national target is to lift refining capacity from roughly 258 MMTPA today to 450 MMTPA by 2030" — This claim cannot be verified against available data, and the source of this specific target is not clearly cited in the article, although it mentions "Construction World, DD News, Business Standard coverage of Minister Hardeep Singh Puri's remarks" as sources for national refining-capacity and petrochemical-intensity targets. [confidence: medium]
- None found for other factual errors.

INTERPRETATION ERRORS:
- "IndianOil's finance director explicitly linked the 30% foreign-currency share to 'interest rate trends' — and the rate backdrop already mapped in this site's green-debt piece explains why" — This explanation assumes that interest rate trends alone justify the 30% foreign-currency share without considering other potential factors such as risk management, currency hedging strategies, or specific project requirements that might influence the decision. [confidence: medium]
- None found for other interpretation errors.

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "14 August 2026" — The date is in the future relative to the current date (June 2025), making it unverifiable and likely incorrect. [confidence: high]

- "₹1 trillion over 5–6 years" (for IndianOil's petrochemical programme) — The article cites this as part of IndianOil's ₹1 trillion commitment, but the table later lists the Panipat, Gujarat, and Barauni expansions separately (₹32,946cr + ~₹19,000cr + unspecified for Barauni), which already exceed ₹50,000cr. The ₹1 trillion figure appears to double-count or conflate multiple projects without clear justification. [confidence: high]

INTERPRETATION ERRORS:
- "petrochemical feedstock competes with road-fuel demand for the same barrel of crude, and India's own petrochemical intensity — the share of crude actually converted into chemicals rather than fuel — has room to grow from roughly 13% today toward a 15% national target by 2030" — The claim implies a direct causal link between increasing petrochemical intensity and reducing import dependence for plastics/polymers, but it does not establish whether the projected 15% petrochemical intensity is sufficient to meet domestic demand or whether other factors (e.g., feedstock availability, technology, or global market conditions) could undermine this goal. [confidence: medium]

- "the RBI's February 2026 liberalisation of the External Commercial Borrowings framework raised the automatic-route ceiling to the higher of $1 billion outstanding or 300% of net worth" — The article attributes this policy change to February 2026, but the claim does not explain how this specific liberalization directly benefits Indian refiners' foreign-currency borrowing costs or why the widened ECB ceiling is uniquely advantageous for petrochemical financing (as opposed to other uses). The reasoning conflates policy availability with targeted financial benefit. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
