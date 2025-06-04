import streamlit as st
import plotly.graph_objs as go
from market_data import get_candlestick_data

def candlestick_chart_page():
    st.title("Grafik Candlestick")
    data = get_candlestick_data()
    fig = go.Figure(data=[go.Candlestick(
        x=data['time'],
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close']
    )])
    st.plotly_chart(fig, use_container_width=True)