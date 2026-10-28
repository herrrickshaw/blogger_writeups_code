from _b4 import load, rep, insert_note, save, SRC
S = "india-raised-cooking-oil-duties-to-help"
N25 = "Notification No. 31/2025-Customs, G.S.R. 355(E), 30 May 2025 (CG-DL-E-30052025-263480)"
N24 = "Notification No. 43/2024-Customs, G.S.R. 573(E), 13 September 2024, in force from 14 September 2024 (CG-DL-E-13092024-257153)"
t = load(S)
t = rep(t, "The first, on 31 May 2025, had halved the basic duty from 20% to 10%.",
    "The first, by notification on 30 May 2025 with immediate effect, had halved the basic duty from 20% to 10%.")
t = rep(t, "<tr><td>31 May 2025</td>", "<tr><td>30 May 2025</td>")
t = rep(t, ">31 May 2025: duty cut</text>", ">30 May 2025: duty cut</text>")
t = rep(t, "press coverage of the 2024 and 2025 changes. The pre-September 2024 rates are from press coverage and should be checked against the notification.</p>",
    "the 2024 and 2025 changes from " + N24 + " and " + N25 + ", read in the Gazette. The 2024 notification sets the crude-oil entries at 20% and removes the concessional entries for refined oils but does not restate the rates it replaced, so the pre-September 2024 rates are still from press coverage.</p>")
t = rep(t, "May 2025 and September 2024 changes as reported by Business Standard, The Week (PTI), All India Radio and USDA FAS. PIB and CBIC pages could not be opened from this blog&rsquo;s tools.",
    "May 2025 and September 2024 changes from the Gazette of India: " + N25 + " (egazette.gov.in/WriteReadData/2025/263480.pdf) and " + N24 + " (egazette.gov.in/WriteReadData/2024/257153.pdf), read through " + SRC + ", with context from Business Standard, The Week (PTI), All India Radio and USDA FAS. Notification No. 31/2026-Customs was not in that index, and PIB and CBIC pages could not be opened from this blog&rsquo;s tools.")
t = insert_note(t, "The 2024 and 2025 duty changes have been checked against the Gazette of India. The 2025 cut was made by " + N25 + ", which took effect on 30 May, not 31 May as first given here; the date has been corrected in the text, table and chart. The 2024 rise to 20% was made by " + N24 + ". The September 2026 notification (No. 31/2026-Customs) was not in the gazette index searched and is still as reported.")
save(S, t)
