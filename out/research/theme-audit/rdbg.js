const { chromium } = require('playwright'); const fs = require('fs'); const R = '/home/user/blogger_writeups_code';
const theme = fs.readFileSync(R + '/theme/theme.xml', 'utf8'); const skin = theme.slice(theme.indexOf('<b:skin><![CDATA[') + 17, theme.indexOf(']]></b:skin>')) + (process.env.EXTRA ? fs.readFileSync(process.env.EXTRA, 'utf8') : '');
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell' });
 const agg = {};
 for (const slug of fs.readFileSync(process.argv[2], 'utf8').trim().split('\n')) {
  const f = process.cwd() + '/r-' + process.pid + '.html'; fs.writeFileSync(f, `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>${skin}</style></head><body><div class="wrap"><div class="widget Blog" id="Blog1"><div class="post-body">${fs.readFileSync(`${R}/posts/${slug}.html`, 'utf8')}</div></div></div></body></html>`);
  const p = await b.newPage({ viewport: { width: 1024, height: 900 } }); await p.route('**/*', r => r.request().url().startsWith('file:') ? r.continue() : r.abort());
  await p.goto('file://' + f, { waitUntil: 'load' }); await p.waitForTimeout(80);
  const r = await p.evaluate(() => { const pb = document.querySelector('.post-body'); const o = [];
   const lum = c => { const m = c.match(/[\d.]+/g); if (!m) return null; const [r, g, b2, a] = m.map(Number); if (a === 0) return null; return [r, g, b2].map(v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }).reduce((s, v, i) => s + v * [.2126, .7152, .0722][i], 0); };
   const bgOf = el => { for (let a = el; a; a = a.parentElement) { const c = getComputedStyle(a).backgroundColor; const m = c.match(/[\d.]+/g); if (m && (m.length < 4 || +m[3] > .5)) return c; } return 'rgb(255,255,255)'; };
   const desc = el => { const pe = el.parentElement; return el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).split(' ')[0] : '') + '<' + pe.tagName.toLowerCase() + (pe.className ? '.' + String(pe.className).split(' ')[0] : ''); };
   for (const el of pb.querySelectorAll('p,li')) { if (el.closest('table,nav,.gs-a11y-bar,svg')) continue; const t = el.textContent.trim(); if (t.length < 120) continue;
    const cs = getComputedStyle(el), fs = parseFloat(cs.fontSize), lh = parseFloat(cs.lineHeight) || fs * 1.2, h = el.getBoundingClientRect().height, lines = Math.max(1, Math.round((h - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom)) / lh));
    const L1 = lum(cs.color), L2 = lum(bgOf(el)); const cr = L1 == null || L2 == null ? 21 : (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
    if (fs < 15) o.push('small ' + desc(el) + ' ' + fs);
    if (cr < 4.5) o.push('lowC ' + desc(el) + ' ' + cs.color + ' ' + cr.toFixed(2));
    if (lines > 1 && t.length / lines > 95) o.push('long ' + desc(el) + ' mw=' + cs.maxWidth);
   } return o; });
  for (const x of r) { const k = x.split(' ').slice(0, 2).join(' ') + (x.startsWith('lowC') ? ' ' + x.split(' ').slice(2, -1).join(' ') : ''); agg[k] = agg[k] || new Set(); agg[k].add(slug); }
  await p.close(); }
 Object.entries(agg).sort((a, b) => b[1].size - a[1].size).slice(0, 40).forEach(([k, v]) => console.log(v.size, k));
 await b.close(); })();
