/* track.js — conversion events for booom.fit (GA4 via the gtag snippet already on every page).
 *
 * Until 2026-09-20 the site sent page views and nothing else, so there was no way to tell how
 * many visitors tapped App Store, Google Play or "try it on the web", which page or section
 * sent them, or whether a calculator was ever used. Everything here is one delegated click
 * listener plus a few attributes — no per-page wiring, so new pages get it for free.
 *
 * Events (mark store_click, webapp_click and generate_lead as key events in GA4 Admin):
 *   store_click       { store: app_store | google_play, page, slot, lang }
 *   webapp_click      { page, slot, lang }                 app.booom.fit
 *   social_click      { network, page, slot }
 *   plan_download     { file, page }                       the 30-day PDF plans
 *   calculator_use    { tool, page }                       any [data-calc] control
 *   language_switch   { to, page }
 *   boomer_open / generate_lead  — fired from boomer-chat.js through window.boomTrack
 *
 * It also stamps UTM / store campaign parameters onto the outgoing app links at load, so the
 * app side can see which page sent a signup. The HTML keeps the clean hrefs (crawlers see those).
 */
(function () {
  'use strict';

  var path = location.pathname.replace(/\/+$/, '') || '/';
  var lang = document.documentElement.getAttribute('lang') || 'sk';
  var campaign = (path === '/' ? 'home' : path.replace(/^\//, '').replace(/\//g, '_')) || 'home';

  function send(name, params) {
    try {
      if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
    } catch (e) { /* analytics must never break a page */ }
  }
  window.boomTrack = send;

  function slotOf(el) {
    var s = el.closest('[data-slot]') || el.closest('section[id], header, nav, footer, .appcta, .hero, .fomo-band');
    if (!s) return 'page';
    return s.getAttribute('data-slot') || s.id || s.className.toString().split(' ')[0] || s.tagName.toLowerCase();
  }

  function host(href) {
    try { return new URL(href, location.href).hostname; } catch (e) { return ''; }
  }

  // ── decorate outgoing app links (UTM + store campaign tokens) ─────────────────────────────
  function decorate() {
    var links = document.querySelectorAll('a[href]');
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      var h = host(a.getAttribute('href'));
      var slot = slotOf(a);
      try {
        var u = new URL(a.href);
        if (h === 'app.booom.fit') {
          if (!u.searchParams.has('utm_source')) {
            u.searchParams.set('utm_source', 'booom.fit');
            u.searchParams.set('utm_medium', 'website');
            u.searchParams.set('utm_campaign', campaign);
            u.searchParams.set('utm_content', slot);
            a.href = u.toString();
          }
        } else if (h === 'play.google.com' && !u.searchParams.has('referrer')) {
          u.searchParams.set('referrer', 'utm_source=booom.fit&utm_medium=website&utm_campaign=' + campaign + '&utm_content=' + slot);
          a.href = u.toString();
        } else if (h === 'apps.apple.com' && !u.searchParams.has('ct')) {
          u.searchParams.set('ct', 'web_' + campaign);
          a.href = u.toString();
        }
      } catch (e) { /* malformed href — leave it */ }
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', decorate);
  else decorate();

  // ── one delegated listener ────────────────────────────────────────────────────────────────
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (!t || !t.closest) return;

    var calc = t.closest('[data-calc]');
    if (calc) send('calculator_use', { tool: path, page: path });

    var lb = t.closest('.lang-btn');
    if (lb) send('language_switch', { to: (lb.textContent || '').trim(), page: path });

    var a = t.closest('a[href]');
    if (!a) return;
    var h = host(a.getAttribute('href'));
    var base = { page: path, slot: slotOf(a), lang: lang };

    if (h === 'apps.apple.com') { base.store = 'app_store'; send('store_click', base); }
    else if (h === 'play.google.com') { base.store = 'google_play'; send('store_click', base); }
    else if (h === 'app.booom.fit') send('webapp_click', base);
    else if (/(^|\.)instagram\.com$/.test(h)) send('social_click', { network: 'instagram', page: path, slot: base.slot });
    else if (/(^|\.)tiktok\.com$/.test(h)) send('social_click', { network: 'tiktok', page: path, slot: base.slot });
    else if (/(^|\.)facebook\.com$/.test(h)) send('social_click', { network: 'facebook', page: path, slot: base.slot });
    else if (/\.pdf($|\?)/i.test(a.getAttribute('href') || '')) send('plan_download', { file: (a.getAttribute('href') || '').split('/').pop(), page: path });
  }, true);
}());
