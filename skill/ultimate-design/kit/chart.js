/* Ultimate Design charts: small, honest SVG charts that read their colors from style.css.
   Axes start at zero, ticks are computed (never hand-typed), values are labeled directly,
   and only the series or bar that carries the story gets the accent color.

   UDChart.bar(el,  { labels, series: [{ name, values, tone }], highlight: [i], unit, height, annotate: { index, text } })
   UDChart.hbar(el, { labels, values, highlight: [i], unit, format })
   UDChart.line(el, { labels, series: [{ name, values, tone, dashed }], unit, height, threshold: { value, label }, annotate: { series, index, text } })
   UDChart.segments(el, { rows: [{ label, note, parts: [{ value, tone, text }] }], legend: [{ tone, text }], repeat })
     one row per unit (a week, a day, a plan); parts are drawn in proportion to value. Use it for run/walk intervals,
     opening hours and time slots, budget or time composition, before/after splits. repeat: true draws value-wide
     blocks side by side instead of stretching (8 blocks of 1'+2').
   tone: "accent" | "danger" | "positive" | "muted" | "ink" | "data-2" ... (defaults: first series accent, others muted) */
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const TONE = (t) => `var(--${t === "muted" ? "data-muted" : t === "ink" ? "ink-2" : t === "soft" ? "accent-soft" : t || "accent"})`;
  function niceTicks(max, count = 5) {
    if (!(max > 0)) return { top: 1, ticks: [0, 1] };
    const raw = max / count;
    const pow = 10 ** Math.floor(Math.log10(raw));
    const f = raw / pow;
    const step = (f <= 1 ? 1 : f <= 2 ? 2 : f <= 2.5 ? 2.5 : f <= 5 ? 5 : 10) * pow;
    const top = Math.ceil(max / step - 1e-9) * step;
    const ticks = [];
    for (let v = 0; v <= top + step / 2; v += step) ticks.push(Math.round(v * 1e6) / 1e6);
    return { top, ticks };
  }
  const fmt = (v, unit, format) => (format ? format(v) : `${Number(v).toLocaleString()}${unit || ""}`);
  function node(tag, attrs, parent, text) {
    const n = document.createElementNS(NS, tag);
    for (const [k, v] of Object.entries(attrs || {})) n.setAttribute(k, v);
    if (text != null) n.textContent = text;
    if (parent) parent.appendChild(n);
    return n;
  }
  // Chart text size comes from --chart-fs (12px on web; canvas.css raises it), and paddings scale with it.
  const unitOf = (el) => (Number.parseFloat(getComputedStyle(el).getPropertyValue("--chart-fs")) || 12) / 12;
  function frame(el, height) {
    el.innerHTML = "";
    el.classList.add("chart");
    const w = Math.max(280, Math.round(el.clientWidth || 640));
    const svg = node("svg", { viewBox: `0 0 ${w} ${height}`, role: "img" });
    el.appendChild(svg);
    return { svg, w };
  }
  function legend(el, series) {
    if (series.length < 2) return;
    const lg = document.createElement("div");
    lg.className = "chart-legend";
    series.forEach((s, i) => {
      const item = document.createElement("span");
      const sw = document.createElement("i");
      sw.style.background = TONE(s.tone || (i === 0 ? "accent" : "muted"));
      if (s.dashed) sw.style.background = "transparent", sw.style.borderTop = `2px dashed ${TONE(s.tone || "muted")}`;
      item.append(sw, s.name);
      lg.appendChild(item);
    });
    el.prepend(lg);
  }
  function yAxis(g, ticks, top, x0, x1, y, fmtTick, k = 1) {
    const grid = node("g", { class: "grid" }, g);
    const ax = node("g", { class: "ax" }, g);
    ticks.forEach((t) => {
      const yy = y(t);
      if (t !== 0) node("line", { x1: x0, x2: x1, y1: yy, y2: yy }, grid);
      node("text", { x: x0 - 8 * k, y: yy + 4 * k, "text-anchor": "end" }, ax, fmtTick(t));
    });
    node("line", { class: "base", x1: x0, x2: x1, y1: y(0), y2: y(0) }, g);
  }
  function title(svg, text) { if (text) node("title", {}, svg, text); }

  function bar(el, o) {
    const series = o.series || [{ name: o.name || "", values: o.values }];
    const labels = o.labels;
    const draw = () => {
      const k = unitOf(el); const height = o.height || Math.round(260 * k);
      const { svg, w } = frame(el, height);
      title(svg, o.title || series.map((s) => s.name).join(" / "));
      const max = Math.max(...series.flatMap((s) => s.values));
      const { top, ticks } = niceTicks(max, o.ticks || 4);
      const left = 44 * k; const right = 8 * k; const topPad = 22 * k; const bottom = 28 * k;
      const y = (v) => topPad + (height - topPad - bottom) * (1 - v / top);
      const g = node("g", {}, svg);
      yAxis(g, ticks, top, left, w - right, y, (t) => fmt(t, "", o.tickFormat), k);
      const band = (w - left - right) / labels.length;
      const inner = band * 0.72; const bw = inner / series.length;
      const hl = new Set(o.highlight || []);
      labels.forEach((lab, i) => {
        const x0 = left + band * i + (band - inner) / 2;
        series.forEach((s, j) => {
          const v = s.values[i];
          const tone = hl.size ? (hl.has(i) && j === 0 ? s.tone || "accent" : j === 0 ? "muted" : s.tone || "ink") : s.tone || (j === 0 ? "accent" : "muted");
          const x = x0 + bw * j;
          node("rect", { x: x + 1, y: y(v), width: Math.max(2, bw - 2), height: Math.max(0, y(0) - y(v)), rx: 2, style: `fill:${TONE(tone)}` }, g);
          if (o.labelValues !== false && (series.length === 1 || j === 0)) {
            node("text", { class: `val${hl.has(i) ? " is-hl" : ""}`, x: x + bw / 2, y: y(v) - 6 * k, "text-anchor": "middle" }, g, fmt(v, o.unit, o.format));
          }
        });
        node("text", { class: "lbl", x: left + band * i + band / 2, y: height - 8 * k, "text-anchor": "middle" }, g, lab);
      });
      if (o.annotate) {
        const i = o.annotate.index;
        node("text", { class: "ann", x: Math.min(w - right, left + band * i + band / 2), y: 12 * k, "text-anchor": i > labels.length / 2 ? "end" : "start" }, g, o.annotate.text);
      }
      legend(el, series);
    };
    draw();
    observe(el, draw);
  }

  function hbar(el, o) {
    const labels = o.labels; const values = o.values;
    const draw = () => {
      const k = unitOf(el); const row = 30 * k; const height = labels.length * row + 8 * k;
      const { svg, w } = frame(el, height);
      title(svg, o.title || "");
      const labelW = Math.min(160 * k, Math.max(64 * k, Math.max(...labels.map((l) => String(l).length)) * 13 * k));
      const valueW = 64 * k;
      const max = o.max || niceTicks(Math.max(...values), 4).top;
      const x = (v) => labelW + ((w - labelW - valueW) * v) / max;
      const hl = new Set(o.highlight || []);
      const g = node("g", {}, svg);
      labels.forEach((lab, i) => {
        const yy = 4 * k + i * row;
        node("text", { class: "lbl", x: 0, y: yy + 17 * k }, g, lab);
        node("rect", { x: labelW, y: yy + 6 * k, width: Math.max(0, x(values[i]) - labelW), height: 14 * k, rx: 2, style: `fill:${TONE(hl.size ? (hl.has(i) ? o.tone || "accent" : "muted") : o.tone || "accent")}` }, g);
        node("text", { class: `val${hl.has(i) ? " is-hl" : ""}`, x: x(values[i]) + 6 * k, y: yy + 17 * k }, g, fmt(values[i], o.unit, o.format));
      });
    };
    draw();
    observe(el, draw);
  }

  function line(el, o) {
    const series = o.series; const labels = o.labels;
    const draw = () => {
      const k = unitOf(el); const height = o.height || Math.round(260 * k);
      const { svg, w } = frame(el, height);
      title(svg, o.title || series.map((s) => s.name).join(" / "));
      const max = Math.max(...series.flatMap((s) => s.values), o.threshold ? o.threshold.value : 0);
      const { top, ticks } = niceTicks(max, o.ticks || 4);
      const left = 44 * k; const right = 64 * k; const topPad = 22 * k; const bottom = 28 * k;
      const y = (v) => topPad + (height - topPad - bottom) * (1 - v / top);
      const x = (i) => left + ((w - left - right) * i) / Math.max(1, labels.length - 1);
      const g = node("g", {}, svg);
      yAxis(g, ticks, top, left, w - right, y, (t) => fmt(t, "", o.tickFormat), k);
      const every = Math.ceil(labels.length / Math.max(2, Math.floor((w - left - right) / (56 * k))));
      labels.forEach((lab, i) => { if (i % every === 0 || i === labels.length - 1) node("text", { class: "lbl", x: x(i), y: height - 8 * k, "text-anchor": "middle" }, g, lab); });
      if (o.threshold) {
        const ty = y(o.threshold.value);
        node("line", { x1: left, x2: w - right, y1: ty, y2: ty, style: "stroke:var(--danger);stroke-dasharray:4 4" }, g);
        node("text", { class: "lbl", x: w - right + 4 * k, y: ty + 4 * k }, g, o.threshold.label || fmt(o.threshold.value, o.unit));
      }
      series.forEach((s, j) => {
        const tone = s.tone || (j === 0 ? "accent" : "muted");
        const d = s.values.map((v, i) => `${i ? "L" : "M"}${x(i).toFixed(1)},${y(v).toFixed(1)}`).join("");
        node("path", { d, fill: "none", style: `stroke:${TONE(tone)};stroke-width:${(j === 0 ? 2.5 : 1.75) * k}${s.dashed ? `;stroke-dasharray:${5 * k} ${4 * k}` : ""}` }, g);
        const last = s.values.length - 1;
        node("circle", { cx: x(last), cy: y(s.values[last]), r: 3.5 * k, style: `fill:${TONE(tone)}` }, g);
        node("text", { class: `val${j === 0 ? " is-hl" : ""}`, x: x(last) + 8 * k, y: y(s.values[last]) + 4 * k }, g, fmt(s.values[last], o.unit, o.format));
      });
      if (o.annotate) {
        const s = series[o.annotate.series || 0]; const i = o.annotate.index;
        node("circle", { cx: x(i), cy: y(s.values[i]), r: 5 * k, style: `fill:none;stroke:var(--ink);stroke-width:${1.5 * k}` }, g);
        node("text", { class: "ann", x: x(i), y: y(s.values[i]) - 12 * k, "text-anchor": i > labels.length / 2 ? "end" : "start" }, g, o.annotate.text);
      }
      legend(el, series);
    };
    draw();
    observe(el, draw);
  }

  function segments(el, o) {
    el.innerHTML = "";
    el.classList.add("segs");
    if (o.legend) {
      const lg = document.createElement("div");
      lg.className = "chart-legend";
      o.legend.forEach((l) => { const s = document.createElement("span"); const i = document.createElement("i"); i.style.background = TONE(l.tone); s.append(i, l.text); lg.appendChild(s); });
      el.appendChild(lg);
    }
    const total = Math.max(...o.rows.map((r) => r.parts.reduce((a, p) => a + p.value, 0)));
    o.rows.forEach((r) => {
      const row = document.createElement("div");
      row.className = "segs__row";
      const head = document.createElement("div");
      head.className = "segs__head";
      head.innerHTML = `<b></b><span></span>`;
      head.querySelector("b").textContent = r.label || "";
      head.querySelector("span").textContent = r.note || "";
      const bar = document.createElement("div");
      bar.className = "segs__bar";
      const sum = r.parts.reduce((a, p) => a + p.value, 0);
      r.parts.forEach((p) => {
        const seg = document.createElement("i");
        seg.style.flexGrow = String(p.value);
        seg.style.background = TONE(p.tone || "accent");
        // labels sit only on accent segments, where on-accent text is guaranteed to pass contrast
        if (p.tone === "muted" || p.tone === "soft") seg.classList.add("is-quiet");
        if (p.text && (!p.tone || p.tone === "accent")) seg.textContent = p.text; else if (p.text) seg.title = p.text;
        bar.appendChild(seg);
      });
      if (!o.repeat && sum < total) { const pad = document.createElement("i"); pad.className = "is-empty"; pad.style.flexGrow = String(total - sum); bar.appendChild(pad); }
      row.append(head, bar);
      el.appendChild(row);
    });
  }

  function observe(el, draw) {
    if (!("ResizeObserver" in window)) return;
    let last = el.clientWidth;
    const ro = new ResizeObserver(() => { if (Math.abs(el.clientWidth - last) > 24) { last = el.clientWidth; draw(); } });
    ro.observe(el);
  }

  // Position the "now" marker and slots in a .windows time bar: data-start/data-end hours on slots, data-from/data-to on the bar.
  function windows(el, now = new Date()) {
    const from = Number(el.dataset.from || 8); const to = Number(el.dataset.to || 22);
    const pos = (h) => `${((h - from) / (to - from)) * 100}%`;
    el.querySelectorAll(".windows__slot").forEach((s) => {
      s.style.left = pos(Number(s.dataset.start)); s.style.width = `calc(${pos(Number(s.dataset.end))} - ${pos(Number(s.dataset.start))})`;
    });
    const marker = el.querySelector(".windows__now");
    const h = now.getHours() + now.getMinutes() / 60;
    if (marker) { if (h >= from && h <= to) marker.style.left = pos(h); else marker.remove(); }
  }

  window.UDChart = { bar, hbar, line, segments, niceTicks, windows };
})();
