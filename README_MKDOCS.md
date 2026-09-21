# Sitio MkDocs

El manual se genera con MkDocs Material desde `chapters/`.

## Desarrollo local

```bash
python3 -m pip install -r requirements.txt
python3 -m mkdocs serve
```

La navegación se mantiene en `chapters/.pages`; sus rutas son relativas a `docs_dir: chapters`.

## Añadir un capítulo

1. Crea el archivo directamente dentro de `chapters/` con un prefijo numérico que mantenga el orden. Por ejemplo: `253-nuevo-capitulo.md`.
2. Añade front matter válido y haz que `title` coincida con el primer H1. El título visible debe conservar el número del capítulo:

```markdown
---
title: "Capítulo 253 — Nuevo Capítulo"
description: "Descripción breve y específica del capítulo."
date: 2026-09-21
tags: []
draft: false
---

# Capítulo 253 — Nuevo Capítulo
```

3. Escribe el contenido debajo del H1. No uses `chapters/` en los enlaces internos: desde otro capítulo, enlaza por ejemplo a `[Fundamentos](02-fundamentos.md)`.
4. Añade el nombre exacto del archivo en `chapters/.pages`, dentro de la sección que corresponda al contenido. El archivo `.pages` ya usa orden natural por nombre, por lo que `253-...` quedará después de `252-...`.
5. Comprueba que no estás duplicando un capítulo archivado en `chapters/_archive/`.
6. Valida y previsualiza el resultado:

```bash
python3 -m mkdocs build --clean --strict
python3 -m mkdocs serve
```

Si el capítulo no se añade a `chapters/.pages`, MkDocs puede generarlo como archivo de documentación pero no aparecerá en la navegación organizada. Si el `title` y el H1 no coinciden, el menú y la página pueden mostrar nombres distintos.

## Validación

```bash
python3 -m mkdocs build --clean --strict
```

La construcción genera `site/index.html`, la búsqueda, el TOC y los enlaces anterior/siguiente.

## Publicación

El workflow `.github/workflows/deploy.yml` instala las dependencias, ejecuta la construcción estricta y publica `site/` mediante GitHub Pages. En la configuración del repositorio, Pages debe usar **GitHub Actions** como fuente de despliegue.
