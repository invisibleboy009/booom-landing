#!/usr/bin/env python3
"""Generate september.html from assets/september-plany.json.

This landing has NO build step — pages are plain static HTML that Vercel serves
as-is. So the 120 day tiles are baked in here rather than assembled by JS in the
browser: the plans stay readable when JS is off or fails, which is the one thing
a campaign landing page cannot afford to get wrong.

Re-run after editing the JSON:  python3 build-september.py
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).parent
PLANY = json.loads((ROOT / 'assets' / 'september-plany.json').read_text(encoding='utf-8'))

ORDER = ['doma-zaciatocnik', 'doma-pokrocily', 'fitko-zaciatocnik', 'fitko-pokrocily']
DEFAULT = 'doma-zaciatocnik'

TYP_LABEL = {
    'silovy': 'Silový', 'kardio': 'Kardio', 'lahky': 'Ľahký',
    'volno': 'Voľno', 'test': 'Test',
}


def e(s):
    return html.escape(str(s), quote=True)


def den_tile(den, aktivny):
    return (
        f'<button type="button" class="den {den["typ"]}" data-d="{den["d"]}"'
        f' aria-expanded="{"true" if aktivny else "false"}"'
        f' aria-label="Deň {den["d"]}, {e(den["nazov"])}">{den["d"]}</button>'
    )


def plan_block(kluc, plan):
    dni = plan['dni']
    tiles = '\n          '.join(den_tile(d, d['d'] == 1) for d in dni)
    def riadok(d):
        # The type label is dropped when the day is already called that —
        # "Deň 7 — VOĽNO  Voľno" says the same thing twice.
        typ = TYP_LABEL[d['typ']]
        stitok = '' if typ.upper() == d['nazov'].upper() else f' <span class="typ">{typ}</span>'
        obsah = e(d['obsah']) if d['obsah'] else 'Voľno je súčasť plánu.'
        return f'<li><b>Deň {d["d"]} — {e(d["nazov"])}</b>{stitok}<br>{obsah}</li>'

    rows = '\n            '.join(riadok(d) for d in dni)
    active = ' is-active' if kluc == DEFAULT else ''
    return f"""      <section class="plan{active}" data-plan="{kluc}" aria-label="{e(plan['kde'])} · {e(plan['uroven'])}">
        <div class="zhrn">
          <h2>{e(plan['kde'])} · {e(plan['uroven'])}</h2>
          <p>{e(plan['popis'])}</p>
          <span class="dl">{e(plan['dlzka'].upper())}</span>
        </div>

        <div class="mriezka">
          {tiles}
        </div>

        <ol class="zoznam">
            {rows}
        </ol>
      </section>"""


d1 = PLANY[DEFAULT]['dni'][0]
plan_bloky = '\n\n'.join(plan_block(k, PLANY[k]) for k in ORDER)

# Only the day text travels to the browser as JSON — the tiles are already in
# the markup above, so this is just what the detail panel needs on a tap.
detail_data = {
    k: {str(d['d']): {'n': d['nazov'], 'o': d['obsah']} for d in p['dni']}
    for k, p in PLANY.items()
}

HTML = f"""<!DOCTYPE html>
<html lang="sk" data-lang="SK">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-V29R9X94FM"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-V29R9X94FM');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="https://booom.fit/30-dni">
  <title>30 dní s BOOOMEROM — tréningová výzva na september | BOOOM</title>
  <meta name="description" content="Štyri 30-dňové tréningové plány: doma alebo vo fitku, začiatočník alebo pokročilý. Vyber si a začni. Zadarmo, bez registrácie — od BOOOM.">
  <meta name="keywords" content="tréningový plán, 30 dní, cvičenie doma, plán do fitka, tréning pre začiatočníkov, mesačná výzva, booom">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="BOOOM">
  <meta property="og:title" content="30 dní s BOOOMEROM — tréningová výzva">
  <meta property="og:description" content="Jeden mesiac, štyri plány, žiadne výhovorky o vybavení. Vyber si, kde cvičíš a na čom si.">
  <meta property="og:url" content="https://booom.fit/30-dni">
  <meta property="og:image" content="https://booom.fit/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="30 dní s BOOOMEROM | BOOOM">
  <meta name="twitter:description" content="Štyri 30-dňové plány — doma alebo vo fitku. Vyber si a začni.">
  <meta name="twitter:image" content="https://booom.fit/assets/og-image.png">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230d0d0d'/%3E%3Ctext x='16' y='23' font-family='Arial,sans-serif' font-size='22' font-weight='900' text-anchor='middle' fill='%2339ff14'%3EB%3C/text%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "30 dní s BOOOMEROM",
    "url": "https://booom.fit/30-dni",
    "inLanguage": "sk",
    "description": "Štyri 30-dňové tréningové plány — doma alebo vo fitku, začiatočník alebo pokročilý.",
    "publisher": {{ "@type": "Organization", "name": "BOOOM", "logo": {{ "@type": "ImageObject", "url": "https://booom.fit/icon-512.png" }} }}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "BOOOM", "item": "https://booom.fit/" }},
      {{ "@type": "ListItem", "position": 2, "name": "30 dní s BOOOMEROM", "item": "https://booom.fit/30-dni" }}
    ]
  }}
  </script>
  <style>
    /* Barlow Condensed, self-hosted. The rest of the landing runs on Inter and
       keeps doing so — only the headings and day numbers are condensed, because
       that is what makes this page read as a BOOOM artefact rather than a
       generic content page. Local files, so no extra third-party request. */
    @font-face {{ font-family: 'Barlow Condensed'; font-style: normal; font-weight: 700; font-display: swap;
      src: url('/assets/fonts/BarlowCondensed-700-latin-ext.woff2') format('woff2');
      unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }}
    @font-face {{ font-family: 'Barlow Condensed'; font-style: normal; font-weight: 700; font-display: swap;
      src: url('/assets/fonts/BarlowCondensed-700-latin.woff2') format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }}
    @font-face {{ font-family: 'Barlow Condensed'; font-style: normal; font-weight: 900; font-display: swap;
      src: url('/assets/fonts/BarlowCondensed-900-latin-ext.woff2') format('woff2');
      unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }}
    @font-face {{ font-family: 'Barlow Condensed'; font-style: normal; font-weight: 900; font-display: swap;
      src: url('/assets/fonts/BarlowCondensed-900-latin.woff2') format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --ink: #070908; --panel: #101410; --panel2: #161b16; --hrana: #1f271f;
      --zelena: #39ff14; --azur: #00d4ff;
      --text: #f1f5f1; --tlm: #98a29a; --tlm2: #5f6961;
      --kond: 'Barlow Condensed', 'Inter', sans-serif;
    }}
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--ink); color: var(--text); line-height: 1.55; -webkit-font-smoothing: antialiased; }}
    a {{ color: var(--azur); }}
    .wrap {{ position: relative; z-index: 1; max-width: 980px; margin: 0 auto; padding: 24px 20px 80px; }}

    /* Ambient glow across the whole VIEWPORT, not inside the hero.
       It used to be .hero::before, and .hero clips (overflow:hidden) — so the
       radial faded out horizontally but got sliced off at the hero's top and
       right edges, leaving two hard-edged rectangles pasted on a black page.
       That is what read as "cut off" (owner, 2026-09-02). Fixed to the viewport
       it has no box to be clipped by. */
    body::before {{ content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 0;
      background: radial-gradient(46% 28% at 26% 8%, rgba(57,255,20,.17), transparent 68%),
                  radial-gradient(38% 22% at 86% 0%, rgba(0,212,255,.11), transparent 70%); }}

    header.nav {{ display: flex; align-items: center; justify-content: space-between; padding: 8px 0 20px; }}
    /* Logo + claim stacked, same as the nav on the rest of the landing. */
    .brand {{ display: flex; flex-direction: column; gap: 2px; text-decoration: none; line-height: 1.1; }}
    .brand-logo {{ font-size: 22px; font-weight: 900; letter-spacing: 2px; color: var(--zelena);
      text-shadow: 0 0 20px rgba(57,255,20,.5); }}
    .brand-claim {{ font-size: 8.5px; font-weight: 700; letter-spacing: 2.5px; color: #fff;
      text-transform: uppercase; }}
    .nav-cta {{ font-size: 13px; font-weight: 700; color: #04140a; background: var(--zelena);
      padding: 9px 16px; border-radius: 10px; text-decoration: none; }}

    .hero {{ position: relative; padding: 30px 0 10px; text-align: center; }}
    .rail {{ position: relative; display: flex; align-items: center; justify-content: center; gap: 12px;
      font-family: var(--kond); font-weight: 700; letter-spacing: .18em; font-size: 19px; }}
    .znak {{ width: 14px; height: 14px; border-radius: 4px; background: var(--zelena); flex: none; }}
    .rail em {{ font-style: normal; color: var(--tlm2); font-size: 12.5px; letter-spacing: .14em; }}
    h1 {{ position: relative; font-family: var(--kond); font-weight: 900; text-transform: uppercase;
      font-size: clamp(46px, 12vw, 104px); line-height: .88; margin: 22px 0 0; text-wrap: balance; }}
    h1 span {{ color: var(--zelena); }}
    .lead {{ position: relative; max-width: 56ch; margin: 20px auto 0; font-size: 17.5px; color: var(--tlm); }}
    .meta {{ position: relative; display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 26px; }}
    .chip {{ border: 1px solid var(--hrana); background: var(--panel); border-radius: 999px; padding: 7px 15px;
      font-family: var(--kond); font-weight: 700; letter-spacing: .12em; text-transform: uppercase;
      font-size: 13px; color: var(--tlm); }}
    .chip b {{ color: var(--zelena); font-weight: 900; }}

    .volba {{ margin-top: 40px; border-top: 1px solid var(--hrana); padding-top: 30px; }}
    .otazka {{ font-family: var(--kond); font-weight: 700; letter-spacing: .16em; text-transform: uppercase;
      font-size: 13px; color: var(--tlm2); margin: 0 0 12px; text-align: center; }}
    .prep {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 24px; }}
    .prep button {{ appearance: none; cursor: pointer; border: 1px solid var(--hrana); background: var(--panel);
      color: var(--text); border-radius: 14px; padding: 18px 16px; text-align: center; font-family: var(--kond);
      font-weight: 900; text-transform: uppercase; font-size: 27px; line-height: 1;
      transition: border-color .15s, background .15s, color .15s; }}
    .prep button small {{ display: block; margin-top: 7px; font-family: 'Inter', sans-serif; font-weight: 500;
      font-size: 13.5px; letter-spacing: 0; text-transform: none; color: var(--tlm2); }}
    .prep button:hover {{ border-color: #37473a; }}
    .prep button:focus-visible {{ outline: 2px solid var(--azur); outline-offset: 2px; }}
    .prep button[aria-pressed="true"] {{ background: var(--zelena); color: #04140a; border-color: var(--zelena); }}
    .prep button[aria-pressed="true"] small {{ color: rgba(4,20,10,.72); }}

    .zhrn {{ display: flex; flex-wrap: wrap; align-items: baseline; gap: 10px 18px; border: 1px solid var(--hrana);
      border-left: 3px solid var(--zelena); background: var(--panel); border-radius: 14px; padding: 18px 20px; }}
    .zhrn h2 {{ font-family: var(--kond); font-weight: 900; text-transform: uppercase; font-size: 29px;
      margin: 0; line-height: 1; }}
    .zhrn p {{ margin: 0; color: var(--tlm); font-size: 15px; flex: 1 1 220px; }}
    .zhrn .dl {{ font-family: var(--kond); font-weight: 900; color: var(--zelena); font-size: 20px; letter-spacing: .04em; }}

    .legenda {{ display: flex; flex-wrap: wrap; gap: 14px; margin: 22px 0 14px; font-size: 12.5px;
      color: var(--tlm2); font-family: var(--kond); letter-spacing: .12em; text-transform: uppercase; font-weight: 700; }}
    .legenda i {{ display: inline-block; width: 11px; height: 11px; border-radius: 3px; margin-right: 6px; vertical-align: -1px; }}

    .mriezka {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 8px; margin-top: 14px; }}
    .den {{ position: relative; aspect-ratio: 1; border-radius: 11px; border: 1px solid var(--hrana);
      background: var(--panel); cursor: pointer; display: flex; align-items: center; justify-content: center;
      font-family: var(--kond); font-weight: 900; font-size: 23px; font-variant-numeric: tabular-nums;
      color: var(--text); transition: transform .12s, border-color .12s; }}
    .den:hover {{ transform: translateY(-2px); }}
    .den:focus-visible {{ outline: 2px solid var(--azur); outline-offset: 2px; }}
    .den::after {{ content: ""; position: absolute; left: 8px; right: 8px; bottom: 7px; height: 3px;
      border-radius: 2px; background: currentColor; opacity: .85; }}
    .den.silovy {{ color: var(--zelena); }}
    .den.kardio {{ color: var(--azur); }}
    .den.lahky  {{ color: #7e8a80; }}
    .den.volno  {{ color: #39423b; background: #0c0f0c; }}
    .den.test   {{ color: #04140a; background: var(--zelena); border-color: var(--zelena); }}
    .den.test::after {{ background: #04140a; }}
    .den[aria-expanded="true"] {{ border-color: var(--azur); }}

    .detail {{ margin-top: 14px; border: 1px solid var(--hrana); background: var(--panel2); border-radius: 14px;
      padding: 20px 22px; min-height: 104px; }}
    .detail .hl {{ display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; }}
    .detail .cislo {{ font-family: var(--kond); font-weight: 900; font-size: 38px; line-height: 1;
      color: var(--zelena); font-variant-numeric: tabular-nums; }}
    .detail .nazov {{ font-family: var(--kond); font-weight: 900; text-transform: uppercase; font-size: 26px; line-height: 1; }}
    .detail p {{ margin: 12px 0 0; font-size: 16.5px; color: var(--text); }}
    .detail .tip {{ margin-top: 10px; font-size: 14px; color: var(--tlm2); }}

    .cta {{ margin-top: 30px; display: flex; flex-wrap: wrap; gap: 12px; align-items: center; }}
    .btn {{ appearance: none; border: 0; cursor: pointer; background: var(--zelena); color: #04140a;
      border-radius: 12px; padding: 17px 26px; font-family: var(--kond); font-weight: 900;
      text-transform: uppercase; letter-spacing: .06em; font-size: 20px; text-decoration: none;
      display: inline-block; }}
    .btn.sek {{ background: transparent; color: var(--text); border: 1px solid var(--hrana); }}
    .btn:focus-visible {{ outline: 2px solid var(--azur); outline-offset: 2px; }}
    .pozn {{ font-size: 13.5px; color: var(--tlm2); margin: 14px 0 0; max-width: 62ch; }}

    footer {{ border-top: 1px solid var(--hrana); margin-top: 44px; padding-top: 20px; display: flex;
      justify-content: space-between; gap: 16px; flex-wrap: wrap; font-family: var(--kond);
      letter-spacing: .14em; text-transform: uppercase; font-size: 12.5px; color: var(--tlm2); }}
    footer a {{ color: var(--tlm2); text-decoration: none; }}
    footer b {{ color: var(--zelena); font-size: 17px; font-weight: 900; letter-spacing: .06em; }}

    /* The day-by-day text list is the no-JS fallback. With JS it is redundant
       (the detail panel does the same job on tap), so it is hidden then. */
    .zoznam {{ list-style: none; margin: 18px 0 0; padding: 0; border-top: 1px solid var(--hrana); }}
    .zoznam li {{ padding: 12px 0; border-bottom: 1px solid var(--hrana); font-size: 15px; color: var(--tlm); }}
    .zoznam b {{ color: var(--text); font-family: var(--kond); font-weight: 900; text-transform: uppercase;
      font-size: 19px; letter-spacing: .02em; }}
    .zoznam .typ {{ font-size: 11px; text-transform: uppercase; letter-spacing: .12em; color: var(--tlm2); }}

    .plan {{ display: none; }}
    html:not(.js) .plan {{ display: block; margin-bottom: 34px; }}
    html:not(.js) .detail {{ display: none; }}
    html.js .plan.is-active {{ display: block; }}
    html.js .zoznam {{ display: none; }}

    @media (max-width: 560px) {{
      .mriezka {{ grid-template-columns: repeat(5, 1fr); }}
      .den {{ font-size: 20px; }}
      .prep button {{ font-size: 23px; }}
    }}

    /* ── TLAČ / ULOŽENIE DO PDF ─────────────────────────────────────────────
       Plán sa netlačí ako obrázok obrazovky, ale ako dokument: biely papier,
       čierny text, žiadne dlaždice a žiadna žiara. Tmavé pozadie by zožralo
       toner a farebné pruhy pri dňoch nesú informáciu, ktorú text nesie tiež.

       Prehliadač si to vykreslí vlastnými fontmi, takže diakritika sedí. Toto
       nahradilo generovanie PDF v jsPDF, ktoré vedelo iba Latin-1 a robilo z
       "Začiatočník" -> "Za iato ník" a z "kľukov" -> "k>ukov". */
    .tlac-hlavicka, .tlac-paticka {{ display: none; }}

    @media print {{
      @page {{ margin: 16mm 14mm; }}
      html, body {{ background: #fff !important; color: #000 !important; }}
      .wrap {{ max-width: none; padding: 0; }}
      header.nav, .hero, .volba, .legenda, .mriezka, .detail, .cta, .pozn, footer {{ display: none !important; }}

      .plan {{ display: none !important; }}
      html.js .plan.is-active, html:not(.js) .plan {{ display: block !important; break-after: page; }}
      html:not(.js) .plan:last-of-type {{ break-after: auto; }}

      .tlac-hlavicka {{ display: block; border-bottom: 2px solid #000; padding-bottom: 8px; margin-bottom: 16px; }}
      .tlac-hlavicka h2 {{ font-family: var(--kond); font-weight: 900; text-transform: uppercase;
        font-size: 26pt; line-height: 1; margin: 0; color: #000; }}
      .tlac-hlavicka span {{ font-size: 9pt; letter-spacing: .1em; text-transform: uppercase; color: #444; }}

      .zhrn {{ background: #fff !important; border: 0 !important; border-left: 3pt solid #000 !important;
        border-radius: 0; padding: 0 0 0 10pt; margin: 0 0 14pt; display: block; break-inside: avoid; }}
      .zhrn h2 {{ font-size: 17pt; color: #000; }}
      .zhrn p {{ color: #333; font-size: 10.5pt; margin-top: 3pt; }}
      .zhrn .dl {{ color: #000; font-size: 11pt; }}

      .zoznam {{ display: block !important; border-top: 1pt solid #000; margin: 0; }}
      .zoznam li {{ color: #222; font-size: 10.5pt; padding: 6pt 0; border-bottom: 1pt solid #ccc;
        break-inside: avoid; }}
      .zoznam b {{ color: #000; font-size: 12.5pt; }}
      .zoznam .typ {{ color: #555; }}

      .tlac-paticka {{ display: block; margin-top: 14pt; font-size: 8.5pt; color: #444; break-inside: avoid; }}
      .tlac-paticka b {{ color: #000; }}
    }}
  </style>
</head>
<body>
  <script>document.documentElement.className += ' js';</script>
  <div class="wrap">
    <!-- Viditeľné iba na papieri / v PDF. -->
    <div class="tlac-hlavicka">
      <h2>30 dní s BOOOMEROM</h2>
      <span>booom.fit &middot; Train. Track. Dominate.</span>
    </div>

    <header class="nav">
      <a class="brand" href="/" aria-label="BOOOM — domov">
        <span class="brand-logo">BOOOM</span>
        <span class="brand-claim">Train &middot; Track &middot; Dominate</span>
      </a>
      <a class="nav-cta" href="/">Stiahnuť appku</a>
    </header>

    <div class="hero">
      <div class="rail"><i class="znak"></i>BOOOM<em>// SEPTEMBER 2026</em></div>
      <h1>30 dní<br><span>s BOOOMEROM</span></h1>
      <p class="lead">Jeden mesiac, štyri plány, žiadne výhovorky o vybavení.
        Vyber si, kde cvičíš a na čom si — zvyšok je pripravený.</p>
      <div class="meta">
        <span class="chip"><b>30</b> dní</span>
        <span class="chip"><b>9</b> voľných a ľahkých dní</span>
        <span class="chip">deň 30 = <b>deň 1</b> na čas</span>
      </div>
    </div>

    <div class="volba">
      <p class="otazka" id="q-kde">Kde cvičíš?</p>
      <div class="prep" id="kde" role="group" aria-labelledby="q-kde">
        <button type="button" data-v="doma" aria-pressed="true">Doma<small>Bez vybavenia</small></button>
        <button type="button" data-v="fitko" aria-pressed="false">Fitko<small>Stroje a činky</small></button>
      </div>
      <p class="otazka" id="q-uroven">Na akej si úrovni?</p>
      <div class="prep" id="uroven" role="group" aria-labelledby="q-uroven">
        <button type="button" data-v="zaciatocnik" aria-pressed="true">Začiatočník<small>Vraciam sa alebo začínam</small></button>
        <button type="button" data-v="pokrocily" aria-pressed="false">Pokročilý<small>Trénujem pravidelne</small></button>
      </div>
    </div>

    <div class="legenda">
      <span><i style="background:#39ff14"></i>Silový</span>
      <span><i style="background:#00d4ff"></i>Kardio</span>
      <span><i style="background:#7e8a80"></i>Ľahký</span>
      <span><i style="background:#39423b"></i>Voľno</span>
      <span><i style="background:#39ff14;box-shadow:0 0 0 2px #04140a inset"></i>Test</span>
    </div>

{plan_bloky}

    <div class="detail" id="detail" aria-live="polite">
      <div class="hl"><span class="cislo">01</span><span class="nazov">{e(d1['nazov'])}</span></div>
      <p>{e(d1['obsah'])}</p>
    </div>

    <div class="cta">
      <a class="btn" id="stiahnut" download
         href="/assets/plany/booom-30-dni-doma-zaciatocnik.pdf">Stiahnuť plán (PDF)</a>
      <a class="btn sek" href="https://app.booom.fit">Otvoriť v BOOOM</a>
    </div>
    <p class="pozn">Ak ťa niečo bolí alebo máš zdravotné obmedzenie, prispôsob si cviky
      alebo sa poraď s odborníkom. Tento plán je návrh pohybu, nie zdravotná rada.</p>

    <div class="tlac-paticka">
      Ak ťa niečo bolí alebo máš zdravotné obmedzenie, prispôsob si cviky alebo sa poraď
      s odborníkom. Tento plán je návrh pohybu, nie zdravotná rada.<br>
      <b>booom.fit/30-dni</b>
    </div>

    <footer>
      <b>BOOOM.FIT</b>
      <span>Train. Track. Dominate.</span>
      <span><a href="/">Domov</a> · <a href="/privacy">Ochrana údajov</a></span>
    </footer>
  </div>

  <script>
  (function () {{
    var DNI = {json.dumps(detail_data, ensure_ascii=False, separators=(',', ':'))};
    var kde = 'doma', uroven = 'zaciatocnik', vybranyDen = 1;

    function kluc() {{ return kde + '-' + uroven; }}
    function aktivnaSekcia() {{ return document.querySelector('.plan[data-plan="' + kluc() + '"]'); }}

    function vykresliDetail() {{
      var d = DNI[kluc()][String(vybranyDen)];
      if (!d) return;
      var h = '<div class="hl"><span class="cislo">' + (vybranyDen < 10 ? '0' : '') + vybranyDen +
              '</span><span class="nazov">' + d.n + '</span></div>' +
              '<p>' + (d.o || 'Dnes nič. Voľno je súčasť plánu.') + '</p>' +
              (vybranyDen === 30 ? '<p class="tip">Porovnaj s Dňom 1. To je celá pointa.</p>' : '');
      document.getElementById('detail').innerHTML = h;
    }}

    function vykresli() {{
      var sekcie = document.querySelectorAll('.plan');
      for (var i = 0; i < sekcie.length; i++) {{
        sekcie[i].classList.toggle('is-active', sekcie[i].dataset.plan === kluc());
      }}
      var akt = aktivnaSekcia();
      if (akt) {{
        var tiles = akt.querySelectorAll('.den');
        for (var j = 0; j < tiles.length; j++) {{
          tiles[j].setAttribute('aria-expanded', String(Number(tiles[j].dataset.d) === vybranyDen));
        }}
      }}
      var odkaz = document.getElementById('stiahnut');
      odkaz.href = '/assets/plany/booom-30-dni-' + kluc() + '.pdf';
      odkaz.setAttribute('download', 'booom-30-dni-' + kluc() + '.pdf');
      vykresliDetail();
    }}

    function prepinac(id, nastav) {{
      document.getElementById(id).addEventListener('click', function (ev) {{
        var b = ev.target.closest('button');
        if (!b) return;
        var deti = this.children;
        for (var i = 0; i < deti.length; i++) deti[i].setAttribute('aria-pressed', String(deti[i] === b));
        nastav(b.dataset.v);
        vykresli();
      }});
    }}
    prepinac('kde', function (v) {{ kde = v; }});
    prepinac('uroven', function (v) {{ uroven = v; }});

    // One delegated listener for all 120 tiles.
    document.addEventListener('click', function (ev) {{
      var t = ev.target.closest('.den');
      if (!t) return;
      vybranyDen = Number(t.dataset.d);
      vykresli();
    }});

    vykresli();
  }})();
  </script>
</body>
</html>
"""

(ROOT / 'september.html').write_text(HTML, encoding='utf-8')
print(f'september.html: {len(HTML) / 1024:.0f} KB, {len(ORDER)} planov x 30 dni')
