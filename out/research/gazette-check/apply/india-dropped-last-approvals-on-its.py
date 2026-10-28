from gzcommon import load, rep, insert_note, save, VIA
S = "india-dropped-last-approvals-on-its"
A, O = "CG-DL-E-17082026-275521", "CG-DL-E-05062026-273164"
t = load(S)
t = rep(t, "<td>No scheme approval or notification</td>",
        "<td>No scheme approval or notification; any data centre &ldquo;operated by an Indian company, whether by way of owning or leasing&rdquo; that meets conditions to be prescribed by rule</td>")
t = rep(t, "The changes reported in the enacted Act match those PRS described in the Bill as introduced; the eligibility rules and the information form were still to be notified, as reported.",
        "The enacted text, read in the Gazette of India (" + A + "), matches what PRS described in the Bill as introduced. It is deemed to apply from 1 April 2026, repeals the June ordinance, and leaves the remaining conditions for data centres to rules that had not been notified, as reported.")
old = t[t.index("<p>The enacted text and the gazette notification could not be opened;"):]
old = old[:old.index("the 14 September UPI notification rests on a single report.")]
t = rep(t, old, "<p>The Act (" + A + ") and the June ordinance (" + O + ") were " + VIA + "; the provisions and the assent date of 17 August 2026 above match them. The eligibility rules and the information form had not been seen. ")
t = rep(t, "assent on 17 August 2026 per Outlook Business, Deccan Chronicle and Eastern Mirror citing the Ministry of Law notification;",
        "the Act as assented to on 17 August 2026, Gazette of India Extraordinary, Part II Section 1, " + A + " (egazette.gov.in/WriteReadData/2026/275521.pdf), and the Income-tax (Amendment) Ordinance, 2026 (No. 2 of 2026), 5 June 2026, " + O + ";")
t = insert_note(t, "Checked against the Gazette of India: the Taxation and Other Laws (Amendment) Act, 2026, assented to on 17 August 2026 (" + A + "), matches the provisions described here. It defines a qualifying data centre as one &ldquo;operated by an Indian company, whether by way of owning or leasing&rdquo; that &ldquo;satisfies such other conditions as may be prescribed&rdquo;, so the old scheme approval is replaced by rules still to come; the table now says so. The Act is deemed to apply from 1 April 2026 and repeals the June ordinance (" + O + "). No figure changed.")
save(S, t)
