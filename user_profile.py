import streamlit as st

INITIAL_BALANCE = 1_000_000

def user_profile_page():
    st.title("Profil Pengguna")
    if "balance" not in st.session_state:
        st.session_state.balance = INITIAL_BALANCE
    if "history" not in st.session_state:
        st.session_state.history = []
    user = {
        "username": "demo_user",
        "balance": st.session_state.balance,
        "history": st.session_state.history
    }
    st.write(f"Username: {user['username']}")
    st.write(f"Saldo: Rp {user['balance']:,}")
    st.write("Riwayat Transaksi:")
    if user["history"]:
        st.table(user["history"])
    else:
        st.info("Belum ada transaksi.")
    if st.button("Reset Saldo & Riwayat"):
        st.session_state.balance = INITIAL_BALANCE
        st.session_state.history = []
        st.success("Saldo dan riwayat transaksi berhasil direset!")