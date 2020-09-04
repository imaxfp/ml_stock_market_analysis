from src.service import cosine_similarity
from src.service.df_preparation import get_init_df

if __name__ == '__main__':
    df_raw, df_encoded = get_init_df("./data/financial_data.csv")
    res = cosine_similarity.measure(df_encoded=df_encoded,
                                    df_raw=df_raw,
                                    row_id=1,
                                    result_file_path='./output/cosine_similarity.csv')
    print(res)
