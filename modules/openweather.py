import requests
import pandas as pd
from time import sleep
import streamlit as st

@st.cache_data
def get_weather_data():
    url = "https://www.ign.es/web/ane-datos-geograficos/-/datos-geograficos/datosPoblacion?tipoBusqueda=capitales"
    lista_tablas_df = pd.read_html(url)
    df = lista_tablas_df[1]


    df["Lat ETRS89"] = df["Lat ETRS89"]/100000000
    df["Lon ETRS89"] = df["Lon ETRS89"]/100000000

    api_key = "cd31574dc65a379909d4f921033a7e96"
    endpoint = f"https://api.openweathermap.org/data/2.5/weather"

    lista_weather_data = []
    for lat, lon in df[["Lat ETRS89", "Lon ETRS89"]].values:
        params = {"appid" : api_key,
                "lat"   : lat,
                "lon"   : lon,
                "units" : "metric"}
        response = requests.get(url = endpoint, params = params)
        data = response.json()
        
        try:
            description = data["weather"][0]["description"]
            temp        = data["main"]["temp"]
            feels_like  = data["main"]["feels_like"]
            temp_min    = data["main"]["temp_min"]
            temp_max    = data["main"]["temp_max"]
            pressure    = data["main"]["pressure"]
            humidity    = data["main"]["humidity"]
            wind_speed  = data["wind"]["speed"]
            dt          = data["dt"]
            lat         = data["coord"]["lat"]
            lon         = data["coord"]["lon"]
            name        = data["name"]
        except Exception as ex:
            print("Error")

        lista_weather_data.append([description, temp, feels_like, temp_min, temp_max, pressure,
                                  humidity, wind_speed, dt, lat, lon, name])

        sleep(0.1)

    df = pd.DataFrame(data = lista_weather_data, columns=["description", "temp", "feels_like", "temp_min",
                                                          "temp_max", "pressure", "humidity",
                                                          "wind_speed", "dt", "lat", "lon", "name"])
    return df        

if __name__ == "__main__":
    df = get_weather_data()
    print(df)