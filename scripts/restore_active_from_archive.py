#!/usr/bin/env python3
"""For any active chapter file that contains a reference to its archived full version,
restore the archived full content into the active file so the active file becomes
self-contained and does not point to the archive.

Pattern searched: './_archive/<name>.md' (backtick-wrapped or plain)
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'chapters'
ARCH = CH / '_archive'

pattern = re.compile(r"\./_archive/([\w\-\.]+\.md)")

files = sorted([p for p in CH.iterdir() if p.suffix == '.md'])
restored = []
for p in files:
    txt = p.read_text(encoding='utf-8')
    m = pattern.search(txt)
    if not m:
        continue
    name = m.group(1)
    arch = ARCH / name
    if arch.exists():
        arch_txt = arch.read_text(encoding='utf-8')
        # Write archived content into active file, but keep a small provenance note
        new_txt = f"<!-- Restored from _archive/{name} into {p.name} -->\n" + arch_txt
        p.write_text(new_txt, encoding='utf-8')
        restored.append((p.name, name))
    else:
        print(f'Warning: archive file not found for {p.name}: {name}')

print('Restored count:', len(restored))
for a,b in restored:
    print(' -', a, '<-- restored from --', b)

