---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 7 — Volatilidad Implícita"

---

# Capítulo 7 — Volatilidad Implícita



---

## Introducción

La mayoría de inversores creen que las opciones se encarecen porque la acción sube.

No es cierto.

En numerosas ocasiones una opción puede perder dinero incluso acertando la dirección del mercado.

La explicación suele encontrarse en la volatilidad implícita.

Comprender este concepto supone uno de los mayores saltos de nivel para cualquier inversor en opciones.

La volatilidad determina:

- el precio de las primas;
- la conveniencia de comprar o vender opciones;
- la estrategia óptima;
- la probabilidad implícita descontada por el mercado.

Por este motivo, ningún gestor profesional abre una posición sin evaluar previamente la volatilidad.

---

## Objetivos

Al finalizar este capítulo el lector será capaz de:

- Diferenciar volatilidad histórica e implícita.
- Interpretar IV Rank e IV Percentile.
- Entender cuándo comprar opciones.
- Entender cuándo vender opciones.
- Evaluar el efecto de los resultados empresariales sobre las primas.

---

# ¿Qué es la volatilidad?

La volatilidad mide la intensidad con la que varía el precio de un activo.

No indica dirección.

No dice si el mercado subirá.

No dice si caerá.

Únicamente mide cuánto espera el mercado que se mueva.

```
Poca volatilidad

───────────────

Mucho movimiento

≈ inexistente

-------------------------

Alta volatilidad

/\/\/\/\/\/\/\/\/\/\/\/\
```

---

# Dos tipos de volatilidad

## Volatilidad Histórica (HV)

Describe lo que ya ha ocurrido.

Se calcula utilizando datos históricos.

Es una medida retrospectiva.

---

## Volatilidad Implícita (IV)

Describe lo que el mercado espera.

No observa el pasado.

Está incorporada en el precio de las opciones.

Es una expectativa colectiva.

---

# Analogía

Imagine que quiere contratar un seguro para su vivienda.

Si la compañía cree que existe una elevada probabilidad de incendio, el seguro será caro.

Si considera que el riesgo es reducido, el seguro será barato.

Las opciones funcionan exactamente igual.

Cuando el mercado espera movimientos importantes, las primas aumentan.

---

# ¿Por qué aumenta la IV?

La volatilidad implícita suele incrementarse cuando existen eventos que generan incertidumbre.

Ejemplos:

- publicación de resultados;
- decisiones regulatorias;
- litigios importantes;
- fusiones;
- crisis financieras;
- acontecimientos geopolíticos.

No aumenta porque el precio suba.

Aumenta porque aumenta la incertidumbre.

---

# El efecto sobre las primas

```
Sube IV

↓

Suben las primas

------------------------

Baja IV

↓

Bajan las primas
```

Esto afecta especialmente a:

- Long Calls;
- Long Puts;
- LEAPS.

Y beneficia normalmente a:

- Covered Calls;
- Cash Secured Puts;
- Iron Condors;
- Credit Spreads.

---

# IV Rank

El IV Rank responde a una pregunta muy sencilla.

> ¿Dónde se encuentra la volatilidad actual respecto al último año?

Ejemplo.

```
IV Rank

10

↓

Volatilidad relativamente baja.

----------------------------

IV Rank

80

↓

Volatilidad relativamente alta.
```

---

# Regla práctica

| IV Rank | Interpretación |
|----------|----------------|
| 0-20 | Primas relativamente baratas. |
| 20-50 | Situación normal. |
| 50-80 | Primas relativamente caras. |
| 80-100 | Volatilidad muy elevada. |

No son reglas absolutas.

Siempre deben interpretarse junto al contexto técnico.

---

# IV Percentile

Mientras que IV Rank compara niveles extremos, IV Percentile responde a otra cuestión.

> ¿Durante qué porcentaje del tiempo la volatilidad ha sido inferior a la actual?

Ambos indicadores son complementarios.

Nunca deben interpretarse de forma aislada.

---

# El Volatility Crush

Uno de los fenómenos más importantes ocurre tras la publicación de resultados.

Antes del evento:

```
Resultados

↓

Aumenta incertidumbre

↓

Sube IV

↓

Suben primas
```

Después del evento:

```
Resultados publicados

↓

Desaparece incertidumbre

↓

Cae IV

↓

Caen primas
```

Este fenómeno recibe el nombre de:

**Volatility Crush**.

---

# Error clásico

Muchos operadores compran Calls el día anterior a resultados.

La acción sube.

Sin embargo, la opción apenas gana dinero.

¿Por qué?

Porque la caída de la volatilidad compensa parcialmente la subida del activo.

---

# Relación con las estrategias

| Estrategia | Preferencia IV |
|------------|----------------|
| Long Call | Baja IV |
| Long Put | Baja IV |
| LEAPS | Baja IV |
| Cash Secured Put | Alta IV |
| Covered Call | Alta IV |
| Bull Put Spread | Alta IV |
| Iron Condor | Alta IV |

---

# Resumen

La volatilidad implícita no predice el mercado.

Determina el precio del seguro que representan las opciones.

Un gestor profesional no pregunta únicamente:

> ¿Va a subir la acción?

También pregunta:

> ¿Estoy pagando demasiado por esa opción?

---

# Checklist

□ Distingo HV de IV.

□ Comprendo IV Rank.

□ Comprendo IV Percentile.

□ Entiendo el Volatility Crush.

□ Sé por qué una opción puede perder valor aunque acierte la dirección.
