# Blog generator (2026-09-20). Reads blog-src/content_{sk,en,cs}.py and writes
#   blog/*.html (sk), en/blog/*.html, cs/blog/*.html  incl. hreflang alternates and a language switch.
# Usage (from anywhere):  python blog-src/make_blog.py   then   node build-i18n.mjs   and commit.
# Figures used in the articles: protein reference intake ~0.8 g/kg (EFSA), ISSN 1.4-2.0 g/kg for
# exercising people, Morton et al. 2018 (Br J Sports Med): gains plateau ~1.6 g/kg/day, upper CI 2.2.
import os, re, json, html, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(os.path.join(HERE, '..'))
SITE = 'https://booom.fit'
DATE = '2026-09-20'

def strip_tags(t):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t))).strip()

FONT = '''  <link rel="preload" href="/assets/fonts/Inter-latin.woff2" as="font" type="font/woff2" crossorigin>
  <style>
    @font-face{font-family:'Inter';font-style:normal;font-weight:100 900;font-display:swap;src:url(/assets/fonts/Inter-cyrillic.woff2) format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}
    @font-face{font-family:'Inter';font-style:normal;font-weight:100 900;font-display:swap;src:url(/assets/fonts/Inter-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
    @font-face{font-family:'Inter';font-style:normal;font-weight:100 900;font-display:swap;src:url(/assets/fonts/Inter-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
  </style>
  <script defer src="/assets/js/track.js"></script>'''

CSS = '''  <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    :root{--green:#00e676;--cyan:#00d4ff;--gold:#ffd700;--bg:#0a0a0a;--card:#111;--border:#1e1e1e;--text:#fff;--muted:#888}
    html{scroll-behavior:smooth}
    body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--text);line-height:1.75;-webkit-font-smoothing:antialiased}
    a{color:var(--cyan)}
    .wrap{max-width:760px;margin:0 auto;padding:24px 20px 80px}
    header.nav{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:8px 0 28px}
    .brand{font-size:22px;font-weight:900;letter-spacing:2px;color:var(--green);text-decoration:none;text-shadow:0 0 20px rgba(0,255,136,.5)}
    .nav-r{display:flex;align-items:center;gap:16px}
    .nav-l{font-size:14px;font-weight:600;color:#bbb;text-decoration:none}
    .nav-cta{font-size:13px;font-weight:700;color:#000;background:linear-gradient(135deg,var(--green),var(--cyan));padding:9px 16px;border-radius:10px;text-decoration:none}
    .crumb{font-size:13px;color:#9a9a9a;margin-bottom:14px}.crumb a{color:#bbb;text-decoration:underline}
    h1{font-size:clamp(28px,6vw,40px);font-weight:900;letter-spacing:-.5px;line-height:1.15;margin-bottom:14px}
    .meta{font-size:13px;color:#9a9a9a;margin-bottom:18px}
    .lead{color:#ccc;font-size:18px;margin-bottom:22px}
    .toc{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:16px 20px;margin:0 0 8px}
    .toc p{font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--green);margin-bottom:8px}
    .toc ol{margin:0 0 0 20px;color:#bbb}.toc li{margin-bottom:4px;font-size:15px}.toc a{color:#bbb;text-decoration:none}.toc a:hover{color:var(--cyan)}
    h2{font-size:24px;font-weight:800;margin:36px 0 12px;line-height:1.25;scroll-margin-top:16px}
    h3{font-size:18px;font-weight:700;margin:20px 0 6px;color:#fff}
    p{color:#bbb;margin-bottom:14px}
    ul,ol{color:#bbb;margin:0 0 14px 22px}li{margin-bottom:6px}
    strong{color:#e8e8e8}
    table{width:100%;border-collapse:collapse;margin:10px 0 16px}
    th,td{text-align:left;padding:10px 8px;border-bottom:1px solid var(--border);font-size:14px;vertical-align:top}
    th{font-size:11px;text-transform:uppercase;letter-spacing:.5px;color:var(--muted)}
    td.n,th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}td.n{font-weight:700}
    .ex{background:#111;border:1px solid #1e1e1e;border-radius:14px;padding:16px 18px;margin:14px 0}.ex p{margin-bottom:6px}.ex p:last-child{margin-bottom:0}
    .note{font-size:13px;color:#9a9a9a}
    .tw{overflow-x:auto;-webkit-overflow-scrolling:touch}
    .appcta{text-align:center;background:linear-gradient(135deg,rgba(0,230,118,.1),rgba(0,212,255,.08));border:1px solid rgba(0,230,118,.3);border-radius:18px;padding:28px 22px;margin-top:40px}
    .appcta h3{font-size:20px;font-weight:900;margin:0 0 8px}
    .appcta p{color:var(--muted);margin-bottom:16px}
    .appcta a.appcta-main{display:inline-block;background:linear-gradient(135deg,var(--green),var(--cyan));color:#000;font-weight:900;padding:14px 28px;border-radius:12px;text-decoration:none}
    .appcta .stores{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:16px}
    .appcta .stores a{display:block}.appcta .stores img{display:block;height:44px;width:auto}
    .faq h3{color:var(--green)}
    .disc{font-size:13px;color:#9a9a9a;margin-top:26px}
    .cards{display:grid;gap:14px;margin:20px 0 8px}
    .cardl{display:block;background:var(--card);border:1px solid var(--border);border-radius:16px;padding:18px 20px;text-decoration:none;transition:border-color .15s}
    .cardl:hover{border-color:rgba(0,230,118,.5)}
    .cardl h2{font-size:20px;margin:0 0 6px;color:#fff}
    .cardl p{margin:0 0 8px;font-size:15px}
    .cardl span{font-size:12px;color:#9a9a9a}
    .lsw{font-size:13px;text-align:right;margin:-14px 0 14px;color:#9a9a9a}.lsw a{color:#bbb}.lsw b{color:#fff}
    footer{text-align:center;color:#9a9a9a;font-size:13px;margin-top:40px}
    footer a{color:#bbb;text-decoration:underline}
  </style>'''

CTA_STORES = '''<div class="stores">
        <a href="https://apps.apple.com/sk/app/id6788675497" target="_blank" rel="noopener" aria-label="Stiahnuť v App Store"><img src="/assets/app-store-badge.svg" alt="Stiahnuť v App Store" width="132" height="44" loading="lazy"></a>
        <a href="https://play.google.com/store/apps/details?id=fit.booom.app" target="_blank" rel="noopener" aria-label="Získať v Google Play"><img src="/assets/google-play-badge.svg" alt="Získať v Google Play" width="149" height="44" loading="lazy"></a>
      </div>'''

def cta(h3, p):
    return '''<div class="appcta" data-slot="article-cta">
      <h3>%s</h3>
      <p>%s</p>
      <a href="https://app.booom.fit" class="appcta-main">Vyskúšať zadarmo vo webe</a>
      %s
    </div>''' % (h3, p, CTA_STORES)

HEAD_TOP = '''<!DOCTYPE html>
<html lang="sk" data-lang="SK">
<head>
  <!-- Google tag (gtag.js) -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-V29R9X94FM');
    /* gtag.js is fetched after load + idle (it cost 500-800 ms of main thread on a throttled phone) */
    (function () {
      function add() { var e = document.createElement('script'); e.async = true; e.src = 'https://www.googletagmanager.com/gtag/js?id=G-V29R9X94FM'; document.head.appendChild(e); }
      if (document.readyState === 'complete') setTimeout(add, 0);
      else window.addEventListener('load', function () { (window.requestIdleCallback || setTimeout)(add, { timeout: 2500 }); });
    }());
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">'''

FAVICON = '''  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230d0d0d'/%3E%3Ctext x='16' y='23' font-family='Arial,sans-serif' font-size='22' font-weight='900' text-anchor='middle' fill='%2300ff88'%3EB%3C/text%3E%3C/svg%3E">'''

def ld(obj):
    return '  <script type="application/ld+json">\n  ' + json.dumps(obj, ensure_ascii=False) + '\n  </script>'

PUBLISHER = {"@type": "Organization", "name": "BOOOM", "logo": {"@type": "ImageObject", "url": SITE + "/icon-512.png"}}

# ═══════════════════════════════════════ multilingual build ═════════════════════════════════════
LANGS = ['sk', 'en', 'cs']
mods = {l: importlib.import_module('content_' + l) for l in LANGS}
for l in LANGS[1:]:
    assert len(mods[l].ARTICLES) == len(mods['sk'].ARTICLES), l
    for a, b in zip(mods['sk'].ARTICLES, mods[l].ARTICLES):
        assert [s[0] for s in a['sections']] == [s[0] for s in b['sections']], (l, a['slug'])

def hub_url(l): return SITE + mods[l].PREFIX + '/blog'
def art_url(l, i): return '%s%s/blog/%s' % (SITE, mods[l].PREFIX, mods[l].ARTICLES[i]['slug'])
def home_href(l): return (mods[l].PREFIX or '') + '/'
def out_path(l, slug=None):
    d = (mods[l].PREFIX.lstrip('/') + '/blog').lstrip('/')
    return '%s/%s.html' % (d, slug) if slug else '%s/index.html' % d
OG = {l: mods[l].UI['og_locale'] for l in LANGS}

def hreflangs(urls):
    tags = ['  <link rel="alternate" hreflang="%s" href="%s">' % (l, urls[l]) for l in LANGS]
    tags.append('  <link rel="alternate" hreflang="x-default" href="%s">' % urls['sk'])
    return '\n'.join(tags)

def lang_switch(cur, urls):
    parts = []
    for l in LANGS:
        parts.append('<b>%s</b>' % l.upper() if l == cur else '<a href="%s" hreflang="%s" lang="%s">%s</a>' % (urls[l].replace(SITE, ''), l, l, l.upper()))
    return '<div class="lsw">%s</div>' % ' · '.join(parts)

def cta_l(ui, h3, p):
    return '''<div class="appcta" data-slot="article-cta">
      <h3>%s</h3>
      <p>%s</p>
      <a href="https://app.booom.fit" class="appcta-main">%s</a>
      <div class="stores">
        <a href="https://apps.apple.com/sk/app/id6788675497" target="_blank" rel="noopener" aria-label="%s"><img src="/assets/app-store-badge.svg" alt="%s" width="132" height="44" loading="lazy"></a>
        <a href="https://play.google.com/store/apps/details?id=fit.booom.app" target="_blank" rel="noopener" aria-label="%s"><img src="/assets/google-play-badge.svg" alt="%s" width="149" height="44" loading="lazy"></a>
      </div>
    </div>''' % (h3, p, ui['try_web'], ui['appstore'], ui['appstore'], ui['gplay'], ui['gplay'])

def page_head(l, title_tag, desc, kw, og_type, og_title, url, urls, extra_meta=''):
    ui = mods[l].UI
    top = HEAD_TOP.replace('<html lang="sk" data-lang="SK">', '<html lang="%s" data-lang="%s">' % (ui['html_lang'], l.upper()))
    if l in ('sk', 'cs'):
        top += '\n  <link rel="preload" href="/assets/fonts/Inter-latin-ext.woff2" as="font" type="font/woff2" crossorigin>'
    alts = ''.join('\n  <meta property="og:locale:alternate" content="%s">' % OG[o] for o in LANGS if o != l)
    q = lambda t: html.escape(t, quote=True)
    return top + '''
  <link rel="canonical" href="%(url)s">
%(hl)s
  <title>%(title_tag)s</title>
  <meta name="description" content="%(desc)s">
  <meta name="keywords" content="%(kw)s">
  <meta property="og:type" content="%(og_type)s">
  <meta property="og:site_name" content="BOOOM">
  <meta property="og:locale" content="%(loc)s">%(alts)s
  <meta property="og:title" content="%(og_title)s">
  <meta property="og:description" content="%(desc)s">
  <meta property="og:url" content="%(url)s">
  <meta property="og:image" content="https://booom.fit/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">%(extra)s
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="%(og_title)s">
  <meta name="twitter:description" content="%(desc)s">
  <meta name="twitter:image" content="https://booom.fit/assets/og-image.png">''' % dict(
        url=url, hl=hreflangs(urls), title_tag=html.escape(title_tag, quote=False), desc=q(desc), kw=q(kw),
        og_type=og_type, loc=OG[l], alts=alts, og_title=q(og_title), extra=extra_meta)

def header(l, urls):
    ui = mods[l].UI
    return '''    <header class="nav">
      <a class="brand" href="%s">BOOOM</a>
      <div class="nav-r"><a class="nav-l" href="%s/blog">%s</a><a class="nav-cta" href="https://app.booom.fit">%s</a></div>
    </header>
    %s''' % (home_href(l), mods[l].PREFIX, ui['blog'], ui['try_free'], lang_switch(l, urls))

def footer(l):
    ui = mods[l].UI
    return '''    <footer>
      <a href="%s">BOOOM</a> · Train. Track. Dominate. · <a href="/privacy">%s</a>
    </footer>''' % (home_href(l), ui['privacy'])

def build_article(l, i):
    m = mods[l]; ui = m.UI; a = m.ARTICLES[i]
    urls = {o: art_url(o, i) for o in LANGS}
    url = urls[l]
    toc = '\n'.join('        <li><a href="#%s">%s</a></li>' % (sid, t) for sid, t, _ in a['sections'])
    body = '\n\n'.join('    <h2 id="%s">%s</h2>\n%s' % (sid, t, b) for sid, t, b in a['sections'])
    body = body.replace('<table>', '<div class="tw"><table>').replace('</table>', '</table></div>')
    words = len(strip_tags(body + ' '.join(q + ' ' + x for q, x in a['faq'])).split())
    mins = max(3, round(words / 200))
    faq_html = '<div class="faq">\n      <h2 id="faq">%s</h2>\n' % ui['faq'] + '\n'.join('      <h3>%s</h3>\n      <p>%s</p>' % (q, x) for q, x in a['faq']) + '\n    </div>'
    schema = [
        {"@context": "https://schema.org", "@type": "Article", "headline": a['title'], "description": a['desc'], "image": SITE + "/assets/og-image.png",
         "datePublished": DATE, "dateModified": DATE, "inLanguage": ui['html_lang'], "author": {"@type": "Organization", "name": "BOOOM", "url": SITE + home_href(l)},
         "publisher": PUBLISHER, "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "wordCount": words},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "BOOOM", "item": SITE + home_href(l)},
            {"@type": "ListItem", "position": 2, "name": ui['blog'], "item": hub_url(l)},
            {"@type": "ListItem", "position": 3, "name": a['crumb'], "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(x)}} for q, x in a['faq']]},
    ]
    page = page_head(l, a['title_tag'], a['desc'], a['kw'], 'article', a['title'], url, urls,
                     '\n  <meta property="article:published_time" content="%s">' % DATE) + '''
%(fav)s
%(font)s
%(ld)s
%(css)s
</head>
<body>
  <main class="wrap">
%(header)s

    <div class="crumb"><a href="%(home)s">BOOOM</a> › <a href="%(prefix)s/blog">%(blog)s</a> › %(crumb)s</div>
    <h1>%(h1)s</h1>
    <p class="meta">%(updated)s %(date)s · %(mins)s %(read)s</p>
    <p class="lead">%(lead)s</p>

    <nav class="toc" aria-label="%(toc_aria)s">
      <p>%(toc_t)s</p>
      <ol>
%(toc)s
        <li><a href="#faq">%(faq_t)s</a></li>
      </ol>
    </nav>

%(body)s

    %(cta)s

    %(faq)s
    %(disc)s

%(footer)s
  </main>
</body>
</html>
''' % dict(fav=FAVICON, font=FONT, ld='\n'.join(ld(x) for x in schema), css=CSS, header=header(l, urls), home=home_href(l), prefix=m.PREFIX, blog=ui['blog'],
           crumb=a['crumb'], h1=a['h1'], updated=ui['updated'], date=ui['date_sk'], mins=mins, read=ui['read'], lead=a['lead'], toc_aria=ui['toc_aria'],
           toc_t=ui['toc'], toc=toc, faq_t=ui['faq'], body=body, cta=cta_l(ui, a['cta'][0], a['cta'][1]), faq=faq_html, disc=a.get('disc', ''), footer=footer(l))
    page = page.replace('/assets/og-image.png', '/assets/og/%s-%s.jpg' % (l, a['slug']))
    p = out_path(l, a['slug'])
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline='').write(page)
    return {'slug': a['slug'], 'title': a['h1'], 'desc': a['card'], 'mins': mins}

def build_hub(l, cards):
    m = mods[l]; ui = m.UI; h = m.HUB
    urls = {o: hub_url(o) for o in LANGS}
    cards_html = '\n'.join('      <a class="cardl" href="%s/blog/%s"><h2>%s</h2><p>%s</p><span>%s %s</span></a>' % (m.PREFIX, c['slug'], c['title'], c['desc'], c['mins'], ui['read']) for c in cards)
    schema = [
        {"@context": "https://schema.org", "@type": "Blog", "name": h['og_title'].split(' — ')[0], "url": urls[l], "inLanguage": ui['html_lang'], "publisher": PUBLISHER,
         "blogPost": [{"@type": "BlogPosting", "headline": c['title'], "url": '%s%s/blog/%s' % (SITE, m.PREFIX, c['slug']), "datePublished": DATE} for c in cards]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "BOOOM", "item": SITE + home_href(l)},
            {"@type": "ListItem", "position": 2, "name": ui['blog'], "item": urls[l]}]},
    ]
    page = page_head(l, h['title_tag'], h['desc'], h['kw'], 'website', h['og_title'], urls[l], urls) + '''
%(fav)s
%(font)s
%(ld)s
%(css)s
</head>
<body>
  <main class="wrap">
%(header)s

    <div class="crumb"><a href="%(home)s">BOOOM</a> › %(blog)s</div>
    <h1>%(h1)s</h1>
    <p class="lead">%(lead)s</p>

    <div class="cards">
%(cards)s
    </div>

    %(cta)s

%(footer)s
  </main>
</body>
</html>
''' % dict(fav=FAVICON, font=FONT, ld='\n'.join(ld(x) for x in schema), css=CSS, header=header(l, urls), home=home_href(l), blog=ui['blog'], h1=h['h1'],
           lead=h['lead'], cards=cards_html, cta=cta_l(ui, h['cta'][0], h['cta'][1]), footer=footer(l))
    page = page.replace('/assets/og-image.png', '/assets/og/%s-blog.jpg' % l)
    p = out_path(l)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline='').write(page)

for l in LANGS:
    cards = [build_article(l, i) for i in range(len(mods[l].ARTICLES))]
    build_hub(l, cards)
    print(l, [c['slug'] + ' ' + str(c['mins']) + 'min' for c in cards])

# ── manifest (read by build-i18n.mjs) + vercel rewrites ──────────────────────────────────
n_articles = len(mods['sk'].ARTICLES)
manifest = {
    'articles': [{l: {'slug': mods[l].ARTICLES[i]['slug'], 'label': mods[l].ARTICLES[i]['crumb']} for l in LANGS} for i in range(n_articles)],
    'all': {'sk': 'Všetky články', 'en': 'All articles', 'cs': 'Všechny články'},
    'guides_all': {'sk': 'Blog: všetky články', 'en': 'Blog: all articles', 'cs': 'Blog: všechny články'},
}
json.dump(manifest, open(os.path.join(HERE, 'manifest.json'), 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=2)
vj = json.load(open('vercel.json', encoding='utf-8'))
have = {r['source'] for r in vj['rewrites']}
added = 0
for l in LANGS:
    routes = [('%s/blog' % mods[l].PREFIX, '/' + out_path(l))] + [('%s/blog/%s' % (mods[l].PREFIX, a['slug']), '/' + out_path(l, a['slug'])) for a in mods[l].ARTICLES]
    for src, dst in routes:
        if src not in have:
            vj['rewrites'].append({'source': src, 'destination': dst}); added += 1
json.dump(vj, open('vercel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open('vercel.json', 'a').write('\n')
print('manifest: %d articles, %d new rewrites' % (n_articles, added))
