import streamlit as st
import pandas as pd

st.title("Deriv Digit Flow Analysis")
file = st.file_uploader("Upload CSV", type="csv")
if file:
    df = pd.read_csv(file)
    st.write(df.head())
    if 'digit' in df.columns:
        freq = df['digit'].value_counts().sort_index()
        st.bar_chart(freq)
        st.write("Most common digit:", freq.idxmax())
    else:
        st.error("CSV must have 'digit' column")
else:
    st.info("Please upload your Deriv digits CSV file.")
