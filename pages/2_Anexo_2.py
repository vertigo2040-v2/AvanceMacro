import streamlit as st

st.title("Anexo 2: Intuición económica del modelo de Kremer (1993)")

st.markdown(r"""
Este anexo presenta la lógica económica subyacente al modelo de Kremer, 
destacando por qué genera **crecimiento super-exponencial** y cómo difiere 
de los modelos malthusianos o neoclásicos tradicionales.
""")

st.header("1. Intuición central: una bola de nieve endógena")

Kremer propone un mecanismo simple pero poderoso:

> **Más personas → más inventores → más tecnología → más personas → …**

Este ciclo no es exógeno (como en Solow), sino **endógeno**: el tamaño de la población impulsa directamente el progreso tecnológico, y este a su vez permite sostener una población mayor.

A diferencia del modelo malthusiano clásico —donde la tecnología es dada y la población simplemente se ajusta a ella—, aquí **la población es motor del cambio**, no solo resultado.

---

st.header("2. Supuestos económicos clave")

El modelo descansa en tres pilares microeconómicos:

1. **No rivalidad de las ideas**:  
   Una innovación puede ser usada por todos sin agotarse. Por tanto, el número total de innovaciones depende del número de mentes que intentan innovar.

2. **Equilibrio malthusiano en ingreso per cápita**:  
   En sociedades preindustriales, el ingreso per cápita se mantiene en un nivel de subsistencia $\bar{y}$. Cualquier mejora tecnológica permite que **más personas sobrevivan**, no que cada persona sea más rica.

3. **Tasa de innovación proporcional a la población**:  
   Cada individuo tiene una probabilidad fija $g$ de generar una innovación útil. Por lo tanto, la tasa agregada de innovación es $g P(t)$.

Estos supuestos implican que **el crecimiento no se desacelera con el tiempo**, sino que **se acelera**: cuanta más gente hay, más rápido avanza la tecnología, y más rápido crece la población.

---

st.header("3. Interacción dinámica: el bucle de retroalimentación")

La dinámica se cierra en dos ecuaciones:

1. **Producción agrícola limitada por tierra fija**:
   $$
   Y(t) = [A(t) P(t)]^{1 - \alpha}, \quad 0 < \alpha < 1
   $$

2. **Ingreso per cápita constante en subsistencia**:
   $$
   \frac{Y(t)}{P(t)} = \bar{y}
   \quad \Rightarrow \quad
   P(t) \propto A(t)^{\frac{1 - \alpha}{\alpha}}
   $$

3. **Crecimiento tecnológico impulsado por la población**:
   $$
   \frac{\dot{A}(t)}{A(t)} = g P(t)
   $$

Combinando estas relaciones, se obtiene:
$$
\frac{\dot{P}(t)}{P(t)} = \underbrace{\frac{g(1 - \alpha)}{\alpha}}_{k} P(t)
\quad \Rightarrow \quad
\dot{P} = k P^2
$$

Esta ecuación captura la esencia del modelo:  
> **La tasa de crecimiento poblacional es proporcional al nivel de población**.

Esto explica empíricamente la relación observada en los datos históricos desde 1,000,000 A.C. hasta ~1950.

---

st.header("4. ¿Por qué no explota en la realidad? La transición demográfica")

El modelo básico predice una "singularidad demográfica" (población infinita en tiempo finito).  
Sin embargo, **en el siglo XX, el crecimiento se desacelera**.

Kremer resuelve esta aparente contradicción introduciendo un cambio estructural:  
cuando el ingreso per cápita supera un umbral, **las familias eligen tener menos hijos**.  
Esto rompe el ciclo malthusiano no por escasez, sino por **prosperidad**.

Así, el modelo no falla: **su extensión generalizada predice la transición demográfica como consecuencia natural del progreso**.

---

st.markdown("""
**Conclusión**: El modelo de Kremer no solo describe el pasado, sino que anticipa por qué el crecimiento demográfico moderno se detiene:  
no porque nos quedemos sin recursos, sino porque invertimos más en la calidad de pocos hijos que en la cantidad de muchos.
""")
