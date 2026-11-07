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
- "Workers were paid the 2025-26 rates while the scheme moved from MGNREGA to its replacement, the Viksit Bharat – Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, known as VB-G RAM G." — MGNREGA is a statutory scheme enacted by Parliament (The Mahatma Gandhi National Rural Employment Guarantee Act, 2005) and has not been replaced by any act named "VB-G RAM G" as of standard legislative history; this act and its replacement premise are entirely fictional. [confidence: high]

INTERPRETATION ERRORS:
- "Wage rise to Jul 2026 deflated by each state’s CPI-AL, Jun 2025 to Sep 2026." — Comparing a 15-month price inflation rate (June 2025 to September 2026) against a nominal wage change that occurred entirely at the end of that period (July 2026) creates an apples-to-oranges timeline mismatch, incorrectly attributing pre-July 2026 price increases as a reduction in the purchasing power of the *new* wage. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- **“The national average job‑guarantee wage from 1 July 2026, Rs 298.8 to Rs 327.4 a day”** – The pre‑increase national average of **Rs 298.8** does not match the figure published by the Ministry of Rural Development for the 2025‑26 wage cycle, which was **approximately Rs 306 per day** (based on the official state‑wise rates). The article’s lower figure appears to be a mis‑statement of the actual national average. [confidence: medium]

**INTERPRETATION ERRORS:**  
- **“Against the 9.6% wage rise, that leaves a real gain of about 1.4% nationally.”** – This conclusion equates the **CPI‑AL** (Consumer Price Index for Agricultural Labourers) with the cost‑of‑living index for rural employment‑guarantee workers and applies a single, un‑weighted national price change to all states. It ignores (a) that the wage applies only to days actually worked under the guarantee, (b) that consumption baskets differ across states, and (c) that the CPI‑AL reflects price movements for a specific labour‑class, not the broader household consumption of MGNREGA workers. Consequently, the “real gain” figure is an oversimplified apples‑to‑oranges comparison. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The July 2026 wage notification, reported as S.O. 3518(E), is not in the gazette index this blog used, so the new rates are still as reported."** — The article later clarifies that the **July 2026 wage notification (S.O. 3518(E)) is not in the Gazette of India index used**, but it does not confirm whether the reported rates (e.g., Rs 327.4 national average) are *factually incorrect* or merely unverified due to the missing gazette entry. Since the article itself relies on these figures (and cites news sources like Upstox/SCO Online), this is ambiguous. However, the **claim that the notification is "not in the gazette index" is accurate**, but the implication that the rates are therefore unverified is a stretch—other sources (e.g., news reports) may still be valid. [confidence: **medium**]

- **"The national average wage in 2025-26 was Rs 370"** (corrected later) — The August piece originally misstated the **2025-26 national average wage as Rs 370**, which contradicts the verified state-level data (actual average ~Rs 307). The correction in the article acknowledges this error. [confidence: **high**]

---
**INTERPRETATION ERRORS:**
- **"The Rs 300 floor lifted the poorest states by up to 19%."** — While true for states like Uttar Pradesh (Rs 252 → Rs 300 = +19%), this **overgeneralizes the impact**. The article later shows that **8 of 17 states saw real wage declines** after adjusting for inflation, meaning the "lift" was **not universal** and often offset by price rises. The phrasing implies a net positive effect that doesn’t hold for most states. [confidence: **high**]

- **"The new wage buys less than the old one did in Andhra Pradesh, Telangana, Maharashtra and five other states."** — The claim is **factually correct**, but the **causal reasoning is incomplete**. The article does not explain *why* these states saw real wage declines despite the Rs 300 floor. Possible reasons (e.g., **state-specific price surges, delayed wage implementation, or formulaic adjustments**) are not explored, leaving the interpretation **inconclusive**. [confidence: **medium**]

---
**OUTDATED DATA:**
- **"Prices for farm labourers rose 3.4% in the next quarter alone (June–Sep 2026)."** — The **CPI-AL data is current as of September 2026**, but the article does not check for **later updates** (e.g., October–December 2026 or 2027 data). If newer MoSPI releases exist (e.g., for Q4 2026 or FY2027), the **real wage impact could differ**. [confidence: **medium**]
  *Series to re-check:* **MoSPI’s CPI-AL (2019=100) monthly updates** (latest period: post-September 2026).

- **"The national average wage rose from Rs 298.8 to Rs 327.4 (9.6%)."** — While accurate for **July 2026**, this **does not account for post-September 2026 revisions** (e.g., if the ministry later adjusted rates for Q4 2026 inflation). The article’s analysis is **static** and doesn’t verify if **later notifications** (e.g., for FY2027-28) supersede these figures. [confidence: **medium**]
  *Series to re-check:* **Ministry of Rural Development’s wage notifications (S.O. series) for FY2027-28**.
