"""EV localisation post: verify PM E-DRIVE outlay/tenure and PMP amendment dates against the gazette."""
from gc3common import load, rep, insert_note, save, SRC, PMED
S = "indias-ev-localisation-deadline-just"
t = load(S)
t = rep(t, "<span>PM E-DRIVE's total outlay, Oct 2024&ndash;Mar 2026</span>",
        "<span>PM E-DRIVE's original outlay, Oct 2024&ndash;Mar 2026; raised to &#8377;11,900cr to Mar 2028 on 10 Aug 2026</span>")
t = rep(t, "outlets date that extension to August 2025 or April 2026.",
        "the gazette shows the extension was S.O. 3626(E) of 7 August 2025.")
t = rep(t, "The gazette text was not opened. Sources:",
        "Both are now checked against the gazette; see the 28 October note. Sources:")
t = rep(t, "with a &#8377;10,900 crore outlay running from 1 October 2024 to 31 March 2026.",
        "with a &#8377;10,900 crore outlay running from 1 October 2024 to 31 March 2026 (notified as S.O. 4259(E) of 29 September 2024; since extended to 31 March 2028 by S.O. 3626(E) of 7 August 2025, with the outlay raised to &#8377;11,900 crore by S.O. 4424(E) of 10 August 2026).")
t = rep(t, "<tr><td>~Mar 2025</td><td>e-Bus</td><td>PMP for e-buses first notified</td></tr>",
        "<tr><td>3 Mar 2025</td><td>e-Bus</td><td>PMP for e-buses first notified (S.O. 1078(E))</td></tr>")
t = rep(t, "<tr><td>3 Mar 2026</td><td>Both</td><td>Second amendment to both PMPs</td></tr>",
        "<tr><td>13 Mar 2026</td><td>Both</td><td>Second amendment to both PMPs (S.O. 1330(E) for e-buses, S.O. 1331(E) for e-trucks)</td></tr>")
t = rep(t, "The PM E-DRIVE budget figures, the Cabinet approval date, and the SIAM/China-rare-earth motive narrative remain sourced to trade coverage found via search rather than read directly, and are flagged as such in the source line below.",
        "The scheme&rsquo;s outlay and tenure have since been checked against its notifications in the gazette (" + PMED + "), " + SRC + ". The split of the budget by segment, the Cabinet approval date and the SIAM/China-rare-earth motive narrative remain sourced to trade coverage found via search rather than read directly, and are flagged as such in the source line below.")
t = insert_note(t, "Checked against the Gazette of India. PM E-DRIVE&rsquo;s extension to 31 March 2028 was S.O. 3626(E) of 7 August 2025, not April 2026, and S.O. 4424(E) of 10 August 2026 raised the scheme&rsquo;s outlay from &#8377;10,900 crore to &#8377;11,900 crore, so the &#8377;10,900 crore in the chart and table is the original figure. The amendment table is also corrected: the second amendment to both PMPs is dated 13 March 2026 (S.O. 1330(E) and 1331(E)), not 3 March; later notifications&rsquo; recitals read &ldquo;3 March&rdquo; in the OCR, but the notifications themselves carry 13 March. The e-bus PMP was first notified on 3 March 2025 as S.O. 1078(E).")
save(S, t)
