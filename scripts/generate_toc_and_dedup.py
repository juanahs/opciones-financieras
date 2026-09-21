#!/usr/bin/env python3
"""Genera CHAPTERS_INDEX.json y DUPLICATES_REPORT.json y reescribe index.html con Full TOC.

Uso: python3 scripts/generate_toc_and_dedup.py
"""
import os
import io
import re
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / 'chapters'
ARCHIVE_DIR = CHAPTERS_DIR / '_archive'

# Cargar archivos markdown activos (excluir _archive)
md_files = sorted([p for p in CHAPTERS_DIR.glob('*.md') if p.name != 'README.md'])

chapters = []
active_items = []

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

for p in md_files:
    text = p.read_text(encoding='utf-8')
    # detect pointer/archive files: start with 'Archivo archivado' or contain that phrase near top
    first_lines = '\n'.join(text.splitlines()[:6])
    is_archived_pointer = 'Archivo archivado' in first_lines or 'Archivo archivado' in text[:200]
    # extract first H1 title (line starting with '# ')
    title = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('# '):
            title = line[2:].strip()
            break
    if not title:
        # fallback to filename
        title = p.stem
    word_count = len(re.findall(r"\w+", text))
    h = sha256_text(text)
    item = {
        'filename': str(p.relative_to(ROOT)),
        'path': str(p),
        'title': title,
        'is_pointer': is_archived_pointer,
        'word_count': word_count,
        'sha256': h
    }
    chapters.append(item)
    if not is_archived_pointer:
        active_items.append((p, text, item))

# Write CHAPTERS_INDEX.json
index = {
    'generated_at': __import__('datetime').datetime.utcnow().isoformat() + 'Z',
    'total_markdown_files': len(md_files),
    'active_chapters_count': len(active_items),
    'chapters': [c for c in chapters]
}
with (ROOT / 'CHAPTERS_INDEX.json').open('w', encoding='utf-8') as f:
    json.dump(index, f, indent=2, ensure_ascii=False)
print('Wrote CHAPTERS_INDEX.json')

# Prepare texts for TF-IDF (active only)
texts = [t for (_p, t, _item) in active_items]
paths = [str(p.relative_to(ROOT)) for (p, _t, _item) in active_items]

# Compute TF-IDF and similarities without external dependencies
from math import log, sqrt
import re

def tokenize(text):
    tokens = re.findall(r"\w+", text.lower())
    stopwords = set([
        'de','la','que','el','en','y','a','los','del','se','las','por','un','para','con','no','una','su','al','lo','como','más','pero','sus','le','ya','o','este','sí','porque','esta','entre','cuando','muy','sin','sobre','también','me','hasta','hay','donde'
    ])
    return [t for t in tokens if t not in stopwords and len(t)>2]

docs_tokens = [tokenize(t) for t in texts]
N = len(docs_tokens)

# term frequencies
tfs = []
df = {}
for tokens in docs_tokens:
    from collections import Counter
    c = Counter(tokens)
    tfs.append(c)
    for term in c.keys():
        df[term] = df.get(term, 0) + 1

# idf
idf = {term: log((N+1)/(df_count+1)) + 1.0 for term, df_count in df.items()}

# tf-idf vectors (sparse dicts)
tfidf_vecs = []
norms = []
for c in tfs:
    vec = {}
    s = 0.0
    for term, freq in c.items():
        w = (1 + log(freq)) * idf.get(term, 0.0)
        vec[term] = w
        s += w*w
    norm = sqrt(s)
    tfidf_vecs.append(vec)
    norms.append(norm)

# cosine similarity
pairs_high = []
pairs_medium = []
for i in range(N):
    for j in range(i+1, N):
        vec_i = tfidf_vecs[i]
        vec_j = tfidf_vecs[j]
        # compute dot product over smaller dict
        if len(vec_i) < len(vec_j):
            small, big = vec_i, vec_j
        else:
            small, big = vec_j, vec_i
        dot = 0.0
        for term, w in small.items():
            if term in big:
                dot += w * big[term]
        denom = norms[i] * norms[j]
        score = (dot / denom) if denom > 0 else 0.0
        if score >= 0.80:
            pairs_high.append({'a': paths[i], 'b': paths[j], 'score': round(score, 4)})
        elif score >= 0.60:
            pairs_medium.append({'a': paths[i], 'b': paths[j], 'score': round(score, 4)})

report = {
    'generated_at': __import__('datetime').datetime.utcnow().isoformat() + 'Z',
    'pairs_high_similarity': pairs_high,
    'pairs_medium_similarity': pairs_medium,
    'active_count': N
}
with (ROOT / 'DUPLICATES_REPORT.json').open('w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)
print('Wrote DUPLICATES_REPORT.json')

# Generate full index HTML (overwrite index.html)
html_lines = []
html_lines.append('<!doctype html>')
html_lines.append('<html lang="es">')
html_lines.append('<head>')
html_lines.append('  <meta charset="utf-8" />')
html_lines.append('  <meta name="viewport" content="width=device-width,initial-scale=1" />')
html_lines.append('  <title>Índice - Opciones Financieras</title>')
html_lines.append('  <style>body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial;margin:40px;line-height:1.5}h1{margin-bottom:.2em}nav ul{list-style:none;padding:0}nav li{margin:.4em 0}a{color:#0366d6;text-decoration:none}footer{margin-top:2em;color:#666;font-size:.9em}code{background:#f6f8fa;padding:.1em .3em;border-radius:4px}</style>')
html_lines.append('</head>')
html_lines.append('<body>')
html_lines.append('  <h1>Índice - Manual de Opciones Financieras</h1>')
html_lines.append('  <p>Accede a los capítulos desde GitHub o localmente. Este índice contiene las entradas consolidadas tras un pase de reorganización.</p>')
html_lines.append('  <h2>TOC completo (capítulos activos)</h2>')
html_lines.append('  <ol>')
# Sort by filename natural
for item in sorted(index['chapters'], key=lambda x: x['filename']):
    if not item['is_pointer']:
        rel = item['filename']
        title = item['title']
        html_lines.append(f'    <li><a href="./{rel}">{title}</a> — <small>{rel}</small></li>')
html_lines.append('  </ol>')
html_lines.append('<hr/>')
html_lines.append('<p>Se recomienda revisar <code>REORG_MAP.json</code> y <code>DUPLICATES_REPORT.json</code> para ver fusiones y duplicados detectados.</p>')
html_lines.append('<footer>Generado automáticamente: reorganización y TOC completo. Fecha: %s</footer>' % index['generated_at'])
html_lines.append('</body>')
html_lines.append('</html>')

(ROOT / 'index.html').write_text('\n'.join(html_lines), encoding='utf-8')
print('Wrote index.html with full TOC')

print('Done')

