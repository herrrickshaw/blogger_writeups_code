// Accessibility audit of the article-index fragment: axe-core at desktop and phone width, plus link-target size,
// heading skips, tiny text and no-JS checks. Usage (needs `npm i playwright axe-core` somewhere on the path):
//   node tools/a11y/index_audit.js out/article-index-updated.html after
// Prints the metrics and any axe violations; writes report_<tag>.json to the temp directory.
const { chromium } = require('playwright');
const fs = require('fs');
const os = require('os');
const path = require('path');
const TMP = os.tmpdir();
const file = process.argv[2]; const tag = process.argv[3] || 'x';
const body = fs.readFileSync(file, 'utf8');
const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Index</title></head><body><main>${body}</main></body></html>`;
const WRAPPED = path.join(TMP, `wrapped_${tag}.html`);
fs.writeFileSync(WRAPPED, html);
(async () => {
  const browser = await chromium.launch();
  const out = {};
  for (const [name, vp, js] of [['desktop', {width: 1280, height: 900}, true], ['phone', {width: 375, height: 800}, true], ['nojs', {width: 1280, height: 900}, false]]) {
    const ctx = await browser.newContext({ viewport: vp, javaScriptEnabled: js, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    // block network so external scripts (accordion.js, Blogger feeds) do not run
    await page.route('**/*', r => r.request().url().startsWith('file:') ? r.continue() : r.abort());
    await page.goto('file://' + WRAPPED, { waitUntil: 'load' });
    const t0 = Date.now();
    if (js) { await page.addScriptTag({ path: require.resolve('axe-core/axe.min.js') }); }
    let axeRes = null;
    if (js) axeRes = await page.evaluate(async () => await axe.run(document, { resultTypes: ['violations'] }));
    const m = await page.evaluate(() => {
      const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
      const links = [...document.querySelectorAll('a[href]')].filter(vis);
      const small = links.filter(a => { const r = a.getBoundingClientRect(); return r.height < 24 || r.width < 24; });
      const names = {}; links.forEach(a => { const k = a.textContent.trim().replace(/\s+/g, ' ') + '|' + a.getAttribute('href'); names[k] = (names[k] || 0) + 1; });
      const sameTextDiffHref = {}; links.forEach(a => { const k = a.textContent.trim().replace(/\s+/g, ' '); (sameTextDiffHref[k] = sameTextDiffHref[k] || new Set()).add(a.getAttribute('href')); });
      const ambiguous = Object.entries(sameTextDiffHref).filter(([k, v]) => v.size > 1 && k.length).length;
      const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => +h.tagName[1]); let skips = 0; for (let i = 1; i < hs.length; i++) if (hs[i] - hs[i - 1] > 1) skips++;
      const overflowX = document.documentElement.scrollWidth > window.innerWidth + 1;
      const tinyText = [...document.querySelectorAll('a,p,li,span,summary,label,button,td,th')].filter(e => vis(e) && e.children.length === 0 && e.textContent.trim().length > 2 && parseFloat(getComputedStyle(e).fontSize) < 12).length;
      return { dom: document.querySelectorAll('*').length, links: links.length, smallTargets: small.length, ambiguousLinkTexts: ambiguous, headingSkips: skips, overflowX, tinyTextNodes: tinyText, textLen: document.body.innerText.length, lang: document.documentElement.lang };
    });
    out[name] = { metrics: m, axe: axeRes ? axeRes.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, help: v.help, sample: v.nodes.slice(0, 2).map(n => n.target.join(' ') + ' :: ' + (n.failureSummary || '').split('\n').slice(1, 3).join(' / ')) })) : 'not run (no JS)' };
    await ctx.close();
  }
  await browser.close();
  fs.writeFileSync(path.join(TMP, `report_${tag}.json`), JSON.stringify(out, null, 1));
  for (const [k, v] of Object.entries(out)) { console.log('==', k, JSON.stringify(v.metrics)); if (Array.isArray(v.axe)) v.axe.forEach(a => console.log('  AXE', a.impact, a.id, a.nodes, a.help, '\n     ', a.sample.join('\n      '))); else console.log('  axe:', v.axe); }
})();
