from _b4 import load, rep, insert_note, save, SRC
S = "indias-first-seabed-mineral-auction"
G = "Ministry of Mines (Administering Authority) notification of 21 September 2026 under section 10 of the Offshore Areas Mineral (Development and Regulation) Act, 2002 (Gazette of India Extraordinary CG-DL-E-22092026-276390)"
t = load(S)
t = rep(t, "gazette notifications of 21 and 24 September 2026 as reported by PSU Watch and Swarajya;",
    "the " + G + ", read in the Gazette&rsquo;s text; the 24 September 2026 rule change as reported by PSU Watch and Swarajya;")
t = rep(t, "The nodule offer has been consolidated into two larger blocks, notified in the gazette on 21 September.",
    "The nodule offer has been consolidated into two larger blocks, notified in the gazette on 21 September: West Sewell Ridge-01, 1,000 sq km, and Sewell Rise-01, 632 sq km, both declared available for composite licences for polymetallic nodules and crusts.")
t = rep(t, "PIB and gazette pages could not be opened from this blog&rsquo;s tools, so details are from coverage: block sizes, gazette dates and the rule change from PSU Watch, Swarajya and Business Standard;",
    "The block notification (" + G + ", egazette.gov.in/WriteReadData/2026/276390.pdf) was read in the Gazette&rsquo;s own text through " + SRC + "; the scan&rsquo;s S.O. number is not fully legible. PIB pages could not be opened, and the 24 September rule change was not found in that index, so the bidder threshold is from PSU Watch, Swarajya and Business Standard;")
t = insert_note(t, "The block details have been checked against the Gazette of India: the Ministry of Mines notification of 21 September 2026 (CG-DL-E-22092026-276390) declares West Sewell Ridge-01 (1,000 sq km) and Sewell Rise-01 (632 sq km) off Great Nicobar available for composite licences for polymetallic nodules and crusts, matching the 1,632 sq km in this piece. The 24 September change to the bidder threshold was not in the gazette index searched and still rests on press reports.")
save(S, t)
