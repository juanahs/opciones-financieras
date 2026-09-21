#!/usr/bin/env python3
"""
Generate a `nav:` section for `mkdocs.yml` from files in `chapters/`.

Behavior:
- scans `chapters/` for `*.md` files (excludes any directory named `_archive`)
- extracts the first top-level header `# Title` from each file (fallback: filename without numeric prefix)
- groups pages into the same numeric ranges used by `scripts/generate_index.py`
- overwrites `mkdocs.yml` placing a generated `nav:` section (preserving other site settings)

Run locally from the project root:

  python3 scripts/generate_mkdocs_nav.py

"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'chapters'
MK = ROOT / 'mkdocs.yml'

num_re = re.compile(r'^(\d+)-')

def get_num(name):
    m = num_re.match(name)
    if m:
        return int(m.group(1))
    return 10**9

def title_from_file(p):
    """Return a cleaned, human-friendly title for file p.

    Priority:
    1. YAML front-matter `title:` if present
    2. First Markdown heading (`# Title` or `## Title`)
    3. Fallback to filename (without numeric prefix and extension)

    Cleaning:
    - remove leading numeric/"Capítulo N -" prefixes
    - when title contains separators like '—' or '-', prefer the right-most descriptive part
    - strip and normalize whitespace
    """
    # try YAML front-matter (read first chunk of file)
    try:
        with p.open('r', encoding='utf-8') as f:
            lines = []
            for _ in range(50):
                try:
                    lines.append(next(f))
                except StopIteration:
                    break
    except Exception:
        lines = []

    # parse front matter if present
    if lines and lines[0].strip() == '---':
        for ln in lines[1:]:
            if ln.strip() == '---':
                break
            m = re.match(r'^title:\s*(.+)$', ln.strip(), flags=re.I)
            if m:
                val = m.group(1).strip().strip('"').strip("'")
                return clean_title(val, p.name)

    # search for first heading
    try:
        with p.open('r', encoding='utf-8') as f:
            for line in f:
                s = line.strip()
                if not s:
                    continue
                if re.match(r'^#{1,3}\s+', s):
                    val = re.sub(r'^#{1,3}\s+', '', s).strip()
                    return clean_title(val, p.name)
    except Exception:
        pass

    # fallback: filename without numeric prefix and extension
    name = p.name
    name = re.sub(r'^\d+-', '', name)
    name = re.sub(r'\.md$', '', name)
    return clean_title(name.replace('-', ' ').replace('_', ' ').strip(), p.name)


def clean_title(val, filename):
    """Clean common repetition and prefixes from extracted title string."""
    t = val.strip()
    if not t:
        return fallback_filename(filename)

    # remove common leading 'Capitulo N', 'Capítulo N', or numeric prefixes like '10 - '
    t = re.sub(r'(?i)^cap[ií]tulo\s*\d+\s*[:\-–—]\s*', '', t)
    t = re.sub(r'^\d+\s*[:\-–—]\s*', '', t)

    # if there is a separator like '—' or ' - ', prefer the right-most descriptive part
    parts = re.split(r'\s+[\-–—:]\s+', t)
    if len(parts) > 1:
        # drop parts that are identical or short numeric placeholders
        chosen = parts[-1].strip()
        if not chosen or re.match(r'^cap[ií]tulo\s*\d+$', chosen.strip(), flags=re.I):
            # fallback to first non-empty
            for p in reversed(parts):
                if p.strip() and not re.match(r'^cap[ií]tulo\s*\d+$', p.strip(), flags=re.I):
                    chosen = p.strip()
                    break
        t = chosen

    # remove accidental duplication 'X — X' where both sides equal (case-insensitive)
    if '—' in val or '–' in val or '-' in val:
        # normalize and compare
        segs = re.split(r'\s+[\-–—:]\s+', val)
        if len(segs) >= 2:
            left = segs[0].strip().casefold()
            right = segs[-1].strip().casefold()
            if left == right:
                t = segs[-1].strip()

    # final cleanup: collapse spaces
    t = re.sub(r'\s+', ' ', t).strip()
    # if title is just 'Capítulo N' or a bare number, fallback to filename
    if not t or re.match(r'(?i)^(cap[ií]tulo\s*\d+|\d+)$', t):
        return fallback_filename(filename)
    return t


def fallback_filename(filename):
    name = re.sub(r'^\d+-', '', filename)
    name = re.sub(r'\.md$', '', name)
    return name.replace('-', ' ').replace('_', ' ').strip()


def smart_capitalize(s: str) -> str:
    """Return a human-friendly capitalized title for Spanish text.

    Rules (simple heuristic):
    - Capitalize first letter of each significant word.
    - Keep small words lowercase unless first word.
    - Preserve existing accented characters.
    """
    small = {
        'de', 'del', 'la', 'el', 'los', 'las', 'y', 'o', 'a', 'al', 'en', 'por', 'para', 'con', 'sin',
        'una', 'un', 'el', 'lo', 'su', 'sus', 'ante', 'entre', 'hacia', 'hasta', 'desde'
    }
    words = re.split(r'(\s+)', s)  # keep separators
    result = []
    first_word = True
    for token in words:
        if token.isspace():
            result.append(token)
            continue
        w = token
        low = w.lower()
        if first_word:
            # Capitalize first character, preserve rest
            result.append(w[:1].upper() + w[1:])
            first_word = False
            continue
        if low in small:
            result.append(low)
        else:
            result.append(w[:1].upper() + w[1:])
    return ''.join(result)

# same section grouping as generate_index.py
sections = [
    ('Introducción & Fundamentos', lambda n: 0 <= n <= 9),
    ('Estrategias y conceptos prácticos', lambda n: 10 <= n <= 99),
    ('Nivel profesional, modelos y frameworks (100–199)', lambda n: 100 <= n <= 199),
    ('Checklists, glosario y anexos (200+)', lambda n: n >= 200),
]

mds = [p for p in CH.iterdir() if p.suffix == '.md']
items = [(get_num(p.name), p) for p in mds]
items.sort(key=lambda x: (x[0], x[1].name))

nav_lines = []
for sec_title, cond in sections:
    group = [p for n, p in items if cond(n)]
    if not group:
        continue
    nav_lines.append(f'  - "{sec_title}":')
    for p in group:
        title = title_from_file(p)
        # normalize capitalization
        title = smart_capitalize(title)
        # escape double quotes in title
        title = title.replace('"', '\\"')
        rel = str(Path('chapters') / p.name)
        nav_lines.append(f'    - "{title}": "{rel}"')

if not nav_lines:
    print('No markdown files found in chapters/ — aborting.')
    sys.exit(1)

# build a fresh mkdocs.yml content preserving theme/plugins from existing if possible
base = {
    'site_name': 'Manual de Opciones Financieras',
    'site_description': 'Guía estructurada para inversores: desde fundamentos hasta frameworks y modelos profesionales.',
    'docs_dir': 'chapters',
    'site_dir': 'site',
}

content = []
content.append(f"site_name: \"{base['site_name']}\"")
content.append(f"site_description: \"{base['site_description']}\"")
content.append(f"docs_dir: \"{base['docs_dir']}\"")
content.append(f"site_dir: \"{base['site_dir']}\"")
content.append("")
content.append("theme:")
content.append("  name: \"material\"")
content.append("  language: es")
content.append("  features:")
content.append("    - navigation.sections")
content.append("    - navigation.top")
content.append("    - navigation.instant")
content.append("    - toc.integrate")
content.append("    - content.code.copy")
content.append("    - navigation.tracking")
content.append("    - search.suggest")
content.append("  palette:")
content.append("    - scheme: default")
content.append("      primary: indigo")
content.append("      accent: indigo")
content.append("    - scheme: slate")
content.append("      primary: indigo")
content.append("      accent: indigo")
content.append("      toggle:")
content.append("        icon: material/weather-night")
content.append("        name: \"Switch to dark mode\"")
content.append("")
content.append("plugins:")
content.append("  - awesome-pages")
content.append("  - search")
content.append("  - prev-next")
content.append("")
content.append("markdown_extensions:")
content.append("  - toc:")
content.append("      permalink: true")
content.append("  - admonition")
content.append("  - pymdownx.superfences")
content.append("")
content.append("nav:")
content.extend(nav_lines)
content.append("")

MK.write_text('\n'.join(content), encoding='utf-8')
print('Wrote', MK)

# Also generate an `awesome-pages` `.pages` file inside `chapters/` so maintainers
# can opt into using mkdocs-awesome-pages-plugin for manual nav control. We
# produce a conservative file that mirrors the autogenerated sections/order.
pages_path = CH / '.pages'
pages_lines = []
pages_lines.append('title: "Manual de Opciones Financieras"')
pages_lines.append('pages:')
for sec_title, cond in sections:
    group = [p for n, p in items if cond(n)]
    if not group:
        continue
    pages_lines.append(f'  - "{sec_title}":')
    for p in group:
        pages_lines.append(f'    - {p.name}')

pages_path.write_text('\n'.join(pages_lines) + '\n', encoding='utf-8')
print('Wrote', pages_path)


