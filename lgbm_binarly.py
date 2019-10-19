import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import re
import regex
import functools
import random
import sklearn
import lightgbm as lgb
from lightgbm import LGBMClassifier
import argparse 




LGB_PARAMS = {
    'objective': 'binary',
    'verbosity': -1,
    'boosting_type': 'gbdt',
    'learning_rate': 0.2,
    'num_leaves': 32,
    'min_child_samples': 79,
    'n_jobs': 4,
    'max_depth': 7,
    'subsample_freq': 1,
    'subsample': 0.9,
    'bagging_seed': 11,
    'reg_alpha': 0.1,
    'reg_lambda': 0.3,
    'colsample_bytree': 1.0
}
def get_label(df, y_col = "transaction"):
    X = df.drop(y_col, axis = 1)
    y = df[y_col]

    return X,y
X_train , y_train  = get_label(train_df)
X_val, y_val = get_label(val_df)

model = LGBMClassifier(**LGB_PARAMS, n_estimators=1000)

model.fit(X_train, y_train,
            eval_set=[(X_train, y_train), (X_val, y_val)], eval_metric="logloss",
            verbose=10, early_stopping_rounds=100)

feature_importances = model.feature_importance()
#%%
y_pred =model.predict_proba(test_X)

