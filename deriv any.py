import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import zipfile

st.set_page_config(page_title="Deriv Digit Flow Analysis", layout="wide")
st.title("📊 Deriv Digit Flow Analysis Tool")

st.markdown("""
Upload a CSV file containing tick data in the format:
