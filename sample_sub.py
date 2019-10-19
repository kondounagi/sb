import datetime


def fix_sample_sub(sub_df, store_info_df):
    def trans_date(day):
        daytime =datetime.datetime.strptime(day, '%Y-%m-%d')
        return daytime
    def sample_sub_date(sub_df):
        sub_df["date"] = sub_df["date"].apply(trans_date)
        return sub_df
    def get_week_day(sub_df):
        def sun_to_mon(num):
            num -= 1
            return num%6
        sub_df["weekday"] = sub_df["date"].weekday().apply(sun_to_mon)
        return sub_df
        

    def merge_store_info(sub_df,store_info):
        sub_df = pd.merge(sub_df,store_info, on = "store_merchant_id", how = "left")

        return sub_df
        
    sub_df = sample_sub_date(sub_df)
    sub_df = get_week_day(sub_df)
    sub_df = merge_store_info(sub_df, store_info_df)
    return sub_df


