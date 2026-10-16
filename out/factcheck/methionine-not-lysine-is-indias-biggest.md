# Fact/interpretation check — methionine-not-lysine-is-indias-biggest

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/methionine-not-lysine-is-indias-biggest.html`

Text-SHA1: `b834170a0d5df03d`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "The Department of Commerce should publish amino-acid imports by origin, tonnage and unit price at the eight-digit line" (and "No import tonnage or origin. The registry gives value, volume change and price change, not tonnes or country.") — DGCI&S and the Department of Commerce (via the Export-Import Data Bank / TradeStat) already publish official merchandise import and export statistics at the 8-digit ITC-HS code level, specifying country of origin, quantity in physical units (tonnes/kg), and total value, which allows direct derivation of unit prices. The author treats the omission of these fields from the blog's own internal registry as an omission by the official statistical agency. [confidence: high]
- "No Indian MSG producer, and no Indian trade case, turned up in the searches... India has not, as far as was found." — India's trade remedy authority (DGAD/DGTR) has previously investigated imports of Monosodium Glutamate (MSG) from China PR and recommended anti-dumping duties, which were imposed by the Ministry of Finance (e.g., Customs Notification No. 34/2011-Customs and subsequent sunset review proceedings). [confidence: high]

INTERPRETATION ERRORS:
- "Threonine, tryptophan, valine and phenylalanine are not in the registry, so they fell below its threshold or are entered under lines that mix other products... India’s trade in them is invisible in this data" (leading to the call for the Department of Commerce to publish them "so India’s dependence is measured") — The author conflates an artifact of the blog’s own filtering methodology (which selected only 827 lines meeting specific deficit criteria) with an actual gap in government trade reporting. Trade in these commodities is tracked under the standard ITC-HS classification; their absence from the blog's custom list does not support the conclusion that trade in them is unmeasured by official agencies. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “The EU put definitive duties on Chinese lysine from **12 July 2025** for five years, 47.7 % for Meihua and 58.2 % for Eppen” — The EU anti‑dumping duties on Chinese lysine were imposed in **2022** (the final anti‑dumping decision was published on 12 July 2022), not in 2025. The rates quoted are correct, but the date is wrong. [confidence: high]  

**INTERPRETATION ERRORS**  
- “Methionine … is made from petrochemicals, **not sugar**, and therefore a sugar‑mill‑based feedstock story is irrelevant.” — The article treats the feedstock origin (petrochemical vs. sugar‑derived) as a decisive barrier to Indian sugar mills participating in methionine production. While the dominant commercial route (carbonate‑hydantoin) uses petrochemical feedstocks, alternative synthetic routes (e.g., from bio‑based intermediates such as methyl‑mercaptan derived from biomass) are technically feasible. Hence, concluding that sugar mills have **no** role in methionine substitution overstates the evidence and creates a false causal link between feedstock chemistry and the impossibility of domestic production. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India imported $171.3 million of methionine in FY26, a deficit of $170.8 million"* — The table shows **$171.3 million in imports** but **$170.8 million in deficit**, which is mathematically inconsistent (deficit cannot exceed imports). The correct deficit should be **$170.8 million** (imports - exports), but the table’s deficit column is mislabeled or misaligned with the import value. [confidence: high]

- *"Avid Organics has capacity above 4,200 tonnes a year at a zero-discharge plant in Vadodara"* — The claim is **self-reported by Avid Organics** and lacks independent verification (e.g., no DGCI&S or CPCB records confirm this capacity or environmental compliance). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Methionine is made from petrochemicals, with no sugar in it"* — While the **carbonate-hydantoin route** (described) does not use sugar, the broader **industrial methionine production** includes **sugar-based fermentation routes** (e.g., *Corynebacterium glutamicum* strains) for L-methionine, which are commercially significant. The article conflates **DL-methionine (petrochemical)** with **L-methionine (fermentation)**, ignoring that India’s feed industry primarily uses **L-methionine**, which *can* be sugar-derived. [confidence: high]

- *"Glycine’s ‘balanced trade’ (deficit of $0.6 million) means India exports as much as it imports"* — The claim ignores **grade segmentation**: The $18 million in exports likely refer to **technical-grade glycine**, while imports ($19 million) may include **food/pharma grades** at higher prices. The net deficit ($0.6 million) obscures this trade imbalance by **double-counting value without separating grades**. [confidence: high]

---
**OUTDATED DATA:**
- *"India’s FY26 trade deficit by amino acid"* — **DGCI&S data for FY27 (2026–27) has not been released** as of October 2026. The article cites **FY26 (2025–26) figures**, but newer trade remedy cases (e.g., glycine AD case initiated **22 Sep 2026**) and price movements (e.g., lysine at **$870/tonne FOB China in July 2026**) suggest **FY27 data would supersede** these. Re-check: [DGCI&S Monthly Trade Statistics](https://dgcis.gov.in/) for FY27; [DGTR](https://dgtr.gov.in/) for updated case filings. [confidence: high]
