# Capítulo 99

# Calendar Spread

---

# Introducción

El Calendar Spread aprovecha una característica fundamental de las opciones:

No todas pierden valor temporal al mismo ritmo.

Las opciones con vencimiento próximo experimentan un deterioro temporal mucho más rápido que las de vencimiento lejano.

El Calendar Spread intenta beneficiarse precisamente de esa diferencia.

---

# Objetivos

- Comprender la estructura temporal.
- Identificar escenarios adecuados.
- Interpretar Theta y Vega.
- Integrar la estrategia dentro de una cartera diversificada.

---

# Estructura

Ejemplo con Calls.

```
Comprar Call

↓

Vencimiento lejano

+

Vender Call

↓

Mismo Strike

↓

Vencimiento cercano
```

---

# Escenario ideal

Especialmente interesante cuando:

- se espera un movimiento moderado;
- el precio permanece próximo al Strike;
- la IV puede aumentar.

---

# Greeks

Habitualmente presenta:

- Theta positiva por la opción vendida.
- Vega positiva por la opción comprada.
- Delta cercana a cero al inicio.

---

# Ventajas

- riesgo limitado;
- exposición controlada;
- buena eficiencia temporal.

---

# Inconvenientes

- gestión más compleja;
- fuerte dependencia del comportamiento temporal;
- sensibilidad a la volatilidad.

---

# Integración técnica

Los Calendar suelen utilizarse cerca de zonas donde se espera consolidación.

No son estrategias orientadas a grandes rupturas inmediatas.

---

# Checklist

□ Mercado lateral.

□ Strike correctamente elegido.

□ Diferencia temporal suficiente.

□ Liquidez elevada.

---

# Conclusión

El Calendar Spread introduce la dimensión temporal como fuente principal de ventaja, desplazando el foco desde la dirección del precio hacia la evolución relativa del tiempo y la volatilidad.
