import datetime
def trans_date(day):
    daytime =datetime.datetime.strptime(day, '%Y-%m-%d')
    return daytime
def fix_sumple_sub(sub_df):
    sub_df["date"] = sub_df["date"].apply(trans_date)
def get_week_day(sub_df):
    def nun_to_mon(num):
        
        return num%6
    

def merge_store_info(sub_df,store_info):
    sub_df = pd.merge(sub_df,store_info, on = "store_merchant_id", how = "left")

    return sub_df


