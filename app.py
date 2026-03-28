import streamlit as st
from src.data_preprocessing import load_data, preprocess_data
from src.model import train_model
from src.utils import predict_demand

st.title("🚴 Bike Demand Polyrhythm Composer")

# ✅ Cache data (IMPORTANT)
@st.cache_data
def get_data():
    df = load_data("data/hour.csv")
    return preprocess_data(df)

# ✅ Cache model (IMPORTANT)
@st.cache_resource
def get_model(df):
    return train_model(df)

df = get_data()
model = get_model(df)

st.write("### Enter Details")

hr = st.slider("Hour", 0, 23)
temp = st.slider("Temperature", 0.0, 1.0)
hum = st.slider("Humidity", 0.0, 1.0)
windspeed = st.slider("Windspeed", 0.0, 1.0)

if st.button("Predict Demand"):
    result = predict_demand(model, hr, temp, hum, windspeed)
    st.success(f"Predicted Bike Demand: {int(result)}")