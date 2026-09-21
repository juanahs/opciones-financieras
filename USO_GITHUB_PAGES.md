# Uso de GitHub Pages

El sitio publicado es:

<https://juanahs.github.io/opciones-financieras/>

## Arquitectura

- `mkdocs.yml` configura Material for MkDocs, `docs_dir: chapters` y `site_url`.
- `chapters/.pages` define las cuatro secciones y todos los capítulos activos.
- `requirements.txt` contiene MkDocs, Material y `mkdocs-awesome-pages-plugin`.
- `.github/workflows/deploy.yml` construye y publica `site/` con GitHub Pages.

## Validación local

```bash
python3 -m pip install -r requirements.txt
python3 -m mkdocs build --clean --strict
```

Para previsualizar cambios:

```bash
python3 -m mkdocs serve
```

## Añadir un capítulo nuevo

Para incorporar un nuevo Markdown a la estructura:

1. Crea `chapters/<numero>-<slug>.md`, usando un número que mantenga la secuencia.
2. Incluye front matter con `title` y un primer H1 idénticos, por ejemplo `Capítulo 253 — Nuevo Capítulo`.
3. Añade el archivo en la sección correspondiente de `chapters/.pages`. Las opciones `sort_type: natural` y `order_by: filename` mantienen el orden `10, 11, ..., 99, 100`.
4. Usa enlaces relativos a `chapters/`; no antepongas `chapters/` en los enlaces entre capítulos.
5. Ejecuta `python3 -m mkdocs build --clean --strict` antes de subir los cambios.

El workflow detecta el nuevo archivo en el siguiente push y lo publica automáticamente junto con la navegación, la búsqueda, el TOC y los enlaces anterior/siguiente.

## Configuración de Pages

En **Settings > Pages**, selecciona **GitHub Actions** como fuente de despliegue. El workflow necesita los permisos `pages: write` e `id-token: write`, ya incluidos en su configuración.

No edites ni abras los archivos Markdown directamente desde la URL publicada: MkDocs los convierte en páginas HTML y reescribe sus enlaces, anchors, assets y navegación para el subpath `/opciones-financieras/`.
