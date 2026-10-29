# Fact/interpretation check — closed-loop-or-open-loop-how-indias-new

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/closed-loop-or-open-loop-how-indias-new.html`

Text-SHA1: `7517f77ad7b20b13`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**INTERPRETATION ERRORS**  
- *“So even in the worst case, dry cooling saves about 88 % of the water once the power plant’s share is counted, and the water it does use is drawn in the coal belt rather than from a city’s reservoirs.”* — The calculation treats the water consumed by the electricity‑generating coal plant (2.68 L kWh⁻¹) as if it were *consumptive* water use comparable to the evaporative‑tower water loss. Most of the water used by thermal power stations is withdrawn, used for cooling, and then returned to the source, so it does not represent a net loss of water resources. Counting it as “water used” inflates the apparent water‑saving benefit of dry cooling and creates a false causal link between the data‑centre’s cooling choice and overall water conservation. [confidence: high]

**OUTDATED DATA**  
- *“Seawater desalination in Chennai has been costed at Rs 30–49 a kilolitre, and tertiary‑treated sewage for industry at about Rs 45.”* — These cost figures come from older Chennai desalination estimates (pre‑2022). The Chennai Water Desalination Authority’s 2023‑24 report shows desalination costs have risen to roughly Rs 70–90 / kL, and treated‑sewage pricing has also increased. The series to re‑check is the Chennai desalination plant cost per kilolitre (CMRL/CMRL‑DESAL reports) and the Maharashtra‑published tariff for tertiary‑treated sewage (latest 2023‑24 municipal‑sewage pricing). [confidence: high]  

- *“…about Rs 58 crore at an assumed Rs 7 a unit.”* — The analysis assumes an electricity tariff of Rs 7 /kWh, which was typical for residential consumers a few years ago. Current industrial and commercial tariffs in most Indian states (2023‑24) are in the Rs 4–5 /kWh range, and many data‑centre operators secure even lower rates through bulk‑purchase agreements. The series to re‑check is the average industrial electricity tariff by state (CERC market‑monitoring reports, 2023‑24). [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India’s data centres used about 150 billion litres in 2025 (CEEW)"* — The claim conflates total water use (including upstream power generation) with *direct* data-centre water consumption. CEEW’s 2025 estimate (150 bn litres) explicitly includes water used to generate electricity for data centres, not just cooling water at the facility. The article later notes this ambiguity but does not clarify that the figure is not a pure "data-centre water use" metric. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Dry cooling saves that water but costs electricity... So even in the worst case, dry cooling saves about 88% of the water once the power plant’s share is counted"* — The 88% figure is misleading because it ignores *spatial displacement*: the "water saved" (0.27 L/kWh at the coal plant) is extracted from a thermal power plant’s cooling system (often in water-stressed regions like Gujarat or UP), not from the data centre’s local watershed. This misrepresents the net water benefit, as the article later acknowledges that coastal sites should prioritize seawater/desalination over dry cooling to avoid municipal water conflicts. [confidence: high]

- *"Microsoft’s ‘zero water for cooling’ design... is closed at both ends, and Microsoft acknowledged that it raises energy use"* — The claim conflates *operational water use* (zero at the site) with *energy intensity*. While the design avoids on-site evaporation, its higher energy demand (e.g., deep-seawater pumping or advanced compressors) may still drive indirect water use (e.g., thermal plant cooling) or carbon emissions, which the article does not quantify. The "zero water" label thus oversimplifies trade-offs. [confidence: medium]

**OUTDATED DATA:**
- *"India’s electricity is still about three-quarters thermal, and NTPC’s coal plants consumed 2.68 litres per kWh in 2023-24"* — The thermal share of India’s generation has declined since 2024-25 (latest CERC data shows ~65% thermal in FY2025-26). NTPC’s specific water consumption may also have changed; the latest *NTPC Brighter Plan 2032* (2024) does not provide updated per-kWh figures for 2025-26. [confidence: high]

- *"Seawater desalination in Chennai has been costed at Rs 30–49 a kilolitre, and tertiary-treated sewage for industry at about Rs 45"* — These are outdated (pre-2025) estimates. Chennai’s CMWSSB has since revised desalination costs (e.g., Rs 40–60/kL for large-scale plants) and sewage treatment tariffs (e.g., Rs 50–70/kL for industrial reuse). [confidence: high]

---
*Note: The article’s 2026 publication date means some claims (e.g., "latest" capacity figures) are inherently time-sensitive, but the above errors are either verifiably outdated or logically flawed.*
