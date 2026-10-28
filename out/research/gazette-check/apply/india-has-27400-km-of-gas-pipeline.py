"""Gazette check, 28 Oct 2026: right-of-user S.O. numbers in the pipeline-map post."""
from g28 import load, rep, insert_note, save, SRC
S = "india-has-27400-km-of-gas-pipeline"
t = load(S)
t = insert_note(t,
    "The right-of-user notices in the table below were checked against the Gazette of India&rsquo;s own text, " + SRC.replace("read in the Gazette of India&rsquo;s own text ", "") + ". "
    "Two S.O. numbers were wrong and are corrected: the 31 July 2025 section 3(1) notice for Silchar&ndash;Panisagar in Assam is S.O. 3577(E), not 3574(E) "
    "(S.O. 3574(E) of the same date is the Panisagar&ndash;Aizawl section in Mizoram), and the 14 January 2026 section 6(1) declaration for Visakh&ndash;Raipur in Odisha is S.O. 221(E), not 5079(E). "
    "Seven more rows now carry Gazette numbers, and Srikakulam&ndash;Angul (5703(E)), the Silchar city-gas spur (3223(E)), Mundra&ndash;Pachpadra (2247(E)) and Dahej&ndash;Parvat (1303(E)) match. "
    "S.O. 5085(E), 2993(E) and 3755(E) could not be found in the index, which does not hold every Gazette issue, so they stay as reported.")
rows = [
    ("<td>s.3(1) and s.6(1), 2026</td><td>—</td>", "<td>s.3(1) 16 Dec 2025; s.6(1) 4 May 2026</td><td>5834(E); 2240(E)</td>"),
    ("<td>3755(E) (2024 s.3(1))</td>", "<td>3755(E) (2024 s.3(1), as reported); 5855(E) (s.6(1), 16 Dec 2025, MP)</td>"),
    ("<td>s.3(1) 31 Jul 2025; s.6(1) Dec 2025</td><td>3574(E)</td>", "<td>s.3(1) 31 Jul 2025; s.6(1) Dec 2025</td><td>3577(E) (corrected from 3574(E))</td>"),
    ("<td>5085(E); 2993(E)</td>", "<td>5085(E); 2993(E) (as reported; not found in the Gazette index); s.3(1) Mizoram 31 Jul 2025: 3574(E)</td>"),
    ("<td>s.3(1) Mar and Jun 2026</td><td>—</td>", "<td>s.3(1) Mar and Jun 2026</td><td>3229(E); 3279(E) (June)</td>"),
    ("<td>s.3(1) Nov 2025; s.6(1) Dec 2025</td><td>—</td>", "<td>s.3(1) 25 Nov 2025; s.6(1) Dec 2025</td><td>5448(E) (s.3(1))</td>"),
    ("<td>s.6(1) 14 Jan 2026 (Odisha)</td><td>5079(E)</td>", "<td>s.6(1) 14 Jan 2026 (Odisha)</td><td>221(E) (corrected from 5079(E))</td>"),
    ("<td>s.6(1) 15 Dec 2025</td><td>—</td>", "<td>s.6(1) 15 Dec 2025</td><td>5826(E)</td>"),
    ("<td>s.3(1) 2026</td><td>—</td>", "<td>s.3(1) Apr and Aug 2026</td><td>1832(E)&ndash;1834(E); 4588(E)&ndash;4590(E)</td>"),
]
for a, b in rows:
    t = rep(t, a, b)
t = rep(t, "<th>S.O. as reported</th>", "<th>S.O. (checked against the Gazette, 28 Oct 2026)</th>")
t = rep(t, "Every entry was found through search-result summaries of the Gazette or of legal-notice sites; the Gazette itself could not be opened from this blog&rsquo;s research environment.",
        "Every entry was first found through search-result summaries of the Gazette or of legal-notice sites; on 28 October 2026 the S.O. numbers were checked against the Gazette&rsquo;s own text through the SansadSaar index of the archive.org Gazette of India collection, and two were corrected. Three numbers that index does not hold are marked as reported.")
t = rep(t, "The Gazette entries were found through search summaries, not read in the Gazette.",
        "The Gazette entries were found through search summaries and then checked against the Gazette&rsquo;s own text where the SansadSaar index holds the notice; three were not found there.")
t = rep(t, "the Gazette PDFs were not opened.",
        "S.O. numbers checked on 28 October 2026 against the Gazette&rsquo;s own text via the SansadSaar index of the archive.org Gazette of India collection (for example CG-DL-E-06082025-265243 for S.O. 3577(E), CG-DL-E-17012026-269419 for S.O. 221(E), CG-DL-E-13122025-268474 for S.O. 5703(E)).")
save(S, t)
