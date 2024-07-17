import streamlit as st


def armar_sidebar_columnas():
    st.title("Usando Columnas, Solapas y Menús")
    columna1, columna2 = st.columns(2)
    columna1.subheader("Análisis de Datos")
    columna2.subheader("Modelo de Machine Learning")

    columna1.text("Hola hola hola")

    st.tabs(["Solapa 1", "Solapa 2", "Solapa 3"])
    columna2.tabs(["Tab1", "Tab2"])

    opciones_menu = ["Análisis de Datos",
                     "Ejecución modelo ML",
                     "Otros"]

    st.sidebar.subheader("OPCIONES")
    escogio = st.sidebar.selectbox(label="Menú",
                         options=opciones_menu)
    columna1.text(f"Escogió: {escogio}")

if __name__ == "__main__":
    armar_sidebar_columnas()