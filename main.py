# Main entry point for the Stock Trading Simulation App
# Jalankan dengan: streamlit run main.py

import streamlit as st
from navigation import show_page

def main():
    st.set_page_config(page_title="Simulasi Trading Saham", layout="wide")
    show_page()

# Pastikan fungsi main() dipanggil saat dijalankan dengan streamlit
main()