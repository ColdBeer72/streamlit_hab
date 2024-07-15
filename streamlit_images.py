import streamlit as st
#!pip install image
from PIL import Image

def mostrar_imagenes():
    # data/curiosidades-del-oso-panda-1280x720x80xX.jpg
    imagen = Image.open("data/curiosidades-del-oso-panda-1280x720x80xX.jpg")

    st.image(image=imagen, caption="Foto de un Oso Panda")

if __name__ == "__main__":
    mostrar_imagenes()