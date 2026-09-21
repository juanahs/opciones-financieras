---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 41 — Vega en la práctica"

---

# Capítulo 41 — Vega en la práctica



---

# Introducción

Después de Delta y Theta, Vega suele ser la Greek que más impacto tiene sobre una cartera de opciones de medio y largo plazo.

Sin embargo, también es una de las menos comprendidas.

Muchos operadores atribuyen a la dirección del precio variaciones que, en realidad, proceden de cambios en la volatilidad implícita.

---

# Qué mide Vega

Vega estima cuánto cambiará el precio de una opción cuando la volatilidad implícita varía un punto porcentual.

Ejemplo.

```
Vega

0,25
```

Si la IV aumenta un punto:

```
Prima

+

0,25 $
```

Aproximadamente.

---

# Vega positiva

Las estrategias compradoras suelen beneficiarse de aumentos de IV.

Ejemplos.

- Long Call.
- Long Put.
- LEAPS.
- Protective Put.

---

# Vega negativa

Las estrategias vendedoras suelen verse perjudicadas por aumentos de IV.

Ejemplos.

- Covered Call.
- Cash Secured Put.
- Iron Condor.
- Bull Put Spread.

---

# Ejemplo práctico

Imagine una LEAPS sobre Microsoft.

La acción apenas se mueve.

Sin embargo:

```
IV

25 %

↓

35 %
```

La opción puede aumentar de valor únicamente por el incremento de incertidumbre.

---

# Vega y vencimiento

Las opciones de vencimiento lejano suelen presentar una Vega superior.

Por ello las LEAPS son especialmente sensibles a cambios de volatilidad.

---

# Vega y Swing Trading

Cuando el análisis técnico anticipa una ruptura importante desde una fase de compresión:

- el movimiento direccional;
- y la posible expansión de IV

pueden trabajar simultáneamente a favor de una Long Call o una LEAPS.

---

# Conclusión

Comprender Vega permite explicar por qué una opción puede ganar o perder valor incluso cuando el precio apenas ha cambiado.
