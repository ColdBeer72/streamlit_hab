import folium.map
import streamlit as st
import folium
import pandas as pd
import modules.openweather as ow
from streamlit_folium import st_folium

def main():
    st.title("Temperaturas en las ciudades de España")

    df = ow.get_weather_data()
    with st.expander(label="Datos - Temperaturas en las ciudades de España"):
        st.dataframe(df)

    map = folium.Map(location = df[df["name"]=="Madrid"][["lat", "lon"]], zoom_start=12)
    points = folium.map.FeatureGroup()

    for lat, lon, temp, nombre in df[["lat", "lon", "temp", "name"]].values:
        texto_a_mostrar = f"Ciudad: {nombre}, Temp: {temp}"
        points.add_child(folium.Marker(location=[lat, lon], popup=texto_a_mostrar))

    map.add_child(points)

    st_folium(fig=map)
        
if __name__ == "__main__":
    main()