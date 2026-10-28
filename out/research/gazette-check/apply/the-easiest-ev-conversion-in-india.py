"""EV conversion post: check PM E-DRIVE outlay and tenure against the gazette."""
from gc3common import load, rep, insert_note, save, SRC, PMED
S = "the-easiest-ev-conversion-in-india"
t = load(S)
t = rep(t, "outlets date that extension to August 2025 or April 2026.",
        "the gazette shows the extension was S.O. 3626(E) of 7 August 2025.")
t = rep(t, "check the outlay against the gazette text.",
        "the gazette shows the outlay was raised to &#8377;11,900 crore by S.O. 4424(E) of 10 August 2026 (see the 28 October note).")
t = rep(t, "within the same &#8377;10,900 crore outlay (a further gazette amendment on 10 August 2026 added &#8377;1,000 crore specifically for e-2Ws and nearly doubled the two-wheeler subsidy cap, from 24.79 lakh to 45.79 lakh vehicles)",
        "within the same &#8377;10,900 crore outlay (S.O. 3626(E) of 7 August 2025); a further gazette amendment on 10 August 2026 (S.O. 4424(E)) raised the total outlay to &#8377;11,900 crore, lifting the e-2W allocation from &#8377;1,772 crore to &#8377;2,767 crore and the number of e-2Ws supported from 24.79 lakh to 45.79 lakh")
t = rep(t, "(&#8377;10,900 crore, October 2024-March 2026)",
        "(&#8377;10,900 crore, October 2024-March 2026, since extended to March 2028 and raised to &#8377;11,900 crore)")
t = insert_note(t, "PM E-DRIVE&rsquo;s outlay and tenure have been checked against its notifications in the Gazette of India. The extension to 31 March 2028 was S.O. 3626(E) of 7 August 2025, within the original &#8377;10,900 crore; S.O. 4424(E) of 10 August 2026 then raised the total outlay to &#8377;11,900 crore, mainly for e-2Ws (&#8377;2,767 crore, up from &#8377;1,772 crore). The full chain: " + PMED + "; " + SRC + ".")
save(S, t)
