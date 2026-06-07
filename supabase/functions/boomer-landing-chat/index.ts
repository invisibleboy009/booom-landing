import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
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
    const { messages, userEmail, sourcePage } = await req.json()

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
          JSON.stringify({ error: 'Dosiahol si denný limit 20 správ. Ďakujeme za záujem o BOOOM! 💪' }),
          { status: 429, headers: { ...corsHeaders, 'Content-Type': 'application/json' } },
        )
      }
    }

    // ── Anthropic call ─────────────────────────────────────────────────────
    const systemPrompt =
      'Si Boomer, AI asistent fitness aplikácie BOOOM (booom.fit). ' +
      'Odpovedáš v slovenčine, stručne (max 4 vety), priateľsky s emoji. ' +
      'Pomáhaš s: fitness, diétami (bezlepková, bezlaktózová, histamínová, Hashimoto), ' +
      'štítnou žľazou, inštaláciou BOOOM PWA appky. ' +
      'Pri zdravotných otázkach vždy dodaj: nie si lekár, odporúčaj konzultáciu s odborníkom. ' +
      'BOOOM je zadarmo na app.booom.fit.'

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
