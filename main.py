import streamlit as st
st.set_page_config(page_title="Adael Vega Tareas 4º Año D")

col1,col2,col3 = st.columns(3)

with col1:
	st.title("tareas 4º año D")

file_path = r"trabajo escolar (1).pdf"
with col1:
	download_setup = st.download_button("Download", open(file_path, "rb"), file_name="trabajo escolar.pdf")





