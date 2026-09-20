#!/usr/bin/env node
/**
 * build-i18n.mjs — static language pages, sitemap and FAQ schema for booom.fit.
 *
 * WHY (2026-09-19): the site had six languages, but all of them lived in lang.js and were
 * applied in the browser. Google indexed the Slovak HTML and nothing else — no /en/, no
 * hreflang, so Czech, Polish, German, Ukrainian and English searches could never find us.
 * This script renders what setLanguage() would have rendered, once, at build time:
 *
 *   /en/index.html, /cs/, /pl/, /uk/, /de/   — index.html with every [data-i18n] element
 *                                              translated, <html lang>, title, descriptions,
 *                                              canonical, og:url/locale and the active
 *                                              language button set for that language
 *   sitemap.xml                              — every public URL with <lastmod> from git and
 *                                              hreflang alternates for the home cluster
 *   faq.html                                 — a FAQPage JSON-LD block built from its h2 + text
 *
 * RUN IT after editing index.html, lang.js, faq.html or vercel.json:   node build-i18n.mjs
 * and commit the generated files with the change — Vercel does not run it. No dependencies.
 *
 * What it does NOT do: subpages (calculators, guides) are Slovak-only content and stay so.
 * Language switching at runtime: lang.js sees data-static-lang on these pages and navigates
 * to the right URL instead of translating in place (see lang.js init).
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs'
import { execSync } from 'node:child_process'

const SITE = 'https://booom.fit'
const LANGS = ['SK', 'EN', 'CS', 'PL', 'UK', 'DE']
const HTML_LANG = { SK: 'sk', EN: 'en', CS: 'cs', PL: 'pl', UK: 'uk', DE: 'de' }
const OG_LOCALE = { SK: 'sk_SK', EN: 'en_GB', CS: 'cs_CZ', PL: 'pl_PL', UK: 'uk_UA', DE: 'de_DE' }
const TIKTOK = L => (L === 'SK' || L === 'CS') ? 'https://www.tiktok.com/@booom.fitness.app' : 'https://www.tiktok.com/@getbooom'
const urlFor = L => L === 'SK' ? `${SITE}/` : `${SITE}/${HTML_LANG[L]}/`

// Blog: one cluster per article, in Slovak / English / Czech (blog-src/make_blog.py writes the pages).
const BLOG_CLUSTERS = [
  { sk: '/blog', en: '/en/blog', cs: '/cs/blog' },
  { sk: '/blog/treningovy-dennik', en: '/en/blog/training-log', cs: '/cs/blog/treninkovy-denik' },
  { sk: '/blog/progresivne-pretazenie', en: '/en/blog/progressive-overload', cs: '/cs/blog/progresivni-pretizeni' },
  { sk: '/blog/kolko-bielkovin-denne', en: '/en/blog/how-much-protein-per-day', cs: '/cs/blog/kolik-bilkovin-denne' },
  { sk: '/blog/hyrox-priprava-8-tyzdnov', en: '/en/blog/hyrox-8-week-training-plan', cs: '/cs/blog/hyrox-priprava-8-tydnu' },
  // tools (BLOG_LOCAL only walks the first five entries)
  { sk: '/1rm-kalkulacka', en: '/en/1rm-calculator', cs: '/cs/1rm-kalkulacka' },
  { sk: '/kalorie-kalkulacka', en: '/en/calorie-calculator', cs: '/cs/kaloricka-kalkulacka' },
  { sk: '/hyrox-pacing', en: '/en/hyrox-pacing-calculator', cs: '/cs/hyrox-pacing-kalkulacka' },
  { sk: '/percento-telesneho-tuku', en: '/en/body-fat-calculator', cs: '/cs/procento-telesneho-tuku' },
]
const clusterOf = {}
for (const c of BLOG_CLUSTERS) for (const k of ['sk', 'en', 'cs']) clusterOf[c[k]] = c

// Localized calculator pages: hrefs and the plain-text labels the home page uses for them.
const TOOLS_LOCAL = {
  EN: {
    '/hyrox-pacing': { href: '/en/hyrox-pacing-calculator', labels: [['Hyrox pacing kalkulačka', 'Hyrox pacing calculator']] },
    '/1rm-kalkulacka': { href: '/en/1rm-calculator', labels: [['1RM kalkulačka', '1RM calculator']] },
    '/kalorie-kalkulacka': { href: '/en/calorie-calculator', labels: [['Kalorická kalkulačka (BMR/TDEE)', 'Calorie calculator (BMR/TDEE)'], ['Kalorická kalkulačka', 'Calorie calculator']] },
    '/percento-telesneho-tuku': { href: '/en/body-fat-calculator', labels: [['Percento telesného tuku', 'Body fat percentage']] },
  },
  CS: {
    '/hyrox-pacing': { href: '/cs/hyrox-pacing-kalkulacka', labels: [] },
    '/1rm-kalkulacka': { href: '/cs/1rm-kalkulacka', labels: [['1RM kalkulačka', 'Kalkulačka 1RM']] },
    '/kalorie-kalkulacka': { href: '/cs/kaloricka-kalkulacka', labels: [] },
    '/percento-telesneho-tuku': { href: '/cs/procento-telesneho-tuku', labels: [['Percento telesného tuku', 'Procento tělesného tuku']] },
  },
}

// Localized blog links for the en/cs home pages (nav, footer, guides grid).
const BLOG_LOCAL = {
  EN: { hub: '/en/blog', all: 'Blog: all articles', articles: [
    { href: '/en/blog/training-log', label: 'Training log: how to start' },
    { href: '/en/blog/progressive-overload', label: 'Progressive overload' },
    { href: '/en/blog/how-much-protein-per-day', label: 'How much protein per day' },
    { href: '/en/blog/hyrox-8-week-training-plan', label: 'Hyrox prep in 8 weeks' } ] },
  CS: { hub: '/cs/blog', all: 'Blog: všechny články', articles: [
    { href: '/cs/blog/treninkovy-denik', label: 'Tréninkový deník: jak začít' },
    { href: '/cs/blog/progresivni-pretizeni', label: 'Progresivní přetížení' },
    { href: '/cs/blog/kolik-bilkovin-denne', label: 'Kolik bílkovin denně' },
    { href: '/cs/blog/hyrox-priprava-8-tydnu', label: 'Hyrox příprava na 8 týdnů' } ] },
}

const read = p => readFileSync(p, 'utf8')
const eolOf = s => s.includes('\r\n') ? '\r\n' : '\n'
const write = (p, s, eol) => writeFileSync(p, s.replace(/\r?\n/g, eol))

// ── translations straight out of lang.js (the part before setLanguage is plain data) ──────
const langSrc = read('lang.js')
const dataPart = langSrc.slice(0, langSrc.indexOf('function setLanguage')).replace(/^const /gm, 'var ')
const { translations, pageTitles } = new Function(dataPart + ';return { translations, pageTitles }')()
for (const L of LANGS) {
  if (!translations[L]) throw new Error(`lang.js has no ${L}`)
  if (!translations[L].meta_description) throw new Error(`lang.js ${L} has no meta_description`)
}

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
const escAttr = s => esc(s).replace(/"/g, '&quot;')
// Same rule as setLanguage: text, except an authored <br> becomes a real line break.
const renderText = v => String(v).split('<br>').map(esc).join('<br>')

function setMeta(html, attr, name, content) {
  const re = new RegExp(`(<meta\\s+${attr}="${name}"\\s+content=")[^"]*(")`)
  if (!re.test(html)) throw new Error(`meta ${name} not found`)
  return html.replace(re, `$1${escAttr(content)}$2`)
}

function localize(src, L) {
  const t = translations[L]
  let html = src
  let skipped = []

  // Elements with data-i18n: replace the inner HTML. A non-greedy match to the first
  // closing tag of the same name is right unless the element nests the same tag — those
  // are left to the runtime and reported, so a new one never silently breaks a page.
  html = html.replace(/(<([a-zA-Z0-9]+)\b[^>]*\bdata-i18n="([^"]+)"[^>]*>)([\s\S]*?)(<\/\2>)/g, (m, open, tag, key, inner, close) => {
    if (t[key] === undefined) { skipped.push(`${key} (no ${L} string)`); return m }
    if (inner.includes(`<${tag}`)) { skipped.push(`${key} (nested <${tag}>)`); return m }
    return open + renderText(t[key]) + close
  })
  html = html.replace(/<[a-zA-Z0-9]+\b[^>]*\bdata-i18n-aria="([^"]+)"[^>]*>/g, tag => {
    const key = tag.match(/data-i18n-aria="([^"]+)"/)[1]
    if (t[key] === undefined) return tag
    return /aria-label="/.test(tag) ? tag.replace(/aria-label="[^"]*"/, `aria-label="${escAttr(t[key])}"`) : tag.replace(/>$/, ` aria-label="${escAttr(t[key])}">`)
  })
  html = html.replace(/<[a-zA-Z0-9]+\b[^>]*\bdata-i18n-placeholder="([^"]+)"[^>]*>/g, tag => {
    const key = tag.match(/data-i18n-placeholder="([^"]+)"/)[1]
    return t[key] === undefined ? tag : tag.replace(/placeholder="[^"]*"/, `placeholder="${escAttr(t[key])}"`)
  })

  // <head>
  html = html.replace(/<html lang="[a-z]+" data-lang="[A-Z]+" data-static-lang="[A-Z]+">/,
    `<html lang="${HTML_LANG[L]}" data-lang="${L}" data-static-lang="${L}">`)
  html = html.replace(/<title>[^<]*<\/title>/, `<title>${esc(pageTitles[L])}</title>`)
  html = setMeta(html, 'name', 'description', t.meta_description)
  html = setMeta(html, 'property', 'og:description', t.meta_description)
  html = setMeta(html, 'name', 'twitter:description', t.meta_description)
  html = setMeta(html, 'property', 'og:title', pageTitles[L])
  html = setMeta(html, 'name', 'twitter:title', pageTitles[L])
  html = setMeta(html, 'property', 'og:url', urlFor(L))
  html = setMeta(html, 'property', 'og:locale', OG_LOCALE[L])
  html = html.replace(/<link rel="canonical" href="[^"]*">/, `<link rel="canonical" href="${urlFor(L)}">`)
  html = html.replace(/("@type":\s*"WebSite"[\s\S]*?"inLanguage":\s*")sk(")/, `$1${HTML_LANG[L]}$2`)

  // Runtime bits setLanguage would have set.
  html = html.replace(/class="lang-btn active"/g, 'class="lang-btn"')
  html = html.replace(new RegExp(`class="lang-btn"([^>]*onclick="setLanguage\\('${L}'\\)")`, 'g'), 'class="lang-btn active"$1')
  html = html.replace(/(<span[^>]*id="langCode"[^>]*>)[^<]*(<\/span>)/, `$1${L}$2`)
  html = html.replace(/(<a\b[^>]*\bdata-tiktok\b[^>]*)href="[^"]*"/g, `$1href="${TIKTOK(L)}"`)
  html = html.replace(/(<a\b[^>]*)href="([^"]*)"([^>]*\bdata-tiktok\b)/g, `$1href="${TIKTOK(L)}"$3`)

  // Blog: the nav, footer and guides links point at the language's own blog.
  if (BLOG_LOCAL[L]) {
    const bl = BLOG_LOCAL[L]
    for (const [skHref, tl] of Object.entries(TOOLS_LOCAL[L])) {
      html = html.split(`href="${skHref}"`).join(`href="${tl.href}"`)
      for (const [skLabel, label] of tl.labels) html = html.split(`>${skLabel}<`).join(`>${label}<`)
    }
    html = html.replace(/href="\/blog"/g, `href="${bl.hub}"`)
    for (const [i, art] of bl.articles.entries()) {
      const skRe = new RegExp(`<a href="${BLOG_CLUSTERS[i + 1].sk}"><span>[^<]*</span>`)
      html = html.replace(skRe, `<a href="${art.href}"><span>${art.label}</span>`)
    }
    html = html.replace(new RegExp(`(<a href="${bl.hub}"><span>)[^<]*(</span>)`), `$1${bl.all}$2`)
  }

  // The page now lives one directory down.
  html = html.replace(/src="lang\.js"/, 'src="/lang.js"')

  return { html, skipped }
}

// ── 1. language pages ─────────────────────────────────────────────────────────────────────
const indexSrc = read('index.html')
const eol = eolOf(indexSrc)
if (!/data-static-lang="SK"/.test(indexSrc)) throw new Error('index.html must carry data-static-lang="SK" on <html>')
if (!/hreflang="x-default"/.test(indexSrc)) throw new Error('index.html must carry the hreflang block')
const dataI18nCount = (indexSrc.match(/\bdata-i18n="/g) || []).length
for (const L of LANGS.filter(l => l !== 'SK')) {
  const { html, skipped } = localize(indexSrc, L)
  const dir = HTML_LANG[L]
  if (!existsSync(dir)) mkdirSync(dir)
  write(`${dir}/index.html`, html, eol)
  const uniq = [...new Set(skipped)]
  console.log(`${dir}/index.html  ${dataI18nCount - skipped.length}/${dataI18nCount} strings${uniq.length ? `  left to runtime: ${uniq.join(', ')}` : ''}`)
}

// ── 2. sitemap.xml ────────────────────────────────────────────────────────────────────────
const lastmod = file => {
  try { return execSync(`git log -1 --format=%cs -- "${file}"`, { encoding: 'utf8' }).trim() || new Date().toISOString().slice(0, 10) }
  catch { return new Date().toISOString().slice(0, 10) }
}
const rewrites = JSON.parse(read('vercel.json')).rewrites || []
const subpages = rewrites
  .filter(r => /^\/[a-z0-9\-\/]+$/.test(r.source) && r.destination.endsWith('.html') && !/^\/(en|cs|pl|uk|de)$/.test(r.source))
  .filter(r => !['/privacy', '/terms'].includes(r.source))   // legal pages: crawlable, not worth a slot
  .map(r => ({ url: `${SITE}${r.source}`, file: r.destination.replace(/^\//, ''), priority: '0.7', changefreq: 'monthly' }))
const homeLastmod = [ 'index.html', 'lang.js' ].map(lastmod).sort().pop()
const alternates = LANGS.map(L => `    <xhtml:link rel="alternate" hreflang="${HTML_LANG[L]}" href="${urlFor(L)}"/>`)
  .concat(`    <xhtml:link rel="alternate" hreflang="x-default" href="${urlFor('SK')}"/>`).join('\n')
const homeEntries = LANGS.map(L => `  <url>
    <loc>${urlFor(L)}</loc>
    <lastmod>${homeLastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${L === 'SK' ? '1.0' : '0.9'}</priority>
${alternates}
  </url>`)
const clusterAlts = c => ['sk', 'en', 'cs'].map(k => `    <xhtml:link rel="alternate" hreflang="${k}" href="${SITE}${c[k]}"/>`)
  .concat(`    <xhtml:link rel="alternate" hreflang="x-default" href="${SITE}${c.sk}"/>`).join('\n')
const subEntries = subpages.map(p => {
  const route = p.url.replace(SITE, '')
  const c = clusterOf[route]
  return `  <url>
    <loc>${p.url}</loc>
    <lastmod>${lastmod(p.file)}</lastmod>
    <changefreq>${p.changefreq}</changefreq>
    <priority>${p.priority}</priority>${c ? '\n' + clusterAlts(c) : ''}
  </url>`
})
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${[...homeEntries, ...subEntries].join('\n')}
</urlset>
`
write('sitemap.xml', sitemap, '\n')
console.log(`sitemap.xml  ${homeEntries.length + subEntries.length} URLs`)

// ── 3. FAQPage schema on faq.html ─────────────────────────────────────────────────────────
const faqSrc = read('faq.html')
const faqEol = eolOf(faqSrc)
const stripTags = s => s.replace(/<script[\s\S]*?<\/script>/g, '').replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/\s+/g, ' ').trim()
const qa = []
const parts = faqSrc.split(/<h2 class="policy-card-title">/).slice(1)
for (const part of parts) {
  const end = part.indexOf('</h2>')
  const q = stripTags(part.slice(0, end))
  let rest = part.slice(end + 5)
  const cut = rest.search(/<h2 class="policy-card-title">|<form\b|<footer\b|<section\b/)
  if (cut > -1) rest = rest.slice(0, cut)
  const a = stripTags(rest).slice(0, 700)
  if (q && a.length > 20) qa.push({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: a } })
}
const faqLd = `<script type="application/ld+json" data-faq-schema>${JSON.stringify({ '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: qa })}</script>`
let faqOut = faqSrc.includes('data-faq-schema')
  ? faqSrc.replace(/<script type="application\/ld\+json" data-faq-schema>[\s\S]*?<\/script>/, faqLd)
  : faqSrc.replace('</head>', `  ${faqLd}\n</head>`)
write('faq.html', faqOut, faqEol)
console.log(`faq.html  FAQPage schema with ${qa.length} questions`)

// ── 4. "Ďalšie nástroje a sprievodcovia" block on every content page ──────────────────────
// Before 2026-09-20 the calculators and guides linked to one or two siblings each, so a crawler
// landing on one rarely found the rest and the pages passed almost no authority to each other.
// One shared block, injected before the <footer> and skipped for the page it sits on.
const SL_GROUPS = [
  ['Kalkulačky', [
    ['/hyrox-pacing', 'Hyrox pacing kalkulačka'],
    ['/1rm-kalkulacka', '1RM kalkulačka'],
    ['/kalorie-kalkulacka', 'Kalorická kalkulačka (BMR a TDEE)'],
    ['/percento-telesneho-tuku', 'Percento telesného tuku'],
  ]],
  ['Sprievodcovia', [
    ['/hyrox-pre-zaciatocnikov', 'Hyrox pre začiatočníkov'],
    ['/crossfit-pre-zaciatocnikov', 'CrossFit pre začiatočníkov'],
    ['/30-dni', '30-dňový tréningový plán'],
    ['/stitna-zlaza', 'Štítna žľaza a výživa'],
    ['/dieta/hashimoto', 'Hashimoto: diéta a suplementácia'],
    ['/dieta/bezlepkova', 'Bezlepková diéta'],
    ['/dieta/bezlaktozova', 'Bezlaktózová diéta'],
    ['/dieta/histaminova', 'Histamínová diéta'],
  ]],
  ['Blog', [
    ['/blog/treningovy-dennik', 'Tréningový denník: ako začať'],
    ['/blog/progresivne-pretazenie', 'Progresívne preťaženie'],
    ['/blog/kolko-bielkovin-denne', 'Koľko bielkovín denne'],
    ['/blog/hyrox-priprava-8-tyzdnov', 'Hyrox príprava na 8 týždňov'],
    ['/blog', 'Všetky články'],
  ]],
]
const SL_CSS = '.sl{max-width:820px;margin:44px auto 0;padding:24px 20px 0;border-top:1px solid #1e1e1e;font-family:Inter,-apple-system,BlinkMacSystemFont,sans-serif;text-align:left}' +
  '.sl-h{font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:#00e676;margin:0 0 16px}' +
  '.sl-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:22px 28px}' +
  '.sl-t{font-size:13px;font-weight:700;color:#e8e8e8;margin:0 0 8px}' +
  '.sl ul{list-style:none;margin:0;padding:0}.sl li{margin:0 0 6px}' +
  '.sl a{font-size:14px;color:#9aa;text-decoration:none;line-height:1.45}.sl a:hover{color:#00d4ff;text-decoration:underline}'
const slBlock = (self, groups = SL_GROUPS, heading = 'Ďalšie nástroje a sprievodcovia') => {
  const cols = groups.map(([title, items]) => {
    const lis = items.filter(([href]) => href !== self).map(([href, label]) => `<li><a href="${href}">${label}</a></li>`).join('')
    return lis ? `<div><p class="sl-t">${title}</p><ul>${lis}</ul></div>` : ''
  }).join('')
  return `<!-- site-links:start (generated by build-i18n.mjs) -->\n<aside class="sl" aria-label="${heading}" data-slot="site-links"><style>${SL_CSS}</style><p class="sl-h">${heading}</p><div class="sl-grid">${cols}</div></aside>\n<!-- site-links:end -->\n`
}
// English and Czech blog pages get their own block (the calculators exist only in Slovak).
const SL_LANG = {
  en: [[
    ['Blog', [
      ['/en/blog/training-log', 'Training log: how to start'],
      ['/en/blog/progressive-overload', 'Progressive overload'],
      ['/en/blog/how-much-protein-per-day', 'How much protein per day'],
      ['/en/blog/hyrox-8-week-training-plan', 'Hyrox prep in 8 weeks'],
      ['/en/blog', 'All articles'],
    ]],
    ['Calculators', [
      ['/en/hyrox-pacing-calculator', 'Hyrox pacing calculator'],
      ['/en/1rm-calculator', '1RM calculator'],
      ['/en/calorie-calculator', 'Calorie calculator (BMR and TDEE)'],
      ['/en/body-fat-calculator', 'Body fat calculator'],
    ]],
  ], 'More articles and tools'],
  cs: [[
    ['Blog', [
      ['/cs/blog/treninkovy-denik', 'Tréninkový deník: jak začít'],
      ['/cs/blog/progresivni-pretizeni', 'Progresivní přetížení'],
      ['/cs/blog/kolik-bilkovin-denne', 'Kolik bílkovin denně'],
      ['/cs/blog/hyrox-priprava-8-tydnu', 'Hyrox příprava na 8 týdnů'],
      ['/cs/blog', 'Všechny články'],
    ]],
    ['Kalkulačky', [
      ['/cs/hyrox-pacing-kalkulacka', 'Hyrox pacing kalkulačka'],
      ['/cs/1rm-kalkulacka', 'Kalkulačka 1RM'],
      ['/cs/kaloricka-kalkulacka', 'Kalorická kalkulačka (BMR a TDEE)'],
      ['/cs/procento-telesneho-tuku', 'Kalkulačka tělesného tuku'],
    ]],
  ], 'Další články a nástroje'],
}
const slPages = new Map()   // route -> file
for (const r of rewrites) if (/^\/[a-z0-9\-\/]+$/.test(r.source) && r.destination.endsWith('.html') && !/^\/(en|cs|pl|uk|de|privacy|terms)$/.test(r.source)) slPages.set(r.source, r.destination.replace(/^\//, ''))
let slCount = 0
for (const [route, file] of slPages) {
  if (!existsSync(file)) continue
  const src = read(file)
  const e = eolOf(src)
  const clean = src.replace(/<!-- site-links:start[\s\S]*?<!-- site-links:end -->\r?\n?/, '')
  const at = clean.indexOf('<footer')
  if (at === -1) { console.log(`site-links: no <footer> in ${file}, skipped`); continue }
  const out = clean.slice(0, at) + slBlock(route, ...(SL_LANG[route.split('/')[1]] || [])) + clean.slice(at)
  if (out !== src) write(file, out, e)
  slCount++
}
console.log(`site-links  block on ${slCount} pages`)
