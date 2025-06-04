# Market dashboard with animated price updates

import streamlit as st
import time
from market_data import get_market_data, update_market_data

def market_dashboard_page():
    st.title("Dashboard Market")
    st.write("Harga saham real-time (simulasi):")

    # Area untuk animasi grafik
    chart_placeholder = st.empty()
    metric_placeholder = st.empty()

    # Slider untuk mengatur kecepatan update (opsional)
    speed = st.sidebar.slider("Kecepatan Update (detik)", min_value=0.5, max_value=3.0, value=1.0, step=0.1)

    # Tombol untuk memulai/berhenti animasi
    if "market_animating" not in st.session_state:
        st.session_state.market_animating = False

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Mulai Animasi"):
            st.session_state.market_animating = True
    with col2:
        if st.button("Stop Animasi"):
            st.session_state.market_animating = False

    # Animasi real-time
    while st.session_state.market_animating:
        update_market_data()
        data = get_market_data()
        metric_placeholder.metric(label="Harga Saham", value=f"Rp {data['price']:,}", delta=f"{data['change']}%")
        chart_placeholder.line_chart(data['history'])
        time.sleep(speed)
        st.rerun()

    # Tampilkan data terakhir jika animasi tidak berjalan
    data = get_market_data()
    metric_placeholder.metric(label="Harga Saham", value=f"Rp {data['price']:,}", delta=f"{data['change']}%")
    chart_placeholder.line_chart(data['history'])
    # ...add more dashboard features/animations as needed...