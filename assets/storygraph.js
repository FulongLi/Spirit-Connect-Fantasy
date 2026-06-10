/* ═══════════════════════════════════════════════════════
   SPIRIT CONNECT — Story Graph engine
   Obsidian / Connected-Papers style force-directed graph:
   drag nodes, pan, zoom, hover to light up neighbours,
   click for details, filter by node type.
   ═══════════════════════════════════════════════════════ */
(function () {
  'use strict';

  window.initStoryGraph = function (cfg) {
    var wrap = document.getElementById(cfg.mountId);
    var detail = document.getElementById(cfg.detailId);
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* ── DOM: filter chips + canvas ── */
    var chips = document.createElement('div');
    chips.className = 'sg-chips';
    var hiddenTypes = {};
    Object.keys(cfg.types).forEach(function (ty) {
      var c = document.createElement('button');
      c.type = 'button';
      c.className = 'sg-chip active';
      c.innerHTML = '<span class="sg-chip-dot" style="background:' + cfg.types[ty].color + '"></span>' + cfg.types[ty].label;
      c.addEventListener('click', function () {
        hiddenTypes[ty] = !hiddenTypes[ty];
        c.classList.toggle('active', !hiddenTypes[ty]);
        hover = null; reheat();
      });
      chips.appendChild(c);
    });
    wrap.appendChild(chips);

    var canvas = document.createElement('canvas');
    canvas.className = 'sg-canvas';
    wrap.appendChild(canvas);
    var ctx = canvas.getContext('2d');
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W = 0, H = cfg.height || 620;

    /* ── data ── */
    var nodes = cfg.nodes.map(function (n, i) {
      var a = (i * 137.508) * Math.PI / 180; // golden-angle spread
      var rad = 60 + 14 * Math.sqrt(i);
      return {
        id: n.id, label: n.label, type: n.type, d: n.d || '',
        r: n.r || (n.type === 'book' ? 15 : n.type === 'character' ? 9.5 : 7.5),
        x: Math.cos(a) * rad, y: Math.sin(a) * rad,
        vx: 0, vy: 0, fixed: false
      };
    });
    var byId = {};
    nodes.forEach(function (n) { byId[n.id] = n; });
    var links = cfg.links.map(function (l) {
      return { a: byId[l[0]], b: byId[l[1]] };
    }).filter(function (l) { return l.a && l.b; });
    var neigh = {};
    nodes.forEach(function (n) { neigh[n.id] = {}; });
    links.forEach(function (l) { neigh[l.a.id][l.b.id] = true; neigh[l.b.id][l.a.id] = true; });
    function deg(n) { return Object.keys(neigh[n.id]).length; }
    nodes.forEach(function (n) { n.r += Math.min(4, deg(n) * 0.35); });

    function visible(n) { return !hiddenTypes[n.type]; }

    /* ── camera ── */
    var cam = { x: 0, y: 0, k: 1 };
    function toWorld(px, py) { return { x: (px - W / 2) / cam.k + cam.x, y: (py - H / 2) / cam.k + cam.y }; }

    /* ── simulation ── */
    var alpha = 1;
    function reheat() { alpha = Math.max(alpha, 0.6); }

    function step() {
      var i, j, a, b, dx, dy, d2, d, f;
      // repulsion
      for (i = 0; i < nodes.length; i++) {
        a = nodes[i]; if (!visible(a)) continue;
        for (j = i + 1; j < nodes.length; j++) {
          b = nodes[j]; if (!visible(b)) continue;
          dx = a.x - b.x; dy = a.y - b.y;
          d2 = dx * dx + dy * dy + 0.01;
          if (d2 > 90000) continue;
          f = 1300 / d2;
          d = Math.sqrt(d2);
          dx /= d; dy /= d;
          a.vx += dx * f; a.vy += dy * f;
          b.vx -= dx * f; b.vy -= dy * f;
        }
      }
      // springs
      links.forEach(function (l) {
        if (!visible(l.a) || !visible(l.b)) return;
        dx = l.b.x - l.a.x; dy = l.b.y - l.a.y;
        d = Math.sqrt(dx * dx + dy * dy) + 0.01;
        var target = 95 + (l.a.r + l.b.r) * 1.6;
        f = (d - target) * 0.012;
        dx /= d; dy /= d;
        l.a.vx += dx * f * d * 0.02 + dx * f;
        l.a.vy += dy * f * d * 0.02 + dy * f;
        l.b.vx -= dx * f * d * 0.02 + dx * f;
        l.b.vy -= dy * f * d * 0.02 + dy * f;
      });
      // gravity to centre
      nodes.forEach(function (n) {
        if (!visible(n)) return;
        n.vx -= n.x * 0.004; n.vy -= n.y * 0.004;
        if (!n.fixed) {
          n.vx *= 0.86; n.vy *= 0.86;
          n.x += n.vx * alpha; n.y += n.vy * alpha;
        } else { n.vx = 0; n.vy = 0; }
      });
      alpha = Math.max(0.06, alpha * 0.985);
    }

    /* ── interaction state ── */
    var hover = null, dragging = null, panning = false;
    var lastP = null, downP = null, moved = false;

    function pick(px, py) {
      var w = toWorld(px, py), best = null, bd = 1e9;
      nodes.forEach(function (n) {
        if (!visible(n)) return;
        var dx = n.x - w.x, dy = n.y - w.y, dd = dx * dx + dy * dy;
        var rr = (n.r + 6) / 1; // world units
        if (dd < rr * rr && dd < bd) { bd = dd; best = n; }
      });
      return best;
    }

    function pos(e) {
      var r = canvas.getBoundingClientRect();
      var t = e.touches ? e.touches[0] : e;
      return { x: t.clientX - r.left, y: t.clientY - r.top };
    }

    function down(e) {
      var p = pos(e); lastP = p; downP = p; moved = false;
      var n = pick(p.x, p.y);
      if (n) { dragging = n; n.fixed = true; }
      else panning = true;
      if (e.touches) e.preventDefault();
    }
    function move(e) {
      var p = pos(e);
      if (dragging) {
        var w = toWorld(p.x, p.y);
        dragging.x = w.x; dragging.y = w.y; reheat();
        moved = moved || Math.abs(p.x - downP.x) + Math.abs(p.y - downP.y) > 4;
      } else if (panning) {
        cam.x -= (p.x - lastP.x) / cam.k; cam.y -= (p.y - lastP.y) / cam.k;
        moved = true;
      } else {
        var n = pick(p.x, p.y);
        if (n !== hover) { hover = n; }
        canvas.style.cursor = n ? 'pointer' : 'grab';
      }
      lastP = p;
      if (e.touches) e.preventDefault();
    }
    function up() {
      if (dragging) {
        if (!moved) { select(dragging); }
        dragging.fixed = false; dragging = null;
      }
      panning = false;
    }
    canvas.addEventListener('mousedown', down);
    canvas.addEventListener('mousemove', move);
    window.addEventListener('mouseup', up);
    canvas.addEventListener('touchstart', down, { passive: false });
    canvas.addEventListener('touchmove', move, { passive: false });
    canvas.addEventListener('touchend', up);
    canvas.addEventListener('wheel', function (e) {
      e.preventDefault();
      var p = pos(e), before = toWorld(p.x, p.y);
      cam.k = Math.min(2.6, Math.max(0.35, cam.k * (e.deltaY < 0 ? 1.12 : 0.89)));
      var after = toWorld(p.x, p.y);
      cam.x += before.x - after.x; cam.y += before.y - after.y;
    }, { passive: false });
    canvas.addEventListener('mouseleave', function () { hover = null; });

    var selected = null;
    function select(n) {
      selected = n;
      var ty = cfg.types[n.type];
      detail.innerHTML =
        '<div class="sl-detail-inner">' +
        '<span class="sl-detail-meta" style="color:' + ty.color + '">' + ty.label +
        ' · ' + cfg.connLabel + ' ' + deg(n) + '</span>' +
        '<h3>' + n.label + '</h3><p>' + n.d + '</p></div>';
    }

    /* ── render ── */
    function resize() {
      W = wrap.clientWidth;
      canvas.width = W * dpr; canvas.height = H * dpr;
      canvas.style.width = W + 'px'; canvas.style.height = H + 'px';
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    window.addEventListener('resize', function () { resize(); });

    function render() {
      ctx.clearRect(0, 0, W, H);
      ctx.save();
      ctx.translate(W / 2, H / 2);
      ctx.scale(cam.k, cam.k);
      ctx.translate(-cam.x, -cam.y);

      var focus = hover || null;
      var inFocus = function (n) {
        if (!focus) return true;
        return n === focus || neigh[focus.id][n.id];
      };

      /* links */
      links.forEach(function (l) {
        if (!visible(l.a) || !visible(l.b)) return;
        var lit = focus && (l.a === focus || l.b === focus);
        ctx.strokeStyle = lit ? 'rgba(94,249,255,0.85)' : (focus ? 'rgba(140,160,200,0.05)' : 'rgba(140,160,200,0.22)');
        ctx.lineWidth = (lit ? 1.6 : 1) / cam.k;
        ctx.beginPath();
        ctx.moveTo(l.a.x, l.a.y);
        ctx.lineTo(l.b.x, l.b.y);
        ctx.stroke();
      });

      /* nodes */
      nodes.forEach(function (n) {
        if (!visible(n)) return;
        var c = cfg.types[n.type].color;
        var dim = focus && !inFocus(n);
        ctx.globalAlpha = dim ? 0.12 : 1;
        ctx.shadowColor = c;
        ctx.shadowBlur = (n === focus || n === selected) ? 22 : 10;
        ctx.fillStyle = c;
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
        if (n === selected) {
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1.6 / cam.k;
          ctx.beginPath();
          ctx.arc(n.x, n.y, n.r + 3.5, 0, Math.PI * 2);
          ctx.stroke();
        }
        /* label */
        var la = dim ? 0.06 : (focus || cam.k > 0.8 || n.type === 'book' || n.r > 10 ? 0.8 : 0.45);
        ctx.globalAlpha = la;
        ctx.fillStyle = '#dbe5f5';
        ctx.font = (n.type === 'book' ? 13 : 11) / Math.sqrt(cam.k) + 'px "Space Grotesk", sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(n.label, n.x, n.y + n.r + 14 / Math.sqrt(cam.k));
        ctx.globalAlpha = 1;
      });
      ctx.restore();
    }

    var running = true;
    function loop() {
      if (alpha > 0.061 || dragging) step();
      render();
      if (running) requestAnimationFrame(loop);
    }
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) running = false;
      else if (!running) { running = true; requestAnimationFrame(loop); }
    });

    resize();
    if (reduce) { for (var s = 0; s < 300; s++) step(); alpha = 0.06; }
    loop();
    detail.innerHTML = '<p class="sl-hint">' + cfg.hint + '</p>';
  };
})();
