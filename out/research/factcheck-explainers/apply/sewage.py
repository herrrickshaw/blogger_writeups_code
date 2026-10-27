from common import *
S = "what-sewage-disposal-in-key-parts-of"
t = load(S)
t = rep(t, "Dengue case counts, by contrast, are reported inconsistently across sources for the same recent years and shouldn't be cited as a single settled number.",
        "Dengue case counts circulate in several versions, but the press figures for 2025 are interim, part-year counts; the full-year reference is the National Centre for Vector Borne Diseases Control series, 23,407 cases in 2025.")
t = rep(t, "Press figures for 2025 of about 15,796 and about 20,866 (apparently an interim count) do not match the full-year official number.",
        "The two press figures for 2025 are both interim counts for part of the year: about 15,796 (The Federal, citing Tamil Nadu&rsquo;s Directorate of Public Health, to early October 2025) and about 20,866 (IANS, January to November 2025). Neither is a full-year figure, so neither contradicts the official total.")
t = rep(t, "the earlier 15,796 and ~20,866 figures came from The Federal's coverage and other search-indexed reporting and are superseded by the official full-year count.",
        "the 15,796 figure (The Federal, citing the Directorate of Public Health, to early October 2025) and the ~20,866 figure (IANS, January to November 2025) are interim counts, superseded by the official full-year count.")
t = insert_note(t, "The summary at the top said Tamil Nadu&rsquo;s dengue counts should not be cited as a single settled number, while the dengue section said the official series settles them. The section was right: the NCVBDC full-year figures are 27,378 cases in 2024 and 23,407 in 2025. The two press figures for 2025 are interim counts, now labelled with their periods and sources: about 15,796 to early October 2025 (The Federal, citing the state&rsquo;s Directorate of Public Health) and about 20,866 for January to November 2025 (IANS).")
save(S, t)
