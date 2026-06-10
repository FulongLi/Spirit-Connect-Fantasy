/* ═══════════════════════════════════════════════════════
   SPIRIT CONNECT — Neural Network Particle Background
   Interactive synaptic web: particles drift, connect, and
   react to the cursor like neurons being scanned.
   ═══════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── Canvas setup ── */
  var canvas = document.createElement('canvas');
  canvas.id = 'neural-bg';
  canvas.setAttribute('aria-hidden', 'true');
  canvas.style.cssText =
    'position:fixed;inset:0;width:100%;height:100%;z-index:-2;pointer-events:none;';
  document.body.prepend(canvas);
  var ctx = canvas.getContext('2d');

  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0;

  /* ── Config ── */
  var CYAN = [0, 229, 255];
  var PURPLE = [124, 77, 255];
  var LINK_DIST = 150;          // max distance for synapse lines
  var MOUSE_RADIUS = 220;       // cursor influence radius
  var particles = [];
  var pulses = [];              // signals travelling along links
  var mouse = { x: -9999, y: -9999, active: false };

  function particleCount() {
    var area = window.innerWidth * window.innerHeight;
    return Math.max(40, Math.min(130, Math.round(area / 14000)));
  }

  function rand(a, b) { return a + Math.random() * (b - a); }

  function makeParticle() {
    var isPurple = Math.random() < 0.22;
    return {
      x: rand(0, W),
      y: rand(0, H),
      vx: rand(-0.22, 0.22),
      vy: rand(-0.22, 0.22),
      r: rand(1.0, 2.4),
      c: isPurple ? PURPLE : CYAN,
      phase: rand(0, Math.PI * 2),       // for glow pulsing
      speed: rand(0.4, 1.1)
    };
  }

  function resize() {
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    var n = particleCount();
    while (particles.length < n) particles.push(makeParticle());
    if (particles.length > n) particles.length = n;
  }

  /* ── Input ── */
  window.addEventListener('pointermove', function (e) {
    mouse.x = e.clientX; mouse.y = e.clientY; mouse.active = true;
  }, { passive: true });
  window.addEventListener('pointerleave', function () {
    mouse.active = false; mouse.x = -9999; mouse.y = -9999;
  });

  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(resize, 150);
  });

  /* ── Synapse pulse (signal firing along a link) ── */
  function maybeFirePulse(a, b) {
    if (pulses.length < 6 && Math.random() < 0.0006) {
      pulses.push({ a: a, b: b, t: 0, speed: rand(0.015, 0.035) });
    }
  }

  /* ── Render loop ── */
  var t = 0;
  var running = true;

  function step() {
    t += 0.016;
    ctx.clearRect(0, 0, W, H);

    var i, j, p, q;

    /* update */
    for (i = 0; i < particles.length; i++) {
      p = particles[i];

      // gentle drift
      p.x += p.vx * p.speed;
      p.y += p.vy * p.speed;

      // cursor attraction — neurons lean toward the "scanner"
      if (mouse.active) {
        var dxm = mouse.x - p.x, dym = mouse.y - p.y;
        var dm = Math.sqrt(dxm * dxm + dym * dym);
        if (dm < MOUSE_RADIUS && dm > 0.001) {
          var force = (1 - dm / MOUSE_RADIUS) * 0.012;
          p.x += dxm * force;
          p.y += dym * force;
        }
      }

      // wrap around edges
      if (p.x < -20) p.x = W + 20; else if (p.x > W + 20) p.x = -20;
      if (p.y < -20) p.y = H + 20; else if (p.y > H + 20) p.y = -20;
    }

    /* links */
    for (i = 0; i < particles.length; i++) {
      p = particles[i];
      for (j = i + 1; j < particles.length; j++) {
        q = particles[j];
        var dx = p.x - q.x, dy = p.y - q.y;
        var distSq = dx * dx + dy * dy;
        if (distSq < LINK_DIST * LINK_DIST) {
          var d = Math.sqrt(distSq);
          var alpha = (1 - d / LINK_DIST) * 0.16;

          // links near the cursor light up
          if (mouse.active) {
            var mx = (p.x + q.x) / 2 - mouse.x;
            var my = (p.y + q.y) / 2 - mouse.y;
            var md = Math.sqrt(mx * mx + my * my);
            if (md < MOUSE_RADIUS) alpha += (1 - md / MOUSE_RADIUS) * 0.28;
          }

          ctx.strokeStyle = 'rgba(' + p.c[0] + ',' + p.c[1] + ',' + p.c[2] + ',' + alpha.toFixed(3) + ')';
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.stroke();

          maybeFirePulse(p, q);
        }
      }
    }

    /* pulses — bright dots travelling along synapses */
    for (i = pulses.length - 1; i >= 0; i--) {
      var pl = pulses[i];
      pl.t += pl.speed;
      if (pl.t >= 1) { pulses.splice(i, 1); continue; }
      var px = pl.a.x + (pl.b.x - pl.a.x) * pl.t;
      var py = pl.a.y + (pl.b.y - pl.a.y) * pl.t;
      var g = ctx.createRadialGradient(px, py, 0, px, py, 6);
      g.addColorStop(0, 'rgba(94,249,255,0.9)');
      g.addColorStop(1, 'rgba(94,249,255,0)');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(px, py, 6, 0, Math.PI * 2);
      ctx.fill();
    }

    /* nodes */
    for (i = 0; i < particles.length; i++) {
      p = particles[i];
      var glow = 0.45 + Math.sin(t * 2 + p.phase) * 0.2;

      // nodes near cursor burn brighter
      if (mouse.active) {
        var ddx = p.x - mouse.x, ddy = p.y - mouse.y;
        var dd = Math.sqrt(ddx * ddx + ddy * ddy);
        if (dd < MOUSE_RADIUS) glow += (1 - dd / MOUSE_RADIUS) * 0.5;
      }

      ctx.fillStyle = 'rgba(' + p.c[0] + ',' + p.c[1] + ',' + p.c[2] + ',' + Math.min(glow, 1).toFixed(3) + ')';
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    }

    if (running && !reduceMotion) requestAnimationFrame(step);
  }

  /* pause when tab hidden */
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
      running = false;
    } else if (!running) {
      running = true;
      if (!reduceMotion) requestAnimationFrame(step);
    }
  });

  resize();
  if (reduceMotion) {
    // static single frame for users who prefer reduced motion
    step();
  } else {
    requestAnimationFrame(step);
  }
})();
