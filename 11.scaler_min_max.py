import pickle
from sklearn.preprocessing import MinMaxScaler

x_scaler_diesel: MinMaxScaler
file_path = "sources/Diesel_x_scaler.pkl"

with open(file_path, "rb") as file:
    x_scaler_diesel = pickle.load(file)

print(type(x_scaler_diesel))
x_scaler_diesel.

# def main():
#     pass

# if __name__ == "__main__":
#     main()