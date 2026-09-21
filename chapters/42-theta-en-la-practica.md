---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 42"

---

# Capítulo 42 — Capítulo 42

# Theta en la práctica

---

# Introducción

Si Delta responde a la pregunta:

> ¿Qué ocurre si cambia el precio?

Theta responde a otra igualmente importante:

> ¿Qué ocurre si no sucede absolutamente nada?

En el mercado de acciones, el paso del tiempo no modifica el valor de una acción.

En el mercado de opciones ocurre exactamente lo contrario.

El tiempo es un activo que se consume.

Y ese consumo tiene un precio.

---

# Objetivos

Al finalizar este capítulo el lector será capaz de:

- Comprender cómo actúa Theta.
- Interpretar su evolución.
- Identificar qué estrategias se benefician del tiempo.
- Integrar Theta dentro de una cartera de Swing Trading.

---

# ¿Qué es Theta?

Theta mide la pérdida de valor temporal de una opción por el simple transcurso del tiempo.

Todo lo demás constante:

```
Hoy

↓

Prima

5,00 €

↓

Mañana

↓

Prima

4,96 €
```

La diferencia aproximada corresponde al efecto de Theta.

---

# El tiempo nunca se detiene

Mientras el mercado permanece abierto o cerrado:

- pasan los días;
- se acerca el vencimiento;
- disminuye el valor temporal.

Este fenómeno afecta a todas las opciones.

La diferencia reside en quién soporta ese coste.

---

# Theta positiva

Las estrategias vendedoras suelen presentar Theta positiva.

Ejemplos:

- Covered Call.
- Cash Secured Put.
- Bull Put Spread.
- Bear Call Spread.
- Iron Condor.

Cada día que transcurre sin grandes cambios suele favorecer estas posiciones.

---

# Theta negativa

Las estrategias compradoras suelen presentar Theta negativa.

Ejemplos:

- Long Call.
- Long Put.
- LEAPS.
- Protective Put.

Necesitan que el mercado se mueva antes de que el tiempo erosione la prima.

---

# Theta no es constante

El deterioro temporal acelera conforme se aproxima el vencimiento.

Representación simplificada:

```
Valor temporal

^

|

|\
| \
|  \
|   \
|    \_____

+---------------->

Tiempo
```

Los últimos días concentran gran parte de la pérdida temporal.

---

# Theta y el vencimiento

Opciones muy lejanas:

- Theta reducida.

Opciones cercanas:

- Theta elevada.

Por ello las LEAPS pierden valor temporal mucho más lentamente que las opciones semanales.

---

# Theta y Swing Trading

Una estructura técnica puede tardar semanas en desarrollarse.

Comprar una opción con apenas unos días hasta vencimiento introduce un enemigo adicional:

```
El tiempo.
```

La hipótesis técnica puede ser correcta.

Pero la opción perder valor antes de que el movimiento ocurra.

---

# Error habitual

Elegir vencimientos extremadamente cortos únicamente porque la prima parece barata.

En realidad:

```
Prima baja

↓

Theta muy elevada

↓

Menor margen temporal
```

---

# Checklist

□ Horizonte temporal definido.

□ Theta compatible con la estrategia.

□ El vencimiento concede tiempo suficiente.

□ Comprendo quién gana con el paso del tiempo.

---

# Conclusión

Theta no es un enemigo ni un aliado.

Es un coste que unas estrategias pagan y otras cobran.

La clave consiste en elegir conscientemente en qué lado desea situarse.
