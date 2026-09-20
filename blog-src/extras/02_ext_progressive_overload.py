# Extension of the 'progressive overload' article (base key: progresivne-pretazenie).
# New section ids: zaciatocnik-vs-pokrocily, cyklus, domov, chyby.
KEY = 'progresivne-pretazenie'

EXTEND = {
    'sk': {
        'sections': [
            ('kolko', ('zaciatocnik-vs-pokrocily', 'Začiatočník, stredne pokročilý, pokročilý: ako sa progres mení', '''    <p>Tempo progresu sa s tréningovým vekom výrazne mení. Začiatočník môže pridávať skoro každý tréning, pokročilý bojuje o jedno opakovanie za mesiac.</p>
    <table>
      <thead><tr><th>Úroveň</th><th>Ako často pridávaš</th><th>Typický skok</th><th>Čo čakať</th></tr></thead>
      <tbody>
        <tr><td><strong>Začiatočník</strong> (zhruba prvý rok pravidelného tréningu)</td><td>Každý tréning až týždeň</td><td>Nohy 2,5 až 5 kg, horné telo 1,25 až 2,5 kg</td><td>Rýchle a pomerne rovnomerné prírastky, technika sa zlepšuje spolu so silou</td></tr>
        <tr><td><strong>Stredne pokročilý</strong> (zhruba 1 až 3 roky)</td><td>Raz za 2 až 4 týždne</td><td>1,25 až 2,5 kg alebo 1 až 2 opakovania</td><td>Progres po vlnách, občas aj týždeň bez zlepšenia</td></tr>
        <tr><td><strong>Pokročilý</strong> (niekoľko rokov)</td><td>Raz za 1 až 3 mesiace</td><td>1,25 kg alebo jedno opakovanie</td><td>Malé prírastky, plánované bloky a pravidelný deload</td></tr>
      </tbody>
    </table>
    <p class="note">Čísla sú len orientačné. Skutočné tempo ovplyvňuje spánok, jedlo, genetika aj to, ako dôsledne trénuješ.</p>
    <p>Úroveň nedefinuje kalendár, ale to, či ti ešte funguje jednoduché pridávanie váhy. Ak sa ti to pri čistej technike dvakrát po sebe zasekne, prejdi na dvojitú progresiu.</p>''')),
            ('deload', ('cyklus', 'Ukážka 8-týždňového cyklu s deloadom', '''    <p>Ako to vyzerá v praxi? Príklad pre tlak na lavičke: jeden ťažký tréning týždenne, rozsah 6 až 8 opakovaní, dvojitá progresia a v siedmom týždni deload. Váhy sú len ukážka, prispôsob ich sebe. Štartovaciu váhu ti pomôže orientačne odhadnúť <a href="/1rm-kalkulacka">1RM kalkulačka</a>.</p>
    <table>
      <thead><tr><th class="n">Týždeň</th><th class="n">Váha</th><th>Série x opakovania</th><th class="n">RPE</th><th>Poznámka</th></tr></thead>
      <tbody>
        <tr><td class="n">1</td><td class="n">60 kg</td><td>3 x 6</td><td class="n">7</td><td>Štart s rezervou</td></tr>
        <tr><td class="n">2</td><td class="n">60 kg</td><td>3 x 7</td><td class="n">7 až 8</td><td>Pridávaš opakovania</td></tr>
        <tr><td class="n">3</td><td class="n">60 kg</td><td>3 x 8</td><td class="n">8</td><td>Horná hranica rozsahu</td></tr>
        <tr><td class="n">4</td><td class="n">62,5 kg</td><td>3 x 6</td><td class="n">8</td><td>Nová váha, späť na 6</td></tr>
        <tr><td class="n">5</td><td class="n">62,5 kg</td><td>3 x 7</td><td class="n">8 až 9</td><td>Opakovania hore</td></tr>
        <tr><td class="n">6</td><td class="n">62,5 kg</td><td>3 x 8</td><td class="n">9</td><td>Najťažší týždeň cyklu</td></tr>
        <tr><td class="n">7</td><td class="n">45 kg</td><td>2 x 6</td><td class="n">5 až 6</td><td>Deload: menej sérií aj váhy</td></tr>
        <tr><td class="n">8</td><td class="n">65 kg</td><td>3 x 6</td><td class="n">8</td><td>Čerstvý, nový rekord</td></tr>
      </tbody>
    </table>
    <p>Ak v 4. týždni nezvládneš 6 opakovaní s 62,5 kg, zostaň ešte týždeň na 60 kg. Pridať za každú cenu nemá zmysel.</p>''')),
            ('stagnacia', ('domov', 'Progresia bez činky: doma a bez vybavenia', '''    <p>Progresívne preťaženie nie je viazané na tyč. Aj doma máš viac možností, než čakáš:</p>
    <ul>
      <li><strong>Ťažší variant cviku:</strong> kliky zo sklonu (ruky na stoličke), potom klasické, potom s nohami na vyvýšenej podložke.</li>
      <li><strong>Tempo:</strong> 3 sekundy dole, krátka pauza a potom nahor.</li>
      <li><strong>Jednostranné varianty:</strong> výpady, bulharský drep, jednonohý rumunský mŕtvy ťah. Keď zaťažíš len jednu nohu, vlastná váha stačí na poriadnu záťaž.</li>
      <li><strong>Odporové gumy:</strong> prejdi na hrubšiu gumu, použi dve naraz alebo stoj ďalej od úchytu, aby bolo väčšie napätie.</li>
      <li><strong>Batoh:</strong> naplň ho knihami alebo fľašami s vodou (1 l vody je približne 1 kg) a pridávaj po 1 až 2 kg.</li>
    </ul>
    <p>Pri ľahších záťažiach choď bližšie k zlyhaniu: sériu ukonči s rezervou 1 až 3 opakovania, aj keď ich je 15 až 30. Výskum naznačuje, že sval môže rásť podobne v širokom rozsahu opakovaní, ak sú série dostatočne náročné. Pri bolestiach kĺbov sa poraď s fyzioterapeutom.</p>''')),
            ('domov', ('chyby', 'Najčastejšie chyby pri pridávaní záťaže', '''    <ul>
      <li><strong>Ego lifting.</strong> Váha, pri ktorej sa rozpadá technika, ti nič nedá. Rátajú sa len čisté opakovania v plnom rozsahu.</li>
      <li><strong>Naháňanie progresu na každom tréningu.</strong> Sleduj trend za 4 až 6 týždňov, nie jednu slabšiu sériu. Objem si rozumne rozlož v týždni (<a href="/blog/treningovy-split">tréningový split</a>).</li>
      <li><strong>Ignorovanie techniky.</strong> Pridávaš váhu a skracuješ rozsah, takže cvik sa vlastne uľahčuje.</li>
      <li><strong>Žiadny záznam.</strong> Bez zapísaných váh a opakovaní nevieš, čo znamená „viac“. Základy nájdeš v článku <a href="/blog/treningovy-dennik">Tréningový denník</a>.</li>
      <li><strong>Zanedbaná regenerácia.</strong> Spánok a pauzy medzi tréningami rozoberá <a href="/blog/regeneracia-a-spanok">regenerácia a spánok</a>.</li>
    </ul>''')),
        ],
        'faq': [
            ('Dá sa uplatniť progresívne preťaženie aj bez posilňovne?', 'Áno. Zvyšuj náročnosť ťažším variantom cviku (napríklad kliky s nohami na vyvýšenej podložke), pomalším tempom, jednostrannými cvikmi, hrubšou odporovou gumou alebo batohom s pridávanou záťažou. Série drž blízko zlyhaniu, teda s rezervou 1 až 3 opakovania.'),
            ('Ako spoznám progres, keď sa váha na tyči nemení?', 'Sleduj opakovania, RPE pri rovnakej váhe, rozsah pohybu a kvalitu techniky. Ak robíš rovnakú váhu s viac opakovaniami alebo väčšou rezervou, zlepšuješ sa. Posudzuj trend za 4 až 6 týždňov, nie jeden tréning.'),
        ],
    },
    'en': {
        'sections': [
            ('kolko', ('zaciatocnik-vs-pokrocily', 'Beginner, intermediate, advanced: how progress changes', '''    <p>Progress slows down with training age. A beginner can add weight almost every workout, an advanced lifter fights for one extra rep a month.</p>
    <table>
      <thead><tr><th>Level</th><th>How often you add</th><th>Typical jump</th><th>What to expect</th></tr></thead>
      <tbody>
        <tr><td><strong>Beginner</strong> (roughly the first year of regular training)</td><td>Every workout to every week</td><td>Legs 2.5 to 5 kg, upper body 1.25 to 2.5 kg</td><td>Fast, fairly steady gains</td></tr>
        <tr><td><strong>Intermediate</strong> (roughly 1 to 3 years)</td><td>Once every 2 to 4 weeks</td><td>1.25 to 2.5 kg or 1 to 2 reps</td><td>Progress in waves, some flat weeks</td></tr>
        <tr><td><strong>Advanced</strong> (several years)</td><td>Once every 1 to 3 months</td><td>1.25 kg or one rep</td><td>Small gains, planned blocks and regular deloads</td></tr>
      </tbody>
    </table>
    <p class="note">Numbers are approximate. The real pace depends on sleep, food, genetics and how consistently you train.</p>
    <p>Your level is defined not by the calendar but by whether simple weight adding still works. If it stalls twice in a row with clean technique, switch to double progression.</p>''')),
            ('deload', ('cyklus', 'An example 8-week cycle with a deload', '''    <p>An example for the bench press: one heavy session per week, a 6 to 8 rep range, double progression and a deload in week seven. Adapt the weights to yourself. The <a href="/en/1rm-calculator">1RM calculator</a> can help you roughly estimate a starting weight.</p>
    <table>
      <thead><tr><th class="n">Week</th><th class="n">Weight</th><th>Sets x reps</th><th class="n">RPE</th><th>Note</th></tr></thead>
      <tbody>
        <tr><td class="n">1</td><td class="n">60 kg</td><td>3 x 6</td><td class="n">7</td><td>Start with some reserve</td></tr>
        <tr><td class="n">2</td><td class="n">60 kg</td><td>3 x 7</td><td class="n">7 to 8</td><td>You add reps</td></tr>
        <tr><td class="n">3</td><td class="n">60 kg</td><td>3 x 8</td><td class="n">8</td><td>Top of the range</td></tr>
        <tr><td class="n">4</td><td class="n">62.5 kg</td><td>3 x 6</td><td class="n">8</td><td>New weight, back to 6</td></tr>
        <tr><td class="n">5</td><td class="n">62.5 kg</td><td>3 x 7</td><td class="n">8 to 9</td><td>Reps go up</td></tr>
        <tr><td class="n">6</td><td class="n">62.5 kg</td><td>3 x 8</td><td class="n">9</td><td>The hardest week of the cycle</td></tr>
        <tr><td class="n">7</td><td class="n">45 kg</td><td>2 x 6</td><td class="n">5 to 6</td><td>Deload: fewer sets and less weight</td></tr>
        <tr><td class="n">8</td><td class="n">65 kg</td><td>3 x 6</td><td class="n">8</td><td>Fresh, a new record</td></tr>
      </tbody>
    </table>
    <p>If you can’t manage 6 reps with 62.5 kg in week 4, stay on 60 kg for another week.</p>''')),
            ('stagnacia', ('domov', 'Progression without a barbell: at home with no equipment', '''    <p>Progressive overload is not tied to a barbell. At home you have more options than you think:</p>
    <ul>
      <li><strong>A harder variation:</strong> incline push-ups (hands on a chair), then standard ones, then with your feet on a raised surface.</li>
      <li><strong>Tempo:</strong> 3 seconds down, a short pause, then up.</li>
      <li><strong>Single-sided variations:</strong> lunges, Bulgarian split squats, single-leg Romanian deadlifts. When you load just one leg, your own body weight is enough for a serious challenge.</li>
      <li><strong>Resistance bands:</strong> move to a thicker band, use two at once or stand farther from the anchor for more tension.</li>
      <li><strong>A backpack:</strong> fill it with books or water bottles (1 litre of water is roughly 1 kg) and add 1 to 2 kg at a time.</li>
    </ul>
    <p>With lighter loads, go closer to failure: finish a set with 1 to 3 reps in reserve, even if that means 15 to 30 reps. Research suggests muscle can grow similarly across a wide range of reps as long as sets are demanding. If you have joint pain, talk to a physiotherapist.</p>''')),
            ('domov', ('chyby', 'Common mistakes when adding load', '''    <ul>
      <li><strong>Ego lifting.</strong> A weight that wrecks your technique gives you nothing. Only clean, full-range reps count.</li>
      <li><strong>Chasing progress every workout.</strong> Watch the trend over 4 to 6 weeks, not one weak set. Spread your volume sensibly across the week (<a href="/en/blog/training-split-guide">training split guide</a>).</li>
      <li><strong>Ignoring technique.</strong> Adding weight while shortening the range actually makes the lift easier.</li>
      <li><strong>No log.</strong> Without written weights and reps, “more” means nothing. The basics are in the article <a href="/en/blog/training-log">Training log</a>.</li>
      <li><strong>Neglected recovery.</strong> Sleep and rest days are covered in <a href="/en/blog/recovery-and-sleep">recovery and sleep</a>.</li>
    </ul>''')),
        ],
        'faq': [
            ('Can I use progressive overload without a gym?', 'Yes. Increase difficulty with a harder exercise variation (for example push-ups with your feet elevated), a slower tempo, single-sided exercises, a thicker resistance band or a backpack with added weight. Keep sets close to failure (1 to 3 reps in reserve).'),
            ('How do I recognise progress when the weight on the bar doesn’t change?', 'Track your reps, RPE at the same weight, range of motion and quality of technique. If you lift the same weight for more reps or with more in reserve, you are improving. Judge the trend over 4 to 6 weeks, not a single workout.'),
        ],
    },
    'cs': {
        'sections': [
            ('kolko', ('zaciatocnik-vs-pokrocily', 'Začátečník, středně pokročilý, pokročilý: jak se progres mění', '''    <p>Tempo progresu se s tréninkovým věkem výrazně mění. Začátečník může přidávat skoro každý trénink, pokročilý bojuje o jedno opakování za měsíc.</p>
    <table>
      <thead><tr><th>Úroveň</th><th>Jak často přidáváš</th><th>Typický skok</th><th>Co čekat</th></tr></thead>
      <tbody>
        <tr><td><strong>Začátečník</strong> (zhruba první rok pravidelného tréninku)</td><td>Každý trénink až týden</td><td>Nohy 2,5 až 5 kg, horní tělo 1,25 až 2,5 kg</td><td>Rychlé a poměrně rovnoměrné přírůstky, technika se zlepšuje spolu se silou</td></tr>
        <tr><td><strong>Středně pokročilý</strong> (zhruba 1 až 3 roky)</td><td>Jednou za 2 až 4 týdny</td><td>1,25 až 2,5 kg nebo 1 až 2 opakování</td><td>Progres po vlnách, občas i týden bez zlepšení</td></tr>
        <tr><td><strong>Pokročilý</strong> (několik let)</td><td>Jednou za 1 až 3 měsíce</td><td>1,25 kg nebo jedno opakování</td><td>Malé přírůstky, plánované bloky a pravidelný deload</td></tr>
      </tbody>
    </table>
    <p class="note">Čísla jsou jen orientační. Skutečné tempo ovlivňuje spánek, jídlo, genetika i to, jak důsledně trénuješ.</p>
    <p>Úroveň nedefinuje kalendář, ale to, zda ti ještě funguje jednoduché přidávání váhy. Pokud se ti to při čisté technice dvakrát po sobě zasekne, přejdi na dvojitou progresi.</p>''')),
            ('deload', ('cyklus', 'Ukázka 8týdenního cyklu s deloadem', '''    <p>Jak to vypadá v praxi? Příklad pro bench press: jeden těžký trénink týdně, rozsah 6 až 8 opakování, dvojitá progrese a v sedmém týdnu deload. Váhy jsou jen ukázka, přizpůsob je sobě. Startovní váhu ti pomůže orientačně odhadnout <a href="/cs/1rm-kalkulacka">kalkulačka 1RM</a>.</p>
    <table>
      <thead><tr><th class="n">Týden</th><th class="n">Váha</th><th>Série x opakování</th><th class="n">RPE</th><th>Poznámka</th></tr></thead>
      <tbody>
        <tr><td class="n">1</td><td class="n">60 kg</td><td>3 x 6</td><td class="n">7</td><td>Start s rezervou</td></tr>
        <tr><td class="n">2</td><td class="n">60 kg</td><td>3 x 7</td><td class="n">7 až 8</td><td>Přidáváš opakování</td></tr>
        <tr><td class="n">3</td><td class="n">60 kg</td><td>3 x 8</td><td class="n">8</td><td>Horní hranice rozsahu</td></tr>
        <tr><td class="n">4</td><td class="n">62,5 kg</td><td>3 x 6</td><td class="n">8</td><td>Nová váha, zpět na 6</td></tr>
        <tr><td class="n">5</td><td class="n">62,5 kg</td><td>3 x 7</td><td class="n">8 až 9</td><td>Opakování nahoru</td></tr>
        <tr><td class="n">6</td><td class="n">62,5 kg</td><td>3 x 8</td><td class="n">9</td><td>Nejtěžší týden cyklu</td></tr>
        <tr><td class="n">7</td><td class="n">45 kg</td><td>2 x 6</td><td class="n">5 až 6</td><td>Deload: méně sérií i váhy</td></tr>
        <tr><td class="n">8</td><td class="n">65 kg</td><td>3 x 6</td><td class="n">8</td><td>Svěží, nový rekord</td></tr>
      </tbody>
    </table>
    <p>Pokud ve 4. týdnu nezvládneš 6 opakování s 62,5 kg, zůstaň ještě týden na 60 kg. Přidávat za každou cenu nemá smysl.</p>''')),
            ('stagnacia', ('domov', 'Progrese bez činky: doma a bez vybavení', '''    <p>Progresivní přetížení není vázané na tyč. I doma máš víc možností, než čekáš:</p>
    <ul>
      <li><strong>Těžší varianta cviku:</strong> kliky ze sklonu (ruce na židli), pak klasické, pak s nohama na vyvýšené podložce.</li>
      <li><strong>Tempo:</strong> 3 sekundy dolů, krátká pauza a pak nahoru.</li>
      <li><strong>Jednostranné varianty:</strong> výpady, bulharský dřep, jednonohý rumunský mrtvý tah. Když zatížíš jen jednu nohu, stačí vlastní váha na pořádnou zátěž.</li>
      <li><strong>Odporové gumy:</strong> přejdi na tvrdší gumu, použij dvě najednou nebo se postav dál od úchytu, aby bylo větší napětí.</li>
      <li><strong>Batoh:</strong> naplň ho knihami nebo lahvemi s vodou (1 l vody je přibližně 1 kg) a přidávej po 1 až 2 kg.</li>
    </ul>
    <p>U lehčích zátěží jdi blíž k selhání: sérii ukonči s rezervou 1 až 3 opakování, i když jich je 15 až 30. Výzkum naznačuje, že sval může růst podobně v širokém rozsahu opakování, pokud jsou série dostatečně náročné. Při bolestech kloubů se poraď s fyzioterapeutem.</p>''')),
            ('domov', ('chyby', 'Nejčastější chyby při přidávání zátěže', '''    <ul>
      <li><strong>Ego lifting.</strong> Váha, při které se rozpadá technika, ti nic nedá. Počítají se jen čistá opakování v plném rozsahu.</li>
      <li><strong>Honění progresu na každém tréninku.</strong> Sleduj trend za 4 až 6 týdnů, ne jednu slabší sérii. Objem si rozumně rozlož v týdnu (<a href="/cs/blog/treninkovy-split">tréninkový split</a>).</li>
      <li><strong>Ignorování techniky.</strong> Přidáváš váhu a zkracuješ rozsah, takže se cvik vlastně usnadňuje.</li>
      <li><strong>Žádný záznam.</strong> Bez zapsaných vah a opakování nevíš, co znamená „víc“. Základy najdeš v článku <a href="/cs/blog/treninkovy-denik">Tréninkový deník</a>.</li>
      <li><strong>Zanedbaná regenerace.</strong> Spánek a pauzy mezi tréninky rozebírá <a href="/cs/blog/regenerace-a-spanek">regenerace a spánek</a>.</li>
    </ul>''')),
        ],
        'faq': [
            ('Dá se progresivní přetížení uplatnit i bez posilovny?', 'Ano. Zvyšuj náročnost těžší variantou cviku (například kliky s nohama na vyvýšené podložce), pomalejším tempem, jednostrannými cviky, tvrdší odporovou gumou nebo batohem s přidávanou zátěží. Série drž blízko selhání, tedy s rezervou 1 až 3 opakování.'),
            ('Jak poznám progres, když se váha na tyči nemění?', 'Sleduj opakování, RPE při stejné váze, rozsah pohybu a kvalitu techniky. Pokud zvedáš stejnou váhu s více opakováními nebo větší rezervou, zlepšuješ se. Posuzuj trend za 4 až 6 týdnů, ne jeden trénink.'),
        ],
    },
}
