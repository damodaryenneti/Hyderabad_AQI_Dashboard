import streamlit as st
import pandas as pd

st.title("📈 AQI Trends")

trend = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "AQI": [120, 130, 110, 145, 135, 125, 140]
})

st.line_chart(
    trend.set_index("Day")
)