# Fact/interpretation check — indias-cheapest-lng-capacity-is-extra

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-cheapest-lng-capacity-is-extra.html`

Text-SHA1: `b277feba1ad06ad0`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Shell’s ₹21,600 crore expansion of Hazira." / "Hazira 6.28 → 26.2 (cleared 2025) | Expansion needing new marine works | 21,600 | 19.92 | 1,084 | ₹21,600 cr incl. new breakwater, jetty and 2.8 million m³ dredging; environment clearance Sep 2025" — The ₹21,600 crore environmental and CRZ clearance granted for Hazira Port is for the overall multi-cargo port expansion (handling dry bulk, containers, break-bulk, and liquid cargo), not an expansion of Shell's LNG regasification terminal from 6.28 to 26.2 MMTPA. Conflating total port cargo throughput (in million metric tonnes per annum) with LNG regasification capacity (MMTPA of LNG) is factually incorrect; adding ~20 MMTPA of LNG regasification capacity at Hazira alone would equal nearly 75 MMSCMD of gas send-out and nearly 40% of India's entire LNG capacity. [confidence: high]

INTERPRETATION ERRORS:
- "in April–May 2026, worked at 24–37% of capacity while Dahej ran at 92%" / "91.9% vs 10.5–40.1% Utilisation of Dahej (on its old 17.5 MMTPA base) against the other seven terminals, April–May 2026" — The article uses the 91.9% figure to argue that Dahej's newly expanded capacity is running full while greenfield terminals sit empty. However, as the text notes, this 91.9% figure uses the old 17.5 MMTPA base as the denominator rather than the expanded 22.5 MMTPA capacity commissioned on 31 March 2026. On the enlarged base, Dahej operated at only 65.6%, and the article concedes the new 5 MMTPA is "mostly headroom." Measuring Dahej against its pre-expansion capacity while comparing it to other terminals on their full capacity bases creates an apples-to-oranges metric that undermines the core causal thesis. [confidence: high]
- "~40 vs 95–100 MMSCMD Gujarat’s GSPL evacuation capacity against the regas capacity of Dahej, Mundra and Hazira" / "yet the GSPL pipelines that evacuate gas from them carry “only around 40 MMSCMD”" — The article compares the combined regasification capacity of Dahej, Hazira, and Mundra against the evacuation capacity of Gujarat State Petronet Limited's (GSPL) network to prove an evacuation bottleneck. This is an invalid comparison because GSPL is an intra-state transmission network. Significant volumes from Dahej and Hazira are evacuated directly into national interstate trunk pipelines operated by GAIL (notably the Hazira–Vijaipur–Jagdishpur [HVJ] and Dahej–Vijaipur [DVPL] systems) which take gas outside Gujarat independently of GSPL. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 8937, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Dahej ran at 92% of capacity while PNGRB’s own data point to the pipeline out, not the tank, as the constraint"** — The claim conflates two timeframes: Dahej’s utilisation is reported at **91.9% for April–May 2026** (PPAC data) and **~85% on the enlarged 22.5 MMTPA capacity in April–June 2026** (Petronet’s own results), but the pipeline constraint (GSPL’s ~40 MMSCMD capacity vs. ~130 MMSCMD regas capacity in Gujarat) is a **long-standing issue** (not specific to 2026). The article’s phrasing misrepresents the temporal link between utilisation and pipeline constraints. [confidence: high]

**INTERPRETATION ERRORS:**
- **"India’s new onshore terminals cost ₹950–1,290 crore per MMTPA, ran 22–35 months late"** — While the cost and delay ranges are factually correct, the claim **misrepresents causality**: the delays are primarily driven by **marine works (breakwaters, dredging), evacuation pipeline gaps, and regulatory hurdles** (e.g., Dabhol’s breakwater took 44 months; Jafrabad’s FSRU is still unoperational due to charter failures). The article later acknowledges this but frames the delays as generic project inefficiencies rather than systemic bottlenecks tied to **location-specific constraints** (e.g., Gujarat’s pipeline choke vs. Dahej’s pre-existing infrastructure). [confidence: high]

**OUTDATED DATA:**
- **"PPAC’s latest Ready Reckoner lists 53.5 MMTPA of regasification capacity"** — As of **June 2026** (PPAC’s May 2026 Ready Reckoner), Dahej’s expansion to **22.5 MMTPA (commissioned 31 March 2026)** is **not reflected** in the capacity figures cited (still listed at 17.5 MMTPA). The article notes this discrepancy but does not adjust the **total nameplate capacity** (should be **~58.5 MMTPA**, not 53.5). [confidence: high]
- **"LNG imports for 2025-26 and June–September 2026"** — The article cites **provisional PPAC data** for these periods but does not clarify whether these are **finalised figures** or **preliminary estimates**. For example, the **2025-26 import figure (34,216 MMSCM)** may be updated in PPAC’s **final annual report** (due ~December 2026). [confidence: medium]

---
**Note:** The article’s reliance on **press reports** (e.g., PTI, ICRA) for cost/schedule data introduces potential variability, but these were flagged only where they conflicted with **direct PPAC/PNGRB sources** (e.g., Dahej’s capacity lag). No **stylistic or minor inconsistencies** were flagged per instructions.
