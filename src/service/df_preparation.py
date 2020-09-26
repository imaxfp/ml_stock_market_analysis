import pandas as pd


def get_init_df(path, nrows):
    """
    Parameters
    ----------
    path: to the data frame csv.
    -------
    """
    df_raw = pd.read_csv(filepath_or_buffer=path, nrows=nrows)
    df_raw = drop_null(df_raw)
    df_raw = rename(df_raw)
    df_encoded = one_hot_encoding(df_raw)

    df_main_features(df_raw)

    print(df_raw)
    print(df_encoded)
    return df_raw, df_encoded


def get_df_features(path, nrows, list_features):
    df_raw, df_encoded = get_init_df(path, nrows)
    df_selected_columns = df_raw[list_features]
    return df_selected_columns, one_hot_encoding(df_selected_columns)


def df_main_features(df):
    """
    Parameters
    ----------
    df: Initial df

    Returns: df with main features
    -------
    """
    df = df[['Ticker', 'Revenue']]
    return df


def rename(df):
    df = df.rename({'Unnamed: 0': 'Ticker'}, axis=1)
    return df


def one_hot_encoding(df):
    """
    @see
     https://medium.com/@athif.shaffy/one-hot-encoding-of-text-b69124bef0a7
     http://queirozf.com/entries/one-hot-encoding-a-feature-on-a-pandas-dataframe-an-example
     http://www.insightsbot.com/python-one-hot-encoding-with-pandas-made-simple/
    """
    list_columns = list(df.select_dtypes(['object']).columns)
    for val in list_columns:
        # Convert to dummies
        df_dummies = pd.get_dummies(df[val], prefix=val)
        df = pd.concat([df, df_dummies], axis=1)
        # Drop 'strings' labels
        df = df.drop([val], axis=1)
    return df


def drop_null(df):
    # log("count of nulls into data frame is ", df.isnull().values.sum())
    if df.isnull().values.sum() > 0:
        # drop column with all 'nan'
        df = df.dropna(axis=1, how='all')
        df = df.where(pd.notnull(df), 0)
        return df
