#!/usr/bin/env python3
"""Remove restoration comments and any literal references to './_archive/' from active chapter files."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'chapters'

pattern_arch = re.compile(r"\./_archive/[\w\-\.]+\.md")
pattern_comment = re.compile(r"<!-- Restored from _archive/.*-->")

files = sorted([p for p in CH.iterdir() if p.suffix == '.md'])
cleaned = []
for p in files:
    txt = p.read_text(encoding='utf-8')
    lines = txt.splitlines()
    new_lines = []
    changed = False
    for L in lines:
        if pattern_comment.search(L):
            changed = True
            continue
        if pattern_arch.search(L):
            changed = True
            continue
        new_lines.append(L)
    if changed:
        p.write_text('\n'.join(new_lines).rstrip() + '\n', encoding='utf-8')
        cleaned.append(p.name)

print('Cleaned references in', len(cleaned), 'files')
for n in cleaned:
    print(' -', n)

