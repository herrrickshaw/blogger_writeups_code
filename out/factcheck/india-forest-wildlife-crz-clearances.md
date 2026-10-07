# Fact/interpretation check — india-forest-wildlife-crz-clearances

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-forest-wildlife-crz-clearances.html`

Text-SHA1: `1955d764176ffb8c`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"MAHESH NAIR (likely a data-entry artifact — an individual's name, not an agency) | 1,697"* — The claim that this is a "likely data-entry artifact" is speculative and unsupported by the article’s own data or external verification. The article does not provide evidence (e.g., cross-checking with official agency lists or MoEFCC records) to confirm this is an error, nor does it explain why the name appears as an agency. [confidence: medium]

**INTERPRETATION ERRORS:**
- *"Forest Clearance is a second land-creation channel... Forest diversion adds ~122,666 more acres of granted land-use change — a different channel (mining, linear infra, hydro), on a different clock."* — The comparison conflates **granted forest diversion orders** (a subset of land-use changes for specific projects) with the **national industrial land bank** (~253,720 acres), which includes developed-and-vacant land across sectors (industrial, commercial, residential, etc.). The two are not directly comparable in scale, purpose, or timing (diversion orders are project-specific; the land bank is a static inventory). [confidence: high]

- *"Wildlife Clearance is the real bottleneck: only 10.7% of decided cases are granted, versus 42.0% for Forest and 31.3% for CRZ."* — While the grant rates are correctly stated, the causal claim that Wildlife Clearance is *the* bottleneck ignores that **4,319 of 4,919 Wildlife Clearance cases are "in process"** (per the next paragraph), meaning most are not yet "decided." The bottleneck may lie in the **pending stage**, not the grant rate of decided cases. [confidence: high]

**OUTDATED DATA:**
- *"Industrial Information & Land Bank, retrieved 2026"* — The **Industrial Information System (IIS)** and **Land Bank** data are periodically updated by the Ministry of Commerce and Industry. The latest official figures (as of mid-2024) for developed-and-vacant industrial land are available in the **Annual Report of the Department for Promotion of Industry and Internal Trade (DPIIT)** or the **IIS portal**. The article should cross-check with the most recent DPIIT publication (e.g., FY2024–25 or FY2025–26). [confidence: high]

- *"1.05 million ha in the pipeline (inflated by delisted applications and one ~74,000-ha outlier)"* — The **PARIVESH 2.0 API** data (fetched 2026-07-22) may have been updated since the article’s publication. Users should verify the current pipeline figure against the latest **MoEFCC’s Forest Clearance dashboard** or the **PARIVESH API** (e.g., via [github.com/herrrickshaw/india-ec-subsector-analysis](https://github.com/herrrickshaw/india-ec-subsector-analysis)) for 2026 Q3/Q4. [confidence: high]
