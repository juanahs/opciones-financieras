---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 6"

---

# Capítulo 6 — Capítulo 6

# Las Greeks

---

## Introducción

Las Greeks son el lenguaje de los operadores profesionales.

Mientras muchos inversores observan únicamente el beneficio o la pérdida de una opción, un gestor analiza primero cómo cambiará esa posición cuando cambie el mercado.

Las Greeks permiten cuantificar esas variaciones.

No predicen el futuro.

Describen la sensibilidad de una posición frente a distintos factores.

---

## Objetivos

Al finalizar este capítulo el lector será capaz de interpretar:

- Delta
- Gamma
- Theta
- Vega
- Rho

desde un punto de vista práctico.

---

# La filosofía correcta

Muchos libros presentan las Greeks como fórmulas matemáticas.

Ese enfoque rara vez ayuda a tomar mejores decisiones.

En este libro responderemos siempre a una única pregunta.

> ¿Qué ocurrirá con mi posición si cambia una variable concreta?

---

# Las cinco variables principales

```
Precio

↓

Delta

---------------------

Tiempo

↓

Theta

---------------------

Volatilidad

↓

Vega

---------------------

Movimiento de Delta

↓

Gamma

---------------------

Tipos de interés

↓

Rho
```

---

# Delta

Delta mide cuánto cambiará aproximadamente el precio de la opción cuando el subyacente se mueva una unidad.

Ejemplo.

```
Delta

0,70

```

Si la acción sube:

1 €

La opción aumentará aproximadamente:

0,70 €

---

## Interpretación práctica

Una Delta de:

0,80

significa que el contrato se comporta aproximadamente como:

80 acciones.

No es una definición.

Es una equivalencia económica.

---

# Gamma

Gamma mide la velocidad con la que cambia Delta.

```
Precio sube

↓

Delta aumenta

↓

La Call responde cada vez más como una acción
```

Gamma elevada implica cambios rápidos en el riesgo.

---

# Theta

Theta representa el efecto del paso del tiempo.

```
Cada día

↓

La opción pierde parte de su valor temporal.
```

Para el comprador:

Theta es una fuerza en contra.

Para el vendedor:

Theta trabaja a su favor.

---

# Vega

Vega mide la sensibilidad frente a cambios en la volatilidad implícita.

```
Aumenta IV

↓

Sube el precio de muchas opciones.

------------------------

Disminuye IV

↓

Baja el precio.
```

Por ello resulta tan importante evitar comprar opciones extremadamente caras.

---

# Rho

Rho mide el impacto de los tipos de interés.

En la mayoría de operaciones de Swing Trading su influencia será muy inferior a Delta, Theta o Vega.

---

# Resumen comparativo

| Greek | Variable | Comprador | Vendedor |
|---------|----------|-----------|-----------|
| Delta | Precio | Muy importante | Muy importante |
| Gamma | Cambio de Delta | Alta | Alta |
| Theta | Tiempo | Negativa | Positiva |
| Vega | Volatilidad | Positiva | Negativa |
| Rho | Tipos | Baja | Baja |

---

# Regla práctica

Antes de abrir cualquier posición pregúntese:

- ¿Qué ocurrirá si el precio no se mueve?
- ¿Qué ocurrirá si aumenta la volatilidad?
- ¿Qué ocurrirá si desaparece la volatilidad?
- ¿Qué ocurrirá dentro de veinte días?

Las respuestas a estas preguntas son mucho más importantes que memorizar definiciones.

---

# Próximo capítulo

El siguiente capítulo estudiará en profundidad la Volatilidad Implícita.

Una vez comprendidas Delta y Theta, la volatilidad será el elemento que permitirá seleccionar correctamente la mayoría de estrategias con opciones.
