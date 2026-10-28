"""SHANTI post: checked against the Act's gazette text, Act No. 39 of 2025, CG-DL-E-21122025-268697."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from g28 import load, rep, insert_note, save

S = "india-ended-63-years-of-state-nuclear"
t = load(S)
t = rep(t, "and given presidential assent on 20 December, taking effect the next day.",
        "and given presidential assent on 20 December; it was published in the Gazette of India on 21 December as Act No. 39 of 2025. Its section 1(2) brings it into force on dates the Centre notifies, and may set different dates for different provisions.")
t = rep(t, 'The new Act opens specified licensed activities to "any other company, except a company incorporated outside India," and to government&ndash;private joint ventures',
        'The new Act (section 3(1)) lets government departments, government companies, &ldquo;any other company&rdquo; and joint ventures among them apply for licences, and defines &ldquo;company&rdquo; to exclude one incorporated outside India (section 2(9))')
t = rep(t, 'are now open to private entities up to a threshold value the government has yet to set, though the Act keeps unspecified "activities of a sensitive nature" under exclusive government control.',
        'are now open to licensees up to a threshold value the government has yet to notify (section 3(2)(b)). Section 3(5) reserves to the Centre or wholly owned bodies the enrichment or isotopic separation of prescribed substances unless notified otherwise, the management of spent fuel including reprocessing, heavy-water production, and anything else the Centre notifies.')
t = rep(t, "The Act&rsquo;s gazetted text was not read for this note.",
        "The Act&rsquo;s gazetted text has since been read (28 October 2026): section 6 gives the operator a right of recourse only where a written contract provides it or the incident results from an act or omission intended to cause nuclear damage.")
t = rep(t, "Licensing mechanics, the foreign-incorporation exclusion, AERB's new statutory status and the fuel-cycle provisions per Law.asia, the Bulletin of the Atomic Scientists, and Mondaq legal analysis of the Act's text.",
        "Licensing mechanics, the foreign-incorporation exclusion, AERB's new statutory status, the fuel-cycle provisions, the right of recourse and the repeal of the 1962 and 2010 Acts checked against the Act itself: The Sustainable Harnessing and Advancement of Nuclear Energy for Transforming India Act, 2025 (No. 39 of 2025), Gazette of India Extraordinary Part II Section 1, 21 December 2025, CG-DL-E-21122025-268697 (egazette.gov.in/WriteReadData/2025/268697.pdf), and its corrigenda of 8 January 2026 (CG-DL-E-08012026-269213), read via the SansadSaar index of the archive.org Gazette of India collection; also Law.asia, the Bulletin of the Atomic Scientists and Mondaq.")
t = insert_note(t, "Checked against the Act in the Gazette of India (Act No. 39 of 2025, assented 20 December 2025, published 21 December, CG-DL-E-21122025-268697). "
                   "Confirmed: the licensing of &ldquo;any other company&rdquo; and joint ventures, with foreign-incorporated companies excluded by definition; AERB&rsquo;s statutory footing (section 7); the fuel-cycle threshold (section 3(2)(b)); recourse only by written contract or intentional act (section 6); and the repeal of the 1962 and 2010 Acts (section 91). "
                   "Corrected: the Act does not hold back unspecified &ldquo;activities of a sensitive nature&rdquo;; section 3(5) lists the activities reserved to the government. "
                   "Not confirmed: the Act comes into force on dates the Centre notifies (section 1(2)); this blog did not find that notification in the Gazette index up to February 2026, so the &ldquo;21 December 2025&rdquo; start date used below is as reported, not as notified. The draft SHANTI Rules were not found in the Gazette index either.")
save(S, t)
