(function () {
  'use strict';

  var SUPABASE_URL = 'https://itwnqpggvcramyckoyiw.supabase.co';
  var SUPABASE_ANON_KEY = 'sb_publishable_kEM_LigU1HXZhw4Agu48LQ_BHYdWVYw';
  var AVATAR_URL = 'https://itwnqpggvcramyckoyiw.supabase.co/storage/v1/object/public/avatars/AI%20Coach%20Booomer.png';
  var EDGE_FN = SUPABASE_URL + '/functions/v1/boomer-landing-chat';

  var supabaseClient = null;
  var chatHistory = [];
  var userEmail = localStorage.getItem('boomer_email') || null;
  var pendingEmail = '';
  var isPanelOpen = false;
  var chatInitialised = false;

  // ── Supabase init ──────────────────────────────────────────────────────────
  function initSupabase() {
    if (window.supabase && window.supabase.createClient) {
      supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
      return true;
    }
    return false;
  }

  // ── Contextual chips ───────────────────────────────────────────────────────
  function getChips() {
    var p = window.location.pathname;
    if (p === '/' || p === '' || p === '/index.html') {
      return ['Čo je BOOOM?', 'Ako nainštalovať?', 'Je to zadarmo?', 'Pre koho je BOOOM?'];
    }
    if (p.indexOf('stitna-zlaza') !== -1) {
      return ['Čo je hypotyreóza?', 'Strava pri štítnej žľaze', 'Môžem cvičiť?', 'Ako mi BOOOM pomôže?'];
    }
    if (p.indexOf('bezlaktozova') !== -1) {
      return ['Čo môžem jesť?', 'Príznaky intolerancie', 'Laktóza a šport', 'Ako sledovať v BOOOM?'];
    }
    if (p.indexOf('bezlepkova') !== -1) {
      return ['Čo je celiaká?', 'Skryté zdroje lepku', 'Bezlepková strava a šport', 'Ako mi BOOOM pomôže?'];
    }
    if (p.indexOf('hashimoto') !== -1) {
      return ['Čo je Hashimoto?', 'Strava pri Hashimoto', 'Cvičenie pri Hashimoto', 'Ako mi BOOOM pomôže?'];
    }
    if (p.indexOf('histaminova') !== -1) {
      return ['Čo je histamínová intolerancia?', 'Čo môžem jesť?', 'Príznaky', 'Ako mi BOOOM pomôže?'];
    }
    return ['Čo je BOOOM?', 'Ako nainštalovať?', 'Diéty a zdravie', 'Kontakt'];
  }

  // ── CSS injection ──────────────────────────────────────────────────────────
  function injectCSS() {
    var style = document.createElement('style');
    style.id = 'boomer-chat-styles';
    style.textContent = [
      /* ── Floating button ── */
      '#boomer-btn{position:fixed;bottom:24px;right:24px;width:56px;height:56px;border-radius:50%;border:2px solid #00ff88;background:#0d0d0d;cursor:pointer;z-index:9999;padding:0;overflow:hidden;box-shadow:0 0 12px rgba(0,255,136,0.6);animation:boomer-pulse 3s ease-in-out infinite;transition:transform 0.2s;flex-shrink:0;}',
      '#boomer-btn:hover{transform:scale(1.08);}',
      '#boomer-btn img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block;}',
      '@keyframes boomer-pulse{0%,100%{box-shadow:0 0 8px rgba(0,255,136,0.4);}50%{box-shadow:0 0 22px rgba(0,255,136,0.9),0 0 40px rgba(0,255,136,0.2);}}',

      /* ── Speech bubble ── */
      '#boomer-bubble{position:fixed;bottom:32px;right:92px;background:#0d0d0d;border:1px solid #00ff88;border-radius:12px;padding:6px 10px;font-size:12px;color:#fff;white-space:nowrap;z-index:9998;font-family:"Inter",-apple-system,sans-serif;pointer-events:none;transition:opacity 0.25s;}',
      '#boomer-bubble::after{content:"";position:absolute;right:-7px;top:50%;transform:translateY(-50%);border:6px solid transparent;border-left-color:#00ff88;border-right-width:0;}',

      /* ── Panel ── */
      '#boomer-panel{position:fixed;bottom:0;right:24px;width:370px;max-height:560px;background:#0d0d0d;border-top:2px solid #00ff88;border-left:1px solid #1e1e1e;border-right:1px solid #1e1e1e;border-radius:16px 16px 0 0;z-index:10000;display:flex;flex-direction:column;font-family:"Inter",-apple-system,sans-serif;transform:translateY(100%);transition:transform 0.32s cubic-bezier(0.4,0,0.2,1);overflow:hidden;}',
      '#boomer-panel.open{transform:translateY(0);}',

      /* ── Header ── */
      '.boomer-header{display:flex;align-items:center;gap:10px;padding:12px 14px;border-bottom:1px solid #1e1e1e;flex-shrink:0;}',
      '.boomer-header-avatar{width:36px;height:36px;border-radius:50%;border:1.5px solid #00ff88;object-fit:cover;flex-shrink:0;}',
      '.boomer-header-info{flex:1;min-width:0;}',
      '.boomer-header-name{font-size:14px;font-weight:700;color:#00ff88;line-height:1.2;}',
      '.boomer-header-sub{font-size:11px;color:#888;}',
      '.boomer-close-btn{background:none;border:1px solid #2a2a2a;color:#888;width:28px;height:28px;border-radius:7px;cursor:pointer;font-size:14px;display:flex;align-items:center;justify-content:center;font-family:inherit;transition:border-color 0.15s,color 0.15s;flex-shrink:0;line-height:1;}',
      '.boomer-close-btn:hover{border-color:#555;color:#fff;}',

      /* ── Disclaimer ── */
      '.boomer-disclaimer{background:rgba(255,255,255,0.03);border-bottom:1px solid #1e1e1e;padding:7px 14px;font-size:11px;color:#666;flex-shrink:0;line-height:1.4;}',

      /* ── Body ── */
      '.boomer-body{flex:1;overflow-y:auto;padding:12px 14px;display:flex;flex-direction:column;gap:10px;min-height:0;}',
      '.boomer-body::-webkit-scrollbar{width:4px;}',
      '.boomer-body::-webkit-scrollbar-track{background:transparent;}',
      '.boomer-body::-webkit-scrollbar-thumb{background:#2a2a2a;border-radius:4px;}',

      /* ── Email gate ── */
      '.boomer-gate{display:flex;flex-direction:column;gap:12px;padding:4px 0;}',
      '.boomer-gate-title{font-size:13px;font-weight:700;color:#fff;}',
      '.boomer-gate-sub{font-size:12px;color:#888;margin-top:-6px;line-height:1.5;}',
      '.boomer-input{width:100%;background:#111;border:1px solid #2a2a2a;border-radius:10px;padding:10px 12px;font-size:13px;color:#fff;font-family:inherit;outline:none;box-sizing:border-box;transition:border-color 0.15s;}',
      '.boomer-input:focus{border-color:#00ff88;}',
      '.boomer-submit-btn{background:linear-gradient(135deg,#00e676,#00d4ff);color:#000;font-weight:800;font-size:13px;border:none;border-radius:10px;padding:10px;cursor:pointer;font-family:inherit;transition:opacity 0.2s;width:100%;}',
      '.boomer-submit-btn:hover{opacity:0.88;}',
      '.boomer-submit-btn:disabled{opacity:0.5;cursor:not-allowed;}',
      '.boomer-error{font-size:12px;color:#ff5252;line-height:1.4;}',

      /* ── Messages ── */
      '.boomer-msg{display:flex;gap:8px;align-items:flex-end;}',
      '.boomer-msg.user{flex-direction:row-reverse;}',
      '.boomer-msg-avatar{width:26px;height:26px;border-radius:50%;object-fit:cover;flex-shrink:0;}',
      '.boomer-msg-bubble{max-width:80%;padding:8px 12px;border-radius:12px;font-size:13px;line-height:1.55;word-break:break-word;}',
      '.boomer-msg.bot .boomer-msg-bubble{background:#161616;color:rgba(255,255,255,0.88);border-radius:12px 12px 12px 2px;}',
      '.boomer-msg.user .boomer-msg-bubble{background:linear-gradient(135deg,#00e676,#00d4ff);color:#000;font-weight:600;border-radius:12px 12px 2px 12px;}',

      /* ── Chips ── */
      '.boomer-chips{display:flex;flex-wrap:wrap;gap:6px;padding:2px 0;}',
      '.boomer-chip{background:rgba(0,255,136,0.07);border:1px solid rgba(0,255,136,0.28);color:rgba(255,255,255,0.8);font-size:11px;font-weight:600;padding:5px 10px;border-radius:100px;cursor:pointer;font-family:inherit;transition:background 0.15s,border-color 0.15s;text-align:left;}',
      '.boomer-chip:hover{background:rgba(0,255,136,0.18);border-color:#00ff88;}',

      /* ── Typing indicator ── */
      '.boomer-typing{display:flex;gap:5px;align-items:center;padding:4px 2px;}',
      '.boomer-typing span{width:7px;height:7px;border-radius:50%;background:#00ff88;animation:boomer-dot 1.2s ease-in-out infinite;display:inline-block;}',
      '.boomer-typing span:nth-child(2){animation-delay:0.2s;}',
      '.boomer-typing span:nth-child(3){animation-delay:0.4s;}',
      '@keyframes boomer-dot{0%,60%,100%{transform:translateY(0);opacity:0.4;}30%{transform:translateY(-5px);opacity:1;}}',

      /* ── Footer input ── */
      '.boomer-footer{border-top:1px solid #1e1e1e;padding:10px 12px;display:flex;gap:8px;align-items:center;flex-shrink:0;}',
      '.boomer-text-input{flex:1;background:#111;border:1px solid #2a2a2a;border-radius:10px;padding:9px 12px;font-size:13px;color:#fff;font-family:inherit;outline:none;transition:border-color 0.15s;min-width:0;}',
      '.boomer-text-input:focus{border-color:#00ff88;}',
      '.boomer-send-btn{background:linear-gradient(135deg,#00e676,#00d4ff);border:none;border-radius:10px;width:36px;height:36px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:opacity 0.2s;padding:0;}',
      '.boomer-send-btn:hover{opacity:0.85;}',
      '.boomer-send-btn:disabled{opacity:0.4;cursor:not-allowed;}',
      '.boomer-send-btn svg{width:16px;height:16px;}',

      /* ── Mobile ── */
      '@media(max-width:480px){#boomer-panel{right:0;width:100%;border-radius:16px 16px 0 0;max-height:75vh;border-left:none;border-right:none;}#boomer-bubble{display:none;}}'
    ].join('');
    document.head.appendChild(style);
  }

  // ── HTML injection ─────────────────────────────────────────────────────────
  function injectHTML() {
    var bubble = document.createElement('div');
    bubble.id = 'boomer-bubble';
    bubble.textContent = 'Ahoj, ako ti môžem pomôcť?';
    document.body.appendChild(bubble);

    var btn = document.createElement('button');
    btn.id = 'boomer-btn';
    btn.setAttribute('aria-label', 'Otvoriť Boomer AI asistenta');
    btn.innerHTML = '<img src="' + AVATAR_URL + '" alt="Boomer AI" />';
    document.body.appendChild(btn);

    var panel = document.createElement('div');
    panel.id = 'boomer-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Boomer AI asistent');
    panel.innerHTML =
      '<div class="boomer-header">' +
        '<img class="boomer-header-avatar" src="' + AVATAR_URL + '" alt="Boomer" />' +
        '<div class="boomer-header-info">' +
          '<div class="boomer-header-name">Boomer</div>' +
          '<div class="boomer-header-sub">AI asistent</div>' +
        '</div>' +
        '<button class="boomer-close-btn" id="boomer-close" aria-label="Zavrieť">&#x2715;</button>' +
      '</div>' +
      '<div class="boomer-disclaimer">&#9877;&#65039; Nie som lekár. Rady sú informačné — konzultuj s odborníkom.</div>' +
      '<div class="boomer-body" id="boomer-body"></div>' +
      '<div class="boomer-footer" id="boomer-footer" style="display:none">' +
        '<input class="boomer-text-input" id="boomer-text-input" type="text" placeholder="Napíš správu…" autocomplete="off" />' +
        '<button class="boomer-send-btn" id="boomer-send-btn" aria-label="Odoslať">' +
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
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function showError(el, msg) {
    el.textContent = msg;
    el.style.display = 'block';
  }

  function scrollBody() {
    var body = document.getElementById('boomer-body');
    if (body) body.scrollTop = body.scrollHeight;
  }

  // ── Email gate ─────────────────────────────────────────────────────────────
  function showEmailGate() {
    var body = document.getElementById('boomer-body');
    body.innerHTML =
      '<div class="boomer-gate">' +
        '<div class="boomer-gate-title">👋 Ahoj! Som Boomer.</div>' +
        '<div class="boomer-gate-sub">Zadaj email a hneď môžeme chatovať.</div>' +
        '<input class="boomer-input" id="boomer-email-input" type="email" placeholder="tvoj@email.com" autocomplete="email" />' +
        '<button class="boomer-submit-btn" id="boomer-email-btn">Získať prístup k Boomerovi</button>' +
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
      showError(errEl, 'Zadaj platný email.');
      return;
    }

    btn.disabled = true;
    btn.textContent = 'Odosiela sa…';
    errEl.style.display = 'none';

    supabaseClient.auth.signInWithOtp({ email: email, options: { shouldCreateUser: true } })
      .then(function (result) {
        if (result.error) throw result.error;
        pendingEmail = email;
        showOtpGate();
      })
      .catch(function (err) {
        btn.disabled = false;
        btn.textContent = 'Získať prístup k Boomerovi';
        showError(errEl, err.message || 'Chyba pri odoslaní. Skús znova.');
      });
  }

  function showOtpGate() {
    var body = document.getElementById('boomer-body');
    body.innerHTML =
      '<div class="boomer-gate">' +
        '<div class="boomer-gate-title">📬 Skontroluj email</div>' +
        '<div class="boomer-gate-sub">Poslali sme 6-miestny kód na <strong style="color:#fff">' + escapeHtml(pendingEmail) + '</strong></div>' +
        '<input class="boomer-input" id="boomer-otp-input" type="text" inputmode="numeric" maxlength="6" placeholder="123456" autocomplete="one-time-code" />' +
        '<button class="boomer-submit-btn" id="boomer-otp-btn">Overiť kód</button>' +
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
      showError(errEl, 'Zadaj 6-miestny kód.');
      return;
    }

    btn.disabled = true;
    btn.textContent = 'Overujem…';
    errEl.style.display = 'none';

    supabaseClient.auth.verifyOtp({ email: pendingEmail, token: token, type: 'email' })
      .then(function (result) {
        if (result.error) throw result.error;
        // Save lead (ignore if already exists)
        return supabaseClient.from('landing_leads').upsert(
          { email: pendingEmail, source_page: window.location.pathname },
          { onConflict: 'email', ignoreDuplicates: true }
        );
      })
      .then(function () {
        localStorage.setItem('boomer_email', pendingEmail);
        userEmail = pendingEmail;
        showChat();
      })
      .catch(function (err) {
        var otpBtn2 = document.getElementById('boomer-otp-btn');
        if (otpBtn2) { otpBtn2.disabled = false; otpBtn2.textContent = 'Overiť kód'; }
        var errEl2 = document.getElementById('boomer-otp-error');
        if (errEl2) showError(errEl2, err.message || 'Nesprávny kód. Skús znova.');
      });
  }

  // ── Chat view ──────────────────────────────────────────────────────────────
  function showChat() {
    if (chatInitialised) return;
    chatInitialised = true;

    var body = document.getElementById('boomer-body');
    var footer = document.getElementById('boomer-footer');

    var chips = getChips();
    var chipsHtml = chips.map(function (c) {
      return '<button class="boomer-chip" data-msg="' + escapeHtml(c) + '">' + escapeHtml(c) + '</button>';
    }).join('');

    body.innerHTML =
      '<div class="boomer-msg bot">' +
        '<img class="boomer-msg-avatar" src="' + AVATAR_URL + '" alt="Boomer" />' +
        '<div class="boomer-msg-bubble">Ahoj! Som Boomer, tvoj AI asistent 💪 Ako ti môžem pomôcť?</div>' +
      '</div>' +
      '<div class="boomer-chips" id="boomer-chips">' + chipsHtml + '</div>';

    footer.style.display = 'flex';

    body.querySelectorAll('.boomer-chip').forEach(function (chip) {
      chip.addEventListener('click', function () { sendMessage(chip.getAttribute('data-msg')); });
    });

    var textInput = document.getElementById('boomer-text-input');
    var sendBtn = document.getElementById('boomer-send-btn');

    function handleSend() {
      var val = textInput.value.trim();
      if (val) sendMessage(val);
    }
    sendBtn.addEventListener('click', handleSend);
    textInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') handleSend(); });
  }

  function appendMessage(role, text) {
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
    scrollBody();
    return msg;
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

    if (chipsEl) chipsEl.parentNode.removeChild(chipsEl);
    if (textInput) textInput.value = '';
    if (sendBtn) sendBtn.disabled = true;

    appendMessage('user', text);

    chatHistory.push({ role: 'user', content: text });
    if (chatHistory.length > 6) chatHistory = chatHistory.slice(-6);

    showTyping();

    fetch(EDGE_FN, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + SUPABASE_ANON_KEY
      },
      body: JSON.stringify({
        messages: chatHistory,
        userEmail: userEmail,
        sourcePage: window.location.pathname
      })
    })
      .then(function (resp) {
        return resp.json().then(function (data) {
          return { ok: resp.ok, data: data };
        });
      })
      .then(function (result) {
        removeTyping();
        var reply = result.ok
          ? (result.data.response || 'Prepáč, nepodarilo sa mi odpovedať.')
          : (result.data.error || 'Nastala chyba. Skús neskôr.');
        appendMessage('bot', reply);
        if (result.ok) {
          chatHistory.push({ role: 'assistant', content: reply });
          if (chatHistory.length > 6) chatHistory = chatHistory.slice(-6);
        }
      })
      .catch(function () {
        removeTyping();
        appendMessage('bot', 'Spojenie zlyhalo. Skontroluj internet a skús znova.');
      })
      .then(function () {
        if (sendBtn) sendBtn.disabled = false;
      });
  }

  // ── Panel open / close ─────────────────────────────────────────────────────
  function openPanel() {
    isPanelOpen = true;
    var panel = document.getElementById('boomer-panel');
    var bubble = document.getElementById('boomer-bubble');
    panel.classList.add('open');
    if (bubble) bubble.style.opacity = '0';

    var body = document.getElementById('boomer-body');
    if (!userEmail) {
      if (body.childElementCount === 0) showEmailGate();
    } else {
      showChat();
    }
  }

  function closePanel() {
    isPanelOpen = false;
    var panel = document.getElementById('boomer-panel');
    var bubble = document.getElementById('boomer-bubble');
    panel.classList.remove('open');
    if (bubble) bubble.style.opacity = '1';
  }

  // ── Hide button/bubble when external input focused ─────────────────────────
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

    document.addEventListener('click', function (e) {
      if (!isPanelOpen) return;
      var panel = document.getElementById('boomer-panel');
      var btn = document.getElementById('boomer-btn');
      if (!panel.contains(e.target) && !btn.contains(e.target)) closePanel();
    });

    document.addEventListener('focusin', onFocusIn);
    document.addEventListener('focusout', onFocusOut);
  }

  function init() {
    if (initSupabase()) {
      setup();
    } else {
      // CDN not ready yet — retry once
      setTimeout(function () {
        if (initSupabase()) {
          setup();
        } else {
          console.warn('Boomer: supabase-js not loaded.');
        }
      }, 600);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
