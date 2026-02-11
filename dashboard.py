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

st.title("Bike Sharing Dashboard")

# =============================
# LOAD DATA
# =============================
@st.cache_data
def load_data():
    if not os.path.exists("main_data.csv"):
        st.error("File day.csv tidak ditemukan.")
        st.stop()

    df = pd.read_csv("main_data.csv")

    df.drop_duplicates(inplace=True)

    # Convert tanggal
    df["dteday"] = pd.to_datetime(df["dteday"])

    # Mapping musim
    season_map = {
        1: "Spring",
        2: "Summer",
        3: "Fall",
        4: "Winter"
    }
    df["season"] = df["season"].replace(season_map)

    # Mapping jenis hari
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
# SIDEBAR FILTER
# =============================
st.sidebar.header("Filter Data")

# Filter musim
season_filter = st.sidebar.multiselect(
    "Pilih Musim",
    options=df["season"].unique(),
    default=df["season"].unique()
)

# Filter jenis hari
day_filter = st.sidebar.multiselect(
    "Pilih Jenis Hari",
    options=df["day_type"].unique(),
    default=df["day_type"].unique()
)

# Filter temperatur
temp_range = st.sidebar.slider(
    "Rentang Temperatur",
    float(df["temp"].min()),
    float(df["temp"].max()),
    (float(df["temp"].min()), float(df["temp"].max()))
)

# Filter tanggal
date_range = st.sidebar.date_input(
    "Rentang Tanggal",
    [df["dteday"].min(), df["dteday"].max()]
)

# =============================
# APPLY FILTER
# =============================
filtered_df = df[
    (df["season"].isin(season_filter)) &
    (df["day_type"].isin(day_filter)) &
    (df["temp"].between(temp_range[0], temp_range[1])) &
    (df["dteday"].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))
]

st.subheader("Preview Data")
st.dataframe(filtered_df.head())

# =============================
# SCATTER TEMP VS CNT
# =============================
st.subheader("Hubungan Temperatur dan Peminjaman")

fig1, ax1 = plt.subplots()
sns.scatterplot(data=filtered_df, x="temp", y="cnt", ax=ax1)
st.pyplot(fig1)

# =============================
# RATA-RATA PEMINJAMAN TEMP
# =============================
st.subheader("Rata-rata Peminjaman Berdasarkan Temperatur")

temp_analysis = filtered_df.groupby("temp_category")["cnt"].mean()

fig2, ax2 = plt.subplots()
sns.barplot(x=temp_analysis.index, y=temp_analysis.values, ax=ax2)
st.pyplot(fig2)

# =============================
# PERBANDINGAN USER PER MUSIM
# =============================
st.subheader("Perbandingan Pengguna Berdasarkan Musim")

season_user = filtered_df.groupby("season")[["casual", "registered"]].mean()

fig3, ax3 = plt.subplots()
season_user.plot(kind="bar", ax=ax3)
st.pyplot(fig3)

# =============================
# TOTAL PEMINJAMAN PER MUSIM
# =============================
st.subheader("Total Peminjaman Berdasarkan Musim")

season_total = filtered_df.groupby("season")["cnt"].mean()

fig4, ax4 = plt.subplots()
sns.barplot(x=season_total.index, y=season_total.values, ax=ax4)
st.pyplot(fig4)

# =============================
# HEATMAP KORELASI
# =============================
st.subheader("Heatmap Korelasi")

fig5, ax5 = plt.subplots(figsize=(8, 6))
sns.hea
