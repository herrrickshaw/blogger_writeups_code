"""Gazette check, 28 Oct 2026: Petroleum and Natural Gas Rules, 2025 (G.S.R. 888(E)) and Oilfields Amendment Act, 2025."""
from g28 import load, rep, insert_note, save, SRC
S = "india-let-oil-companies-put-solar-on"
t = load(S)
t = insert_note(t,
    "The Petroleum and Natural Gas Rules, 2025 have now been " + SRC + ": G.S.R. 888(E), dated 9 December 2025 (CG-DL-E-11122025-268409), in force from publication, "
    "replacing the Petroleum Concession Rules, 1949 and the Petroleum and Natural Gas Rules, 1959. One correction: the chapter on &ldquo;Environment Protection, Decarbonisation, Monitoring of Greenhouse Gas Emissions and Flared Gas&rdquo; "
    "is Chapter VII, not Chapter VIII; Chapter VIII covers sharing of infrastructure. Its content is as described: environmental protection, flared-gas reporting each quarter, and site restoration backed by a site restoration fund. "
    "The Rules also list among a lessee&rsquo;s rights &ldquo;to explore, plan, develop, and establish comprehensive energy projects in the oilfield&rdquo; and to use the oilfield for decarbonisation, "
    "with a separate surface lease needed for land actually used. The Oilfields (Regulation and Development) Amendment Act, 2025 is confirmed as Act No. 6 of 2025, assented to on 28 March 2025 (CG-DL-E-28032025-262080).")
t = rep(t, "That rulebook's Chapter VIII &mdash;", "That rulebook's Chapter VII &mdash;")
t = rep(t, "The Petroleum and Natural Gas Rules, 2025, and its Chapter VIII on environment protection, decarbonisation, GHG monitoring and site-restoration funds, are corroborated across current-affairs and legal-explainer coverage (Insights on India, C4S Courses) of the draft and final rules; this piece did not independently fetch the rules' full gazette text.",
        "The Petroleum and Natural Gas Rules, 2025 (G.S.R. 888(E), 9 December 2025, Gazette of India Extraordinary CG-DL-E-11122025-268409) and its Chapter VII on environment protection, decarbonisation, GHG monitoring and site-restoration funds were read in the Gazette&rsquo;s own text on 28 October 2026, through the SansadSaar index of the archive.org Gazette of India collection; earlier versions of this piece relied on current-affairs and legal-explainer coverage (Insights on India, C4S Courses) and called it Chapter VIII.")
t = rep(t, "Gazette of India notification of Act No. 6 of 2025 (egazette.gov.in)", "Gazette of India notification of Act No. 6 of 2025 (egazette.gov.in; CG-DL-E-28032025-262080)")
save(S, t)
