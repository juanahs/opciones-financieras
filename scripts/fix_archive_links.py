#!/usr/bin/env python3
"""Replace references to archived chapter files in active markdown files.

For any link or literal path that points to 'chapters/_archive/NAME.md' this script will:
- If 'chapters/NAME.md' exists, replace the reference to point to './chapters/NAME.md'
- Otherwise, leave it and report it for manual review

It operates in-place and prints a summary.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'chapters'
ARCH = CH / '_archive'

pattern = re.compile(r"\bchapters/_archive/([\w\-\.]+\.md)\b")

files = sorted([p for p in CH.iterdir() if p.suffix=='.md'])
replacements = []
for p in files:
    txt = p.read_text(encoding='utf-8')
    matches = list(pattern.finditer(txt))
    if not matches:
        continue
    new_txt = txt
    changed = False
    for m in matches:
        name = m.group(1)
        active = CH / name
        if active.exists():
            new_txt = new_txt.replace(f'chapters/_archive/{name}', f'chapters/{name}')
            changed = True
            replacements.append((p.name, name))
        else:
            print(f'Warning: referenced archived file not found as active: {name} (in {p.name})')
    if changed:
        p.write_text(new_txt, encoding='utf-8')

print('Replacements made:', len(replacements))
for a,b in replacements:
    print(' -', a, '<-- now points to -->', b)

