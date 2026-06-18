import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .section-header { color: #1B4332; border-left: 5px solid #468432; padding-left: 10px; margin-top: 20px; margin-bottom: 20px; }
    .quote-card { background-color: #F8F9FA; padding: 20px; border-radius: 8px; border-left: 4px solid #FFA02E; margin-bottom: 15px; font-style: italic; color: #403D39; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<h2 class="section-header"> Reflexiones desde el Territorio</h2>',
    unsafe_allow_html=True,
)

st.write(
    """
La historia fundamental que emerge de este análisis no se reduce a medir matemáticamente quién conserva más porciones de tierra. 
El verdadero núcleo del estudio radica en visibilizar **cómo las relaciones de poder preexistentes influyen de manera directa en la materialización de las decisiones económicas** dentro de las comunidades rurales.
"""
)

st.markdown(
    """
<div class="quote-card">
    "Los resultados sugieren que las prioridades asociadas al cuidado y al bienestar familiar están latentes en el territorio, pero su capacidad real de concretarse y financiarse depende críticamente de quién posee la tierra en papel y quién ejerce la representación efectiva en la firma de los acuerdos."
</div>
""",
    unsafe_allow_html=True,
)

st.subheader("Evidencia desde los Círculos de Participación")
st.write(
    """
La experiencia recopilada a través de los **círculos de mujeres y hombres** desarrollados a lo largo del proyecto evidencia que las prácticas de conservación y cuidado no responden únicamente a preferencias o deseos individuales. 

Estas decisiones están mediadas, y muchas veces limitadas, por las dinámicas de poder, la capacidad de negociación intra-hogar y el acceso real a la administración de los recursos económicos dentro de los hogares rurales de Paya, Nunchía y Yopal.
"""
)
