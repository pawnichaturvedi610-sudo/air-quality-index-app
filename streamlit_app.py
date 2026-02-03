import streamlit as st

st.set_page_config(page_title="AQI Prediction App", layout="centered")

st.title("Predict the Air Quality Index (AQI) based on input parameters.")

pm25 = st.number_input("PM2.5", 0.0, 500.0, 50.0)
pm10 = st.number_input("PM10", 0.0, 500.0, 80.0)
no2 = st.number_input("NO2", 0.0, 200.0, 40.0)
so2 = st.number_input("SO2", 0.0, 200.0, 20.0)
co = st.number_input("CO", 0.0, 10.0, 1.0)
temp = st.number_input("Temperature (°C)", -10.0, 50.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 50.0)

if st.button("Predict AQI"):
    aqi = (
        pm25 * 0.5 +
        pm10 * 0.3 +
        no2 * 0.2 +
        so2 * 0.1 +
        co * 10
    )

    st.success(f"Predicted AQI: {int(aqi)}")

    if aqi <= 50:
        st.info("Air Quality: Good 😊")
    elif aqi <= 100:
        st.warning("Air Quality: Moderate 😐")
    elif aqi <= 200:
        st.error("Air Quality: Poor 😷")
    else:
        st.error("Air Quality: Very Poor ☠️")
