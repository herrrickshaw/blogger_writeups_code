# Solvents for polystyrene (PS / EPS "thermocol"): what else dissolves it

Prepared 10 October 2026. **Status: a reading of abstracts, patents, project pages and search
summaries, not of full texts.** OpenAlex (`api.openalex.org`) is blocked from this session, so there
are no citation counts. Numbers are leads to check against the source. Companion to
`limonene-eps-recycling-literature.md`.

Grades: **A** peer-reviewed (abstract seen), **B** patent or review, **C** press, vendor or project
page, **D** preprint, thesis or student/conference paper.

## 1. Bottom line

- **Limonene is one of many solvents that work; it is not the best-documented one.** The evidence
  points to three families: (a) terpenes and related natural oils (limonene, p-cymene, terpinene,
  phellandrene, eucalyptus and other essential oils), (b) "greener" synthetic solvents (dimethyl
  carbonate, ethyl acetate, isoamyl acetate, 1,3-dioxolane, glycol ethers), and (c) conventional
  hazardous solvents (toluene, benzene, THF, DMF, methylene chloride) that dissolve PS well but
  carry toxicity or food-contact baggage.
- **Dissolving is easy; getting a clean, reusable polymer and solvent back is the hard part.** Each
  route needs one of: distillation (heat, some chain degradation), an anti-solvent (ethanol,
  methanol, butanol, heptane) that must itself be recovered, or supercritical CO2.
- **The only solvent-based PS recycling at industrial scale found uses other solvents.** CreaSolv
  (Fraunhofer IVV, proprietary formulation, EPS with HBCD flame retardant) and Polystyvert
  (p-cymene with heptane anti-solvent, Canada).
- **Cyrene, gamma-valerolactone and ethyl lactate**: a search for these with EPS returned nothing.
  Not evidence they fail; evidence I did not find a study.

## 2. Comparison (as seen; sources in section 4)

| Solvent | What was seen | Recovery route | Concerns | Grade |
|---|---|---|---|---|
| d-Limonene | Dissolves EPS fast; volume cut reported at 96-98% (Colombian study, iGEM team) and about 100x (Brazilian thesis); no chain degradation claimed | Ethanol anti-solvent (96%); distillation | Flash point about 47 C, strong odour, high solvent use per unit EPS | D / B |
| p-Cymene | Dissolves PS better than limonene; 33% w/w at room temperature in Polystyvert patent | Steam distillation (Hattori); heptane anti-solvent (Polystyvert) | Petro- or pine-derived; scale-up cost unknown | A / B |
| Terpinene, phellandrene | Grouped with limonene and p-cymene as suitable, no polymer degradation (García 2009) | Distillation (some degradation reported elsewhere); supercritical CO2 proposed | Availability | A |
| Essential oils (commercial, unpurified) | Full dissolution at up to 1:1 by weight; at least 4x faster than limonene | Methanol precipitation; oil reused | One repository paper | D |
| Dimethyl carbonate (DMC) | Cube of EPS dissolves in about 45 s at room temperature (patent examples); DMC with butanol 68-75 s | Non-solvent precipitation, filtration, extrusion | Low boiling and flammable; patent figures self-reported | B |
| Isoamyl acetate, 1,3-dioxolane | Claimed to need lower distillation temperatures than limonene | Distillation | Dioxolane is volatile (bp about 76 C); patent only | B |
| Ethyl acetate | Used as a "biodegradable" solvent with ethanol, isopropanol or water as anti-solvents | Anti-solvent | Volume-reduction figures not seen | D |
| Acetone | EPS cup volume cut by up to 55% (Colombian study); a swelling/shrinking agent more than a full solvent | Evaporation | Highly flammable; partial effect | D |
| Toluene, benzene, xylene, THF, chloroform, methylene chloride | Good solvents; the benchmark | Distillation | Toxicity; restricts food-contact reuse; benzene carcinogenic | A / B |
| Ionic liquids | Dissolve PS to oligomer fractions at low energy (2025 review) | Not shown | Cost, scale, toxicity unclear | A (review) |
| Supercritical CO2 | Proposed for solvent removal and for XPS | Pressure release | Capital cost | A / B |

## 3. Picking a solvent: what the literature says matters

- **Hansen solubility parameters** are the standard screen (PS sphere centre roughly delta-v 18,
  delta-h 5 MPa^0.5, R0 about 5 in one 2-D source). They are a guide, not a guarantee; earlier
  work found them only about two-thirds to three-quarters accurate.
- **Boiling point sets the energy bill.** A solvent that boils low is easier to strip but riskier to
  store; a high-boiling one (limonene, 176 C) needs heat that degrades the polymer.
- **Anti-solvent versus distillation.** Anti-solvent precipitation avoids heat but adds a second
  solvent to separate and recycle.
- **Additives travel with the solution.** The reason CreaSolv exists is HBCD removal (reported
  above 99.7%, recyclate below 100 ppm). Thermocol packaging in India has no such flame-retardant
  problem in most cases, but insulation foam may.
- **Food-contact reuse** is the commercial prize and the regulatory obstacle: residual solvent
  limits apply and none of the sources report them for terpene routes.

## 4. Sources seen

- García et al. 2009, "Study of the solubility and stability of polystyrene wastes in a dissolution
  recycling process", Waste Management (A): https://pubmed.ncbi.nlm.nih.gov/19217275/
- Hattori et al., p-cymene and PS, Journal of Wood Science (A):
  https://jwoodscience.springeropen.com/counter/pdf/10.1007/s10086-009-1073-x.pdf
- US 7,728,047 (dimethyl carbonate and butanol) and US 7,745,503 (dialkyl carbonates) (B):
  https://patents.google.com/patent/US7728047 , https://patents.google.com/patent/US7745503
- US 12,162,991, FF Future / Brightplus, isoamyl acetate and 1,3-dioxolane (B):
  https://patents.google.com/patent/US12162991
- Polystyvert patents, e.g. US 11,407,878 (B): https://patents.justia.com/patent/20230002583
- US 6,403,661 and US 5,629,352 on limonene's drawbacks and glycol-ether alternatives (B):
  https://patents.google.com/patent/US5629352
- Fraunhofer IVV, PolyStyreneLoop / CreaSolv (C):
  https://www.ivv.fraunhofer.de/en/recycling-environment/recycling-of-contaminated-plastics/polystyreneloop.html
- 2025 review of green solvents (Springer) (A):
  https://link.springer.com/article/10.1007/s44371-025-00450-2
- Colombian EPS-volume studies (acetone; limonene) (D):
  https://revistas.unilibre.edu.co/index.php/avances/article/download/7420/7086/21779
- Brazilian limonene/ethanol work (D):
  https://revista.unifacear.edu.br/rem/article/download/566/555/1112
- Essential-oil EPS recycling, repository paper (D):
  https://ri.uaemex.mx/repositorio/handle/20.500.11799/99315
- USP ethyl acetate thesis (D): https://bdta.abcd.usp.br/directbitstream/d785b59e-ada1-49fb-95d8-22ac3df8acc8/AnaCarlaCezario%20-%20TF.pdf

## 5. Gaps and cautions

1. **PolyStyreneLoop's current status is unconfirmed.** The Terneuzen plant (3,300 t/yr) was reported
   opened in June 2021 with later plans for XPS; I found no 2024-2026 report either way.
2. **No head-to-head comparison.** The sources test different EPS grades, temperatures and
   loadings, so the volume-reduction figures above cannot be ranked against each other.
3. **No cost or LCA data** for any of the solvents beyond vendor claims.
4. **Cyrene, gamma-valerolactone, ethyl lactate:** no EPS studies found.
5. **Not tested here:** nothing in this note was reproduced. Dissolving PS in flammable solvents is
   a fire hazard; none of this is a bench protocol.
