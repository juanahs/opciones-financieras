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

## Configuración de Pages

En **Settings > Pages**, selecciona **GitHub Actions** como fuente de despliegue. El workflow necesita los permisos `pages: write` e `id-token: write`, ya incluidos en su configuración.

No edites ni abras los archivos Markdown directamente desde la URL publicada: MkDocs los convierte en páginas HTML y reescribe sus enlaces, anchors, assets y navegación para el subpath `/opciones-financieras/`.
