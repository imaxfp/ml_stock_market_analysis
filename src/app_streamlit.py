import os
import sys

# SET current environment variables
os.environ['PYTHONPATH'] = '/usr/local/bin/python3.8'
sys.path.append("~/Documents/github/ml-stock-market-analysis")
print(os.environ)

import streamlit as st
import pandas as pd
from src.service import df_preparation, similarity

# from service import similarity

df = pd.read_csv("./data/financial_data.csv")
df_raw, df_encoded = df_preparation.get_init_df("./data/financial_data.csv")

st.title("Raw data:")
st.dataframe(df_raw)

# Measure cosine similarities
similarity.measure(df_encoded=df_encoded, df_raw=df_raw, row_id=1, result_file_path='./output/cosine_similarity.csv')

st.title("Prepared data:")
df_view = df_raw[['Ticker', 'Revenue', 'Sector', 'Asset Growth', 'Operating Cash Flow growth', 'cosine_similarities']]
st.dataframe(df_view)
