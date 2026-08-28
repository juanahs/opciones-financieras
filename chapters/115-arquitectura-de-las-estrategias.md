# Capítulo 115

# Arquitectura de las Estrategias con Opciones

---

# Introducción

Tras estudiar decenas de estrategias es fácil cometer un error:

Pensar que cada una es completamente distinta.

En realidad, la mayoría pueden construirse a partir de un pequeño número de bloques básicos.

Comprender esta arquitectura resulta mucho más útil que memorizar nombres.

---

# Los cuatro bloques fundamentales

Toda estrategia nace de combinar alguno de estos elementos:

```
Long Call

Long Put

Short Call

Short Put
```

A partir de ellos aparecen todas las demás estructuras.

---

# Estrategias direccionales

```
Long Call

↓

Bull Call

↓

Diagonal

↓

PMCC

↓

ZEBRA
```

---

# Estrategias de ingreso

```
Short Put

↓

Cash Secured Put

↓

Wheel

↓

Bull Put Spread
```

---

# Estrategias de cobertura

```
Long Put

↓

Protective Put

↓

Collar
```

---

# Estrategias neutrales

```
Short Put

+

Short Call

↓

Strangle

↓

Straddle

↓

Iron Condor

↓

Iron Butterfly
```

---

# Estrategias sintéticas

```
Long Call

+

Short Put

↓

Synthetic Long

-------------------

Long Put

+

Short Call

↓

Synthetic Short
```

---

# Árbol general

```
4 bloques básicos

↓

12 estructuras simples

↓

30+ estrategias conocidas

↓

Miles de variantes posibles
```

---

# Filosofía

Un gestor profesional no memoriza estrategias.

Comprende cómo se construyen.

Cuando domina los bloques elementales puede diseñar estructuras adaptadas al problema concreto que desea resolver.

---

# Conclusión

La verdadera habilidad no consiste en recordar nombres.

Consiste en reconocer qué combinación de riesgos necesita la cartera y construirla utilizando los componentes adecuados.
