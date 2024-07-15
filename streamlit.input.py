import streamlit as st

def crear_input():
    usuario = st.text_input(label="Usuario", max_chars=10)
    st.text(usuario)
    contra = st.text_input(label="Contraseña", max_chars=12, type='password')
    st.text(contra)
    parrafo = st.text_area(label="Descripción", height=8, max_chars=250)
    st.text(parrafo)
    numero = st.number_input(label="Edad", min_value=0, max_value=140, step=1, value=18)
    st.text(numero)
    fecha = st.date_input(label="Fecha de Nacimiento")
    st.text(fecha)
    color = st.color_picker(label="Escoga color")
    st.text(color)
    hora = st.time_input("Hora")
    st.text(hora)
    
if __name__ == "__main__":
    crear_input()