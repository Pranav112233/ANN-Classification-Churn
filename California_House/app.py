import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# -------------------------------
# Dummy Training Data (Simple)
# -------------------------------
data = {
    "Area": [500, 800, 1000, 1500, 2000],
    "Bedrooms": [1, 2, 2, 3, 4],
    "Age": [10, 8, 6, 4, 2],
    "Price": [50, 80, 100, 150, 200]
}

df = pd.DataFrame(data)

X = df[["Area", "Bedrooms", "Age"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🏠 House Price Predictor")

st.write("Enter house details:")

area = st.number_input("Area (sq ft)", min_value=100)
bedrooms = st.number_input("Number of Bedrooms", min_value=1)
age = st.number_input("Age of House (years)", min_value=0)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, age]])
    prediction = model.predict(input_data)

    st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs")