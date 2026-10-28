"""Mobile Phone Manufacturing Scheme: check the outlay and terms against the gazette notification of 21 Aug 2026."""
from gc3common import load, rep, insert_note, save, SRC
S = "the-phone-plis-successor-pays-up-to-5"
t = load(S)
t = rep(t, "I could not open the gazette text to see which is right.",
        "The gazette notification itself (Part I, Section 1, CG-DL-E-21082026-275648, " + SRC + ") gives the outlay as &ldquo;&#8377;62,500 crores, including administrative charges&rdquo;, fungible between the two target segments, so the Cabinet figure is the scheme total; the &#8377;62,300 crore in the guidelines is consistent with about &#8377;200 crore going to administration, though the gazette does not state that amount.")
t = rep(t, "Not read: the gazette notification itself, so the outlay conflict stays open.",
        "Gazette of India, Extraordinary, Part I, Section 1, Mobile Phone Manufacturing Scheme (MeitY, 21 August 2026), CG-DL-E-21082026-275648 (egazette.gov.in/WriteReadData/2026/275648.pdf), " + SRC + "; its OCR confirms the &#8377;62,500 crore outlay including administrative charges, the five-year tenure, the &#8377;5,000&ndash;25,000 crore threshold schedule, the &#8377;10,000 crore entry level for new brands, the baseline of last year&rsquo;s sales plus 15% and the 2.75% band rate for FY2026-27 and FY2027-28; the remaining rates in the table are illegible in the OCR and stay as read from the guidelines.")
t = insert_note(t, "Checked against the Gazette of India notification of the Mobile Phone Manufacturing Scheme (CG-DL-E-21082026-275648). The outlay question this piece left open is settled: the gazette gives &#8377;62,500 crore including administrative charges, fungible between the two target segments. The sales thresholds, the 15% moving baseline, the &#8377;10,000 crore entry level for new brands and the 2.75% band rate for the first two years also match the gazette text.")
save(S, t)
