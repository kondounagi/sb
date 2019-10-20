def get_submission(predict_series,csv_path = "./data/sample_submit.csv")

    sub = pd.read_csv(csv_path)

    sub["transaction"]= predict_series

    sub.to_csv("./submit_team9.csv",index =False)
