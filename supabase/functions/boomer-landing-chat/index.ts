// boomer-landing-chat — the Boomer chat widget on booom.fit (assets/js/boomer-chat.js).
// v33 (2026-09-19): the widget now sends `lang` (sk|en|cs|pl|uk|de) and Boomer answers in
// that language; before, the prompt hard-coded Slovak while the site had six languages.
// Deployed through the Supabase MCP (verify_jwt ON — the widget sends the anon key).
// This file is the source of record; keep it in sync with production.
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
}

const LANG_NAME: Record<string, string> = {
  sk: 'slovenčine', en: 'angličtine (English)', cs: 'češtine', pl: 'poľštine (polski)', uk: 'ukrajinčine (українська)', de: 'nemčine (Deutsch)',
}
const LIMIT_MSG: Record<string, string> = {
  sk: 'Dosiahol si denný limit 20 správ. Ďakujeme za záujem o BOOOM! 💪',
  en: 'You have reached the daily limit of 20 messages. Thanks for your interest in BOOOM! 💪',
  cs: 'Dosáhl jsi denního limitu 20 zpráv. Díky za zájem o BOOOM! 💪',
  pl: 'Osiągnąłeś dzienny limit 20 wiadomości. Dzięki za zainteresowanie BOOOM! 💪',
  uk: 'Ти досяг денного ліміту 20 повідомлень. Дякуємо за інтерес до BOOOM! 💪',
  de: 'Du hast das Tageslimit von 20 Nachrichten erreicht. Danke für dein Interesse an BOOOM! 💪',
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders })
  }

  if (req.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), {
      status: 405,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    })
  }

  try {
    const { messages, userEmail, sourcePage, lang: rawLang } = await req.json()
    const lang = typeof rawLang === 'string' && LANG_NAME[rawLang.toLowerCase()] ? rawLang.toLowerCase() : 'sk'

    if (!messages || !Array.isArray(messages) || messages.length === 0) {
      return new Response(JSON.stringify({ error: 'Invalid request: messages required' }), {
        status: 400,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      })
    }

    const supabaseUrl = Deno.env.get('SUPABASE_URL') ?? ''
    const serviceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
    const anthropicKey = Deno.env.get('ANTHROPIC_API_KEY') ?? ''

    if (!anthropicKey) {
      return new Response(JSON.stringify({ error: 'Service temporarily unavailable' }), {
        status: 503,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      })
    }

    const supabase = createClient(supabaseUrl, serviceRoleKey)

    // ── Rate limit: max 20 messages per email ──────────────────────────────
    let currentCount = 0
    if (userEmail) {
      const { data: lead } = await supabase
        .from('landing_leads')
        .select('chat_count')
        .eq('email', userEmail)
        .maybeSingle()

      currentCount = lead?.chat_count ?? 0

      if (currentCount >= 20) {
        return new Response(
          JSON.stringify({ error: LIMIT_MSG[lang] }),
          { status: 429, headers: { ...corsHeaders, 'Content-Type': 'application/json' } },
        )
      }
    }

    // ── Anthropic call ─────────────────────────────────────────────────────
    const systemPrompt =
      'Si Boomer, AI asistent fitness aplikácie BOOOM (booom.fit). ' +
      `Odpovedáš VŽDY v ${LANG_NAME[lang]}, aj keď ti používateľ píše iným jazykom. ` +
      'Stručne (max 4 vety), priateľsky s emoji. ' +
      'Pomáhaš s: fitness, diétami (bezlepková, bezlaktózová, histamínová, Hashimoto), ' +
      'štítnou žľazou, inštaláciou BOOOM PWA appky. ' +
      'Pri zdravotných otázkach vždy dodaj: nie si lekár, odporúčaj konzultáciu s odborníkom. ' +
      'BOOOM je zadarmo na app.booom.fit.' +
      (sourcePage ? ` Používateľ je na stránke ${String(sourcePage).slice(0, 80)}.` : '')

    // Keep last 6 messages, ensure valid roles for Anthropic
    const safeMessages = messages
      .slice(-6)
      .filter((m: { role: string; content: string }) => m.role === 'user' || m.role === 'assistant')
      .map((m: { role: string; content: string }) => ({
        role: m.role as 'user' | 'assistant',
        content: String(m.content).slice(0, 1000), // cap content length
      }))

    // Anthropic requires messages to alternate and start with user
    const validMessages = safeMessages.filter((_: unknown, i: number) => {
      if (i === 0) return safeMessages[0].role === 'user'
      return safeMessages[i].role !== safeMessages[i - 1].role
    })

    const anthropicResp = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': anthropicKey,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({
        model: 'claude-haiku-4-5-20251001',
        max_tokens: 300,
        system: systemPrompt,
        messages: validMessages.length > 0 ? validMessages : [{ role: 'user', content: messages[messages.length - 1]?.content ?? '' }],
      }),
    })

    if (!anthropicResp.ok) {
      const errText = await anthropicResp.text()
      console.error('Anthropic API error:', anthropicResp.status, errText)
      return new Response(JSON.stringify({ error: 'AI service error. Skús znova.' }), {
        status: 502,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      })
    }

    const aiData = await anthropicResp.json()
    const response: string = aiData.content?.[0]?.text ?? 'Prepáč, nepodarilo sa mi odpovedať. Skús znova.'

    // ── Increment chat_count ───────────────────────────────────────────────
    if (userEmail) {
      supabase
        .from('landing_leads')
        .update({ chat_count: currentCount + 1 })
        .eq('email', userEmail)
        .then(() => {}) // fire-and-forget
    }

    return new Response(JSON.stringify({ response }), {
      status: 200,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    })
  } catch (err) {
    console.error('Edge function error:', err)
    return new Response(JSON.stringify({ error: 'Internal server error' }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    })
  }
})
