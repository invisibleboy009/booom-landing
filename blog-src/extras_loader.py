# Merges blog-src/extras/*.py into a content module's ARTICLES list.
#
# Each extras file defines EXACTLY ONE of:
#   EXTEND = {'sk': {...}, 'en': {...}, 'cs': {...}}   longer version of an existing article
#       per language: 'sections': [(after_section_id, (id, title, body_html)), ...]  (inserted after that id)
#                     'faq': [(question, answer_html), ...]                          (appended)
#       KEY = 'treningovy-dennik' etc. (the Slovak slug of the base article)
#   NEW = {'sk': article_dict, 'en': article_dict, 'cs': article_dict}   a brand-new article
#       article_dict has the same fields as the base articles; 'disc' is 'health' or 'train'.
# New articles are appended in file-name order (name files 10_..., 11_...).
import os, importlib.util

BASE_KEYS = ['treningovy-dennik', 'progresivne-pretazenie', 'kolko-bielkovin-denne', 'hyrox-priprava-8-tyzdnov']
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extras')

def _load(path):
    spec = importlib.util.spec_from_file_location('extra_' + os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def merge(articles, lang, disc_map):
    articles = list(articles)
    if not os.path.isdir(HERE):
        return articles
    for name in sorted(os.listdir(HERE)):
        if not name.endswith('.py') or name.startswith('_'):
            continue
        m = _load(os.path.join(HERE, name))
        if hasattr(m, 'EXTEND'):
            i = BASE_KEYS.index(m.KEY)
            a = dict(articles[i])
            ext = m.EXTEND[lang]
            secs = list(a['sections'])
            for after, sec in ext.get('sections', []):
                ids = [s[0] for s in secs]
                pos = ids.index(after) + 1 if after in ids else len(secs)
                secs.insert(pos, sec)
            a['sections'] = secs
            a['faq'] = list(a['faq']) + list(ext.get('faq', []))
            articles[i] = a
        elif hasattr(m, 'NEW'):
            a = dict(m.NEW[lang])
            a['disc'] = disc_map[a.get('disc', 'train')]
            articles.append(a)
    return articles
