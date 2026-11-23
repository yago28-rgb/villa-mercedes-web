#!/usr/bin/env python3
"""
Villa Mercedes · generador de la web estática (ES, EN, FR).

Uso:
    python3 build.py               versión para publicar
    python3 build.py --pendientes  igual, pero muestra los [PENDIENTE] para revisar en local

Edita CONFIG y vuelve a ejecutarlo. Los textos de cada página están en contenido.py.
Genera site/ con todas las páginas, robots.txt, sitemap.xml y .htaccess.
"""
import hashlib
import html
import json
import os
import re
import sys
from pathlib import Path

# ── Configuración: rellena antes de publicar ──────────────────────────────
CONFIG = {
    "SITE_URL": "https://www.TU-DOMINIO.es",  # dominio definitivo, con https y sin barra final
    "WHATSAPP": "",              # número internacional sin "+", p. ej. "34600000000"
    "TELEFONO": "",              # mismo número en formato visible, p. ej. "+34 600 000 000"
    "EMAIL": "",                 # correo que recibe consultas y reservas
    "REGISTRO_TURISTICO": "",    # n.º de inscripción en el Registro General de Empresas Turísticas de Cantabria
    "NRUA": "",                  # Número de Registro Único de Arrendamientos
    "MAX_GUESTS": None,          # capacidad máxima real (número)
    "CHECKIN": "",               # hora de entrada en formato 24 h, p. ej. "16:00"
    "CHECKOUT": "",              # hora de salida, p. ej. "11:00"
    "LAT": "",                   # latitud con 5 decimales (Google Maps > clic derecho sobre la casa)
    "LNG": "",                   # longitud con 5 decimales
    "SAME_AS": [],               # perfiles oficiales: Instagram, Facebook, anuncio de Booking…
}
SHOW_PENDING = "--pendientes" in sys.argv
if os.environ.get("VM_SITE_URL"):  # solo para pruebas locales
    CONFIG["SITE_URL"] = os.environ["VM_SITE_URL"]

ROOT = Path(__file__).parent
OUT = ROOT / "site"
esc = html.escape
LANGS = ["es", "en", "fr"]
LOCALE = {"es": "es_ES", "en": "en_GB", "fr": "fr_FR"}
PREFIX = {"es": "/", "en": "/en/", "fr": "/fr/"}
LANG_NAME = {"es": "Español", "en": "English", "fr": "Français"}

# Rutas por página e idioma (URL limpias: cada página es una carpeta con index.html)
ROUTES = {
    "home": {"es": "", "en": "", "fr": ""},
    "casa": {"es": "la-casa/", "en": "the-house/", "fr": "la-maison/"},
    "galeria": {"es": "galeria/", "en": "gallery/", "fr": "galerie/"},
    "guia": {"es": "que-ver-en-santona/", "en": "things-to-do-in-santona/", "fr": "que-faire-a-santona/"},
    "reservar": {"es": "reservar/", "en": "book/", "fr": "reserver/"},
    "opiniones": {"es": "opiniones/", "en": "reviews/", "fr": "avis/"},
    "faq": {"es": "preguntas-frecuentes/", "en": "faq/", "fr": "questions-frequentes/"},
    "contacto": {"es": "contacto/", "en": "contact/", "fr": "contact/"},
    "condiciones": {"es": "condiciones-de-reserva/", "en": "booking-terms/", "fr": "conditions-de-reservation/"},
    "aviso": {"es": "aviso-legal/", "en": "legal-notice/", "fr": "mentions-legales/"},
    "privacidad": {"es": "privacidad/", "en": "privacy/", "fr": "confidentialite/"},
    "cookies": {"es": "cookies/", "en": "cookies/", "fr": "cookies/"},
}

# Idioma activo mientras se genera cada página
_L = {"lang": "es"}


def L():
    return _L["lang"]


def X(es, en, fr):
    """Texto en el idioma activo."""
    return {"es": es, "en": en, "fr": fr}[L()]


def U(key, lang=None, anchor=""):
    """URL relativa a la raíz de una página."""
    lang = lang or L()
    return PREFIX[lang] + ROUTES[key][lang] + (f"#{anchor}" if anchor else "")


def ABS(path):
    return CONFIG["SITE_URL"].rstrip("/") + path


# ── Datos pendientes ──────────────────────────────────────────────────────
# En la versión publicable no sale ningún [PENDIENTE]: los bloques que lo contienen
# se omiten. Con --pendientes se ven resaltados para revisarlos.
PEND = "\x00PEND\x00"
_pending_log = {}


_all_pending = set()


def P(text):
    _all_pending.add(text)
    return f"{PEND}{text}{PEND}"


def has_p(s):
    return PEND in s


def keep(items):
    """Filtra de una lista los elementos con datos pendientes (solo en la versión publicable)."""
    return list(items) if SHOW_PENDING else [i for i in items if not has_p(json.dumps(i, ensure_ascii=False) if not isinstance(i, str) else i)]


def opt(s):
    """Devuelve el bloque solo si no tiene pendientes (o si se están mostrando)."""
    return s if (SHOW_PENDING or not has_p(s)) else ""


def finish_pending(doc, page):
    found = re.findall(re.escape(PEND) + r"(.*?)" + re.escape(PEND), doc, flags=re.S)
    if found:
        _pending_log.setdefault(page, set()).update(found)
    if SHOW_PENDING:
        return re.sub(re.escape(PEND) + r"(.*?)" + re.escape(PEND), lambda m: f'<span class="pend">[PENDIENTE: {m.group(1)}]</span>', doc, flags=re.S)
    return re.sub(re.escape(PEND) + r".*?" + re.escape(PEND), "", doc, flags=re.S)


# ── Fotos ─────────────────────────────────────────────────────────────────
W = {
    "jardin-comedor-exterior": (2048, 1536), "dormitorio-principal": (2048, 1536),
    "dormitorio-dos-camas": (1754, 1536), "salon-comedor": (2048, 1536),
    "salon-salida-jardin": (2048, 1504), "bano-banera": (2048, 1536), "cocina": (1932, 1536),
    "bano-ducha": (2048, 1536), "fachada-urbanizacion": (1870, 1536), "jardin-zona-lounge": (2048, 1536),
    "mesa-exterior-detalle": (2048, 1536), "jardin-vista-general": (2048, 1536),
}
ALT = {
    "jardin-comedor-exterior": ("Jardín de Villa Mercedes en Santoña con mesa de comedor para seis junto al muro de piedra",
                                "Garden at Villa Mercedes in Santoña with a dining table for six by the stone wall",
                                "Jardin de Villa Mercedes à Santoña avec une table pour six près du mur en pierre"),
    "dormitorio-principal": ("Dormitorio principal con cama de matrimonio, cojines verdes y toallas",
                             "Main bedroom with a double bed, green cushions and towels",
                             "Chambre principale avec lit double, coussins verts et serviettes"),
    "dormitorio-dos-camas": ("Dormitorio con dos camas individuales y ventana hacia la ladera",
                             "Twin bedroom with two single beds and a window facing the hillside",
                             "Chambre avec deux lits simples et fenêtre donnant sur la colline"),
    "salon-comedor": ("Salón con sofá, sillones, mesa baja y comedor al fondo",
                      "Living room with sofa, armchairs, coffee table and dining area",
                      "Salon avec canapé, fauteuils, table basse et coin repas"),
    "salon-salida-jardin": ("Salón con puerta acristalada que da al jardín",
                            "Living room with a glazed door opening onto the garden",
                            "Salon avec porte vitrée donnant sur le jardin"),
    "bano-banera": ("Baño con bañera y mampara, lavabo con mueble de madera, inodoro y bidé",
                    "Bathroom with bathtub and screen, wooden vanity unit, toilet and bidet",
                    "Salle de bains avec baignoire et pare-bain, meuble vasque en bois, WC et bidet"),
    "cocina": ("Cocina equipada con horno, microondas, lavadora, nevera y puerta a la terraza",
               "Fitted kitchen with oven, microwave, washing machine, fridge and door to the terrace",
               "Cuisine équipée avec four, micro-ondes, lave-linge, réfrigérateur et porte sur la terrasse"),
    "bano-ducha": ("Baño con plato de ducha y mampara, lavabo e inodoro",
                   "Shower room with shower tray and screen, washbasin and toilet",
                   "Salle d'eau avec douche et paroi, lavabo et WC"),
    "fachada-urbanizacion": ("Fachada de la urbanización Villa Mercedes en Santoña, edificio de ladrillo con tejado de teja",
                             "Villa Mercedes residential complex in Santoña, a brick building with a tiled roof",
                             "Résidence Villa Mercedes à Santoña, bâtiment en brique avec toit en tuiles"),
    "jardin-zona-lounge": ("Zona de descanso del jardín con sofás de ratán y mesa baja",
                           "Garden lounge area with rattan sofas and a low table",
                           "Coin détente du jardin avec canapés en rotin et table basse"),
    "mesa-exterior-detalle": ("Mesa exterior puesta junto al muro de piedra con musgo",
                              "Outdoor table laid beside the moss-covered stone wall",
                              "Table extérieure dressée près du mur en pierre couvert de mousse"),
    "jardin-vista-general": ("Vista general del jardín con sofás, comedor exterior y muro de piedra",
                             "View of the garden with sofas, outdoor dining area and stone wall",
                             "Vue d'ensemble du jardin avec canapés, coin repas extérieur et mur en pierre"),
}
CAP = {
    "jardin-comedor-exterior": ("Comedor exterior", "Outdoor dining", "Repas en extérieur"),
    "dormitorio-principal": ("Dormitorio principal", "Main bedroom", "Chambre principale"),
    "dormitorio-dos-camas": ("Dormitorio con dos camas", "Twin bedroom", "Chambre à deux lits"),
    "salon-comedor": ("Salón comedor", "Living and dining room", "Salon et salle à manger"),
    "salon-salida-jardin": ("Salón", "Living room", "Salon"),
    "bano-banera": ("Baño con bañera", "Bathroom", "Salle de bains"),
    "cocina": ("Cocina", "Kitchen", "Cuisine"),
    "bano-ducha": ("Baño con ducha", "Shower room", "Salle d'eau"),
    "fachada-urbanizacion": ("La urbanización", "The building", "La résidence"),
    "jardin-zona-lounge": ("Zona de sofás", "Lounge area", "Coin canapés"),
    "mesa-exterior-detalle": ("Mesa exterior", "Outdoor table", "Table extérieure"),
    "jardin-vista-general": ("El jardín", "The garden", "Le jardin"),
}


def alt(n):
    return X(*ALT[n])


def cap(n):
    return X(*CAP[n])


def pic(n, sizes, cls="", lazy=True, high=False, extra=""):
    w, h = W[n]
    big = min(2048, w)
    sets = []
    for fmt in ("avif", "webp"):
        s = ", ".join([f"/img/{n}-640.{fmt} 640w", f"/img/{n}-1200.{fmt} 1200w", f"/img/{n}-2048.{fmt} {big}w"])
        sets.append(f'<source type="image/{fmt}" srcset="{s}" sizes="{sizes}">')
    load = ' loading="lazy"' if lazy else (' fetchpriority="high"' if high else "")
    c = f' class="{cls}"' if cls else ""
    return (f"<picture{c}>" + "".join(sets) +
            f'<img src="/img/{n}-1200.webp" width="1200" height="{round(h * 1200 / w)}" alt="{esc(alt(n))}"{load} decoding="async"{extra}></picture>')


# ── Iconos lineales ───────────────────────────────────────────────────────
ICON = {
    "home": '<path d="M3 11 12 4l9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1v-9Z"/>',
    "wifi": '<path d="M2.5 9a14 14 0 0 1 19 0M5.5 12.5a9.5 9.5 0 0 1 13 0M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.2" r=".9" fill="currentColor"/>',
    "kitchen": '<path d="M4 10h16v2a6 6 0 0 1-6 6h-4a6 6 0 0 1-6-6v-2ZM2 10h2M20 10h2M9 6c0-1 1-1 1-2M13 6c0-1 1-1 1-2"/>',
    "bed": '<path d="M3 18v-7a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v7M3 14h18M3 18v2M21 18v2M7 9V7a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v2"/>',
    "bath": '<path d="M4 12h16v3a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4v-3ZM6 12V6a2 2 0 0 1 4 0M7 19l-1 2M17 19l1 2"/>',
    "sofa": '<path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3M2 13a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v5H2v-5ZM5 18v2M19 18v2"/>',
    "garden": '<path d="M12 21v-9M12 12c0-4 3-7 7-7 0 4-3 7-7 7ZM12 15c0-3-2.5-5.5-6-5.5 0 3.5 2.5 5.5 6 5.5ZM5 21h14"/>',
    "linen": '<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3V4Z"/><path d="M5 8h14M9 12h6"/>',
    "nosmoke": '<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8M7 13h7"/>',
    "car": '<path d="M5 16V11l2-5h10l2 5v5M3 16h18v3H3zM7 19v2M17 19v2"/><circle cx="7.5" cy="13.5" r=".8" fill="currentColor"/><circle cx="16.5" cy="13.5" r=".8" fill="currentColor"/>',
    "lang": '<path d="M4 5h9v7H8l-4 3V5ZM15 9h5v8l-3-2h-4v-3"/>',
    "walk": '<circle cx="13" cy="4.5" r="1.8"/><path d="M10 21l2-6-2-3 1-5 4 3 3 1M12 12l-3 2-2 4"/>',
    "plane": '<path d="M2 16l20-8-6 12-3-5-5-1Z"/>',
    "star": '<path d="m12 3 2.6 5.6 6.1.7-4.5 4.2 1.2 6L12 16.6 6.6 19.5l1.2-6L3.3 9.3l6.1-.7L12 3Z"/>',
    "whatsapp": '<path d="M4 20l1.3-4A8 8 0 1 1 8 18.7L4 20Z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 .8a4 4 0 0 1-2-2l.8-1-1-2L9 9.5Z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "pin": '<path d="M12 21s-7-6.3-7-12a7 7 0 0 1 14 0c0 5.7-7 12-7 12Z"/><circle cx="12" cy="9" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "tag": '<path d="M3 12V4h8l10 10-8 8L3 12Z"/><circle cx="7.5" cy="7.5" r="1.3"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4V5Z"/>',
}


def ic(k, size=24):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[k]}</svg>'


def arrow(d, size=18):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true"><path d="{d}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


PREV = "M15 5l-7 7 7 7"
NEXT = "M9 5l7 7-7 7"

# ── Recursos con huella para caché larga ──────────────────────────────────
def _v(path):
    return hashlib.sha1((OUT / path).read_bytes()).hexdigest()[:10]


ASSET = {}


def asset(path):
    if path not in ASSET:
        ASSET[path] = f"/{path}?v={_v(path)}"
    return ASSET[path]


# ── Cabecera, navegación y pie ────────────────────────────────────────────
def NAV():
    return [("casa", X("La casa", "The house", "La maison")), ("galeria", X("Galería", "Gallery", "Galerie")),
            ("guia", X("Qué ver", "Things to do", "À voir")), ("opiniones", X("Opiniones", "Reviews", "Avis")),
            ("faq", X("Preguntas", "FAQ", "Questions")), ("contacto", X("Contacto", "Contact", "Contact"))]


def lang_switch(key, cls):
    links = "".join(
        f'<a href="{U(key, lg)}" hreflang="{lg}" lang="{lg}"{" aria-current=" + chr(34) + "true" + chr(34) if lg == L() else ""}>'
        f'<abbr title="{LANG_NAME[lg]}">{lg.upper()}</abbr></a>' for lg in LANGS)
    return f'<div class="{cls}" aria-label="{X("Idioma", "Language", "Langue")}" role="group">{links}</div>'


def header(key, local_title, local_links, cta=True):
    links = "".join(f'<a href="{U(k)}"{" aria-current=" + chr(34) + "page" + chr(34) if k == key else ""}>{t}</a>' for k, t in NAV())
    loc = "".join(f'<a href="{h}">{t}</a>' for h, t in local_links)
    book = f'<a href="{U("reservar")}" class="pill pill-sm">{X("Reservar", "Book", "Réserver")}</a>' if cta else ""
    return f"""<a class="skip" href="#contenido">{X("Saltar al contenido", "Skip to content", "Aller au contenu")}</a>
<header>
<nav class="gnav" aria-label="{X("Principal", "Main", "Principale")}">
  <div class="container gnav-in">
    <a href="{U("home")}" class="gnav-logo" aria-label="{X("Villa Mercedes, inicio", "Villa Mercedes, home", "Villa Mercedes, accueil")}">{ic("home", 18)}</a>
    <div class="gnav-links">{links}{lang_switch(key, "gnav-lang")}</div>
    <button type="button" class="gnav-menu" aria-expanded="false" aria-label="{X("Menú", "Menu", "Menu")}"><span></span></button>
  </div>
</nav>
<nav class="lnav" aria-label="{esc(local_title)}">
  <div class="container lnav-in">
    <a href="#contenido" class="lnav-title">{esc(local_title)}</a>
    <div class="lnav-links">{loc}</div>
    {book}
    <span class="scroll-progress" aria-hidden="true"></span>
  </div>
</nav>
</header>"""


def nap_html():
    phone = f'<a href="tel:{CONFIG["TELEFONO"].replace(" ", "")}">{esc(CONFIG["TELEFONO"])}</a>' if CONFIG["TELEFONO"] else P("teléfono")
    mail = f'<a href="mailto:{CONFIG["EMAIL"]}">{esc(CONFIG["EMAIL"])}</a>' if CONFIG["EMAIL"] else P("email")
    return (f'<p class="foot-nap"><b>Villa Mercedes</b> · Barrio Piedrahita, Urbanización Villa Mercedes, 74 · 39740 Santoña, Cantabria, {X("España", "Spain", "Espagne")}'
            + opt(f" · {phone}") + opt(f" · {mail}") + "</p>")


def footer(key, crumbs):
    reg, nrua = CONFIG["REGISTRO_TURISTICO"], CONFIG["NRUA"]
    reg_txt = (X("N.º de inscripción en el Registro General de Empresas Turísticas de Cantabria: ",
                 "Cantabria Tourism Register number: ", "N° d'inscription au registre du tourisme de Cantabrie : ") + (esc(reg) if reg else P("número de registro turístico")))
    nrua_txt = X("Número de Registro Único de Arrendamientos (NRUA): ", "Single Rental Register number (NRUA): ",
                 "Numéro du registre unique des locations (NRUA) : ") + (esc(nrua) if nrua else P("NRUA"))
    crumb_html = "".join(f'<li>{f"<a href={chr(34)}{U(k)}{chr(34)}>{t}</a>" if k else t}</li>' for k, t in crumbs)
    col = lambda title, items: f'<div><h2>{title}</h2><ul>' + "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in items) + "</ul></div>"
    cols = "".join([
        col(X("La casa", "The house", "La maison"), [(U("casa"), X("Estancia por estancia", "Room by room", "Pièce par pièce")), (U("casa", anchor="plano"), X("Plano", "Floor plan", "Plan")),
                                                     (U("casa", anchor="equipamiento"), X("Equipamiento", "Amenities", "Équipements")), (U("galeria"), X("Galería", "Gallery", "Galerie"))]),
        col(X("Santoña", "Santoña", "Santoña"), [(U("guia", anchor="playas"), X("Playas", "Beaches", "Plages")), (U("guia", anchor="faro-del-caballo"), X("Faro del Caballo", "Faro del Caballo", "Phare du Caballo")),
                                                 (U("guia", anchor="bilbao"), X("Bilbao y el Guggenheim", "Bilbao and the Guggenheim", "Bilbao et le Guggenheim")), (U("guia", anchor="como-llegar"), X("Cómo llegar", "Getting here", "Comment venir"))]),
        col(X("Reservas", "Bookings", "Réservations"), [(U("reservar"), X("Reservar", "Book", "Réserver")), (U("condiciones"), X("Condiciones de reserva", "Booking terms", "Conditions de réservation")),
                                                       (U("faq"), X("Preguntas frecuentes", "FAQ", "Questions fréquentes")), (U("opiniones"), X("Opiniones", "Reviews", "Avis"))]),
        col(X("Contacto", "Contact", "Contact"), [(U("contacto"), X("Escríbenos", "Get in touch", "Nous écrire")), (U("contacto", anchor="mapa"), X("Cómo encontrarnos", "Find us", "Nous trouver"))]),
    ])
    return f"""<footer class="foot">
  <div class="container">
    <div class="foot-notes">
      <p>{X("El vídeo de la portada se ha generado con inteligencia artificial a partir de fotografías reales del apartamento. Las fotografías de la web son reales y no se han modificado con IA.",
            "The home page video was generated with artificial intelligence from real photos of the apartment. The photos on this site are real and have not been altered with AI.",
            "La vidéo de la page d'accueil a été générée par intelligence artificielle à partir de photos réelles de l'appartement. Les photos du site sont réelles et n'ont pas été retouchées par IA.")}</p>
      <p>{X("Distancias aproximadas. La puntuación de ubicación procede de las valoraciones de huéspedes en Booking.com.",
            "Distances are approximate. The location score comes from guest ratings on Booking.com.",
            "Distances approximatives. La note d'emplacement provient des évaluations des voyageurs sur Booking.com.")}</p>
      {opt(f"<p>{reg_txt}. {nrua_txt}.</p>")}
      {nap_html()}
    </div>
    <ol class="foot-crumbs" aria-label="{X("Estás aquí", "You are here", "Vous êtes ici")}"><li><a href="{U("home")}" aria-label="{X("Inicio", "Home", "Accueil")}">{ic("home", 14)}</a></li>{crumb_html}</ol>
    <div class="foot-cols">{cols}</div>
    <div class="foot-bottom">
      <p>Copyright © <span data-year>2026</span> Villa Mercedes. {X("Todos los derechos reservados.", "All rights reserved.", "Tous droits réservés.")}</p>
      {lang_switch(key, "foot-lang")}
      <nav class="foot-legal" aria-label="Legal"><a href="{U("aviso")}">{X("Aviso legal", "Legal notice", "Mentions légales")}</a><a href="{U("privacidad")}">{X("Privacidad", "Privacy", "Confidentialité")}</a><a href="{U("cookies")}">Cookies</a><a href="{U("condiciones")}">{X("Condiciones", "Terms", "Conditions")}</a></nav>
    </div>
  </div>
</footer>"""


# ── <head> y datos estructurados ──────────────────────────────────────────
def head(key, title, desc, jsonld, noindex=False, preload=""):
    url = ABS(U(key)) if key else ""
    tags = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
        f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(desc)}">',
        '<meta name="robots" content="noindex">' if noindex else "",
        '<meta name="theme-color" content="#ffffff">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">',
        '<link rel="manifest" href="/site.webmanifest">',
    ]
    if key:
        tags.append(f'<link rel="canonical" href="{url}">')
        tags += [f'<link rel="alternate" hreflang="{lg}" href="{ABS(U(key, lg))}">' for lg in LANGS]
        tags.append(f'<link rel="alternate" hreflang="x-default" href="{ABS(U(key, "es"))}">')
    tags += [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Villa Mercedes">',
        f'<meta property="og:locale" content="{LOCALE[L()]}">',
        *[f'<meta property="og:locale:alternate" content="{LOCALE[lg]}">' for lg in LANGS if lg != L()],
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{url}">' if url else "",
        f'<meta property="og:image" content="{ABS("/img/og.jpg")}">',
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{esc(alt("jardin-comedor-exterior"))}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(title)}">',
        f'<meta name="twitter:description" content="{esc(desc)}">',
        f'<meta name="twitter:image" content="{ABS("/img/og.jpg")}">',
        '<link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>',
        preload,
        f'<link rel="stylesheet" href="{asset("css/styles.css")}">',
        '<script>document.documentElement.classList.add("js")' + (';document.documentElement.classList.add("show-pending")' if SHOW_PENDING else "") + "</script>",
    ]
    for block in jsonld or []:
        tags.append(f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False, separators=(",", ":"))}</script>')
    return "\n".join(t for t in tags if t)


def breadcrumbs_ld(crumbs):
    items = [{"@type": "ListItem", "position": 1, "name": X("Inicio", "Home", "Accueil"), "item": ABS(U("home"))}]
    for i, (k, t) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": t, **({"item": ABS(U(k))} if k else {})})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def website_ld():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": ABS("/#website"), "name": "Villa Mercedes",
            "url": ABS(U("home")), "inLanguage": {"es": "es-ES", "en": "en-GB", "fr": "fr-FR"}[L()]}


def rental_ld():
    """VacationRental: solo datos reales. Los campos vacíos de CONFIG no se publican."""
    imgs = ["jardin-comedor-exterior", "salon-comedor", "cocina", "dormitorio-principal", "dormitorio-dos-camas",
            "bano-banera", "bano-ducha", "jardin-vista-general", "salon-salida-jardin", "jardin-zona-lounge"]
    acc = {"@type": "Accommodation", "additionalType": "EntirePlace",
           "floorSize": {"@type": "QuantitativeValue", "value": 60, "unitCode": "MTK"},
           "numberOfBedrooms": 2, "numberOfBathroomsTotal": 2,
           "bed": [{"@type": "BedDetails", "numberOfBeds": 1, "typeOfBed": "Double"},
                   {"@type": "BedDetails", "numberOfBeds": 2, "typeOfBed": "Single"}],
           # Nombres de la lista de servicios que admite Google para VacationRental; solo los confirmados
           "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": v} for n, v in
                              [("wifi", True), ("kitchen", True), ("microwave", True), ("ovenStove", True), ("tv", True),
                               ("patio", True), ("smokingAllowed", False)]]}
    if CONFIG["MAX_GUESTS"]:
        acc["occupancy"] = {"@type": "QuantitativeValue", "value": CONFIG["MAX_GUESTS"]}
    d = {
        "@context": "https://schema.org", "@type": "VacationRental", "@id": ABS("/#vacationrental"),
        "name": "Villa Mercedes",
        "description": X("Apartamento vacacional de 60 m² con dos dormitorios, dos baños, terraza y jardín en Santoña (Cantabria), a 16 minutos a pie de la playa de Berria.",
                         "60 m² holiday apartment with two bedrooms, two bathrooms, a terrace and a garden in Santoña (Cantabria), a 16-minute walk from Berria beach.",
                         "Appartement de vacances de 60 m² avec deux chambres, deux salles de bains, terrasse et jardin à Santoña (Cantabrie), à 16 minutes à pied de la plage de Berria."),
        "url": ABS(U("home")),
        "image": [ABS(f"/img/{n}-1200.webp") for n in imgs],
        "address": {"@type": "PostalAddress", "streetAddress": "Barrio Piedrahita, Urbanización Villa Mercedes, 74",
                    "postalCode": "39740", "addressLocality": "Santoña", "addressRegion": "Cantabria", "addressCountry": "ES"},
        "knowsLanguage": ["es", "en", "fr"],
        "containsPlace": acc,
    }
    if CONFIG["LAT"] and CONFIG["LNG"]:
        d["latitude"], d["longitude"] = float(CONFIG["LAT"]), float(CONFIG["LNG"])
    if CONFIG["CHECKIN"]:
        d["checkinTime"] = CONFIG["CHECKIN"] + ":00"
    if CONFIG["CHECKOUT"]:
        d["checkoutTime"] = CONFIG["CHECKOUT"] + ":00"
    if CONFIG["REGISTRO_TURISTICO"]:
        d["identifier"] = CONFIG["REGISTRO_TURISTICO"]
    if CONFIG["TELEFONO"]:
        d["telephone"] = CONFIG["TELEFONO"]
    if CONFIG["EMAIL"]:
        d["email"] = CONFIG["EMAIL"]
    if CONFIG["SAME_AS"]:
        d["sameAs"] = CONFIG["SAME_AS"]
    return d


def site_config():
    return json.dumps({"whatsapp": CONFIG["WHATSAPP"], "email": CONFIG["EMAIL"], "maxGuests": CONFIG["MAX_GUESTS"], "blockedDates": [],
                       "pending": SHOW_PENDING, "urls": {"reservar": U("reservar"), "condiciones": U("condiciones"), "privacidad": U("privacidad")}})


def render(key, title, desc, local_title, local_links, body, crumbs, jsonld=None, bookbar=False, cta=True, preload="", out=None, noindex=False):
    bb = (f'<a href="{U("reservar")}" class="bookbar"><span><b>Villa Mercedes</b> · {X("60 m² con jardín", "60 m² with garden", "60 m² avec jardin")}</span>'
          f'<span class="pill pill-sm">{X("Ver fechas", "Check dates", "Voir les dates")}</span></a>') if bookbar else ""
    blocks = (jsonld or []) + ([breadcrumbs_ld(crumbs)] if crumbs else [])
    doc = f"""<!doctype html>
<html lang="{L()}">
<head>
{head(key, title, desc, blocks, noindex, preload)}
</head>
<body>
{header(key or "home", local_title, local_links, cta)}
<main id="contenido">
{body}
</main>
{bb}
{footer(key or "home", crumbs)}
<script type="application/json" id="site-config">{site_config()}</script>
<script src="{asset("js/main.js")}" defer></script>
</body>
</html>
"""
    rel = out or (PREFIX[L()] + ROUTES[key][L()] + "index.html")
    doc = finish_pending(doc, rel)
    if not out:
        doc = relativize(doc, rel)
    path = OUT / rel.lstrip("/")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc, encoding="utf-8")
    if key and not noindex:
        SITEMAP.add(key)


def relativize(doc, rel):
    """Convierte las rutas internas "/..." en relativas a la página, para que la web
    funcione igual en el hosting, en Live Server abriendo cualquier carpeta o en una subcarpeta.
    Las URL absolutas (canonical, hreflang, og:, JSON-LD) no cambian. La 404 se queda con rutas
    desde la raíz, porque el servidor la sirve en cualquier profundidad."""
    depth = rel.strip("/").count("/")
    up = "../" * depth
    doc = re.sub(r'(?<=")/(?=")', up or "./", doc)   # enlaces a la portada: "/"
    return re.sub(r'(?<=["\s,(])/(?=[A-Za-z0-9#?_.-])', up, doc)


# ── robots.txt, sitemap.xml, .htaccess y manifest ─────────────────────────
SITEMAP = set()


def write_server_files():
    keys = [k for k in ROUTES if k in SITEMAP]
    urls = []
    for k in keys:
        for lg in LANGS:
            alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{a}" href="{ABS(U(k, a))}"/>' for a in LANGS)
            alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{ABS(U(k, "es"))}"/>'
            urls.append(f"  <url>\n    <loc>{ABS(U(k, lg))}</loc>{alts}\n  </url>")
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {ABS('/sitemap.xml')}\n", encoding="utf-8")
    host = re.sub(r"^https?://", "", CONFIG["SITE_URL"]).rstrip("/")
    (OUT / ".htaccess").write_text((ROOT / "htaccess.template").read_text(encoding="utf-8").replace("{{HOST}}", host.replace(".", r"\.")).replace("{{HOST_PLAIN}}", host), encoding="utf-8")
    (OUT / "site.webmanifest").write_text(json.dumps({
        "name": "Villa Mercedes", "short_name": "Villa Mercedes", "lang": "es", "start_url": "/", "display": "browser",
        "background_color": "#ffffff", "theme_color": "#ffffff",
        "icons": [{"src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}, {"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}],
    }, ensure_ascii=False, indent=2), encoding="utf-8")


def clean_old():
    """Borra las páginas generadas en versiones anteriores (rutas .html antiguas)."""
    for p in list(OUT.glob("*.html")) + list(OUT.glob("legal/*.html")):
        p.unlink()
    if (OUT / "legal").exists() and not any((OUT / "legal").iterdir()):
        (OUT / "legal").rmdir()
    for lg in LANGS:
        for slug in {r[lg] for r in ROUTES.values() if r[lg]}:
            f = OUT / PREFIX[lg].lstrip("/") / slug / "index.html"
            if f.exists():
                f.unlink()


def run():
    import contenido
    clean_old()
    for lg in LANGS:
        _L["lang"] = lg
        contenido.build_all()
    _L["lang"] = "es"
    contenido.page_404()
    write_server_files()
    if "TU-DOMINIO" in CONFIG["SITE_URL"]:
        print("AVISO: SITE_URL todavía es el dominio de ejemplo. Cámbialo antes de publicar.")
    print("Páginas generadas en", OUT)
    if _all_pending:
        print(f"Datos pendientes ({len(_all_pending)}):", "; ".join(sorted(_all_pending)))


if __name__ == "__main__":
    # Se importa a sí mismo como módulo para que contenido.py comparta el mismo estado
    sys.path.insert(0, str(ROOT))
    import build
    build.run()
