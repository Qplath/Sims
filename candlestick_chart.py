# Candlestick chart page

import streamlit as st
import plotly.graph_objs as go

def candlestick_chart_page():
    st.title("Grafik Candlestick")
    if 'candlestick_data' in st.session_state:
        data = st.session_state['candlestick_data']
        fig = go.Figure(data=[go.Candlestick(
            x=data['time'],
            open=data['open'],
            high=data['high'],
            low=data['low'],
            close=data['close']
        )])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Data candlestick belum tersedia.")