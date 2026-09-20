(function () {
  'use strict';

  // ── Constants ──────────────────────────────────────────────────────────────
  var SUPABASE_URL = 'https://itwnqpggvcramyckoyiw.supabase.co';
  var SUPABASE_ANON_KEY = 'sb_publishable_kEM_LigU1HXZhw4Agu48LQ_BHYdWVYw';
  // Servírované z vlastného hostingu, NIE zo Supabase storage. Pôvodná adresa
  // ukazovala na 5,6 MB PNG v Supabase buckete a každá návšteva landingu ho
  // stiahla nanovo — 63 MB za jediný deň (24. 8. 2026), prakticky celý
  // prečerpaný free-tier egress projektu. Tento WebP má 44 kB a Vercel si
  // prenos neúčtuje. Rovnaký obrázok používa appka ako /avatars/ai-coach-booomer.webp.
  var AVATAR_URL = '/assets/booomer-avatar.webp';
  var EDGE_FN = SUPABASE_URL + '/functions/v1/boomer-landing-chat';
  var LS_EMAIL = 'boomer_email';
  var LS_CONVOS = 'boomer_conversations';
  var MAX_DISPLAY = 20;
  var MAX_API_CTX = 6;

  // ── State ──────────────────────────────────────────────────────────────────
  var BUBBLE_MSGS = [
    'Ahoj, ako ti môžem pomôcť? 💪',
    'Čau makáč! Hoď mi sem svoje max na bench a ja ti poviem kde máš rezervu. 💪',
    'Hej! Koľko dávaš na drep? Za 10 sekúnd ti poviem či trénuješ správne.',
    'Silák, odkedy tréningy nezapisuješ? Tvoje PR ťa čakajú v BOOOM. 🔥',
    'Čo ťa zastavuje od ďalšieho PR? Opýtaj sa ma — som tu pre teba 24/7.',
    'Ahoj! Zaujíma ťa ako schudnúť a pritom nestratiť svalovku? Mám odpoveď.'
  ];
  var bubbleIdx = 0;

  // ── Language ───────────────────────────────────────────────────────
  // The page's language (lang.js writes data-lang on <html>; static language pages carry
  // it in the HTML). Read on every use, not once: subpages switch language in place.
  function lang() {
    var l = (document.documentElement.getAttribute('data-lang') || 'SK').toUpperCase();
    return LANG_STR[l] ? l : 'SK';
  }
  function S() { return LANG_STR[lang()]; }

  var LANG_STR = {
    SK: {
      locale: 'sk-SK', today: 'Dnes', yesterday: 'Včera', convo: 'Konverzácia ',
      bubble: 'Ahoj, ako ti môžem pomôcť?', bubbles: null,
      greeting: 'Ahoj! Som Boomer, tvoj AI asistent 💪 Ako ti môžem pomôcť?',
      openAria: 'Otvoriť Boomer AI asistenta', back: 'Späť', history: 'História', histAria: 'História konverzácií',
      newChat: 'Nová konverzácia', close: 'Zavrieť', rename: 'Premenovať',
      disclaimer: '&#9877;&#65039; Nie som lekár. Rady sú informačné — konzultuj s odborníkom.',
      placeholder: 'Napíš správu…', send: 'Odoslať',
      histEmpty: 'Žiadne uložené konverzácie.<br/>Začni chatovať a automaticky sa uložia.',
      gateSub: 'Zadaj email a hneď môžeme chatovať.', gateBtn: 'Získať prístup k Boomerovi',
      emailInvalid: 'Zadaj platný email.', sending: 'Odosiela sa…', sendFail: 'Chyba pri odoslaní. Skús znova.',
      otpTitle: '📬 Skontroluj email', otpSub: 'Poslali sme 6-miestny kód na ', otpBtn: 'Overiť kód',
      otpInvalid: 'Zadaj 6-miestny kód.', verifying: 'Overujem…', otpWrong: 'Nesprávny kód. Skús znova.',
      noReply: 'Prepáč, nepodarilo sa mi odpovedať.', errGeneric: 'Nastala chyba. Skús neskôr.',
      errNet: 'Spojenie zlyhalo. Skontroluj internet a skús znova.',
      chipsHome: ['Čo je BOOOM?', 'Ako nainštalovať?', 'Je to zadarmo?', 'Pre koho je BOOOM?'],
      chipsDefault: ['Čo je BOOOM?', 'Ako nainštalovať?', 'Diéty a zdravie', 'Kontakt'],
      follow: ['Povedz mi viac', 'Ako mi BOOOM pomôže?', 'Mám ďalšiu otázku']
    },
    EN: {
      locale: 'en-GB', today: 'Today', yesterday: 'Yesterday', convo: 'Conversation ',
      bubble: 'Hi, how can I help?',
      bubbles: ['Hi, how can I help? 💪', 'Send me your bench max and I will tell you where the reserve is. 💪', 'What is stopping your next PR? Ask me — I am here 24/7.'],
      greeting: 'Hi! I am Boomer, your AI assistant 💪 How can I help?',
      openAria: 'Open the Boomer AI assistant', back: 'Back', history: 'History', histAria: 'Conversation history',
      newChat: 'New conversation', close: 'Close', rename: 'Rename',
      disclaimer: '&#9877;&#65039; I am not a doctor. This is information, not advice — talk to a professional.',
      placeholder: 'Type a message…', send: 'Send',
      histEmpty: 'No saved conversations.<br/>Start chatting and they save automatically.',
      gateSub: 'Enter your email and we can chat right away.', gateBtn: 'Get access to Boomer',
      emailInvalid: 'Enter a valid email.', sending: 'Sending…', sendFail: 'Could not send. Try again.',
      otpTitle: '📬 Check your email', otpSub: 'We sent a 6-digit code to ', otpBtn: 'Verify code',
      otpInvalid: 'Enter the 6-digit code.', verifying: 'Verifying…', otpWrong: 'Wrong code. Try again.',
      noReply: 'Sorry, I could not answer that.', errGeneric: 'Something went wrong. Try later.',
      errNet: 'Connection failed. Check your internet and try again.',
      chipsHome: ['What is BOOOM?', 'How do I install it?', 'Is it free?', 'Who is BOOOM for?'],
      chipsDefault: ['What is BOOOM?', 'How do I install it?', 'Diets & health', 'Contact'],
      follow: ['Tell me more', 'How does BOOOM help me?', 'I have another question']
    },
    CS: {
      locale: 'cs-CZ', today: 'Dnes', yesterday: 'Včera', convo: 'Konverzace ',
      bubble: 'Ahoj, jak ti můžu pomoct?',
      bubbles: ['Ahoj, jak ti můžu pomoct? 💪', 'Pošli mi svoje maximum na bench a řeknu ti, kde máš rezervu. 💪', 'Co ti brání v dalším PR? Zeptej se mě — jsem tu 24/7.'],
      greeting: 'Ahoj! Jsem Boomer, tvůj AI asistent 💪 Jak ti můžu pomoct?',
      openAria: 'Otevřít Boomer AI asistenta', back: 'Zpět', history: 'Historie', histAria: 'Historie konverzací',
      newChat: 'Nová konverzace', close: 'Zavřít', rename: 'Přejmenovat',
      disclaimer: '&#9877;&#65039; Nejsem lékař. Rady jsou informační — poraď se s odborníkem.',
      placeholder: 'Napiš zprávu…', send: 'Odeslat',
      histEmpty: 'Žádné uložené konverzace.<br/>Začni chatovat a automaticky se uloží.',
      gateSub: 'Zadej e-mail a hned můžeme chatovat.', gateBtn: 'Získat přístup k Boomerovi',
      emailInvalid: 'Zadej platný e-mail.', sending: 'Odesílá se…', sendFail: 'Chyba při odeslání. Zkus to znovu.',
      otpTitle: '📬 Zkontroluj e-mail', otpSub: 'Poslali jsme 6místný kód na ', otpBtn: 'Ověřit kód',
      otpInvalid: 'Zadej 6místný kód.', verifying: 'Ověřuji…', otpWrong: 'Nesprávný kód. Zkus to znovu.',
      noReply: 'Promiň, nepodařilo se mi odpovědět.', errGeneric: 'Nastala chyba. Zkus to později.',
      errNet: 'Spojení selhalo. Zkontroluj internet a zkus to znovu.',
      chipsHome: ['Co je BOOOM?', 'Jak nainstalovat?', 'Je to zdarma?', 'Pro koho je BOOOM?'],
      chipsDefault: ['Co je BOOOM?', 'Jak nainstalovat?', 'Diety a zdraví', 'Kontakt'],
      follow: ['Řekni mi víc', 'Jak mi BOOOM pomůže?', 'Mám další otázku']
    },
    PL: {
      locale: 'pl-PL', today: 'Dziś', yesterday: 'Wczoraj', convo: 'Rozmowa ',
      bubble: 'Cześć, jak mogę pomóc?',
      bubbles: ['Cześć, jak mogę pomóc? 💪', 'Wyślij mi swój max na ławce, a powiem ci, gdzie masz rezerwę. 💪', 'Co cię powstrzymuje przed kolejnym rekordem? Zapytaj — jestem tu 24/7.'],
      greeting: 'Cześć! Jestem Boomer, twój asystent AI 💪 Jak mogę pomóc?',
      openAria: 'Otwórz asystenta Boomer AI', back: 'Wstecz', history: 'Historia', histAria: 'Historia rozmów',
      newChat: 'Nowa rozmowa', close: 'Zamknij', rename: 'Zmień nazwę',
      disclaimer: '&#9877;&#65039; Nie jestem lekarzem. To informacje, nie porady — skonsultuj się ze specjalistą.',
      placeholder: 'Napisz wiadomość…', send: 'Wyślij',
      histEmpty: 'Brak zapisanych rozmów.<br/>Zacznij pisać, a zapiszą się automatycznie.',
      gateSub: 'Podaj e-mail i od razu możemy rozmawiać.', gateBtn: 'Uzyskaj dostęp do Boomera',
      emailInvalid: 'Podaj poprawny e-mail.', sending: 'Wysyłanie…', sendFail: 'Błąd wysyłania. Spróbuj ponownie.',
      otpTitle: '📬 Sprawdź e-mail', otpSub: 'Wysłaliśmy 6-cyfrowy kod na ', otpBtn: 'Zweryfikuj kod',
      otpInvalid: 'Wpisz 6-cyfrowy kod.', verifying: 'Weryfikuję…', otpWrong: 'Zły kod. Spróbuj ponownie.',
      noReply: 'Przepraszam, nie udało mi się odpowiedzieć.', errGeneric: 'Wystąpił błąd. Spróbuj później.',
      errNet: 'Połączenie nie powiodło się. Sprawdź internet i spróbuj ponownie.',
      chipsHome: ['Czym jest BOOOM?', 'Jak zainstalować?', 'Czy jest za darmo?', 'Dla kogo jest BOOOM?'],
      chipsDefault: ['Czym jest BOOOM?', 'Jak zainstalować?', 'Diety i zdrowie', 'Kontakt'],
      follow: ['Powiedz mi więcej', 'Jak BOOOM mi pomoże?', 'Mam kolejne pytanie']
    },
    UK: {
      locale: 'uk-UA', today: 'Сьогодні', yesterday: 'Вчора', convo: 'Розмова ',
      bubble: 'Привіт, чим можу допомогти?',
      bubbles: ['Привіт, чим можу допомогти? 💪', 'Надішли свій максимум на жимі, і я скажу, де є резерв. 💪', 'Що заважає наступному рекорду? Запитай — я тут 24/7.'],
      greeting: 'Привіт! Я Boomer, твій AI-асистент 💪 Чим можу допомогти?',
      openAria: 'Відкрити AI-асистента Boomer', back: 'Назад', history: 'Історія', histAria: 'Історія розмов',
      newChat: 'Нова розмова', close: 'Закрити', rename: 'Перейменувати',
      disclaimer: '&#9877;&#65039; Я не лікар. Це інформація, а не поради — порадься з фахівцем.',
      placeholder: 'Напиши повідомлення…', send: 'Надіслати',
      histEmpty: 'Немає збережених розмов.<br/>Почни чат — вони збережуться автоматично.',
      gateSub: 'Введи e-mail і одразу почнемо чат.', gateBtn: 'Отримати доступ до Boomer',
      emailInvalid: 'Введи коректний e-mail.', sending: 'Надсилаю…', sendFail: 'Помилка надсилання. Спробуй ще раз.',
      otpTitle: '📬 Перевір пошту', otpSub: 'Ми надіслали 6-значний код на ', otpBtn: 'Підтвердити код',
      otpInvalid: 'Введи 6-значний код.', verifying: 'Перевіряю…', otpWrong: 'Неправильний код. Спробуй ще раз.',
      noReply: 'Вибач, не вдалося відповісти.', errGeneric: 'Сталася помилка. Спробуй пізніше.',
      errNet: 'Немає зʼєднання. Перевір інтернет і спробуй ще раз.',
      chipsHome: ['Що таке BOOOM?', 'Як встановити?', 'Це безкоштовно?', 'Для кого BOOOM?'],
      chipsDefault: ['Що таке BOOOM?', 'Як встановити?', 'Дієти та здоровʼя', 'Контакт'],
      follow: ['Розкажи більше', 'Як BOOOM мені допоможе?', 'Маю ще запитання']
    },
    DE: {
      locale: 'de-DE', today: 'Heute', yesterday: 'Gestern', convo: 'Unterhaltung ',
      bubble: 'Hallo, wie kann ich helfen?',
      bubbles: ['Hallo, wie kann ich helfen? 💪', 'Schick mir dein Bankdrück-Maximum und ich sage dir, wo Reserve ist. 💪', 'Was hält dich vom nächsten Rekord ab? Frag mich — ich bin rund um die Uhr da.'],
      greeting: 'Hallo! Ich bin Boomer, dein KI-Assistent 💪 Wie kann ich helfen?',
      openAria: 'Boomer-KI-Assistent öffnen', back: 'Zurück', history: 'Verlauf', histAria: 'Gesprächsverlauf',
      newChat: 'Neue Unterhaltung', close: 'Schließen', rename: 'Umbenennen',
      disclaimer: '&#9877;&#65039; Ich bin kein Arzt. Das sind Informationen, keine Beratung — sprich mit Fachleuten.',
      placeholder: 'Nachricht schreiben…', send: 'Senden',
      histEmpty: 'Keine gespeicherten Unterhaltungen.<br/>Schreib los, sie werden automatisch gespeichert.',
      gateSub: 'Gib deine E-Mail ein und wir können sofort chatten.', gateBtn: 'Zugang zu Boomer erhalten',
      emailInvalid: 'Gib eine gültige E-Mail ein.', sending: 'Wird gesendet…', sendFail: 'Senden fehlgeschlagen. Versuch es noch einmal.',
      otpTitle: '📬 Prüf deine E-Mail', otpSub: 'Wir haben einen 6-stelligen Code geschickt an ', otpBtn: 'Code prüfen',
      otpInvalid: 'Gib den 6-stelligen Code ein.', verifying: 'Prüfe…', otpWrong: 'Falscher Code. Versuch es noch einmal.',
      noReply: 'Sorry, darauf konnte ich nicht antworten.', errGeneric: 'Etwas ist schiefgelaufen. Versuch es später.',
      errNet: 'Verbindung fehlgeschlagen. Prüf dein Internet und versuch es noch einmal.',
      chipsHome: ['Was ist BOOOM?', 'Wie installiere ich es?', 'Ist es kostenlos?', 'Für wen ist BOOOM?'],
      chipsDefault: ['Was ist BOOOM?', 'Wie installiere ich es?', 'Ernährung & Gesundheit', 'Kontakt'],
      follow: ['Erzähl mir mehr', 'Wie hilft mir BOOOM?', 'Ich habe noch eine Frage']
    }
  };
  function bubbles() { return lang() === 'SK' ? BUBBLE_MSGS : S().bubbles; }

  var supabaseClient = null;
  var displayMessages = [];      // {role:'user'|'bot', text:string}
  var chatHistory = [];          // API format, rebuilt before each fetch
  var userEmail = localStorage.getItem(LS_EMAIL) || null;
  var pendingEmail = '';
  var isPanelOpen = false;
  var chatInitialised = false;
  var currentConvoId = null;

  // ── Supabase (loaded on demand) ────────────────────────────────────────────
  // supabase-js is ~170 kB and is only needed for the email sign-in step. Someone who never
  // opens the chat, or already has an email stored, should not pay for it on every page view.
  // window.loadSupabase is shared with the testimonials block on the home page.
  var SB_SRC = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js';
  function loadSupabaseLib() {
    if (window.supabase && window.supabase.createClient) return Promise.resolve();
    if (window.__sbLoading) return window.__sbLoading;
    window.__sbLoading = new Promise(function (resolve, reject) {
      var el = document.createElement('script');
      el.src = SB_SRC;
      el.onload = function () { resolve(); };
      el.onerror = function () { window.__sbLoading = null; reject(new Error('supabase-js failed to load')); };
      document.head.appendChild(el);
    });
    return window.__sbLoading;
  }
  window.loadSupabase = loadSupabaseLib;
  function getClient() {
    return loadSupabaseLib().then(function () {
      if (!supabaseClient) supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
      return supabaseClient;
    });
  }
  function track(name, params) { if (window.boomTrack) window.boomTrack(name, params); }

  // ── Conversation persistence ───────────────────────────────────────────────
  function loadConversations() {
    try { return JSON.parse(localStorage.getItem(LS_CONVOS) || '[]'); }
    catch (e) { return []; }
  }

  function saveConversations(convos) {
    try { localStorage.setItem(LS_CONVOS, JSON.stringify(convos)); } catch (e) {}
  }

  function ensureConvoId() {
    if (!currentConvoId) currentConvoId = 'convo_' + Date.now();
  }

  function generateConvoName() {
    for (var i = 0; i < displayMessages.length; i++) {
      if (displayMessages[i].role === 'user') {
        var t = displayMessages[i].text;
        return t.length > 34 ? t.substring(0, 34) + '…' : t;
      }
    }
    return S().convo + new Date().toLocaleDateString(S().locale);
  }

  function saveCurrentConversation() {
    if (!chatInitialised || displayMessages.length === 0) return;
    ensureConvoId();
    var convos = loadConversations();
    var idx = -1;
    for (var i = 0; i < convos.length; i++) {
      if (convos[i].id === currentConvoId) { idx = i; break; }
    }
    var snapshot = displayMessages.slice(-MAX_DISPLAY);
    if (idx !== -1) {
      convos[idx].messages = snapshot;
      convos[idx].date = new Date().toISOString();
    } else {
      convos.unshift({
        id: currentConvoId,
        name: generateConvoName(),
        messages: snapshot,
        date: new Date().toISOString()
      });
      if (convos.length > 50) convos.length = 50;
    }
    saveConversations(convos);
  }

  function renameConversation(id, newName) {
    var convos = loadConversations();
    for (var i = 0; i < convos.length; i++) {
      if (convos[i].id === id) { convos[i].name = newName; break; }
    }
    saveConversations(convos);
  }

  function rebuildApiHistory() {
    chatHistory = [];
    var slice = displayMessages.slice(-MAX_API_CTX);
    for (var i = 0; i < slice.length; i++) {
      chatHistory.push({
        role: slice[i].role === 'user' ? 'user' : 'assistant',
        content: slice[i].text
      });
    }
  }

  // ── Initial chips ──────────────────────────────────────────────────────────
  function getInitialChips() {
    var p = window.location.pathname;
    // Page-specific chips exist in Slovak only (the pages are Slovak); other languages get the general set.
    if (lang() !== 'SK') return (p === '/' || p === '' || /\/index\.html$/.test(p) || /^\/(en|cs|pl|uk|de)\/?$/.test(p)) ? S().chipsHome : S().chipsDefault;
    if (p === '/' || p === '' || p === '/index.html')
      return ['Čo je BOOOM?', 'Ako nainštalovať?', 'Je to zadarmo?', 'Pre koho je BOOOM?'];
    if (p.indexOf('stitna-zlaza') !== -1)
      return ['Čo je hypotyreóza?', 'Strava pri štítnej žľaze', 'Môžem cvičiť?', 'Ako mi BOOOM pomôže?'];
    if (p.indexOf('bezlaktozova') !== -1)
      return ['Čo môžem jesť?', 'Príznaky intolerancie', 'Laktóza a šport', 'Ako sledovať v BOOOM?'];
    if (p.indexOf('bezlepkova') !== -1)
      return ['Čo je celiaká?', 'Skryté zdroje lepku', 'Bezlepková strava a šport', 'Ako mi BOOOM pomôže?'];
    if (p.indexOf('hashimoto') !== -1)
      return ['Čo je Hashimoto?', 'Strava pri Hashimoto', 'Cvičenie pri Hashimoto', 'Ako mi BOOOM pomôže?'];
    if (p.indexOf('histaminova') !== -1)
      return ['Čo je histamínová intolerancia?', 'Čo môžem jesť?', 'Príznaky', 'Ako mi BOOOM pomôže?'];
    return ['Čo je BOOOM?', 'Ako nainštalovať?', 'Diéty a zdravie', 'Kontakt'];
  }

  // ── Follow-up chips ────────────────────────────────────────────────────────
  function getFollowUpChips(botReply, userMsg) {
    if (lang() !== 'SK') return S().follow;
    var ctx = ((botReply || '') + ' ' + (userMsg || '')).toLowerCase();
    if (/strava|jedlo|jedn|proteín|kalóri|makro|jedálniček/.test(ctx))
      return ['Koľko proteínu denne?', 'Čo jesť pred tréningom?', 'Ako sledovať makrá?'];
    if (/cvič|tréning|workout|silový|kardio|pohyb/.test(ctx))
      return ['Ako často cvičiť?', 'Cvičenie pri mojom stave?', 'Odporúčaný plán?'];
    if (/hashimoto|štítna|tyreoíd|hypotyreóz/.test(ctx))
      return ['Aké potraviny vynechať?', 'Cvičenie pri Hashimoto?', 'Ako mi BOOOM pomôže?'];
    if (/histamín|intolerancia|alergi/.test(ctx))
      return ['Čo môžem jesť?', 'Histamín a šport?', 'Ako sledovať v BOOOM?'];
    if (/laktóza|bezlaktóz|mlieko|mliečn/.test(ctx))
      return ['Náhrady mlieka?', 'Laktóza a šport?', 'Bezlaktózový jedálniček?'];
    if (/lepok|celiak|bezlepk|gluten/.test(ctx))
      return ['Skryté zdroje lepku?', 'Bezlepkový jedálniček?', 'Šport pri celiakii?'];
    if (/booom|app|aplikáci|inštaláci|zadarmo/.test(ctx))
      return ['Ako nainštalovať?', 'Je to zadarmo?', 'Čo všetko sleduje?'];
    return ['Povedz mi viac', 'Ako mi BOOOM pomôže?', 'Mám ďalšiu otázku'];
  }

  // ── CSS injection ──────────────────────────────────────────────────────────
  function injectCSS() {
    var style = document.createElement('style');
    style.id = 'boomer-chat-styles';
    style.textContent = [
      /* Floating button */
      '#boomer-btn{position:fixed;bottom:24px;right:24px;width:56px;height:56px;border-radius:50%;border:2px solid #00ff88;background:#0d0d0d;cursor:pointer;z-index:9999;padding:0;overflow:hidden;box-shadow:0 0 12px rgba(0,255,136,0.6);animation:boomer-pulse 3s ease-in-out infinite;transition:transform 0.2s;flex-shrink:0;}',
      '#boomer-btn:hover{transform:scale(1.08);}',
      '#boomer-btn img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block;}',
      '@keyframes boomer-pulse{0%,100%{box-shadow:0 0 8px rgba(0,255,136,0.4);}50%{box-shadow:0 0 22px rgba(0,255,136,0.9),0 0 40px rgba(0,255,136,0.2);}}',

      /* Speech bubble */
      '#boomer-bubble{position:fixed;bottom:32px;right:92px;background:#0d0d0d;border:1px solid #00ff88;border-radius:12px;padding:8px 12px;font-size:12px;color:#fff;white-space:normal;max-width:230px;line-height:1.5;z-index:9998;font-family:"Inter",-apple-system,sans-serif;pointer-events:none;transition:opacity 0.45s ease;}',
      '#boomer-bubble::after{content:"";position:absolute;right:-7px;top:50%;transform:translateY(-50%);border:6px solid transparent;border-left-color:#00ff88;border-right-width:0;}',

      /* Panel */
      '#boomer-panel{position:fixed;bottom:0;right:24px;width:370px;max-height:560px;background:#0d0d0d;border-top:2px solid #00ff88;border-left:1px solid #1e1e1e;border-right:1px solid #1e1e1e;border-radius:16px 16px 0 0;z-index:10000;display:flex;flex-direction:column;font-family:"Inter",-apple-system,sans-serif;transform:translateY(100%);transition:transform 0.32s cubic-bezier(0.4,0,0.2,1);overflow:hidden;}',
      '#boomer-panel.open{transform:translateY(0);}',

      /* Header */
      '.boomer-header{display:flex;align-items:center;gap:8px;padding:12px 14px;border-bottom:1px solid #1e1e1e;flex-shrink:0;}',
      '.boomer-header-avatar{width:36px;height:36px;border-radius:50%;border:1.5px solid #00ff88;object-fit:cover;flex-shrink:0;}',
      '.boomer-header-info{flex:1;min-width:0;}',
      '.boomer-header-name{font-size:14px;font-weight:700;color:#00ff88;line-height:1.2;}',
      '.boomer-header-sub{font-size:11px;color:#888;}',
      '.boomer-icon-btn{background:none;border:1px solid #2a2a2a;color:#888;width:28px;height:28px;border-radius:7px;cursor:pointer;display:flex;align-items:center;justify-content:center;font-family:inherit;transition:border-color 0.15s,color 0.15s;flex-shrink:0;padding:0;}',
      '.boomer-icon-btn:hover{border-color:#555;color:#fff;}',
      '.boomer-icon-btn.active{border-color:#00ff88;color:#00ff88;}',

      /* Disclaimer */
      '.boomer-disclaimer{background:rgba(255,255,255,0.03);border-bottom:1px solid #1e1e1e;padding:7px 14px;font-size:11px;color:#666;flex-shrink:0;line-height:1.4;}',

      /* Body */
      '.boomer-body{flex:1;overflow-y:auto;padding:12px 14px;display:flex;flex-direction:column;gap:10px;min-height:0;}',
      '.boomer-body::-webkit-scrollbar{width:4px;}',
      '.boomer-body::-webkit-scrollbar-track{background:transparent;}',
      '.boomer-body::-webkit-scrollbar-thumb{background:#2a2a2a;border-radius:4px;}',

      /* Email gate */
      '.boomer-gate{display:flex;flex-direction:column;gap:12px;padding:4px 0;}',
      '.boomer-gate-title{font-size:13px;font-weight:700;color:#fff;}',
      '.boomer-gate-sub{font-size:12px;color:#888;margin-top:-6px;line-height:1.5;}',
      '.boomer-input{width:100%;background:#111;border:1px solid #2a2a2a;border-radius:10px;padding:10px 12px;font-size:13px;color:#fff;font-family:inherit;outline:none;box-sizing:border-box;transition:border-color 0.15s;}',
      '.boomer-input:focus{border-color:#00ff88;}',
      '.boomer-submit-btn{background:linear-gradient(135deg,#00e676,#00d4ff);color:#000;font-weight:800;font-size:13px;border:none;border-radius:10px;padding:10px;cursor:pointer;font-family:inherit;transition:opacity 0.2s;width:100%;}',
      '.boomer-submit-btn:hover{opacity:0.88;}',
      '.boomer-submit-btn:disabled{opacity:0.5;cursor:not-allowed;}',
      '.boomer-error{font-size:12px;color:#ff5252;line-height:1.4;}',

      /* Messages */
      '.boomer-msg{display:flex;gap:8px;align-items:flex-end;}',
      '.boomer-msg.user{flex-direction:row-reverse;}',
      '.boomer-msg-avatar{width:26px;height:26px;border-radius:50%;object-fit:cover;flex-shrink:0;}',
      '.boomer-msg-bubble{max-width:80%;padding:8px 12px;border-radius:12px;font-size:13px;line-height:1.55;word-break:break-word;}',
      '.boomer-msg.bot .boomer-msg-bubble{background:#161616;color:rgba(255,255,255,0.88);border-radius:12px 12px 12px 2px;}',
      '.boomer-msg.user .boomer-msg-bubble{background:linear-gradient(135deg,#00e676,#00d4ff);color:#000;font-weight:600;border-radius:12px 12px 2px 12px;}',

      /* Chips */
      '.boomer-chips{display:flex;flex-wrap:wrap;gap:6px;padding:2px 0;}',
      '.boomer-chip{background:rgba(0,255,136,0.07);border:1px solid rgba(0,255,136,0.28);color:rgba(255,255,255,0.8);font-size:11px;font-weight:600;padding:5px 10px;border-radius:100px;cursor:pointer;font-family:inherit;transition:background 0.15s,border-color 0.15s;text-align:left;}',
      '.boomer-chip:hover{background:rgba(0,255,136,0.18);border-color:#00ff88;}',

      /* Typing */
      '.boomer-typing{display:flex;gap:5px;align-items:center;padding:4px 2px;}',
      '.boomer-typing span{width:7px;height:7px;border-radius:50%;background:#00ff88;animation:boomer-dot 1.2s ease-in-out infinite;display:inline-block;}',
      '.boomer-typing span:nth-child(2){animation-delay:0.2s;}',
      '.boomer-typing span:nth-child(3){animation-delay:0.4s;}',
      '@keyframes boomer-dot{0%,60%,100%{transform:translateY(0);opacity:0.4;}30%{transform:translateY(-5px);opacity:1;}}',

      /* Footer input */
      '.boomer-footer{border-top:1px solid #1e1e1e;padding:10px 12px;display:flex;gap:8px;align-items:center;flex-shrink:0;}',
      '.boomer-text-input{flex:1;background:#111;border:1px solid #2a2a2a;border-radius:10px;padding:9px 12px;font-size:13px;color:#fff;font-family:inherit;outline:none;transition:border-color 0.15s;min-width:0;}',
      '.boomer-text-input:focus{border-color:#00ff88;}',
      '.boomer-send-btn{background:linear-gradient(135deg,#00e676,#00d4ff);border:none;border-radius:10px;width:36px;height:36px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:opacity 0.2s;padding:0;}',
      '.boomer-send-btn:hover{opacity:0.85;}',
      '.boomer-send-btn:disabled{opacity:0.4;cursor:not-allowed;}',
      '.boomer-send-btn svg{width:16px;height:16px;}',

      /* History panel — slides in from left over main content */
      '#boomer-history-panel{position:absolute;inset:0;background:#0d0d0d;z-index:5;display:flex;flex-direction:column;transform:translateX(-100%);transition:transform 0.28s cubic-bezier(0.4,0,0.2,1);}',
      '#boomer-history-panel.open{transform:translateX(0);}',
      '.boomer-hist-header{display:flex;align-items:center;gap:8px;padding:12px 14px;border-bottom:1px solid #1e1e1e;flex-shrink:0;}',
      '.boomer-hist-title{flex:1;font-size:13px;font-weight:700;color:#fff;letter-spacing:0.2px;}',
      '.boomer-hist-body{flex:1;overflow-y:auto;padding:4px 0 12px;}',
      '.boomer-hist-body::-webkit-scrollbar{width:4px;}',
      '.boomer-hist-body::-webkit-scrollbar-track{background:transparent;}',
      '.boomer-hist-body::-webkit-scrollbar-thumb{background:#2a2a2a;border-radius:4px;}',
      '.boomer-hist-date{font-size:10px;color:#444;padding:10px 14px 4px;text-transform:uppercase;letter-spacing:0.8px;}',
      '.boomer-hist-item{display:flex;align-items:center;gap:6px;padding:9px 14px;cursor:pointer;transition:background 0.15s;border-left:2px solid transparent;}',
      '.boomer-hist-item:hover{background:rgba(255,255,255,0.04);}',
      '.boomer-hist-item.active{background:rgba(0,255,136,0.06);border-left-color:#00ff88;}',
      '.boomer-hist-name{flex:1;font-size:12px;color:#aaa;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0;line-height:1.4;}',
      '.boomer-hist-item.active .boomer-hist-name{color:#00ff88;}',
      '.boomer-hist-edit{background:none;border:none;color:#3a3a3a;cursor:pointer;padding:3px 5px;border-radius:4px;font-size:12px;flex-shrink:0;line-height:1;transition:color 0.15s;}',
      '.boomer-hist-edit:hover{color:#00ff88;}',
      '.boomer-hist-rename{flex:1;background:#111;border:1px solid #00ff88;border-radius:6px;padding:3px 8px;font-size:12px;color:#fff;font-family:inherit;outline:none;min-width:0;}',
      '.boomer-hist-empty{padding:32px 14px;font-size:13px;color:#444;text-align:center;line-height:1.6;}',

      /* Mobile */
      '@media(max-width:480px){#boomer-panel{right:0;width:100%;border-radius:16px 16px 0 0;max-height:75vh;border-left:none;border-right:none;}#boomer-bubble{display:none;}}'
    ].join('');
    document.head.appendChild(style);
  }

  // ── HTML injection ─────────────────────────────────────────────────────────
  function injectHTML() {
    var bubble = document.createElement('div');
    bubble.id = 'boomer-bubble';
    bubble.textContent = S().bubble;
    document.body.appendChild(bubble);

    var btn = document.createElement('button');
    btn.id = 'boomer-btn';
    btn.setAttribute('aria-label', S().openAria);
    btn.innerHTML = '<img src="' + AVATAR_URL + '" alt="Boomer AI" />';
    document.body.appendChild(btn);

    var panel = document.createElement('div');
    panel.id = 'boomer-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Boomer AI asistent');
    panel.innerHTML =
      /* ── History overlay ── */
      '<div id="boomer-history-panel" aria-hidden="true">' +
        '<div class="boomer-hist-header">' +
          '<button class="boomer-icon-btn" id="boomer-hist-back" aria-label="' + S().back + '" style="font-size:16px;">&#8592;</button>' +
          '<span class="boomer-hist-title">' + S().history + '</span>' +
          '<button class="boomer-icon-btn" id="boomer-hist-new" aria-label="' + S().newChat + '" style="font-size:20px;border-color:#00ff88;color:#00ff88;">+</button>' +
        '</div>' +
        '<div class="boomer-hist-body" id="boomer-hist-body"></div>' +
      '</div>' +
      /* ── Main chat ── */
      '<div class="boomer-header">' +
        '<img class="boomer-header-avatar" src="' + AVATAR_URL + '" alt="Boomer" />' +
        '<div class="boomer-header-info">' +
          '<div class="boomer-header-name">Boomer</div>' +
          '<div class="boomer-header-sub">AI asistent</div>' +
        '</div>' +
        /* History button (clock icon) */
        '<button class="boomer-icon-btn" id="boomer-hist-btn" aria-label="' + S().histAria + '" title="' + S().history + '">' +
          '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>' +
        '</button>' +
        /* New chat button */
        '<button class="boomer-icon-btn" id="boomer-newchat-btn" aria-label="' + S().newChat + '" title="' + S().newChat + '" style="font-size:18px;">+</button>' +
        '<button class="boomer-icon-btn" id="boomer-close" aria-label="' + S().close + '" style="font-size:14px;">&#x2715;</button>' +
      '</div>' +
      '<div class="boomer-disclaimer">' + S().disclaimer + '</div>' +
      '<div class="boomer-body" id="boomer-body"></div>' +
      '<div class="boomer-footer" id="boomer-footer" style="display:none">' +
        '<input class="boomer-text-input" id="boomer-text-input" type="text" placeholder="' + S().placeholder + '" autocomplete="off" />' +
        '<button class="boomer-send-btn" id="boomer-send-btn" aria-label="' + S().send + '">' +
          '<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">' +
            '<line x1="22" y1="2" x2="11" y2="13"></line>' +
            '<polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>' +
          '</svg>' +
        '</button>' +
      '</div>';
    document.body.appendChild(panel);
  }

  // ── Utilities ──────────────────────────────────────────────────────────────
  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function showError(el, msg) { el.textContent = msg; el.style.display = 'block'; }

  function scrollBody() {
    var b = document.getElementById('boomer-body');
    if (b) b.scrollTop = b.scrollHeight;
  }

  // ── History panel ──────────────────────────────────────────────────────────
  function openHistory() {
    renderHistoryList();
    var hp = document.getElementById('boomer-history-panel');
    var hb = document.getElementById('boomer-hist-btn');
    if (hp) { hp.classList.add('open'); hp.setAttribute('aria-hidden', 'false'); }
    if (hb) hb.classList.add('active');
  }

  function closeHistory() {
    var hp = document.getElementById('boomer-history-panel');
    var hb = document.getElementById('boomer-hist-btn');
    if (hp) { hp.classList.remove('open'); hp.setAttribute('aria-hidden', 'true'); }
    if (hb) hb.classList.remove('active');
  }

  function groupLabel(isoDate) {
    var d = new Date(isoDate);
    var now = new Date();
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate()).getTime();
    var dDay = new Date(d.getFullYear(), d.getMonth(), d.getDate()).getTime();
    if (dDay === today) return S().today;
    if (dDay === today - 86400000) return S().yesterday;
    return d.toLocaleDateString(S().locale, { day: 'numeric', month: 'long' });
  }

  function renderHistoryList() {
    var body = document.getElementById('boomer-hist-body');
    if (!body) return;
    var convos = loadConversations();
    if (convos.length === 0) {
      body.innerHTML = '<div class="boomer-hist-empty">' + S().histEmpty + '</div>';
      return;
    }

    var groups = {}, groupOrder = [];
    for (var i = 0; i < convos.length; i++) {
      var lbl = groupLabel(convos[i].date);
      if (!groups[lbl]) { groups[lbl] = []; groupOrder.push(lbl); }
      groups[lbl].push(convos[i]);
    }

    var html = '';
    for (var g = 0; g < groupOrder.length; g++) {
      var gl = groupOrder[g];
      html += '<div><div class="boomer-hist-date">' + escapeHtml(gl) + '</div>';
      var items = groups[gl];
      for (var j = 0; j < items.length; j++) {
        var c = items[j];
        var active = c.id === currentConvoId ? ' active' : '';
        html +=
          '<div class="boomer-hist-item' + active + '" data-id="' + escapeHtml(c.id) + '">' +
            '<span class="boomer-hist-name">' + escapeHtml(c.name) + '</span>' +
            '<button class="boomer-hist-edit" data-id="' + escapeHtml(c.id) + '" data-name="' + escapeHtml(c.name) + '" aria-label="' + S().rename + '" title="Premenovať">&#x270F;</button>' +
          '</div>';
      }
      html += '</div>';
    }
    body.innerHTML = html;

    body.querySelectorAll('.boomer-hist-item').forEach(function (item) {
      item.addEventListener('click', function (e) {
        if (e.target.classList.contains('boomer-hist-edit')) return;
        loadConversation(item.getAttribute('data-id'));
      });
    });

    body.querySelectorAll('.boomer-hist-edit').forEach(function (editBtn) {
      editBtn.addEventListener('click', function (e) {
        e.stopPropagation();
        startRename(editBtn);
      });
    });
  }

  function startRename(editBtn) {
    var id = editBtn.getAttribute('data-id');
    var origName = editBtn.getAttribute('data-name');
    var item = editBtn.parentElement;
    var nameEl = item.querySelector('.boomer-hist-name');

    nameEl.style.display = 'none';
    editBtn.style.display = 'none';

    var input = document.createElement('input');
    input.type = 'text';
    input.value = origName;
    input.className = 'boomer-hist-rename';
    item.insertBefore(input, editBtn);
    input.focus();
    input.select();

    function commit() {
      var newName = input.value.trim() || origName;
      renameConversation(id, newName);
      nameEl.textContent = newName;
      nameEl.style.display = '';
      editBtn.setAttribute('data-name', newName);
      editBtn.style.display = '';
      if (input.parentElement) input.parentElement.removeChild(input);
    }

    input.addEventListener('blur', commit);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); input.blur(); }
      if (e.key === 'Escape') { input.value = origName; input.blur(); }
    });
  }

  function loadConversation(id) {
    saveCurrentConversation();
    var convos = loadConversations();
    var convo = null;
    for (var i = 0; i < convos.length; i++) {
      if (convos[i].id === id) { convo = convos[i]; break; }
    }
    if (!convo) return;

    currentConvoId = convo.id;
    displayMessages = convo.messages ? convo.messages.slice() : [];
    rebuildApiHistory();
    closeHistory();

    var body = document.getElementById('boomer-body');
    var footer = document.getElementById('boomer-footer');
    body.innerHTML = '';
    for (var i = 0; i < displayMessages.length; i++) {
      appendMessageToDOM(displayMessages[i].role, displayMessages[i].text);
    }
    footer.style.display = 'flex';
    scrollBody();
  }

  function startNewChat() {
    saveCurrentConversation();
    currentConvoId = 'convo_' + Date.now();
    displayMessages = [];
    chatHistory = [];
    closeHistory();

    var body = document.getElementById('boomer-body');
    var footer = document.getElementById('boomer-footer');
    body.innerHTML = '';
    if (!chatInitialised) {
      showChat();
    } else {
      footer.style.display = 'flex';
      renderFreshGreeting();
    }
  }

  // ── Email gate ─────────────────────────────────────────────────────────────
  function showEmailGate() {
    var body = document.getElementById('boomer-body');
    body.innerHTML =
      '<div class="boomer-gate">' +
        '<div class="boomer-gate-title">👋 Ahoj! Som Boomer.</div>' +
        '<div class="boomer-gate-sub">' + S().gateSub + '</div>' +
        '<input class="boomer-input" id="boomer-email-input" type="email" placeholder="tvoj@email.com" autocomplete="email" />' +
        '<button class="boomer-submit-btn" id="boomer-email-btn">' + S().gateBtn + '</button>' +
        '<div class="boomer-error" id="boomer-gate-error" style="display:none"></div>' +
      '</div>';

    var emailBtn = document.getElementById('boomer-email-btn');
    var emailInput = document.getElementById('boomer-email-input');
    emailBtn.addEventListener('click', submitEmail);
    emailInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') submitEmail(); });
    setTimeout(function () { emailInput.focus(); }, 50);
  }

  function submitEmail() {
    var emailInput = document.getElementById('boomer-email-input');
    var btn = document.getElementById('boomer-email-btn');
    var errEl = document.getElementById('boomer-gate-error');
    if (!emailInput || !btn) return;

    var email = emailInput.value.trim();
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      showError(errEl, S().emailInvalid);
      return;
    }

    btn.disabled = true;
    btn.textContent = S().sending;
    errEl.style.display = 'none';

    getClient().then(function (sb) { return sb.auth.signInWithOtp({ email: email, options: { shouldCreateUser: true } }); })
      .then(function (result) {
        if (result.error) throw result.error;
        pendingEmail = email;
        showOtpGate();
      })
      .catch(function (err) {
        btn.disabled = false;
        btn.textContent = S().gateBtn;
        showError(errEl, err.message || S().sendFail);
      });
  }

  function showOtpGate() {
    var body = document.getElementById('boomer-body');
    body.innerHTML =
      '<div class="boomer-gate">' +
        '<div class="boomer-gate-title">' + S().otpTitle + '</div>' +
        '<div class="boomer-gate-sub">' + S().otpSub + '<strong style="color:#fff">' + escapeHtml(pendingEmail) + '</strong></div>' +
        '<input class="boomer-input" id="boomer-otp-input" type="text" inputmode="numeric" maxlength="6" placeholder="123456" autocomplete="one-time-code" />' +
        '<button class="boomer-submit-btn" id="boomer-otp-btn">' + S().otpBtn + '</button>' +
        '<div class="boomer-error" id="boomer-otp-error" style="display:none"></div>' +
      '</div>';

    var otpBtn = document.getElementById('boomer-otp-btn');
    var otpInput = document.getElementById('boomer-otp-input');
    otpBtn.addEventListener('click', verifyOtp);
    otpInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') verifyOtp(); });
    setTimeout(function () { otpInput.focus(); }, 50);
  }

  function verifyOtp() {
    var tokenInput = document.getElementById('boomer-otp-input');
    var btn = document.getElementById('boomer-otp-btn');
    var errEl = document.getElementById('boomer-otp-error');
    if (!tokenInput || !btn) return;

    var token = tokenInput.value.trim();
    if (!token || token.length < 6) {
      showError(errEl, S().otpInvalid);
      return;
    }

    btn.disabled = true;
    btn.textContent = S().verifying;
    errEl.style.display = 'none';

    getClient().then(function (sb) { return sb.auth.verifyOtp({ email: pendingEmail, token: token, type: 'email' }); })
      .then(function (result) {
        if (result.error) throw result.error;
        return supabaseClient.from('landing_leads').upsert(
          { email: pendingEmail, source_page: window.location.pathname },
          { onConflict: 'email', ignoreDuplicates: true }
        );
      })
      .then(function () {
        localStorage.setItem(LS_EMAIL, pendingEmail);
        userEmail = pendingEmail;
        track('generate_lead', { method: 'boomer_chat', page: window.location.pathname });
        showChat();
      })
      .catch(function (err) {
        var b2 = document.getElementById('boomer-otp-btn');
        if (b2) { b2.disabled = false; b2.textContent = S().otpBtn; }
        var e2 = document.getElementById('boomer-otp-error');
        if (e2) showError(e2, err.message || S().otpWrong);
      });
  }

  // ── Chat view ──────────────────────────────────────────────────────────────
  function renderFreshGreeting() {
    var body = document.getElementById('boomer-body');
    var chips = getInitialChips();
    var chipsHtml = chips.map(function (c) {
      return '<button class="boomer-chip" data-msg="' + escapeHtml(c) + '">' + escapeHtml(c) + '</button>';
    }).join('');

    var greet = document.createElement('div');
    greet.className = 'boomer-msg bot';
    greet.innerHTML =
      '<img class="boomer-msg-avatar" src="' + AVATAR_URL + '" alt="Boomer" />' +
      '<div class="boomer-msg-bubble">' + S().greeting + '</div>';
    body.appendChild(greet);

    var chipsEl = document.createElement('div');
    chipsEl.className = 'boomer-chips';
    chipsEl.id = 'boomer-chips';
    chipsEl.innerHTML = chipsHtml;
    body.appendChild(chipsEl);

    chipsEl.querySelectorAll('.boomer-chip').forEach(function (chip) {
      chip.addEventListener('click', function () { sendMessage(chip.getAttribute('data-msg')); });
    });
  }

  function showChat() {
    var footer = document.getElementById('boomer-footer');
    var body = document.getElementById('boomer-body');

    // Wire input handlers exactly once
    if (!chatInitialised) {
      chatInitialised = true;
      var textInput = document.getElementById('boomer-text-input');
      var sendBtn = document.getElementById('boomer-send-btn');
      function handleSend() {
        var val = textInput.value.trim();
        if (val) sendMessage(val);
      }
      sendBtn.addEventListener('click', handleSend);
      textInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') handleSend(); });
    }

    footer.style.display = 'flex';
    body.innerHTML = '';
    ensureConvoId();

    // Resume most recent saved conversation if any
    var convos = loadConversations();
    if (convos.length > 0 && convos[0].messages && convos[0].messages.length > 0) {
      currentConvoId = convos[0].id;
      displayMessages = convos[0].messages.slice();
      rebuildApiHistory();
      for (var i = 0; i < displayMessages.length; i++) {
        appendMessageToDOM(displayMessages[i].role, displayMessages[i].text);
      }
      scrollBody();
    } else {
      renderFreshGreeting();
    }
  }

  function appendMessageToDOM(role, text) {
    var body = document.getElementById('boomer-body');
    var msg = document.createElement('div');
    msg.className = 'boomer-msg ' + role;
    if (role === 'bot') {
      msg.innerHTML =
        '<img class="boomer-msg-avatar" src="' + AVATAR_URL + '" alt="Boomer" />' +
        '<div class="boomer-msg-bubble">' + escapeHtml(text) + '</div>';
    } else {
      msg.innerHTML = '<div class="boomer-msg-bubble">' + escapeHtml(text) + '</div>';
    }
    body.appendChild(msg);
    return msg;
  }

  function appendMessage(role, text) {
    displayMessages.push({ role: role, text: text });
    if (displayMessages.length > MAX_DISPLAY) displayMessages = displayMessages.slice(-MAX_DISPLAY);
    var msg = appendMessageToDOM(role, text);
    scrollBody();
    return msg;
  }

  function showFollowUpChips(botReply, userMsg) {
    var body = document.getElementById('boomer-body');
    var chips = getFollowUpChips(botReply, userMsg);
    var chipsEl = document.createElement('div');
    chipsEl.className = 'boomer-chips';
    chips.forEach(function (c) {
      var chip = document.createElement('button');
      chip.className = 'boomer-chip';
      chip.textContent = c;
      chip.addEventListener('click', function () {
        if (chipsEl.parentElement) chipsEl.parentElement.removeChild(chipsEl);
        sendMessage(c);
      });
      chipsEl.appendChild(chip);
    });
    body.appendChild(chipsEl);
    scrollBody();
  }

  function showTyping() {
    var body = document.getElementById('boomer-body');
    var el = document.createElement('div');
    el.className = 'boomer-msg bot';
    el.id = 'boomer-typing';
    el.innerHTML =
      '<img class="boomer-msg-avatar" src="' + AVATAR_URL + '" alt="Boomer" />' +
      '<div class="boomer-msg-bubble boomer-typing"><span></span><span></span><span></span></div>';
    body.appendChild(el);
    scrollBody();
  }

  function removeTyping() {
    var el = document.getElementById('boomer-typing');
    if (el) el.parentNode.removeChild(el);
  }

  function sendMessage(text) {
    var textInput = document.getElementById('boomer-text-input');
    var sendBtn = document.getElementById('boomer-send-btn');
    var chipsEl = document.getElementById('boomer-chips');

    if (chipsEl && chipsEl.parentElement) chipsEl.parentElement.removeChild(chipsEl);
    if (textInput) textInput.value = '';
    if (sendBtn) sendBtn.disabled = true;

    appendMessage('user', text);
    rebuildApiHistory();
    showTyping();

    fetch(EDGE_FN, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + SUPABASE_ANON_KEY },
      body: JSON.stringify({ messages: chatHistory, userEmail: userEmail, sourcePage: window.location.pathname, lang: lang().toLowerCase() })
    })
      .then(function (resp) {
        return resp.json().then(function (data) { return { ok: resp.ok, data: data }; });
      })
      .then(function (result) {
        removeTyping();
        var reply = result.ok
          ? (result.data.response || S().noReply)
          : (result.data.error || S().errGeneric);
        appendMessage('bot', reply);
        if (result.ok) {
          saveCurrentConversation();
          showFollowUpChips(reply, text);
        }
      })
      .catch(function () {
        removeTyping();
        appendMessage('bot', S().errNet);
      })
      .then(function () {
        if (sendBtn) sendBtn.disabled = false;
      });
  }

  // ── Panel open / close ─────────────────────────────────────────────────────
  function openPanel() {
    isPanelOpen = true;
    document.getElementById('boomer-panel').classList.add('open');
    var bubble = document.getElementById('boomer-bubble');
    if (bubble) bubble.style.opacity = '0';

    track('boomer_open', { page: window.location.pathname });
    var body = document.getElementById('boomer-body');
    if (!userEmail) {
      loadSupabaseLib().catch(function () {});   // warm it up while the gate is read
      if (body.childElementCount === 0) showEmailGate();
    } else if (!chatInitialised) {
      showChat();
    }
  }

  function closePanel() {
    isPanelOpen = false;
    closeHistory();
    document.getElementById('boomer-panel').classList.remove('open');
    var bubble = document.getElementById('boomer-bubble');
    if (bubble) bubble.style.opacity = '1';
  }

  // ── Hide button/bubble on external input focus ─────────────────────────────
  function onFocusIn(e) {
    var tag = e.target && e.target.tagName;
    if (tag !== 'INPUT' && tag !== 'TEXTAREA') return;
    var panel = document.getElementById('boomer-panel');
    if (panel && panel.contains(e.target)) return;
    var btn = document.getElementById('boomer-btn');
    var bubble = document.getElementById('boomer-bubble');
    if (btn) { btn.style.opacity = '0'; btn.style.pointerEvents = 'none'; }
    if (bubble) bubble.style.opacity = '0';
  }

  function onFocusOut(e) {
    var tag = e.target && e.target.tagName;
    if (tag !== 'INPUT' && tag !== 'TEXTAREA') return;
    var panel = document.getElementById('boomer-panel');
    if (panel && panel.contains(e.target)) return;
    var btn = document.getElementById('boomer-btn');
    var bubble = document.getElementById('boomer-bubble');
    if (btn) { btn.style.opacity = '1'; btn.style.pointerEvents = 'auto'; }
    if (bubble && !isPanelOpen) bubble.style.opacity = '1';
  }

  // ── Bootstrap ──────────────────────────────────────────────────────────────
  function setup() {
    injectCSS();
    injectHTML();

    document.getElementById('boomer-btn').addEventListener('click', function () {
      if (isPanelOpen) closePanel(); else openPanel();
    });
    document.getElementById('boomer-close').addEventListener('click', closePanel);
    document.getElementById('boomer-hist-btn').addEventListener('click', openHistory);
    document.getElementById('boomer-hist-back').addEventListener('click', closeHistory);
    document.getElementById('boomer-hist-new').addEventListener('click', startNewChat);
    document.getElementById('boomer-newchat-btn').addEventListener('click', function () {
      if (chatInitialised) startNewChat();
    });

    document.addEventListener('click', function (e) {
      if (!isPanelOpen) return;
      var panel = document.getElementById('boomer-panel');
      var btn = document.getElementById('boomer-btn');
      if (!panel.contains(e.target) && !btn.contains(e.target)) closePanel();
    });

    document.addEventListener('focusin', onFocusIn);
    document.addEventListener('focusout', onFocusOut);

    /* Rotate bubble messages every 8 seconds */
    setInterval(function () {
      var bubble = document.getElementById('boomer-bubble');
      if (!bubble || isPanelOpen) return;
      bubble.style.opacity = '0';
      setTimeout(function () {
        bubbleIdx = (bubbleIdx + 1) % bubbles().length;
        bubble.textContent = bubbles()[bubbleIdx];
        bubble.style.opacity = '1';
      }, 460);
    }, 8000);
  }

  function init() { setup(); }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
