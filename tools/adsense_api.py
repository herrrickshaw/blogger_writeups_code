#!/usr/bin/env python3
"""AdSense Management API v2 client — read-only account/site/ad-unit status audit.

Reuses the same OAuth client as blogger_api.py (same Google Cloud project,
same registered redirect URI), but requests the AdSense read-only scope and
stores its own refresh token, since the scope differs from Blogger's.

One-time setup before `auth`:
  1. Enable "AdSense Management API" for this project in Cloud Console:
     https://console.cloud.google.com/apis/library/adsense.googleapis.com?project=79331854634
  2. python3 tools/adsense_api.py auth

Then:
  python3 tools/adsense_api.py accounts
  python3 tools/adsense_api.py sites     --account <accountId>
  python3 tools/adsense_api.py adclients --account <accountId>
  python3 tools/adsense_api.py adunits   --account <accountId> --adclient <adClientId>
  python3 tools/adsense_api.py audit                       # full walk, human-readable
"""
import argparse
import http.server
import json
import pathlib
import secrets
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

API = "https://adsense.googleapis.com/v2"
SCOPE = "https://www.googleapis.com/auth/adsense.readonly"

SECRETS = pathlib.Path.home() / ".config" / "market-secrets"
CLIENT_FILE = SECRETS / "blogger_client.json"   # reused: same GCP project/client
TOKEN_FILE = SECRETS / "adsense_token.json"      # separate: different scope

DEFAULT_PORT = 8765


def _req(url, data=None, headers=None, method=None):
    body = data if (data is None or isinstance(data, bytes)) else json.dumps(data).encode()
    r = urllib.request.Request(url, data=body, headers=headers or {}, method=method)
    with urllib.request.urlopen(r, timeout=60) as resp:
        return json.loads(resp.read().decode() or "{}")


def _form(url, fields):
    return _req(url, data=urllib.parse.urlencode(fields).encode(),
                headers={"Content-Type": "application/x-www-form-urlencoded"})


def _client():
    if not CLIENT_FILE.exists():
        sys.exit(f"missing {CLIENT_FILE} — run blogger_api.py auth first (same client is reused)")
    blob = json.loads(CLIENT_FILE.read_text())
    kind = "installed" if "installed" in blob else ("web" if "web" in blob else None)
    cfg = blob[kind]
    return cfg["client_id"], cfg["client_secret"], kind


def cmd_auth(args):
    cid, csec, kind = _client()
    port = args.port or DEFAULT_PORT
    state = secrets.token_urlsafe(16)
    got = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            got.update({k: v[0] for k, v in q.items()})
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Authorised. You can close this tab.</h2>")

        def log_message(self, *a):
            pass

    try:
        srv = http.server.HTTPServer(("127.0.0.1", port), H)
    except OSError as e:
        sys.exit(f"cannot bind port {port} ({e}) — pass --port with a free one")
    redirect = f"http://127.0.0.1:{port}"
    if kind == "web":
        print("Reusing the WEB OAuth client already registered for Blogger.")
        print(f"Its redirect URI ({redirect}) is already saved from that setup, so no")
        print("Cloud Console changes are needed here UNLESS you get a redirect_uri_mismatch error.\n")
    auth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": redirect, "response_type": "code",
        "scope": SCOPE, "access_type": "offline", "prompt": "consent", "state": state,
    })
    print("Open this URL and sign in as the AdSense account owner:\n")
    print("  " + auth_url + "\n")
    try:
        webbrowser.open(auth_url)
    except Exception:
        pass
    threading.Thread(target=srv.handle_request, daemon=True).start()
    for _ in range(300):
        if got:
            break
        time.sleep(1)
    srv.server_close()
    if got.get("state") != state:
        sys.exit("state mismatch — aborting")
    if "code" not in got:
        sys.exit(f"no authorisation code returned: {got}")

    tok = _form("https://oauth2.googleapis.com/token", {
        "code": got["code"], "client_id": cid, "client_secret": csec,
        "redirect_uri": redirect, "grant_type": "authorization_code",
    })
    if "refresh_token" not in tok:
        sys.exit("no refresh_token returned — revoke prior access at "
                 "https://myaccount.google.com/permissions and retry")
    SECRETS.mkdir(parents=True, exist_ok=True)
    TOKEN_FILE.write_text(json.dumps({"refresh_token": tok["refresh_token"]}, indent=2))
    TOKEN_FILE.chmod(0o600)
    print(f"refresh token saved to {TOKEN_FILE} (mode 600)")


_access = {"token": None, "expires": 0}


def access_token():
    if _access["token"] and time.time() < _access["expires"] - 30:
        return _access["token"]
    if not TOKEN_FILE.exists():
        sys.exit(f"missing {TOKEN_FILE} — run: python3 tools/adsense_api.py auth")
    rt = json.loads(TOKEN_FILE.read_text())["refresh_token"]
    cid, csec, _ = _client()
    tok = _form("https://oauth2.googleapis.com/token", {
        "refresh_token": rt, "client_id": cid, "client_secret": csec,
        "grant_type": "refresh_token",
    })
    _access["token"] = tok["access_token"]
    _access["expires"] = time.time() + tok.get("expires_in", 3600)
    return _access["token"]


def api(path, params=None):
    url = f"{API}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    headers = {"Authorization": f"Bearer {access_token()}"}
    try:
        return _req(url, headers=headers)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        sys.exit(f"HTTP {e.code} on {path}: {body[:500]}")


def cmd_accounts(_args):
    data = api("/accounts")
    for a in data.get("accounts", []):
        print(json.dumps(a, indent=2))
    if not data.get("accounts"):
        print("no accounts returned:", json.dumps(data, indent=2))


def cmd_sites(args):
    data = api(f"/accounts/{args.account}/sites")
    for s in data.get("sites", []):
        print(json.dumps(s, indent=2))
    if not data.get("sites"):
        print("no sites returned:", json.dumps(data, indent=2))


def cmd_adclients(args):
    data = api(f"/accounts/{args.account}/adclients")
    for c in data.get("adClients", []):
        print(json.dumps(c, indent=2))
    if not data.get("adClients"):
        print("no adclients returned:", json.dumps(data, indent=2))


def cmd_adunits(args):
    data = api(f"/accounts/{args.account}/adclients/{args.adclient}/adunits")
    for u in data.get("adUnits", []):
        print(json.dumps(u, indent=2))
    if not data.get("adUnits"):
        print("no adunits returned:", json.dumps(data, indent=2))


def cmd_audit(_args):
    print("=== accounts ===")
    accts = api("/accounts").get("accounts", [])
    if not accts:
        print("No accounts visible to this token.")
        return
    for a in accts:
        acc_id = a["name"].split("/")[-1]
        print(f"\naccount: {a['name']}  display={a.get('displayName')}  "
              f"state={a.get('state')}  premium={a.get('premium')}  "
              f"timezone={a.get('timeZone', {}).get('id')}")

        sites = api(f"/accounts/{acc_id}/sites").get("sites", [])
        print(f"  sites ({len(sites)}):")
        for s in sites:
            print(f"    - {s.get('domain')}  state={s.get('state')}  "
                  f"autoAdsEnabled={s.get('autoAdsEnabled')}")

        clients = api(f"/accounts/{acc_id}/adclients").get("adClients", [])
        print(f"  ad clients ({len(clients)}):")
        for c in clients:
            client_id = c["name"].split("/")[-1]
            print(f"    - {c['name']}  productCode={c.get('productCode')}  "
                  f"reportingId={c.get('reportingDimensionId')}")
            units = api(f"/accounts/{acc_id}/adclients/{client_id}/adunits").get("adUnits", [])
            print(f"      ad units ({len(units)}):")
            for u in units:
                print(f"        - {u.get('displayName')}  state={u.get('state')}  "
                      f"id={u['name'].split('/')[-1]}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("auth")
    p.add_argument("--port", type=int, default=None)
    p.set_defaults(func=cmd_auth)

    p = sub.add_parser("accounts")
    p.set_defaults(func=cmd_accounts)

    p = sub.add_parser("sites")
    p.add_argument("--account", required=True)
    p.set_defaults(func=cmd_sites)

    p = sub.add_parser("adclients")
    p.add_argument("--account", required=True)
    p.set_defaults(func=cmd_adclients)

    p = sub.add_parser("adunits")
    p.add_argument("--account", required=True)
    p.add_argument("--adclient", required=True)
    p.set_defaults(func=cmd_adunits)

    p = sub.add_parser("audit")
    p.set_defaults(func=cmd_audit)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
