import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

st.title("Simulación del Modelo de Kremer (1993)")
st.markdown("""
Este modelo muestra cómo **más población → más inventores → más tecnología → más población**, 
generando crecimiento *super-exponencial* hasta la transición demográfica reciente.
""")
st.markdown("""
## 🧠 ¿Qué explica esta simulación?

Esta aplicación recrea el modelo central del artículo **“Population Growth and Technological Change: One Million B.C. to 1990”** de **Michael Kremer (1993)**.

### 🎯 Objetivo del modelo
Kremer propone una explicación unificada del crecimiento demográfico mundial durante casi un millón de años, basada en dos ideas clave:

1. **La tecnología es no rival**: una innovación puede ser usada por todos sin agotarse. Por lo tanto, **más personas → más inventores → más tecnología**.
2. **La población está limitada por la tecnología disponible** (visión malthusiana): mejor tecnología → más alimentos → más personas pueden sobrevivir.

### 🔁 Mecanismo central
Estas dos fuerzas se retroalimentan:
> **Población ↑ → Innovación ↑ → Tecnología ↑ → Población ↑**

Este ciclo genera un **crecimiento super-exponencial**: no solo la población crece, sino que su *tasa de crecimiento también aumenta con el tiempo*.

### ⚖️ ¿Dónde está el equilibrio?
- En el largo plazo histórico (hasta ~1950), **no hay equilibrio estable**: el sistema se acelera continuamente.
- Solo recientemente, con el aumento del ingreso per cápita, surge la **transición demográfica**: las familias eligen tener menos hijos, rompiendo el ciclo malthusiano.
- Pero durante la mayor parte de la historia humana, **la población fue el motor —y no el freno— del progreso tecnológico**.

### 🌍 Evidencia empírica
Kremer muestra que:
- La tasa de crecimiento poblacional ha sido aproximadamente **proporcional al nivel de población** (ver Figura I del paper).
- Entre sociedades aisladas (ej. Tasmania vs. Viejo Mundo), **las más pobladas desarrollaron más tecnología**.

Esta simulación te permite explorar esos mecanismos en tiempo real.
""")

# === Instrucciones interactivas ===
with st.expander("ℹ️ ¿Cómo usar esta simulación?"):
    st.markdown("""
    **Parámetros principales:**
    - **`g` (productividad de investigación)**: Qué tan eficaz es cada persona generando innovación.  
      Valores típicos: entre **0.005 y 0.01**. Si es muy bajo, el crecimiento es lento; si es muy alto, explota antes de 1950.
    - **`α`**: Elasticidad de la tierra en la producción (normalmente **0.6–0.8**). Cuanto más alto, más limitada está la población por recursos.
    - **Población inicial global**: En **billones**. Kremer estima ~4 millones en -10,000 → **0.004 billones**.
    
    **Controles:**
    - Marca ✅ *"Incluir transición demográfica"* para simular la caída en tasas de crecimiento tras 1950.
    - Cambia la población inicial para ver cómo pequeñas diferencias se amplifican con el tiempo.
    
    **Nota:** El modelo es *super-exponencial*: cambios pequeños al inicio tienen enormes efectos a largo plazo.
    """)

# === Botón de parámetros calibrados ===
if st.button("🎯 Usar parámetros calibrados (Kremer, 1993)"):
    st.session_state["g_slider"] = 0.00016
    st.session_state["alpha_slider"] = 0.7
    st.session_state["pop0_global_input"] = 0.004
    st.session_state["P0_old_input"] = 50.0
    st.session_state["P0_tas_input"] = 0.004

# Inicializar estado con las CLAVES DE LOS WIDGETS
if "g_slider" not in st.session_state:
    st.session_state["g_slider"] = 0.005
if "alpha_slider" not in st.session_state:
    st.session_state["alpha_slider"] = 0.7
if "pop0_global_input" not in st.session_state:
    st.session_state["pop0_global_input"] = 0.004
if "P0_old_input" not in st.session_state:
    st.session_state["P0_old_input"] = 50.0
if "P0_tas_input" not in st.session_state:
    st.session_state["P0_tas_input"] = 0.004

# Parámetros interactivos (usan las mismas claves)
col1, col2 = st.columns(2)
with col1:
    g = st.slider(
        "Productividad de investigación (g)",
        min_value=0.001,
        max_value=0.02,
        value=st.session_state["g_slider"],
        step=0.001,
        key="g_slider"
    )
    alpha = st.slider(
        "Parámetro α (elasticidad tierra)",
        min_value=0.5,
        max_value=0.9,
        value=st.session_state["alpha_slider"],
        step=0.05,
        key="alpha_slider"
    )
with col2:
    include_dem_trans = st.checkbox("Incluir transición demográfica (post-1950)", True)
    pop0_global = st.number_input(
        "Población inicial global (billones) en -10,000",
        min_value=0.0001,
        max_value=0.1,
        value=st.session_state["pop0_global_input"],
        step=0.001,
        format="%.4f",
        key="pop0_global_input"
    )

# Validación visual
if pop0_global < 0.001:
    st.warning("⚠️ Población inicial muy baja (<1 millón). El crecimiento será extremadamente lento.")

# === Simulación global ===
years_sim = np.arange(-10000, 2000, 10)
P_global = np.full_like(years_sim, pop0_global, dtype=float)
dt = 10

# Integración numérica robusta con detección de explosión
explosion_detected = False
for i in range(1, len(years_sim)):
    dPdt = (g / (1 - alpha)) * P_global[i-1]**2
    P_global[i] = P_global[i-1] + dPdt * dt
    
    if np.isinf(P_global[i]) or np.isnan(P_global[i]):
        st.warning(f"⚠️ Explosión detectada en el año {int(years_sim[i])}. La población creció demasiado rápido.")
        explosion_detected = True
        for j in range(i, len(years_sim)):
            P_global[j] = P_global[i-1]
        break

    if P_global[i] <= 0:
        P_global[i] = 1e-12

# Aplicar transición demográfica suave (solo después de 1950)
if include_dem_trans and not explosion_detected:
    for i, y in enumerate(years_sim):
        if y >= 1950:
            years_since_1950 = y - 1950
            reduction_factor = max(0.2, 1 - 0.015 * years_since_1950)
            if i > 0:
                current_growth = np.log(P_global[i] / P_global[i-1])
                adjusted_growth = current_growth * reduction_factor
                P_global[i] = P_global[i-1] * np.exp(adjusted_growth)

# === Gráfico 1: Visión general (todo el rango) ===
fig1_general, ax1_general = plt.subplots(figsize=(8, 4))
ax1_general.plot(df_hist["Year"], df_hist["Pop"], 'o-', label="Datos históricos (Kremer)", color="black", markersize=3)
ax1_general.plot(years_sim, P_global, '-', label="Simulación global", color="red")
ax1_general.set_yscale("log")
ax1_general.set_xlabel("Año (negativo = A.C., positivo = D.C.)")
ax1_general.set_ylabel("Población (billones)")
ax1_general.set_title("Evolución global de la población (visión general)")

ax1_general.set_xticks([-1000000, -500000, -100000, -10000, 0, 1000, 2000])
ax1_general.set_xticklabels(["-1M", "-500K", "-100K", "-10K", "0", "1K", "2K"], rotation=45)

ax1_general.legend()
ax1_general.grid(True, which="both", ls="--", lw=0.5)
st.pyplot(fig1_general)

# === Gráfico 2: Zoom en los últimos 12,000 años ===
fig1_zoom, ax1_zoom = plt.subplots(figsize=(8, 4))

mask_zoom = (df_hist["Year"] >= -10000) & (df_hist["Year"] <= 2000)
df_hist_zoom = df_hist[mask_zoom].copy()

mask_sim_zoom = (years_sim >= -10000) & (years_sim <= 2000)
years_sim_zoom = years_sim[mask_sim_zoom]
P_global_zoom = P_global[mask_sim_zoom]

ax1_zoom.plot(df_hist_zoom["Year"], df_hist_zoom["Pop"], 'o-', label="Datos históricos (Kremer)", color="black", markersize=4)
ax1_zoom.plot(years_sim_zoom, P_global_zoom, '-', label="Simulación global", color="red")

if st.checkbox("Usar escala logarítmica (zoom)", True):
    ax1_zoom.set_yscale("log")
    ax1_zoom.text(0.05, 0.95, 
                 "Escala log → cada salto = multiplicación",
                 transform=ax1_zoom.transAxes, fontsize=8, verticalalignment='top', bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.5))
else:
    ax1_zoom.set_yscale("linear")

ax1_zoom.set_xlabel("Año (negativo = A.C., positivo = D.C.)")
ax1_zoom.set_ylabel("Población (billones)")
ax1_zoom.set_title("Zoom: Evolución de la población (últimos 12,000 años)")

ax1_zoom.set_xticks([-10000, -5000, -1000, 0, 500, 1000, 1500, 1900, 2000])
ax1_zoom.set_xticklabels(["-10K", "-5K", "-1K", "0", "500", "1K", "1.5K", "1900", "2000"], rotation=45)

ax1_zoom.legend()
ax1_zoom.grid(True, which="both", ls="--", lw=0.5)
st.pyplot(fig1_zoom)

# Mensaje dinámico según g
if g < 0.005:
    st.warning("⚠️ g muy bajo: el crecimiento será muy lento.")
elif g > 0.015:
    st.warning("⚠️ g muy alto: la población explotará antes de 1950.")

# === Gráfico 2: Tasa de crecimiento vs población (CORREGIDO) ===
log_P = np.log(P_global)
dlogP = np.diff(log_P)
dt_years = np.diff(years_sim)
gr_sim_full = dlogP / dt_years
P_mid = P_global[:-1]

valid = (P_mid > 1e-10) & (dt_years != 0) & np.isfinite(gr_sim_full)
P_plot = P_mid[valid]
gr_plot = gr_sim_full[valid]

fig2, ax2 = plt.subplots(figsize=(6, 4))
hist_gr = np.diff(np.log(df_hist["Pop"])) / np.diff(df_hist["Year"])
hist_valid = (df_hist["Pop"].iloc[:-1] > 0) & np.isfinite(hist_gr)
ax2.scatter(
    df_hist["Pop"].iloc[:-1][hist_valid],
    hist_gr[hist_valid],
    label="Datos históricos",
    color="black",
    s=15
)
ax2.plot(P_plot, gr_plot, label="Simulación", color="red")
ax2.set_xlabel("Población (billones)")
ax2.set_ylabel("Tasa de crecimiento anual")
ax2.set_title("Tasa de crecimiento vs. nivel de población")
ax2.legend()
ax2.grid(True, ls="--", lw=0.5)
st.pyplot(fig2)

# === Sección comparativa: Regiones aisladas ===
st.subheader("🌍 Comparación entre regiones aisladas (sin contacto tecnológico)")
with st.expander("ℹ️ ¿Qué muestra esta simulación?"):
    st.markdown("""
    **Contexto histórico (Kremer, 1993, Sección IV.B):**  
    Hasta 1500, regiones como Tasmania, las Américas y el Viejo Mundo estuvieron aisladas.  
    El modelo predice que **la región con mayor población inicial generará más innovación** (más inventores), lo que lleva a:
    - Mayor crecimiento poblacional.
    - Mayor densidad tecnológica (aquí proxieda por la población misma).

    **En esta simulación:**  
    - Ambas regiones usan los mismos parámetros (`g`, `α`).  
    - Solo difieren en su **población inicial**.  
    - No hay intercambio de ideas (tecnología no se difunde).  
    - Observamos cómo pequeñas diferencias iniciales se amplifican con el tiempo.

    **Ejemplo real:**  
    - Viejo Mundo (1500): ~407 millones → civilizaciones avanzadas.  
    - Tasmania (1500): ~1,200–5,000 personas → perdió tecnologías como hacer fuego.
    """)

st.write("Simulamos dos sociedades independientes desde **10,000 A.C. hasta 1500 D.C.**")

col3, col4 = st.columns(2)
with col3:
    P0_old_millions = st.number_input(
        "Población inicial: Viejo Mundo (millones)",
        min_value=1.0,
        max_value=1000.0,
        value=st.session_state["P0_old_input"],
        step=10.0,
        key="P0_old_input"
    )
with col4:
    P0_tas_millions = st.number_input(
        "Población inicial: Tasmania (millones)",
        min_value=0.001,
        max_value=10.0,
        value=st.session_state["P0_tas_input"],
        step=0.001,
        format="%.3f",
        key="P0_tas_input"
    )

# Convertir a billones
P0_old = P0_old_millions / 1000
P0_tas = P0_tas_millions / 1000

# Simulación aislada (hasta 1500)
years_iso = np.arange(-10000, 1500, 10)
P_old = np.full_like(years_iso, P0_old, dtype=float)
P_tas = np.full_like(years_iso, P0_tas, dtype=float)

def simulate_population(P0, years, g, alpha, dt=10):
    P = np.full_like(years, P0, dtype=float)
    for i in range(1, len(years)):
        dPdt = (g / (1 - alpha)) * P[i-1]**2
        P[i] = P[i-1] + dPdt * dt
        if np.isinf(P[i]) or np.isnan(P[i]) or P[i] > 1000:
            P[i] = 1000
            break
        if P[i] < 1e-12:
            P[i] = 1e-12
    return P

P_old = simulate_population(P0_old, years_iso, g, alpha)
P_tas = simulate_population(P0_tas, years_iso, g, alpha)

# Gráfico 3: Comparación de trayectorias
fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.plot(years_iso, P_old, label=f"Viejo Mundo ({P0_old_millions:.0f}M)", color="blue")
ax3.plot(years_iso, P_tas, label=f"Tasmania ({P0_tas_millions:.3f}M)", color="orange")
ax3.set_yscale("log")
ax3.set_xlabel("Año (negativo = A.C., positivo = D.C.)")
ax3.set_ylabel("Población (billones, escala log)")
ax3.set_title("Evolución de poblaciones aisladas (10,000 A.C. – 1500 D.C.)")
ax3.set_xticks([-10000, -5000, -1000, 0, 500, 1000, 1500])
ax3.set_xticklabels(["-10K", "-5K", "-1K", "0", "500", "1K", "1500"], rotation=45)
ax3.legend()
ax3.grid(True, which="both", ls="--", lw=0.5)
st.pyplot(fig3)

# Gráfico 4: Brecha tecnológica relativa
ratio = np.divide(P_old, P_tas, out=np.ones_like(P_old), where=P_tas != 0)
fig4, ax4 = plt.subplots(figsize=(6, 4))
ax4.plot(years_iso, ratio, color="purple")
ax4.set_yscale("log")
ax4.set_xlabel("Año")
ax4.set_ylabel("Relación (Viejo Mundo / Tasmania)")
ax4.set_title("Brecha tecnológica relativa (proxy: relación de poblaciones)")
ax4.set_xticks([-10000, -5000, -1000, 0, 500, 1000, 1500])
ax4.set_xticklabels(["-10K", "-5K", "-1K", "0", "500", "1K", "1500"], rotation=45)
ax4.grid(True, which="both", ls="--", lw=0.5)
st.pyplot(fig4)

st.caption("💡 En ausencia de contacto, la región con mayor población inicial acumula ventaja tecnológica mucho más rápido. "
          "Esto explica por qué Tasmania perdió tecnologías básicas, mientras el Viejo Mundo desarrolló civilizaciones complejas.")

st.markdown("""
### 📉 ¿Por qué se desacelera el crecimiento poblacional si la tecnología sigue avanzando?

Durante casi toda la historia humana, más tecnología → más ingreso → más hijos → más población.  
Pero **a partir del siglo XX**, en los países más ricos, esta relación se invierte:

> **Más ingreso → menos hijos por familia → crecimiento poblacional se desacelera.**

Esto no es un colapso malthusiano (falta de recursos), sino una **transición demográfica** causada por:
- Mayor costo de oportunidad del tiempo de las mujeres (educación, empleo).
- Menor mortalidad infantil → no se necesitan tantos hijos para asegurar supervivencia.
- Preferencia por invertir en la **calidad** (educación, salud) de pocos hijos, no en la **cantidad**.

Como dice Kremer (1993, p. 698):
> *“The generalized model predicts that population growth rates will eventually decline—not due to overpopulation and environmental collapse, but to increased income and declining fertility.”*

Esta gráfica compara dos escenarios desde 1900:
- **Con transición demográfica**: reproduce la realidad histórica (crecimiento se frena tras ~1960).
- **Sin transición**: el modelo simple predice aceleración continua (¡incluso explosión!).

La diferencia entre ambas líneas muestra **el poder de la prosperidad para cambiar los incentivos reproductivos**.
""")

# === Gráfico 3: Desaceleración reciente (1900–2000) ===
st.subheader("📉 Desaceleración del crecimiento poblacional (1900–2000)")

years_recent = np.arange(1900, 2001, 1)
P_with_trans = np.full_like(years_recent, P_global[np.argmin(np.abs(years_sim - 1900))], dtype=float)
P_without_trans = np.full_like(years_recent, P_global[np.argmin(np.abs(years_sim - 1900))], dtype=float)

P_1900 = P_global[np.argmin(np.abs(years_sim - 1900))]
P_with_trans[0] = P_1900
P_without_trans[0] = P_1900

# Simular sin transición
for i in range(1, len(years_recent)):
    dPdt = (g / (1 - alpha)) * P_without_trans[i-1]**2
    P_without_trans[i] = P_without_trans[i-1] + dPdt * 1
    if P_without_trans[i] > 1000:
        P_without_trans[i] = 1000
        break

# Simular con transición
for i in range(1, len(years_recent)):
    dPdt = (g / (1 - alpha)) * P_with_trans[i-1]**2
    P_with_trans[i] = P_with_trans[i-1] + dPdt * 1
    if P_with_trans[i] > 1000:
        P_with_trans[i] = 1000
        break
    if years_recent[i] >= 1950:
        years_since_1950 = years_recent[i] - 1950
        reduction_factor = max(0.2, 1 - 0.015 * years_since_1950)
        current_growth = np.log(P_with_trans[i] / P_with_trans[i-1])
        adjusted_growth = current_growth * reduction_factor
        P_with_trans[i] = P_with_trans[i-1] * np.exp(adjusted_growth)

# Calcular tasas de crecimiento (%/año)
gr_with = np.diff(np.log(P_with_trans)) * 100
gr_without = np.diff(np.log(P_without_trans)) * 100

mask_hist = (df_hist["Year"] >= 1900) & (df_hist["Year"] <= 2000)
df_hist_recent = df_hist[mask_hist].copy()
gr_hist = np.diff(np.log(df_hist_recent["Pop"])) / np.diff(df_hist_recent["Year"]) * 100

fig_recent, ax_recent = plt.subplots(figsize=(8, 4))
ax_recent.plot(
    df_hist_recent["Year"].iloc[:-1], gr_hist,
    'o-', color="black", label="Datos históricos", markersize=4
)
ax_recent.plot(
    years_recent[:-1], gr_with,
    '-', color="green", label="Con transición demográfica"
)
ax_recent.plot(
    years_recent[:-1], gr_without,
    '--', color="red", label="Sin transición demográfica"
)

ax_recent.set_xlabel("Año")
ax_recent.set_ylabel("Tasa de crecimiento anual (%)")
ax_recent.set_title("Desaceleración del crecimiento poblacional (1900–2000)")
ax_recent.legend()
ax_recent.grid(True, ls="--", lw=0.5)
st.pyplot(fig_recent)

st.caption("💡 La transición demográfica explica por qué el crecimiento poblacional se desacelera tras ~1960, "
          "a pesar de que la tecnología sigue avanzando. Sin ella, el modelo predice aceleración continua.")