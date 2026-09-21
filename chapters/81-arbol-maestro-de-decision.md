---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 81 — Árbol Maestro de Decisión"

---

# Capítulo 81 — Árbol Maestro de Decisión



---

# Introducción

Este árbol resume la filosofía completa del libro.

Debe responderse de arriba abajo.

Nunca saltando pasos.

---

# Árbol principal

```
¿Existe tendencia?

│

├── NO

│      │

│      ├── Esperar

│      │

│      └── No operar

│

└── SÍ

        │

        ├── ¿Existe soporte?

        │

        ├── ¿Existe confirmación?

        │

        ├── ¿IV alta?

        │          │

        │          ├── Sí

        │          │      │

        │          │      ├── Cash Secured Put

        │          │      ├── Covered Call

        │          │      └── Bull Put Spread

        │          │

        │          └── No

        │

        │                 ├── Compra acciones

        │                 ├── LEAPS

        │                 └── Bull Call Spread

        │

        └── Definir gestión
```

---

# Segundo árbol

```
¿Poseo acciones?

│

├── Sí

│      │

│      ├── ¿Quiero venderlas?

│      │

│      ├── Sí

│      │       │

│      │       └── Covered Call

│      │

│      └── No

│

└── No

        │

        ├── ¿Quiero comprarlas?

        │

        ├── Sí

        │      │

        │      ├── Compra directa

        │      ├── Cash Secured Put

        │      └── LEAPS

        │

        └── Esperar
```

---

# Conclusión

Todo el proceso puede resumirse en una idea:

**Primero analizar el mercado. Después seleccionar la estrategia. Nunca al contrario.**
