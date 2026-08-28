# Capítulo 17

# Poor Man's Covered Call (PMCC)

---

# Introducción

La Poor Man's Covered Call (PMCC) es una de las estrategias más eficientes para un inversor patrimonial.

Su objetivo es reproducir gran parte del comportamiento de una Covered Call utilizando mucho menos capital.

La idea fundamental es extremadamente sencilla.

En lugar de comprar 100 acciones:

```
Comprar acciones

↓

Vender Calls periódicamente
```

se sustituye la posición por una LEAPS con Delta elevada.

```
Comprar LEAPS

↓

Vender Calls periódicamente
```

La LEAPS actúa como sustituto económico de las acciones.

---

# Objetivos

Al finalizar este capítulo el lector será capaz de:

- Comprender la lógica de la PMCC.
- Construir correctamente la estrategia.
- Seleccionar la LEAPS adecuada.
- Gestionar las Calls vendidas.
- Entender sus ventajas frente a una Covered Call tradicional.

---

# Filosofía

La PMCC responde a una única pregunta.

> ¿Es necesario inmovilizar 50.000 €, 80.000 € o 100.000 € para generar primas periódicas?

En muchas ocasiones la respuesta es:

No.

Una LEAPS bien seleccionada puede proporcionar una exposición muy similar utilizando aproximadamente entre un 30 % y un 50 % del capital.

---

# Construcción

```
Comprar LEAPS

↓

Delta alta

↓

Vender Calls OTM

↓

Repetir periódicamente
```

---

# Selección de la LEAPS

Una LEAPS adecuada suele cumplir:

- vencimiento superior a un año;
- Delta entre 0,75 y 0,90;
- elevada liquidez;
- spread Bid/Ask reducido.

---

# Selección de la Call vendida

Generalmente:

- OTM;
- vencimiento corto;
- Strike cercano a una resistencia técnica.

---

# Ventajas

- Mucho menor consumo de capital.
- Riesgo máximo limitado.
- Excelente eficiencia.
- Posibilidad de diversificar más.

---

# Inconvenientes

- Mayor complejidad.
- Vega elevada.
- Necesidad de gestionar vencimientos.

---

# Integración con Swing Trading

Ideal cuando:

- tendencia primaria alcista;
- fuerte fortaleza relativa;
- estructura de reacumulación;
- ruptura de máximos;
- horizonte superior a un año.

---

# Comparación

| Covered Call | PMCC |
|---------------|------|
| Compra acciones | Compra LEAPS |
| Capital elevado | Capital reducido |
| Dividendos | No |
| Theta neutra | Theta negativa en LEAPS |
| Gran eficiencia | Muy alta eficiencia |

---

# Conclusión

La PMCC constituye una evolución natural de la Covered Call para inversores que desean optimizar el uso del capital sin renunciar a la generación periódica de primas.
