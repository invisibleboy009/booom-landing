# Czech blog content (for /cs/blog and /cs/blog/*). The generator is blog-src/make_blog.py.
# Structure is shared by content_sk.py and content_en.py: same article order and section ids.
# Run: python blog-src/make_blog.py   (then node build-i18n.mjs, and commit the generated html).

LANG = 'cs'
PREFIX = '/cs'         # URL prefix of this language ('' for Slovak, '/en', '/cs')
UI = dict(
    html_lang='cs', og_locale='cs_CZ', date_sk='20. září 2026',
    blog='Blog', home='BOOOM', toc='Obsah', toc_aria='Obsah článku', faq='Časté otázky',
    updated='Aktualizováno', read='min čtení', privacy='Ochrana údajů',
    try_free='Vyzkoušet zdarma', try_web='Vyzkoušet zdarma na webu',
    appstore='Stáhnout v App Store', gplay='Získat v Google Play',
)
HUB = dict(
    title_tag='Blog — trénink, výživa a Hyrox | BOOOM',
    og_title='Blog BOOOM — trénink, výživa a Hyrox',
    h1='Blog BOOOM: trénink, výživa a Hyrox',
    desc='Blog BOOOM: praktické články o tréninkovém deníku, progresivním přetížení, bílkovinách a přípravě na Hyrox. Zdarma, bez keců.',
    kw='fitness blog, tréninkový deník, progresivní přetížení, bílkoviny, hyrox příprava, BOOOM',
    lead='Praktické články bez keců, které ti pomůžou trénovat chytřeji. K většině z nich najdeš i kalkulačku nebo nástroj přímo na webu.',
    cta=('Trénuj s BOOOM', 'Tréninkový deník, AI trenér, Hyrox simulátor a sledování výživy v jedné appce. Zdarma pro iOS, Android i web.'),
)

DISC_HEALTH = '<p class="disc">Článek má informativní charakter a nenahrazuje radu lékaře ani nutričního terapeuta. Při zdravotních problémech se poraď s odborníkem.</p>'
DISC_TRAIN = '<p class="disc">Článek má informativní charakter a nenahrazuje osobního trenéra ani lékaře. Pokud máš zdravotní potíže nebo zranění, před zahájením náročného tréninku se poraď s odborníkem.</p>'

ARTICLES = []

# ═══════════════════════════════════════ 1. Tréninkový deník ════════════════════════════════════
ARTICLES.append(dict(
    slug='treninkovy-denik',
    title='Tréninkový deník: jak si ho vést a proč ti pomůže růst',
    title_tag='Tréninkový deník — jak si ho vést a co zapisovat | BOOOM',
    h1='Tréninkový deník: jak si ho vést a proč ti pomůže růst',
    crumb='Tréninkový deník',
    desc='Co si zapisovat do tréninkového deníku, jak ho vést krok za krokem a jak z něj vyčíst pokrok. Praktický návod pro silový trénink, Hyrox i běh.',
    card='Co zapisovat, jak na to v praxi a jak z čísel poznat, jestli opravdu děláš pokrok.',
    kw='tréninkový deník, jak si vést tréninkový deník, zápis tréninků, sledování pokroku, tréninkový plán, silový trénink',
    lead='Většina lidí si myslí, že si pamatuje, kolik minulý týden zvedli. Většina se mýlí. Tréninkový deník je nejlevnější způsob, jak z tréninku udělat systém, který umí růst.',
    cta=('Zapisuj tréninky bez papíru', 'BOOOM si pamatuje tvoje váhy a opakování, sám ukáže osobní rekordy a odmění tě XP. Tréninkový deník, který tě neotravuje.'),
    disc=DISC_TRAIN,
    faq=[
        ('Kolik času zabere zapisování tréninku?', 'U dobrého nástroje zhruba minutu až dvě na celý trénink. Pokud ti zápis zabírá víc, zjednoduš formát — zapisuj jen to, co opravdu používáš.'),
        ('Musím zapisovat i lehké tréninky a kardio?', 'Ano, aspoň v minimu: datum, druh aktivity a délku nebo vzdálenost. I lehké dny patří do obrazu toho, kolik zátěže reálně zvládáš.'),
        ('Co když vynechám trénink nebo zápis?', 'Nic se neděje. Deník není soutěž v dokonalosti. Vynechaný den nedoháněj, prostě pokračuj v plánu. Důležité je, aby ti zápisy přinášely informace, ne výčitky.'),
        ('Je lepší zapisovat na papír, nebo do appky?', 'Funguje obojí. Papír je rychlý a nic tě neruší, appka umí sama počítat rekordy, objem a grafy. Nejlepší deník je ten, který si opravdu vedeš.'),
    ],
    sections=[
        ('preco', 'Proč si zapisovat tréninky', '''    <p>Bez zápisů trénuješ podle pocitu. Pocit je užitečný, ale nespolehlivý: dobrý den zkreslí, jak ti trénink šel, a únava ho zase zkreslí opačným směrem. Deník ti dává data, která nezávisejí na náladě.</p>
    <ul>
      <li><strong>Víš, co máš dnes porazit.</strong> Růst síly stojí na postupném přidávání zátěže (víc v článku <a href="/cs/blog/progresivni-pretizeni">Progresivní přetížení</a>). Bez čísel z minulého tréninku nevíš, co znamená „víc“.</li>
      <li><strong>Vidíš pokrok, i když ho v zrcadle nevidíš.</strong> Svaly rostou pomalu, ale váhy a opakování stoupají rychleji a motivují.</li>
      <li><strong>Najdeš příčinu, když to nejde.</strong> Stagnace, bolest nebo únava zanechávají stopu v datech: méně spánku, víc objemu, vynechaná jídla.</li>
      <li><strong>Drží tě u návyku.</strong> Sebemonitorování patří mezi nejlépe prozkoumané techniky, které pomáhají udržet nový návyk.</li>
    </ul>'''),
        ('co', 'Co zapisovat: minimum a bonusy', '''    <table>
      <thead><tr><th>Kategorie</th><th>Co si zapsat</th></tr></thead>
      <tbody>
        <tr><td><strong>Minimum (silový trénink)</strong></td><td>Datum, cvik, váha, počet opakování, počet sérií</td></tr>
        <tr><td><strong>Velmi užitečné</strong></td><td>Jak těžká série byla (RPE 1 až 10 nebo kolik opakování ti zbylo v záloze), krátká poznámka k technice</td></tr>
        <tr><td><strong>Bonus</strong></td><td>Spánek, energie, tělesná hmotnost, obvody, fotky</td></tr>
        <tr><td><strong>Běh a Hyrox</strong></td><td>Vzdálenost, čas, tempo, tep, splity jednotlivých běhů a stanic</td></tr>
      </tbody>
    </table>
    <p>Začni minimem. Deník s deseti sloupci přestaneš vést za dva týdny, deník s pěti vydrží roky.</p>'''),
        ('ako', 'Jak si deník vést v praxi', '''    <ol>
      <li><strong>Vyber si jeden formát a drž se ho.</strong> Sešit, tabulka nebo appka. Přepínání mezi nimi je nejčastější důvod, proč se deník rozpadne.</li>
      <li><strong>Před tréninkem se podívej na minulý záznam</strong> a stanov si cíl na dnes: o opakování víc nebo o 2,5 kg víc.</li>
      <li><strong>Zapisuj hned po sérii</strong>, ne večer z paměti. Paměť zaokrouhluje nahoru.</li>
      <li><strong>Přidej poznámku, když se něco stalo</strong> — bolelo rameno, špatně se ti spalo, změnila se technika.</li>
      <li><strong>Jednou týdně si dej pět minut</strong> a projdi si zápisy: co roste, co stojí, co je potřeba změnit.</li>
    </ol>'''),
        ('progres', 'Jak z deníku vyčíst pokrok', '''    <p>Nesleduj všechno. Stačí tři věci:</p>
    <ul>
      <li><strong>Nejlepší série v hlavních cvicích.</strong> Z ní si můžeš odhadnout i 1RM v <a href="/cs/1rm-kalkulacka">kalkulačce 1RM</a> a porovnat ho v čase.</li>
      <li><strong>Týdenní objem</strong> (série × opakování × váha) pro každou svalovou skupinu. Roste postupně, s občasným odlehčením.</li>
      <li><strong>Frekvenci tréninků.</strong> Počet dokončených tréninků za týden je jednoduchý ukazatel konzistence.</li>
    </ul>
    <div class="ex">
      <p><strong>Příklad: tlak na lavici, 4 týdny, 3 série</strong></p>
      <table>
        <thead><tr><th>Týden</th><th>Váha</th><th>Opakování v sériích</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>60 kg</td><td>8 / 8 / 7</td></tr>
          <tr><td>2</td><td>60 kg</td><td>9 / 8 / 8</td></tr>
          <tr><td>3</td><td>60 kg</td><td>10 / 9 / 8</td></tr>
          <tr><td>4</td><td>62,5 kg</td><td>8 / 8 / 7</td></tr>
        </tbody>
      </table>
      <p>Tři týdny přidáváš opakování, ve čtvrtém přidáš váhu a začneš znovu. Bez deníku by ti to vypadlo z hlavy.</p>
    </div>'''),
        ('chyby', 'Nejčastější chyby', '''    <ul>
      <li><strong>Příliš složitý formát.</strong> Pokud zápis trvá déle než rozcvička, přestaneš.</li>
      <li><strong>Zapisuješ jen rekordy.</strong> Bez průměrných dnů nevidíš trend.</li>
      <li><strong>Deník nepoužíváš.</strong> Zápis je zbytečný, pokud ho před tréninkem neotevřeš.</li>
      <li><strong>Nezaznamenáš změnu podmínek.</strong> Jiná lavice, jiné činky, jiný rozsah pohybu: bez poznámky ta čísla nepůjde porovnat.</li>
    </ul>'''),
        ('forma', 'Papír, tabulka, nebo appka?', '''    <table>
      <thead><tr><th>Forma</th><th>Výhoda</th><th>Nevýhoda</th></tr></thead>
      <tbody>
        <tr><td>Sešit</td><td>Rychlý, nic tě neruší</td><td>Žádné grafy, špatně se v něm hledá</td></tr>
        <tr><td>Tabulka</td><td>Vlastní vzorce, dá se filtrovat</td><td>Na telefonu v posilovně nepohodlná</td></tr>
        <tr><td>Appka</td><td>Předvyplní minulé váhy, sama počítá rekordy a objem</td><td>Je potřeba vybrat tu, která tě neotravuje</td></tr>
      </tbody>
    </table>
    <p>Aplikace BOOOM je postavená právě na tomhle: zapíšeš cvik, appka ti ukáže minulý výkon, sama vyhodnotí osobní rekordy a odmění tě XP a ranky. Vyzkoušet ji můžeš zdarma i na webu.</p>'''),
    ],
))

# ═══════════════════════════════════════ 2. Progresivní přetížení ═══════════════════════════════
ARTICLES.append(dict(
    slug='progresivni-pretizeni',
    title='Progresivní přetížení: jak přidávat váhu, aby síla a svaly dál rostly',
    title_tag='Progresivní přetížení — jak přidávat váhu a opakování | BOOOM',
    h1='Progresivní přetížení: jak přidávat váhu, aby síla a svaly dál rostly',
    crumb='Progresivní přetížení',
    desc='Co je progresivní přetížení, pět způsobů, jak ho uplatnit, jednoduchá dvojitá progrese, RPE a co dělat při stagnaci. Praktický návod pro silový trénink.',
    card='Jak přidávat váhu, opakování a objem tak, aby síla rostla a stagnace tě nezdolala.',
    kw='progresivní přetížení, jak přidávat váhu, dvojitá progrese, RPE, stagnace v síle, deload, silový trénink',
    lead='Tělo roste, jen když ho k tomu dotlačíš. Pokud děláš pořád stejné série se stejnou váhou, přestane se přizpůsobovat. Progresivní přetížení je princip, který stojí za všemi dobrými plány.',
    cta=('Ať se progres počítá sám', 'BOOOM u každého cviku ukáže, jaký byl tvůj minulý výkon, a automaticky zaznamená nové rekordy. Ty jen přidáváš.'),
    disc=DISC_TRAIN,
    faq=[
        ('Musím přidávat váhu každý trénink?', 'Ne. Začátečníci mohou přidávat každý týden nebo dokonce každý trénink, pokročilí často jen jednou za několik týdnů. Důležitý je směr, ne rychlost.'),
        ('Co když nezvládnu přidat ani opakování?', 'Občasný slabší trénink je normální. Pokud se to opakuje víc týdnů, zkontroluj spánek, příjem kalorií a bílkovin (<a href="/cs/blog/kolik-bilkovin-denne">kolik bílkovin denně</a>) a zvaž odlehčený týden.'),
        ('Jak často mám dělat deload?', 'Orientačně jednou za 4 až 8 týdnů nebo když zaznamenáš delší zhoršení výkonu a únavu. Objem a zátěž sniž zhruba o třetinu až polovinu.'),
        ('Funguje progresivní přetížení i při hubnutí?', 'Ano. V deficitu je cílem udržet sílu, což je signál, že neztrácíš sval. Přidávání zátěže může být pomalejší, a to je v pořádku.'),
    ],
    sections=[
        ('co', 'Co je progresivní přetížení', '''    <p><strong>Progresivní přetížení</strong> znamená postupně zvyšovat nároky, které trénink klade na tělo. Svaly a nervový systém se přizpůsobí tomu, co děláš. Pokud nároky zůstanou stejné, přizpůsobení se zastaví a s ním i pokrok.</p>
    <p>Nemusíš přidávat váhu na tyč. Přetížení lze zvyšovat několika způsoby a často je chytřejší je střídat.</p>'''),
        ('sposoby', 'Pět způsobů, jak zvyšovat zátěž', '''    <table>
      <thead><tr><th>Způsob</th><th>Jak to vypadá</th></tr></thead>
      <tbody>
        <tr><td><strong>Váha</strong></td><td>Přidáš 1,25 až 5 kg na tyč</td></tr>
        <tr><td><strong>Opakování</strong></td><td>Místo 8 uděláš 9 nebo 10 se stejnou váhou</td></tr>
        <tr><td><strong>Série</strong></td><td>Ze 3 sérií přejdeš na 4</td></tr>
        <tr><td><strong>Technika a rozsah</strong></td><td>Hlubší dřep, pomalejší excentrická fáze, pauza dole</td></tr>
        <tr><td><strong>Hustota</strong></td><td>Stejná práce za kratší čas, kratší pauzy</td></tr>
      </tbody>
    </table>'''),
        ('dvojita', 'Dvojitá progrese: nejjednodušší metoda', '''    <p>Stanov si rozsah opakování, například 8 až 12. Začni s váhou, se kterou zvládneš dolní hranici ve všech sériích. Držíš stejnou váhu a přidáváš opakování, dokud nedosáhneš horní hranice ve všech sériích. Tehdy přidáš váhu a vrátíš se na 8.</p>
    <div class="ex">
      <p><strong>Příklad: jednoruční přítah s činkou</strong></p>
      <table>
        <thead><tr><th>Týden</th><th>Váha</th><th>Opakování (3 série)</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>24 kg</td><td>8 / 8 / 8</td></tr>
          <tr><td>2</td><td>24 kg</td><td>10 / 9 / 8</td></tr>
          <tr><td>3</td><td>24 kg</td><td>12 / 11 / 10</td></tr>
          <tr><td>4</td><td>24 kg</td><td>12 / 12 / 12</td></tr>
          <tr><td>5</td><td>26 kg</td><td>8 / 8 / 8 a znovu</td></tr>
        </tbody>
      </table>
    </div>'''),
        ('kolko', 'O kolik přidávat', '''    <ul>
      <li><strong>Horní tělo a izolované cviky:</strong> obvykle 1,25 až 2,5 kg.</li>
      <li><strong>Nohy a mrtvý tah:</strong> obvykle 2,5 až 5 kg.</li>
      <li><strong>Začátečníci</strong> postupují rychleji, často každý týden. <strong>Pokročilí</strong> jen jednou za několik týdnů, někdy jen o opakování.</li>
    </ul>
    <p>Pokud nemáš malé kotouče, kup si magnetická závaží po 0,5 až 1,25 kg. Malé skoky jsou lepší než stagnace.</p>'''),
        ('rpe', 'RPE a rezerva v opakováních', '''    <p><strong>RPE</strong> (rate of perceived exertion) je škála 1 až 10, jak těžká série byla. RPE 10 znamená úplné selhání, RPE 8 znamená, že ti v záloze zůstala asi dvě opakování. Tento údaj se označuje také jako <strong>RIR</strong> (reps in reserve).</p>
    <p>Většina pracovních sérií by měla končit s rezervou 1 až 3 opakování. Tak budeš na sval tlačit dost, ale nebudeš se zbytečně vyčerpávat. Do <a href="/cs/blog/treninkovy-denik">tréninkového deníku</a> si RPE zapisuj alespoň u poslední série cviku.</p>'''),
        ('deload', 'Odlehčený týden (deload)', '''    <p>Únava se nahromadí rychleji, než si myslíš. Jednou za 4 až 8 týdnů, nebo když ti výkon klesá několik tréninků po sobě, sniž objem i zátěž zhruba o třetinu až polovinu. Po týdnu se vrátíš s čerstvými silami a často překonáš předchozí rekordy.</p>'''),
        ('stagnacia', 'Co dělat při stagnaci', '''    <ol>
      <li><strong>Zkontroluj spánek.</strong> Pravidelně méně než 7 hodin se projeví na síle i regeneraci.</li>
      <li><strong>Zkontroluj příjem.</strong> Při chronickém deficitu síla stagnuje. Spočítej si potřebu v <a href="/cs/kaloricka-kalkulacka">kalorické kalkulačce</a> a bílkoviny podle článku <a href="/cs/blog/kolik-bilkovin-denne">Kolik bílkovin denně</a>.</li>
      <li><strong>Změň podnět.</strong> Jiný rozsah opakování, variantu cviku nebo tempo.</li>
      <li><strong>Zkontroluj techniku.</strong> Natoč si sérii na video.</li>
      <li><strong>Dej si deload.</strong></li>
    </ol>
    <p>Aktuální sílu si můžeš orientačně odhadnout v <a href="/cs/1rm-kalkulacka">kalkulačce 1RM</a> a po pár týdnech porovnat.</p>'''),
    ],
))

# ═══════════════════════════════════════ 3. Kolik bílkovin denně ════════════════════════════════
ARTICLES.append(dict(
    slug='kolik-bilkovin-denne',
    title='Kolik bílkovin denně potřebuješ (a jak si je rozložit)',
    title_tag='Kolik bílkovin denně — výpočet podle váhy a cíle | BOOOM',
    h1='Kolik bílkovin denně potřebuješ (a jak si je rozložit)',
    crumb='Kolik bílkovin denně',
    desc='Kolik bílkovin denně potřebuješ na svaly, hubnutí i běžný život. Tabulka podle váhy, potraviny s bílkovinami, vzorový den a nejčastější mýty.',
    card='Tabulka podle váhy a cíle, obsah bílkovin v běžných potravinách a vzorový den.',
    kw='kolik bílkovin denně, bílkoviny na kg, příjem bílkovin, bílkoviny na hubnutí, bílkoviny a svaly, protein',
    lead='Číslo, které znáš z posilovny, jsou „2 gramy na kilo“. Je to rozumný odhad, ale ne vždy a ne pro každého. Tady je, proč, kdy stačí míň a jak si bílkoviny rozložit během dne.',
    cta=('Zapisuj jídlo i makra jednoduše', 'BOOOM má skener čárových kódů, databázi potravin a denní cíl bílkovin podle tvé váhy.'),
    disc=DISC_HEALTH,
    faq=[
        ('Musím pít proteinový nápoj?', 'Ne. Protein je jen pohodlný zdroj bílkovin. Pokud je zvládáš získat z jídla, nepotřebuješ ho.'),
        ('Dokáže tělo využít najednou jen 30 gramů bílkovin?', 'Ne, je to zjednodušení. Tělo dokáže využít i víc, jen trávení trvá déle. Rozložení do 3 až 5 jídel je praktické, ne povinné.'),
        ('Škodí bílkoviny ledvinám?', 'U zdravých lidí studie při běžně vyšším příjmu poškození ledvin neprokázaly. Pokud máš onemocnění ledvin, příjem bílkovin musíš konzultovat s lékařem.'),
        ('Stačí bílkoviny z rostlinné stravy?', 'Ano. Kombinuj různé zdroje (luštěniny, tofu, obiloviny, ořechy) a cíl si nastav spíš k horní hranici rozsahu.'),
    ],
    sections=[
        ('odpoved', 'Krátká odpověď', '''    <p>Pro zdravého dospělého se sedavým způsobem života je referenční příjem přibližně <strong>0,8 g bílkovin na kg</strong> tělesné hmotnosti denně. Pokud <strong>silově trénuješ</strong>, chceš nabírat svaly nebo hubneš, většina doporučení se pohybuje v rozsahu <strong>1,6 až 2,2 g na kg</strong>.</p>
    <table>
      <thead><tr><th>Tělesná hmotnost</th><th class="n">1,6 g/kg</th><th class="n">2,0 g/kg</th><th class="n">2,2 g/kg</th></tr></thead>
      <tbody>
        <tr><td>60 kg</td><td class="n">96 g</td><td class="n">120 g</td><td class="n">132 g</td></tr>
        <tr><td>70 kg</td><td class="n">112 g</td><td class="n">140 g</td><td class="n">154 g</td></tr>
        <tr><td>80 kg</td><td class="n">128 g</td><td class="n">160 g</td><td class="n">176 g</td></tr>
        <tr><td>90 kg</td><td class="n">144 g</td><td class="n">180 g</td><td class="n">198 g</td></tr>
      </tbody>
    </table>'''),
        ('preco', 'Proč právě tento rozsah', '''    <p>Metaanalýza z roku 2018 (Morton a kol., British Journal of Sports Medicine) spojila desítky studií se silovým tréninkem. Přírůstky svalů se s vyšším příjmem bílkovin zlepšovaly přibližně do <strong>1,6 g na kg</strong> a vyšší hodnoty už většinou nepřinášely další přínos. Horní hranice intervalu spolehlivosti byla kolem <strong>2,2 g na kg</strong>, proto se tato hodnota běžně uvádí jako strop, nad který už nemá smysl jít.</p>
    <p>Víc neznamená vždy víc svalů. Nad zhruba 2,2 g na kg už obvykle jde o zbytečné kalorie navíc.</p>'''),
        ('cielu', 'Podle cíle', '''    <table>
      <thead><tr><th>Situace</th><th class="n">g na kg denně</th></tr></thead>
      <tbody>
        <tr><td>Zdravý dospělý bez pravidelného tréninku</td><td class="n">~0,8</td></tr>
        <tr><td>Rekreačně aktivní</td><td class="n">1,2 až 1,6</td></tr>
        <tr><td>Silový trénink a nabírání svalů</td><td class="n">1,6 až 2,2</td></tr>
        <tr><td>Hubnutí se silovým tréninkem</td><td class="n">1,8 až 2,2</td></tr>
      </tbody>
    </table>
    <p>V kalorickém deficitu se vyplatí být spíš u horní hranice, pomáhá to zachovat svalovou hmotu a lépe tě zasytí. Deficit si můžeš nastavit v <a href="/cs/kaloricka-kalkulacka">kalorické kalkulačce</a>.</p>'''),
        ('rozlozenie', 'Jak si je rozložit během dne', '''    <p>Praktický cíl jsou 3 až 5 jídel s přibližně <strong>0,3 až 0,4 g bílkovin na kg</strong> v jednom jídle. Pro 80 kg je to zhruba 25 až 35 g. Přesné načasování kolem tréninku je méně důležité než celkový denní příjem.</p>'''),
        ('potraviny', 'Kolik bílkovin mají běžné potraviny', '''    <table>
      <thead><tr><th>Potravina</th><th class="n">Bílkoviny (orientačně)</th></tr></thead>
      <tbody>
        <tr><td>Kuřecí prsa vařená, 100 g</td><td class="n">30 g</td></tr>
        <tr><td>Losos, 100 g</td><td class="n">20 g</td></tr>
        <tr><td>Tuňák v konzervě, 100 g</td><td class="n">25 g</td></tr>
        <tr><td>Vejce, 1 kus</td><td class="n">6 g</td></tr>
        <tr><td>Tvaroh, 100 g</td><td class="n">12 g</td></tr>
        <tr><td>Řecký jogurt, 150 g</td><td class="n">15 g</td></tr>
        <tr><td>Tofu, 100 g</td><td class="n">10 g</td></tr>
        <tr><td>Čočka vařená, 100 g</td><td class="n">9 g</td></tr>
        <tr><td>Syrovátkový protein, 1 odměrka (30 g)</td><td class="n">24 g</td></tr>
      </tbody>
    </table>
    <p class="note">Hodnoty jsou orientační a liší se podle výrobce a způsobu přípravy.</p>'''),
        ('den', 'Vzorový den pro 80 kg (cíl přibližně 160 g)', '''    <table>
      <thead><tr><th>Jídlo</th><th>Co</th><th class="n">Bílkoviny</th></tr></thead>
      <tbody>
        <tr><td>Snídaně</td><td>3 vejce, řecký jogurt 150 g, ovesné vločky 50 g</td><td class="n">~40 g</td></tr>
        <tr><td>Oběd</td><td>Kuřecí prsa 150 g s rýží a zeleninou</td><td class="n">~45 g</td></tr>
        <tr><td>Svačina</td><td>Tvaroh 200 g</td><td class="n">~24 g</td></tr>
        <tr><td>Večeře</td><td>Losos 150 g se zeleninou</td><td class="n">~30 g</td></tr>
        <tr><td>Po tréninku</td><td>Syrovátkový protein 1 odměrka</td><td class="n">~24 g</td></tr>
        <tr><td><strong>Celkem</strong></td><td></td><td class="n">~163 g</td></tr>
      </tbody>
    </table>'''),
        ('mytus', 'Mýty a bezpečnost', '''    <ul>
      <li><strong>„Bílkoviny ničí ledviny.“</strong> U zdravých lidí to studie při běžně vyšším příjmu nepotvrdily. Pokud máš onemocnění ledvin, poraď se s lékařem.</li>
      <li><strong>„Bez proteinu se svaly nedělají.“</strong> Rozhoduje celkový denní příjem, ne forma.</li>
      <li><strong>„Čím víc, tím lépe.“</strong> Po překročení horní hranice rozsahu už nezískáš nic.</li>
    </ul>
    <p>Příjem si zapisuj a sleduj průměr za týden. V <a href="/cs/blog/treninkovy-denik">tréninkovém deníku</a> si můžeš u každého týdne porovnat příjem s tím, jak se ti daří v tréninku.</p>'''),
    ],
))

# ═══════════════════════════════════════ 4. Hyrox příprava ══════════════════════════════════════
ARTICLES.append(dict(
    slug='hyrox-priprava-8-tydnu',
    title='Hyrox příprava na 8 týdnů: ukázkový plán pro začátečníky',
    title_tag='Hyrox příprava na 8 týdnů — plán pro začátečníky | BOOOM',
    h1='Hyrox příprava na 8 týdnů: ukázkový plán pro začátečníky',
    crumb='Hyrox příprava na 8 týdnů',
    desc='8týdenní plán přípravy na první Hyrox: týdenní struktura, běhy, síla, nácvik stanic, simulace a taper. Pro ty, kdo zvládnou uběhnout 5 km.',
    card='Týden po týdnu: běhy, silový trénink, hybridní tréninky, simulace a taper před prvním Hyroxem.',
    kw='hyrox příprava, hyrox tréninkový plán, hyrox 8 týdnů, hyrox pro začátečníky, hyrox trénink, hyrox stanice',
    lead='Osm týdnů stačí na to, aby se první Hyrox dal dokončit s úsměvem, pokud už umíš běhat a v posilovně nejsi úplně od nuly. Tady je plán, který ti ukáže, co dělat každý týden.',
    cta=('Zapisuj splity a sleduj pokrok', 'BOOOM měří tvoje splity v reálném čase, ukáže rozbor běh vs. stanice a fatigue index. Tréninkový deník pro Hyrox.'),
    disc=DISC_TRAIN,
    faq=[
        ('Stačí 8 týdnů na první Hyrox?', 'Pokud umíš uběhnout 5 km vkuse a trénuješ aspoň 3krát týdně, na dokončení prvních závodů ano. Pokud ne, prodluž si základní fázi.'),
        ('Kolik mám běhat týdně?', 'V tomto plánu orientačně 15 až 25 km týdně, většinu v klidném tempu. Důležitější než kilometry je pravidelnost.'),
        ('Můžu se připravit doma?', 'Část ano: běhy, silový trénink s činkami a vlastní vahou. Specifické stanice (SkiErg, sáně, veslování) si vyzkoušej v gymu aspoň několikrát před závodem.'),
        ('Jak se mám připravit na pacing?', 'Použij <a href="/cs/hyrox-pacing-kalkulacka">kalkulačku Hyrox pacing</a>: zadej cílový čas a získáš tempo běhů a časy stanic. Po simulaci je nahraď skutečnými splity.'),
    ],
    sections=[
        ('pre-koho', 'Pro koho je plán', '''    <ul>
      <li>Zvládneš uběhnout <strong>5 km vkuse</strong>, i pomalu.</li>
      <li>Trénuješ <strong>3 až 4krát týdně</strong> a znáš základní cviky (dřep, mrtvý tah, výpady, tlaky).</li>
      <li>Máš 8 týdnů a cíl dokončit první Hyrox, ne vyhrát kategorii.</li>
    </ul>
    <p>Pokud tyto podmínky nesplňuješ, přidej si na začátek základní fázi. Pokud máš zranění nebo zdravotní omezení, poraď se s lékařem. Plán je ukázkový, přizpůsob si ho svému času a schopnostem.</p>'''),
        ('format', 'Hyrox ve zkratce', '''    <p>Hyrox je <strong>8 kol, každé z nich tvoří 1 km běhu a jedna funkční stanice</strong>. Stanice jdou v tomto pořadí: SkiErg, Sled Push, Sled Pull, Burpee Broad Jumps, Rowing, Farmers Carry, Sandbag Lunges a Wall Balls. Víc o formátu najdeš v článku <a href="/hyrox-pre-zaciatocnikov">Hyrox pro začátečníky</a> (slovensky). Váhy závisejí na kategorii a sezóně, ověř si je v oficiálních pravidlech.</p>'''),
        ('tyzden', 'Struktura týdne', '''    <table>
      <thead><tr><th>Den</th><th>Trénink</th></tr></thead>
      <tbody>
        <tr><td><strong>1</strong></td><td>Lehký běh v konverzačním tempu</td></tr>
        <tr><td><strong>2</strong></td><td>Silový trénink: dřep, mrtvý tah, tlaky, tahy, výpady</td></tr>
        <tr><td><strong>3</strong></td><td>Intervaly nebo tempový běh</td></tr>
        <tr><td><strong>4</strong></td><td>Hybridní trénink: běh střídaný se stanicemi</td></tr>
        <tr><td>5 až 7</td><td>Odpočinek, procházka, mobilita</td></tr>
      </tbody>
    </table>'''),
        ('plan', 'Plán týden po týdnu', '''    <table>
      <thead><tr><th>Týden</th><th>Lehký běh</th><th>Síla</th><th>Intervaly / tempo</th><th>Hybrid</th></tr></thead>
      <tbody>
        <tr><td><strong>1</strong></td><td>30 min</td><td>Celé tělo, 3 × 8–10</td><td>5 × 2 min těžce / 2 min lehce</td><td>4 × (400 m běh + 15 wall balls)</td></tr>
        <tr><td><strong>2</strong></td><td>35 min</td><td>Stejné cviky, přidej váhu</td><td>6 × 2 min</td><td>4 × (400 m + 20 wall balls)</td></tr>
        <tr><td><strong>3</strong></td><td>40 min</td><td>Síla + farmers carry 4 × 40 m</td><td>4 × 4 min tempo / 2 min lehce</td><td>5 × (500 m + 250 m SkiErg)</td></tr>
        <tr><td><strong>4</strong> (odlehčený)</td><td>30 min</td><td>2 × 8, lehčeji</td><td>4 × 2 min</td><td>3 × (500 m + stanice)</td></tr>
        <tr><td><strong>5</strong></td><td>45 min</td><td>Síla + výpady s pytlem 4 × 20 m</td><td>3 × 6 min tempo / 2 min lehce</td><td>6 × (600 m + stanice)</td></tr>
        <tr><td><strong>6</strong></td><td>50 min</td><td>Síla + sled push a pull</td><td>5 × 4 min</td><td>6 × (800 m + stanice), stanice naostro</td></tr>
        <tr><td><strong>7</strong> (simulace)</td><td>40 min</td><td>Lehká síla</td><td>—</td><td>Poloviční nebo celá simulace Hyroxu v cílovém tempu</td></tr>
        <tr><td><strong>8</strong> (taper)</td><td>25–30 min</td><td>2 krátké tréninky, 2 × 6</td><td>4 × 1 min svižně</td><td>15 min lehká aktivace pár dní před závodem</td></tr>
      </tbody>
    </table>
    <p class="note">Ukázkový plán, ne univerzální předpis. Pokud ti některý týden nevyjde, nedohánej ho, pokračuj dalším.</p>'''),
        ('stanice', 'Nácvik stanic: technika ve zkratce', '''    <ul>
      <li><strong>SkiErg:</strong> tah z boků a trupu, nejen z rukou. Drž rovnoměrný rytmus.</li>
      <li><strong>Sled Push:</strong> nízké těžiště, krátké a rychlé kroky, plynule.</li>
      <li><strong>Sled Pull:</strong> nohy a trup pracují, ruce jen přenášejí lano.</li>
      <li><strong>Burpee Broad Jumps:</strong> krátké skoky v rytmu, šetři dech a ruce.</li>
      <li><strong>Rowing:</strong> nejdřív nohy, potom trup, nakonec ruce.</li>
      <li><strong>Farmers Carry:</strong> pevný stisk, krátké kroky, nepouštěj závaží bez potřeby.</li>
      <li><strong>Sandbag Lunges:</strong> kolena pod kontrolou, pytel stabilně na ramenou.</li>
      <li><strong>Wall Balls:</strong> plynulý dřep a hod, krátké série s krátkými pauzami.</li>
    </ul>'''),
        ('preteky', 'Poslední týden a den závodu', '''    <ul>
      <li><strong>Nezkoušej nové věci.</strong> Jídlo, obuv a oblečení musí být ověřené z tréninku.</li>
      <li><strong>Spi.</strong> V posledních dnech před závodem je spánek nejlepší příprava.</li>
      <li><strong>Startuj pomalu.</strong> První kilometr se na adrenalin zdá lehký a přehnané tempo zaplatíš ve druhé polovině.</li>
      <li><strong>Drž pacing.</strong> Cílové tempo si spočítej v <a href="/cs/hyrox-pacing-kalkulacka">kalkulačce Hyrox pacing</a>.</li>
    </ul>'''),
        ('sledovanie', 'Jak sledovat pokrok', '''    <p>Po každé simulaci si zapiš splity všech běhů a stanic. Uvidíš, kde ztrácíš čas, a můžeš tam zaměřit trénink. Silový pokrok sleduj v <a href="/cs/1rm-kalkulacka">kalkulačce 1RM</a> a v <a href="/cs/blog/treninkovy-denik">tréninkovém deníku</a>.</p>'''),
    ],
))

import extras_loader
ARTICLES = extras_loader.merge(ARTICLES, LANG, {'health': DISC_HEALTH, 'train': DISC_TRAIN})
