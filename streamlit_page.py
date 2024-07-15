import streamlit as st
import modules.page_config as pc

# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
def cambiar_conf_pagina():
    json = pc.get_page_config_default()
    st.set_page_config(**json)

if __name__ == "__main__":
    cambiar_conf_pagina()