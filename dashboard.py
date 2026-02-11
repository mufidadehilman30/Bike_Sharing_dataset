import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# PAGE CONFIG
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
    df = pd.read_csv("main_data.csv")

    # Hapus duplikat
    df.drop_duplicates(inplace=True)

    # Mapping season jika masih angka
    season_map = {
        1: "Spring",
        2: "Summer",
        3: "Fall",
        4: "Winter"
    }

    if df["season"].dtype != "object":
        df["season"] = df["season"].map(season_map)

    # Mapping working day
    df["day_type"] = df["workingday"].map({
        0: "Holiday",
        1: "Working Day"
    })

    # Feature Engineering Temp Category
    df["temp_category"] = pd.cut(
        df["temp"],
        bins=5,
        labels=["Very Low", "Low", "Moderate", "High", "Very High"]
    )
