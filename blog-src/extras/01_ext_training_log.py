# Extension of the article 'training log' (base key = Slovak slug). Adds 4 sections and 2 FAQ items per language.
KEY = 'treningovy-dennik'

EXTEND = {
    'sk': {
        'sections': [
            ('ako', ('sablona', 'Šablóna: ako vyzerá jeden záznam', '''    <p>Zober si tieto dva vzory a skopíruj ich do zošita alebo tabuľky. Čísla sú len ilustračné, nie odporúčanie, koľko máš zdvíhať alebo behať. Nad každý záznam napíš dátum a jednu vetu o tom, ako sa cítiš (energia 1 až 5).</p>
    <p><strong>Silový tréning</strong></p>
    <table>
      <thead><tr><th>Cvik</th><th>Váha</th><th>Opakovania</th><th>RPE</th><th>Poznámka</th></tr></thead>
      <tbody>
        <tr><td>Drep vzad</td><td>80 kg</td><td>5 / 5 / 5</td><td>7 / 8 / 8</td><td>Hĺbka ako minule</td></tr>
        <tr><td>Tlak na lavičke</td><td>60 kg</td><td>8 / 8 / 7</td><td>8 / 8 / 9</td><td>Posledné opakovanie pomalé</td></tr>
        <tr><td>Veslovanie s činkou</td><td>50 kg</td><td>10 / 10 / 9</td><td>8 / 8 / 9</td><td>Bez švihu z driekov</td></tr>
      </tbody>
    </table>
    <p><strong>Hyrox tréning (prvé štyri kolá)</strong></p>
    <table>
      <thead><tr><th>Kolo</th><th>Beh 1 km</th><th>Stanica</th><th>Čas stanice</th></tr></thead>
      <tbody>
        <tr><td>1</td><td class="n">5:05</td><td>SkiErg</td><td class="n">4:10</td></tr>
        <tr><td>2</td><td class="n">5:15</td><td>Sled Push</td><td class="n">2:20</td></tr>
        <tr><td>3</td><td class="n">5:25</td><td>Sled Pull</td><td class="n">3:00</td></tr>
        <tr><td>4</td><td class="n">5:35</td><td>Burpee Broad Jumps</td><td class="n">4:30</td></tr>
      </tbody>
    </table>
    <p>Pod tabuľku patrí celkový čas, RPE celého tréningu a jedna poznámka, napríklad „nohy ťažké po saních“. Váhy na staniciach závisia od kategórie a sezóny, over si ich v oficiálnych pravidlách pre svoju kategóriu.</p>''')),
            ('progres', ('stagnacia', 'Stagnácia: kedy je čas zmeniť plán', '''    <p>Jeden slabší tréning nič neznamená, spôsobí ho spánok, stres aj počasie. O stagnácii má zmysel uvažovať, keď sa v hlavných cvikoch 3 až 4 tréningy po sebe nezlepší ani váha, ani opakovania pri podobnom RPE. Pozeraj sa na štvortýždňový priemer, nie na jeden deň.</p>
    <p>Skôr než zmeníš program, skontroluj základy:</p>
    <ul>
      <li><strong>Spánok a regenerácia.</strong> Dospelým sa bežne odporúča 7 až 9 hodín (viac v článku <a href="/blog/regeneracia-a-spanok">Regenerácia a spánok</a>).</li>
      <li><strong>Jedlo.</strong> V kalórickom deficite je stagnácia sily pomerne bežná. Skontroluj príjem v <a href="/kalorie-kalkulacka">kalorickej kalkulačke</a> a bielkoviny podľa článku <a href="/blog/kolko-bielkovin-denne">Koľko bielkovín denne</a>.</li>
      <li><strong>Poctivosť záznamu.</strong> Rovnaký rozsah pohybu, rovnaké pauzy, rovnaké RPE.</li>
    </ul>
    <p>Ak základy sedia, mení sa jedna vec naraz: pridaj sériu, zmeň rozsah opakovaní alebo vymeň variáciu cviku. Viac o postupnom zvyšovaní záťaže nájdeš v článku <a href="/blog/progresivne-pretazenie">Progresívne preťaženie</a>.</p>
    <p><strong>Odľahčenie (deload)</strong> sa bežne zaraďuje raz za 4 až 8 týždňov alebo keď výkon klesá dva týždne po sebe a cítiš sa unavene. Jeden týždeň zníž počet sérií zhruba na polovicu a váhy nechaj mierne, potom pokračuj v pláne.</p>''')),
            ('stagnacia', ('poznamky', 'Poznámky: bolesť, únava a spánok', '''    <p>Čísla ukážu, čo sa stalo. Poznámky vysvetlia prečo. Stačí pár slov, ak sa dá, vždy rovnakým spôsobom:</p>
    <table>
      <thead><tr><th>Téma</th><th>Čo si zapísať</th></tr></thead>
      <tbody>
        <tr><td><strong>Bolesť</strong></td><td>Kde, kedy (pri cviku, po ňom, ráno), miera 0 až 10, tupá alebo ostrá</td></tr>
        <tr><td><strong>Únava</strong></td><td>Energia 1 až 5, ťažké nohy, mimoriadne slabý začiatok tréningu</td></tr>
        <tr><td><strong>Spánok</strong></td><td>Počet hodín a či bol prerušovaný</td></tr>
        <tr><td><strong>Okolnosti</strong></td><td>Stres, choroba, vynechané jedlo, veľa kávy, cestovanie</td></tr>
      </tbody>
    </table>
    <p>Po mesiaci uvidíš vzorce: slabšie tréningy po dvoch krátkych nociach, plece, ktoré protestuje pri jednom konkrétnom cviku, únava v týždni pred menštruáciou alebo pred termínom v práci. Takéto zistenia sa dajú využiť pri plánovaní.</p>
    <p class="note">Denník nie je diagnostický nástroj a tento článok nie je lekárska rada. Ak bolesť pretrváva, je ostrá alebo sa objaví necitlivosť či opuch, nestačí ju zapísať: nechaj sa vyšetriť lekárom alebo fyzioterapeutom.</p>''')),
            ('poznamky', ('behanie', 'Beh, Hyrox a CrossFit v denníku', '''    <p>Pri vytrvalostných tréningoch nie sú váha a opakovania, ale čas, vzdialenosť a intenzita. Zapisuj:</p>
    <ul>
      <li><strong>Beh:</strong> typ (ľahký, tempový, intervaly), vzdialenosť, čas, priemerné tempo, RPE. Pri intervaloch zapíš každý úsek zvlášť, nielen priemer.</li>
      <li><strong>Hyrox:</strong> čas každého 1 km behu a každej stanice, celkový čas a poznámku o behu po ťažkých staniciach. Splity porovnaj s plánom z <a href="/hyrox-pacing">Hyrox pacing kalkulačky</a>. Ako trénovať do závodu, nájdeš v <a href="/blog/hyrox-priprava-8-tyzdnov">8-týždňovom pláne</a> a v článku <a href="/blog/hyrox-stanice-technika">Hyrox stanice: technika</a>.</li>
      <li><strong>CrossFit:</strong> názov tréningu (WOD), formát (AMRAP, na čas, EMOM), výsledok a či išlo o predpísanú, alebo upravenú verziu. Viac pre začiatočníkov je na stránke <a href="/crossfit-pre-zaciatocnikov">CrossFit pre začiatočníkov</a> (slovensky).</li>
    </ul>'''))
        ],
        'faq': [
            ('Ako poznám, že naozaj stagnujem, a nie je to len slabší týždeň?', 'Jeden slabší tréning nič neznamená. O stagnácii sa dá uvažovať, keď sa v hlavných cvikoch 3 až 4 tréningy po sebe nezlepší ani váha, ani opakovania pri podobnom RPE. Najprv skontroluj spánok, jedlo a presnosť zápisu, až potom meň plán.'),
            ('Ako zapisovať RPE, keď neviem presne odhadnúť, koľko opakovaní zostalo?', 'Pýtaj sa, koľko opakovaní by ti ešte zostalo v zálohe. Žiadne = RPE 10, jedno = 9, dve = 8, tri = 7. Prvé týždne odhaduj aj s chybou, časom sa odhad spresní a čísla budú porovnateľné.'),
        ],
    },
    'en': {
        'sections': [
            ('ako', ('sablona', 'A template: what one entry looks like', '''    <p>Copy these examples into a notebook or spreadsheet. The numbers are only illustrations, not a recommendation. Above each entry write the date and one line on how you feel (energy 1 to 5).</p>
    <p><strong>Strength session</strong></p>
    <table>
      <thead><tr><th>Exercise</th><th>Weight</th><th>Reps</th><th>RPE</th><th>Note</th></tr></thead>
      <tbody>
        <tr><td>Back squat</td><td>80 kg</td><td>5 / 5 / 5</td><td>7 / 8 / 8</td><td>Same depth as last time</td></tr>
        <tr><td>Bench press</td><td>60 kg</td><td>8 / 8 / 7</td><td>8 / 8 / 9</td><td>Last rep slow</td></tr>
        <tr><td>Barbell row</td><td>50 kg</td><td>10 / 10 / 9</td><td>8 / 8 / 9</td><td>No swing from the lower back</td></tr>
      </tbody>
    </table>
    <p><strong>Hyrox session (first four rounds)</strong></p>
    <table>
      <thead><tr><th>Round</th><th>1 km run</th><th>Station</th><th>Station time</th></tr></thead>
      <tbody>
        <tr><td>1</td><td class="n">5:05</td><td>SkiErg</td><td class="n">4:10</td></tr>
        <tr><td>2</td><td class="n">5:15</td><td>Sled Push</td><td class="n">2:20</td></tr>
        <tr><td>3</td><td class="n">5:25</td><td>Sled Pull</td><td class="n">3:00</td></tr>
        <tr><td>4</td><td class="n">5:35</td><td>Burpee Broad Jumps</td><td class="n">4:30</td></tr>
      </tbody>
    </table>
    <p>Under the table goes the total time, the RPE of the whole session and one note, for example “legs heavy after the sled”. Station weights depend on your category and the season, so check the official rules for your category.</p>''')),
            ('progres', ('stagnacia', 'Plateaus: when to change the plan', '''    <p>One weak session means nothing: sleep, stress and weather all play a part. It is worth considering a plateau when neither the weight nor the reps on your main lifts improve for 3 to 4 sessions in a row at a similar RPE. Look at a four-week average, not one day.</p>
    <p>Before you change the programme, check the basics:</p>
    <ul>
      <li><strong>Sleep and recovery.</strong> Adults are commonly advised to get 7 to 9 hours (more in <a href="/en/blog/recovery-and-sleep">Recovery and sleep</a>).</li>
      <li><strong>Food.</strong> Strength often stalls in a calorie deficit. Check your intake in the <a href="/en/calorie-calculator">calorie calculator</a> and your protein with <a href="/en/blog/how-much-protein-per-day">How much protein per day</a>.</li>
      <li><strong>Honest logging.</strong> The same range of motion, the same rest times, the same RPE.</li>
    </ul>
    <p>If the basics are in place, change one thing at a time: add a set, shift the rep range or swap an exercise variation. There is more on gradually raising the load in <a href="/en/blog/progressive-overload">Progressive overload</a>.</p>
    <p>A <strong>deload</strong> is commonly scheduled every 4 to 8 weeks, or when performance drops for two weeks in a row and you feel worn out. For one week, cut the number of sets to roughly half, keep the weights moderate, then return to the plan.</p>''')),
            ('stagnacia', ('poznamky', 'Notes: pain, fatigue and sleep', '''    <p>The numbers show what happened. Notes explain why. A few words are enough, written the same way each time:</p>
    <table>
      <thead><tr><th>Topic</th><th>What to write down</th></tr></thead>
      <tbody>
        <tr><td><strong>Pain</strong></td><td>Where, when (during the lift, after it, next morning), level 0 to 10, dull or sharp</td></tr>
        <tr><td><strong>Fatigue</strong></td><td>Energy 1 to 5, heavy legs, unusually weak start to the session</td></tr>
        <tr><td><strong>Sleep</strong></td><td>Hours slept and whether it was broken</td></tr>
        <tr><td><strong>Circumstances</strong></td><td>Stress, illness, a skipped meal, lots of coffee, travel</td></tr>
      </tbody>
    </table>
    <p>After a month you will see patterns: weaker sessions after two short nights, a shoulder that complains on one specific exercise, tiredness in the week before a work deadline.</p>
    <p class="note">A log is not a diagnostic tool and this article is not medical advice. If pain persists, is sharp, or comes with numbness or swelling, do not just log it: get it checked by a doctor or physiotherapist.</p>''')),
            ('poznamky', ('behanie', 'Running, Hyrox and CrossFit in your log', '''    <p>For endurance sessions the key numbers are not weight and reps but time, distance and intensity. Write down:</p>
    <ul>
      <li><strong>Running:</strong> type (easy, tempo, intervals), distance, time, average pace, RPE. For intervals log each rep separately, not just the average.</li>
      <li><strong>Hyrox:</strong> the time of every 1 km run and every station, the total time and a note on how the running felt after heavy stations. Compare your splits with the plan from the <a href="/en/hyrox-pacing-calculator">Hyrox pacing calculator</a>. For race preparation see the <a href="/en/blog/hyrox-8-week-training-plan">8-week plan</a> and <a href="/en/blog/hyrox-stations-technique">Hyrox stations: technique</a>.</li>
      <li><strong>CrossFit:</strong> the workout name (WOD), format (AMRAP, for time, EMOM), the result and whether you did the prescribed or a scaled version. Beginners can start with <a href="/crossfit-pre-zaciatocnikov">CrossFit for beginners</a> (Slovak).</li>
    </ul>'''))
        ],
        'faq': [
            ('How do I know I am really plateauing and not just having a bad week?', 'One weak session means nothing. You can start thinking about a plateau when neither the weight nor the reps on your main lifts improve for 3 to 4 sessions in a row at a similar RPE. Check sleep, food and the accuracy of your log first, and only then change the plan.'),
            ('How do I log RPE if I am not sure?', 'Ask how many reps you would have had left in reserve. None = RPE 10, one = 9, two = 8, three = 7. Your guesses will be rough at first, but they improve with practice.'),
        ],
    },
    'cs': {
        'sections': [
            ('ako', ('sablona', 'Šablona: jak vypadá jeden záznam', '''    <p>Vezmi si tyto dva vzory a zkopíruj je do sešitu nebo tabulky. Čísla jsou jen ilustrační, ne doporučení, kolik máš zvedat nebo běhat. Nad každý záznam napiš datum a jednu větu o tom, jak se cítíš (energie 1 až 5).</p>
    <p><strong>Silový trénink</strong></p>
    <table>
      <thead><tr><th>Cvik</th><th>Váha</th><th>Opakování</th><th>RPE</th><th>Poznámka</th></tr></thead>
      <tbody>
        <tr><td>Dřep vzadu</td><td>80 kg</td><td>5 / 5 / 5</td><td>7 / 8 / 8</td><td>Hloubka jako minule</td></tr>
        <tr><td>Bench press</td><td>60 kg</td><td>8 / 8 / 7</td><td>8 / 8 / 9</td><td>Poslední opakování pomalé</td></tr>
        <tr><td>Přítahy s činkou</td><td>50 kg</td><td>10 / 10 / 9</td><td>8 / 8 / 9</td><td>Bez švihu z beder</td></tr>
      </tbody>
    </table>
    <p><strong>Hyrox trénink (první čtyři kola)</strong></p>
    <table>
      <thead><tr><th>Kolo</th><th>Běh 1 km</th><th>Stanice</th><th>Čas stanice</th></tr></thead>
      <tbody>
        <tr><td>1</td><td class="n">5:05</td><td>SkiErg</td><td class="n">4:10</td></tr>
        <tr><td>2</td><td class="n">5:15</td><td>Sled Push</td><td class="n">2:20</td></tr>
        <tr><td>3</td><td class="n">5:25</td><td>Sled Pull</td><td class="n">3:00</td></tr>
        <tr><td>4</td><td class="n">5:35</td><td>Burpee Broad Jumps</td><td class="n">4:30</td></tr>
      </tbody>
    </table>
    <p>Pod tabulku patří celkový čas, RPE celého tréninku a jedna poznámka, například „nohy těžké po saních“. Váhy na stanicích závisejí na kategorii a sezóně, ověř si je v oficiálních pravidlech pro svou kategorii.</p>''')),
            ('progres', ('stagnacia', 'Stagnace: kdy je čas změnit plán', '''    <p>Jeden slabší trénink nic neznamená, způsobí ho spánek, stres i počasí. O stagnaci má smysl uvažovat, když se v hlavních cvicích 3 až 4 tréninky po sobě nezlepší ani váha, ani opakování při podobném RPE. Dívej se na čtyřtýdenní průměr, ne na jeden den.</p>
    <p>Než změníš program, zkontroluj základy:</p>
    <ul>
      <li><strong>Spánek a regenerace.</strong> Dospělým se běžně doporučuje 7 až 9 hodin (víc v článku <a href="/cs/blog/regenerace-a-spanek">Regenerace a spánek</a>).</li>
      <li><strong>Jídlo.</strong> V kalorickém deficitu je stagnace síly poměrně běžná. Zkontroluj příjem v <a href="/cs/kaloricka-kalkulacka">kalorické kalkulačce</a> a bílkoviny podle článku <a href="/cs/blog/kolik-bilkovin-denne">Kolik bílkovin denně</a>.</li>
      <li><strong>Poctivost záznamu.</strong> Stejný rozsah pohybu, stejné pauzy, stejné RPE.</li>
    </ul>
    <p>Pokud základy sedí, měň jednu věc najednou: přidej sérii, změň rozsah opakování nebo vyměň variantu cviku. Víc o postupném zvyšování zátěže najdeš v článku <a href="/cs/blog/progresivni-pretizeni">Progresivní přetížení</a>.</p>
    <p><strong>Odlehčení (deload)</strong> se běžně zařazuje jednou za 4 až 8 týdnů nebo když výkon klesá dva týdny po sobě a cítíš se unaveně. Jeden týden sniž počet sérií zhruba na polovinu, váhy nech mírné a pak pokračuj v plánu.</p>''')),
            ('stagnacia', ('poznamky', 'Poznámky: bolest, únava a spánek', '''    <p>Čísla ukážou, co se stalo. Poznámky vysvětlí proč. Stačí pár slov, pokud možno vždy stejným způsobem:</p>
    <table>
      <thead><tr><th>Téma</th><th>Co si zapsat</th></tr></thead>
      <tbody>
        <tr><td><strong>Bolest</strong></td><td>Kde, kdy (při cviku, po něm, ráno), míra 0 až 10, tupá nebo ostrá</td></tr>
        <tr><td><strong>Únava</strong></td><td>Energie 1 až 5, těžké nohy, mimořádně slabý začátek tréninku</td></tr>
        <tr><td><strong>Spánek</strong></td><td>Počet hodin a zda byl přerušovaný</td></tr>
        <tr><td><strong>Okolnosti</strong></td><td>Stres, nemoc, vynechané jídlo, hodně kávy, cestování</td></tr>
      </tbody>
    </table>
    <p>Po měsíci uvidíš vzorce: slabší tréninky po dvou krátkých nocích, rameno, které protestuje u jednoho konkrétního cviku, únava v týdnu před termínem v práci. Taková zjištění se dají využít při plánování.</p>
    <p class="note">Deník není diagnostický nástroj a tento článek není lékařská rada. Pokud bolest přetrvává, je ostrá nebo se objeví necitlivost či otok, nestačí ji zapsat: nech se vyšetřit lékařem nebo fyzioterapeutem.</p>''')),
            ('poznamky', ('behanie', 'Běh, Hyrox a CrossFit v deníku', '''    <p>U vytrvalostních tréninků nejsou důležité váha a opakování, ale čas, vzdálenost a intenzita. Zapisuj:</p>
    <ul>
      <li><strong>Běh:</strong> typ (lehký, tempový, intervaly), vzdálenost, čas, průměrné tempo, RPE. U intervalů zapiš každý úsek zvlášť, ne jen průměr.</li>
      <li><strong>Hyrox:</strong> čas každého běhu na 1 km a každé stanice, celkový čas a poznámku o běhu po těžkých stanicích. Splity porovnej s plánem z <a href="/cs/hyrox-pacing-kalkulacka">Hyrox pacing kalkulačky</a>. Jak trénovat na závod, najdeš v <a href="/cs/blog/hyrox-priprava-8-tydnu">8týdenním plánu</a> a v článku <a href="/cs/blog/hyrox-stanice-technika">Hyrox stanice: technika</a>.</li>
      <li><strong>CrossFit:</strong> název tréninku (WOD), formát (AMRAP, na čas, EMOM), výsledek a zda šlo o předepsanou, nebo upravenou verzi. Víc pro začátečníky je na stránce <a href="/crossfit-pre-zaciatocnikov">CrossFit pro začátečníky</a> (slovensky).</li>
    </ul>'''))
        ],
        'faq': [
            ('Jak poznám, že opravdu stagnuji, a není to jen slabší týden?', 'Jeden slabší trénink nic neznamená. O stagnaci se dá uvažovat, když se v hlavních cvicích 3 až 4 tréninky po sobě nezlepší ani váha, ani opakování při podobném RPE. Nejdřív zkontroluj spánek, jídlo a přesnost zápisu, teprve pak měň plán.'),
            ('Jak zapisovat RPE, když nedokážu přesně odhadnout, kolik opakování zbylo?', 'Ptej se, kolik opakování by ti ještě zbylo v záloze. Žádné = RPE 10, jedno = 9, dvě = 8, tři = 7. První týdny odhaduj i s chybou, časem se odhad zpřesní a čísla budou srovnatelná.'),
        ],
    },
}
