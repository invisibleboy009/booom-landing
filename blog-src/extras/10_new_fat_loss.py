# NEW article: losing fat without losing muscle (sk / en / cs). Format: see extras_loader.py.

NEW = {}

# ═══════════════════════════════════════ SK ═══════════════════════════════════════
NEW['sk'] = dict(
    slug='chudnutie-bez-straty-svalov',
    title='Chudnutie bez straty svalov: ako schudnúť tuk a udržať sval',
    title_tag='Chudnutie bez straty svalov: deficit a tréning | BOOOM',
    h1='Chudnutie bez straty svalov: ako schudnúť tuk a udržať sval',
    crumb='Chudnutie bez straty svalov',
    desc='Ako schudnúť tuk a udržať svaly: veľkosť kalorického deficitu, bielkoviny, silový tréning, kroky, spánok a sledovanie pokroku. Praktický návod s príkladom.',
    card='Aký veľký deficit, koľko bielkovín a ako trénovať, aby z tela odchádzal tuk, nie svaly.',
    kw='chudnutie bez straty svalov, ako schudnúť a udržať svaly, kalorický deficit, bielkoviny pri chudnutí, silový tréning pri chudnutí, redukcia tuku',
    lead='Schudnúť sa dá aj tak, že prídeš o časť svalov. Výsledok potom nevyzerá ani nefunguje dobre: menšie telo, ale mäkšie a slabšie. Tu je návod, ako deficit nastaviť, čo jesť, ako trénovať a ako zistiť, či ti to funguje.',
    cta=('Sleduj silu aj váhu na jednom mieste', 'BOOOM zapisuje tréningy s automatickými rekordmi a počíta makrá, takže hneď vidíš, či ti sila v deficite drží.'),
    disc='health',
    faq=[
        ('Dá sa naraz schudnúť tuk a pribrať sval?', 'V niektorých situáciách áno: pri úplných začiatočníkoch, pri návrate po dlhšej pauze alebo pri vyššom podiele tuku, ak je dosť bielkovín a tréning je ťažký. Pokročilí zvyčajne cielia len na udržanie svalov, každý prírastok je pri deficite pomalý.'),
        ('Koľko kilogramov týždenne je rozumné schudnúť?', 'Bežné odporúčanie je 0,5 až 1 % telesnej hmotnosti týždenne, čo je pri 80 kg zhruba 0,4 až 0,8 kg. Pomalšie tempo je v poriadku a zvyčajne lepšie šetrí svaly aj energiu.'),
        ('Musím počítať kalórie?', 'Nemusíš, ale niekoľko týždňov ich zapisovať je užitočné, lebo si nastavíš odhad porcií. Cieľ vieš zistiť v <a href="/kalorie-kalkulacka">kalorickej kalkulačke</a>. Ak ťa počítanie stresuje alebo naň myslíš neustále, radšej sa poraď s odborníkom.'),
        ('Prečo mi váha stojí, hoci jem v deficite?', 'Denná hmotnosť kolíše o viac než tuk: mení sa voda, soľ, obsah čriev aj hormonálny cyklus. Sleduj priemer za týždeň a obvod pása aspoň 2 až 3 týždne. Ak sa nič nehýbe, zvýš kroky alebo mierne uber kalórie, napríklad o 100 až 150 kcal.'),
        ('Je lepšie kardio, alebo silový tréning?', 'Na udržanie svalov je základ silový tréning, kardio a kroky pomáhajú zvýšiť výdaj energie. Najlepšie funguje kombinácia: ťažké zdvíhanie 2 až 4-krát týždenne a k tomu chôdza alebo mierne kardio.'),
        ('Ako dlho môžem byť v deficite?', 'Pevný limit neexistuje. Mnohí robia bloky 8 až 12 týždňov a potom si dajú 1 až 2 týždne na úrovni udržiavania. Ak ťa sprevádza silná únava, zlý spánok a klesajúca sila, deficit ukonči skôr a poraď sa s odborníkom.'),
    ],
    sections=[
        ('princip', 'Princíp: prečo je sval v deficite v ohrození', '''    <p>Tuk ubúda, keď dlhodobo prijímaš menej energie, než spotrebuješ. Chýbajúcu energiu si telo berie z tukových zásob, ale aj zo svalov. Sval je pre telo drahý: jeho udržiavanie stojí energiu, a ak mu nedáš dôvod, prečo ho má nechať, časť môže zmiznúť.</p>
    <p>Rozhoduje teda signál. Ak dostatok bielkovín a ťažký tréning posielajú správu „tento sval potrebujem“, väčšina úbytku ide na tuk. Ak ješ málo bielkovín a takmer netrénuješ, schudneš, ale so svalmi. Úplní začiatočníci a ľudia po dlhšej pauze môžu pri miernom deficite dokonca sval pribrať, pokročilí ho zvyčajne len udržia.</p>
    <p>Na výsledok stačia štyri veci:</p>
    <ul>
      <li>mierny kalorický deficit,</li>
      <li>dosť bielkovín,</li>
      <li>silový tréning s ťažkými váhami,</li>
      <li>dosť spánku a regenerácie.</li>
    </ul>'''),
        ('deficit', 'Aký veľký deficit', '''    <p>Väčší deficit neznamená lepší výsledok. Čím rýchlejšie chudneš, tým väčšie je riziko straty svalov, sily a energie. Bežné odporúčanie je <strong>15 až 20 % pod dennou spotrebou (TDEE)</strong>, čo zodpovedá úbytku približne <strong>0,5 až 1 % telesnej hmotnosti týždenne</strong>. Svoje TDEE si spočítaš v <a href="/kalorie-kalkulacka">kalorickej kalkulačke</a>.</p>
    <table>
      <thead><tr><th>Deficit</th><th class="n">Kalórie denne (TDEE 2&nbsp;759)</th><th>Poznámka</th></tr></thead>
      <tbody>
        <tr><td>10 %</td><td class="n">2&nbsp;483 kcal</td><td>Pomalé a šetrné k tréningu</td></tr>
        <tr><td>15 %</td><td class="n">2&nbsp;345 kcal</td><td>Dobrá voľba pre štíhlejších a pokročilých</td></tr>
        <tr><td>20 %</td><td class="n">2&nbsp;207 kcal</td><td>Horná hranica pre väčšinu ľudí</td></tr>
        <tr><td>25 % a viac</td><td class="n">2&nbsp;069 kcal a menej</td><td>Rastie riziko straty svalov a únavy</td></tr>
      </tbody>
    </table>
    <div class="ex">
      <p><strong>Príklad: 80 kg, TDEE 2&nbsp;759 kcal</strong></p>
      <ul>
        <li>Deficit 20 %: 2&nbsp;759 × 0,8 ≈ <strong>2&nbsp;207 kcal denne</strong>, teda zhruba o 550 kcal menej.</li>
        <li>Očakávaný úbytok: 0,5 až 1 % z 80 kg je <strong>0,4 až 0,8 kg týždenne</strong>.</li>
        <li>Týždenný deficit okolo 3&nbsp;850 kcal zodpovedá orientačne pol kilu tuku.</li>
      </ul>
      <p>V prvých dňoch môže hmotnosť klesnúť rýchlejšie kvôli vode a obsahu čriev. Nie je to tuk, tak z toho netvor trend.</p>
    </div>
    <p>Kto má tuku už menej, mal by zostať skôr pri spodnej hranici. Kto má viac tuku, znesie aj vyšší deficit.</p>'''),
        ('bielkoviny', 'Bielkoviny: najdôležitejšia makroživina', '''    <p>Pri chudnutí sa oplatí byť pri hornej hranici odporúčaní, teda <strong>1,8 až 2,2 g bielkovín na kg</strong> telesnej hmotnosti denne. Pre 80 kg je to 144 až 176 g, ideálne rozložených do 3 až 5 jedál po približne 0,3 až 0,4 g na kg (pri 80 kg zhruba 25 až 35 g v jedle). Bielkoviny pomáhajú zachovať sval, lepšie zasýtia a telo na ich spracovanie spotrebuje viac energie ako pri sacharidoch alebo tukoch.</p>
    <p>Rozsah vychádza z metaanalýzy Morton a kol. (2018, British Journal of Sports Medicine). Zdroje, rozloženie počas dňa a príklady potravín nájdeš v článku <a href="/blog/kolko-bielkovin-denne">Koľko bielkovín denne</a>. Proteínový prášok je len pohodlný spôsob, ako sa k číslu dostať, nie povinnosť.</p>'''),
        ('trening', 'Tréning: zdvíhaj ďalej ťažko', '''    <p>Sval si telo nechá vtedy, keď ho tréning naozaj zaťažuje. Preto v deficite netreba prejsť na „tónovanie“ s ľahkými váhami a množstvom opakovaní. Drž sa ťažkých základných cvikov a približne rovnakej záťaže ako pred diétou.</p>
    <ul>
      <li><strong>Drž intenzitu.</strong> Váhy a blízkosť k limitu série sú dôležitejšie než celkový počet sérií.</li>
      <li><strong>Zníž objem, ak trpí regenerácia.</strong> Ak regenerácia nestíha, uber radšej pár sérií (napríklad o tretinu) než váhu na tyči.</li>
      <li><strong>Cieľom je udržať silu.</strong> Ak sila v hlavných cvikoch drží alebo klesne len mierne, sval zrejme držíš.</li>
      <li><strong>Pokračuj v progresii.</strong> Aj pomalšie pridávanie je úspech, viac v článku <a href="/blog/progresivne-pretazenie">Progresívne preťaženie</a>.</li>
    </ul>
    <p>Silu a objem najľahšie strážiš v <a href="/blog/treningovy-dennik">tréningovom denníku</a>: rýchlo v ňom uvidíš, kedy sa výkon láme.</p>'''),
        ('kardio-kroky', 'Kardio a kroky: nástroje, nie trest', '''    <p>Kardio ani kroky nie sú trestom za zjedené jedlo. Sú to nástroje, ktorými zvýšiš výdaj bez ďalšieho rezania kalórií.</p>
    <ul>
      <li><strong>Kroky a bežný pohyb (NEAT)</strong> sú často najlacnejší spôsob, ako zvýšiť výdaj. Chôdza takmer nezaťažuje regeneráciu, takže sa dobre kombinuje s ťažkým tréningom. Skús pridať 2&nbsp;000 až 3&nbsp;000 krokov denne oproti dnešku.</li>
      <li><strong>Kardio</strong> stačí 2 až 3-krát týždenne v miernej intenzite. Ťažké intervaly tiež fungujú, ale dávkuj ich opatrne, lebo sa počítajú do celkovej únavy.</li>
    </ul>
    <p>Ak sa pripravuješ na beh alebo Hyrox, kardio máš v pláne tak či tak. Len počítaj s tým, že deficit a veľký objem behania sa často navzájom ubíjajú.</p>'''),
        ('spanok-stres', 'Spánok a stres', '''    <p>Dospelým sa bežne odporúča 7 až 9 hodín spánku. Pri nedostatku spánku býva väčší hlad, chuť na sladké aj horší výkon v tréningu, a diéta sa drží ťažšie. Stres a málo regenerácie robia podobný problém.</p>
    <p>Ak chudneš, spánok je súčasť plánu, nie bonus. Skús mať pravidelný čas spánku a nenechávaj sa nachytať večerným hladom z nedospania. Viac k spánku a regenerácii nájdeš v článku <a href="/blog/regeneracia-a-spanok">Regenerácia a spánok</a>.</p>'''),
        ('sledovanie', 'Ako sledovať, či to funguje', '''    <p>Jedno číslo na váhe je málo. Sleduj viacero ukazovateľov naraz:</p>
    <table>
      <thead><tr><th>Ukazovateľ</th><th>Ako</th><th>Čo ti povie</th></tr></thead>
      <tbody>
        <tr><td><strong>Hmotnosť</strong></td><td>Vážiť sa ráno rovnako, počítať týždenný priemer</td><td>Tempo úbytku, bez denných výkyvov</td></tr>
        <tr><td><strong>Obvod pása</strong></td><td>Raz týždenne, v rovnakom mieste</td><td>Úbytok tuku v oblasti brucha</td></tr>
        <tr><td><strong>Fotky</strong></td><td>Každé 2 až 4 týždne, rovnaké svetlo a póza</td><td>Zmeny, ktoré čísla neukážu</td></tr>
        <tr><td><strong>Odhad tuku</strong></td><td><a href="/percento-telesneho-tuku">Kalkulačka US Navy</a></td><td>Trend v čase, nie presné číslo</td></tr>
        <tr><td><strong>Sila</strong></td><td>Záznamy v tréningovom denníku</td><td>Či držíš sval</td></tr>
      </tbody>
    </table>
    <p>Ideálny obraz je klesajúci týždenný priemer a obvod pása pri stabilnej sile. Varovné signály sú:</p>
    <ul>
      <li>sila klesá vo viacerých cvikoch naraz,</li>
      <li>výrazná únava a zhoršený spánok,</li>
      <li>hlad, ktorý sa nedá zvládnuť, alebo pokles nálady.</li>
    </ul>
    <p>V takom prípade deficit zmierni. Ak diétu držíš dlhšie (zhruba 8 až 12 týždňov) alebo sa výkon dlhodobo zhoršuje, pomôže <strong>diet break</strong>: 1 až 2 týždne na úrovni udržiavania (TDEE). Silu, rekordy a makrá vieš sledovať aj v appke <a href="https://app.booom.fit">BOOOM</a>.</p>'''),
        ('kedy-nie', 'Kedy nie je vhodný agresívny deficit', '''    <p>Nie sme lekári a tento návod nie je pre každého. Pred chudnutím sa poraď s lekárom alebo nutričným terapeutom, ak sa ťa týka niečo z tohto:</p>
    <ul>
      <li>vek do 18 rokov (telo rastie a potrebuje energiu),</li>
      <li>tehotenstvo alebo dojčenie,</li>
      <li>porucha príjmu potravy v minulosti alebo v súčasnosti, prípadne úzkosť z počítania kalórií a váženia,</li>
      <li>chronické ochorenie (napríklad cukrovka, štítna žľaza, srdce, obličky) alebo pravidelné lieky,</li>
      <li>už nízka telesná hmotnosť.</li>
    </ul>
    <p>V týchto prípadoch deficit nastavuje odborník, nie kalkulačka.</p>'''),
    ],
)

# ═══════════════════════════════════════ EN ═══════════════════════════════════════
NEW['en'] = dict(
    slug='lose-fat-keep-muscle',
    title='Lose fat, keep muscle: how to diet without losing strength',
    title_tag='Lose Fat, Keep Muscle: Deficit and Training | BOOOM',
    h1='Lose fat, keep muscle: how to diet without losing strength',
    crumb='Lose fat, keep muscle',
    desc="How to lose fat and keep muscle: how big a calorie deficit to run, protein, lifting, steps, sleep and how to track progress. A practical guide.",
    card="How big a deficit, how much protein and how to train so that what leaves your body is fat, not muscle.",
    kw="lose fat keep muscle, lose weight without losing muscle, calorie deficit, protein when dieting, strength training while cutting, fat loss",
    lead="You can lose weight and lose part of your muscle along with it. The result looks and performs worse: a smaller body, but a softer and weaker one. Here is how to set the deficit, what to eat, how to train and how to tell whether it is working.",
    cta=("Track strength and weight in one place", "BOOOM logs your workouts with automatic PRs and counts your macros, so you can see right away whether your strength holds up in a deficit."),
    disc='health',
    faq=[
        ("Can you lose fat and gain muscle at the same time?", "In some situations yes: complete beginners, people returning after a long break, or people with higher body fat, provided protein is high enough and training is hard. Advanced lifters usually aim only to maintain muscle, and any gain in a deficit is slow."),
        ("How much weight per week is reasonable to lose?", "The usual recommendation is 0.5 to 1 % of body weight per week, which is roughly 0.4 to 0.8 kg for someone weighing 80 kg. A slower pace is fine and usually protects muscle and energy better."),
        ("Do I have to count calories?", "You do not have to, but logging them for a few weeks is useful because it calibrates your sense of portion sizes. You can find your target in the <a href=\"/en/calorie-calculator\">calorie calculator</a>. If counting stresses you out or you think about it constantly, talk to a professional instead."),
        ("Why is the scale not moving when I am eating in a deficit?", "Daily weight moves for reasons other than fat: water, salt, gut contents and hormonal cycles all play a part. Track a weekly average and your waist for at least 2 to 3 weeks. If nothing changes, add steps or trim calories slightly, for example by 100 to 150 kcal."),
        ("Is cardio or strength training better for fat loss?", "For keeping muscle, strength training is the foundation, while cardio and steps help raise energy expenditure. A combination works best: heavy lifting 2 to 4 times a week plus walking or moderate cardio."),
        ("How long can I stay in a deficit?", "There is no fixed limit. Many people run blocks of 8 to 12 weeks and then take 1 to 2 weeks at maintenance. If you have heavy fatigue, poor sleep and falling strength, end the deficit sooner and talk to a professional."),
    ],
    sections=[
        ('princip', 'The principle: why muscle is at risk in a deficit', '''    <p>Fat goes down when you consistently take in less energy than you use. Your body covers the missing energy from fat stores, but also from muscle. Muscle is expensive to maintain, and if you give the body no reason to keep it, some of it can disappear.</p>
    <p>So what matters is the signal. If enough protein and hard training send the message "I need this muscle", most of the loss comes from fat. If you eat little protein and barely train, you will lose weight, but with muscle included. Complete beginners and people returning after a break can even gain some muscle in a mild deficit, while advanced lifters usually just hold on to what they have.</p>
    <p>Four things are enough to get there:</p>
    <ul>
      <li>a moderate calorie deficit,</li>
      <li>enough protein,</li>
      <li>strength training with heavy weights,</li>
      <li>enough sleep and recovery.</li>
    </ul>'''),
        ('deficit', 'How big should the deficit be', '''    <p>A bigger deficit does not mean a better result. The faster you lose, the higher the risk of losing muscle, strength and energy. The usual recommendation is <strong>15 to 20 % below your daily expenditure (TDEE)</strong>, which corresponds to losing roughly <strong>0.5 to 1 % of body weight per week</strong>. You can work out your TDEE in the <a href="/en/calorie-calculator">calorie calculator</a>.</p>
    <table>
      <thead><tr><th>Deficit</th><th class="n">Daily calories (TDEE 2,759)</th><th>Note</th></tr></thead>
      <tbody>
        <tr><td>10 %</td><td class="n">2,483 kcal</td><td>Slow and easy on training</td></tr>
        <tr><td>15 %</td><td class="n">2,345 kcal</td><td>A good choice for leaner and more advanced lifters</td></tr>
        <tr><td>20 %</td><td class="n">2,207 kcal</td><td>Upper limit for most people</td></tr>
        <tr><td>25 % or more</td><td class="n">2,069 kcal or less</td><td>Higher risk of muscle loss and fatigue</td></tr>
      </tbody>
    </table>
    <div class="ex">
      <p><strong>Example: 80 kg, TDEE 2,759 kcal</strong></p>
      <ul>
        <li>20 % deficit: 2,759 × 0.8 ≈ <strong>2,207 kcal per day</strong>, so roughly 550 kcal less.</li>
        <li>Expected loss: 0.5 to 1 % of 80 kg is <strong>0.4 to 0.8 kg per week</strong>.</li>
        <li>A weekly deficit of about 3,850 kcal corresponds, roughly speaking, to half a kilo of fat.</li>
      </ul>
      <p>In the first few days weight can drop faster because of water and gut contents. That is not fat, so do not treat it as your trend.</p>
    </div>
    <p>If you are already lean, stay nearer the lower end. If you carry more fat, you can tolerate a bigger deficit.</p>'''),
        ('bielkoviny', 'Protein: the most important macro', '''    <p>When dieting it pays to sit at the top of the recommended range, that is <strong>1.8 to 2.2 g of protein per kg</strong> of body weight per day. For 80 kg that is 144 to 176 g, ideally spread over 3 to 5 meals of roughly 0.3 to 0.4 g per kg each (about 25 to 35 g per meal at 80 kg). Protein helps preserve muscle, keeps you fuller and costs the body more energy to process than carbohydrate or fat.</p>
    <p>The range comes from the Morton et al. (2018, British Journal of Sports Medicine) meta-analysis. Sources, distribution across the day and food examples are in the article <a href="/en/blog/how-much-protein-per-day">How much protein per day</a>. Protein powder is just a convenient way to reach the number, not a requirement.</p>'''),
        ('trening', 'Training: keep lifting heavy', '''    <p>Your body keeps muscle when training really challenges it. That is why a deficit is no reason to switch to "toning" with light weights and lots of reps. Stick to heavy compound lifts and about the same load you used before the diet.</p>
    <ul>
      <li><strong>Keep the intensity.</strong> The weights and how close you get to your limit matter more than total sets.</li>
      <li><strong>Reduce volume if recovery suffers.</strong> If you are worn out, drop a few sets (for example by a third) rather than weight on the bar.</li>
      <li><strong>Aim to maintain strength.</strong> If strength in your main lifts holds or drops only slightly, you are probably keeping your muscle.</li>
      <li><strong>Keep progressing.</strong> Even slower progress is a win, more in the article <a href="/en/blog/progressive-overload">Progressive overload</a>.</li>
    </ul>
    <p>The easiest place to watch strength and volume is a <a href="/en/blog/training-log">training log</a>: you will quickly see when performance starts to slip.</p>'''),
        ('kardio-kroky', 'Cardio and steps: tools, not punishment', '''    <p>Neither cardio nor steps are a punishment for something you ate. They are tools for raising expenditure without cutting yet more calories.</p>
    <ul>
      <li><strong>Steps and everyday movement (NEAT)</strong> are often the cheapest way to raise expenditure. Walking barely taxes recovery, so it combines well with heavy training. Try adding 2,000 to 3,000 steps a day compared with now.</li>
      <li><strong>Cardio</strong> 2 to 3 times a week at moderate intensity is enough. Hard intervals also work, but dose them carefully because they count towards your total fatigue.</li>
    </ul>
    <p>If you are preparing for running or Hyrox, you already have cardio in your plan. Just keep in mind that a deficit and a high running volume often work against each other.</p>'''),
        ('spanok-stres', 'Sleep and stress', '''    <p>Adults are commonly advised to get 7 to 9 hours of sleep. When sleep is short, hunger tends to be higher, cravings for sweet food stronger and training performance worse, and it is harder to stick to a diet. Stress and poor recovery cause a similar problem.</p>
    <p>If you are dieting, sleep is part of the plan, not a bonus. Try to keep a regular bedtime. You will find more in the article <a href="/en/blog/recovery-and-sleep">Recovery and sleep</a>.</p>'''),
        ('sledovanie', 'How to track whether it is working', '''    <p>A single number on the scale is not enough. Track several indicators at once:</p>
    <table>
      <thead><tr><th>Indicator</th><th>How</th><th>What it tells you</th></tr></thead>
      <tbody>
        <tr><td><strong>Body weight</strong></td><td>Weigh in the same way each morning, use the weekly average</td><td>Rate of loss, without daily noise</td></tr>
        <tr><td><strong>Waist</strong></td><td>Once a week, at the same spot</td><td>Fat loss around the midsection</td></tr>
        <tr><td><strong>Photos</strong></td><td>Every 2 to 4 weeks, same light and pose</td><td>Changes the numbers miss</td></tr>
        <tr><td><strong>Body-fat estimate</strong></td><td><a href="/en/body-fat-calculator">US Navy calculator</a></td><td>Trend over time, not an exact figure</td></tr>
        <tr><td><strong>Strength</strong></td><td>Entries in your training log</td><td>Whether you are keeping muscle</td></tr>
      </tbody>
    </table>
    <p>The ideal picture is a falling weekly average and waist with steady strength. Warning signs are:</p>
    <ul>
      <li>strength falling in several lifts at once,</li>
      <li>marked fatigue and worse sleep,</li>
      <li>hunger you cannot manage, or a drop in mood.</li>
    </ul>
    <p>In that case ease off the deficit. If you have been dieting for longer (roughly 8 to 12 weeks) or performance has been slipping for a while, a <strong>diet break</strong> can help: 1 to 2 weeks at maintenance (TDEE). You can also track strength, PRs and macros in the <a href="https://app.booom.fit">BOOOM</a> app.</p>'''),
        ('kedy-nie', 'Who should not diet aggressively', '''    <p>We are not doctors and this guide is not for everyone. Talk to a doctor or a dietitian before dieting if any of this applies to you:</p>
    <ul>
      <li>being under 18 (the body is still growing and needs energy),</li>
      <li>pregnancy or breastfeeding,</li>
      <li>a past or current eating disorder, or anxiety about counting calories and weighing yourself,</li>
      <li>a chronic condition (for example diabetes, thyroid, heart or kidney disease) or regular medication,</li>
      <li>an already low body weight.</li>
    </ul>
    <p>In these cases the deficit should be set by a professional, not a calculator.</p>'''),
    ],
)

# ═══════════════════════════════════════ CS ═══════════════════════════════════════
NEW['cs'] = dict(
    slug='hubnuti-bez-ztraty-svalu',
    title='Hubnutí bez ztráty svalů: jak zhubnout tuk a udržet sval',
    title_tag='Hubnutí bez ztráty svalů: deficit a trénink | BOOOM',
    h1='Hubnutí bez ztráty svalů: jak zhubnout tuk a udržet sval',
    crumb='Hubnutí bez ztráty svalů',
    desc='Jak zhubnout tuk a udržet svaly: velikost kalorického deficitu, bílkoviny, silový trénink, kroky, spánek a sledování pokroku. Praktický návod s příkladem.',
    card='Jak velký deficit, kolik bílkovin a jak trénovat, aby z těla odcházel tuk, ne svaly.',
    kw='hubnutí bez ztráty svalů, jak zhubnout a udržet svaly, kalorický deficit, bílkoviny při hubnutí, silový trénink při hubnutí, redukce tuku',
    lead='Zhubnout jde i tak, že přijdeš o část svalů. Výsledek pak nevypadá ani nefunguje dobře: menší tělo, ale měkčí a slabší. Tady je návod, jak nastavit deficit, co jíst, jak trénovat a jak poznat, že ti to funguje.',
    cta=('Sleduj sílu i váhu na jednom místě', 'BOOOM zapisuje tréninky s automatickými rekordy a počítá makra, takže hned vidíš, jestli ti síla v deficitu drží.'),
    disc='health',
    faq=[
        ('Dá se najednou zhubnout tuk a přibrat sval?', 'V některých situacích ano: u úplných začátečníků, při návratu po delší pauze nebo při vyšším podílu tuku, pokud je dost bílkovin a trénink je těžký. Pokročilí většinou cílí jen na udržení svalů, každý přírůstek je při deficitu pomalý.'),
        ('Kolik kilogramů týdně je rozumné zhubnout?', 'Běžné doporučení je 0,5 až 1 % tělesné hmotnosti týdně, což je při 80 kg zhruba 0,4 až 0,8 kg. Pomalejší tempo je v pořádku a obvykle lépe šetří svaly i energii.'),
        ('Musím počítat kalorie?', 'Nemusíš, ale několik týdnů je zapisovat je užitečné, protože si nastavíš odhad porcí. Cíl zjistíš v <a href="/cs/kaloricka-kalkulacka">kalorické kalkulačce</a>. Pokud tě počítání stresuje nebo na ně myslíš pořád, raději se poraď s odborníkem.'),
        ('Proč mi váha stojí, i když jím v deficitu?', 'Denní hmotnost kolísá z víc důvodů než jen kvůli tuku: mění se voda, sůl, obsah střev i hormonální cyklus. Sleduj týdenní průměr a obvod pasu alespoň 2 až 3 týdny. Pokud se nic nehýbe, přidej kroky nebo mírně uber kalorie, například o 100 až 150 kcal.'),
        ('Je lepší kardio, nebo silový trénink?', 'K udržení svalů je základ silový trénink, kardio a kroky pomáhají zvýšit výdej energie. Nejlíp funguje kombinace: těžké zvedání 2 až 4krát týdně a k tomu chůze nebo mírné kardio.'),
        ('Jak dlouho můžu být v deficitu?', 'Pevný limit neexistuje. Mnozí dělají bloky 8 až 12 týdnů a pak si dají 1 až 2 týdny na úrovni udržování. Pokud tě provází silná únava, špatný spánek a klesající síla, deficit ukonči dřív a poraď se s odborníkem.'),
    ],
    sections=[
        ('princip', 'Princip: proč je sval v deficitu v ohrožení', '''    <p>Tuk ubývá, když dlouhodobě přijímáš méně energie, než spotřebuješ. Chybějící energii si tělo bere z tukových zásob, ale i ze svalů. Sval je pro tělo drahý: jeho udržování stojí energii, a když mu nedáš důvod, proč ho má nechat, část může zmizet.</p>
    <p>Rozhoduje tedy signál. Když dostatek bílkovin a těžký trénink posílají zprávu „tenhle sval potřebuji“, většina úbytku jde na tuk. Když jíš málo bílkovin a skoro netrénuješ, zhubneš, ale i se svaly. Úplní začátečníci a lidé po delší pauze mohou při mírném deficitu dokonce sval přibrat, pokročilí ho většinou jen udrží.</p>
    <p>Na výsledek stačí čtyři věci:</p>
    <ul>
      <li>mírný kalorický deficit,</li>
      <li>dost bílkovin,</li>
      <li>silový trénink s těžkými váhami,</li>
      <li>dost spánku a regenerace.</li>
    </ul>'''),
        ('deficit', 'Jak velký deficit', '''    <p>Větší deficit neznamená lepší výsledek. Čím rychleji hubneš, tím větší je riziko ztráty svalů, síly a energie. Běžné doporučení je <strong>15 až 20 % pod denním výdejem (TDEE)</strong>, což odpovídá úbytku zhruba <strong>0,5 až 1 % tělesné hmotnosti týdně</strong>. Své TDEE si spočítáš v <a href="/cs/kaloricka-kalkulacka">kalorické kalkulačce</a>.</p>
    <table>
      <thead><tr><th>Deficit</th><th class="n">Kalorie denně (TDEE 2&nbsp;759)</th><th>Poznámka</th></tr></thead>
      <tbody>
        <tr><td>10 %</td><td class="n">2&nbsp;483 kcal</td><td>Pomalé a šetrné k tréninku</td></tr>
        <tr><td>15 %</td><td class="n">2&nbsp;345 kcal</td><td>Dobrá volba pro štíhlejší a pokročilé</td></tr>
        <tr><td>20 %</td><td class="n">2&nbsp;207 kcal</td><td>Horní hranice pro většinu lidí</td></tr>
        <tr><td>25 % a víc</td><td class="n">2&nbsp;069 kcal a méně</td><td>Roste riziko ztráty svalů a únavy</td></tr>
      </tbody>
    </table>
    <div class="ex">
      <p><strong>Příklad: 80 kg, TDEE 2&nbsp;759 kcal</strong></p>
      <ul>
        <li>Deficit 20 %: 2&nbsp;759 × 0,8 ≈ <strong>2&nbsp;207 kcal denně</strong>, tedy zhruba o 550 kcal méně.</li>
        <li>Očekávaný úbytek: 0,5 až 1 % z 80 kg je <strong>0,4 až 0,8 kg týdně</strong>.</li>
        <li>Týdenní deficit kolem 3&nbsp;850 kcal odpovídá orientačně půl kilu tuku.</li>
      </ul>
      <p>V prvních dnech může hmotnost klesnout rychleji kvůli vodě a obsahu střev. Není to tuk, takže z toho nedělej trend.</p>
    </div>
    <p>Kdo má tuku už méně, měl by zůstat spíš u spodní hranice. Kdo má víc tuku, snese i vyšší deficit.</p>'''),
        ('bielkoviny', 'Bílkoviny: nejdůležitější makroživina', '''    <p>Při hubnutí se vyplatí být u horní hranice doporučení, tedy <strong>1,8 až 2,2 g bílkovin na kg</strong> tělesné hmotnosti denně. Pro 80 kg je to 144 až 176 g, ideálně rozložených do 3 až 5 jídel po přibližně 0,3 až 0,4 g na kg (u 80 kg zhruba 25 až 35 g v jídle). Bílkoviny pomáhají zachovat sval, lépe zasytí a tělo na jejich zpracování spotřebuje víc energie než u sacharidů nebo tuků.</p>
    <p>Rozsah vychází z metaanalýzy Morton a kol. (2018, British Journal of Sports Medicine). Zdroje, rozložení během dne a příklady potravin najdeš v článku <a href="/cs/blog/kolik-bilkovin-denne">Kolik bílkovin denně</a>. Proteinový prášek je jen pohodlný způsob, jak se k číslu dostat, ne povinnost.</p>'''),
        ('trening', 'Trénink: zvedej dál těžce', '''    <p>Sval si tělo nechá tehdy, když ho trénink opravdu zatěžuje. Proto v deficitu není třeba přecházet na „tónování“ s lehkými váhami a spoustou opakování. Drž se těžkých základních cviků a zhruba stejné zátěže jako před dietou.</p>
    <ul>
      <li><strong>Drž intenzitu.</strong> Váhy a blízkost k limitu série jsou důležitější než celkový počet sérií.</li>
      <li><strong>Sniž objem, pokud trpí regenerace.</strong> Když regenerace nestíhá, uber raději pár sérií (například o třetinu) než váhu na tyči.</li>
      <li><strong>Cílem je udržet sílu.</strong> Pokud síla v hlavních cvicích drží nebo klesne jen mírně, sval nejspíš držíš.</li>
      <li><strong>Pokračuj v progresi.</strong> I pomalejší přidávání je úspěch, víc v článku <a href="/cs/blog/progresivni-pretizeni">Progresivní přetížení</a>.</li>
    </ul>
    <p>Sílu a objem nejlíp hlídáš v <a href="/cs/blog/treninkovy-denik">tréninkovém deníku</a>: rychle v něm uvidíš, kdy se výkon láme.</p>'''),
        ('kardio-kroky', 'Kardio a kroky: nástroje, ne trest', '''    <p>Kardio ani kroky nejsou trestem za snědené jídlo. Jsou to nástroje, kterými zvýšíš výdej bez dalšího řezání kalorií.</p>
    <ul>
      <li><strong>Kroky a běžný pohyb (NEAT)</strong> jsou často nejlevnější způsob, jak zvýšit výdej. Chůze skoro nezatěžuje regeneraci, takže se dobře kombinuje s těžkým tréninkem. Zkus přidat 2&nbsp;000 až 3&nbsp;000 kroků denně oproti dnešku.</li>
      <li><strong>Kardio</strong> stačí 2 až 3krát týdně v mírné intenzitě. Těžké intervaly také fungují, ale dávkuj je opatrně, protože se počítají do celkové únavy.</li>
    </ul>
    <p>Pokud se připravuješ na běh nebo Hyrox, kardio v plánu máš stejně. Jen počítej s tím, že deficit a velký objem běhání se často vzájemně kazí.</p>'''),
        ('spanok-stres', 'Spánek a stres', '''    <p>Dospělým se běžně doporučuje 7 až 9 hodin spánku. Při nedostatku spánku bývá větší hlad, chuť na sladké i horší výkon v tréninku a dieta se drží hůř. Stres a málo regenerace dělají podobný problém.</p>
    <p>Pokud hubneš, spánek je součást plánu, ne bonus. Zkus mít pravidelný čas spánku a nenech se nachytat večerním hladem z nedospání. Víc ke spánku a regeneraci najdeš v článku <a href="/cs/blog/regenerace-a-spanek">Regenerace a spánek</a>.</p>'''),
        ('sledovanie', 'Jak sledovat, jestli to funguje', '''    <p>Jedno číslo na váze je málo. Sleduj víc ukazatelů najednou:</p>
    <table>
      <thead><tr><th>Ukazatel</th><th>Jak</th><th>Co ti řekne</th></tr></thead>
      <tbody>
        <tr><td><strong>Hmotnost</strong></td><td>Vážit se ráno stejně, počítat týdenní průměr</td><td>Tempo úbytku, bez denních výkyvů</td></tr>
        <tr><td><strong>Obvod pasu</strong></td><td>Jednou týdně, na stejném místě</td><td>Úbytek tuku v oblasti břicha</td></tr>
        <tr><td><strong>Fotky</strong></td><td>Každé 2 až 4 týdny, stejné světlo a póza</td><td>Změny, které čísla neukážou</td></tr>
        <tr><td><strong>Odhad tuku</strong></td><td><a href="/cs/procento-telesneho-tuku">Kalkulačka US Navy</a></td><td>Trend v čase, ne přesné číslo</td></tr>
        <tr><td><strong>Síla</strong></td><td>Záznamy v tréninkovém deníku</td><td>Jestli držíš sval</td></tr>
      </tbody>
    </table>
    <p>Ideální obraz je klesající týdenní průměr a obvod pasu při stabilní síle. Varovné signály jsou:</p>
    <ul>
      <li>síla klesá ve více cvicích najednou,</li>
      <li>výrazná únava a zhoršený spánek,</li>
      <li>hlad, který nejde zvládnout, nebo pokles nálady.</li>
    </ul>
    <p>V takovém případě deficit zmírni. Pokud dietu držíš déle (zhruba 8 až 12 týdnů) nebo se výkon dlouhodobě zhoršuje, pomůže <strong>diet break</strong>: 1 až 2 týdny na úrovni udržování (TDEE). Sílu, rekordy a makra můžeš sledovat i v appce <a href="https://app.booom.fit">BOOOM</a>.</p>'''),
        ('kedy-nie', 'Kdy není vhodný agresivní deficit', '''    <p>Nejsme lékaři a tenhle návod není pro každého. Před hubnutím se poraď s lékařem nebo nutričním terapeutem, pokud se tě týká něco z tohoto:</p>
    <ul>
      <li>věk do 18 let (tělo roste a potřebuje energii),</li>
      <li>těhotenství nebo kojení,</li>
      <li>porucha příjmu potravy v minulosti nebo v současnosti, případně úzkost z počítání kalorií a vážení,</li>
      <li>chronické onemocnění (například cukrovka, štítná žláza, srdce, ledviny) nebo pravidelné léky,</li>
      <li>už nízká tělesná hmotnost.</li>
    </ul>
    <p>V těchto případech deficit nastavuje odborník, ne kalkulačka.</p>'''),
    ],
)
