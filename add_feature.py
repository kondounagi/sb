def get_tanka(df):
    df["tanka"] = df["store_merchant_idGMVmean"]/df["store_store_merchant_idactive_usermean"]
    return df
