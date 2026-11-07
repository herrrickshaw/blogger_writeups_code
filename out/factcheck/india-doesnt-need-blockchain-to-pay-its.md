# Fact/interpretation check — india-doesnt-need-blockchain-to-pay-its

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-doesnt-need-blockchain-to-pay-its.html`

Text-SHA1: `8263270b239db466`

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
- **“The minimum price at which they may sell sugar has been held at ₹31 a kilo since February 2019.”** – The sugar industry’s Minimum Selling Price (MSP) is revised annually by the Ministry of Food Processing Industries and the Government of India; it has not been fixed at ₹31 /kg since 2019. [confidence: high]  

- **“The Sugarcane (Control) Order, 1966 requires mills to pay within 14 days of delivery, and states enforce it.”** – The 14‑day payment provision was introduced by an amendment to the Sugarcane (Control) Order in 2018, not in the original 1966 order. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“The one place where several parties genuinely share a record they do not trust each other to keep, land records, is where an Indian state is now testing a blockchain.”** – This statement treats land‑record reconciliation as the *only* multi‑party domain lacking trusted shared data. In reality, other domains such as e‑NAM auction bids, crop‑insurance claim data, and inter‑state market transactions also involve multiple distrustful parties and could benefit from tamper‑evident records. The claim therefore overstates the uniqueness of the land‑record use‑case. [confidence: medium]  

- **“An escrow would have made those payments certain only if the mills had the money to lock up first.”** – The article presents escrow as a solution to late cane payments, implying that the escrow mechanism would resolve the payment‑delay problem. However, the core issue is mills’ cash‑flow constraints; without external financing (e.g., bank guarantees), an escrow does not guarantee payment. Thus the causal link between escrow implementation and resolution of arrears is overstated. [confidence: medium]  

**OUTDATED DATA**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"₹417 cr recovered from ineligible PM-KISAN beneficiaries by December 2025"** — The article later clarifies that the government only publishes this figure (₹416.75 cr) but does not disclose the **total amount paid to ineligible beneficiaries**, which is critical for calculating recovery rates. The claim stands as a partial fact but omits a key context. [confidence: high]
- **"₹12,779 cr of 2025-26 cane dues still unpaid by mills on 20 April 2026"** — The article notes this figure comes from a **parliamentary standing committee report** (February 2026) and a **PIB update (April 2026)**, but the **August 2026 USDA FAS figure (₹3,382 cr remaining)** suggests significant clearing occurred post-April. The claim is accurate for the stated date but may mislead readers into assuming the arrears persisted unchanged. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- **"A ledger records those decisions [on eligibility]; it does not make them"** — While true, this framing **overstates the ledger’s role** in preventing fraud. The article later admits the prototype relies on **agency verification flags** (e.g., "verified" status passed by the paying agency), meaning the ledger **only enforces pre-existing errors** (e.g., ineligible payments) rather than preventing them. The claim implies the ledger could act as a safeguard, but its utility is limited to **audit trails**, not decision-making. [confidence: high]
- **"Escrow fixes the risk mills cannot afford to cover"** — The article acknowledges escrow’s theoretical value but **ignores the financial feasibility**: mills would need **₹8,769–10,522 cr in escrow at any time**, requiring bank guarantees or collateral—something the article admits is "an open question." The causal claim that escrow "fixes" late payments assumes mills have the liquidity to implement it, which is unproven. [confidence: high]

---
**OUTDATED DATA:**
- **"₹4.84 lakh crore of trade since 2016 on e-NAM"** — The latest PIB update (28 July 2026) cites **₹4.84 lakh crore**, but the article does not check if this includes **2025-26 data** or if a newer fiscal year (2026-27) figure exists. The **1.89 crore farmer registrations by June 2026** also lacks a comparison to the **latest quarterly/annual report** (e.g., PIB’s 2026-27 progress). [confidence: medium]
- **"Farmer ID count passed 11 crore on 23 October 2026, five months ahead of the March 2027 target"** — While accurate for the stated date, the article does not verify if this is the **final count for 2026-27** or if a **November/December 2026 update** (post-article publication) revised the target or numbers. The **28,680 tenants/sharecroppers registered (October 2026)** also lacks a newer benchmark. [confidence: medium]
