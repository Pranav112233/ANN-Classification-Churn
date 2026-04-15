import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="House Price Predictor", layout="wide")

# -------------------------------
# Dummy Dataset (Replace with yours if needed)
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

# Train model
model = LinearRegression()
model.fit(X, y)

y_pred_train = model.predict(X)
r2 = r2_score(y, y_pred_train)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Predict", "Data Analysis", "Model Performance"])

# -------------------------------
# 1. Prediction Page
# -------------------------------
if option == "Predict":
    st.title("🏠 House Price Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        area = st.slider("Area (sq ft)", 100, 3000, 1000)
    with col2:
        bedrooms = st.slider("Bedrooms", 1, 5, 2)
    with col3:
        age = st.slider("Age", 0, 30, 5)

    if st.button("Predict Price"):
        input_data = np.array([[area, bedrooms, age]])
        prediction = model.predict(input_data)[0]

        st.success(f"💰 Estimated Price: ₹ {prediction:.2f} Lakhs")

        # Download result
        result_df = pd.DataFrame({
            "Area": [area],
            "Bedrooms": [bedrooms],
            "Age": [age],
            "Predicted Price": [prediction]
        })

        st.download_button(
            "Download Result",
            result_df.to_csv(index=False),
            file_name="prediction.csv"
        )

# -------------------------------
# 2. Data Analysis Page
# -------------------------------
elif option == "Data Analysis":
    st.title("📊 Data Analysis")

    st.subheader("Dataset")
    st.dataframe(df)

    # Scatter Plot (Income vs Price style like your project)
    st.subheader("Area vs Price")
    fig, ax = plt.subplots()
    ax.scatter(df["Area"], df["Price"])
    ax.set_xlabel("Area")
    ax.set_ylabel("Price")
    st.pyplot(fig)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    cax = ax.matshow(df.corr(), cmap='coolwarm')
    plt.xticks(range(len(df.columns)), df.columns, rotation=45)
    plt.yticks(range(len(df.columns)), df.columns)
    fig.colorbar(cax)
    st.pyplot(fig)

# -------------------------------
# 3. Model Performance
# -------------------------------
else:
    st.title("📈 Model Performance")

    st.write(f"R² Score: **{r2:.2f}**")

    # Actual vs Predicted Plot
    fig, ax = plt.subplots()
    ax.scatter(y, y_pred_train)
    ax.set_xlabel("Actual Price")
    ax.set_ylabel("Predicted Price")
    ax.set_title("Actual vs Predicted")
    st.pyplot(fig)