"""BHAVYA post: checked against the scheme notification, Gazette of India CG-DL-E-10042026-271698."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from g28 import load, rep, insert_note, save

S = "india-will-spend-rs-33660-crore-on"
t = load(S)
t = rep(t, "<td>Union Cabinet, 18 March 2026; notified 10 April 2026</td>",
        "<td>Union Cabinet, 18 March 2026; notified by DPIIT on 10 April 2026 (F. No. P-32026/2/2024-MIITUS, Gazette of India Extraordinary CG-DL-E-10042026-271698)</td>")
t = rep(t, "<td>100 to 1,000 acres; from 25 acres in hill and north-eastern states, union territories and small states; greenfield or eligible brownfield</td>",
        "<td>At least 100 contiguous acres; at least 25 acres in hill states, the North-East, union territories and states with under one crore people; up to 20 of the 100 parks may be 500&ndash;1,000 acres, the rest under 500; brownfield case by case; at least 90% of the land must be encumbrance-free before approval</td>")
t = rep(t, "<td>Up to Rs 1 crore an acre for core, value-added and social infrastructure (such as worker housing); up to 25% of support may go to external links such as roads and rail</td>",
        "<td>Up to Rs 1 crore an acre, as equity through NICDIT in three milestone-linked tranches over three years, for core, value-added, social and external infrastructure; up to 25% of a park&rsquo;s funding may go to external connectivity, where the Centre pays no more than 25% of the cost and the state the rest; private-developer parks get the lower of Rs 50 lakh an acre or 50% of infrastructure cost</td>")
t = rep(t, "<td>National Industrial Corridor Development Corporation (NICDC) with states and private developers</td>",
        "<td>A special purpose vehicle of the National Industrial Corridor Development and Implementation Trust (NICDIT) and the state&rsquo;s nodal agency, which owns the land and assets; with a private developer, a three-way joint venture in which the developer may keep up to 25% of developed land. NICDC is the project management agency</td>")
t = rep(t, "The industrial corridor programme, which BHAVYA&rsquo;s implementer NICDC also runs,",
        "The industrial corridor programme, run by NICDC, which is BHAVYA&rsquo;s project management agency,")
t = rep(t, "<p>The Cabinet release, the scheme guidelines and the land bank&rsquo;s pages could not be opened directly; figures come from their text as indexed by search engines and from news reports.",
        "<p>The scheme notification of 10 April 2026 was read in the Gazette of India&rsquo;s own text (CG-DL-E-10042026-271698, via the SansadSaar index of the archive.org Gazette of India collection); the scheme-design rows above follow it. The notification does not state the 34,000-acre or 15-lakh-jobs targets, which come from the Cabinet release as reported, or the round dates, which come from the operational guidelines as reported; the Cabinet release, the guidelines and the land bank&rsquo;s pages could not be opened directly.")
t = rep(t, "notification date 10 April 2026 and scheme details per PIB-based summaries;",
        "scheme notification: DPIIT, F. No. P-32026/2/2024-MIITUS, 10 April 2026, Gazette of India Extraordinary Part I Section 1, CG-DL-E-10042026-271698 (egazette.gov.in/WriteReadData/2026/271698.pdf), read via the SansadSaar index of the archive.org Gazette of India collection;")
t = insert_note(t, "The scheme table was checked against the BHAVYA notification in the Gazette of India (DPIIT, 10 April 2026, CG-DL-E-10042026-271698). "
                   "Outlay, period, the 100 parks and the 50 in phase one, and the Rs 1 crore an acre are confirmed. Three rows were corrected or filled in: parks need at least 100 acres (25 in hill, North-Eastern and small states) and only up to 20 may be 500&ndash;1,000 acres; "
                   "funding is equity through NICDIT in three tranches, with a lower Rs 50 lakh an acre for private-developer parks; and parks are built by NICDIT-state SPVs, with NICDC as project management agency, not as builder.")
save(S, t)
