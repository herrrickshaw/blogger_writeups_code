# CHANGES: textbooks-say-project-returns-converge (findings 09)

Primary source used for all changes: Mauboussin and Callahan, "Competitive Advantage Period: The Neglected Value Driver", Counterpoint Global Insights, 14 April 2026. https://www.morganstanley.com/im/publication/insights/articles/article_theneglectedvaluedriver_ltr.pdf (read via Internet Archive copy; local copy raw/09/cap.pdf). Re-checked against raw/09/cap.txt: Exhibit 9 text (lines ~898-905), Exhibit 11 text (~1025), IPO sentence (~1317).

## HEADLINE ARGUMENT - AUTHOR PLEASE DECIDE
The "-0.8 pts, slightly negative, not converged" point holds only for TRADITIONAL ROIC. On ROIC adjusted for internally generated intangibles the paper gives average +1.9 pts (25th -4.7, 75th +6.2), and about half of firm-years above cost of capital. I kept the argument (wide, persistent dispersion; not a tight band at zero) but made the sign measure-dependent everywhere. If you prefer a firmer line, the whole "below cost of capital" framing could be dropped.

## Changes applied
1. Display H1 (and recommended Blogger TITLE): "...About 79% of the Gap Survives Each Year" -> "...About 79% of a Company's Edge Over Average Returns Survives Each Year". Why: 0.79 is persistence of deviation from average ROIC, not of the ROIC-CoC gap (Exhibit 11 / ROIC formula in paper). Recommended Blogger title: "Textbooks Say Project Returns Converge to Cost of Capital. About 79% of a Company's Edge Over Average Returns Survives Each Year".
2. Intro italic paragraph: "79% of any given return-over-cost-of-capital gap survives ... the average company's return has actually sat slightly below its cost of capital" -> "79% of a company's deviation from the average return on capital carries into the following year ... sat slightly below its cost of capital on the traditional measure (and slightly above it once internally generated intangibles are counted)". Source: Exhibit 9 and 11 text.
3. Short version bullet 2: "four-fifths of any given year's ROIC-CoC gap is still present" -> "four-fifths of a company's deviation from the average ROIC carries into the following year (an annual factor backed out of five-year ROIC correlations)". Source: Exhibit 11; paper says one-year correlations "overstate the fade rate" and recommends the five-year basis.
4. Short version bullet 3: "-0.8 pts" labelled "on traditional ROIC"; added adjusted-ROIC figures (+1.9; -4.7; +6.2) and the sentence that the sign depends on measurement. Source: Exhibit 9 text.
5. Section 2 para 1: same persistence reframing as (3).
6. Section 2 para 2: IPO cohort "stabilising at a new, lower level around year five" -> "stabilising around year five" (paper says "narrowed before stabilizing around year five"; no "lower level"). Added "using traditional ROIC" to the -0.8 figure, added adjusted figures and "about half of firm-year observations show an ROIC above the cost of capital". "a full 10 percentage points" -> "about 10 percentage points on either measure" (traditional IQR 10.0; adjusted 10.9).
7. Section 2 note: search-summary/blocked-fetch caveat replaced by the real citation (paper title, date, Exhibits 9 and 11).
8. Section 3 note: "reached via search-indexed summaries; direct fetch blocked" replaced by citation of "Measuring the Moat" (15 Oct 2024), read in full via Internet Archive; added that the paper treats the mechanisms across sections, not as one list. The blog's own inference (strong moats at low-fade end) caveat is kept.
9. Section 5: "-0.8-percentage-point historical average spread" qualified as traditional ROIC (+1.9 adjusted); "this summary of search-indexed excerpts" -> "this summary".
10. Sources and caveats: first part rewritten to cite both documents with link; the "blocked / search summaries" caveat removed. Damodaran caveat left untouched.
11. SVG chart (plain literals, no script): title now "(traditional ROIC)", subtitle adds "April 2026"; bar values/geometry unchanged (-4.3, -0.8, +5.7 are correct for traditional ROIC). Figcaption now cites the paper and gives the adjusted-ROIC figures.
12. Visible correction note (class gb-card, as a <p>) inserted directly before the "Sources and caveats" h2. No dateModified element exists in the post.

## Not applied
- None rejected. G3 (consumer/production advantage framing) CONFIRMED, only the caveat wording changed. The "patents" item and "strong-moat firms sit at low fade end" remain the blog's own inference (flagged in the post already; paper's Consumer Staples 0.90/0.10 is consistent but not a company-level test).

## Ripples checked
- 0.79 / 0.70-0.90 / 0.10-0.30 / ~0.21 confirmed exactly; no change to values.
- -0.8, -4.3, +5.7 occurrences: intro, bullet 3, section 2, section 5, chart, sources - all now qualified. No JS data arrays or stat cards in this post.
- Section 4 (India ICRA data) does not depend on the corrected figures.
- Post duplicates id="s1" (two headings); pre-existing, not touched.
- Related-sources suggestion from findings (Hirsch 2018; Gschwandtner; Damodaran) not added to avoid adding unrequested content.

## Verification
    ## diff stat
    27
     textbooks-say-project-returns-converge.html |   27 ++++++++++++++-------------
     1 file changed, 14 insertions(+), 13 deletions(-)
    <div orig=      10 new=      10
    </div orig=      10 new=      10
    <table orig=       0 new=       0
    </table orig=       0 new=       0
    <script orig=       4 new=       4
    </script orig=       4 new=       4
    scripts parsed: 2, failures: 0
