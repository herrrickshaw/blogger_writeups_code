/* gs-content-guard-v2 (2026-10-26) — replaces gs-table-guard-v1; pairs with
   gs-table-template-v1 and gs-readable-v1 in the theme skin.
   1. Tables: wraps each post table, marks number cells for right alignment.
   2. Auto ads: an ad container that AdSense inserts inside a structure that it
      breaks is moved to just after the outermost such structure. Structures: tables,
      lists, figures, code blocks, collapsible sections, quotes, side-by-side layouts
      (row flex, multi-column grid), boxes that clip their content, and boxed notes
      and cards (tinted, framed or accent-ruled) that are not most of the post.
   3. An ad placed directly after a heading is moved above the heading, so a heading
      is never separated from the text it introduces. */
(function () {
  var WRAP = '.gb-tblwrap,.tw,.gs-tblwrap';
  var NUM = /^[\s(]*[-+−–~≈<>]?\s*(?:Rs\.?|₹|\$|€|£|¥)?\s*[-+−–]?\d[\d,.\s]*(?:%|x|×|pp|bn|mn|cr|crore|lakh|MW|GW|kt|Mt|t)?\s*(?:\([^)]{0,12}\))?\s*[)*†‡]*$/i;
  var HOLD = 'table,ul,ol,dl,figure,pre,details,blockquote';

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

  function opaque(c) {
    var m = c.match(/[\d.]+/g);
    return !!m && (m.length < 4 || +m[3] > 0.1) && !(+m[0] > 250 && +m[1] > 250 && +m[2] > 250);
  }

  // Does this element break up an ad placed inside it? A boxed element (tinted, framed
  // or with an accent rule) counts too, since an ad inside a note or card reads as part
  // of it; but not a box that holds most of the post, or every ad would sink to the end.
  function holds(el, bodyH) {
    if (el.matches(HOLD)) return true;
    var s = getComputedStyle(el);
    if (/flex/.test(s.display) && !/column/.test(s.flexDirection) && el.children.length > 2) return true;
    if (/grid/.test(s.display) && s.gridTemplateColumns.split(' ').length > 1) return true;
    if (s.overflowY !== 'visible' && (s.maxHeight !== 'none' || el.style.height)) return true;
    var boxed = opaque(s.backgroundColor) || (parseFloat(s.borderLeftWidth) > 0 && parseFloat(s.borderRightWidth) > 0) ||
                parseFloat(s.borderLeftWidth) >= 3;
    return boxed && el.getBoundingClientRect().height < 0.6 * bodyH;
  }

  function place(ad) {
    var body = ad.closest('.post-body');
    if (!body) return;
    var out = null, bodyH = body.getBoundingClientRect().height;
    for (var a = ad.parentElement; a && a !== body; a = a.parentElement) if (holds(a, bodyH)) out = a;
    if (out) {
      out = out.closest(WRAP) && body.contains(out.closest(WRAP)) ? out.closest(WRAP) : out;
      out.parentNode.insertBefore(ad, out.nextSibling);
    }
    var prev = ad.previousElementSibling;
    if (prev && /^H[2-4]$/.test(prev.tagName)) prev.parentNode.insertBefore(ad, prev);
  }

  function run() {
    var ts = document.querySelectorAll('.post-body table');
    for (var i = 0; i < ts.length; i++) prep(ts[i]);
    var ads = document.querySelectorAll('.post-body .google-auto-placed');
    for (var j = 0; j < ads.length; j++) place(ads[j]);
  }

  new MutationObserver(function (muts) {
    for (var i = 0; i < muts.length; i++) {
      var added = muts[i].addedNodes;
      for (var k = 0; k < added.length; k++) {
        var n = added[k];
        if (n.nodeType !== 1) continue;
        if (n.matches('.google-auto-placed')) { place(n); continue; }
        var inner = n.querySelectorAll('.google-auto-placed');
        for (var q = 0; q < inner.length; q++) place(inner[q]);
        if (n.matches('table')) prep(n);
        var nt = n.querySelectorAll('table');
        for (var z = 0; z < nt.length; z++) prep(nt[z]);
      }
    }
  }).observe(document.documentElement, { childList: true, subtree: true });

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
})();
