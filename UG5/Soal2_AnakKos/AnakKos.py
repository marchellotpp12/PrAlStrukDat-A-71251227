import streamlit as st
import pandas as pd

# --- Title ---
st.title("Perhitungan Pengeluaran Anak Kos")


# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
uang_bulanan = st.number_input("Masukkan Uang Bulanan", min_value=0, step=10000)


# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")
makanan = st.number_input("Makanan", min_value=0, step=10000) # Ada 5
kos = st.number_input("Kos", min_value=0, step=1000) # Kategori
transportasi = st.number_input("Transportasi, min_value=0, step=1000") # Pengeluaran
internet = st.number_input("Internet, min_value=0, step=1000") # Ya kan
hiburan = st.number_input("hiburan, min_value=0, step=1000") # Paham lah ya

# --- Tombol Ngitung Pengeluaran ---
if ??? # if jangan dihapus, cuman nambahin tombol disini :

    # --- Ngitung Total Pengeluaran ---x
    ???

    # --- Ngitung Sisa Uang ---
    ???


    # --- Menampilkan Hasil Perhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric(
            # Tampilin uang bulanan di sini
            ???
        )
    with kolom2:
        st.metric(
            # Tampilin total pengeluaran di sini
            ???
        )
    with kolom3:
        st.metric(
            # Tampilin sisa uang di sini
            ???
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if ???:
        ??? 

    # Kondisi 2
    elif ???:
        ??? 

    # Kondisi 3
    else:
        ???


    # --- Data Pengeluaran ---
    # Ini gausah diubah! 
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "Makanan",
            "Kos",
            "Transportasi",
            "Internet/Pulsa",
            "Hiburan"
        ],
        "Pengeluaran": [
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    ??? # Cari pengeluaran terbesar

    st.subheader("Pengeluaran Terbesar")
    ??? # Tampilin pengeluaran terbesar di sini


    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    ??? # Tampilin grafik pengeluaran di sini