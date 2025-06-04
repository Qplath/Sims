import streamlit as st
from navigation import show_page

def main():
    st.set_page_config(page_title="Simulasi Trading Saham", layout="wide")
    show_page()

main()