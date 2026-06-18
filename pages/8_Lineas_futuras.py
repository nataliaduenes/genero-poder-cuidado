import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .section-header { color: #1B4332; border-left: 5px solid #468432; padding-left: 10px; margin-top: 20px; margin-bottom: 20px; }
    .future-card { background-color: #E8F5E9; padding: 20px; border-radius: 8px; border-left: 4px solid #468432; margin-bottom: 15px; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<h2 class="section-header"> Líneas Futuras de Investigación</h2>',
    unsafe_allow_html=True,
)

st.subheader("Limitación Metodológica Actual")
st.warning(
    """
A la fecha, el proyecto dispone de información espacial precisa sobre las áreas específicas que las comunidades han destinado voluntariamente a la conservación. Sin embargo, no se cuenta con los registros del área total o poligonal completa de los predios. 

Debido a esta ausencia de datos de control, actualmente no es posible establecer relaciones estadísticas robustas o proporcionales entre el género de los tomadores de decisión y los resultados biofísicos o ambientales finales a escala predial.
"""
)

st.markdown(
    """
<div class="future-card">
    <strong>🚀 El Siguiente Eje Estratégico:</strong><br>
    Esta limitación constituye la base de la futura agenda de investigación. El próximo paso requiere la integración total de los datos del Catastro Multipropósito para cruzar los polígonos completos de propiedad con los mapas de monitoreo de cobertura vegetal. Solo así se podrá cuantificar el impacto porcentual neto del liderazgo femenino frente a la mitigación del cambio climático y la deforestación.
</div>
""",
    unsafe_allow_html=True,
)
