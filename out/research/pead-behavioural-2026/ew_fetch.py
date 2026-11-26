import sys, re, time, urllib.request, ssl, os, html
days = sys.argv[1:]
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
for i, d in enumerate(days, 1):
    out = f"ew/{d}.html"
    if os.path.exists(out) and os.path.getsize(out) > 5000:
        continue
    t0 = time.time()
    try:
        req = urllib.request.Request(f"https://earnings-watcher.com/wiki/earnings-reactions-{d}", headers=UA)
        data = urllib.request.urlopen(req, timeout=40).read()
        open(out, "wb").write(data); st = f"{len(data)}B"
    except Exception as e:
        st = f"ERR {e}"
    print(f"[{i}/{len(days)}] {d} {st} {time.time()-t0:.1f}s", flush=True)
    time.sleep(1.1)
