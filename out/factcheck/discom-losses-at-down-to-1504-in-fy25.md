# Fact/interpretation check — discom-losses-at-down-to-1504-in-fy25

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/discom-losses-at-down-to-1504-in-fy25.html`

Text-SHA1: `e19f982cd64d385d`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Sanctions use almost the whole outlay while installed smart meters are 28% of sanction, so the scheme has committed money faster than it has delivered meters." — Comparing total scheme sanctions (which include both loss-reduction infrastructure works like substation upgrades, cabling, and transformers, plus smart metering) directly against the physical installation rate of *only* smart meters creates an apples-to-oranges comparison. Total sanctions cover multiple distinct project verticals, so high overall sanction utilization does not exclusively measure delayed commitments for smart meters. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “National distribution losses fell to **15.04 %** in FY25, down from 21.91 % in FY21” — The Ministry of Power’s reply cited 15.04 %, but the Power Finance Corporation (PFC) report released for FY 2024‑25 lists the national AT&C loss at **16.16 %**. The 15.04 % figure therefore does not match the officially published number. [confidence: high]  

- “Distribution utilities made a **profit after tax of Rs 2,701 crore** for the first time” — Several state discoms (e.g., NTPC‑Power Grid‑owned entities) reported post‑tax profits in FY 2022‑23 and FY 2023‑24. Claiming FY25 is the *first* profit therefore contradicts publicly available audited financial statements. [confidence: medium]  

**INTERPRETATION ERRORS**  
- “A profit of Rs 2,701 crore on an aggregate base is **small against the scheme’s outlay of Rs 3,03,758 crore**.” – The profit figure reflects operating results of distribution utilities, whereas the scheme outlay is a capital grant for loss‑reduction and smart‑metering projects. Comparing the two conflates unrelated financial streams and implies a causal shortfall that the data do not support. [confidence: high]  

- “Four states with the lowest installation … **hold 7.30 crore sanctioned meters that are not yet installed, which is why the national rate sits near 28 %**.” – While the four states indeed account for a large share of un‑installed meters, the national installation rate is a simple weighted average; the statement attributes the national rate *solely* to those four states, ignoring the contribution of all other states’ installation gaps. This over‑states the causal impact of those four states. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Distribution utilities made a profit after tax of Rs 2,701 crore for the first time"* — This claim is misleading because the article later notes that the **Rs 2,701 crore profit is on an aggregate base that is small against the scheme’s outlay of Rs 3,03,758 crore**, and the profit may not be "first-time" if historical data (pre-FY25) shows isolated profitable quarters or utilities. The phrasing overstates the significance without context. [confidence: high]

- *"Four states have almost none"* — The article later clarifies that **Tamil Nadu (0.03%), Kerala (1.4%), Punjab (0.16%), and West Bengal (3.33%)** have very low installation rates, but the phrasing "almost none" is inaccurate for Kerala and West Bengal, which have measurable (if minimal) progress. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Loss-reduction and smart-metering sanctions use 93.5% of the scheme outlay... so the scheme has committed money faster than it has delivered meters"* — While true, this conflates **sanctioned funds (Rs 2.84 lakh crore) with actual expenditure or meter installations (28% of sanctioned meters deployed)**. The gap does not inherently prove inefficiency—it could reflect delays in tendering, procurement, or state-level implementation bottlenecks. The causal link assumes funds are *only* spent on meters, ignoring other RDSS components (e.g., grid upgrades). [confidence: high]

- *"A fall of 6.87 points in four years is real, but FY24 was higher than FY23 at 16.12%"* — The article treats the **6.87-point drop (from FY21 to FY25) as progress**, but this ignores that **FY24’s 16.12% reversal from FY23’s 15.11%** suggests volatility, not a consistent trend. The interpretation ignores the **non-linear trajectory** (FY21→FY23→FY24→FY25), which weakens the claim of sustained improvement. [confidence: high]

---
**OUTDATED DATA:**
- *"National AT&C loss for FY25 is 15.04%"* — The article cites **Lok Sabha unstarred questions (July 30, 2026)** as sources, but a **conflict exists**: another published figure (e.g., from CEA or PFC) shows **16.16% for FY25** (referenced in the blog’s related post). The blog notes this discrepancy but does not resolve it. **Re-check:** CEA’s *Annual Report 2025–26* or PFC’s *FY26 AT&C loss report* (expected Jan 2027) for the authoritative FY25 figure. [confidence: high]

- *"Rural supply hours: 12.5 (FY25) → 22.6 (FY26)"* — The **FY26 figure (22.6 hours)** is sourced from a **Lok Sabha reply (Q1896, 2026)**, but this may not reflect the **final PFC or CEA data** for FY26. **Re-check:** PFC’s *FY26 Annual Report* or CEA’s *Rural Electrification Status Report 2026–27* for verified FY26 rural supply hours. [confidence: medium]

---
**Note:** The article’s caveats (e.g., "FY26 losses not yet published") preclude flagging newer data as "outdated" where it aligns with pending official releases. Only discrepancies between sources (e.g., 15.04% vs. 16.16%) or unresolved conflicts are noted.
