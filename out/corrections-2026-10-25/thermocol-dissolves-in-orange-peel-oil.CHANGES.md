# CHANGES: thermocol-dissolves-in-orange-peel-oil (findings 20)

**Recommended title change: none.**

## Changes applied
1. **Hattori limonene figure: caveat added, figure NOT changed** ("Limonene is not the best terpene" section, paragraph after the chart). Inserted after "At that strength the solution is about two-thirds polymer.": a dated caveat that Table 2 of the InTech review chapter (https://doi.org/10.5772/59156, reproducing Hattori et al., Advances in Polymer Technology 2008, PS film Mn 1.2x10^5, 50 C; raw/20/intech.txt) lists p-cymene 212, **d-limonene 127**, other isomers 122-131, toluene 117 g per 100 g solvent, so 182-197 may be wrong, and that 127 g would make the solution about 56% polymer (127/227), not two-thirds. The post cites Hattori et al., J Wood Sci 2010 (a different paper; Springer blocked it), so the two may not be the same measurement. **Author to check the original paper.**
2. **Review chapter and "reused at least 10 times"**: the chapter was read in full and does not contain that claim (it says limonene recycling "has been realized in practical use with a semi-industrial scale"). Table row source cell "Secondary; not traced to a table" -> "Secondary; not found in the chapter's full text"; Sources note now says the statement was not found there on re-reading. The claim itself (table row and the "Solvent ageing" bullet) is unchanged.
3. **Noguchi note in Sources**: "parts 2 and 3 not seen" -> part 3 is a life-cycle assessment by the same authors (Packaging Technology and Science 11:39-44), so the post's "independent" cost/LCA wording remains accurate. Stat card ("0 independent ... studies") and the Section text were left unchanged.
4. **Ozeki, Ida and Osa**: Sources "(title only; paywalled)" -> abstract read (Polymer J. 2024/2025): d-limonene is a medium solvent for atactic polystyrene, between toluene and cyclohexane.
5. **OpenAlex remark** in Sources: "could not be reached" -> "later reachable for metadata checks, but no ... systematic search were run".
6. **Correction note** (inline-styled box copied from the post's own "Updated 12 October" box, as a `<p>`) before "Sources and caveats". No dateModified element.

## Not applied / flagged
- **182-197 g figure, chart bar and chart aria-label/text (inline SVG, not script)**: untouched as instructed. If the author decides 127 is correct, the following must change together: SVG aria-label ("limonene and isomers 182 to 197"), bar width/label for limonene, the "182 to 197 g" sentence, "about two-thirds polymer" (-> about 56%), and "p-cymene dissolved more than limonene" wording would still hold (212 > 127).
- Optional addition suggested by the findings, not made: qualify "quick and cold" (Section "What dissolves") with Ozeki's finding that limonene is only a *medium* solvent for polystyrene.
- Garcia et al. 2009 (0.26 g/mL, 25 C, extruded PS): unverified; unchanged. Also the "about a quarter polymer" arithmetic depends on it.
- IIT Hyderabad grant Rs 35.7 lakh: still unavailable; unchanged. 40.5 g/g and 77.3% only snippet-confirmed.
- CreaSolv/PolyStyreneLoop: insolvency March 2022 / restart June 2022 / 3,000 t/y regular operation (Plasteurope 19 Jun 2023) confirmed. The names "German EPS Converters", EUR 17 million and the 8,000 t target remain unconfirmed (paywalled); the post states them without hedge - author may want to hedge.
- Indian policy, EU risk assessment, IARC supply figure, 91.9% Nagpur limonene: not rechecked in the findings pass.
- Applied Sciences 2024 (alcohol anti-solvent solubility limit, doi 10.3390/app14177950) now identified; not added to the post.

## Verification
- diff vs original: 8 changed lines (`diff posts/thermocol-dissolves-in-orange-peel-oil.html out/corrections-2026-10-25/thermocol-dissolves-in-orange-peel-oil.html`); no CSS, script, Google Translate, AI-disclosure or gs-idx lines changed.
- tag counts (orig->new): <div 17->17; </div 17->17; <table 2->2; </table 2->2; <script 4->4; </script 4->4 (all unchanged).
- inline <script> blocks parsed with node: 2 blocks, ok, ok; script text identical to original.

## Revision 25 Oct 2026 (later the same day): Hattori figure settled, caveat replaced

The author supplied the InTech chapter (https://www.intechopen.com/chapters/47821, Hattori, "Recycling of
Expanded Polystyrene Using Natural Solvents", doi 10.5772/59156). Read in full, plus the 2010 paper itself:
Hattori, Shikata, Maekawa, Aoyama, "Dissolution of polystyrene into p-cymene and related substances in tree
leaf oils", J Wood Sci 56(2):169-171, doi 10.1007/s10086-009-1073-x. Full text taken from the Kitami Institute of
Technology repository (https://kitami-it.repo.nii.ac.jp/record/7532/files/Hattori_562.pdf); Springer's own
page returned a client challenge and was not retried.

- **The post's figures are correct.** 2010 paper, Table 1 (50 °C, mean ± SD, n=5): p-cymene 212.0, 2-p-cymenol
  156.7, (R)-limonene 181.7, α-terpinene 197.1, terpinolene 191.4, Abies leaf oil 84.7 g/100 g solvent. The chart
  values (212 / 182–197 / 157) match exactly.
- The chapter's Table 2 (d-limonene 127, isomers 122–131, p-cymene 212, 2-p-cymenol 105) cites its ref [10],
  an earlier study with a different polystyrene film (Mn 1.2×10^5). Both are at 50 °C; the difference is the
  polystyrene sample, not an error in the post.
- Changes: the "treat as unconfirmed" caveat is replaced by a "Checked" note giving Table 1 and explaining the
  127 g figure; chart caption "(abstract)" → "Table 1"; the visible correction note and the sources entry now cite
  the full paper.
- Unchanged: "reused at least 10 times" is still not in the chapter (its only recovery figure is 98% of geranyl
  acetate recovered by steam distillation), so that change stands.
