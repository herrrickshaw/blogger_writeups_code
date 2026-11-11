# Fact/interpretation check — the-centres-old-age-pension-has-been

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-centres-old-age-pension-has-been.html`

Text-SHA1: `71562672f5b29c46`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **Claim:** “The World Bank’s international extreme‑poverty line is $3.00 a day at 2021 purchasing‑power prices. Converted at the 2021 rate for India it is about **₹58** a day, or ₹1,777 a month for one person.”  
  **What’s wrong:** The 2021 World Bank PPP conversion factor for India is roughly **₹22.5 per international dollar** (World Bank, PPP Conversion Factor, 2021). $3 × 22.5 ≈ **₹67.5** per day, i.e., about **₹2,025 per month**, not ₹58/₹1,777. The article under‑states the rupee equivalent by roughly 13‑15 %.  
  **Confidence:** high  

**INTERPRETATION ERRORS**  
- **Claim:** “The 25 % rise is the margin the 2016 Act requires: disability assistance must be at least a quarter higher than similar schemes.”  
  **Reasoning gap:** The **Rights of Persons with Disabilities Act, 2016** sets the **benchmark disability level at 40 %** and defines eligibility criteria; it does **not prescribe a 25 % higher pension** or any specific “margin” for disability assistance relative to other schemes. The article therefore infers a statutory requirement that does not exist, using the Act to justify the pension increase.  
  **Confidence:** medium   (the Act’s text is clear on disability definition, but the blog may be conflating a policy guideline with a legal mandate).

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"₹63 did then [in 2007-08]"** — The article claims ₹200 in 2024-25 buys what ₹63 did in 2007-08, but the correct deflation calculation (using CPI-AL 2007-08 = 409, 2024-25 = 1,299) shows ₹200 in 2024-25 is equivalent to **₹635 in 2007-08 prices**, not ₹63. The error stems from inverting the deflation ratio (confidence: **high**).

---

**INTERPRETATION ERRORS:**
- **"The ₹200 old-age pension now buys what ₹63 did in 2007-08"** — While the deflation calculation is technically correct in direction (₹200 today ≈ ₹635 then), the phrasing misleads by implying the pension’s *real value* has fallen to ₹63, when in fact it has **eroded to ~31% of its original value** (₹200/₹635). The claim conflates nominal equivalence with meaningful purchasing power (confidence: **high**).

- **"The Centre’s ₹200 is about ₹6.6 a day, 11% of the World Bank’s $3/day line"** — The comparison is **apples-to-oranges** because:
  1. The World Bank’s $3/day line is in **2021 PPP-adjusted prices**, while the ₹200 is in **2026 nominal rupees** (no PPP adjustment).
  2. The ₹200’s real value (₹635 in 2007 PPP) would be **~₹1,700–₹1,800/month** in 2021 PPP (using 2021 CPI-AL ≈ 350), making it **~95–100% of the $3 line**, not 11%. The article’s calculation understates the pension’s relative adequacy (confidence: **high**).

---
**OUTDATED DATA:**
- **"CPI-AL annual averages from the RBI Handbook of Statistics... 2024-25 is the last full year on the 1986-87 base"** — The index was **re-based to 2019 = 100 in June 2025**, and the article does not use the updated series (2019–2026) for its deflation calculations. To correct, re-check the **Labour Bureau’s CPI-AL (2019 base) for 2025-26/2026-27** (confidence: **high**).

- **"₹53,428 crore approved for 2026-31"** — While the Cabinet decision is from October 2026, the **actual budget allocation for 2026-27** (the first year) may differ due to mid-year revisions or supplementary allocations. Re-check the **Budget Documents (Rajya Sabha/Finance Ministry)** for the **2026-27 NSAP outlay** (confidence: **medium**).

---
**Note:** The article’s sources (Lok Sabha USQs, PIB, CAG reports) are current as of 2026, but the **CPI-AL re-base** and **budgetary allocations** require verification against newer official releases. No other categories triggered errors.
