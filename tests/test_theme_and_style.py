import json
import pathlib

import pytest

import build_site_style as BS
import theme_build as TB

BASE = ("<?xml version='1.0'?><html xmlns:b='http://www.google.com/2005/gml/b'><head>"
        "<b:skin><![CDATA[\n.hero{color:red}\n.card .x{a:b}\n/* .hero in a comment */\n.other{c:d}\n]]></b:skin></head>"
        "<body><div id='Blog1'/></body>\n</html>\n")


@pytest.fixture
def theme(tmp_path, monkeypatch):
    for name, val in (("ROOT", tmp_path), ("BASE", tmp_path / "theme" / "base.xml"), ("OUT", tmp_path / "theme" / "theme.xml"),
                      ("MODULES", tmp_path / "theme" / "modules.json")):
        monkeypatch.setattr(TB, name, val)
    (tmp_path / "theme").mkdir()
    (tmp_path / "templates").mkdir()
    (tmp_path / "templates" / "a.css").write_text("\n.mod-a{x:1}\n/* tail a */\n\n")
    (tmp_path / "templates" / "b.js").write_text("console.log('b');\n")
    mods = [{"id": "css-a", "kind": "css", "file": "templates/a.css"},
            {"id": "js-b", "kind": "js", "file": "templates/b.js"},
            {"id": "scope-s", "kind": "scope", "classes": ["hero", "card"]}]
    (tmp_path / "theme" / "modules.json").write_text(json.dumps(mods))
    (tmp_path / "theme" / "base.xml").write_text(BASE)
    monkeypatch.setattr(TB.sys, "argv", ["tb"])
    return tmp_path


def run(monkeypatch, *argv):
    monkeypatch.setattr(TB.sys, "argv", ["tb", *argv])
    TB.main()


def test_load_modules_reads_bodies_and_rejects_bad(theme):
    mods = TB.load_modules()
    assert mods[0]["body"] == ".mod-a{x:1}\n/* tail a */" and mods[1]["body"] == "console.log('b');" and mods[2]["body"] == ""
    (theme / "templates" / "bad.css").write_text("a{} ]]> b")
    (theme / "theme" / "modules.json").write_text(json.dumps([{"id": "x", "kind": "css", "file": "templates/bad.css"}]))
    with pytest.raises(SystemExit, match=r"contains '\]\]>'"):
        TB.load_modules()
    (theme / "theme" / "modules.json").write_text(json.dumps([{"id": "x", "kind": "weird", "file": "templates/a.css"}]))
    with pytest.raises(SystemExit, match="unknown kind 'weird'"):
        TB.load_modules()


def test_block_wrapping():
    css = TB.block({"id": "i", "kind": "css", "body": "b{}"})
    assert css == "/* BEGIN theme-module: i */\nb{}\n/* END theme-module: i */\n"
    js = TB.block({"id": "i", "kind": "js", "body": "x()"})
    assert js == "<script>//<![CDATA[\n/* BEGIN theme-module: i */\nx()\n/* END theme-module: i */\n//]]></script>\n"


def test_scope_skin_only_inside_skin_outside_comments_and_not_midname():
    t = ("<style>.hero{x}</style><b:skin><![CDATA[.hero{a} .hero-x{b} /* .hero{c} */ .card .hero, .hero:hover{d}\n"
         "@media x{.hero{e}}.heroic{f}]]></b:skin>.hero{outside}")
    out = TB.scope_skin(t, ["hero"])
    skin = out[out.index("<b:skin>"):out.index("</b:skin>")]
    assert ".hero:not(.post-body *){a}" in skin and ".hero-x{b}" in skin and "/* .hero{c} */" in skin
    assert ".card .hero," in skin and ".hero:not(.post-body *):hover{d}" in skin      # only selectors that START with the class are scoped
    assert "@media x{.hero:not(.post-body *){e}}" in skin and ".heroic{f}" in skin
    assert out.startswith("<style>.hero{x}</style>") and out.endswith(".hero{outside}")


def test_build_inserts_css_before_skin_end_js_before_body_and_scopes(theme):
    mods = TB.load_modules()
    out = TB.build(BASE, mods)
    assert out.index("/* BEGIN theme-module: css-a */") < out.index("]]></b:skin>")
    assert out.index("<script>//<![CDATA[") < out.rindex("</body>")
    assert ".hero:not(.post-body *){color:red}" in out and ".card:not(.post-body *) .x{a:b}" in out
    assert "/* .hero in a comment */" in out
    TB.verify(out, BASE, mods)


def test_build_skips_retired_and_validates_base(theme):
    mods = TB.load_modules()
    mods[0]["retired"] = True
    assert "css-a" not in TB.build(BASE, mods)
    with pytest.raises(SystemExit, match="has 0"):
        TB.build("<html></body></html>", mods)
    with pytest.raises(SystemExit, match="has 2"):
        TB.build(BASE.replace("</head>", "]]></b:skin></head>"), mods)
    with pytest.raises(SystemExit, match="not followed by </html>"):
        TB.build(BASE.replace("</html>", "<p/></html>"), mods)
    with pytest.raises(SystemExit, match="not followed by </html>"):
        TB.build(BASE.replace("</body>", ""), mods)


def test_strip_roundtrip_and_hand_pasted_copies(theme):
    mods = TB.load_modules()
    built = TB.build(BASE, mods)
    stripped, removed = TB.strip(built, mods)
    assert stripped == BASE and removed == ["css-a x1", "js-b x1", "scope-s x2"]
    hand_css = BASE.replace("]]></b:skin>", "/* css-a (pasted) */\n.mod-a{x:1}\n/* tail a */\n]]></b:skin>")
    s, removed = TB.strip(hand_css, mods)
    assert s == BASE and removed == ["css-a x1"]
    hand_js = BASE.replace("</body>", "<script>//<![CDATA[\n/* js-b (old) */\nold();\n//]]></script>\n</body>")
    s, removed = TB.strip(hand_js, mods)
    assert s == BASE and removed == ["js-b x1"]
    with pytest.raises(SystemExit, match="unmarked copy but not its last line"):
        TB.strip(BASE.replace("]]></b:skin>", "/* css-a (x) */\n.different{}\n]]></b:skin>"), mods)
    assert TB.strip(BASE, mods) == (BASE, [])


def test_verify_failures(theme):
    mods = TB.load_modules()
    out = TB.build(BASE, mods)
    with pytest.raises(SystemExit, match="not well-formed XML"):
        TB.verify(out.replace("</html>", ""), BASE, mods)
    with pytest.raises(SystemExit, match="appears 2 times"):
        TB.verify(out.replace("</b:skin>", "/* BEGIN theme-module: css-a */</b:skin>"), BASE, mods)
    with pytest.raises(SystemExit, match="not exactly base"):
        TB.verify(out, BASE + " ", mods)
    mods[0]["retired"] = True
    with pytest.raises(SystemExit, match="css-a: appears 1 times"):
        TB.verify(out, BASE, mods)


def test_main_build_check_and_stale(theme, monkeypatch, capsys):
    run(monkeypatch)
    out = theme / "theme" / "theme.xml"
    assert out.exists() and "wrote" in capsys.readouterr().out
    with pytest.raises(SystemExit) as e:
        run(monkeypatch, "--check")
    assert e.value.code == 0 and "is up to date" in capsys.readouterr().out
    out.write_text("old")
    with pytest.raises(SystemExit) as e:
        run(monkeypatch, "--check")
    assert e.value.code == 1 and "out of date" in capsys.readouterr().out
    assert out.read_text() == "old"                                  # --check never writes
    custom = theme / "custom.xml"
    run(monkeypatch, "--out", str(custom))
    assert custom.read_text() == TB.build(BASE, TB.load_modules())


def test_main_base_with_modules_in_it_exits(theme, monkeypatch):
    (theme / "theme" / "base.xml").write_text(TB.build(BASE, TB.load_modules()))
    with pytest.raises(SystemExit, match="still contains modules"):
        run(monkeypatch)


def test_main_fresh_backup_replaces_base_and_reports_changes(theme, monkeypatch, capsys):
    backup = theme / "backup.xml"
    changed = BASE.replace(".other{c:d}", ".other{c:d}.newrule{z:z}")
    backup.write_text(TB.build(changed, TB.load_modules()))
    run(monkeypatch, "--base", str(backup))
    out = capsys.readouterr().out
    assert "modules removed from it: css-a x1, js-b x1, scope-s x2" in out and "live theme has changed since theme/base.xml" in out
    assert (theme / "theme" / "base.xml").read_text() == changed
    backup.write_text(changed)
    run(monkeypatch, "--base", str(backup))
    out = capsys.readouterr().out
    assert "modules removed from it: none" in out and "has changed since" not in out


def test_main_empty_base_arg_and_latest(theme, monkeypatch, capsys, tmp_path):
    with pytest.raises(SystemExit, match="empty path"):
        run(monkeypatch, "--base", "  ")
    home = tmp_path / "home"
    (home / "Downloads").mkdir(parents=True)
    monkeypatch.setattr(pathlib.Path, "expanduser", lambda self: home / "Downloads" if str(self) == "~/Downloads" else self)
    with pytest.raises(SystemExit, match="no Blogger theme backup"):
        TB.latest_backup()
    (home / "Downloads" / "notes.xml").write_text("<x/>")
    older = home / "Downloads" / "old-theme.xml"
    older.write_text(BASE)
    newer = home / "Downloads" / "new-theme.xml"
    newer.write_text(BASE.replace("<body>", "<body><!-- newer -->"))
    import os
    os.utime(older, (1, 1))
    os.utime(newer, (2_000_000_000, 2_000_000_000))
    assert TB.latest_backup() == str(newer) and "new-theme.xml" in capsys.readouterr().out
    run(monkeypatch, "--base", "latest")
    assert "newer" in (theme / "theme" / "base.xml").read_text()


# ================================================================ build_site_style
@pytest.mark.parametrize("c,want", [
    ("#000", 0.0), ("#fff", 1.0), ("#FFFFFF", 1.0), ("#ff0000", 0.2126), ("#0f0", 0.7152), ("#00f", 0.0722),
    ("rgb(255,255,255)", 1.0), ("rgba(0, 0, 0, .5)", 0.0), ("rgb(255 0 0 / 0.5)", None), ("#12", None), ("#gggggg", None),
    ("red", None), ("rgb(1,2)", None), ("rgb(a,b,c)", None), ("  #fff  ", 1.0), ("#ffffffaa", 1.0),
])
def test_lum(c, want):
    got = BS.lum(c)
    assert (got is None) if want is None else got == pytest.approx(want, abs=1e-4)


def test_lum_slash_separated_rgb():
    assert BS.lum("rgb(255/0/0)") == pytest.approx(0.2126)


@pytest.mark.parametrize("sel,want", [
    (".card", ["card"]), (".card .title", ["title"]), (".a.b", ["b"]), ("div.card", ["card"]), ("#id .x", []), (".a > .b", []),
    (".a + .b", []), (".a ~ .b", []), ("a[href] .x", []), (".x::before", []), ("div", []), (".a:hover", ["a"]), ("", []),
])
def test_classes_in(sel, want):
    assert BS.classes_in(sel) == want


@pytest.fixture
def posts(tmp_path, monkeypatch):
    monkeypatch.setattr(BS, "POSTS", tmp_path / "posts")
    monkeypatch.setattr(BS, "OUT", tmp_path / "templates" / "site-style.css")
    (tmp_path / "posts").mkdir()
    (tmp_path / "templates").mkdir()

    def add(name, css):
        (tmp_path / "posts" / f"{name}.html").write_text(f"<style>{css}</style><p>x</p>")
    return tmp_path, add


def test_collect_dark_light_never_and_thresholds(posts):
    tmp, add = posts
    add("a", ".dark{background:#111}.light{background:#fff}.mid{background:#808080}.body{background:#000}"
             "body{background:#000}.select{background:#000}.post-body{background:#000}.nobg{color:red}")
    add("b", ".grad{background:linear-gradient(#000,#222)}.img{background-image:linear-gradient(#fff,#eee)}"
             ".multi,.other{background:#001}.x .y{background:#000}.cmb:hover{background:#000}.tag > .z{background:#000}")
    dark, light = BS.collect()
    assert dark == ["cmb", "dark", "grad", "multi", "other", "y"]        # NEVER names (.body, .select, .post-body) excluded
    assert "z" not in dark and "mid" not in dark and "nobg" not in dark
    assert light == ["img", "light"]


def test_collect_boundary_luminance(posts):
    tmp, add = posts
    # #6b6b6b lum=0.4196 <0.42 dark; #6c6c6c = 0.4235 not dark; #b8b8b8=0.7216 >0.72 light; #b7b7b7 = 0.7176 not light
    add("a", ".d1{background:#6b6b6b}.d2{background:#6c6c6c}.l1{background:#b8b8b8}.l2{background:#b7b7b7}")
    dark, light = BS.collect()
    assert dark == ["d1"] and light == ["l1"]


def test_collect_var_resolution_and_depth(posts):
    tmp, add = posts
    add("a", ":root{--bg:#000;--alias:var(--bg);--l1:var(--l2);--l2:var(--l3);--l3:var(--l4);--l4:var(--l5);--l5:#000}"
             ".v{background:var(--bg)}.w{background:var(--alias)}.deep{background:var(--l1)}.ok4{background:var(--l2)}"
             ".unk{background:var(--missing,#000)}")
    dark, _ = BS.collect()
    assert "v" in dark and "w" in dark and "unk" in dark and "ok4" in dark       # four hops still resolve
    assert "deep" not in dark                                                       # five hops do not


def test_collect_conflicts_majority_and_tie_to_dark(posts):
    tmp, add = posts
    add("a", ".tie{background:#000}.maj{background:#000}.minor{background:#fff}")
    add("b", ".tie{background:#fff}.maj{background:#000}.minor{background:#fff}")
    add("c", ".maj{background:#fff}.minor{background:#fff}.dd{background:#000}")
    add("d", ".minor{background:#000}.light2{background:#fff}.light2x{background:#fff}")
    dark, light = BS.collect()
    assert "tie" in dark and "tie" not in light                # tie goes dark
    assert "maj" in dark and "maj" not in light                # dark 2 vs light 1
    assert "minor" in light and "minor" not in dark            # light 3 vs dark 1
    assert "light2" in light


def test_collect_skips_at_rules_empty_css_and_non_utf8(posts):
    tmp, add = posts
    (tmp / "posts" / "nocss.html").write_text("<p>none</p>")
    (tmp / "posts" / "bin.html").write_bytes(b"<style>.ok{background:#000}</style>\xff\xfe")
    add("a", "@media (x){.zz{background:#000}}.real{background:#000}")
    dark, _ = BS.collect()
    assert "ok" in dark and "real" in dark


def test_main_writes_css_and_refuses_empty(posts, capsys, monkeypatch):
    tmp, add = posts
    with pytest.raises(SystemExit, match="refusing to write an empty module"):
        BS.main()
    add("a", ".panel{background:#111}.soft{background:#fff}")
    BS.main()
    css = BS.OUT.read_text(encoding="utf-8")
    assert ".post-body :is(.panel)" in css and ".post-body :is(.soft)" in css and "from 1 posts" in css
    assert "1 dark classes, 1 light classes" in css and "{" in css and "{{" not in css
    assert "1 dark classes, 1 light classes, from 1 posts" in capsys.readouterr().out


def test_main_no_light_classes_uses_placeholder_and_many_dark_truncates_print(posts, capsys):
    tmp, add = posts
    add("a", "".join(f".d{i:02d}{{background:#000}}" for i in range(30)))
    BS.main()
    css = BS.OUT.read_text(encoding="utf-8")
    assert ".post-body :is(.gs-none)" in css
    out = capsys.readouterr().out
    assert "dark : d00" in out and " …" in out and "light: " in out
