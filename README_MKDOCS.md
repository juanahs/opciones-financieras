# MkDocs site (Manual de Opciones Financieras)

Este repositorio contiene los capítulos en `chapters/` y ahora está preparado para generar
un sitio estático utilizando MkDocs + Material for MkDocs.

Instrucciones rápidas (local):

1. Crear un virtualenv e instalar dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Generar y servir localmente (modo desarrollo):

```bash
mkdocs serve
```

Abre http://127.0.0.1:8000 para ver el sitio. MkDocs detecta cambios en `chapters/` y los recarga.

3. Construir sitio estático:

```bash
mkdocs build
```

El sitio se generará en `site/`.

Despliegue automático:

Se incluye un GitHub Action (`.github/workflows/mkdocs-deploy.yml`) que construye y publica
el contenido de `site/` en GitHub Pages al hacer push a `main` o `master`. El Action usa
`${{ secrets.GITHUB_TOKEN }}` integrado y no requiere configuración extra para repositorios
públicos; para repositorios privados revisa la política de tu organización.

Notas y opciones siguientes (puedo implementarlas si quieres):

- Generar automáticamente una sección `nav:` en `mkdocs.yml` con títulos legibles (extraídos
  del primer encabezado `#` de cada Markdown). Eso mejora la navegación (en vez de mostrar
  el nombre de fichero).
- Eliminar los prefijos numéricos del texto de enlace en el índice HTML o al construir la
  navegación de MkDocs.
- Añadir plantillas y estilos personalizados para adaptar el aspecto del tema Material.

Si quieres, implemento la generación automática de `nav:` con títulos extraídos y/o una
conversión del `index.html` actual para redirigir a la versión de MkDocs.

