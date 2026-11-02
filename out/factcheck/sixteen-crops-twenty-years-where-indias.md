# Fact/interpretation check — sixteen-crops-twenty-years-where-indias

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/sixteen-crops-twenty-years-where-indias.html`

Text-SHA1: `6ca35b2bf41fc518`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- *“The fastest growers, maize and moong, are the crops where both land and yield expanded, pulled by new demand from ethanol and poultry feed in maize’s case.”* — The article attributes maize’s land‑ and yield‑expansion to ethanol demand (and poultry feed for moong) without presenting evidence of a causal link; the data shown only demonstrate correlation, not that these demand factors *pulled* the growth. [confidence: high]  

- *“The crops with the most room to grow output without more land are those with the widest gaps between their best and worst states: jowar, maize, moong, urad and bajra.”* — A wide inter‑state yield gap does not automatically imply that output can be increased solely by closing the gap; other constraints (soil, climate, input availability) may limit expansion, so the inference overstates what the yield‑gap statistic alone can tell us. [confidence: medium]  

**OUTDATED DATA:**  
- *“All figures are from the Department of Agriculture’s Unified Portal for Agricultural Statistics (UPAG): … 2025‑26 at the third advance estimate.”* — By October 2026 the final (or at least revised) 2025‑26 estimates have typically been released, superseding the third‑advance numbers used in the analysis. The series to re‑check is the UPAG “All‑India production, area and yield” for FY 2025‑26 (final/revised release). [confidence: high]  

- *“District‑wise production, 2015‑16 to 2024‑25 (district shares use the 2022‑23 to 2024‑25 average).”* — More recent district‑level data for 2025‑26 are now available from UPAG; relying on averages that stop at 2024‑25 makes the district‑share figures outdated. The series to re‑check is the UPAG “District‑wise production” for FY 2025‑26. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"0.0% Annual soybean yield growth over twenty years; every tonne of extra output came from more land"** — This claim is **incorrect** based on the article’s own data. The soybean yield in 2023-26 is stated as **~1,060 kg/ha**, identical to the 2003-06 baseline (~1,060 kg/ha), but the article later clarifies that **area expanded from 73 to 129 lakh hectares** while yield remained flat. However, the **2025-26 production peak (15.3 million tonnes) and subsequent drop (12.6 million in 2025-26)** contradict the "all extra output from land" narrative, as yield stagnation alone cannot explain such volatility. The **UPAG data (2025-26 third advance estimates) likely show yield fluctuations**, not a strict 0% growth. [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- **"The crops with the most room to grow output without more land are those with the widest gaps between their best and worst states"** — This is a **false causal claim**. While yield gaps (e.g., jowar’s 2.9× AP vs. national average) reflect **potential for improvement**, they do not inherently imply "room to grow output without more land." For example:
  - **Maize** (widest gap: 194% in WB vs. 70% in Maharashtra) grew **5.8% annually**, but **half from new land**—contradicting the claim.
  - **Jowar** (widest gap: 285% in AP) **shrunk** due to land loss, not yield potential.
  The reasoning conflates **yield potential** (a static metric) with **actual growth drivers** (land vs. yield expansion). [confidence: **high**]

---
**OUTDATED DATA:**
- **"Output averaged 147 million tonnes in 2023-26, up from 88 million in 2003-06"** — The **2025-26 third advance estimate (500 million tonnes for sugarcane alone)** and **record rice output (154 million tonnes in 2025-26)** suggest these figures are **already superseded**. Re-check:
  - **UPAG all-India production data (2025-26 final estimates)** for rice, wheat, and sugarcane.
  - **2024-25 and 2025-26 actuals** (not just 2023-26 averages). [confidence: **high**]

---
**Note:** No stylistic or minor inconsistencies flagged. The article’s core methodology (log-scale decomposition, UPAG sources) appears sound, but the above gaps exist.
