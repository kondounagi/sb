columns= ["transaction","GMV" ,"active_user","wallet_rate"]

fig = plt.figure(figsize = (10,10))
def get_hists(df,colunns):
    fig = plt.figure(figsize = (10,10))
    for i in range(4):
        
        
        print(f"Skewness: {df.skew()}"  )
        print(f"Kurtosis: {df.kurt()}" )
        plt.subplot(2,2,i+1)
        plt.hist(df.values, bins = 100)
        plt.title(f"{columns[i]}")