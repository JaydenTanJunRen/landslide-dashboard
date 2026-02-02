import streamlit as st

st.set_page_config(
    page_title="Landslide Guard AI",
    page_icon="🌋",
    layout="wide", # This makes it look like a dashboard
    initial_sidebar_state="expanded"
)

# Create 4 columns for top metrics
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(label="Soil Moisture", value="85%", delta="High Risk", delta_color="inverse")
with m2:
    st.metric(label="Ground Tilt", value="1.2°", delta="Stable")
with m3:
    st.metric(label="Rain Forecast", value="120mm", delta="Severe")
with m4:
    # We can use a colored box for the final Risk Level
    st.markdown("### Risk Level")
    st.error("CRITICAL") # Displays a red box

col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📸 Live Terrain Analysis")
    # In a real setup, this URL will point to your Supabase Storage
    st.image("https://images.unsplash.com/photo-1500382017468-9049fee74a62", 
             caption="Last Capture: 5 mins ago", use_container_width=True)

with col_right:
    st.subheader("🤖 Clawdbot Logic")
    st.info("""
    **Analysis Report:**
    * **Pore Pressure:** Critical (Soil saturated).
    * **Movement:** None detected.
    * **Decision:** Monitoring frequency increased to 30s.
    """)

st.subheader("📈 Ground Saturation Trend (Past 24 Hours)")

# Create some dummy data for now
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(24, 1) / 10 + 0.8, # Simulating high moisture levels
    columns=['Moisture %']
)
st.area_chart(chart_data)

# 🚨 Alarm Trigger
current_moisture = 85 # This will come from Supabase later

if current_moisture > 80:
    st.toast("🚨 EMERGENCY ALERT SENT TO TELEGRAM", icon="⚠️")
    
    # This plays a 'beep' sound in the viewer's browser automatically
    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3", autoplay=True)
    
    # Flashing warning for the GUI
    st.markdown("<h1 style='text-align: center; color: red; background-color: yellow;'>⚠️ LANDSLIDE IMMINENT - EVACUATE ⚠️</h1>", unsafe_allow_html=True)

