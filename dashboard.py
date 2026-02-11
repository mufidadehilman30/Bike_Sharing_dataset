import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

st.title("Bike Sharing Dashboard")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")

    # Hapus duplikat
    df = df.drop_duplicates()

    # Mapping season
    season_map = {
        1: "Spring",
        2: "Summer",
        3: "Fall",
        4: "Winter"
    }
    df["season"] = df["season"].map(season_map)

    # Mapping workingday
    df["day_type"] = df["workingday"].map({
        0: "Holiday",
        1: "Working Day"
    })

    # Temp category
    df["temp_category"] = pd.cut(
        df["temp"],
        bins=5,
        labels=["Very Low", "Low", "Moderate", "High", "Very High"]
    )

    return df


df = load_data()

# =========================
# SIDEBAR
# =========================
st.sidebar.header("Filter")

season_filter = st.sidebar.multiselect(
    "Pilih Season",
    df["season"].dropna().unique(),
    default=df["season"].dropna().unique()
)

filtered_df = df[df["season"].isin(season_filter)]

# =========================
# METRIC
# =========================
st.subheader("Ringkasan")

col1, col2, col3 = st.columns(3)

col1.metric("Total Rental", int(filtered_df["cnt"].sum()))
col2.metric("Rata-rata Temperatur", round(filtered_df["temp"].mean(), 2))
col3.metric("Jumlah Data", filtered_df.shape[0])

# =========================
# SCATTER TEMP VS CNT
# =========================
st.subheader("Hubungan Temperatur dan Rental")

fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x="temp", y="cnt", ax=ax)
st.pyplot(fig)

st.write(
    "Insight: Rental meningkat ketika temperatur berada pada kondisi nyaman."
)

# =========================
# BAR TEMP CATEGORY
# =========================
st.subheader("Rata-rata Rental Berdasarkan Kategori Temperatur")

temp_avg = filtered_df.groupby("temp_category")["cnt"].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(data=temp_avg, x="temp_category", y="cnt", ax=ax2)
st.pyplot(fig2)

st.write(
    "Insight: Temperatur moderat hingga hangat menghasilkan jumlah rental tertinggi."
)

# =========================
# SEASON ANALYSIS
# =========================
st.subheader("Perbandingan User Berdasarkan Season")

season_user = filtered_df.groupby("season")[["casual", "registered"]].mean()

fig3, ax3 = plt.subplots()
season_user.plot(kind="bar", ax=ax3)
st.pyplot(fig3)

# =========================
# HEATMAP
# =========================
st.subheader("Korelasi Variabel Numerik")

fig4, ax4 = plt.subplots(figsize=(10,6))
sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, ax=ax4)
st.pyplot(fig4)

# =========================
# DATA PREVIEW
# =========================
st.subheader("Preview Data")
st.dataframe(filtered_df.head())
