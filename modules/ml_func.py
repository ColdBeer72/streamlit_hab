import os
import pandas as pd
import pickle
import sklearn

def read_data():
    os.chdir("/home/coldbeer/Hackaboss/streamlit_hab/sources")
    csv_files = [file for file in os.listdir() if file.endswith("csv") and file.startswith("MY")]
    lista_df = []
    for file in csv_files:
        df = pd.read_csv(file, encoding="latin1", header=1)
        df = df.iloc[:, :13]
        df.dropna(inplace=True)

        df.columns = ["Model Year", "Make", "Model", "Vehicle Class", "Engine Size", "Cylinders",
                       "Transmission", "Fuel Type", "Fuel Consumption City", "Fuel Consumption Hwy",
                       "Fuel Consumption Comb", "Fuel Consumption Comb (mpg)", "CO2 Emissions"]

        int_columns = ["Model Year", "CO2 Emissions"]
        float_columns = ["Engine Size", "Cylinders", "Fuel Consumption City", "Fuel Consumption Hwy",
                       "Fuel Consumption Comb", "Fuel Consumption Comb (mpg)"]
        string_columns = ["Make", "Model", "Vehicle Class", "Transmission", "Fuel Type"]

        df[int_columns] = df[int_columns].astype(int)
        df[float_columns] = df[float_columns].astype(float)
        df[string_columns] = df[string_columns].astype(str)
        lista_df.append(df)

    df = pd.concat(lista_df, ignore_index=True)
    df.drop_duplicates(inplace=True)

    fuel_type_dic = {
                    "X" : "Reg. Gasoline", 
                    "Z" : "Prm. Gasoline",
                    "D" : "Diesel",
                    "E" : "Ethanol (E85)",
                    "N" : "Natural Gas"}
    df["Fuel Type"] = df["Fuel Type"].replace(fuel_type_dic)
    return df

def load_pkls(fuel_type_selected):
    pass

if __name__ == "__main__":
    df = read_data()
    print(df)