---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 100"

---

# Capítulo 100 — Capítulo 100

# Diagonal Spread

---

# Introducción

El Diagonal Spread combina dos dimensiones diferentes:

- distintos Strikes;
- distintos vencimientos.

Puede considerarse una evolución del Calendar Spread, incorporando además una visión direccional del mercado.

Es una estrategia ampliamente utilizada por gestores que desean combinar generación de Theta con exposición direccional moderada.

---

# Objetivos

Al finalizar este capítulo el lector será capaz de:

- Comprender la estructura de un Diagonal Spread.
- Diferenciarlo de un Calendar.
- Seleccionar los parámetros adecuados.
- Gestionarlo correctamente.

---

# Estructura

Ejemplo alcista.

```
Comprar Call

↓

Strike inferior

↓

Vencimiento lejano

+

Vender Call

↓

Strike superior

↓

Vencimiento cercano
```

---

# Objetivo

Obtener ingresos periódicos mediante la venta de opciones mientras se mantiene una exposición alcista utilizando una opción de largo plazo.

---

# Cuándo utilizarla

Especialmente adecuada cuando:

- existe tendencia alcista moderada;
- no se espera un movimiento explosivo inmediato;
- la IV del vencimiento corto resulta atractiva.

---

# Ventajas

- menor coste que una Covered Call;
- buena eficiencia del capital;
- posibilidad de realizar Rolls sucesivos.

---

# Inconvenientes

- gestión compleja;
- sensibilidad a Vega;
- múltiples variables simultáneas.

---

# Greeks

| Greek | Comportamiento habitual |
|---------|------------------------|
| Delta | Positiva |
| Gamma | Moderada |
| Theta | Positiva |
| Vega | Positiva |

---

# Gestión

La opción corta suele gestionarse de forma activa.

Puede:

- recomprarse;
- rolarse;
- dejar expirar.

La opción larga constituye la posición estructural.

---

# Integración con Swing Trading

```
Reacumulación

↓

Inicio tendencia

↓

Diagonal
```

---

# Checklist

□ Tendencia alcista.

□ LEAPS líquida.

□ Vencimiento corto líquido.

□ Strike superior coherente.

□ Plan de Roll.

---

# Conclusión

El Diagonal Spread combina eficiencia de capital, generación de Theta y exposición direccional, convirtiéndose en una excelente herramienta para inversores experimentados.
