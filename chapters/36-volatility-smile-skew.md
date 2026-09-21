---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 36"

---

# Capítulo 36 — Capítulo 36

# Smile y Skew de Volatilidad

---

# Introducción

Uno de los supuestos del modelo Black-Scholes afirma que todas las opciones de un mismo vencimiento deberían compartir una volatilidad implícita similar.

En la práctica esto nunca ocurre.

La realidad muestra que distintos Strikes cotizan con volatilidades diferentes.

Este fenómeno recibe el nombre de:

- Volatility Smile.
- Volatility Skew.

---

# Objetivos

- Comprender por qué aparece el Skew.
- Interpretar la información del mercado.
- Aplicarlo a la selección de estrategias.

---

# Smile

```
IV

^

|

      /\

     /  \

____/____\__________

Strike
```

Los Strikes extremos presentan mayor IV.

---

# Skew

En acciones individuales suele observarse un patrón diferente.

```
IV

^

|

\

 \

  \

   \__________

Strike
```

Las Puts OTM suelen cotizar con IV superior.

---

# ¿Por qué?

Muchos inversores desean proteger sus carteras.

La demanda de Puts incrementa su precio.

Al aumentar el precio aumenta también la volatilidad implícita.

---

# Aplicaciones

El Skew influye en:

- Covered Calls.
- Cash Secured Puts.
- Credit Spreads.
- Protective Puts.

---

# Ejemplo

Una Put muy OTM puede parecer cara.

Sin embargo:

no necesariamente está sobrevalorada.

Simplemente incorpora un mayor coste del seguro frente a movimientos extremos.

---

# Interpretación

Un Skew muy pronunciado suele reflejar:

- preocupación del mercado;
- búsqueda intensa de cobertura;
- mayor demanda de protección.

---

# Conclusión

Comprender el Skew permite interpretar mejor el precio de las primas y seleccionar estructuras más eficientes.
