# About page ("O nás" / "About") in sk / en / cs. Rendered by make_blog.py (build_about) to
#   o-nas.html, en/about.html, cs/o-nas.html
# Facts come from the founder's story on the home page (lang.js story_*). No surname, no photo and
# no qualification claim on purpose: the page says openly that this is a practical point of view.
# Section tuples: (id, h2, html body). The figures are the ones already public on the home page.
SOCIALS = [
    ('Instagram', 'https://www.instagram.com/booom_fitness_app'),
    ('TikTok', 'https://www.tiktok.com/@booom.fitness.app'),
    ('Facebook', 'https://www.facebook.com/booom.fit'),
]
SOCIALS_EN = [
    ('Instagram', 'https://www.instagram.com/booom_fitness_app'),
    ('TikTok', 'https://www.tiktok.com/@getbooom'),
    ('Facebook', 'https://www.facebook.com/booom.fit'),
]
EMAIL = 'laco@booom.fit'

ABOUT = {
    'sk': dict(
        path='o-nas.html', route='/o-nas', label='O nás',
        title_tag='O nás — kto stojí za BOOOM a prečo vznikol | BOOOM',
        og_title='O nás — kto stojí za BOOOM',
        h1='O nás: kto stojí za BOOOM a prečo vznikol',
        crumb='O nás',
        desc='BOOOM vytvoril Laco po vlastnej skúsenosti s nediagnostikovanou štítnou žľazou. Bez predstieranej odbornosti, zadarmo a bez postranných úmyslov.',
        kw='o nás BOOOM, kto stojí za BOOOM, príbeh zakladateľa, fitness appka zadarmo, tréningový denník',
        lead='BOOOM je fitness denník, ktorý spája tréning, výživu, regeneráciu a krvné hodnoty do jedného obrazu. Vznikol z jednej vlastnej skúsenosti, nie zo štúdie trhu.',
        sections=[
            ('kto-som', 'Kto som', '''<p>Volám sa Laco a BOOOM som vytvoril ja. Športujem odmalička. Od desiatich rokov som robil kanoistiku na Draždiaku a Dunaji, neskôr som prešiel na silový tréning.</p>
      <p>Aj po konci športovej kariéry som pokračoval v gyme. Trénoval som štyri až päťkrát týždenne, poctivo, s jedlom pod kontrolou (mal som vlastnú reštauráciu). A výsledky prichádzali: benchpress 165 kg, mŕtvy ťah 200 kg, drep 180 kg. Bol som na svojom silovom vrchole a myslel som si, že mám všetko vyriešené.</p>'''),
            ('ked-to-prestalo-fungovat', 'Keď to prestalo fungovať', '''<p>Vo veku okolo 35 až 38 rokov sa to začalo lámať. Trénoval som rovnako, jedol rovnako, no priberal som. Ráno som vstával dolámaný, cez deň som bojoval s hmlou v hlave a ospalosťou. Skúšal som všetko, čo sa dalo: fasting, detoxy, tvrdé low-carb diéty. Nič nezaberalo a nikto mi nevedel povedať prečo. Keď váha ukázala 127,6 kg, bol som na dne. Vinu som hádzal na stres a prácu.</p>
      <p>Nakoniec ma na krvné testy doslova dotlačil kamarát z gymu. Endokrinológ zistil, že moja štítna žľaza funguje na približne 10 % a že mám Hashimotovu tyreoiditídu. Nebol som lenivý a nemal som slabú vôľu. Bol som chorý a nevedel som o tom.</p>'''),
            ('preco-booom', 'Prečo BOOOM', '''<p>Vtedy mi chýbal nástroj, ktorý by mi ukázal súvislosti medzi tréningom, jedlom, spánkom a krvnými hodnotami. Nie ďalšia appka, ktorá povie, koľko kalórií má avokádo, ale denník, ktorý ťa naučí sledovať vlastné telo ako celok. Keby som ho mal, ušetril by som si roky frustrácie.</p>
      <p>Celý príbeh nájdeš na <a href="/#story">hlavnej stránke</a>.</p>'''),
            ('zadarmo', 'Zadarmo, bez háčikov', '''<p>BOOOM je celý zadarmo. Žiadne balíčky, žiadne predplatné, žiadne poplatky a žiadne zľavové kódy. Nič ti nepredávam a nemám za tým žiadny postranný úmysel. Vytvoril som to, lebo som také niečo sám potreboval, a chcem, aby to malo k dispozícii každý, kto sa točí v tom istom kruhu ako ja kedysi.</p>'''),
            ('co-najdes', 'Čo v BOOOM nájdeš', '''<ul>
        <li>tréningový denník s automatickým sledovaním osobných rekordov, XP a ranky</li>
        <li>AI tréner Boomer</li>
        <li>Hyrox simulátor so splitmi v reálnom čase</li>
        <li>skener čiarových kódov, kalórie a makrá</li>
        <li>AI odhad zloženia tela z fotiek</li>
        <li>sledovanie 36 krvných parametrov</li>
        <li>podpora hodiniek (Wear OS, Apple Watch)</li>
      </ul>'''),
            ('na-rovinu', 'Na rovinu', '''<p>Nie som lekár, tréner ani výživový poradca. Nemám žiadny certifikát, len roky praxe a vlastnú skúsenosť. Preto tu nájdeš kalkulačky a články, ktoré vychádzajú z bežne prijímaných odporúčaní, a vždy uvádzame, kde ide len o odhad. Nič z toho nenahrádza lekára. Ak niečo dlhodobo nehrá, choď na krvné testy. Mne to zachránilo zdravie.</p>'''),
        ],
        contact_h='Kontakt', contact_p='Napíš mi, prečítam si každú správu:', socials=SOCIALS,
        cta=('Vyskúšaj BOOOM', 'Tréningový denník, AI tréner, Hyrox simulátor a sledovanie výživy v jednej appke. Zadarmo pre iOS, Android aj web.'),
        note='Kto za BOOOM stojí a prečo o zdraví píšeme z praktického hľadiska, nájdeš na stránke <a href="/o-nas">O nás</a>.',
    ),
    'en': dict(
        path='en/about.html', route='/en/about', label='About',
        title_tag='About — who is behind BOOOM and why it exists | BOOOM',
        og_title='About — who is behind BOOOM',
        h1='About: who is behind BOOOM and why it exists',
        crumb='About',
        desc='BOOOM was built by Laco after his own experience with an undiagnosed thyroid problem. No pretend-expert credentials, free, and no hidden agenda.',
        kw='about BOOOM, who is behind BOOOM, founder story, free fitness app, workout log',
        lead='BOOOM is a fitness journal that brings training, nutrition, recovery and blood markers into one picture. It came out of one personal experience, not out of a market study.',
        sections=[
            ('who-i-am', 'Who I am', '''<p>My name is Laco and I built BOOOM. I have been an athlete since childhood. From the age of ten I did canoeing on the Danube, and later I moved on to strength training.</p>
      <p>Even after my sports career ended I kept going to the gym. I trained four to five times a week, properly, with my food under control (I owned a restaurant). And the results came: a 165 kg bench press, a 200 kg deadlift, a 180 kg squat. I was at my strength peak and I thought I had it all figured out.</p>'''),
            ('when-it-stopped-working', 'When it stopped working', '''<p>Somewhere around the age of 35 to 38 it started to fall apart. I trained the same, ate the same, and still gained weight. I woke up broken every morning and fought brain fog and sleepiness all day. I tried everything: fasting, detoxes, harsh low-carb diets. Nothing worked and nobody could tell me why. When the scale showed 127.6 kg (about 281 lb), I hit rock bottom. I blamed stress and work.</p>
      <p>In the end a friend from the gym practically pushed me into getting blood tests. The endocrinologist found that my thyroid was working at about 10 % and that I had Hashimoto's thyroiditis. I was not lazy and I did not lack willpower. I was sick and did not know it.</p>'''),
            ('why-booom', 'Why BOOOM', '''<p>What I was missing back then was a tool that would show me the connections between training, food, sleep and blood values. Not another app that tells you how many calories an avocado has, but a journal that teaches you to follow your own body as a whole. If I had had one, I would have saved myself years of frustration.</p>
      <p>You can read the whole story on the <a href="/en/#story">home page</a>.</p>'''),
            ('free', 'Free, no catch', '''<p>BOOOM is completely free. No packages, no subscriptions, no fees and no discount codes. I am not selling you anything and there is no hidden agenda behind it. I built it because I needed something like it myself, and I want it to be available to everyone who is going round in the same circle I once was.</p>'''),
            ('what-you-get', 'What you will find in BOOOM', '''<ul>
        <li>a workout log with automatic tracking of personal records, XP and ranks</li>
        <li>an AI coach called Boomer</li>
        <li>a Hyrox simulator with live splits</li>
        <li>a barcode scanner, calories and macros</li>
        <li>an AI body composition estimate from photos</li>
        <li>tracking of 36 blood markers</li>
        <li>watch support (Wear OS, Apple Watch)</li>
      </ul>'''),
            ('straight-talk', 'Straight talk', '''<p>I am not a doctor, a trainer or a nutrition adviser. I have no certificate, just years of practice and my own experience. That is why the calculators and articles here are based on widely accepted recommendations, and we always say where something is only an estimate. None of it replaces a doctor. If something has felt off for a long time, get blood tests done. It saved my health.</p>'''),
        ],
        contact_h='Contact', contact_p='Write to me, I read every message:', socials=SOCIALS_EN,
        cta=('Try BOOOM', 'Workout log, AI coach, Hyrox simulator and nutrition tracking in one app. Free for iOS, Android and the web.'),
        note='Who is behind BOOOM and why we write about health from a practical point of view: see the <a href="/en/about">About</a> page.',
    ),
    'cs': dict(
        path='cs/o-nas.html', route='/cs/o-nas', label='O nás',
        title_tag='O nás — kdo stojí za BOOOM a proč vznikl | BOOOM',
        og_title='O nás — kdo stojí za BOOOM',
        h1='O nás: kdo stojí za BOOOM a proč vznikl',
        crumb='O nás',
        desc='BOOOM vytvořil Laco po vlastní zkušenosti s nediagnostikovanou štítnou žlázou. Bez předstírané odbornosti, zdarma a bez postranních úmyslů.',
        kw='o nás BOOOM, kdo stojí za BOOOM, příběh zakladatele, fitness appka zdarma, tréninkový deník',
        lead='BOOOM je fitness deník, který spojuje trénink, výživu, regeneraci a krevní hodnoty do jednoho obrazu. Vznikl z jedné vlastní zkušenosti, ne ze studie trhu.',
        sections=[
            ('kdo-jsem', 'Kdo jsem', '''<p>Jmenuji se Laco a BOOOM jsem vytvořil já. Sportuji odmala. Od deseti let jsem dělal kanoistiku na Dunaji a později jsem přešel na silový trénink.</p>
      <p>I po konci sportovní kariéry jsem pokračoval v gymu. Trénoval jsem čtyřikrát až pětkrát týdně, poctivě, s jídlem pod kontrolou (měl jsem vlastní restauraci). A výsledky přicházely: benchpress 165 kg, mrtvý tah 200 kg, dřep 180 kg. Byl jsem na svém silovém vrcholu a myslel jsem si, že mám všechno vyřešené.</p>'''),
            ('kdyz-to-prestalo-fungovat', 'Když to přestalo fungovat', '''<p>Ve věku kolem 35 až 38 let se to začalo lámat. Trénoval jsem stejně, jedl jsem stejně, a přesto jsem přibíral. Ráno jsem vstával dolámaný, přes den jsem bojoval s mlhou v hlavě a ospalostí. Zkoušel jsem všechno, co šlo: fasting, detoxy, tvrdé low-carb diety. Nic nezabíralo a nikdo mi neuměl říct proč. Když váha ukázala 127,6 kg, byl jsem na dně. Vinu jsem házel na stres a práci.</p>
      <p>Nakonec mě na krevní testy doslova dotlačil kamarád z gymu. Endokrinolog zjistil, že moje štítná žláza funguje na přibližně 10 % a že mám Hashimotovu tyreoiditidu. Nebyl jsem líný a neměl jsem slabou vůli. Byl jsem nemocný a nevěděl jsem o tom.</p>'''),
            ('proc-booom', 'Proč BOOOM', '''<p>Tehdy mi chyběl nástroj, který by mi ukázal souvislosti mezi tréninkem, jídlem, spánkem a krevními hodnotami. Ne další appka, která řekne, kolik kalorií má avokádo, ale deník, který tě naučí sledovat vlastní tělo jako celek. Kdybych ho měl, ušetřil bych si roky frustrace.</p>
      <p>Celý příběh najdeš na <a href="/cs/#story">hlavní stránce</a>.</p>'''),
            ('zdarma', 'Zdarma, bez háčků', '''<p>BOOOM je celý zdarma. Žádné balíčky, žádné předplatné, žádné poplatky a žádné slevové kódy. Nic ti neprodávám a nemám za tím žádný postranní úmysl. Vytvořil jsem to, protože jsem něco takového sám potřeboval, a chci, aby to měl k dispozici každý, kdo se točí ve stejném kruhu jako já kdysi.</p>'''),
            ('co-najdes', 'Co v BOOOM najdeš', '''<ul>
        <li>tréninkový deník s automatickým sledováním osobních rekordů, XP a ranků</li>
        <li>AI trenér Boomer</li>
        <li>Hyrox simulátor se splity v reálném čase</li>
        <li>skener čárových kódů, kalorie a makra</li>
        <li>AI odhad složení těla z fotek</li>
        <li>sledování 36 krevních parametrů</li>
        <li>podpora hodinek (Wear OS, Apple Watch)</li>
      </ul>'''),
            ('na-rovinu', 'Na rovinu', '''<p>Nejsem lékař, trenér ani výživový poradce. Nemám žádný certifikát, jen roky praxe a vlastní zkušenost. Proto tu najdeš kalkulačky a články, které vycházejí z běžně přijímaných doporučení, a vždy uvádíme, kde jde jen o odhad. Nic z toho nenahrazuje lékaře. Pokud něco dlouhodobě nehraje, jdi na krevní testy. Mně to zachránilo zdraví.</p>'''),
        ],
        contact_h='Kontakt', contact_p='Napiš mi, přečtu si každou zprávu:', socials=SOCIALS,
        cta=('Vyzkoušej BOOOM', 'Tréninkový deník, AI trenér, Hyrox simulátor a sledování výživy v jedné appce. Zdarma pro iOS, Android i web.'),
        note='Kdo za BOOOM stojí a proč o zdraví píšeme z praktického hlediska, najdeš na stránce <a href="/cs/o-nas">O nás</a>.',
    ),
}
