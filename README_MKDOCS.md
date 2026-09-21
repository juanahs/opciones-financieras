# Sitio MkDocs

El manual se genera con MkDocs Material desde `chapters/`.

## Desarrollo local

```bash
python3 -m pip install -r requirements.txt
python3 -m mkdocs serve
```

La navegación se mantiene en `chapters/.pages`; sus rutas son relativas a `docs_dir: chapters`.

## Validación

```bash
python3 -m mkdocs build --clean --strict
```

La construcción genera `site/index.html`, la búsqueda, el TOC y los enlaces anterior/siguiente.

## Publicación

El workflow `.github/workflows/deploy.yml` instala las dependencias, ejecuta la construcción estricta y publica `site/` mediante GitHub Pages. En la configuración del repositorio, Pages debe usar **GitHub Actions** como fuente de despliegue.
