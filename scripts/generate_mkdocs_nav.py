"""
Minimal safe mkdocs nav generator (NO-OP)

This repository previously contained an automated nav generator that
also injected the `prev-next` plugin into `mkdocs.yml`. That plugin
caused CI installation failures in some runners and was removed from
`requirements.txt` and `mkdocs.yml`.

To avoid unintentionally reintroducing the plugin, this script is a
safe no-op: it prints an informational message and leaves the committed
`mkdocs.yml` unchanged. If you want to re-enable automatic nav
generation, restore a prior version of this script that builds `nav:`
from `chapters/` and remove the NO-OP behavior.
"""

import sys
from pathlib import Path

print("generate_mkdocs_nav.py: no-op generator (mkdocs.yml is committed).")
print("If you need to regenerate mkdocs.yml from chapters/, restore the full generator.")
sys.exit(0)
