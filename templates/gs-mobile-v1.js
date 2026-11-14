/* gs-mobile-v1 (2026-11-15) — phone readability for posts written before the visual-first style.
   Pairs with templates/gs-mobile-v1.css. Measured problem (docs/MOBILE_READABILITY.md): most inline
   SVG charts were drawn about 700 units wide, so on a 375px phone they shrink to half size and
   their labels render at about 6px.
   1. Charts: an inline SVG whose typical label would render below 10px is given the width at which
      it renders at 10px (never more than its natural width) inside a sideways scroller, with a
      one-line "swipe" hint above it. Charts built with tools/exec_viz.py (.xv) are already sized
      for phones and are left alone.
   2. Tables: a table wrapper that still needs sideways scrolling gets the same hint, and the CSS
      keeps its first column in view while it scrolls. */
(function () {
  var MIN_PX = 10;
  var SCROLLS = '.gs-chartscroll,.xv';

  function hint(text, before) {
    var p = document.createElement('p');
    p.className = 'gs-swipe';
    p.setAttribute('aria-hidden', 'true');
    p.textContent = text;
    before.parentNode.insertBefore(p, before);
  }

  function typicalFont(svg) {
    var t = svg.querySelectorAll('text'), a = [], i, f;
    for (i = 0; i < t.length && i < 200; i++) {
      f = parseFloat(window.getComputedStyle(t[i]).fontSize);
      if (f > 0) a.push(f);
    }
    if (!a.length) return 0;
    a.sort(function (x, y) { return x - y; });
    return a[a.length >> 1];
  }

  function scrollsAlready(el) {
    for (var a = el.parentElement; a && !a.classList.contains('post-body'); a = a.parentElement) {
      var o = window.getComputedStyle(a).overflowX;
      if (o === 'auto' || o === 'scroll') return true;
    }
    return false;
  }

  function charts(root) {
    var svgs = root.querySelectorAll('svg[viewBox]'), i;
    for (i = 0; i < svgs.length; i++) {
      var svg = svgs[i];
      if (svg.closest(SCROLLS) || scrollsAlready(svg)) continue;
      var vb = svg.viewBox && svg.viewBox.baseVal;
      if (!vb || vb.width < 300) continue;
      var shown = svg.getBoundingClientRect().width;
      if (shown < 120) continue;
      var f = typicalFont(svg);
      if (!f) continue;
      var need = Math.min(vb.width, vb.width * MIN_PX / f);
      if (need <= shown + 1) continue;
      var wrap = document.createElement('div');
      wrap.className = 'gs-chartscroll';
      wrap.setAttribute('tabindex', '0');
      wrap.setAttribute('role', 'region');
      wrap.setAttribute('aria-label', 'Chart, scrolls sideways');
      svg.parentNode.insertBefore(wrap, svg);
      wrap.appendChild(svg);
      svg.style.width = Math.round(need) + 'px';
      svg.style.maxWidth = 'none';
      svg.style.height = 'auto';
      hint('Swipe sideways to read the whole chart →', wrap);
    }
  }

  function tables(root) {
    var w = root.querySelectorAll('.gs-tblwrap,.gb-tblwrap,.tw'), i;
    for (i = 0; i < w.length; i++) {
      var box = w[i], t = box.querySelector('table');
      if (!t || box.classList.contains('gs-scrolls')) continue;
      var scroller = box.scrollWidth > box.clientWidth + 4 ? box : (t.scrollWidth > t.clientWidth + 4 ? t : null);
      if (!scroller) continue;
      box.classList.add('gs-scrolls');
      hint('Swipe the table sideways for more columns →', box);
    }
  }

  function run() {
    var posts = document.querySelectorAll('.post-body'), i;
    for (i = 0; i < posts.length; i++) {
      try { charts(posts[i]); tables(posts[i]); } catch (e) { /* never break the page */ }
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
  var timer;
  window.addEventListener('resize', function () { clearTimeout(timer); timer = setTimeout(run, 250); });
})();
