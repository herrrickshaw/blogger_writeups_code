# Sugarcane bagasse: liquefaction and hydrolysis, what the literature says

Prepared 10 October 2026. **Status: a reading of abstracts, patents and search summaries, not of
full texts.** `api.openalex.org` and `www.sciencedirect.com` both return a proxy 403 from this
session (checked again on request, no key in the environment), so there are no citation counts and
no ScienceDirect full texts. ScienceDirect abstracts appeared through web search only. Every figure
is tagged with where it was seen. Treat the numbers as leads to check against the paper.

Grades: **A** peer-reviewed (abstract seen), **B** patent or review, **C** press/vendor/project
page, **D** preprint, thesis, conference or regional paper.

## 1. Bottom line

- **"Liquefaction" means three different things, and the products differ.** (a) Solvolytic
  liquefaction in a polyol (PEG, glycerol, polyhydric alcohol) with an acid catalyst gives a
  hydroxyl-rich liquid that can replace part of the polyol in rigid polyurethane foam. (b)
  Hydrothermal liquefaction (water or water/alcohol, 300-320 C, often a base catalyst) gives a
  bio-crude. (c) Dissolving only the lignin gives a phenol substitute for adhesives. **Hydrolysis**
  (acid or enzymes) is a different aim: release sugars (glucose, xylose) for ethanol, xylitol,
  furfural or levulinic acid.
- **The lab results are real and consistent in direction, but small and not comparable.** Studies
  report mg/g, g/100 g, mol% and % conversion; feedstock, solids loading, enzyme dose and
  pretreatment all differ. No head-to-head on one bagasse exists in what I found.
- **Hydrolysis yield is set mostly by pretreatment, then variety, enzyme dose and solids.** One
  115-variety study found combined sugar yield after pretreatment and enzymes ranging from 27.3 to
  55.2 g per 100 g dry matter (ScienceDirect abstract).
- **For liquefaction to polyols, the closest paper is Xie et al. 2015 (Materials, open access):**
  almost 75% of bagasse flour converted to liquid in 9 min at 150 C (microwave, polyhydric alcohol
  and phosphoric acid, bagasse:solvent 1/4). I could see only the abstract. Foam compressive
  strength and viscosity values were not in what I saw.
- **No techno-economic or life-cycle study of a bagasse polyol or foam was found.** A 2018 LCA of
  bagasse valorisation routes (Waste and Biomass Valorization, NCL library record) exists but I
  could not see its content.
- **India angle:** bagasse is already at the mill gate and is burned for cogeneration, so the
  question is not collection (the 2G stubble problem) but displacement of boiler fuel. No Indian
  bagasse-polyol or bagasse-liquefaction work turned up.

## 2. What was found, graded

### Composition and recalcitrance
| Claim | Source seen | Grade |
|---|---|---|
| Raw bagasse about 40.4% cellulose, 23.8% hemicellulose, 27.2% lignin, 3.0% ash, 4.4% extractives | A Brazilian/regional paper (search summary; one sample) | D |
| Lignin drives recalcitrance; dilute acid releases xylose from hemicellulose and leaves most lignin and cellulose | Dilute-acid studies (search summaries) | A/D |
| 4% acid vs 0.5% acid: xylose release similar though hemicellulose reduced almost 80%; inhibitors about five times higher | Brazilian paper (search summary) | D |
| Detoxifying hydrothermal hydrolysate raised fermentation efficiency 12.7%; no significant gain for acid hydrolysate | same | D |

### Hydrolysis yields (not comparable across rows)
| Pretreatment / route | Result as reported | Grade |
|---|---|---|
| 115 cane varieties, pretreatment + enzymes | 27.3-55.2 g sugar per 100 g DM | A |
| Dilute acid then enzymes | max total reducing sugar 282.85 mg/g (10 FPU, 50 C, 48 h); a comparison table in the same paper lists acid-only pretreatment up to 487.5 mg/g (0.1-0.9 M H2SO4, 80-120 C) | A |
| KOH | total sugar yield up to 81.6% (5% solids, 20 FPU/g) | A |
| NaOH | cellulose conversion 85.33%; 443.52 mg reducing sugar per g bagasse (18 FPU/g, 64 h, 1:30) | A |
| FeCl3 + surfactant | glucose 42.2 g/100 g raw, stated as 93.8% of the glucose | A |
| Lime | glucose 256, 320, 384 mg/g after 72 h depending on pretreatment time | A |
| Ten deep eutectic solvents vs alkali, acid, ionic liquid | ChCl:lactic acid removed 50.6% of lignin (dilute alkali 59.7%) and gave 90.4% sugar yield; [BMIM][OAc] 98.0% | A |
| Liquid hot water + DES | 85.05 g/L fermentable sugar (glucose 60.96, xylose 24.09) | A |
| Protic ionic liquid [TEA][HSO4] | glucose about 75% of that from [Emim][OAc]; reported 40 times cheaper | A |
| Subcritical water (conference) | optimum 169.66 C, 19.41 min, 1:6.85 bagasse:water; no yield seen | D |
| Sulfuric acid + glycerol pretreatment | cellulose recovery over 97% at low acid and high glycerol | A/D |

### Platform chemicals from hydrolysate
- Xylose yield 82% with a sulfonated resin, then hydrogenation to xylitol at 100% selectivity (CICEQ 2023, A/D).
- Xylitol by fermentation 54.42% after a threefold concentration (Frontiers in Nutrition 2022, A).
- Methanesulfonic acid on soda-pretreated bagasse: about 75 mol% levulinic acid and 85 mol% furfural; a model biorefinery from the same group: about 190 kg levulinic acid, 89 kg formic acid, 40 kg furfural per tonne dry bagasse (RSC Advances 2016, A).
- Furfural formation lowers xylose selectivity; high furfural and high levulinic yields conflict in acid systems (IJOGCT 2017, A/D).

### Liquefaction to polyols and foam
| Claim | Source seen | Grade |
|---|---|---|
| About 75% of bagasse flour liquefied in 9 min at 150 C, bagasse:solvent 1/4, polyhydric alcohol + phosphoric acid, microwave; higher temperature and low bagasse:solvent ratio gave low hydroxyl number; foams from higher-temperature liquefaction performed better | Xie et al., Materials 8, 2015 (abstract) | A |
| PEG 400/glycerol with H2SO4 at 140-180 C: hemicellulose most reactive, then lignin, then cellulose; residue ash rises (re-condensation); activation energies 30.51 (lignin), 72.83 (cellulose), 67.09 (bagasse) kJ/mol | Springer, 2020 (search summary) | A |
| Rigid PU foam: bagasse polyol replacing commercial PEG polyol raised density and compressive strength; above 30% replacement surface heterogeneous; thermal conductivity fell 0.035 to 0.029 | ScienceDirect (search summary) | A |
| HTL bio-oil with glycerol co-solvent in foam: higher replacement lowered first-stage thermal stability, raised second | ScienceDirect 2022 (search summary) | A |
| Bagasse as filler in flexible PU foam: elongation at break fell | RSC Advances 2024 (search summary) | A |
| Biomass sources lowered compressive strength vs control; higher-hydroxyl biomass gave better foam | BioResources 2020, several biomasses (search summary) | A |
| **Cassava bagasse (not sugarcane)**: replacing 20% to 100% of polyether polyol cut compressive strength 0.171 to 0.057 MPa | search summary | D |

### Hydrothermal liquefaction (bio-crude)
- KOH, methanol co-solvent, 320 C, 15 min, 10 wt%: 36.3 wt% bio-crude (IIT Madras record, D/A).
- About 36% bio-oil from sugarcane bagasse and straw at milder conditions (search summary; the source contradicts itself on catalyst effect).
- **Sorghum bagasse**, not sugarcane: 61.8% with K2CO3 at 300 C. Co-liquefaction with soybean oil about 95 wt%, inflated by the lipid. Do not quote these as sugarcane bagasse yields.

### Lignin to adhesive
- Bagasse lignin substituting up to 30% of phenol in PF resin gave plywood meeting interior-grade standards (Industrial Crops and Products 2013, A).
- Bagasse pyrolysis bio-oil: up to 20% substitution comparable to a Chinese standard PF resin (A/D).
- Liquefied wood to carbon fibre exists (Douglas fir, phenol/H2SO4, melt-spun, carbonised at 900 C) but was not shown for bagasse.

## 3. Where the literature is thin
1. No techno-economics or LCA for bagasse polyol, foam or sugar-platform routes found.
2. Residue and mass balance: about a quarter of bagasse is not liquefied in the best case I saw; what happens to that residue and to the re-condensed ash/lignin is not reported in the abstracts.
3. Foam properties: compressive strength, density and thermal values for bagasse-polyol foam were not recoverable from abstracts; the one numeric strength drop I found is cassava.
4. Enzyme cost, solids loading above 5-10%, and inhibitor handling are the usual commercial barriers for hydrolysis; none of the sources priced them.
5. No India-specific bagasse liquefaction or hydrolysis work found (searched ICAR, National Sugar Institute, IIT). Praj and ICT Mumbai 2G work treats bagasse as one of several residues.
6. Bagasse already has uses: boiler fuel, paper (TNPL), 2G ethanol. Any new route has to beat the boiler.

## 4. India context (from this blog's earlier posts and search)
- About 527 sugar mills and roughly 80 million tonnes of wet bagasse a year (about 50% moisture), from Waste Management World coverage (secondary); paper's share ranges from 5 to 24 million tonnes in sources the blog could not reconcile.
- Bagasse cogeneration 9,806 MW at 31 December 2024 (Powerline, citing MNRE); combined bagasse-and-biomass cogeneration about 11,748 MW at 31 July 2026 (blog's MNRE-sourced figure). Different dates and scope; not additive.
- 2G ethanol: six of twelve PM JI-VAN plants sanctioned, two operational; Panipat's failure is a stubble-logistics one. Bagasse has no collection problem, so it tests a different question.

## 5. Next steps
- Run `tools/openalex_batch.py out/research/bagasse_openalex_queries.txt` on the Mac with your key (`export OPENALEX_API_KEY=...`).
- Read in full: Xie et al. 2015 (open access, PMC5458812), the 2022 bagasse HTL-polyol foam paper, and the 115-variety paper.
- Search for a bagasse-polyol techno-economic study and for any Indian pilot.
