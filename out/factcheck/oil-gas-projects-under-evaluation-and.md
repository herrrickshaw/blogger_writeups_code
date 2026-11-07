# Fact/interpretation check — oil-gas-projects-under-evaluation-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/oil-gas-projects-under-evaluation-and.html`

Text-SHA1: `ed7b53551db32d4e`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- "GEM's last global pipeline census (2022) found 122,500 km in pre-construction against 70,900 km being built" — Global Energy Monitor (GEM) Global Gas Infrastructure Tracker; newer annual updates for 2023, 2024, and 2025 are available. [confidence: high]
- "GEM's 2022 oil pipeline report had the US ahead of every other country in new capacity by length, with pre-construction projects adding about 21.8 mb/d." — Global Energy Monitor (GEM) Global Oil Infrastructure Tracker; newer annual releases are available. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- “2025 was a record: 9 projects, 72 Mtpa sanctioned (Wood Mackenzie), **over 100 bcm/yr by the IEA's count**.” – 72 Mtpa of LNG is roughly 34–35 bcm/yr (1 Mtpa ≈ 0.48 bcm/yr). It cannot correspond to “over 100 bcm/yr”. The two figures are inconsistent, indicating a mis‑statement of the volume. [confidence: high]  

**INTERPRETATION ERRORS:**  
- “The economics explain it: deepwater breakeven is roughly $40/bbl against about $65/bbl for new US shale wells, **which matters when ADI sees Brent at $55‑60 on a 2‑4.5 MMbpd surplus**.” – The claim that the Brent price being between the two breakevens automatically makes deepwater projects more attractive is a false causal inference. Investment decisions also depend on project lead‑times, financing risk, capital intensity, and the fact that the cited 2‑4.5 MMbpd surplus is a global supply‑demand gap, not a US‑shale‑specific metric. Thus the breakeven comparison alone does not substantively support the conclusion that deepwater will dominate. [confidence: medium]  

**OUTDATED DATA:**  
- none found   (the request was to report only two distinct problem types).

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India has the world's third-largest buildout, with nearly three-quarters already under construction"* — **India’s pipeline buildout is not third-largest globally** (confidence: **high**). The claim conflates *proportion under construction* (where India may lead regionally) with *total length* or *global ranking*. The 2022 GEM *Asia Gas Tracker* (cited) does not rank India as top-3 in absolute terms; China and Russia dominate pipeline capacity. The phrasing risks misinterpretation as a global ranking, which is unsupported.

---

**INTERPRETATION ERRORS:**
- *"The economics explain it: deepwater breakeven is roughly $40/bbl against about $65/bbl for new US shale wells, which matters when ADI sees Brent at $55-60 on a 2-4.5 MMbpd surplus"* — **The breakeven comparison does not logically justify offshore FID activity** (confidence: **high**). While deepwater ($40/bbl) is cheaper than shale ($65/bbl), the $55-60 Brent forecast *overlaps* the deepwater breakeven, meaning offshore projects are not *guaranteed* to be economic. The claim ignores:
  1. **Project-specific costs**: $40/bbl is a *general* breakeven; actual costs vary by field (e.g., deepwater Gulf of Mexico vs. West Africa).
  2. **Surplus context**: A 2-4.5 MMbpd supply surplus suggests *demand weakness*, which could depress prices further, undermining the breakeven logic.
  3. **Timing lag**: FIDs in 2026 may reflect *anticipated* price recovery, not current economics.

- *"Whether even a fraction is built depends on contracting in a softer market"* (LNG segment) — **The claim conflates *proposed* projects with *likely* FIDs** (confidence: **high**). The 648 Mtpa North American pre-FID stock (IGU 2024) is *not* a forecast of sanctioned capacity but a *potential* pipeline. The article later states that Wood Mackenzie expects *only 4-5 FIDs in 2026*, implying most pre-FID projects are speculative. The causal link to "contracting in a softer market" is plausible but *not supported by the data*: the 648 Mtpa figure is *proposed*, not *contracted*, and lacks LNG offtake commitments.

---
**OUTDATED DATA:**
- *"GEM's last global pipeline census (2022) found 122,500 km in pre-construction against 70,900 km being built"* — **Series to re-check: *Global Energy Monitor’s "Pipe Dreams" pipeline tracker*** (confidence: **high**). The 2022 data is explicitly labeled as outdated in the article itself ("A 2022 snapshot, not current"). A 2026 update would clarify whether the pre-construction backlog has shrunk (e.g., due to cancellations) or grown (e.g., new projects in India/Asia).

- *"GEM's extraction tracker (GOGET) found at least 20 fields approved in 2023, around 8 billion boe"* — **Series to re-check: *GEM’s GOGET (Global Oil & Gas Extraction Tracker)*** (confidence: **high**). The article notes this is from 2023 but provides no 2024/2025/2026 update. A newer GOGET release could show whether 2026 saw a continuation of "capital discipline" (as implied in the onshore segment) or a rebound in approvals.

- *"I found no 2026 update, so treat this segment as the least evidenced here"* (Oil pipelines) — **Series to re-check: *GEM’s oil pipeline report*** (confidence: **high**). The 2022 US-dominated data (21.8 mb/d pre-construction) is flagged as outdated. A 2026 update from GEM or Wood Mackenzie would address whether US pipeline projects remain dominant or if new regions (e.g., Africa, Asia) have emerged.

- *"IEA's May 2026 Oil Market Report expected 2026 refinery throughput to fall by 1.6 mb/d to 82.3 mb/d"* — **Series to re-check: *IEA’s Oil Market Report*** (confidence: **high**). The article cites this as "current" but does not confirm whether a later 2026 update (e.g., June/July) revised the forecast. The IEA’s *June 2026* or *October 2026* reports might show whether the 1.6 mb/d decline materialized or was adjusted.

---
**Note on LPG/India data:**
- *"I found no India demand or import data this round"* — This is **not an outdated-data issue** but a **data gap**, not a factual or interpretive error. It is explicitly acknowledged as a limitation.
