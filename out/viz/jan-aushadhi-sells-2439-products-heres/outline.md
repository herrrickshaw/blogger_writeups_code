Revised
16 September 2026
· v1.1.0 · [what changed](#changelog)

2,439Products in the current PMBJP basket — 2,125 medicines + 314 surgical items

91%China's share of India's paracetamol API imports — the highest-dependency molecule checked, and Jan Aushadhi's single most common one (43 SKUs)

15Molecules cross-referenced against known China-API-dependency figures

0Public datasets mapping any Jan Aushadhi product to its API's country of origin

Jan Aushadhi — formally the Pradhan Mantri Bhartiya Janaushadhi Pariyojana (PMBJP) — sells generic versions of almost the entire National List of Essential Medicines at government-run Kendras, priced 50–80% below branded equivalents. Its current product basket, per the [official PMBI Product List](https://www.pmbi.co.in/ProductList.aspx), runs to 2,439 items. This piece does two things with that list: shows what's actually in it, and traces what can honestly be said about where the active ingredients behind its best-known molecules come from — a question this blog has already found, in researching India's broader pharma-API dependency, does not have a single clean answer.

Union Minister Mansukh L. Mandaviya at the signing of an MoU between the National Yuva Cooperative Society and the Bureau of Pharma PSUs of India (BPPI) to set up 1,000 more Janaushadhi Kendras. Source: Press Information Bureau, Government of India, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Mansukh_L._Mandaviya_addressing_at_the_signing_ceremony_of_an_MoU_between_National_Yuva_Cooperative_Society_(NYCS)_and_Bureau_of_Pharma_PSUs_of_India_(BPPI)_for_setting_up_of_1000_Pradhan_Mantri_Bharatiya_Janaushadhi_Kendras.jpg), [GODL-India](https://en.wikipedia.org/wiki/Government_Open_Data_License_%E2%80%93_India).

## 1. What's actually in the catalogue

The 2,125 medicine-type products span roughly 60 named therapeutic groups; a handful account for most of the basket.


[T1 "1. What's actually in the catalogue" 10 rows; use rows by number in a chart "table" spec]
  cols: c0 Therapeutic group | c1 Products
  r0: Cardiovascular System (CVS) | 304
  r1: Central Nervous System (CNS) | 301
  r2: Antibiotics | 172
  r3: Anti-Diabetic | 148
  r4: Gastrointestinal (GIT) | 119
  r5: Respiratory | 113
  r6: Analgesic/Antipyretic/Anti-Inflammatory | 106
  r7: Supplement/Vitamin/Mineral | 106
  r8: Oncology | 88
  r9: Dermatology/Topical/External | 86


The remaining ~580 medicine products spread across smaller categories — ophthalmic/otic, urology, gynaecology, orthopaedics, anti-fungal, steroids & hormones, and further down, single-digit groups like anti-retroviral, anti-viral and vaccines. The other 314 products are surgical items and consumables (gloves, sutures, catheters, dressings) with no active pharmaceutical ingredient and no bearing on the sourcing question this piece is actually about.

A data-quality note from the source file itself. 344 of the 2,439 listed products (about 14%) carry an MRP of ₹0 or blank in the official export — not a transcription error on this end, but present in the source data as supplied. It most plausibly reflects products that are approved and listed but not currently priced or actively stocked at most Kendras; there is no way to confirm that distinction from the product list alone.

## 2. The question this list alone can't answer

India's pharma-API dependency on China is well documented at the national level: this blog's earlier reporting found 43.45% of India's pharma imports by value come from China, and that China supplies 70% or more of 97 distinct active ingredients. What doesn't exist — not from BPPI, not from PMBI, not from CDSCO's WHO-GMP manufacturer registry, not from any secondary source this research could locate — is a public dataset connecting any specific Jan Aushadhi product, batch or drug code to the country its API actually came from. CDSCO's WHO-GMP database records where the formulation is made (India has 1,500+ WHO-GMP-certified facilities); it says nothing about where the powder that went into that formulation was synthesised.

So the honest version of this question isn't "which Jan Aushadhi drugs use Chinese APIs" — nobody publishes that — it's "of Jan Aushadhi's most common molecules, which are independently known to be China-API-dependent, and by roughly how much."

## 3. The cross-reference: 15 molecules, checked against the catalogue

Matching well-documented China-dependency figures against how many distinct Jan Aushadhi SKUs contain each molecule (by name, case-insensitive, across every formulation and combination product) gives a genuine, if partial, picture:


[T2 "3. The cross-reference: 15 molecules, checked against the catalogue" 15 rows; use rows by number in a chart "table" spec]
  cols: c0 Molecule | c1 Route | c2 China import dependency | c3 Jan Aushadhi SKUs | c4 PLI-localised?
  r0: Paracetamol | Synthetic (petrochemical) | 91% | 43 | No
  r1: Metformin | Synthetic | KSMs "mostly Chinese origin"; partial PLI progress claimed | 77 | Partial
  r2: Diclofenac | Synthetic (petrochemical) | 72–80% | 23 | No
  r3: Amoxycillin | Fermentation | 89.9% | 22 | No
  r4: Atorvastatin | Synthetic | Localised under the Bulk Drugs PLI; residual dependency not separately quantified | 20 | Yes
  r5: Aspirin | Synthetic (petrochemical) | Not separately published; India retains domestic capacity | 16 | No
  r6: Cefixime | Semi-synthetic | Not independently located | 11 | No
  r7: Ceftriaxone | Semi-synthetic | Not independently located | 9 | No
  r8: Metronidazole | Synthetic | Not independently located | 8 | No
  r9: Ciprofloxacin | Fermentation | 97.98%→98.02% (FY23-24→FY24-25, flat) | 7 | No
  r10: Azithromycin | Semi-synthetic | Not independently located | 6 | No
  r11: Ibuprofen | Synthetic (petrochemical) | 99.34%→80.73% (FY23-24→FY24-25, improved, no PLI) | 5 | No
  r12: Ampicillin | Fermentation | Not molecule-specific; penicillin family generally near-total | 4 | No
  r13: Penicillin G | Fermentation | 95.8% | 2 | Yes
  r14: Rifampicin | Semi-synthetic | 89.17%→89.01% (FY23-24→FY24-25, flat) despite PLI localisation | 0 | Yes


[chart: 
 
 China Import-Dependency, by Molecule 
 Most-recent reported China-dependency figure, molecules used across Jan Aushadhi's catalogue 

 Ciprofloxacin 
 
 98.02% 
 7 Jan Aushadhi SKUs 

 Penicillin G 
 
 95.8% 
 2 SKUs • PLI-localised, still near-total dependent 

 Paracetamol 
 
 91% 
 43 SKUs • most common molecule in the catalogue 

 Amoxycillin 
 
 89.9% 
 22 SKUs 

 Rifampicin 
 
 89.01% 
 0 current SKUs • PLI-localised, still flat-dependent 

 Diclofenac 
 
 72–80% 
 23 SKUs 

 Source: this post's own Section 3 cross-reference table, per PIB Annexure PRID 223741]

Six of Jan Aushadhi's most common molecules are all 72%+ China-import-dependent — PLI localisation (Penicillin G, Rifampicin) hasn't closed the gap.

Four findings stand out. First, the molecule with the single largest number of Jan Aushadhi formulations — metformin, 77 SKUs once every dose strength and combination is counted — is also one where the PLI scheme claims real if partial progress, unlike paracetamol (43 SKUs, 91% dependent, not on the PLI's localised-molecule list at all). Second, Penicillin G and Rifampicin both show the same pattern, drawn from this blog's own earlier PIB Annexure analysis: both are Bulk Drugs PLI-localised molecules, and both are still near-total or flat China-dependent (95.8%, and 89.17%→89.01%) — localisation and falling dependency are not the same thing. Third, ibuprofen cuts the other way: its dependence fell sharply, 99.34% to 80.73% in a single year, with no PLI project behind that improvement at all — market forces alone moved this number more than the PLI scheme moved Penicillin G or Rifampicin. Fourth, for five of the fifteen molecules checked — cefixime, ceftriaxone, metronidazole, azithromycin and ampicillin — no independently verifiable China-dependency figure could be located at all. That is a real gap in what is publicly known, not a finding of low dependency; this piece reports it as a gap rather than guessing a number.

## 4. One product that quietly disappeared

An earlier, apparently older PMBJP price list this research also examined listed "Rifampicin and Isoniazide Tablets IP (450mg+300mg)," a fixed-dose anti-TB combination, drug code 379. That exact product — and anything else containing "rifampicin" or "isoniazid" by name — is absent from the current 2,439-item catalogue. Rifampicin itself remains a Bulk Drugs PLI-localised molecule, so this isn't necessarily a supply problem; it could equally be a reformulation, a rename, or simply that the older list this research consulted was already stale by the time it was found. Flagged here as an open question, not a conclusion.

## 5. What would actually close the gap

Nothing in this catalogue or its category structure is a mystery — PMBI publishes the product list itself in full, and it updates daily. What's missing is one layer down: BPPI does not require or publish API country-of-origin disclosure from the manufacturers whose formulations it lists, the way, for instance, US FDA drug listings increasingly require facility-level API sourcing data. Without that, a reader can know that Jan Aushadhi's paracetamol is one of 43 SKUs pulling from a China-91%-dependent molecule, but not whether the specific strip in a specific Kendra's shelf traces to a domestic KSM plant or an imported one. Closing that gap is a disclosure-policy question, not a research one — and outside what this piece, or any public source available to it, can currently answer.

Sources: official PMBI Product List ([pmbi.co.in/ProductList.aspx](https://www.pmbi.co.in/ProductList.aspx)), full CSV export dated 16 September 2026, consistent in size (2,439 products) with the 2,110-medicine + 315-surgical basket the government reported as current to 31 December 2025 in a February 2026 Lok Sabha written reply (PIB annexure, static.pib.gov.in); this blog's own "India Cannot Sell ‘China-Free’ Medicine While Importing 43% of What's In It" and "India's ₹60,000 Crore API Push, Traced to Its Six Actual Schemes," whose PIB-sourced China-dependency and Bulk Drugs PLI figures are reused directly here, not re-derived; the Ciprofloxacin, Rifampicin and Ibuprofen FY23-24/FY24-25 figures corrected against and reused from this blog's own "Five Years and ₹25,000 Crore Later, China Still Supplies Three-Quarters of India's Drug-Making Ingredients," whose 90-line PIB China-import Annexure (PRID 2237414, 10 Mar 2026) is the primary source — this piece's first published version had a less precise Ciprofloxacin figure and reported Ibuprofen as unquantified, both corrected after a same-day archive cross-check; industry/trade-press commentary (of less certain primary-document backing, flagged accordingly) for the diclofenac figure. SKU-match counts were computed by case-insensitive substring search against the product list's Generic Name field and are reproducible against the source file. pmbi.co.in, janaushadhi.gov.in and the PIB annexure PDF could not be fetched directly from this session's network; the underlying product list was supplied directly by the reader.

### Related on this blog

See also: [India Cannot Sell “China-Free” Medicine While Importing 43% of What's In It](https://blog.vertistratsolution.com/2026/08/india-cannot-sell-china-free-medicine.html) · [Five Years and ₹25,000 Crore Later, China Still Supplies Three-Quarters of India's Drug-Making Ingredients](https://blog.vertistratsolution.com/2026/09/five-years-and-25000-crore-later-china.html) · [India's ₹60,000 Crore API Push, Traced to Its Six Actual Schemes](https://blog.vertistratsolution.com/2026/09/indias-60000-crore-api-push-traced-to.html) · [Ethanol Freed Up Refinery Capacity for Petrochemicals. The Pharma Chain Hasn't Seen Much of It Yet.](https://blog.vertistratsolution.com/2026/09/ethanol-freed-up-refinery-capacity-for.html).

Revision history.

- v1.1.0 — 16 September 2026 — corrected Ciprofloxacin (was 99.6%, now the more precise 97.98%→98.02% FY23-24/FY24-25) and Ibuprofen (was "not independently located," now 99.34%→80.73%, the sharpest single-year improvement in the dataset with no PLI behind it), and added a specific trend figure for Rifampicin (89.17%→89.01%) -- all against this blog's own "Five Years and ₹25,000 Crore Later" and its 90-line PIB Annexure, found via tools/research_crosscheck.py, the archive cross-check script added specifically to catch this failure mode.

- v1.0.0 — 16 September 2026 — first published.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]
