from gzcommon import load, rep, insert_note, save, VIA
S = "india-has-legalised-e100-for-flex-fuel"
D1, D2 = "CG-DL-E-28042026-272125", "CG-DL-E-27072026-274834"
t = load(S)
t = rep(t, "<td>Proposed adding E85 and E100 to the emission and certification rules</td>",
        "<td>Proposed adding E85 and E100 to the emission and certification rules: &ldquo;(E85)&rdquo; becomes &ldquo;(E85) or (E100)&rdquo; in the rule 115 tables, with a separate annexure for E100 vehicles (Gazette, " + D1 + ")</td>")
t = rep(t, "<p>The text of G.S.R. 911(E) could not be opened; its contents come from press reports of the notification.",
        "<p>The final notification, G.S.R. 911(E), is not in the Gazette of India index this blog used, so its contents come from press reports; they match the two drafts, of 27 April and 13 July 2026, which were " + VIA + " (" + D1 + "; G.S.R. 634(E), " + D2 + ").")
t = rep(t, "Notification: Business Standard (26 October 2026), NewsOrbiter and PGurus on G.S.R. 911(E) and the April 2026 draft;",
        "Notification: Business Standard (26 October 2026), NewsOrbiter and PGurus on G.S.R. 911(E); draft rules of 27 April 2026, Gazette of India Extraordinary " + D1 + " (egazette.gov.in/WriteReadData/2026/272125.pdf), and G.S.R. 634(E) of 13 July 2026, " + D2 + ";")
t = insert_note(t, "Checked against the Gazette of India: the April 2026 draft (" + D1 + ") proposed changing &ldquo;(E85)&rdquo; to &ldquo;(E85) or (E100)&rdquo; in the emission and certification tables of the Central Motor Vehicles Rules, with a separate annexure for E100 vehicles, as described here. A second draft, G.S.R. 634(E) of 13 July 2026 (" + D2 + "), added a reference fuel for E100 and would require makers to state, on a sticker on each vehicle, whether it is compatible with E85 and E100. The final G.S.R. 911(E) is not in the index this blog used, so it is still described from press reports. No figure changed.")
save(S, t)
