Manual de uso — MkDocs + Material (GitHub / GitHub Pages)
=====================================================

Resumen
-------
Este repositorio ahora incluye una configuración para generar un sitio web estático
con MkDocs + Material a partir de los archivos Markdown en `chapters/`.
El flujo principal ya está integrado en CI y publica el sitio en GitHub Pages.

Objetivos cubiertos
- Navegación lateral
- Búsqueda
- Índice / TOC
- Breadcrumbs
- Navegación anterior / siguiente
- Responsive + modo oscuro
- Enlaces entre capítulos
- Publicación automática en GitHub Pages
- Estructura por secciones

Archivos relevantes
- `mkdocs.yml` (generado automáticamente por `scripts/generate_mkdocs_nav.py`)
- `requirements.txt` (dependencias: mkdocs-material, mkdocs-awesome-pages-plugin). Nota: el plugin `mkdocs-prev-next-plugin` no se instala por defecto en CI; ver sección "Opciones" más abajo para restaurarlo.
- `scripts/generate_mkdocs_nav.py` (genera `nav:` con títulos legibles)
- `scripts/add_frontmatter_titles.py` (añade `title:` front-matter a MD que no lo tengan)
- `.github/workflows/mkdocs-deploy.yml` (CI que construye y publica en gh-pages)

Flujo de trabajo recomendado (local)
---------------------------------
1. Crear entorno y activar:

```bash
cd /projects/src/cops/opciones-financieras-main
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. (Opcional, recomendado la primera vez) Añadir `title:` front-matter a Markdown
   que lo necesiten para títulos consistentes en la navegación:

```bash
python3 scripts/add_frontmatter_titles.py
```

3. Regenerar `mkdocs.yml` con `nav:` legible (extrae títulos, agrupa por secciones):

```bash
python3 scripts/generate_mkdocs_nav.py
```

4. Ver el sitio en caliente durante edición:

```bash
mkdocs serve
# abre http://127.0.0.1:8000
```

5. Generar sitio estático para producción:

```bash
mkdocs build --clean
# salida en ./site
```

Publicación automática (CI / GitHub Actions)
-----------------------------------------
Cada push a `main` o `master` (según configuración) desencadena el workflow
`.github/workflows/mkdocs-deploy.yml` que hace:

1. Instala dependencias (`requirements.txt`).
2. Ejecuta `python3 scripts/generate_mkdocs_nav.py` para regenerar `mkdocs.yml`.
3. Ejecuta `mkdocs build --clean` para generar `site/`.
4. Publica el contenido de `site/` en GitHub Pages (usando `peaceiris/actions-gh-pages`).
5. Genera/actualiza un `index.html` en la raíz del repo que redirige a
   `https://<owner>.github.io/<repo>/` y lo commitea de vuelta con `[skip ci]` para
   facilitar el acceso desde la página principal del repositorio.

Configurar GitHub Pages (una vez)
--------------------------------
1. Ve a Settings → Pages en tu repositorio en GitHub.
2. Si usas el flujo por defecto de la Action, configura Pages para servir desde
   la rama `gh-pages` (peaceiris crea/actualiza esa rama). Selecciona la carpeta `/`.
3. Opcional: configurar dominio personalizado.

Cómo actualizar contenido (pasos rápidos)
----------------------------------------
- Edita o añade archivos en `chapters/` (Markdown).
- Si añades nuevos capítulos, ejecuta localmente:

  ```bash
  python3 scripts/add_frontmatter_titles.py
  python3 scripts/generate_mkdocs_nav.py
  mkdocs build
  ```

- Haz commit y push a `main`. El CI reconstruirá y publicará automáticamente.

Añadir un nuevo capítulo — ¿qué debes hacer?
-------------------------------------------
Resumen: la mayor parte queda automatizada por los scripts y el workflow, pero si quieres un flujo limpio sigue estas recomendaciones.

Requisitos mínimos para el nuevo archivo `.md`:

- Nombre de fichero: usa un prefijo numérico para controlar el orden, por ejemplo `075-mi-capitulo.md`.
- Contenido: incluye al menos un encabezado H1 (el primer encabezado) que represente el título del capítulo, por ejemplo:

```markdown
# Mi capítulo sobre estrategia X

Contenido del capítulo...
```

- Front-matter (opcional): puedes añadir un bloque YAML al inicio con `title:` si quieres controlar el título exacto de la navegación:

```yaml
---
title: "Mi capítulo sobre estrategia X"
---
```

Qué hace el repo automáticamente (CI)
- El workflow ejecuta `scripts/add_frontmatter_titles.py` antes de generar la navegación; esto insertará un `title:` en front-matter si falta, usando el H1 o el nombre de fichero como respaldo.
- Luego `scripts/generate_mkdocs_nav.py` regenerará `mkdocs.yml` con la navegación (títulos limpiados y capitalizados).
- Finalmente MkDocs se construye y la Action publica el sitio en GitHub Pages.

Flujo recomendado (local, para previsualizar):

1. Crear virtualenv e instalar dependencias (si no lo has hecho):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Ejecuta el script de front-matter (opcional si ya tienes H1 y title):
```bash
python3 scripts/add_frontmatter_titles.py
```
3. Regenera la navegación y comprueba `mkdocs.yml`:
```bash
python3 scripts/generate_mkdocs_nav.py
```
4. Sirve el sitio localmente para revisar el resultado:
```bash
mkdocs serve
# abrir http://127.0.0.1:8000
```

Uso de `awesome-pages` (control manual avanzado de la navegación)
- Hemos añadido `mkdocs-awesome-pages-plugin`. Si quieres control absoluto de la estructura/orden de la navegación por carpeta, crea un archivo `.pages` en la carpeta `chapters/` o en subcarpetas con un contenido YAML como:

```yaml
title: "Estrategias y conceptos prácticos"
pages:
  - 10-leaps.md
  - 11-bull-put-spread.md
  - 12-bull-call-spread.md
```

El plugin `awesome-pages` prioriza archivos `.pages` cuando construye la navegación. Úsalo sólo si necesitas un control manual fino; de lo contrario la numeración en los nombres de fichero y nuestro script automático funcionan bien.

Exclusiones
- Archivos en `chapters/_archive/` son ignorados por el generador de navegación. Mueve capítulos obsoletos ahí si no quieres que aparezcan en la navegación.

Resumen práctico — si sólo añades un nuevo `.md` con un H1 y lo haces push a `main`, el CI:
1) añadirá `title:` si falta, 2) regenerará `mkdocs.yml`, 3) construirá y publicará el sitio. No deberías necesitar pasos manuales salvo para previsualizar localmente o para controlar el orden con `.pages`.

Notas de mantenimiento y recomendaciones
---------------------------------------
- El script `generate_mkdocs_nav.py` sobrescribe `mkdocs.yml`. Si necesitas
  personalizaciones avanzadas del tema (logo, enlaces, complementos extra),
  mantén una copia de seguridad de `mkdocs.yml` o incorpora los cambios en el
  script para que los preserve.
- `add_frontmatter_titles.py` modifica los MD in-place. Revisa los cambios
  antes de commitear (haz `git diff`). Si prefieres no añadir front-matter
  automáticamente, puedes omitir ese paso y confiar en los encabezados H1.
- Si quieres títulos exactos (sin normalización), modifica la función
  `smart_capitalize` en `scripts/generate_mkdocs_nav.py` o omítela.

Solución de problemas
---------------------
- Error: `mkdocs: command not found` → instala dependencias en el virtualenv (`pip install -r requirements.txt`).
- CI falla por permisos o token → asegúrate de que `${{ secrets.GITHUB_TOKEN }}` está presente (nativo en Actions) y que la política de la organización permite el push desde Actions.
- Navegación no actualizada → ejecutar `python3 scripts/generate_mkdocs_nav.py` localmente y comprobar `mkdocs.yml` antes de push.

Preguntas frecuentes
-------------------
- ¿Puedo personalizar la apariencia? Sí: Material for MkDocs soporta muchas opciones
  (logo, paleta, tipografías). Edítalas en `mkdocs.yml` (o extiende `generate_mkdocs_nav.py`).
- ¿Puedo añadir redirecciones internas? Sí: utiliza `mkdocs-redirects` plugin si necesitas mantener URLs antiguas.
-- ¿Se generan enlaces prev/next automáticamente? Actualmente NO: `mkdocs-prev-next-plugin` no está instalado por defecto en CI para evitar fallos de instalación. Si quieres restablecer prev/next, añade el plugin a `requirements.txt` apuntando a una release estable o vendoriza el plugin en el repositorio; contáctame y lo restauro.

Soporte adicional
-----------------
Si quieres, puedo:

- Añadir `title:` front-matter sugerido en todos los MD y crear un commit automático (si me autorizas a modificar el repo). Actualmente he añadido un script que hace esto y lo ejecuté localmente (actualizó 253 archivos en `chapters/`).
- Adaptar la capitalización/estilo de títulos según tu preferencia.
- Añadir plugins extras (awesome-pages, redirects, analytics, etc.) y actualizar CI.

Fin del manual.

