---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 3 — Anatomía de un contrato de opciones"

---

# Capítulo 3 — Anatomía de un contrato de opciones



---

## Introducción

Antes de estudiar estrategias es imprescindible aprender a leer un contrato de opciones exactamente igual que lo hace un operador profesional.

Cuando un gestor observa una cadena de opciones no ve una lista de precios.

Ve cientos de contratos con características diferentes.

Cada uno representa una combinación distinta de:

- tiempo
- riesgo
- probabilidad
- sensibilidad al precio
- sensibilidad a la volatilidad

Aprender a interpretar correctamente un contrato es la base de toda la operativa posterior.

---

## Objetivos

Al finalizar este capítulo el lector será capaz de:

- Leer cualquier contrato de opciones.
- Identificar todos sus componentes.
- Comprender cómo cambia el contrato con el tiempo.
- Interpretar correctamente una cadena de opciones.

---

## Anatomía completa

Ejemplo:

```
AAPL

19 SEP 2026

220

CALL
```

Cada línea contiene una información diferente.

```
┌────────────────────────────┐

AAPL

Activo subyacente

└────────────────────────────┘

┌────────────────────────────┐

19 SEP 2026

Fecha de vencimiento

└────────────────────────────┘

┌────────────────────────────┐

220

Strike

└────────────────────────────┘

┌────────────────────────────┐

CALL

Tipo de contrato

└────────────────────────────┘
```

---

# El ticker

El primer dato identifica el activo.

Ejemplos:

| Ticker | Empresa |
|----------|----------------|
| AAPL | Apple |
| MSFT | Microsoft |
| NVDA | NVIDIA |
| ASML | ASML Holding |
| META | Meta |
| COST | Costco |
| AMD | AMD |

Toda la valoración posterior dependerá del comportamiento de esa empresa.

---

# El vencimiento

Todas las opciones tienen fecha de caducidad.

Por ejemplo:

```
18 JUL 2026

15 AGO 2026

19 SEP 2026

18 DIC 2026

15 ENE 2027

17 ENE 2028
```

Cuanto mayor sea el vencimiento:

- mayor valor temporal;
- menor Theta diaria;
- mayor sensibilidad a Vega;
- mayor coste.

---

# El Strike

El Strike determina el precio contractual.

No cambia.

La acción sí cambia.

Ejemplo.

```
Acción

218 $

Strike

220 $

```

Si mañana la acción cotiza a:

230 $

El Strike seguirá siendo:

220 $

---

# Call o Put

Todo contrato pertenece únicamente a uno de estos grupos.

```
CALL

Derecho a comprar

----------------------

PUT

Derecho a vender
```

No existen otros tipos de opciones.

Todas las estrategias del libro se construyen únicamente combinando Calls y Puts.

---

# Cantidad de acciones

En Estados Unidos:

```
1 contrato

=

100 acciones
```

Por ello:

```
5 contratos

=

500 acciones

```

Este dato resulta imprescindible para calcular:

- exposición
- riesgo
- capital necesario
- asignación

---

# Prima

Supongamos:

```
Prima

3,80 $
```

Muchos principiantes creen que pagarán:

3,80 $

En realidad:

```
3,80

×

100

=

380 $
```

La prima siempre debe multiplicarse por el multiplicador del contrato.

---

# Valor intrínseco

El valor intrínseco representa el beneficio que tendría el contrato si pudiera ejercerse inmediatamente.

Ejemplo.

```
Acción

225 $

Call Strike

220 $

```

Valor intrínseco:

```
225−220

=

5 $
```

Todo lo que exceda esos 5 $ será valor temporal.

---

# Valor temporal

Supongamos:

```
Prima

7 $

Valor intrínseco

5 $
```

Entonces:

```
Valor temporal

2 $
```

Este componente desaparecerá progresivamente conforme se acerque el vencimiento.

---

# Resumen gráfico

```
Prima

│

├───────────────┐

│

Valor Intrínseco

│

└───────────────┐

Valor Temporal
```

Toda opción puede descomponerse siempre de esta forma.

---

# Errores habituales

- Confundir Strike con cotización.
- Olvidar multiplicar la prima por 100.
- Comprar contratos demasiado próximos al vencimiento.
- Ignorar el valor temporal.
- Elegir únicamente por precio.

---

# Checklist

□ Sé leer un contrato.

□ Distingo Strike de cotización.

□ Comprendo el efecto del vencimiento.

□ Sé calcular el coste real de la prima.

□ Comprendo qué parte del precio corresponde a tiempo.
