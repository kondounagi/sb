


def count_series(df, column test_df = None):
    encodeed = df.groupby(column)[column].count() #median or mean
    df[column +"_count"] = df[column].map(encodeed )
    if !(test_df is None):
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


