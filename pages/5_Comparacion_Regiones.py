import streamlit as st
import matplotlib.pyplot as plt

st.title("Comparación entre regiones aisladas (Kremer, 1993)")

st.markdown("""
En la **Sección IV.B**, Kremer compara sociedades que estuvieron **aisladas tecnológicamente hasta 1500 d.C.**  
El modelo predice que **las regiones con mayor área (→ mayor población inicial) desarrollarían más tecnología** y, por tanto, alcanzarían **mayor densidad poblacional**.
""")

# Datos de la Tabla VII
regiones = ["Viejo Mundo", "Américas", "Australia", "Tasmania"]
area_km2 = [83.98, 38.43, 7.69, 0.068]  # millones de km²
pob_1500 = [407, 14, 0.2, 0.003]       # millones (usamos valor medio para Tasmania)
densidad = [p * 1e6 / (a * 1e6) for p, a in zip(pob_1500, area_km2)]  # hab/km²

# Gráfico de dispersión
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(area_km2, densidad, s=100, color="purple")
for i, region in enumerate(regiones):
    ax.text(area_km2[i], densidad[i] + 0.01, region, fontsize=10, ha='center')

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Área de tierra (millones de km², escala log)")
ax.set_ylabel("Densidad poblacional en 1500 (hab/km², escala log)")
ax.set_title("Área vs. Densidad poblacional en 1500")
ax.grid(True, which="both", ls="--", lw=0.5)
st.pyplot(fig)

st.markdown("""
### Interpretación
- **Viejo Mundo**: gran área → alta densidad → civilizaciones complejas.
- **Tasmania**: área muy pequeña → baja densidad → perdió tecnologías básicas.
- La relación **no es proporcional**, sino **acelerada**: pequeñas diferencias iniciales se amplifican.

> *"Among societies without technological contact, those with greater land area, and hence greater initial population, had faster technological change."*  
> — Kremer (1993, p. 708)
""")