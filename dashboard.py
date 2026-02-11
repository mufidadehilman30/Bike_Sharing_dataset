import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)

st.title("Bike Sharing Analysis Dashboard")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")

    # Hapus duplikat
    df.drop_duplicates(inplace=True)

    # Mapping Season
    season_map = {
        1: "Spring",
        2: "Summer",
        3: "Fall",
        4: "Winter"
    }
    df["season"] = df["season"].replace(season_map)

    # Mapping working day
    df["day_type"] = df["workingday"].map({
        0: "Holiday",
        1: "Working Day"
    })

    # Temp Category
    df["temp_category"] = pd.cut(
        df["temp"],
        bins=5,
        labels=["Very Low", "Low", "Moderate", "High", "Very High"]
    )

    return df

df = load_data()

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("Filter Data")

selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=df["season"].unique(),
    default=df["season"].unique()
)

filtered_df = df[df["season"].isin(selected_season)]

# =========================
# METRIC SUMMARY
# =========================
st.subheader("Ringkasan Data")

col1, col2, col3 = st.columns(3)

col1.metric("Total Peminjaman", int(filtered_df["cnt"].sum()))
col2.metric("Rata-rata Temperatur", round(filtered_df["temp"].mean(), 2))
col3.metric("Jumlah Hari", filtered_df.shape[0])

# =========================
# ANALISIS 1
# Hubungan Temperatur dan Peminjaman
# =========================
st.subheader("Hubungan Temperatur dan Jumlah Peminjaman")

fig1, ax1 = plt.subplots()
sns.scatterplot(data=filtered_df, x="temp", y="cnt", ax=ax1)
st.pyplot(fig1)

st.info("""
Insight:
Jumlah peminjaman sepeda cenderung meningkat ketika temperatur berada pada kondisi sedang hingga hangat.
""")

# =========================
# ANALISIS 2
# Rata-rata Peminjaman Berdasarkan Kategori Temperatur
# =========================
st.subheader("Rata-rata Peminjaman Berdasarkan Kategori Temperatur")

temp_analysis = filtered_df.groupby("temp_category")["cnt"].mean()

fig2, ax2 = plt.subplots()
sns.barplot(x=temp_analysis.index, y=temp_analysis.values, ax=ax2)
st.pyplot(fig2)

st.info("""
Insight:
Kategori temperatur Moderate hingga High menunjukkan tingkat peminjaman sepeda paling tinggi.
""")

# =========================
# ANALISIS 3
# Perbandingan Pengguna Berdasarkan Musim
# =========================
st.subheader("Perbandingan Pengguna Casual dan Registered Berdasarkan Musim")

season_user = filtered_df.groupby("season")[["casual", "registered"]].mean()

fig3, ax3 = plt.subplots()
season_user.plot(kind="bar", ax=ax3)
st.pyplot(fig3)

st.info("""
Insight:
Pengguna registered cenderung lebih stabil di semua musim dibandingkan pengguna casual.
""")

# =========================
# ANALISIS 4
# Total Peminjaman Berdasarkan Musim
# =========================
st.subheader("Total Peminjaman Berdasarkan Musim")

season_total = filtered_df.groupby("season")["cnt"].mean()

fig4, ax4 = plt.subplots()
sns.barplot(x=season_total.index, y=season_total.values, ax=ax4)
st.pyplot(fig4)

st.info("""
Insight:
Musim tertentu menunjukkan tingkat penggunaan sepeda yang lebih tinggi dibandingkan musim lainnya.
""")

# =========================
# HEATMAP KORELASI
# =========================
st.subheader("Heatmap Korelasi Variabel Numerik")

fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, ax=ax5)
st.pyplot(fig5)

st.info("""
Insight:
Variabel temperatur dan feeling temperature memiliki korelasi kuat terhadap jumlah peminjaman sepeda.
""")

# =========================
# DATA PREVIEW
# =========================
st.subheader("📄 Preview Dataset")

st.dataframe(filtered_df.head())
