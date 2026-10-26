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
