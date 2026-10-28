"""Gazette check, 28 Oct 2026: FCO Seventh Amendment Order and the eighth clause 22(c) list."""
from g28 import load, rep, insert_note, save, SRC
S = "bio-fertiliser-and-green-credits"
t = load(S)
t = insert_note(t,
    "The 13 October note below has been checked against the Gazette. The Fertiliser (Inorganic, Organic or Mixed) (Control) "
    "Seventh Amendment Order, 2026 (S.O. 3482(E), dated 29 June 2026; Gazette of India Extraordinary CG-DL-E-03072026-274068) does what was reported: "
    "makers of Fermented Organic Manure and Liquid Fermented Organic Manure need no clause 8(3) authorisation letter for ten years from the Order&rsquo;s publication, "
    "and &ldquo;and Bio Gas plants&rdquo; is added after &ldquo;Compressed Bio Gas plants&rdquo; in the definitions and in the Schedule heading for organic carbon enhancer. "
    "No Eighth Amendment Order affecting this waiver was found; the Ninth Amendment Order of 22 July 2026 (S.O. 4045(E), CG-DL-E-24072026-274783) changes only the dealer provisions of clause 8(4). "
    "A new, eighth clause 22(c) list was found: S.O. 4123(E) of 27 July 2026 (CG-DL-E-29072026-274927) authorises 8 more plants to sell in bulk for three years, "
    "in Karnataka (Kodagu; Bengaluru Urban), Rajasthan (Hanumangarh), Gujarat (Tapi; Surat), Punjab (Fazilka) and Uttar Pradesh (Mathura; Mirzapur), taking the total to 127. "
    "The S.O. numbers for notifications V, VI and VII below match the Gazette. These were " + SRC + ".")
t = rep(t, "The Gazette text was not opened, and a later Eighth Amendment Order (July 2026) was not examined, so check the Gazette before relying on this.",
        "The Gazette text has since been read; see the 28 October note above.")
t = rep(t, "As of the most recent Gazette notification (25 February 2026), <strong>119 individual plants</strong>",
        "As of the seventh Gazette notification (25 February 2026), <strong>119 individual plants</strong> (127 after an eighth list on 27 July 2026)")
t = rep(t, "<tr><td>VII</td><td>25 Feb 2026</td><td>1018(E)</td><td>13</td></tr>\n<tr><td><strong>Total</strong></td><td colspan=\"2\"></td><td><strong>119</strong></td></tr>",
        "<tr><td>VII</td><td>25 Feb 2026</td><td>1018(E)</td><td>13</td></tr>\n<tr><td>VIII</td><td>27 Jul 2026</td><td>4123(E)</td><td>8</td></tr>\n"
        "<tr><td><strong>Total</strong></td><td colspan=\"2\"></td><td><strong>127</strong></td></tr>")
t = rep(t, "S.O. 1018(E) — 13 plants. (Total: 119 across all seven notifications.)</li>",
        "S.O. 1018(E) — 13 plants. (Total: 119 across the first seven notifications.)</li>\n"
        "<li>DA&amp;FW Gazette Notification VIII, 27 Jul 2026, S.O. 4123(E) — 8 plants (CG-DL-E-29072026-274927); total 127.</li>\n"
        "<li>Fertiliser (Inorganic, Organic or Mixed) (Control) Seventh Amendment Order, 2026, S.O. 3482(E), 29 Jun 2026 (CG-DL-E-03072026-274068); Ninth Amendment Order, 2026, S.O. 4045(E), 22 Jul 2026 (CG-DL-E-24072026-274783). "
        "Read via the SansadSaar index of the archive.org Gazette of India collection.</li>")
save(S, t)
