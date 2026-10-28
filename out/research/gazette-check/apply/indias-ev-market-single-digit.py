"""EV market post: verify the e-2W extension and PM E-DRIVE outlay against the gazette."""
from gc3common import load, rep, insert_note, save, SRC, PMED
S = "indias-ev-market-single-digit"
t = load(S)
t = rep(t, "(press reports; the order text was not opened)",
        "(confirmed in S.O. 4424(E) of 10 August 2026, Gazette of India, Extraordinary, CG-DL-E-10082026-275344)")
t = rep(t, "<td>PM E-DRIVE (Sept 2024, ₹10,900 cr/2 yrs)</td>",
        "<td>PM E-DRIVE (Sept 2024, ₹10,900 cr/2 yrs; extended to Mar 2028 and raised to ₹11,900 cr by Aug 2026)</td>")
t = rep(t, "with an outlay of ₹10,900 crore over two years",
        "with an outlay of ₹10,900 crore over two years (later extended to 31 March 2028 by S.O. 3626(E) of 7 August 2025, and raised to ₹11,900 crore by S.O. 4424(E) of 10 August 2026, per the gazette)")
t = insert_note(t, "The 12 October note below has been checked against the Gazette of India. S.O. 1617(E) of 27 March 2026 had set 31 July 2026 as the last day for the e-2W incentive; S.O. 4424(E) of 10 August 2026 extended it to 31 March 2028 at &#8377;2,500 a kWh, capped at &#8377;5,000, raised the e-2W allocation to &#8377;2,767 crore, set 31 December 2027 as the last date for claims and raised PM E-DRIVE&rsquo;s total outlay from &#8377;10,900 crore to &#8377;11,900 crore. The full chain of notifications: " + PMED + "; " + SRC + ".")
save(S, t)
