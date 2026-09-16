(function () {
  var PLATE = "media/cinema-c1-austin-night.jpg";
  var SHOTS = [
    { id: "C1", pos: "50% 55%", zoom: 1 },
    { id: "C2", pos: "62% 48%", zoom: 1.18 },
    { id: "C3", pos: "38% 60%", zoom: 1.22 },
    { id: "C4", pos: "78% 28%", zoom: 1.35 },
    { id: "C5", pos: "50% 70%", zoom: 1.12 }
  ];
  var NODES = [
    { id: "cam-fwd", label: "Forward bumper camera", kind: "VISION", x: 28, y: 62 },
    { id: "cam-rear", label: "Rear fascia camera", kind: "VISION", x: 88, y: 58 },
    { id: "cam-lbp", label: "Left B-pillar camera", kind: "VISION", x: 46, y: 42 },
    { id: "cam-rbp", label: "Right B-pillar camera", kind: "VISION", x: 72, y: 40 },
    { id: "cam-ws-l", label: "Windshield camera L", kind: "VISION", x: 40, y: 36 },
    { id: "cam-ws-r", label: "Windshield camera R", kind: "VISION", x: 58, y: 34 },
    { id: "cam-lf", label: "Left fender camera", kind: "VISION", x: 22, y: 52 },
    { id: "cam-rf", label: "Right fender camera", kind: "VISION", x: 80, y: 50 },
    { id: "cam-cabin", label: "Cabin occupancy camera", kind: "VISION", x: 64, y: 48 },
    { id: "radar-cabin", label: "Cabin occupancy radar", kind: "RADAR", x: 68, y: 54 },
    { id: "ln-settle", label: "Lightning settlement", kind: "COMMS", x: 50, y: 86, paper: true }
  ];

  var GPU_MESH_AVAILABLE = false;
  var BLOCKED_MESH = /\.(glb|gltf|usdz)$/i;
  var lod = "cinema";
  var shot = 0;
  var rot = 0;
  var drag = null;

  var titleLoop = document.getElementById("title-loop");
  titleLoop.addEventListener("error", function () {
    titleLoop.removeAttribute("src");
    titleLoop.load();
  });
  titleLoop.querySelector("source").addEventListener("error", function () {
    titleLoop.removeAttribute("src");
  });

  document.getElementById("enter-console").addEventListener("click", function () {
    document.getElementById("title-page").classList.add("hidden");
    document.getElementById("console").classList.remove("hidden");
    titleLoop.pause();
  });

  var shotsEl = document.getElementById("shots");
  SHOTS.forEach(function (s, i) {
    var b = document.createElement("button");
    b.type = "button";
    b.textContent = s.id;
    if (i === 0) b.className = "on";
    b.addEventListener("click", function () {
      shot = i;
      Array.prototype.forEach.call(shotsEl.children, function (el, j) {
        el.classList.toggle("on", j === i);
      });
      applyPlate();
    });
    shotsEl.appendChild(b);
  });

  var list = document.getElementById("node-list");
  var nodesEl = document.getElementById("nodes");
  NODES.forEach(function (n) {
    var li = document.createElement("li");
    var btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = n.label;
    btn.addEventListener("click", function () { selectNode(n.id); });
    var kind = document.createElement("span");
    kind.className = "kind";
    kind.textContent = n.kind;
    li.appendChild(btn);
    li.appendChild(kind);
    list.appendChild(li);

    var dot = document.createElement("button");
    dot.type = "button";
    dot.className = "node";
    dot.dataset.id = n.id;
    dot.style.left = n.x + "%";
    dot.style.top = n.y + "%";
    dot.title = n.label;
    dot.addEventListener("click", function (e) {
      e.stopPropagation();
      selectNode(n.id);
    });
    nodesEl.appendChild(dot);
  });

  document.querySelectorAll("[data-lod]").forEach(function (b) {
    b.addEventListener("click", function () {
      lod = b.getAttribute("data-lod");
      document.querySelectorAll("[data-lod]").forEach(function (x) {
        x.classList.toggle("on", x === b);
      });
      if (lod === "mesh" && !GPU_MESH_AVAILABLE) {
        document.getElementById("lod-badge").textContent = "MESH LOD";
        document.getElementById("mesh-veil").classList.remove("hidden");
      } else {
        document.getElementById("lod-badge").textContent = "CINEMA LOD";
        document.getElementById("mesh-veil").classList.add("hidden");
        lod = "cinema";
      }
      applyPlate();
    });
  });

  function selectNode(id) {
    var n = NODES.filter(function (x) { return x.id === id; })[0];
    if (!n) return;
    Array.prototype.forEach.call(document.querySelectorAll(".node"), function (el) {
      el.classList.toggle("on", el.dataset.id === id);
    });
    document.getElementById("insp-title").textContent = n.label;
    document.getElementById("insp-body").textContent = n.paper
      ? "Comms · Cabin compute · 1 Hz. Fare rail placeholder. No wallet code in this module. Lightning receive labels stay Fountain or Bitcoin Jungle — HUD never holds keys."
      : "Paper VISION/RADAR node. Listed only. No live OEM API. No keys.";
  }

  function applyPlate() {
    var img = document.getElementById("plate");
    var s = SHOTS[shot];
    if (BLOCKED_MESH.test(PLATE)) {
      throw new Error("rejected mesh path");
    }
    img.src = PLATE;
    img.style.objectPosition = s.pos;
    img.style.transform = "scale(" + s.zoom + ")";
  }

  var wrap = document.getElementById("plate-wrap");
  wrap.addEventListener("pointerdown", function (e) {
    drag = { x: e.clientX, r: rot };
    wrap.classList.add("grabbing");
    wrap.setPointerCapture(e.pointerId);
  });
  wrap.addEventListener("pointermove", function (e) {
    if (!drag) return;
    rot = drag.r + (e.clientX - drag.x) * 0.12;
    wrap.style.transform = "rotateY(" + rot + "deg)";
  });
  wrap.addEventListener("pointerup", function () {
    drag = null;
    wrap.classList.remove("grabbing");
  });

  applyPlate();
})();
