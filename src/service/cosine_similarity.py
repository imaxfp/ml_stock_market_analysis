from sklearn.metrics.pairwise import cosine_similarity

from src.util.util_log import log


def measure(df_encoded, df_raw, row_id, result_file_path):
    '''

    Parameters
    ----------
    df_encoded: will be created matrix for the cosine similarities calculation
    df_raw: initial dataframe, column 'cosine' will be added
    row_id: specific item in the matrix for measure distance with other items
    result_file_path: the measurement result will ne stored by the following path
    Returns df_raw with additional column 'cosine'
    -------
    Example:
        matrix = [[1, 3],
                  [4, 1]]
    cosine_similarity(matrix[0:1], m2)

    Result:
    [[1.         0.53687549]]
    '''

    log.info('Start cosine similarity calculation')

    # Prepare working matrix
    matrix = df_encoded.values
    # Vector for comparison
    vector_for_comparing = matrix[row_id: row_id + 1]
    # Calculate similarity

    # feature importance
    cosine_similarity_matrix = cosine_similarity(vector_for_comparing, matrix)
    cosine_column = cosine_similarity_matrix.flatten()
    df_raw['cosine_similarities'] = cosine_column
    df_raw = df_raw.sort_values(["cosine_similarities"], ascending=False)
    df_raw.to_csv(result_file_path)
    log.info('End cosine similarity calculation')
    return df_raw
