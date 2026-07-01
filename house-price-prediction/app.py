import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/house_price_model.pkl")

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict its price.")

# User Inputs
area = st.number_input("Area (sq ft)", min_value=500, value=4000)
bedrooms = st.number_input("Bedrooms", min_value=1, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
stories = st.number_input("Stories", min_value=1, value=1)

mainroad = st.selectbox("Main Road", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
parking = st.number_input("Parking Spaces", min_value=0, value=1)
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])
furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

# Convert categorical values to numerical values
mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0

furnishing_map = {
    "Furnished": 0,
    "Semi-Furnished": 1,
    "Unfurnished": 2
}

furnishingstatus = furnishing_map[furnishingstatus]

# Prediction
if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furnishingstatus]
    })

    prediction = model.predict(input_data)

    st.success(f"🏡 Predicted House Price: ₹ {prediction[0]:,.2f}")