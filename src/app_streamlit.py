import os
import sys
# TODO DO NOT USE IT! USE GLOBAL ENV VARS
# os.environ['PYTHONPATH'] = '/usr/local/bin/python3.8'
#sys.path.append("/app")

import altair as alt
from service import df_preparation, similarity
from service.features_processing import random_forest_regressor, xgboost
import streamlit as st
import pandas as pd

independent_features = [
    "Gross Profit",
    "Preferred Dividends",
    "Inventory Turnover",
    "Receivables Turnover",
    "Days Payables Outstanding",
    "Stock-based compensation to Revenue"
]

dependent_feature = ['Revenue']

st.title("Similarity analysis for the financial instruments")
df_columns_for_selection = ['Ticker'] + independent_features + dependent_feature

independent_features = st.multiselect("Select specific features for the 'similarity analysis'",
                                      list(independent_features),
                                      list(independent_features))

df_raw, df_encoded = df_preparation.get_df_features(path="./data/financial_data.csv",
                                                    nrows=100,
                                                    list_features=df_columns_for_selection)


def calculate_cosine_similarity():
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
        unsafe_allow_html=True, )

    # Measure cosine similarities
    st.write('You selected:', ticker)
    target_row = df_raw[df_raw['Ticker'] == ticker]

    similarity.cosine(df_encoded=df_encoded, df_raw=df_raw, row_id=target_row.index[0],
                      result_file_path='./output/cosine_similarity.csv')

    df_for_print = df_raw[["Ticker", "cosine_similarities"] + dependent_feature + independent_features]
    st.write(df_for_print)


calculate_cosine_similarity()


def plot_bar_chart(title, data):
    """
    https://altair-viz.github.io/user_guide/data.html
    Parameters
    ----------
    title
    data
    Returns
    -------
    """
    st.write(title)
    st.write(alt.Chart(data=data, width=500, height=500).mark_bar().encode(
        x='x',
        y='y',
    ))


def build_bar_chart(df_raw, independent_features, dependent_feature, fun, title):
    feature_imp, independent_features = fun(df_raw, independent_features, dependent_feature)
    data = pd.DataFrame({'x': list(feature_imp),
                         'y': list(independent_features)})
    plot_bar_chart(title, data)


# Visualisation which plots the correlation measure for every feature in the data set.
corr = df_raw.corr()

build_bar_chart(df_raw,
                independent_features,
                dependent_feature,
                xgboost,
                "Feature importance prediction with 'xgboost' algorithm:")

build_bar_chart(df_raw,
                independent_features,
                dependent_feature,
                random_forest_regressor,
                "Feature importance prediction with 'random forest regressor' algorithm:")
