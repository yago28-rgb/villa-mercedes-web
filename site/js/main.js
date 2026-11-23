/* ==========================================================================
   Villa Mercedes · main.js
   Sin dependencias. Cada efecto está reescrito a partir de componentes MIT de
   21st.dev (Aceternity UI y Motion Primitives). Cada módulo solo se activa si
   la página contiene su marcado, así que el mismo archivo sirve a todas.
   ========================================================================== */
"use strict";

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const lerp = (a, b, t) => a + (b - a) * t;
const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;
const FINE = matchMedia("(hover: hover) and (pointer: fine)").matches;
const hasIO = "IntersectionObserver" in window;
const CONFIG = JSON.parse($("#site-config")?.textContent || "{}");

/* ── Textos de la interfaz en español, inglés y francés ──────────────── */
const LANG = (document.documentElement.lang || "es").slice(0, 2);
const LOCALE = { es: "es-ES", en: "en-GB", fr: "fr-FR" }[LANG] || "es-ES";
const I18N = {
  es: {
    play: "Reproducir", pause: "Pausar", photos: (n) => `${n} ${n === 1 ? "fotografía" : "fotografías"}`, of: "de", see: "Ver",
    wait: "Espera unos segundos antes de volver a enviar.", name: "Escribe tu nombre.", fullName: "Escribe tu nombre y apellidos.",
    email: "Escribe un email válido.", msg: "Escribe al menos 10 caracteres.", consent: "Necesitamos tu permiso para publicarla.",
    phone: "Escribe un teléfono de contacto.", terms: "Debes aceptar las condiciones de reserva.",
    noChannel: "No hemos podido abrir el envío. Inténtalo de nuevo más tarde.", pendingChannel: "[PENDIENTE: configura WHATSAPP o EMAIL en build.py]",
    sent: "Mensaje preparado. Envíalo desde la ventana que se ha abierto.",
    sentBooking: "Solicitud preparada. Envíala desde la ventana que se ha abierto y te confirmaremos disponibilidad y precio.",
    reviewMsg: (f) => `Opinión sobre Villa Mercedes\nNombre: ${f.name}\nFecha de la estancia: ${f.stay}\nPuntuación: ${f.rating}/10\n\n${f.message}\n\nAutorizo su publicación en la web.`,
    contactMsg: (f) => `Hola, soy ${f.name}.\n\n${f.message}\n\nEmail: ${f.email}`,
    subjReview: "Opinión · Villa Mercedes", subjContact: "Consulta · Villa Mercedes", subjBooking: "Solicitud de reserva · Villa Mercedes",
    wd: ["L", "M", "X", "J", "V", "S", "D"], arrival: ", llegada", departure: ", salida", unavailable: ", no disponible",
    night: (n) => (n === 1 ? "noche" : "noches"), chooseDates: "Elige fechas",
    guests: (a, c) => `${a} ${a === 1 ? "adulto" : "adultos"}${c ? `, ${c} ${c === 1 ? "niño" : "niños"}` : ""}`,
    pickStart: "Elige el día de llegada", pickEnd: "Ahora elige el día de salida", selected: (n) => `${n} ${n === 1 ? "noche seleccionada" : "noches seleccionadas"}`,
    rDates: "Fechas", rNights: "Noches", rGuests: "Huéspedes", rName: "A nombre de", rContact: "Contacto",
    bookMsg: (d) => [`Hola, quiero reservar Villa Mercedes.`, `Fechas: del ${d.from} al ${d.to} (${d.n} ${d.n === 1 ? "noche" : "noches"}).`, `Huéspedes: ${d.guests}.`, d.notes ? `\n${d.notes}\n` : "", `Nombre: ${d.name}`, `Email: ${d.email}`, `Teléfono: ${d.phone}`],
    resumeTour: "Reanudar recorrido automático", pauseTour: "Pausar recorrido automático",
  },
  en: {
    play: "Play", pause: "Pause", photos: (n) => `${n} ${n === 1 ? "photo" : "photos"}`, of: "of", see: "View",
    wait: "Please wait a few seconds before sending again.", name: "Please enter your name.", fullName: "Please enter your full name.",
    email: "Please enter a valid email address.", msg: "Please write at least 10 characters.", consent: "We need your permission to publish it.",
    phone: "Please enter a contact phone number.", terms: "Please accept the booking terms.",
    noChannel: "We couldn’t open the message. Please try again later.", pendingChannel: "[PENDIENTE: configura WHATSAPP o EMAIL en build.py]",
    sent: "Message ready. Send it from the window that has just opened.",
    sentBooking: "Request ready. Send it from the window that has just opened and we’ll confirm availability and price.",
    reviewMsg: (f) => `Review of Villa Mercedes\nName: ${f.name}\nMonth of stay: ${f.stay}\nScore: ${f.rating}/10\n\n${f.message}\n\nI agree to it being published on the website.`,
    contactMsg: (f) => `Hello, my name is ${f.name}.\n\n${f.message}\n\nEmail: ${f.email}`,
    subjReview: "Review · Villa Mercedes", subjContact: "Enquiry · Villa Mercedes", subjBooking: "Booking request · Villa Mercedes",
    wd: ["M", "T", "W", "T", "F", "S", "S"], arrival: ", check-in", departure: ", check-out", unavailable: ", unavailable",
    night: (n) => (n === 1 ? "night" : "nights"), chooseDates: "Choose dates",
    guests: (a, c) => `${a} ${a === 1 ? "adult" : "adults"}${c ? `, ${c} ${c === 1 ? "child" : "children"}` : ""}`,
    pickStart: "Choose your arrival date", pickEnd: "Now choose your departure date", selected: (n) => `${n} ${n === 1 ? "night" : "nights"} selected`,
    rDates: "Dates", rNights: "Nights", rGuests: "Guests", rName: "Name", rContact: "Contact",
    bookMsg: (d) => [`Hello, I’d like to book Villa Mercedes.`, `Dates: ${d.from} to ${d.to} (${d.n} ${d.n === 1 ? "night" : "nights"}).`, `Guests: ${d.guests}.`, d.notes ? `\n${d.notes}\n` : "", `Name: ${d.name}`, `Email: ${d.email}`, `Phone: ${d.phone}`],
    resumeTour: "Resume automatic tour", pauseTour: "Pause automatic tour",
  },
  fr: {
    play: "Lecture", pause: "Pause", photos: (n) => `${n} photo${n === 1 ? "" : "s"}`, of: "sur", see: "Voir",
    wait: "Patientez quelques secondes avant de renvoyer.", name: "Indiquez votre nom.", fullName: "Indiquez votre nom et prénom.",
    email: "Indiquez une adresse email valide.", msg: "Écrivez au moins 10 caractères.", consent: "Nous avons besoin de votre accord pour le publier.",
    phone: "Indiquez un numéro de téléphone.", terms: "Vous devez accepter les conditions de réservation.",
    noChannel: "Impossible d’ouvrir l’envoi. Réessayez plus tard.", pendingChannel: "[PENDIENTE: configura WHATSAPP o EMAIL en build.py]",
    sent: "Message prêt. Envoyez-le depuis la fenêtre qui vient de s’ouvrir.",
    sentBooking: "Demande prête. Envoyez-la depuis la fenêtre qui vient de s’ouvrir : nous vous confirmerons disponibilité et prix.",
    reviewMsg: (f) => `Avis sur Villa Mercedes\nNom : ${f.name}\nMois du séjour : ${f.stay}\nNote : ${f.rating}/10\n\n${f.message}\n\nJ’accepte sa publication sur le site.`,
    contactMsg: (f) => `Bonjour, je m’appelle ${f.name}.\n\n${f.message}\n\nEmail : ${f.email}`,
    subjReview: "Avis · Villa Mercedes", subjContact: "Demande · Villa Mercedes", subjBooking: "Demande de réservation · Villa Mercedes",
    wd: ["L", "M", "M", "J", "V", "S", "D"], arrival: ", arrivée", departure: ", départ", unavailable: ", indisponible",
    night: (n) => (n === 1 ? "nuit" : "nuits"), chooseDates: "Choisissez vos dates",
    guests: (a, c) => `${a} adulte${a === 1 ? "" : "s"}${c ? `, ${c} enfant${c === 1 ? "" : "s"}` : ""}`,
    pickStart: "Choisissez la date d’arrivée", pickEnd: "Choisissez maintenant la date de départ", selected: (n) => `${n} nuit${n === 1 ? "" : "s"} sélectionnée${n === 1 ? "" : "s"}`,
    rDates: "Dates", rNights: "Nuits", rGuests: "Voyageurs", rName: "Au nom de", rContact: "Contact",
    bookMsg: (d) => [`Bonjour, je souhaite réserver Villa Mercedes.`, `Dates : du ${d.from} au ${d.to} (${d.n} nuit${d.n === 1 ? "" : "s"}).`, `Voyageurs : ${d.guests}.`, d.notes ? `\n${d.notes}\n` : "", `Nom : ${d.name}`, `Email : ${d.email}`, `Téléphone : ${d.phone}`],
    resumeTour: "Reprendre la visite automatique", pauseTour: "Mettre en pause la visite automatique",
  },
};
const T = I18N[LANG] || I18N.es;
const esc = (v) => String(v).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

/* ── Utilidad: aparece una vez al entrar en pantalla ─────────────────── */
function onceInView(els, cb, opts = { rootMargin: "0px 0px -12% 0px" }) {
  if (!hasIO || REDUCED) { els.forEach((el) => cb(el)); return; }
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { cb(e.target); io.unobserve(e.target); } });
  }, opts);
  els.forEach((el) => io.observe(el));
}

/* ── Bucle de scroll común (un solo listener y rAF para toda la página) ─ */
const scrollTasks = [];
let ticking = false;
function addScrollTask(fn) { scrollTasks.push(fn); }
function runScroll() {
  ticking = false;
  const vh = innerHeight;
  scrollTasks.forEach((fn) => fn(vh));
}
addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(runScroll); } }, { passive: true });
addEventListener("resize", () => requestAnimationFrame(runScroll));
/* progreso 0→1 de un elemento entre que su parte superior entra por abajo (start) y sale (end) */
function progressOf(el, vh, start = 1, end = 0) {
  const r = el.getBoundingClientRect();
  const a = vh * start;
  const b = vh * end - r.height;
  return clamp((a - r.top) / (a - b));
}

/* ── Navegación global (móvil) y local fija ──────────────────────────── */
(() => {
  const gnav = $(".gnav");
  const btn = $(".gnav-menu");
  if (btn) {
    btn.addEventListener("click", () => {
      const open = !gnav.classList.contains("is-open");
      gnav.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", String(open));
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && gnav.classList.contains("is-open")) { gnav.classList.remove("is-open"); btn.setAttribute("aria-expanded", "false"); btn.focus(); }
    });
  }
  const lnav = $(".lnav");
  const bar = $(".scroll-progress");
  if (lnav) addScrollTask(() => {
    lnav.classList.toggle("is-stuck", scrollY > 44);
    const max = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.setProperty("--p", max > 0 ? (scrollY / max).toFixed(4) : "0");
  });
})();

/* ── Animated Background (Motion Primitives) ─────────────────────────── */
function animatedBackground(group, { follow = "hover", activeSel = "[aria-pressed=true],[aria-current]" } = {}) {
  const pill = document.createElement("span");
  pill.className = "ab-pill";
  pill.setAttribute("aria-hidden", "true");
  group.prepend(pill);
  const items = () => $$(":scope > a, :scope > button", group);
  const moveTo = (el) => {
    if (!el) return;
    pill.style.width = `${el.offsetWidth}px`;
    pill.style.height = `${el.offsetHeight}px`;
    pill.style.transform = `translate(${el.offsetLeft}px, ${el.offsetTop}px)`;
  };
  const active = () => items().find((el) => el.matches(activeSel));
  if (follow === "hover") {
    group.addEventListener("pointerover", (e) => {
      const el = e.target.closest("a,button");
      if (el && group.contains(el)) { group.classList.add("is-hover"); moveTo(el); }
    });
    group.addEventListener("pointerleave", () => group.classList.remove("is-hover"));
    group.addEventListener("focusin", (e) => { group.classList.add("is-hover"); moveTo(e.target); });
    group.addEventListener("focusout", () => group.classList.remove("is-hover"));
  } else {
    moveTo(active());
    addEventListener("resize", () => moveTo(active()));
  }
  return { refresh: () => moveTo(active()) };
}
$$(".lnav-links, .gnav-links").forEach((g) => { if (g.matches(".lnav-links")) animatedBackground(g); });

/* ── Magnetic (Motion Primitives) ────────────────────────────────────── */
if (FINE && !REDUCED) {
  $$("[data-magnetic]").forEach((el) => {
    const s = Number(el.dataset.magnetic) || 0.35;
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      el.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * s}px, ${(e.clientY - r.top - r.height / 2) * s}px)`;
    });
    el.addEventListener("pointerleave", () => { el.style.transform = ""; });
  });
}

/* ── Text Effect (Motion Primitives) / Text Generate (Aceternity) ────── */
$$("[data-text-effect]").forEach((el) => {
  if (REDUCED) return;
  const walk = (node) => {
    [...node.childNodes].forEach((n) => {
      if (n.nodeType === 3) {
        const frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach((part) => {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.append(part); return; }
          const s = document.createElement("span");
          s.className = "tw";
          s.textContent = part;
          frag.append(s);
        });
        n.replaceWith(frag);
      } else if (n.nodeType === 1 && n.tagName !== "BR") walk(n);
    });
  };
  el.setAttribute("aria-label", el.textContent.trim().replace(/\s+/g, " "));
  walk(el);
  $$(".tw", el).forEach((w, i) => { w.style.setProperty("--i", i); w.setAttribute("aria-hidden", "true"); });
});
const textEffects = $$("[data-text-effect]");
requestAnimationFrame(() => requestAnimationFrame(() => onceInView(textEffects, (el) => el.classList.add("is-in"), { rootMargin: "0px 0px -5% 0px" })));

/* ── Revelados ───────────────────────────────────────────────────────── */
(() => {
  const els = $$("[data-reveal]");
  const groups = new Map();
  els.forEach((el) => {
    const n = groups.get(el.parentElement) || 0;
    groups.set(el.parentElement, n + 1);
    if (!el.style.getPropertyValue("--d")) el.style.setProperty("--d", `${Math.min(n, 6) * 0.08}s`);
  });
  onceInView(els, (el) => el.classList.add("is-in"));
  onceInView($$("[data-clip]"), (el) => el.classList.add("is-in"), { rootMargin: "0px 0px -18% 0px" });
})();

/* ── Container Scroll Animation (Aceternity UI) + vídeo ──────────────── */
(() => {
  const wrap = $(".cs");
  if (!wrap) return;
  const card = $(".cs-card", wrap);
  if (!REDUCED) addScrollTask((vh) => {
    const r = wrap.getBoundingClientRect();
    const p = clamp((vh - r.top) / (vh * 0.95));
    const e = 1 - Math.pow(1 - p, 3);
    card.style.setProperty("--rx", `${(22 * (1 - e)).toFixed(2)}deg`);
    card.style.setProperty("--sc", (0.92 + 0.08 * e).toFixed(4));
  });

  const mobile = matchMedia("(max-width: 734px)").matches;
  const video = $("video", wrap);
  const slides = $(".slides", wrap);
  const pause = $(".cs-pause", wrap);
  const label = $(".cs-label", wrap);
  let userPaused = REDUCED;
  const setPressed = (p) => {
    pause.setAttribute("aria-pressed", String(p));
    $(".sr-only", pause).textContent = p ? T.play : T.pause;
  };
  const setLabel = (t) => {
    if (label.textContent === t) return;
    label.classList.add("is-out");
    setTimeout(() => { label.textContent = t; label.classList.remove("is-out"); }, 250);
  };

  if (mobile || !video) {
    // Fotos reales en vertical, nítidas, con Ken Burns
    video?.remove();
    slides.hidden = false;
    const imgs = $$("img", slides);
    let i = 0;
    let timer = null;
    const show = (k) => {
      imgs.forEach((im, j) => im.classList.toggle("is-on", j === k));
      setLabel(imgs[k].dataset.label);
    };
    const play = () => { if (!timer && !userPaused) timer = setInterval(() => { i = (i + 1) % imgs.length; show(i); }, 5200); };
    const stop = () => { clearInterval(timer); timer = null; };
    show(0);
    setPressed(userPaused);
    if (!userPaused) play();
    pause.addEventListener("click", () => { userPaused = !userPaused; setPressed(userPaused); userPaused ? stop() : play(); });
    if (hasIO) new IntersectionObserver(([e]) => (e.isIntersecting ? play() : stop())).observe(slides);
    return;
  }

  slides?.remove();
  video.poster = video.dataset.poster;
  video.src = video.dataset.src;
  if (userPaused) setPressed(true);
  else video.play().then(() => setPressed(false)).catch(() => setPressed(true));
  pause.addEventListener("click", () => {
    if (video.paused) { userPaused = false; video.play(); setPressed(false); }
    else { userPaused = true; video.pause(); setPressed(true); }
  });
  if (hasIO) new IntersectionObserver(([e]) => { if (!userPaused) e.isIntersecting ? video.play().catch(() => {}) : video.pause(); }).observe(video);
  const scenes = JSON.parse(video.dataset.scenes || "[[0,\"\"]]");
  video.addEventListener("timeupdate", () => {
    let t = scenes[0][1];
    scenes.forEach(([s, n]) => { if (video.currentTime >= s) t = n; });
    setLabel(t);
  });
})();

/* ── Statement: relleno palabra a palabra con el scroll ──────────────── */
(() => {
  const p = $(".statement p");
  if (!p || REDUCED) return;
  const text = p.textContent.trim();
  const hl = (p.dataset.highlight || "").split("|").filter(Boolean);
  p.innerHTML = `<span class="sr-only">${p.innerHTML}</span>` + text.split(/\s+/).map((w) => `<span class="sw${hl.some((h) => w.includes(h)) ? " hl" : ""}" aria-hidden="true">${w}</span>`).join(" ");
  const words = $$(".sw", p);
  addScrollTask((vh) => {
    const r = p.getBoundingClientRect();
    const prog = clamp((vh * 0.82 - r.top) / (r.height + vh * 0.3));
    const lit = Math.round(prog * words.length);
    words.forEach((w, i) => w.classList.toggle("on", i < lit));
  });
})();

/* ── Infinite Slider (Motion Primitives): velocidad suave al pasar el ratón ─ */
$$(".islider").forEach((wrap) => {
  const track = $(".islider-track", wrap);
  if (REDUCED) return;
  track.innerHTML += track.innerHTML;
  $$(":scope > *", track).slice(track.children.length / 2).forEach((c) => c.setAttribute("aria-hidden", "true"));
  const base = Number(wrap.dataset.speed || 40);
  const hover = Number(wrap.dataset.speedHover || 12);
  let speed = base;
  let target = base;
  let x = 0;
  let last = performance.now();
  let visible = true;
  wrap.addEventListener("pointerenter", () => { target = hover; });
  wrap.addEventListener("pointerleave", () => { target = base; });
  if (hasIO) new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(wrap);
  const loop = (now) => {
    const dt = Math.min(0.05, (now - last) / 1000);
    last = now;
    if (visible && !document.hidden) {
      speed = lerp(speed, target, 0.06);
      const half = track.scrollWidth / 2;
      x -= speed * dt;
      if (-x >= half) x += half;
      track.style.transform = `translate3d(${x}px,0,0)`;
    }
    requestAnimationFrame(loop);
  };
  requestAnimationFrame(loop);
});

/* ── Carousel con microinteracciones (Aceternity UI) ─────────────────── */
$$(".car").forEach((car) => {
  const scroller = $(".car-scroller", car);
  const cards = $$(".car-card", car);
  const dots = $$(".car-dot", car);
  const prev = $(".car-prev", car);
  const next = $(".car-next", car);
  let current = 0;
  let padL = parseFloat(getComputedStyle($(".car-track", car)).paddingLeft) || 0;
  addEventListener("resize", () => { padL = parseFloat(getComputedStyle($(".car-track", car)).paddingLeft) || 0; });
  const go = (i) => {
    const c = cards[clamp(i, 0, cards.length - 1)];
    scroller.scrollTo({ left: c.offsetLeft - padL, behavior: REDUCED ? "auto" : "smooth" });
  };
  const mark = () => {
    const sl = scroller.scrollLeft;
    let best = 0;
    let bestD = Infinity;
    cards.forEach((c, i) => {
      const d = Math.abs(c.offsetLeft - padL - sl);
      if (d < bestD) { bestD = d; best = i; }
    });
    current = best;
    dots.forEach((d, i) => d.setAttribute("aria-current", String(i === best)));
    prev.disabled = sl < 4;
    next.disabled = sl > scroller.scrollWidth - scroller.clientWidth - 4;
  };
  scroller.addEventListener("scroll", () => requestAnimationFrame(mark), { passive: true });
  dots.forEach((d, i) => d.addEventListener("click", () => go(i)));
  prev.addEventListener("click", () => go(current - 1));
  next.addEventListener("click", () => go(current + 1));
  requestAnimationFrame(mark);
  if (FINE && !REDUCED) {
    cards.forEach((c) => {
      c.addEventListener("pointermove", (e) => {
        const r = c.getBoundingClientRect();
        c.style.setProperty("--tx", `${((e.clientX - r.left) / r.width - 0.5) * 10}deg`);
        c.style.setProperty("--ty", `${-((e.clientY - r.top) / r.height - 0.5) * 10}deg`);
      });
      c.addEventListener("pointerleave", () => { c.style.removeProperty("--tx"); c.style.removeProperty("--ty"); });
    });
  }
});

/* ── Sliding Number (Motion Primitives) ──────────────────────────────── */
const SN = {
  build(el, value, decimals = 0) {
    const str = new Intl.NumberFormat(LOCALE, { minimumFractionDigits: decimals, maximumFractionDigits: decimals }).format(value);
    el.dataset.value = str;
    el.innerHTML = `<span class="sr-only">${str}</span>` + [...str].map((ch, k) => (/\d/.test(ch)
      ? `<span class="sn-col" aria-hidden="true"><span class="sn-strip" style="--k:${k}">${"0123456789".split("").map((n) => `<span>${n}</span>`).join("")}</span></span>`
      : `<span class="sn-sep" aria-hidden="true">${ch}</span>`)).join("");
    return str;
  },
  set(el, value, decimals = 0) {
    const str = new Intl.NumberFormat(LOCALE, { minimumFractionDigits: decimals, maximumFractionDigits: decimals }).format(value);
    if (el.dataset.len !== String(str.length)) { SN.build(el, value, decimals); el.dataset.len = String(str.length); el.offsetHeight; }
    const sr = $(".sr-only", el);
    if (sr) sr.textContent = str;
    let k = 0;
    $$(".sn-strip", el).forEach((s) => {
      while (!/\d/.test(str[k])) k++;
      s.style.transform = `translateY(-${Number(str[k]) * 10}%)`;
      k++;
    });
  },
};
$$("[data-sliding]").forEach((el) => {
  const v = Number(el.dataset.sliding);
  const d = Number(el.dataset.decimals || 0);
  if (REDUCED || !hasIO) { SN.set(el, v, d); return; }
  onceInView([el], () => { SN.build(el, v, d); el.dataset.len = String(el.dataset.value.length); }, { rootMargin: "300px 0px" });
  onceInView([el], () => requestAnimationFrame(() => SN.set(el, v, d)), { threshold: 0.6 });
});

/* ── Hero Parallax (Aceternity UI) ───────────────────────────────────── */
(() => {
  const hp = $(".hp");
  if (!hp || REDUCED) return;
  const stage = $(".hp-stage", hp);
  const rows = $$(".hp-row", hp);
  addScrollTask((vh) => {
    const r = hp.getBoundingClientRect();
    const p = clamp((vh - r.top) / (r.height + vh * 0.2));
    const e = clamp(p / 0.45);
    stage.style.setProperty("--hrx", `${(15 * (1 - e)).toFixed(2)}deg`);
    stage.style.setProperty("--hrz", `${(18 * (1 - e)).toFixed(2)}deg`);
    stage.style.setProperty("--hty", `${(-120 * (1 - e) + 40 * e).toFixed(1)}px`);
    stage.style.setProperty("--hop", (0.25 + 0.75 * e).toFixed(3));
    rows.forEach((row, i) => {
      const dir = i % 2 === 0 ? 1 : -1;
      row.style.transform = `translate3d(${(dir * (p * 520 - 200)).toFixed(1)}px,0,0)`;
    });
  });
})();

/* ── Ruta dibujada a Berria ──────────────────────────────────────────── */
(() => {
  const map = $(".route-map");
  if (!map) return;
  const path = $(".route-path", map);
  map.style.setProperty("--len", path.getTotalLength().toFixed(1));
  if (REDUCED) { map.style.setProperty("--draw", 1); map.style.setProperty("--pin", 1); return; }
  addScrollTask((vh) => {
    const p = progressOf(map, vh, 0.95, 0.35);
    map.style.setProperty("--draw", clamp(p * 1.15).toFixed(3));
    map.style.setProperty("--pin", clamp((p - 0.75) * 4).toFixed(3));
  });
})();

/* ── CTA final: imagen que se acerca con el scroll ───────────────────── */
(() => {
  const f = $(".final");
  if (!f || REDUCED) return;
  addScrollTask((vh) => f.style.setProperty("--fs", (1.15 - 0.15 * progressOf(f, vh, 1, 0.2)).toFixed(4)));
})();

/* ── Barra de reserva fija: tras el hero y oculta al llegar al pie ───── */
(() => {
  const bar = $(".bookbar");
  if (!bar) return;
  const hero = $("[data-bookbar-after]");
  const foot = $(".final") || $(".foot");
  addScrollTask((vh) => {
    const after = hero ? hero.getBoundingClientRect().bottom < 0 : scrollY > vh;
    const nearFoot = foot.getBoundingClientRect().top < vh * 0.9;
    bar.classList.toggle("is-on", after && !nearFoot);
  });
})();

/* ── Sticky Scroll Reveal (Aceternity UI) ────────────────────────────── */
(() => {
  const ssr = $(".ssr");
  if (!ssr) return;
  const steps = $$(".ssr-step", ssr);
  const imgs = $$(".ssr-img", ssr);
  const bars = $$(".ssr-progress span", ssr);
  let active = -1;
  const set = (i) => {
    if (i === active) return;
    imgs.forEach((im, k) => { im.classList.toggle("was-active", k === active); im.classList.toggle("is-active", k === i); });
    steps.forEach((s, k) => s.classList.toggle("is-active", k === i));
    active = i;
  };
  set(0);
  addScrollTask((vh) => {
    let i = 0;
    steps.forEach((s, k) => { if (s.getBoundingClientRect().top < vh * 0.55) i = k; });
    set(i);
    bars.forEach((b, k) => {
      const r = steps[k].getBoundingClientRect();
      const f = k < i ? 1 : k > i ? 0 : clamp((vh * 0.55 - r.top) / r.height);
      b.style.setProperty("--f", f.toFixed(3));
    });
  });
})();

/* ── Lens (Aceternity UI) ────────────────────────────────────────────── */
$$("[data-lens]").forEach((lens) => {
  const img = $("img", lens);
  const glass = document.createElement("div");
  glass.className = "lens-glass";
  lens.append(glass);
  const zoom = Number(lens.dataset.lens) || 2.4;
  const src = img.dataset.full || img.currentSrc || img.src;
  glass.style.backgroundImage = `url("${src}")`;
  const move = (x, y) => {
    const r = lens.getBoundingClientRect();
    const px = x - r.left;
    const py = y - r.top;
    glass.style.left = `${px}px`;
    glass.style.top = `${py}px`;
    glass.style.backgroundSize = `${r.width * zoom}px ${r.height * zoom}px`;
    glass.style.backgroundPosition = `${-(px * zoom - 110)}px ${-(py * zoom - 110)}px`;
  };
  lens.addEventListener("pointerenter", (e) => { lens.classList.add("is-on"); move(e.clientX, e.clientY); });
  lens.addEventListener("pointermove", (e) => move(e.clientX, e.clientY));
  lens.addEventListener("pointerleave", () => lens.classList.remove("is-on"));
  lens.addEventListener("pointerdown", (e) => { if (e.pointerType !== "mouse") { lens.classList.toggle("is-on"); move(e.clientX, e.clientY); } });
});

/* ── Galería: filtros, Direction Aware Hover y Morphing Dialog ───────── */
(() => {
  const grid = $(".ggrid");
  if (!grid) return;
  const items = $$(".gitem", grid);
  const count = $(".gcount");
  const filters = $(".gfilters");
  let visible = items.slice();

  /* Filtros con reordenación animada (técnica FLIP) */
  if (filters) {
    const ab = animatedBackground(filters, { follow: "active", activeSel: "[aria-pressed=true]" });
    $$("button", filters).forEach((b) => b.addEventListener("click", () => {
      const cat = b.dataset.filter;
      $$("button", filters).forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
      ab.refresh();
      const first = new Map(items.map((it) => [it, it.getBoundingClientRect()]));
      items.forEach((it) => it.classList.toggle("is-hidden", cat !== "all" && it.dataset.cat !== cat));
      visible = items.filter((it) => !it.classList.contains("is-hidden"));
      if (count) count.textContent = T.photos(visible.length);
      if (REDUCED) return;
      visible.forEach((it, k) => {
        const a = first.get(it);
        const z = it.getBoundingClientRect();
        if (a.width === 0) {
          it.animate([{ opacity: 0, transform: "scale(.92)" }, { opacity: 1, transform: "none" }], { duration: 600, delay: k * 30, easing: "cubic-bezier(.16,1,.3,1)", fill: "backwards" });
          return;
        }
        const dx = a.left - z.left;
        const dy = a.top - z.top;
        const sx = a.width / z.width;
        const sy = a.height / z.height;
        it.animate([{ transform: `translate(${dx}px,${dy}px) scale(${sx},${sy})`, transformOrigin: "top left" }, { transform: "none", transformOrigin: "top left" }], { duration: 650, easing: "cubic-bezier(.16,1,.3,1)" });
      });
    }));
  }

  /* Direction Aware Hover */
  if (FINE) items.forEach((it) => {
    const dir = (e) => {
      const r = it.getBoundingClientRect();
      const x = (e.clientX - r.left - r.width / 2) / (r.width / 2);
      const y = (e.clientY - r.top - r.height / 2) / (r.height / 2);
      return Math.abs(x) > Math.abs(y) ? (x > 0 ? "right" : "left") : (y > 0 ? "bottom" : "top");
    };
    it.addEventListener("pointerenter", (e) => {
      it.classList.remove("is-hover");
      it.dataset.dir = dir(e);
      requestAnimationFrame(() => requestAnimationFrame(() => it.classList.add("is-hover")));
    });
    it.addEventListener("pointerleave", (e) => { it.dataset.dir = dir(e); it.classList.remove("is-hover"); });
  });

  /* Morphing Dialog: la miniatura se transforma en la foto ampliada */
  const md = $(".md");
  const stage = $(".md-stage", md);
  const big = $(".md-img", md);
  const cap = $(".md-cap", md);
  const thumbs = $(".md-thumbs", md);
  let cur = 0;
  let opener = null;
  thumbs.innerHTML = items.map((it, i) => `<button type="button" data-i="${i}" aria-label="${T.see}: ${$("img", it).alt}"><img src="${$("img", it).currentSrc || $("img", it).src}" alt=""></button>`).join("");
  const thumbBtns = $$("button", thumbs);
  const setThumbs = () => {
    thumbBtns.forEach((b, i) => { b.hidden = items[i].classList.contains("is-hidden"); b.setAttribute("aria-current", String(i === cur)); });
    thumbBtns[cur].scrollIntoView({ block: "nearest", inline: "center", behavior: REDUCED ? "auto" : "smooth" });
  };
  const load = (i) => {
    cur = i;
    const it = items[i];
    big.src = it.dataset.full;
    big.alt = $("img", it).alt;
    cap.textContent = `${$(".dah b", it).textContent} · ${visible.indexOf(it) + 1} ${T.of} ${visible.length}`;
    setThumbs();
    big.classList.remove("is-zoomed");
    big.style.transform = "";
  };
  const flip = (fromRect, toEl, reverse = false) => {
    const to = toEl.getBoundingClientRect();
    const t = `translate(${fromRect.left - to.left}px,${fromRect.top - to.top}px) scale(${fromRect.width / to.width},${fromRect.height / to.height})`;
    const frames = [{ transform: t, borderRadius: "18px" }, { transform: "none", borderRadius: "18px" }];
    return toEl.animate(reverse ? frames.reverse() : frames, { duration: REDUCED ? 1 : 620, easing: "cubic-bezier(.16,1,.3,1)" }).finished;
  };
  const open = async (i) => {
    opener = items[i];
    load(i);
    md.classList.add("is-open");
    document.body.style.overflow = "hidden";
    if (!big.complete) await big.decode().catch(() => {});
    requestAnimationFrame(() => md.classList.add("is-shown"));
    await flip($("img", opener).getBoundingClientRect(), big);
    $(".md-close", md).focus();
  };
  const close = async () => {
    md.classList.remove("is-shown");
    const target = items[cur];
    if (!target.classList.contains("is-hidden")) {
      const r = $("img", target).getBoundingClientRect();
      if (r.top < innerHeight && r.bottom > 0) await flip(r, big, true).catch(() => {});
    }
    md.classList.remove("is-open");
    document.body.style.overflow = "";
    $("button", target)?.focus();
  };
  const step = (d) => {
    const k = visible.indexOf(items[cur]);
    const n = visible[(k + d + visible.length) % visible.length];
    load(items.indexOf(n));
    if (!REDUCED) big.animate([{ opacity: 0, transform: `translateX(${d * 40}px)` }, { opacity: 1, transform: "none" }], { duration: 450, easing: "cubic-bezier(.16,1,.3,1)" });
  };
  items.forEach((it, i) => $("button", it).addEventListener("click", () => open(i)));
  thumbBtns.forEach((b, i) => b.addEventListener("click", () => load(i)));
  $(".md-close", md).addEventListener("click", close);
  $(".md-prev", md).addEventListener("click", () => step(-1));
  $(".md-next", md).addEventListener("click", () => step(1));
  $(".md-back", md).addEventListener("click", close);
  stage.addEventListener("click", (e) => { if (e.target === stage) close(); });
  md.addEventListener("keydown", (e) => {
    if (e.key === "Escape") close();
    if (e.key === "ArrowRight") step(1);
    if (e.key === "ArrowLeft") step(-1);
    if (e.key === "Tab") {
      const f = $$("button:not([hidden])", md);
      if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f.at(-1).focus(); }
      else if (!e.shiftKey && document.activeElement === f.at(-1)) { e.preventDefault(); f[0].focus(); }
    }
  });
  /* Zoom en la foto ampliada (clic) con desplazamiento siguiendo el puntero */
  big.addEventListener("click", (e) => {
    const z = !big.classList.contains("is-zoomed");
    big.classList.toggle("is-zoomed", z);
    if (!z) { big.style.transform = ""; return; }
    const r = big.getBoundingClientRect();
    big.style.transformOrigin = `${((e.clientX - r.left) / r.width) * 100}% ${((e.clientY - r.top) / r.height) * 100}%`;
    big.style.transform = "scale(2.2)";
  });
  big.addEventListener("pointermove", (e) => {
    if (!big.classList.contains("is-zoomed") || e.pointerType !== "mouse") return;
    const r = big.parentElement.getBoundingClientRect();
    big.style.transformOrigin = `${((e.clientX - r.left) / r.width) * 100}% ${((e.clientY - r.top) / r.height) * 100}%`;
  });
  big.style.transition = "transform .45s cubic-bezier(.16,1,.3,1)";
  let tx = null;
  md.addEventListener("touchstart", (e) => { tx = e.touches[0].clientX; }, { passive: true });
  md.addEventListener("touchend", (e) => {
    if (tx === null || big.classList.contains("is-zoomed")) return;
    const dx = e.changedTouches[0].clientX - tx;
    if (Math.abs(dx) > 50) step(dx < 0 ? 1 : -1);
    tx = null;
  });
  /* Abrir directamente una foto desde un enlace: galeria.html#foto-cocina */
  const fromHash = (delay) => {
    const pre = items.findIndex((it) => `#${it.id}` === location.hash);
    if (pre >= 0 && !md.classList.contains("is-open")) setTimeout(() => open(pre), delay);
  };
  fromHash(400);
  addEventListener("hashchange", () => fromHash(0));
})();

/* ── Tracing Beam (Aceternity UI) ────────────────────────────────────── */
(() => {
  const tb = $(".tb");
  if (!tb) return;
  const secs = $$(".tb-sec", tb);
  addScrollTask((vh) => {
    const r = tb.getBoundingClientRect();
    tb.style.setProperty("--tb", clamp((vh * 0.6 - r.top) / r.height).toFixed(4));
    secs.forEach((s) => s.classList.toggle("is-active", s.getBoundingClientRect().top < vh * 0.6));
  });
})();

/* ── Card Spotlight (Aceternity UI) ──────────────────────────────────── */
if (FINE) $$(".place").forEach((c) => c.addEventListener("pointermove", (e) => {
  const r = c.getBoundingClientRect();
  c.style.setProperty("--mx", `${e.clientX - r.left}px`);
  c.style.setProperty("--my", `${e.clientY - r.top}px`);
}));

/* ── Timeline (Aceternity UI) ────────────────────────────────────────── */
$$(".tl").forEach((tl) => {
  const items = $$(".tl-item", tl);
  addScrollTask((vh) => {
    const r = tl.getBoundingClientRect();
    tl.style.setProperty("--tl", clamp((vh * 0.55 - r.top) / (r.height - 72)).toFixed(4));
    items.forEach((it) => it.classList.toggle("is-active", it.getBoundingClientRect().top < vh * 0.55));
  });
});

/* ── Preguntas: buscador ─────────────────────────────────────────────── */
(() => {
  const input = $("#faq-q");
  if (!input) return;
  const empty = $(".faq-empty");
  const norm = (s) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  input.addEventListener("input", () => {
    const q = norm(input.value.trim());
    let shown = 0;
    $$(".faq-group").forEach((g) => {
      let n = 0;
      $$("details", g).forEach((d) => {
        const ok = !q || norm(d.textContent).includes(q);
        d.hidden = !ok;
        if (ok) n++;
        if (q && ok) d.open = true;
      });
      g.hidden = n === 0;
      shown += n;
    });
    empty.hidden = shown > 0;
  });
})();

/* ── Contacto y formularios: WhatsApp o email con el mensaje preparado ─ */
function deliver(text, subject) {
  if (CONFIG.whatsapp) { open(`https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(text)}`, "_blank", "noopener"); return true; }
  if (CONFIG.email) { location.href = `mailto:${CONFIG.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(text)}`; return true; }
  return false;
}
function setError(input, msg) {
  const err = input.closest(".f-field, .f-check")?.querySelector(".f-err");
  input.setAttribute("aria-invalid", String(Boolean(msg)));
  if (!err) return;
  err.id ||= `${input.name}-err`;
  err.textContent = msg || "";
  err.hidden = !msg;
  msg ? input.setAttribute("aria-describedby", err.id) : input.removeAttribute("aria-describedby");
}
function okMessage(el, text) {
  el.innerHTML = `<span class="f-ok"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".35"/><path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" pathLength="1" style="stroke-dasharray:1;stroke-dashoffset:1;animation:draw .6s .1s var(--ease-out) forwards"/></svg>${text}</span>`;
}
document.head.insertAdjacentHTML("beforeend", "<style>@keyframes draw{to{stroke-dashoffset:0}}</style>");
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

$$("form[data-form]").forEach((form) => {
  const kind = form.dataset.form;
  const status = $(".f-status", form);
  const F = (n) => form.elements.namedItem(n);
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (F("website")?.value) return; // honeypot
    const last = Number(sessionStorage.getItem("vm:last-send") || 0);
    if (Date.now() - last < 20000) { status.textContent = T.wait; return; }
    const checks = [];
    if (F("name")) checks.push([F("name"), F("name").value.trim().length >= 2 ? "" : T.name]);
    if (F("email")) checks.push([F("email"), EMAIL_RE.test(F("email").value.trim()) ? "" : T.email]);
    if (F("message")) checks.push([F("message"), F("message").value.trim().length >= 10 ? "" : T.msg]);
    if (F("consent")) checks.push([F("consent"), F("consent").checked ? "" : T.consent]);
    checks.forEach(([el, m]) => setError(el, m));
    const bad = checks.find(([, m]) => m);
    if (bad) { bad[0].focus(); return; }
    const f = { name: F("name").value.trim(), message: F("message").value.trim(), email: F("email")?.value.trim() || "", stay: F("stay")?.value || "-", rating: F("rating")?.value || "" };
    const text = kind === "review" ? T.reviewMsg(f) : T.contactMsg(f);
    if (!deliver(text, kind === "review" ? T.subjReview : T.subjContact)) {
      status.textContent = CONFIG.pending ? T.pendingChannel : T.noChannel;
      return;
    }
    sessionStorage.setItem("vm:last-send", String(Date.now()));
    okMessage(status, T.sent);
  });
});

/* ── Motor de reserva (frontend) ─────────────────────────────────────── */
(() => {
  const root = $("#booking");
  if (!root) return;
  const pad = (n) => String(n).padStart(2, "0");
  const iso = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  const parse = (s) => { const [y, m, d] = s.split("-").map(Number); return new Date(y, m - 1, d); };
  const addDays = (d, n) => { const r = new Date(d); r.setDate(r.getDate() + n); return r; };
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const cap = (s) => s.charAt(0).toUpperCase() + s.slice(1);
  const fmtMonth = new Intl.DateTimeFormat(LOCALE, { month: "long", year: "numeric" });
  const fmtDay = new Intl.DateTimeFormat(LOCALE, { weekday: "long", day: "numeric", month: "long", year: "numeric" });
  const fmtShort = new Intl.DateTimeFormat(LOCALE, { day: "numeric", month: "short" });
  const fmtLong = new Intl.DateTimeFormat(LOCALE, { day: "numeric", month: "long", year: "numeric" });
  const blocked = new Set(CONFIG.blockedDates || []); // vendrá de Supabase/iCal en la fase de backend
  const maxGuests = CONFIG.maxGuests || null;

  const state = { view: new Date(today.getFullYear(), today.getMonth(), 1), start: null, end: null, adults: 2, children: 0, step: 0, focus: iso(today) };
  const months = $(".cal-months", root);
  const nightsEl = $("#sum-nights");
  const datesEl = $("#sum-dates");
  const guestsEl = $("#sum-guests");
  const summary = $(".summary", root);
  const stepsNav = $(".steps", root);
  const panels = $$(".panel", root);
  const stepBtns = $$("button", stepsNav);
  const ab = animatedBackground(stepsNav, { follow: "active", activeSel: "[aria-current=step]" });

  const nights = () => (state.start && state.end ? Math.round((parse(state.end) - parse(state.start)) / 86400000) : 0);
  const rangeBlocked = (a, b) => { for (let d = parse(a); d < parse(b); d = addDays(d, 1)) if (blocked.has(iso(d))) return true; return false; };

  function renderCal() {
    months.innerHTML = "";
    let q = 0;
    for (let k = 0; k < 2; k++) {
      const first = new Date(state.view.getFullYear(), state.view.getMonth() + k, 1);
      const off = (first.getDay() + 6) % 7;
      const days = new Date(first.getFullYear(), first.getMonth() + 1, 0).getDate();
      let html = T.wd.map((d) => `<span class="cal-wd" aria-hidden="true">${d}</span>`).join("");
      for (let i = 0; i < off; i++) html += "<span></span>";
      for (let d = 1; d <= days; d++) {
        const date = new Date(first.getFullYear(), first.getMonth(), d);
        const s = iso(date);
        const dis = date < today || blocked.has(s);
        const st = s === state.start;
        const en = s === state.end;
        const inR = state.start && state.end && s > state.start && s < state.end;
        if (inR) q++;
        const lab = `${fmtDay.format(date)}${st ? T.arrival : ""}${en ? T.departure : ""}${blocked.has(s) ? T.unavailable : ""}`;
        html += `<button type="button" class="day${st ? " is-start" : ""}${en ? " is-end" : ""}${inR ? " in-range" : ""}" style="--q:${inR ? q : 0}" data-iso="${s}" tabindex="${s === state.focus ? 0 : -1}" aria-label="${lab}" aria-pressed="${Boolean(st || en || inR)}" ${dis ? "disabled" : ""}><span class="fill" aria-hidden="true"></span><span>${d}</span></button>`;
      }
      months.insertAdjacentHTML("beforeend", `<div class="cal-month${k === 1 ? " m2" : ""}"><h3 class="cal-title">${cap(fmtMonth.format(first))}</h3><div class="cal-grid" role="group" aria-label="${fmtMonth.format(first)}">${html}</div></div>`);
    }
    $(".cal-prev", root).disabled = state.view <= new Date(today.getFullYear(), today.getMonth(), 1);
  }

  function renderSummary() {
    const n = nights();
    SN.set(nightsEl, n);
    $("#sum-nights-label").textContent = T.night(n);
    datesEl.textContent = state.start ? `${fmtShort.format(parse(state.start))} – ${state.end ? fmtShort.format(parse(state.end)) : "…"}` : T.chooseDates;
    guestsEl.textContent = T.guests(state.adults, state.children);
    summary.classList.toggle("is-ready", Boolean(state.start && state.end));
    $("#cal-status").textContent = !state.start ? T.pickStart : !state.end ? T.pickEnd : T.selected(n);
    $$("[data-next]", root)[0].disabled = !(state.start && state.end);
  }

  function goStep(i) {
    if (i > 0 && !(state.start && state.end)) return;
    state.step = i;
    panels.forEach((p, k) => {
      p.hidden = k !== i;
      if (k === i && !REDUCED) { p.classList.remove("is-entering"); p.offsetWidth; p.classList.add("is-entering"); }
    });
    stepBtns.forEach((b, k) => {
      if (k === i) b.setAttribute("aria-current", "step");
      else b.removeAttribute("aria-current");
      b.classList.toggle("done", k < i);
      b.disabled = k > 0 && !(state.start && state.end);
    });
    ab.refresh();
    if (i === 3) buildReview();
    const top = root.getBoundingClientRect().top + scrollY - 70;
    if (scrollY > top) scrollTo({ top, behavior: REDUCED ? "auto" : "smooth" });
  }

  months.addEventListener("click", (e) => {
    const b = e.target.closest(".day");
    if (!b || b.disabled) return;
    const s = b.dataset.iso;
    state.focus = s;
    if (!state.start || state.end || s <= state.start || rangeBlocked(state.start, s)) { state.start = s; state.end = null; }
    else state.end = s;
    renderCal();
    renderSummary();
    $(`[data-iso="${s}"]`, months)?.focus();
  });
  months.addEventListener("keydown", (e) => {
    const delta = { ArrowLeft: -1, ArrowRight: 1, ArrowUp: -7, ArrowDown: 7 }[e.key];
    const b = e.target.closest(".day");
    if (delta === undefined || !b) return;
    e.preventDefault();
    const next = addDays(parse(b.dataset.iso), delta);
    if (next < today) return;
    state.focus = iso(next);
    const lastShown = new Date(state.view.getFullYear(), state.view.getMonth() + 2, 1);
    if (next < state.view) state.view = new Date(next.getFullYear(), next.getMonth(), 1);
    if (next >= lastShown) state.view = new Date(next.getFullYear(), next.getMonth() - 1, 1);
    renderCal();
    $(`[data-iso="${state.focus}"]`, months)?.focus();
  });
  $(".cal-prev", root).addEventListener("click", () => { state.view = new Date(state.view.getFullYear(), state.view.getMonth() - 1, 1); renderCal(); });
  $(".cal-next", root).addEventListener("click", () => { state.view = new Date(state.view.getFullYear(), state.view.getMonth() + 1, 1); renderCal(); });

  // Huéspedes: el máximo sale de la capacidad real cuando se configure
  $$("[data-count]", root).forEach((row) => {
    const key = row.dataset.count;
    const out = $("output", row);
    const [minus, plus] = $$("button", row);
    const sync = () => {
      out.value = state[key];
      const total = state.adults + state.children;
      minus.disabled = state[key] <= (key === "adults" ? 1 : 0);
      plus.disabled = maxGuests ? total >= maxGuests : false;
      renderSummary();
    };
    minus.addEventListener("click", () => { state[key]--; sync(); });
    plus.addEventListener("click", () => { state[key]++; sync(); });
    sync();
  });

  stepBtns.forEach((b, i) => b.addEventListener("click", () => goStep(i)));
  $$("[data-next]", root).forEach((b) => b.addEventListener("click", () => {
    if (state.step === 2) {
      const f = $("#guest-form");
      const F = (n) => f.elements.namedItem(n);
      const checks = [
        [F("name"), F("name").value.trim().length >= 2 ? "" : T.fullName],
        [F("email"), EMAIL_RE.test(F("email").value.trim()) ? "" : T.email],
        [F("phone"), F("phone").value.replace(/\D/g, "").length >= 9 ? "" : T.phone],
      ];
      checks.forEach(([el, m]) => setError(el, m));
      const bad = checks.find(([, m]) => m);
      if (bad) { bad[0].focus(); return; }
    }
    goStep(state.step + 1);
  }));
  $$("[data-back]", root).forEach((b) => b.addEventListener("click", () => goStep(state.step - 1)));

  function buildReview() {
    const f = $("#guest-form");
    const F = (n) => f.elements.namedItem(n).value.trim();
    const n = nights();
    $("#review-list").innerHTML = `
      <li><span>${T.rDates}</span><span>${fmtLong.format(parse(state.start))} – ${fmtLong.format(parse(state.end))}</span></li>
      <li><span>${T.rNights}</span><span>${n}</span></li>
      <li><span>${T.rGuests}</span><span>${guestsEl.textContent}</span></li>
      <li><span>${T.rName}</span><span>${esc(F("name"))}</span></li>
      <li><span>${T.rContact}</span><span>${esc(F("email"))} · ${esc(F("phone"))}</span></li>`;
  }

  $("#confirm").addEventListener("click", () => {
    const terms = $("#terms");
    setError(terms, terms.checked ? "" : T.terms);
    if (!terms.checked) { terms.focus(); return; }
    const f = $("#guest-form");
    const F = (n) => f.elements.namedItem(n).value.trim();
    const n = nights();
    const text = T.bookMsg({ from: fmtLong.format(parse(state.start)), to: fmtLong.format(parse(state.end)), n, guests: guestsEl.textContent, notes: F("notes"), name: F("name"), email: F("email"), phone: F("phone") }).filter(Boolean).join("\n");
    const out = $("#confirm-status");
    if (!deliver(text, T.subjBooking)) { out.textContent = CONFIG.pending ? T.pendingChannel : T.noChannel; return; }
    okMessage(out, T.sentBooking);
  });

  // Fechas precargadas desde otra página: reservar.html?llegada=2026-11-06&salida=2026-11-09
  const params = new URLSearchParams(location.search);
  const a = params.get("llegada");
  const s = params.get("salida");
  if (a && s && a < s && parse(a) >= today && !rangeBlocked(a, s)) { state.start = a; state.end = s; state.view = new Date(parse(a).getFullYear(), parse(a).getMonth(), 1); }

  renderCal();
  renderSummary();
  goStep(0);
})();

/* ── Mapa: se carga solo cuando el visitante lo pide (rendimiento y privacidad) ─ */
$$(".map-facade").forEach((box) => {
  $(".map-load", box)?.addEventListener("click", () => {
    const f = document.createElement("iframe");
    f.src = box.dataset.src.replace(/&amp;/g, "&");
    f.title = box.dataset.title || "Mapa";
    f.loading = "lazy";
    f.referrerPolicy = "no-referrer-when-downgrade";
    box.replaceChildren(f);
    box.classList.add("is-loaded");
    f.focus();
  });
});

/* ── Pie: año ────────────────────────────────────────────────────────── */
$$("[data-year]").forEach((el) => { el.textContent = new Date().getFullYear(); });

/* ── Hero: tarjetas flotantes con parallax de ratón y scroll ─────────── */
(() => {
  const float = $(".cs-float");
  if (!float || REDUCED) return;
  const cards = $$(".fl", float);
  const hero = $(".hero");
  if (FINE) hero.addEventListener("pointermove", (e) => {
    const mx = (e.clientX / innerWidth - 0.5) * 2;
    const my = (e.clientY / innerHeight - 0.5) * 2;
    cards.forEach((c) => { c.style.setProperty("--mx", mx.toFixed(3)); c.style.setProperty("--my", my.toFixed(3)); });
  });
  addScrollTask((vh) => {
    const p = clamp(scrollY / vh);
    cards.forEach((c) => c.style.setProperty("--sy", p.toFixed(3)));
  });
})();

/* ── Plano interactivo ───────────────────────────────────────────────── */
(() => {
  const root = $(".plan");
  const src = $("#plan-data");
  if (!root || !src) return;
  const { order, rooms } = JSON.parse(src.textContent);
  const svg = $(".plan-svg", root);
  const zones = $$("[data-zone]", svg);
  const tabsEl = $(".plan-tabs", root);
  const tabs = $$("button", tabsEl);
  const ab = animatedBackground(tabsEl, { follow: "active", activeSel: '[aria-pressed="true"]' });
  const imgs = $$(".plan-photo img", root);
  const count = $(".plan-count", root);
  const info = $(".plan-info", root);
  const playBtn = $(".plan-play", root);
  const bar = $(".plan-bar i", root);
  const DUR = 5200;
  let cur = order[0];
  let paused = REDUCED;
  let visible = false;
  let timer = null;
  let front = 0;

  const render = (key) => {
    const r = rooms[key];
    $(".plan-k", info).textContent = r.k;
    $(".plan-name", info).textContent = r.name;
    $(".plan-desc", info).textContent = r.desc;
    $(".plan-list", info).innerHTML = r.items.map((x) => `<li>${x}</li>`).join("");
    $(".plan-link", info).href = r.href;
  };
  const select = (key, { user = false } = {}) => {
    if (user) stop(true);
    const changed = key !== cur;
    cur = key;
    svg.classList.add("has-sel");
    zones.forEach((z) => z.classList.toggle("is-sel", z.dataset.zone === key));
    $$(".furn, .lbl", svg).forEach((g) => g.classList.toggle("on", g.dataset.of === key));
    tabs.forEach((t) => t.setAttribute("aria-pressed", String(t.dataset.room === key)));
    ab.refresh();
    const t = tabs.find((b) => b.dataset.room === key);
    if (t && user) t.scrollIntoView({ block: "nearest", inline: "center", behavior: REDUCED ? "auto" : "smooth" });
    count.textContent = `${order.indexOf(key) + 1} / ${order.length}`;
    if (!changed) return;
    const r = rooms[key];
    const next = imgs[1 - front];
    next.src = r.img;
    next.alt = r.alt;
    const show = () => { imgs[front].classList.remove("is-on"); imgs[front].alt = ""; next.classList.add("is-on"); front = 1 - front; };
    if (next.complete) requestAnimationFrame(show); else next.onload = show;
    if (REDUCED) { render(key); return; }
    info.classList.add("is-swap");
    setTimeout(() => { render(key); info.classList.remove("is-swap"); }, 260);
  };
  const step = (d, user) => select(order[(order.indexOf(cur) + d + order.length) % order.length], { user });

  /* Recorrido automático con barra de progreso */
  const run = () => {
    clearTimeout(timer);
    bar.classList.remove("run");
    if (paused || !visible) return;
    void bar.offsetWidth;
    bar.style.setProperty("--plan-t", `${DUR}ms`);
    bar.classList.add("run");
    timer = setTimeout(() => { step(1, false); run(); }, DUR);
  };
  function stop(byUser) {
    paused = true;
    clearTimeout(timer);
    bar.classList.remove("run");
    playBtn.setAttribute("aria-pressed", "true");
    playBtn.setAttribute("aria-label", T.resumeTour);
    if (byUser) root.dataset.userStopped = "1";
  }
  playBtn.addEventListener("click", () => {
    if (paused) {
      paused = false;
      playBtn.setAttribute("aria-pressed", "false");
      playBtn.setAttribute("aria-label", T.pauseTour);
      step(1, false);
      run();
    } else stop(true);
  });
  if (REDUCED) stop(false);

  zones.forEach((z) => {
    z.addEventListener("click", () => select(z.dataset.zone, { user: true }));
    z.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); select(z.dataset.zone, { user: true }); }
    });
  });
  tabs.forEach((t) => t.addEventListener("click", () => select(t.dataset.room, { user: true })));
  tabsEl.addEventListener("keydown", (e) => {
    if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
    e.preventDefault();
    step(e.key === "ArrowRight" ? 1 : -1, true);
    tabs.find((b) => b.dataset.room === cur).focus();
  });
  $(".plan-prev", root).addEventListener("click", () => step(-1, true));
  $(".plan-next", root).addEventListener("click", () => step(1, true));

  /* Al entrar en pantalla: dibuja muros y arranca el recorrido */
  onceInView([svg], () => {
    svg.classList.add("is-drawn");
    setTimeout(() => select(cur), REDUCED ? 0 : 1500);
  }, { threshold: 0.35 });
  if (hasIO) new IntersectionObserver(([e]) => { visible = e.isIntersecting; run(); }, { threshold: 0.4 }).observe(root);
  addEventListener("resize", () => ab.refresh());
})();
