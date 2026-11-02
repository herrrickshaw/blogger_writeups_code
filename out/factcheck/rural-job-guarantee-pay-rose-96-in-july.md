# Fact/interpretation check — rural-job-guarantee-pay-rose-96-in-july

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/rural-job-guarantee-pay-rose-96-in-july.html`

Text-SHA1: `d9d286f7f8f7bcc6`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Workers were paid the 2025-26 rates while the scheme moved from MGNREGA to its replacement, the Viksit Bharat – Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, known as VB-G RAM G." — MGNREGA has not been replaced by a law named "Viksit Bharat – Guarantee for Rozgar and Ajeevika Mission (Gramin) Act (VB-G RAM G)" as of any known legislative enactment; this legislation is entirely fictitious. [confidence: high]

INTERPRETATION ERRORS:
- "The index rose from 140.06 in June 2026 to 144.82 in September, 3.4% in three months... Over the whole stretch from June 2025... prices for agricultural labourers rose 8.0%. Against the 9.6% wage rise, that leaves a real gain of about 1.4% nationally" — Comparing a discrete percentage wage hike against an accumulated point-to-point price inflation rate over a different timeframe to determine a net "real gain" creates a mathematical mismatch and misrepresents purchasing power dynamics over the period. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “Andhra Pradesh | 2025‑26 wage 307 → 312 | +1.6 % | Farm‑labour prices +11.8 % | Real change ‑9.1 %” — The real change should be the wage growth minus the price growth (1.6 % − 11.8 % = ‑10.2 %). The article’s figure of ‑9.1 % is mathematically incorrect. [confidence: high]  
- “Telangana | 2025‑26 wage 307 → 308 | +0.3 % | Farm‑labour prices +9.7 % | Real change ‑8.5 %” — Using the same calculation, the real change should be ‑9.4 % (0.3 % − 9.7 %). The reported ‑8.5 % is therefore inaccurate. [confidence: high]  

**INTERPRETATION ERRORS**  
- “The price comparison uses each state’s overall CPI‑AL; it does not account for the extra 25 days of work the new law guarantees, which raises what a household can earn without changing the daily rate.” — By judging whether the new wage “buys less” solely on CPI‑AL, the article implicitly assumes that real‑wage welfare is determined only by daily‑rate purchasing power. Ignoring the additional guaranteed work days (the “extra 25 days”) means the analysis under‑estimates total earnings, so the conclusion that workers in those states are worse‑off is not supported by the data presented. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The new wage buys less than the old one did" in Andhra Pradesh, Telangana, Maharashtra, Tamil Nadu, Haryana, Karnataka, Punjab, and Gujarat** — The article states this as a fact based on CPI-AL inflation data, but the **2025-26 wage rates for these states were already above the Rs 300 floor** (e.g., Andhra Pradesh: Rs 307 → Rs 312; Telangana: Rs 307 → Rs 308). The **real wage decline is mathematically correct**, but the phrasing implies the floor itself caused the loss, which is misleading because the floor only applied to states below Rs 300 (e.g., Uttar Pradesh, Bihar). The error lies in conflating the floor’s intent with the states where it didn’t apply. [confidence: high]

---

**INTERPRETATION ERRORS:**
- **"The Rs 300 floor lifted the poorest states by up to 19%"** — While true for states like Uttar Pradesh (Rs 252 → Rs 300, +19%), the claim **fails to distinguish between nominal and real gains**. The article later shows that **even in these states, inflation (e.g., +7.4% in Uttar Pradesh) eroded much of the nominal rise**, leaving real gains of only +10.9%. The initial framing overstates the floor’s *effective* impact. [confidence: high]

- **"Prices for farm labourers rose 3.4% in the next quarter alone"** — This is correct, but the article **does not clarify whether this 3.4% is all-India or state-specific**. The real wage losses in states like Andhra Pradesh (-9.1%) are driven by **state-level CPI-AL inflation (e.g., +11.8%)**, not the national average. Using the national price rise to generalize understates the divergence across states. [confidence: high]

---
**OUTDATED DATA:**
- **None found** — All data (CPI-AL, wage notifications) are either:
  1. **Officially verified** (e.g., Gazette of India for 2025-26 rates, MoSPI for CPI-AL),
  2. **Explicitly labeled as of September 2026** (e.g., "latest" CPI-AL figures), or
  3. **Acknowledged as provisional** (e.g., S.O. 3518(E) not in the Gazette index but reported by multiple sources). No figures appear stale.
