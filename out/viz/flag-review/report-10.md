# Flag review, chunk 10

## annexure-314-hsn-codes-mapped-to

**Verdict: NOT-AN-ERROR.** The "Textil" truncation is not in the post or the edition.

**Evidence**
- Source of truth is `posts/annexure-314-hsn-codes-mapped-to.html`. No `out/update-*` file exists for this slug.
- The post heading for the Specialty Fibres segment is complete: "Specialty Fibres & Composites (31 codes, 27 confirmed under M/o Textiles)". All 13 segment headings in the post end in "confirmed under M/o Textiles)".
- The only place the string is cut is `out/viz/annexure-314-hsn-codes-mapped-to/outline.md` line 265. The outline tool clipped the label at 64 characters: `[T12 "Specialty Fibres & Composites (31 codes, 27 confirmed under M/o Textil" 31 rows; ...]`.
  - It is the only T-label long enough to be clipped; the other 12 are complete.
  - `outline.md` is an intermediate prompt file, not reader-facing.
- `spec.json` and `edition.html` do not use T12. `spec.json` references only table T2, and "Textil" never appears there as a truncated word. The edition shows "confirmed under M/o Textiles)" in full.
- Segment counts reconcile (python on the post text): 15+118+12+5+14+23+10+11+8+34+22+31+11 = 314. Confirmed counts 15+101+11+5+13+17+5+10+8+22+18+27+9 = 261. 314-261 = 53, which matches the post and spec ("261 of 314", "53 under other ministries").
- The spec's derived figures also hold: 34+31+23+22 = 110, 118-101 = 17, 34-22 = 12, and 17+12 = 29.

**Proposed fix:** none for the post or edition. Optionally, the outline generator could use a longer label cap (a pipeline matter, not a content error).
