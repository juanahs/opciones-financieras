#!/usr/bin/env python3
"""Merge archived duplicate chapter files into their active counterparts.

Rules:
- For each pair (active, archived) provided in the mapping below, append the archived file's body
  to the active file with a clear separator block that records the source filename and timestamp.
- Remove the archived file only after successful merge (we keep archived files as backup; this script
  will not delete them, but will report the merged list).
- Preserve existing headings. When appending, strip any leading top-level heading from the archived
  file to avoid duplicate chapter headings.

Run from repository root:
  python3 scripts/merge_archived_duplicates.py

"""
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'chapters'
ARCH = CH / '_archive'

# Mapping: active -> archived
MAPPINGS = {
    '126-checklist-profesional-completo.md': '126-checklist-profesional-antes-de-operar.md',
    '146-el-proceso-completo-de-una-operacion.md': '146-psicologia-del-operador-de-opciones.md',
    '147-construccion-de-un-plan-de-trading-con-opciones.md': '147-diario-profesional-de-operaciones.md',
    '148-roadmap-profesional-de-aprendizaje.md': '148-plan-anual-de-mejora.md',
    '181-apple-caso-completo.md': '181-estudio-de-caso-apple.md',
    '184-microsoft-caso-completo.md': '184-estudio-de-caso-microsoft.md',
    '211-glosario-profesional.md': '211-glosario-profesional-a.md',
}

merged = []
errors = []

for active, archived in MAPPINGS.items():
    active_path = CH / active
    archived_path = ARCH / archived
    if not active_path.exists():
        errors.append(f'Active file not found: {active_path}')
        continue
    if not archived_path.exists():
        # maybe archived file was not moved or located elsewhere
        alt = CH / archived
        if alt.exists():
            archived_path = alt
        else:
            errors.append(f'Archived file not found: {archived_path} (or {alt})')
            continue
    try:
        a_text = active_path.read_text(encoding='utf-8')
        b_text = archived_path.read_text(encoding='utf-8')
        # strip leading heading from archived file
        lines = b_text.splitlines()
        # remove leading blank lines
        i = 0
        while i < len(lines) and lines[i].strip() == '':
            i += 1
        # if first non-empty line is a markdown heading, remove it
        if i < len(lines) and lines[i].lstrip().startswith('#'):
            i += 1
            # also skip one blank line after heading if present
            if i < len(lines) and lines[i].strip() == '':
                i += 1
        body = '\n'.join(lines[i:]).strip()
        if not body:
            note = f'\n\n<!-- Merged file {archived} was empty after stripping heading. -->\n'
            a_text = a_text.rstrip() + note
        else:
            sep = '\n\n---\n\n'
            meta = f'<!-- Merged from {archived} into {active} on {datetime.utcnow().isoformat()}Z -->\n\n'
            a_text = a_text.rstrip() + sep + meta + body + '\n'
        active_path.write_text(a_text, encoding='utf-8')
        merged.append((active, archived))
    except Exception as e:
        errors.append(f'Error merging {archived} -> {active}: {e}')

# report
print('Merged pairs:')
for act, arch in merged:
    print(' -', act, '<--', arch)
if errors:
    print('\nErrors:')
    for e in errors:
        print(' -', e)
else:
    print('\nNo errors.')

# final duplicate check
num_re = r'^(\d+)-'
import re
files = sorted([p.name for p in CH.iterdir() if p.suffix=='.md'])
counts = {}
for f in files:
    m = re.match(num_re, f)
    k = int(m.group(1)) if m else None
    counts[k] = counts.get(k, 0) + 1
dups = [k for k,v in counts.items() if k is not None and v > 1]
print('\nAfter merge, duplicate numeric prefixes remaining:', len(dups))
if dups:
    for k in dups:
        print(' -', k)

print('\nNote: archived files remain in', ARCH)

