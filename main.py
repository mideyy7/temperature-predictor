import streamlit as st
import pandas as pd
import joblib

forest = joblib.load("weather_model.pk1")

st.title("Weather Prediction App")


land_avg_temp = st.number_input("Land Average Temperature", value=0.0)
land_max_temp = st.number_input("Land Max Temperature", value=0.0)
land_min_temp = st.number_input("Land Min Temperature", value=0.0)

if st.button("Predict Weather"): 
    input_df = pd.DataFrame({
        "LandAverageTemperature": [land_avg_temp],
        "LandMaxTemperature": [land_max_temp],
        "LandMinTemperature": [land_min_temp]
    })

    predicted = forest.predict(input_df)
    st.success(f"Predicted Temperature: {predicted[0]:.2f} degree Celcius")