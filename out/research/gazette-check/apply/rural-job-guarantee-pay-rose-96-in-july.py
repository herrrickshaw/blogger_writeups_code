from gzcommon import load, rep, insert_note, save, VIA
S = "rural-job-guarantee-pay-rose-96-in-july"
t = load(S)
t = rep(t, "Wage rates: S.O. 3518(E) of 30 June 2026 and the March 2025 notification for 2025-26, as reported by Upstox, SCC Online, The Tribune, Zee Business and others; some sites give different figures for a few states (Karnataka, Punjab, Goa, Kerala), and the gazette-based lists were used.",
        "Wage rates: 2025-26 from S.O. 1463(E) of 27 March 2025, checked in the Gazette of India (CG-DL-E-27032025-262013); from 1 July 2026, S.O. 3518(E) of 30 June 2026 as reported by Upstox, SCC Online, The Tribune and others; some sites give different figures for a few states (Karnataka, Punjab, Goa, Kerala), and the gazette-based lists were used.")
t = rep(t, "<p>The gazette notifications could not be opened directly; state wage rates come from news lists of the notifications, which disagree for a few states.",
        "<p>The 2025-26 rates and the Act&rsquo;s start date were " + VIA + " (S.O. 1463(E), CG-DL-E-27032025-262013; S.O. 2382(E), CG-DL-E-11052026-272413). The July 2026 wage notification, S.O. 3518(E), is not in that index, so the new rates come from news lists of it, which disagree for a few states.")
t = rep(t, "2025-26 rates from the notification of 27 March 2025 as reported by Zee Business, Adda247, HR Informative and a Maharashtra government notice;",
        "2025-26 rates: Ministry of Rural Development S.O. 1463(E), 27 March 2025, effective 1 April 2025, Gazette of India Extraordinary CG-DL-E-27032025-262013 (egazette.gov.in/WriteReadData/2025/262013.pdf); VB-G RAM G Act, 2025 (36 of 2025) brought into force on 1 July 2026 by S.O. 2382(E), 11 May 2026, CG-DL-E-11052026-272413;")
t = insert_note(t, "Checked against the Gazette of India: the 2025-26 wage rates in the table match S.O. 1463(E) of 27 March 2025 (CG-DL-E-27032025-262013) for all 17 states, and the VB-G RAM G Act&rsquo;s start on 1 July 2026 matches S.O. 2382(E) of 11 May 2026 (CG-DL-E-11052026-272413). The July 2026 wage notification, reported as S.O. 3518(E), is not in the gazette index this blog used, so the new rates are still as reported. No figure changed.")
save(S, t)
