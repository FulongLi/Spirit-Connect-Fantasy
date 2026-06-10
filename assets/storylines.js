/* ═══════════════════════════════════════════════════════
   SPIRIT CONNECT — Story Lines engine
   Left: book shelf. Click a book → an animated line grows
   left-to-right with branches; nodes = major story events.
   ═══════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var NS = 'http://www.w3.org/2000/svg';

  function el(tag, attrs, parent) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }

  window.initStorylines = function (cfg) {
    var canvas = document.getElementById(cfg.canvasId);
    var detail = document.getElementById(cfg.detailId);
    var list = document.getElementById(cfg.listId);
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var current = null;

    /* ── book shelf ── */
    cfg.books.forEach(function (book) {
      var card = document.createElement('button');
      card.type = 'button';
      card.className = 'sl-book';
      card.style.setProperty('--accent', book.accent);
      card.innerHTML =
        '<span class="sl-book-glyph">' + book.glyph + '</span>' +
        '<span class="sl-book-meta"><strong>' + book.title + '</strong>' +
        '<em>' + book.subtitle + '</em>' +
        '<span class="sl-book-status">' + book.status + '</span></span>';
      card.addEventListener('click', function () { select(book, card); });
      list.appendChild(card);
    });
    if (cfg.lockedCard) {
      var lk = document.createElement('div');
      lk.className = 'sl-book sl-locked';
      lk.innerHTML = '<span class="sl-book-glyph">···</span>' +
        '<span class="sl-book-meta"><strong>' + cfg.lockedCard + '</strong></span>';
      list.appendChild(lk);
    }

    function select(book, card) {
      if (current === book) return;
      current = book;
      Array.prototype.forEach.call(list.children, function (c) { c.classList.remove('active'); });
      if (card) card.classList.add('active');
      detail.innerHTML = '<p class="sl-hint">' + cfg.hint + '</p>';
      draw(book);
    }

    function showDetail(book, node, context) {
      detail.innerHTML =
        '<div class="sl-detail-inner">' +
        '<span class="sl-detail-meta" style="color:' + book.accent + '">' +
        book.title + ' · ' + context + '</span>' +
        '<h3>' + node.t + '</h3>' +
        '<p>' + (node.d || '') + '</p></div>';
    }

    /* ── timeline drawing ── */
    function draw(book) {
      canvas.innerHTML = '';
      var n = book.nodes.length;
      var SP = 110, X0 = 80, Y = 290, H = 560;
      var lastX = X0 + (n - 1) * SP;
      (book.branches || []).forEach(function (br) {
        var bx = X0 + br.from * SP + 50 + (br.nodes.length - 1) * 95;
        if (bx > lastX) lastX = bx;
      });
      var W = lastX + 110;

      var svg = el('svg', { viewBox: '0 0 ' + W + ' ' + H, width: W, height: H, class: 'sl-svg' }, null);
      canvas.appendChild(svg);
      var defs = el('defs', {}, svg);
      defs.innerHTML =
        '<filter id="slglow" x="-80%" y="-80%" width="260%" height="260%">' +
        '<feGaussianBlur stdDeviation="3.5" result="b"/>' +
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>';

      var ac = book.accent;
      var T = reduce ? 0 : 1800;

      /* main line */
      var main = el('path', {
        d: 'M ' + X0 + ' ' + Y + ' L ' + (X0 + (n - 1) * SP) + ' ' + Y,
        stroke: ac, 'stroke-width': 2.5, fill: 'none',
        filter: 'url(#slglow)', 'stroke-linecap': 'round'
      }, svg);
      if (!reduce) {
        var mlen = main.getTotalLength();
        main.style.strokeDasharray = mlen;
        main.style.strokeDashoffset = mlen;
        main.getBoundingClientRect();
        main.style.transition = 'stroke-dashoffset ' + T + 'ms cubic-bezier(.4,0,.2,1)';
        main.style.strokeDashoffset = '0';
      }

      /* main nodes */
      book.nodes.forEach(function (node, i) {
        var x = X0 + i * SP;
        var g = el('g', { class: 'sl-n', tabindex: 0 }, svg);
        el('circle', { cx: x, cy: Y, r: 18, fill: 'transparent' }, g);
        el('circle', { cx: x, cy: Y, r: 6, fill: '#0f1b2d', stroke: ac, 'stroke-width': 2, class: 'sl-dot', filter: 'url(#slglow)' }, g);
        var above = (i % 2 === 0);
        var t = el('text', { x: x, y: above ? Y - 22 : Y + 36, 'text-anchor': 'middle', class: 'sl-label' }, g);
        t.textContent = node.t;
        var delay = n > 1 ? (i / (n - 1)) * T : 0;
        g.style.opacity = 0;
        g.style.transition = 'opacity .45s ease ' + delay + 'ms';
        requestAnimationFrame(function () { g.style.opacity = 1; });
        g.addEventListener('click', function () { activate(g); showDetail(book, node, cfg.mainLabel); });
        g.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); g.click(); } });
      });

      /* branches */
      (book.branches || []).forEach(function (br) {
        var sx = X0 + br.from * SP;
        var dir = br.dir === 'up' ? -1 : 1;
        var by = Y + dir * 88;
        var endX = sx + 50 + (br.nodes.length - 1) * 95;
        var bdelay = n > 1 ? (br.from / (n - 1)) * T : 0;

        var p = el('path', {
          d: 'M ' + sx + ' ' + Y + ' L ' + (sx + 50) + ' ' + by + ' L ' + endX + ' ' + by,
          stroke: ac, 'stroke-width': 1.6, fill: 'none', opacity: .7, 'stroke-linecap': 'round'
        }, svg);
        if (!reduce) {
          var plen = p.getTotalLength();
          p.style.strokeDasharray = plen;
          p.style.strokeDashoffset = plen;
          p.getBoundingClientRect();
          p.style.transition = 'stroke-dashoffset 900ms ease ' + bdelay + 'ms';
          p.style.strokeDashoffset = '0';
        }

        var bl = el('text', { x: endX + 14, y: by + 4, class: 'sl-branch-label', fill: ac }, svg);
        bl.textContent = br.label;
        bl.style.opacity = 0;
        bl.style.transition = 'opacity .5s ease ' + (bdelay + 600) + 'ms';
        requestAnimationFrame(function () { bl.style.opacity = .85; });

        br.nodes.forEach(function (node, j) {
          var x = sx + 50 + j * 95;
          var g = el('g', { class: 'sl-n sl-bn', tabindex: 0 }, svg);
          el('circle', { cx: x, cy: by, r: 14, fill: 'transparent' }, g);
          el('circle', { cx: x, cy: by, r: 4.5, fill: '#0f1b2d', stroke: ac, 'stroke-width': 1.6, class: 'sl-dot' }, g);
          var t = el('text', { x: x, y: dir < 0 ? by - 14 : by + 24, 'text-anchor': 'middle', class: 'sl-label sl-label-sm' }, g);
          t.textContent = node.t;
          var d2 = bdelay + 300 + (reduce ? 0 : j * 140);
          g.style.opacity = 0;
          g.style.transition = 'opacity .4s ease ' + d2 + 'ms';
          requestAnimationFrame(function () { g.style.opacity = 1; });
          g.addEventListener('click', function () { activate(g); showDetail(book, node, br.label); });
          g.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); g.click(); } });
        });
      });

      function activate(g) {
        Array.prototype.forEach.call(svg.querySelectorAll('.sl-n.active'), function (x) { x.classList.remove('active'); });
        g.classList.add('active');
      }
      canvas.scrollLeft = 0;
    }

    if (cfg.books.length) select(cfg.books[0], list.children[0]);
  };
})();
