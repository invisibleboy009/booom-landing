# English blog content (translation of content_sk.py). The generator is blog-src/make_blog.py.
# Structure is shared with content_sk.py and content_cs.py: same article order and section ids.

LANG = 'en'
PREFIX = '/en'         # URL prefix of this language ('' for Slovak, '/en', '/cs')
UI = dict(
    html_lang='en', og_locale='en_GB', date_sk='September 20, 2026',
    blog='Blog', home='BOOOM', toc='Contents', toc_aria='Article contents', faq='FAQ',
    updated='Updated', read='min read', privacy='Privacy policy',
    try_free='Try it free', try_web='Try it free on the web',
    appstore='Download on the App Store', gplay='Get it on Google Play',
)
HUB = dict(
    title_tag='Blog — training, nutrition and Hyrox | BOOOM',
    og_title='BOOOM Blog — training, nutrition and Hyrox',
    h1='BOOOM Blog: training, nutrition and Hyrox',
    desc='BOOOM blog: practical articles on the training log, progressive overload, protein and Hyrox preparation. Free, no fluff.',
    kw='fitness blog, workout log, progressive overload, protein, hyrox training, BOOOM',
    lead='Practical, no-fluff articles that help you train smarter. For most of them you will also find a calculator or tool right on the website.',
    cta=('Train with BOOOM', 'Workout log, AI coach, Hyrox simulator and nutrition tracking in one app. Free for iOS, Android and the web.'),
)

DISC_HEALTH = '<p class="disc">This article is for information only and does not replace the advice of a doctor or a nutritionist. If you have health problems, talk to a professional.</p>'
DISC_TRAIN = '<p class="disc">This article is for information only and does not replace a personal trainer or a doctor. If you have health problems or an injury, talk to a professional before starting demanding training.</p>'

ARTICLES = []

# ═══════════════════════════════════════ 1. Training log ═══════════════════════════════════
ARTICLES.append(dict(
    slug='training-log',
    title='Training Log: How to Keep One and Why It Helps You Grow',
    title_tag='Training Log — How to Keep One and What to Write Down | BOOOM',
    h1='Training Log: How to Keep One and Why It Helps You Grow',
    crumb='Training log',
    desc='What to write in your training log, how to keep it step by step and how to read your progress from it. A practical guide for strength training, Hyrox and running.',
    card='What to write down, how to do it in practice and how to read from the numbers whether you are really progressing.',
    kw='workout log, how to keep a workout log, workout tracker, track progress, training plan, strength training',
    lead='Most people think they remember how much they lifted last week. Most people are wrong. A training log is the cheapest way to turn your workouts into a system that can keep growing.',
    cta=('Log your workouts without paper', 'BOOOM remembers your weights and reps, shows your personal records on its own and rewards you with XP. A training log that doesn’t get in your way.'),
    disc=DISC_TRAIN,
    faq=[
        ('How long does logging a workout take?', 'With a good tool, roughly a minute or two for the whole workout. If it takes you longer, simplify the format and only log what you actually use.'),
        ('Do I have to log easy workouts and cardio too?', 'Yes, at least the minimum: date, type of activity and duration or distance. Easy days are part of the picture of how much load you really handle.'),
        ('What if I skip a workout or a log entry?', 'Nothing happens. A log is not a perfection contest. Don’t try to make up for a missed day, just carry on with the plan. What matters is that your entries give you information, not guilt.'),
        ('Is it better to log on paper or in an app?', 'Both work. Paper is fast and nothing distracts you; an app can calculate records, volume and charts for you. The best log is the one you actually keep.'),
    ],
    sections=[
        ('preco', 'Why log your workouts', '''    <p>Without a log you train by feel. Feel is useful but unreliable: a good day distorts what you managed, and fatigue distorts it the other way. A log gives you data that doesn’t depend on your mood.</p>
    <ul>
      <li><strong>You know what to beat today.</strong> Strength growth is built on gradually adding load (more in the article <a href="/en/blog/progressive-overload">Progressive overload</a>). Without the numbers from your last workout, you don’t know what “more” means.</li>
      <li><strong>You see progress even when you can’t see it in the mirror.</strong> Muscles grow slowly, but weights and reps go up faster and that is motivating.</li>
      <li><strong>You find the cause when things stall.</strong> Stagnation, pain or fatigue leave a trace in the data: less sleep, more volume, skipped meals.</li>
      <li><strong>It keeps you on the habit.</strong> Self-monitoring is among the best-studied techniques for sticking to a new habit.</li>
    </ul>'''),
        ('co', 'What to write down: the minimum and the bonuses', '''    <table>
      <thead><tr><th>Category</th><th>What to log</th></tr></thead>
      <tbody>
        <tr><td><strong>Minimum (strength training)</strong></td><td>Date, exercise, weight, number of reps, number of sets</td></tr>
        <tr><td><strong>Very useful</strong></td><td>How hard the set was (RPE 1 to 10, or how many reps you had left in reserve), a short note on technique</td></tr>
        <tr><td><strong>Bonus</strong></td><td>Sleep, energy, body weight, measurements, photos</td></tr>
        <tr><td><strong>Running and Hyrox</strong></td><td>Distance, time, pace, heart rate, splits of individual runs and stations</td></tr>
      </tbody>
    </table>
    <p>Start with the minimum. You’ll stop keeping a log with ten columns within two weeks; a log with five will last for years.</p>'''),
        ('ako', 'How to keep a log in practice', '''    <ol>
      <li><strong>Pick one format and stick to it.</strong> A notebook, a spreadsheet or an app. Switching between them is the most common reason a log falls apart.</li>
      <li><strong>Look at your last entry before the workout</strong> and set a goal for today: one more rep or 2.5 kg more.</li>
      <li><strong>Log right after the set</strong>, not in the evening from memory. Memory rounds up.</li>
      <li><strong>Add a note when something happened</strong> — your shoulder hurt, you slept badly, you changed your technique.</li>
      <li><strong>Once a week, take five minutes</strong> and go through your entries: what is growing, what is stuck, what needs to change.</li>
    </ol>'''),
        ('progres', 'How to read progress from your log', '''    <p>Don’t track everything. Three things are enough:</p>
    <ul>
      <li><strong>Your best set in the main lifts.</strong> From it you can also estimate your 1RM in the <a href="/en/1rm-calculator">1RM calculator</a> and compare it over time.</li>
      <li><strong>Weekly volume</strong> (sets × reps × weight) for each muscle group. It rises gradually, with an occasional lighter week.</li>
      <li><strong>Training frequency.</strong> The number of completed workouts per week is a simple indicator of consistency.</li>
    </ul>
    <div class="ex">
      <p><strong>Example: bench press, 4 weeks, 3 sets</strong></p>
      <table>
        <thead><tr><th>Week</th><th>Weight</th><th>Reps per set</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>60 kg</td><td>8 / 8 / 7</td></tr>
          <tr><td>2</td><td>60 kg</td><td>9 / 8 / 8</td></tr>
          <tr><td>3</td><td>60 kg</td><td>10 / 9 / 8</td></tr>
          <tr><td>4</td><td>62.5 kg</td><td>8 / 8 / 7</td></tr>
        </tbody>
      </table>
      <p>For three weeks you add reps, in the fourth you add weight and start over. Without a log you wouldn’t remember any of this.</p>
    </div>'''),
        ('chyby', 'The most common mistakes', '''    <ul>
      <li><strong>A format that’s too complicated.</strong> If logging takes longer than your warm-up, you’ll quit.</li>
      <li><strong>You only log records.</strong> Without the average days you can’t see the trend.</li>
      <li><strong>You don’t use the log.</strong> An entry is pointless if you don’t open it before training.</li>
      <li><strong>You don’t note changed conditions.</strong> A different bench, different dumbbells, a different range of motion: without a note, those numbers can’t be compared.</li>
    </ul>'''),
        ('forma', 'Paper, spreadsheet or app?', '''    <table>
      <thead><tr><th>Format</th><th>Advantage</th><th>Disadvantage</th></tr></thead>
      <tbody>
        <tr><td>Notebook</td><td>Fast, nothing distracts you</td><td>No charts, hard to search</td></tr>
        <tr><td>Spreadsheet</td><td>Your own formulas, can be filtered</td><td>Awkward on a phone in the gym</td></tr>
        <tr><td>App</td><td>Pre-fills last weights, calculates records and volume on its own</td><td>You need to pick one that doesn’t get in your way</td></tr>
      </tbody>
    </table>
    <p>The BOOOM app is built on exactly this: you log an exercise, the app shows your last performance, evaluates personal records on its own and rewards you with XP and ranks. You can try it for free on the web too.</p>'''),
    ],
))

# ═══════════════════════════════════════ 2. Progressive overload ══════════════════════════════
ARTICLES.append(dict(
    slug='progressive-overload',
    title='Progressive Overload: How to Add Weight So You Keep Growing',
    title_tag='Progressive Overload — How to Add Weight and Reps | BOOOM',
    h1='Progressive Overload: How to Add Weight So You Keep Growing',
    crumb='Progressive overload',
    desc='What progressive overload is, five ways to apply it, simple double progression, RPE and what to do when you plateau. A practical guide for strength training.',
    card='How to add weight, reps and volume so you keep growing and don’t get beaten by a plateau.',
    kw='progressive overload, how to add weight, double progression, RPE, strength plateau, deload, strength training',
    lead='Your body only grows when you push it to. If you keep doing the same sets with the same weight, it stops adapting. Progressive overload is the principle behind every good training plan.',
    cta=('Let your progress count itself', 'For every exercise, BOOOM shows what you lifted last time and automatically records new PRs. You just add weight.'),
    disc=DISC_TRAIN,
    faq=[
        ('Do I have to add weight every workout?', 'No. Beginners can add every week or even every workout, advanced lifters often only once every few weeks. Direction matters, not speed.'),
        ('What if I can’t even add a rep?', 'An occasional weaker workout is normal. If it keeps happening for several weeks, check your sleep, calorie and protein intake (<a href="/en/blog/how-much-protein-per-day">how much protein per day</a>) and consider a lighter week.'),
        ('How often should I deload?', 'As a rule of thumb once every 4 to 8 weeks, or when you notice a longer decline in performance and fatigue. Cut volume and load by roughly a third to a half.'),
        ('Does progressive overload work when losing weight too?', 'Yes. In a deficit the goal is to maintain strength, which is a signal that you are not losing muscle. Adding load may be slower, and that is fine.'),
    ],
    sections=[
        ('co', 'What is progressive overload', '''    <p><strong>Progressive overload</strong> means gradually increasing the demand your training puts on your body. Muscles and the nervous system adapt to what you do. If the demand stays the same, adaptation stops, and progress stops with it.</p>
    <p>You don’t have to add weight to the bar. Overload can be increased in several ways, and it is often smarter to alternate them.</p>'''),
        ('sposoby', 'Five ways to increase the load', '''    <table>
      <thead><tr><th>Method</th><th>What it looks like</th></tr></thead>
      <tbody>
        <tr><td><strong>Weight</strong></td><td>You add 1.25 to 5 kg to the bar</td></tr>
        <tr><td><strong>Reps</strong></td><td>Instead of 8 you do 9 or 10 with the same weight</td></tr>
        <tr><td><strong>Sets</strong></td><td>You go from 3 sets to 4</td></tr>
        <tr><td><strong>Technique and range</strong></td><td>A deeper squat, a slower eccentric phase, a pause at the bottom</td></tr>
        <tr><td><strong>Density</strong></td><td>The same work in less time, shorter rests</td></tr>
      </tbody>
    </table>'''),
        ('dvojita', 'Double progression: the simplest method', '''    <p>Set a rep range, for example 8 to 12. Start with a weight you can lift for the bottom of the range in all sets. Keep the same weight and add reps until you hit the top of the range in all sets. Then add weight and go back to 8.</p>
    <div class="ex">
      <p><strong>Example: one-arm dumbbell row</strong></p>
      <table>
        <thead><tr><th>Week</th><th>Weight</th><th>Reps (3 sets)</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>24 kg</td><td>8 / 8 / 8</td></tr>
          <tr><td>2</td><td>24 kg</td><td>10 / 9 / 8</td></tr>
          <tr><td>3</td><td>24 kg</td><td>12 / 11 / 10</td></tr>
          <tr><td>4</td><td>24 kg</td><td>12 / 12 / 12</td></tr>
          <tr><td>5</td><td>26 kg</td><td>8 / 8 / 8 and repeat</td></tr>
        </tbody>
      </table>
    </div>'''),
        ('kolko', 'How much to add', '''    <ul>
      <li><strong>Upper body and isolation exercises:</strong> usually 1.25 to 2.5 kg.</li>
      <li><strong>Legs and deadlift:</strong> usually 2.5 to 5 kg.</li>
      <li><strong>Beginners</strong> progress faster, often every week. <strong>Advanced lifters</strong> only once every few weeks, sometimes just by a rep.</li>
    </ul>
    <p>If you don’t have small plates, buy magnetic weights of 0.5 to 1.25 kg. Small jumps beat stagnation.</p>'''),
        ('rpe', 'RPE and reps in reserve', '''    <p><strong>RPE</strong> (rate of perceived exertion) is a 1 to 10 scale of how hard a set was. RPE 10 means complete failure, RPE 8 means you had about two reps left in reserve. This figure is also called <strong>RIR</strong> (reps in reserve).</p>
    <p>Most working sets should end with 1 to 3 reps in reserve. That way you put enough pressure on the muscle without needlessly exhausting yourself. In your <a href="/en/blog/training-log">training log</a>, note the RPE at least for the last set of an exercise.</p>'''),
        ('deload', 'The lighter week (deload)', '''    <p>Fatigue builds up faster than you think. Once every 4 to 8 weeks, or when your performance drops over several workouts in a row, cut both volume and load by roughly a third to a half. After a week you come back fresh and often beat your previous records.</p>'''),
        ('stagnacia', 'What to do when you plateau', '''    <ol>
      <li><strong>Check your sleep.</strong> Regularly getting less than 7 hours shows up in both strength and recovery.</li>
      <li><strong>Check your intake.</strong> In a chronic deficit, strength stalls. Work out your needs in the <a href="/en/calorie-calculator">calorie calculator</a> and your protein using the article <a href="/en/blog/how-much-protein-per-day">How much protein per day</a>.</li>
      <li><strong>Change the stimulus.</strong> A different rep range, an exercise variation or tempo.</li>
      <li><strong>Check your technique.</strong> Film a set on video.</li>
      <li><strong>Take a deload.</strong></li>
    </ol>
    <p>You can roughly estimate your current strength in the <a href="/en/1rm-calculator">1RM calculator</a> and compare it after a few weeks.</p>'''),
    ],
))

# ═══════════════════════════════════════ 3. How much protein per day ═══════════════════════════════
ARTICLES.append(dict(
    slug='how-much-protein-per-day',
    title='How Much Protein Do You Need per Day (and How to Spread It Out)',
    title_tag='How Much Protein per Day — Calculation by Weight and Goal | BOOOM',
    h1='How Much Protein Do You Need per Day (and How to Spread It Out)',
    crumb='How much protein per day',
    desc='How much protein you need per day for muscle, weight loss and everyday life. A table by body weight, protein-rich foods, a sample day and the most common myths.',
    card='A table by body weight and goal, the protein content of common foods and a sample day.',
    kw='how much protein per day, protein per kg, protein intake, protein for weight loss, protein and muscle, protein powder',
    lead='The number you know from the gym is “2 grams per kilo”. It is a reasonable estimate, but not always and not for everyone. Here is why, when less is enough and how to spread your protein across the day.',
    cta=('Log food and macros the easy way', 'BOOOM has a barcode scanner, a food database and a daily protein goal based on your weight.'),
    disc=DISC_HEALTH,
    faq=[
        ('Do I have to drink a protein shake?', 'No. Protein powder is just a convenient source of protein. If you manage to get enough from food, you don’t need it.'),
        ('Can the body only use 30 grams of protein at once?', 'No, that is a simplification. The body can use more, it just takes longer to digest. Spreading it over 3 to 5 meals is practical, not mandatory.'),
        ('Is protein bad for the kidneys?', 'In healthy people, studies have not shown kidney damage at commonly higher intakes. If you have kidney disease, you need to discuss your protein intake with a doctor.'),
        ('Is protein from a plant-based diet enough?', 'Yes. Combine different sources (legumes, tofu, grains, nuts) and aim for the upper end of the range.'),
    ],
    sections=[
        ('odpoved', 'The short answer', '''    <p>For a healthy adult with a sedentary lifestyle, the reference intake is approximately <strong>0.8 g of protein per kg</strong> of body weight per day. If you <strong>strength train</strong>, want to build muscle or are losing weight, most recommendations fall in the range of <strong>1.6 to 2.2 g per kg</strong>.</p>
    <table>
      <thead><tr><th>Body weight</th><th class="n">1.6 g/kg</th><th class="n">2.0 g/kg</th><th class="n">2.2 g/kg</th></tr></thead>
      <tbody>
        <tr><td>60 kg</td><td class="n">96 g</td><td class="n">120 g</td><td class="n">132 g</td></tr>
        <tr><td>70 kg</td><td class="n">112 g</td><td class="n">140 g</td><td class="n">154 g</td></tr>
        <tr><td>80 kg</td><td class="n">128 g</td><td class="n">160 g</td><td class="n">176 g</td></tr>
        <tr><td>90 kg</td><td class="n">144 g</td><td class="n">180 g</td><td class="n">198 g</td></tr>
      </tbody>
    </table>'''),
        ('preco', 'Why this particular range', '''    <p>A 2018 meta-analysis (Morton et al., British Journal of Sports Medicine) pooled dozens of studies with strength training. Muscle gains improved with higher protein intake up to roughly <strong>1.6 g per kg</strong>, and higher values mostly brought no further benefit. The upper bound of the confidence interval was around <strong>2.2 g per kg</strong>, which is why this value is commonly given as a ceiling above which there is no point going.</p>
    <p>More doesn’t always mean more muscle. Above roughly 2.2 g per kg it is usually just extra calories.</p>'''),
        ('cielu', 'By goal', '''    <table>
      <thead><tr><th>Situation</th><th class="n">g per kg per day</th></tr></thead>
      <tbody>
        <tr><td>Healthy adult without regular training</td><td class="n">~0.8</td></tr>
        <tr><td>Recreationally active</td><td class="n">1.2 to 1.6</td></tr>
        <tr><td>Strength training and building muscle</td><td class="n">1.6 to 2.2</td></tr>
        <tr><td>Losing weight with strength training</td><td class="n">1.8 to 2.2</td></tr>
      </tbody>
    </table>
    <p>In a calorie deficit it pays to aim for the upper end: it helps preserve muscle mass and keeps you fuller. You can set your deficit in the <a href="/en/calorie-calculator">calorie calculator</a>.</p>'''),
        ('rozlozenie', 'How to spread it across the day', '''    <p>A practical goal is 3 to 5 meals with about <strong>0.3 to 0.4 g of protein per kg</strong> in each meal. For 80 kg that is roughly 25 to 35 g. The exact timing around your workout matters less than your total daily intake.</p>'''),
        ('potraviny', 'How much protein common foods have', '''    <table>
      <thead><tr><th>Food</th><th class="n">Protein (approx.)</th></tr></thead>
      <tbody>
        <tr><td>Cooked chicken breast, 100 g</td><td class="n">30 g</td></tr>
        <tr><td>Salmon, 100 g</td><td class="n">20 g</td></tr>
        <tr><td>Canned tuna, 100 g</td><td class="n">25 g</td></tr>
        <tr><td>Egg, 1 piece</td><td class="n">6 g</td></tr>
        <tr><td>Cottage cheese, 100 g</td><td class="n">12 g</td></tr>
        <tr><td>Greek yogurt, 150 g</td><td class="n">15 g</td></tr>
        <tr><td>Tofu, 100 g</td><td class="n">10 g</td></tr>
        <tr><td>Cooked lentils, 100 g</td><td class="n">9 g</td></tr>
        <tr><td>Whey protein, 1 scoop (30 g)</td><td class="n">24 g</td></tr>
      </tbody>
    </table>
    <p class="note">Values are approximate and vary by manufacturer and preparation method.</p>'''),
        ('den', 'Sample day for 80 kg (target around 160 g)', '''    <table>
      <thead><tr><th>Meal</th><th>What</th><th class="n">Protein</th></tr></thead>
      <tbody>
        <tr><td>Breakfast</td><td>3 eggs, Greek yogurt 150 g, rolled oats 50 g</td><td class="n">~40 g</td></tr>
        <tr><td>Lunch</td><td>Chicken breast 150 g with rice and vegetables</td><td class="n">~45 g</td></tr>
        <tr><td>Snack</td><td>Cottage cheese 200 g</td><td class="n">~24 g</td></tr>
        <tr><td>Dinner</td><td>Salmon 150 g with vegetables</td><td class="n">~30 g</td></tr>
        <tr><td>After training</td><td>Whey protein 1 scoop</td><td class="n">~24 g</td></tr>
        <tr><td><strong>Total</strong></td><td></td><td class="n">~163 g</td></tr>
      </tbody>
    </table>'''),
        ('mytus', 'Myths and safety', '''    <ul>
      <li><strong>“Protein ruins your kidneys.”</strong> In healthy people, studies have not confirmed this at commonly higher intakes. If you have kidney disease, talk to a doctor.</li>
      <li><strong>“You can’t build muscle without protein powder.”</strong> What matters is your total daily intake, not the form.</li>
      <li><strong>“The more, the better.”</strong> Once you go past the upper end of the range, you gain nothing more.</li>
    </ul>
    <p>Log your intake and watch the weekly average. In your <a href="/en/blog/training-log">training log</a> you can compare your intake with how your training is going, week by week.</p>'''),
    ],
))

# ═══════════════════════════════════════ 4. Hyrox training plan ══════════════════════════════════════
ARTICLES.append(dict(
    slug='hyrox-8-week-training-plan',
    title='8-Week Hyrox Training Plan: A Sample Plan for Beginners',
    title_tag='8-Week Hyrox Training Plan — for Beginners | BOOOM',
    h1='8-Week Hyrox Training Plan: A Sample Plan for Beginners',
    crumb='8-week Hyrox training plan',
    desc='An 8-week plan to prepare for your first Hyrox: weekly structure, runs, strength, station practice, simulation and taper. For those who can run 5 km.',
    card='Week by week: runs, strength training, hybrid workouts, simulation and taper before your first Hyrox.',
    kw='hyrox training plan, hyrox 8 week plan, hyrox for beginners, how to train for hyrox, hyrox workout, hyrox stations',
    lead='Eight weeks is enough to finish your first Hyrox with a smile, if you can already run and you’re not a total newcomer to the gym. Here is a plan that shows you what to do each week.',
    cta=('Log splits and track progress', 'BOOOM measures your splits in real time and shows a run-vs-station breakdown and a fatigue index. A training log for Hyrox.'),
    disc=DISC_TRAIN,
    faq=[
        ('Are 8 weeks enough for a first Hyrox?', 'If you can run 5 km in one go and train at least 3 times a week, yes, for finishing your first race. If not, extend the base phase.'),
        ('How much should I run per week?', 'In this plan roughly 15 to 25 km per week, most of it at an easy pace. Consistency matters more than kilometres.'),
        ('Can I prepare at home?', 'Partly: runs and strength training with dumbbells and bodyweight. Try the specific stations (SkiErg, sled, rowing) in a gym at least a few times before the race.'),
        ('How should I prepare for pacing?', 'Use the <a href="/en/hyrox-pacing-calculator">Hyrox pacing calculator</a>: enter your target time and you get run paces and station times. After the simulation, replace them with your actual splits.'),
    ],
    sections=[
        ('pre-koho', 'Who the plan is for', '''    <ul>
      <li>You can run <strong>5 km in one go</strong>, even slowly.</li>
      <li>You train <strong>3 to 4 times a week</strong> and know the basic exercises (squat, deadlift, lunges, presses).</li>
      <li>You have 8 weeks and your goal is to finish your first Hyrox, not to win your category.</li>
    </ul>
    <p>If you don’t meet these conditions, add a base phase at the start. If you have an injury or health limitations, talk to a doctor. The plan is a sample, so adapt it to your time and abilities.</p>'''),
        ('format', 'Hyrox in brief', '''    <p>Hyrox is <strong>8 rounds, each made up of 1 km of running and one functional station</strong>. The stations come in this order: SkiErg, Sled Push, Sled Pull, Burpee Broad Jumps, Rowing, Farmers Carry, Sandbag Lunges and Wall Balls. You can find more about the format in the article <a href="/hyrox-pre-zaciatocnikov">Hyrox for beginners</a> (Slovak). Weights depend on the category and season, so check them in the official rules.</p>'''),
        ('tyzden', 'Weekly structure', '''    <table>
      <thead><tr><th>Day</th><th>Workout</th></tr></thead>
      <tbody>
        <tr><td><strong>1</strong></td><td>Easy run at conversational pace</td></tr>
        <tr><td><strong>2</strong></td><td>Strength training: squat, deadlift, presses, pulls, lunges</td></tr>
        <tr><td><strong>3</strong></td><td>Intervals or tempo run</td></tr>
        <tr><td><strong>4</strong></td><td>Hybrid workout: running alternated with stations</td></tr>
        <tr><td>5 to 7</td><td>Rest, a walk, mobility</td></tr>
      </tbody>
    </table>'''),
        ('plan', 'Week-by-week plan', '''    <table>
      <thead><tr><th>Week</th><th>Easy run</th><th>Strength</th><th>Intervals / tempo</th><th>Hybrid</th></tr></thead>
      <tbody>
        <tr><td><strong>1</strong></td><td>30 min</td><td>Full body, 3 × 8–10</td><td>5 × 2 min hard / 2 min easy</td><td>4 × (400 m run + 15 wall balls)</td></tr>
        <tr><td><strong>2</strong></td><td>35 min</td><td>Same exercises, add weight</td><td>6 × 2 min</td><td>4 × (400 m + 20 wall balls)</td></tr>
        <tr><td><strong>3</strong></td><td>40 min</td><td>Strength + farmers carry 4 × 40 m</td><td>4 × 4 min tempo / 2 min easy</td><td>5 × (500 m + 250 m SkiErg)</td></tr>
        <tr><td><strong>4</strong> (deload)</td><td>30 min</td><td>2 × 8, lighter</td><td>4 × 2 min</td><td>3 × (500 m + station)</td></tr>
        <tr><td><strong>5</strong></td><td>45 min</td><td>Strength + sandbag lunges 4 × 20 m</td><td>3 × 6 min tempo / 2 min easy</td><td>6 × (600 m + station)</td></tr>
        <tr><td><strong>6</strong></td><td>50 min</td><td>Strength + sled push and pull</td><td>5 × 4 min</td><td>6 × (800 m + station), stations at race effort</td></tr>
        <tr><td><strong>7</strong> (simulation)</td><td>40 min</td><td>Light strength</td><td>—</td><td>Half or full Hyrox simulation at target pace</td></tr>
        <tr><td><strong>8</strong> (taper)</td><td>25–30 min</td><td>2 short workouts, 2 × 6</td><td>4 × 1 min brisk</td><td>15 min easy activation a few days before the race</td></tr>
      </tbody>
    </table>
    <p class="note">A sample plan, not a universal prescription. If a week doesn’t go to plan, don’t try to make it up, just carry on with the next one.</p>'''),
        ('stanice', 'Practising the stations: technique in brief', '''    <ul>
      <li><strong>SkiErg:</strong> pull from your hips and trunk, not just your arms. Keep an even rhythm.</li>
      <li><strong>Sled Push:</strong> low centre of gravity, short and quick steps, keep it smooth.</li>
      <li><strong>Sled Pull:</strong> your legs and trunk do the work, your hands only pass the rope along.</li>
      <li><strong>Burpee Broad Jumps:</strong> short jumps in rhythm, save your breath and your arms.</li>
      <li><strong>Rowing:</strong> legs first, then trunk, arms last.</li>
      <li><strong>Farmers Carry:</strong> firm grip, short steps, don’t put the weights down unless you have to.</li>
      <li><strong>Sandbag Lunges:</strong> knees under control, the bag stable on your shoulders.</li>
      <li><strong>Wall Balls:</strong> a smooth squat and throw, short sets with short pauses.</li>
    </ul>'''),
        ('preteky', 'The last week and race day', '''    <ul>
      <li><strong>Don’t try new things.</strong> Food, shoes and clothing must be proven in training.</li>
      <li><strong>Sleep.</strong> In the last days before the race, sleep is the best preparation.</li>
      <li><strong>Start slowly.</strong> The first kilometre feels easy on adrenaline, and you’ll pay for an overeager pace in the second half.</li>
      <li><strong>Hold your pacing.</strong> Work out your target pace in the <a href="/en/hyrox-pacing-calculator">Hyrox pacing calculator</a>.</li>
    </ul>'''),
        ('sledovanie', 'How to track progress', '''    <p>After each simulation, write down the splits of all runs and stations. You’ll see where you lose time and can focus your training there. Track strength progress in the <a href="/en/1rm-calculator">1RM calculator</a> and in your <a href="/en/blog/training-log">training log</a>.</p>'''),
    ],
))

import extras_loader
ARTICLES = extras_loader.merge(ARTICLES, LANG, {'health': DISC_HEALTH, 'train': DISC_TRAIN})
