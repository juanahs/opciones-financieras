# Capítulo 35

# Greeks Avanzadas

---

# Introducción

La mayoría de libros presentan las Greeks como conceptos independientes.

Delta.

Gamma.

Theta.

Vega.

Rho.

Sin embargo, un gestor profesional rara vez analiza una Greek de forma aislada.

Las Greeks constituyen un sistema dinámico.

Modificar una de ellas implica modificar el comportamiento global de la posición.

Comprender esa interacción permite anticipar cómo evolucionará una cartera incluso antes de que cambie el precio del subyacente.

---

# Objetivos

Al finalizar este capítulo el lector será capaz de:

- Interpretar conjuntamente las Greeks.
- Analizar exposiciones agregadas.
- Comprender la evolución temporal del riesgo.
- Gestionar una cartera mediante Greeks.

---

# Las Greeks como cuadro de mandos

Imagine el panel de un avión.

```
Velocidad

Altitud

Combustible

Motor
```

Ningún piloto toma decisiones observando un único indicador.

Con las opciones ocurre exactamente lo mismo.

---

# Delta

Pregunta:

> ¿Qué ocurre si la acción sube un euro?

---

# Gamma

Pregunta:

> ¿Cómo cambiará la Delta cuando cambie el precio?

---

# Theta

Pregunta:

> ¿Cuánto cuesta mantener esta posición un día más?

---

# Vega

Pregunta:

> ¿Qué sucede si cambia la volatilidad implícita?

---

# Rho

Pregunta:

> ¿Cómo afectan los tipos de interés?

---

# Interacción

Supongamos una Long Call ATM.

```
Delta

Media

Gamma

Alta

Theta

Negativa

Vega

Alta
```

Si el precio comienza a subir:

```
Delta

↑

Gamma

↓

Theta

↓

```

La exposición evoluciona constantemente.

---

# Exposición agregada

Lo realmente importante es la cartera.

Ejemplo.

```
Covered Call

+

Cash Secured Put

+

LEAPS

+

Bull Put Spread
```

Cada estrategia aporta Greeks distintas.

La suma determina el riesgo real.

---

# Cartera equilibrada

Un gestor suele preguntarse:

```
¿Tengo demasiada Delta?

↓

¿Demasiada Vega?

↓

¿Exceso de Theta?

↓

¿Exceso de Gamma?
```

La respuesta condiciona las siguientes operaciones.

---

# Ejemplo práctico

Supongamos una cartera con:

- Covered Calls.
- Cash Secured Puts.
- PMCC.

La cartera probablemente presentará:

```
Delta positiva

Theta positiva

Vega moderada

Gamma reducida
```

Un cambio importante de volatilidad afectará menos que a una cartera formada exclusivamente por LEAPS.

---

# Error habitual

Analizar únicamente la Delta.

Esto equivale a conducir mirando únicamente el velocímetro.

---

# Checklist

□ Analizo la cartera completa.

□ Comprendo la interacción entre Greeks.

□ No interpreto cada Greek por separado.

□ Reviso las exposiciones periódicamente.

---

# Conclusión

Las Greeks deben entenderse como un sistema de gestión del riesgo.

La verdadera ventaja aparece cuando se interpretan conjuntamente.
