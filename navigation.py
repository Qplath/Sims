# Handles navigation between pages/modules

import streamlit as st
from market_dashboard import market_dashboard_page
from candlestick_chart import candlestick_chart_page
from user_profile import user_profile_page
from transaction import transaction_page
from tutorial import tutorial_page

def show_page():
    pages = {
        "Dashboard Market": market_dashboard_page,
        "Grafik Candlestick": candlestick_chart_page,
        "Profil Pengguna": user_profile_page,
        "Transaksi Beli/Jual": transaction_page,
        "Tutorial": tutorial_page,
    }
    st.sidebar.title("Navigasi")
    selection = st.sidebar.radio("Pilih Halaman", list(pages.keys()))
    pages[selection]()