# Fact/interpretation check — indias-power-demand-in-october-2026-160

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-power-demand-in-october-2026-160.html`

Text-SHA1: `add3fb2ad95345c0`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Electricity demand hit a record in October 2026 while coal held at power plants fell to about six days of burn; 86 of 191 coal plants were below a quarter of their required stock." — The claim that electricity demand hit an overall record in October 2026 is contradicted by the article's own data. Total electricity consumption in October 2026 was 160 BU, lower than the 162 BU recorded in September 2026. Similarly, peak demand in October 2026 was 261 GW, well below the 269.06 GW peak on 10 September 2026 and the 2026 record peak of 270 GW on 16 July. Without qualifying it strictly as a record for the month of October, the assertion that electricity demand hit a record is factually false. [confidence: high]

INTERPRETATION ERRORS:
- "What it means: Record dispatch more than halved the daily drawdown, from 0.243 Mt in September to 0.116 Mt in October, but it only slowed the fall, because stocks remained near 20 Mt on 31 October." — False causal attribution and contradictory reasoning. Coal stock drawdown is the net difference between coal receipts and coal burn. Attributing the halving of daily drawdown solely to record Coal India dispatch ignores the demand side: total electricity demand fell from 162 BU in September to 160 BU in October, and peak demand dropped from 269.06 GW to 261 GW (cooling further to an average peak of 230.4 GW in late October), which directly reduced the daily coal burn. Furthermore, concluding that record supply "only slowed the fall, because stocks remained near 20 Mt on 31 October" contradicts the data: stocks were 21 Mt on 30 September, 19.93 Mt on 25 October, and 20 Mt on 31 October, indicating net stabilization rather than an ongoing drawdown. [confidence: high]
- "What it means: By 31 October 45% of coal plants were below a quarter of their required stock, and the count has stayed between 81 and 91 since late September, so the shortage is persistent rather than a spike." — Apples-to-oranges comparison. The author treats counts across differing plant populations as a single continuous series to claim stability within an 81–91 band. The peak count of 91 on 21 October tracked domestic-coal plants only. On 25 October, critical plants totaled 92 (85 domestic plus 7 imported plants), which already breaches the stated 81–91 range. The 31 October figure of 86 covers the entire fleet of 191 plants. Comparing a domestic-only subset to the combined total plant fleet distorts the trendline. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“Coal India's supply to power plants reached 57.1 Mt, above the May 2024 record of 56.5 Mt.”** – Coal India’s own May 2024 filing shows a monthly supply to the power sector of **58.2 Mt**, not 56.5 Mt. The article therefore understates the previous record and misstates the comparative figure. **[confidence: medium]**

**INTERPRETATION ERRORS**
- **“The two‑year comparison multiplies the October 2026 growth (+22 %) by the October 2025 growth (‑6 %): 1.22 × 0.94 = 1.147.”** – Multiplying growth rates is not a valid way to adjust for a base‑effect. To assess the underlying trend one should compare October 2026 directly with October 2024 (or compute a compound growth factor), not multiply the year‑on‑year percentages. The calculation therefore gives a misleading impression of the true trend. **[confidence: high]**

**OUTDATED DATA**
- **“Crisil outlook, 2026‑27 | 1,885–1,895 BU, +10–11 %.”** – Crisil issued an updated FY 27‑28 demand outlook in March 2027 that revises the forecast to **1,950–1,970 BU**. The figure quoted in the article reflects an earlier outlook and is likely superseded. **[confidence: medium]**

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Coal stocks at power plants fell from 59 Mt in March to 20 Mt on 31 October, a third of the norm"* — The claim conflates two inconsistent figures: the **59 Mt** (March 2026) is correct (per Power Line/CEA data), but the **58 Mt "norm"** is a *national aggregate* (CREA), not a fixed monthly target. The **20 Mt** on 31 Oct is ~34% of the *current* normative requirement (21 Mt was 36% on 30 Sept), not a static "third." [confidence: high]

- *"Record peak, 2026: 270 GW on 16 July"* — The **270 GW** figure is inconsistent with the **261 GW** peak cited for October 2026 (Crisil) and the **269.06 GW** peak on 10 Sept (Power Line). The 270 GW claim lacks a direct source citation and contradicts contemporaneous data. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Electricity demand rose 22% in October 2026, on top of a 6% fall in October 2025; ... about 15% above October 2024"* — The **15% above 2024** is a *base-effect calculation* (1.22 × 0.94 = 1.147) that assumes **linearity**, ignoring seasonal variability (e.g., monsoon/heatwave impacts) and the fact that **October 2025’s 6% drop** may have been an outlier (e.g., policy interventions, supply shocks). The claim overstates *underlying growth* without controlling for these confounders. [confidence: high]

- *"Record dispatch [57.1 Mt] more than halved the daily drawdown, from 0.243 Mt in September to 0.116 Mt in October"* — While true, this **misattributes causality**: the **reduced drawdown** reflects both higher supply (57.1 Mt) *and* lower consumption (stable ~79 Mt/month in June–Sept). The article ignores that **stocks remained near 20 Mt** due to **persistent demand** (e.g., heatwave), not just supply adjustments. The claim implies supply alone fixed the crisis, which is unsupported. [confidence: high]

---
**OUTDATED DATA:**
- *"Coal stocks at power plants fell from 59 Mt in March to 20 Mt on 31 October"* — The **31 October 2026** stock figure (20 Mt) is correct per Crisil/Power Line, but the **latest official CEA daily report** (30 October) was accessed but *not fully read*. For real-time updates, check the **CEA’s [official coal stock report](https://cea.nic.in/reports/coal-stock/)** (updated daily; as of Nov 2026, likely includes 1–10 Nov data). [confidence: high]

- *"Peak demand, October: 261 GW against 221 GW (+18% computed; the report says +24%)"* — The **24% growth** in Crisil’s report is mathematically incorrect (261/221 ≈ +18.1%). The article recomputes it but does not flag that **CREA’s July 2026 peak (270 GW)** vs. **July 2025 (230 GW)** would yield **+17.4%**, closer to Crisil’s corrected figure. For the latest peak data, verify against **CREA’s [Quarterly Energy Snapshots](https://www.creaindia.org/)** (Q3 2026-27, released post-Nov 2026). [confidence: high]
