import streamlit as st
import pandas as pd

st.title("📊 Current Air Quality")

aqi = 135

col1, col2, col3 = st.columns(3)

col1.metric("AQI", aqi)
col2.metric("City", "Hyderabad")
col3.metric("Status", "Moderate")

data = {
    "Pollutant": ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"],
    "Value": [58, 92, 24, 12, 0.8, 35]
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

st.bar_chart(df.set_index("Pollutant"))