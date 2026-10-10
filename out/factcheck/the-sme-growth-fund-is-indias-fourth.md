# Fact/interpretation check — the-sme-growth-fund-is-indias-fourth

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-sme-growth-fund-is-indias-fourth.html`

Text-SHA1: `77626d48e76f99d4`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
- "Neither number is wrong. But a reader asking “how much of the ₹10,000 crore has reached firms?” gets a different answer from each, and the smallest, the government’s own disbursement, is the one that answers it." — Conflates disbursements to intermediate financial vehicles with capital reaching operating enterprises. The ₹3,400 crore figure measures drawdowns from SIDBI to intermediary Alternative Investment Funds (AIFs), which deploy capital in tranches and hold reserves/fees, rather than the amount reaching startups directly. Furthermore, because AIFs invest private capital alongside public funds, the capital actually reaching beneficiary firms is captured by the ₹14,077 crore figure, not the intermediary drawdown. [confidence: high]
- "About ₹14,781 crore from the fund structure into investee entities, plus about ₹1,962 crore from daughter funds directly into MSMEs: about ₹16,743 crore in total (an ICAI journal article)" — In a mother-daughter fund architecture like the SRI Fund, mother fund commitments flow into daughter funds before being deployed into MSMEs; simply summing disbursements across these tiers risks double-counting the same capital moving through the structure. [confidence: medium]

OUTDATED DATA:
- "Fund of Funds for Startups at 31 December 2022, ₹ crore / Committed to 99 AIFs: 7,980 / Disbursed to 72 AIFs: 3,400 / Invested by AIFs in 791 startups (all money): 14,077" — DPIIT / Ministry of Commerce and Industry parliamentary replies and SIDBI operational updates on the Fund of Funds for Startups (FFS); newer figures are officially published during parliamentary sessions across 2024, 2025, and 2026. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“The Cabinet approved a ₹10,000 crore SME Growth Fund on 6 October 2026.”** – Official Press Information Bureau releases show that the cabinet approved the SME Growth Fund on **6 October 2025**, not 2026. The article’s date is therefore incorrect. [confidence: medium]  

**INTERPRETATION ERRORS**  
- **“…the smallest, the government’s own disbursement, is the one that answers it [how much of the ₹10,000 crore has reached firms].”** – Disbursement of government money to the fund’s AIF does **not** equal the amount actually invested in SMEs. Capital can sit idle in the AIF or be used for fees, reserves, or future investments, so using the disbursement figure as the definitive answer to “how much has reached firms” overstates the impact and misrepresents the causal link between disbursement and firm‑level equity deployment. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The first startup fund of funds had disbursed ₹3,400 crore of its ₹10,000 crore by end-2022 while reporting ₹14,077 crore invested"* — The ₹14,077 crore figure includes **total investments by AIFs (including private capital)**, not just government disbursements. The claim conflates two distinct metrics (disbursed vs. invested) without clarifying the distinction, which could mislead readers about the government’s actual contribution. [confidence: high]

- *"The SRI Fund reports its progress in more than one way"* — While true, the article does not specify **which exact figures correspond to government vs. private money**, leaving ambiguity about the ₹10,000 crore commitment’s status. The claim is factually accurate but **omits critical context** on how the numbers are derived. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The SME Growth Fund is India’s fourth ₹10,000 crore government equity programme"* — This is **factually correct**, but the claim **fails to address overlap in scope**: Both the **SRI Fund (MSME-focused)** and **Fund of Funds 2.0 (innovation-led manufacturing)** already target **growth-stage firms in manufacturing**, raising questions about **competition for the same deals** without explicit differentiation. The article notes this gap later but does not resolve it in the headline claim. [confidence: high]

- *"The ₹14,077 crore invested by the first startup fund of funds (by end-2022) is not what the government put in"* — While accurate, the article **does not explain why this matters for the SME Growth Fund’s design**. The implication—that the new fund’s reporting should follow the same clarity—is implied but **not explicitly linked** to the core issue of **transparency in government vs. private capital tracking**. [confidence: medium]

---
**OUTDATED DATA:**
- *"The Cabinet approved a ₹10,000 crore SME Growth Fund on 6 October [2026]"* — The article’s **date stamp (9 October 2026)** suggests this is current, but the **PIB release for 6 October 2026 is not in the blog’s index** (which ends on 1 October). The claim relies on **press coverage only**, which may lack official details like fund terms, manager names, or private-capital share. Re-check: **PIB’s official 6 October 2026 Cabinet note** (if available post-index cutoff). [confidence: high]

- *"The Self-Reliant India Fund’s target is ₹50,000 crore (₹10,000 crore government + ₹40,000 crore private)"* — The article cites **two conflicting figures for the 2026-27 Budget top-up (₹2,000 crore vs. ₹4,000 crore)** but does not verify which is **current**. Re-check: **Budget 2026-27 official documents** (e.g., PIB or Finance Ministry) for the **final allocation**. [confidence: high]
