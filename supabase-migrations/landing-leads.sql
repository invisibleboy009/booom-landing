CREATE TABLE IF NOT EXISTS landing_leads (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  email text UNIQUE NOT NULL,
  source_page text,
  created_at timestamptz DEFAULT now(),
  chat_count integer DEFAULT 0
);

ALTER TABLE landing_leads ENABLE ROW LEVEL SECURITY;

CREATE POLICY "insert_lead" ON landing_leads
  FOR INSERT WITH CHECK (true);

CREATE POLICY "update_own_lead" ON landing_leads
  FOR UPDATE USING (email = current_setting('app.user_email', true));
