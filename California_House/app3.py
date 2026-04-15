import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# -------------------------------
# Dummy Training Data (Expanded)
# -------------------------------
data = {
    "MedInc": [2, 3, 4, 5, 6],
    "HouseAge": [10, 20, 30, 40, 50],
    "AveRooms": [4, 5, 6, 7, 8],
    "AveBedrms": [1, 1.5, 2, 2.5, 3],
    "Population": [1000, 1500, 2000, 2500, 3000],
    "AveOccup": [2, 3, 3.5, 4, 5],
    "Latitude": [34, 35, 36, 37, 38],
    "Longitude": [-118, -119, -120, -121, -122],
    "Price": [100, 150, 200, 300, 400]
}

df = pd.DataFrame(data)

X = df.drop("Price", axis=1)
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🏠 Advanced House Price Predictor")

st.write("Enter complete house details:")

medinc = st.number_input("Median Income (in tens of thousands)", min_value=0.0)
house_age = st.number_input("House Age (years)", min_value=0)
ave_rooms = st.number_input("Average Rooms", min_value=0.0)
ave_bedrms = st.number_input("Average Bedrooms", min_value=0.0)
population = st.number_input("Population", min_value=0)
ave_occup = st.number_input("Average Occupancy", min_value=0.0)
latitude = st.number_input("Latitude", min_value=30.0, max_value=45.0)
longitude = st.number_input("Longitude", min_value=-125.0, max_value=-110.0)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Price"):
    input_data = np.array([[
        medinc, house_age, ave_rooms, ave_bedrms,
        population, ave_occup, latitude, longitude
    ]])

    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ₹ {prediction[0]:.2f} Lakhs")