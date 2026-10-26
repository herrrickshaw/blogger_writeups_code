// usage: node taudit.js <theme.xml> <guard.js|-> <slugs.txt> <out.jsonl> [extra.css]
const { chromium } = require('playwright'); const fs = require('fs');
const R = '/home/user/blogger_writeups_code';
const [themeFile, guardFile, slugFile, outFile, extraCss] = process.argv.slice(2);
const theme = fs.readFileSync(themeFile, 'utf8');
const skin = theme.slice(theme.indexOf('<b:skin><![CDATA[') + 17, theme.indexOf(']]></b:skin>')) + (extraCss ? fs.readFileSync(extraCss, 'utf8') : '');
const guard = guardFile === '-' ? '' : fs.readFileSync(guardFile, 'utf8');
const slugs = fs.readFileSync(slugFile, 'utf8').trim().split('\n');
const AD = '<div class="google-auto-placed ap_container" style="width:100%;height:auto;clear:both;text-align:center"><ins class="adsbygoogle adsbygoogle-noablate" data-ad-status="filled" data-adsbygoogle-status="done" style="display:block;margin:auto;background-color:transparent;height:280px"><div style="width:100%;height:280px;background:#fc0"></div></ins></div>';
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell' });
  const out = fs.createWriteStream(outFile);
  const file = process.cwd() + '/page-' + process.pid + '.html';
  for (const slug of slugs) {
    const post = fs.readFileSync(`${R}/posts/${slug}.html`, 'utf8');
    fs.writeFileSync(file, `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>${skin}</style></head><body>
<header class="site-head"><div class="wrap"><a class="site-title" href="#">Masala <span>Deutsch</span></a><div class="site-nav"><a href="#">Home</a><a href="#">Article index</a><a href="#">About</a></div></div></header>
<div class="wrap"><div class="main section" id="main"><div class="widget Blog" id="Blog1"><div class="post-head"><h1>Post title</h1><div class="meta">October 26, 2026</div></div>
<div class="post-body">${post}</div><div class="gs-topics"><span class="k">Topics</span><a href="#">Energy &amp; Fuels</a><a href="#">Trade &amp; Tariffs</a></div>
<div class="pager"><a href="#">&#8592; Newer</a><a class="pager-index" href="#">All articles &#183; Index</a><a href="#">Older &#8594;</a></div></div></div></div>
<footer class="site-foot"><div class="wrap">Footer</div></footer><script>${guard}</script></body></html>`);
    for (const w of [375, 1024]) {
      const p = await b.newPage({ viewport: { width: w, height: 900 } });
      await p.route('**/*', r => r.request().url().startsWith('file:') ? r.continue() : r.abort());
      try { await p.goto('file://' + file, { waitUntil: 'load', timeout: 20000 }); } catch (e) {}
      await p.waitForTimeout(120);
      const res = await p.evaluate(async (AD) => {
        const vw = document.documentElement.clientWidth, pb = document.querySelector('.post-body');
        const pbr = pb.getBoundingClientRect();
        const desc = el => el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className.trim() ? '.' + el.className.trim().split(/\s+/)[0] : '');
        const clippedBy = el => { for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) { const s = getComputedStyle(a); if (s.overflowX !== 'visible' || s.overflowY !== 'visible') return a; } return null; };
        // 1. page overflow and its outermost unclipped causes
        const pageOverflow = document.documentElement.scrollWidth - vw;
        const offenders = [];
        if (pageOverflow > 2) for (const el of pb.querySelectorAll('*')) {
          const r = el.getBoundingClientRect(); if (r.right <= vw + 2 || !r.width || clippedBy(el)) continue;
          let par = el.parentElement, outer = true; while (par && par !== pb) { if (par.getBoundingClientRect().right > vw + 2) { outer = false; break; } par = par.parentElement; }
          if (outer) offenders.push(desc(el) + ':' + Math.round(r.right - vw));
        }
        // 2. theme chrome classes reused inside posts (theme rules leak into them)
        const CH = ['card', 'meta', 'more', 'kicker', 'hero', 'wrap', 'slot', 'topics', 'topic', 'pager', 'section-label', 'browse', 'site-head', 'site-foot', 'k'];
        const leak = {}; for (const c of CH) { const n = pb.querySelectorAll('.' + c).length; if (n) leak[c] = n; }
        // 3. inline overflow:hidden boxes turned into scrollers by .post-body div[style*="overflow"]
        let ovhScroll = 0; for (const d of pb.querySelectorAll('div[style*="overflow"]')) { const st = d.getAttribute('style').replace(/\s/g, '');
          if (/overflow(-x)?:hidden/.test(st) && (d.scrollHeight > d.clientHeight + 1 || d.scrollWidth > d.clientWidth + 1) && getComputedStyle(d).overflowX !== 'hidden') ovhScroll++; }
        // 4. media wider than the article column and not inside a scroller
        const media = []; for (const el of pb.querySelectorAll('img,svg,canvas,iframe,video,pre,embed,object')) { if (el.closest('svg') && el.tagName !== 'svg') continue; const r = el.getBoundingClientRect();
          if (r.width && r.right > pbr.right + 2 && !clippedBy(el)) media.push(desc(el) + ':' + Math.round(r.width)); }

        // 6. readability of running text: size, line length, leading, contrast
        const lum = c => { const m = c.match(/[\d.]+/g); if (!m) return null; const [r, g, b2, a] = m.map(Number); if (a === 0) return null; return [r, g, b2].map(v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }).reduce((s, v, i) => s + v * [.2126, .7152, .0722][i], 0); };
        const bgOf = el => { for (let a = el; a; a = a.parentElement) { const c = getComputedStyle(a).backgroundColor; const m = c.match(/[\d.]+/g); if (m && (m.length < 4 || +m[3] > .5)) return c; } return 'rgb(255,255,255)'; };
        const txt = []; for (const el of pb.querySelectorAll('p,li')) { if (el.closest('table,nav,.gs-a11y-bar,svg')) continue; const t = el.textContent.trim(); if (t.length < 120) continue;
          const cs = getComputedStyle(el), fs = parseFloat(cs.fontSize), lh = cs.lineHeight === 'normal' ? fs * 1.2 : parseFloat(cs.lineHeight), h = el.getBoundingClientRect().height;
          const lines = Math.max(1, Math.round((h - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom)) / lh)); const L1 = lum(cs.color), L2 = lum(bgOf(el));
          const cr = L1 == null || L2 == null ? 21 : (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
          txt.push({ fs, lhr: lh / fs, cpl: lines > 1 ? t.length / lines : null, cr }); }
        const med = a => { a = a.filter(x => x != null).sort((x, y) => x - y); return a.length ? a[Math.floor(a.length / 2)] : null; };
        const readab = { n: txt.length, fs: med(txt.map(x => x.fs)), lhr: med(txt.map(x => x.lhr)), cpl: med(txt.map(x => x.cpl)),
          small: txt.filter(x => x.fs < 15).length, long: txt.filter(x => x.cpl && x.cpl > 95).length, tight: txt.filter(x => x.lhr < 1.4).length, lowC: txt.filter(x => x.cr < 4.5).length };
        // 5. simulated Auto ads: one container after the first child of every element with 2+ element children
        const hosts = [...pb.querySelectorAll('*')].filter(e => e.children.length >= 2 && !e.closest('svg,script,style,select,canvas') && !['SCRIPT', 'STYLE', 'SVG', 'svg', 'SELECT', 'COLGROUP', 'THEAD'].includes(e.tagName));
        const pick = hosts.length > 80 ? hosts.filter((_, i) => i % Math.ceil(hosts.length / 80) === 0) : hosts;
        const ads = [];
        for (const h of pick) { const t = document.createElement('template'); t.innerHTML = AD; const ad = t.content.firstChild; ad.dataset.host = desc(h); h.insertBefore(ad, h.children[1]); ads.push(ad); }
        await new Promise(r => setTimeout(r, 60));
        const adOverflow = document.documentElement.scrollWidth - vw;
        const bad = {}, hb = {}; let cur = null; const add = k => { bad[k] = (bad[k] || 0) + 1; const kk = k + '|' + cur; hb[kk] = (hb[kk] || 0) + 1; };
        for (const ad of ads) {
          if (!ad.isConnected) continue; cur = ad.dataset.host + '<' + (ad.parentElement.parentElement ? ad.parentElement.parentElement.tagName.toLowerCase() + '.' + String(ad.parentElement.parentElement.className).split(' ')[0] : '');
          const r = ad.getBoundingClientRect(), par = ad.parentElement, ps = getComputedStyle(par);
          if (ad.closest('table')) add('in-table');
          else if (ad.closest('ul,ol,dl')) add('in-list');
          else if (ad.closest('figure,pre,details,blockquote')) add('in-' + ad.closest('figure,pre,details,blockquote').tagName.toLowerCase());
          if (/flex/.test(ps.display) && !/column/.test(ps.flexDirection)) add('in-row-flex');
          if (/grid/.test(ps.display) && ps.gridTemplateColumns.split(' ').length > 1) add('in-multi-col-grid');
          if (r.width < 300) add('narrower-than-300');
          const c = clippedBy(ad); if (c) { const cr = c.getBoundingClientRect(); if (r.bottom > cr.bottom + 2 || r.right > cr.right + 2 || r.top < cr.top - 2) add('clipped'); }
          if (r.height < 270) add('squashed');
          const pv = ad.previousElementSibling; if (pv && /^H[2-4]$/.test(pv.tagName)) add('right-after-heading');
        }
        return { readab, pageOverflow, offenders: offenders.slice(0, 6), leak, ovhScroll, media: media.slice(0, 6), adsTried: ads.length, adBad: bad, hostBad: hb, adOverflow };
      }, AD);
      out.write(JSON.stringify({ slug, w, ...res }) + '\n');
      await p.close();
    }
  }
  out.end(); await b.close(); fs.unlinkSync(file);
})();
