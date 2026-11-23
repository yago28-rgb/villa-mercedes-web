"""
Villa Mercedes · textos de cada página en español, inglés y francés.

X("español", "english", "français") devuelve el texto del idioma que se está generando.
P("dato") marca un dato pendiente: no se publica hasta que lo rellenes.
"""
import json

from build import (ALT, CAP, CONFIG, NEXT, PREV, U, W, X, L, P, ROUTES, ABS, alt, arrow, cap, esc, ic, keep, opt,
                   pic, render, rental_ld, website_ld)


def build_all():
    page_home()
    page_casa()
    page_galeria()
    page_guia()
    page_reservar()
    page_opiniones()
    page_faq()
    page_contacto()
    page_condiciones()
    page_aviso()
    page_privacidad()
    page_cookies()


def crumbs_head(label):
    home = X("Inicio", "Home", "Accueil")
    return f'<ol class="crumbs" aria-label="{X("Ruta", "Breadcrumb", "Fil d’Ariane")}"><li><a href="{U("home")}">{home}</a></li><li aria-current="page">{label}</li></ol>'


# ══════════════════════════════════════════════════════════════════════════
#  INICIO
# ══════════════════════════════════════════════════════════════════════════
def page_home():
    t_badge = X("Ubicación valorada en Booking.com", "Location rated by Booking.com guests", "Emplacement noté sur Booking.com")
    t_kicker = X("Apartamento vacacional en Santoña, Cantabria", "Holiday apartment in Santoña, Cantabria", "Appartement de vacances à Santoña, Cantabrie")
    t_sub = X("Tu casa con jardín, a un paseo de la playa de Berria.", "Your home with a garden, a short walk from Berria beach.", "Votre maison avec jardin, à deux pas de la plage de Berria.")
    t_cta = X("Consultar disponibilidad", "Check availability", "Voir les disponibilités")
    t_plan = X("Recorre el plano", "Explore the floor plan", "Parcourir le plan")
    facts = [("home", "60 m²", X("Alojamiento entero", "Entire apartment", "Logement entier")),
             ("bed", "2", X("Dormitorios", "Bedrooms", "Chambres")),
             ("bath", "2", X("Baños completos", "Bathrooms", "Salles de bains")),
             ("garden", X("Jardín", "Garden", "Jardin"), X("y terraza", "and terrace", "et terrasse")),
             ("walk", "16 min", X("a pie de Berria", "walk to Berria", "à pied de Berria"))]
    facts_html = "".join(f'<li data-reveal style="--d:{0.6 + i * 0.08:.2f}s">{ic(k, 22)}<b>{a}</b><span>{b}</span></li>' for i, (k, a, b) in enumerate(facts))
    slide_list = [("jardin-vista-general", X("El jardín", "The garden", "Le jardin")),
                  ("salon-salida-jardin", X("Salón con salida al jardín", "Living room opening onto the garden", "Salon ouvert sur le jardin")),
                  ("dormitorio-principal", X("Dormitorio principal", "Main bedroom", "Chambre principale")),
                  ("cocina", X("Cocina equipada", "Fitted kitchen", "Cuisine équipée")),
                  ("jardin-zona-lounge", X("Zona de sofás", "Lounge area", "Coin canapés"))]
    slides = "".join(
        f'<img src="/img/{n}-v-720.webp" srcset="/img/{n}-v-720.webp 720w, /img/{n}-v.webp 1080w" sizes="(max-width: 734px) calc(100vw - 40px), 1px" width="1080" height="1350" alt="{esc(alt(n))}" data-label="{esc(lab)}"'
        + ' loading="lazy" decoding="async">'
        for i, (n, lab) in enumerate(slide_list))
    scenes = json.dumps([[0, X("Urbanización Villa Mercedes", "Villa Mercedes complex", "Résidence Villa Mercedes")],
                         [3.8, X("Salón con salida al jardín", "Living room opening onto the garden", "Salon ouvert sur le jardin")],
                         [6.7, X("Dormitorio principal", "Main bedroom", "Chambre principale")],
                         [7.4, X("Jardín y terraza", "Garden and terrace", "Jardin et terrasse")]], ensure_ascii=False)
    t_video = X("Recorrido en vídeo por el exterior, el salón, el dormitorio y el jardín", "Video tour of the exterior, living room, bedroom and garden",
                "Visite vidéo de l’extérieur, du salon, de la chambre et du jardin")
    t_slides = X("Fotografías del apartamento", "Photos of the apartment", "Photos de l’appartement")
    t_note = X("En ordenador: vídeo generado con IA a partir de fotografías reales. En móvil: fotografías reales.",
               "On desktop: AI-generated video based on real photos. On mobile: real photos.",
               "Sur ordinateur : vidéo générée par IA à partir de photos réelles. Sur mobile : photos réelles.")
    t_pause = X("Pausar", "Pause", "Pause")
    floats = [
        ("fl-1", "1.2", "1.1s", '<img src="/img/jardin-comedor-exterior-640.webp" width="640" height="480" alt="" loading="lazy">', X("Jardín", "Garden", "Jardin"), X("Comedor para seis", "Dining for six", "Table pour six")),
        ("fl-2", ".8", "1.25s", f'<span class="fl-ic">{ic("walk", 22)}</span>', X("16 min a pie", "16-minute walk", "16 min à pied"), X("Playa de Berria", "Berria beach", "Plage de Berria")),
        ("fl-3", ".7", "1.4s", f'<span class="fl-ic">{ic("wifi", 22)}</span>', X("Wifi gratis", "Free wifi", "Wifi gratuit"), X("Ropa de cama y toallas", "Bed linen and towels", "Linge de lit et serviettes")),
        ("fl-4", "1.1", "1.55s", '<img src="/img/dormitorio-principal-640.webp" width="640" height="480" alt="" loading="lazy">', X("2 dormitorios", "2 bedrooms", "2 chambres"), X("Matrimonio y dos camas", "Double and twin", "Lit double et lits jumeaux")),
    ]
    floats_html = "".join(f'<div class="fl {c}" style="--dp:{dp};--d:{d}"><div class="fl-in">{media}<p><b>{a}</b><span>{b}</span></p></div></div>' for c, dp, d, media, a, b in floats)

    statement = X("60&nbsp;m² pensados para descansar. Dos dormitorios, dos baños, una cocina con todo lo necesario y un jardín junto a la ladera verde. Reserva directa, sin intermediarios.",
                  "60&nbsp;m² made for slowing down. Two bedrooms, two bathrooms, a kitchen with everything you need and a garden beside the green hillside. Book direct, no middlemen.",
                  "60&nbsp;m² pensés pour se reposer. Deux chambres, deux salles de bains, une cuisine tout équipée et un jardin au pied de la colline verdoyante. Réservation directe, sans intermédiaire.")
    hl = X("jardín|directa", "garden|direct", "jardin|directe")
    chips = [("home", X("60 m² · alojamiento entero", "60 m² · entire apartment", "60 m² · logement entier")),
             ("bed", X("2 dormitorios", "2 bedrooms", "2 chambres")), ("bath", X("2 baños completos", "2 bathrooms", "2 salles de bains")),
             ("garden", X("Jardín y terraza", "Garden and terrace", "Jardin et terrasse")), ("walk", X("16 min a pie de Berria", "16-minute walk to Berria", "16 min à pied de Berria")),
             ("wifi", X("Wifi gratis", "Free wifi", "Wifi gratuit")), ("linen", X("Ropa de cama y toallas", "Bed linen and towels", "Linge de lit et serviettes")),
             ("lang", X("Español, inglés y francés", "Spanish, English and French spoken", "On parle espagnol, anglais et français")),
             ("plane", X("Aeropuerto de Santander a 40 km", "Santander airport 40 km away", "Aéroport de Santander à 40 km"))]
    chips_html = "".join(f'<span class="chip">{ic(k, 20)}{t}</span>' for k, t in chips)
    cards = [("salon-comedor", X("Salón", "Living room", "Salon"), X("Luz natural y salida directa al jardín.", "Natural light and direct access to the garden.", "Lumière naturelle et accès direct au jardin."), U("casa", anchor="salon")),
             ("jardin-vista-general", X("Jardín", "Garden", "Jardin"), X("Comedor exterior para seis y zona de sofás.", "Outdoor dining for six and a lounge area.", "Table extérieure pour six et coin canapés."), U("casa", anchor="jardin")),
             ("cocina", X("Cocina", "Kitchen", "Cuisine"), X("Totalmente equipada, con salida a la terraza.", "Fully equipped, opening onto the terrace.", "Entièrement équipée, avec accès à la terrasse."), U("casa", anchor="cocina")),
             ("dormitorio-principal", X("Dormitorios", "Bedrooms", "Chambres"), X("Uno de matrimonio y otro con dos camas.", "One double and one twin room.", "Une chambre double et une chambre à deux lits."), U("casa", anchor="dormitorios")),
             ("bano-banera", X("Baños", "Bathrooms", "Salles de bains"), X("Dos baños completos: bañera y ducha.", "Two full bathrooms: bath and shower.", "Deux salles de bains : baignoire et douche."), U("casa", anchor="banos")),
             ("fachada-urbanizacion", X("Ubicación", "Location", "Emplacement"), X("Urbanización tranquila en Santoña.", "A quiet residential complex in Santoña.", "Une résidence calme à Santoña."), U("guia"))]
    car = "".join(f'<a class="car-card" href="{h}">{pic(n, "(min-width:1068px) 400px, 80vw")}<div class="car-tx"><p>{t}</p><h3>{d}</h3></div><span class="car-plus" aria-hidden="true">+</span></a>' for n, t, d, h in cards)
    go_to = X("Ir a", "Go to", "Aller à")
    dots = "".join(f'<button type="button" class="car-dot" aria-label="{go_to} {t}"><span></span></button>' for _, t, _, _ in cards)
    rows = [["jardin-comedor-exterior", "salon-comedor", "cocina", "dormitorio-principal", "jardin-zona-lounge"],
            ["bano-banera", "mesa-exterior-detalle", "salon-salida-jardin", "dormitorio-dos-camas", "jardin-vista-general"],
            ["fachada-urbanizacion", "bano-ducha", "jardin-zona-lounge", "cocina", "salon-comedor"]]
    gal = U("galeria")
    hp = "".join('<div class="hp-row">' + "".join(f'<a class="hp-item" href="{gal}#foto-{n}" tabindex="-1">{pic(n, "420px")}<span>{cap(n)}</span></a>' for n in r) + "</div>" for r in rows)
    focus = [("salon-salida-jardin", X("Para reunirse", "To get together", "Pour se retrouver"), X("El salón se abre al jardín.", "The living room opens onto the garden.", "Le salon s’ouvre sur le jardin."), U("casa", anchor="salon")),
             ("dormitorio-dos-camas", X("Para descansar", "To rest", "Pour se reposer"), X("Dos dormitorios tranquilos.", "Two quiet bedrooms.", "Deux chambres au calme."), U("casa", anchor="dormitorios")),
             ("cocina", X("Para cocinar", "To cook", "Pour cuisiner"), X("Todo a mano en la cocina.", "Everything to hand in the kitchen.", "Tout à portée de main en cuisine."), U("casa", anchor="cocina")),
             ("mesa-exterior-detalle", X("Para comer fuera", "To eat outdoors", "Pour manger dehors"), X("Mesa para seis junto al muro.", "A table for six by the wall.", "Une table pour six près du mur."), U("casa", anchor="jardin"))]
    fc = "".join(f'<a class="fc-item" href="{h}" data-reveal>{pic(n, "(min-width:1068px) 300px, (min-width:735px) 50vw, 100vw")}<div><h3>{t}</h3><p>{d}</p></div></a>' for n, t, d, h in focus)
    direct = [("tag", X("Sin comisiones de plataforma", "No platform fees", "Sans frais de plateforme"),
               X("Reservas con nosotros, sin intermediarios.", "You book with us, with no middlemen.", "Vous réservez avec nous, sans intermédiaire.")),
              ("chat", X("Trato directo", "Talk to the owner", "Contact direct"),
               X("Te respondemos nosotros, en español, inglés o francés.", "We answer you ourselves, in Spanish, English or French.", "Nous vous répondons nous-mêmes, en espagnol, anglais ou français.")),
              ("lock", X("Condiciones claras", "Clear terms", "Conditions claires"),
               X("Precio, fianza y cancelación por escrito antes de confirmar.", "Price, deposit and cancellation in writing before you confirm.", "Prix, caution et annulation par écrit avant de confirmer."))]
    direct_html = "".join(f'<div class="card" data-reveal>{ic(k, 32)}<h3 class="mt-s">{t}</h3><p class="muted">{d}</p></div>' for k, t, d in direct)
    t_route = X("Esquema del recorrido a pie desde Villa Mercedes hasta la playa de Berria, unos 16 minutos",
                "Diagram of the walk from Villa Mercedes to Berria beach, about 16 minutes",
                "Schéma du trajet à pied de Villa Mercedes à la plage de Berria, environ 16 minutes")
    t_beach = X("Playa de Berria", "Berria beach", "Plage de Berria")
    dist = [(X("Playa de Berria", "Berria beach", "Plage de Berria"), X("16 min a pie", "16 min on foot", "16 min à pied")),
            (X("Aeropuerto de Santander", "Santander airport", "Aéroport de Santander"), "40 km"),
            ("Santander", X("42 km aprox.", "approx. 42 km", "env. 42 km")),
            ("Bilbao", X("1 h en coche aprox.", "approx. 1 h by car", "env. 1 h en voiture"))]
    dist_html = "".join(f"<li><span>{a}</span><span>{b}</span></li>" for a, b in dist)
    body = f"""
<section id="inicio" class="hero" data-bookbar-after>
  <div class="hero-aura" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="container hero-in">
    <a class="hero-badge" href="{U("opiniones")}" data-reveal><b>8,8</b><span>{t_badge}</span><i aria-hidden="true"></i></a>
    <h1 class="hero-h1"><span class="eyebrow">{t_kicker}</span><span class="display">Villa Mercedes</span></h1>
    <p class="sub h3" data-reveal style="--d:.35s">{t_sub}</p>
    <div class="ctas" data-reveal style="--d:.5s">
      <span data-magnetic><a href="{U("reservar")}" class="pill">{t_cta}</a></span>
      <a href="{U("casa", anchor="plano")}" class="link-chev">{t_plan}</a>
    </div>
    <ul class="hero-facts">{facts_html}</ul>
  </div>
  <div class="cs">
    <div class="cs-float" aria-hidden="true">{floats_html}</div>
    <div class="cs-card">
      <div class="cs-screen">
        <video muted loop playsinline preload="none" data-poster="/video/hero-poster.webp" data-src="/video/hero.mp4" data-scenes='{esc(scenes)}' aria-label="{t_video}"></video>
        <div class="slides" role="group" aria-label="{t_slides}" hidden>{slides}</div>
        <p class="cs-badge" aria-live="off"><span class="cs-label">{X("Urbanización Villa Mercedes", "Villa Mercedes complex", "Résidence Villa Mercedes")}</span></p>
        <button type="button" class="cs-pause" aria-pressed="false"><span class="sr-only">{t_pause}</span><span class="pp" aria-hidden="true"></span></button>
      </div>
    </div>
    <p class="cs-note">{t_note}</p>
  </div>
</section>

<section class="statement" aria-label="{X("Resumen", "Summary", "Résumé")}">
  <div class="container narrow"><p data-highlight="{hl}">{statement}</p></div>
</section>

<div class="islider" data-speed="40" data-speed-hover="10" role="region" aria-label="{X("Lo esencial", "Key facts", "L’essentiel")}">
  <div class="islider-track">{chips_html}</div>
</div>

<section class="section" aria-labelledby="hl-t">
  <div class="container sec-head"><h2 id="hl-t" class="h2" data-text-effect>{X("Lo esencial, de un vistazo", "The essentials at a glance", "L’essentiel en un coup d’œil")}</h2><a href="{U("casa", anchor="plano")}" class="link-chev" data-reveal>{X("Ver el plano de la casa", "See the floor plan", "Voir le plan de la maison")}</a></div>
  <div class="car">
    <div class="car-scroller"><div class="car-track">{car}</div></div>
    <div class="container car-controls">
      <div class="car-dots">{dots}</div>
      <div class="car-arrows">
        <button type="button" class="circle-btn car-prev" aria-label="{X("Anterior", "Previous", "Précédent")}">{arrow(PREV)}</button>
        <button type="button" class="circle-btn car-next" aria-label="{X("Siguiente", "Next", "Suivant")}">{arrow(NEXT)}</button>
      </div>
    </div>
  </div>
</section>

<section class="section bg-2" aria-labelledby="num-t">
  <div class="container">
    <h2 id="num-t" class="h2" data-text-effect>{X("Todo en su sitio", "Everything in its place", "Tout est à sa place")}</h2>
    <dl class="nums">
      <div data-reveal><dt>{X("Superficie del alojamiento", "Floor area", "Surface du logement")}</dt><dd><span class="sn sn-grad" data-sliding="60">60</span><span class="sn-unit">m²</span></dd></div>
      <div data-reveal><dt>{X("Dormitorios", "Bedrooms", "Chambres")}</dt><dd><span class="sn sn-grad" data-sliding="2">2</span></dd></div>
      <div data-reveal><dt>{X("Baños completos", "Bathrooms", "Salles de bains")}</dt><dd><span class="sn sn-grad" data-sliding="2">2</span></dd></div>
      <div data-reveal><dt>{X("Minutos a pie hasta la playa de Berria", "Minutes’ walk to Berria beach", "Minutes à pied jusqu’à la plage de Berria")}</dt><dd><span class="sn sn-grad" data-sliding="16">16</span><span class="sn-unit">min</span></dd></div>
      <div data-reveal><dt>{X("Puntuación de ubicación en Booking.com", "Booking.com location score", "Note d’emplacement sur Booking.com")}</dt><dd><span class="sn sn-grad" data-sliding="8.8" data-decimals="1">{X("8,8", "8.8", "8,8")}</span></dd></div>
    </dl>
  </div>
</section>

<section class="hp" aria-labelledby="hp-t">
  <div class="container hp-head center">
    <h2 id="hp-t" class="h2" data-text-effect>{X("La casa, tal como es", "The house as it really is", "La maison telle qu’elle est")}</h2>
    <p class="lead mt-s" data-reveal>{X("Fotografías reales del apartamento y la urbanización.", "Real photos of the apartment and the building.", "Photos réelles de l’appartement et de la résidence.")}</p>
    <div class="ctas center mt-m" data-reveal><a href="{gal}" class="link-chev">{X("Ver la galería completa", "See the full gallery", "Voir toute la galerie")}</a></div>
  </div>
  <div class="hp-stage" aria-hidden="true">{hp}</div>
</section>

<section class="section" aria-labelledby="fc-t">
  <div class="container">
    <h2 id="fc-t" class="h2" data-text-effect>{X("Un rincón para cada momento", "A spot for every moment", "Un coin pour chaque moment")}</h2>
    <div class="fc">{fc}</div>
  </div>
</section>

<section class="section bg-2" aria-labelledby="loc-t">
  <div class="container">
    <h2 id="loc-t" class="h2" data-text-effect>{X("Santoña, a pie", "Santoña on foot", "Santoña à pied")}</h2>
    <p class="lead mt-s" data-reveal>{X("Entre el monte Buciero y las marismas, en el centro de la costa de Cantabria.", "Between Monte Buciero and the marshes, in the middle of the Cantabrian coast.", "Entre le mont Buciero et les marais, au centre de la côte cantabrique.")}</p>
    <div class="route-grid">
      <div class="route-map" role="img" aria-label="{t_route}">
        <svg viewBox="0 0 800 460" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
          <defs><linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9d3dd"/><stop offset="1" stop-color="#d4e3e8"/></linearGradient></defs>
          <rect width="800" height="460" fill="#eef1ee"/>
          <path d="M0 0H800V120C700 150 640 92 560 110S420 170 330 130 160 80 0 128Z" fill="url(#sea)"/>
          <path d="M560 110C600 130 640 170 700 180S790 160 800 150V0H760" fill="#d7e5d3" opacity=".7"/>
          <path d="M0 380C120 360 180 420 300 400S520 360 800 420V460H0Z" fill="#dfe8dc"/>
          <g stroke="#ffffff" stroke-width="10" fill="none" stroke-linecap="round" opacity=".9"><path d="M80 300C200 280 300 300 420 260S600 230 740 250"/><path d="M300 460C320 380 330 330 360 290"/></g>
          <path class="route-path" d="M210 340C250 320 280 300 330 286S410 250 430 220 470 170 505 150" fill="none" stroke="#0071e3" stroke-width="5" stroke-linecap="round"/>
          <g class="route-pin"><circle cx="505" cy="150" r="12" fill="#0071e3"/><circle cx="505" cy="150" r="22" fill="#0071e3" opacity=".18"/></g>
          <circle cx="210" cy="340" r="11" fill="#1d1d1f"/><circle cx="210" cy="340" r="4" fill="#fff"/>
          <text x="228" y="372" font-family="-apple-system, Helvetica, Arial" font-size="17" font-weight="600" fill="#1d1d1f">Villa Mercedes</text>
          <text x="522" y="140" font-family="-apple-system, Helvetica, Arial" font-size="17" font-weight="600" fill="#1d1d1f">{t_beach}</text>
        </svg>
        <p class="route-time"><b>16 min</b><span>{X("a pie hasta Berria", "walk to Berria", "à pied jusqu’à Berria")}</span></p>
        <p class="route-note">{X("Esquema ilustrativo, no a escala", "Illustrative diagram, not to scale", "Schéma indicatif, pas à l’échelle")}</p>
      </div>
      <div class="card" data-reveal>
        <h3 class="h3">{X("Distancias", "Distances", "Distances")}</h3>
        <ul class="dist mt-s">{dist_html}</ul>
        <p class="mt-m"><a href="{U("guia")}" class="link-chev">{X("Qué ver en Santoña", "Things to do in Santoña", "Que faire à Santoña")}</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="dir-t">
  <div class="container">
    <h2 id="dir-t" class="h2" data-text-effect>{X("Por qué reservar directo", "Why book direct", "Pourquoi réserver en direct")}</h2>
    <div class="direct mt-l">{direct_html}</div>
  </div>
</section>

<section class="section bg-2" aria-labelledby="op-t">
  <div class="container center">
    <h2 id="op-t" class="h2" data-text-effect>{X("Lo que valoran los huéspedes", "What guests value", "Ce que les voyageurs apprécient")}</h2>
    <p class="score mt-m" data-reveal>{X("8,8", "8.8", "8,8")}</p>
    <p class="sub" data-reveal>{X("Puntuación de ubicación en Booking.com", "Booking.com location score", "Note d’emplacement sur Booking.com")}</p>
    <div class="ctas center mt-m" data-reveal><a href="{U("opiniones")}" class="link-chev">{X("Leer opiniones", "Read reviews", "Lire les avis")}</a></div>
  </div>
</section>

<section class="final" aria-labelledby="fin-t">
  {pic("jardin-vista-general", "100vw")}
  <div class="pblur" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
  <div class="final-tx">
    <h2 id="fin-t" class="h1" data-text-effect>{X("Reserva directa, sin comisiones", "Book direct, no booking fees", "Réservez en direct, sans frais")}</h2>
    <p class="sub mt-s" data-reveal>{X("Hablas con nosotros, no con una plataforma.", "You deal with us, not a platform.", "Vous parlez avec nous, pas avec une plateforme.")}</p>
    <div class="ctas" data-reveal><span data-magnetic><a href="{U("reservar")}" class="pill pill-light">{X("Ver fechas libres", "See available dates", "Voir les dates libres")}</a></span><a href="{U("contacto")}" class="link-chev link-light">{X("Escríbenos", "Get in touch", "Nous écrire")}</a></div>
  </div>
</section>"""
    title = X("Alquiler vacacional en Santoña con jardín | Villa Mercedes",
              "Holiday Rental in Santoña with Garden | Villa Mercedes",
              "Location vacances à Santoña avec jardin | Villa Mercedes")
    desc = X("Apartamento de 60 m² con 2 dormitorios, 2 baños, terraza y jardín en Santoña (Cantabria), a 16 min a pie de la playa de Berria. Reserva directa sin comisiones.",
             "60 m² holiday apartment in Santoña, Cantabria: 2 bedrooms, 2 bathrooms, terrace and garden, a 16-minute walk from Berria beach. Book direct with no fees.",
             "Appartement de 60 m² à Santoña (Cantabrie) : 2 chambres, 2 salles de bains, terrasse et jardin, à 16 min à pied de la plage de Berria. Réservation directe.")
    preload = '<link rel="preload" as="image" href="/video/hero-poster.webp" media="(min-width: 735px)" fetchpriority="high">'
    render("home", title, desc, "Villa Mercedes",
           [(U("casa"), X("La casa", "The house", "La maison")), (U("galeria"), X("Galería", "Gallery", "Galerie")),
            (U("guia"), X("Qué ver", "Things to do", "À voir")), (U("opiniones"), X("Opiniones", "Reviews", "Avis"))],
           body, [], [website_ld(), rental_ld()], bookbar=True, preload=preload)


# ══════════════════════════════════════════════════════════════════════════
#  LA CASA (incluye el plano interactivo)
# ══════════════════════════════════════════════════════════════════════════
PLAN_ROOMS = [
    ("salon", ("Salón", "Living room", "Salon"), ("Comedor y estar", "Dining and lounge", "Séjour et repas"), (113, 203, 291, 224), (190, 245)),
    ("cocina", ("Cocina", "Kitchen", "Cuisine"), ("Salida a la terraza", "Opens onto the terrace", "Accès terrasse"), (410, 203, 297, 224), (545, 290)),
    ("dorm1", ("Dormitorio 1", "Bedroom 1", "Chambre 1"), ("Matrimonio", "Double", "Lit double"), (113, 487, 202, 150), (196, 522)),
    ("bano1", ("Baño 1", "Bath 1", "SdB 1"), ("Bañera", "Bathtub", "Baignoire"), (321, 487, 86, 150), (364, 535)),
    ("bano2", ("Baño 2", "Bath 2", "SdB 2"), ("Ducha", "Shower", "Douche"), (413, 487, 86, 150), (456, 535)),
    ("dorm2", ("Dormitorio 2", "Bedroom 2", "Chambre 2"), ("Dos camas", "Twin", "Deux lits"), (505, 487, 202, 150), (626, 522)),
]
PLAN_ORDER = ["salon", "cocina", "dorm1", "dorm2", "bano1", "bano2", "jardin"]


def plan_info():
    day, night, out = X("Zona de día", "Day area", "Espace jour"), X("Zona de noche", "Night area", "Espace nuit"), X("Exterior", "Outdoors", "Extérieur")
    linen, towels = X("Ropa de cama incluida", "Bed linen included", "Linge de lit fourni"), X("Toallas incluidas", "Towels included", "Serviettes fournies")
    return {
        "salon": (day, X("Salón comedor", "Living and dining room", "Salon et salle à manger"),
                  X("Un solo espacio para estar y comer, con puerta acristalada directa al jardín.", "One space to relax and eat, with a glazed door straight onto the garden.", "Un seul espace pour se détendre et manger, avec une porte vitrée donnant directement sur le jardin."),
                  [X("Sofá y sillones", "Sofa and armchairs", "Canapé et fauteuils"), X("Mesa de comedor", "Dining table", "Table à manger"), X("Televisión y radio", "TV and radio", "Télévision et radio"), X("Puerta al jardín", "Door to the garden", "Porte sur le jardin")],
                  "salon-salida-jardin", "foto-salon-comedor"),
        "cocina": (day, X("Cocina", "Kitchen", "Cuisine"),
                   X("Totalmente equipada, con salida a la terraza para comer fuera sin dar la vuelta.", "Fully equipped, with a door to the terrace so you can eat outside.", "Entièrement équipée, avec une porte sur la terrasse pour manger dehors."),
                   [X("Horno y microondas", "Oven and microwave", "Four et micro-ondes"), X("Nevera", "Fridge", "Réfrigérateur"), X("Cafetera, tetera y tostadora", "Coffee maker, kettle and toaster", "Cafetière, bouilloire et grille-pain"), X("Lavadora", "Washing machine", "Lave-linge"), X("Salida a la terraza", "Terrace access", "Accès à la terrasse")],
                   "cocina", "foto-cocina"),
        "dorm1": (night, X("Dormitorio principal", "Main bedroom", "Chambre principale"),
                  X("Con cama de matrimonio. La ropa de cama y las toallas están incluidas.", "With a double bed. Bed linen and towels are included.", "Avec un lit double. Le linge de lit et les serviettes sont fournis."),
                  [X("Cama de matrimonio", "Double bed", "Lit double"), linen, towels], "dormitorio-principal", "foto-dormitorio-principal"),
        "bano1": (night, X("Baño con bañera", "Bathroom with bathtub", "Salle de bains avec baignoire"),
                  X("Baño completo con bañera y mampara.", "Full bathroom with a bathtub and screen.", "Salle de bains complète avec baignoire et pare-bain."),
                  [X("Bañera con mampara", "Bathtub with screen", "Baignoire avec pare-bain"), X("Lavabo con mueble", "Vanity unit", "Meuble vasque"), X("Inodoro y bidé", "Toilet and bidet", "WC et bidet")], "bano-banera", "foto-bano-banera"),
        "bano2": (night, X("Baño con ducha", "Shower room", "Salle d’eau"),
                  X("Segundo baño completo, con plato de ducha.", "A second full bathroom, with a shower.", "Une seconde salle de bains, avec douche."),
                  [X("Ducha con mampara", "Shower with screen", "Douche avec paroi"), X("Lavabo con mueble", "Vanity unit", "Meuble vasque"), X("Inodoro", "Toilet", "WC")], "bano-ducha", "foto-bano-ducha"),
        "dorm2": (night, X("Dormitorio con dos camas", "Twin bedroom", "Chambre à deux lits"),
                  X("Dos camas individuales y ventana hacia la ladera verde.", "Two single beds and a window onto the green hillside.", "Deux lits simples et une fenêtre sur la colline verdoyante."),
                  [X("Dos camas individuales", "Two single beds", "Deux lits simples"), linen, towels], "dormitorio-dos-camas", "foto-dormitorio-dos-camas"),
        "jardin": (out, X("Jardín y terraza", "Garden and terrace", "Jardin et terrasse"),
                   X("Césped, comedor exterior y una zona de sofás junto al muro de piedra.", "Lawn, an outdoor dining area and a lounge corner by the stone wall.", "Pelouse, coin repas extérieur et coin canapés près du mur en pierre."),
                   [X("Césped", "Lawn", "Pelouse"), X("Comedor exterior para seis", "Outdoor dining for six", "Table extérieure pour six"), X("Zona de sofás", "Lounge area", "Coin canapés"), X("Terraza junto a la cocina", "Terrace by the kitchen", "Terrasse près de la cuisine")],
                   "jardin-vista-general", "foto-jardin-vista-general"),
    }


def _door(h, e, leaf):
    r = abs(e[0] - h[0]) + abs(e[1] - h[1])
    cross = (e[0] - h[0]) * (leaf[1] - h[1]) - (e[1] - h[1]) * (leaf[0] - h[0])
    sweep = 1 if cross > 0 else 0
    return f'<path d="M{h[0]} {h[1]}L{leaf[0]} {leaf[1]}"/><path class="arc" d="M{e[0]} {e[1]}A{r} {r} 0 0 {sweep} {leaf[0]} {leaf[1]}"/>'


def plan_svg(info):
    outer = ["M110 200H190", "M280 200H600", "M640 200H710V640H110V476", "M110 440V200"]
    inner = ["M407 200V300", "M407 360V430", "M110 430H300", "M340 430H450", "M490 430H710",
             "M110 484H272", "M308 484H345", "M375 484H437", "M467 484H512", "M548 484H710",
             "M318 484V640", "M410 484V640", "M502 484V640"]
    doors = "".join([_door((308, 484), (272, 484), (308, 520)), _door((345, 484), (375, 484), (345, 514)),
                     _door((467, 484), (437, 484), (467, 514)), _door((512, 484), (548, 484), (512, 520)),
                     _door((300, 430), (340, 430), (300, 390)), _door((490, 430), (450, 430), (490, 390)),
                     _door((110, 440), (110, 476), (146, 440))])
    chairs = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/>' for x, y, w, h in
                     [(214, 62, 20, 14), (266, 62, 20, 14), (214, 134, 20, 14), (266, 134, 20, 14), (178, 97, 14, 20), (308, 97, 14, 20)])
    salon_chairs = "".join(f'<rect x="{x}" y="{y}" width="16" height="12" rx="3"/>' for x, y in [(310, 220), (354, 220), (310, 288), (354, 288)])
    furn = {
        "jardin": f'<ellipse cx="250" cy="105" rx="52" ry="26"/>{chairs}<rect x="500" y="64" width="112" height="26" rx="9"/><rect x="618" y="64" width="26" height="84" rx="9"/><rect x="526" y="104" width="54" height="32" rx="5"/><rect x="474" y="106" width="30" height="30" rx="8"/>',
        "salon": f'<rect x="132" y="318" width="150" height="38" rx="8"/><rect x="132" y="318" width="38" height="96" rx="8"/><rect x="196" y="368" width="58" height="34" rx="4"/><rect x="262" y="372" width="30" height="30" rx="8"/><rect x="300" y="236" width="80" height="48" rx="4"/>{salon_chairs}',
        "cocina": '<rect x="414" y="207" width="180" height="26" rx="2"/><rect x="677" y="207" width="26" height="150" rx="2"/><rect x="677" y="362" width="26" height="36" rx="2"/><circle cx="460" cy="220" r="7"/><circle cx="482" cy="220" r="7"/>',
        "dorm1": '<rect x="170" y="540" width="92" height="94" rx="6"/><rect x="176" y="610" width="36" height="18" rx="5"/><rect x="220" y="610" width="36" height="18" rx="5"/><rect x="142" y="610" width="22" height="22" rx="3"/><rect x="268" y="610" width="22" height="22" rx="3"/>',
        "dorm2": '<rect x="526" y="548" width="48" height="86" rx="6"/><rect x="532" y="612" width="36" height="16" rx="5"/><rect x="636" y="548" width="48" height="86" rx="6"/><rect x="642" y="612" width="36" height="16" rx="5"/>',
        "bano1": '<rect x="325" y="580" width="78" height="54" rx="10"/><rect x="333" y="588" width="62" height="38" rx="14"/><rect x="378" y="492" width="26" height="20" rx="4"/>',
        "bano2": '<rect x="455" y="590" width="42" height="44" rx="3"/><path d="M455 590l42 44M497 590l-42 44"/><rect x="417" y="492" width="26" height="20" rx="4"/><ellipse cx="428" cy="620" rx="10" ry="13"/>',
    }
    furn_html = "".join(f'<g class="furn" data-of="{k}">{v}</g>' for k, v in furn.items())
    zones = "".join(f'<rect class="zone" data-zone="{k}" x="{x}" y="{y}" width="{w}" height="{h}" rx="3" tabindex="0" role="button" aria-label="{esc(info[k][1])}"/>'
                    for k, _, _, (x, y, w, h), _ in PLAN_ROOMS)
    labels = "".join(f'<g class="lbl" data-of="{k}"><text class="rn" x="{lx}" y="{ly}">{X(*n)}</text><text class="rs" x="{lx}" y="{ly + 18}">{X(*s)}</text></g>'
                     for k, n, s, _, (lx, ly) in PLAN_ROOMS)
    outer_p = "".join(f'<path pathLength="1" d="{d}"/>' for d in outer)
    inner_p = "".join(f'<path pathLength="1" d="{d}"/>' for d in inner)
    t_aria = X("Esquema de la distribución de Villa Mercedes", "Layout diagram of Villa Mercedes", "Schéma de la distribution de Villa Mercedes")
    t_wall, t_terr, t_hall = X("Muro de piedra", "Stone wall", "Mur en pierre"), X("Terraza", "Terrace", "Terrasse"), X("Distribuidor", "Hallway", "Couloir")
    t_garden, t_garden_s = X("Jardín", "Garden", "Jardin"), X("Comedor y sofás", "Dining and sofas", "Repas et canapés")
    t_jardin = esc(info["jardin"][1])
    return f"""<svg class="plan-svg" viewBox="0 0 820 700" role="group" aria-label="{t_aria}">
  <defs>
    <pattern id="pl-grass" width="16" height="16" patternUnits="userSpaceOnUse"><path d="M3 6l2 -3M11 13l2 -3" stroke="#c6d6c0" stroke-width="1.2" stroke-linecap="round"/></pattern>
    <pattern id="pl-stone" width="24" height="16" patternUnits="userSpaceOnUse"><rect width="24" height="16" fill="#d9d6cc"/><path d="M0 8H24M8 0V8M20 8V16" stroke="#c2beb2" stroke-width="1"/></pattern>
    <pattern id="pl-tile" width="20" height="20" patternUnits="userSpaceOnUse"><rect width="20" height="20" fill="#efebe3"/><path d="M0 0H20V20" fill="none" stroke="#e1dbd0" stroke-width="1"/></pattern>
  </defs>
  <rect class="zone zone-out" data-zone="jardin" x="20" y="20" width="780" height="660" rx="26" tabindex="0" role="button" aria-label="{t_jardin}"/>
  <rect x="20" y="20" width="780" height="660" rx="26" fill="url(#pl-grass)" pointer-events="none"/>
  <rect x="44" y="30" width="732" height="16" rx="4" fill="url(#pl-stone)" pointer-events="none"/>
  <text class="rs tiny" x="410" y="62">{t_wall}</text>
  <rect x="110" y="160" width="600" height="40" fill="url(#pl-tile)" pointer-events="none"/>
  <text class="rs tiny" x="655" y="184">{t_terr}</text>
  <rect x="110" y="200" width="600" height="440" fill="#fff" pointer-events="none"/>
  <rect x="113" y="433" width="594" height="48" fill="#fafafa" pointer-events="none"/>
  <text class="rs tiny" x="420" y="462">{t_hall}</text>
  {zones}
  <g class="furn-all" pointer-events="none">{furn_html}</g>
  <g class="walls" pointer-events="none">
    <g class="w-out">{outer_p}</g>
    <g class="w-in">{inner_p}</g>
    <g class="glass"><path d="M190 200H280M600 200H640"/></g>
    <g class="doors">{doors}</g>
  </g>
  <g class="lbl" data-of="jardin" pointer-events="none"><text class="rn" x="410" y="104">{t_garden}</text><text class="rs" x="410" y="122">{t_garden_s}</text></g>
  <g pointer-events="none">{labels}</g>
</svg>"""


def plan_section():
    info = plan_info()
    gal = U("galeria")
    data = {k: {"k": v[0], "name": v[1], "desc": v[2], "items": v[3], "img": f"/img/{v[4]}-1200.webp", "alt": alt(v[4]), "href": f"{gal}#{v[5]}"} for k, v in info.items()}
    tab_names = [("salon", X("Salón", "Living room", "Salon")), ("cocina", X("Cocina", "Kitchen", "Cuisine")), ("dorm1", X("Dormitorio 1", "Bedroom 1", "Chambre 1")),
                 ("dorm2", X("Dormitorio 2", "Bedroom 2", "Chambre 2")), ("bano1", X("Baño 1", "Bath 1", "SdB 1")), ("bano2", X("Baño 2", "Bath 2", "SdB 2")), ("jardin", X("Jardín", "Garden", "Jardin"))]
    tabs = "".join(f'<button type="button" data-room="{k}" aria-pressed="{"true" if i == 0 else "false"}">{n}</button>' for i, (k, n) in enumerate(tab_names))
    first = info["salon"]
    items = "".join(f"<li>{x}</li>" for x in first[3])
    plan_json = json.dumps({"order": PLAN_ORDER, "rooms": data, "see": X("Ver la foto", "See the photo", "Voir la photo")}, ensure_ascii=False).replace("</", "<\\/")
    t_h = X("Recorre el plano", "Explore the floor plan", "Parcourez le plan")
    t_lead = X("Toca una estancia para ver cómo es y qué tiene.", "Tap a room to see what it looks like and what it has.", "Touchez une pièce pour la découvrir.")
    t_rooms = X("Estancias", "Rooms", "Pièces")
    t_photo = X("Ver la foto", "See the photo", "Voir la photo")
    t_prev, t_next = X("Estancia anterior", "Previous room", "Pièce précédente"), X("Estancia siguiente", "Next room", "Pièce suivante")
    t_pause = X("Pausar recorrido automático", "Pause automatic tour", "Mettre en pause la visite automatique")
    t_note = X("Esquema orientativo de la distribución, no a escala.", "Indicative layout diagram, not to scale.", "Schéma indicatif de la distribution, pas à l’échelle.")
    first_img = first[4]
    first_alt = esc(alt(first_img))
    svg = plan_svg(info)
    return f"""<section id="plano" class="section bg-2" aria-labelledby="pl-t">
  <div class="container">
    <div class="sec-head"><div><h2 id="pl-t" class="h2" data-text-effect>{t_h}</h2><p class="lead mt-s" data-reveal>{t_lead}</p></div></div>
    <div class="plan mt-l">
      <div class="plan-tabs-wrap" data-reveal><div class="plan-tabs" role="group" aria-label="{t_rooms}">{tabs}</div></div>
      <div class="plan-grid">
        <div class="plan-card" data-reveal>{svg}</div>
        <div class="plan-panel" data-reveal style="--d:.15s">
          <div class="plan-photo">
            <img class="is-on" src="/img/{first_img}-1200.webp" width="1200" height="900" alt="{first_alt}" loading="lazy" decoding="async">
            <img src="/img/{first_img}-1200.webp" width="1200" height="900" alt="" loading="lazy" decoding="async">
            <span class="plan-count" aria-hidden="true">1 / 7</span>
          </div>
          <div class="plan-info" aria-live="polite">
            <p class="ssr-k plan-k">{first[0]}</p>
            <h3 class="h3 plan-name">{first[1]}</h3>
            <p class="plan-desc">{first[2]}</p>
            <ul class="plan-list">{items}</ul>
            <a class="link-chev plan-link" href="{gal}#{first[5]}">{t_photo}</a>
          </div>
          <div class="plan-nav">
            <button type="button" class="circle-btn plan-prev" aria-label="{t_prev}">{arrow(PREV, 16)}</button>
            <button type="button" class="circle-btn plan-play" aria-pressed="false" aria-label="{t_pause}"><span class="pp" aria-hidden="true"></span></button>
            <button type="button" class="circle-btn plan-next" aria-label="{t_next}">{arrow(NEXT, 16)}</button>
            <span class="plan-bar" aria-hidden="true"><i></i></span>
          </div>
        </div>
      </div>
      <p class="f-note mt-m">{t_note} {P("plano real con medidas para sustituir este esquema")}</p>
    </div>
  </div>
  <script type="application/json" id="plan-data">{plan_json}</script>
</section>"""


def page_casa():
    steps = [
        ("salon", "salon-salida-jardin", X("Salón comedor", "Living and dining room", "Salon et salle à manger"), X("Un espacio abierto para reunirse", "An open space to get together", "Un espace ouvert pour se retrouver"),
         X("La puerta acristalada da paso directo al jardín, así que el salón y el exterior funcionan como un solo espacio.", "A glazed door leads straight into the garden, so the living room and the outdoors work as one space.", "Une porte vitrée donne directement sur le jardin : salon et extérieur ne font qu’un."),
         [X("Sofá y sillones", "Sofa and armchairs", "Canapé et fauteuils"), X("Mesa de comedor", "Dining table", "Table à manger"), X("Televisión y radio", "TV and radio", "Télévision et radio"), X("Salida directa al jardín", "Direct access to the garden", "Accès direct au jardin")]),
        ("cocina", "cocina", X("Cocina", "Kitchen", "Cuisine"), X("Todo a mano para cocinar en casa", "Everything you need to cook at home", "Tout pour cuisiner comme à la maison"),
         X("Totalmente equipada y con salida a la terraza, para sacar la comida al jardín sin dar la vuelta.", "Fully equipped and opening onto the terrace, so meals go straight out to the garden.", "Entièrement équipée et ouverte sur la terrasse, pour servir le repas au jardin sans détour."),
         [X("Horno y microondas", "Oven and microwave", "Four et micro-ondes"), X("Nevera", "Fridge", "Réfrigérateur"), X("Cafetera, tetera y tostadora", "Coffee maker, kettle and toaster", "Cafetière, bouilloire et grille-pain"), X("Lavadora", "Washing machine", "Lave-linge"), X("Utensilios de cocina", "Cookware and utensils", "Ustensiles de cuisine")]),
        ("dormitorios", "dormitorio-principal", X("Dormitorios", "Bedrooms", "Chambres"), X("Dos habitaciones para descansar", "Two bedrooms to rest in", "Deux chambres pour se reposer"),
         X("Una con cama de matrimonio y otra con dos camas individuales, con ventana hacia la ladera verde.", "One with a double bed and one with two single beds, with a window onto the green hillside.", "L’une avec un lit double, l’autre avec deux lits simples et une fenêtre sur la colline."),
         [X("Cama de matrimonio", "Double bed", "Lit double"), X("Dos camas individuales", "Two single beds", "Deux lits simples"), X("Ropa de cama incluida", "Bed linen included", "Linge de lit fourni"), X("Toallas incluidas", "Towels included", "Serviettes fournies")]),
        ("banos", "bano-banera", X("Baños", "Bathrooms", "Salles de bains"), X("Dos baños completos", "Two full bathrooms", "Deux salles de bains"),
         X("Uno con bañera y mampara, el otro con plato de ducha. Así nadie espera por la mañana.", "One with a bathtub and screen, the other with a shower. No queueing in the morning.", "L’une avec baignoire, l’autre avec douche. Personne n’attend le matin."),
         [X("Bañera con mampara", "Bathtub with screen", "Baignoire avec pare-bain"), X("Ducha con mampara", "Shower with screen", "Douche avec paroi"), X("Lavabo con mueble en ambos", "Vanity unit in both", "Meuble vasque dans les deux")]),
        ("jardin", "jardin-zona-lounge", X("Jardín y terraza", "Garden and terrace", "Jardin et terrasse"), X("El sitio favorito de la casa", "The best spot in the house", "Le coin préféré de la maison"),
         X("Césped, comedor exterior para seis y una zona de sofás junto al muro de piedra, con la ladera verde al fondo.", "Lawn, outdoor dining for six and a lounge corner by the stone wall, with the green hillside behind.", "Pelouse, table pour six et coin canapés près du mur en pierre, avec la colline verdoyante en fond."),
         [X("Comedor exterior para seis", "Outdoor dining for six", "Table extérieure pour six"), X("Zona de sofás", "Lounge area", "Coin canapés"), X("Muro de piedra con musgo", "Moss-covered stone wall", "Mur en pierre moussu"), X("Ladera verde al fondo", "Green hillside behind", "Colline verdoyante en fond")]),
    ]
    media = "".join(f'<div class="ssr-img">{pic(n, "(min-width:1068px) 55vw, 100vw")}</div>' for _, n, *_ in steps)
    prog = "".join("<span></span>" for _ in steps)
    st = "".join(f'<article class="ssr-step" id="{a}"><div class="m-img">{pic(n, "100vw")}</div><p class="ssr-k">{k}</p><h2 class="h2">{h}</h2><p>{d}</p><ul>' + "".join(f"<li>{x}</li>" for x in li) + "</ul></article>"
                 for a, n, k, h, d, li in steps)
    amen = [
        ("kitchen", X("Cocina", "Kitchen", "Cuisine"), [X("Horno", "Oven", "Four"), X("Microondas", "Microwave", "Micro-ondes"), X("Nevera", "Fridge", "Réfrigérateur"), X("Cafetera y tetera", "Coffee maker and kettle", "Cafetière et bouilloire"), X("Tostadora", "Toaster", "Grille-pain"), X("Utensilios de cocina", "Cookware", "Ustensiles")]),
        ("bed", X("Descanso", "Sleeping", "Couchage"), [X("Cama de matrimonio", "Double bed", "Lit double"), X("Dos camas individuales", "Two single beds", "Deux lits simples"), X("Ropa de cama incluida", "Bed linen included", "Linge de lit fourni"), X("Cuna: ", "Cot: ", "Lit bébé : ") + P("disponibilidad de cuna")]),
        ("bath", X("Baños", "Bathrooms", "Salles de bains"), [X("Bañera con mampara", "Bathtub with screen", "Baignoire avec pare-bain"), X("Plato de ducha", "Shower", "Douche"), X("Toallas incluidas", "Towels included", "Serviettes fournies")]),
        ("sofa", X("Salón", "Living room", "Salon"), [X("Sofá y sillones", "Sofa and armchairs", "Canapé et fauteuils"), X("Mesa de comedor", "Dining table", "Table à manger"), X("Televisión", "TV", "Télévision"), "Radio"]),
        ("garden", X("Exterior", "Outdoors", "Extérieur"), [X("Jardín con césped", "Garden with lawn", "Jardin avec pelouse"), X("Comedor exterior para seis", "Outdoor dining for six", "Table extérieure pour six"), X("Zona de sofás", "Lounge area", "Coin canapés"), X("Terraza", "Terrace", "Terrasse")]),
        ("linen", X("Hogar", "Home", "Maison"), [X("Lavadora", "Washing machine", "Lave-linge"), X("Plancha", "Iron", "Fer à repasser"), X("Wifi gratis", "Free wifi", "Wifi gratuit"), X("Calefacción: ", "Heating: ", "Chauffage : ") + P("tipo de calefacción")]),
    ]
    amen_html = "".join(f'<div class="card" data-reveal>{ic(k, 40)}<h3>{t}</h3><ul>' + "".join(f"<li>{x}</li>" for x in keep(li)) + "</ul></div>" for k, t, li in amen)
    rules = keep([("nosmoke", X("Prohibido fumar en el apartamento", "No smoking in the apartment", "Interdit de fumer dans l’appartement")),
                  ("car", X("Sin plaza de parking privada", "No private parking space", "Pas de place de parking privée")),
                  ("lang", X("Atención en español, inglés y francés", "We speak Spanish, English and French", "Accueil en espagnol, anglais et français")),
                  ("clock", X("Entrada a partir de las ", "Check-in from ", "Arrivée à partir de ") + (CONFIG["CHECKIN"] or P("hora de entrada")) + X(" · salida antes de las ", " · check-out by ", " · départ avant ") + (CONFIG["CHECKOUT"] or P("hora de salida"))),
                  ("star", X("Mascotas: ", "Pets: ", "Animaux : ") + P("si se admiten mascotas y condiciones")),
                  ("lock", X("Fianza: ", "Deposit: ", "Caution : ") + P("importe y forma de la fianza"))])
    rules_html = "".join(f'<div class="rule" data-reveal>{ic(k, 28)}<span>{t}</span></div>' for k, t in rules)
    t_lens = X("Mira los detalles", "Look closer", "Regardez de plus près")
    t_lens_p = X("Pasa el ratón por la foto, o tócala en el móvil, para ampliar.", "Hover over the photo, or tap it on mobile, to zoom in.", "Survolez la photo, ou touchez-la sur mobile, pour zoomer.")
    t_lupa = X("Lupa", "Zoom", "Loupe")
    body = f"""
<section class="phero">
  <div class="container">
    {crumbs_head(X("La casa", "The house", "La maison"))}
    <h1 class="h1" data-text-effect>{X("La casa, estancia por estancia", "The house, room by room", "La maison, pièce par pièce")}</h1>
    <p class="lead" data-reveal>{X("60 m² en una planta, con dos dormitorios, dos baños, cocina, salón y jardín.", "60 m² on one level, with two bedrooms, two bathrooms, a kitchen, a living room and a garden.", "60 m² de plain-pied : deux chambres, deux salles de bains, cuisine, salon et jardin.")}</p>
  </div>
  <div class="container mt-l"><div class="phero-media" data-clip>{pic("jardin-comedor-exterior", "(min-width:1200px) 1200px, 100vw", lazy=False, high=True)}</div></div>
</section>

<section class="section" aria-label="{X("Recorrido por las estancias", "Tour of the rooms", "Visite des pièces")}">
  <div class="container ssr">
    <div class="ssr-media" aria-hidden="true"><div class="ssr-sticky">{media}<div class="ssr-progress">{prog}</div></div></div>
    <div class="ssr-steps">{st}</div>
  </div>
</section>

<section id="equipamiento" class="section bg-2" aria-labelledby="eq-t">
  <div class="container">
    <h2 id="eq-t" class="h2" data-text-effect>{X("Equipamiento", "Amenities", "Équipements")}</h2>
    <p class="lead mt-s" data-reveal>{X("Todo lo que encontrarás al llegar, por estancias.", "Everything you’ll find when you arrive, room by room.", "Tout ce que vous trouverez à votre arrivée, pièce par pièce.")}</p>
    <div class="amen">{amen_html}</div>
  </div>
</section>

<section class="section" aria-labelledby="det-t">
  <div class="container">
    <h2 id="det-t" class="h2" data-text-effect>{t_lens}</h2>
    <p class="lead mt-s" data-reveal>{t_lens_p}</p>
    <div class="lens mt-l" data-lens="2.4" data-reveal>{pic("mesa-exterior-detalle", "(min-width:1200px) 1200px, 100vw", extra=' data-full="/img/mesa-exterior-detalle-2048.webp"')}<span class="lens-hint" aria-hidden="true">{t_lupa}</span></div>
  </div>
</section>

{plan_section()}

<section id="normas" class="section" aria-labelledby="no-t">
  <div class="container">
    <h2 id="no-t" class="h2" data-text-effect>{X("Normas de la casa", "House rules", "Règlement de la maison")}</h2>
    <div class="rules">{rules_html}</div>
    <div class="ctas mt-l" data-reveal><span data-magnetic><a href="{U("reservar")}" class="pill">{X("Consultar disponibilidad", "Check availability", "Voir les disponibilités")}</a></span><a href="{U("faq")}" class="link-chev">{X("Preguntas frecuentes", "FAQ", "Questions fréquentes")}</a></div>
  </div>
</section>"""
    title = X("La casa: 2 dormitorios, 2 baños y jardín | Villa Mercedes",
              "The House: 2 Bedrooms, 2 Bathrooms and a Garden | Villa Mercedes",
              "La maison : 2 chambres et jardin à Santoña | Villa Mercedes")
    desc = X("Salón con salida al jardín, cocina equipada, dormitorio de matrimonio y otro con dos camas, dos baños y plano interactivo del apartamento en Santoña.",
             "Living room opening onto the garden, fitted kitchen, a double and a twin bedroom, two bathrooms and an interactive floor plan of the Santoña apartment.",
             "Salon ouvert sur le jardin, cuisine équipée, chambre double et chambre à deux lits, deux salles de bains et plan interactif de l’appartement à Santoña.")
    label = X("La casa", "The house", "La maison")
    render("casa", title, desc, label,
           [("#salon", X("Salón", "Living room", "Salon")), ("#cocina", X("Cocina", "Kitchen", "Cuisine")), ("#dormitorios", X("Dormitorios", "Bedrooms", "Chambres")),
            ("#equipamiento", X("Equipamiento", "Amenities", "Équipements")), ("#plano", X("Plano", "Floor plan", "Plan")), ("#normas", X("Normas", "Rules", "Règlement"))],
           body, [("casa", label)], [rental_ld()], bookbar=True)


# ══════════════════════════════════════════════════════════════════════════
#  GALERÍA
# ══════════════════════════════════════════════════════════════════════════
def page_galeria():
    G = [("jardin-comedor-exterior", "exterior", "big"), ("salon-comedor", "salon", ""), ("cocina", "cocina", ""),
         ("dormitorio-principal", "dormitorios", "wide"), ("jardin-zona-lounge", "exterior", ""), ("bano-banera", "banos", ""),
         ("salon-salida-jardin", "salon", "big"), ("dormitorio-dos-camas", "dormitorios", ""), ("bano-ducha", "banos", ""),
         ("mesa-exterior-detalle", "exterior", "wide"), ("jardin-vista-general", "exterior", ""), ("fachada-urbanizacion", "exterior", "")]
    names = {"salon": X("Salón", "Living room", "Salon"), "cocina": X("Cocina", "Kitchen", "Cuisine"), "dormitorios": X("Dormitorios", "Bedrooms", "Chambres"),
             "banos": X("Baños", "Bathrooms", "Salles de bains"), "exterior": X("Exterior", "Outdoors", "Extérieur")}
    cats = [("all", X("Todas", "All", "Toutes"))] + list(names.items())
    f = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{t}</button>' for k, t in cats)
    enlarge = X("Ampliar", "Enlarge", "Agrandir")
    items = "".join(f'<figure class="gitem {s}" id="foto-{n}" data-cat="{c}" data-full="/img/{n}-2048.webp"><button type="button" aria-label="{enlarge}: {esc(alt(n))}">{pic(n, "(min-width:1068px) 25vw, 50vw")}</button>'
                    f'<figcaption class="dah"><span><b>{cap(n)}</b><span>{names[c]}</span></span></figcaption></figure>' for n, c, s in G)
    t_count = X("12 fotografías", "12 photos", "12 photos")
    body = f"""
<section class="phero">
  <div class="container">
    {crumbs_head(X("Galería", "Gallery", "Galerie"))}
    <h1 class="h1" data-text-effect>{X("Fotos del apartamento en Santoña", "Photos of the Santoña apartment", "Photos de l’appartement à Santoña")}</h1>
    <p class="lead" data-reveal>{X("Fotografías reales, sin retoques con IA. Filtra por estancia y pulsa una foto para verla a pantalla completa.", "Real photos, not retouched with AI. Filter by room and tap a photo to see it full screen.", "Photos réelles, sans retouche par IA. Filtrez par pièce et touchez une photo pour l’afficher en plein écran.")}</p>
  </div>
</section>
<section class="section" style="padding-top:0" aria-label="{X("Fotografías", "Photos", "Photos")}">
  <div class="container">
    <div class="center"><div class="gfilters" role="group" aria-label="{X("Filtrar por estancia", "Filter by room", "Filtrer par pièce")}">{f}</div></div>
    <div class="ggrid">{items}</div>
    <p class="gcount center" aria-live="polite">{t_count}</p>
    <div class="ctas center mt-l"><span data-magnetic><a href="{U("reservar")}" class="pill">{X("Consultar disponibilidad", "Check availability", "Voir les disponibilités")}</a></span><a href="{U("casa", anchor="plano")}" class="link-chev">{X("Ver el plano", "See the floor plan", "Voir le plan")}</a></div>
  </div>
</section>
<div class="md" role="dialog" aria-modal="true" aria-label="{X("Visor de fotografías", "Photo viewer", "Visionneuse de photos")}">
  <div class="md-back"></div>
  <div class="md-stage"><img class="md-img" alt=""></div>
  <div class="md-ui">
    <button type="button" class="circle-btn md-close" aria-label="{X("Cerrar", "Close", "Fermer")}"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
    <button type="button" class="circle-btn md-prev" aria-label="{X("Anterior", "Previous", "Précédente")}">{arrow(PREV)}</button>
    <button type="button" class="circle-btn md-next" aria-label="{X("Siguiente", "Next", "Suivante")}">{arrow(NEXT)}</button>
    <p class="md-cap" aria-live="polite"></p>
    <div class="md-thumbs"></div>
  </div>
</div>"""
    title = X("Fotos de Villa Mercedes, apartamento con jardín en Santoña",
              "Photos of Villa Mercedes, Holiday Apartment in Santoña",
              "Photos de Villa Mercedes, appartement avec jardin à Santoña")
    desc = X("12 fotografías reales del apartamento: salón, cocina, dos dormitorios, dos baños, jardín y terraza en Santoña (Cantabria).",
             "12 real photos of the apartment: living room, kitchen, two bedrooms, two bathrooms, garden and terrace in Santoña, Cantabria.",
             "12 photos réelles de l’appartement : salon, cuisine, deux chambres, deux salles de bains, jardin et terrasse à Santoña (Cantabrie).")
    label = X("Galería", "Gallery", "Galerie")
    render("galeria", title, desc, label, [(U("casa"), X("La casa", "The house", "La maison")), (U("reservar"), X("Disponibilidad", "Availability", "Disponibilités"))], body, [("galeria", label)])


# ══════════════════════════════════════════════════════════════════════════
#  GUÍA: QUÉ VER EN SANTOÑA
# ══════════════════════════════════════════════════════════════════════════
ART_SEA = '<svg viewBox="0 0 400 120" preserveAspectRatio="none"><path d="M0 70C60 55 100 85 160 72S260 50 320 62 400 58 400 58V120H0Z" fill="#b9d3dd"/><path d="M0 92C70 80 120 100 190 90S300 76 400 88V120H0Z" fill="#9cc2d1"/><circle cx="330" cy="34" r="14" fill="#f5d9a8"/></svg>'
ART_HILL = '<svg viewBox="0 0 400 120" preserveAspectRatio="none"><path d="M0 120L90 50 160 85 250 20 400 100V120Z" fill="#b8ccb2"/><path d="M0 120L120 80 220 100 330 60 400 90V120Z" fill="#9db795"/><rect x="262" y="8" width="8" height="18" fill="#fff"/><path d="M258 8h16l-8-6Z" fill="#b4553f"/></svg>'
ART_MARSH = '<svg viewBox="0 0 400 120" preserveAspectRatio="none"><rect width="400" height="120" fill="#e3ece6"/><path d="M0 80C80 70 160 95 240 82S360 70 400 76V120H0Z" fill="#c7d9d5"/><g stroke="#7f9a78" stroke-width="2"><path d="M40 90V60M48 92V66M300 86V58M308 88V64"/></g><path d="M180 50q10-8 20 0q10-8 20 0" fill="none" stroke="#55636b" stroke-width="2"/></svg>'
ART_FOOD = '<svg viewBox="0 0 400 120" preserveAspectRatio="none"><rect width="400" height="120" fill="#efe8dc"/><rect x="150" y="34" width="100" height="56" rx="8" fill="#d8c8a8"/><path d="M164 52h72M164 62h72M164 72h72" stroke="#b4553f" stroke-width="5" stroke-linecap="round"/></svg>'
ART_CITY = '<svg viewBox="0 0 400 120" preserveAspectRatio="none"><rect width="400" height="120" fill="#e6ecef"/><path d="M60 100V60h30v40M100 100V40h24v60M136 100V70h40v30M240 100V50l30-20 30 20v50M310 100V64h40v36" fill="#c4d2d9"/><path d="M0 100h400v20H0Z" fill="#a9c3cf"/></svg>'


def place(title, meta, text, query, art):
    url = "https://www.openstreetmap.org/search?query=" + query.replace(" ", "+")
    t_map = X("Ver en el mapa", "View on map", "Voir sur la carte")
    t_new = X("(se abre en otra pestaña)", "(opens in a new tab)", "(s’ouvre dans un nouvel onglet)")
    return (f'<article class="place" data-reveal><div class="place-art" aria-hidden="true">{art}</div><p class="place-meta">{meta}</p><h3>{title}</h3><p>{text}</p>'
            f'<a class="link-chev" href="{url}" target="_blank" rel="noopener">{t_map}: {esc(title)}<span class="sr-only"> {t_new}</span></a></article>')


def page_guia():
    book = U("reservar")
    secs = [
        ("playas", X("Playas", "Beaches", "Plages"), X("Playas de Santoña: Berria y San Martín", "Beaches in Santoña: Berria and San Martín", "Les plages de Santoña : Berria et San Martín"),
         X("Dos playas muy distintas a poca distancia de la casa: el gran arenal abierto al mar y la pequeña playa dentro de la bahía.",
           "Two very different beaches close to the house: a long stretch of sand open to the sea and a small beach inside the bay.",
           "Deux plages très différentes à proximité de la maison : une grande étendue de sable face à l’océan et une petite plage dans la baie."),
         place(X("Playa de Berria", "Berria beach", "Plage de Berria"), X("16 min a pie desde la casa", "16 minutes’ walk from the house", "16 min à pied de la maison"),
               X("Unos dos kilómetros de arena abierta al Cantábrico, entre el monte Buciero y el monte Brusco. Al estar abierta al mar suele tener oleaje.",
                 "About two kilometres of sand facing the Bay of Biscay, between Monte Buciero and Monte Brusco. Being open to the sea, it often has waves.",
                 "Environ deux kilomètres de sable face au golfe de Gascogne, entre le mont Buciero et le mont Brusco. Ouverte sur l’océan, elle a souvent des vagues."),
               "Playa de Berria Santoña", ART_SEA)
         + place(X("Playa de San Martín", "San Martín beach", "Plage de San Martín"), "Santoña",
                 X("Al final del paseo marítimo, junto al fuerte de San Martín y dentro de la bahía. Desde aquí sale el camino hacia el Faro del Caballo.",
                   "At the end of the seafront promenade, next to San Martín fort and inside the bay. The path to Faro del Caballo starts here.",
                   "Au bout de la promenade, près du fort de San Martín, à l’intérieur de la baie. C’est ici que commence le chemin du phare du Caballo."),
                 "Playa de San Martín Santoña", ART_SEA)),
        ("faro-del-caballo", X("Naturaleza", "Nature", "Nature"), X("Monte Buciero y el Faro del Caballo", "Monte Buciero and Faro del Caballo", "Le mont Buciero et le phare du Caballo"),
         X("El monte Buciero cierra Santoña frente al mar: una pequeña península de encinar y acantilados con varias sendas señalizadas.",
           "Monte Buciero closes off Santoña from the sea: a small headland of holm oaks and cliffs with several waymarked paths.",
           "Le mont Buciero ferme Santoña face à la mer : une petite péninsule de chênes verts et de falaises, parcourue de sentiers balisés."),
         place(X("Faro del Caballo", "Faro del Caballo lighthouse", "Phare du Caballo"), X("Monte Buciero", "Monte Buciero", "Mont Buciero"),
               X("Se baja hasta él por una escalera de 763 escalones tallada en el acantilado a finales del siglo XIX. Desde el paseo marítimo se tarda alrededor de una hora hasta el mirador y otra media hora en bajar; después hay que volver a subir. En temporada alta el acceso puede requerir reserva gratuita: consúltalo en el Ayuntamiento de Santoña antes de ir.",
                 "You reach it down a staircase of 763 steps cut into the cliff in the late 19th century. From the seafront it takes about an hour to the viewpoint and another half hour to go down, and then you have to climb back up. In high season access may require a free booking, so check with Santoña Town Council before you go.",
                 "On y descend par un escalier de 763 marches taillé dans la falaise à la fin du XIXᵉ siècle. Depuis la promenade, comptez environ une heure jusqu’au belvédère et une demi-heure pour descendre, puis il faut remonter. En haute saison, l’accès peut nécessiter une réservation gratuite : renseignez-vous auprès de la mairie de Santoña."),
               "Faro del Caballo Santoña", ART_HILL)
         + place(X("Sendas del Buciero", "Buciero trails", "Sentiers du Buciero"), X("Desde el fuerte de San Martín", "From San Martín fort", "Depuis le fort de San Martín"),
                 X("La senda al Faro del Caballo empieza junto al fuerte de San Martín y sigue el camino señalizado del monte. No es una ruta para días de lluvia o viento fuerte.",
                   "The Faro del Caballo trail starts by San Martín fort and follows the hill’s waymarked path. Avoid it on rainy or very windy days.",
                   "Le sentier du phare part du fort de San Martín et suit le chemin balisé du mont. À éviter par temps de pluie ou de vent fort."),
                 "Monte Buciero Santoña", ART_HILL)),
        ("marismas", X("Naturaleza", "Nature", "Nature"), X("Marismas de Santoña, Victoria y Joyel", "Santoña, Victoria and Joyel marshes", "Marais de Santoña, Victoria et Joyel"),
         X("Parque natural desde 2006, con unas 6.678 hectáreas. Está reconocido como humedal Ramsar y Zona de Especial Protección para las Aves.",
           "A natural park since 2006, covering about 6,678 hectares. It is a Ramsar wetland and a Special Protection Area for birds.",
           "Parc naturel depuis 2006, d’environ 6 678 hectares. Il est classé zone humide Ramsar et zone de protection spéciale pour les oiseaux."),
         place(X("Observación de aves", "Birdwatching", "Observation des oiseaux"), X("Parque natural", "Natural park", "Parc naturel"),
               X("Las marismas son una parada clave en la migración de la espátula. Lleva prismáticos y quédate en los caminos.",
                 "The marshes are a key stopover for migrating spoonbills. Bring binoculars and stay on the paths.",
                 "Les marais sont une halte essentielle pour la spatule en migration. Prenez des jumelles et restez sur les chemins."),
               "Marismas de Santoña", ART_MARSH)
         + place(X("Paseos por la marisma", "Marshland walks", "Balades dans les marais"), "Santoña",
                 X("Sendas llanas y tranquilas, aptas para ir con niños.", "Flat, quiet paths, suitable for children.", "Chemins plats et calmes, adaptés aux enfants."),
                 "Marismas Santoña Victoria Joyel", ART_MARSH)),
        ("anchoas", X("Gastronomía", "Food", "Gastronomie"), X("Anchoas de Santoña", "Santoña anchovies", "Les anchois de Santoña"),
         X("Santoña es conocida por sus conservas de anchoa del Cantábrico, curadas en salazón y fileteadas a mano.",
           "Santoña is known for its Cantabrian anchovies, salt-cured and filleted by hand.",
           "Santoña est réputée pour ses anchois du Cantabrique, affinés au sel et filetés à la main."),
         place(X("Conserveras", "Canneries", "Conserveries"), "Santoña",
               X("Varias conserveras tienen tienda propia y algunas organizan visitas. Pregunta horarios en cada una.",
                 "Several canneries have their own shop and some run tours. Check opening times with each one.",
                 "Plusieurs conserveries ont leur boutique et certaines proposent des visites. Renseignez-vous sur les horaires."),
               "conservas anchoa Santoña", ART_FOOD)),
        ("costa", X("Excursiones", "Day trips", "Excursions"), X("Costa de Cantabria: Laredo y Santander", "The Cantabrian coast: Laredo and Santander", "La côte cantabrique : Laredo et Santander"),
         X("Dos escapadas fáciles desde la casa, una de ellas cruzando la bahía en barco.", "Two easy trips from the house, one of them by boat across the bay.", "Deux escapades faciles depuis la maison, dont une en bateau à travers la baie."),
         place("Laredo", X("En barco por la bahía", "By boat across the bay", "En bateau par la baie"),
               X("Un barco de pasajeros cruza la bahía hasta El Puntal de Laredo en unos 15 minutos, sobre todo en temporada. Consulta horarios en el puerto.",
                 "A passenger boat crosses the bay to El Puntal in Laredo in about 15 minutes, mainly in season. Check times at the harbour.",
                 "Un bateau traverse la baie jusqu’à El Puntal de Laredo en 15 minutes environ, surtout en saison. Horaires au port."),
               "Puntal de Laredo", ART_SEA)
         + place("Santander", X("42 km aprox.", "approx. 42 km", "env. 42 km"),
                 X("La península de la Magdalena, las playas de El Sardinero y el Centro Botín, junto a la bahía.",
                   "La Magdalena peninsula, El Sardinero beaches and the Centro Botín on the bay.",
                   "La péninsule de la Magdalena, les plages d’El Sardinero et le Centro Botín au bord de la baie."),
                 "Santander", ART_CITY)),
        ("bilbao", X("Excursiones", "Day trips", "Excursions"), X("Excursión a Bilbao y el Museo Guggenheim", "Day trip to Bilbao and the Guggenheim Museum", "Excursion à Bilbao et au musée Guggenheim"),
         X("A una hora en coche aproximadamente, Bilbao da para un día completo.", "About an hour away by car, Bilbao is worth a full day.", "À environ une heure de route, Bilbao mérite une journée entière."),
         place(X("Museo Guggenheim Bilbao", "Guggenheim Museum Bilbao", "Musée Guggenheim Bilbao"), X("1 h en coche aprox.", "approx. 1 h by car", "env. 1 h en voiture"),
               X("El edificio de Frank Gehry, inaugurado en 1997, a orillas de la ría. Compra la entrada con antelación en temporada alta.",
                 "Frank Gehry’s building, opened in 1997, on the banks of the estuary. Book tickets ahead in high season.",
                 "Le bâtiment de Frank Gehry, inauguré en 1997, au bord de la ría. Réservez vos billets à l’avance en haute saison."),
               "Museo Guggenheim Bilbao", ART_CITY)
         + place(X("Casco Viejo", "Old Town", "Vieille ville"), "Bilbao",
                 X("Las Siete Calles, el mercado de la Ribera y los bares de pintxos.", "The Seven Streets, La Ribera market and the pintxo bars.", "Les Sept Rues, le marché de la Ribera et les bars à pintxos."),
                 "Casco Viejo Bilbao", ART_CITY)),
        ("como-llegar", X("Cómo llegar", "Getting here", "Venir"), X("Cómo llegar a Villa Mercedes", "How to get to Villa Mercedes", "Comment venir à Villa Mercedes"),
         "Barrio Piedrahita, Urbanización Villa Mercedes, 74 · 39740 Santoña, Cantabria.",
         place(X("En avión", "By plane", "En avion"), "40 km",
               X("El aeropuerto de Santander está a 40 km de la casa. Bilbao queda a una hora en coche aproximadamente.",
                 "Santander airport is 40 km from the house. Bilbao is about an hour away by car.",
                 "L’aéroport de Santander est à 40 km de la maison. Bilbao est à environ une heure de route."),
               "Aeropuerto Seve Ballesteros Santander", ART_CITY)
         + opt(place(X("En transporte público", "By public transport", "En transports en commun"), X("Autobús", "Bus", "Bus"),
                     X("Cómo llegar sin coche: ", "Getting here without a car: ", "Venir sans voiture : ") + P("líneas y horarios de autobús"), "estación de autobuses Santoña", ART_CITY))),
    ]
    out = ""
    for i, (a, k, t, d, c) in enumerate(secs):
        out += f'<section class="tb-sec" id="{a}" aria-labelledby="{a}-t"><span class="tb-dot" aria-hidden="true"></span><p class="ssr-k">{k}</p><h2 id="{a}-t" class="h2">{t}</h2><p>{d}</p><div class="places">{c}</div></section>'
        if i == 2:
            out += (f'<aside class="guide-cta" data-reveal><p><b>{X("Alójate a 16 minutos a pie de Berria.", "Stay a 16-minute walk from Berria beach.", "Logez à 16 minutes à pied de Berria.")}</b> '
                    f'{X("Villa Mercedes tiene dos dormitorios, dos baños y jardín.", "Villa Mercedes has two bedrooms, two bathrooms and a garden.", "Villa Mercedes a deux chambres, deux salles de bains et un jardin.")}</p>'
                    f'<a href="{book}" class="pill pill-sm">{X("Ver disponibilidad", "Check availability", "Voir les disponibilités")}</a></aside>')
    toc = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, _, t, _, _ in secs)
    body = f"""
<section class="phero">
  <div class="container">
    {crumbs_head(X("Qué ver en Santoña", "Things to do in Santoña", "Que faire à Santoña"))}
    <h1 class="h1" data-text-effect>{X("Qué ver en Santoña y alrededores", "Things to do in Santoña and nearby", "Que voir à Santoña et dans les environs")}</h1>
    <p class="lead" data-reveal>{X("Playas, la ruta al Faro del Caballo, las marismas, las anchoas y escapadas a Laredo, Santander y Bilbao, desde Villa Mercedes.", "Beaches, the walk to Faro del Caballo, the marshes, anchovies and trips to Laredo, Santander and Bilbao, all from Villa Mercedes.", "Plages, la randonnée du phare du Caballo, les marais, les anchois et des escapades à Laredo, Santander et Bilbao, depuis Villa Mercedes.")}</p>
  </div>
  <div class="container mt-l"><div class="phero-media" data-clip>{pic("fachada-urbanizacion", "(min-width:1200px) 1200px, 100vw", lazy=False, high=True)}</div></div>
</section>
<section class="section" aria-label="{X("Guía local", "Local guide", "Guide local")}">
  <div class="container narrow">
    <nav class="toc" aria-label="{X("En esta guía", "In this guide", "Dans ce guide")}"><p class="ssr-k">{X("En esta guía", "In this guide", "Dans ce guide")}</p><ol>{toc}</ol></nav>
    <div class="tb mt-l"><span class="tb-rail" aria-hidden="true"></span><span class="tb-beam" aria-hidden="true"></span>{out}</div>
    <div class="ctas mt-l"><span data-magnetic><a href="{book}" class="pill">{X("Reservar Villa Mercedes", "Book Villa Mercedes", "Réserver Villa Mercedes")}</a></span><a href="{U("casa")}" class="link-chev">{X("Ver la casa", "See the house", "Voir la maison")}</a></div>
    {opt('<p class="f-note mt-m">' + P("fotos propias o con licencia de cada lugar") + "</p>")}
  </div>
</section>"""
    title = X("Qué ver en Santoña: playas, Faro del Caballo y Bilbao",
              "Things to Do in Santoña, Cantabria: Beaches and Day Trips",
              "Que faire à Santoña : plages, phare du Caballo et Bilbao")
    desc = X("Guía de Santoña: playa de Berria, ruta al Faro del Caballo, marismas, anchoas y excursiones a Laredo, Santander y Bilbao con el Museo Guggenheim.",
             "Santoña guide: Berria beach, the Faro del Caballo walk, the marshes, anchovies and day trips to Laredo, Santander and Bilbao’s Guggenheim Museum.",
             "Guide de Santoña : plage de Berria, randonnée du phare du Caballo, marais, anchois et excursions à Laredo, Santander et au Guggenheim de Bilbao.")
    label = X("Qué ver en Santoña", "Things to do", "Que faire à Santoña")
    render("guia", title, desc, X("Qué ver", "Things to do", "À voir"),
           [("#playas", X("Playas", "Beaches", "Plages")), ("#faro-del-caballo", X("Faro", "Lighthouse", "Phare")), ("#marismas", X("Marismas", "Marshes", "Marais")),
            ("#costa", X("Costa", "Coast", "Côte")), ("#bilbao", "Bilbao"), ("#como-llegar", X("Cómo llegar", "Getting here", "Venir"))],
           body, [("guia", label)], bookbar=True)


# ══════════════════════════════════════════════════════════════════════════
#  RESERVAR
# ══════════════════════════════════════════════════════════════════════════
def page_reservar():
    tl = [(X("Eliges fechas", "Pick your dates", "Choisissez vos dates"), X("Ves en el calendario las noches libres y eliges llegada y salida.", "See which nights are free on the calendar and pick check-in and check-out.", "Consultez les nuits libres sur le calendrier et choisissez vos dates.")),
          (X("Te confirmamos", "We confirm", "Nous confirmons"), X("Revisamos tu solicitud y te respondemos con la disponibilidad y el precio final, sin comisiones.", "We check your request and reply with availability and the final price, with no fees.", "Nous étudions votre demande et vous répondons avec la disponibilité et le prix final, sans frais.")),
          (X("Pagas de forma segura", "Pay securely", "Payez en toute sécurité"), X("Te indicamos por escrito cómo pagar antes de confirmar la reserva.", "We tell you in writing how to pay before confirming the booking.", "Nous vous indiquons par écrit comment payer avant de confirmer.") + " " + P("forma de pago, pago completo o depósito")),
          (X("Registro de viajeros", "Guest registration", "Enregistrement des voyageurs"), X("Antes de llegar te pedimos los datos que exige la normativa de registro de viajeros.", "Before you arrive we ask for the details required by Spain’s guest registration rules.", "Avant votre arrivée, nous vous demandons les informations exigées par la réglementation espagnole."))]
    tl_html = "".join(f'<div class="tl-item"><span class="tl-dot" aria-hidden="true"></span><h3>{t}</h3><p>{d}</p></div>' for t, d in tl)
    t_steps = [X("Fechas", "Dates", "Dates"), X("Huéspedes", "Guests", "Voyageurs"), X("Tus datos", "Your details", "Vos coordonnées"), X("Confirmar", "Confirm", "Confirmer")]
    steps_html = "".join(f'<button type="button"{" aria-current=" + chr(34) + "step" + chr(34) if i == 0 else ""}><b>{i + 1}</b>{t}</button>' for i, t in enumerate(t_steps))
    cont, back = X("Continuar", "Continue", "Continuer"), X("Atrás", "Back", "Retour")
    guests_max = X("Capacidad máxima: ", "Maximum occupancy: ", "Capacité maximale : ") + (str(CONFIG["MAX_GUESTS"]) if CONFIG["MAX_GUESTS"] else P("capacidad máxima")) + X(" personas. ", " guests. ", " personnes. ")
    body = f"""
<section class="phero">
  <div class="container">
    {crumbs_head(X("Reservar", "Book", "Réserver"))}
    <h1 class="h1" data-text-effect>{X("Reservar Villa Mercedes en Santoña", "Book Villa Mercedes in Santoña", "Réserver Villa Mercedes à Santoña")}</h1>
    <p class="lead" data-reveal>{X("Elige tus fechas y te confirmamos disponibilidad y precio. Reserva directa, sin comisiones.", "Choose your dates and we’ll confirm availability and price. Direct booking, no fees.", "Choisissez vos dates et nous confirmons disponibilité et prix. Réservation directe, sans frais.")}</p>
  </div>
</section>

<section class="section" style="padding-top:0" aria-label="{X("Reserva", "Booking", "Réservation")}">
  <div class="container bk" id="booking">
    <div>
      <nav class="steps" aria-label="{X("Pasos de la reserva", "Booking steps", "Étapes de la réservation")}">{steps_html}</nav>

      <div class="panel">
        <div class="cal-head"><h2 class="h3">{t_steps[0]}</h2><div class="cal-nav"><button type="button" class="circle-btn cal-prev" aria-label="{X("Mes anterior", "Previous month", "Mois précédent")}">{arrow(PREV)}</button><button type="button" class="circle-btn cal-next" aria-label="{X("Mes siguiente", "Next month", "Mois suivant")}">{arrow(NEXT)}</button></div></div>
        <div class="cal-months"></div>
        <p class="legend"><span id="cal-status" aria-live="polite">{X("Elige el día de llegada", "Choose your arrival date", "Choisissez la date d’arrivée")}</span>{opt("<span>" + X("Estancia mínima: ", "Minimum stay: ", "Séjour minimum : ") + P("estancia mínima por temporada") + "</span>")}</p>
        <div class="ctas mt-m"><button type="button" class="pill" data-next disabled>{cont}</button></div>
      </div>

      <div class="panel" hidden>
        <h2 class="h3">{t_steps[1]}</h2>
        <div class="counter-row" data-count="adults"><div><b>{X("Adultos", "Adults", "Adultes")}</b><small>{X("13 años o más", "Age 13 or over", "13 ans et plus")}</small></div><div class="stepper"><button type="button" class="circle-btn" aria-label="{X("Quitar adulto", "Remove adult", "Retirer un adulte")}">−</button><output aria-live="polite">2</output><button type="button" class="circle-btn" aria-label="{X("Añadir adulto", "Add adult", "Ajouter un adulte")}">+</button></div></div>
        <div class="counter-row" data-count="children"><div><b>{X("Niños", "Children", "Enfants")}</b><small>{X("De 0 a 12 años", "Age 0 to 12", "De 0 à 12 ans")}</small></div><div class="stepper"><button type="button" class="circle-btn" aria-label="{X("Quitar niño", "Remove child", "Retirer un enfant")}">−</button><output aria-live="polite">0</output><button type="button" class="circle-btn" aria-label="{X("Añadir niño", "Add child", "Ajouter un enfant")}">+</button></div></div>
        <p class="f-note mt-m">{opt(guests_max)}{X("Un dormitorio de matrimonio y otro con dos camas individuales.", "One double bedroom and one twin bedroom.", "Une chambre double et une chambre à deux lits.")}</p>
        <div class="ctas mt-m"><button type="button" class="pill pill-ghost" data-back>{back}</button><button type="button" class="pill" data-next>{cont}</button></div>
      </div>

      <div class="panel" hidden>
        <h2 class="h3">{t_steps[2]}</h2>
        <form id="guest-form" class="form mt-m" novalidate>
          <label class="f-field"><input name="name" autocomplete="name" placeholder=" " required><span>{X("Nombre y apellidos", "Full name", "Nom et prénom")}</span><em class="f-err" hidden></em></label>
          <div class="f-row f-2">
            <label class="f-field"><input name="email" type="email" autocomplete="email" placeholder=" " required><span>Email</span><em class="f-err" hidden></em></label>
            <label class="f-field"><input name="phone" type="tel" autocomplete="tel" placeholder=" " required><span>{X("Teléfono", "Phone", "Téléphone")}</span><em class="f-err" hidden></em></label>
          </div>
          <label class="f-field"><textarea name="notes" placeholder=" "></textarea><span>{X("Algo que debamos saber (opcional)", "Anything we should know (optional)", "Quelque chose à nous dire (facultatif)")}</span></label>
        </form>
        <div class="ctas mt-m"><button type="button" class="pill pill-ghost" data-back>{back}</button><button type="button" class="pill" data-next>{X("Revisar", "Review", "Vérifier")}</button></div>
      </div>

      <div class="panel" hidden>
        <h2 class="h3">{X("Revisa tu solicitud", "Review your request", "Vérifiez votre demande")}</h2>
        <ul class="dist mt-s" id="review-list"></ul>
        <label class="f-check mt-m"><input type="checkbox" id="terms" name="terms"><span>{X("He leído y acepto las", "I have read and accept the", "J’ai lu et j’accepte les")} <a href="{U("condiciones")}" target="_blank" rel="noopener">{X("condiciones de reserva", "booking terms", "conditions de réservation")}</a> {X("y la", "and the", "et la")} <a href="{U("privacidad")}" target="_blank" rel="noopener">{X("política de privacidad", "privacy policy", "politique de confidentialité")}</a>.<em class="f-err" hidden></em></span></label>
        <div class="ctas mt-m"><button type="button" class="pill pill-ghost" data-back>{back}</button><span data-magnetic><button type="button" class="pill" id="confirm">{X("Enviar solicitud", "Send request", "Envoyer la demande")}</button></span></div>
        <p class="f-note mt-s" id="confirm-status" role="status">{X("Se abrirá WhatsApp o tu correo con la solicitud preparada.", "WhatsApp or your email app will open with the request ready to send.", "WhatsApp ou votre messagerie s’ouvrira avec la demande prête à envoyer.")}</p>
      </div>
    </div>

    <aside class="summary" aria-label="{X("Resumen de la estancia", "Stay summary", "Résumé du séjour")}">
      <h2 class="h3">{X("Tu estancia", "Your stay", "Votre séjour")}</h2>
      <div class="nights"><span class="sn" id="sum-nights">0</span><span class="sub" id="sum-nights-label">{X("noches", "nights", "nuits")}</span></div>
      <ul>
        <li><span>{t_steps[0]}</span><span id="sum-dates">{X("Elige fechas", "Choose dates", "Choisissez vos dates")}</span></li>
        <li><span>{t_steps[1]}</span><span id="sum-guests">{X("2 adultos", "2 adults", "2 adultes")}</span></li>
        {opt("<li><span>" + X("Precio por noche", "Price per night", "Prix par nuit") + "</span><span>" + P("tarifas por temporada") + "</span></li>")}
        {opt("<li><span>" + X("Limpieza", "Cleaning", "Ménage") + "</span><span>" + P("importe de limpieza") + "</span></li>")}
        <li class="total"><span>Total</span><span>{X("Te lo confirmamos", "We’ll confirm it", "Nous vous le confirmons")}</span></li>
      </ul>
      <small>{X("Sin comisiones de intermediarios.", "No middleman fees.", "Sans frais d’intermédiaire.")} <a href="{U("condiciones")}">{X("Condiciones de reserva", "Booking terms", "Conditions de réservation")}</a></small>
    </aside>
  </div>
</section>

<section class="section bg-2" aria-labelledby="how-t">
  <div class="container">
    <h2 id="how-t" class="h2" data-text-effect>{X("Cómo funciona", "How it works", "Comment ça marche")}</h2>
    <div class="tl"><span class="tl-rail" aria-hidden="true"></span><span class="tl-beam" aria-hidden="true"></span>{tl_html}</div>
  </div>
</section>"""
    title = X("Reservar apartamento en Santoña sin comisiones | Villa Mercedes",
              "Book Your Holiday Apartment in Santoña Direct | Villa Mercedes",
              "Réserver votre appartement à Santoña en direct | Villa Mercedes")
    desc = X("Elige fechas y huéspedes y envía tu solicitud. Te confirmamos disponibilidad y precio de Villa Mercedes en Santoña, sin comisiones de intermediarios.",
             "Choose your dates and guests and send a request. We’ll confirm availability and price for Villa Mercedes in Santoña, with no middleman fees.",
             "Choisissez vos dates et envoyez votre demande. Nous confirmons la disponibilité et le prix de Villa Mercedes à Santoña, sans frais d’intermédiaire.")
    label = X("Reservar", "Book", "Réserver")
    render("reservar", title, desc, label, [("#booking", X("Fechas", "Dates", "Dates")), ("#how-t", X("Cómo funciona", "How it works", "Fonctionnement")), (U("condiciones"), X("Condiciones", "Terms", "Conditions"))],
           body, [("reservar", label)], cta=False)


# ══════════════════════════════════════════════════════════════════════════
#  OPINIONES
# ══════════════════════════════════════════════════════════════════════════
def page_opiniones():
    ratings = "".join(f'<option value="{n}"{" selected" if n == 9 else ""}>{n}</option>' for n in range(10, 0, -1))
    body = f"""
<section class="phero">
  <div class="container">
    {crumbs_head(X("Opiniones", "Reviews", "Avis"))}
    <h1 class="h1" data-text-effect>{X("Opiniones de huéspedes", "Guest reviews", "Avis des voyageurs")}</h1>
    <p class="lead" data-reveal>{X("Solo publicamos opiniones reales, con nombre, fecha y el permiso de quien la escribe.", "We only publish genuine reviews, with the author’s name, date and permission.", "Nous ne publions que des avis réels, avec le nom, la date et l’accord de leur auteur.")}</p>
  </div>
</section>
<section class="section" style="padding-top:0" aria-labelledby="sc-t">
  <div class="container center">
    <h2 id="sc-t" class="sr-only">{X("Puntuación", "Score", "Note")}</h2>
    <p class="score" data-reveal>{X("8,8", "8.8", "8,8")}</p>
    <p class="sub" data-reveal>{X("Puntuación de ubicación en Booking.com", "Booking.com location score", "Note d’emplacement sur Booking.com")}</p>
    <p class="f-note mt-s" data-reveal>{X("Anunciado como «Villa Mercedes - 17001».", "Listed as “Villa Mercedes - 17001”.", "Annoncé sous le nom « Villa Mercedes - 17001 ».")} {P("fecha de consulta de la puntuación")}</p>
    {opt('<div class="plan-empty mt-l"><p>' + X("Aquí aparecerán las opiniones de los huéspedes.", "Guest reviews will appear here.", "Les avis des voyageurs apparaîtront ici.") + "<br>" + P("reseñas reales con permiso del autor") + "</p></div>")}
  </div>
</section>
<section class="section bg-2" aria-labelledby="rv-t">
  <div class="container" style="max-width:820px">
    <h2 id="rv-t" class="h2" data-text-effect>{X("¿Te has alojado en Villa Mercedes?", "Have you stayed at Villa Mercedes?", "Vous avez séjourné à Villa Mercedes ?")}</h2>
    <p class="lead mt-s" data-reveal>{X("Cuéntanos qué tal fue. Si nos das permiso, la publicaremos con tu nombre.", "Tell us how it went. With your permission, we’ll publish it with your name.", "Racontez-nous votre séjour. Avec votre accord, nous le publierons avec votre nom.")}</p>
    <form class="form mt-l" data-form="review" novalidate>
      <div class="f-row f-2">
        <label class="f-field"><input name="name" autocomplete="name" placeholder=" " required><span>{X("Nombre (como quieres que aparezca)", "Name (as you’d like it shown)", "Nom (tel qu’il doit apparaître)")}</span><em class="f-err" hidden></em></label>
        <label class="f-field always"><input name="stay" type="month" placeholder=" "><span>{X("Mes de la estancia", "Month of stay", "Mois du séjour")}</span></label>
      </div>
      <label class="f-field always"><select name="rating">{ratings}</select><span>{X("Puntuación de 1 a 10", "Score from 1 to 10", "Note de 1 à 10")}</span></label>
      <label class="f-field"><textarea name="message" placeholder=" " required></textarea><span>{X("Tu opinión", "Your review", "Votre avis")}</span><em class="f-err" hidden></em></label>
      <label class="f-check"><input type="checkbox" name="consent"><span>{X("Autorizo que se publique en esta web con mi nombre y la fecha de la estancia.", "I agree to it being published on this website with my name and the date of my stay.", "J’accepte sa publication sur ce site avec mon nom et la date du séjour.")}<em class="f-err" hidden></em></span></label>
      <div class="hp-field" aria-hidden="true"><label>{X("No rellenar", "Leave blank", "Ne pas remplir")} <input name="website" tabindex="-1" autocomplete="off"></label></div>
      <div class="ctas"><span data-magnetic><button type="submit" class="pill">{X("Enviar opinión", "Send review", "Envoyer l’avis")}</button></span></div>
      <p class="f-note f-status" role="status"></p>
    </form>
  </div>
</section>"""
    title = X("Opiniones de huéspedes | Villa Mercedes, Santoña", "Guest Reviews | Villa Mercedes, Santoña", "Avis des voyageurs | Villa Mercedes, Santoña")
    desc = X("Opiniones reales de huéspedes de Villa Mercedes en Santoña y puntuación de ubicación en Booking.com. Cuéntanos tu estancia.",
             "Genuine guest reviews of Villa Mercedes in Santoña and its Booking.com location score. Tell us about your stay.",
             "Avis réels des voyageurs de Villa Mercedes à Santoña et note d’emplacement sur Booking.com. Racontez-nous votre séjour.")
    label = X("Opiniones", "Reviews", "Avis")
    render("opiniones", title, desc, label, [("#rv-t", X("Deja tu opinión", "Leave a review", "Laisser un avis"))], body, [("opiniones", label)], bookbar=True)


# ══════════════════════════════════════════════════════════════════════════
#  PREGUNTAS FRECUENTES (sin FAQPage: Google ya no muestra ese resultado enriquecido)
# ══════════════════════════════════════════════════════════════════════════
def page_faq():
    a_book = f'<a href="{U("reservar")}">{X("Reservar", "Book", "Réserver")}</a>'
    a_guide = f'<a href="{U("guia")}">{X("guía de Santoña", "Santoña guide", "guide de Santoña")}</a>'
    groups = [
        (X("La casa", "The house", "La maison"), [
            (X("¿Cuántas personas caben?", "How many people does it sleep?", "Combien de personnes peut-on loger ?"),
             X("Tiene un dormitorio con cama de matrimonio y otro con dos camas individuales. Capacidad máxima: ", "There is one double bedroom and one twin bedroom. Maximum occupancy: ", "Il y a une chambre double et une chambre à deux lits. Capacité maximale : ")
             + (str(CONFIG["MAX_GUESTS"]) if CONFIG["MAX_GUESTS"] else P("capacidad máxima")) + "."),
            (X("¿Están incluidas las toallas y la ropa de cama?", "Are towels and bed linen included?", "Le linge de lit et les serviettes sont-ils fournis ?"), X("Sí, ambas están incluidas.", "Yes, both are included.", "Oui, les deux sont fournis.")),
            (X("¿Hay wifi?", "Is there wifi?", "Y a-t-il le wifi ?"), X("Sí, el wifi es gratuito.", "Yes, wifi is free.", "Oui, le wifi est gratuit.")),
            (X("¿Hay lavadora?", "Is there a washing machine?", "Y a-t-il un lave-linge ?"), X("Sí, en la cocina.", "Yes, in the kitchen.", "Oui, dans la cuisine.")),
            (X("¿Tiene calefacción?", "Is there heating?", "Y a-t-il le chauffage ?"), P("tipo de calefacción")),
            (X("¿Hay cuna o trona para niños?", "Is there a cot or high chair?", "Y a-t-il un lit bébé ou une chaise haute ?"), P("cuna y trona")),
        ]),
        (X("Llegada y salida", "Arrival and departure", "Arrivée et départ"), [
            (X("¿A qué hora es la entrada y la salida?", "What are the check-in and check-out times?", "Quelles sont les heures d’arrivée et de départ ?"),
             X("Entrada a partir de las ", "Check-in from ", "Arrivée à partir de ") + (CONFIG["CHECKIN"] or P("hora de entrada")) + X(". Salida antes de las ", ". Check-out by ", ". Départ avant ") + (CONFIG["CHECKOUT"] or P("hora de salida")) + "."),
            (X("¿Hay aparcamiento?", "Is there parking?", "Y a-t-il un parking ?"), X("El apartamento no tiene plaza de parking privada.", "The apartment has no private parking space.", "L’appartement n’a pas de place de parking privée.")),
            (X("¿Cómo se llega en transporte público?", "Can I get there by public transport?", "Peut-on venir en transports en commun ?"), P("líneas y horarios de autobús")),
            (X("¿A qué distancia está el aeropuerto?", "How far is the airport?", "À quelle distance est l’aéroport ?"),
             X("El aeropuerto de Santander está a 40 km y la ciudad de Santander a unos 42 km. Bilbao queda a una hora en coche aproximadamente.",
               "Santander airport is 40 km away and Santander city about 42 km. Bilbao is roughly an hour by car.",
               "L’aéroport de Santander est à 40 km et la ville de Santander à environ 42 km. Bilbao est à une heure de route environ.")),
        ]),
        (X("Reserva y pago", "Booking and payment", "Réservation et paiement"), [
            (X("¿Cómo reservo?", "How do I book?", "Comment réserver ?"),
             X(f"Elige tus fechas en {a_book} y te confirmamos disponibilidad y precio. Reservar directamente no tiene comisiones de intermediarios.",
               f"Choose your dates on the {a_book} page and we’ll confirm availability and price. Booking direct has no middleman fees.",
               f"Choisissez vos dates sur la page {a_book} et nous confirmons disponibilité et prix. La réservation directe est sans frais d’intermédiaire.")),
            (X("¿Cómo se paga?", "How do I pay?", "Comment payer ?"), P("forma de pago, pago completo o depósito")),
            (X("¿Cuál es la política de cancelación?", "What is the cancellation policy?", "Quelle est la politique d’annulation ?"), P("política de cancelación")),
            (X("¿Hay fianza?", "Is there a deposit?", "Y a-t-il une caution ?"), P("importe y devolución de la fianza")),
        ]),
        (X("Normas", "House rules", "Règlement"), [
            (X("¿Se puede fumar?", "Can I smoke?", "Peut-on fumer ?"), X("No, está prohibido fumar en el apartamento.", "No, smoking is not allowed in the apartment.", "Non, il est interdit de fumer dans l’appartement.")),
            (X("¿Se admiten mascotas?", "Are pets allowed?", "Les animaux sont-ils acceptés ?"), P("mascotas")),
            (X("¿En qué idiomas atendéis?", "Which languages do you speak?", "Quelles langues parlez-vous ?"), X("En español, inglés y francés.", "Spanish, English and French.", "Espagnol, anglais et français.")),
        ]),
        (X("Entorno", "The area", "Les environs"), [
            (X("¿A qué distancia está la playa?", "How far is the beach?", "À quelle distance est la plage ?"), X("La playa de Berria está a unos 16 minutos a pie.", "Berria beach is about a 16-minute walk.", "La plage de Berria est à environ 16 minutes à pied.")),
            (X("¿Qué se puede visitar cerca?", "What is there to see nearby?", "Que visiter à proximité ?"),
             X(f"El monte Buciero y el Faro del Caballo, las marismas, las conserveras de anchoa y escapadas a Laredo, Santander o Bilbao. Lo tienes todo en la {a_guide}.",
               f"Monte Buciero and Faro del Caballo, the marshes, the anchovy canneries and trips to Laredo, Santander or Bilbao. It’s all in our {a_guide}.",
               f"Le mont Buciero et le phare du Caballo, les marais, les conserveries d’anchois et des escapades à Laredo, Santander ou Bilbao. Tout est dans notre {a_guide}.")),
        ]),
    ]
    out = ""
    for g, qs in groups:
        qs = keep(qs)
        if not qs:
            continue
        out += f'<section class="faq-group" data-reveal><h2>{g}</h2><div class="acc">' + "".join(
            f'<details><summary>{q}<span class="plus" aria-hidden="true"></span></summary><div class="a"><p>{a}</p></div></details>' for q, a in qs) + "</div></section>"
    t_search = X("Buscar en las preguntas", "Search the questions", "Rechercher dans les questions")
    t_ph = X("Busca: parking, wifi, playa…", "Search: parking, wifi, beach…", "Rechercher : parking, wifi, plage…")
    a_contact = f'<a href="{U("contacto")}">{X("escríbenos", "get in touch", "écrivez-nous")}</a>'
    body = f"""
<section class="phero">
  <div class="container">
    {crumbs_head(X("Preguntas frecuentes", "FAQ", "Questions fréquentes"))}
    <h1 class="h1" data-text-effect>{X("Preguntas frecuentes", "Frequently asked questions", "Questions fréquentes")}</h1>
    <p class="lead" data-reveal>{X("Si no encuentras tu respuesta,", "If you can’t find your answer,", "Si vous ne trouvez pas votre réponse,")} {a_contact}.</p>
    <div class="faq-search" data-reveal>{ic("search", 18)}<label class="sr-only" for="faq-q">{t_search}</label><input id="faq-q" type="search" placeholder="{t_ph}" autocomplete="off"></div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="narrow">{out}<p class="faq-empty" hidden>{X("No hay preguntas con ese texto.", "No questions match that search.", "Aucune question ne correspond.")} <a href="{U("contacto")}">{X("Pregúntanos directamente", "Ask us directly", "Posez-nous la question")}</a>.</p></div>
</section>"""
    title = X("Preguntas frecuentes | Villa Mercedes, apartamento en Santoña", "FAQ | Villa Mercedes Holiday Apartment, Santoña", "Questions fréquentes | Villa Mercedes, Santoña")
    desc = X("Wifi, ropa de cama, aparcamiento, distancia a la playa y al aeropuerto, normas y cómo reservar Villa Mercedes en Santoña.",
             "Wifi, bed linen, parking, distance to the beach and airport, house rules and how to book Villa Mercedes in Santoña.",
             "Wifi, linge, parking, distance de la plage et de l’aéroport, règlement et réservation de Villa Mercedes à Santoña.")
    label = X("Preguntas frecuentes", "FAQ", "Questions fréquentes")
    render("faq", title, desc, X("Preguntas", "FAQ", "Questions"), [(U("contacto"), X("Contacto", "Contact", "Contact"))], body, [("faq", label)], bookbar=True)


# ══════════════════════════════════════════════════════════════════════════
#  CONTACTO
# ══════════════════════════════════════════════════════════════════════════
def page_contacto():
    wa, em, tel = CONFIG["WHATSAPP"], CONFIG["EMAIL"], CONFIG["TELEFONO"]
    fast = X("La forma más rápida", "The fastest way", "Le plus rapide")
    channels = ""
    channels += (f'<a class="channel" href="https://wa.me/{wa}" target="_blank" rel="noopener">{ic("whatsapp", 40)}<span><b>WhatsApp</b><span>{fast}</span></span></a>' if wa
                 else opt(f'<div class="channel">{ic("whatsapp", 40)}<span><b>WhatsApp</b><span>{P("número de WhatsApp")}</span></span></div>'))
    channels += (f'<a class="channel" href="tel:{tel.replace(" ", "")}">{ic("chat", 40)}<span><b>{X("Teléfono", "Phone", "Téléphone")}</b><span>{esc(tel)}</span></span></a>' if tel else "")
    channels += (f'<a class="channel" href="mailto:{em}">{ic("mail", 40)}<span><b>Email</b><span>{esc(em)}</span></span></a>' if em
                 else opt(f'<div class="channel">{ic("mail", 40)}<span><b>Email</b><span>{P("email de contacto")}</span></span></div>'))
    t_map = X("Ver el mapa", "Show the map", "Afficher la carte")
    t_map_note = X("El mapa se carga desde OpenStreetMap al pulsar el botón.", "The map loads from OpenStreetMap when you press the button.", "La carte se charge depuis OpenStreetMap lorsque vous appuyez sur le bouton.")
    t_frame = X("Mapa de Santoña", "Map of Santoña", "Carte de Santoña")
    osm = "https://www.openstreetmap.org/export/embed.html?bbox=-3.50%2C43.425%2C-3.415%2C43.475&amp;layer=mapnik"
    body = f"""
<section class="phero">
  <div class="container">
    {crumbs_head(X("Contacto", "Contact", "Contact"))}
    <h1 class="h1" data-text-effect>{X("Contacto", "Contact us", "Nous contacter")}</h1>
    <p class="lead" data-reveal>{X("Te atendemos en español, inglés y francés.", "We speak Spanish, English and French.", "Nous parlons espagnol, anglais et français.")}</p>
  </div>
</section>
<section class="section bg-2" aria-label="{X("Canales de contacto", "Contact options", "Moyens de contact")}">
  <div class="container contact-grid">
    <div class="contact-side">{channels}
      <div class="card card-white" data-reveal><h2 class="h3">{X("Dirección", "Address", "Adresse")}</h2><address class="mt-s lead">Villa Mercedes<br>Barrio Piedrahita, Urbanización Villa Mercedes, 74<br>39740 Santoña, Cantabria, {X("España", "Spain", "Espagne")}</address></div>
    </div>
    <div class="card card-white" data-reveal>
      <h2 class="h3">{X("Escríbenos", "Send us a message", "Écrivez-nous")}</h2>
      <form class="form mt-m" data-form="contact" novalidate>
        <div class="f-row f-2">
          <label class="f-field"><input name="name" autocomplete="name" placeholder=" " required><span>{X("Nombre", "Name", "Nom")}</span><em class="f-err" hidden></em></label>
          <label class="f-field"><input name="email" type="email" autocomplete="email" placeholder=" " required><span>Email</span><em class="f-err" hidden></em></label>
        </div>
        <label class="f-field"><textarea name="message" placeholder=" " required></textarea><span>{X("Mensaje", "Message", "Message")}</span><em class="f-err" hidden></em></label>
        <div class="hp-field" aria-hidden="true"><label>{X("No rellenar", "Leave blank", "Ne pas remplir")} <input name="website" tabindex="-1" autocomplete="off"></label></div>
        <p class="f-note">{X("Usaremos tus datos solo para responderte.", "We’ll only use your details to reply to you.", "Vos données ne servent qu’à vous répondre.")} <a href="{U("privacidad")}">{X("Privacidad", "Privacy", "Confidentialité")}</a>.</p>
        <div class="ctas"><span data-magnetic><button type="submit" class="pill">{X("Enviar", "Send", "Envoyer")}</button></span></div>
        <p class="f-note f-status" role="status"></p>
      </form>
    </div>
  </div>
</section>
<section id="mapa" class="section" aria-labelledby="map-t">
  <div class="container">
    <h2 id="map-t" class="h2" data-text-effect>{X("Cómo encontrarnos", "How to find us", "Comment nous trouver")}</h2>
    <div class="map-frame map-facade mt-l" data-src="{osm}" data-title="{t_frame}" data-reveal>
      <div class="map-ph" aria-hidden="true">{ic("pin", 44)}</div>
      <button type="button" class="pill pill-light map-load">{t_map}</button>
      <p class="map-note">{t_map_note}</p>
    </div>
    <p class="f-note mt-s">{X("Zona aproximada. La ubicación exacta se envía con la confirmación de la reserva.", "Approximate area. The exact location is sent with your booking confirmation.", "Zone approximative. L’emplacement exact est envoyé avec la confirmation.")} <a href="{U("guia", anchor="como-llegar")}">{X("Cómo llegar", "Getting here", "Comment venir")}</a></p>
  </div>
</section>"""
    title = X("Contacto | Villa Mercedes, apartamento vacacional en Santoña", "Contact | Villa Mercedes Holiday Apartment, Santoña", "Contact | Villa Mercedes, location de vacances à Santoña")
    desc = X("Escríbenos para reservar o resolver dudas sobre Villa Mercedes. Barrio Piedrahita, 74, Santoña (Cantabria). Atención en español, inglés y francés.",
             "Get in touch to book or ask about Villa Mercedes. Barrio Piedrahita 74, Santoña, Cantabria. We speak Spanish, English and French.",
             "Écrivez-nous pour réserver ou poser vos questions sur Villa Mercedes. Barrio Piedrahita 74, Santoña (Cantabrie). Espagnol, anglais et français.")
    label = X("Contacto", "Contact", "Contact")
    render("contacto", title, desc, label, [("#mapa", X("Mapa", "Map", "Carte")), (U("faq"), X("Preguntas", "FAQ", "Questions"))], body, [("contacto", label)])


# ══════════════════════════════════════════════════════════════════════════
#  LEGALES (plantillas: revisar con un profesional antes de publicar)
# ══════════════════════════════════════════════════════════════════════════
def legal_page(key, title, h1, sections, crumbs=None):
    notice = opt('<p class="notice">' + P("plantilla legal pendiente de revisión por un profesional") + "</p>")
    secs = ""
    for h, items in sections:
        items = keep(items)
        if items:
            secs += f"<h2>{h}</h2><ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
    body = f"""
<section class="phero phero-left">
  <div class="narrow">
    {crumbs_head(h1)}
    <h1 class="h1">{h1}</h1>
    {notice}
  </div>
</section>
<section class="section legal" style="padding-top:0"><div class="narrow">{secs}</div></section>"""
    desc = X(f"{h1} de Villa Mercedes, apartamento vacacional en Santoña (Cantabria).", f"{h1} for Villa Mercedes, holiday apartment in Santoña, Cantabria.", f"{h1} de Villa Mercedes, appartement de vacances à Santoña (Cantabrie).")
    render(key, f"{title} | Villa Mercedes", desc, h1, [], body, crumbs or [(key, h1)])


def page_condiciones():
    reg = esc(CONFIG["REGISTRO_TURISTICO"]) or P("número de registro turístico")
    nrua = esc(CONFIG["NRUA"]) or P("NRUA")
    h1 = X("Condiciones de reserva", "Booking terms", "Conditions de réservation")
    legal_page("condiciones", h1, h1, [
        (X("Reserva y pago", "Booking and payment", "Réservation et paiement"), [
            X("La reserva se confirma por escrito, con el precio total, antes de cualquier pago.", "Bookings are confirmed in writing, with the total price, before any payment.", "La réservation est confirmée par écrit, avec le prix total, avant tout paiement."),
            X("Forma de pago: ", "Payment: ", "Paiement : ") + P("pago completo o depósito y plazos")]),
        (X("Estancia", "Your stay", "Séjour"), [
            X("Entrada a partir de las ", "Check-in from ", "Arrivée à partir de ") + (CONFIG["CHECKIN"] or P("hora de entrada")) + X(". Salida antes de las ", ". Check-out by ", ". Départ avant ") + (CONFIG["CHECKOUT"] or P("hora de salida")) + ".",
            X("Capacidad máxima: ", "Maximum occupancy: ", "Capacité maximale : ") + (str(CONFIG["MAX_GUESTS"]) if CONFIG["MAX_GUESTS"] else P("capacidad máxima")) + ".",
            X("Estancia mínima: ", "Minimum stay: ", "Séjour minimum : ") + P("estancia mínima por temporada")]),
        (X("Cancelación", "Cancellation", "Annulation"), [P("política de cancelación")]),
        (X("Fianza", "Deposit", "Caution"), [P("importe, cobro y devolución de la fianza")]),
        (X("Normas", "House rules", "Règlement"), [
            X("Prohibido fumar en el apartamento.", "No smoking in the apartment.", "Interdit de fumer dans l’appartement."),
            X("Mascotas: ", "Pets: ", "Animaux : ") + P("mascotas"),
            X("El apartamento no tiene plaza de parking privada.", "The apartment has no private parking space.", "L’appartement n’a pas de place de parking privée.")]),
        (X("Registro de viajeros", "Guest registration", "Enregistrement des voyageurs"), [
            X("Antes de la llegada se solicitarán los datos de los viajeros que exige la normativa española (Real Decreto 933/2021).", "Before arrival we will ask for the guest details required by Spanish law (Royal Decree 933/2021).", "Avant l’arrivée, nous demanderons les informations exigées par la loi espagnole (décret royal 933/2021).")]),
        (X("Datos del alojamiento", "Property details", "Informations sur le logement"), [
            X("N.º de inscripción en el Registro General de Empresas Turísticas de Cantabria: ", "Cantabria Tourism Register number: ", "N° d’inscription au registre du tourisme de Cantabrie : ") + reg + ".",
            "NRUA: " + nrua + "."]),
    ], crumbs=[("reservar", X("Reservar", "Book", "Réserver")), ("condiciones", h1)])


def page_aviso():
    h1 = X("Aviso legal", "Legal notice", "Mentions légales")
    legal_page("aviso", h1, h1, [
        (X("Titular del sitio web", "Website owner", "Éditeur du site"), [
            X("Titular: ", "Owner: ", "Titulaire : ") + P("nombre o razón social"), "NIF: " + P("NIF"),
            X("Domicilio: ", "Address: ", "Adresse : ") + P("domicilio del titular"),
            "Email: " + (esc(CONFIG["EMAIL"]) or P("email")),
            X("Registro turístico de Cantabria: ", "Cantabria Tourism Register: ", "Registre du tourisme de Cantabrie : ") + (esc(CONFIG["REGISTRO_TURISTICO"]) or P("número de registro turístico"))]),
        (X("Condiciones de uso", "Terms of use", "Conditions d’utilisation"), [
            X("Los textos y fotografías de esta web pertenecen a su titular. No se permite copiarlos sin autorización.", "The text and photos on this website belong to its owner and may not be copied without permission.", "Les textes et photos de ce site appartiennent à son éditeur et ne peuvent être copiés sans autorisation."),
            P("legislación aplicable y jurisdicción")]),
    ])


def page_privacidad():
    h1 = X("Política de privacidad", "Privacy policy", "Politique de confidentialité")
    legal_page("privacidad", X("Privacidad", "Privacy", "Confidentialité"), h1, [
        (X("Responsable", "Data controller", "Responsable du traitement"), [P("titular y datos de contacto del responsable")]),
        (X("Datos que tratamos", "Data we process", "Données traitées"), [
            X("Los que nos envías por el formulario, WhatsApp o email para consultar o reservar.", "The details you send us through the form, WhatsApp or email to ask about or book a stay.", "Celles que vous nous envoyez par le formulaire, WhatsApp ou email pour une demande ou une réservation."),
            X("Los datos de los viajeros que exige la normativa, solo si reservas.", "Guest details required by law, only if you book.", "Les informations voyageurs exigées par la loi, uniquement en cas de réservation.")]),
        (X("Finalidad y base jurídica", "Purpose and legal basis", "Finalité et base juridique"), [
            X("Responder a tu consulta y gestionar tu reserva: medidas precontractuales y ejecución del contrato (RGPD, art. 6.1.b).", "Answering your enquiry and managing your booking: pre-contractual steps and performance of a contract (GDPR, Art. 6(1)(b)).", "Répondre à votre demande et gérer votre réservation : mesures précontractuelles et exécution du contrat (RGPD, art. 6.1.b)."),
            X("Registro de viajeros: obligación legal (RGPD, art. 6.1.c).", "Guest registration: legal obligation (GDPR, Art. 6(1)(c)).", "Enregistrement des voyageurs : obligation légale (RGPD, art. 6.1.c).")]),
        (X("Conservación y derechos", "Retention and your rights", "Conservation et droits"), [
            P("plazos de conservación"),
            X("Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad, y reclamar ante la Agencia Española de Protección de Datos.", "You may exercise your rights of access, rectification, erasure, objection, restriction and portability, and complain to the Spanish Data Protection Agency (AEPD).", "Vous pouvez exercer vos droits d’accès, de rectification, d’effacement, d’opposition, de limitation et de portabilité, et saisir l’Agence espagnole de protection des données (AEPD).")]),
    ])


def page_cookies():
    h1 = X("Política de cookies", "Cookie policy", "Politique de cookies")
    legal_page("cookies", "Cookies", h1, [
        (X("Cookies de esta web", "Cookies on this website", "Cookies de ce site"), [
            X("Esta web no instala cookies propias de análisis ni de publicidad.", "This website does not set its own analytics or advertising cookies.", "Ce site n’installe pas de cookies d’analyse ni de publicité."),
            X("Para evitar envíos repetidos del formulario se usa el almacenamiento de sesión del navegador, que se borra al cerrarlo.", "To prevent repeated form submissions, the browser’s session storage is used and is cleared when you close it.", "Pour éviter les envois répétés du formulaire, le stockage de session du navigateur est utilisé ; il s’efface à la fermeture.")]),
        (X("Servicios de terceros", "Third-party services", "Services tiers"), [
            X("El mapa de la página de contacto solo se carga desde OpenStreetMap si pulsas «Ver el mapa».", "The map on the contact page only loads from OpenStreetMap if you press “Show the map”.", "La carte de la page contact ne se charge depuis OpenStreetMap que si vous appuyez sur « Afficher la carte ».")]),
    ])


def page_404():
    links = "".join(f'<li><a href="{U(k)}">{t}</a></li>' for k, t in [("home", "Inicio"), ("casa", "La casa"), ("galeria", "Galería"), ("reservar", "Reservar")])
    body = f"""
<section class="nf"><div class="container">
  <p class="display" aria-hidden="true">404</p>
  <h1 class="h2 mt-s">Esta página no existe</h1>
  <p class="lead mt-s">Puede que el enlace esté mal escrito o que la página se haya movido.</p>
  <p class="lead" lang="en">This page doesn’t exist. <a href="{U("home", "en")}">Go to the English site</a>.</p>
  <p class="lead" lang="fr">Cette page n’existe pas. <a href="{U("home", "fr")}">Aller au site en français</a>.</p>
  <ul class="nf-links mt-m">{links}</ul>
</div></section>"""
    render(None, "Página no encontrada | Villa Mercedes", "La página que buscas no existe.", "Villa Mercedes", [], body, [], out="/404.html", noindex=True)
