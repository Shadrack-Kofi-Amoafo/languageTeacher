/* ============================================================
   Lumière — 3D hero scene (Three.js r147, vendored)
   A levitating cloche over a signature dish, golden dust,
   drag-to-rotate with inertia, mouse parallax, soft shadows.
   ============================================================ */
(function () {
  "use strict";

  var canvas = document.getElementById("hero-canvas");
  if (!canvas || typeof THREE === "undefined") return;

  var WebGLOk = (function () {
    try {
      var c = document.createElement("canvas");
      return !!(window.WebGLRenderingContext && (c.getContext("webgl") || c.getContext("experimental-webgl")));
    } catch (e) { return false; }
  })();
  if (!WebGLOk) { canvas.style.display = "none"; return; }

  /* ---------- Renderer / scene / camera ---------- */
  var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputEncoding = THREE.sRGBEncoding;

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(38, 1, 0.1, 100);
  camera.position.set(0, 2.35, 6.4);
  camera.lookAt(0, 0.75, 0);

  /* ---------- Lights: warm key, cool rim, soft fill ---------- */
  scene.add(new THREE.AmbientLight(0xfff4e0, 0.45));

  var key = new THREE.DirectionalLight(0xffe7c2, 1.15);
  key.position.set(3.2, 5.5, 3.4);
  key.castShadow = true;
  key.shadow.mapSize.set(2048, 2048);
  key.shadow.camera.near = 1;
  key.shadow.camera.far = 20;
  key.shadow.camera.left = -6; key.shadow.camera.right = 6;
  key.shadow.camera.top = 6; key.shadow.camera.bottom = -6;
  key.shadow.radius = 6;
  scene.add(key);

  var rim = new THREE.DirectionalLight(0x7fa8ff, 0.55);
  rim.position.set(-4.5, 3.0, -3.5);
  scene.add(rim);

  var spot = new THREE.SpotLight(0xffd9a0, 0.9, 22, Math.PI / 5.2, 0.55, 1.2);
  spot.position.set(0, 8.5, 0.5);
  spot.target.position.set(0, 0, 0);
  scene.add(spot, spot.target);

  var under = new THREE.PointLight(0xd2a75c, 0.5, 9);
  under.position.set(0, 0.45, 0);
  scene.add(under);

  /* ---------- The composition group ---------- */
  var stage = new THREE.Group();
  scene.add(stage);

  /* Porcelain plate — lathed profile */
  var profile = [
    new THREE.Vector2(0.0, 0.030),
    new THREE.Vector2(0.42, 0.028),
    new THREE.Vector2(0.78, 0.045),
    new THREE.Vector2(1.06, 0.115),
    new THREE.Vector2(1.30, 0.255),
    new THREE.Vector2(1.34, 0.300)
  ];
  var porcelain = new THREE.MeshStandardMaterial({ color: 0xf6f3ee, roughness: 0.32, metalness: 0.04 });
  var plate = new THREE.Mesh(new THREE.LatheGeometry(profile, 96), porcelain);
  plate.castShadow = true;
  plate.receiveShadow = true;
  stage.add(plate);

  var plateFoot = new THREE.Mesh(
    new THREE.CylinderGeometry(0.62, 0.62, 0.03, 64),
    porcelain
  );
  plateFoot.position.y = -0.015;
  stage.add(plateFoot);

  /* Inner plate rim (gold band, the house signature) */
  var band = new THREE.Mesh(
    new THREE.TorusGeometry(0.98, 0.016, 16, 96),
    new THREE.MeshStandardMaterial({ color: 0xd2a75c, roughness: 0.25, metalness: 0.9 })
  );
  band.rotation.x = Math.PI / 2;
  band.position.y = 0.085;
  stage.add(band);

  /* The dish — a stylised golden dome with garnish spheres */
  var dishGroup = new THREE.Group();
  var dome = new THREE.Mesh(
    new THREE.SphereGeometry(0.72, 48, 32, 0, Math.PI * 2, 0, Math.PI / 2),
    new THREE.MeshStandardMaterial({ color: 0xc98f45, roughness: 0.5, metalness: 0.08 })
  );
  dome.scale.y = 0.62;
  dome.castShadow = true;
  dishGroup.add(dome);

  function garnish(color, x, z, r, y) {
    var m = new THREE.Mesh(
      new THREE.SphereGeometry(r, 24, 18),
      new THREE.MeshStandardMaterial({ color: color, roughness: 0.35, metalness: 0.05 })
    );
    m.position.set(x, y, z);
    m.castShadow = true;
    dishGroup.add(m);
    return m;
  }
  garnish(0x5e8c4a, 0.30, 0.22, 0.075, 0.34);   // herb
  garnish(0x8c2f39, -0.34, 0.14, 0.06, 0.32);   // berry
  garnish(0x5e8c4a, -0.18, -0.34, 0.065, 0.30); // herb
  garnish(0xd2a75c, 0.16, -0.30, 0.07, 0.31);   // buttercube-ish
  dishGroup.position.y = 0.05;
  stage.add(dishGroup);

  /* Glass cloche — hovers, tilts, breathes */
  var glass = new THREE.MeshPhysicalMaterial({
    color: 0xffffff,
    metalness: 0,
    roughness: 0.04,
    transmission: 0.97,
    thickness: 0.35,
    clearcoat: 1,
    clearcoatRoughness: 0.06,
    transparent: true,
    opacity: 0.35
  });
  var cloche = new THREE.Group();
  var dome2 = new THREE.Mesh(new THREE.SphereGeometry(1.06, 64, 40, 0, Math.PI * 2, 0, Math.PI / 2), glass);
  dome2.castShadow = false;
  var rim2 = new THREE.Mesh(
    new THREE.TorusGeometry(1.055, 0.028, 20, 96),
    new THREE.MeshStandardMaterial({ color: 0xd2a75c, roughness: 0.28, metalness: 0.95 })
  );
  rim2.rotation.x = Math.PI / 2;
  var knob = new THREE.Mesh(
    new THREE.SphereGeometry(0.085, 24, 18),
    new THREE.MeshStandardMaterial({ color: 0xd2a75c, roughness: 0.22, metalness: 0.95 })
  );
  knob.position.y = 1.02;
  cloche.add(dome2, rim2, knob);
  cloche.position.y = 1.55;
  stage.add(cloche);

  /* Halo ring — the "light" motif */
  var halo = new THREE.Mesh(
    new THREE.TorusGeometry(2.35, 0.0085, 12, 160),
    new THREE.MeshStandardMaterial({ color: 0xd2a75c, roughness: 0.3, metalness: 0.85,
      emissive: 0x6b5222, emissiveIntensity: 0.55 })
  );
  halo.rotation.x = Math.PI / 2 - 0.12;
  halo.position.y = 1.1;
  stage.add(halo);

  var halo2 = halo.clone();
  halo2.scale.setScalar(1.24);
  halo2.material = halo.material.clone();
  halo2.material.opacity = 0.45;
  halo2.material.transparent = true;
  halo2.position.y = 1.45;
  stage.add(halo2);

  /* Ground shadow catcher */
  var ground = new THREE.Mesh(
    new THREE.CircleGeometry(6.5, 48),
    new THREE.ShadowMaterial({ opacity: 0.4 })
  );
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -0.02;
  ground.receiveShadow = true;
  scene.add(ground);

  /* Golden dust — drifting particles */
  var COUNT = 220;
  var positions = new Float32Array(COUNT * 3);
  var seeds = new Float32Array(COUNT);
  for (var i = 0; i < COUNT; i++) {
    var a = Math.random() * Math.PI * 2;
    var rad = 0.8 + Math.random() * 3.2;
    positions[i * 3] = Math.cos(a) * rad;
    positions[i * 3 + 1] = Math.random() * 3.6 - 0.2;
    positions[i * 3 + 2] = Math.sin(a) * rad;
    seeds[i] = Math.random() * Math.PI * 2;
  }
  var dustGeo = new THREE.BufferGeometry();
  dustGeo.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  var dust = new THREE.Points(dustGeo, new THREE.PointsMaterial({
    color: 0xe8c987, size: 0.045, sizeAttenuation: true,
    transparent: true, opacity: 0.75,
    blending: THREE.AdditiveBlending, depthWrite: false
  }));
  scene.add(dust);

  /* ---------- Interaction: drag to rotate with inertia ---------- */
  var dragging = false, lastX = 0, lastY = 0;
  var velY = 0.0016, velX = 0;
  var targetRotX = 0;

  function pointerDown(x, y) { dragging = true; lastX = x; lastY = y; }
  function pointerMove(x, y) {
    if (!dragging) return;
    velY = (x - lastX) * 0.00042;
    velX = (y - lastY) * 0.00022;
    lastX = x; lastY = y;
  }
  function pointerUp() { dragging = false; }

  canvas.addEventListener("mousedown", function (e) { pointerDown(e.clientX, e.clientY); });
  window.addEventListener("mousemove", function (e) { pointerMove(e.clientX, e.clientY); });
  window.addEventListener("mouseup", pointerUp);
  canvas.addEventListener("touchstart", function (e) {
    if (e.touches[0]) pointerDown(e.touches[0].clientX, e.touches[0].clientY);
  }, { passive: true });
  canvas.addEventListener("touchmove", function (e) {
    if (e.touches[0]) pointerMove(e.touches[0].clientX, e.touches[0].clientY);
  }, { passive: true });
  window.addEventListener("touchend", pointerUp);

  /* Mouse parallax for the camera */
  var parX = 0, parY = 0;
  window.addEventListener("mousemove", function (e) {
    parX = (e.clientX / window.innerWidth - 0.5);
    parY = (e.clientY / window.innerHeight - 0.5);
  });

  /* ---------- Resize ---------- */
  function resize() {
    var w = canvas.clientWidth || window.innerWidth;
    var h = canvas.clientHeight || window.innerHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
  window.addEventListener("resize", resize);
  resize();

  /* ---------- Animate ---------- */
  var clock = new THREE.Clock();
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function animate() {
    requestAnimationFrame(animate);
    var t = clock.getElapsedTime();

    /* Stage rotation: drag velocity decays toward a gentle auto-spin */
    if (!reduceMotion) {
      stage.rotation.y += velY;
      velY += (0.0016 - velY) * 0.02;
      targetRotX += velX;
      targetRotX = Math.max(-0.16, Math.min(0.22, targetRotX));
      velX *= 0.9;
      stage.rotation.x += (targetRotX - stage.rotation.x) * 0.08;
    }

    /* Cloche levitation — the slow reveal, forever */
    if (!reduceMotion) {
      cloche.position.y = 1.5 + Math.sin(t * 0.55) * 0.22;
      cloche.rotation.z = Math.sin(t * 0.4) * 0.05;
      cloche.rotation.y = Math.sin(t * 0.3) * 0.08;
    }

    /* Halo rings counter-rotate */
    halo.rotation.z += 0.0012;
    halo2.rotation.z -= 0.0008;

    /* Dust drift */
    var pos = dust.geometry.attributes.position;
    for (var i = 0; i < COUNT; i++) {
      var y = pos.getY(i);
      if (!reduceMotion) {
        y += 0.0022 + 0.001 * Math.sin(seeds[i] + t);
        if (y > 3.6) y = -0.2;
        pos.setY(i, y);
      }
    }
    pos.needsUpdate = true;
    dust.rotation.y = t * 0.02;

    /* Camera parallax */
    camera.position.x += (parX * 0.55 - camera.position.x) * 0.04;
    camera.position.y += (2.35 - parY * 0.45 - camera.position.y) * 0.04;
    camera.lookAt(0, 0.8, 0);

    renderer.render(scene, camera);
  }
  animate();
})();
