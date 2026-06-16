import streamlit as st
import streamlit.components.v1 as components
import os

st.title("🌳 ¿Quién posee la tierra?")

st.markdown("""
Esta sección presenta la distribución por género de las personas propietarias o poseedoras de los predios vinculados al proyecto de **ABC Colombia**.

Históricamente, el catastro tradicional muestra un fuerte desbalance donde los títulos formales de propiedad "en papel" se concentran mayoritariamente en los hombres.
""")

# Renderizar el mapa de propietarios
if os.path.exists("mapa_genero.html"):
    with open("mapa_genero.html", "r", encoding="utf-8") as f:
        html_mapa = f.read()
    components.html(html_mapa, height=550, scrolling=True)
else:
    st.warning("Asegúrate de subir el archivo 'mapa_genero.html' a la raíz de tu proyecto para visualizar el mapa.")
