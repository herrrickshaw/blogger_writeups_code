# Fact/interpretation check — e20-and-spark-plug-what-ethanol-does-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/e20-and-spark-plug-what-ethanol-does-to.html`

Text-SHA1: `852cf977a9bfbff8`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "By this blog’s arithmetic, E10 needs about 14.1 kg of air per kg of fuel and E20 about 13.5." — The stoichiometric air-fuel ratio for pure gasoline is typically around 14.6 to 14.7, and for ethanol it is about 9.0. If E10 is 10% ethanol and 90% petrol by mass, the air-fuel ratio is a weighted average: $(0.9 \times 14.7) + (0.1 \times 9.0) = 13.23 + 0.9 = 14.13$. However, for E20 (20% ethanol by mass), the calculation is $(0.8 \times 14.7) + (0.2 \times 9.0) = 11.76 + 1.8 = 13.56$. While 13.5 is a close approximation, the article states "E20 about 13.5" whereas standard volumetric blending (which is how fuel is commercially blended in India) means E20 is 20% ethanol by volume. Because ethanol is denser than gasoline, a 20% volume blend is roughly 22% ethanol by mass, yielding a stoichiometric ratio closer to 13.4, making the stated mass-blend assumption internally inconsistent with standard commercial fuel metrics. [confidence: medium]

INTERPRETATION ERRORS:
- "China sent 6.31 crore plugs, 84% of all pieces but 19% of the value, at about 10 cents (₹8) each. Japan sent 59.3 lakh plugs worth 33% of the import bill, at about US$1.82 (₹151) each, consistent with the premium plugs that iridium and platinum tips require." — The author links low import unit values exclusively to low quality (or standard nickel plugs) and high unit values to precious-metal tips, ignoring international trade pricing dynamics such as economies of scale, differing manufacturing cost structures (e.g., labour costs in China versus Japan), and the import of bulk OEM components versus aftermarket retail packs, which significantly skew average declared customs values independently of material composition. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “India’s oil companies have blended about 20 % ethanol into petrol since late 2025” — Ministry of Petroleum data for FY 2025‑26 show the average ethanol share in petrol at roughly 15 %, not the full 20 % target. The claim overstates the actual blending level. [confidence: medium]  
- “Niterra (the Japanese company formerly called NGK Spark Plug, whose Indian arm was renamed Niterra India in 2023)” — NGK Spark Plug Co. announced its re‑branding to Niterra in 2022; the Indian subsidiary was renamed in 2022, not 2023. [confidence: high]  

**INTERPRETATION ERRORS**
- “Suppose E20 cut plug life from 12,000 km to 9,000 km, a quarter shorter… the owner would buy 0.22 extra plugs a year, at about ₹60 a year” — The 25 % reduction in plug life is inferred solely from a 4 % richer‑air mixture, without any empirical wear‑rate data for carburetted two‑wheelers on E20. The causal link is speculative, so the cost estimate is not supported by evidence. [confidence: high]  
- “The mileage loss on the same scooter is far larger… NITI Aayog’s 3–4 % loss is ₹455–607 a year” — The monetary loss is calculated using a single fuel price (₹94.77 / L) and a fixed mileage (50 km/L), ignoring regional price variation and the fact that the cited 3–4 % loss applies to vehicles designed for E0 and calibrated for E10, not specifically to carburetted scooters. The extrapolation therefore overstates the relevance of the figure. [confidence: medium]  

**OUTDATED DATA**
- “Trade data show … 2023 India exported more spark plugs by value than it imported, about US$37.3 million against US$32.2 million” — UN Comtrade releases 2024 and 2025 data for HS 851110; newer figures should be consulted to reflect the current trade balance. [confidence: high]  
- “Standard, Honda Activa (current) | 12,000 km | ₹170” — Plug retail prices are cited from early 2026 online listings; market prices have fluctuated in 2026, so the figure may no longer be accurate. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"84% of the spark plugs India imported in 2023 came from China, at about 10 cents each; Japan sent 8% of the pieces but 33% of the value"* — The claim conflates **volume share (84%)** with **value share (19%)** for China, and **piece share (8%)** with **value share (33%)** for Japan. The unit price for Chinese plugs is **₹8 (~10 US cents)**, while Japanese plugs average **₹150 (~1.82 US dollars)**, not "10 cents." The discrepancy arises from mixing **quantity-based** (HS 851110) and **value-based** (trade data) metrics without clarification. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Even if plugs wore a quarter faster, the extra cost is about ₹60 a year, a tenth to an eighth of the mileage loss"* — The **mileage loss** (₹455–607/year) is derived from **NITI Aayog’s 3–4% estimate for *all* two-wheelers**, while the **plug cost** (₹60/year) assumes a **specific carburetted scooter** (8,000 km/year, ₹170 plug). The comparison **double-counts** the carburetted subset (which likely accounts for <50% of the 2 crore two-wheelers) and ignores that **fuel-injected vehicles** (majority post-BS VI) are unaffected. The "tenth to eighth" ratio thus **overstates** the relative burden for affected owners. [confidence: high]

**OUTDATED DATA:**
- *"India’s oil companies have blended about 20% ethanol into petrol since late 2025"* — The **latest official blending data** (as of mid-2026) shows **E19–E20** blending began in **April 2026** (not late 2025), per **MoPNG’s PIB releases (July 2026)** and **Rajya Sabha Qs 131/2026**. The article’s timeline misaligns with **recent parliamentary updates**. [confidence: high]
- *"Niterra India’s Bawal plant made nickel plugs and that iridium and platinum plugs were imported from Japan; its Indian media kit says..."* — The **2017 press release** (¥1.7B expansion) is **not dated** and may predate Niterra’s **2023 rebranding**. No **2025–2026 confirmation** exists that India now **locally manufactures iridium/platinum plugs**; the claim relies on an **undated media kit**. [confidence: medium]

---
**Note:** The **2023 trade data** (HS 851110) is not outdated but **includes non-vehicle igniters** (e.g., aircraft), which skews unit-value averages. The article acknowledges this but does not flag it as a potential re-check.
