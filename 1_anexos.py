import streamlit as st

st.title("Anexo: Derivación analítica del modelo de Kremer (1993)")

st.markdown(r"""
Este anexo presenta la derivación formal del modelo central de Kremer (1993), 
alineado con la discusión de los modelos de crecimiento endógeno en 
**David Romer, *Macroeconomía Avanzada* (Capítulo 3)**.
""")

st.header("1. Supuestos fundamentales")

st.markdown(r"""
El modelo se basa en tres pilares microeconómicos:

1. **La tecnología es no rival**: una innovación puede ser usada por todos sin agotarse.  
   → El número total de innovaciones depende del número de personas que intentan innovar.
2. **Equilibrio malthusiano**: el ingreso per cápita se mantiene en el nivel de subsistencia $\bar{y}$.
3. **Crecimiento tecnológico endógeno**: la tasa de innovación es proporcional a la población.

Estos supuestos permiten cerrar un sistema dinámico entre población $P(t)$ y tecnología $A(t)$.
""")

st.header("2. Función de producción agrícola")

st.markdown(r"""
Siguiendo a Malthus y Kremer, la producción de alimentos determina el tamaño máximo de la población. 
La función de producción es:

$$
Y(t) = [A(t) P(t)]^{1 - \alpha}, \quad 0 < \alpha < 1
$$

donde:
- $Y(t)$: producción total de alimentos,
- $A(t)$: nivel de tecnología (eficiencia del trabajo),
- $P(t)$: población (trabajo),
- $\alpha$: elasticidad de la tierra (normalizada a 1 unidad).

En equilibrio malthusiano, el ingreso per cápita es constante en $\bar{y}$, por lo que:

$$
\frac{Y(t)}{P(t)} = \bar{y} \quad \Rightarrow \quad Y(t) = \bar{y} P(t)
$$

Igualando ambas expresiones:

$$
\bar{y} P(t) = [A(t) P(t)]^{1 - \alpha}
$$

Despejando $P(t)$:

$$
P(t) = \left( \frac{A(t)^{1 - \alpha}}{\bar{y}} \right)^{\frac{1}{\alpha}} = \frac{A(t)^{\frac{1 - \alpha}{\alpha}}}{\bar{y}^{1/\alpha}}
\tag{1}
$$

Esta ecuación muestra que **la población es una función creciente de la tecnología**.
""")

st.header("3. Dinámica del cambio tecnológico")

st.markdown(r"""
Kremer asume que las innovaciones son descubiertas por individuos, y que la tasa de innovación es proporcional al número de personas:

$$
\frac{\dot{A}(t)}{A(t)} = g P(t)
\tag{2}
$$

donde:
- $g > 0$: productividad de la investigación (probabilidad de innovar por persona),
- $\dot{A}(t)$: tasa de cambio de la tecnología.

Este es el corazón del modelo: **más población → más inventores → más tecnología**.
""")

st.header("4. Sistema dinámico completo")

st.markdown(r"""
Sustituimos (1) en (2). Primero, tomamos logaritmos de (1):

$$
\ln P = \frac{1 - \alpha}{\alpha} \ln A - \frac{1}{\alpha} \ln \bar{y}
$$

Derivamos respecto al tiempo:

$$
\frac{\dot{P}}{P} = \frac{1 - \alpha}{\alpha} \cdot \frac{\dot{A}}{A}
$$

Ahora sustituimos (2):

$$
\frac{\dot{P}}{P} = \frac{1 - \alpha}{\alpha} \cdot g P
\quad \Rightarrow \quad
\dot{P} = \underbrace{\frac{g(1 - \alpha)}{\alpha}}_{k} P^2
\tag{3}
$$

Esta es una **ecuación diferencial de crecimiento super-exponencial**: la tasa de crecimiento de la población es proporcional al **nivel** de población.

La solución es:
$$
P(t) = \frac{1}{C - k t}
$$
lo que implica una **singularidad demográfica** (población infinita en tiempo finito) si no hay cambios estructurales.
""")

st.header("5. Predicción empírica")

st.markdown(r"""
Kremer estima la regresión:
$$
\text{GRPOP}_t = \beta_0 + \beta_1 \text{POP}_t + \varepsilon_t
$$

y encuentra que $\beta_0 \approx 0$ y $\beta_1 > 0$, lo cual es consistente con (3), ya que:

$$
\frac{\dot{P}}{P} = k P \quad \Rightarrow \quad \text{GRPOP} \propto \text{POP}
$$

Esto se observa en los datos históricos desde 1,000,000 A.C. hasta ~1950.
""")

st.header("6. Conexión con David Romer (*Macroeconomía Avanzada*)")

st.markdown(r"""
Como señala **David Romer (Capítulo 3, 5ª ed.)**, los modelos de crecimiento endógeno con externalidades de conocimiento comparten la idea central de que **las ideas son no rivales**. 

Sin embargo, Kremer hace una contribución única:

- En lugar de enfocarse en capital humano o I+D formal (como en los modelos de Paul Romer, 1990), 
  **usa la población como proxy de capacidad innovadora**.
- Aplica el modelo a **un millón de años de historia**, no solo al período moderno.
- Muestra que el crecimiento puede ser endógeno incluso en sociedades sin mercados formales.

> *"Kremer’s model is a striking example of how simple assumptions about the nonrivalry of ideas can generate powerful predictions about long-run development."*  
> — David Romer, *Advanced Macroeconomics*, p. 132 (5ª ed., 2019)

Además, el modelo ilustra el concepto de **externalidades positivas de la población**: cada persona adicional genera conocimiento que beneficia a todos, sin recibir compensación directa.
""")

st.header("7. Extensión: transición demográfica")

st.markdown(r"""
El modelo básico no explica la desaceleración post-1950. Kremer lo generaliza asumiendo que la tasa de crecimiento poblacional es una función del ingreso per cápita $y$:

$$
n = n(y), \quad \text{con } 
\begin{cases}
n'(y) > 0 & \text{si } y \text{ es bajo} \\
n'(y) < 0 & \text{si } y \text{ es alto}
\end{cases}
$$

Cuando $y$ supera un umbral (por mayor educación, menor mortalidad infantil, etc.), **la fertilidad cae**, rompiendo el ciclo malthusiano. Esto es coherente con la teoría del capital humano (Becker, 1960) y con la evidencia empírica.
""")

st.header("Referencias")

st.markdown("""
- Kremer, M. (1993). *Population Growth and Technological Change: One Million B.C. to 1990*.  
  **The Quarterly Journal of Economics**, 108(3), 681–716.
- Romer, D. (2019). *Advanced Macroeconomics* (5ª ed.). McGraw-Hill. Capítulo 3.
- Romer, P. M. (1990). *Endogenous Technological Change*.  
  **Journal of Political Economy**, 98(5), S71–S102.
""")