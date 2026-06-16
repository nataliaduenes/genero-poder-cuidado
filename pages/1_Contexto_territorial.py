import streamlit as st
import os

st.title("📍 Contexto territorial")

st.markdown("""
Los acuerdos de conservación analizados se ubican estratégicamente en los municipios de:
- **Paya** (Boyacá)
- **Nunchía** (Casanare)
- **Yopal** (Casanare)

El interés central de este proyecto es comprender cómo las relaciones de género y las estructuras de poder preexistentes influyen de manera directa en las decisiones económicas y en la organización de las tareas de cuidado en los hogares rurales.
""")

# Cargar la gráfica comparativa inicial aquí
if os.path.exists("grafica_propiedad_encargado.png"):
    st.image(
        "grafica_propiedad_encargado.png", 
        caption="Comparativa general: Condición de Propiedad vs. Persona Encargada del Acuerdo", 
        use_container_width=True
    )
else:
    st.info("Nota: Sube el archivo 'grafica_propiedad_encargado.png' a tu GitHub para visualizar la gráfica en esta introducción.")
