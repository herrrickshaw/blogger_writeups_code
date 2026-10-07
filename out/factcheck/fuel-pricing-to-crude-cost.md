# Fact/interpretation check — fuel-pricing-to-crude-cost

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fuel-pricing-to-crude-cost.html`

Text-SHA1: `ef133d7760d594b0`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Ethanol is excise-exempt, so the more of the litre it makes up, the less central excise the government collects on that litre — and, as the map below shows, that foregone excise outweighs ethanol's own cost premium over crude-linked petrol, so a cost-reflective blended price actually falls slightly as the blend rises." — The author assumes that because central excise is applied on a per-litre basis, substituting a portion of gasoline with excise-exempt ethanol mechanically reduces the total absolute excise collected per litre. However, standard Indian fiscal mechanics dictate that fixed-rate central excise is levied on the total volume of *petrol* (or blended fuel) cleared, or alternatively, if excise applies strictly to the petroleum component, the consumer retail price reflects the blended product where tax incidence per volume unit of final fuel depends on whether the excise is statutory per litre of total fuel or per litre of petroleum component. Furthermore, the claim that a higher ethanol blend (priced at ₹71.16/l procurement cost) results in a net *drop* in the final cost-reflective retail price compared to crude-linked petrol (where the underlying dealer price ex-refinery is around ₹53.07/l) ignores the fact that ethanol is more expensive than the raw dealer-price component of unblended petrol, creating an internal cost increase that is not necessarily offset by a proportional tax reduction unless the excise exemption is structured to pass the full tax savings directly to the blend volume. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's installed ethanol distillery capacity is roughly 2,000 crore litres for ESY2025-26 (CareEdge estimate)"* — **2,000 crore litres is 20 billion litres**, which is implausibly high for India’s total ethanol capacity (latest official data from 2024–25 shows ~10.5 billion litres installed capacity, per PPAC/Ministry of Food Processing Industries). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The scenario range makes the excise lever visible: a 97% swing in crude (past-year low to high) would, on a naive full pass-through, move Delhi petrol by ≈43% (₹87.65 to ₹125.71)"* — **The claim conflates "naive full pass-through" with the actual tax structure.** The 43% swing assumes *only* the dealer price (crude-linked) moves, ignoring that VAT/GST also compounds on the higher dealer price, amplifying the pass-through beyond the "naive" baseline. The article later clarifies this is a deliberate simplification to isolate tax effects, but the phrasing risks misleading readers into thinking the 43% figure represents the *total* pass-through effect. [confidence: high]

**OUTDATED DATA:**
- *"PPAC's last published monthly Indian basket crude price runs only to September 2025"* — **PPAC’s Indian Basket series is now published monthly (e.g., October 2025 onward), but the article uses a static 01.10.2025 baseline for all scenarios. Re-check: PPAC’s [official monthly series](https://www.ppac.gov.in) (or [Business Standard’s archive](https://www.business-standard.com)) for October 2025–September 2026 updates. [confidence: high]

---
*Note: No other distinct factual, interpretation, or outdated-data issues were found in the provided text.*
