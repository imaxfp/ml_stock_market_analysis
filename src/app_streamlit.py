import os
import sys

# SET current environment variables
os.environ['PYTHONPATH'] = '/usr/local/bin/python3.8'
sys.path.append("~/Documents/github/ml-stock-market-analysis")
print(os.environ)

import streamlit as st
import pandas as pd
from src.service import df_preparation, similarity

df_raw, df_encoded = df_preparation.get_init_df(path="./data/financial_data.csv", nrows=100)

# from service import similarity
ticker = st.selectbox('Select Ticker', (df_raw['Ticker'].tolist()))
st.write(
    """
    <style type="text/css" media="screen">
    div[role="listbox"] ul {
        height:300px;
    }
    </style>
    """
    ,
    unsafe_allow_html=True,
)

st.title("Raw data:")
st.dataframe(df_raw)

# Measure cosine similarities
st.write('You selected:', ticker)
target_row = df_raw[df_raw['Ticker']==ticker]
similarity.measure(df_encoded=df_encoded, df_raw=df_raw, row_id=target_row.index[0], result_file_path='./output/cosine_similarity.csv')

st.title("Prepared data:")
df_view = df_raw[['Ticker', 'cosine_similarities', 'Revenue', 'Sector', 'Asset Growth', 'Operating Cash Flow growth']]
st.dataframe(df_view)
