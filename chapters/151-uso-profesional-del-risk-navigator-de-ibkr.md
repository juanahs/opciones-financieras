---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 151"

---

# Capítulo 151 — Capítulo 151

# Uso Profesional de Risk Navigator en Interactive Brokers

---

# Introducción

El Risk Navigator es una de las herramientas más potentes de Interactive Brokers.

Su finalidad no consiste únicamente en mostrar beneficios y pérdidas.

Permite comprender cómo responderá la cartera completa ante distintos escenarios.

---

# Objetivos

Con Risk Navigator es posible analizar:

- Delta total.
- Gamma.
- Theta.
- Vega.
- sensibilidad al precio;
- sensibilidad al tiempo;
- sensibilidad a la volatilidad.

---

# Flujo recomendado

```
Nueva operación

↓

Abrir Risk Navigator

↓

Simular incorporación

↓

Analizar impacto

↓

Enviar orden
```

Nunca al revés.

---

# Escenarios

Antes de ejecutar una operación conviene responder.

```
¿Qué ocurre si el mercado cae un 10 %?

↓

¿Qué ocurre si la IV aumenta?

↓

¿Qué ocurre si pasan 30 días?
```

---

# Análisis de Delta

Una nueva posición puede parecer pequeña.

Sin embargo.

```
Delta existente

+

Nueva Delta

↓

Cambio importante
```

El análisis agregado evita este problema.

---

# Simulación

Resulta recomendable simular.

- movimientos del subyacente;
- expansión de IV;
- contracción de IV;
- paso del tiempo.

---

# Beneficios

El uso sistemático de Risk Navigator permite.

- reducir sorpresas;
- comprender el riesgo real;
- construir carteras equilibradas.

---

# Error frecuente

Analizar únicamente el gráfico del subyacente.

El verdadero riesgo aparece cuando todas las posiciones interactúan simultáneamente.

---

# Checklist

□ Simulación realizada.

□ Greeks revisadas.

□ Riesgo agregado aceptable.

□ Liquidez suficiente.

---

# Conclusión

Risk Navigator transforma una colección de operaciones independientes en una cartera gestionada profesionalmente.
