# NABET-accredited EIA consultants, 27 Nov 2026

Post: `out/post-nabet-accredited-eia-consultants-register.html` (built by `build.py`; arithmetic asserted in `calc.py`).

Data saved here: `nabet_aco_2026-11-27.csv` (256 organisations: name, ORG code, State parsed from the address, certificate, category, dates), `nabet_scope_2026-11-27.csv` (2,139 organisation-sector rows), `nabet_list_2022-02-14.csv` and `nabet_list_2022-05-09.csv` (NABET's List of ACOs, Rev. 19 and Rev. 23). Contact details were not kept.

Sources opened: NABET portal list, NABET list PDFs (2022), NABET scheme v3 and FAQs and "Reflections", EIA Notification consolidated text (para 13), CAG Report 39 of 2016 ch. 2 (Table 2.8), India Together 2013, Mint 2010, Delhi High Court 7 Nov 2013, NGT OA 137/2026 case note and order.

Not used: an NGT appeal rejoinder (Sep 2026) quoting an audit of "21 approvals" with non-accredited consultants (search excerpt only, audit not identified).

Parsing notes: 12 addresses assigned a State by hand (towns: Sangli, Madurai, Kashipur, Bhubaneswar x2, Kolhapur, Ankleshwar x2, Nashik, Bellary, Vapi, Hosapete). Entry 128 has no sector lines; entries 51 and 229 have no ORG code. Sector 26 is "Deleted" in the scheme.

Repeat before publishing: the portal list changes; rerun the fetch and calc.py (the asserts will fail loudly if counts move). No individual organisation is named in the post.
