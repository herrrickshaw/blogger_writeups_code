const { chromium } = require('playwright'); const fs = require('fs'); const R = '/home/user/blogger_writeups_code';
const sk = f => { const t = fs.readFileSync(f, 'utf8'); return t.slice(t.indexOf('<b:skin><![CDATA[') + 17, t.indexOf(']]></b:skin>')); };
const html = `<header class="site-head"><div class="wrap"><a class="site-title" href="#">Masala <span>Deutsch</span></a><div class="site-nav"><a href="#">Home</a><a href="#">Article index</a><a href="#">About</a></div></div></header>
<div class="hero-section"><div class="hero"><div class="wrap"><div class="kicker">Featured</div><h2><a href="#">A <strong>headline</strong></a></h2><p>Standfirst text for the hero.</p><a class="more" href="#">Read</a></div></div></div>
<div class="wrap"><div class="main"><div class="widget Blog" id="Blog1"><div class="section-label">Recent analysis</div>
<div class="card"><h3><a href="#">Card one</a></h3><div class="meta">Oct 26</div><p>Snippet text that runs for a while to wrap a couple of lines on a phone screen.</p><a class="more" href="#">Read the piece</a></div>
<div class="card"><h3><a href="#">Card two</a></h3><div class="meta">Oct 25</div><p>Snippet.</p><a class="more" href="#">Read the piece</a></div>
<div class="pager"><a href="#">Newer</a><a href="#">Older</a></div></div></div></div><footer class="site-foot"><div class="wrap">Footer</div></footer>`;
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell' });
 for (const w of [375, 1024]) { const out = [];
  for (const s of [sk(R + '/theme/base.xml'), sk(R + '/theme/theme.xml')]) { const p = await b.newPage({ viewport: { width: w, height: 900 } });
   await p.setContent(`<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>${s}</style></head><body>${html}</body></html>`);
   out.push(await p.evaluate(() => [...document.body.querySelectorAll('*')].map(e => { const c = getComputedStyle(e), r = e.getBoundingClientRect(); return e.tagName + '.' + e.className + ' ' + [c.font, c.color, c.backgroundColor, c.padding, c.margin, c.border, Math.round(r.width), Math.round(r.height)].join('|'); })));
   if (w === 375) out.push(await p.evaluate(() => [...document.querySelectorAll('.site-nav a')].map(a => Math.round(a.getBoundingClientRect().height)).join(',')));
   await p.close(); }
  const [a, , bb] = w === 375 ? out : [out[0], null, out[1]]; const d = a.map((x, i) => x !== bb[i] ? x.split(' ')[0] + '\n   old ' + x.slice(x.indexOf(' ')) + '\n   new ' + bb[i].slice(bb[i].indexOf(' ')) : null).filter(Boolean);
  console.log(w, 'differing elements:', d.length); d.slice(0, 8).forEach(x => console.log(' ', x)); if (w === 375) console.log(' nav link heights old', out[1], 'new', out[3]); }
 await b.close(); })();
