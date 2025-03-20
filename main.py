import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title="Dava Visualization with Streamlit",
                   page_icon="😊"

)
st.title("Dava Visualization with Streamlit")
with st.sidebar:
   upload=st.file_uploader("upload csv")

if upload is not None:
    df=pd.read_csv(upload)
    st.dataframe(df.head())