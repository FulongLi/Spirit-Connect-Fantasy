import * as THREE from "three";
import { mergeGeometries } from "three/addons/utils/BufferGeometryUtils.js";

/*
 * Spirit Connection Pod (灵接舱), sixth generation.
 *
 * Design reference: 《月球暗面》 V2 manuscript (月球暗面_V2/zh_md file names).
 *  - 08_第二次数字矫正: the new pods are egg-shaped capsules of smooth white
 *    composite with "no unnecessary lines", and no longer need black liquid, so
 *    there are no fluid conduits on this model.
 *  - 09_数字吉姆的空房间: the occupant lies fully flat on an ergonomic couch that
 *    spreads pressure across the back and limbs; an egg-shaped canopy closes over.
 *  - 03_黑水与苏醒 / 06_蓝黑球体与时间井: the canopy closes and opens slowly and is
 *    semi-transparent (半透明舱盖); faint status lights blink rhythmically along
 *    the edge; inside is a soft but cold light.
 *  - 25_再见小女孩 / 27_三天失败: "a row of silver-white shells".
 *  - 18_童年的另一个世界 / 20_月暗副本: faint interface light patterns (接口光纹)
 *    flow over the shell and pulse like breathing.
 *  - 06_蓝黑球体与时间井: Dr. Lune adjusts the pod from a console and watches the
 *    occupants' real-time waveforms, so each pod has a slim monitoring pylon.
 *
 * Local frame: +z is the foot end (faces outward, toward the camera path),
 * -z is the head end (faces the central core), y is up, the floor is y = 0.
 * All geometry is built once and shared by every pod instance.
 */

const P = {
  length: 40,
  radius: 8.2,
  vScale: 0.64,
  axisY: 8.7,
  headBias: 0.1,
  window: [0.16, 0.86],
  windowHalfAngle: 1.02,
  linerScale: 0.93,
  canopyScale: 1.012,
};

const HINGE_S = P.window[0];
const OPEN_ANGLE = 0.26;

const tmpA = new THREE.Vector3();
const tmpB = new THREE.Vector3();
const tmpC = new THREE.Vector3();

function sToZ(s) {
  return (s - 0.5) * P.length;
}

function radiusAt(s) {
  const c = Math.min(1, Math.max(0, s));
  return P.radius * Math.pow(Math.sin(Math.PI * c), 0.62) * (1 + P.headBias * Math.cos(Math.PI * c));
}

// phi = 0 is the underside, phi = PI is the top centre line.
function surfacePoint(s, phi, scale, target) {
  const r = radiusAt(s) * scale;
  return target.set(r * Math.sin(phi), P.axisY - r * Math.cos(phi) * P.vScale, sToZ(s));
}

function surfaceNormal(s, phi, scale, target) {
  const e = 1e-3;
  surfacePoint(s, phi, scale, tmpA);
  surfacePoint(s, phi + e, scale, tmpB).sub(tmpA);
  surfacePoint(Math.min(1, s + e), phi, scale, tmpC).sub(tmpA);
  target.crossVectors(tmpB, tmpC);
  if (target.lengthSq() < 1e-12) return target.set(0, 0, s < 0.5 ? -1 : 1);
  return target.normalize();
}

function windowHalfAngle(s) {
  const [w0, w1] = P.window;
  if (s <= w0 || s >= w1) return 0;
  const mid = (w0 + w1) / 2;
  const half = (w1 - w0) / 2;
  const u = (s - mid) / half;
  return P.windowHalfAngle * Math.sqrt(Math.max(0, 1 - u * u));
}

function cosSpaced(a, b, n) {
  const out = [];
  for (let i = 0; i <= n; i++) out.push(a + (b - a) * (0.5 - 0.5 * Math.cos((Math.PI * i) / n)));
  return out;
}

function hullRows() {
  const [w0, w1] = P.window;
  const head = cosSpaced(0, w0, 14);
  const win = cosSpaced(w0, w1, 40).slice(1);
  const foot = cosSpaced(w1, 1, 12).slice(1);
  return [...head, ...win, ...foot];
}

// Builds a surface over rows of s, each row spanning [phiA(s), phiB(s)].
function buildSurface(rows, range, cols, scale, flip = false) {
  const positions = [];
  const normals = [];
  const uvs = [];
  const indices = [];
  const p = new THREE.Vector3();
  const n = new THREE.Vector3();
  rows.forEach((s, i) => {
    const [a, b] = range(s);
    for (let j = 0; j <= cols; j++) {
      const phi = a + ((b - a) * j) / cols;
      surfacePoint(s, phi, scale, p);
      surfaceNormal(s, phi, scale, n);
      if (flip) n.negate();
      positions.push(p.x, p.y, p.z);
      normals.push(n.x, n.y, n.z);
      uvs.push(j / cols, i / (rows.length - 1));
    }
  });
  const stride = cols + 1;
  for (let i = 0; i < rows.length - 1; i++) {
    for (let j = 0; j < cols; j++) {
      const a = i * stride + j;
      const b = a + stride;
      const c = a + 1;
      const d = b + 1;
      if (flip) indices.push(a, b, c, c, b, d);
      else indices.push(a, c, b, c, d, b);
    }
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.Float32BufferAttribute(positions, 3));
  geo.setAttribute("normal", new THREE.Float32BufferAttribute(normals, 3));
  geo.setAttribute("uv", new THREE.Float32BufferAttribute(uvs, 2));
  geo.setIndex(indices);
  return geo;
}

// A thin ribbon lying on the shell, following a path of (s, phi) samples.
function buildRibbon(samples, halfWidth, scale, attrs) {
  const positions = [];
  const uvs = [];
  const indices = [];
  const p = new THREE.Vector3();
  const nrm = new THREE.Vector3();
  const next = new THREE.Vector3();
  const side = new THREE.Vector3();
  samples.forEach(([s, phi], i) => {
    const [ns, nphi] = samples[Math.min(samples.length - 1, i + 1)];
    const [ps, pphi] = samples[Math.max(0, i - 1)];
    surfacePoint(s, phi, scale, p);
    surfaceNormal(s, phi, scale, nrm);
    surfacePoint(ns, nphi, scale, next);
    surfacePoint(ps, pphi, scale, tmpC);
    next.sub(tmpC).normalize();
    side.crossVectors(nrm, next).normalize().multiplyScalar(halfWidth);
    positions.push(p.x + side.x, p.y + side.y, p.z + side.z, p.x - side.x, p.y - side.y, p.z - side.z);
    const u = i / (samples.length - 1);
    uvs.push(u, 0, u, 1);
    if (i < samples.length - 1) {
      const a = i * 2;
      indices.push(a, a + 1, a + 2, a + 1, a + 3, a + 2);
    }
  });
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.Float32BufferAttribute(positions, 3));
  geo.setAttribute("uv", new THREE.Float32BufferAttribute(uvs, 2));
  geo.setIndex(indices);
  return withLightAttrs(geo, attrs);
}

function flat(g) {
  return g.index ? g.toNonIndexed() : g;
}

function ensureUv(g) {
  if (!g.getAttribute("uv")) g.setAttribute("uv", new THREE.Float32BufferAttribute(new Float32Array(g.getAttribute("position").count * 2), 2));
  return g;
}

function withLightAttrs(geo, { kind = 0, seq = 0 } = {}) {
  const count = geo.getAttribute("position").count;
  geo.setAttribute("aKind", new THREE.Float32BufferAttribute(new Float32Array(count).fill(kind), 1));
  geo.setAttribute("aSeq", new THREE.Float32BufferAttribute(new Float32Array(count).fill(seq), 1));
  if (!geo.getAttribute("uv")) geo.setAttribute("uv", new THREE.Float32BufferAttribute(new Float32Array(count * 2), 2));
  geo.deleteAttribute("normal");
  return geo;
}

function windowOutline(scale, steps = 60) {
  const [w0, w1] = P.window;
  const pts = [];
  const p = new THREE.Vector3();
  const rows = cosSpaced(w0, w1, steps);
  rows.forEach((s) => pts.push(surfacePoint(s, Math.PI + windowHalfAngle(s), scale, p).clone()));
  rows.slice(1, -1).reverse().forEach((s) => pts.push(surfacePoint(s, Math.PI - windowHalfAngle(s), scale, p).clone()));
  return new THREE.CatmullRomCurve3(pts, true, "centripetal");
}

function roundedRect(hw, hd, r) {
  const shape = new THREE.Shape();
  shape.moveTo(-hw + r, -hd);
  shape.lineTo(hw - r, -hd);
  shape.quadraticCurveTo(hw, -hd, hw, -hd + r);
  shape.lineTo(hw, hd - r);
  shape.quadraticCurveTo(hw, hd, hw - r, hd);
  shape.lineTo(-hw + r, hd);
  shape.quadraticCurveTo(-hw, hd, -hw, hd - r);
  shape.lineTo(-hw, -hd + r);
  shape.quadraticCurveTo(-hw, -hd, -hw + r, -hd);
  return shape;
}

// Extrudes a top-view shape (x, z) upward between y0 and y1.
function slab(shape, y0, y1, bevel, curveSegments = 10) {
  const geo = new THREE.ExtrudeGeometry(shape, {
    depth: Math.max(0.01, y1 - y0 - bevel * 2),
    bevelEnabled: bevel > 0,
    bevelThickness: bevel,
    bevelSize: bevel,
    bevelSegments: 3,
    curveSegments,
  });
  geo.rotateX(-Math.PI / 2);
  geo.translate(0, y0 + bevel, 0);
  return geo;
}

function buildGeometries(quality) {
  const low = quality === "low";
  const cols = low ? 40 : 64;
  const [w0, w1] = P.window;
  const rows = hullRows();
  const winRows = rows.filter((s) => s >= w0 && s <= w1);

  const hull = buildSurface(rows, (s) => {
    const c = windowHalfAngle(s);
    return [Math.PI + c, 3 * Math.PI - c];
  }, cols, 1);

  const liner = buildSurface(winRows, (s) => {
    const c = windowHalfAngle(s);
    return [Math.PI + c, 3 * Math.PI - c];
  }, Math.round(cols * 0.75), P.linerScale, true);

  const canopy = buildSurface(winRows, (s) => {
    const c = windowHalfAngle(s);
    return [Math.PI - c, Math.PI + c];
  }, low ? 14 : 22, P.canopyScale);

  // Lip between the outer hull and the inner liner along the window edge.
  const lipParts = [-1, 1].map((sign) => {
    const positions = [];
    const indices = [];
    const p = new THREE.Vector3();
    winRows.forEach((s, i) => {
      const phi = Math.PI + sign * windowHalfAngle(s);
      surfacePoint(s, phi, 1.0, p);
      positions.push(p.x, p.y, p.z);
      surfacePoint(s, phi, P.linerScale, p);
      positions.push(p.x, p.y, p.z);
      if (i < winRows.length - 1) {
        const a = i * 2;
        indices.push(a, a + 1, a + 2, a + 1, a + 3, a + 2);
      }
    });
    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.Float32BufferAttribute(positions, 3));
    geo.setIndex(indices);
    geo.computeVertexNormals();
    return geo;
  });

  const band = (s0, s1, scale) => buildSurface(cosSpaced(s0, s1, 3), () => [0, Math.PI * 2], cols, scale);
  const gasket = new THREE.TubeGeometry(windowOutline(1.004), low ? 90 : 160, 0.13, 6, true);
  const trimParts = [...lipParts, band(0.112, 0.138, 1.02), band(0.888, 0.902, 1.016), gasket];

  // Slim monitoring pylon beside the head end (Dr. Lune's console).
  const post = new THREE.CylinderGeometry(0.32, 0.55, 8.4, 16);
  post.translate(0, 4.2, 0);
  const postFoot = new THREE.CylinderGeometry(1.25, 1.45, 0.5, 24);
  postFoot.translate(0, 0.25, 0);
  const screenFrame = new THREE.BoxGeometry(5.2, 3.3, 0.28);
  screenFrame.rotateX(-0.5);
  screenFrame.translate(0, 9.0, 0.15);
  [post, postFoot, screenFrame].forEach((g) => g.translate(11.6, 0, -11));
  trimParts.push(mergeGeometries([post, postFoot, screenFrame].map(flat)));
  const trim = mergeGeometries(trimParts.map(flat).map(ensureUv));

  const screen = new THREE.PlaneGeometry(4.7, 2.85);
  screen.rotateX(-0.5);
  screen.translate(11.6, 9.08, -10.7);

  // Canopy frame and two structural ribs: these travel with the canopy.
  const canopyFrame = new THREE.TubeGeometry(windowOutline(P.canopyScale + 0.004), low ? 90 : 160, 0.1, 6, true);
  const ribs = [0.42, 0.63].map((s) => buildRibbon(
    cosSpaced(-1, 1, 16).map((u) => [s, Math.PI + u * windowHalfAngle(s) * 0.985]),
    0.12,
    P.canopyScale + 0.006,
    {}
  ));
  ribs.forEach((g) => {
    g.deleteAttribute("aKind");
    g.deleteAttribute("aSeq");
    g.computeVertexNormals();
  });
  const canopyTrim = mergeGeometries([canopyFrame, ...ribs].map(flat).map(ensureUv));

  // Integrated support base: recessed foot, bevelled deck and a saddle that
  // follows the underside of the shell.
  const foot = slab(roundedRect(4.4, 13.0, 2.2), 0, 1.05, 0.12, 6);
  const deck = slab(roundedRect(5.4, 14.6, 2.8), 1.0, 3.3, 0.45, 10);
  const saddleShape = new THREE.Shape();
  const sz0 = sToZ(0.2);
  const sz1 = sToZ(0.82);
  saddleShape.moveTo(sz0 - 1.5, 3.0);
  for (let i = 0; i <= 24; i++) {
    const s = 0.2 + (0.62 * i) / 24;
    saddleShape.lineTo(sToZ(s), P.axisY - radiusAt(s) * P.vScale + 0.25);
  }
  saddleShape.lineTo(sz1 + 1.5, 3.0);
  saddleShape.closePath();
  const saddle = new THREE.ExtrudeGeometry(saddleShape, { depth: 5.2, bevelEnabled: true, bevelThickness: 0.3, bevelSize: 0.3, bevelSegments: 2, curveSegments: 4 });
  saddle.rotateY(-Math.PI / 2);
  saddle.translate(2.6, 0, 0);
  const base = mergeGeometries([deck, saddle].map(flat));

  // Ergonomic couch, seen through the canopy (top-view outline, extruded up).
  const outline = [
    [0, -12.8], [1.9, -12.4], [2.3, -10.6], [1.6, -9.0], [4.1, -8.0], [4.3, -3.5],
    [3.8, 1.5], [3.4, 6.0], [2.6, 10.0], [0, 10.8], [-2.6, 10.0], [-3.4, 6.0],
    [-3.8, 1.5], [-4.3, -3.5], [-4.1, -8.0], [-1.6, -9.0], [-2.3, -10.6], [-1.9, -12.4],
  ].map(([x, z]) => new THREE.Vector2(x, -z));
  const couchCurve = new THREE.SplineCurve([...outline, outline[0]]);
  const couchShape = new THREE.Shape(couchCurve.getPoints(low ? 48 : 96));
  const couch = slab(couchShape, 5.4, 6.4, 0.32, 4);

  // Light layer: flowing interface patterns on the flanks, a breathing band
  // behind the head collar, rhythmic status lights beside the canopy edge and
  // an underglow line around the base. All share one shader and draw call.
  const lights = [];
  const flankPhi = Math.PI / 2 - 0.42;
  [flankPhi, Math.PI * 2 - flankPhi].forEach((phi, k) => {
    lights.push(buildRibbon(cosSpaced(0.07, 0.95, 70).map((s) => [s, phi]), 0.2, 1.004, { kind: 0, seq: k * 0.5 }));
  });
  lights.push(buildRibbon(cosSpaced(0, 1, 72).map((u) => [0.146, u * Math.PI * 2]), 0.09, 1.006, { kind: 2 }));
  const indicator = new THREE.BoxGeometry(0.5, 0.08, 0.2);
  const basis = new THREE.Matrix4();
  const nrm = new THREE.Vector3();
  const tan = new THREE.Vector3();
  const bin = new THREE.Vector3();
  const pos = new THREE.Vector3();
  let seq = 0;
  [-1, 1].forEach((sign) => {
    for (let i = 0; i < 7; i++) {
      const s = 0.56 + i * 0.042;
      const phi = Math.PI + sign * (windowHalfAngle(s) + 0.13);
      surfacePoint(s, phi, 1.008, pos);
      surfaceNormal(s, phi, 1, nrm);
      surfacePoint(s + 0.01, phi, 1.008, tan).sub(pos);
      tan.addScaledVector(nrm, -tan.dot(nrm)).normalize();
      bin.crossVectors(tan, nrm);
      basis.makeBasis(tan, nrm, bin).setPosition(pos);
      const g = indicator.clone().applyMatrix4(basis);
      lights.push(withLightAttrs(flat(g), { kind: 1, seq: seq++ }));
    }
  });
  const glowShape = roundedRect(5.43, 14.63, 2.8).getPoints(24);
  const glowPos = [];
  const glowUv = [];
  const glowIdx = [];
  glowShape.forEach((p2, i) => {
    glowPos.push(p2.x, 1.12, -p2.y, p2.x, 1.32, -p2.y);
    glowUv.push(i / (glowShape.length - 1), 0, i / (glowShape.length - 1), 1);
    if (i < glowShape.length - 1) glowIdx.push(i * 2, i * 2 + 2, i * 2 + 1, i * 2 + 1, i * 2 + 2, i * 2 + 3);
  });
  const glow = new THREE.BufferGeometry();
  glow.setAttribute("position", new THREE.Float32BufferAttribute(glowPos, 3));
  glow.setAttribute("uv", new THREE.Float32BufferAttribute(glowUv, 2));
  glow.setIndex(glowIdx);
  lights.push(withLightAttrs(glow, { kind: 3 }));
  const light = mergeGeometries(lights.map(flat));

  [hull, liner, canopy, trim, canopyTrim, foot, base, couch, screen, light].forEach((g) => g.computeBoundingSphere());

  const hinge = surfacePoint(HINGE_S, Math.PI, P.canopyScale, new THREE.Vector3());
  return { hull, liner, canopy, trim, canopyTrim, foot, base, couch, screen, light, hinge };
}

const lightVertex = /* glsl */ `
  attribute float aKind;
  attribute float aSeq;
  varying vec2 vUv;
  varying float vKind;
  varying float vSeq;
  void main() {
    vUv = uv;
    vKind = aKind;
    vSeq = aSeq;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;

const lightFragment = /* glsl */ `
  uniform float uTime;
  uniform float uLevel;
  uniform vec3 uColor;
  varying vec2 vUv;
  varying float vKind;
  varying float vSeq;
  void main() {
    float breath = 0.84 + 0.16 * sin(uTime * 1.25);
    float across = 1.0 - abs(vUv.y * 2.0 - 1.0);
    vec3 tint = uColor;
    float a;
    if (vKind < 0.5) {
      float p = fract(vUv.x * 1.6 - uTime * 0.21 + vSeq);
      float pulse = smoothstep(0.0, 0.05, p) * (1.0 - smoothstep(0.05, 0.4, p));
      a = (0.36 + 0.9 * pulse) * smoothstep(0.0, 0.7, across);
      a *= smoothstep(0.0, 0.06, vUv.x) * (1.0 - smoothstep(0.94, 1.0, vUv.x));
    } else if (vKind < 1.5) {
      float blink = 0.5 + 0.5 * sin(uTime * 2.1 - vSeq * 0.85);
      a = 0.3 + 0.7 * smoothstep(0.6, 1.0, blink);
      tint = mix(uColor, vec3(0.86, 0.96, 1.0), 0.35);
    } else if (vKind < 2.5) {
      a = 0.6 * breath * smoothstep(0.0, 0.8, across);
    } else {
      a = 0.32 * breath * (1.0 - vUv.y);
    }
    gl_FragColor = vec4(tint * a * uLevel * breath, 1.0);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
  }
`;

function makeWaveTexture() {
  const c = document.createElement("canvas");
  c.width = 256;
  c.height = 128;
  const ctx = c.getContext("2d");
  ctx.fillStyle = "#061421";
  ctx.fillRect(0, 0, 256, 128);
  ctx.strokeStyle = "rgba(120, 200, 255, 0.16)";
  ctx.lineWidth = 1;
  for (let x = 0; x <= 256; x += 32) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, 128);
    ctx.stroke();
  }
  const trace = (y0, amp, freq, color, width) => {
    ctx.strokeStyle = color;
    ctx.lineWidth = width;
    ctx.beginPath();
    for (let x = 0; x <= 256; x += 2) {
      const t = (x / 256) * Math.PI * 2;
      const y = y0 + Math.sin(t * freq) * amp + Math.sin(t * freq * 3.1 + 1.3) * amp * 0.35;
      if (x === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();
  };
  trace(40, 10, 3, "rgba(110, 225, 255, 0.95)", 2);
  trace(84, 7, 5, "rgba(255, 214, 140, 0.8)", 1.5);
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.wrapS = THREE.RepeatWrapping;
  return tex;
}

const THEME = {
  day: { shell: "#eef2f5", trim: "#97a3ae", base: "#a7b0b9", foot: "#59626c", liner: "#1d2a36", couch: "#2b3744", canopy: 0.2, light: 0.62, env: 1.0 },
  night: { shell: "#c6d1dc", trim: "#7c8ea1", base: "#2c3644", foot: "#121923", liner: "#0b141e", couch: "#18222e", canopy: 0.26, light: 1.0, env: 1.25 },
};

export function createSpiritConnectionPodKit({ quality = "high", anisotropy = 4 } = {}) {
  const geo = buildGeometries(quality);
  const time = { value: 0 };
  const waveTexture = makeWaveTexture();
  waveTexture.anisotropy = anisotropy;

  const mats = {
    shell: new THREE.MeshPhysicalMaterial({ color: THEME.night.shell, roughness: 0.34, metalness: 0.08, clearcoat: 1, clearcoatRoughness: 0.14 }),
    trim: new THREE.MeshStandardMaterial({ color: THEME.night.trim, roughness: 0.3, metalness: 0.88, side: THREE.DoubleSide }),
    base: new THREE.MeshStandardMaterial({ color: THEME.night.base, roughness: 0.46, metalness: 0.62 }),
    foot: new THREE.MeshStandardMaterial({ color: THEME.night.foot, roughness: 0.7, metalness: 0.3 }),
    liner: new THREE.MeshStandardMaterial({ color: THEME.night.liner, roughness: 0.62, metalness: 0.1, side: THREE.BackSide, emissive: "#6fd3ff", emissiveIntensity: 0.05 }),
    couch: new THREE.MeshPhysicalMaterial({ color: THEME.night.couch, roughness: 0.68, metalness: 0.05, sheen: 0.6, sheenColor: "#5b7c99", sheenRoughness: 0.5 }),
    canopy: new THREE.MeshPhysicalMaterial({
      color: "#d4eeff",
      roughness: 0.05,
      metalness: 0,
      clearcoat: 1,
      clearcoatRoughness: 0.04,
      ior: 1.5,
      transparent: true,
      opacity: THEME.night.canopy,
      depthWrite: false,
      side: THREE.DoubleSide,
    }),
    screen: new THREE.MeshBasicMaterial({ map: waveTexture, color: "#c8e8ff" }),
  };
  mats.canopy.envMapIntensity = THEME.night.env;
  let themeLight = THEME.night.light;
  const pods = [];

  function createPod({ accent = "#2bb8ff", enabled = true, seed = 0 } = {}) {
    const group = new THREE.Group();
    group.name = "spirit-connection-pod";

    const add = (geometry, material, { cast = false, receive = false, order = 0 } = {}) => {
      const mesh = new THREE.Mesh(geometry, material);
      mesh.castShadow = cast;
      mesh.receiveShadow = receive;
      mesh.renderOrder = order;
      return mesh;
    };

    group.add(add(geo.foot, mats.foot, { receive: true }));
    group.add(add(geo.base, mats.base, { cast: true, receive: true }));
    group.add(add(geo.hull, mats.shell, { cast: true, receive: true }));
    group.add(add(geo.liner, mats.liner, { receive: true }));
    group.add(add(geo.couch, mats.couch, { receive: true }));
    group.add(add(geo.trim, mats.trim, { cast: true }));
    group.add(add(geo.screen, mats.screen));

    const lightMat = new THREE.ShaderMaterial({
      uniforms: {
        uTime: time,
        uLevel: { value: enabled ? 0.45 : 0.12 },
        uColor: { value: new THREE.Color(accent) },
      },
      vertexShader: lightVertex,
      fragmentShader: lightFragment,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    });
    group.add(add(geo.light, lightMat, { order: 2 }));

    // The canopy pivots on a hinge at the head end of the window.
    const hinge = new THREE.Group();
    hinge.position.copy(geo.hinge);
    const canopyGroup = new THREE.Group();
    canopyGroup.position.copy(geo.hinge).negate();
    canopyGroup.add(add(geo.canopyTrim, mats.trim, { cast: true }));
    canopyGroup.add(add(geo.canopy, mats.canopy, { order: 3 }));
    hinge.add(canopyGroup);
    group.add(hinge);

    const state = { group, hinge, lightMat, enabled, open: 0, level: lightMat.uniforms.uLevel.value, seed };
    pods.push(state);
    return {
      group,
      setAccent(color) {
        lightMat.uniforms.uColor.value.set(color);
      },
    };
  }

  function update({ dt, elapsed, activeIndex = -1, motion = 1 }) {
    time.value = elapsed;
    waveTexture.offset.x = (waveTexture.offset.x + dt * 0.06 * motion) % 1;
    const ease = Math.min(1, dt * 2.4);
    pods.forEach((pod, i) => {
      const active = pod.enabled && i === activeIndex;
      pod.open += ((active ? 1 : 0) - pod.open) * ease;
      pod.hinge.rotation.x = -pod.open * OPEN_ANGLE;
      const target = (pod.enabled ? (active ? 1.15 : 0.45) : 0.12) * themeLight;
      pod.level += (target - pod.level) * ease;
      pod.lightMat.uniforms.uLevel.value = pod.level;
    });
    const anyOpen = pods.reduce((m, p) => Math.max(m, p.open), 0);
    mats.liner.emissiveIntensity = 0.05 + anyOpen * 0.12;
  }

  function setTheme(mode) {
    const t = THEME[mode] || THEME.night;
    mats.shell.color.set(t.shell);
    mats.trim.color.set(t.trim);
    mats.base.color.set(t.base);
    mats.foot.color.set(t.foot);
    mats.liner.color.set(t.liner);
    mats.couch.color.set(t.couch);
    mats.canopy.opacity = t.canopy;
    mats.canopy.envMapIntensity = t.env;
    themeLight = t.light;
  }

  function dispose() {
    Object.values(geo).forEach((g) => g.isBufferGeometry && g.dispose());
    Object.values(mats).forEach((m) => m.dispose());
    pods.forEach((p) => p.lightMat.dispose());
    waveTexture.dispose();
    pods.length = 0;
  }

  return { createPod, update, setTheme, dispose, dimensions: { ...P } };
}
