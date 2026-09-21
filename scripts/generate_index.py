#!/usr/bin/env python3
from pathlib import Path
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'chapters'
OUT = ROOT / 'index.html'

# collect markdown files in chapters (exclude _archive dir)
mds = sorted([p for p in CH.iterdir() if p.suffix == '.md'])
num_re = re.compile(r'^(\d+)-')

def get_num(p):
    m = num_re.match(p.name)
    if m:
        return int(m.group(1))
    return 10**9

# group into sections by number ranges
sections = [
    ('Introducción & Fundamentos', lambda n: 0 <= n <= 9),
    ('Estrategias y conceptos prácticos', lambda n: 10 <= n <= 99),
    ('Nivel profesional, modelos y frameworks (100–199)', lambda n: 100 <= n <= 199),
    ('Checklists, glosario y anexos (200+)', lambda n: n >= 200),
]

items = [(get_num(p), p.name) for p in mds]
items.sort(key=lambda x: (x[0], x[1]))

html = []
html.append('<!doctype html>')
html.append('<html lang="es">')
html.append('<head>')
html.append('  <meta charset="utf-8" />')
html.append('  <meta name="viewport" content="width=device-width,initial-scale=1" />')
html.append('  <title>Índice - Opciones Financieras</title>')
html.append('  <style>body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial;margin:40px;line-height:1.5}h1{margin-bottom:.2em}nav ul, ul{list-style:none;padding:0;margin:0}nav li, ul li{margin:.4em 0}a{color:#0366d6;text-decoration:none}footer{margin-top:2em;color:#666;font-size:.9em}code{background:#f6f8fa;padding:.1em .3em;border-radius:4px}</style>')
html.append('</head>')
html.append('<body>')
html.append('  <h1>Manual de Opciones Financieras</h1>')
html.append('  <p>Guía estructurada para inversores: desde fundamentos hasta frameworks y modelos profesionales.</p>')
html.append('')
html.append('  <h2>Índice</h2>')

for sec_title, cond in sections:
    html.append(f'  <h3>{sec_title}</h3>')
    # use unordered list so browsers don't render numeric prefixes (filenames already include numbers)
    html.append('  <ul>')
    for num, fname in items:
        if cond(num):
            # Show only the filename as link text (e.g. "10-leaps.md")
            html.append(f'    <li><a href="./chapters/{fname}">{fname}</a></li>')
    html.append('  </ul>')

html.append('<hr/>')
html.append('<p>Si detectas duplicados o quieres reorganizar capítulos, mueve/renombra archivos en <code>chapters/</code> y ejecuta <code>scripts/generate_index.py</code> localmente para regenerar este índice.</p>')
html.append(f'<footer>Índice generado: {datetime.now(timezone.utc).isoformat()}Z</footer>')
html.append('</body>')
html.append('</html>')

OUT.write_text('\n'.join(html), encoding='utf-8')
print('Wrote', OUT)
