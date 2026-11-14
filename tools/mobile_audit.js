#!/usr/bin/env node
/* Phone-readability audit (docs/MOBILE_READABILITY.md). Renders post bodies at 375px inside the theme's own
   CSS and scripts, taken from theme/theme.xml, and measures what a phone reader actually gets.

     node tools/mobile_audit.js                          all of posts/: summary + the 25 worst posts
     node tools/mobile_audit.js --json out.json          also write every post's measurements
     node tools/mobile_audit.js out/update-x.html --shot x.png
                                                         one file: measurements + a full-page screenshot

   Needs the pre-installed Playwright (require('playwright')); no network: every request is blocked. */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const args = process.argv.slice(2);
const opt = (k) => { const i = args.indexOf(k); return i >= 0 ? args.splice(i, 2)[1] : null; };
const jsonOut = opt('--json'), shot = opt('--shot');
const W = +(opt('--width') || 375);

function themeParts() {
  const t = fs.readFileSync(path.join(ROOT, 'theme/theme.xml'), 'utf8');
  const un = (s) => s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&amp;/g, '&');
  const skin = (t.match(/<b:skin[^>]*><!\[CDATA\[([\s\S]*?)\]\]><\/b:skin>/) || [, ''])[1];
  const css = un(skin.replace(/\$\([^)]*\)/g, 'inherit'));
  const js = [...t.matchAll(/<script>\/\/<!\[CDATA\[([\s\S]*?)\/\/\]\]><\/script>/g)].map((m) => m[1]).join('\n;\n');
  return { css, js };
}

function measure() {
  const W = innerWidth, root = document.querySelector('.post-body');
  const scroller = (e) => { for (let a = e.parentElement; a && a !== document.body; a = a.parentElement) { const s = getComputedStyle(a).overflowX; if (s === 'auto' || s === 'scroll') return a; } return null; };
  const tables = [...root.querySelectorAll('table')].map((t) => { const s = scroller(t); return !!(s && s.scrollWidth > s.clientWidth + 2); });
  const charts = [...root.querySelectorAll('svg')].filter((s) => s.getBoundingClientRect().width > 120).map((s) => {
    const vb = s.viewBox && s.viewBox.baseVal, k = vb && vb.width ? s.getBoundingClientRect().width / vb.width : 1;
    const f = [...s.querySelectorAll('text')].map((t) => parseFloat(getComputedStyle(t).fontSize) * k).filter((x) => x > 0).sort((a, b) => a - b);
    return f.length ? f[f.length >> 1] : null;
  }).filter((x) => x !== null);
  const paras = [...root.querySelectorAll('p')].map((p) => p.innerText.trim().split(/\s+/).length);
  return {
    pageWidth: document.documentElement.scrollWidth, wide: document.documentElement.scrollWidth > W + 1,
    swipeTables: tables.filter(Boolean).length, tables: tables.length,
    smallCharts: charts.filter((x) => x < 9.5).length, charts: charts.length,
    longParas: paras.filter((n) => n > 90).length, words: root.innerText.split(/\s+/).length,
  };
}

(async () => {
  const { css, js } = themeParts();
  const files = args.length ? args : fs.readdirSync(path.join(ROOT, 'posts')).filter((f) => f.endsWith('.html')).map((f) => path.join(ROOT, 'posts', f));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: W, height: 900 } });
  await p.route('**/*', (r) => r.abort());
  const out = [];
  for (const f of files) {
    const body = fs.readFileSync(f, 'utf8');
    await p.setContent(`<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><style>body{margin:0;padding:0 16px;background:#fff}${css}</style>`
      + `<div id=Blog1><div class="post-body entry-content">${body}</div></div><script>try{${js}}catch(e){}</script>`, { waitUntil: 'load' });
    out.push({ file: path.relative(ROOT, f), ...(await p.evaluate(measure)) });
    if (shot) await p.screenshot({ path: shot, fullPage: true });
  }
  await b.close();
  if (jsonOut) fs.writeFileSync(jsonOut, JSON.stringify(out, null, 1));
  const sum = (k) => out.reduce((a, x) => a + x[k], 0);
  console.log(`${out.length} posts at ${W}px | pages wider than the screen: ${out.filter((x) => x.wide).length}`
    + ` | charts with labels under 9.5px: ${sum('smallCharts')} of ${sum('charts')}`
    + ` | tables that need swiping: ${sum('swipeTables')} of ${sum('tables')}`
    + ` | posts with 3+ paragraphs over 90 words: ${out.filter((x) => x.longParas >= 3).length}`);
  const score = (x) => 3 * x.smallCharts + 2 * x.swipeTables + x.longParas + (x.wide ? 10 : 0);
  const worst = out.filter((x) => score(x) > 0).sort((a, b) => score(b) - score(a)).slice(0, out.length > 1 ? 25 : 1);
  for (const x of worst) console.log(`  ${String(score(x)).padStart(3)}  ${x.file}  small charts ${x.smallCharts}, swipe tables ${x.swipeTables}, long paragraphs ${x.longParas}${x.wide ? ', TOO WIDE' : ''}`);
})();
