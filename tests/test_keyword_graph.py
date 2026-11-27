import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import keyword_graph as kg  # noqa: E402


def doc(head, body, **kw):
    return {"head": head.lower(), "body": (head + " " + body).lower(), **kw}


def corpus():
    bat = "sodium-ion cells weigh more per kwh than lfp cells; the battery pack mass and cell density decide range. "
    crude = "sour crude grades with high sulphur: refinery runs of sour crude and the crude basket price. "
    d = {
        "bat1": doc("Sodium-ion battery pack mass", bat * 3),
        "bat2": doc("Battery pack density and lfp cells", bat * 3),
        "bat3": doc("LFP battery cells compared", bat * 2),
        "oil1": doc("Sour crude refinery runs", crude * 3),
        "oil2": doc("Crude basket and sour crude price", crude * 3),
        "oil3": doc("Refinery sour crude grades", crude * 2),
    }
    # filler posts so a term is not in half the corpus
    for i in range(14):
        d[f"x{i}"] = doc(f"Unrelated topic {i} wheat harvest", f"wheat mandi harvest topic{i} unique{i} words{i} " * 3)
    return d


def test_phrases_and_words_are_terms_and_stop_words_break_phrases():
    t = kg.terms("the sodium-ion battery pack of the cell")
    assert "sodium-ion" in t and "battery pack" in t and "sodium-ion battery" in t
    assert "pack cell" not in t           # "of the" sits between them


def test_related_pairs_follow_subject_not_chance():
    g = kg.compute(corpus())["posts"]
    assert {x["slug"] for x in g["bat1"]["related"][:2]} == {"bat2", "bat3"}
    assert {x["slug"] for x in g["oil1"]["related"][:2]} == {"oil2", "oil3"}
    assert all(x["slug"].startswith("oil") for x in g["oil2"]["related"] if x["score"] > 0.07)


def test_every_link_names_the_shared_terms():
    g = kg.compute(corpus())["posts"]
    for x in g["bat1"]["related"]:
        assert x["shared"], x


def test_keywords_prefer_distinctive_terms_and_do_not_repeat_a_phrase_as_a_word():
    k = kg.compute(corpus())["posts"]["bat1"]["keywords"]
    assert any("sodium" in w for w in k)
    assert not ("sour" in k and "sour crude" in k)


def test_hubs_need_headings_and_keywords_and_skip_title_filler():
    c = corpus()
    for i in range(8):
        c[f"f{i}"] = doc("A guide to things", "the guide guide guide filler words text " * 2)
    hubs = kg.compute(c)["hubs"]
    assert any("sour" in h for h in hubs) and any("battery" in h for h in hubs)
    assert "guide" not in hubs


def test_plural_folding_keeps_a_readable_spelling():
    kg.SURFACE.clear()
    kg.terms("biogas plants and biogas plant")
    assert kg.show("biogas") == "biogas" and kg.show("plant") in ("plant", "plants")


def test_a_post_always_gets_at_least_two_links_when_anything_is_close():
    g = kg.compute(corpus())["posts"]
    assert all(len(v["related"]) >= 2 for s, v in g.items() if s.startswith(("bat", "oil")))
