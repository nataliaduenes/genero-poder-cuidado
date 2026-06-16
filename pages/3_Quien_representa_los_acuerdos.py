import streamlit as st
import streamlit.components.v1 as components
import os

st.title("✍️ ¿Quién representa los acuerdos?")

st.markdown("""
La representación efectiva de los acuerdos permite aproximarse a quién ejerce la gestión cotidiana y administrativa de los procesos de conservación.

Al analizar quién decide estar presente y firmar el acuerdo voluntario de Pagos por Servicios Ambientales (PSA), observamos la fuerza y el liderazgo real de las comunidades en el territorio, independientemente de quién tenga las escrituras.
""")

# Renderizar el mapa de personas a cargo
if os.path.exists("mapa_genero_a_cargo.html"):
    with open("mapa_genero_a_cargo.html", "r", encoding="utf-8") as f:
        html_mapa_cargo = f.read()
    components.html(html_mapa_cargo, height=550, scrolling=True)
else:
    st.warning("Asegúrate de subir el archivo 'mapa_genero_a_cargo.html' a la raíz de tu proyecto para visualizar el mapa.")
