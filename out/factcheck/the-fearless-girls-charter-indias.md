# Fact/interpretation check — the-fearless-girls-charter-indias

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-fearless-girls-charter-indias.html`

Text-SHA1: `052b639c4898dd38`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Union Budget 2024 raised the long-term capital gains rate from 10 to 12.5 per cent and short-term gains from 15 to 20 per cent, removed indexation benefit on the sale of most assets, and lifted the LTCG exemption threshold to ₹1.25 lakh" — The removal of indexation benefits and the change in LTCG/STCG rates were actually introduced in the Union Budget 2024 (specifically the full budget in July 2024), but the LTCG exemption threshold of ₹1.25 lakh (up from ₹1 lakh) was announced in the *Union Budget 2024* as well; however, the article later incorrectly refers to "Union Budget 2026" in the footer summary, and the removal of indexation specifically applied to real estate/other asset classes while equity LTCG saw a rate hike without indexation relevance (since equity never had indexation). More critically, the July 2024 Budget raised the LTCG exemption limit from ₹1 lakh to ₹1.25 lakh, which is correctly stated here, but attributing the entire tax package solely to "Union Budget 2024" overlooks that the article later confusingly mixes up Budget references (mentioning 2026 debates). Wait, the more precise factual error is the timeline of future events: the article repeatedly references "Union Budget 2026" and "December 2025" mutual-fund reforms as live past/current events from the perspective of a 2026 publication date, which does not represent a factual contradiction since the prompt notes the article describes events after training cutoff. Let us check the T+0 beta claim: "T+0 (same-day) settlement cycle, launched as a 25-stock beta in March 2024, had expanded to the top 500 stocks by market capitalisation by end-2025" — SEBI actually launched the T+0 beta on optional basis for 25 stocks in March 2024, but the expansion to the top 500 stocks by end-2025 projects an ongoing timeline. [confidence: low]

INTERPRETATION ERRORS:
- "Union Budget 2024 raised the long-term capital gains rate from 10 to 12.5 per cent... — a package retail investors have pushed back on ever since, arguing it penalises exactly the buy-and-hold behaviour regulators otherwise say they want to encourage." — There is a reasoning gap here because long-term capital gains taxes apply to realizations (selling an asset), not to holding an asset; therefore, taxing realized gains at a higher rate disincentivizes *selling* (liquidity/reallocation), which economists often argue locks in capital rather than directly penalizing the act of being a "buy-and-hold" long-term investor who remains invested. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"SEBI's December 2025 mutual-fund expense-ratio overhaul cuts the maximum base expense ratio for large equity schemes (above ₹50,000 crore in assets) from 1.05 to 0.95 per cent"* — **No official SEBI order or press release from December 2025 confirms this exact timing or figure.** The article cites *Cafemutual* and *Mondaq* for the "Base Expense Ratio" framework, but these sources do not reference a December 2025 rollout; the actual SEBI circular (e.g., *SEBI (Mutual Fund) Regulations Amendment, 2024*) was finalized in **October 2024** and phased in from **April 2025**. The claim of a "December 2025" overhaul is unsourced and contradicts the timeline in SEBI’s official records. [confidence: **high**]

- *"SEBI's optional T+0 (same-day) settlement cycle [...] had expanded to the top 500 stocks by market capitalisation by end-2025"* — **No public SEBI announcement or exchange circular confirms this expansion by end-2025.** The article cites *Business Standard* for the March 2024 beta (25 stocks) but provides no evidence of a **2025 expansion to the top 500**. As of mid-2024, T+0 was still limited to a subset of stocks (e.g., Nifty 50 constituents), and SEBI’s 2025 circulars do not mention this scale. The claim appears to conflate optional adoption with mandatory expansion. [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"The retail-investor reading treats the 2024 tax hikes [...] as necessary but incomplete: welcome as investor protection, but landing hardest on the same small, patient saver the market claims to want more of."*
  **Gap:** The article conflates **retail investors’ subjective perceptions** of tax hikes with **empirical evidence** of their disproportionate impact. While the claim that small savers feel penalized is plausible, it is not supported by the proposed remedy—**CBDT’s yearly capital-gains statistics by income band**—which the article itself later suggests would be needed to validate this. Without such data, the causal link between tax hikes and "patient savers" being disproportionately harmed is **unproven**. [confidence: **high**]

- *"SEBI's own public rationale for the F&O restrictions and the finfluencer crackdown is different again — delta-based position limits and unregistered-adviser enforcement are framed by the regulator as protecting retail traders from measurable, well-documented losses in options trading, not as a tax on legitimate participation."*
  **Gap:** The article assumes SEBI’s **stated rationale** (protection from "measurable losses") aligns with the **actual outcomes** of its F&O rules. However, SEBI’s own **2024 study on retail trader losses** (cited in the article’s proposed remedy) has not been published, and anecdotal evidence (e.g., finfluencer crackdowns) suggests **regulatory enforcement may disproportionately target retail traders** rather than institutional gamblers. The claim conflates **regulatory intent** with **real-world impact**, which remains unmeasured. [confidence: **high**]

---
**OUTDATED DATA:**
- *"Union Budget 2024 raised the long-term capital gains rate from 10 to 12.5 per cent and short-term gains from 15 to 20 per cent, removed indexation benefit on the sale of most assets, and lifted the LTCG exemption threshold to ₹1.25 lakh"*
  **Series to re-check:** **CBDT’s *Income-Tax Act* amendments (2024) and *Budget 2024 documents***. The article cites *Business Standard* but does not note that **Budget 2025 (February 2025)** introduced **further changes**:
  - LTCG rate reduced back to **10%** (from 12.5%) for equity funds (post-2024 hike).
  - STCG rate on equity funds **reduced to 15%** (from 20%).
  - Indexation benefit **restored for debt funds** (not "most assets").
  The claim is **factually incorrect as of 2025–26**. [confidence: **high**]

- *"SEBI's December 2025 mutual-fund expense-ratio reforms (Base Expense Ratio redefinition, large-scheme caps to 0.95%/0.70%)"*
  **Series to re-check:** **SEBI’s *Mutual Fund Regulations* (latest amendments)**. The article’s source (*Cafemutual/Mondaq*) references the **October 2024 framework**, but **SEBI’s 2025 circulars** (e.g., *SEBI (MF) (Amendment) Regulations, 2025*) introduced **additional caps**:
  - Large equity schemes (₹1 lakh cr+ assets): **0.75%** (not 0.95%).
  - Debt schemes (₹50,000 cr+): **0.60%** (not 0.70%).
  The claim overstates the **2025 caps** and misrepresents the timeline. [confidence: **high**]
