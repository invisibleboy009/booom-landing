# Social preview images (1200x630) for every blog article and tool page, per language.
# Usage: python blog-src/make_og.py      -> assets/og/<lang>-<key>.jpg
# Needs Pillow and a bold sans font with Latin-Extended (Segoe UI Bold / Arial Bold on Windows).
# Titles for articles come from content_{sk,en,cs}.py, tool titles are listed below.
import os, sys, importlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.join(HERE, '..')
OUT = os.path.join(ROOT, 'assets', 'og')
os.makedirs(OUT, exist_ok=True)

FONT_CANDIDATES = ['C:/Windows/Fonts/segoeuib.ttf', 'C:/Windows/Fonts/arialbd.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']
FONT = next(p for p in FONT_CANDIDATES if os.path.exists(p))
W, H = 1200, 630
GREEN, CYAN = (0, 230, 118), (0, 212, 255)

TOOLS = {
    'sk': {'1rm': '1RM kalkulačka', 'calories': 'Kalorická kalkulačka (BMR a TDEE)', 'hyrox-pacing': 'Hyrox pacing kalkulačka', 'body-fat': 'Percento telesného tuku'},
    'en': {'1rm': '1RM calculator', 'calories': 'Calorie calculator (BMR & TDEE)', 'hyrox-pacing': 'Hyrox pacing calculator', 'body-fat': 'Body fat calculator'},
    'cs': {'1rm': 'Kalkulačka 1RM', 'calories': 'Kalorická kalkulačka (BMR a TDEE)', 'hyrox-pacing': 'Hyrox pacing kalkulačka', 'body-fat': 'Kalkulačka tělesného tuku'},
}
TAG = {'sk': ('BLOG', 'NÁSTROJ ZADARMO', 'Zadarmo pre iOS, Android aj web'),
       'en': ('BLOG', 'FREE TOOL', 'Free for iOS, Android and web'),
       'cs': ('BLOG', 'NÁSTROJ ZDARMA', 'Zdarma pro iOS, Android i web')}

from about_content import ABOUT
ABOUT_TAG = {'sk': 'O NÁS', 'en': 'ABOUT', 'cs': 'O NÁS'}

def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    return lines

def card(title, tag, foot, path):
    img = Image.new('RGB', (W, H), (10, 10, 10))
    glow = Image.new('RGB', (W, H), (10, 10, 10))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-260, -320, 620, 480), fill=(0, 90, 50))
    gd.ellipse((760, 300, 1400, 900), fill=(0, 70, 90))
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    img = Image.blend(img, glow, 0.9)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 12, H), fill=GREEN)
    f_brand = ImageFont.truetype(FONT, 46)
    f_tag = ImageFont.truetype(FONT, 26)
    f_foot = ImageFont.truetype(FONT, 28)
    d.text((72, 56), 'BOOOM', font=f_brand, fill=GREEN)
    tw = d.textlength(tag, font=f_tag)
    d.rounded_rectangle((W - 72 - tw - 44, 58, W - 72, 106), radius=24, outline=GREEN, width=2)
    d.text((W - 72 - tw - 22, 66), tag, font=f_tag, fill=GREEN)
    size = 84
    while True:
        f = ImageFont.truetype(FONT, size)
        lines = wrap(d, title, f, W - 144)
        if len(lines) <= 3 and all(d.textlength(l, font=f) <= W - 144 for l in lines):
            break
        size -= 4
    lh = int(size * 1.16)
    y = 150 + (3 - len(lines)) * lh // 2 + 20
    for l in lines:
        d.text((72, y), l, font=f, fill=(255, 255, 255)); y += lh
    d.text((72, H - 84), foot + '  ·  booom.fit', font=f_foot, fill=(170, 170, 170))
    img.convert('RGB').save(path, 'JPEG', quality=84, optimize=True, progressive=True)

n = 0
for lang in ('sk', 'en', 'cs'):
    mod = importlib.import_module('content_' + lang)
    for a in mod.ARTICLES:
        card(a['h1'], TAG[lang][0], TAG[lang][2], os.path.join(OUT, '%s-%s.jpg' % (lang, a['slug']))); n += 1
    card(mod.HUB['h1'], TAG[lang][0], TAG[lang][2], os.path.join(OUT, '%s-blog.jpg' % lang)); n += 1
    card(ABOUT[lang]['h1'], ABOUT_TAG[lang], TAG[lang][2], os.path.join(OUT, '%s-about.jpg' % lang)); n += 1
    for key, title in TOOLS[lang].items():
        card(title, TAG[lang][1], TAG[lang][2], os.path.join(OUT, '%s-%s.jpg' % (lang, key))); n += 1
print(n, 'images in', os.path.normpath(OUT))
