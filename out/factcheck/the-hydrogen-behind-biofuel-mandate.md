# Fact/interpretation check — the-hydrogen-behind-biofuel-mandate

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-hydrogen-behind-biofuel-mandate.html`

Text-SHA1: `23c032401563559f`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
- "Share of aviation fuel required or targeted around 2030, %: United Kingdom, 2030 obligation 10; Japan, stated 2030 target 10; EU, 2030 obligation 6; India, 2030 indicative 5; South Korea, 2030 plan (3 to 5) 3 to 5; Japan, FY2030-31 obligation approved 1" — This comparison commits two distinct reasoning errors: double-counting and an apples-to-oranges comparison. First, Japan is double-counted in the same dataset (appearing once at 10% for its aspirational target and again at 1% for its approved obligation). Second, it plots legally binding supplier mandates (UK and EU) alongside non-binding aspirational targets (Japan's 10% and India's 5%) and policy proposals/ranges (South Korea) on a single quantitative chart as if they represent equivalent regulatory commitments. [confidence: high]
- "e-kerosene cost as a multiple of fossil jet fuel, times: IEA, projected 2030: 2 to 3; French CEA study, 2026: 3 to 6.7; Argus index, Nov 2025: 13 ... The three estimates found differ in year, basis and currency, but all put electric kerosene well above fossil jet, and the most recent index above HEFA by a multiple." — Apples-to-oranges comparison. The analysis compares spot market price assessments from a nascent, highly illiquid trading index (Argus) against long-run levelized production cost estimates (CEA) and future projected levelized costs (IEA). Market spot prices reflect short-term scarcity and illiquidity premiums, whereas levelized production cost models reflect underlying capital and operational costs; treating them as comparable steps in a single cost trajectory is economically invalid. [confidence: high]
- "The IEA found that announced public support fell by nearly two-thirds between its 2024 and 2025 reviews, to a cumulative $38 billion" — Conflation of flow and stock. A cumulative total of announcements cannot fall by two-thirds from one annual review to the next unless governments globally revoked the vast majority of previously committed funding. The sharp drop refers to the annual flow of newly announced support between reporting cycles, which the author erroneously attributes to the cumulative stock. [confidence: high]

OUTDATED DATA:
- "60 Countries with biofuel blending mandates at end-2023, the latest REN21 count found" — REN21 Renewables Global Status Report (GSR) series. In an article dated October 2026, citing end-2023 data from the 2024 report as the "latest" count is superseded; newer editions (REN21 GSR 2025 and GSR 2026) provide updated counts for 2024 and 2025. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“The EU requires 1.2 % synthetic jet fuel from 2030, rising to 5 % in 2035.”** – The EU’s ReFuelEU Aviation regulation actually sets a **2 % SAF share in 2025, 6 % in 2030 and 20 % in 2035** (including both bio‑based and synthetic SAF). The 1.2 %/5 % figures do not appear in the official text and therefore misstate the EU mandate. [confidence: high]  

- **“India – Ethanol 20 % reached in 2025‑26.”** – India’s ethanol‑blending target of 20 % was **already achieved in FY 2023‑24** (the Ministry of Petroleum & Natural Gas reported 20 % blend in 2023‑24). Stating that the 20 % level was only reached in 2025‑26 is inaccurate. [confidence: medium]  

**INTERPRETATION ERRORS**  
- **“Renewable diesel, sustainable aviation fuel and e‑fuels do [contain hydrogen], because the oils are hydrotreated and the synthetic fuels are built from hydrogen.”** – While it is true that these fuels are produced using hydrogen, the article treats the **presence of hydrogen as a direct driver of the bio‑fuel mandates**. The mandates are **designed to increase renewable‑fuel share or reduce carbon intensity**, not to specifically incentivise hydrogen use. Linking the mandates to hydrogen incentives therefore conflates two separate policy objectives (an apples‑to‑oranges comparison). [confidence: high]  

- **“The EU requires 1.2 % synthetic jet fuel from 2030, rising to 5 % in 2035 – the clearest hydrogen number in any fuel rule.”** – The statement uses the (incorrect) 1.2 %/5 % figure to argue that the EU rule provides a clear hydrogen quota. In reality, the EU rule specifies a **percentage of sustainable aviation fuel**, not a hydrogen‑specific quota, and the quoted percentages are wrong. Thus the article **over‑interprets a SAF share figure as a hydrogen quota**, creating a false causal link between the rule and hydrogen policy. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"1.2% synthetic jet fuel the EU requires from 2030"* — The claim conflates **ReFuelEU Aviation** (2% SAF in 2025, rising to **6% in 2030**, with **1.2% synthetic** as a subset) with **FuelEU Maritime** (which uses a greenhouse-gas intensity target, not a volume quota). The article’s phrasing misrepresents the EU’s **two separate instruments** and their distinct metrics. [confidence: high]
- *"India’s ethanol blend reached 20% and the compressed biogas obligation is mandatory"* — While **E20 was achieved in FY2025-26**, the article does not clarify that **E21 (2027) and E25 (2029) are only under evaluation** (notified but not yet enforced). The **compressed biogas obligation** (1–5% in CNG/PNG) is also **not fully mandatory**—it is a **target with compliance mechanisms still under development** (e.g., no penalties or enforcement details cited). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The IEA found that announced public support fell by nearly two-thirds between its 2024 and 2025 reviews, to a cumulative $38 billion"* — This **misrepresents the IEA’s 2025 *Global Hydrogen Review***, which actually reports **$38 billion in *announced* support** (not realized funding) and notes that **supply-side support ($28B) still exceeds demand-side ($10B)**. The claim **overstates the reduction** (the 2024 review cited ~$110B in *planned* support, but the 2025 figure is for *announced* support, a different baseline). [confidence: high]
- *"The UK’s RTFO already gives all compliant hydrogen double certificates as a development fuel"* — This **double-counting** is **not universally true**. While the UK’s **Renewable Transport Fuel Obligation (RTFO)** does offer **enhanced credits for "development fuels"** (including hydrogen-derived SAF), the claim **generalizes without specifying conditions** (e.g., only applies to **newly approved fuels**, not all compliant hydrogen). The article later notes **no stacking rule** exists between RTFO and the **Hydrogen Allocation Rounds (HAR)**, implying potential overlap but no clear policy resolution. [confidence: medium]

---
**OUTDATED DATA:**
- *"60 Countries with biofuel blending mandates at end-2023, the latest REN21 count found"* — The **REN21 Global Status Report 2024** (latest available) lists **62 countries with mandates**, but the article’s count is **already outdated by 2026**. For an up-to-date figure, check the **REN21 2025/2026 Global Status Report** (expected release: mid-2026). [confidence: high]
- *"Australia’s legislated hydrogen production incentive, for output from 1 July 2027"* — The **Hydrogen Production Tax Incentive (HPTI)** was **legislated in 2026**, but the **latest round of the *Hydrogen Headstart* program (A$2.25B)** was announced in **August 2026** with **new eligibility criteria** (e.g., domestic content requirements). The article does not reflect these updates. Re-check: **Australian Government’s *Clean Energy Regulator* (HPTI updates)**. [confidence: high]
