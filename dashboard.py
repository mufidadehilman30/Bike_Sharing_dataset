import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =============================
# CONFIG
# =============================
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
sns.set_style("whitegrid")

st.title("🚲 Bike Sharing Dashboard")

# =============================
# LOAD DATA
# =============================
@st.cache_data
def load_data():
    if not os.path.exists("day.csv"):
        st.error("File day.csv tidak ditemukan. Pastikan file ada di folder project.")
        st.stop()

    df = pd.read_csv("day.csv")

    # Hapus duplikat
    df.drop_duplicates(inplace=True)

    # Mapping musim
    season_map = {
        1: "Spring",
        2: "Summer",
        3: "Fall",
        4: "Winter"
    }
    df["season"] = df["season"].replace(season_map)

    # Mapping hari kerja / libur
    df["day_type"] = df["workingday"].map({
        0: "Holiday",
        1: "Working Day"
    })

    # Kategori temperatur
    df["temp_category"] = pd.cut(
        df["temp"],
        bins=5,
        labels=["Very Low", "Low", "Moderate", "High", "Very High"]
    )

    return df


df = load_data()

# =============================
# DATA PREVIEW
# =============================
st.subheader("Preview Data")
st.dataframe(df.head())

# =============================
# SCATTER TEMP VS CNT
# =============================
st.subheader("Hubungan Temperatur dan Peminjaman")

fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x="temp", y="cnt", ax=ax1)
st.pyplot(fig1)

# =============================
# RATA-RATA PEMINJAMAN BERDASARKAN TEMP
# =============================
st.subheader("Rata-rata Peminjaman Berdasarkan Temperatur")

temp_analysis = df.groupby("temp_category")["cnt"].mean()

fig2, ax2 = plt.subplots()
sns.barplot(x=temp_analysis.index, y=temp_analysis.values, ax=ax2)
st.pyplot(fig2)

# =============================
# PERBANDINGAN PENGGUNA PER MUSIM
# =============================
st.subheader("Perbandingan Pengguna Berdasarkan Musim")

season_user = df.groupby("season")[["casual", "registered"]].mean()

fig3, ax3 = plt.subplots()
season_user.plot(kind="bar", ax=ax3)
st.pyplot(fig3)

# =============================
# TOTAL PEMINJAMAN PER MUSIM
# =============================
st.subheader("Total Peminjaman Berdasarkan Musim")

season_total = df.groupby("season")["cnt"].mean()

fig4, ax4 = plt.subplots()
sns.barplot(x=season_total.index, y=season_total.values, ax=ax4)
st.pyplot(fig4)

# =============================
# HEATMAP KORELASI
# =============================
st.subheader("Heatmap Korelasi")

fig5, ax5 = plt.subplots(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, ax=ax5)
st.pyplot(fig5)
