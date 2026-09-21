# Manual de Opciones Financieras

Guía práctica y estructurada para inversores interesados en el uso profesional de opciones sobre acciones. Cubre desde fundamentos teóricos hasta estrategias, gestión de riesgo, modelos operativos y casos prácticos.

## Objetivo

Proveer a inversores con experiencia en acciones (swing traders y gestores discretos) de una referencia completa sobre:

- Fundamentos de las opciones (contratos, greeks, volatilidad)
- Estrategias básicas y avanzadas (calls, puts, spreads, straddles, condors, etc.)
- Modelos operativos y checklists para ejecución y gestión de operaciones
- Frameworks profesionales para selección de strike, vencimiento y gestión de cartera
- Casos prácticos aplicados a empresas reales y consideraciones fiscales

## Público objetivo

Inversores con conocimientos básicos/intermedios de mercados y estructuras técnicas que desean aplicar opciones para mejorar la relación rentabilidad/riesgo de sus carteras.

## Cómo usar este manual

- Abre `index.html` en el directorio raíz para acceder al índice estático ordenado por capítulo.
- Leer en orden recomendado: Introducción → Fundamentos → Estrategias → Modelos Profesionales → Checklists y Anexos.
- Buscar estudios de caso en la sección profesional para ver ejemplos aplicados.

## Estructura resumida

1) Introducción y Fundamentos (Capítulos 0–9)
  - Contexto, contratos, greeks y volatilidad.

2) Estrategias y prácticas operativas (Capítulos 10–99)
  - Spreads, sintéticos, collars, wheel, cash-secured put, covered call, gestión de posiciones, rolls, assignment.

3) Nivel profesional y frameworks (Capítulos 100–199)
  - Arquitecturas de estrategia, modelos operativos por estrategia, análisis avanzado de option chains y gestión profesional del capital.

4) Checklists, glosario y anexos (Capítulos 200+)
  - Checklists por estrategia, glosario A–Z, estudios de caso y consideraciones fiscales.

## Ejemplos de capítulos clave

- `chapters/00-introduccion.md` — Introducción
- `chapters/06-greeks.md` — Greeks en la práctica
- `chapters/126-checklist-profesional-completo.md` — Checklist profesional (niveles)
- `chapters/181-apple-caso-completo.md` — Caso práctico: Apple
- `chapters/211-glosario-profesional.md` — Glosario A–Z

## Mantenimiento

- Para regenerar el índice estático después de editar o añadir capítulos: `python3 scripts/generate_index.py` (ejecutar desde `opciones-financieras-main/`).

## Aviso legal

Material con fines educativos y técnicos. No constituye asesoramiento financiero.
