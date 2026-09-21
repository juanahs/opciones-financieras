#!/usr/bin/env python3
"""Ensure a standard front-matter template is present in each chapter markdown.

This script will:
- For each `chapters/*.md` (skipping `chapters/_archive/`), ensure the file has a
  YAML front-matter block starting with `---` and ending with `---`.
- If the front-matter is missing keys, it will insert default keys without
  overwriting existing values:
    title: (kept if present)
    description: ""
    date: YYYY-MM-DD (today UTC if not present)
    tags: []
    draft: false

Run locally before commit if you want consistent front-matter across files.
"""
from pathlib import Path
from datetime import datetime, timezone
import re

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'chapters'

def read_file(p: Path) -> str:
    return p.read_text(encoding='utf-8')

def write_file(p: Path, s: str) -> None:
    p.write_text(s, encoding='utf-8')

def ensure_template(p: Path) -> bool:
    """Return True if modified."""
    text = read_file(p)
    today = datetime.now(timezone.utc).date().isoformat()

    if text.startswith('---'):
        m = re.match(r'^(---\s*\n)(.*?)(\n---\s*\n)(.*)$', text, flags=re.S)
        if not m:
            # malformed front-matter: create a fresh block
            fm = f'---\ntitle: ""\ndescription: ""\ndate: {today}\ntags: []\ndraft: false\n---\n\n'
            write_file(p, fm + text)
            return True
        prefix, fm, suffix, rest = m.group(1), m.group(2), m.group(3), m.group(4)
        fm_lines = fm.splitlines()
        keys_present = {re.match(r'^([A-Za-z0-9_\-]+)\s*:', l).group(1).lower()
                        for l in fm_lines if re.match(r'^([A-Za-z0-9_\-]+)\s*:', l)}

        changed = False
        add_lines = []
        if 'title' not in keys_present:
            # try to extract H1 from rest
            title = extract_h1(rest) or ''
            add_lines.append(f'title: "{title}"')
            changed = True
        if 'description' not in keys_present:
            add_lines.append('description: ""')
            changed = True
        if 'date' not in keys_present:
            add_lines.append(f'date: {today}')
            changed = True
        if 'tags' not in keys_present:
            add_lines.append('tags: []')
            changed = True
        if 'draft' not in keys_present:
            add_lines.append('draft: false')
            changed = True

        if changed:
            # insert added lines at top of front-matter so title appears first
            new_fm = '\n'.join(add_lines + fm_lines).strip() + '\n'
            new_text = prefix + new_fm + suffix + rest
            write_file(p, new_text)
            return True
        return False

    else:
        # no front-matter; create one with title extracted from first H1 or filename
        body = text
        title = extract_h1(body) or fallback_filename(p.name)
        fm = (
            '---\n'
            f'title: "{title}"\n'
            'description: ""\n'
            f'date: {datetime.now(timezone.utc).date().isoformat()}\n'
            'tags: []\n'
            'draft: false\n'
            '---\n\n'
        )
        write_file(p, fm + body)
        return True


def fallback_filename(name: str) -> str:
    s = re.sub(r'^\d+-', '', name)
    s = re.sub(r'\.md$', '', s)
    return s.replace('-', ' ').replace('_', ' ').strip()


def extract_h1(text: str) -> str:
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r'^#\s+(.*)', s)
        if m:
            return m.group(1).strip()
        # don't search past first non-empty non-heading line
        break
    return ''


def main():
    if not CH.exists():
        print('chapters/ not found; aborting')
        return
    changed = []
    for p in sorted(CH.iterdir()):
        if p.is_dir():
            if p.name == '_archive':
                continue
            continue
        if p.suffix.lower() != '.md':
            continue
        try:
            if ensure_template(p):
                changed.append(p.name)
        except Exception as e:
            print('error', p, e)

    print(f'Updated {len(changed)} files')
    for n in changed[:200]:
        print('  ', n)


if __name__ == '__main__':
    main()

