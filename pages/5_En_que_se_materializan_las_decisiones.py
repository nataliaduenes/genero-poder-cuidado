import streamlit as st
import os

st.title("💰 ¿En qué se materializan las decisiones?")

st.markdown("""
Las prioridades de inversión muestran cómo se traducen las decisiones económicas en los hogares rurales. 

Administrar el recurso monetario de los Pagos por Servicios Ambientales (PSA) impacta directamente en el ecosistema:
* **Administración Masculina:** Existe una tendencia marcada hacia la compra de herramientas mecánicas (como motosierras). Esto genera un proceso contraproducente, pues acelera la destrucción del hábitat que se planeaba proteger.
* **Administración Femenina / Mixta:** El gasto se diversifica hacia insumos de conservación, soberanía alimentaria y educación familiar.
""")

# Cargar la imagen del gráfico de barras
if os.path.exists("uso_recursos_genero-2.jpg"):
    st.image("uso_recursos_genero-2.jpg", caption="Tendencias de inversión del incentivo por género", use_column_width=True)
elif os.path.exists("grafica_propiedad_encargado.png"):
    st.image("grafica_propiedad_encargado.png", caption="Gráfica de Propiedad vs Encargado", use_column_width=True)
else:
    st.info("Sube el archivo de imagen 'uso_recursos_genero-2.jpg' a la raíz de tu GitHub para ver la gráfica en esta sección.")
