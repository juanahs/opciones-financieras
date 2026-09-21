#!/usr/bin/env python3
"""Add a YAML front-matter `title:` to markdown files in `chapters/` that lack one.

Behavior:
- For each `*.md` in `chapters/` (skips directories named `_archive`),
- If the file already has front-matter with a `title:` entry, it is left unchanged.
- Otherwise, the script extracts a title from YAML front-matter (if present),
  or from the first Markdown heading (`#`/`##`/`###`), or falls back to the
  filename without numeric prefix. The extracted title is cleaned and
  capitalized with a simple Spanish-aware heuristic, and inserted as
  `title: "..."` in the front-matter (creating the front-matter block if needed).

Run from project root:
  python3 scripts/add_frontmatter_titles.py

This script modifies files in-place. It prints a summary of changed files.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'chapters'

def fallback_filename(filename: str) -> str:
    name = re.sub(r'^\d+-', '', filename)
    name = re.sub(r'\.md$', '', name)
    return name.replace('-', ' ').replace('_', ' ').strip()

def extract_title_from_text(text: str, filename: str) -> str:
    """Extract a title from text: front-matter title, first heading, else filename fallback."""
    # front-matter title
    if text.startswith('---'):
        m = re.search(r'^---\s*\n(.*?)\n---\s*\n', text, flags=re.S)
        if m:
            fm = m.group(1)
            for ln in fm.splitlines():
                mm = re.match(r'^title:\s*(.+)$', ln.strip(), flags=re.I)
                if mm:
                    val = mm.group(1).strip().strip('"').strip("'")
                    return clean_title(val, filename)
    # first heading
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if re.match(r'^#{1,3}\s+', s):
            val = re.sub(r'^#{1,3}\s+', '', s).strip()
            return clean_title(val, filename)
        # if first non-empty line is not a heading, don't treat as title
        break
    return clean_title(fallback_filename(filename), filename)


def clean_title(val: str, filename: str) -> str:
    t = val.strip()
    if not t:
        return fallback_filename(filename)
    # remove 'Capítulo N -' or numeric prefix
    t = re.sub(r'(?i)^cap[ií]tulo\s*\d+\s*[:\-–—]\s*', '', t)
    t = re.sub(r'^\d+\s*[:\-–—]\s*', '', t)
    # choose right-most part if ' - ' or ' — ' present
    parts = re.split(r'\s+[\-–—:]\s+', t)
    if len(parts) > 1:
        t = parts[-1].strip()
    t = re.sub(r'\s+', ' ', t).strip()
    if not t:
        return fallback_filename(filename)
    return smart_capitalize(t)


def smart_capitalize(s: str) -> str:
    small = {
        'de', 'del', 'la', 'el', 'los', 'las', 'y', 'o', 'a', 'al', 'en', 'por', 'para', 'con', 'sin',
        'una', 'un', 'lo', 'su', 'sus', 'ante', 'entre', 'hacia', 'hasta', 'desde'
    }
    words = re.split(r'(\s+)', s)
    result = []
    first = True
    for token in words:
        if token.isspace():
            result.append(token)
            continue
        w = token
        low = w.lower()
        if first:
            result.append(w[:1].upper() + w[1:])
            first = False
            continue
        if low in small:
            result.append(low)
        else:
            result.append(w[:1].upper() + w[1:])
    return ''.join(result)


def ensure_frontmatter_title(path: Path) -> bool:
    """Return True if file was modified, False otherwise."""
    text = path.read_text(encoding='utf-8')
    if text.startswith('---'):
        # find front-matter block
        m = re.match(r'^(---\s*\n)(.*?)(\n---\s*\n)(.*)$', text, flags=re.S)
        if m:
            prefix, fm, suffix, rest = m.group(1), m.group(2), m.group(3), m.group(4)
            # check if title exists
            if re.search(r'^title:\s*', fm, flags=re.I | re.M):
                return False
            # compute title from rest or fm
            title = extract_title_from_text(text, path.name)
            # insert title line at top of front-matter
            new_fm = f'title: "{title}"\n{fm}'
            new_text = prefix + new_fm + suffix + rest
            path.write_text(new_text, encoding='utf-8')
            return True
        else:
            # malformed front-matter; treat as no front-matter
            pass

    # no front-matter: create one
    title = extract_title_from_text(text, path.name)
    fm = f'---\ntitle: "{title}"\n---\n\n'
    new_text = fm + text
    path.write_text(new_text, encoding='utf-8')
    return True


def main():
    if not CH.exists():
        print('chapters/ directory not found — aborting')
        return
    changed = []
    for p in sorted(CH.iterdir()):
        if p.is_dir():
            if p.name == '_archive':
                continue
            # skip other directories
            continue
        if p.suffix.lower() != '.md':
            continue
        try:
            mod = ensure_frontmatter_title(p)
        except Exception as e:
            print('Error processing', p, e)
            continue
        if mod:
            changed.append(p.name)

    print(f'Updated {len(changed)} files')
    for n in changed[:200]:
        print('  ', n)


if __name__ == '__main__':
    main()

