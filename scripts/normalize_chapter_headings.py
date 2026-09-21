#!/usr/bin/env python3
"""Normalize chapter headings in ./chapters: ensure first heading is "# Capítulo N — Title"

This script overwrites files in-place. It targets files with names like "012-name.md" or "12-name.md".
It will: read file, determine existing visible title (first markdown heading if any, else filename), and ensure the first non-empty line is a top-level heading with the normalized title.

Run from repository root or this directory. Example:

    python3 scripts/normalize_chapter_headings.py

"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'chapters'
if not ROOT.exists():
    print('Chapters directory not found:', ROOT)
    raise SystemExit(1)

md_files = sorted([p for p in ROOT.iterdir() if p.suffix == '.md'])
num_re = re.compile(r'^(\d+)-(.+)\.md$')

modified = []

for p in md_files:
    m = num_re.match(p.name)
    if not m:
        # skip non-numbered files
        continue
    num = int(m.group(1))
    slug = m.group(2)
    # default title from filename
    default_title = slug.replace('-', ' ').replace('_', ' ').strip()
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    # find first non-empty line
    first_idx = None
    for i, L in enumerate(lines):
        if L.strip() != '':
            first_idx = i
            break
    if first_idx is None:
        # empty file: create heading
        new_heading = f'# Capítulo {num} — {default_title}\n'
        p.write_text(new_heading + '\n', encoding='utf-8')
        modified.append(p.name)
        continue
    first_line = lines[first_idx]
    # if first line is a heading, extract its text
    heading_re = re.compile(r'^\s*#+\s*(.+)$')
    hm = heading_re.match(first_line)
    if hm:
        existing_title = hm.group(1).strip()
        # Remove any leading "Capítulo X — " so we can replace with correct chapter number
        existing_title = re.sub(r'^[Cc]ap[ií]tulo\s+\d+\s*[-—–]\s*', '', existing_title).strip()
    else:
        # use the first non-empty line as title candidate
        existing_title = first_line.strip()
    # choose title: if candidate is short (like a heading), use it, else fallback to filename
    if existing_title == '':
        title = default_title
    else:
        title = existing_title
    new_heading = f'# Capítulo {num} — {title}'
    # replace or insert
    if hm:
        # replace lines[first_idx]
        lines[first_idx] = new_heading
    else:
        # insert heading before first_idx
        lines.insert(first_idx, new_heading)
    new_text = '\n'.join(lines).strip() + '\n'
    if new_text != text:
        p.write_text(new_text, encoding='utf-8')
        modified.append(p.name)

print('Normalized headings in', len(modified), 'files')
for n in modified[:200]:
    print(' -', n)
if len(modified) == 0:
    print('No changes needed.')

