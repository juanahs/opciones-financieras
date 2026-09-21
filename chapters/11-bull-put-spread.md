---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 11 — Bull Put Spread"

---

# Capítulo 11 — Bull Put Spread



---

## Introducción

El Bull Put Spread es una de las estrategias con mejor relación entre eficiencia del capital y control del riesgo para un inversor en acciones.

Puede entenderse como una evolución natural de la Cash Secured Put.

Mientras que la Cash Secured Put requiere disponer del capital suficiente para comprar las acciones, el Bull Put Spread limita el riesgo máximo mediante la compra de una segunda Put.

El resultado es una estrategia:

- alcista;
- de riesgo definido;
- con Theta positiva;
- muy eficiente en consumo de capital.

No pretende sustituir la compra de acciones.

Pretende expresar una visión moderadamente alcista utilizando mucho menos capital.

---

## Objetivos

Al finalizar este capítulo el lector será capaz de:

- Construir correctamente un Bull Put Spread.
- Entender cuándo es superior a una Cash Secured Put.
- Calcular beneficio máximo y pérdida máxima.
- Integrarlo con un análisis técnico basado en Swing Trading.

---

# Construcción

La estrategia se compone de dos operaciones simultáneas.

```
Vender Put

+

Comprar Put inferior
```

Ejemplo:

```
Microsoft

Precio

500 $

↓

Vender Put 480

↓

Comprar Put 460
```

La segunda Put limita completamente el riesgo.

---

# Flujo económico

```
Venta Put

↓

+ Prima

--------------------

Compra Put

↓

- Prima

--------------------

Resultado

↓

Crédito neto
```

La operación comienza con ingreso de efectivo.

---

# Perfil de beneficios

```
Beneficio

^

|

───────────────

|

|

|

|

|__________________________

Precio
```

El beneficio máximo queda limitado al crédito recibido.

La pérdida máxima también queda limitada.

---

# ¿Qué opinión expresa?

El Bull Put Spread expresa una visión:

- moderadamente alcista;
- neutral-alcista;
- ligeramente lateral.

No necesita una gran subida.

En muchas ocasiones basta con que la acción no caiga.

---

# Comparación con Cash Secured Put

| Característica | Cash Secured Put | Bull Put Spread |
|----------------|-----------------:|----------------:|
| Capital requerido | Alto | Bajo |
| Riesgo máximo | Similar al de comprar acciones | Limitado |
| Prima | Mayor | Menor |
| Posible asignación | Sí | Poco habitual si se gestiona antes del vencimiento |
| Uso del capital | Bajo | Muy eficiente |

---

# ¿Cuándo utilizarla?

Especialmente cuando:

- no desea inmovilizar grandes cantidades de efectivo;
- espera una subida moderada;
- existe un soporte claramente identificado;
- IV relativamente elevada.

---

# ¿Cuándo NO utilizarla?

No suele ser la mejor alternativa cuando:

- desea comprar realmente las acciones;
- espera una subida muy fuerte;
- IV es extremadamente baja.

---

# Integración con Swing Trading

Supongamos el siguiente contexto.

```
Reacumulación

↓

LPS

↓

Ruptura pendiente
```

La expectativa es favorable.

Sin embargo, aún no existe confirmación definitiva.

En este contexto un Bull Put Spread puede ofrecer una excelente relación entre:

- probabilidad;
- riesgo;
- capital empleado.

---

# Ejemplo

ASML

Precio actual:

720 €

Zona de soporte:

690 €

Construcción:

```
Vender Put 690

↓

Comprar Put 660

↓

Cobrar crédito
```

Mientras el precio permanezca por encima del Strike vendido al vencimiento, el crédito recibido constituirá el beneficio máximo.

---

# Ventajas

- Riesgo perfectamente conocido.
- Excelente eficiencia del capital.
- Theta positiva.
- Menor exposición psicológica.

---

# Inconvenientes

- Beneficio limitado.
- No permite adquirir acciones.
- Requiere comprender el funcionamiento de los spreads.

---

# Gestión

Un gestor rara vez espera al vencimiento.

Si una parte importante del beneficio ya se ha materializado antes de tiempo, suele valorar el cierre anticipado para liberar capital y reducir riesgo.

---

# Checklist

□ Tendencia primaria favorable.

□ Soporte claramente definido.

□ IV relativamente alta.

□ Riesgo máximo aceptable.

□ Liquidez adecuada.

□ Spread Bid/Ask reducido.

---

# Conclusión

El Bull Put Spread representa una de las estrategias más eficientes para expresar una visión moderadamente alcista cuando el objetivo principal no es adquirir acciones sino optimizar la relación entre riesgo y capital utilizado.
