"""Search the SansadSaar Central Gazette (Extraordinary) index, Sep 2022 - Oct 2026, and print official text.
# Expects a blob-filtered clone of https://github.com/NakliTechie/sansadsaar-gazettes at ../gz relative to this file (see ROOT).

  python3 gz.py meta "<regex on ministry/department/subject>" [--from YYYY-MM-DD] [--to YYYY-MM-DD] [--limit N]
  python3 gz.py text <gazette_id or ugid> [--grep REGEX] [--chars N]
  python3 gz.py textsearch "<regex>" --from YYYY-MM-DD --to YYYY-MM-DD [--ministry REGEX] [--limit N]

Data: NakliTechie/sansadsaar-gazettes (archive.org gazetteofindia OCR). Text shards are fetched lazily with git.
Cite the gazette_id (CG-DL-E-DDMMYYYY-NNNNNN) and the egazette URL printed with each hit.
"""
import json, glob, re, sys, subprocess, os, argparse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "gz")
G = os.path.join(ROOT, "docs", "gazettes")

def records():
    for f in sorted(glob.glob(os.path.join(G, "reports-central-*.json"))):
        for r in json.load(open(f))["records"]:
            yield r

def shard_for(ident):
    m = json.load(open(os.path.join(G, "manifest.json")))["texts"]
    k = "central|" + ident.replace("in.gazette.central.", "central_").replace(".", "_").replace("-", "")
    return m.get(k), k

def load_shard(i):
    fn = f"texts-{i:02d}.json" if i < 100 else f"texts-{i}.json"
    p = os.path.join(G, fn)
    if not os.path.exists(p):
        import fcntl, time
        with open(os.path.join(ROOT, ".fetch.lock"), "w") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            for _ in range(5):
                if os.path.exists(p): break
                r = subprocess.run(["git", "-C", ROOT, "checkout", "HEAD", "--", f"docs/gazettes/{fn}"], capture_output=True, timeout=300)
                if r.returncode == 0: break
                time.sleep(5)
    return json.load(open(p))

def find(idq):
    for r in records():
        if idq in (r["gazette_id"], r["ugid"], r["identifier"]):
            return r

def text_of(r):
    i, k = shard_for(r["identifier"])
    if i is None:
        return None
    d = load_shard(i)
    v = d.get(k) or d.get("texts", {}).get(k) if isinstance(d, dict) else None
    if v is None and isinstance(d, dict):
        for kk, vv in d.items():
            if isinstance(vv, dict) and k in vv:
                v = vv[k]; break
    if isinstance(v, dict):
        v = v.get("eng") or v.get("text") or json.dumps(v)[:200000]
    return v

def show(r):
    print(f'{r["issue_date"]}  {r["gazette_id"]}  {r["ministry"]} / {r["department"]}\n   {r["subject"][:300]}\n   {r["gazette_source_url"]}')

ap = argparse.ArgumentParser()
ap.add_argument("cmd"); ap.add_argument("q")
ap.add_argument("--from", dest="f", default="2022-01-01"); ap.add_argument("--to", default="2099-01-01")
ap.add_argument("--limit", type=int, default=40); ap.add_argument("--grep"); ap.add_argument("--chars", type=int, default=6000)
ap.add_argument("--ministry")
a = ap.parse_args()
if a.cmd == "meta":
    rx = re.compile(a.q, re.I); n = 0
    for r in records():
        if a.f <= r["issue_date"] <= a.to and rx.search(" ".join([r["ministry"], r["department"], r["office"], r["subject"]])):
            show(r); n += 1
            if n >= a.limit: break
    print(n, "hits")
elif a.cmd == "text":
    r = find(a.q)
    if not r: sys.exit("not found")
    show(r); t = text_of(r) or ""
    if a.grep:
        for m in re.finditer(a.grep, t, re.I):
            print("...", t[max(0, m.start()-500):m.start()+800].replace("\n", " "), "...\n")
    else:
        print(t[:a.chars])
elif a.cmd == "textsearch":
    rx = re.compile(a.q, re.I); mrx = re.compile(a.ministry, re.I) if a.ministry else None; n = 0
    for r in records():
        if not (a.f <= r["issue_date"] <= a.to): continue
        if mrx and not mrx.search(r["ministry"] + " " + r["department"]): continue
        t = text_of(r) or ""
        m = rx.search(t)
        if m:
            show(r); print("   >>", t[max(0, m.start()-200):m.start()+300].replace("\n", " ")); n += 1
            if n >= a.limit: break
    print(n, "hits")
