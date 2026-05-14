import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Dashboard Hospitalar")

data = pd.DataFrame({
    'x': np.arange(20),
    'y': np.random.randn(20)
})

st.dataframe(data)

st.line_chart(data)
