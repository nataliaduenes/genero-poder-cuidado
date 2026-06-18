import streamlit as st
import os

st.title("💰 ¿En qué se materializan las decisiones?")

st.markdown("""
Las prioridades de inversión muestran cómo se traducen las decisiones económicas en los hogares rurales. 

Administrar el recurso monetario proveniente de los Pagos por Servicios Ambientales (PSA) impacta directamente en la sostenibilidad del ecosistema:
* **Administración Masculina:** Muestra una tendencia muy marcada hacia la adquisición de herramientas mecánicas (como motosierras). Esto genera un proceso contraproducente, acelerando la presión o destrucción del hábitat que originalmente se pactó proteger.
* **Administración Femenina o Mixta:** El destino del gasto se diversifica e inclina hacia insumos de conservación, soberanía alimentaria, mejoras del hogar y bienestar familiar.
""")

# Cargar la gráfica real de uso de recursos (motosierras)
if os.path.exists("prioridades_inversion_genero.png"):
    st.image(
        "prioridades_inversion_genero.png", 
        caption="Tendencias de inversión del incentivo económico según el género del decisor", 
        use_container_width=True
    )
else:
    st.info("Nota: Sube el archivo 'prioridades_inversión_género.png' a tu GitHub para visualizar la gráfica de tendencias de inversión.")
