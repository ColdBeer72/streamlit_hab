# pip install streamlit
import streamlit as st
import pandas as pd
import requests

def cargar_datos():
    pass

def mostrar_textos():
    st.title("Conociendo Streamlit en :orange[Hack a Boss]")
    st.header("Bootcamp de Data Science e Inteligencia Artificial")
    st.subheader("Comisión 10")
    st.text("Rosalía")
    st.text("Alexia")
    st.text("Diego")
    nombre = "Manuel"
    st.text(nombre)
    st.markdown("# Título en MarkDown")
    st.success("Datos ingresados correctamente!!!")
    st.warning("Escriba una contraseña más compleja")
    st.info("Escriba la información necesaria")
    st.error("Edad no válida")
    try:
        resultado = 4/0
    except Exception as ex:
        st.exception(ex)
        
    st.write("Me encanta la ciencia de datos :)")
    st.write("### Titulo write")

    df = pd.read_csv("data/AccidentesBicicletas_2021.csv", sep = ";")
    #st.dataframe(df)

    df = df.style.highlight_null(color="orange")
    st.dataframe(df)

    url = "https://api.frankfurter.app/latest"
    response = requests.get(url=url)
    st.json(response.json())

    

if __name__ == "__main__":  # especificando cuál es la función principal
                            # que se empieza a ejecutar cuando hacemos RUN
                            # a este archivo.py
    mostrar_textos()