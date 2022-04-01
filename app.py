import streamlit as st
import pandas as pd

adf = pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
st.write(df)
st.map(df)
