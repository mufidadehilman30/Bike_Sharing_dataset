import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Dashboard")

df = pd.read_csv("main_data.csv")

# Filter Musim
season_filter = st.sidebar.multiselect(
    "Pilih Musim",
    df["season"].unique(),
    default=df["season"].unique()
)

filtered_df = df[df["season"].isin(season_filter)]

# Temperatur Analysis
st.subheader("Pengaruh Temperatur")
df['temp.category'] = pd.cut(
    df['temp'],
    bins=[0, 20, 30, 100],
    labels=['Dingin', 'Normal', 'Panas']
)

temp_analysis = filtered_df.groupby("temp_category")["cnt"].mean()

fig, ax = plt.subplots()
sns.barplot(x=temp_analysis.index, y=temp_analysis.values, ax=ax)
st.pyplot(fig)

# User Analysis
st.subheader("Perbandingan Pengguna")

season_user = filtered_df.groupby("season")[["casual","registered"]].mean()

fig, ax = plt.subplots()
season_user.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Insight Dashboard
st.markdown("### Insight")

st.info("""
• Temperatur moderat meningkatkan peminjaman  
• Musim panas memiliki penggunaan tertinggi  
• Pengguna registered mendominasi penggunaan layanan  
""")
