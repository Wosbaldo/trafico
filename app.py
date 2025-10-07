import streamlit as st
from gnews import GNews

st.title("Noticias Locales por Departamento - El Salvador")

departamentos = [
    "Ahuachapán", "Santa Ana", "Sonsonate", "Chalatenango", "La Libertad",
    "San Salvador", "Cuscatlán", "La Paz", "Cabañas", "San Vicente",
    "Usulután", "San Miguel", "Morazán", "La Unión"
]

google_news = GNews(language='es', country='sv', max_results=5)

seleccionado = None

filas = [departamentos[:7], departamentos[7:]]

for fila in filas:
    cols = st.columns(7)
    for col, depto in zip(cols, fila):
        if col.button(depto):
            seleccionado = depto

if seleccionado:
    st.subheader(f"Noticias en {seleccionado}")
    noticias = google_news.get_news(seleccionado)

    if noticias:
        for noticia in noticias:
            st.markdown(f"### [{noticia['title']}]({noticia['url']})")
            st.write(noticia['description'])
            st.write(f"Fecha: {noticia['published date']}")
            st.write("---")
    else:
        st.write("No se encontraron noticias para este departamento.")
