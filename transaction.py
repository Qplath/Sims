import streamlit as st

def transaction_page():
    st.title("Transaksi Beli/Jual")
    st.write("Simulasikan transaksi saham seperti akun demo nyata.")
    if "balance" not in st.session_state:
        st.session_state.balance = 1_000_000
    if "history" not in st.session_state:
        st.session_state.history = []
    action = st.radio("Aksi", ["Beli", "Jual"])
    stock = st.text_input("Kode Saham", "ABC")
    amount = st.number_input("Jumlah Lot", min_value=1, value=1)
    price = st.number_input("Harga per Lembar", min_value=100, value=10000)
    total = amount * 100 * price
    st.write(f"Total Transaksi: Rp {total:,}")
    st.write(f"Saldo Saat Ini: Rp {st.session_state.balance:,}")
    if st.button("Eksekusi Transaksi"):
        if action == "Beli":
            if st.session_state.balance >= total:
                st.session_state.balance -= total
                st.session_state.history.append({
                    "Tipe": "Beli",
                    "Saham": stock,
                    "Jumlah Lot": amount,
                    "Harga": price,
                    "Total": total
                })
                st.success(f"Berhasil membeli {amount} lot {stock} di harga Rp {price:,}.")
            else:
                st.error("Saldo tidak cukup untuk melakukan pembelian.")
        else:
            st.session_state.balance += total
            st.session_state.history.append({
                "Tipe": "Jual",
                "Saham": stock,
                "Jumlah Lot": amount,
                "Harga": price,
                "Total": total
            })
            st.success(f"Berhasil menjual {amount} lot {stock} di harga Rp {price:,}.")
    st