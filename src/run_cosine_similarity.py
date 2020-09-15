import sys

from src.service import similarity
from src.service.df_preparation import get_init_df

import os
os.environ['PATH'] = '/Users/maxim/Documents/github/ml-stock-market-analysis/src'
# current environment variables
print("os.environ = ", os.environ)




def measure(df_raw, df_encoded):
    return similarity.measure(df_encoded=df_encoded,
                              df_raw=df_raw,
                              row_id=1,
                              result_file_path='./output/cosine_similarity.csv')


if __name__ == '__main__':
    print("pathh -=== ", sys.path)
    df_raw, df_encoded = get_init_df("./data/financial_data.csv")
    res = measure(df_raw, df_encoded)
    res.sort_values('cosine_similarities')
    print(res)
