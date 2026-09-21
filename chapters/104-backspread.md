---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 104 — Backspread"

---

# Capítulo 104 — Backspread



---

# Introducción

El Backspread representa, conceptualmente, la estrategia opuesta al Ratio Spread.

Mientras el Ratio Spread suele beneficiarse de movimientos moderados, el Backspread busca capturar movimientos extraordinariamente intensos.

Por ello suele utilizarse cuando el gestor espera un incremento significativo de la volatilidad o una ruptura importante.

---

# Estructura

Ejemplo con Calls.

```
Vender

1 Call

↓

Comprar

2 Calls

↓

Strike superior
```

---

# Objetivo

Beneficiarse de un movimiento alcista muy intenso limitando parcialmente el coste inicial.

---

# Escenarios adecuados

- ruptura de resistencia histórica;
- expansión de volatilidad;
- eventos con potencial de movimiento extraordinario.

---

# Escenarios poco adecuados

- mercados laterales;
- baja volatilidad persistente;
- movimientos reducidos.

---

# Ventajas

- potencial alcista muy elevado;
- riesgo definido en muchas configuraciones;
- Vega positiva.

---

# Inconvenientes

- zona intermedia desfavorable;
- complejidad;
- sensibilidad temporal.

---

# Greeks

| Greek | Comportamiento |
|--------|----------------|
| Delta | Positiva creciente |
| Gamma | Muy positiva |
| Theta | Habitualmente negativa |
| Vega | Positiva |

---

# Integración con análisis técnico

```
Gran base

↓

SOS

↓

Ruptura histórica

↓

Backspread
```

---

# Checklist

□ Posible ruptura.

□ Catalizador identificado.

□ Riesgo conocido.

□ Liquidez suficiente.

---

# Conclusión

El Backspread constituye una herramienta especializada para escenarios excepcionales donde el gestor espera movimientos considerablemente superiores a los descontados por el mercado.
