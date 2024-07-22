import streamlit as st
import plotly.express as px
# from modules.ml_func import *
import modules.ml_func
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def main():
    st.title("Modelo de Machine Learning sobre la contaminación de CO2")
    st.write("Bienvenido a la aplicación web del modelo de machine learning sobre las Emisiones de Carbono (CO2)")
    st.write("Los datos de este proyecto fueron extraídos de:")
    st.markdown("[Open Canadá](https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64)")

    lista_tabs = ["Exploratory Data Analysis", "Machine Learning Model", "Data"]
    tab1, tab2, tab3 = st.tabs(lista_tabs)

    df = modules.ml_func.read_data()

    #***********Exploratory Data Analysis************
    fig_scatter = px.scatter(data_frame=df,
                             x="Fuel Consumption City",
                             y="CO2 Emissions",
                             color="Fuel Type")
    st.plotly_chart(fig_scatter)

    #**********Modelo de Machine Learning
    fuel_types= df["Fuel Type"].unique()
    fuel_type_selected = tab2.radio(label="Seleccione el tipo de combustible", options=fuel_types,
               index=0, horizontal=True)
    X_scaler: MinMaxScaler
    y_scaler: MinMaxScaler
    X_scaler, y_scaler, model = load_pkls(flue_type_selected)

    min_model_year, min_engine_size, min_cylinders, min_fuel_consumption = X_scaler.data_min_
    max_model_year, max_engine_size, max_cylinders, max_fuel_consumption = X_scaler.data_max_
    min_co2_emission = y_scaler.data_min_
    max_co2_emission = y_scaler.data_max_

    tab2col1, tab2col2 = tab2.columns(2)
    model_year = tab2col1.slider(label="Model Year",
                    min_value=int(min_model_year),
                    max_value=int(max_model_year),
                    step=1)
    engine_size = tab2col2.slider(label="Engine Size",
                    min_value=float(min_engine_size),
                    max_value=float(max_engine_size),
                    step=0.1)
    cylinders = tab2col1.slider(label="Cylinders",
                    min_value=int(min_cylinders),
                    max_value=int(max_cylinders),
                    step=1)
    fuel_consumption = tab2col2.slider(label="Fuel Consumption City",
                    min_value=float(min_fuel_consumption),
                    max_value=float(max_fuel_consumption),
                    step=0.1)

    data = np.array([model_year, engine_size, cylinders, fuel_consumption])
    data = X_scaler.transform(data)
    prediction = model.predict(data)
    prediction = y_scaler.inverse_transform(prediction)

    tab2col2.dataframe(data=prediction)
    
    #**********DATA************
    tab3.dataframe(df)
    

if __name__ == "__main__":
    main()