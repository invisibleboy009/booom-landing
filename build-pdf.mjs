/**
 * Pre-render the four plan PDFs into assets/plany/.
 *
 * Why build time and not in the browser:
 *
 *   - window.print() cannot preselect a destination. The visitor gets their
 *     printer, and "Save as PDF" is buried in a dropdown — two extra steps for
 *     someone who arrived from an Instagram DM (owner, 2026-09-02).
 *   - jsPDF's built-in Helvetica is Latin-1 and has no Slovak diacritics at
 *     all, which is what turned "Začiatočník" into "Za iato ník".
 *
 * Chromium's own print pipeline has neither problem, and on a static site the
 * plans never change between deploys — so the PDFs are just files. One tap, no
 * library shipped to the visitor, and it works with JavaScript disabled.
 *
 * Run after changing the plans or the print stylesheet:
 *
 *   python3 build-september.py
 *   PLAYWRIGHT=<cesta>/node_modules/playwright/index.js node build-pdf.mjs
 *
 * Playwright lives in the app repo; this landing has no node_modules of its own
 * and does not need one. ESM ignores NODE_PATH, hence the explicit path.
 */
import { createServer } from 'node:http'
import { readFile, mkdir, stat } from 'node:fs/promises'
import { extname, join, normalize } from 'node:path'

// Playwright is CommonJS, so a dynamic import lands its exports under
// .default — unlike a static import, which unwraps them.
const pw = await import(process.env.PLAYWRIGHT || 'playwright')
const chromium = (pw.default || pw).chromium

const ROOT = new URL('.', import.meta.url).pathname
const PORT = 5271
const PLANY = [
  ['doma', 'zaciatocnik'],
  ['doma', 'pokrocily'],
  ['fitko', 'zaciatocnik'],
  ['fitko', 'pokrocily'],
]
const MIME = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.json': 'application/json', '.woff2': 'font/woff2', '.png': 'image/png', '.svg': 'image/svg+xml',
}

// Absolute asset paths (/assets/fonts/…) do not resolve over file://, so the
// page is served for real. Without this the PDFs come out in a fallback font.
const server = createServer(async (req, res) => {
  try {
    const rel = normalize(decodeURIComponent(req.url.split('?')[0])).replace(/^(\.\.[/\\])+/, '')
    const file = join(ROOT, rel)
    const body = await readFile(file)
    res.writeHead(200, { 'Content-Type': MIME[extname(file)] || 'application/octet-stream' })
    res.end(body)
  } catch {
    res.writeHead(404).end('nenajdene')
  }
})
await new Promise(r => server.listen(PORT, '127.0.0.1', r))

await mkdir(join(ROOT, 'assets', 'plany'), { recursive: true })
// The sandbox ships Chromium at a fixed path (PLAYWRIGHT_BROWSERS_PATH) and
// Playwright's own headless-shell download is absent, so point at it directly.
const browser = await chromium.launch({
  executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium',
})
const page = await browser.newPage()
const chyby = []
page.on('pageerror', e => chyby.push(e.message))

for (const [kde, uroven] of PLANY) {
  await page.goto(`http://127.0.0.1:${PORT}/september.html`, { waitUntil: 'networkidle' })
  await page.evaluate(() => document.fonts.ready)
  await page.click(`#kde button[data-v="${kde}"]`)
  await page.click(`#uroven button[data-v="${uroven}"]`)

  const kluc = `${kde}-${uroven}`
  const out = join(ROOT, 'assets', 'plany', `booom-30-dni-${kluc}.pdf`)
  await page.pdf({
    path: out, format: 'A4', printBackground: true,
    margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' },
  })
  const { size } = await stat(out)
  console.log(`booom-30-dni-${kluc}.pdf  ${(size / 1024).toFixed(0)} kB`)
}

await browser.close()
server.close()
if (chyby.length) { console.error('CHYBY NA STRANKE:', chyby); process.exit(1) }
console.log('hotovo')
