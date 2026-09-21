---
description: ""
date: 2026-09-21
tags: []
draft: false
title: "Capítulo 120"

---

# Capítulo 120 — Capítulo 120

# Risk Navigator de Interactive Brokers

---

# Introducción

Una de las mayores ventajas de Interactive Brokers es disponer de herramientas profesionales normalmente reservadas para instituciones.

Entre ellas destaca Risk Navigator.

No se limita a mostrar beneficios o pérdidas.

Permite comprender cómo reaccionará la cartera completa ante distintos escenarios.

---

# Objetivos

- Comprender el funcionamiento de Risk Navigator.
- Interpretar escenarios.
- Analizar Greeks agregadas.
- Mejorar la gestión del riesgo.

---

# ¿Qué permite analizar?

Entre otros aspectos:

- Delta total.
- Gamma.
- Theta.
- Vega.
- Riesgo por subyacente.
- Riesgo por sector.
- Simulación de escenarios.

---

# Filosofía

Antes de abrir una nueva operación debemos preguntarnos:

```
¿Cómo cambia la cartera?

No

↓

¿Cómo cambia la operación?
```

---

# Escenarios

Ejemplo.

```
Mercado

-5 %

↓

Impacto cartera

----------------

IV

+10 %

↓

Impacto cartera

----------------

Paso del tiempo

↓

Impacto cartera
```

---

# Greeks agregadas

No basta con conocer la Delta de una posición.

Importa mucho más conocer la Delta total.

Lo mismo ocurre con:

- Vega.
- Theta.
- Gamma.

---

# Simulación

Una de las funciones más valiosas consiste en modificar:

- precio;
- volatilidad;
- tiempo.

Y observar inmediatamente el resultado esperado.

---

# Aplicación práctica

Antes de vender una nueva Put.

```
Nueva CSP

↓

Actualizar simulación

↓

¿Aumenta demasiado Delta?

↓

Sí

↓

Reducir tamaño
```

---

# Checklist

□ Revisar Delta agregada.

□ Revisar Vega.

□ Revisar concentración.

□ Simular escenarios.

□ Analizar exposición futura.

---

# Conclusión

Risk Navigator transforma una colección de operaciones individuales en una cartera gestionada profesionalmente.
