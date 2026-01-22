import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Anexo 3: Evidencia empírica del modelo de Kremer (1993)")

st.markdown("""
Este anexo presenta los datos históricos y la evidencia empírica central del paper de Kremer (1993), 
tal como aparecen en la **Tabla I** y la **Figura I** del artículo.
""")

# Datos históricos del paper (Tabla I)
data = {
    "Year": [-1_000_000, -300_000, -25_000, -10_000, -5000, -4000, -3000, -2000, -1000,
             -500, -200, 1, 200, 400, 600, 800, 1000, 1100, 1200, 1300, 1400, 1500,
             1600, 1650, 1700, 1750, 1800, 1850, 1875, 1900, 1920, 1930, 1940, 1950,
             1960, 1970, 1980, 1990],
    "Pop_millions": [0.125, 1, 3.34, 4, 5, 7, 14, 27, 50, 100, 150, 170, 190, 190, 200,
                     220, 265, 320, 360, 360, 350, 425, 545, 545, 610, 720, 900,
                     1200, 1325, 1625, 1813, 1987, 2213, 2516, 3019, 3693, 4450, 5333]
}
df_hist = pd.DataFrame(data)
df_hist["Pop"] = df_hist["Pop_millions"] / 1000  # en billones

# Calcular tasas de crecimiento anual
df_hist["Growth_rate"] = np.nan
for i in range(len(df_hist) - 1):
    dt = df_hist["Year"].iloc[i+1] - df_hist["Year"].iloc[i]
    if dt > 0:
        gr = (np.log(df_hist["Pop"].iloc[i+1]) - np.log(df_hist["Pop"].iloc[i])) / dt
        df_hist.loc[i, "Growth_rate"] = gr

st.header("1. Datos históricos de población mundial")

st.dataframe(df_hist[["Year", "Pop_millions", "Growth_rate"]].rename(columns={
    "Year": "Año",
    "Pop_millions": "Población (millones)",
    "Growth_rate": "Tasa de crecimiento anual"
}).style.format({
    "Población (millones)": "{:.0f}",
    "Tasa de crecimiento anual": "{:.6f}"
}))

st.caption("Fuente: Kremer (1993), Tabla I. Datos compilados de McEvedy & Jones (1978), Deevey (1960) y Naciones Unidas.")

st.header("2. Figura I del paper: Tasa de crecimiento vs. nivel de población")

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(
    df_hist["Pop"][:-1],
    df_hist["Growth_rate"][:-1],
    color="black",
    s=30,
    label="Datos históricos"
)

# Regresión lineal (sin intercepto, como en el paper)
X = df_hist["Pop"][:-1].values
y = df_hist["Growth_rate"][:-1].values
valid = (X > 0) & np.isfinite(y)
X = X[valid]
y = y[valid]

# Regresión sin intercepto: y = beta * x
beta = np.sum(X * y) / np.sum(X**2)
ax.plot(X, beta * X, color="red", label=f"Regresión: GRPOP = {beta:.3f} · POP")

ax.set_xlabel("Población (billones)")
ax.set_ylabel("Tasa de crecimiento anual")
ax.set_title("Figura I: Crecimiento poblacional vs. nivel de población")
ax.legend()
ax.grid(True, ls="--", lw=0.5)
st.pyplot(fig)

st.markdown(r"""
Kremer estima la regresión:
$$
\text{GRPOP}_t = \beta \cdot \text{POP}_t
$$
y encuentra $\beta \approx 0.00054$ (con POP en billones).  
Esta relación es **consistente con el modelo**:  
$$
\frac{\dot{P}}{P} = k P \quad \Rightarrow \quad \text{GRPOP} \propto \text{POP}
$$

> *"The growth rate of population has been approximately proportional to its level over most of history."*  
> — Kremer (1993, p. 682)
""")

st.header("3. ¿Por qué falla después de 1950?")

st.markdown("""
La regresión se ajusta bien hasta ~1950, pero **después de 1950 la tasa de crecimiento se estabiliza o cae**, 
a pesar de que la población sigue creciendo.

Esto no invalida el modelo, sino que **confirma su extensión**:  
cuando el ingreso per cápita supera un umbral, comienza la **transición demográfica** (fertilidad cae), 
rompiendo el ciclo malthusiano.
""")

st.header("Referencia")

st.markdown("""
- Kremer, M. (1993). *Population Growth and Technological Change: One Million B.C. to 1990*.  
  **The Quarterly Journal of Economics**, 108(3), 681–716. (Tabla I, Figura I, Sección IV.A)
""")