


def count_encodding(df, column ,test_df = None):
    """
    columnを入れると　頻度エンコーディングをします。
    test_dfを入れると
    """
    encodeed = df.groupby(column)[column].count() #median or mean
    df[column +"_count"] = df[column].map(encodeed )
    if not(test_df is None):
        test_df[column +"_count"] = df[column].map(encodeed)
        return df, test_df
    return df


def get_group_window_mean(df, group_col ,target_col,  w_size = 2 ):
    new_col_name = target_col + "_group_win_mean"
    df_gb = df[[group_col, target_col]].copy()
    for_shift = df.groupby(group_col)[target_col].shift(1).isna()
    df_gb = df_gb.groupby(group_col)[target_col].rolling(w_size).mean().shift(1).reset_index().sort_values("level_1").reset_index(drop = True)
    df_gb.loc[for_shift, :] = np.nan
    df[new_col_name] = df_gb[target_col]
    
    return df



def target_enc(df, cols, target_col):
    """
    cols ：エンコードしたいカラムの「リスト」
    target_col
    """

    for col in cols:
        for agg_type in ['mean']:
            new_col_name = col+target_col+agg_type
            temp_df = df[[col, target_col]]
            #temp_df['TransactionAmt'] = temp_df['TransactionAmt'].astype(int)
            temp_df = temp_df.groupby([col])[target_col].agg([agg_type]).reset_index().rename(
                                                    columns={agg_type: new_col_name})

            temp_df.index = list(temp_df[col])
            temp_df = temp_df[new_col_name].to_dict()   

            df[new_col_name] = df[col].map(temp_df)
    return df