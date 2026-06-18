import streamlit as st
import os

st.title("💰 ¿En qué se materializan las decisiones?")

st.markdown("""
Las prioridades de inversión muestran cómo se traducen las decisiones económicas en los hogares rurales. 

Administrar el recurso monetario proveniente de los Pagos por Servicios Ambientales (PSA) impacta directamente en la sostenibilidad del ecosistema:
* **La producción agropecuaria es la principal prioridad de inversión para todos los grupos. No obstante, las decisiones lideradas por mujeres muestran una mayor orientación hacia salud, educación, bienestar familiar y fortalecimiento del hogar, mientras que las lideradas por hombres se concentran más en infraestructura productiva, maquinaria y activos del predio.


Los resultados sugieren que la capacidad de decisión influye en las prioridades de inversión y, por tanto, en las estrategias de sostenibilidad y cuidado desarrolladas en los territorios rurales.""")

# Cargar la gráfica real de uso de recursos (motosierras)
if os.path.exists("prioridades_inversion_genero.png"):
    st.image(
        "prioridades_inversion_genero.png", 
        caption="Tendencias de inversión del incentivo económico según el género del decisor", 
        use_container_width=True
    )
else:
    st.info("Nota: Sube el archivo 'prioridades_inversión_género.png' a tu GitHub para visualizar la gráfica de tendencias de inversión.")
