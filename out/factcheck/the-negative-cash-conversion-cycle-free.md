# Fact/interpretation check — the-negative-cash-conversion-cycle-free

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-negative-cash-conversion-cycle-free.html`

Text-SHA1: `d8692fbe0668e811`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Financial years end between September 2025 and August 2026." and "financial years ending Sep 2025 to Aug 2026" — The article cites future dates (the current date of this response being earlier than late 2026), making financial year-end data for 2025/2026 impossible to have been reported in annual statements yet. [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 198290, Requested 5863. Please try again in 29m54.096s. Need more tokens? Upgrade to Dev Tier today at https:/]

## Mistral open-mistral-nemo

Here is the structured feedback based on the provided article:

---

**FACTUAL ERRORS:**
- **“Carillion’s standard supplier terms before it collapsed in 2018 [were] 120 days”** — The article states this as a fact, but the **House of Commons report (May 2018)** explicitly describes Carillion’s *standard* terms as **"an extraordinary 120 days"** while noting that suppliers could be paid in **45 days via early payment facilities**. The claim conflates *standard terms* (120 days) with *actual payment behavior* (often 45 days with discounts), which complicates the narrative about "running out of cash." The report’s wording suggests the 120-day term was a **negotiated but rarely honored** baseline, not the norm. [confidence: high]

- **“Apple’s cash conversion cycle, the most negative of 14 companies checked”** — While Apple’s **−72 days** is indeed the most negative in the table, the article does not clarify whether this is based on **absolute values** or **relative to industry peers**. For example, **Larsen & Toubro (−26 days)** or **Maruti Suzuki (−15 days)** are also negative but in entirely different sectors (construction vs. automotive). The claim risks **misleading readers** into assuming Apple’s cycle is uniquely extreme without contextualizing it against sector norms. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- **“A negative cash conversion cycle is a sign of a superb business, or of one quietly running out of cash”** — The reasoning gap lies in **equating the *existence* of a negative cycle with financial health** without distinguishing between:
  1) **Sustainable negative cycles** (e.g., supermarkets with zero DSO and long DPO due to bargaining power).
  2) **Unsustainable negative cycles** (e.g., Carillion’s case, where long DPO masked **debt substitution** via supplier finance).
  The article later acknowledges this distinction but **does not explicitly debunk the initial binary framing** as universally applicable. A reader might infer that *any* negative cycle is ambiguous, which is true—but the article’s **checklist later in the piece** refines this into a **multi-factor test**, not a simple either/or. [confidence: high]

- **“The negative cycles come from different places: Apple (−72 days) holds very little inventory (11 days) and takes about 115 days to pay suppliers. That is bargaining power: suppliers compete to be in its products.”** — While **Apple’s 115-day DPO** is plausible given its scale, the claim **overstates the causal link** between DPO and "suppliers competing to be in its products." The **true driver** is likely Apple’s **global supply chain leverage** (e.g., forcing suppliers to accept longer terms via contracts or bulk discounts). The article does not explore whether Apple’s DPO is **negotiated in advance** (a bargaining power play) or **resulting from cash flow constraints** (a warning sign). The distinction is critical but left implicit. [confidence: high]

---

**OUTDATED DATA:**
- **“Financial years ending Sep 2025 to Aug 2026; average of opening and closing balances”** — The article was **revised on 28 October 2026**, but the data is pulled from **Yahoo Finance** without verification against **company annual reports** (as noted in the "Method and limits" section). For **Indian companies**, the latest fiscal years (e.g., **2025–26 for most listed firms**) may have been superseded by:
  - **Annual reports for FY 2026–27** (published post-March 2027).
  - **Quarterly updates** (e.g., Q1 FY 2027–28, released by mid-October 2027).
  The article does not check if **Hindustan Unilever, Maruti Suzuki, or others** have since revised their DPO/DIO/DSO metrics in **post-2026 filings**. [confidence: high]
  *Series to re-check:* **Company-specific annual reports (e.g., HUL’s FY 2026–27 report, Maruti’s Q1 FY 2027–28 update)**.

- **“Supplier finance disclosures under IFRS (rules effective 1 Jan 2024)”** — The article cites the **IAS 7/IFRS 7 amendments** but does not verify whether the **14 companies analyzed** (e.g., Apple, Hindustan Unilever) have **already disclosed supplier finance terms** in their **FY 2025–26 or FY 2026–27 filings**. For example:
  - **Hindustan Unilever** (IFRS-listed) would be required to disclose such arrangements if used.
  - **Apple** (US GAAP) would follow **FASB’s 2022-04 update**, but the article does not confirm if it has done so in recent filings.
  The claim assumes **compliance is universal**, but enforcement varies by jurisdiction. [confidence: medium]

---
