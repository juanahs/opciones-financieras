#!/usr/bin/env python3
"""Clean merged active chapter files by removing merge markers and deduplicating paragraphs.

Behavior:
- Targets the same mapping used by the merge script (merge_archived_duplicates.py).
- For each active file in the mapping, removes the auto-inserted merge metadata comment and separator,
  then deduplicates exact paragraph duplicates while preserving original order.
- Ensures the top-level heading (# Capítulo N — ...) is preserved at the top.
- Writes cleaned content in place and reports stats per file.

Run:
  python3 scripts/clean_merged.py

"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'chapters'
ARCH = CH / '_archive'

MAPPINGS = {
    '126-checklist-profesional-completo.md': '126-checklist-profesional-antes-de-operar.md',
    '146-el-proceso-completo-de-una-operacion.md': '146-psicologia-del-operador-de-opciones.md',
    '147-construccion-de-un-plan-de-trading-con-opciones.md': '147-diario-profesional-de-operaciones.md',
    '148-roadmap-profesional-de-aprendizaje.md': '148-plan-anual-de-mejora.md',
    '181-apple-caso-completo.md': '181-estudio-de-caso-apple.md',
    '184-microsoft-caso-completo.md': '184-estudio-de-caso-microsoft.md',
    '211-glosario-profesional.md': '211-glosario-profesional-a.md',
}

heading_re = re.compile(r'^\s*#\s*Cap[ií]tulo\s+(\d+)\s*[-—–]\s*(.*)$', re.IGNORECASE)
merge_meta_re = re.compile(r'<!--\s*Merged from .* into .* on .*Z\s*-->')

stats = []
for active in MAPPINGS.keys():
    p = CH / active
    if not p.exists():
        print('Active missing, skipping:', active)
        continue
    text = p.read_text(encoding='utf-8')
    # remove the merge metadata comment and separators (a line with '---') that were inserted
    # We'll replace occurrences of the pattern: '\n\n---\n\n<!-- Merged from ... -->\n\n' or similar
    # Simpler approach: remove all merge meta comments and all lines consisting of only ---
    lines = text.splitlines()
    filtered = []
    i = 0
    while i < len(lines):
        L = lines[i]
        if merge_meta_re.search(L):
            # skip this line
            i += 1
            # also skip single blank after meta if present
            if i < len(lines) and lines[i].strip() == '':
                i += 1
            continue
        if L.strip() == '---':
            i += 1
            # skip following blank if present
            if i < len(lines) and lines[i].strip() == '':
                i += 1
            continue
        filtered.append(L)
        i += 1
    cleaned_text = '\n'.join(filtered).strip() + '\n'
    # Now deduplicate exact paragraphs: split by two or more newlines
    paras = re.split(r'\n{2,}', cleaned_text)
    # preserve heading if first paragraph is a Capítulo heading
    start_idx = 0
    heading = None
    if paras and heading_re.match(paras[0].splitlines()[0].strip() if paras[0].strip() else ''):
        heading = paras[0].strip()
        start_idx = 1
    seen = set()
    out_paras = []
    if heading:
        out_paras.append(heading)
        seen.add(heading)
    removed = 0
    for ptext in paras[start_idx:]:
        pnorm = ptext.strip()
        if not pnorm:
            continue
        if pnorm in seen:
            removed += 1
            continue
        seen.add(pnorm)
        out_paras.append(pnorm)
    new_text = '\n\n'.join(out_paras).strip() + '\n'
    if new_text != text:
        p.write_text(new_text, encoding='utf-8')
    stats.append((active, len(paras)-start_idx, removed))

print('Cleaned files:')
for fn, total_paras, removed in stats:
    print(f' - {fn}: paragraphs={total_paras}, duplicates_removed={removed}')

print('\nNote: archived files still in', ARCH)

