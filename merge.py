columns= ["transaction","GMV" ,"active_user","wallet_rate"]

fig = plt.figure(figsize = (10,10))
def get_hists(df,colunns):
    fig = plt.figure(figsize = (10,10))
    for i in range(4):
        print(f"Skewness: {df[colunn[i]].skew()}"  )
        print(f"Kurtosis: {df.kurt()}" )
        plt.subplot(2,2,i+1)
        plt.hist(df.values, bins = 100)
        plt.title(f"{columns[i]}")


def get_day(df):
    df["Year"]= df["data"].str[0:4].astype(int)
    df["Month"]= df["data"].str[5:7].astype(int)
    df["Day"]= df["data"].str[8:].astype(int)
    return df
  
def kyuryobi(df):
    df["Payday"] = 0
    df["Payday"].loc[df["Day"].isin([10, 15, 25])]= 1
    return df

def target_enc(df, cols, target_col):
    for col in cols:
        for agg_type in ['mean','std']:
            new_col_name = col+target_col+agg_type
            temp_df = df[[col, 'TransactionAmt']]
            #temp_df['TransactionAmt'] = temp_df['TransactionAmt'].astype(int)
            temp_df = temp_df.groupby([col])[target_col].agg([agg_type]).reset_index().rename(
                                                    columns={agg_type: new_col_name})

            temp_df.index = list(temp_df[col])
            temp_df = temp_df[new_col_name].to_dict()   

            df[new_col_name] = df[col].map(temp_df)



def label_encode(df):
    for f in df.columns:
        if df[f].dtype.name =='object': 
            lbl = sklearn.preprocessing.LabelEncoder()
            lbl.fit(list(df[f].values.astype(str)))
            df[f] = lbl.transform(list(df[f].values))
        return df