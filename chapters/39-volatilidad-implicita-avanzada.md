---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 39 — Volatilidad Implícita Avanzada"

---

# Capítulo 39 — Volatilidad Implícita Avanzada



---

# Introducción

La volatilidad implícita (IV) constituye el principal factor diferenciador entre invertir en acciones e invertir utilizando opciones.

Un inversor en acciones necesita responder principalmente a dos preguntas:

- ¿En qué dirección se moverá el precio?
- ¿Cuándo podría producirse ese movimiento?

El operador de opciones debe añadir una tercera cuestión:

> ¿Está cara o barata la incertidumbre que estoy comprando o vendiendo?

Esta pregunta condiciona la elección de prácticamente todas las estrategias descritas en este manual.

---

# Objetivos

Al finalizar este capítulo el lector será capaz de:

- Interpretar correctamente la IV.
- Compararla con su histórico.
- Comprender la expansión y contracción de volatilidad.
- Incorporar la IV en la toma de decisiones.

---

# Qué representa realmente la IV

La IV no mide el movimiento real.

Mide el movimiento esperado por el mercado.

Es una expectativa.

No una predicción.

Dos acciones con el mismo precio pueden presentar volatilidades implícitas completamente distintas porque el mercado anticipa riesgos diferentes.

---

# Ejemplo

Empresa A

```
Precio

100 €

IV

18 %
```

Empresa B

```
Precio

100 €

IV

62 %
```

Ambas cotizan exactamente al mismo precio.

Sin embargo, el mercado espera movimientos mucho mayores en la segunda.

---

# La IV no indica dirección

Una IV elevada no significa:

- que el precio vaya a subir;
- ni que vaya a bajar.

Únicamente indica que el mercado espera movimientos importantes.

Estos movimientos pueden producirse en cualquiera de las dos direcciones.

---

# Expansión de volatilidad

```
IV

20 %

↓

35 %

↓

60 %
```

Las primas aumentan incluso aunque el precio apenas cambie.

Esto beneficia principalmente a:

- compradores anteriores;
- posiciones con Vega positiva.

---

# Contracción de volatilidad

```
IV

70 %

↓

40 %

↓

25 %
```

Las primas disminuyen.

Aunque la acción permanezca prácticamente inmóvil.

Este fenómeno sorprende con frecuencia a los principiantes.

---

# Volatilidad antes de resultados

Un patrón habitual es:

```
Presentación de resultados

↓

Aumenta incertidumbre

↓

Sube la IV

↓

Publicación

↓

Desaparece incertidumbre

↓

Cae la IV
```

Esta caída recibe el nombre de:

**IV Crush**.

---

# Estrategias favorecidas

## IV elevada

Generalmente favorece:

- Covered Call.
- Cash Secured Put.
- Bull Put Spread.
- Bear Call Spread.
- Iron Condor.

Porque las primas son relativamente elevadas.

---

## IV reducida

Generalmente favorece:

- Long Call.
- Long Put.
- LEAPS.
- Bull Call Spread.
- Bear Put Spread.

Porque comprar opciones resulta relativamente más barato.

---

# Error habitual

Muchos inversores observan una prima muy elevada y concluyen:

```
Gran prima

↓

Gran oportunidad
```

En realidad suele significar:

```
Gran incertidumbre

↓

Mayor riesgo esperado
```

---

# Integración con Swing Trading

Supongamos un Spring confirmado en Wyckoff.

Existen dos posibilidades:

```
IV Baja

↓

Comprar LEAPS

puede ser razonable

-------------------------

IV Muy Alta

↓

Bull Put Spread

o

esperar estabilización
```

La estructura técnica sigue siendo alcista.

Sin embargo, la estrategia óptima puede cambiar completamente debido a la volatilidad.

---

# Conclusión

La dirección del precio explica una parte del comportamiento de una opción.

La volatilidad implícita explica la otra.

Ignorar cualquiera de las dos conduce a decisiones incompletas.
