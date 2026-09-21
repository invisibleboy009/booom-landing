# 🚀 BOOOM Landing Page — Comprehensive Handoff Summary
**Generated:** 2026-06-19  
**Repository:** C:\Users\laco\booom-landing  
**Branch:** master (clean working tree)  
**Last Commit:** d5eb494 - fix: lang.js syntax error in DE translations

---

## 📊 Project Overview

**BOOOM** is a next-generation fitness application landing page with:
- **Multi-language support:** 6 languages (SK, EN, CS, PL, UK, DE)
- **Educational content:** Thyroid health, specialized diets, enhanced fitness (LAB)
- **AI Chat Widget:** Boomer AI assistant with email OTP registration
- **Deployment:** Vercel (with custom routing)
- **Tech Stack:** Static HTML/CSS/JS, Supabase Edge Functions, Anthropic Claude API

---

## 📁 Modified Files (Last 30 Days)

### Core Files (Most Frequently Modified)
| File | Changes | Description |
|------|---------|-------------|
| `index.html` | 57 modifications | Main landing page |
| `lang.js` | 16 modifications | i18n translations (2009 lines, 6 languages) |
| `stitna-zlaza.html` | 13 modifications | Thyroid health page |
| `dieta/bezlaktozova.html` | 11 modifications | Lactose-free diet page |
| `dieta/bezlepkova.html` | 8 modifications | Gluten-free diet page |
| `vercel.json` | 7 modifications | Vercel routing configuration |
| `dieta/histaminova.html` | 6 modifications | Histamine intolerance page |
| `dieta/hashimoto.html` | 5 modifications | Hashimoto thyroiditis page |
| `lab.html` | 3 modifications | Enhanced fitness educational page |
| `assets/js/boomer-chat.js` | 3 modifications | AI chat widget |

### New Files Added
- `all_i18n_keys.txt` - Complete list of 196 i18n keys
- `email-templates/confirm.html` - Email confirmation template
- `privacy.html` - Privacy policy page
- `supabase/functions/boomer-landing-chat/index.ts` - Supabase Edge Function
- `supabase-migrations/landing-leads.sql` - Database schema
- `.gitignore` - Git ignore rules

### Deleted Files
- `screenshots/*.jpg` - 15 screenshot files removed (legacy flat-screenshot showcase)

---

## 🌍 Language Structure (lang.js)

**Total:** 2009 lines, 6 complete language translations

### Supported Languages
1. **SK** (Slovak) - Default, lines 2-328
2. **EN** (English) - lines 329-655
3. **CS** (Czech) - lines 656-982
4. **PL** (Polish) - lines 983-1308
5. **UK** (Ukrainian) - lines 1309-1635
6. **DE** (German) - lines 1636-1948 (most recent addition)

### Translation Categories (196 unique keys)
- **Navigation:** nav_tagline, nav_cta, nav_features, nav_thyroid, nav_diets_*, nav_story, nav_ranks
- **Hero Section:** hero_badge, hero_h1_*, hero_subtitle, hero_cta*, hero_stat*_label, hero_scroll
- **Features:** features_title, features_subtitle, features_p1-p3_*, features_h1-h3_*, feature_tag_*
- **Story (Founder):** story_h1-h5, story_p1-p14, story_key1-3, story_emil, story_highlight, story_conclusion
- **LAB (Enhanced Fitness):** lab_*, substances_*, markers_*, psych_*, detection_*, chart_*
- **Testimonials:** testimonial1-3_*, testimonials_*
- **FOMO Section:** fomo_*
- **Diets Teaser:** teaser_*, diets_*
- **CTA & Footer:** cta_*, footer_*, ranks_*
- **Phone Features:** fp_*, hps_*, badge1-3_*

### Last Translation Issue Fixed
- **Commit d5eb494:** Fixed syntax error in German (DE) translations

---

## 🔧 vercel.json Configuration

```json
{
  "rewrites": [
    {"source": "/stitna-zlaza", "destination": "/stitna-zlaza.html"},
    {"source": "/dieta/bezlaktozova", "destination": "/dieta/bezlaktozova.html"},
    {"source": "/dieta/bezlepkova", "destination": "/dieta/bezlepkova.html"},
    {"source": "/dieta/histaminova", "destination": "/dieta/histaminova.html"},
    {"source": "/dieta/hashimoto", "destination": "/dieta/hashimoto.html"},
    {"source": "/privacy", "destination": "/privacy.html"},
    {"source": "/(.*)", "destination": "/index.html"}
  ]
}
```

**Note:** Clean URL routing without .html extensions

---

## 📄 Current Page Structure

### Main Pages
1. **index.html** - Main landing page
   - Hero with 3D phone showcase
   - Stats dashboard (8 sections, 36 blood params, 24/7 AI Coach)
   - Features grid with progressive disclosure modal
   - Founder's Story (accordion)
   - Testimonials (3 beta users)
   - FOMO section (Early Access counter)
   - Diet & Health teasers (4 specialized guides)
   - Ranks progression
   - Footer with navigation

2. **stitna-zlaza.html** - Thyroid health guide
   - Science cards, strumigeny, soja, medication warnings

3. **dieta/bezlaktozova.html** - Lactose-free diet
   - 7-day meal plan with macros
   - Bulking toggle feature

4. **dieta/bezlepkova.html** - Gluten-free diet (celiac)
   - 7-day meal plan

5. **dieta/histaminova.html** - Histamine intolerance
   - 7-day meal plan

6. **dieta/hashimoto.html** - Hashimoto thyroiditis diet
   - 7-day meal plan
   - Selenium, myo-inositol supplementation

7. **lab.html** - BOOOM LAB (Enhanced fitness education)
   - **RESTRICTED ACCESS badge**
   - Educational deep-dive: Testosterone, Trenbolone, Anavar, Dianabol
   - Blood markers (36 parameters)
   - Psychological reality (God Mode vs Hormonal Hell)
   - Detection visual cues
   - Charts (Natural vs Enhanced testosterone, Strength rollercoaster)
   - ⚠️ Disclaimer: Educational purposes only

8. **privacy.html** - Privacy policy

---

## 🤖 Supabase Edge Function: boomer-landing-chat

**Location:** `supabase/functions/boomer-landing-chat/index.ts`

### Functionality
- **AI Model:** Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)
- **Max Tokens:** 300
- **Rate Limiting:** 20 messages per email per day
- **Language:** Slovak responses (4 sentences max)
- **Scope:** Fitness, diets (gluten-free, lactose-free, histamine, Hashimoto), thyroid, BOOOM PWA installation

### System Prompt
```
Si Boomer, AI asistent fitness aplikácie BOOOM (booom.fit).
Odpovedáš v slovenčine, stručne (max 4 vety), priateľsky s emoji.
Pomáhaš s: fitness, diétami (bezlepková, bezlaktózová, histamínová, Hashimoto),
štítnou žľazou, inštaláciou BOOOM PWA appky.
Pri zdravotných otázkach vždy dodaj: nie si lekár, odporúčaj konzultáciu s odborníkom.
BOOOM je zadarmo na app.booom.fit.
```

### Environment Variables Required
- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY`
- `ANTHROPIC_API_KEY`

### CORS Headers
```javascript
{
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS'
}
```

### Rate Limit Logic
- Tracks `chat_count` in `landing_leads` table
- Increments after successful AI response
- Returns 429 error at 20 messages: "Dosiahol si denný limit 20 správ. Ďakujeme za záujem o BOOOM! 💪"

### Message History
- Keeps last 6 messages
- Content capped at 1000 characters per message
- Ensures alternating user/assistant roles
- Always starts with user message

---

## 🗄️ Supabase Database Schema

**Migration:** `supabase-migrations/landing-leads.sql`

### Table: landing_leads
- Stores email OTP verification
- Tracks chat usage count
- Stores conversation history

---

## 📱 Boomer AI Chat Widget

**File:** `assets/js/boomer-chat.js`

### Features
- Floating chat button (bottom-right)
- Email OTP registration flow
- Persistent chat history (localStorage)
- Conversation history panel
- Follow-up suggestion chips
- Rate limit display
- Mobile responsive

### Integration
- Included on all HTML pages via `<script>` tag
- Connects to Supabase Edge Function
- No jQuery dependency

---

## 🎨 Current Page Sections & Status

### ✅ Completed Sections (index.html)
1. ✅ **Navigation** - Mobile hamburger menu, language switcher (6 langs), diet dropdown
2. ✅ **Hero** - 3D phone showcase, animated badges, weight dashboard, stats grid
3. ✅ **Features Grid** - 6 feature cards with progressive disclosure modal
4. ✅ **Founder's Story** - Accordion with Emil story, Hashimoto diagnosis, full i18n
5. ✅ **Testimonials** - 3 beta user testimonials with ratings
6. ✅ **FOMO Section** - Early Access counter (473/500 available)
7. ✅ **Diet Teasers** - 4 specialized diet guides (thyroid, lactose, gluten, histamine, Hashimoto)
8. ✅ **LAB Teaser** - Enhanced fitness restricted access teaser
9. ✅ **Ranks** - 6-rank progression system
10. ✅ **CTA** - Final call-to-action with benefits
11. ✅ **Footer** - Navigation links, privacy policy

### ✅ Specialized Pages Status
- ✅ Thyroid page (stitna-zlaza.html) - Science content updated
- ✅ Lactose-free diet - 7-day meal plan with bulking toggle
- ✅ Gluten-free diet - 7-day meal plan
- ✅ Histamine intolerance - 7-day meal plan
- ✅ Hashimoto diet - 7-day meal plan
- ✅ LAB page - Full enhanced fitness educational content
- ✅ Privacy policy page

---

## 🐛 Known Issues & TODOs

### No Critical Issues Found

**Search Results:** No TODO, FIXME, XXX, HACK, or BUG comments found in codebase

### Minor Notes
- "Biohacking" appears 15 times across translations (not a bug, intentional feature)
- `appendMessageToDOM` function in boomer-chat.js (functional, no issues)

---

## 📜 Last 10 Git Commits (Detailed)

```
d5eb494 (HEAD -> master, origin/master) fix: lang.js syntax error in DE translations
│  lang.js | 1 modification
│
c50672a feat: German language (DE) added to landing page
│  all_i18n_keys.txt            | 196 new lines
│  email-templates/confirm.html | 153 new lines
│  index.html                   | 263 modifications
│  lang.js                      | 1271 additions
│
0fbdf3f fix(nav): reorder navigation menu links to prioritize thyroid and diet content
│  index.html | minor nav reorder
│
a7f8588 fix(i18n): CRITICAL - translate entire Founder's Story to all 5 languages
│  index.html | story structure
│  lang.js    | massive translation additions
│
15235ec fix(copy): upgrade hero headlines from weak single-word to punchy marketing copy
│  lang.js | hero headline improvements
│
14e7ff0 fix(hero): CRITICAL - repair broken desktop two-column layout
│  index.html | CSS layout fixes
│
019603d fix(i18n): enterprise-grade internationalization audit - critical violations remediated
│  index.html | i18n data attributes
│  lab.html   | i18n fixes
│  lang.js    | translation completions
│
bb992a5 fix: comprehensive i18n audit - eliminate hardcoded Slovak strings
│  index.html | remove hardcoded SK strings
│  lang.js    | centralize translations
│
aaa7dfd feat: complete i18n audit - 100% translation coverage
│  lang.js | full i18n coverage
│
178afaa fix: complete internationalization for LAB content across all languages
│  lang.js | LAB translations
```

---

## 🔗 DNS & Deployment Info

### Current Deployment
- **Platform:** Vercel
- **Production URL:** *(not specified in repo, likely booom.fit or similar)*
- **Routing:** Custom rewrites via vercel.json
- **Build:** Static site (no build step required)

### Google Analytics
- **Tracking ID:** G-48KJX7NJZR
- **Deployed on:** 2026-06-08
- **Pages:** All HTML pages include GA script

### External Integrations
- **Supabase:** Edge Functions, Database (landing_leads table)
- **Anthropic API:** Claude Haiku 4.5 for chat
- **Email OTP:** Supabase Auth (configured in boomer-chat.js)

---

## 🚀 Development Workflow

### Local Development
1. No build step required
2. Open `index.html` in browser
3. Language switcher works via localStorage

### Language Management
- **Add new key:** Add to all 6 language objects in lang.js
- **Key naming:** category_element_detail (e.g., `hero_h1_line1`)
- **Usage:** `<element data-i18n="key_name">Default Text</element>`
- **Auto-detection:** Browser language detection on first visit

### Testing Checklist
- ✅ All 6 languages render correctly
- ✅ Mobile hamburger menu works
- ✅ Diet dropdown hover (desktop) and tap (mobile)
- ✅ Features modal progressive disclosure
- ✅ Founder's Story accordion
- ✅ Boomer AI chat widget (OTP flow, rate limits)
- ✅ Language persistence in localStorage
- ✅ Smooth scroll navigation

---

## 📊 Project Statistics

- **Total Commits (30 days):** 76
- **Files Tracked:** 40+
- **Lines of Code (lang.js):** 2,009
- **i18n Keys:** 196
- **Supported Languages:** 6
- **HTML Pages:** 9
- **Diet Guides:** 4
- **Educational Pages:** 2 (Thyroid, LAB)

---

## 🎯 Key Project Highlights

### Recent Major Milestones
1. ✅ **German (DE) language fully added** (c50672a, d5eb494)
2. ✅ **Founder's Story translated to all 5 languages** (a7f8588)
3. ✅ **Comprehensive i18n audit completed** (019603d, bb992a5, aaa7dfd)
4. ✅ **LAB educational section added** (6708552)
5. ✅ **Boomer AI chat widget with OTP registration** (83cd1c7)
6. ✅ **4 specialized diet pages with 7-day meal plans** (multiple commits)
7. ✅ **Mobile hamburger menu** (a870131)
8. ✅ **Privacy policy page** (a7801d2)
9. ✅ **Google Analytics integration** (8615960)

### Content Strategy
- **Target Audience:** SK, CZ, PL, UK, DE, EN markets
- **Focus:** Health-conscious fitness enthusiasts with specific conditions (Hashimoto, intolerances)
- **Unique Value:** 36 blood parameter tracking, AI Coach, personalized diet plans
- **Early Access:** First 500 users get priority features forever

---

## 🔮 Next Steps Recommendations

### Potential Enhancements
1. **A/B Testing:** Hero CTA variations
2. **Analytics:** Track language preference distribution
3. **SEO:** Add meta descriptions for all language versions
4. **Performance:** Image optimization (if new images added)
5. **Accessibility:** ARIA labels audit (partially implemented)
6. **Email Marketing:** Integrate confirm.html template with actual email service
7. **Chat Analytics:** Track Boomer AI conversation topics and satisfaction

### Maintenance
- **Monitor:** Supabase Edge Function rate limits and costs
- **Update:** Anthropic API version when new models available
- **Review:** Chat conversation quality and adjust system prompt if needed
- **Backup:** Export landing_leads data regularly

---

## 📞 Contact & Resources

- **Founder:** Laco (lvolny1@gmail.com)
- **Git User:** laco
- **Working Directory:** C:\Users\laco\booom-landing
- **Platform:** Windows 10 Home 10.0.19045
- **Shell:** PowerShell (primary), Bash available

---

## ✅ Summary Checklist

- [x] All files from last 30 days documented
- [x] Full lang.js structure (6 languages, 196 keys) mapped
- [x] vercel.json routing configuration included
- [x] Open TODOs checked (none found)
- [x] Current page sections and status listed
- [x] No known bugs identified
- [x] Last 10 git commits detailed
- [x] Supabase Edge Function fully documented
- [x] DNS and deployment info provided
- [x] Boomer AI chat widget specs included

---

**End of Handoff Summary**  
*Generated by Claude Sonnet 4.5 on 2026-06-19*

## Jazykove verzie a SEO (2026-09-19)

- `/en/`, `/cs/`, `/pl/`, `/uk/`, `/de/` su STATICKE stranky generovane z `index.html` + `lang.js` skriptom `node build-i18n.mjs`. Po kazdej zmene `index.html`, `lang.js`, `faq.html` alebo `vercel.json` ho spusti a commitni vygenerovane subory (Vercel ho nespusta).
- Ten isty skript generuje `sitemap.xml` (lastmod z gitu, hreflang alternates) a FAQPage JSON-LD v `faq.html`.
- `lang.js`: na strankach s `data-static-lang` prepnutie jazyka NAVIGUJE na URL jazyka; boty (UA bot/crawl/headless...) sa nikdy nepresmeruju. Podstranky (kalkulacky, sprievodcovia) prekladaju in-place ako predtym.
- `vercel.json` uz nema catch-all na index.html; neexistujuce URL vracaju `404.html`.

## Vykon, meranie a obsah (2026-09-20)

- **Pismo**: Inter je self-hosted v `assets/fonts/Inter-{latin,latin-ext,cyrillic}.woff2` (variable). Kazda stranka ma inline `@font-face` + preload; Google Fonts uz sa nenacitava.
- **supabase-js** sa uz nenacitava synchronne: `boomer-chat.js` vystavuje `window.loadSupabase()` (nacita sa pri otvoreni chatu; testimonials na home ho nacitaju tesne pred zobrazenim alebo po 4 s).
- **`vercel.json` headers**: fonty 1 rok immutable, obrazky 7 dni, skripty 1 h, + nosniff / referrer / frame / permissions hlavicky.
- **Meranie**: `assets/js/track.js` (deferred na kazdej stranke) posiela GA4 udalosti `store_click`, `webapp_click`, `social_click`, `plan_download`, `calculator_use` (element s `data-calc`), `language_switch`, `boomer_open`, `generate_lead`. Odchadzajuce linky na app dostavaju UTM (`utm_campaign` = slug stranky, `utm_content` = sekcia), Play `referrer`, App Store `ct`. V GA4 Admin treba oznacit `store_click`, `webapp_click`, `generate_lead` ako key events.
- **Blog (SK/EN/CS)**: obsah je v `blog-src/content_{sk,en,cs}.py`, `python blog-src/make_blog.py` z nich vygeneruje `blog/`, `en/blog/`, `cs/blog/` (hreflang, prepinac jazykov, JSON-LD), potom `node build-i18n.mjs` a commit. Novy clanok = pridaj polozku do vsetkych troch `ARTICLES` (rovnake `sections` id), rewrite do `vercel.json`, riadok do `BLOG_CLUSTERS`, `BLOG_LOCAL` a `SL_GROUPS`/`SL_LANG` v `build-i18n.mjs`. Kalkulacky su len po slovensky, preto ich linky v EN/CS clankoch nesu dodatok (Slovak)/(slovensky).
- **Prepojenia**: `build-i18n.mjs` krok 4 vklada blok "Dalsie nastroje a sprievodcovia" pred `<footer>` kazdej obsahovej stranky (medzi znackami `site-links:start/end`); nastroje/clanky pridavaj do `SL_GROUPS`.
- **Kalkulacky**: 1RM, kalorie, Hyrox pacing a percento tuku (nova kalkulacka US Navy) maju rozsirene texty; FAQ v HTML a FAQPage JSON-LD musia zostat zhodne.
- **Nav na home**: hamburger pod 1500 px, od 1500 do 1699 px sa socialne pilulky skryju (ostavaju v menu a pateke), od 1700 px je vsetko. Najdlhsie su ukrajinske popisky, s nimi je to overene.

## Preklady kalkulaciek a nahladove obrazky (2026-09-20)

- Kalkulacky maju EN a CS verzie: `en/1rm-calculator`, `en/calorie-calculator`, `en/hyrox-pacing-calculator`, `en/body-fat-calculator` a `cs/1rm-kalkulacka`, `cs/kaloricka-kalkulacka`, `cs/hyrox-pacing-kalkulacka`, `cs/procento-telesneho-tuku` (rucne HTML, kopie SK stranok s prelozenymi textami a JS retazcami; logika sa nesmie rozchadzat, pri oprave vzorca uprav vsetky tri). Rewrites su vo `vercel.json`, hreflang zhluky v `BLOG_CLUSTERS` (`build-i18n.mjs`, polozky 5+ su nastroje), lokalizovane linky na EN/CS home v `TOOLS_LOCAL`, blok suvisiacich odkazov v `SL_LANG`.
- Nahladove obrazky (og:image) pre clanky a nastroje: `python blog-src/make_og.py` (Pillow, font Segoe UI Bold z Windows) zapise `assets/og/<jazyk>-<kluc>.jpg`; `make_blog.py` ich dosadzuje do clankov, nastroje ich maju v HTML.
- Recenzie: home uz nevklada Review JSON-LD (Search Console: "viacero recenzii bez aggregateRating"). Referencie ostavaju viditelne; funkcia `markup()` v `index.html` ostala nevyuzita.

## Blog: rozsirenia, nove clanky, manifest (2026-09-20, vecer)

- Clanky su teraz 8 (SK/EN/CS): treningovy-dennik, progresivne-pretazenie, kolko-bielkovin-denne, hyrox-priprava-8-tyzdnov (rozsirene) + chudnutie-bez-straty-svalov, treningovy-split, hyrox-stanice-technika, regeneracia-a-spanok (nove).
- Zdroj: zaklad v `blog-src/content_{sk,en,cs}.py`, rozsirenia a nove clanky v `blog-src/extras/NN_*.py` (`EXTEND` = pridat sekcie/FAQ do existujuceho, `NEW` = novy clanok; format v `blog-src/extras_loader.py`). Novy clanok = novy subor `extras/1N_*.py` s `NEW` pre sk/en/cs, potom `python blog-src/make_blog.py`, `python blog-src/make_og.py`, `node build-i18n.mjs`, commit.
- `make_blog.py` zapisuje `blog-src/manifest.json` a chybajuce rewrites do `vercel.json`; `build-i18n.mjs` z manifestu sam generuje zoznam clankov na home (medzi `<!-- blog-links:start/end -->` v `index.html`), EN/CS home, bloky suvisiacich odkazov a sitemap hreflang. Uz sa nic nedopisuje rucne.
- Karusel na home: bodky su len indikator, prepinaju sipky (`hero_prev`, `hero_next` v `lang.js`), kvoli minimalnej velkosti dotykovej plochy.

## Rychlost: meranie a upravy (2026-09-20)

- Baseline (Chrome trace, mobil, Fast 4G, CPU 4x pomalsi): home LCP 964 ms (H1 text, TTFB 166 ms), CLS 0,01, 24 poziadaviek; blog LCP 1122 ms. Google Tag Manager zabral 490-820 ms hlavneho vlakna, latin-ext font sa na SK/CS/PL strankach zistil az po layoute (1,1 s retaz).
- Upravy: `gtag.js` sa nacita po `load` + idle (dataLayer sa plni hned, takze udalosti z `track.js` nepadnu); `<link rel="preload">` pre `Inter-latin-ext` (SK/CS/PL) alebo `Inter-cyrillic` (UK), EN/DE ho nemaju. Generuje `make_blog.py` (blog) a `build-i18n.mjs` (jazykove home).
- Neurobene (uvazene): prekodovanie hero plagatov (usetri ~19 %, text na plagatoch by trpel), rozdelenie `lang.js` (68 kB gz, nie je na kritickej ceste), zuzenie fontu (vyzaduje fonttools).
- Doplnok (rychlost, vecer): trace (`performance_start_trace`, mobil, Fast 4G, CPU 4x) ukazala, ze prve vykreslenie blogu cakalo na jeden ~1 s Layout cez cely clanok. `content-visibility:auto` na sekciach clankov a na `.content` kalkulaciek (generuje `make_blog.py`, kalkulacky maju pravidlo v CSS) skratilo Layout na ~490 ms a FCP/LCP z ~1,7 s na ~1,1 s (zive meranie 1094 ms). Zalozne pismo `Inter Fallback` (size-adjust 107,4 %) LCP nezmenilo, ale znizuje posun pri vymene pisma, ostava. Preload latin-ext LCP nezhorsil ani nezlepsil (kolisanie merani ~±300 ms).

## O nas / About (2026-09-21)

- Stranka "O nas": SK `/o-nas` (`o-nas.html`), EN `/en/about` (`en/about.html`), CS `/cs/o-nas` (`cs/o-nas.html`). Text je v `blog-src/about_content.py` (dict `ABOUT` pre sk/en/cs), generuje ju `make_blog.py` (`build_about`), ktory zapisuje aj rewrites do `vercel.json`. OG obrazky `assets/og/<jazyk>-about.jpg` robi `make_og.py`.
- Obsah: pribeh (bez priezviska a fotky), otvorene "nie som lekar/trener/vyzivovy poradca, nemam certifikat", sekcia "Zadarmo, bez hacikov" (BOOOM je celý zadarmo, ziadne balicky/poplatky/zlavove kody), funkcie, kontakt + socialne siete. Schema: `AboutPage` + `Organization` (sameAs) + `BreadcrumbList`, bez osobneho mena. Ak sa v appke nieco spoplatni, treba upravit sekciu "zadarmo" vo vsetkych 3 jazykoch (a FAQ/terms to uz dnes pise ako "momentalne zadarmo").
- Prelinkovanie: pata blogovych clankov ("O nas"), zdravotne clanky (`DISC_HEALTH`) maju pod upozornenim odkaz na About, `stitna-zlaza.html` (upozornenie hore), paticka a mobilne menu na home (`/o-nas`, EN/CS home na svoju verziu, PL/UK/DE na `/en/about`), blok suvisiacich odkazov ("BOOOM": O nas, Caste otazky) a sitemap hreflang cluster v `build-i18n.mjs`.
- Oprava faktu: stitna zlaza fungovala na priblizne 10 % (predtym "necelych 20 %") v `lang.js` `story_p7` vo vsetkych 6 jazykoch.
- Postup pri zmene textu: uprav `about_content.py`, potom `python blog-src/make_blog.py`, `python blog-src/make_og.py`, `node build-i18n.mjs`, commit.

## Google Analytics: novy webovy stream (2026-09-21)

- Zistenie: v GA ucte BOOOM (vlastnost `booom-f64cc`) boli len aplikacne streamy (Android/iOS) a ziadny webovy; predchadzajuci merací kod webu `G-V29R9X94FM` sa v tomto ucte nenasiel a vlastnost hlasila 0 udajov z webu.
- Riesenie: v tej istej vlastnosti vznikol webovy stream "booom.fit web" (`https://booom.fit`, ID streamu 15816741080), merací kod `G-48KJX7NJZR`. Kod je vymeneny vo vsetkych strankach a v generatoroch (`blog-src/make_blog.py`, `build-september.py`). Zalozne subory `index.html.backup` a `lab.html.disabled` maju stary kod zamerne.
- Kluce udalosti (`store_click`, `webapp_click`, `generate_lead`): oznacuju sa v GA Admin > Kluce udalosti > Nova kluca udalost (nazov presne ako udalost). Udalosti sa v zozname ukazu az po prvom spusteni.
