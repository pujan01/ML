import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm, model_selection
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)﻿


quandl.ApiConfig.api_key = "o25QNDvSXrTmhzw8fpHv"
df = quandl.get('WIKI/GOOGL')
# print(df.head())

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HC_PTL'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HC_PTL', 'PCT_Change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)
forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)


df.dropna(inplace=True)
print(df.head())
