import streamlit as st

st.set_page_config(
    page_title="Hyderabad Air Quality Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Hyderabad Air Quality Monitoring System")

st.image(
    "https://images.unsplash.com/photo-1569163139394-de44cb5894a4",
    use_container_width=True
)

st.markdown("""
### Welcome

This project provides:

- Real-time Air Quality Information
- Pollutant Analysis
- AQI Trends
- Health Recommendations
- Hyderabad Environmental Monitoring

Use the sidebar to navigate through pages.
""")