# Slovak blog content (source of truth for /blog and /blog/*). The generator is blog-src/make_blog.py.
# Structure is shared by content_en.py and content_cs.py: keep the same article order and section ids.
# Run: python blog-src/make_blog.py   (then node build-i18n.mjs, and commit the generated html).

LANG = 'sk'
PREFIX = ''            # URL prefix of this language ('' for Slovak, '/en', '/cs')
UI = dict(
    html_lang='sk', og_locale='sk_SK', date_sk='20. septembra 2026',
    blog='Blog', home='BOOOM', toc='Obsah', toc_aria='Obsah článku', faq='Časté otázky',
    updated='Aktualizované', read='min čítania', privacy='Ochrana údajov',
    try_free='Vyskúšať zadarmo', try_web='Vyskúšať zadarmo vo webe',
    appstore='Stiahnuť v App Store', gplay='Získať v Google Play',
)
HUB = dict(
    title_tag='Blog — tréning, výživa a Hyrox | BOOOM',
    og_title='Blog BOOOM — tréning, výživa a Hyrox',
    h1='Blog BOOOM: tréning, výživa a Hyrox',
    desc='Blog BOOOM: praktické články o tréningovom denníku, progresívnom preťažení, bielkovinách a príprave na Hyrox. Zadarmo, bez vaty.',
    kw='fitness blog, tréningový denník, progresívne preťaženie, bielkoviny, hyrox príprava, BOOOM',
    lead='Praktické články bez vaty, ktoré ti pomôžu trénovať múdrejšie. K väčšine z nich nájdeš aj kalkulačku alebo nástroj priamo na webe.',
    cta=('Trénuj s BOOOM', 'Tréningový denník, AI tréner, Hyrox simulátor a sledovanie výživy v jednej appke. Zadarmo pre iOS, Android aj web.'),
)

DISC_HEALTH = '<p class="disc">Článok má informatívny charakter a nenahrádza radu lekára ani nutričného terapeuta. Pri zdravotných problémoch sa poraď s odborníkom.</p>'
DISC_TRAIN = '<p class="disc">Článok má informatívny charakter a nenahrádza osobného trénera ani lekára. Ak máš zdravotné problémy alebo zranenie, pred začatím náročného tréningu sa poraď s odborníkom.</p>'

ARTICLES = []

# ═══════════════════════════════════════ 1. Tréningový denník ═══════════════════════════════════
ARTICLES.append(dict(
    slug='treningovy-dennik',
    title='Tréningový denník: ako si ho viesť a prečo ti pomôže rásť',
    title_tag='Tréningový denník — ako si ho viesť a čo zapisovať | BOOOM',
    h1='Tréningový denník: ako si ho viesť a prečo ti pomôže rásť',
    crumb='Tréningový denník',
    desc='Čo si zapisovať do tréningového denníka, ako ho viesť krok za krokom a ako z neho vyčítať pokrok. Praktický návod pre silový tréning, Hyrox aj beh.',
    card='Čo zapisovať, ako to robiť v praxi a ako z čísel vyčítať, či skutočne napredujete.',
    kw='tréningový denník, ako si viesť tréningový denník, zápis tréningov, sledovanie pokroku, tréningový plán, silový tréning',
    lead='Väčšina ľudí si myslí, že si pamätá, koľko zdvihla minulý týždeň. Väčšina sa mýli. Tréningový denník je najlacnejší spôsob, ako z tréningu spraviť systém, ktorý dokáže rásť.',
    cta=('Zapisuj tréningy bez papiera', 'BOOOM si pamätá tvoje váhy a opakovania, sám ukáže osobné rekordy a odmení ťa XP. Tréningový denník, ktorý ťa neotravuje.'),
    disc=DISC_TRAIN,
    faq=[
        ('Koľko času zaberie zapisovanie tréningu?', 'Pri dobrom nástroji zhruba minútu až dve na celý tréning. Ak ti zápis zaberá viac, zjednoduš formát — zapisuj len to, čo naozaj používaš.'),
        ('Musím zapisovať aj ľahké tréningy a kardio?', 'Áno, aspoň v minime: dátum, druh aktivity a trvanie alebo vzdialenosť. Aj ľahké dni patria do obrazu o tom, koľko záťaže reálne zvládaš.'),
        ('Čo ak vynechám tréning alebo zápis?', 'Nič sa nedeje. Denník nie je súťaž v dokonalosti. Vynechaný deň nedobiehaj, len pokračuj v pláne. Dôležité je, aby ti zápisy prinášali informáciu, nie výčitky.'),
        ('Je lepšie zapisovať na papier alebo do appky?', 'Funguje oboje. Papier je rýchly a nič ťa nevyrušuje, appka vie sama počítať rekordy, objem a grafy. Najlepší denník je ten, ktorý si naozaj vedieš.'),
    ],
    sections=[
        ('preco', 'Prečo si zapisovať tréningy', '''    <p>Bez zápisov trénuješ podľa pocitu. Pocit je užitočný, ale nespoľahlivý: dobrý deň skreslí to, čo si zvládol, a únava skreslí naopak. Denník ti dáva dáta, ktoré nezávisia od nálady.</p>
    <ul>
      <li><strong>Vieš, čo máš dnes porážať.</strong> Rast sily stojí na postupnom pridávaní záťaže (viac v článku <a href="/blog/progresivne-pretazenie">Progresívne preťaženie</a>). Bez čísel z minulého tréningu nevieš, čo znamená „viac“.</li>
      <li><strong>Vidíš pokrok, aj keď ho v zrkadle nevidíš.</strong> Svaly rastú pomaly, no váhy a opakovania idú hore rýchlejšie a sú motivujúce.</li>
      <li><strong>Nájdeš príčinu, keď to nejde.</strong> Stagnácia, bolesť alebo únava majú stopu v dátach: menej spánku, viac objemu, vynechané jedlá.</li>
      <li><strong>Drží ťa pri návyku.</strong> Sebamonitorovanie patrí medzi najlepšie preskúmané techniky, ktoré pomáhajú dodržať nový zvyk.</li>
    </ul>'''),
        ('co', 'Čo zapisovať: minimum a bonusy', '''    <table>
      <thead><tr><th>Kategória</th><th>Čo si zapísať</th></tr></thead>
      <tbody>
        <tr><td><strong>Minimum (silový tréning)</strong></td><td>Dátum, cvik, váha, počet opakovaní, počet sérií</td></tr>
        <tr><td><strong>Veľmi užitočné</strong></td><td>Ako ťažká séria bola (RPE 1 až 10 alebo koľko opakovaní ti zostalo v zálohe), krátka poznámka k technike</td></tr>
        <tr><td><strong>Bonus</strong></td><td>Spánok, energia, telesná hmotnosť, obvody, fotky</td></tr>
        <tr><td><strong>Beh a Hyrox</strong></td><td>Vzdialenosť, čas, tempo, tep, splity jednotlivých behov a staníc</td></tr>
      </tbody>
    </table>
    <p>Začni minimom. Denník s desiatimi stĺpcami prestaneš viesť za dva týždne, denník s piatimi vydrží roky.</p>'''),
        ('ako', 'Ako si denník viesť v praxi', '''    <ol>
      <li><strong>Vyber si jeden formát a drž sa ho.</strong> Zošit, tabuľka alebo appka. Prepínanie medzi nimi je najčastejší dôvod, prečo sa denník rozpadne.</li>
      <li><strong>Pred tréningom pozri minulý záznam</strong> a stanov si cieľ na dnes: o opakovanie viac alebo o 2,5 kg viac.</li>
      <li><strong>Zapisuj hneď po sérii</strong>, nie večer z pamäti. Pamäť zaokrúhľuje nahor.</li>
      <li><strong>Pridaj poznámku, keď sa niečo stalo</strong> — bolelo rameno, zle si spal, zmenil si techniku.</li>
      <li><strong>Raz za týždeň si daj päť minút</strong> a prejdi si zápisy: čo rastie, čo stojí, čo treba zmeniť.</li>
    </ol>'''),
        ('progres', 'Ako z denníka vyčítať pokrok', '''    <p>Nesleduj všetko. Stačia tri veci:</p>
    <ul>
      <li><strong>Najlepšia séria v hlavných cvikoch.</strong> Z nej si vieš odhadnúť aj 1RM v <a href="/1rm-kalkulacka">1RM kalkulačke</a> a porovnať ho v čase.</li>
      <li><strong>Týždenný objem</strong> (série × opakovania × váha) pre každú svalovú skupinu. Rastie postupne, s občasným odľahčením.</li>
      <li><strong>Frekvenciu tréningov.</strong> Počet dokončených tréningov za týždeň je jednoduchý ukazovateľ konzistencie.</li>
    </ul>
    <div class="ex">
      <p><strong>Príklad: tlak na lavičke, 4 týždne, 3 série</strong></p>
      <table>
        <thead><tr><th>Týždeň</th><th>Váha</th><th>Opakovania v sériách</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>60 kg</td><td>8 / 8 / 7</td></tr>
          <tr><td>2</td><td>60 kg</td><td>9 / 8 / 8</td></tr>
          <tr><td>3</td><td>60 kg</td><td>10 / 9 / 8</td></tr>
          <tr><td>4</td><td>62,5 kg</td><td>8 / 8 / 7</td></tr>
        </tbody>
      </table>
      <p>Tri týždne pridávaš opakovania, v štvrtom pridáš váhu a začneš odznova. Bez denníka by si si to nepamätal.</p>
    </div>'''),
        ('chyby', 'Najčastejšie chyby', '''    <ul>
      <li><strong>Príliš zložitý formát.</strong> Ak zápis trvá dlhšie ako rozcvička, prestaneš.</li>
      <li><strong>Zapisuješ len rekordy.</strong> Bez priemerných dní nevidíš trend.</li>
      <li><strong>Denník nepoužívaš.</strong> Zápis je zbytočný, ak ho pred tréningom neotvoríš.</li>
      <li><strong>Nezaznamenáš zmenu podmienok.</strong> Iná lavička, iné činky, iný rozsah pohybu: bez poznámky tie čísla nepôjdu porovnať.</li>
    </ul>'''),
        ('forma', 'Papier, tabuľka alebo appka?', '''    <table>
      <thead><tr><th>Forma</th><th>Výhoda</th><th>Nevýhoda</th></tr></thead>
      <tbody>
        <tr><td>Zošit</td><td>Rýchly, nič ťa nevyrušuje</td><td>Žiadne grafy, ťažko sa v ňom hľadá</td></tr>
        <tr><td>Tabuľka</td><td>Vlastné vzorce, dá sa filtrovať</td><td>Na telefóne v posilňovni nepohodlná</td></tr>
        <tr><td>Appka</td><td>Predvyplní minulé váhy, sama počíta rekordy a objem</td><td>Treba si vybrať tú, ktorá ťa neotravuje</td></tr>
      </tbody>
    </table>
    <p>Aplikácia BOOOM je postavená práve na tomto: zapíšeš cvik, appka ti ukáže minulý výkon, sama vyhodnotí osobné rekordy a odmení ťa XP a ranky. Vyskúšať ju môžeš zadarmo aj vo webe.</p>'''),
    ],
))

# ═══════════════════════════════════════ 2. Progresívne preťaženie ══════════════════════════════
ARTICLES.append(dict(
    slug='progresivne-pretazenie',
    title='Progresívne preťaženie: ako pridávať váhu, aby si stále rástol',
    title_tag='Progresívne preťaženie — ako pridávať váhu a opakovania | BOOOM',
    h1='Progresívne preťaženie: ako pridávať váhu, aby si stále rástol',
    crumb='Progresívne preťaženie',
    desc='Čo je progresívne preťaženie, päť spôsobov, ako ho uplatniť, jednoduchá dvojitá progresia, RPE a čo robiť pri stagnácii. Praktický návod pre silový tréning.',
    card='Ako pridávať váhu, opakovania a objem tak, aby si rástol a nezdolala ťa stagnácia.',
    kw='progresívne preťaženie, ako pridávať váhu, dvojitá progresia, RPE, stagnácia v sile, deload, silový tréning',
    lead='Telo rastie, len keď ho k tomu dotlačíš. Ak robíš stále rovnaké série s rovnakou váhou, prestane sa prispôsobovať. Progresívne preťaženie je princíp, ktorý stojí za všetkými dobrými plánmi.',
    cta=('Nech sa progres počíta sám', 'BOOOM pri každom cviku ukáže, čo si zdvihol minule, a automaticky zaznamená nové rekordy. Ty len pridávaš.'),
    disc=DISC_TRAIN,
    faq=[
        ('Musím pridávať váhu každý tréning?', 'Nie. Začiatočníci môžu pridávať každý týždeň alebo dokonca každý tréning, pokročilí často len raz za niekoľko týždňov. Dôležitý je smer, nie rýchlosť.'),
        ('Čo ak nezvládnem pridať ani opakovanie?', 'Občasný slabší tréning je normálny. Ak sa to opakuje viac týždňov, skontroluj spánok, príjem kalórií a bielkovín (<a href="/blog/kolko-bielkovin-denne">koľko bielkovín denne</a>) a zváž odľahčený týždeň.'),
        ('Ako často mám robiť deload?', 'Orientačne raz za 4 až 8 týždňov alebo keď zaznamenáš dlhšie zhoršenie výkonu a únavu. Objem a záťaž zníž zhruba o tretinu až polovicu.'),
        ('Funguje progresívne preťaženie aj pri chudnutí?', 'Áno. V deficite je cieľom udržať silu, čo je signál, že nestrácaš sval. Pridávanie záťaže môže byť pomalšie, a to je v poriadku.'),
    ],
    sections=[
        ('co', 'Čo je progresívne preťaženie', '''    <p><strong>Progresívne preťaženie</strong> znamená postupne zvyšovať nárok, ktorý tréning kladie na telo. Svaly a nervový systém sa prispôsobia tomu, čo robíš. Ak nárok ostane rovnaký, prispôsobenie sa zastaví a s ním aj pokrok.</p>
    <p>Nemusíš pridávať váhu na tyči. Preťaženie sa dá zvyšovať viacerými spôsobmi a často je múdrejšie ich striedať.</p>'''),
        ('sposoby', 'Päť spôsobov, ako zvyšovať záťaž', '''    <table>
      <thead><tr><th>Spôsob</th><th>Ako to vyzerá</th></tr></thead>
      <tbody>
        <tr><td><strong>Váha</strong></td><td>Pridáš 1,25 až 5 kg na tyč</td></tr>
        <tr><td><strong>Opakovania</strong></td><td>Namiesto 8 spravíš 9 alebo 10 pri rovnakej váhe</td></tr>
        <tr><td><strong>Série</strong></td><td>Zo 3 sérií prejdeš na 4</td></tr>
        <tr><td><strong>Technika a rozsah</strong></td><td>Hlbší drep, pomalšia excentrická fáza, pauza dole</td></tr>
        <tr><td><strong>Hustota</strong></td><td>Rovnaká práca za kratší čas, kratšie pauzy</td></tr>
      </tbody>
    </table>'''),
        ('dvojita', 'Dvojitá progresia: najjednoduchšia metóda', '''    <p>Stanov si rozsah opakovaní, napríklad 8 až 12. Začni s váhou, s ktorou zvládneš dolnú hranicu vo všetkých sériách. Držíš tú istú váhu a pridávaš opakovania, kým nedosiahneš hornú hranicu vo všetkých sériách. Vtedy pridáš váhu a vrátiš sa na 8.</p>
    <div class="ex">
      <p><strong>Príklad: veslovanie s jednoručkou</strong></p>
      <table>
        <thead><tr><th>Týždeň</th><th>Váha</th><th>Opakovania (3 série)</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>24 kg</td><td>8 / 8 / 8</td></tr>
          <tr><td>2</td><td>24 kg</td><td>10 / 9 / 8</td></tr>
          <tr><td>3</td><td>24 kg</td><td>12 / 11 / 10</td></tr>
          <tr><td>4</td><td>24 kg</td><td>12 / 12 / 12</td></tr>
          <tr><td>5</td><td>26 kg</td><td>8 / 8 / 8 a znova</td></tr>
        </tbody>
      </table>
    </div>'''),
        ('kolko', 'O koľko pridávať', '''    <ul>
      <li><strong>Horné telo a izolované cviky:</strong> obvykle 1,25 až 2,5 kg.</li>
      <li><strong>Nohy a mŕtvy ťah:</strong> obvykle 2,5 až 5 kg.</li>
      <li><strong>Začiatočníci</strong> napredujú rýchlejšie, často každý týždeň. <strong>Pokročilí</strong> len raz za niekoľko týždňov, niekedy len o opakovanie.</li>
    </ul>
    <p>Ak nemáš malé kotúče, kúp si magnetické závažia po 0,5 až 1,25 kg. Malé skoky sú lepšie než stagnácia.</p>'''),
        ('rpe', 'RPE a rezerva v opakovaniach', '''    <p><strong>RPE</strong> (rate of perceived exertion) je škála 1 až 10, ako ťažká séria bola. RPE 10 znamená úplné zlyhanie, RPE 8 znamená, že ti v zálohe zostali asi dve opakovania. Tento údaj sa označuje aj ako <strong>RIR</strong> (reps in reserve).</p>
    <p>Väčšina pracovných sérií by mala končiť s rezervou 1 až 3 opakovania. Takto budeš dostatočne tlačiť na sval, no nebudeš sa zbytočne vyčerpávať. Do <a href="/blog/treningovy-dennik">tréningového denníka</a> si RPE zapisuj aspoň pri poslednej sérii cviku.</p>'''),
        ('deload', 'Odľahčený týždeň (deload)', '''    <p>Únava sa nazbiera rýchlejšie, než si myslíš. Raz za 4 až 8 týždňov, alebo keď ti výkon klesá niekoľko tréningov po sebe, zníž objem aj záťaž zhruba o tretinu až polovicu. Po týždni sa vrátiš s čerstvými silami a často prekonáš predchádzajúce rekordy.</p>'''),
        ('stagnacia', 'Čo robiť pri stagnácii', '''    <ol>
      <li><strong>Skontroluj spánok.</strong> Menej ako 7 hodín pravidelne sa prejaví na sile aj regenerácii.</li>
      <li><strong>Skontroluj príjem.</strong> Pri chronickom deficite sila stagnuje. Spočítaj si potrebu v <a href="/kalorie-kalkulacka">kalorickej kalkulačke</a> a bielkoviny podľa článku <a href="/blog/kolko-bielkovin-denne">Koľko bielkovín denne</a>.</li>
      <li><strong>Zmeň podnet.</strong> Iný rozsah opakovaní, variant cviku alebo tempo.</li>
      <li><strong>Skontroluj techniku.</strong> Natoč si sériu na video.</li>
      <li><strong>Daj si deload.</strong></li>
    </ol>
    <p>Aktuálnu silu si vieš orientačne odhadnúť v <a href="/1rm-kalkulacka">1RM kalkulačke</a> a po pár týždňoch porovnať.</p>'''),
    ],
))

# ═══════════════════════════════════════ 3. Koľko bielkovín denne ═══════════════════════════════
ARTICLES.append(dict(
    slug='kolko-bielkovin-denne',
    title='Koľko bielkovín denne potrebuješ (a ako si ich rozložiť)',
    title_tag='Koľko bielkovín denne — výpočet podľa váhy a cieľa | BOOOM',
    h1='Koľko bielkovín denne potrebuješ (a ako si ich rozložiť)',
    crumb='Koľko bielkovín denne',
    desc='Koľko bielkovín denne potrebuješ na svaly, chudnutie aj bežný život. Tabuľka podľa váhy, potraviny s bielkovinami, vzorový deň a najčastejšie mýty.',
    card='Tabuľka podľa váhy a cieľa, obsah bielkovín v bežných potravinách a vzorový deň.',
    kw='koľko bielkovín denne, bielkoviny na kg, príjem bielkovín, bielkoviny na chudnutie, bielkoviny a svaly, proteín',
    lead='Číslo, ktoré poznáš z posilňovne, je „2 gramy na kilo“. Je to rozumný odhad, no nie vždy a nie pre každého. Tu je, prečo, kedy stačí menej a ako si bielkoviny rozložiť počas dňa.',
    cta=('Zapisuj jedlo aj makrá jednoducho', 'BOOOM má skener čiarových kódov, databázu potravín a denný cieľ bielkovín podľa tvojej váhy.'),
    disc=DISC_HEALTH,
    faq=[
        ('Musím piť proteínový nápoj?', 'Nie. Proteín je len pohodlný zdroj bielkovín. Ak ich zvládaš získať z jedla, nepotrebuješ ho.'),
        ('Dokáže telo využiť naraz len 30 gramov bielkovín?', 'Nie, je to zjednodušenie. Telo dokáže využiť aj viac, len trávenie trvá dlhšie. Rozloženie do 3 až 5 jedál je praktické, nie povinné.'),
        ('Škodia bielkoviny obličkám?', 'U zdravých ľudí štúdie pri bežne vyššom príjme poškodenie obličiek nepreukázali. Ak máš ochorenie obličiek, príjem bielkovín musíš konzultovať s lekárom.'),
        ('Stačia bielkoviny z rastlinnej stravy?', 'Áno. Kombinuj rôzne zdroje (strukoviny, tofu, obilniny, orechy) a cieľ si nastav skôr k hornej hranici rozsahu.'),
    ],
    sections=[
        ('odpoved', 'Krátka odpoveď', '''    <p>Pre zdravého dospelého so sedavým životom je referenčný príjem približne <strong>0,8 g bielkovín na kg</strong> telesnej hmotnosti denne. Ak <strong>silovo trénuješ</strong>, chceš naberať sval alebo chudneš, väčšina odporúčaní sa pohybuje v rozsahu <strong>1,6 až 2,2 g na kg</strong>.</p>
    <table>
      <thead><tr><th>Telesná hmotnosť</th><th class="n">1,6 g/kg</th><th class="n">2,0 g/kg</th><th class="n">2,2 g/kg</th></tr></thead>
      <tbody>
        <tr><td>60 kg</td><td class="n">96 g</td><td class="n">120 g</td><td class="n">132 g</td></tr>
        <tr><td>70 kg</td><td class="n">112 g</td><td class="n">140 g</td><td class="n">154 g</td></tr>
        <tr><td>80 kg</td><td class="n">128 g</td><td class="n">160 g</td><td class="n">176 g</td></tr>
        <tr><td>90 kg</td><td class="n">144 g</td><td class="n">180 g</td><td class="n">198 g</td></tr>
      </tbody>
    </table>'''),
        ('preco', 'Prečo práve tento rozsah', '''    <p>Metaanalýza z roku 2018 (Morton a kol., British Journal of Sports Medicine) spojila desiatky štúdií so silovým tréningom. Prírastky svalov sa s vyšším príjmom bielkovín zlepšovali približne do <strong>1,6 g na kg</strong> a vyššie hodnoty už zväčša neprinášali ďalší benefit. Horná hranica intervalu spoľahlivosti bola okolo <strong>2,2 g na kg</strong>, preto sa táto hodnota bežne uvádza ako strop, nad ktorý už nemá zmysel ísť.</p>
    <p>Viac neznamená vždy viac svalov. Nad zhruba 2,2 g na kg už zvyčajne ide o zbytočné kalórie navyše.</p>'''),
        ('cielu', 'Podľa cieľa', '''    <table>
      <thead><tr><th>Situácia</th><th class="n">g na kg denne</th></tr></thead>
      <tbody>
        <tr><td>Zdravý dospelý bez pravidelného tréningu</td><td class="n">~0,8</td></tr>
        <tr><td>Rekreačne aktívny</td><td class="n">1,2 až 1,6</td></tr>
        <tr><td>Silový tréning a naberanie svalov</td><td class="n">1,6 až 2,2</td></tr>
        <tr><td>Chudnutie so silovým tréningom</td><td class="n">1,8 až 2,2</td></tr>
      </tbody>
    </table>
    <p>V kalorickom deficite sa oplatí byť skôr pri hornej hranici, pomáha to zachovať svalovú hmotu a lepšie ťa zasýti. Deficit si vieš nastaviť v <a href="/kalorie-kalkulacka">kalorickej kalkulačke</a>.</p>'''),
        ('rozlozenie', 'Ako si ich rozložiť počas dňa', '''    <p>Praktický cieľ je 3 až 5 jedál s približne <strong>0,3 až 0,4 g bielkovín na kg</strong> v jednom jedle. Pre 80 kg je to zhruba 25 až 35 g. Presné načasovanie okolo tréningu je menej dôležité než celkový denný príjem.</p>'''),
        ('potraviny', 'Koľko bielkovín majú bežné potraviny', '''    <table>
      <thead><tr><th>Potravina</th><th class="n">Bielkoviny (orientačne)</th></tr></thead>
      <tbody>
        <tr><td>Kuracie prsia varené, 100 g</td><td class="n">30 g</td></tr>
        <tr><td>Losos, 100 g</td><td class="n">20 g</td></tr>
        <tr><td>Tuniak v konzerve, 100 g</td><td class="n">25 g</td></tr>
        <tr><td>Vajce, 1 kus</td><td class="n">6 g</td></tr>
        <tr><td>Tvaroh, 100 g</td><td class="n">12 g</td></tr>
        <tr><td>Grécky jogurt, 150 g</td><td class="n">15 g</td></tr>
        <tr><td>Tofu, 100 g</td><td class="n">10 g</td></tr>
        <tr><td>Šošovica varená, 100 g</td><td class="n">9 g</td></tr>
        <tr><td>Srvátkový proteín, 1 odmerka (30 g)</td><td class="n">24 g</td></tr>
      </tbody>
    </table>
    <p class="note">Hodnoty sú orientačné a líšia sa podľa výrobcu a spôsobu prípravy.</p>'''),
        ('den', 'Vzorový deň pre 80 kg (cieľ približne 160 g)', '''    <table>
      <thead><tr><th>Jedlo</th><th>Čo</th><th class="n">Bielkoviny</th></tr></thead>
      <tbody>
        <tr><td>Raňajky</td><td>3 vajcia, grécky jogurt 150 g, ovsené vločky 50 g</td><td class="n">~40 g</td></tr>
        <tr><td>Obed</td><td>Kuracie prsia 150 g s ryžou a zeleninou</td><td class="n">~45 g</td></tr>
        <tr><td>Desiata</td><td>Tvaroh 200 g</td><td class="n">~24 g</td></tr>
        <tr><td>Večera</td><td>Losos 150 g so zeleninou</td><td class="n">~30 g</td></tr>
        <tr><td>Po tréningu</td><td>Srvátkový proteín 1 odmerka</td><td class="n">~24 g</td></tr>
        <tr><td><strong>Spolu</strong></td><td></td><td class="n">~163 g</td></tr>
      </tbody>
    </table>'''),
        ('mytus', 'Mýty a bezpečnosť', '''    <ul>
      <li><strong>„Bielkoviny ničia obličky.“</strong> U zdravých ľudí to štúdie pri bežne vyššom príjme nepotvrdili. Ak máš ochorenie obličiek, poraď sa s lekárom.</li>
      <li><strong>„Bez proteínu sa svaly nerobia.“</strong> Rozhoduje celkový denný príjem, nie forma.</li>
      <li><strong>„Čím viac, tým lepšie.“</strong> Po prekročení hornej hranice rozsahu už nič nezískaš.</li>
    </ul>
    <p>Príjem si zapisuj a sleduj priemer za týždeň. V <a href="/blog/treningovy-dennik">tréningovom denníku</a> si vieš pri každom týždni porovnať príjem s tým, ako sa ti darí v tréningu.</p>'''),
    ],
))

# ═══════════════════════════════════════ 4. Hyrox príprava ══════════════════════════════════════
ARTICLES.append(dict(
    slug='hyrox-priprava-8-tyzdnov',
    title='Hyrox príprava na 8 týždňov: ukážkový plán pre začiatočníkov',
    title_tag='Hyrox príprava na 8 týždňov — plán pre začiatočníkov | BOOOM',
    h1='Hyrox príprava na 8 týždňov: ukážkový plán pre začiatočníkov',
    crumb='Hyrox príprava na 8 týždňov',
    desc='8-týždňový plán prípravy na prvý Hyrox: týždenná štruktúra, behy, sila, nácvik staníc, simulácia a taper. Pre tých, čo zvládnu odbehnúť 5 km.',
    card='Týždeň po týždni: behy, silový tréning, hybridné tréningy, simulácia a taper pred prvým Hyroxom.',
    kw='hyrox príprava, hyrox tréningový plán, hyrox 8 týždňov, hyrox pre začiatočníkov, hyrox tréning, hyrox stanice',
    lead='Osem týždňov stačí na to, aby si prvý Hyrox dokončil s úsmevom, ak už vieš behať a nie si úplný nováčik v posilňovni. Tu je plán, ktorý ti ukáže, čo robiť každý týždeň.',
    cta=('Zapisuj splity a sleduj pokrok', 'BOOOM meria tvoje splity v reálnom čase, ukáže run-vs-stanica rozbor a fatigue index. Tréningový denník pre Hyrox.'),
    disc=DISC_TRAIN,
    faq=[
        ('Stačí 8 týždňov na prvý Hyrox?', 'Ak vieš odbehnúť 5 km v kuse a trénuješ aspoň 3-krát týždenne, na dokončenie prvých pretekov áno. Ak nie, predĺž si základnú fázu.'),
        ('Koľko mám behať týždenne?', 'V tomto pláne orientačne 15 až 25 km týždenne, väčšinu v pokojnom tempe. Dôležitejšia než kilometre je pravidelnosť.'),
        ('Môžem sa pripraviť doma?', 'Časť áno: behy, silový tréning s činkami a vlastnou váhou. Špecifické stanice (SkiErg, sane, veslovanie) si vyskúšaj v gyme aspoň niekoľkokrát pred pretekmi.'),
        ('Ako sa mám pripraviť na pacing?', 'Použi <a href="/hyrox-pacing">Hyrox pacing kalkulačku</a>: zadaj cieľový čas a získaš tempo behov a časy staníc. Po simulácii ich nahraď skutočnými splitmi.'),
    ],
    sections=[
        ('pre-koho', 'Pre koho je plán', '''    <ul>
      <li>Zvládneš odbehnúť <strong>5 km v kuse</strong>, aj pomaly.</li>
      <li>Trénuješ <strong>3 až 4-krát týždenne</strong> a poznáš základné cviky (drep, mŕtvy ťah, výpady, tlaky).</li>
      <li>Máš 8 týždňov a cieľ dokončiť prvý Hyrox, nie vyhrať kategóriu.</li>
    </ul>
    <p>Ak tieto podmienky nespĺňaš, pridaj si na začiatok základnú fázu. Ak máš zranenie alebo zdravotné obmedzenia, poraď sa s lekárom. Plán je ukážkový, prispôsob si ho svojmu času a schopnostiam.</p>'''),
        ('format', 'Hyrox v skratke', '''    <p>Hyrox je <strong>8 kôl, každé z nich je 1 km behu a jedna funkčná stanica</strong>. Stanice idú v tomto poradí: SkiErg, Sled Push, Sled Pull, Burpee Broad Jumps, Rowing, Farmers Carry, Sandbag Lunges a Wall Balls. Viac o formáte nájdeš v článku <a href="/hyrox-pre-zaciatocnikov">Hyrox pre začiatočníkov</a>. Váhy závisia od kategórie a sezóny, over si ich v oficiálnych pravidlách.</p>'''),
        ('tyzden', 'Štruktúra týždňa', '''    <table>
      <thead><tr><th>Deň</th><th>Tréning</th></tr></thead>
      <tbody>
        <tr><td><strong>1</strong></td><td>Ľahký beh v konverzačnom tempe</td></tr>
        <tr><td><strong>2</strong></td><td>Silový tréning: drep, mŕtvy ťah, tlaky, ťahy, výpady</td></tr>
        <tr><td><strong>3</strong></td><td>Intervaly alebo tempový beh</td></tr>
        <tr><td><strong>4</strong></td><td>Hybridný tréning: beh striedaný so stanicami</td></tr>
        <tr><td>5 až 7</td><td>Odpočinok, prechádzka, mobilita</td></tr>
      </tbody>
    </table>'''),
        ('plan', 'Plán týždeň po týždni', '''    <table>
      <thead><tr><th>Týždeň</th><th>Ľahký beh</th><th>Sila</th><th>Intervaly / tempo</th><th>Hybrid</th></tr></thead>
      <tbody>
        <tr><td><strong>1</strong></td><td>30 min</td><td>Celé telo, 3 × 8–10</td><td>5 × 2 min ťažko / 2 min ľahko</td><td>4 × (400 m beh + 15 wall balls)</td></tr>
        <tr><td><strong>2</strong></td><td>35 min</td><td>Rovnaké cviky, pridaj váhu</td><td>6 × 2 min</td><td>4 × (400 m + 20 wall balls)</td></tr>
        <tr><td><strong>3</strong></td><td>40 min</td><td>Sila + farmers carry 4 × 40 m</td><td>4 × 4 min tempo / 2 min ľahko</td><td>5 × (500 m + 250 m SkiErg)</td></tr>
        <tr><td><strong>4</strong> (odľahčený)</td><td>30 min</td><td>2 × 8, ľahšie</td><td>4 × 2 min</td><td>3 × (500 m + stanica)</td></tr>
        <tr><td><strong>5</strong></td><td>45 min</td><td>Sila + výpady s vakom 4 × 20 m</td><td>3 × 6 min tempo / 2 min ľahko</td><td>6 × (600 m + stanica)</td></tr>
        <tr><td><strong>6</strong></td><td>50 min</td><td>Sila + sled push a pull</td><td>5 × 4 min</td><td>6 × (800 m + stanica), stanice naostro</td></tr>
        <tr><td><strong>7</strong> (simulácia)</td><td>40 min</td><td>Ľahká sila</td><td>—</td><td>Polovičná alebo celá simulácia Hyroxu v cieľovom tempe</td></tr>
        <tr><td><strong>8</strong> (taper)</td><td>25–30 min</td><td>2 krátke tréningy, 2 × 6</td><td>4 × 1 min svižne</td><td>15 min ľahká aktivácia pár dní pred pretekom</td></tr>
      </tbody>
    </table>
    <p class="note">Ukážkový plán, nie univerzálny predpis. Ak ti niektorý týždeň nevyjde, nedobiehaj ho, pokračuj nasledujúcim.</p>'''),
        ('stanice', 'Nácvik staníc: technika v skratke', '''    <ul>
      <li><strong>SkiErg:</strong> ťah z bokov a trupu, nielen z rúk. Drž rovnomerný rytmus.</li>
      <li><strong>Sled Push:</strong> nízke ťažisko, krátke a rýchle kroky, plynulo.</li>
      <li><strong>Sled Pull:</strong> nohy a trup pracujú, ruky len prenášajú lano.</li>
      <li><strong>Burpee Broad Jumps:</strong> krátke skoky v rytme, šetri dych a ruky.</li>
      <li><strong>Rowing:</strong> najprv nohy, potom trup, nakoniec ruky.</li>
      <li><strong>Farmers Carry:</strong> pevné držanie, krátke kroky, nepúšťaj závažia bez potreby.</li>
      <li><strong>Sandbag Lunges:</strong> kolená pod kontrolou, vak stabilne na pleciach.</li>
      <li><strong>Wall Balls:</strong> plynulý drep a hod, krátke série s krátkymi pauzami.</li>
    </ul>'''),
        ('preteky', 'Posledný týždeň a deň pretekov', '''    <ul>
      <li><strong>Neskúšaj nové veci.</strong> Jedlo, obuv a oblečenie musia byť overené z tréningu.</li>
      <li><strong>Spi.</strong> V posledných dňoch pred pretekmi je spánok najlepšia príprava.</li>
      <li><strong>Štartuj pomaly.</strong> Prvý kilometer sa na adrenalín zdá ľahký a prehnané tempo zaplatíš v druhej polovici.</li>
      <li><strong>Drž pacing.</strong> Cieľové tempo si spočítaj v <a href="/hyrox-pacing">Hyrox pacing kalkulačke</a>.</li>
    </ul>'''),
        ('sledovanie', 'Ako sledovať pokrok', '''    <p>Po každej simulácii si zapíš splity všetkých behov a staníc. Uvidíš, kde strácaš čas, a vieš tam zamerať tréning. Silový pokrok si sleduj v <a href="/1rm-kalkulacka">1RM kalkulačke</a> a v <a href="/blog/treningovy-dennik">tréningovom denníku</a>.</p>'''),
    ],
))

