import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.use('Agg')
import streamlit as st
import os

# ==============================
# JUDUL DASHBOARD
# ==============================
st.title("Dashboard Analisis Penyewaan Sepeda")

# ==============================
# LOAD DATA
# ==============================
DATA_PATH = "main_data.csv"   # ganti jika nama file berbeda

if not os.path.exists(DATA_PATH):
    st.error(f"File {DATA_PATH} tidak ditemukan")
    st.stop()

df = pd.read_csv(DATA_PATH)

st.success("Data berhasil dimuat")
st.write("Contoh Data:")
st.dataframe(df.head())

# ==============================
# CEK KOLOM WAJIB
# ==============================
required_cols = ["mnth", "weathersit", "cnt"]

for col in required_cols:
    if col not in df.columns:
        st.error(f"Kolom '{col}' tidak ditemukan di dataset")
        st.stop()

# ==============================
# AGREGASI DATA
# ==============================
monthly_avg = df.groupby("mnth")["cnt"].mean()
weather_avg = df.groupby("weathersit")["cnt"].mean()

# ==============================
# GRAFIK 1: RATA-RATA BULANAN
# ==============================
st.subheader("Rata-rata Penyewaan per Bulan")

if monthly_avg.empty:
    st.warning("Data bulanan kosong")
else:
    fig1, ax1 = plt.subplots()
    ax1.plot(monthly_avg.index, monthly_avg.values, marker="o")
    ax1.set_xlabel("Bulan")
    ax1.set_ylabel("Rata-rata Penyewaan")
    ax1.set_title("Rata-rata Penyewaan Sepeda per Bulan")
    st.pyplot(fig1)

# ==============================
# GRAFIK 2: CUACA
# ==============================
st.subheader("Rata-rata Penyewaan berdasarkan Cuaca")

if weather_avg.empty:
    st.warning("Data cuaca kosong")
else:
    fig2, ax2 = plt.subplots()
    ax2.bar(weather_avg.index.astype(str), weather_avg.values)
    ax2.set_xlabel("Kategori Cuaca")
    ax2.set_ylabel("Rata-rata Penyewaan")
    ax2.set_title("Pengaruh Cuaca terhadap Penyewaan")
    st.pyplot(fig2)

# ==============================
# STATISTIK DESKRIPTIF
# ==============================
st.subheader("Statistik Penyewaan")

st.write(df["cnt"].describe())
