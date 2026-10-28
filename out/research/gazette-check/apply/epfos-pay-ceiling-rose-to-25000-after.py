from gzcommon import load, rep, insert_note, save, VIA
S = "epfos-pay-ceiling-rose-to-25000-after"
N, P = "CG-DL-E-17092026-276299", "CG-DL-E-30052026-273002"
t = load(S)
t = rep(t, "The effective date and gazette notification (S.O. 5109(E)) and the Expenditure Finance Committee&rsquo;s 16 June 2026 recommendation are as reported by compliance publishers and need checking against the gazette.",
        "The notification, S.O. 5109(E) under section 2(89) of the Code on Social Security, 2020, was " + VIA + " (" + N + "; the scanned number reads &ldquo;509(E)&rdquo;): it sets Rs 25,000 a month for Chapter III of the Code from its publication on 17 September 2026 and supersedes S.O. 2702(E) of 29 May 2026 (" + P + "), which had set Rs 15,000. The Expenditure Finance Committee&rsquo;s 16 June 2026 recommendation is as reported by compliance publishers.")
t = insert_note(t, "Checked against the Gazette of India: the new ceiling is notified under section 2(89) of the Code on Social Security, 2020, for Chapter III of the Code (the provident fund, pension and insurance schemes), at Rs 25,000 a month from the date of publication, 17 September 2026 (" + N + "). It supersedes S.O. 2702(E) of 29 May 2026 (" + P + "), which had re-notified the Rs 15,000 ceiling under the Code. The figures and dates in the piece match. No figure changed.")
save(S, t)
