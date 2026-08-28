# Capítulo 109

# Synthetic Long Stock

---

# Introducción

Una posición Synthetic Long intenta reproducir el comportamiento económico de poseer acciones utilizando exclusivamente opciones.

Su construcción es elegante desde el punto de vista financiero porque deriva directamente de la Paridad Put-Call.

Aunque muchos inversores la conocen únicamente desde un punto de vista teórico, constituye una herramienta muy utilizada por gestores institucionales para optimizar el uso del capital.

---

# Objetivos

Al finalizar este capítulo el lector será capaz de:

- Comprender la construcción de una Synthetic Long.
- Compararla con la compra directa de acciones.
- Identificar sus ventajas e inconvenientes.
- Saber cuándo resulta apropiada.

---

# Estructura

```
Comprar Call ATM

+

Vender Put ATM

↓

Mismo Strike

↓

Mismo vencimiento
```

---

# Resultado

La combinación replica aproximadamente el comportamiento de una posición larga en acciones.

```
Acciones

≈

Long Call

+

Short Put
```

---

# Ventajas

- menor desembolso inicial en determinados casos;
- gran eficiencia del capital;
- elevada Delta positiva;
- flexibilidad para gestionar la posición.

---

# Inconvenientes

- posible Assignment;
- uso de margen;
- mayor complejidad operativa;
- sensibilidad a la volatilidad.

---

# Integración con Swing Trading

Escenario apropiado.

```
Gran ruptura

↓

Convicción elevada

↓

Synthetic Long
```

---

# Riesgos

- caída importante del subyacente;
- Assignment de la Put;
- necesidad de gestionar garantías.

---

# Comparación

| Estrategia | Capital | Assignment | Complejidad |
|------------|----------|------------|-------------|
| Acciones | Alto | No | Baja |
| LEAPS | Medio | No | Baja |
| Synthetic Long | Variable | Sí | Alta |

---

# Checklist

□ Tendencia alcista.

□ Margen suficiente.

□ Assignment comprendido.

□ Liquidez elevada.

□ Plan de salida.

---

# Conclusión

La Synthetic Long permite replicar una posición accionarial utilizando opciones, pero requiere una comprensión profunda del riesgo asociado a la venta de Puts.
