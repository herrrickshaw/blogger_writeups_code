# Were IEM filings with no Part B built anyway? A 40-filing web check (7 Oct 2026)

**Frame:** Part A filings dated 2017–2021 with no Part B found in DPIIT's lists to August 2024,
grouped by company and state: 4,724 pairs. **Sample:** 40 drawn at random (seed 20261007).
Two first draws were address fragments misread from the PDFs as company names and were
replaced by the next random draws (seed 7).

**Method:** for each, web searches for the CIN and MCA status (search-result snippets from
Zauba, Tofler, InstaFinancials and similar MCA mirrors), the company website, and news,
ratings releases, pollution-board papers or certifications about the stated product at the
stated district. Research agents did the searches; the classification and sources for each
row are in `iem_noB_sample_webcheck_2026-10-07.csv`. Rows are research leads, not verified facts.

| Classification | Filings | Share |
|---|---|---|
| Built: plant or product line at the filed location found operating | 19 | 48% |
| Announced or under construction, no production found | 4 | 10% |
| Dropped or moved elsewhere | 1 | 3% |
| Company active, nothing found on this project | 9 | 23% |
| Company not identified (often a firm, or a misread name) | 7 | 18% |

With 40 filings the 95% interval on the "built" share is roughly 33% to 63%. Several "built"
rows rest on weaker evidence (company and district match but the start date or product line
was not confirmed: Keihin FIE, Chanakya Bakery, Emami Agrotech, DCM Shriram, Speciality
Sintered), so the share with firm evidence is nearer a third.

25 of the 40 have a CIN visible in search results. Firms and LLPs (no CIN) are over-represented
among the "not found" rows.
