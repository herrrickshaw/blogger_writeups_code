"""Correct the BHAVYA Rasayan capacity and site claims in the two July chemical posts."""
from common import load, rep, insert_note, save

NOTE_TXT = ("Earlier versions of this piece attributed +150 KTPA of dyes and +80 KTPA of pigments to the BHAVYA Rasayan chemical parks "
            "and, in one place, named three host states. The Cabinet decision of 24 July 2026 (Rs 3,030 crore, 2026-27 to 2030-31) sets no capacity target: "
            "it funds common infrastructure in three parks of at least 8 sq km each, chosen by a challenge among states, with up to Rs 1,000 crore of central support per park. "
            "Those figures have been removed. This blog&rsquo;s October 2026 piece on the scheme, &ldquo;India&rsquo;s Rs 3,030 Crore Chemical Parks Copy the Bulk-Drug Parks&rdquo;, has the details.")

s = "chemical-import-substitution-analysis"
t = load(s)
t = rep(t, "<td>Dyes (+150 KTPA), Pigments (+80 KTPA), Auxiliaries</td>",
        "<td>Common infrastructure only; the Cabinet decision sets no capacity target</td>")
t = insert_note(t, NOTE_TXT)
save(s, t)

s = "top-15-chemicals-for-import"
t = load(s)
t = rep(t, "<li>3 sites planned: Andhra Pradesh, Gujarat, Tamil Nadu</li>",
        "<li>3 parks of at least 8 sq km each, to be chosen by a challenge among states; up to Rs 1,000 crore of central support each</li>")
t = rep(t, "<li>Capacity: +150 KTPA dyes + 80 KTPA pigments</li>",
        "<li>Capacity: no target set; the scheme funds common infrastructure (Cabinet, 24 July 2026)</li>")
t = rep(t, "<td>+150 KTPA dyes + 80 KTPA pigments</td>", "<td>No capacity target set</td>")
t = insert_note(t, NOTE_TXT)
save(s, t)
