# Fact/interpretation check — indias-lysine-deficit-is-102-million

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-lysine-deficit-is-102-million.html`

Text-SHA1: `5991b9ac33ef31aa`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "The Department of Commerce should publish amino-acid imports by origin, tonnage and unit price at the eight-digit line, including threonine, tryptophan and valine , so India’s dependence on Chinese supply is measured and not inferred from a vendor report." — The DGCI&S (under the Department of Commerce) already publishes official import data broken down by country of origin, quantity/tonnage, and value at the 8-digit ITC-HS level (including for lysine under HS 29224100). Bilateral import volumes, values, and unit prices from China are already tracked and publicly accessible in official trade databases; they do not need to be inferred from commercial market vendor reports. [confidence: high]

INTERPRETATION ERRORS:
- "Chemical synthesis gives a mixture of the D and L forms, so it is used for glycine, which has no mirror image, and for amino acids that are useful in either form, such as DL-methionine." — This is a false causal explanation. Chemical synthesis yields a racemic mixture of D- and L-enantiomers only when synthesizing chiral molecules. Glycine is achiral (it has no stereocenters and no D- or L-enantiomers). Chemical synthesis is viable for glycine precisely because stereospecificity is irrelevant, not because the synthesis produces a D/L mixture. [confidence: high]
- "At the yield above, 25,000 tonnes of lysine needs about 50,000 to 62,500 tonnes of sugar or sugar-equivalent a year, on this blog’s arithmetic. That is a big plant for one mill, and about 0.2% of the sugar India eats." — This is an apples-to-oranges comparison. The feedstock demand for the proposed fermentation plant is calculated in fermentable sugar equivalents from industrial byproducts like molasses, whereas "the sugar India eats" (~28 million tonnes) measures refined white sugar consumed directly in human diets. Benchmarking industrial byproduct feedstock demand against dietary table-sugar consumption is conceptually mismatched. [confidence: medium]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- “For lysine the organism is *Corynebacterium glutamicum*, sometimes *Brevibacterium flavum*.” — Modern commercial lysine production worldwide is carried out almost exclusively with engineered strains of *Corynebacterium glutamicum*; *Brevibacterium flavum* has not been used in industrial lysine fermentations for decades and is not a current producer. The statement therefore misidentifies an active production organism. [confidence: high]  

**INTERPRETATION ERRORS:**  
- “The world price is set by a few very large Chinese plants, whose oversupply has pushed prices to record lows.” — While Chinese capacity dominates global lysine supply, price formation in the global amino‑acid market is driven by overall supply‑and‑demand balance, contract structures, and commodity‑price indices, not unilaterally “set” by a handful of producers. The claim conflates market dominance with price‑setting power, creating a causal link that is not supported by the underlying economics. [confidence: high]  

**OUTDATED DATA:**  
none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India imports $106 million of lysine a year and its unit price fell 18.7% in FY26"* — The article later clarifies that the **$106 million figure is the *value* of imports (not the unit price or quantity)**, while the **$102 million deficit** is the net import cost after domestic supply. The claim conflates total import value with unit price change, which is misleading without context. [confidence: high]
- *"China’s share of world lysine capacity, by two industry reports [is] 76–79%"* — The two cited figures (76% in 2023 and 78.9% capacity share) are **from different years and definitions** (production share vs. operating capacity), and neither is a primary source. The article does not reconcile these discrepancies. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The world price is set by very large Chinese plants. [...] A smaller maker is therefore competing with plants of a scale that India does not have"* — While Chinese dominance is plausible, the claim **overstates causality**: India’s inability to produce lysine isn’t solely due to scale but also **sterility requirements, oxygen-dependent fermentation, and downstream processing barriers** (e.g., ion exchange, crystallization). The article later acknowledges these but frames scale as the *primary* obstacle without sufficient evidence that smaller plants couldn’t adapt. [confidence: high]
- *"Molasses is the cheap part. The fermenter is the hard part"* — While true, this **ignores the feedstock availability gap**: India’s molasses supply is already diverted to ethanol, and the article’s own arithmetic shows a 25,000-tonne lysine plant would require **50,000–62,500 tonnes of sugar-equivalent annually**—a tiny fraction (0.2%) of total sugar consumption but **not negligible given ethanol’s priority**. The claim downplays logistical constraints. [confidence: medium]

---
**OUTDATED DATA:**
- *"India’s FY26 trade deficit in lysine, on $106 million of imports"* — The data is from **FY26 (2025–26)**, but newer official releases (e.g., **DGCI&S monthly trade data** or **Commerce Ministry’s latest HS-8 breakdown**) may exist for **FY27 (2026–27)**. Re-check the [DGCI&S import database](https://dgcis.gov.in/) for updated figures. [confidence: high]
- *"China’s operating capacity at 4.31 million tonnes, over 78.9% of the world"* — This is from a **2023/2025 industry report abstract**, but **no primary source is cited**. The latest **FAO or USDA global amino acid market reports (2026)** could provide updated capacity data. [confidence: high]
