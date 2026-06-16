import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

st.title("⚖️ ¿Cómo se distribuye el poder?")

st.markdown("""
La relación entre propiedad y representación permite explorar las dinámicas de poder presentes dentro de los hogares rurales vinculados al proyecto.

A través del lente del **Feminismo de Datos**, esta matriz visualiza el número de personas que retuvieron, cedieron o delegaron su capacidad de decisión:
""")

# Datos exactos de la imagen image_091b3a.png
datos_matriz = {
    'Mujer': [97.9, 2.4, 38.2],
    'Hombre': [2.1, 96.3, 32.4],
    'Ambos': [0.0, 1.2, 29.4]
}
indices_propietario = ['Mujer', 'Hombre', 'Ambos']
df_transicion = pd.DataFrame(datos_matriz, index=indices_propietario)

# Paleta corporativa oficial: Mujer (#468432), Hombre (#FFA02E), Ambos (#9AD872), Mínimo (#FFEF91)
colores_proyecto = ["#FFEF91", "#9AD872", "#FFA02E", "#468432"]
cmap_personalizado = LinearSegmentedColormap.from_list("ColoresProyecto", colores_proyecto, N=256)

# Crear columnas para organizar texto y gráfico
col_text, col_graph = st.columns([1, 1.2])

with col_text:
    st.write("""
    **Análisis de Hallazgos:**
    * **Propiedad Individual:** Si la tierra está a nombre de un solo género (Mujer u Hombre), la firma del acuerdo casi no se delega (97.9% y 96.3%).
    * **Propiedad Compartida ("Ambos"):** Cuando el papel es mixto, la responsabilidad física prefiere individualizarse. En esa transición, **las mujeres asumen un rol líder con el 38.2% de las firmas**, superando notablemente a los hombres (32.4%).
    """)

with col_graph:
    fig, ax = plt.subplots(figsize=(6, 4.5))
    sns.set_theme(style="white")
    sns.heatmap(df_transicion, annot=True, fmt=".1f", cmap=cmap_personalizado, linewidths=2, linecolor='white',
                cbar_kws={'label': 'Porcentaje (%)'}, annot_kws={"size": 11, "weight": "bold"})
    
    plt.title('Matriz de transferencia de poder', fontsize=12, fontweight='bold', pad=15)
    plt.ylabel('ORIGEN: Género del Propietario Legal', fontsize=9, fontweight='bold')
    plt.xlabel('DESTINO: A quién se le dejó / delegó la firma', fontsize=9, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
