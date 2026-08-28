# Capítulo 152

# Volatility Lab de Interactive Brokers

---

# Introducción

La mayoría de los inversores observan únicamente el precio.

Los operadores profesionales de opciones observan dos gráficos simultáneamente:

- el precio;
- la volatilidad.

Interactive Brokers incorpora una de las mejores herramientas para este análisis: **Volatility Lab**.

Su finalidad consiste en estudiar la volatilidad de un activo desde diferentes perspectivas para determinar si las opciones están relativamente caras o baratas.

---

# Objetivos

Volatility Lab permite responder preguntas como:

- ¿La IV actual es alta?
- ¿Es baja respecto a los últimos años?
- ¿Está aumentando?
- ¿Está disminuyendo?
- ¿Qué vencimientos presentan mejores oportunidades?

---

# Flujo de trabajo

```
Seleccionar empresa

↓

Abrir Volatility Lab

↓

Analizar IV

↓

Comparar con HV

↓

Analizar estructura temporal

↓

Seleccionar estrategia
```

---

# Módulo 1

## Historical Volatility

Representa la volatilidad que realmente ha experimentado el precio.

No incorpora expectativas futuras.

---

# Módulo 2

## Implied Volatility

Representa la volatilidad descontada por el mercado.

Es una expectativa.

No una predicción.

---

# Interpretación

```
IV

>

HV
```

Puede indicar que el mercado espera movimientos superiores a los observados históricamente.

---

```
IV

<

HV
```

Puede indicar expectativas moderadas.

No implica automáticamente que las opciones estén infravaloradas.

---

# Smile

Volatility Lab facilita visualizar el comportamiento de la volatilidad para distintos Strikes.

```
Strike

↓

IV diferente
```

No todas las opciones del mismo vencimiento cotizan con la misma volatilidad implícita.

---

# Term Structure

Analiza cómo cambia la IV entre distintos vencimientos.

```
30 días

↓

60 días

↓

90 días

↓

180 días
```

Esta información resulta especialmente útil para:

- Calendar Spreads.
- Diagonal Spreads.
- LEAPS.

---

# Integración con el análisis técnico

Volatility Lab nunca sustituye al gráfico.

El procedimiento recomendado es:

```
TradingView

↓

Wyckoff

↓

VSA

↓

Volatility Lab

↓

Option Chain
```

---

# Checklist

□ IV revisada.

□ HV revisada.

□ Smile analizado.

□ Term Structure revisada.

□ Estrategia coherente.

---

# Conclusión

Volatility Lab convierte la volatilidad en una variable observable y cuantificable, permitiendo seleccionar estrategias con una base mucho más sólida que la simple intuición.
