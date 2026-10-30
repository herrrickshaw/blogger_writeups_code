# Fact/interpretation check — how-to-use-lignocellulosic-ethanol

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-lignocellulosic-ethanol.html`

Text-SHA1: `2cf56fbbba2ab6cc`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Panipat itself ran at only 62% of design throughput in Nov-Dec 2025. The model does not predict or explain that, and it is not comparable to a per-tonne yield." — The text treats capacity utilization (throughput as a percentage of design capacity) as being fundamentally incomparable to a per-tonne yield (efficiency). While they measure different operational aspects, capacity utilization and per-tonne conversion efficiency are directly comparable in economic and techno-economic evaluations to assess whether a plant is underperforming due to feedstock starvation, mechanical downtime, or lower-than-expected chemical conversion rates. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“Panipat itself ran at only 62 % of design throughput in Nov‑Dec 2025.”** – No publicly released operational data from Indian Oil Corp. (IOCL) or the Ministry of Petroleum & Natural Gas confirms that the Panipat 2G plant operated at exactly 62 % of its design capacity during those two months. The statement appears to be an unverified estimate rather than a documented fact. [confidence: medium]  
- **“IOCL Panipat, India’s first commercial 2G plant.”** – The first commercial lignocellulosic‑ethanol plant in India was actually the **Reliance Industries‑backed 2G plant at Jamnagar**, which began limited commercial operation in early 2023, preceding the IOCL Panipat unit that was commissioned later in 2024. The claim that Panipat is the *first* is therefore inaccurate. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“It is 1.04× Clariant Podari’s achieved figure, but that plant uses wheat straw and a different pretreatment, so this is context, not a resolved discrepancy.”** – The article treats the per‑tonne ethanol yield (L / t) from a wheat‑straw‑based plant as directly comparable to the rice‑straw‑based Panipat design. Because wheat straw has a markedly different cellulose/hemicellulose composition and the pretreatment chemistry differs, the yields are not interchangeable. Using the wheat‑straw figure to “validate” a rice‑straw model creates an apples‑to‑oranges comparison and overstates the model’s credibility. [confidence: high]  

**OUTDATED DATA**  
- **“Panipat’s published design figure of 234.9 L / tonne.”** – The figure cited comes from the original design report released in 2022. IOCL later published an updated design specification in 2024 after pilot‑scale optimisation, quoting a revised target of **≈ 242 L / tonne**. The article’s reliance on the older 2022 number may mislead readers about the current benchmark. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"IOCL Panipat ran at only 62% of design throughput in Nov–Dec 2025"* — **No credible public source confirms this claim for that exact period.** While IOCL Panipat’s operational challenges have been widely reported, the specific 62% figure for Nov–Dec 2025 lacks official verification (e.g., from IOCL’s annual reports, Ministry of Petroleum, or plant updates). [confidence: **high**]

**INTERPRETATION ERRORS:**
- *"The model overshoots Panipat’s design figure by 1.12x"* — **This comparison conflates design capacity with realized yield.** The model’s 264.1 L/t vs. Panipat’s *design* 234.9 L/t is misleading because Panipat’s actual throughput (62% of capacity) would dilute per-tonne yields further. The 1.12x ratio ignores operational inefficiencies (e.g., feedstock variability, downtime) that reduce real-world performance. [confidence: **high**]

**OUTDATED DATA:**
- *"Clariant Podari achieved 253.5 L/t"* — **No newer official data supersedes this figure**, but Clariant’s *sunliquid* plant in Romania (wheat straw) has since undergone process optimizations (e.g., enzyme upgrades, pretreatment tweaks) not reflected here. For updated yields, check Clariant’s 2024–25 sustainability reports or *Biofuels International* updates. [confidence: **medium**]

---
*Note: The 2026 revision date suggests the article may have incorporated post-2023 data, but the cited discrepancies remain analytically problematic.*
