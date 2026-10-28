"""Gazette check, 28 Oct 2026: resolve the reused S.O. numbers and unresolved rows in the right-of-user post."""
from g28 import load, rep, insert_note, save, SRC
S = "right-of-user-what-indias-pipeline"
t = load(S)
t = insert_note(t,
    "The notification-number problem this piece flagged is resolved. Read in the Gazette of India&rsquo;s own text (via the SansadSaar index of the archive.org Gazette of India collection), "
    "S.O. 4224(E) of 17 September 2025 (CG-DL-E-19092025-266249) is the section 3(1) notice, and S.O. 1303(E) of 11 March 2026 (CG-DL-E-13032026-270932) the section 6(1) declaration, "
    "for Reliance Ethane Pipeline Ltd&rsquo;s liquid-ethane line from Dahej to Parvat in Gujarat. No Cauvery Asset notice carries either number. "
    "S.O. numbers restart every calendar year, which is how the same number can point to two projects: S.O. 4224(E) of 30 July 2026 is a different notice, for the Barmer&ndash;Bhogat crude line of Vedanta and ONGC. "
    "The Cauvery Asset declaration for Kilakarai and Ramanathapuram taluks is for natural gas, not crude oil; it was published on 19 March 2026 (CG-DL-E-19032026-271072), following S.O. 4057(E) of 3 September 2025, though its own S.O. number is illegible in the scan. "
    "&ldquo;MSAE to MSNAA&rdquo; is an ONGC natural-gas pipeline in Krishna district, notified under section 3(1) by S.O. 1475(E) of 19 March 2026 (CG-DL-E-21032026-271162). "
    "The Mehsana&ndash;Bhatinda network and its spur to the HPCL Rajasthan refinery are GSPL India Gasnet Ltd&rsquo;s, not GAIL&rsquo;s (S.O. 5448(E), 25 November 2025, CG-DL-E-27112025-268030). "
    "The table and caveats below are corrected accordingly.")
rows = [
    ('<td>Srikakulam&ndash;Angul Gas Pipeline (spur)</td><td>Natural gas</td><td>GAIL</td><td>Srikakulam district</td><td>~19 Dec 2025</td>',
     '<td>Srikakulam&ndash;Angul Gas Pipeline (spur)</td><td>Natural gas</td><td>GAIL</td><td>Srikakulam district</td><td>~19 Dec 2025 (the 19 Dec 2025 notice found in the Gazette, S.O. 5909(E), covers Odisha; no Andhra Pradesh notice was found)</td>'),
    ('<td>Jerripotulapalem &amp; Narva villages, Pendurthi Mandal, Visakhapatnam Dist.</td><td>s.3(1), 17 Dec 2025</td>',
     '<td>Jerripotulapalem &amp; Narva villages, Pendurthi Mandal, Visakhapatnam Dist.</td><td>s.3(1), 17 Dec 2025, S.O. 5869(E)</td>'),
    ('<td>Unresolved ("MSAE to MSNAA")</td><td>Unresolved</td><td>Unresolved</td><td>Krishna District</td><td>s.3(1), ~23 Mar 2026</td>',
     '<td>ONGC gas lines ("MSAE to MSNAA")</td><td>Natural gas</td><td>ONGC</td><td>Krishna District</td><td>s.3(1), 19 Mar 2026, S.O. 1475(E)</td>'),
    ('<td>Mehsana&ndash;Bhatinda Network (+HRRL spurline)</td><td>Natural gas</td><td>GAIL</td><td>Mehsana origin</td><td>s.3(1), 25 Nov 2025</td>',
     '<td>Mehsana&ndash;Bhatinda Network (+HRRL spurline)</td><td>Natural gas</td><td>GSPL India Gasnet (GIGL)</td><td>Mehsana origin</td><td>s.3(1), 25 Nov 2025, S.O. 5448(E) (HRRL spur, Jalore to Barmer, Rajasthan)</td>'),
    ('<td>Dahej&ndash;Parvat / Dahej&ndash;Nagothane</td><td>Liquid ethane</td><td>Reliance (REPL)</td><td>Dahej origin</td><td>~17 Sep 2025 / ~11 Mar 2026 (numbers unconfirmed &mdash; see caveat)</td>',
     '<td>Dahej&ndash;Parvat / Dahej&ndash;Nagothane</td><td>Liquid ethane</td><td>Reliance (REPL)</td><td>Dahej origin</td><td>Dahej&ndash;Parvat: s.3(1) 17 Sep 2025, S.O. 4224(E); s.6(1) 11 Mar 2026, S.O. 1303(E) (confirmed in the Gazette)</td>'),
    ('<td>Punjab</td><td>Mehsana&ndash;Bhatinda Network</td><td>Natural gas</td><td>GAIL</td>',
     '<td>Punjab</td><td>Mehsana&ndash;Bhatinda Network</td><td>Natural gas</td><td>GSPL India Gasnet (GIGL)</td>'),
    ('<td>Rajasthan</td><td>Mehsana&ndash;Bhatinda Network</td><td>Natural gas</td><td>GAIL</td>',
     '<td>Rajasthan</td><td>Mehsana&ndash;Bhatinda Network</td><td>Natural gas</td><td>GSPL India Gasnet (GIGL)</td>'),
    ('<td>Odisha</td><td>Srikakulam&ndash;Angul Gas Pipeline</td><td>Natural gas</td><td>GAIL</td><td>multiple districts</td><td>~19 Dec 2025</td>',
     '<td>Odisha</td><td>Srikakulam&ndash;Angul Gas Pipeline</td><td>Natural gas</td><td>GAIL</td><td>multiple districts</td><td>s.3(1) 4 Dec 2025, S.O. 5703(E); 19 Dec 2025, S.O. 5909(E)</td>'),
    ('<td>Cauvery Asset Projects</td><td>Crude oil/associated</td><td>ONGC</td><td>Kilakarai &amp; Ramanathapuram taluks, Ramanathapuram Dist.</td><td>s.6(1), ~21 Mar 2026 (S.O. number unconfirmed &mdash; see caveat)</td>',
     '<td>Cauvery Asset Projects</td><td>Natural gas</td><td>ONGC</td><td>Kilakarai &amp; Ramanathapuram taluks, Ramanathapuram Dist.</td><td>s.6(1), published 19 Mar 2026 (S.O. number illegible in the Gazette scan); s.3(1) S.O. 4057(E), 3 Sep 2025</td>'),
]
for a, b in rows:
    t = rep(t, a, b)
t = rep(t, "This piece also caught its own search tooling reusing the same two notification numbers for two unrelated pipelines in different searches, which is disclosed in full in &sect;5 and &sect;6 rather than smoothed over.",
        "This piece also caught its own search tooling reusing the same two notification numbers for two unrelated pipelines in different searches; a check against the Gazette&rsquo;s own text on 28 October 2026 resolved both to the Reliance ethane line (see the note above).")
t = rep(t, "first, this piece's own search tooling reused the identical notification numbers &mdash; S.O. 1303(E) and S.O. 4224(E) &mdash; for two unrelated projects (a Liquid Ethane pipeline in Gujarat/Maharashtra, and the Cauvery Asset Projects in Tamil Nadu) across different search passes; two of three mentions pointed to the ethane pipeline, so that is what is reported below, but neither attribution should be treated as confirmed.",
        "first, this piece's own search tooling reused the identical notification numbers &mdash; S.O. 1303(E) and S.O. 4224(E) &mdash; for two unrelated projects (a Liquid Ethane pipeline in Gujarat/Maharashtra, and the Cauvery Asset Projects in Tamil Nadu) across different search passes; the Gazette&rsquo;s own text, checked on 28 October 2026, shows both belong to Reliance&rsquo;s Dahej&ndash;Parvat ethane line.")
t = rep(t, 'Second, at least one project below ("MSAE to MSNAA", Krishna District, Andhra Pradesh) could not be resolved to a named pipeline, operator, or fluid type at all, and is included only because it was independently findable, not because it is understood.',
        'Second, one project below ("MSAE to MSNAA", Krishna District, Andhra Pradesh) could not at first be resolved; the Gazette shows it is an ONGC natural-gas pipeline (S.O. 1475(E), 19 March 2026).')
t = rep(t, "Nothing in &sect;5 is a verbatim read of a gazette notification; all of it is WebSearch's own summarisation of how secondary sources describe these notifications, which is why this piece surfaced and disclosed a specific case of the search tooling reusing the same notification numbers (S.O. 1303(E), S.O. 4224(E)) across two unrelated pipelines rather than treating either attribution as safe to publish without that flag.",
        "&sect;5 was first built from WebSearch&rsquo;s summaries of how secondary sources describe these notifications. On 28 October 2026 its S.O. numbers, operators and fluids were checked against the Gazette&rsquo;s own text through the SansadSaar index of the archive.org Gazette of India collection: the reused numbers S.O. 1303(E) and S.O. 4224(E) both belong to the Reliance ethane line, the Cauvery Asset row was corrected to natural gas, the Krishna district row was identified, and the Mehsana&ndash;Bhatinda operator was corrected to GSPL India Gasnet. Rows without a number were not all checked.")
save(S, t)
