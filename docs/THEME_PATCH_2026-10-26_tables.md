# Theme patch: gs-table-template-v1 + gs-table-guard-v1 (26 Oct 2026)

Fixes tables broken by Auto-ads containers placed inside table rows, hides empty ad boxes,
and gives every post table one readable template. Apply in Blogger > Theme > Customise > Edit HTML.
Do not paste the whole theme (see DESIGN_LOG 2026-08-08); make two insertions.

## Step 1 — CSS: paste immediately BEFORE the single line `]]></b:skin>`

```css
/* gs-table-template-v1 (2026-10-26) — one readable template for every post table,
   and no ad containers inside tables.
   1. Every post table gets the same look: dark header, light row stripes, clear
      padding, text left-aligned, numbers right-aligned in tabular figures. Per-post
      table styles (accent headers, right-aligned text cells) are overridden so a
      reader sees one table style across the blog. Inline row highlights survive.
   2. The gs-table-guard-v1 script wraps unwrapped tables in .gs-tblwrap (scrolls on
      phones), marks number cells .gs-num and moves any Auto-ads container that
      lands inside a table to just after the table.
   3. Empty (unfilled) Auto-ads containers collapse instead of showing an empty
      "Advertisement" box; the label and spacing apply only to filled ads. */
#Blog1 .post-body .gs-tblwrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1.2rem 0}
#Blog1 .post-body table.gs-t{border-collapse:collapse!important;width:100%;max-width:100%;
  font-family:var(--sans);font-size:.88rem;line-height:1.45;font-variant-numeric:tabular-nums;margin:0}
#Blog1 .post-body table.gs-t th,#Blog1 .post-body table.gs-t td{text-align:left!important;
  vertical-align:top;padding:.5rem .7rem!important;border:0!important;
  border-bottom:1px solid #dcdcdc!important;white-space:normal;word-break:normal;overflow-wrap:anywhere}
#Blog1 .post-body table.gs-t thead th,#Blog1 .post-body table.gs-t tr.gs-head>th{
  background:#1f2328!important;color:#fff!important;font-weight:600;vertical-align:bottom}
#Blog1 .post-body table.gs-t tbody tr:nth-child(even)>td{background:#f6f7f8}
#Blog1 .post-body table.gs-t tbody th{background:transparent;color:inherit;font-weight:600}
#Blog1 .post-body table.gs-t .gs-num{text-align:right!important}
#Blog1 .post-body table.gs-t td.gs-num{white-space:nowrap}
#Blog1 .post-body table.gs-t caption{caption-side:top;text-align:left;font-weight:600;padding:0 0 .4rem}
@media (max-width:640px){
  #Blog1 .post-body table.gs-t{font-size:.84rem}
  #Blog1 .post-body .gb-tblwrap>table.gs-t:not(.gs-wide),#Blog1 .post-body .tw>table.gs-t:not(.gs-wide){min-width:0}
  #Blog1 .post-body table.gs-t.gs-wide{min-width:560px}
}
.post-body .google-auto-placed:not(:has(ins[data-ad-status="filled"])){
  margin:0!important;padding:0!important;border:0!important;min-height:0}
.post-body .google-auto-placed:not(:has(ins[data-ad-status="filled"]))::before{content:none}
```

## Step 2 — script: paste immediately BEFORE the final `</body>` (the last one, just above `</html>`)

```html
<script>//<![CDATA[
/* gs-table-guard-v1 (2026-10-26) — pairs with gs-table-template-v1 in the theme skin.
   Wraps each post table, marks number cells for right alignment, and moves any
   Auto-ads container that AdSense inserts inside a table to just after the table,
   where it no longer breaks the rows. */
(function () {
  var WRAP = '.gb-tblwrap,.tw,.gs-tblwrap';
  var NUM = /^[\s(]*[-+−–~≈<>]?\s*(?:Rs\.?|₹|\$|€|£|¥)?\s*[-+−–]?\d[\d,.\s]*(?:%|x|×|pp|bn|mn|cr|crore|lakh|MW|GW|kt|Mt|t)?\s*(?:\([^)]{0,12}\))?\s*[)*†‡]*$/i;

  function outer(t) { return t.closest(WRAP) || t; }

  function evict(ad) {
    var t = ad.parentNode && ad.parentNode.closest ? ad.parentNode.closest('table') : null;
    if (!t) return;
    var o = outer(t);
    if (o.parentNode) o.parentNode.insertBefore(ad, o.nextSibling);
  }

  function prep(t) {
    if (t.classList.contains('gs-t')) return;
    if (!t.closest('.post-body')) return;
    if (!t.closest(WRAP)) {
      var w = document.createElement('div');
      w.className = 'gs-tblwrap';
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    }
    t.classList.add('gs-t');
    var rows = t.rows, ncol = 0, r, c;
    for (r = 0; r < rows.length; r++) ncol = Math.max(ncol, rows[r].cells.length);
    if (ncol >= 4) t.classList.add('gs-wide');
    if (!t.tHead && rows.length && rows[0].cells.length &&
        Array.prototype.every.call(rows[0].cells, function (x) { return x.tagName === 'TH'; })) {
      rows[0].classList.add('gs-head');
    }
    var numCount = [], bodyCount = [], simple = true;
    for (r = 0; r < rows.length; r++) {
      var cells = rows[r].cells;
      for (c = 0; c < cells.length; c++) {
        var cell = cells[c];
        if (cell.colSpan > 1) simple = false;
        if (cell.tagName !== 'TD') continue;
        bodyCount[c] = (bodyCount[c] || 0) + 1;
        var txt = (cell.textContent || '').trim();
        if (txt && txt.length <= 40 && NUM.test(txt)) {
          cell.classList.add('gs-num');
          numCount[c] = (numCount[c] || 0) + 1;
        }
      }
    }
    if (!simple) return;
    var head = t.tHead ? t.tHead.rows : (rows[0] && rows[0].classList.contains('gs-head') ? [rows[0]] : []);
    for (r = 0; r < head.length; r++) {
      for (c = 0; c < head[r].cells.length; c++) {
        if (bodyCount[c] && (numCount[c] || 0) / bodyCount[c] >= 0.6) head[r].cells[c].classList.add('gs-num');
      }
    }
  }

  function run(root) {
    var ts = (root || document).querySelectorAll('.post-body table');
    for (var i = 0; i < ts.length; i++) prep(ts[i]);
    var ads = document.querySelectorAll('.post-body table .google-auto-placed');
    for (var j = 0; j < ads.length; j++) evict(ads[j]);
  }

  new MutationObserver(function (muts) {
    for (var i = 0; i < muts.length; i++) {
      var added = muts[i].addedNodes;
      for (var k = 0; k < added.length; k++) {
        var n = added[k];
        if (n.nodeType !== 1) continue;
        if (n.matches('.google-auto-placed')) evict(n);
        else if (n.querySelector) {
          var inner = n.querySelectorAll('.google-auto-placed');
          for (var q = 0; q < inner.length; q++) evict(inner[q]);
          if (n.matches('table')) prep(n);
          var nt = n.querySelectorAll('table');
          for (var z = 0; z < nt.length; z++) prep(nt[z]);
        }
      }
    }
  }).observe(document.documentElement, { childList: true, subtree: true });

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { run(); });
  else run();
})();
//]]></script>
```

## Step 3 — save, then check a post with tables
- https://masaladeutsch.blogspot.com/2026/10/a-hectare-under-power-line-now-pays.html : the 3-column table should have no
  "Advertisement" row inside it; text left-aligned, the 200 values right-aligned.
- Any ad that AdSense places in a table now appears just below the table.
