import streamlit as st

st.title("🏥 Health Recommendations")

aqi = 135

if aqi <= 50:
    st.success("Air quality is good.")
elif aqi <= 100:
    st.info("Air quality is satisfactory.")
elif aqi <= 200:
    st.warning(
        "Moderate AQI. Sensitive individuals should limit prolonged outdoor activities."
    )
else:
    st.error(
        "Poor air quality. Consider wearing a mask outdoors."
    )