---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 26"

---

# Capítulo 26 — Capítulo 26

# Cómo leer una Option Chain

---

# Introducción

Una cadena de opciones (Option Chain) es la herramienta de trabajo más importante de cualquier operador de opciones.

Sin embargo, para un inversor acostumbrado únicamente a comprar acciones, puede resultar intimidante.

Decenas de vencimientos.

Cientos de Strikes.

Múltiples columnas.

Bid.

Ask.

Volumen.

Open Interest.

Greeks.

IV.

Aprender a leer correctamente esta información permite transformar una larga lista de números en una representación del riesgo descontado por el mercado.

---

# Objetivos

Al finalizar este capítulo el lector será capaz de:

- Interpretar una cadena de opciones.
- Seleccionar contratos líquidos.
- Detectar spreads excesivos.
- Analizar Open Interest.
- Evitar errores frecuentes.

---

# Estructura general

Una cadena suele organizarse así:

```
CALLS

Bid

Ask

Vol

OI

IV

Strike

IV

OI

Vol

Bid

Ask

PUTS
```

Las Calls aparecen a la izquierda.

Las Puts a la derecha.

El Strike ocupa el centro.

---

# Bid

El Bid representa:

> El mejor precio que alguien está dispuesto a pagar.

Si vende una opción inmediatamente, normalmente recibirá un precio cercano al Bid.

---

# Ask

El Ask representa:

> El mejor precio al que alguien está dispuesto a vender.

Si compra inmediatamente, normalmente pagará un precio próximo al Ask.

---

# Spread

La diferencia entre Bid y Ask recibe el nombre de:

Spread.

Ejemplo.

```
Bid

3,90

Ask

4,10

Spread

0,20
```

Cuanto menor sea:

mejor.

---

# Regla práctica

| Spread | Calidad |
|----------|----------|
| Muy pequeño | Excelente |
| Moderado | Aceptable |
| Muy amplio | Evitar salvo necesidad |

---

# Volumen

El volumen indica cuántos contratos se han negociado durante la sesión.

No debe confundirse con el Open Interest.

---

# Open Interest

El Open Interest representa:

> El número de contratos actualmente abiertos.

```
Open Interest

5000

↓

Gran liquidez
```

```
Open Interest

5

↓

Liquidez muy reducida
```

---

# Liquidez

Una buena liquidez implica:

- ejecución más sencilla;
- menor deslizamiento;
- spreads reducidos;
- facilidad para hacer rolls.

---

# Volatilidad Implícita

La mayoría de plataformas muestran la IV correspondiente a cada Strike.

Esta información permite detectar:

- opciones caras;
- opciones relativamente baratas;
- skew de volatilidad.

---

# Greeks

Las plataformas modernas incorporan normalmente:

- Delta
- Gamma
- Theta
- Vega

No es necesario memorizar cada número.

Lo importante es comprender cómo cambia el riesgo al seleccionar distintos Strikes.

---

# Ejemplo

```
Strike

100

Delta

0,80

Theta

-0,03

IV

28 %

OI

12.500
```

Un operador profesional obtiene inmediatamente varias conclusiones:

- opción líquida;
- elevada sensibilidad al precio;
- volatilidad moderada;
- deterioro temporal reducido.

---

# Checklist

□ Spread reducido.

□ Open Interest elevado.

□ Buen volumen.

□ Delta adecuada.

□ IV coherente.

□ Vencimiento correcto.

---

# Conclusión

Una Option Chain no es simplemente una tabla de precios.

Es un mapa completo del riesgo descontado por el mercado.

Aprender a interpretarla correctamente constituye una ventaja competitiva para cualquier inversor.
