import streamlit as st


def crear_botones():
    st.title("Botones y Sliders")

    boton_aceptar = st.button(label="Aceptar")

    if boton_aceptar == True:
        st.text("Apretó el botón ACEPTAR")

    # Radio Button
    # Elegir 1 entre varias opciones

    opciones = ["Soltero", "Casado", "Divorciado"]
    estado_civil = st.radio(label="Estado civil",
             options=opciones,
             index=0,
             horizontal=False)
    st.text(f"Estado civil seleccionado: {estado_civil}")
    if estado_civil == "Soltero":
        st.info("Su estado civil es SOLTERO")
    elif estado_civil == "Casado":
        st.info("Su estado civil es CASADO")
    else:
        st.info("Su estado civil es OTRO")

    # Checkbox
    # Elegir una opción o no

    aceptar = st.checkbox("Aceptar términos y condiciones")
    if aceptar:
        st.success("Usted aceptó los Términos y Condiciones")
    else:
        st.warning("Usted no aceptó los Términos y Condiciones")

    # SelectBox -> MultiSelect
    # Elegir varias opciones entre muchas

    librerias = ["numpy", "pandas", "random", "datetime", "sklearn"]
    librerias_seleccionadas = st.multiselect(label="Librerías", options=librerias)
    st.text(librerias_seleccionadas)

    if "random" in librerias_seleccionadas:
        st.info("Seguramente vas a generar número aleatorios")

    # SelectBox -> Simple
    # Elegir UNA opciones entre muchas
    
    libreria_seleccionada = st.selectbox(label="Librería", options=librerias)
    st.text(libreria_seleccionada)

    # Slider
    edad = st.slider(label="Edad", min_value=0, max_value=99, value=65, step=1)
    st.text(f"Su edad es {edad}")

    calificaciones = ["Excelente", "Muy Bien", "Bien", "Regular", "Mal"]
    calificacion = st.select_slider(label="Calificación", options=calificaciones)

    
if __name__ == "__main__":
    crear_botones()