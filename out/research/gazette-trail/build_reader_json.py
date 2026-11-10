#!/usr/bin/env python3
"""Rebuild masaladeutsch's Gazette Trail reader data (data/gazette_trail.json in herrrickshaw/masaladeutsch)
from gazette-translated-indexed's own db/schema.sql + db/seed_*.sql.

    python3 build_reader_json.py <path-to-gazette-translated-indexed> <out.json> [--compare old.json]
"""
import sys, os, glob, json, sqlite3, collections

repo, out = sys.argv[1], sys.argv[2]
cmp = sys.argv[sys.argv.index("--compare") + 1] if "--compare" in sys.argv else None
db = sqlite3.connect(":memory:")
db.executescript(open(os.path.join(repo, "db/schema.sql")).read())
seeds = sorted(glob.glob(os.path.join(repo, "db/seed_*.sql")))
ayush = [s for s in seeds if s.endswith("seed_ayush.sql")]
for s in [s for s in seeds if s not in ayush] + ayush:        # Ayush after its cross-ministry dependency
    db.executescript(open(s).read())
assert not db.execute("PRAGMA foreign_key_check").fetchall()
ACT = {"amends": ("amends", "amended by"), "supersedes": ("supersedes", "superseded by"),
       "corrigendum": ("corrigendum to", "corrected by"), "rescinds": ("rescinds", "rescinded by"),
       "repeals": ("repeals", "repealed by"), "cites": ("cites", "cited by")}
N = {}
for r in db.execute("""select g.gazette_id,g.series,g.number,g.year,g.gsr_or_so,g.publish_date,m.name,m.department,a.title,t.subject_summary
                       from gazette_notification g left join ministry m using(ministry_id) left join act_or_rule a using(instrument_id)
                       left join subject_thread t using(thread_id) where g.archived_at is null"""):
    gid, series, number, year, gs, date, mn, dept, act, thr = r
    N[gid] = {"id": gid, "series": series, "number": number, "year": year, "gsr_or_so": gs, "date": date,
              "ministry": mn, "department": dept, "act": act, "thread": thr, "links": []}
lab = lambda g: f'{N[g]["gsr_or_so"] or N[g]["number"]} ({N[g]["date"]})'
L = 0
for s, t, rel in db.execute("select source_gazette_id,target_gazette_id,relation_type from cross_reference where archived_at is null"):
    if s not in N or t not in N: continue
    L += 1
    a, p = ACT.get(rel, (rel, rel + " by"))
    N[s]["links"].append({"dir": "out", "verb": a, "id": t, "label": lab(t)})
    N[t]["links"].append({"dir": "in", "verb": p, "id": s, "label": lab(s)})
for n in N.values(): n["links"].sort(key=lambda x: (x["dir"], x["verb"], x["id"]))
notes = sorted(N.values(), key=lambda n: (n["ministry"] or "", n["date"] or "", n["id"]))
res = {"title": "Gazette Trail reader data", "source_project": "https://github.com/herrrickshaw/gazette-translated-indexed",
       "ministry_count": len({n["ministry"] for n in notes}), "notification_count": len(notes), "link_count": L, "notifications": notes}
if cmp:
    old = json.load(open(cmp)); res = {**{k: old[k] for k in ("title", "source_project", "note")}, **{k: v for k, v in res.items() if k not in ("title", "source_project")}}
    O = {n["id"]: n for n in old["notifications"]}
    diff = collections.Counter()
    for gid, n in N.items():
        o = O.get(gid)
        if not o: diff["new"] += 1; continue
        for k in n:
            if k == "links":
                if sorted((x["dir"], x["verb"], x["id"]) for x in n[k]) != sorted((x["dir"], x["verb"], x["id"]) for x in o[k]): diff["links"] += 1
            elif n[k] != o.get(k): diff[k] += 1
    diff["missing"] = len(set(O) - set(N))
    print("compare vs old:", dict(diff), "| old", old["notification_count"], old["link_count"], old["ministry_count"])
json.dump(res, open(out, "w"), ensure_ascii=False, separators=(",", ":"))
print("notifications", res["notification_count"], "links", L, "ministries", res["ministry_count"])
