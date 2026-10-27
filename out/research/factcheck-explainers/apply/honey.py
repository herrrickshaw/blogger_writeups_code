from common import *
S = "the-national-beekeeping-honey-mission"
t = load(S)
t = rep(t, "a 2020 government-linked investigation found ten of thirteen major honey brands",
        "a 2020 investigation by the Centre for Science and Environment, an independent non-profit, found ten of thirteen major honey brands")
t = rep(t, "and that test still isn't mandatory for anything sold domestically, only for export.",
        "and that test is still not required for honey sold in India; since August 2020 it has been mandatory only for honey exported to the United States.")
t = rep(t, "engineered specifically to defeat the tests Indian regulations actually require, which check only for C4 sugar (cane) and C3 sugar (rice) markers &mdash; not the syrup CSE says Chinese exporters told them could pass \"even if 50-80% of the honey is adulterated.\"",
        "engineered specifically to defeat the tests Indian regulations then required, which covered C4 sugar (cane) and C3 sugar (rice) markers, a specific marker for rice syrup (SMR) and foreign oligosaccharides. CSE reported that the failing samples passed the C3, C4 and SMR tests, and that Chinese exporters told it the syrup could pass \"even if 50-80% of the honey is adulterated.\"")
t = rep(t, "remains, per Drishti IAS's contemporaneous explainer, \"not required by Indian law for honey that is being marketed locally but is needed for export\" &mdash;",
        "is not required for honey sold in India, as FSSAI confirmed in December 2020; since 1 August 2020 the Export Inspection Council has required it only for honey exported to the United States, not for exports in general &mdash;")
t = rep(t, "matching what is needed for export</b>", "matching what is required for exports to the United States</b>")
t = rep(t, "citing the Centre for Science and Environment's investigation as originally reported by The Hindu.",
        "citing the Centre for Science and Environment's investigation as originally reported by The Hindu. The NMR requirement for honey exported to the United States from 1 August 2020 per the Export Inspection Council, and FSSAI&rsquo;s December 2020 position that NMR is not required domestically, per contemporaneous reports; corrected 27 October 2026.")
t = insert_note(t, "Three corrections. The 2020 investigation was by the Centre for Science and Environment, an independent non-profit, not a &ldquo;government-linked&rdquo; body. India&rsquo;s 2020 honey standard did not check only C3 and C4 markers: it also had a rice-syrup marker (SMR) and foreign oligosaccharides, and CSE reported that the failing samples passed the C3, C4 and SMR tests. And the NMR test is not required for exports in general: the Export Inspection Council made it mandatory from 1 August 2020 only for honey exported to the United States, and FSSAI said in December 2020 that it is not required domestically.")
save(S, t)
