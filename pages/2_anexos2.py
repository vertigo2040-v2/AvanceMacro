import streamlit as st

st.title("Anexo: Derivación matemática del modelo de Kremer (1993)")

st.markdown(r"""
Este anexo presenta la derivación formal del modelo central de Michael Kremer (1993), 
tal como aparece en su artículo *“Population Growth and Technological Change: One Million B.C. to 1990”*.
""")

st.header("1. Supuestos básicos")

El modelo se construye sobre dos supuestos fundamentales:

1. **La tecnología es no rival**: cada innovación puede ser usada por todos sin agotarse. Por lo tanto, la tasa de innovación es proporcional al número de personas.
2. **Equilibrio malthusiano**: el ingreso per cápita se mantiene en un nivel de subsistencia constante, $\bar{y}$, determinado por la tecnología disponible.

Estos supuestos permiten vincular dinámicamente la población $P(t)$ y el nivel tecnológico $A(t)$.

st.header("2. Función de producción agrícola")

Kremer modela la producción de alimentos —el cuello de botella demográfico— mediante:

$$
Y(t) = [A(t) P(t)]^{1 - \alpha} T^{\alpha}, \quad 0 < \alpha < 1
$$

donde:
- $Y(t)$: producción total de alimentos,
- $A(t)$: nivel de tecnología,
- $P(t)$: población (trabajo),
- $T$: cantidad fija de tierra.

Dado que **la tierra es un recurso fijo y no crece con el tiempo**, Kremer **normaliza $T = 1$** sin pérdida de generalidad. Esto simplifica la función a:

$$
Y(t) = [A(t) P(t)]^{1 - \alpha}
\tag{1}
$$

> 🔹 **Nota**: La normalización $T = 1$ es estándar en modelos de crecimiento con factores fijos. No afecta las dinámicas relativas, solo escala los niveles absolutos.

st.header("3. Condición malthusiana")

En equilibrio malthusiano, el ingreso per cápita se mantiene en el nivel de subsistencia $\bar{y}$:

$$
\frac{Y(t)}{P(t)} = \bar{y} \quad \Rightarrow \quad Y(t) = \bar{y} P(t)
\tag{2}
$$

Igualando (1) y (2):

$$
\bar{y} P(t) = [A(t) P(t)]^{1 - \alpha}
$$

Despejando $P(t)$:

$$
P(t) = \left( \frac{A(t)^{1 - \alpha}}{\bar{y}} \right)^{\frac{1}{\alpha}} = \frac{A(t)^{\frac{1 - \alpha}{\alpha}}}{\bar{y}^{1/\alpha}}
\tag{3}
$$

Esta ecuación muestra que **la población es una función creciente de la tecnología**.

st.header("4. Dinámica del cambio tecnológico")

Kremer postula que la tasa de crecimiento tecnológico es proporcional a la población:

$$
\frac{\dot{A}(t)}{A(t)} = g P(t)
\tag{4}
$$

donde $g > 0$ es la productividad de la investigación (probabilidad de innovar por persona).

st.header("5. Sistema dinámico cerrado")

Derivamos (3) logarítmicamente:

$$
\ln P = \frac{1 - \alpha}{\alpha} \ln A - \frac{1}{\alpha} \ln \bar{y}
$$

Derivando respecto al tiempo:

$$
\frac{\dot{P}}{P} = \frac{1 - \alpha}{\alpha} \cdot \frac{\dot{A}}{A}
$$

Sustituimos (4):

$$
\frac{\dot{P}}{P} = \frac{1 - \alpha}{\alpha} \cdot g P
\quad \Rightarrow \quad
\dot{P} = \underbrace{\frac{g(1 - \alpha)}{\alpha}}_{k} P^2
\tag{5}
$$

Esta es una **ecuación diferencial de crecimiento super-exponencial**: la tasa de crecimiento de la población es proporcional al **nivel** de población.

st.header("6. Solución y predicción empírica")

La solución de (5) es:

$$
P(t) = \frac{1}{C - k t}
$$

lo que implica una **singularidad demográfica** (población infinita en tiempo finito) si no hay cambios estructurales.

Empíricamente, Kremer estima la regresión:

$$
\text{GRPOP}_t = \beta_0 + \beta_1 \text{POP}_t + \varepsilon_t
$$

y encuentra $\beta_0 \approx 0$, $\beta_1 > 0$, lo cual es consistente con:

$$
\frac{\dot{P}}{P} = k P \quad \Rightarrow \quad \text{GRPOP} \propto \text{POP}
$$

Este patrón se observa en los datos históricos desde 1,000,000 A.C. hasta ~1950.

st.header("7. Extensión: transición demográfica")

Para explicar la desaceleración post-1950, Kremer generaliza el modelo asumiendo que la tasa de crecimiento poblacional depende del ingreso per cápita $y$:

$$
n = n(y), \quad \text{con } 
\begin{cases}
n'(y) > 0 & \text{si } y \text{ es bajo} \\
n'(y) < 0 & \text{si } y \text{ es alto}
\end{cases}
$$

Cuando el ingreso supera un umbral, **la fertilidad cae**, rompiendo el ciclo malthusiano. Esto explica la transición demográfica sin recurrir a colapsos ecológicos.

st.header("Referencia")

- Kremer, M. (1993). *Population Growth and Technological Change: One Million B.C. to 1990*.  
  **The Quarterly Journal of Economics**, 108(3), 681–716.